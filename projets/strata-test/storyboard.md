# Storyboard (V2, angle 16 Go) : « Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) »

> **Mis à jour le 14/11 (après-midi), prêt pour la voix.** Chaque plan renvoie à un vrai fichier et à son timecode (codes TT, INST, CONF, DRAGON, BRICK, T3, VOY, MON0 à MON4 : voir « Les rushes » juste en dessous). Les trous R… sont remplis ; les cartes de verdict ne portent plus de note sur 5 (les consoles F12 n'ont pas été filmées), seulement la durée, les demandes et les relances.
>
> **Les timecodes de la vidéo sont des estimations** (script du 14/11, ≈ 13 min 30 à 14 min de voix). **À recaler sur `voix-off-montee.wav`** ; en HyperFrames, `data-start` = le timecode en secondes. Le hook est calculé à 155 mots/min : la question centrale tombe vers 0:28.

## Les rushes (regardés le 14/11)

Dossier : `D:\_Technovore\Youtube\Strata test\`. Timecode = position dans le fichier ; l'heure entre parenthèses est celle de la barre des tâches.

| Code | Fichier | Ce qu'il y a, et où |
|---|---|---|
| **TT** | `Tous les tests strata.mp4` (14/11, 3:57) | **Les résultats.** L'île 0:00-0:40 (la nuit et les étoiles 0:22-0:35) · Sillage 0:41-1:28 (accueil 0:42 et 1:12, chiffres 0:48, destinations et prix 0:54, méthode 1:00, témoignages 1:06) · le mini-Minecraft 1:29-2:27 (blocs posés 2:00-2:27) · le casse-briques 2:28-2:51 (game over 2:30, partie 2:36, bonus « WIDE » 2:48) · **Latitude Sud, le site de Claude** 2:52-3:10 · l'essai 1 en anglais 3:11-3:57 (« From the dunes… » 3:48). ⚠️ Onglets et barre d'adresse visibles : recadre ou floute le haut. |
| **INST** | `Strata installation.mp4` (11/11, 5:40) | Accueil de l'appli 0:00 (19:21) · choix du modèle et du contexte 0:06-1:36, la ligne « Coder IQ1_M · 24,4 Go » 1:24 · téléchargement « 58.4 GB » 1:42-2:24 (19:30) · « Full performance » 2:30-2:48 · « A little tuning » 2:54 (20:02) · « Hello, I'm Strata » 3:00 · premier message 3:06 (20:06), réponse « Je am a Codex model, GPT-5 » 3:42 · il répond en anglais malgré « parle en français » 4:12-5:00 · « 60 tok/s · last reply » 5:00 · Gestionnaire des tâches 5:24-5:30 (VRAM 14,6 / 16 Go, RAM 29,6 Go utilisés, « 32,0 Go DDR5 »). |
| **CONF** | `Strata config avec pi.mp4` (13/11, 5:08, 19:15 → 19:20) | Page Models (contexte 128K, « Fits fully in memory ») 0:00-0:10 · Monitor 0:12-0:40 · `models.json` dans le Bloc-notes 0:48-1:54 (`"maxTokens": 32000` en gros 1:42) · page Serving, l'adresse et `coder-iq1_m` 1:24-1:36 · site de Pi, la commande d'installation 2:36-3:06 · Pi qui démarre 4:06-4:12 · le prompt du casse-briques collé 4:48-5:08. |
| **DRAGON** | `speedtest pi.mp4` (13/11, 1:09, 19:45) | Le prompt du dragon 0:21 · l'histoire qui s'écrit 0:27-0:42 · « Disk read » à 165-183 Mo/s 0:33-0:39 · « Last: 590 tokens at 50.8 tok/s » en haut à droite 0:45. La case Speed est cachée par Pi : le chiffre se montre avec MON3. |
| **BRICK** | `brick game intro.mp4` (13/11, 0:22, 19:33) | Pi devant le moniteur, le prompt du casse-briques envoyé 0:01-0:03, la réflexion qui défile et le moniteur en « Generating » 0:04-0:21. Sert aussi de **plan générique** pour l'île (prompt flouté). |
| **T3** | `test 3 pi qwen.mp4` (13/11, 0:14, 20:30) | Le prompt du mini-Minecraft envoyé, le début de la réflexion. |
| **VOY** | `test voyage debut.mp4` (14/11, 1:06, 10:29 → 10:35) | Le prompt de Sillage, `AGENTS.md` en contexte 0:00-0:09 · le chargement du modèle dans l'appli 0:12-0:51 · Pi qui suit le plan, le moniteur en « Generating » 0:57-1:06. |
| — | `test 2 pi qwen.mp4` (13/11, 20:11) | « Tikaya », le test abandonné : à ne pas utiliser. |

| Code | Capture du moniteur | Ce qu'elle montre |
|---|---|---|
| **MON0** | `Strata-Monitor-2026-11-13.png` (13/11, 18:32) | Au repos : VRAM 15,1 / 16 Go, RAM 24,0 / 31 Go, lecture disque 0,1 Mo/s. |
| **MON1** | `Strata-Monitor-2026-11-13 (1).png` (19:01) | En plein calibrage : « 81.5 t/s Decode now », RAM 29,7 / 31 Go en rouge, lecture disque 239 Mo/s. |
| **MON2** | `Strata-Monitor-2026-11-13 (2).png` (19:07) | Fin du calibrage : 18 requêtes, « average output was 69.4 tok/s ». |
| **MON3** | `Strata-Monitor-2026-11-13 (3).png` (19:46) | Le dragon : ligne 07:45:59, 590 tokens à **50,8 tok/s** ; 45 requêtes (casse-briques compris), « average output was **67.8** tok/s », une pointe à 83,6 ; RAM **30,8 / 31 Go**. |
| **MON4** | `Strata-Monitor-2026-11-14.png` (14/11, 11:30) | Sillage : 63 requêtes, « average output was **66.1** tok/s », un creux à 42,9 ; contexte 54k / 128K ; toutes les requêtes « Done ». |

**Pas filmé, dit à l'oral et illustré au montage** (décidé le 14/11) : le lancement de l'île (plans génériques BRICK, prompt flouté) ; Pi bloqué sur Chrome (carte texte et la ligne de `chrono.mjs`) ; la réponse « written and verified » (carte texte). **Encore à capturer sur ton PC** : les prompts de l'île et de « Sanaka Voyages » (cartes texte) et les 12 photos (sans le chemin) ; `AGENTS.md` et `i18n.js` (`D:\strata-demo\voyage`) ; la sortie de `node chrono.mjs` (à lancer dans un terminal et filmer). Les captures web sont faites (liste en bas).

## La grammaire (celle de la vidéo d'installation, audit du 11/11 § 3)

- **Fond noir**, halo sombre. Pas le bleu ardoise de la 16 Go.
- **De vraies images** presque tout le temps. Schémas seulement pour **deux** idées (les experts, la carte, la RAM et le SSD ; la limite de réponse), en plans courts.
- **Un plan nouveau toutes les 1 à 3 s dans les 30 premières secondes**, puis toutes les 10 s au plus.
- **Un GIF ou un meme avant 0:15** : V05 (0:09).
- **Le défi affiché avant 0:30** : la pastille « PRONOSTIC : LOCAL contre CLAUDE » apparaît à **0:28** et reste en bas jusqu'à la section 5.
- **Grands mots qui s'écrivent avec la voix**, un mot coloré par phrase.
- **Les 15 premières secondes** : les quatre démos, le nom du modèle, **la vitesse**. Aucun contexte, aucun logo, aucun titre.
- **Cartes de verdict** (V11c, V18f, V20d, V20g) : fond noir, le nom du test, puis **durée · demandes · relances**.

## Section 0 : Hook (0:00 – 0:43)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V01 | 0:00 – 0:01 | L'île qui tourne | « 3D » | « Cette île en 3D… » | TT 0:06 |
| V02 | 0:01 – 0:02 | Sillage, l'accueil sur le Kilimandjaro | « SITE » | « …ce site… » | TT 1:12 |
| V03 | 0:02 – 0:03 | Le mini-Minecraft, un bloc posé | « MINECRAFT » | « …ce mini-Minecraft… » | TT 2:00-2:12 |
| V03b | 0:03 – 0:05 | Le casse-briques en pleine partie | « JEU » | « …ce casse-briques : » | TT 2:36 |
| V04 | 0:05 – 0:09 | Les quatre en mosaïque | « **Qwen 3.8 Flash Next** » · « chez moi » | « c'est Qwen 3.8 Flash Next qui les a écrits, chez moi… » | TT |
| V05 | 0:09 – 0:11 | **GIF** : quelqu'un qui tape comme un fou | « 16 Go de VRAM » | « …sur une carte de seize gigas… » | GIF |
| V05b | 0:11 – 0:14 | MON3, la phrase « average output was 67.8 tok/s » surlignée | **« ≈ 70 tok/s »** en très gros | « …à près de soixante-dix tokens par seconde. » | MON3 |
| V05d | 0:14 – 0:20 | Entrée sur un prompt dans Pi (prompt flouté), puis un compteur « relances : à la main » | « **1 demande** par test » · « rien d'automatique » | « Une seule demande par test, rien d'automatique… je le relance. » | BRICK 0:01-0:03 |
| V05c | 0:20 – 0:23 | Quatre vignettes : l'île et le casse-briques cochés, le site et le mini-Minecraft avec leurs relances | « **2 / 4** du premier coup » | « Et deux sur quatre ont marché du premier coup. » | TT |
| V06a | 0:23 – 0:25 | La fiche Hugging Face du Coder, « half of its experts removed » surligné | « la **moitié** » | « Sauf que ce n'est qu'une moitié de modèle. » | `P03-2-moitie-des-experts` |
| V06b | 0:25 – 0:27 | Schéma très court : une grille d'experts dont la moitié s'éteint | « gardée pour **le code** » (écrit, pas dit) | | schéma |
| V06c | 0:27 – 0:31 | Fond noir, le logo de Claude. **La pastille pronostic apparaît en bas** | « ÇA **REMPLACE** CLAUDE ? » | « Alors, est-ce que ça remplace Claude ? » | texte |
| V07a | 0:31 – 0:33 | Ligne 1 qui s'écrit, le moniteur derrière | « 1. La vitesse » | « Au programme : la vitesse… » | texte + CONF 0:20 |
| V07b | 0:33 – 0:35 | Ligne 2, le téléchargement derrière | « 2. Ce qu'il faut à ton PC » | « …ce qu'il faut à ton PC… » | texte + INST 1:48 |
| V07c | 0:35 – 0:37 | Ligne 3, Latitude Sud derrière | « 3. Le site, fait par Claude » | « …le site fait par Claude… » | texte + TT 2:58 |
| V07d | 0:37 – 0:39 | Ligne 4, le ticket du plantage derrière | « 4. Là où ça casse » | « …et là où ça casse. » | texte + C2 |
| V07e | 0:39 – 0:43 | Plein écran, deux mots qui s'opposent, la pastille grossit | « **TON PRONOSTIC** » · « LE LOCAL TIENT » / « CLAUDE ÉCRASE » | « Ton pronostic : le local tient, ou Claude écrase ? » | texte |

## Section 1 : Niveau un, l'île en 3D (0:43 – 2:12)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V08a | 0:43 – 0:47 | Pi devant le moniteur de Strata, l'écran de Pi encore vide | « NIVEAU 1 : **L'ÎLE EN 3D** » | « Niveau un : une île en 3D. » | BRICK 0:00 |
| V08b | 0:47 – 0:53 | Zoom sur Pi ; en incrustation, `~/.pi/agent/` et `~/.claude/` barré | « Pi : **son propre dossier** » | « À gauche, Pi… la config de mon Claude. » | BRICK 0:00 + texte |
| V08c | 0:53 – 0:58 | Le moniteur seul | « Strata = le moteur » | « À droite, le compteur de Strata… » | CONF 0:12-0:40 |
| V09a | 0:58 – 1:05 | Le prompt anglais de l'île en carte texte ; la phrase de la doc « weaker … in languages other than English » surlignée | « en anglais : **sa doc le dit** » | « Ma demande, je l'écris en anglais… » | texte + C4 |
| V09b | 1:05 – 1:15 | Les exigences qui s'écrivent une à une | « relief · eau · 15 arbres · souris · touche N · 0 erreur » | « Une île en cubes, en 3D… » | texte |
| V09c | 1:15 – 1:24 | **GIF** pièce d'arcade qui tombe | « jamais toucher au code · **chaque relance compte** » | « Règle du jeu… une pièce de plus à l'arcade. » | GIF |
| V10a | 1:24 – 1:28 | Entrée dans Pi ; l'heure de départ en incrustation | « 23:42 » | « Je lance. » | BRICK 0:01-0:03 (prompt flouté) |
| V10b | 1:28 – 1:38 | Accéléré : la réflexion qui défile, le moniteur qui passe en « Generating » | « tokens par seconde » · « 1 token ≈ ¾ de mot » | « Et regarde le compteur… on la mesure plus loin. » | BRICK 0:04-0:21 |
| V11a | 1:38 – 1:44 | L'heure d'arrivée en incrustation | « 23:58 · **15 min 32 s** · 1 demande · 0 relance » | « Il a fini : quinze minutes et demie… » | texte |
| V11b | 1:44 – 1:54 | L'île : la rotation, le zoom, la nuit et les étoiles | | « …elle tourne à la souris… la nuit tombe, avec les étoiles. » | TT 0:00-0:40 |
| V11c | 1:54 – 1:58 | **Carte de verdict** | « ÎLE · 15 min 32 s · 1 demande · 0 relance » | | texte |
| V11d | 1:58 – 2:12 | La miniature de la vidéo du 09/11 qui glisse, puis « 29,6 Go » face à « 16 Go » | « Lundi dernier : 16 Go suffisent » · « 29,6 Go > 16 Go » · « **COMMENT IL TIENT ?** » | « Bon. Lundi dernier… Comment il tient ? » | C5 + P03 |

## Section 2 : Comment ça tient chez moi (2:12 – 3:55)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V12a | 2:12 – 2:20 | Schéma : des centaines d'experts, quelques-uns s'allument à chaque mot | « 6 milliards au travail, sur 125 » | « En fait, le modèle d'origine… » | schéma |
| V12b | 2:20 – 2:26 | La page GitHub de Strata, la licence MIT | « **GRATUIT** · open source » | « Strata, c'est le programme qui range tout ça. » | `P02-1-haut`, `P02-2-licence-mit` |
| V12c | 2:26 – 2:34 | Schéma : les experts chauds dans la carte, le reste en RAM, la table sur le SSD | « → la carte » · « → la RAM » · « → le SSD » | « La carte garde les experts les plus utilisés… » | schéma |
| V13a | 2:34 – 2:43 | `MODELS.md`, la règle surlignée | « RAM ≥ experts + ≈ 10 Go » | « Sauf que sa règle, c'est… » | C4 |
| V13b | 2:43 – 2:51 | « a 32 GB PC with a 12 to 16 GB GPU runs the Coder » surligné ; puis la ligne « Coder IQ1_M » dans l'appli | « 32 Go + 16 Go = **le Coder** » | « …sa doc ne prévoit qu'un seul fichier : le Coder. » | C4 + INST 1:24 |
| V13c | 2:51 – 2:58 | La fiche du Coder, « This is an experimental release » | « moitié · pour le code · **EXPÉRIMENTAL** » | « Le même modèle, coupé de moitié… » | P03 |
| V13d | 2:58 – 3:05 | Le tableau : 79,2 contre 82,8, « 95.7% » | « 95 % · **selon ses auteurs** » | « Ils annoncent quatre-vingt-quinze pour cent… » | P03 |
| V13e | 3:05 – 3:09 | Fond noir | « moi, je regarde **ce qu'il fait** » | « Ça, c'est leur chiffre… » | texte |
| V15a | 3:09 – 3:15 | Le téléchargement, « 58.4 GB to download », l'horloge 19:30 | « ≈ 60 Go » | « Et ce que ça demande, en vrai… » | INST 1:42-2:24 |
| V15b | 3:15 – 3:21 | « Hello, I'm Strata », puis le premier message, l'horloge 20:06 | « 19:30 → 20:06 · **un peu plus d'une demi-heure** » | « Chez moi, entre le clic sur Télécharger… » | INST 3:00-3:06 |
| V15c | 3:21 – 3:30 | La barre « System RAM 30.8 / 31 GB » en rouge, puis le Gestionnaire des tâches. Meme « This is fine » possible : la RAM est vraiment pleine | « RAM : **30,8 / 31 Go** » | « Il faut aussi tout fermer… trente virgule huit gigas sur trente et un. » | MON3 + INST 5:24-5:30 |
| V15d | 3:30 – 3:45 | La case « Disk read » : 0,1 au repos, puis 165 → 183 Mo/s pendant le dragon | « au repos : **0** » · « pendant qu'il écrit : **≈ 200 Mo/s** » · « RAM pleine → **le SSD** » | « Et regarde cette case du moniteur… une partie passe par le SSD. » | MON2 + DRAGON 0:33-0:39 |
| V15e | 3:45 – 3:55 | La vignette de l'île qui rétrécit, « NIVEAU 2 » qui arrive | « une île, **ça se regarde** » | « Bon, ça tient. Mais une île… » | TT 0:10 + texte |

## Section 3 : Le site en deux essais, le mini-Minecraft, le casse-briques (3:55 – 6:50)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V17a | 3:55 – 4:00 | Les 12 photos en mosaïque (sans le chemin) | « NIVEAU 2 : **LE SITE** » | « Niveau deux : le site… » | captures des photos |
| V17b | 4:00 – 4:13 | Le prompt « Sanaka Voyages » en carte texte, les exigences qui se cochent | « accueil · 6 destinations · avis · galerie · mobile » | « Le site d'une agence de voyage… c'est moi qui les ai données. » | texte |
| V17c | 4:13 – 4:23 | L'essai 1 qui défile : « From the dunes to the great lagoon », « The Plain of the Giraffes » | « ESSAI 1 · 31 min · **EN ANGLAIS** » | « Premier essai, et là, ça se passe mal… » | TT 3:11-3:57 |
| V17d | 4:23 – 4:33 | Carte texte : l'horloge qui saute de 21:46 à 23:37 ; la ligne de `chrono.mjs` « ⏸ bloqué 110 min 51 s » | « **BLOQUÉ 1 h 50** » | « Et à la fin, il veut se tester tout seul… » | texte + capture chrono |
| V18a | 4:33 – 4:45 | `AGENTS.md` qui défile, puis `i18n.js` et ses textes en français | « ESSAI 2 : **LE PLAN DE CLAUDE** » | « Donc deuxième essai, autrement… » | captures des fichiers |
| V18b | 4:45 – 4:55 | Le prompt de Sillage envoyé, puis Pi qui suit le plan, le moniteur en « Generating » | « **17 min** · 0 erreur » | « Le modèle local, lui, suit le plan… » | VOY 0:00-0:09, 0:57-1:06 |
| V18c | 4:55 – 5:01 | Les deux lignes « ⏸ bloqué » de `chrono.mjs` | « encore **2 blocages** sur Chrome » | « Bon, il s'est encore bloqué deux fois… » | capture chrono |
| V18d | 5:01 – 5:13 | Carte du plan ; deux cases barrées (« galerie plein écran », « avis qui défilent »), deux ajoutées (« diaporama », « fiche par destination ») | « LE PLAN : 770 lignes · 228 textes · **⅓ de la page déjà dedans** » | « Attention quand même… pour chaque destination. » | texte |
| V18e | 5:13 – 5:25 | Sillage : l'accueil sur le Kilimandjaro, les destinations et leurs prix, les témoignages | | « Et le résultat a vraiment l'air d'un site d'agence… » | TT 0:41-1:28 |
| V18f | 5:25 – 5:29 | **Carte de verdict** | « SITE · essai 1 : 31 min, en anglais, bloqué · essai 2 (plan de Claude) : 17 min · 2 relances » | | texte |
| V19a | 5:29 – 5:33 | **GIF** « boss fight » sur fond noir | « NIVEAU 3 : **LE PLUS DUR** » | « Niveau trois, le plus dur… » | GIF |
| V19b | 5:33 – 5:43 | Le prompt du mini-Minecraft envoyé dans Pi | « monde généré · textures en pixels · marcher · **casser · poser** » | « Un monde en cubes généré… » | T3 0:00-0:05 |
| V19c | 5:43 – 5:48 | La réflexion qui défile : rien que du texte | « il ne voit **jamais** ce qu'il dessine » | « Là, il doit inventer le monde… » | T3 0:06-0:14 |
| V20a | 5:48 – 5:56 | Carte texte : « index.html written and verified », puis « 0 fichier » | « « écrit et vérifié » · **0 FICHIER** » | « Premier essai : il me répond… » | texte |
| V20b | 5:56 – 6:04 | Cartes texte : les trois relances, puis le bug `pos.concat` | « 3 relances · 35 min · **un vrai bug trouvé** » | « Il a fallu trois relances… » | texte |
| V20c | 6:04 – 6:16 | Le monde, la balade, les blocs de terre, pierre, sable et bois posés | | « Mais au bout du compte, on se balade… » | TT 1:29-2:27 |
| V20d | 6:16 – 6:20 | **Carte de verdict** | « 3D · 35 min · 3 relances » | | texte |
| V20e | 6:20 – 6:30 | Le prompt du casse-briques collé dans Pi | « 6 rangées · souris · 3 vies · bonus · bruitages · étincelles · 0 erreur » | « Et pour finir, le grand classique… » | CONF 4:48-5:08 |
| V20f | 6:30 – 6:46 | La partie : les vies, le game over, les bonus « WIDE » et « 3x » | « 8 min · 1 demande » | « Huit minutes… et les bonus qui élargissent la raquette… » | TT 2:28-2:51 |
| V20g | 6:46 – 6:50 | **Carte de verdict** | « JEU · 8 min 12 s · 1 demande · 0 relance » | | texte |

## Section 4 : La vitesse, en vrai (6:50 – 9:00)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V21a | 6:50 – 7:00 | L'histoire du dragon qui s'écrit dans Pi | « une histoire de dragon · **presque pas de réflexion** » | « Bref, et la vitesse ?… » | DRAGON 0:21-0:42 |
| V21b | 7:00 – 7:04 | La ligne 07:45:59 du moniteur, « 590 · 50.8 » surlignée | « **51 tok/s** » | « …le moniteur affiche cinquante et un tokens par seconde. » | MON3 |
| V21c | 7:04 – 7:14 | Les phrases « average output was 69.4 tok/s » puis « 66.1 tok/s » ; puis les lignes 42,9 et 83,6 | « pendant les tests : **≈ 70** » · « de 43 à 84 » | « Et pendant les vrais tests… de quarante-trois à quatre-vingt-quatre. » | MON2, MON4, MON3 |
| V22a | 7:14 – 7:23 | Le ticket du repère : « RTX 5070 Ti », « Ryzen 7 9700X », « 31.2 GiB » | « le repère » | « Du coup, pour te donner un repère… » | C1 |
| V22b | 7:23 – 7:30 | « 70.4 » et « thinking off for the suite; temperature 0 » surlignés | « ≈ 70 tok/s · **réflexion coupée** » | « …environ soixante-dix… la réflexion coupée… » | C1 |
| V22c | 7:30 – 7:34 | « Speed only: no correctness check was run » surligné | « sans test de justesse » | « …et sans vérifier si le code marche. » | C1 |
| V22d | 7:34 – 7:41 | Deux barres : ≈ 70 chez toi (réflexion allumée), 70 pour le repère (coupée) | « chez moi : **du même ordre** » | « Chez moi, c'est du même ordre… » | graphique |
| V22e | 7:41 – 7:56 | Le ticket #2250 : « Radeon 9600 XT », « 30.3 GiB », « 37.6 » | « carte de 16 Go abordable · ≈ 37 tok/s » | « Et si ta carte est plus abordable ?… » | C7 |
| V22f | 7:56 – 8:02 | Deux barres : RTX 5080 « 960 Go/s », RTX 5060 Ti « 448 Go/s » | « haut de la fourchette » | « …j'ai une 5080… juste moins vite. » | graphique (T40) |
| V23a | 8:02 – 8:17 | Schéma : une barre « réponse ≤ 16 384 tokens » où la réflexion grignote la place du code | « réflexion + fichier ≤ **16 384** » | « Et justement, la réflexion, c'est le piège… » | schéma |
| V23b | 8:17 – 8:23 | La barre qui déborde, le fichier coupé au milieu d'une fonction | « le fichier s'arrête **au milieu** » | « …ça peut déborder… » | schéma |
| V23c | 8:23 – 8:35 | `models.json` dans le Bloc-notes, `"maxTokens": 32000` en gros | « limite montée à la main · **le fichier en description** » · « …pas toujours assez » | « Du coup, avant le premier test… » | CONF 1:42 |
| V23d | 8:35 – 8:48 | Le tableau de vitesses du projet, la ligne du Coder | « 59 → 43 tok/s · 1 000 → 128 000 tokens » · « autre machine · moteur ancien » | « Le projet le publie lui-même… » | C4 |
| V23e | 8:48 – 9:00 | Le moniteur, puis deux barres : « Pi ≈ 1 500 tokens » / « OpenCode ≈ 7 400 » | « Pi : **5 fois moins** à relire » | « Donc plus l'agent lit de code… » | CONF 0:20 + graphique |

## Section 5 : Et Claude ? (9:00 – 9:30)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V24a | 9:00 – 9:07 | Fond noir, le logo de Claude, la pastille pronostic revient | « ET CLAUDE ? » · « pas de faux match » | « Et Claude, dans tout ça ?… » | texte |
| V24b | 9:07 – 9:15 | Latitude Sud qui défile | « 1 phrase · **2 min 23 s** · en français » | « Je lui ai juste demandé un site de voyage… ça tient la route. » | TT 2:52-3:10 |
| V24c | 9:15 – 9:24 | Écran partagé : Latitude Sud / l'essai 1 en anglais | « mon modèle : 31 min · en anglais · demande détaillée » | « Mon modèle, lui, avait mis une demi-heure… » | TT 2:58 + TT 3:48 |
| V24d | 9:24 – 9:30 | `AGENTS.md` en vignette | « le plan de Sillage : **Claude** » | « Et le plan qui a sauvé le deuxième essai… Bon, et là où ça casse ? » | capture du fichier |

## Section 6 : Là où ça casse (9:30 – 10:35)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V26a | 9:30 – 9:36 | Le moniteur, toutes les requêtes « Done » | « chez moi : **0 plantage** » | « Chez moi, le moteur n'a jamais planté pendant les tests. » | MON4 |
| V26b | 9:36 – 9:46 | Le ticket #5104 : le titre, « exit code -6 », « could not copy experts » | « le moteur plante · cartes de 8 et 12 Go » | « Et chez les autres ?… » | C2 |
| V26c | 9:46 – 9:54 | « The usual cause is running out of RAM » **barré**, puis « Root cause confirmed » | « la vraie cause : **un bug** » | « Le message accuse la RAM. Sauf que… » | C2 |
| V26d | 9:54 – 10:02 | Le ticket « non-finite logits » : « RTX 5080 », « IQ3_S and IQ3_XXS » | « un utilisateur de 5080 rapporte » | « Un utilisateur de 5080 rapporte… » | C3 |
| V26e | 10:02 – 10:09 | Carte texte, **aucun nom de chaîne** | « un autre testeur : le Coder **a raté** la tâche » | « Et un autre testeur… » | texte |
| V26f | 10:09 – 10:19 | La page des versions, la date de création du dépôt | « créé le 24/09 · une version tous les 2-3 jours » | « Strata est jeune… » | C6 |
| V26g | 10:19 – 10:35 | La version de Strata dans l'appli, puis un message d'erreur copié (sans clé) | « note ta version » · « copie le **message exact** » | « Donc note ta version… » | capture de l'appli + texte |

## Section 7 : Le verdict, et ce soir (10:35 – 13:10)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V27a | 10:35 – 10:41 | Les quatre résultats côte à côte | « ÇA REMPLACE **MON ABONNEMENT** ? » | « Alors, est-ce que ça remplace… Pas complètement. » | TT |
| V27b | 10:41 – 10:56 | La page de prix de Claude, « Pro » et « $20 » ; puis un schéma : Claude → le plan, ta carte → le travail | « **20 $ / mois** → le plan » · « ta carte → **l'exécution** » | « Mais il n'en faut plus qu'un petit… » | C8 + schéma |
| V27c | 10:56 – 11:10 | Les vignettes et leurs demandes (île 1, casse-briques 1, mini-Minecraft 4) ; puis « From the dunes… » et « written and verified » côte à côte | « même sans plan : **il s'en sort** » · « ses vraies fautes : 2 » | « Et même sans plan… » | TT + texte |
| V27d | 11:10 – 11:24 | Les lignes « ⏸ bloqué » de `chrono.mjs`, le total qui s'additionne | « **plus de 2 h** à attendre Chrome » | « Le reste du temps perdu… » | capture chrono |
| V27e | 11:24 – 11:40 | Carte texte « the response hit the output token limit », puis `"maxTokens": 32000` barré | « 32 000 : **PAS ASSEZ** » · « −7 min » | « Et une erreur, c'est la mienne… » | texte + CONF 1:42 |
| V27f | 11:40 – 11:50 | Les lignes `write _sim.js`, `write harness.js`, `write validate.js` de `chrono.mjs` | « **ses propres tests** · sans qu'on le demande » | « Et ce qui m'a le plus surpris… » | capture chrono |
| V27g | 11:50 – 11:53 | Fond noir | « Un mauvais achat évité ? **Abonne-toi** » | « Si cette vidéo t'a évité un mauvais achat… » | texte |
| V28a | 11:53 – 12:03 | Ligne 1, le Gestionnaire des tâches derrière | « 1. 12-16 Go de VRAM · 32 Go de RAM · 90 Go de disque » | « Si tu veux le refaire ce soir… » | texte + INST 5:24-5:30 |
| V28b | 12:03 – 12:14 | Ligne 2, la liste des modèles de l'appli, la ligne du Coder | « 2. L'appli Strata · **elle te dit si ça tient** » | « Deux : tu installes l'appli Strata… » | texte + INST 1:24 |
| V28c | 12:14 – 12:21 | Ligne 3, le téléchargement du Coder | « 3. Le Coder · sans images · **ferme tout** » | « Trois : tu prends le Coder… » | texte + INST 1:48 |
| V28d | 12:21 – 12:43 | Ligne 4 : la page Serving (l'adresse), puis `models.json`, `"baseUrl"` et `"maxTokens"` ; puis la touche Échap | « 4. Branche Pi · **monte la limite** » · « bloqué 3 min → **Échap** » | « Quatre : tu branches Pi… » | texte + CONF 1:24-1:42 |
| V28e | 12:43 – 12:52 | Fond noir, deux lignes | « 48 Go → les petites tailles » · « 64 Go → toutes » | « Par contre, si tu as plus de RAM… » | texte |
| V28f | 12:52 – 12:58 | La miniature de la vidéo LM Studio du 02/11 | « 1re IA en local ? **Commence là** » | « Si c'est ta toute première IA en local… » | C5 |
| V29a | 12:58 – 13:04 | La pastille pronostic revient en grand | « **QUI AVAIT RAISON ?** » | « Bref, et ton pronostic du début ?… » | texte |
| V29b | 13:04 – 13:10 | Carte vers la vidéo du jeudi 19/11, écran de fin | « Jeudi : même carte, plus vite » | « Jeudi, on cherche comment aller plus vite… » | C5 |

## Rythme

- **0:00 – 0:28** : 12 plans en 28 s (2,3 s en moyenne, 6 s au plus pour V05d). Puis le plan en 4 lignes (2 s chacune).
- **0:43 – 2:12** : plans de 4 à 12 s, vraie image partout sauf le GIF et les cartes du prompt.
- **Après** : un plan toutes les 5 à 12 s ; jamais plus de 15 s de schéma de suite (V23a).
- **GIF / memes** : V05 (0:09), V09c (1:15), V15c (3:21, « This is fine » : la RAM est vraiment pleine), V19a (5:29).
- **Retournements visuels** : V11d (29,6 Go > 16 Go), V17c (« EN ANGLAIS »), V18d (les deux cases barrées), V20a (« 0 FICHIER »), V26c (la RAM barrée), V27e (32 000 barré).

## Captures web (faites le 14/11)

Dans `D:\_Technovore\Youtube\Strata test\captures web`, en 3840 × 2160, sans onglets ni barre d'adresse, pseudos et avatars floutés. Chaque passage existe en deux versions : propre, et `-surligne` (ou `-barre`), pour faire apparaître le surlignage au montage. `-haut` = le haut de la page ; `-page` = la page entière, pour un défilement.

| Code | Fichiers | Pour |
|---|---|---|
| P02 | `P02-1-haut` (l'en-tête, 44,1 k étoiles), `P02-2-licence-mit` | V12b |
| P03 | `P03-1-haut`, `P03-2-moitie-des-experts`, `P03-3-experimental`, `P03-4-scores` (82.80 · 79.20 · 95.7%), `P03-5-taille` (« reduces to only 29.6 GB ») | V06a, V11d, V13c, V13d |
| C1 | `C1-1-haut`, `C1-2-machine`, `C1-3-vitesse` (70.4 et « thinking off… »), `C1-4-sans-test` | V22a-V22c |
| C2 | `C2-1-haut` (le titre), `C2-2-plantage`, `C2-3-faux-message-barre`, `C2-4-vraie-cause` | V07d, V26b, V26c |
| C3 | `C3-1-haut`, `C3-2-logits` (les trois passages sont dans le titre) | V26d |
| C4 | `C4-models-1-will-it-fit` (avec la règle des 10 Go), `C4-models-2-32-go-16-go`, `C4-models-3-anglais`, `C4-details-1-vitesses-coder` | V09a, V13a, V13b, V23d |
| C5 | `C5-1-miniature-16-go-09-11.jpg`, `C5-2-miniature-lm-studio-02-11.jpg` (celles que YouTube affiche le 14/11). **Celle du 19/11 reste à faire** | V11d, V28f, V29b |
| C6 | `C6-1-haut` (la page des versions), `C6-creation-1-date` (l'API GitHub, « created_at: 2026-09-24 ») | V26f |
| C7 | `C7-1-haut` (le titre : « AMD Radeon 9600 XT », 16 GB VRAM & 32 GB RAM), `C7-2-carte` (30.3 GiB, 37.6) | V22e |
| C8 | `C8-1-haut`, `C8-2-pro` (« $20 if billed monthly », « Claude Code ») | V27b |

À refaire le jour du montage : C8 (le prix peut changer), et ajouter à C5 la miniature du 19/11 quand elle existe. Pour C8 : `node projets/strata-test/captures-web.mjs "D:/_Technovore/Youtube/Strata test/captures web" C8` ; ce que montrent les pages est noté en T46 de [`sources.md`](sources.md).

## À vérifier avant le montage

- [ ] TT : onglets, barre d'adresse et chemins (`D:/strata-demo/…`) recadrés ou floutés ; aucune clé d'API à l'écran.
- [ ] Les plans génériques (BRICK pour l'île, V05d, V08, V10) : le prompt du casse-briques flouté, pour ne pas montrer une autre demande que celle dont parle la voix.
- [ ] Aucun nom de chaîne ou de créateur à l'écran (V26e reste une carte texte ; pseudos GitHub floutés).
- [ ] Les chiffres affichés sont dans [`sources.md`](sources.md) : vitesse, RAM, disque, demi-heure (T45) ; durées, relances, blocages (T41) ; le plan et Latitude Sud (T42) ; le prix (T43) ; les autres (T5, T6, T7, T13, T14, T25, T30, T39, T40).
- [ ] Les GIF et memes sont du type déjà utilisé sur la chaîne (pas ton visage).
