# Sources : deux cartes d'occasion pour avoir le maximum de VRAM

> Recherche du 24/10/2026 (phase 1). Fiche : [`fiche.md`](fiche.md). Machine de l'auteur : [`../claude-ou-mon-pc-1/fiche.md`](../claude-ou-mon-pc-1/fiche.md). Modèles et noms : [`../claude-ou-mon-pc-1/modeles-5080.md`](../claude-ou-mon-pc-1/modeles-5080.md).
>
> `⚠️` = source unique, secondaire, non datée, en dollars, ou non confirmée à la source officielle. Les colonnes « 1re vérif » et « 2e vérif » sont vides : elles servent aux deux vérifications du pipeline.
> **Aucune vitesse (tokens/s) n'est annoncée dans la fiche.** Celles de ce document sont des mesures publiées par d'autres, datées, avec leur contexte ; l'auteur mesure les siennes.

## Limites de la recherche (à lire d'abord)

- **leboncoin, eBay.fr, Back Market et Rakuten refusent l'accès automatique (erreur 403).** Les prix français d'occasion viennent donc de résultats de recherche (extraits de pages leboncoin, sans date), de deux agrégateurs (Okazza, DealTracker) et de guides européens. Ce sont des **prix demandés**, pas des ventes conclues. L'auteur doit relever les vraies annonces lui-même, la veille du script (comme pour la vidéo « 16 Go » : relevé 24-25 oct., épinglé le 27 nov.).
- Le marché est **en hausse** (F18) : un prix de septembre n'est pas un prix d'octobre.
- La fiche constructeur Gigabyte (carte mère) renvoie 403 : les slots viennent d'une copie chez un revendeur (F60).
- Les articles de loi sur Légifrance n'ont pas pu être lus : le texte vient de service-public.gouv.fr (F74) ; les numéros d'articles viennent de sources secondaires (F75, F76).

## vidIQ (24/10/2026)

8 appels, 40 crédits (solde avant : 4 871).

### Mots-clés (`vidiq_keyword_research`, pays FR)

| Mot-clé | Volume mensuel estimé | Score volume (0-100) | Concurrence | Tendance | Remarque |
|---|---|---|---|---|---|
| carte graphique occasion ia | < 750 | 0 | inconnue | inconnue | trop petit pour être le mot-clé du titre |
| 2 cartes graphiques ia | < 750 | 0 | inconnue | inconnue | idem |
| vram | 15 336 | 62 | 69 | −54,7 % | gros volume, mais en baisse et surtout mondial |
| ia en local | 21 403 | 65 | 42 | +90,8 % | **meilleur mot-clé français** (déjà celui de « Claude ou mon PC ? ») |
| ia locale | 9 091 | 59 | 53 | inconnue | variante |
| local ai | 278 076 | 81 | 70 | +30,2 % | 10 112 recherches en France (`countryVolume`) |
| budget gpu | 9 552 | 59 | 63 | +81,4 % | monte vite, en anglais |
| rtx 3090 | 30 215 | 67 | 52 | −41,8 % | en baisse |
| local llm | 87 763 | 74 | 52 | −10,5 % | |
| carte graphique | 4 315 | 54 | 40 | inconnue | |

Lecture : personne ne cherche « carte graphique occasion ia » sur YouTube en français. La demande est dans **« ia en local »** (+90,8 %), pas dans le matériel d'occasion. Le titre doit porter « IA en local » ou « VRAM », et la curiosité doit faire le clic.

### Vidéos de référence (`vidiq_outliers` en `en`, `vidiq_youtube_search`)

Vues relevées le 24/10/2026. « Breakout » = multiple des vues habituelles de la chaîne.

| Vidéo | Chaîne (abonnés) | Vues | Date | Angle déjà pris |
|---|---|---|---|---|
| [I Turned Two Pieces of E-Waste into One AI Supercomputer!](https://www.youtube.com/watch?v=u6LRz8AcJLQ) | TinyTechGuy (6,6 K) | 60,3 K (×77) | 18/10/2026, 31:42 | **deux vieilles cartes en une seule machine** : le plus proche de notre idée. ⚠️ à regarder en entier avant de filmer |
| [The Cheapest 32GB Nvidia GPU You Can Buy for Local AI (Tesla V100)](https://www.youtube.com/watch?v=3P6m_QBIgAo) | Lon.TV (415 K) | 386 K (×19) | 06/09/2026, 15:09 | une seule carte de datacentre, 32 Go |
| [The Only Local AI GPUs Worth Buying Right Now (Ranked)](https://www.youtube.com/watch?v=Oa3MUGsFays) | Digital Spaceport (104 K) | 137 K | 16/09/2026, 20:28 | classement des 17 cartes, prix par Go de VRAM, tableau en ligne |
| [Best Ways to Get 48GB VRAM for Local AI](https://www.youtube.com/watch?v=2FjEvCDA8Yg) | RepoChad (11,9 K) | 41 K | 21/09/2026, 17:35 | les routes vers 48 Go : 2×3090, A6000, 2×7900 XTX, 2×Arc Pro B60, Mac |
| [54GB of VRAM for $35: The Cheapest Local AI Hack?](https://www.youtube.com/watch?v=baRbCkOUGA4) | RepoChad | 47 K | 10/10/2026, 10:22 | neuf cartes de minage P106 de 6 Go : coupe par couches, pièges |
| [The Truth About Running AI On Your Own Hardware](https://www.youtube.com/watch?v=HRLhJjaCu-E) | Locally (3,6 K) | 139,4 K (×725) | 09/08/2026, 13:56 | vérité sur le matériel local |
| [The Only GPUs Worth Buying For Local AI (October 2026)](https://www.youtube.com/watch?v=YPKYFxpyUlQ) | Locally | 11,4 K | 17/10/2026, 13:23 | une carte par taille de VRAM, prix d'octobre, $/Go |
| [The Best Local AI Models For A 48GB VRAM Setup](https://www.youtube.com/watch?v=haSZQNa9Qs8) | Locally | 2,8 K | 18/10/2026, 11:24 | ce qui tient dans 48 Go (2×3090, 2×7900 XTX, 2×B60) |
| [Top 5 Budget GPU for Local AI 2026](https://www.youtube.com/watch?v=pnACi9ELFhI) | Red Stapler (180 K) | 58,8 K | 26/03/2026, 3:42 | top 5 : RTX 3060 12 Go « reine du budget » |
| [Every Way to Run Qwen 3.8 27B: Free TPU to a $16,000 AI Server](https://www.youtube.com/watch?v=QCJXnij6W0Y) | Morgans Code (2,1 K) | 15,7 K | 07/10/2026, 11:01 | inclut 2×RTX 3060 12 Go avec tensor split et des P40/V100 |
| [Forget the $7,000 RTX 5090: Real AI on a $19 GPU](https://www.youtube.com/watch?v=S6_5Wfn2BkM) | Deep Tech with Amir Husain (4 K) | 87,5 K (×158) | 10/10/2026, 14:10 | une carte à 19 $ |
| [Build a Home AI Lab: What It Takes and What It Costs](https://www.youtube.com/watch?v=sUEdvHxPKN0) | Manolo Remiddi (30,7 K) | 176,9 K (×20) | 21/08/2026, 25:01 | coût d'un labo à la maison |
| [Best Hardware for Running Local LLMs in 2026: Mac vs NVIDIA vs Cloud](https://www.youtube.com/watch?v=sR8sJ2mybQU) | Kai (56,1 K) | 119,5 K (×28) | 12/08/2026, 13:48 | la chaîne que Technovore suit déjà (voir `etudes/kai.md`) |

Dans la description de Locally (17/10), un lien vers « Two cheap GPUs against one expensive one » (youtu.be/Yzoa38-Bhwo) : **c'est exactement notre sujet**, mais vidIQ n'en donne pas les chiffres. ⚠️ à ouvrir avant le script.

### Ce qui existe en français

- **Aucune vidéo française sur le multi-GPU d'occasion pour l'IA** dans les résultats : `vidiq_outliers` en `fr` (mots « carte graphique occasion IA locale deux GPU ») ne renvoie que du hors-sujet (mise à jour de pilotes, affiches IA, réparation) ; `vidiq_youtube_search` en français, deux requêtes, ne renvoie que des vidéos anglaises. ⚠️ Ce n'est pas un recensement complet de YouTube.
- Le plus proche en français : [IA locale : est-ce que ça vaut le coup ? J'ai installé et comparé 5 modèles](https://www.youtube.com/watch?v=rxzxx5Zy3sw), Loïc Frissard - Digitiz (11,6 K abonnés), 57,6 K vues, 24/09/2026, 11:20. C'est du logiciel, pas du matériel.
- Signe d'appétit français pour le bricolage de cartes : [Tuto facile : ajouter de la RAM à sa carte graphique](https://www.youtube.com/watch?v=n-Zouctc9c0), Le BENGE (84,9 K), 612,9 K vues, 26/07/2026.
- **Angles déjà pris en anglais** (à ne pas copier) : classements de cartes avec prix par Go (Digital Spaceport, Locally), « 48 Go : les 5 routes » (RepoChad), le rig de minage à 35 $ (RepoChad), les deux déchets électroniques (TinyTechGuy), la V100 seule (Lon.TV).
- **Angles libres** : les prix et la garantie **en France, en euros** ; la comparaison **2 cartes à 12 Go contre 1 carte à 24 Go** à VRAM égale ; **ajouter une carte d'occasion à côté d'une 5080** dans une carte mère micro-ATX réelle ; ce qui change quand la 2e carte est sur un slot x4.

## Tableau des faits

Les numéros sont ceux que reprend `fiche.md`. Les tailles de fichiers viennent de l'API de Hugging Face, lues le 24/10/2026 (1 Go = 10⁹ octets, comme sur Hugging Face). Une carte « 24 Go » a 24 Gio, soit 25,8 Go décimaux.

### A. Prix d'occasion

| n° | Affirmation | Source (URL + date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| F1 | RTX 3060 12 Go d'occasion : médiane **280 €**, 44 annonces des 30 derniers jours, tendance stable. Prix demandés, pas des ventes. | https://okazza.com/prix/rtx-3060, mis à jour le 24/10/2026 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : la page Okazza ne sépare pas les 3060 de 8 et de 12 Go. |
| F2 | RTX 3060 12 Go d'occasion : environ 160 à 230 € (170-240 € à deux ventilateurs, 220-290 € modèles haut de gamme) ; neuve 210-300 €. ⚠️ date approximative (guide publié environ 2 mois avant le 24/10) | https://www.geekom.fr/rtx-3060/ | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : guide daté du 20/08/2026, sans méthode. |
| F3 | RTX 3060 12 Go : annonces leboncoin surtout entre 190 et 390 €. ⚠️ extraits de recherche, sans date | https://www.leboncoin.fr/ck/ordinateurs/rtx-3060-12go (vu le 24/10/2026) | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés) |
| F4 | RTX 3090 d'occasion en France : prix moyen **834 €**, la plupart des annonces entre 715 et 1 600 €. ⚠️ page sans date, aucun marché listé | https://www.dealtracker.org/fr/fr/product/rtx_3090/ (vu le 24/10/2026) | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : page sans date ni taille d'échantillon (annonces de particuliers : leboncoin, Vinted, eBay, Facebook). |
| F5 | RTX 3090 sur leboncoin : 800 € (Founders Edition, Meaux), 825 € (MSI, Port-la-Nouvelle), 900 € (Asus, Saintes), 1 190 € (EVGA FTW3 Ultra, Mâcon). ⚠️ extraits sans date, annonces possiblement retirées | https://www.leboncoin.fr/ck/ordinateurs/rtx-3090/p-2 (vu le 24/10/2026) | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés) |
| F6 | RTX 3090 d'occasion en Europe : 600 à 900 € ; RTX 3060 12 Go : 180-260 € ; P40 : 230-330 € ; MI50 32 Go : 200-260 € ; V100 32 Go : 450-900 € ; V100 16 Go : 280-450 €. Prix vus sur eBay États-Unis et Royaume-Uni, convertis en euros, **sans TVA ni douane ni transport** (sauf MI50 « livraison comprise ») ⚠️ | https://pasqualepillitteri.it/en/news/10761/used-server-gpu-local-llm-prices-europe, 12/08/2026 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : la page ne dit pas si TVA, douane et transport sont inclus (seule la MI50 est « shipping included »). |
| F7 | Prix **américains** de la RTX 3090 d'occasion : 1 600-1 700 $ (« going rate », 22/10/2026) ; 1 207 $ (moyenne des 3 offres les plus basses eBay et Amazon, septembre) ; 1 343 $ (moyenne de 301 annonces eBay, 4 sept.). Écart fort avec la France ⚠️ | https://locallyexplains.site/prices/ (22/10/2026) ; https://gpupoet.com/gpu/market-report/gpu-market-report-october-2026 ; https://pcserverandparts.com/news/used-graphics-card-buying-guide-2026/ (4/09/2026) | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : le « going rate » de locallyexplains est 1 700 $ (22/10), pas 1 600-1 700 $ ; le 1 343 $ mélange annonces vendues et actives. |
| F8 | RTX 3090 sur gpuprix (France) : moins chère neuve 2 218 € ; seule offre d'occasion 3 159 € (Amazon.fr, reconditionnée) ; médiane sur 12 mois 1 990 €. Donnée aberrante, **à ne pas utiliser** comme prix d'occasion | https://gpuprix.com/fr/france/gpus/geforce-rtx-3090, 24/10/2026 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés) |
| F9 | RX 6800 XT 16 Go sur leboncoin : 360 € (très bon état, Bordères-sur-l'Échez) et 399 € (Sapphire Nitro+, Cernay) ; une MSI Gaming X Trio à 320 € sur eBay.de. ⚠️ extraits sans date, 2 annonces | https://www.leboncoin.fr/ck/ordinateurs/6800-xt (vu le 24/10/2026) ; https://www.ebay.de/itm/396882360498 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés) |
| F10 | RX 7900 XTX 24 Go : 750 € sur leboncoin (Sapphire Pulse, Oradour-sur-Vayres, très bon état) ; 790 € sur eBay.de. Neuve, elle est passée de 1 199,90 à 1 409,90 € en une semaine en septembre 2026. Aux États-Unis, d'occasion : environ 1 200 $ (17/10/2026). ⚠️ annonces sans date | https://www.leboncoin.fr/ck/ordinateurs/rx-7900-xtx ; https://www.cowcotland.com/news/102399/.html ; https://www.youtube.com/watch?v=YPKYFxpyUlQ (description, 17/10/2026) | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés) |
| F11 | RTX 4060 Ti 16 Go : **aucun prix d'occasion trouvé en France**. Repères : 750 $ (« lowest price », page non datée) ; 824 € le moins cher en France au 1er août 2026 sur gpuprix, avec un minimum sur 12 mois de 393 € identique à la médiane, donc suspect ⚠️ | https://digitalspaceport.com/local-ai-gpu-price-and-performance/ ; https://gpuprix.com/fr/france/gpus/geforce-rtx-4060-ti-16gb | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : gpuprix affiche le 24/10 un plus bas de 389 € (neuf, rupture de stock) ; le 824 € n'est plus retrouvé : données instables. |
| F12 | Intel Arc A770 16 Go : plus d'occasion trouvé ; neuve 325 € en France au 29/06/2026 (médiane 3 mois 352 €). Le ReBAR (Resizable BAR) est obligatoire pour la série Arc A. ⚠️ | https://gpuprix.com/fr/insights/analyse-marche-intel-arc-a770 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). Vu au passage : gpuprix (France, 24/10) donne 675 € neuve au plus bas, médiane 3 mois 303 € ; le « 325 € au 29/06 » n'est plus retrouvé. ReBAR « de fait obligatoire » ✅ (la carte tourne sans, mais bien plus lentement). |
| F13 | Tesla P40 24 Go : 220 à 290 $ nue (ventes de septembre 2026), 250 à 325 $ avec refroidissement ; 270 $ sur un autre suivi. Sur eBay.de, des particuliers l'affichaient à 340 et 400 € (instantané 2025 ⚠️). | https://insiderllm.com/guides/used-tesla-p40-local-ai/ (maj 24/09/2026) ; https://digitalspaceport.com/local-ai-gpu-price-and-performance/ ; https://www.ebay.de/itm/405968568300 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés) |
| F14 | AMD Instinct MI50 32 Go : **les sources se contredisent** : 200-260 € (F6, août 2026) contre 500 à 650 $ sur eBay (vérifié « début août 2026 » par un autre guide) ; 120-210 $ sur Alibaba. ⚠️ prix non fiable | https://localaimaster.com/blog/amd-mi50-local-llm, 06/09/2026 | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). La contradiction des sources est confirmée (localaimaster, 06/09/2026). |
| F15 | Références de prix **neufs** en France (le 24/10/2026) : RTX 5080 médiane 1 900 € ; RTX 5060 Ti (toutes versions) 670 € ; RX 9060 XT 720 € ; RTX 5070 Ti 1 460 €. Chaque jour, le plus bas prix chez 14 marchands français ; neuf ou occasion non précisé. | https://www.comparateur-gamer.fr/evolution-prix/carte-graphique, 24/10/2026 | | ✅ comparateur-gamer.fr, 24/10/2026 : RTX 5080 1 900 €, 5060 Ti 670 €, RX 9060 XT 720 €, 5070 Ti 1 460 € (médianes, 14 marchands). Neuf ou occasion non précisé : ce sont des marchands, donc du neuf en pratique. |
| F16 | Cartes modifiées à plus de VRAM (RTX 2080 Ti 22 Go : 610 $ + 10 $ de port ; RTX 3080 20 Go : 979 $ ; RTX 4090 48 Go : 5 469 $) sur eBay États-Unis, relevées le 7/10/2026. Garantie mince, revente difficile. ⚠️ | https://www.youtube.com/watch?v=hS3VYqbQr6A (description, 09/10/2026) | | ⚠️ à relever par l'auteur (consigne du 24/10 : prix d'occasion non revérifiés). La description (vidéo du 08/10/2026, relevés eBay US du 7/10) dit bien 610 $ + 10 $, 979 $ et 5 469 $. |
| F17 | Digital Spaceport donne la RTX 4060 Ti 16 Go à éviter, la RTX 3060 12 Go « meilleure entrée de gamme » et la RTX 3090 « meilleur rapport » ; Red Stapler classe la RTX 3060 12 Go n° 1 des cartes bon marché. Avis, pas des mesures. | https://www.youtube.com/watch?v=Oa3MUGsFays (16/09/2026) ; https://www.youtube.com/watch?v=pnACi9ELFhI (26/03/2026) | | ✅ chapitres des deux vidéos : « RTX 4060 Ti (16GB): Why You Should Avoid It », « RTX 3060 (12GB): Best Budget Entry-Level », « RTX 3090 24GB (Best Value) » ; Red Stapler « #1: RTX 3060 12GB (The Ultimate Budget AI King) ». |
| F18 | Le marché monte : prix en hausse sur 59 des 81 cartes entre août et septembre 2026 (surtout aux États-Unis) ; en France, les cartes graphiques ont pris +4,1 % en 30 jours et +25,5 % en 3 mois (relevés quotidiens depuis le 14 mai 2026). | https://gpupoet.com/gpu/market-report/gpu-market-report-october-2026 ; https://www.comparateur-gamer.fr/evolution-prix/carte-graphique (24/10/2026) | | ⚠️ 59 sur 81 ✅ (gpupoet, 01/10/2026, août → septembre, eBay et Amazon, en dollars, pays non dit). France : la page du 24/10 relue affiche **+5,3 % sur 30 jours et +30,8 % sur 3 mois** (605 modèles), pas +4,1 / +25,5 : l'indice bouge chaque jour. C'est un indice de cartes **neuves** chez 14 marchands, pas de l'occasion. |

### Tableau « € par Go de VRAM » (occasion, France, octobre 2026)

Calculé sur les fourchettes ci-dessus, par Go indiqué sur la boîte (Gio). Un seul site ou des annonces sans date : ⚠️.

> **2e vérif (24/10)** : ⚠️ ces deux tableaux ne sont qu'un **ordre de grandeur** ; tous les prix d'occasion sont à relever par l'auteur. La VRAM de chaque carte est juste. Le « ✅ » de la 3060 n'en est plus un (F1 mélange 8 et 12 Go) ; l'A770 neuve est à 675 € le 24/10 chez gpuprix, pas 325 € (F12).

| Carte | VRAM | Fourchette d'occasion retenue | € par Go | Fait | Remarque |
|---|---|---|---|---|---|
| RTX 3060 | 12 Go | 200 à 300 € (médiane 280 €) | 17 à 25 | F1, F2, F3 | ✅ plusieurs sources ; CUDA |
| RTX 3090 | 24 Go | 800 à 1 000 € ⚠️ | 33 à 42 | F4, F5, F6 | annonces, pas ventes ; 1 600 $ aux États-Unis (F7) |
| RX 6800 XT | 16 Go | 360 à 400 € ⚠️ | 22 à 25 | F9 | 2 annonces ; pas de CUDA |
| RX 7900 XTX | 24 Go | 750 à 900 € ⚠️ | 31 à 38 | F10 | 1 annonce + eBay.de ; pas de CUDA |
| RTX 4060 Ti | 16 Go | non trouvé ⚠️ | n.d. | F11 | neuve ≈ 824 € ? |
| Arc A770 | 16 Go | non trouvé ; neuve 325 € ⚠️ | 20 (neuve) | F12 | ReBAR obligatoire |
| Tesla P40 | 24 Go | 230 à 330 € ⚠️ (+ 25 à 35 $ de ventilateur) | 10 à 14 | F6, F13 | eBay États-Unis / Royaume-Uni, sans TVA ni douane |
| AMD MI50 | 32 Go | 200 à 260 € **ou** 500 à 650 $ ⚠️ | 6 à 8 **ou** 15 à 20 | F6, F14 | prix contradictoires |
| Tesla V100 | 32 Go | 450 à 900 € ⚠️ | 14 à 28 | F6 | Volta : fin de support CUDA (F70) |
| RTX 5060 Ti (neuve, pour comparer) | 16 Go | ≈ 670 € | ≈ 42 | F15 | prix toutes versions confondues |

### Paires d'occasion (prix des deux cartes, hors transport)

| Paire | VRAM totale | Prix d'occasion estimé | € par Go | Faits |
|---|---|---|---|---|
| 2 × RTX 3060 12 Go | 24 Go | 400 à 600 € (2 × 280 = 560 €) | 17 à 25 | F1-F3 |
| 2 × RX 6800 XT 16 Go | 32 Go | 720 à 800 € ⚠️ | 22 à 25 | F9 |
| 2 × RTX 3090 | 48 Go | 1 600 à 2 000 € ⚠️ | 33 à 42 | F4, F5 |
| 2 × Tesla P40 | 48 Go | 460 à 660 € + ventilateurs ⚠️ | 10 à 14 | F6, F13 |
| 2 × MI50 | 64 Go | 400 à 520 € **ou** 1 000 à 1 300 $ ⚠️ | 6 à 20 | F14 |
| **5080 (déjà là) + 1 × RTX 3090** | 40 Go | + 800 à 1 000 € ⚠️ | 33 à 42 (sur la carte ajoutée) | F4, F5 |
| 5080 (déjà là) + 1 × RTX 3060 | 28 Go | + 200 à 300 € | 17 à 25 | F1-F3 |

### B. Multi-GPU en local

| n° | Affirmation | Source (URL + date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| F20 | Dans llama.cpp, `--split-mode` (`-sm`) vaut `none` (une seule carte), `layer` (**défaut** : couches et cache KV répartis, « pipelined »), `row` (poids répartis par lignes, « parallelized ») ou `tensor` (poids et KV répartis, « parallelized, EXPERIMENTAL »). | https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md (lu le 24/10/2026) | | ✅ `tools/server/README.md` et `common/arg.cpp` (master, 24/10) : textes identiques. Nouveau à noter : `--fit` est actif par défaut et ajuste les réglages non fixés pour tenir en mémoire. |
| F21 | `--tensor-split` (`-ts`) : « fraction of the model to offload to each GPU », liste de proportions, par exemple `3,1`. `--main-gpu` (`-mg`) choisit la carte avec `-sm none`, ou celle des résultats intermédiaires et du KV avec `-sm row`. `--device` (`-dev`) liste les cartes à utiliser. | même page | | ✅ même page, textes identiques. |
| F22 | Le backend Vulkan de llama.cpp répartit un modèle sur plusieurs cartes depuis la PR n° 5321, fusionnée le 07/02/2024 ; les cartes se choisissent avec `GGML_VK_VISIBLE_DEVICES` et **les données passent par la RAM système** (jugé « pas rapide » par l'auteur de la PR). | https://github.com/ggml-org/llama.cpp/pull/5321 | | ✅ PR « Basic Vulkan Multi-GPU implementation » (0cc4m), fusionnée le 07/02/2024 : copie par la RAM, `GGML_VK_VISIBLE_DEVICES`. ⚠️ c'était 2024 : aujourd'hui, Vulkan prend **par défaut toutes les cartes dédiées** (code de `ggml-vulkan.cpp`) et la variable ne sert qu'à filtrer ; on peut aussi compiler llama.cpp avec CUDA **et** Vulkan et choisir les cartes avec `--device` (`docs/build.md`). |
| F23 | Mélanger des marques : une discussion de mesures Vulkan liste une machine avec RTX 3090, RX 6800 XT, Radeon Pro VII et Arc A770 ensemble ; l'auteur de la PR F22 disait faire tourner un 70B en q4_k_s sur trois cartes de marques différentes (RTX 3090, Radeon Pro VII, Arc A770). Mesures de 2024, ⚠️ pas de confirmation récente. | https://github.com/ggml-org/llama.cpp/discussions/10879 ; https://github.com/ggml-org/llama.cpp/pull/5321 | | ⚠️ le message du 08/01/2025 (0cc4m, discussion ouverte le 18/12/2024) donne des mesures **carte par carte** (Llama 2 7B Q4_0) pour RTX 3090, RX 6800 XT, Radeon Pro VII et Arc A770, pas un modèle réparti sur les quatre. Le 70B q4_k_s sur trois marques ✅ (PR 5321, février 2024 : 3,34 tok/s). |
| F24 | Ollama : si le modèle tient sur **une** carte, il se charge sur elle ; sinon il est réparti sur toutes les cartes. La FAQ ajoute que sur une seule carte, c'est en général le plus rapide, car il y a moins de transferts sur le bus PCI. | https://docs.ollama.com/faq (lu le 24/10/2026) | | ✅ docs.ollama.com/faq, 24/10 : texte identique. |
| F25 | La variable `OLLAMA_SCHED_SPREAD` pour forcer la répartition sur toutes les cartes n'est **pas** dans la FAQ officielle ; elle est décrite par des sources secondaires, qui préviennent qu'elle ne multiplie pas les tokens/s. ⚠️ | https://knightli.com/2026/04/19/ollama-multiple-gpu-notes/ (19/04/2026) | | ✅ la variable existe dans le code d'Ollama (`envconfig/config.go` : « Always schedule model across all GPUs ») ; toujours absente de la FAQ. ⚠️ « ne multiplie pas les tokens/s » reste une source secondaire. |
| F26 | LM Studio 0.3.14 (27/03/2025) : on active ou désactive chaque carte ; stratégies d'allocation « evenly » et « priority order » (« essaie d'allouer plus sur les cartes listées en premier »). Le mode priorité et la limite « mémoire dédiée » sont marqués **CUDA seulement** ; AMD « en cours ». | https://lmstudio.ai/blog/lmstudio-v0.3.14, 27/03/2025 | | ✅ billet du 27/03/2025 : interrupteur par carte, « evenly » et « priority order » ; « Priority Order Mode » et la limite à la mémoire dédiée « Currently CUDA Only » ; AMD « actively working ». |
| F27 | Un fil Reddit de mai 2026 dit qu'en Vulkan, LM Studio ne propose que la répartition des couches. ⚠️ anecdotique | https://reddit.sentinel-team.org/posts/1t975bx/snapshots/2026-05-15T23%3A40%3A01.25497Z | | ⚠️ non revérifié (anecdotique). |
| F28 | La VRAM s'additionne, la vitesse non. Pour un modèle de 8 B qui tient déjà sur une RTX 3090 : 111,7 tok/s avec 1 carte, 108,1 avec 2, 104,9 avec 4, 101,1 avec 6 (de 3,3 à 9,6 % **plus lent**). Moteur et quantification non précisés. | https://insiderllm.com/guides/multi-gpu-local-ai/, publié le 06/02/2026, mis à jour le 24/09/2026 | | ⚠️ la page ne donne **ni source, ni moteur, ni protocole** (« Benchmarks with an 8B model on RTX 3090s ») : chiffres non sourcés, à ne pas citer. |
| F29 | Même page : sur 2 × RTX 4090, llama.cpp, LLaMA 3 70B Q3_K, **traitement du prompt** : couches 1 287 ; lignes 582 ; tenseur 1 072 (tokens/s). La page conclut que la répartition par couches gagne sur la plupart des PCIe grand public. Elle donne aussi 16 à 18 tok/s pour un 70B Q4 sur 2 × RTX 3090 en couches, mais **sans source** ⚠️. | même page | | ⚠️ chiffres présents mais **sans source** (le seul lien voisin est la PR 19378 sur le mode tensor) ; l'en-tête dit « tok/s » et la légende « prompt processing ». Le 16-18 tok/s est bien sans source. |
| F30 | Cartes de tailles différentes : « la performance est tirée vers la carte la plus lente » ; llama.cpp accepte `--tensor-split` avec des proportions inégales (exemple `24,12`). | même page | | ⚠️ « pulled toward the slower card » est un raisonnement sur une paire 3090 + 3060, pas une mesure. L'exemple `--tensor-split 24,12` ✅ (réglage proportionnel à la VRAM). |
| F31 | PCIe : deux cartes sur une carte mère grand public se partagent souvent 16 lignes en x8/x8 ; certaines cartes mères font x16/x4. La page annonce « 35-40 % de pénalité » pour le parallélisme de tenseur sur la 2e carte en x4 ; un autre guide annonce « jusqu'à 40 % » en répartition par couches avec une carte en x4. ⚠️ deux sources secondaires, aucune mesure primaire : **l'auteur le mesure** (voir fiche). | https://insiderllm.com/guides/multi-gpu-local-ai/ ; https://bestllmfor.com/guide/setup-multi-gpu-llama/ | | ⚠️ insiderllm : « 35-40 % » pour le **parallélisme de tenseur** sur la 2e carte, sans source. bestllmfor dit « you may lose 40% performance with split layer » (pas « jusqu'à »), sans mesure. Les 4 Go/s correspondent au PCIe 3.0 x4 (≈ 3,9 Go/s par sens, calcul). L'auteur mesure. |
| F32 | Mesure publiée (description de vidéo) : répartir Qwen 3.8 27B sur 2 × RTX 5060 Ti 16 Go donne environ 22 tok/s, « environ la moitié d'une seule RTX 3090 ». ⚠️ chaîne à voix de synthèse, sans protocole | https://www.youtube.com/watch?v=YPKYFxpyUlQ (description, 17/10/2026) | | ✅ description du 17/10/2026 : « about 22 tok/s, around half a single RTX 3090 ». ⚠️ contexte non précisé. |
| F33 | « Deux cartes de 24 Go mettent bien leur mémoire en commun, pour la capacité : llama.cpp répartit les couches ; la vitesse ne double pas. » | https://www.youtube.com/watch?v=haSZQNa9Qs8 (description, 18/10/2026) | | ✅ description du 18/10/2026 : « Yes for capacity, since llama.cpp splits the layers across both cards; the speed does not double ». |
| F34 | Mémoire du contexte : Qwen 3.8 27B demande environ 20 Go au total à 32 K de contexte et 26 Go à 128 K (cache KV : 2,3 Go à 32 K, 8,7 Go à 128 K) ; en Q8 (29 Go) avec 262 K de contexte (≈ 16 Go de KV), environ 45 Go. Llama 3.3 70B en Q4_K_M (42,5 Go) laisse place à environ 15 K de tokens sur 48 Go. Estimations publiées. | https://www.youtube.com/watch?v=3fKTcu69ZvE (10/10/2026) ; https://www.youtube.com/watch?v=haSZQNa9Qs8 (18/10/2026) | | ✅ les deux descriptions donnent ces chiffres (20 Go à 32 K, 26 Go à 128 K, KV 2,3 → 8,7 Go ; Q8 29 Go + 262 K ≈ 16 Go ≈ 45 Go ; 70B Q4_K_M 42,5 Go, ≈ 15 K tokens). ⚠️ estimations publiées. |
| F35 | Pour mesurer une seule carte dans une machine qui en a deux, le fil de mesures de llama.cpp demande `-sm none -mg <n°>` ; un résultat à 4 × RTX 3090 sur PCIe Gen 3 x16 en `-sm tensor` (Qwen 35B MoE) est posté le 07/09/2026. Utile comme protocole. | https://github.com/ggml-org/llama.cpp/discussions/15013 | | ✅ discussion « Performance of llama.cpp on Nvidia CUDA » : « run the test on a single GPU using `-sm none -mg YOUR_GPU_NUMBER` » ; message de nd4w33d du 07/09/2026 : 4 × RTX 3090, « PCIe GEN 3@16x », Qwen 3.6 35B-A3B, `-sm tensor -ts 1/1/1/1`. |

### C. Ce qui tient selon la VRAM (tailles réelles des fichiers)

Tailles en Go décimaux, lues sur Hugging Face le 24/10/2026. Les dépôts sont ceux de `modeles-5080.md` (ISTA-DASLab, Unsloth, LiquidAI), plus Bartowski pour Llama 3.3 70B.

| n° | Fichier | Taille | Dépôt |
|---|---|---|---|
| F40 | Qwen3.8-27B-UD-IQ4_XS | 14,25 Go | https://huggingface.co/unsloth/Qwen3.8-27B-GGUF |
| F41 | Qwen3.8-27B-UD-Q4_K_S / Q4_K_M | 15,36 / 16,46 Go | idem |
| F42 | Qwen3.8-27B-UD-Q5_K_M / Q6_K / Q8_0 | 19,77 / 21,98 / 29,05 Go | idem |
| F43 | Qwen3.8-27B ISTA IQ3_S (+ MTP) | 11,77 (12,12) Go | https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF |
| F44 | Qwen3.6-35B-A3B UD-IQ4_XS / UD-Q4_K_M / UD-Q5_K_M | 18,21 / 22,66 / 27,09 Go | https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF |
| F45 | Qwen3.6-35B-A3B UD-Q6_K / UD-Q8_K_XL / Q8_0 | 30,01 / 39,10 / 37,80 Go | idem |
| F46 | Nemotron 3.5 Bolt 74B-A9B UD-IQ2_XXS / UD-IQ3_XXS / UD-Q2_K_XL / UD-Q3_K_XL | 22,02 / 31,56 / 28,75 / 39,03 Go | https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF |
| F47 | Gemma 4 12B Q6_K / Q8_0 / BF16 | 9,79 / 12,67 / 23,83 Go | https://huggingface.co/unsloth/gemma-4-12b-it-GGUF |
| F48 | LFM2.5-24B-A2B QAD-Q4_0 / Q4_K_M / Q6_K / Q8_0 | 13,58 / 14,53 / 19,69 / 25,49 Go | https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF |
| F49 | Llama 3.3 70B Instruct IQ3_M / Q3_K_M / IQ4_XS / Q4_K_M | 31,94 / 34,27 / 37,90 / 42,52 Go ; Q5_K_M : 49,95 Go (2 fichiers) | https://huggingface.co/bartowski/Llama-3.3-70B-Instruct-GGUF |
| F50 | gpt-oss-20b (F16, natif) / Q8_0 | 13,79 / 12,11 Go | https://huggingface.co/unsloth/gpt-oss-20b-GGUF |
| F51 | gpt-oss-120b Q4_K_M (2 fichiers) / F16 | 62,77 (49,63 + 13,14) / 65,37 Go | https://huggingface.co/unsloth/gpt-oss-120b-GGUF |
| F52 | Qwen3.8-Flash-Next UD-IQ3_XXS / UD-IQ4_XS | ≈ 81,96 / ≈ 93,69 Go (3 fichiers) | https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF |

**Méthode** (la même que `modeles-5080.md` : on retire environ 1 Go de tampons CUDA par carte, estimation) :

| VRAM totale | = en Go décimaux | Place pour poids + cache (≈) | Exemple |
|---|---|---|---|
| 24 Go | 25,8 | ≈ 23,8 | 2 × RTX 3060 12 Go, ou 1 × RTX 3090 |
| 32 Go | 34,4 | ≈ 32,4 | 2 × RX 6800 XT 16 Go |
| 40 Go | 42,9 | ≈ 40,9 | 5080 16 Go + RTX 3090 24 Go |
| 48 Go | 51,5 | ≈ 49,5 | 2 × RTX 3090 |

Avec le cache KV de Qwen3.8-27B (2,3 Go à 32 K, F34). ✅ = tient avec 32 K de contexte ; ⚠️ = tient de justesse ou avec peu de contexte ; ❌ = ne tient pas en VRAM seule.

| Modèle (quantification, taille) | 24 Go | 32 Go | 40 Go | 48 Go |
|---|---|---|---|---|
| Qwen3.8-27B Q4_K_M (16,46) | ✅ | ✅ | ✅ | ✅ |
| Qwen3.8-27B Q5_K_M (19,77) | ✅ (≈ 22,1) | ✅ | ✅ | ✅ |
| Qwen3.8-27B Q6_K (21,98) | ⚠️ (≈ 24,3 > 23,8) | ✅ | ✅ | ✅ |
| Qwen3.8-27B Q8_0 (29,05) | ❌ | ⚠️ (≈ 31,4) | ✅ (128 K : ≈ 37,8) | ✅ (262 K : ≈ 45) |
| Qwen3.6-35B-A3B Q4_K_M (22,66) | ⚠️ | ✅ | ✅ | ✅ |
| Qwen3.6-35B-A3B Q6_K (30,01) | ❌ | ⚠️ | ✅ | ✅ |
| Qwen3.6-35B-A3B Q8_K_XL (39,10) | ❌ | ❌ | ⚠️ | ✅ |
| Nemotron 3.5 Bolt UD-IQ2_XXS (22,02) | ⚠️ | ✅ | ✅ | ✅ |
| Nemotron 3.5 Bolt UD-IQ3_XXS (31,56) | ❌ | ⚠️ | ✅ | ✅ |
| Nemotron 3.5 Bolt UD-Q3_K_XL (39,03) | ❌ | ❌ | ⚠️ | ✅ |
| Gemma 4 12B Q8_0 (12,67) | ✅ | ✅ | ✅ | ✅ |
| LFM2.5-24B-A2B Q6_K (19,69) | ✅ | ✅ | ✅ | ✅ |
| gpt-oss-20b (13,79) | ✅ | ✅ | ✅ | ✅ |
| Llama 3.3 70B IQ3_M (31,94) | ❌ | ⚠️ (sans contexte) | ✅ | ✅ |
| Llama 3.3 70B Q4_K_M (42,52) | ❌ | ❌ | ❌ | ✅ (≈ 15 K de contexte, F34) |
| Llama 3.3 70B Q5_K_M (49,95) | ❌ | ❌ | ❌ | ❌ |
| gpt-oss-120b Q4_K_M (62,77) | ❌ | ❌ | ❌ | ❌ en VRAM ; ≈ 13 Go d'experts en RAM : ⚠️ à essayer |
| Qwen3.8-Flash-Next IQ3_XXS (≈ 82) | ❌ | ❌ | ❌ | ❌ : plus de 32 Go à poser en RAM, or ta machine en a 32 (voir `modeles-5080.md`, 1.2) |

Le tableau ne dit **rien** sur la vitesse. Les modèles de la ligne « 70B dense » qui tiennent dans 48 Go sont le seul cas où 2 cartes font vraiment gagner un modèle que la 5080 ne pourra jamais lancer.

### D. La machine de l'auteur

| n° | Affirmation | Source (URL + date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| F60 | Gigabyte B850M AORUS ELITE WIFI6E ICE : **1 slot PCI Express x16 (PCIEX16) relié au CPU**, en PCIe 5.0 x16 avec les Ryzen 9000/7000, « qui ne peut accueillir qu'une carte graphique ou un SSD NVMe » ; **1 slot x16 relié au chipset, en PCIe 3.0 et en x4 (PCIEX4)** ; 2 connecteurs M.2 reliés au CPU. Texte repris de la fiche Gigabyte par un revendeur. ⚠️ la page Gigabyte renvoie 403 ; **vérifie dans le manuel** | https://online.westech.sk/gigabyte-aorus-b850m-elite-wifi6e-ice-amd-b850-am5-4xddr5-matx_d175806.html (vu le 24/10/2026) ; fiche officielle : https://www.gigabyte.com/Motherboard/B850M-AORUS-ELITE-WIFI6E-ICE-rev-1x/sp | | ✅ **manuel Gigabyte** (rév. 1003, commun à la WIFI6E ICE et à la WIFI6E), spécifications p. 8-9 et schéma p. 5 : PCIEX16 relié au CPU (PCIe 5.0 x16 avec les Ryzen 9000/7000) ; **PCIEX4 relié au chipset, PCIe 3.0, x4 dans un connecteur x16** ; M2A_CPU et M2B_CPU tous deux reliés au CPU, donc aucun partage avec PCIEX4. Schéma p. 4 : PCIEX16 en haut, PCIEX4 en **dernière position**, environ 3 positions plus bas (≈ 61 mm, mesuré sur le schéma ⚠️). Format 24,4 × 24,4 cm. |
| F61 | Corsair RM1000e : 1000 W, +12 V en rail unique de 62,5 A ; **câbles** : 1 × 12V-2x6, 1 × 12V-2x6 vers 2 × 8 broches PCIe, plus des câbles PCIe 8 broches. **Le nombre de 8 broches change selon la source** : 4 (page Corsair, lecture automatique ⚠️) ou 3 (Memory Express et Best Buy). | https://www.corsair.com/us/en/p/psu/cp-9020297-na/rm1000e-fully-modular-low-noise-atx-power-supply-atx-3-1-compliant-cp-9020297-na ; https://www.memoryexpress.com/Products/MX00132467 (vus le 24/10/2026) | | ⚠️ page Corsair CP-9020297 (RM1000e **2025, ATX 3.1**, RPS0217) relue dans le code de la page : 1 câble 12V-2x6 ; 1 câble « 12V-2x6 to Dual 8-Pin (6+2) » ; 2 câbles PCIe 8 broches simples ; 2 câbles EPS 4+4. Donc **4 connecteurs 8 broches PCIe** + 1 12V-2x6 (Hardware Busters : « 4x PCIe 6+2 pin (3x cables), 1x 12+4 pin (600W) », 9 prises sur le bloc **dont une seule 12V-2x6**). Le nom du câble double laisse penser qu'il se branche sur cette prise 12V-2x6 : si c'est le cas, avec la 5080 sur le câble natif, il ne reste que **2 × 8 broches**. À vérifier sur ton bloc (étiquette, photo du panneau). « 3 » chez Memory Express et Best Buy : non revérifié. |
| F62 | NVIDIA RTX 5080 : puissance totale de la carte 360 W (Founders Edition, les modèles partenaires peuvent varier) ; alimentation conseillée **850 W minimum** ; connexion : 3 câbles PCIe 8 broches via l'adaptateur fourni **ou** 1 câble PCIe Gen 5 de 450 W ou plus. | https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/ (lu le 24/10/2026) | | ✅ page NVIDIA : 360 W, 850 W (« based on a PC configured with a Ryzen 9 9950X »), « 3x PCIe 8-pin cables (adapter in box) OR 1x 450 W or greater PCIe Gen 5 cable ». La page Inno3D de la X3 OC dit la même chose. |
| F63 | Inno3D RTX 5080 X3 OC : 300 mm de long, 120 mm de haut, 50 mm d'épaisseur, **2,5 slots** (un revendeur la donne en 2 slots et 41 mm : ⚠️ vérifie sur la carte). | https://www.geektopia.es/es/product/inno3d/geforce-rtx-5080-x3-oc/ ; https://shop.inception.co.uk/inno3d-gaming-oc-geforce-rtx-5080-x3-nvidia-16-gb-gddr7-g50803-16d7x-17603930.html | | ✅ **page Inno3D officielle** : la X3 **OC** fait 300 × 120 × 50 mm, **2,5 slots** ; la X3 sans OC fait 300 × 116 × 41 mm, 2 slots. Le revendeur décrivait la version sans OC : vérifie le nom exact sur ta carte. |
| F64 | RTX 3090 : 24 Go GDDR6X, 350 W, 936 Go/s (NVIDIA). Repris d'une liste de sources de vidéo. ⚠️ | https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090/ (cité par https://www.youtube.com/watch?v=ceSXJw1rmDc, 11/10/2026) | | ✅ page NVIDIA : 24 Go GDDR6X, bus 384 bits, 350 W, 750 W conseillés, « 2x PCIe 8-pin (adapter to 1x 12-pin included) » (Founders Edition), **3 slots**, 313 × 138 mm. ⚠️ le 936 Go/s n'est pas sur la page lue. |
| F65 | Consommation et connecteurs de la RTX 3060 12 Go et de la RX 6800 XT : **non relevés** ⚠️. À prendre sur les fiches NVIDIA et AMD avant le script. | (à compléter) | | ✅ complété : RTX 3060 12 Go : 170 W, 550 W conseillés, 192 bits (page NVIDIA ; connecteur selon le modèle de la marque) ; **il existe une 3060 à 8 Go** (128 bits). RX 6800 XT : 300 W, 750 W minimum, 16 Go, 512 Go/s, 2,5 slots (page AMD). |

**Ce que ça donne pour la machine** (déductions, pas des mesures) :

- **Une 2e carte sur le slot x4** : le seul slot libre est un x4 en PCIe 3.0 passant par le chipset (F60, ✅ manuel), soit environ 3,9 Go/s par sens (calcul). Avec la répartition par couches, seuls les résultats intermédiaires passent d'une carte à l'autre ; mais le chargement du modèle et le traitement du prompt peuvent en souffrir (F31). **À mesurer.**
- **Encombrement** (corrigé le 24/10, 2e vérif) : la 5080 X3 OC fait 2,5 slots, 50 mm (F63). Le slot x4 est en **dernière** position de la carte mère, environ 3 positions sous le x16 (F60, schéma du manuel). Donc **toute carte de 2 slots ou plus mise dans le x4 dépasse sous la carte mère** : il faut un boîtier à 5 emplacements pour une carte de 2 slots (une 3060), 6 pour une carte de 3 slots (une 3090 Founders Edition). Entre les ventilateurs de la 5080 et la 2e carte, il reste environ 1 cm (estimation sur le schéma). ⚠️ **mesure ton boîtier** (nombre d'emplacements, espace sous la carte mère).
- **Alimentation** (corrigé le 24/10, 2e vérif) : la RM1000e 2025 a 4 connecteurs 8 broches PCIe et un câble 12V-2x6, mais **une seule prise 12V-2x6 sur le bloc**, que le câble double « 12V-2x6 to Dual 8-Pin » semble utiliser aussi (F61). Si la 5080 prend le câble natif, il reste peut-être seulement **2 × 8 broches** : assez pour une 3090 Founders Edition (2 × 8 broches, F64) ou une 3060, pas pour une 3090 de marque à trois 8 broches. 360 W (F62) + 350 W (F64) = 710 W pour les deux cartes, sur 1000 W, avec le processeur en plus : **ça passe sur le papier** (estimation, sans les pics de consommation). ⚠️ vérifie ta référence (étiquette) et le panneau du bloc.
- **Cartes sans sortie vidéo** (P40, MI50) : la carte mère a un DisplayPort à l'arrière et une prise HDMI avant (F_HDMI) pour la puce graphique du processeur (manuel, p. 8) ; et de toute façon l'écran reste branché sur la 5080. ✅
- **P40 et prise EPS** (déduction ⚠️) : la carte mère n'a qu'une prise processeur 8 broches (ATX_12V, schéma du manuel) et le bloc fournit 2 câbles EPS (F61) : un câble EPS reste libre. Vérifie le brochage avant de le brancher sur une P40.
- **Second PC** : seule voie sûre pour 2 × 3090 (48 Go) ou des cartes de datacentre. Les 32 Go de RAM de la machine actuelle (déjà trop justes pour Flash-Next) pèsent peu si tout tient en VRAM.

### E. Risques de l'occasion

| n° | Affirmation | Source (URL + date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| F70 | NVIDIA : la branche de pilotes 580 est la **dernière** à prendre en charge Maxwell, Pascal et Volta (donc P40, P100, V100). CUDA 13.0 a retiré la compilation hors ligne et les bibliothèques pour ces architectures (les notes de version de cuFFT et cuSPARSE le confirment). La version actuelle est CUDA 13.4 Update 2. Les P40 et V100 fonctionnent donc avec CUDA 12.x et un pilote 580, pas au-delà. | https://pcserverandparts.com/news/used-graphics-card-buying-guide-2026/ (publié 09/09/2026, modifié 20/10/2026) ; https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html (lu le 24/10/2026) ; https://www.phoronix.com/news/NVIDIA-580-Linux-Driver-Last-HW | | ✅ notes de CUDA 13.0, « Deprecated Architectures » : « Offline compilation and library support for these architectures have been removed in CUDA Toolkit 13.0 » (cuFFT, cuSPARSE aussi). Notes actuelles : « CUDA Toolkit 13.4 Update 2 » ✅. 580 dernière branche : citation NVIDIA reprise par Phoronix (01/07/2025) ✅. Nuance : R580 est la branche de CUDA 13.0 ; ce qui manque, c'est la compilation : pour P40 et V100, llama.cpp se compile avec un toolkit CUDA 12.x. Mises à jour de sécurité jusqu'en octobre 2028 (selon pcserverandparts ⚠️). |
| F71 | Tesla P40 : refroidissement passif (aucun ventilateur), alimentation par un 8 broches **EPS** (pas PCIe), 250 W, **aucune sortie vidéo**, FP16 à 1/64 du FP32, 347 Go/s (un tiers d'une RTX 3090). Sans ventilateur, elle chute de 16 à 3-4 tok/s (étranglement thermique). Un kit ventilateur coûte 25 à 35 $. | https://insiderllm.com/guides/used-tesla-p40-local-ai/ (23/02/2026, maj 24/09/2026) | | ✅ insiderllm (23/02/2026, maj 24/09/2026) : passive, 8 broches EPS (adaptateur 2 × PCIe 8 broches vers EPS : 8 à 15 $), 250 W (750 W conseillés), aucune sortie, FP16 à 1/64, 347 Go/s, 16 → 3-4 tok/s sans ventilation, kit 25 à 35 $. |
| F72 | AMD MI50 (gfx906) : absente de la matrice de prise en charge de ROCm 7.14 (août 2026) ; passage en mode maintenance dès ROCm 6.0 ; refroidissement passif (« suppose un tunnel d'air ») ; firmware d'origine **sans sortie vidéo** (le contournement, flasher le BIOS d'une Radeon Pro VII, peut briquer la carte). La voie recommandée est le backend Vulkan de llama.cpp. | https://localaimaster.com/blog/amd-mi50-local-llm (06/09/2026) ; https://www.guru3d.com/story/discontinuation-for-amds-vega-graphics-architecture-in-rocm-gpu-programming-software-stack/ | | ⚠️ la matrice officielle lue le 24/10 est « ROCm 10.1.0 compatibility matrix » (26/08/2026) : gfx906 (MI50) **absent** ✅ ; le « 7.14 » vient de localaimaster. Passif, sortie vidéo, flash risqué, Vulkan conseillé : ✅ localaimaster (06/09/2026). Mode maintenance dès ROCm 6.0 : guru3d non relu ⚠️. MI50 : 2 × 8 broches **PCIe**, 300 W (fiche AMD, vue via un moteur de recherche ⚠️). Au passage : la **RX 6800 XT (gfx1030) n'est pas dans la matrice** non plus (seules la W6800 et la V620, même puce). |
| F73 | Cartes de minage : test de Linus Tech Tips sur 19 cartes d'occasion, « presque toutes » ont passé ; deux défauts relevés (VRAM défaillante à plus de 100 °C sur une RTX 3060 ; une RX 5700 XT 3 % plus lente). Conseil : n'acheter qu'avec droit de retour. RTX 3090 : la mémoire GDDR6X est sur les deux faces du PCB ; une température de jonction mémoire très haute, des ventilateurs qui montent vite et des plantages en charge longue sont des signaux d'alerte ; remplacer les pads est possible mais pas toujours efficace. Source de la 2e partie : un vendeur de waterblocks. ⚠️ | https://pcserverandparts.com/news/used-graphics-card-buying-guide-2026/ ; https://www.formulamod.net/blogs/new/used-rtx-3090-ai-cooling-water-block-checklist | | ⚠️ le test LTT date de **février 2023** (rapporté par Tom's Hardware le 05/02/2023, cité par pcserverandparts) : 19 cartes, « presque toutes » passent (seuil : 3 % sous la référence) ; une RTX 3060 Gigabyte à VRAM défaillante au-delà de 100 °C ✅ ; une RX 5700 XT 3 % plus lente dans Kombustor mais normale en jeu. Partie RTX 3090 (vendeur de waterblocks) : non relue ⚠️. |
| F74 | **Garantie légale de conformité** (vendeur professionnel, acheteur non professionnel) : **2 ans** à partir de la délivrance du bien ; réparation ou remplacement gratuits sous 30 jours, sinon réduction du prix ou remboursement ; les défauts sont présumés exister à la vente pendant 12 mois (au-delà, c'est à l'acheteur de prouver). **Exclus : les biens neufs ou d'occasion vendus par un particulier.** | https://www.service-public.gouv.fr/particuliers/vosdroits/F11094 (« Vérifié le 17 août 2026 ») | | ✅ service-public F11094 (« Vérifié le 17 août 2026 ») et art. L217-3 : « qui apparaissent dans un délai de deux ans à compter de celle-ci » ; occasion incluse ; 30 jours ; exclusion des ventes par un particulier. ⚠️ la fiche range le reconditionné tantôt avec le neuf (24 mois), tantôt avec l'occasion. |
| F75 | Pour un bien d'**occasion**, la présomption d'antériorité est de **12 mois** (6 avant la réforme du 1er janvier 2022), contre 24 mois pour le neuf ; la prescription est de 2 ans à compter de la délivrance, neuf ou occasion (fiche DGCCRF reprise par l'UFC). Les articles à ouvrir sur Légifrance : L217-3 et suivants (dont L217-7 et L217-12) du Code de la consommation. ⚠️ je n'ai pas pu lire Légifrance : **vérifie qu'un vendeur professionnel ne peut pas ramener la durée à moins de 2 ans pour de l'occasion** | https://www.inc-conso.fr/sites/default/files/pdf/tableau-economie-circulaire-12-2023.pdf (déc. 2023) ; DGCCRF, « Les garanties légales », oct. 2023 | | ✅ art. L217-7 : « Pour les biens d'occasion, ce délai est fixé à douze mois » (ordonnance 2021-1247). **Le vendeur pro ne peut pas réduire les 2 ans** : L217-3 ne prévoit aucune exception pour l'occasion, et L219-1 dit « Les dispositions du présent titre sont d'ordre public » ; service-public : 2 ans « quel que soit le type de bien (neuf, reconditionné ou d'occasion) ». ❌ L217-12 n'est pas la prescription : c'est le refus de mise en conformité pour coût disproportionné. Texte lu sur codes.droit.org (données de l'API Légifrance, édition du 10/10/2026). |
| F76 | **Vente entre particuliers** : pas de garantie de conformité (F74) ; reste la **garantie des vices cachés** (Code civil, art. 1641 et suivants), action dans les **2 ans à compter de la découverte du vice** (art. 1648, jugé prescription par la chambre mixte de la Cour de cassation le 21/07/2023). Une clause « sans garantie » est écrite dans le contrat et ne protège pas un vendeur qui connaissait le défaut. L'acheteur doit prouver le vice. ⚠️ sources secondaires (Lextenso, notaires) : Légifrance et la fiche service-public n'ont pas pu être lus | https://www.labase-lextenso.fr/l-essentiel-droit-des-contrats/2023-n8/le-regime-de-la-prescription-de-l-article-1648-du-code-civil-DCO201r7 | | ✅ C. civ. art. 1641 ; art. 1648 : « dans un délai de deux ans à compter de la découverte du vice » ; art. 1643 : la clause de non-garantie ne vaut que si le vendeur ignorait le vice ; Cass. ch. mixte 21/07/2023 n° 20-10.763 listée sous l'art. 1648. Service-public F11007 (vérifié le 25/11/2025) : vaut aussi entre particuliers, preuve à l'acheteur, dans la limite de 20 ans après la vente. L217-30 : la garantie des vices cachés s'ajoute à la garantie de conformité. |
| F77 | **Back Market** : garantie commerciale de 12 mois **en plus** des garanties légales (communiqué avec Bouygues Telecom, oct. 2025) ; place de marché, ce sont les vendeurs qui répondent des produits ; UFC-Que Choisir a porté plainte en 2022 en estimant que la loi impose 24 mois, y compris pour le reconditionné. **Aucune fiche de RTX 3090 sur Back Market trouvée** ⚠️. | https://www.bouygues.com/app/uploads/2025/10/cp-back-market-x-bytel_octobre-2025.pdf ; https://next.ink/brief-article/pratiques-commerciales-trompeuses-lufc-que-choisir-porte-plainte-contre-back-market-qui-se-defend/ | | ⚠️ plainte confirmée (next.ink, 17/06/2022) : l'UFC dit que la garantie légale de 24 mois s'impose aussi au reconditionné ; Back Market répond que ses 12 mois s'ajoutent aux garanties légales. Communiqué Bouygues : 403, non relu. |
| F78 | Grosbill propose des cartes graphiques « seconde vie » (dont une RTX 3090 24 Go, état « satisfaisant »), avec « retours gratuits 14 jours » ; prix et durée de garantie non lus ⚠️. | https://www.grosbill.com/carte-graphique/generique-carte-graphique-rtx-3090-24gb-seconde-vie-etat-satisfaisant-142434.aspx (vu le 24/10/2026) | | ⚠️ le 24/10, l'adresse Grosbill renvoie vers la catégorie « cartes graphiques » : l'annonce RTX 3090 « seconde vie » **n'existe plus**. |
| F79 | **Droit de rétractation** de 14 jours pour un achat à distance chez un professionnel : général, ⚠️ non confirmé dans cette recherche (Code de la consommation, L221-18) ; ne vaut pas pour un particulier. | à vérifier sur https://www.service-public.gouv.fr | | ✅ art. L221-18 : 14 jours pour un contrat à distance ou hors établissement, à compter de la **réception** du bien ; service-public F10485 (vérifié le 01/01/2026) : prolongé jusqu'à 12 mois si le vendeur ne t'a pas informé ; vise les achats chez un professionnel (rien entre particuliers, rien en magasin). |

**Tests à faire à la réception** (conseils de bon sens appuyés sur F71-F73, ⚠️ à valider) : GPU-Z (VRAM, bus, version du BIOS) ; 30 minutes de charge avec `llama-bench` en lisant la **température de la mémoire** (HWiNFO) ; écouter les ventilateurs ; ouvrir la photo du dos de la carte (traces de pads) ; refaire le test sur chaque carte seule avec `-sm none -mg <n°>` (F35). Filme le déballage. Le délai de retour (14 jours chez un professionnel, F78, F79 ⚠️) est plus court que la garantie : teste tout dans cette fenêtre.

## Pour les conseils d'achat d'occasion

À reprendre dans le guide d'achat d'avant le Black Friday 2026 (dernière semaine de novembre) et dans « Louer, acheter ou s'abonner » (janvier 2027). **Les prix d'occasion sont à relever par toi le jour du script** (consigne du 24/10) ; les « € par Go » ne sont qu'un ordre de grandeur ⚠️. Statut de la 2e vérif entre crochets.

1. La RTX 3060 12 Go est la carte d'occasion la moins chère pour de la CUDA avec 12 Go : [PRIX D'OCCASION À RELEVER], de l'ordre de 20 à 25 € par Go ⚠️. Prends bien la **12 Go** : il existe une 3060 à 8 Go (F1, F65). [⚠️ prix à relever ; 12/8 Go ✅]
2. La RTX 3090 reste la référence à 24 Go, et la seule des deux à garder CUDA sur une seule carte : [PRIX D'OCCASION À RELEVER] en France, à ne pas confondre avec les prix en dollars des vidéos américaines (F7). [⚠️ prix à relever]
3. La RX 6800 XT (16 Go) donne le Go le moins cher des grandes cartes de jeu, de l'ordre de 22 à 25 € par Go ⚠️, mais sans CUDA ; et ROCm ne la prend pas en charge officiellement (seule la W6800, même puce, F72) : la voie sûre est Vulkan (F22). [⚠️ prix à relever ; ROCm et Vulkan ✅]
4. Les cartes de datacentre sont tentantes (de l'ordre de 6 à 14 € par Go pour la P40 et la MI50 ⚠️, plus pour la V100), mais elles n'ont ni ventilateur ni sortie vidéo, la P40 se branche sur une prise 8 broches **EPS** (pas PCIe), la P40 et la V100 n'ont plus de CUDA 13, et la MI50 n'a plus ROCm (F70-F72) : ne les prends pas comme première carte. [⚠️ prix à relever ; le reste ✅]
5. Deux cartes additionnent la VRAM, pas la vitesse : en mode par défaut, le modèle est coupé en tranches de couches et, pour une seule conversation, les cartes travaillent chacune leur tour (F20, F33). [✅]
6. Chez un vendeur professionnel, même d'occasion, tu as 2 ans de garantie légale de conformité, qu'il ne peut pas réduire, et un défaut présumé exister à la vente pendant 12 mois (F74, F75) ; entre particuliers, il ne te reste que les vices cachés, à prouver, dans les 2 ans après leur découverte (F76). [✅ Code de la consommation L217-3, L217-7, L219-1 ; Code civil 1641, 1648]
7. Achetée à distance chez un pro, tu as 14 jours après la réception pour te rétracter : teste la carte dans ce délai (30 minutes de charge, température de la mémoire, surtout sur une RTX 3090) (F73, F79). [✅ délai ; ⚠️ tests = conseils de bon sens]
8. Vérifie ta carte mère et ton boîtier avant d'acheter : sur beaucoup de micro-ATX, dont la tienne, le 2e slot est un PCIe 3.0 x4 relié au chipset, tout en bas ; une carte de 2 slots y dépasse sous la carte mère et demande un boîtier à 5 emplacements (F60). Ce que coûte le x4 en vitesse, tu le mesures (F31). [✅ slot ; ⚠️ effet sur la vitesse à mesurer]
9. Les prix des cartes **neuves** montent en France (+5,3 % en 30 jours et +30,8 % en 3 mois au 24/10, F18) : relève les prix d'occasion la veille du script, pas en octobre. [⚠️ indice du neuf, qui bouge chaque jour]
10. Si tu n'as besoin que d'un modèle de 27 B en 4 bits, 24 Go suffisent (F41, F42) ; le deuxième achat ne devient utile qu'au-delà (70 B en Q4_K_M = 42,5 Go, soit 48 Go, F49). [✅ tailles Hugging Face]

## 2e vérification (24/10)

Faite en repartant des sources primaires, sans vidIQ. **Les prix d'occasion n'ont pas été revérifiés** (consigne du 24/10) : F1-F14 et F16 sont marqués « ⚠️ à relever par l'auteur », et la fiche et les conseils portent un crochet [PRIX D'OCCASION À RELEVER].

**Sources primaires lues** : Code de la consommation et Code civil (codes.droit.org, PDF générés depuis l'API Légifrance, éditions des 10/10 et 18/10/2026 ; Légifrance renvoie 403) ; service-public F11094, F11007, F10485 ; manuel Gigabyte `mb_manual_b850m-ae-wf6e-ice_1003_e.pdf` (download.gigabyte.com) ; page Corsair CP-9020297 (code de la page) et test Hardware Busters ; pages NVIDIA (RTX 5080, 3090, 3060), AMD (RX 6800 XT), Inno3D (5080 X3 OC et X3) ; notes de CUDA 13.0 et 13.4 Update 2 ; matrice ROCm ; `README.md`, `arg.cpp`, `build.md` et `ggml-vulkan.cpp` de llama.cpp, PR 5321, discussions 10879 et 15013 ; FAQ et `envconfig/config.go` d'Ollama ; billet LM Studio 0.3.14 ; API Hugging Face (tailles).

**Décompte de la colonne « 2e vérif »** (50 faits) : 23 ✅, 27 ⚠️ (dont 15 prix « à relever »), 0 fait entièrement faux ; une erreur ❌ dans F75 (l'article L217-12).

**Corrections**

1. **F75** : L217-12 n'est pas la prescription (c'est le refus de mise en conformité pour coût disproportionné) ❌. Et ce que la 1re vérif demandait est confirmé : un vendeur pro **ne peut pas** réduire les 2 ans pour de l'occasion (L217-3 sans exception, L219-1 « d'ordre public »).
2. **F61, alimentation** : 4 connecteurs 8 broches PCIe (pas 3), mais une seule prise 12V-2x6 sur le bloc ; avec la 5080 sur le câble natif, il ne resterait que 2 × 8 broches si le câble double utilise cette prise. Texte « Ce que ça donne pour la machine », fiche (point 3, budget) corrigés.
3. **F60, encombrement** : le slot x4 est en dernière position ; **une carte de 2 slots** y dépasse déjà sous la carte mère (5 emplacements nécessaires), pas seulement la 3090. Corrigé dans la machine, le conseil 8 et la fiche.
4. **F63** : le « 2 slots, 41 mm » du revendeur est la X3 sans OC ; la X3 OC fait bien 2,5 slots, 50 mm.
5. **F18** : +5,3 % / +30,8 % au 24/10 (et non +4,1 / +25,5), et c'est un indice de cartes **neuves**. Corrigé dans le conseil 9 et la fiche (budget).
6. **F22** : depuis 2024, Vulkan prend toutes les cartes par défaut, et llama.cpp peut combiner CUDA et Vulkan (`--device`) : utile pour le test 5 (5080 + RX 6800 XT).
7. **F23** : les mesures du 08/01/2025 sont carte par carte, pas un modèle réparti sur les quatre.
8. **F28, F29, F31** : chiffres sans source dans les guides ; F31 de bestllmfor dit « may lose 40 % » en couches, insiderllm « 35-40 % » en tenseur.
9. **F72** : matrice ROCm 10.1.0 (26/08/2026) ; la RX 6800 XT n'y est pas non plus. Conseil 3 corrigé (« Vulkan ou ROCm » → Vulkan).
10. **Conseil 4** : seule la P40 est confirmée en EPS (la MI50 prend 2 × 8 broches PCIe) ; les 6-14 € par Go ne valent que pour la P40 et la MI50, pas la V100 (14-28).
11. **Conseil 5** : « une seule carte travaille à la fois » précisé : en mode par couches, pour une seule conversation.
12. **Conseil 7** : le délai de 14 jours est un droit de rétractation pour un achat à distance chez un pro, compté à partir de la réception (L221-18).
13. **F65** complété (3060 : 170 W, 550 W ; RX 6800 XT : 300 W, 750 W, 2,5 slots) ; il existe une 3060 à 8 Go (conseil 1).
14. **F73** : le test LTT date de février 2023.
15. **F78** : l'annonce Grosbill RTX 3090 « seconde vie » n'existe plus.
16. **F25** : `OLLAMA_SCHED_SPREAD` confirmé dans le code d'Ollama.
17. **Section C** : tailles revérifiées par l'API Hugging Face pour F40-F46 et F49 (Qwen3.8-27B : 14,25 / 16,46 / 19,77 / 21,98 / 29,05 Go ; ISTA IQ3_S 11,77 et 12,12 Go ; Qwen3.6-35B-A3B : 18,21 / 22,66 / 27,09 / 30,01 / 37,80 / 39,10 Go ; Nemotron Bolt : 22,02 / 31,56 / 39,03 Go ; Llama 3.3 70B : 31,94 / 34,27 / 37,90 / 42,52 Go et 39,99 + 9,96 = 49,95 Go) : tous ✅. Conversions Gio → Go (25,8 / 34,4 / 42,9 / 51,5) ✅. F47, F48, F50-F52 non revérifiés.
18. **Fiche** : le nom de la vidéo #1 est désormais « Abonnement ou IA locale ? #1 » (renommée le 24/10) ; « Claude ou mon PC ? #1 » corrigé.
