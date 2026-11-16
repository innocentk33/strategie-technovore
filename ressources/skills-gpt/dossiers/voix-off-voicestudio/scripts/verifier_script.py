#!/usr/bin/env python3
"""Vérifie un script annoté pour VoiceStudio (moteur par défaut OmniVoice).

Usage:
    python verifier_script.py script.txt [--mode voice|longform]
    cat script.txt | python verifier_script.py - --mode voice

Signale :
  - mots en MAJUSCULES (épelés lettre par lettre par VoiceStudio)
  - onomatopées non voulues ([question-*], [surprise-*]…), seuls [laughter]/[sigh] sont gardés
  - balises inconnues (lues à voix haute), dont les balises ElevenLabs/SSML
  - balises longform ([slow], [fast], [emphasis], [spell], [voice:]) en mode voice
  - pauses > 10 s ou mal formées
  - lots > 4096 caractères
Les lignes d'en-tête "LOT …" et la section "Notes" sont ignorées.
"""
import argparse
import re
import sys

USEFUL_NONVERBAL = {"laughter", "sigh"}
NONVERBAL = {
    "laughter", "sigh", "confirmation-en", "question-en", "question-ah",
    "question-oh", "question-ei", "question-yi", "surprise-ah", "surprise-oh",
    "surprise-wa", "surprise-yo", "dissatisfaction-hnn",
}
LONGFORM = {"slow", "/slow", "fast", "/fast", "emphasis", "/emphasis", "spell", "/spell"}
ELEVENLABS_HINT = {
    "excited", "whispers", "whisper", "happy", "sad", "angry", "sarcastic",
    "curious", "laughs", "laughing", "sighs", "breath", "breathes", "shouts",
    "crying", "giggles", "exhales", "inhales",
}
MAX_CHARS = 4096
PAUSE_RE = re.compile(r"^pause(?:\s+(\d+(?:[.,]\d+)?)\s*(ms|s))?$", re.I)
TAG_RE = re.compile(r"\[\[.*?\]\]|\[[^\[\]]*\]|<[^<>]+>")
CAPS_RE = re.compile(r"\b[A-ZÀÂÄÇÉÈÊËÎÏÔÖÙÛÜŸÆŒ]{2,}\b")
HEADER_RE = re.compile(r"^\s*LOT\s+\d+", re.I)
NOTES_RE = re.compile(r"^\s*\**\s*Notes?\s*\**\s*:?\s*$", re.I)


def split_lots(text):
    lots, current, in_notes = [], [], False
    for line in text.splitlines():
        if NOTES_RE.match(line):
            in_notes = True
            continue
        if HEADER_RE.match(line):
            in_notes = False
            if current:
                lots.append(current)
            current = [(None, line)]
            continue
        if not in_notes:
            current.append((True, line))
    if current:
        lots.append(current)
    return lots


def check_tag(tag, mode):
    if tag.startswith("[["):
        return None  # prononciation forcée
    if tag.startswith("<"):
        name = tag.strip("<>/").split()[0].lower()
        if name == "strong":
            return f"{tag} : emphase CosyVoice 3 seulement, lue à voix haute sur le moteur par défaut"
        return f"{tag} : balise SSML/HTML non reconnue, sera lue à voix haute (pause → [pause 1s])"
    inner = tag[1:-1].strip()
    low = inner.lower()
    if low in USEFUL_NONVERBAL:
        return None
    if low in NONVERBAL:
        return f"{tag} : simple onomatopée (ah/oh/wa…), à retirer ; exprimer l'idée par le texte et la ponctuation"
    m = PAUSE_RE.match(inner)
    if m:
        if m.group(1):
            val = float(m.group(1).replace(",", "."))
            secs = val / 1000 if m.group(2).lower() == "ms" else val
            if secs > 10:
                return f"{tag} : pause > 10 s (maximum 10 s)"
        return None
    if low.startswith("pause"):
        return f"{tag} : pause mal formée (formats : [pause], [pause 500ms], [pause 1.5s])"
    if low in LONGFORM or low.startswith("voice:"):
        if mode == "voice":
            return f"{tag} : balise longform, ignorée/lue sur la page Voice (Audiobook/Stories seulement)"
        return None
    if low in ELEVENLABS_HINT:
        return f"{tag} : balise de type ElevenLabs, non reconnue, sera lue à voix haute"
    return f"{tag} : balise inconnue, sera lue à voix haute"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--mode", choices=["voice", "longform"], default="voice")
    args = ap.parse_args()
    text = sys.stdin.read() if args.path == "-" else open(args.path, encoding="utf-8").read()

    issues = 0
    for i, lot in enumerate(split_lots(text), 1):
        header = next((l for k, l in lot if k is None), f"(bloc {i})").strip()
        body_lines = [l for k, l in lot if k]
        body = "\n".join(body_lines).strip()
        if not body:
            continue
        problems = []
        if len(body) > MAX_CHARS:
            problems.append(f"lot de {len(body)} caractères (> {MAX_CHARS}) : le découper")
        for tag in TAG_RE.findall(body):
            msg = check_tag(tag, args.mode)
            if msg:
                problems.append(msg)
        without_tags = TAG_RE.sub(" ", body)
        for word in sorted(set(CAPS_RE.findall(without_tags))):
            problems.append(
                f"« {word} » en majuscules : sera épelé. OK si sigle à épeler, "
                f"sinon l'écrire en minuscules (emphase par position/pause)"
            )
        tags_nv = [t for t in TAG_RE.findall(body) if t[1:-1].lower() in USEFUL_NONVERBAL]
        if len(tags_nv) > 1:
            problems.append(f"{len(tags_nv)} sons non verbaux ([laughter]/[sigh]) dans ce lot : en garder un au plus")
        if problems:
            print(header)
            for p in problems:
                print(f"  - {p}")
            issues += len(problems)

    if issues == 0:
        print(f"Aucun problème détecté (mode {args.mode}).")
    else:
        print(f"\n{issues} point(s) à vérifier (mode {args.mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
