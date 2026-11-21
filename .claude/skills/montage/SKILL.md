---
name: montage
description: Montage complet d'une vidéo Technovore en HyperFrames, style « premium noir » (un projet par vidéo dans le dossier premium-noir, hors dépôt) : voix reçue (sa vraie voix, une prise brute à nettoyer, ou une voix clonée VoiceStudio/OmniVoice en une ou deux versions), meilleures prises, micro-pauses, montage plan par plan calé sur les mots (scripts/montage.py), captures web surlignées, logos, photos de produits, schémas à l'échelle, mèmes muets, musique et bruitages, critiques indépendantes, rendu 1080p puis 4K, retouches de voix envoyées par l'auteur. À utiliser dès qu'il faut faire, reprendre, corriger ou relancer le montage d'une vidéo, intégrer une voix ou des reprises de voix, refaire un rendu, ou briefer un agent de montage, même si l'auteur dit seulement « fais le montage », « voilà la voix », « remplace ces passages » ou « lance la 4K ».
---

# Montage d'une vidéo Technovore

## Sur une autre machine

Ce skill s'écrit avec deux racines, plus un dossier temporaire. Définis-les avant de commencer et remplace-les partout (dans les commandes shell, ce sont les variables `$PREMIUM` et `$DEPOT`) :

| Racine | Sens | Valeur par défaut (machine de l'auteur, macOS) |
|---|---|---|
| `<DEPOT>` | la racine de ce dépôt (`AGENTS.md`, `projets/`, `calendrier.md`) | `~/Dev/youtubeSkill` |
| `<PREMIUM>` | le dossier `premium-noir` : les projets de montage (un par vidéo) et `style/` | `~/HyperStudio/premium-noir` |
| `<TMP>` | un dossier de travail temporaire (briefs de sous-agents, fichiers jetables) | à ton choix, par exemple le dossier temporaire de ta session |

```bash
export DEPOT="$HOME/Dev/youtubeSkill"             # adapte : là où tu as cloné le dépôt
export PREMIUM="$HOME/HyperStudio/premium-noir"   # adapte : là où tu as copié premium-noir
```

**Prérequis** :
- **Le dossier `premium-noir`, qui n'est PAS dans ce dépôt** (ni dans git). Il faut le copier ou le synchroniser à part (disque externe, cloud, `rsync`) : son `style/` (`RECETTE.md`, `tokens.css`, `components/`, `fonts/`, `media.json`, `voice-presets/`) et le **dernier projet fini** (`2026-11-qwen-27b-32go/`, avec ses `scripts/`, `assets/` : polices, musiques, logos, mèmes), qui sert de modèle à copier (`references/demarrage.md`). Sans lui, ce skill décrit une méthode mais on ne peut ni rendre ni reprendre une vidéo existante. Les anciens projets ne sont utiles que pour reprendre ces vidéos-là. Compte environ 310 Mo par projet, hors rendus.
- **Node.js** et `npx --yes hyperframes@0.9.47` (la version épinglée, la même pour tous les rendus ; ne la change pas au milieu d'un projet).
- **ffmpeg** et ffprobe.
- **Python 3** et **`uv`** : les scripts se lancent par `uv run --no-project --with torch --with transformers --with numpy python scripts/…` (les paquets se téléchargent seuls ; le modèle wav2vec2 français vient de Hugging Face au premier lancement). PSOLA : `--with praat-parselmouth`.
- **Google Chrome** pour les captures web (`scripts/captures-web.mjs`, Chrome sans interface). Si le chemin de Chrome est écrit pour macOS dans ce script, adapte-le.
- Les commandes sont écrites pour **bash** et ont été testées sur macOS : sous Windows, utilise **WSL** ou Git Bash ; `sed -i ''` (BSD) devient `sed -i` (GNU).
- Pas de sous-agents chez toi (Codex, Gemini CLI…) : fais les étapes toi-même, une par une (`references/sous-agents.md`, encadré en tête). Pas de vidIQ : le kit d'upload se fait alors à partir des relevés datés existants, et tu le dis.

`premium-noir/` n'est pas un dépôt git : sauvegarde avant d'écraser.

Le montage se fait hors de ce dépôt, dans `<PREMIUM>/<AAAA-MM-sujet>/` (un projet HyperFrames par vidéo). Ce dépôt garde le script, les sources, le téléprompteur et le kit d'upload (`projets/<nom>/`). Tout le montage est **généré par du Python** : on ne touche jamais `index.html` ni `compositions/` à la main, on modifie `scripts/montage.py` et on le relance.

Projet modèle le plus récent : `<PREMIUM>/2026-11-qwen-27b-32go/` (voix clonée, 21/11/2026). Pour une vraie voix, la méthode de la voix vient de `2026-11-qwen-27b-8go/` (19/11/2026).

## Règles qui ne se discutent pas

1. **Rien d'inventé à l'écran.** Chaque chiffre, prix, nom ou adresse affiché vient de `projets/<nom>/sources.md` ou du relevé de prix daté, et la voix le dit. Une URL dans un mini navigateur est la vraie adresse de la page, jamais une adresse reconstituée. Pourquoi : la chaîne vit de sa crédibilité, et deux critiques ont déjà trouvé des adresses inventées (32 Go, v2 et v3).
2. **Aucun nom de chaîne, pseudo ou nom de personne** à l'écran, dans la voix, la description ou les sous-titres (on floute dans les captures). Pas de chemin de dossier ni de clé. Pourquoi : l'auteur estime qu'il faut une autorisation pour citer quelqu'un (07/11).
3. **Mèmes muets**, en petite carte étiquetée « GIF », qui ne cachent aucun texte. **Jamais de tampon** (encadré rouge penché « VITESSE : NON » : `stamp()` de `blocs3.py` est interdit depuis le 18/11). **Bruitages sobres** : pas de boum, pas d'impact, pas de son d'extinction (power-down).
4. **Voix sans raté** : pas de mot doublé, sauté, tranché, de débris, de souffle, de clic ni de blanc de plus de 0,8 s. On transcrit en **verbatim avec wav2vec2**, jamais Whisper ni Parakeet (Whisper efface les répétitions, Parakeet sautait le premier mot des prises : c'est là que tombaient les « et et »). Accélération ×1,25 au plus (au-delà, les chiffres s'avalent). Hauteur changée seulement par **PSOLA** (Praat via parselmouth, formants gardés), **jamais `asetrate`** (ça change le timbre et la durée).
5. **Prix** : le meilleur prix du jour du relevé, tous marchands confondus (Amazon d'abord), daté à l'écran et dans la description. Jamais « même marchand, même jour ».
6. **1080p d'abord, 4K seulement sur son « ok »**, sauf s'il a donné carte blanche pour **cette** vidéo (il l'a fait pour « Qwen 27B sur 8 Go » et « 32 Go pour Qwen 27B », pas pour les suivantes). Pourquoi : le 18/11, une 4K lancée sans sa relecture lui a été reprochée.
7. **Au plus 2 revues indépendantes de la voix et 3 critiques du montage**, puis on livre en disant ce qui reste douteux.
8. Pas de commit sans demande. Ne modifie pas `claude-youtube/`. Écris en français et tutoie l'auteur.

## Style de montage de l'auteur (recopié de la mémoire de Claude, pour tout agent)

Le 12/11/2026, l'auteur a jugé « atroce » un premier montage fait de gabarits centrés et statiques, de gros titres et de captures minuscules. Il veut le dynamisme de **sa** vidéo de référence (« Comment utiliser une IA sans internet sur ton PC », https://youtu.be/9hr_zaJuUbM). Sa grammaire :
- fond noir, halo de sol ; texte qui s'écrit mot à mot sur la voix (gris puis blanc, mot clé en couleur, mot barré en rouge) ; petits surtitres en capitales espacées ;
- captures réelles en cartes en perspective, avec recadrage surligné ; icônes à trait, pastilles (« Gratuit ») ;
- mèmes muets en petites cartes étiquetées « GIF », choisis pour parler au public francophone jeune (un mème qui colle au propos, ou une simple ligne de texte avec le mot clé en couleur) ;
- un plan évolue sur les mots au lieu de rester sur sa première image ; plus de mouvements de caméra ;
- passages lents accélérés à ×1,1 ; blancs retirés pour une parole fluide ; une voix hachée ou bégayante le gêne plus que tout.

Comment s'en servir :
- Pour trouver les ratés (mots doublés comme « et et », « un un »), **ne te fie ni à Whisper ni à Parakeet** : transcription verbatim wav2vec2 (`jonatasgrosman/wav2vec2-large-xlsr-53-french`, `scripts/w2v_transcrire.py`), découpée seulement dans des silences ; cherche les doublons ; vérifie l'énergie à chaque raccord (les raccords hérités tranchaient souvent un mot) et retranscris ±2 s autour. Donne à l'auteur une bobine des raccords (`renders/controle-raccords-v3.m4a`).
- Pour une référence d'actualité (un jeu, un prix), vérifie le fait du jour avant de l'utiliser.
- Voix clonée (VoiceStudio) : l'auteur peut en fournir deux versions du même texte ; on monte la meilleure prise **phrase par phrase** (de préférence en changeant de source entre deux phrases), on aligne hauteur (PSOLA), débit (×1,25 au plus) et niveau, on unifie le fond des pauses, au plus 2 revues de voix. Sa vraie voix est plus grave que le clone (107 Hz contre 119 Hz) : la remonter pour la coller au clone reste une décision à lui faire valider. Détails : `references/voix-clonee.md`.
- Reprises de sa vraie voix : insérées en ×1,1 (c'est sa règle : « dans la reprise, le son doit être en 1.1 »), comptées depuis le fichier brut ; seules les reprises (et le hook, pour le raccourcir) passent en ×1,1, pas le reste d'une voix clonée. Banque réutilisable : `<DEPOT>/ressources/voix/reprises/`, guide `<DEPOT>/ressources/voix/prononciations.md` ; méthode : `references/retouches.md`.
- Écriture pour une voix de synthèse (VoiceStudio) : suis `<DEPOT>/.claude/rules/voix-synthese.md` (aucune pause balisée, nombres en lettres, liaisons écrites comme elles se disent, numéros de carte en milliers, conventions Ti / XT / R9700 / ASUS).
- Annonces d'occasion : dis « sur leboncoin » ou « en occasion » ; **jamais la ville ni le pseudo du vendeur**, ni à la voix ni dans les `[VISUEL]` (floute pseudo, ville et photo dans les captures). Ne bâtis pas un hook sur un petit marchand nommé. Les villes restent dans `recherche/` et `sources.md`.
- Prix : comparateur gpuprix.com non fiable sur les variantes 8/16 Go (constat du 20/11) ; ne le cite pas. Pour un prix, ouvre les pages produit Amazon (vendeur, stock, livraison : les vendeurs tiers et les livraisons tardives sont des pièges à dire), puis LDLC et les autres ; les relevés que l'auteur envoie (leboncoin, bons plans) se notent « relevé de l'auteur ».
- 4K : avant tout rendu 4K, l'auteur a relu le dernier 1080p. Exception : carte blanche donnée pour **une** vidéo précise (8 Go le 18/11, 32 Go le 21/11).

En plus, pour Claude sur la machine de l'auteur : la mémoire `~/.claude/projects/-Users-innocent-Dev-youtubeSkill/memory/` (`technovore-montage-style`, `montage-rendu-4k-confirmation`, `technovore-voix-clonee`, `technovore-reprises-voix`, `technovore-ecriture-tts`, `technovore-vendeurs-anonymes`, `technovore-prix-meilleur-marchand`) dit la même chose, en plus complet. Elle ne suit pas le dépôt : rien de ce qui compte ne doit n'être que là.

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
10. **À chaque sortie de vidéo** (l'auteur dit qu'elle est sortie, ou une vidéo publique n'est pas « Publié » dans le README) : lance le skill **`radar`** avant tout le reste (règle de l'`AGENTS.md` du dépôt).

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
