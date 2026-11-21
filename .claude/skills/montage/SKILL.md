---
name: montage
description: Montage complet d'une vidéo Technovore en HyperFrames, style « premium noir » (projets dans ~/HyperStudio/premium-noir/) : voix reçue (sa vraie voix, une prise brute à nettoyer, ou une voix clonée VoiceStudio/OmniVoice en une ou deux versions), meilleures prises, micro-pauses, montage plan par plan calé sur les mots (scripts/montage.py), captures web surlignées, logos, photos de produits, schémas à l'échelle, mèmes muets, musique et bruitages, critiques indépendantes, rendu 1080p puis 4K, retouches de voix envoyées par l'auteur. À utiliser dès qu'il faut faire, reprendre, corriger ou relancer le montage d'une vidéo, intégrer une voix ou des reprises de voix, refaire un rendu, ou briefer un agent de montage, même si l'auteur dit seulement « fais le montage », « voilà la voix », « remplace ces passages » ou « lance la 4K ».
---

# Montage d'une vidéo Technovore

Le montage se fait hors de ce dépôt, dans `~/HyperStudio/premium-noir/<AAAA-MM-sujet>/` (un projet HyperFrames par vidéo). Ce dépôt garde le script, les sources, le téléprompteur et le kit d'upload (`projets/<nom>/`). Tout le montage est **généré par du Python** : on ne touche jamais `index.html` ni `compositions/` à la main, on modifie `scripts/montage.py` et on le relance.

Projet modèle le plus récent : `~/HyperStudio/premium-noir/2026-11-qwen-27b-32go/` (voix clonée, 21/11/2026). Pour une vraie voix, la méthode de la voix vient de `2026-11-qwen-27b-8go/` (19/11/2026).

## Règles qui ne se discutent pas

1. **Rien d'inventé à l'écran.** Chaque chiffre, prix, nom ou adresse affiché vient de `projets/<nom>/sources.md` ou du relevé de prix daté, et la voix le dit. Une URL dans un mini navigateur est la vraie adresse de la page, jamais une adresse reconstituée. Pourquoi : la chaîne vit de sa crédibilité, et deux critiques ont déjà trouvé des adresses inventées (32 Go, v2 et v3).
2. **Aucun nom de chaîne, pseudo ou nom de personne** à l'écran, dans la voix, la description ou les sous-titres (on floute dans les captures). Pas de chemin de dossier ni de clé. Pourquoi : l'auteur estime qu'il faut une autorisation pour citer quelqu'un (07/11).
3. **Mèmes muets**, en petite carte étiquetée « GIF », qui ne cachent aucun texte. **Jamais de tampon** (encadré rouge penché « VITESSE : NON » : `stamp()` de `blocs3.py` est interdit depuis le 18/11). **Bruitages sobres** : pas de boum, pas d'impact, pas de son d'extinction (power-down).
4. **Voix sans raté** : pas de mot doublé, sauté, tranché, de débris, de souffle, de clic ni de blanc de plus de 0,8 s. On transcrit en **verbatim avec wav2vec2**, jamais Whisper ni Parakeet (Whisper efface les répétitions, Parakeet sautait le premier mot des prises : c'est là que tombaient les « et et »). Accélération ×1,25 au plus (au-delà, les chiffres s'avalent). Hauteur changée seulement par **PSOLA** (Praat via parselmouth, formants gardés), **jamais `asetrate`** (ça change le timbre et la durée).
5. **Prix** : le meilleur prix du jour du relevé, tous marchands confondus (Amazon d'abord), daté à l'écran et dans la description. Jamais « même marchand, même jour ».
6. **1080p d'abord, 4K seulement sur son « ok »**, sauf s'il a donné carte blanche pour **cette** vidéo (il l'a fait pour « Qwen 27B sur 8 Go » et « 32 Go pour Qwen 27B », pas pour les suivantes). Pourquoi : le 18/11, une 4K lancée sans sa relecture lui a été reprochée.
7. **Au plus 2 revues indépendantes de la voix et 3 critiques du montage**, puis on livre en disant ce qui reste douteux.
8. Pas de commit sans demande. Ne modifie pas `claude-youtube/`. Écris en français et tutoie l'auteur.

## Déroulé

1. **Démarrer le projet** à partir du plus récent (copie, puis ce qui change) : `references/demarrage.md`. Lis aussi ce qui prime quand les vieux documents (`style/RECETTE.md`, `style/AGENT.md`) contredisent la pratique.
2. **La voix**, par un sous-agent Opus (brief : `references/briefs/modele-voix-reelle.md` ou `modele-voix-clonee.md`) :
   - vraie voix (prise brute avec plusieurs essais par phrase) : `references/voix-reelle.md` ;
   - voix clonée VoiceStudio (une ou deux versions du même texte) : `references/voix-clonee.md`.
   Sorties attendues : `assets/audio/voix.flac` (−16 LUFS, −2,5 dBTP, 48 kHz) et `sources/voix.words.json` (chaque mot avec ses temps). **Tout le montage s'ancre sur ce fichier de mots.**
3. **Revue de la voix** par un autre sous-agent Opus qui n'a pas monté la voix (`modele-verif-voix.md`), corrections, seconde revue si besoin, et c'est fini : `references/verifications.md`.
4. **Images** en parallèle de la voix, par un sous-agent Sonnet (`modele-captures.md`) : captures web surlignées, photos de produits, logos, manifeste `edit-plan/captures.md`. Règles : `references/visuels.md`.
5. **Écrire `scripts/montage.py`** : un plan par phrase forte du script, ancré sur la voix avec `T("…")`, avec les briques de `kit.py` / `blocs*.py` et les aides du haut de `montage.py`. API et conventions : `references/moteur.md`. Mèmes, musique, bruitages : `references/visuels.md` et `references/son.md`.
6. **Boucle courte** à chaque modification : `MC_DRY=1` (ancres), génération, `check`, planches d'images aux moments touchés, et tu regardes les images avant de dire que c'est bon : `references/verifications.md`.
7. **Rendu 1080p, puis critique indépendante** (sous-agent Opus, `modele-critique.md`), corrections, nouveau rendu. Trois tours au plus.
8. **Livraison** : chemin du dernier 1080p et ce qui a changé, puis 4K sur accord. Ensuite, kit d'upload et sous-titres (sous-agent Sonnet, `modele-upload.md`, skill `upload`), et mise à jour du README et du calendrier : `references/livraison.md`.
9. **Retouches envoyées par l'auteur** (reprises de voix, prononciations) : `references/retouches.md`.
10. **À chaque sortie de vidéo** (l'auteur dit qu'elle est sortie, ou une vidéo publique n'est pas « Publié » dans le README) : lance le skill **`radar`** avant tout le reste (règle du `CLAUDE.md` du dépôt).

Pour écrire le montage avant d'avoir la voix (voix et mots fictifs, `MC_VOICE`, `STRATA_WORDS`) : `references/demarrage.md`, « Tester un projet neuf avant d'avoir la voix ».

Avant chaque étape, vérifie qu'aucun sous-agent de l'étape précédente ne tourne encore et relis ce qu'il a écrit : `references/sous-agents.md`.

## Quand charger quoi

| Situation | Référence |
|---|---|
| Nouvelle vidéo, structure du dossier, scripts à copier ou à réécrire, ce qui prime | `references/demarrage.md` |
| Prise brute de sa vraie voix | `references/voix-reelle.md` |
| Voix clonée (une ou deux versions) | `references/voix-clonee.md` |
| Reprises de voix de l'auteur, banque de prononciations | `references/retouches.md` |
| Écrire ou corriger `montage.py`, une brique, un plan | `references/moteur.md` |
| Captures, logos, produits, schémas, carte, mèmes | `references/visuels.md` |
| Musique, coupures, bruitages, niveaux | `references/son.md` |
| check, planches, revues, critiques, mesures, 1080p et 4K | `references/verifications.md` |
| 4K, chapitres, upload, sous-titres, README, calendrier | `references/livraison.md` |
| Un symptôme déjà vu (mème qui cache un titre, ancre qui tombe à côté…) | `references/pieges.md` |
| Lancer un sous-agent, choisir son modèle, son brief | `references/sous-agents.md` et `references/briefs/` |
