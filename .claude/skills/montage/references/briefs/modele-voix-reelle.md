<!-- Modèle (origine de chaque variable : ../sous-agents.md, « D’où viennent les variables »). Remplace : {{TITRE}} (titre de la vidéo), {{PROJET}} (chemin absolu du projet premium-noir), {{PRECEDENT}} (projet précédent à vraie voix, ex. <PREMIUM>/2026-11-qwen-27b-8go), {{DUREE_PRISE}}, {{DUREE_VISEE}}, {{PRONONCIATIONS}} (sigles et leur prononciation), {{SCRATCH}} (dossier de travail). Exemple réel : exemples/brief-voix-8go.md. Modèle : Opus. -->
Tu nettoies la voix off brute d'une vidéo YouTube française de la chaîne Technovore : « {{TITRE}} ». Réponds en français. Ne commite rien. N'écris que dans le projet et dans `{{SCRATCH}}`.

## Projet
- Dossier : `{{PROJET}}/` (lance tout depuis cette racine).
- Prise brute : `sources/prise-originale.flac` ({{DUREE_PRISE}} ; l'auteur a fait plusieurs prises de beaucoup de phrases et improvise un peu).
- Texte attendu : `sources/teleprompteur.txt` (lignes à lire seulement ; les nombres en chiffres sont dits en toutes lettres ; {{PRONONCIATIONS}}). La voix finale devrait faire environ {{DUREE_VISEE}}.
- **La méthode existe** (même auteur, même micro). Les scripts sont dans `scripts/` : `voix.py` (lis son en-tête en entier : morceaux gardés depuis `edit-plan/voice-keep.json`, bords calés sur l'énergie, souffles atténués, pauses resserrées, passages lents ×1,1, fondus, mastering −16 LUFS / −2,5 dBTP, 48 kHz, greffe avec `merge_prev` / `force_tempo`), `teleprompteur.py`, `w2v_transcrire.py` (wav2vec2 verbatim ; torch n'est dans aucun Python : `uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py …`, en arrière-plan), `w2v_candidats.py`, `verif_raccords.py`, `verif_begaiements.py`, `verif_voix.py`, `verif_texte.py`, `verif_souffles.py`, `mots.py`, `vue.py`, `retouche_voix.py`. Format et niveau de détail attendus : `{{PRECEDENT}}/edit-plan/voice-keep.json`, `voice-report.json`, `sources/voix.words.json`. Adapte chemins, `PARTIES` et texte de la bobine ; garde les réglages, sauf si la mesure de cette prise impose autre chose (**remesure le plancher de bruit et les seuils**).

## Ce que l'auteur exige
Une voix sans aucun raté : pour chaque phrase du téléprompteur, la **meilleure prise complète** (souvent la dernière) ; pas de mot doublé, de faux départ, de bégaiement, de débris à un raccord, de mot tranché, de deux mots superposés, de souffle audible, de blanc de plus de 0,8 s, de clic. Verbatim avec wav2vec2 (pas Whisper ni Parakeet). Une reformulation qui garde le sens passe ; **un chiffre changé est corrigé** par une greffe prise ailleurs dans la prise si c'est propre, sinon signalé. L'auteur ne refera aucune prise.

## Sorties
- `assets/audio/voix.flac`, `sources/voix-avant-master.flac`
- `sources/voix.words.json` (mots de la voix finale avec leurs temps ; nombres en chiffres ; « 14 000 » en un mot avec espace insécable) et `sources/voix.phrases.json`
- `edit-plan/voice-keep.json`, `voice-cuts.json`, `voice-map.json`, `voice-report.json`
- `renders/controle-raccords.m4a` (+ .txt) : la bobine des raccords.
- Relance wav2vec2 sur la voix finale et vérifie-toi (`verif_texte.py`, `verif_voix.py`, `verif_raccords.py`, `verif_begaiements.py`, `verif_souffles.py`).

## Ta réponse finale (courte)
Durée, LUFS et crête, nombre de raccords, phrases absentes ou sans prise propre (temps dans la prise), phrases improvisées gardées, écarts qui changent un chiffre (et ce que tu as fait), points dont tu doutes (temps dans la voix finale).
