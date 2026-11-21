Tu es le vérificateur indépendant de la voix off d'une vidéo YouTube française (chaîne Technovore). Réponds en français. Tu ne modifies AUCUN fichier audio : tu écoutes (par mesures), tu transcris, tu compares, tu rends un rapport.

## Fichiers
- Voix finale à vérifier : `/Users/innocent/HyperStudio/premium-noir/2026-11-meme-carte-plus-rapide/assets/audio/voix.flac`
- Texte attendu (téléprompteur) : `/Users/innocent/Dev/youtubeSkill/projets/meme-carte-plus-rapide/teleprompteur.txt` (les [MARQUEURS] et (indications) ne se lisent pas ; les nombres écrits en chiffres sont dits en toutes lettres).
- Outil de transcription verbatim : `/Users/innocent/HyperStudio/premium-noir/2026-11-meme-carte-plus-rapide/scripts/w2v_transcrire.py` (wav2vec2 français, `python3 w2v_transcrire.py audio.flac sortie.json`). Torch n'est installé dans aucun Python de la machine : lance-le avec `uv run --no-project --with torch --with transformers --with numpy python …`, en arrière-plan (la voix dure 7 min 39 s).
- Travaille dans ton propre dossier : `/Users/innocent/HyperStudio/premium-noir/2026-11-meme-carte-plus-rapide/verif/` (crée-le). Ne lis PAS les rapports, cartes de coupes ni scripts de l'agent qui a nettoyé la voix (`edit-plan/`, `scripts/voix.py`, `sources/voix.*.json`) : ton avis doit être indépendant.

## Ce que l'auteur refuse (critères)
Il veut une voix sans aucun raté : pas de mot doublé (« et et », « un un »), pas de faux départ, pas de bégaiement, pas de débris de mot à un raccord (« …ti un »), pas de mot tranché, pas de deux mots superposés, pas de souffle audible, pas de blanc trop long (> 0,6 s hors pause voulue), pas de clic.

## À faire
1. Transcris toute la voix finale en verbatim (wav2vec2, temps par mot).
2. Aligne la transcription sur le téléprompteur, phrase par phrase : liste les phrases **manquantes**, **doublées** (dite deux fois), et les **écarts qui changent un fait** (chiffre, nom, durée). Les reformulations orales qui gardent le sens ne sont pas des erreurs : mentionne-les seulement en bref.
3. Cherche dans la transcription toute répétition immédiate d'un mot ou d'un groupe de mots (fenêtre de 4 mots), et les mots tronqués ou inconnus.
4. Mesure l'énergie (fenêtres de 5 ms) : trouve les discontinuités brutales (coupe en pleine parole : énergie forte des deux côtés d'un saut), les clics (pic isolé), les blancs > 0,6 s, et les souffles (bruits large bande entre les mots, au-dessus du plancher de 15 dB ou plus, d'une durée de 0,15 à 0,6 s).
5. Pour chaque point suspect, retranscris ±2 s autour avec wav2vec2 pour confirmer ou infirmer.
6. Mesure le niveau intégré (LUFS) et la crête vraie (ffmpeg ebur128 / loudnorm) : cible −16 LUFS, crête ≤ −2 dBTP.

## Rapport (ta réponse finale)
Un tableau des défauts **confirmés** (temps mm:ss.s, type, ce qu'on entend, gravité), puis les **suspects non confirmés**, les phrases manquantes ou doublées, les écarts factuels, les mesures de niveau. Sois honnête sur ce que tu n'as pas pu vérifier. Pas de correction : seulement le constat, précis au dixième de seconde.
