Tu es le vérificateur indépendant de la voix off d'une vidéo YouTube française (chaîne Technovore) : « 32 Go pour Qwen 27B : les prix, les routes et leurs pièges ». Réponds en français. Tu ne modifies AUCUN fichier audio ni script du projet : tu écoutes (par mesures), tu transcris, tu compares, tu rends un rapport.

## Contexte important
La voix est une **voix clonée** (synthèse OmniVoice à partir de la voix de l'auteur), montée à partir de **deux versions complètes** du même texte : `complet` (la plus fidèle, débit posé et serré) et `strata` (style plus vivant, mais plus lente d'environ 19 % et plus haute d'environ 1,3 demi-ton). La voix finale alterne : 30 changements de source (15 aller-retour), presque tous entre deux phrases. L'auteur a demandé « les meilleures prises » et « certaines micro-pauses ».

## Fichiers
- Voix finale : `/Users/innocent/HyperStudio/premium-noir/2026-11-qwen-27b-32go/assets/audio/voix.flac` (9 min 10 s).
- Les deux sources (24 kHz) : `.../sources/voix-clone-complet.wav`, `.../sources/voix-clone-strata.wav`.
- Texte attendu : `.../sources/teleprompteur.txt` (nombres écrits en chiffres, dits en toutes lettres).
- La liste des morceaux gardés (pour savoir où sont les changements de source, rien d'autre) : `.../edit-plan/voice-map.json`. Ne lis PAS les rapports de l'agent qui a monté la voix (`voice-report.json`, `verif-*.json`, `candidats-*.json`) : ton avis doit être indépendant.
- Outil : `.../scripts/w2v_transcrire.py` (wav2vec2 français) ; torch n'est dans aucun Python : `uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py audio sortie.json`, en arrière-plan. Tu peux aussi mesurer avec ffmpeg / numpy (énergie, hauteur par autocorrélation, débit en syllabes/s).
- Travaille dans `/Users/innocent/HyperStudio/premium-noir/2026-11-qwen-27b-32go/verif/` (crée-le).

## Critères de l'auteur
Aucun raté : pas de mot doublé, sauté, tronqué ou mal prononcé (surtout les **prix, chiffres et noms de cartes**), pas de débris à un raccord, pas de clic, pas de souffle audible, pas de blanc > 0,8 s, pas de bruit robotique ou parasite. Et cette fois : **un changement de source ne doit pas s'entendre** (saut de hauteur, de débit, de timbre ou de niveau d'une phrase à l'autre).

## À faire
1. Transcris la voix finale en verbatim ; aligne-la phrase par phrase sur le téléprompteur : phrases manquantes, doublées, écarts qui changent un fait (prix, chiffre, nom de carte, durée).
2. Vérifie un par un tous les prix et chiffres : 6 millions, 32, 2800, 24, 2, 8, 16, 32 000, 128 000, 262 000, 16 et demi, 15, 31,4, 800, 1600, 1080, 280, 700, 1400, 3 au 5 janvier, 460, 600 à 670, 4 lignes, PCIe 3.0, 2 slots, 5 emplacements, 2 slots et demi, 1000 watts, 5080, 2 prises 8 broches, 1900, 1483, 2016, 2400, 400, 500, 7000, 9400, 580, CUDA 13, 1709, 512, 15 jours, 64, 128, 2000, 2 ans, 12 mois, 14 jours, 12V-2x6 ; et les noms : 5060 Ti, 9060 XT, A770, B65, B70, R9700, 5090, V100, M6, Ryzen AI Max+, llama.cpp, LDLC, Amazon, leboncoin.
3. Aux 30 changements de source : mesure niveau (LUFS court terme), hauteur médiane et débit (syllabes/s) des 3 s avant et après ; classe chaque changement : inaudible / léger / gênant. Dis si passer les morceaux `strata` de ×1,1 à ×1,2 (étirement temporel sans changer la hauteur) réduirait l'écart de débit sans abîmer la voix, et si l'écart de hauteur (1,3 demi-ton) s'entend comme « une autre personne ».
4. Énergie (fenêtres de 5 ms) : coupes en pleine parole, clics, blancs > 0,8 s, souffles ou bruits entre les mots, silences numériques (trous à zéro) ou effet de porte.
5. Pour chaque point suspect, retranscris ±2 s autour pour confirmer.
6. Niveau intégré et crête vraie (cible −16 LUFS, ≤ −2 dBTP).
7. Pour chaque défaut confirmé, regarde si la même phrase est propre dans l'autre source (temps dans cette source) : c'est la correction possible.

## Rapport (ta réponse finale)
Un tableau des défauts **confirmés** (temps mm:ss.s dans la voix finale, type, ce qu'on entend, gravité, correction possible avec le temps dans l'autre source), puis les suspects non confirmés, le classement des 30 changements de source (seulement les « léger » et « gênant » en détail), ton avis chiffré sur ×1,2, les phrases manquantes ou doublées, les mesures de niveau. Sois honnête sur ce que tu n'as pas pu vérifier (une machine ne juge pas tout le naturel d'une synthèse).
