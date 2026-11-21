Tu nettoies la voix off brute d'une vidéo YouTube française de la chaîne Technovore : « Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? ». Réponds en français. Ne commite rien.

## Projet
- Dossier : `<PREMIUM>/2026-11-qwen-27b-8go/` (lance tout depuis cette racine).
- Prise brute : `sources/prise-originale.flac` (16 min 09 s : l'auteur a fait plusieurs prises de beaucoup de phrases).
- Texte attendu : `sources/teleprompteur.txt` (lignes à lire seulement ; les nombres en chiffres sont dits en toutes lettres ; « UD-IQ2_XS » se dit à peu près « U D I Q 2 X S »). La voix finale devrait faire environ 8 min 30.
- **La méthode existe et vient de servir deux fois** (même auteur, même micro). Les scripts de la vidéo précédente sont copiés dans `scripts/` : `voix.py` (lis son en-tête en entier : morceaux gardés depuis `edit-plan/voice-keep.json`, bords calés sur l'énergie, souffles atténués, pauses resserrées à 0,49 s au plus, passages lents accélérés ×1,1, fondus, mastering −16 LUFS / −2,5 dBTP, 48 kHz, greffe de mot avec `merge_prev` / `force_tempo`, détecteur de souffles), `teleprompteur.py`, `w2v_transcrire.py` (transcription verbatim wav2vec2 français ; torch n'est dans aucun Python : `uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py …`, en arrière-plan), `verif_raccords.py`, `verif_begaiements.py`, `verif_voix.py`, `mots.py`. Le projet précédent, pour le format et le niveau de détail attendus : `<PREMIUM>/2026-11-meme-carte-plus-rapide/edit-plan/voice-keep.json`, `voice-report.json`, `sources/voix.words.json`. Adapte les scripts (chemins, texte) ; garde les réglages finaux, sauf si la mesure de cette prise impose autre chose (plancher de bruit et seuils en dB à remesurer).

## Ce que l'auteur exige
Une voix sans aucun raté : pour chaque phrase du téléprompteur, garde la **meilleure prise complète** (souvent la dernière) ; pas de mot doublé, de faux départ, de bégaiement, de débris de mot à un raccord, de mot tranché, de deux mots superposés, de souffle audible, de blanc trop long, de clic. Transcris en verbatim avec wav2vec2 (pas Whisper ni Parakeet). Une reformulation orale qui garde le sens est acceptable ; **un chiffre changé doit être signalé** (et corrigé par une greffe prise ailleurs dans la prise brute si c'est possible proprement, comme on l'a fait pour « 4060 Ti » dans la vidéo précédente). L'auteur ne refera aucune prise.

## Sorties
- `assets/audio/voix.flac` (voix finale masterisée), `sources/voix-avant-master.flac`
- `sources/voix.words.json` (mots de la voix finale avec leurs temps dans la voix finale ; nombres écrits en chiffres, même format que le projet précédent, « 14 000 » en un seul mot avec espace insécable comme avant) et `sources/voix.phrases.json`
- `edit-plan/voice-keep.json`, `edit-plan/voice-cuts.json`, `edit-plan/voice-map.json`, `edit-plan/voice-report.json`
- `renders/controle-raccords.m4a` (+ .txt) : la bobine des raccords pour écoute.
- Relance la transcription wav2vec2 sur la voix finale et compare-la au téléprompteur pour te vérifier toi-même (répétitions dans une fenêtre de 4 mots, mots tronqués, blancs > 0,6 s, niveau).

## Ta réponse finale (courte)
Durée de la voix finale, LUFS et crête, nombre de raccords, les phrases du téléprompteur **absentes** ou sans prise propre (avec le temps dans la prise brute), les phrases improvisées gardées, les écarts qui changent un chiffre (et ce que tu as fait), et les points dont tu doutes (temps dans la voix finale).
