# 32 Go pour Qwen 27B : les prix, les routes et leurs pièges : kit d'upload YouTube

> **Vidéo** : `/Users/innocent/HyperStudio/premium-noir/2026-11-qwen-27b-32go/renders/q32-montage-final-4k.mp4` (**périmée depuis les reprises de voix du 21/11** ; nouvelle version contrôlée : la 1080p `renders/q32-montage-v5.mp4` (2e lot : « 5060 Ti » et « 16 gigas et demi » redits, hook ×1,1, musique −5 dB), la 4K est à refaire après ton accord) : 30 i/s, **568,3 s (9:28)**. Les temps viennent de la voix avec reprises (`sources/voix.words.json`, la voix démarre à 0 : temps de la voix = temps de la vidéo ; elle finit à 556,8 s, la vidéo 11,4 s plus tard).
> **Sortie** : **lun. 30 nov. 2026, 18 h** ([`calendrier.md`](../../calendrier.md), ligne 5). Faits : [`sources.md`](sources.md) (F1 à F122) ; prix : [`recherche/prix-20-11.md`](recherche/prix-20-11.md).
> **vidIQ, 21/11 : 0 crédit dépensé.** Les outils de mots-clés, d'outliers et de recherche YouTube ne sont pas chargés dans cette session (ToolSearch ne trouve que des outils de comptes, de miniatures, de vidéos de chaîne et de réseaux sociaux). Les volumes ci-dessous sont repris de `sources.md` et des kits voisins, datés ; les vidéos hôtes viennent de la page de résultats de YouTube (curl, 21/11), pas de vidIQ.

## Mots-clés (relevés vidIQ des 23, 24 et 26/10 : aucun n'est refait)

| Mot-clé | Recherches/mois | Concurrence | Usage |
|---|---|---|---|
| vram | 15 336 (−54,7 % sur 30 jours), vidIQ 24/10 | 69 | Titre B, tags, hashtag : « 32 Go de VRAM » est la forme que le public tape |
| ia en local | 15 204, vidIQ 26/10 (21 403, +90,8 %, le 24/10) | 42 | Hashtag, tags : le mot-clé du pilier |
| ia local | 111 094 (8 546 en France), vidIQ 26/10 | 58 | Tags |
| local llm | 87 763, vidIQ 24/10 | 52 | Tags |
| qwen | 179 672 (8 045 en France), vidIQ 23/10 | 48,3 | Première ligne, hashtag, tags |
| carte graphique | 4 315, vidIQ 24/10 | 40 | Tags (« carte graphique ia ») |
| budget gpu | 9 552 (+81,4 %), vidIQ 24/10 | 63 | Pas utilisé : en anglais, c'est le sujet de la vidéo du 26/11 |
| llama.cpp | 21 080 (−46 % sur 30 jours), vidIQ 23/10 | 53,3 | Description, tags (la répartition par couches vient de lui) |
| **qwen 27b**, **32 go vram**, **rtx 5060 ti**, **arc pro b65**, **r9700**, **mac mini m6** | **non mesurés** (outil absent le 21/11) | — | Titre, première ligne, chapitres, tags : à mesurer au radar du 30/11 |

**Lecture** : personne ne cherche « carte graphique occasion ia » (moins de 750, vidIQ 24/10) ; la demande est dans « ia en local », « vram » et le nom du modèle. Le titre garde « 32 Go » et « Qwen 27B » ; les noms des cartes (B65, R9700, 5060 Ti) sont dans les chapitres, la description et les tags, là où la recherche les trouve.

## Titres

| | Titre | Car. | Ce que la vidéo tient |
|---|---|---|---|
| **A · Calendrier (recommandé)** | 32 Go pour Qwen 27B : les prix, les routes et leurs pièges | 58 | Oui : 32 Go et Qwen 27B (0:00 à 0:20), les prix relevés le 20/11 (0:32), 3 routes (0:32, 2:01, 4:06, 5:52), un piège pour chacune (3:03, 5:06, 6:40) |
| B · VRAM et prix | 32 Go de VRAM pour Qwen 27B : 3 routes, 3 pièges (prix du 20 novembre) | 70 | Oui pour les 3 routes et leur piège ; la date des prix est dite à 0:36 et à 7:40 (« le 20 novembre »). « VRAM » est le mot que le public tape. Mais « 3 pièges » écrase les pièges de la 1re route (la tour, l'alimentation, la vitesse) et le cas Tesla V100 : A est plus sûr |

- **Publie avec A seul**, pour les trois miniatures : le test A/B décidé le 15/11 (h, i, j) ne doit tester que l'image.
- A et la miniature ne se répètent pas : l'image demande « 32 GO PAS CHER ? » (la fourchette de prix), le titre promet les routes et leurs pièges. La voix y répond à 0:18 (« 2800 euros… ou, si t'es malin, beaucoup moins ») et à partir de 7:40.
- **Le sujet existe déjà en anglais** (section Suggestions) : « Every way to get 32 GB VRAM… ». Ce qui te distingue : prix français, Amazon contre LDLC, un piège par route, le droit français de l'achat.
- Écarté : un titre avec « de 1 600 à 2 800 € » (la RTX 5090 monte à 7 000 et 9 400 € : la fourchette ne vaut que pour les cartes de 32 Go citées « en stock »).

## Description

```
Pour faire tourner Qwen 27B avec une longue conversation, il te faut 32 Go de VRAM : de 1 600 à 2 800 € en stock le 20/11, selon la route et le site où tu cliques. Trois routes, trois pièges : deux cartes de 16 Go, une seule carte de 32 Go, ou un autre ordinateur.

La même carte coûtait 280 € ou 400 € de moins sur Amazon que chez LDLC, ce jour-là. Au programme : l'addition de la mémoire (31,4 Go), la place, l'alimentation, llama.cpp avec deux cartes, puis la garantie légale et la rétractation.

CHAPITRES
0:00 Introduction : Qwen 27B et ses 32 Go
0:47 Combien de mémoire il te faut vraiment
0:59 Le cache de la conversation et l'addition : 31,4 Go sur 32
2:00 Route 1 : deux cartes de 16 Go (RTX 5060 Ti)
2:30 Route 1 : AMD, Intel et occasion (RX 9060 XT, Arc A770)
3:00 Route 1 : le piège de la place, de l'alimentation et de la vitesse
4:04 Route 2 : une seule carte de 32 Go (Arc Pro B65, B70, R9700)
4:53 Route 2 : le piège du logiciel qui doit gérer la carte
5:10 Route 2 : RTX 5090 et Tesla V100
5:50 Route 3 : changer d'ordinateur (Mac mini M6, Ryzen AI Max+)
6:43 Avant de payer : garantie légale, rétractation, leboncoin
7:33 La route que je prendrais, selon ce que tu as déjà
8:10 Si tu veux une seule carte : B65, B70 ou R9700
8:37 Si tu veux changer d'ordinateur, ou garder ton argent

PRIX RELEVÉS LE 20/11/2026 (TTC affichés, marchand nommé)
• 5060 Ti 16 Go ASUS Dual : 799,99 € Amazon https://www.amazon.fr/dp/B0F4DVKSZ4 ; 1 079,95 € LDLC (1 par client) https://www.ldlc.com/fiche/PB00676833.html
• RX 9060 XT 16 Go ASUS Prime : 699,99 € Amazon, livraison du 3 au 5 janvier https://www.amazon.fr/dp/B0F7LTBFZF
• Arc A770 16 Go : 459,95 € LDLC, rupture en ligne https://www.ldlc.com/fiche/PB00522209.html
• 5060 Ti 16 Go d'occasion : autour de 600 à 670 € (leboncoin, particuliers)
• Arc Pro B65 32 Go : 1 899,95 € LDLC https://www.ldlc.com/fiche/PB00751013.html ; 1 483 € vendeur tiers Amazon, livrée en décembre https://www.amazon.fr/dp/B0HK7VKS9L
• Arc Pro B70 32 Go ASUS : 2 016 € Amazon https://www.amazon.fr/dp/B09CMSRZZ4
• R9700 32 Go Gigabyte : 2 399,99 € Amazon https://www.amazon.fr/dp/B0FJ8XPXTM ; 2 799,95 € LDLC https://www.ldlc.com/fiche/PB00711272.html
• RTX 5090 32 Go : 6 975,27 € vendeur tiers Amazon, fin décembre https://www.amazon.fr/dp/B0F3L2LTRD ; 9 399,95 € LDLC, rupture https://www.ldlc.com/fiche/PB00663200.html
• Mac mini M6 32 Go : 1 709 € LDLC, plus de 15 jours https://www.ldlc.com/fiche/PB00751971.html
• GMKtec EVO-X2 Ryzen AI Max+ 64 Go : 2 029,99 €, précommande https://gmktec.fr/products/gmktec-evo-x2-amd-ryzen-ai-max-395-mini-pc-1

PRÉCISIONS
Prix du 20/11, avant le Black Friday (27/11) : ils ont pu changer. Le 21/11, l'offre Amazon de la RX 9060 XT à 699,99 € n'était plus en ligne.
Les 31,4 Go sont un calcul (fichier 4 bits, cache 16 bits), pas une mesure. Garantie légale et rétractation : droit français.
Occasion : annonces de particuliers ; pas de prix vérifiable pour la Tesla V100 ; TVA du GMKtec non précisée sur sa page.

SOURCES
Qwen3.8-27B : https://huggingface.co/Qwen/Qwen3.8-27B
Le fichier 4 bits : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
llama.cpp : https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
Guide AMD (R9700) : https://www.amd.com/content/dam/amd/en/documents/products/graphics/workstation/radeon-ai-pro-rocm-pytorch-guide.pdf
NVIDIA, CUDA 13 : https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html
Garantie légale : https://www.service-public.gouv.fr/particuliers/vosdroits/F11094
Vices cachés : https://www.service-public.gouv.fr/particuliers/vosdroits/F11007
Rétractation : https://www.service-public.gouv.fr/particuliers/vosdroits/F10485
Qwen 27B sur 8 Go de VRAM : [LIEN À COLLER]

Carte : svg-maps, CC BY 4.0.
MUSIQUES : « Future Minimal » par kissan4 et « Dark Ambient for Crime and Tension » par megalix (Pixabay).

Dis-moi en commentaire : tu pars sur quelle route, avec quelle carte aujourd'hui ?
Sur Technovore, j'ouvre le capot de l'IA que tu utilises. Si cette vidéo t'a évité un mauvais achat, abonne-toi.

#IAenLocal #Qwen #VRAM
```

- **Taille : 4 072 caractères sur 5 000** (compté par script le 21/11 ; les adresses en font environ la moitié). Corps hors chapitres, prix, liens et sources (deux premiers paragraphes, précisions, crédits, appel) : environ 1 250 caractères.
- **Chiffres** (voix finale, `sources.md`) : 32 Go (0:12) ; 1 600 € la paire de 5060 Ti Dual sur Amazon (2:12 ; F117, F118) et 2 800 € la R9700 chez LDLC (0:18 ; F100) ; 280 € d'écart (2:23 ; F118) et 400 € (4:41 ; F118) ; 31,4 Go (1:33 ; F109, calcul en Gio) ; prix de chaque ligne : F97 à F122 (voix : « 800 », « 700 », « 460 », « 1900 », « 2016 », « 2400 », « 2800 », « presque 7000 », « 9400 », « 1709 », « autour de 2000 » : la description donne le prix exact de la page, TTC affiché le 20/11).
- **Ce que la voix arrondit et la description précise** : 799,99 → « 800 » ; 699,99 → « 700 » ; 1 899,95 → « 1900 » ; 2 399,99 → « 2400 » ; 2 029,99 → « autour de 2000 ».
- **PRÉCISIONS** (3 lignes) : les prix sont ceux du 20/11 et ont pu changer (Black Friday le 27/11) ; l'offre Amazon de la RX 9060 XT (699,99 €) n'était plus en ligne le 21/11 (demande de l'auteur ; je n'ai pas rouvert la page, voir « À vérifier ») ; les 31,4 Go sont un calcul ; occasion, V100, TVA du GMKtec.
- **Aucune chaîne ni créateur nommé.** Pas de chemin de dossier ni de clé. Deux pseudos de musiciens (kissan4, megalix) : c'est le crédit Pixabay, comme dans les kits précédents. Aucun lien vers une annonce de particulier, aucun lien d'affiliation.
- **Liens** vérifiés ouverts (code 200, curl, 21/11) : les 13 pages de marchands, les deux dépôts Hugging Face, le README de llama.cpp, le guide AMD, les notes de version de CUDA, les trois fiches service-public. Les pages Amazon ouvrent, mais le prix et le stock affichés le 21/11 n'ont pas été relus. **À coller** : le lien de « Qwen 27B sur 8 Go » (sortie lun. 23/11, pas encore dans `README.md`), à la place de `[LIEN À COLLER]`.
- **Carte** : la carte d'Afrique vient du paquet `@svg-maps/world` (licence CC BY 4.0, lue dans le registre npm le 21/11) ; le crédit est exigé par la licence ; pas de lien (la page du paquet refuse curl, la page du dépôt contient un nom de personne).
- **Musiques** : `scripts/montage.py` utilise `music-minimal-long` et `music-tension-long` ; `style/media.json` les crédite à kissan4 (« future minimal ») et megalix (« dark ambient for crime and tension »), Pixabay. Même liaison que dans les kits précédents.
- **Appel à s'abonner** : la voix le dit à 4:02 (« si cette vidéo t'a évité un mauvais achat, abonne-toi ») ; la description reprend la phrase. L'appel à commenter n'est **pas** dans la voix (la fin est « garde ton argent », puis « et on se dit à la prochaine, salut », reprise de l'auteur du 21/11) : il n'est que dans la description et le commentaire épinglé.
- **Hashtags** : #IAenLocal (le mot-clé du pilier), #Qwen, #VRAM.

### Chapitres : vérification

Recalculés le 21/11 sur la voix du 2e lot de reprises (v5, `voix.words.json`). 14 chapitres, premier à 0:00, le plus court fait 12 s (0:47 → 0:59) : les trois règles de YouTube sont tenues. Ceux du montage (`chapitres.txt`, 8 chapitres) sont remplacés par des chapitres plus précis. Quand aucune seconde entière ne tombe dans le silence avant la phrase, j'ai pris celle qui empiète le moins (signalé).

| Début | Titre | Ce qui l'ouvre dans la voix | Vérification |
|---|---|---|---|
| 0:00 | Introduction | « Qwen 27B, c'est l'un des meilleurs modèles… » | 0,03 s |
| 0:47 | Combien de mémoire il te faut vraiment | « Première réponse » | 47,39 s (« PC » finit à 46,66) |
| 0:59 | Le cache de la conversation et l'addition | « Parce que pendant que tu discutes » | 59,36 s (« mémoire » finit à 58,86) |
| 2:00 | Route 1 : deux cartes de 16 Go | « Première route, la plus tentante » | 120,17 s (« place » finit à 119,38) ; le montage dit 2:00 aussi |
| 2:30 | Route 1 : AMD, Intel et occasion | « Et chez AMD ? » | 149,90 s (« cliques » finit à 149,34) : aucune seconde dans le silence ; 2:30 coupe 0,10 s du début de « Et » |
| 3:00 | Route 1 : le piège de la place… | « Maintenant, le vrai piège de cette route, c'est ta tour » | 180,47 s (« l'heure » finit à 179,92) |
| 4:04 | Route 2 : une seule carte de 32 Go | « Deuxième route » | 244,28 s (« abonne-toi » finit à 243,32) ; le montage dit 4:04 aussi |
| 4:53 | Route 2 : le piège du logiciel | « Côté AMD, j'ai trouvé un guide officiel » | 293,62 s (« plus » finit à 293,07) : 4:53 reprend 0,07 s de la fin de « plus » |
| 5:10 | Route 2 : RTX 5090 et Tesla V100 | « Et chez NVIDIA ? » | 309,98 s (« carte » finit à 309,50) : 5:10 coupe 0,02 s du début de « Et » |
| 5:50 | Route 3 : changer d'ordinateur | « Troisième route » | 350,13 s (« week-end » finit à 349,37) |
| 6:43 | Avant de payer | « Et avant de payer, un dernier piège » | 403,29 s (« entier » finit à 402,54) ; le montage dit 6:43 aussi |
| 7:33 | La route que je prendrais | « Alors, quelle route ? » | 453,65 s (« partout » finit à 452,70) ; le montage dit 7:33 aussi |
| 8:10 | Si tu veux une seule carte | « Pour une seule carte, je prendrais la moins chère » | 490,33 s (« janvier » finit à 489,74) |
| 8:37 | Si tu veux changer d'ordinateur… | « Si tu veux remplacer tout l'ordinateur » | 517,48 s (« 2800 » finit à 516,91) |

« À la prochaine » (9:14 dans le montage) reste hors des chapitres : la phrase « Et on se dit à la prochaine, salut ! » ne dure que 2 s (554,74 à 556,85 s), moins que les 10 s qu'exige YouTube pour un chapitre.

## Tags

```
qwen 27b, qwen 3.8 27b, qwen3.8, 32 go vram, 32gb vram, vram, ia en local, ia locale, ia local, llm local, local llm, carte graphique ia, carte graphique ia locale, rtx 5060 ti 16 go, rx 9060 xt, arc pro b65, arc pro b70, radeon ai pro r9700, rtx 5090, mac mini m6, ryzen ai max+, tesla v100, llama.cpp, deux cartes graphiques, technovore
```

**338 caractères sur 500.** « qwen3.8 » corrige l'écriture du nom de fichier. Pas de « qwen 4 » : voir « À vérifier ».

## Commentaire épinglé

```
Tu pars sur quelle route : deux cartes de 16 Go, une seule de 32 Go, ou un autre ordinateur ? Dis-moi ta carte actuelle et ton boîtier, je te dis quel piège regarder en premier. Les prix sont ceux du 20/11 : si tu en vois un meilleur aujourd'hui, mets-le ici.
```

La voix ne pose aucune question au public : le commentaire épinglé la pose.

## Sous-titres

- Français : [`deux-cartes-occasion.fr.srt`](deux-cartes-occasion.fr.srt) (184 sous-titres, 0:00-9:17 ; recalés le 21/11 sur la voix du 2e lot de reprises, 8 blocs réécrits pour les phrases reformulées).
- Anglais : [`deux-cartes-occasion.en.srt`](deux-cartes-occasion.en.srt), mêmes numéros et mêmes temps ; « GB », prix à l'anglaise (€1,600 ; €2,016), « legal guarantee », dates « November 20 ».
- Dans Studio : « Avec synchronisation », langue de la vidéo en français.
- Le texte est celui de la voix (`voix.phrases.json` : le téléprompteur, sauf les phrases que l'auteur a reformulées dans ses reprises du 21/11, écrites comme il les dit) : « gigas » en français (comme dit), « 31,4 », « 32 000 ». Les segments (≤ 2 lignes de 42 caractères) coupent sur la ponctuation et sur les silences, jamais entre un nombre et son unité (« 5060 / Ti »).
- Contrôle par script : 184 blocs dans chaque fichier, mêmes numéros et mêmes temps ; temps croissants, aucun chevauchement, tout dans [0 ; 568,3 s] (dernier bloc : 9:17,0) ; durées de 0,75 à 5,21 s ; 2 lignes au plus, ligne la plus longue 42 caractères en français et en anglais (aucune au-dessus de 46) ; chaque bloc commence au premier mot de la voix (écart < 0,02 s) ; **1 715 mots de la voix sur 1 715 couverts** (100 %). Trois blocs d'une seule courte phrase (« Et chez AMD ? », « Et chez NVIDIA ? », « Allez, salut ! », 0,6 s de voix) finissent 0,25 s après leur dernier mot au lieu de 0,15 s pour atteindre 0,85 s.

## Suggestions

Le pourquoi est dans [`etudes/suggestions-2026-10-23.md`](../../etudes/suggestions-2026-10-23.md). **vidIQ indisponible** (outils de recherche absents) : recherches YouTube « 32 go vram qwen 27b », « carte graphique ia locale 32 go », « 2 cartes graphiques ia locale », « quelle carte graphique pour qwen 27b » et « RTX 5060 Ti 16 Go deux cartes IA », filtre « ce mois-ci », par curl le **21/11/2026** ; dates et vues lues sur la page de chaque vidéo. Pas un recensement complet. YouTube traduit les titres en français : sauf indication, les vidéos sont en anglais à l'origine, avec une piste française doublée.

### Les vidéos hôtes

| # | Vidéo (titre affiché en français) | Chaîne | Vues (21/11) | Sortie |
|---|---|---|---|---|
| 1 | *Quelle carte graphique choisir pour faire tourner Qwen 4 27B en local* (`gs2Vqh5Jz6c`) | Locally | 16 360 | 14/11 |
| 2 | *Qwen 4 27B arrive : faut-il acheter un GPU maintenant ou attendre ?* (`M_be-Cppn3U`) | RepoChad | 16 199 | 17/11 |
| 3 | *32 Go de VRAM : est-ce que ça vaut encore le coup pour l'IA locale ? Ce qu'elle apporte de plus que…* (`DY0wVKgJkI4`) | KernelBrief | 5 553 | 18/11 |
| 4 | *6 GPU pour l'IA locale : de 300 € à 6500 €, lequel acheter ?* (`Ku-c6seuvMI`, en français à l'origine) | pkillsleep | 8 139 | 16/11 |
| 5 | *La RTX 5060 Ti 16 Go est la carte IA au meilleur rapport qualité-prix, à condition d'en acheter deux* (`hvogZp7nAI0`) | Simply AI | 921 | 09/11 |

**Les mots qu'on partage, et ce qu'on ne prend pas** :
1. Locally (n° 1) : « quelle carte graphique », « Qwen 27B », « IA locale ». Pas « Qwen 4 » (le titre dit « Qwen 27B » comme la voix), pas le plan « quel GPU acheter » sans prix ni piège.
2. RepoChad (n° 2) : « acheter un GPU ». Pas « maintenant ou attendre ».
3. KernelBrief (n° 3) : **le plus proche de ta vidéo** : « 32 Go de VRAM », « IA locale ». Sa miniature promet « SAME 32GB. $6,300 LESS » (une RTX 5090 contre deux RTX 5060 Ti), donc ta route 1 contre ta carte à 7 000 €. Ne prends pas son angle « ça vaut le coup ? » ; ce qui te distingue : les prix français de deux marchands, un piège par route.
4. pkillsleep (n° 4) : « GPU », « IA locale », prix en euros. Pas « de 300 € à 6500 € » : sa vidéo est un classement, la tienne une route.
5. Simply AI (n° 5) : « RTX 5060 Ti 16 Go », « en acheter deux » : la même route 1. Ce qui te distingue : la tour (slot en x4, boîtier à 5 emplacements) et la vitesse qui ne double pas, que son titre promet de contourner.

**À surveiller hors planche** : *Every Way to Get 32GB of VRAM for Local AI (Real Prices, Nov 2026)* (NodeRunner, 575 vues, 16/11, en anglais sans piste française), **exactement ton sujet et la même formule de titre** ; et *Every way to get 32 GB VRAM at Full Context* (23/10, 7 701 vues, même formule de titre). D'autres chaînes ont refait « Every way to get… » pour 64 et 256 Go. Regarde la miniature et le plan du premier avant la sortie : s'il traite aussi le droit de l'achat (garantie, rétractation) et le slot en x4, ton titre est moins unique que tu ne le crois.

### La planche

Les cinq miniatures sont dans [`miniature/hotes/`](miniature/hotes/). `planches.py` a tourné sur des copies renommées (`32go-h.png`, `-i`, `-j`) : [`suggestions-32go-h.png`](../../ressources/miniatures/planches/suggestions-32go-h.png), [`-i`](../../ressources/miniatures/planches/suggestions-32go-i.png), [`-j`](../../ressources/miniatures/planches/suggestions-32go-j.png). Ordre : KernelBrief (n° 3), pkillsleep (n° 4), **la nôtre**, RepoChad (n° 2), Locally (n° 1), Simply AI (n° 5).

### La comparaison à 168 px

- **Elle se repère** : « 32 GO PAS CHER ? » est le seul texte en français de la planche avec celui de pkillsleep, et la seule miniature qui pose une question de prix ; les autres annoncent un nom (« QWEN 4 27B »), un résultat (« 6 300 $ DE MOINS ») ou un ordre (« BUY TWO »). La barre de 32 Go et le logo violet de Qwen se lisent même petits. **h** et **j** : le visage perplexe (le meme) est le seul de la colonne avec la silhouette à capuche de pkillsleep, et il regarde le texte. **i** (sans visage) est la plus discrète : « 32 GO PAS CHER ? » tient sur une ligne plus petite, les deux cartes portent le regard.
- **Elle promet autre chose** : « pas cher ? » (le prix, avec le doute) là où KernelBrief promet un écart en dollars et Simply AI un conseil d'achat ; le titre apporte les routes et les pièges, et le logo de Qwen le sujet. Les deux ne se répètent pas.
- **La couleur** : la palette de h (jaune et orange) se confond avec trois miniatures de la planche (KernelBrief, pkillsleep, Simply AI). **j et i** (ardoise et menthe) sont les seules de la colonne : mon pari est **j** (visage + palette de Technovore).
- **Attention** : la miniature demande « pas cher ? » ; la vidéo répond « ça dépend de ce que tu as déjà » et, au mieux, 1 600 € la paire. Elle tient la promesse dans le doute (« beaucoup moins » que 2 800 € à 0:21 ; « la meilleure carte, parfois, c'est celle que tu n'achètes pas » à 9:13), mais pas le mot « cher » : le visage perplexe porte ce doute.
- **Retouche avant de publier** : aucune.

### L'enchaînement

- **Écran de fin, de 9:17 à 9:28** (la voix finit à 556,8 s, la vidéo à 568,3 s : environ 11 s ; YouTube demande au moins 5 s et au plus 20 s) : à gauche, « Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? » (sortie lun. 23/11, **URL à remplir** : elle n'est pas encore dans `README.md`) ; à droite, « Le setup par budget » (*Setup Black Friday IA locale*, sortie jeu. 26/11, **URL à remplir** : pas dans `README.md` non plus). Les deux seront publiques le 30/11.
- **Vidéo suivante** : *Combien coûte Claude Fable 5.2 chez toi ?* (mar. 1er déc., 18 h, [`calendrier.md`](../../calendrier.md)). La voix ne l'annonce pas (règle du 26/11).
- **Fiche pendant le plateau de rétention** : vers **1:51 à 1:57** (la voix dit « si t'as qu'une carte de 8 gigas, on a vu dans une vidéo précédente comment Qwen 27B y tourne quand même », 110,9 à 117,3 s), vers « Qwen 27B sur 8 Go » ; une seconde à **7:33**, vers « Le setup par budget », quand la voix demande « quelle route ? » (la vidéo du 26/11 donne des configurations par budget). Plateau inconnu : recale-les sur la courbe au radar du 30/11.

## À vérifier avant l'upload

- **Écoute les sous-titres une fois sur la vidéo.** Je n'ai pas écouté l'audio. `voix.words.json` est un alignement du téléprompteur sur la voix (wav2vec2), pas une transcription libre : si la voix clonée dit un mot autre que le script, ce fichier ne le montre pas. Les endroits où `renders/controle-raccords.txt` signale des défauts réparés (à réécouter dans la vidéo finale) : « 5060 Ti » vers **2:06**, **2:52**, **7:54** (entendu « cinquante soixante-dix » dans l'une des deux sources), « 9060 XT » vers **3:26**, « cliques » vers **2:28**, « 14 jours » vers **7:04**, « outils » vers **4:56**, « valable » vers **7:31**.
- **Aucune correction de transcription n'a été nécessaire** (les 17 différences de texte entre `voix.phrases.json` et sa version « dite » ne sont que de la ponctuation) : le texte des sous-titres est le téléprompteur ; seuls la ponctuation et les traits d'union diffèrent de `voix.words.json` (« micro-ATX », « abonne-toi », « mini-PC Ryzen AI Max+ »).
- **Le chapitre de l'addition (1:23)** est impossible (voir le tableau) : l'addition est dans le chapitre de 1:01.
- **Prix** : relus contre `recherche/prix-20-11.md` ; **je n'ai pas rouvert les pages le 21/11**, sauf pour vérifier que les liens répondent (200) : les prix et le stock des pages Amazon et LDLC ont pu bouger (Black Friday le 27/11). Relis-les le jour de l'upload ; l'offre Amazon de la RX 9060 XT à 699,99 € « n'était plus en ligne » le 21/11 selon toi : je l'ai gardée dans la description avec la mention, parce que la voix la cite.
- **Garantie légale** : la voix dit « 2 ans… présumé exister 2 ans pour le neuf, 12 mois pour l'occasion » ; la fiche service-public F11094, relue le 21/11 (« vérifiée le 17 août 2026 »), dit « 24 mois pour les biens neufs et reconditionnés, 12 mois pour les biens d'occasion » : c'est bon (l'ancienne note de F74 dans `sources.md` disait 12 mois partout).
- **« Qwen 27B » et « Qwen 4 »** : trois des cinq vidéos hôtes écrivent « Qwen 4 27B » ; la voix et `sources.md` disent « Qwen 27B » (Qwen3.8-27B sur Hugging Face). Je n'ai pas vérifié si c'est le même modèle : tag « qwen 4 » non ajouté.
- **Non mesuré** : « qwen 27b », « 32 go vram », « rtx 5060 ti », « arc pro b65 », « r9700 », « mac mini m6 » : les outils vidIQ ne sont pas chargés (0 crédit dépensé).
- **GMKtec** : la description donne 2 029,99 € (la voix : « autour de 2000 », « un peu plus de 2000 » dans prix-20-11.md) ; la page ne dit pas clairement si la TVA est incluse : c'est dit à la fin des PRÉCISIONS.
- Après chargement : `calendrier.md` et `README.md` disent encore « Voix » : passe-les à « Programmé ». Ajoutés par ce kit : les cinq miniatures sous `miniature/hotes/` et les trois planches sous `ressources/miniatures/planches/`.
- Après la sortie : skill `radar` (règle du dépôt).
