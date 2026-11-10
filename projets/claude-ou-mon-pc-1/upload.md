# 16 Go de VRAM : kit d'upload YouTube

> Vidéo : `2026-11-16-go-de-vram-suffisent-1080p60-20261109-1149.mp4` (11:39, 1920×1080, 60 i/s). Chapitres calés sur la vidéo finale, retranscrite le 09/11 (Whisper, en local), pas sur le script.
> Déjà sur YouTube, en privé : [`jMZFDNbwRNI`](https://studio.youtube.com/video/jMZFDNbwRNI/edit), titre *16 Go de VRAM : Est-ce vraiment suffisant pour les LLM ?* (relevé par vidIQ le 09/11). **⚠️ Ses tags actuels sont tes anciens tags Flutter** (« apprendre flutter », « unity »…) : remplace-les par ceux d'en dessous.
> Publication : **lun. 9 nov. 2026, 18 h** (voir [`calendrier.md`](../../calendrier.md)). La vidéo annonce Strata « la semaine prochaine » : c'est bien le 16 nov.

## Titre

Garde celui que tu as mis : *16 Go de VRAM : Est-ce vraiment suffisant pour les LLM ?* (55 caractères, lisible en entier sur mobile). Il porte « 16 Go de VRAM » et « LLM », les mots qu'on cherche.

## Description

```
Sur la même carte de 16 Go, le même modèle tourne à 101 tokens par seconde chez l'un, et à 13 chez l'autre. La différence, c'est le fichier : un qui rentre dans la carte, un qui déborde en RAM. On fait les comptes de ta carte graphique (le fichier, la mémoire de la conversation, l'agent de code), on calcule la vitesse, on voit ce que vaut Qwen 27B face à Claude, et je t'explique pourquoi mon Qwen était si lent.

Pas de banc d'essai ici : des mesures publiées et des calculs, sources en bas.

CHAPITRES
0:00 101 ou 13 tokens/s sur la même carte
0:31 Ta carte, un budget en 3 lignes
0:51 Ligne 1 : le fichier (16 Go, ce n'est pas 16 Go)
1:43 Ligne 2 : la mémoire de la conversation
2:24 Ligne 3 : l'agent de code
3:05 Ça va vite comment ?
4:05 Pourquoi 13 tokens/s : le fichier déborde
5:00 AMD, cartes de 8 Go et de 12 Go
5:48 Un modèle de 125 milliards sur un PC de joueur (Strata)
7:44 La RAM coûte 6 fois plus cher
8:08 Qwen 27B contre Claude
9:01 Pourquoi mon Qwen était si lent
10:33 Vérifier si ta carte déborde
10:51 Verdict

Installer ton IA en local pas à pas (LM Studio) : https://www.youtube.com/watch?v=9hr_zaJuUbM

SOURCES (vérifiées du 05 au 08/11/2026)
Qwen3.8-27B (fiche et config) : https://huggingface.co/Qwen/Qwen3.8-27B
Tailles des fichiers GGUF : https://huggingface.co/api/models/unsloth/Qwen3.8-27B-GGUF/tree/main
101 tokens/s avec MTP sur RTX 5080 : https://github.com/sudoingX/qwen38-mtp
25 tokens/s sur RTX 5060 Ti : https://www.paulsprogrammingnotes.com/2026/08/running-qwen-3-8-27b-16gb.html
50 000 tokens avant le premier message : https://www.xda-developers.com/claude-code-using-fifty-thousand-tokens-before-typed-prompt-fixed-it/
Strata : https://github.com/Niko1221/Strata
Qwen 27B contre Claude Opus 5 : https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-claude-opus-5-high
La réflexion de Qwen (22 000 tokens) : https://simonwillison.net/2026/Aug/16/qwen-38-27b/
Le débordement en RAM (NVIDIA) : https://nvidia.custhelp.com/app/answers/detail/a_id/5490
Cartes graphiques sur Steam : https://store.steampowered.com/hwsurvey/

Dis-moi en commentaire ta carte graphique et ta RAM : je te dis ce qui tient chez toi.

#IAenlocal #LLM #VRAM
```

## Tags

```
16 go vram, vram llm, ia en local, llm local, ia locale, qwen 27b, qwen3.8, rtx 5080, rtx 5060 ti, carte graphique ia, combien de vram pour llm, quantisation, gguf, lm studio, llama.cpp, strata, claude code, local llm, technovore
```

Les tags pèsent peu ; ils corrigent surtout les fautes (« qwen3.8 », « llama.cpp »). « ia en local » reste le mot-clé du pilier (18 376 recherches par mois, vidIQ, 24/10 : [`installer-ia-locale/sources.md`](../installer-ia-locale/sources.md)). Les outils de mots-clés de vidIQ (`vidiq_keyword_research`, `vidiq_outliers`) n'étaient pas branchés dans cette session du 09/11 : les volumes ne sont pas refaits.

## Commentaire épinglé

```
Ta carte graphique et ta RAM ? Donne-les-moi, je te dis quel modèle tient chez toi.
```

## Sous-titres

- Français : [`16-go-de-vram.fr.srt`](16-go-de-vram.fr.srt) (135 sous-titres, 0:00-11:38).
- Anglais : [`16-go-de-vram.en.srt`](16-go-de-vram.en.srt), même découpage et mêmes temps.

Ils sont faits à partir de la vidéo finale, transcrite avec Whisper le 09/11 (horodatage par mot), puis le texte a été corrigé à la main avec le téléprompteur : Qwen, Claude Code, Q4_K_M, les chiffres. Les phrases que tu as improvisées sont gardées (« Oh my god ! », « Coup dur pour Guillaume »). Dans Studio : Sous-titres → Ajouter une langue → Importer un fichier → « Avec horodatage ». Mets d'abord le français comme langue de la vidéo.

## Réglages dans YouTube Studio

| Champ | Valeur |
|---|---|
| Tags | Ceux d'en haut, **à la place des tags Flutter** |
| Miniature | Charte verte, gabarit « ABONNEMENT OU IA LOCALE » (voir [`fiche.md`](fiche.md)), en PNG sous 2 Mo |
| Fiche (carte) | Vers [*Comment utiliser une IA sans internet sur ton PC*](https://www.youtube.com/watch?v=9hr_zaJuUbM) à **11:21**, quand tu dis « je te la mets en fiche » |
| Écran de fin | La vidéo d'installation (en attendant celle de Strata, le 16 nov.) + abonnement |
| Playlist | Celle du pilier IA chez moi |
| Public | Non, pas conçue pour les enfants |
| Contenu modifié ou synthétique | Non |
| Chapitres automatiques | Décocher (les tiens sont dans la description) |
| Programmation | lun. 9 nov., 18 h |

## Suggestions

- **Vidéos hôtes du mois** : à refaire quand `vidiq_outliers` (`language: fr`) répond de nouveau. En attendant, la vidéo anglaise *Is 16GB All You Need for Serious Local LLM?* (359 K vues en 10 jours, voir [`fiche.md`](fiche.md)) partage nos mots « 16GB » et « LLM ».
- **Enchaînement** : fiche à 11:21 vers l'installation ; le 16 nov., ajoute la vidéo Strata dans l'écran de fin de celle-ci.
