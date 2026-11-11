# Storyboard (V2, angle 16 Go) : « Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) »

> **Les timecodes sont des estimations** : il n'y a pas encore de voix. Ils sont calculés sur le [script V2](script.md) (1 296 mots, chaque trou compté pour 6 mots une fois rempli), à 145 mots/min : **≈ 9 min 30** de voix, plutôt **≈ 10 min** avec tes phrases. **À recaler sur `voix-off-montee.wav`** ; en HyperFrames, `data-start` = le timecode en secondes. Les plans **P…** sont les fichiers du tournage ([`plan-tests.md`](plan-tests.md), section 10) ; **C…** sont des captures web (liste en bas, à faire pendant le téléchargement). Les trous **R1 à R15** sont ceux de la fiche du plan (section 11).
>
> **Changements depuis la V1** : calé sur le script V2 (plus de variantes A / B ; section 2 raccourcie ; la liste « ce soir » porte les commandes) ; les trous renommés R1 à R15 ; un plan pour la ligne `"maxTokens": 32000` (V23c) ; P08, P11, P33 et P40 supprimés (fondus dans P07, P12, le montage et P41) ; « fits / tight » remplacé par le libellé que Strata affiche vraiment ; « tout est en RAM » corrigé (V15d) ; le ticket du plantage montré avec sa cause (V26c) ; **Pi remplace OpenCode** et l'installation passe par l'appli (V08b, V23c, V23e, V24b, V28b, V28d ; tes décisions du 11/11).

## La grammaire (celle de la vidéo d'installation, audit du 11/11 § 3)

- **Fond noir**, halo sombre. Pas le bleu ardoise de la 16 Go.
- **De vraies images** presque tout le temps : ton écran, le moniteur, les pages GitHub et Hugging Face, les tickets, la phrase surlignée en jaune. Schémas seulement pour **deux** idées (les experts dans la carte, la RAM et le SSD ; la limite de réponse), en plans courts, entre des vraies images.
- **Un plan nouveau toutes les 1 à 3 s dans les 30 premières secondes**, puis toutes les 10 s au plus.
- **Un GIF ou un meme avant 0:15** : V05 (0:08).
- **Le défi affiché avant 0:30** : la pastille « PRONOSTIC : LOCAL contre CLAUDE » apparaît à **0:22** et reste en bas jusqu'à la section 5.
- **Grands mots qui s'écrivent avec la voix**, un mot coloré par phrase, un mot barré pour le retournement (V25b).
- **Les 15 premières secondes** : les trois démos qui tournent, **la vitesse affichée**, le score sur 3. Aucun contexte, aucun logo, aucun titre.
- **Une image réelle toutes les 15 s** au moins.
- **Cartes de verdict** (V11c, V18b, V20b, V25a) : fond noir, le nom du test, puis **durée · premier coup oui / non · x / 5 · relance**. C'est là que vont les chiffres de R3, R7, R9 et R12 ; la voix n'en dit qu'une phrase.

## Section 0 : Hook (0:00 – 0:42)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V01 | 0:00 – 0:02 | Le jeu en pleine partie, le compteur de tok/s incrusté en bas à droite | « JEU » | « Ce casse-briques… » | P20 + P12 |
| V02 | 0:02 – 0:04 | Le site qui défile vite | « SITE » | « …ce site… » | P21 |
| V03 | 0:04 – 0:06 | L'île 3D qui tourne, bascule jour → nuit | « 3D » | « …cette île en 3D : » | P22 |
| V04 | 0:06 – 0:08 | Les trois en triptyque, le moniteur dessous | « Écrit par une IA. **Chez moi.** » · « 16 Go de VRAM · 32 Go de RAM » | « une IA les a écrits chez moi, sur ma 5080… » | P20-P22, P12 |
| V05 | 0:08 – 0:10 | **GIF** : quelqu'un qui tape comme un fou (Hackerman ou Kermit) | **⟦R1⟧ tok/s** en très gros | « …à ⟦R1⟧ tokens par seconde. » | GIF |
| V05b | 0:10 – 0:12 | Le compteur du moniteur en gros plan, le chiffre qui bouge | « tokens par seconde » | | P10 |
| V05c | 0:12 – 0:15 | Trois vignettes (jeu, site, île), chacune cochée ou barrée | « **⟦R2⟧ / 3** du premier coup » | « ⟦R2⟧ sur trois ont marché du premier coup. » | P20-P22 |
| V06a | 0:15 – 0:17 | Gestionnaire des tâches, la RAM, « 32 Go » entouré | « 32 Go » | « Sauf que le modèle complet ne rentre pas dans mes trente-deux gigas… » | P04 |
| V06b | 0:17 – 0:19 | La fiche Hugging Face du Coder, « half of its experts removed » surligné en jaune | « la **moitié** » | « …j'ai pris sa moitié… » | P03 |
| V06c | 0:19 – 0:22 | Schéma très court : une grille d'experts dont la moitié s'éteint | « gardée pour **le code** » | « …gardée pour le code. » | schéma |
| V06d | 0:22 – 0:25 | Fond noir, le vrai logo de Claude en couleurs. **La pastille pronostic apparaît en bas** | « ÇA **REMPLACE** CLAUDE ? » | « Alors, une moitié de modèle, est-ce que ça remplace Claude ? » | texte |
| V07a | 0:25 – 0:27 | Ligne 1 qui s'écrit, le moniteur derrière | « 1. La vitesse » | « Au programme : la vitesse… » | texte + P10 |
| V07b | 0:27 – 0:29 | Ligne 2, le téléchargement derrière | « 2. Ce qu'il faut à ton PC » | « …ce qu'il faut à ton PC… » | texte + P07 |
| V07c | 0:29 – 0:31 | Ligne 3, un résultat de Claude derrière | « 3. Le même test, donné à Claude » | « …le même test donné à Claude… » | texte + P30 |
| V07d | 0:31 – 0:34 | Ligne 4, une capture d'erreur derrière | « 4. Là où ça casse » | « …et là où ça casse. » | texte + P16 ou C2 |
| V07e | 0:34 – 0:42 | Plein écran, deux mots qui s'opposent, la pastille grossit | « **TON PRONOSTIC** » · « LE LOCAL TIENT » / « CLAUDE ÉCRASE » | « Ton pronostic : le local tient, ou Claude écrase ? » | texte |

**Si un test a raté** : V01 à V03 montrent l'échec tel quel (le jeu figé, le site tronqué, l'écran noir) ; V05c le dit avec la case barrée. Rien d'autre ne change.

## Section 1 : Niveau un, le jeu (0:42 – 2:03)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V08a | 0:42 – 0:46 | Le terminal en deux volets, Pi à gauche, le moniteur à droite | « NIVEAU 1 : **LE JEU** » | « Niveau un : le jeu. » | P12 |
| V08b | 0:46 – 0:53 | Zoom sur Pi ; en incrustation, `~/.pi/agent/` et `~/.claude/` barré | « Pi : **son propre dossier** » | « À gauche, Pi… et qui ne touche pas à la config de mon Claude. » | P12 + texte |
| V08c | 0:53 – 0:58 | Zoom sur le moniteur | « Strata = le moteur » | « À droite, le compteur de Strata… » | P12 |
| V09a | 0:58 – 1:05 | Le prompt anglais collé ; en incrustation, la phrase de la doc « weaker … in languages other than English » surlignée | « en anglais : **sa doc le dit** » | « Ma demande, je l'écris en anglais… » | P12 + C4 |
| V09b | 1:05 – 1:17 | Le même prompt, les exigences qui s'écrivent une à une | « 6 rangées · souris · 3 vies · bonus · bruitages · étincelles · 0 erreur » | « Un casse-briques complet, dans un seul fichier… » | P12 |
| V09c | 1:17 – 1:25 | **GIF** pièce d'arcade qui tombe | « **1 ESSAI** · 1 relance » | « Règle du jeu : un seul essai… comme une dernière pièce à l'arcade. » | GIF |
| V10a | 1:25 – 1:29 | Entrée, l'horloge de la barre des tâches en gros plan | l'heure de départ | « Je lance. » | P12 |
| V10b | 1:29 – 1:38 | Accéléré de la génération, le compteur en gros | « **⟦R1⟧ tok/s** » · « 1 token ≈ ¾ de mot » | « Et regarde le compteur… trois quarts de mot. » | P12 |
| V11a | 1:38 – 1:42 | Le dernier fichier écrit, l'horloge d'arrivée, double-clic sur `index.html` | | « Il a fini. Je l'ouvre… » | P12, P20 |
| V11b | 1:42 – 1:50 | La partie (une brique casse, un bonus tombe, le son monte), puis la console F12 | | « …le moment de vérité : ⟦R3⟧. » | P20 |
| V11c | 1:50 – 1:54 | **Carte de verdict** | « JEU · ⟦durée⟧ · premier coup : ⟦oui / non⟧ · **⟦x⟧ / 5** · ⟦relance⟧ » (R3) | | texte |
| V11d | 1:54 – 2:03 | La miniature de la vidéo du 09/11 qui glisse, puis la taille du Coder (29,6 Go) face à « 16 Go » | « Lundi dernier : 16 Go suffisent » · « 29,6 Go > 16 Go » · « **COMMENT IL TIENT ?** » | « Bon. Lundi dernier… Comment il tient ? » | C5 + P03 |

## Section 2 : Comment ça tient chez moi (2:03 – 3:49)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V12a | 2:03 – 2:11 | Schéma : des centaines d'experts, quelques-uns s'allument à chaque mot | « 6 milliards au travail, sur 125 » | « En fait, le modèle d'origine est découpé en centaines de petits spécialistes… » | schéma |
| V12b | 2:11 – 2:17 | La page GitHub de Strata, la licence MIT en gros plan | « **GRATUIT** · open source » | « Strata, c'est le programme qui range tout ça. » | P02 |
| V12c | 2:17 – 2:25 | Schéma : les experts chauds dans la carte, le reste en RAM, la table sur le SSD | « les plus utilisés → la carte » · « le reste → la RAM » · « la table → le SSD » | « La carte garde les experts les plus utilisés… » | schéma |
| V13a | 2:25 – 2:34 | `MODELS.md`, « Will it fit? », la règle surlignée | « RAM ≥ experts + ≈ 10 Go » | « Sauf que sa règle, c'est… » | C4 |
| V13b | 2:34 – 2:42 | `MODELS.md`, « a 32 GB PC with a 12 to 16 GB GPU runs the Coder » surligné | « 32 Go + 16 Go = **le Coder** » | « …sa doc ne prévoit qu'un seul fichier : le Coder. » | C4 |
| V13c | 2:42 – 2:49 | La fiche du Coder, « This is an experimental release » surligné | « moitié · pour le code · **EXPÉRIMENTAL** » | « Le même modèle, coupé de moitié… expérimental. » | P03 |
| V13d | 2:49 – 2:56 | Le tableau de la fiche : SWE-bench Verified 79,2 contre 82,8, « 95.7% » | « 95 % du score de code · **selon ses auteurs** » | « Ils annoncent quatre-vingt-quinze pour cent… » | P03 |
| V13e | 2:56 – 3:00 | Fond noir | « leur chiffre » · « moi, je regarde **ce qu'il fait** » | « Ça, c'est leur chiffre. Moi, je regarde ce qu'il fait. » | texte |
| V15a | 3:00 – 3:07 | Le téléchargement du Coder dans l'appli, accéléré | « ≈ 60 Go » | « Et ce que ça demande, en vrai : une soixantaine de gigas… » | P07 |
| V15b | 3:07 – 3:14 | « Preparing your model », le curseur qui saccade, la RAM qui monte | « premier chargement : **⟦R4⟧** » | « …un premier chargement de ⟦R4⟧. » | P07 |
| V15c | 3:14 – 3:24 | Le graphique de RAM du Gestionnaire pendant une génération. **Meme « This is fine »** seulement si la RAM a vraiment chuté | « RAM libre : **⟦R5⟧** » | « Il faut aussi tout fermer… la RAM libre descend à ⟦R5⟧. » | P15 |
| V15d | 3:24 – 3:39 | L'écran Advanced, la ligne `--resident-experts` (ou `--mmap-experts`) surlignée | « resident experts = ce que la carte ne garde pas, **copié en RAM** · rien lu sur le SSD » puis « chez moi : **⟦R6⟧** » | « Et sur l'écran de lancement, regarde cette ligne… Chez moi : ⟦R6⟧. » | P06 |
| V15e | 3:39 – 3:49 | La vignette du jeu qui rétrécit, « NIVEAU 2 » qui arrive | « le grand classique » | « Bon, ça tient. Mais un casse-briques, c'est le grand classique… » | P20 + texte |

## Section 3 : Niveau deux, puis le boss (3:49 – 4:42)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V17a | 3:49 – 3:54 | Le terminal, nouveau dossier vide | « NIVEAU 2 : **LE SITE** » | « Niveau deux : le site… » | P13 |
| V17b | 3:54 – 4:04 | Le prompt « Tikaya » collé, les exigences qui se cochent | « titre + téléphone · 3 cartes · 3 tarifs · FAQ · mobile » | « Une page de présentation pour une appli de paiement qui n'existe pas… » | P13 |
| V18a | 4:04 – 4:11 | Le site ouvert : défilement lent, la FAQ qui s'ouvre, F12 en 375 px | | « ⟦R7⟧. » | P21 |
| V18b | 4:11 – 4:15 | **Carte de verdict** | « SITE · ⟦durée⟧ · premier coup : ⟦oui / non⟧ · **⟦x⟧ / 5** » (R7) | | texte |
| V19a | 4:15 – 4:19 | **GIF** « boss fight » sur fond noir | « BOSS FINAL : **LA 3D** » | « Et maintenant, le boss final… » | GIF |
| V19b | 4:19 – 4:26 | Le prompt de l'île collé | « relief · eau · 15 arbres · souris · **N = nuit** » | « Un relief généré, de l'eau… » | P14 |
| V19c | 4:26 – 4:32 | Pi : rien que du texte (aucune image) ; puis ton pronostic sur fond noir | « il ne voit **jamais** ce qu'il dessine » · « Mon pronostic : **⟦R8⟧** » | « Là, c'est le plus dur… Mon pronostic : ⟦R8⟧. » | P14 + texte |
| V20a | 4:32 – 4:38 | L'île qui s'affiche (ou l'écran noir), la rotation à la souris, la touche N | | « Et là : ⟦R9⟧. » | P22 |
| V20b | 4:38 – 4:42 | **Carte de verdict** | « 3D · ⟦durée⟧ · premier coup : ⟦oui / non⟧ · **⟦x⟧ / 5** · ⟦fluide ?⟧ » (R9) | | texte |

## Section 4 : La vitesse, en vrai (4:42 – 6:24)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V21a | 4:42 – 4:50 | Le moniteur en plein écran pendant le jeu | « JEU · **⟦R1⟧** tok/s » | « Bref, et la vitesse ? Le compteur affichait ⟦R1⟧… » | P12 |
| V21b | 4:50 – 4:57 | Le moniteur pendant le site et l'île | « SITE · 3D · **⟦R10⟧** » | « …et ⟦R10⟧ pour le site et l'île. » | P13, P14 |
| V22a | 4:57 – 5:06 | Le ticket du repère : « RTX 5070 Ti », « Ryzen 7 9700X », « 31.2 GiB » | « le repère » | « Du coup, pour te donner un repère… » | C1 |
| V22b | 5:06 – 5:13 | « 70.4 » et « thinking off for the suite; temperature 0 » surlignés | « ≈ 70 tok/s · **réflexion coupée** » | « …environ soixante-dix tokens par seconde… Mais avec la réflexion coupée… » | C1 |
| V22c | 5:13 – 5:17 | « Speed only: no correctness check was run » surligné | « sans test de justesse » | « …et sans vérifier si le code marche. » | C1 |
| V22d | 5:17 – 5:24 | Deux barres : ton tok/s contre 70 | « chez moi : **⟦R11⟧** » | « Chez moi : ⟦R11⟧. » | graphique |
| V22e | après R11 (≈ 15 s) | Le ticket #2250 : « Radeon 9600 XT », « 30.3 GiB », « 37.6 » surlignés | « carte de 16 Go abordable · ≈ 37 tok/s » | « Et si ta carte est plus abordable ?… » | C7 (T39) |
| V22f | ≈ 6 s | Deux barres sur fond noir : RTX 5080 « 960 Go/s », RTX 5060 Ti « 448 Go/s » ; « ta carte : ça tourne, moins vite » | « haut de la fourchette » | « …j'ai une 5080… juste moins vite. » | T40 |
| V23a | 5:24 – 5:39 | Schéma : une barre « réponse ≤ 1/8 du contexte = 8 192 tokens » où la réflexion grignote la place du code | « réflexion + fichier ≤ **8 192** » | « Et justement, la réflexion, c'est le piège… » | schéma |
| V23b | 5:39 – 5:45 | Un fichier qui s'arrête au milieu d'une fonction (la capture d'écran du calibrage s'il a été coupé, plan 5 ; sinon la barre qui déborde) | « le fichier s'arrête **au milieu** » | « …ça peut déborder, et le fichier s'arrête au milieu. » | capture ou schéma |
| V23c | 5:45 – 5:57 | `models.json` de Pi, la ligne `"maxTokens": 32000` surlignée | « limite montée à la main · **la ligne en description** » | « Du coup, avant le premier test, j'ai monté cette limite… dans le fichier de Pi. » | P09 |
| V23d | 5:57 – 6:10 | Le tableau de vitesses du projet, la ligne du Coder (58,9 … 43,0) surlignée | « 59 → 43 tok/s · 1 000 → 128 000 tokens » · « autre machine · moteur ancien » | « Le projet le publie lui-même… » | C4 |
| V23e | 6:10 – 6:24 | Le moniteur pendant une longue lecture de prompt, puis deux barres : « Pi ≈ 1 500 tokens » / « OpenCode ≈ 7 400 » | « plus il lit, plus il ralentit » · « Pi : **5 fois moins** à relire » | « Donc plus l'agent lit de code, plus il ralentit. C'est pour ça que j'ai pris Pi… » | P12 + graphique |

## Section 5 : Le même test, donné à Claude (6:24 – 7:04)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V24a | 6:24 – 6:31 | Écran partagé : à gauche les trois résultats locaux, à droite trois cases « Claude » vides ; la pastille pronostic revient | « LOCAL » / « CLAUDE » · « **mot pour mot** » | « Maintenant, le vrai test : les trois mêmes demandes… » | P20-P22 |
| V24b | 6:31 – 6:38 | Les vrais logos de Pi et de Claude Code | « pas le même outil · **la même demande** » · « durée · 5 points » | « Ce n'est pas le même outil… je note la même chose… » | texte |
| V25a | 6:38 – 6:50 | Les trois résultats de Claude, chacun avec sa **carte de verdict** | « JEU · SITE · 3D : ⟦durée⟧ · **⟦x⟧ / 5** » (R12) | « ⟦R12⟧. » | P30, P31, P32 |
| V25b | 6:50 – 6:58 | **Retournement** : l'écran partagé complet, le mot du perdant barré (« LE LOCAL ~~TIENT~~ » ou « CLAUDE ~~ÉCRASE~~ », ou aucun si c'est serré) | « sur ces 3 demandes : ⟦R13⟧ » | « Donc, sur ces trois demandes : ⟦R13⟧. » | P20-P22 + P30-P32 |
| V25c | 6:58 – 7:04 | Fond noir | « 3 essais · 1 tentative chacun » | « Attention quand même… rien de plus. » | texte |

## Section 6 : Là où ça casse (7:04 – 8:11)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V26a | 7:04 – 7:12 | Ton incident (le message exact du moteur) ; sinon, le moniteur sans erreur | « chez moi : **⟦R14⟧** » | « Chez moi : ⟦R14⟧. » | P16 ou P12 |
| V26b | 7:12 – 7:22 | Le ticket #5104 : le titre, « exit code -6 », « could not copy experts » surlignés | « le moteur plante · une longue demande · cartes de 8 et 12 Go » | « Et chez les autres ? Sur GitHub, un ticket encore ouvert… » | C2 |
| V26c | 7:22 – 7:30 | La ligne « The usual cause is running out of RAM » **barrée**, puis le commentaire qui donne la cause (« Root cause confirmed ») | « le message accuse la RAM » · « la vraie cause : **un bug** » | « Le message accuse la RAM. Sauf que des utilisateurs ont trouvé la vraie cause… » | C2 |
| V26d | 7:30 – 7:38 | Le ticket « non-finite logits » : « RTX 5080 », « IQ3_S and IQ3_XXS » lisibles | « un utilisateur de 5080 rapporte » | « Un utilisateur de 5080 rapporte une autre erreur… » | C3 |
| V26e | 7:38 – 7:45 | Carte-texte, **aucun nom de chaîne** | « un autre testeur : le Coder **a raté** la tâche · d'autres versions l'ont réussie » | « Et un autre testeur a vu ce Coder rater une tâche… » | texte |
| V26f | 7:45 – 7:55 | La page des versions : 0.2.9 (31/10) → 0.2.13 (09/11), la date de création du dépôt | « créé le 24/09 · une version tous les 2-3 jours » | « Strata est jeune… » | C6 |
| V26g | 7:55 – 8:11 | `strata --version` dans une fenêtre, puis un message d'erreur copié (sans clé) | « note ta version » · « copie le **message exact** » | « Donc note ta version… c'est comme ça que la cause de ce bug a été trouvée. » | P41 + texte |

## Section 7 : Le verdict, et ce soir (8:11 – 9:31)

| Plan | Timecode | Ce qu'on voit | Texte à l'écran | Voix (résumé) | Source |
|---|---|---|---|---|---|
| V27a | 8:11 – 8:17 | Les trois résultats locaux côte à côte | « ÇA REMPLACE **MON ABONNEMENT** ? » | « Alors, est-ce que ça remplace mon abonnement ? » | P20-P22 |
| V27b | 8:17 – 8:28 | `strata launch --stop` : la RAM et la VRAM qui reviennent dans le Gestionnaire | « **⟦R15⟧** » (une phrase courte de ton verdict) | « ⟦R15⟧. » | P41 |
| V28a | 8:28 – 8:38 | Fond noir, ligne 1 qui s'écrit, le Gestionnaire derrière | « 1. 32 Go de RAM · 90 Go de disque libres » | « Si tu veux le refaire ce soir, voilà la liste. Un… » | texte + P04 |
| V28b | 8:38 – 8:49 | Ligne 2, la page Models de l'appli, la ligne du Coder et son libellé | « 2. L'appli Strata · **elle te dit si ça tient** » | « Deux : tu installes l'appli Strata… avant de le télécharger. » | texte + P05 |
| V28c | 8:49 – 8:56 | Ligne 3, le téléchargement du Coder dans l'appli | « 3. Le Coder · sans images · **ferme tout** » | « Trois : tu prends le Coder, sans les images… » | texte + P07 |
| V28d | 8:56 – 9:05 | Ligne 4, la ligne d'installation du Terminal, `strata connect pi --check` qui passe, `"maxTokens": 32000` | « 4. Le Terminal · `strata connect pi` · **monte la limite** » | « Quatre : tu installes aussi le Terminal… » | texte + P09 |
| V28e | 9:05 – 9:14 | Fond noir, deux lignes | « 48 Go → les petites tailles » · « 64 Go → toutes » | « Par contre, si tu as plus de RAM… » | texte |
| V28f | 9:14 – 9:20 | La miniature de la vidéo LM Studio du 02/11 (carte YouTube) | « 1re IA en local ? **Commence là** » | « Si c'est ta toute première IA en local… » | C5 |
| V29a | 9:20 – 9:26 | La pastille pronostic revient en grand | « **QUI AVAIT RAISON ?** » | « Bref, et ton pronostic du début ?… » | texte |
| V29b | 9:26 – 9:31 | Carte vers la vidéo du jeudi 19/11, écran de fin | « Jeudi : même carte, plus vite » | « Jeudi, on cherche comment aller plus vite… Elle arrive juste là. » | C5 |

## Rythme

- **0:00 – 0:25** : 12 plans en 25 s (2,1 s en moyenne, 3 s au plus). Puis le plan en 4 lignes (2 à 3 s chacune).
- **0:42 – 2:03** : plans de 4 à 12 s, vraie image partout sauf le GIF.
- **Après** : un plan toutes les 5 à 12 s ; jamais plus de 12 s de schéma de suite (V23a).
- **GIF / memes** : V05 (0:08), V09c (1:17), V15c (3:14, seulement si la RAM a vraiment chuté), V19a (4:14).
- **Retournements visuels** : V11d (29,6 Go > 16 Go), V26c (la RAM barrée), V25b (le mot barré).

## Captures web (pendant le téléchargement, étape 2 du plan)

| Code | Capture | Pour |
|---|---|---|
| C1 | https://github.com/Niko1221/Strata/issues/4997 : « RTX 5070 Ti », « Ryzen 7 9700X », « 31.2 GiB », « 70.4 », « thinking off for the suite; temperature 0 », « Speed only: no correctness check was run » | V22 |
| C2 | https://github.com/Niko1221/Strata/issues/5104 : le titre, « exit code -6 », « could not copy experts », « The usual cause is running out of RAM », le commentaire « Root cause confirmed » | V07d, V26b, V26c |
| C3 | https://github.com/Niko1221/Strata/issues/5046 : le titre (« RTX 5080 », « non-finite logits », « IQ3_S and IQ3_XXS ») | V26d |
| C7 | https://github.com/Niko1221/Strata/issues/2250 : la machine (« 9600 XT », « 30.3 GiB ») et « 37.6 » | V22e |
| C4 | `docs/MODELS.md` : « Will it fit? », « a 32 GB PC with a 12 to 16 GB GPU runs the Coder », « weaker outside code and in languages other than English » ; `docs/DETAILS.md` : le tableau « Output (tokens/s) », ligne Coder | V09a, V13a, V13b, V23d |
| C5 | Les miniatures des vidéos du 09/11 et du 02/11 (YouTube Studio) ; celle du 19/11 quand elle existe | V11d, V28f, V29b |
| C6 | https://github.com/Niko1221/Strata/releases (0.2.9 → 0.2.13 et leurs dates) et la date de création du dépôt | V26f |

(La page GitHub de Strata et la fiche Hugging Face du Coder sont les plans P02 et P03.)

## À vérifier avant le montage

- [ ] Aucun nom de chaîne ou de créateur à l'écran (V26e reste une carte-texte ; les pseudos GitHub des tickets sont floutés ou hors cadre).
- [ ] Les chiffres affichés (V06c, V11d « 29,6 Go », V12a « 6 sur 125 », V13d « 95 % », V22 « 70 », V23a « 8 192 », V23d « 59 → 43 », V28e « 48 / 64 », V23e « 1 500 / 7 400 ») sont tous dans [`sources.md`](sources.md) (T6, T25, T7, T13, T30, T5, T14).
- [ ] Aucune clé d'API, aucun onglet de navigateur, aucun dossier de travail dans les plans P.
- [ ] Les GIF et memes sont du type déjà utilisé sur la chaîne (memes et visages d'acteurs OK ; **pas ton visage**).
