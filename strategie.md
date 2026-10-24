# Stratégie Technovore v4 : le génie caché de la tech

> Version 4 du 21/10/2026. Elle garde le positionnement de la v3 (11/10) et change le rythme : une vidéo longue chaque lundi, plus de Shorts, un plan sur 6 mois, et un radar à chaque sortie.
> Sources : vidIQ (vidéos qui dépassent la moyenne de leur chaîne, en anglais et en français), tes repérages (Uber, God's Eye, REA, Red Stapler, Waze, WhatsApp), les âges de ton audience, et les études [Kai](etudes/kai.md) et [Morgans Code](etudes/morganscode.md).

**Tes choix :**
- **Public visé** : France, Belgique et Suisse. **Public réel** (avril-oct. 2026) : 63 % d'Afrique francophone, 36 % de France. **Âge** : 61 % de 18-24 ans, 33 % de 25-34 ans, 4 % de 35-44 ans. **94 % ont moins de 35 ans.**
- **Envies** : l'IA en local et raconter la tech.
- **Style** : ta voix (enregistrée au téléprompteur depuis ArtCraft, ou clonée) et du motion design, sans visage.
- **Rythme** : **une vidéo longue par semaine, le lundi à 18 h, aucun Short** (décidé le 21/10), en solo. **Objectif** : croissance.
- **IA sans tester** : pour les modèles trop gros pour ta 5080, tu fais le calcul à partir des sources, comme Kai et Morgans Code (décidé le 21/10).
- **Flutter** : plus de nouvelles vidéos. **Chaîne** : on fait évoluer Technovore.

---

## 0. Ce qui change

### Le 23/10 (soir) : les scripts des 6 mois écrits d'avance

À ta demande, 14 vidéos ont leur script final :
- les vidéos génie : Waze, pseudo, iPhone, WhatsApp, lag, SQLite, sans contact, écran blanc ;
- les histoires : pixel, Python, Windows Phone, llama.cpp, jeux possédés ;
- « Louer, acheter ».

Pour chacune :
- recherche vidIQ et web ;
- double vérification des faits (Opus) ;
- V1 avec `/youtube script` ;
- grill avec `youtube-script-grill` (variante storytelling) et version finale.

La synthèse est dans [`etudes/calendrier-vidiq-2026-10-23.md`](etudes/calendrier-vidiq-2026-10-23.md). Les créneaux IA restent au radar.

| Avant | Après | Pourquoi |
|---|---|---|
| Mobile Money le 8 févr. (idée 17) | **Abandonnée** ; llama.cpp avance au 8 févr. | Elle ne te plaît pas |
| llama.cpp le 8 mars | **Le lag des jeux en ligne** le 8 mars (idée 21) | Choisi au radar du 23/10 : ×108 chez DeadInSperanza, rien en français |
| Plusieurs titres et hooks (Waze, SQLite, Python, pseudo, WhatsApp) | Corrigés dans les fiches et les scripts | La 2e vérification les a trouvés faux ou trop forts : voir les idées 3, 4, 6, 13 et 18 |
| Pixel : 3,6 ou 3,7 milliards ? Python et SQLite sans titre ; jeux à avancer avant GTA 6 ? | *D'un pixel à 3,7 milliards de joueurs* ; *Python, le langage de l'IA, est un cadeau de Noël* ; *Sans cette base de données, ton téléphone ne marche pas* ; les jeux gardent le 22 févr. | Tes choix du 23/10 au soir. GTA 6 sort le 19/11 : en novembre, une vidéo sur les jeux serait noyée sous les siennes |
| Créneau radar IA du 30 nov. | ***IA en local : comment lire le nom d'un modèle*** (idée 22) | Ta demande du 23/10 : poser les bases (noms des modèles, local ou open source, routeurs, harnais) avant de plonger dans la technique. Recherche, double vérification, V1 et grill faits le soir même |
| IA en local le 30 nov., après Claude #1 (2 nov.) et Coût Claude (16 nov.) | **IA en local le 2 nov., Claude #1 le 16 nov., Coût Claude le 30 nov.** | Ta décision du 23/10 (nuit) : c'est elle qui pose les bases, elle passe donc avant. Claude #1 sort toujours 11 jours avant le Black Friday, et Coût Claude deux semaines après lui |
| Coût Claude le 30 nov., le lundi qui suit le Black Friday | **Coût Claude le 23 nov., pseudo le 30 nov.** | Ta demande du 24/10 : qu'il sorte avant le Black Friday. Seule exception à l'alternance des piliers : Claude #1 et Coût Claude se suivent, comme une suite en deux parties |
| La série « Claude ou mon PC ? » | **La série « Abonnement ou IA locale ? »**, qui est aussi le nom de la playlist. Dans la voix, pas de « épisode un » : chaque vidéo renvoie à celle qui explique une partie en détail (« si t'as pas tout suivi, j'ai une vidéo qui l'explique, je te la mets là ») | Ta décision du 24/10 : on compare plusieurs abonnements (Claude, ChatGPT…) à un PC, pas seulement Claude. Bandeau des miniatures vert-02 et vert-10 changé le jour même |
| Le coût, vidéo par vidéo | **Le calcul en quatre cas** : matériel déjà là ou pas, contre un abonnement à 20 $ et à 100 $ ; puis le pour et le contre ; puis ton choix | Ta demande du 24/10. En entier dans Claude #1 (16 nov.) et dans Louer, acheter (4 janv.) ; une phrase et un renvoi dans Coût Claude. Les conseils d'achat parlent aussi de l'occasion |
| — | **Nouvelle vidéo : deux cartes d'occasion pour le max de VRAM** (idée 23), le 21 déc., **calculée** | Ta demande du 24/10 : pas d'achat de cartes, on en parle en théorie. Recherche et double vérification faites le jour même (`projets/deux-cartes-occasion/`). Les prix d'occasion, tu les relèves toi-même au moment de la vidéo |
| — | **Nouvelle vidéo : Mac mini ou PC gamer pour l'IA en local ?** (idée 24), provisoire au 1er févr., calculée | Ta demande du 24/10, inspirée de Locally (40 K vues, ×21,9). Notre angle : le duel en euros avec ta machine, puis le calcul en quatre cas de la série |
| *IA en local : comment lire le nom d'un modèle* le 2 nov., l'iPhone le 7 déc. | **Nouvelle vidéo : *Pourquoi avoir ta propre IA, et comment l'installer*** (idée 25, LM Studio) **le 2 nov. ; *IA en local* le 7 déc. ; l'iPhone le 15 févr.** (créneau radar IA) | Ta décision du 24/10 (nuit) : une progression douce, d'abord la base (pourquoi le local, installer, discuter), ensuite les noms, pour que chaque vidéo renvoie aux anciennes. Le hook : Fable 5 coupé pour tout le monde puis revenu, donc ça peut arriver n'importe quand, chez n'importe quel fournisseur. LM Studio parce que c'est le plus simple, et gratuit au travail. L'équilibre des piliers ne change pas |

### Le 23/10 : deux sujets mal compris

| Avant | Après | Pourquoi |
|---|---|---|
| Pixel (14 déc.) recadré sur « il n'y a pas de blanc », ton brouillon en 2e acte | **Deux vidéos.** Le 14 déc. : ton hommage au jeu vidéo, *D'un pixel à 3,7 milliards de joueurs* (idée 20). L'écran sans blanc (idée 10) passe au 19 avr., provisoire | Ton sous-texte : on est parti d'un pixel avec Pong, et aujourd'hui des milliards de joueurs sont connectés. Le recadrage l'avait perdu |
| *Windows Phone, il lui manquait les applis* | ***Ton téléphone est une brique*** : le sujet, ce sont les applis ; Windows Phone en est la preuve (idée 14) | Ce sont nos applis qui font qu'on aime notre téléphone. Windows Phone a échoué faute des applis que tout le monde aimait |

Désormais, chaque fiche écrit le **texte** (le sujet) et le **sous-texte** (ce que la vidéo dit vraiment), le « problème de surface / problème profond » du skill `youtube-script-grill`. Un recadrage qui change le sous-texte fait une autre vidéo.

### Après l'audit du 22/10

L'audit complet, chiffres compris, est dans [`etudes/audit-2026-10-22.md`](etudes/audit-2026-10-22.md). Le plan v4 ne change pas. Ce qui change :

| Avant | Après | Pourquoi |
|---|---|---|
| Hook dans les 5 premières secondes | **Les 15 premières secondes sont les plus fortes de la vidéo** (section 5) | ArtCraft perd 34 % de ses spectateurs en 15 s et 53 % en 1 min. Ceux qui passent 3:20 restent jusqu'au bout, et le test de PhotoCraft est au-dessus de la médiane : le fond tient, c'est l'entrée qui fuit |
| Playlist Flutter archivée | **Les tutos restent publics**, la playlist Flutter passe en bas de la page de chaîne | La formation et la vidéo d'installation font 86 % des heures publiques et 615 des 755 abonnés gagnés en 12 mois |
| Coût Claude le 2 nov., Claude #1 le 16 nov. | **Claude #1 le 2 nov., Coût Claude le 16 nov.** (ta décision du 22/10 au soir) | Coût Claude a besoin d'une mesure sur ta 5080 : les essais de Claude #1 (23-24/10) la lui donnent |
| Monétisation regardée à 6 mois | **Regarder le premier palier du Programme Partenaire tout de suite** | 3 260 h publiques sur 12 mois, en baisse : sous 3 000 h vers décembre (estimation) |

### De la v3 à la v4 (21/10)

| v3 | v4 | Pourquoi |
|---|---|---|
| 2 vidéos longues par mois, le lundi à 20 h | **1 vidéo longue par semaine, le lundi à 18 h** | Ta décision. Le guide de l'algorithme dit que la régularité compte plus que le volume : un rythme fixe de 4 par mois bat 12 vidéos irrégulières |
| 1 Short par vidéo longue, en test jusqu'au 7/12 | **Plus aucun Short** | Ta décision. Sur un an, tes Shorts ont rapporté 2 abonnés, contre 772 pour les vidéos longues ; Kai les a abandonnés, et Morgans Code n'en fait pas |
| Vidéos IA : tests sur ta 5080 | **Deux formats : testé** (ce qui tient dans 16 Go) **et calculé** (le reste) | Kai et Morgans Code ne testent presque rien. Ils calculent à partir des notes de version et des mesures des autres, et ça marche ([`etudes/morganscode.md`](etudes/morganscode.md)) |
| Calendrier jusqu'au 31 janvier | **Plan sur 6 mois, jusqu'au 26 avril** ; fermé jusqu'au 25 janv., puis provisoire | Au-delà de 3 mois, l'actu de l'IA rend un plan figé faux |
| Choix des sujets une fois pour toutes | **Un radar à chaque sortie** : ta vidéo à J+7, les concurrents, le public français, puis le choix du créneau libre | Procédure dans `CLAUDE.md`, journal dans [`etudes/radar.md`](etudes/radar.md) |
| Objectifs J30/J60/J90 | **Objectifs à 1, 3 et 6 mois** (section 6) | Le rythme double |
| Coût Claude le 4 janv., Claude #1 le 23 nov. | **Coût Claude le 2 nov., Claude #1 le 16 nov.** | Le format « combien ça coûte » est le plus sûr chez Kai, et Claude #1 sort 11 jours avant le Black Friday au lieu de 4 |
| OpenCode hors calendrier | **Sortie le mer. 21/10** | Vidéo d'actu, publiée avant le passage au rythme hebdomadaire |

### De la v2 à la v3 (11/10)

| v2 | v3 | Pourquoi |
|---|---|---|
| Pilier signature « On ne possède plus rien » (Sony, streaming, Plex) | Pilier signature **« Le génie derrière l'app »** : l'ingénierie cachée des applis que tu utilises tous les jours | C'est le format qui surperforme le plus dans les données (tableau 1). Les récits « louer ou posséder » passent en réserve. |
| Uber mis de côté (Jared a déjà raconté l'histoire business) | **Uber en premier**, sous l'angle ingénierie | Jared raconte comment Uber a tué les taxis. Toi, tu racontes comment la carte en direct fonctionne : ce n'est pas le même sujet. |
| Défi « 30 jours avec une IA locale » | Série **« Claude ou mon PC ? »** : un épisode par modèle, avec la révélation au début | Un mois sur un seul modèle, c'est trop long quand un nouveau modèle sort toutes les deux semaines. |
| Uber en premier le 26 oct. | **ArtCraft le 26 oct., Uber le 9 nov.** (décidé le 12/10) | ArtCraft est un sujet d'actu qui perd de la valeur chaque semaine, alors qu'Uber ne périme pas. |
| Windows 10 en vidéo longue le 26 oct. | **Un Short cette semaine** (pas sorti, archivé le 19/10) | La date du 13 octobre est passée. Le sujet ne vaut plus une vidéo de 2 semaines de travail. |
| ArtCraft le 26 oct. | **ArtCraft le 19 oct.** (terminé en avance) ; les autres dates ne bougent pas | La semaine gagnée accueille les essais Qwen et les tests de VRAM, qui surchargeaient début novembre. |
| 1 Short par semaine (16 jusqu'au 31 janv.) | **1 Short par vidéo longue** (7), en test jusqu'au J60 (décidé le 19/10) ; **arrêtés le 21/10** (v4) | Sur un an, les Shorts t'ont rapporté 2 abonnés, contre 772 pour les vidéos longues. Chez Thibaut Dcode, ils font 2,5 % des vues. |
| Pixel gardé pour 5 K abonnés | **Pixel le 21 décembre**, recadré sur l'astuce cachée | C'est ta passion, et l'angle « astuce de génie » marche même sur une toute petite chaîne (Andy Geers, ci-dessous). |
| Cible : 20-40 ans | Cible : **18-30 ans** | 94 % de ton audience actuelle a moins de 35 ans. |

---

## 1. Ce qui dépasse la moyenne : tes inspirations

**Comment lire « × moyenne »** : c'est le score de vidIQ. ×35 veut dire que la vidéo a fait environ 35 fois les vues habituelles de sa chaîne.

### Le génie derrière l'app (ingénierie des applis du quotidien)

| Chaîne (abonnés) | Vidéo | Vues | × moyenne |
|---|---|---|---|
| Philipp Lackner (260 K) | [The Genius System Behind the Uber App's Real-Time Map](https://www.youtube.com/watch?v=gHIs0Mdow8M) | 601 K | ×35,7 |
| Yeshendra Dhaker (10 K) | [How Uber Finds Your Driver in 10 Seconds](https://www.youtube.com/watch?v=Cdx4DF9N8d8) | 43 K | ×52 |
| Enrico Tartarotti (258 K) | [The Insane Design Of Messaging](https://www.youtube.com/watch?v=6DSW1rN-ZV4) (2 oct. 2026) | 1,52 M | ×23,5 |
| ByteMonk (405 K) | [How Big Tech Checks Your Username in Milliseconds](https://www.youtube.com/watch?v=_l5Q5kKHtR8) | 706 K | ×22 |
| ByteMonk | [How UPI Works: Real-Time Payments in India](https://www.youtube.com/watch?v=iI2NaN_QVTI) | 773 K | ×44 |
| ByteMonk | [Inside SQLite: The 300KB File That Beat Oracle and Postgres](https://www.youtube.com/watch?v=zzaj4ueQe8U) | 220 K | ×12,6 |
| ByteMonk | [What REALLY Happens When You Type Localhost?](https://www.youtube.com/watch?v=PwNJXUdMkVY) | 312 K | ×8,3 |
| ByteMonk | [How NGINX Handles MILLIONS of Requests With Just 1 Process](https://www.youtube.com/watch?v=I6dpN0geIb4) | 331 K | ×8,2 |
| ByteMonk | [Inside a Real High-Frequency Trading System](https://www.youtube.com/watch?v=iwRaNYa8yTw) | 528 K | ×6,6 |
| ByteMonk | [The Hidden Security Magic Behind Mobile Payments](https://www.youtube.com/watch?v=JQ_wXA9JA1g) | 195 K | ×4,5 |
| Enrico Tartarotti | [The Ridiculous Engineering Of Notion](https://www.youtube.com/watch?v=b00sgRR_Vc0) | 559 K | ×8,9 |
| Core Dumped (513 K) | [Why Some Projects Use Multiple Programming Languages](https://www.youtube.com/watch?v=XJC5WB2Bwrc) | 1,55 M | ×9,6 |
| Hussein Nasser (523 K) | [you won't forget how postgres works after this](https://www.youtube.com/watch?v=q9jixKv4h2I) | 227 K | ×13,5 |
| Low Level (1,17 M) | [I Hacked This Temu Router. What I Found Should Be Illegal.](https://www.youtube.com/watch?v=KsiuA5gOl1o) | 5,1 M | ×22,6 |

### Astuces cachées et histoires de la tech (pour l'écran sans blanc, idée 10)

| Chaîne (abonnés) | Vidéo | Vues | × moyenne |
|---|---|---|---|
| Andy Geers (1,1 K) | [The Genius Trick Behind Exile's Impossible Map](https://www.youtube.com/watch?v=MdPz9dLmOtI) | 94 K | **×431** |
| Enrico Tartarotti | [The LIES That Make Hardware ACTUALLY Work](https://www.youtube.com/watch?v=wLIgrGAIRsE) | 761 K | ×6,8 |

### IA en local et repos GitHub viraux

| Chaîne (abonnés) | Vidéo | Vues | × moyenne |
|---|---|---|---|
| Red Stapler | [I ran Qwen3.8 27B on single 8GB Card!](https://www.youtube.com/watch?v=ye50BbXEczo) (5 min 15) | 588 K | non mesuré |
| **Rudy IO (1,4 K), en français** | [Mon setup d'IA agentique : comment tout fonctionne ensemble](https://www.youtube.com/watch?v=of3ciczOMp4) | 35 K | **×105** |
| Bilawal Sidhu | [God's Eye View Blew Up](https://www.youtube.com/watch?v=o_FJ1NIH9yw) | 2,94 M | non mesuré |
| Eric Tech | [How To Use REA To Clone Any Software In Minutes](https://www.youtube.com/watch?v=FnB9tHKBJXQ) | 65 K en moins d'une journée | non mesuré |
| ByteMonk | [The Truth About the 700 OpenAI Agents That Attacked Hugging Face](https://www.youtube.com/watch?v=dt_OMxufoGE) | 940 K | ×39 |
| ByteMonk | [OpenClaw: The Most Dangerous AI Project on GitHub?](https://www.youtube.com/watch?v=Hv84JhzKvKQ) | 278 K | ×11 |
| **FUTC (58,8 K), chaîne photo** | [Somebody Vibe Coded EVERY SINGLE ADOBE App](https://www.youtube.com/watch?v=eFB79TYI-Vw) (7 oct. 2026, 20 min) | **2,24 M en 5 jours** | **≈ ×100** (médiane de ses 30 dernières vidéos : 22 K, calcul manuel) |
| FUTC | [I Tried The Vibe Coded After Effects Clone.](https://www.youtube.com/watch?v=5mi_tYSdkWQ) (suite, 3 jours après) | 444 K | ≈ ×20 |
| Jay E \| RoboNuggets | [Quelqu'un vient de recréer Adobe gratuitement… (7 applis)](https://www.youtube.com/watch?v=Fuo1i_-9Frc) | 557 K en 4 jours | non mesuré |
| **Morgans Code (2 K)**, calculé sans test | [6× Faster Than llama.cpp — The New Way to Run 125B Models](https://www.youtube.com/watch?v=i7nSjm5tTRw) | 62,9 K | ×16,4 |
| Morgans Code | [Is $1,500 All You Need to Run DeepSeek V4.1 Flash?](https://www.youtube.com/watch?v=mat0oOXVCcU) (20 oct. 2026) | 17,7 K en un jour | ×2,4 |
| **Le Lab IA (18,6 K), en français** | [Adieu le cloud pour les LLM ! Vive le local](https://www.youtube.com/watch?v=C0Q6cO9nTAs) | 47,8 K | ×24 |
| **Bricolo2.0 (6 K), en français** | [Gérer HomeAssistant avec une IA 100 % gratuite](https://www.youtube.com/watch?v=PYeJ6nhGCDY) | 25,9 K | ×31 |

**La vague ArtCraft (octobre 2026).** Le 7 octobre, le développeur Brandon Thomas publie ArtCraft : 7 clones open source des logiciels Adobe (Photoshop, Illustrator, Premiere, Lightroom, Acrobat, After Effects, InDesign), écrits en Rust avec Claude Opus 5.5. Ils sont encore en alpha. Pourquoi FUTC fait ×100 :
1. **L'ennemi commun** : son public de photographes déteste l'abonnement Adobe, et lui en parle depuis un an (« I Made 5 Photography Apps Because Adobe Wouldn't », 116 K).
2. **Le titre « Somebody… »** : un inconnu a fait un exploit contre un géant. Le mot « EVERY SINGLE » est en majuscules.
3. **La vitesse** : sa vidéo sort le jour de l'article de Gizmodo.
4. **Les suites immédiates** : After Effects (444 K), puis Office (329 K). Le sujet continue de surperformer après la première vidéo.

Avec REA (Eric Tech), c'est **la 2e anomalie sur le même thème** : « l'IA recrée un logiciel payant ». C'est exactement le terrain de « Claude ou mon PC ? ».

### En français : la preuve que « comment ça marche vraiment » fonctionne

| Chaîne (abonnés) | Vidéo | Vues | × moyenne |
|---|---|---|---|
| Fransosiche (47,7 K) | [Hacker un Wi-Fi, comment ça fonctionne vraiment en 2026 ?](https://www.youtube.com/watch?v=w-TQER9MhE4) | 256 K | ×7,2 |
| **Thibaut Dcode** | [LA FACE SOMBRE DERRIÈRE LA GRATUITÉ DE WAZE](https://www.youtube.com/watch?v=3-3_3KdaTSw) (13 sept. 2026) | **1,09 M** | ×4,6 |
| Thibaut Dcode | [L'INQUIÉTANT PROBLÈME DE REVOLUT](https://www.youtube.com/watch?v=G_8CK0yFqQY) | 161 K | ×16,7 |
| Thibaut Dcode | [L'EFFRAYANTE VÉRITÉ SUR DOCTOLIB](https://www.youtube.com/watch?v=2am50PHuOtE) | 388 K | ×12,7 |
| Thibaut Dcode | [GTA 6 ARRIVE… ET ROCKSTAR VA TOUT EFFACER SANS TE PRÉVENIR](https://www.youtube.com/watch?v=wE0ws9mFpDU) | 375 K | ×11,9 |
| Thibaut Dcode | [L'EFFRAYANTE VÉRITÉ SUR L'EMPIRE WHATSAPP](https://www.youtube.com/watch?v=7EgYg0OxbX0) (4 oct. 2026) | 152 K | ×0,55 (une semaine en ligne) |
| Jared (18,5 K) | Comment Uber a tué les taxis ? (histoire business, pas ingénierie) | 179 K | — |

**Thibaut Dcode, le concurrent français le plus proche.** C'est une chaîne de décryptage business, avec une vidéo par semaine, le dimanche. Sur sa chaîne, **ce sont les applis et la tech qui dépassent le plus sa moyenne** (Revolut, Doctolib, GTA 6, Waze), devant les marques de distribution. Son angle est **business** (« la face sombre », « le business caché ») ; le tien est **ingénierie** (« comment la machine marche »). C'est le même cas qu'Uber avec Jared : même appli, autre sujet.

**Bonus :** une vidéo d'ingénierie sur Waze ou WhatsApp peut apparaître en suggestion à côté des siennes, qui font des centaines de milliers de vues.

**Correction** : dans la version précédente, j'écrivais qu'aucune vidéo française ne parlait de Waze. C'était faux : mon scan ne couvrait que les titres contenant « comment fonctionne ». Côté ingénierie, en revanche, je n'ai toujours rien trouvé en français sur Uber, WhatsApp ou Waze.

### Ce que ces vidéos ont en commun

1. **Une appli que tout le monde a dans la poche** (Uber, WhatsApp, un champ « pseudo », un paiement), et **un mécanisme invisible** derrière.
2. **Un titre « génie / insensé / secret » + un chiffre qui semble impossible** : 1 process, 300 Ko, quelques millisecondes, 10 secondes.
3. **Entre 8 et 15 minutes.** La vidéo Uber de Philipp Lackner dure 9 min 57.
4. **Elles font sortir une chaîne de dev de sa niche.** Philipp Lackner est une chaîne de tutos Android/Kotlin, comme l'était Technovore. **Sa vidéo Uber est la plus vue de toute sa chaîne**, avec 5,3 % d'engagement, contre 2 à 2,5 % pour ses tutos les plus vus.
5. **Ce sont des sujets universels.** WhatsApp ou une appli de VTC parlent autant à ton public africain actuel qu'au public français que tu vises. Tu n'as pas à choisir entre les deux.

---

## 2. Positionnement

> **Technovore montre aux 18-30 ans curieux de tech le génie caché derrière les applis qu'ils utilisent tous les jours, et ce que leur propre PC peut faire avec l'IA, en récits animés en voix off, là où les chaînes tech françaises font surtout de l'actu, des tutos ou des histoires business.**

- **Angle unique** : un développeur qui ouvre le capot des applis et qui fait tourner une IA chez lui. Il **raconte** au lieu de faire un cours.
- **Spectateur cible** : un ou une étudiante, ou un jeune dev, de 18 à 30 ans. Il utilise Uber et WhatsApp tous les jours et s'est déjà demandé « mais comment ça marche ? ». Il a entendu parler de l'IA en local sans jamais l'essayer.
- **Différenciation** :
  - Jared raconte des histoires d'entreprises ;
  - Thibaut Dcode décrypte le business caché des marques et des applis (Waze, Doctolib, WhatsApp) ;
  - Makertronic fait de l'actu hardware ;
  - Rudy IO et Nathan Inline montrent leurs configurations IA ;
  - en anglais, ByteMonk et Enrico Tartarotti font des explications d'ingénierie. **En français, personne ne raconte l'ingénierie des applis du quotidien.**
  - en anglais, Kai et Morgans Code calculent le coût de l'IA locale, en dollars et sans tester. **Toi, tu comptes en euros, tu testes ce qui tient dans ta 5080 et tu calcules le reste à la source.** En français, personne ne fait ni l'un ni l'autre (radar du 21/10).
- **Micro-niche de départ** : « Le génie derrière l'app » + « Abonnement ou IA locale ? » (« Claude ou mon PC ? » jusqu'au 24/10).
- **Élargissement prévu** :
  - **10 K abonnés** : les grandes histoires de la tech (Sony, llama.cpp, Plex, le streaming) ;
  - **50 K** : enquêtes documentaires longues ;
  - **100 K** : la référence en France sur « comment marche vraiment la tech ».

---

## 3. Piliers

> **Hub** = série récurrente qui fidélise. **Hero** = grosse vidéo événement ou d'actualité. **Help** = vidéo qui répond à une recherche précise et dure dans le temps.

### Pilier 1 : « Le génie derrière l'app » (Hub)
- **But** : la série signature. Elle doit faire tes plus gros pics de vues.
- **Format** : 10 à 14 min. Hook sur un geste banal (« ouvre Uber »), puis le problème impossible, puis l'astuce de génie, en motion design (Remotion). Fin : ce que ça change pour toi.
- **Fréquence** : environ 1 semaine sur 3 (9 vidéos sur 27 d'ici fin avril).
- **Trafic visé** : accueil et suggestions (il se place à côté des vidéos ByteMonk et Enrico Tartarotti).
- **Exemples** :
  1. *Le génie caché derrière la carte en temps réel d'Uber*.
  2. *Comment 50 ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes*.
  3. *Comment Google sait en une milliseconde que ton pseudo est déjà pris*.

### Pilier 2 : « IA chez moi » (Hub + Help)
- **But** : la tendance la plus forte (« ia en local » +215 %), avec tes vraies expériences.
- **Deux formats, selon que le modèle tient ou non dans ta 5080** (décidé le 21/10) :
  - **Testé**, la série **« Abonnement ou IA locale ? »** (sa playlist ; « Claude ou mon PC ? » jusqu'au 24/10 : on compare plusieurs abonnements à l'IA locale, pas seulement Claude). Pour ce qui tient dans 16 Go. On montre d'abord le résultat, on demande au public s'il vient de Claude Opus 5.5, on révèle que non, puis on explique comment c'est fait. Un épisode par nouveau modèle. Le thème « même carte, plus rapide » (le meilleur de Morgans Code, idée 16) se teste aussi chez toi.
  - **Calculé**, pour ce qui ne tient pas (DeepSeek, Kimi, Claude). Le calcul part des sources, comme chez Kai et Morgans Code (« combien ça coûte ? », « N Go, ça suffit ? », « louer ou acheter ? »). C'est le format léger qui rend le rythme hebdomadaire tenable.
- **Règles du calculé** :
  1. Dis-le dans les 30 premières secondes : « je n'ai pas cette machine, alors j'ai fait le calcul, et voici d'où viennent les chiffres ».
  2. Chaque chiffre a sa source, datée dans `sources.md` : note de version, ticket GitHub, benchmark, prix relevé dans une boutique française. Ne recopie jamais un chiffre de Kai ou de Morgans : remonte à leur source.
  3. Le calcul s'affiche à l'écran, puis on le confronte à une mesure : la tienne pour la partie qui tient dans 16 Go, sinon celle d'un tiers, citée.
  4. Une estimation n'est jamais présentée comme une mesure. Écris « environ », « au mieux », « d'après X ».
  5. Des prix en euros, TVA comprise. Pas d'électricité : le seul coût compté est l'achat (décidé le 23/10).
- **Fréquence** : **une semaine sur deux**, en alternance avec les deux autres piliers.
- **Trafic visé** : accueil pour les épisodes, recherche pour les « combien ça coûte ».
- **Exemples** :
  1. *16 Go de VRAM suffisent-ils pour remplacer Claude ?* (Qwen sur RTX 5080, épisode 1 de « Abonnement ou IA locale ? »).
  2. *Il a recréé 7 logiciels Adobe avec une IA. J'ai testé son Photoshop.* (ArtCraft, le repo viral d'octobre).
  3. *Combien coûte Claude Opus 5.5 en local ? (j'ai fait le calcul)*.

### Pilier 3 : « Les grandes histoires de la tech » (Hero)
- **But** : vidéos passion et partageables, qui élargissent le public.
- **Format** : documentaire de 12 à 18 min.
- **Fréquence** : un peu moins d'une par mois (5 sur 27 d'ici fin avril : pixel, Python, Windows Phone, jeux, llama.cpp).
- **Trafic visé** : accueil.
- **Exemples** :
  1. *D'un pixel à 3,7 milliards de joueurs* : ton hommage au jeu vidéo (idée 20).
  2. *Le dev qui a mis un ChatGPT dans ton PC* : l'histoire de llama.cpp.
  3. *Tu n'as jamais possédé tes jeux*.

### Équilibre des piliers (27 vidéos du 26 oct. au 26 avr.)

| Pilier | Type | Vidéos | Part |
|---|---|---|---|
| Le génie derrière l'app | Hub | 9 | 33 % |
| IA chez moi | Hub (testé) et Help (calculé : « combien ça coûte », « louer ou acheter ») | 13 | 48 % |
| Grandes histoires | Hero | 5 | 19 % |
| **Total** | Hub ~60 % · Help ~20 % · Hero ~20 % | **27** | **100 %** |

**Lecture :** le modèle commentaire/essai recommande Hero 25-30 %, Hub 45-50 %, Help 20-25 %. Le skill stratégie recommande 70/15/15 pour une chaîne en croissance. Tu es entre les deux. Les vidéos calculées donnent enfin au Help sa place : elles répondent à des recherches (« combien coûte… en local »).

---

## 4. La niche est-elle viable ?

| Critère | Évaluation | Détail |
|---|---|---|
| **Revenus publicitaires estimés** | CPM 8 à 14 $ (Tech/SaaS), RPM 2 à 8 $ (commentaire/essai) | Références américaines. **Pas de chiffre pour la France ni par tranche d'âge** dans les références. |
| **Concurrence** | Faible en français, forte en anglais | En anglais : ByteMonk, Enrico Tartarotti, Fireship, Low Level. En français, l'ingénierie des applis n'a pas de chaîne attitrée. |
| **Durée de vie** | Surtout durable | Le fonctionnement d'Uber ou de WhatsApp reste valable des années. Seuls les épisodes « Abonnement ou IA locale ? » vieillissent vite, et c'est voulu : un nouveau modèle, un nouvel épisode. |
| **Demande** | En hausse | « ia en local » +215 %. Les vidéos d'ingénierie font ×4 à ×44 la moyenne de leur chaîne (tableau 1). |
| **Monétisation** | Seuil de 1 000 abonnés atteint | Heures de visionnage à vérifier dans Studio. |
| **Sponsors** | Moyen à élevé | Matériel IA, hébergeurs, outils de dev, cours en ligne. Le public de 18-30 ans en tech intéresse les plateformes d'apprentissage. |
| **Autres revenus** | Newsletter, abonnements à la chaîne | |

**Verdict : bon.**
- **Le plus gros risque** : la production. Une vidéo « génie » demande beaucoup de schémas animés. Tes animations Remotion doivent devenir réutilisables (carte, serveurs, flux de données). C'est encore plus vrai au rythme hebdomadaire, d'où l'alternance avec les vidéos calculées.
- **La plus grosse opportunité** : le format qui a fait la plus grosse vidéo d'une chaîne de tutos Android n'a aucun équivalent en français.

### ⚠️ Garde-fous
1. **Voix off clonée (ta propre voix)** : c'est viable. YouTube cite explicitement « cloner sa propre voix pour des voix off ou des doublages » parmi les cas qui **ne demandent pas d'étiquette IA**, et une étiquette ne coupe de toute façon ni l'audience ni les revenus. Le vrai risque de démonétisation vient de la **forme du contenu**, pas de la voix. Il vise les vidéos qui ressemblent à un modèle répété, les diaporamas avec peu de narration et les lectures de textes que tu n'as pas écrits. Donc : script original, vrai montage, et jamais un article lu tel quel.
2. **Les chiffres d'ingénierie se vérifient à la source** : blogs d'ingénierie officiels (Uber Engineering, Meta Engineering), conférences, articles de presse datés. Une erreur technique dans les commentaires coûte cher en crédibilité auprès d'un public de devs.
3. **Repos de rétro-ingénierie (REA et autres)** : en France, la décompilation n'est autorisée que dans des cas précis (interopérabilité, article L122-6-1 du Code de la propriété intellectuelle). À l'écran, utilise **une app à toi** ou un logiciel open source, et ne distribue jamais un clone.
4. **Pas de copie de DVD ni de contournement de protection à l'écran** : c'est puni de 3 750 € d'amende (article L335-3-1 du Code de la propriété intellectuelle).
5. **Images d'archives** : extraits courts et commentés. Privilégie tes propres captures et ton motion design.
6. **Vidéos calculées** : les 5 règles du pilier 2. Le risque ici, c'est la crédibilité : sous les vidéos de Kai, les commentaires les plus likés corrigent ses chiffres.

---

## 5. Rythme de publication

**Décidé le 21/10 : 1 vidéo longue par semaine, le lundi à 18 h (heure de Paris). Aucun Short.**

- **Étude vidIQ (5,08 M de chaînes)** : 12 vidéos et plus par mois font grandir les vues 8 fois plus vite, mais **la régularité compte plus que le volume** : un rythme régulier de 4 vidéos par mois vaut mieux que 12 vidéos irrégulières. Ton levier, c'est de **ne jamais rater un lundi**.
- **Pourquoi c'est tenable** :
  - une vidéo lourde (génie, histoire) alterne avec une vidéo légère (IA calculée) ;
  - chaque semaine, tu montes la vidéo suivante et tu écris celle d'après ;
  - le pseudo sert de joker si une semaine déraille.
  - Compte 20 à 30 h par semaine (estimation, à vérifier au bilan du 23/11).
- **Pas de Shorts** : sur un an, ils t'ont rapporté 2 abonnés, contre 772 pour les vidéos longues. Chez Thibaut Dcode, ils font 2,5 % des vues, et Kai les a abandonnés avant de décoller. Le guide Shorts du skill va dans le même sens : ~10 % de public en commun avec la vidéo longue, et un lien « vidéo associée » qui convertit à moins de 1 %.
- **Créneau** : 18 h au lieu de 20 h. Vérifie dans Studio > Audience que ça tombe un peu avant le pic de ton public, et refais le point au bilan du 23/11.
- **Exigence minimale** :
  - plus de 8 minutes (pubs en milieu de vidéo possibles) ;
  - des chapitres ;
  - les 15 premières secondes les plus fortes de la vidéo, et aucune phrase de remplissage jusqu'à 30 s (règles ci-dessous) ;
  - une réponse à tous les commentaires des 2 premières heures : le guide de l'algorithme les compte comme décisives.

### La règle des 15 premières secondes (22/10)

**Les 15 premières secondes doivent être les plus impactantes de toute la vidéo.**

- **Pourquoi** :
  - ArtCraft perd 34 % de ses spectateurs en 15 s et 53 % en une minute ;
  - son intro est dans le bas du classement des vidéos de même durée (indice 0,31), alors que le test de PhotoCraft, au milieu, est au-dessus de la médiane (0,55 à 0,60) ;
  - les spectateurs qui passent 3:20 restent jusqu'au bout ;
  - le guide de l'algorithme fixe à 40 % la rétention sous laquelle une vidéo est moins poussée : ArtCraft est à 28 %.
- **Comment** :
  - le moment le plus fort de la vidéo passe au début : le résultat, le chiffre le plus fou, la révélation, ou l'image que promet la miniature ;
  - le contexte et les explications viennent après ;
  - c'est déjà la structure de « Claude ou mon PC ? » (le résultat d'abord) ; on l'applique à tous les piliers.
- **Ce qu'on ne met pas** : présentation, logo, « dans cette vidéo… », ni contexte avant la promesse.
- **Contrôle** :
  - à chaque grill et à chaque storyboard, relis les 15 premières secondes seules : doivent-elles donner envie de rester ?
  - à chaque radar, relève le % de spectateurs à 0:15 (cible 75 %) et à 1:00 (cible 50 %). Ces cibles sont des estimations, à recaler au bilan du 23/11.
- **Attention** : la promesse doit être tenue plus loin dans la vidéo. Le guide de référencement rappelle que YouTube compare le contenu à la miniature et au titre.

### Les 30 premières secondes et le ton (23/10)

Cette règle prolonge celle des 15 s. Elle vient de l'étude de 9 vidéos de Cam, V2F et Dis Cyril (`etudes/storytelling-2026-10-23.md`).

- **0-15 s** : le meilleur moment (règle ci-dessus).
- **15-30 s** : la question centrale, une seule, puis le pont : le récit repart d'un endroit inattendu, ou le défi pose sa contrainte. Ça ouvre une deuxième question avant que la première soit résolue.
- **Chaque phrase des 30 s** confirme le clic, ouvre une question ou fait monter l'enjeu. Sinon, elle saute.
- **Le budget** : à ton débit (145 à 180 mots/min), 30 s font 75 à 90 mots.
- **Le ton** : tu parles à un ami. Chaque fait arrive avec une liaison orale (« donc », « du coup », « en fait », « sauf que », « en effet », « voilà comment… »), puis une réaction ou une traduction pour le spectateur.
  - Cam et V2F mettent 1,5 à 2,7 liaisons pour 100 mots.
  - Nos téléprompteurs ArtCraft, OpenCode et Uber en mettent 0,7 à 0,9.
  - Vise 1,5 ou plus.
- **Contrôle** : la variante storytelling du skill `youtube-script-grill`. Elle fait passer le test des 30 secondes et compte les liaisons (axe 10) à chaque grill.

### La semaine type

| Jour | Vidéo de la semaine suivante | Vidéo d'après | Outil ou skill |
|---|---|---|---|
| Lundi | 18 h : publication, puis réponses aux commentaires pendant 2 h. Voix | **Radar**, puis choix du sujet | `CLAUDE.md`, « Radar » ; `ressources/voix/sm7b.sh` ou ta voix clonée (`voix-off-voicestudio`) |
| Mardi-samedi | Montage : schémas animés, captures | Recherche à la source, script, grill | `coach-montage-video`, Remotion ou HyperFrames ; `youtube-script-grill` |
| Dimanche | Miniature, titre, description, chapitres, sous-titres, puis programmation | — | `coach-miniature-youtube`, `/youtube metadata` |

---

## 6. Objectifs à 1, 3 et 6 mois (point de départ le 21/10 : 2 610 abonnés, ~3 200 vues sur 30 jours, 36 % des vues en France)

Les cibles d'abonnés et de vues sont des estimations : les références du skill n'ont aucune donnée de croissance pour une chaîne tech française de cette taille. On les recale à chaque bilan. Les seuils de CTR, de vision moyenne et de rétention viennent des guides du skill.

### À 1 mois (~23 novembre)
| Objectif | Cible | Action |
|---|---|---|
| Vidéos publiées depuis le 19/10 | 7 | ArtCraft, OpenCode, Uber, la vidéo d'installation, Waze, Claude #1, Coût Claude : pas un lundi raté |
| Vues moyennes par nouvelle vidéo (à 28 j) | 1 500 | Hook sur un geste banal, miniature avec un chiffre impossible |
| CTR moyen | 6 % (4-6 % = moyen, 7-10 % = bon) | Sous 3 %, change la miniature dès J+2 (ArtCraft était à 0,9 %) |
| Vision moyenne | ≥ 40 % | En dessous, YouTube pousse moins la vidéo |
| Rétention à 15 s | 75 % (ArtCraft : 66 %) | La règle des 15 premières secondes (section 5) ; cible estimée |
| Rétention à 30 s | 55 % | Référence commentaire : 55-65 % |
| Abonnés | 2 750 (+140) | Question en fin de vidéo : « Quelle appli je décortique ensuite ? » |
| Heures de travail | 30 h par semaine au plus | Au-delà, plus de vidéos calculées, moins de vidéos lourdes |
| Identité | Mise à jour | Bannière et description « le génie caché de la tech » ; Uber en vidéo à la une pour les non-abonnés ; playlists Génie et IA en haut, Flutter en bas. **Les tutos utiles restent publics** (86 % des heures) ; ceux à moins de 5 h par an seront masqués après la 10e vidéo des nouveaux thèmes (calendrier, S9) |
| Programme Partenaire | Premier palier vérifié | Studio > Gagner de l'argent, avant que les heures passent sous 3 000 (vers décembre) |

### À 3 mois (~25 janvier)
| Objectif | Cible | Action |
|---|---|---|
| Vidéos publiées depuis le 19/10 | 16 | |
| Abonnés | 3 200 (+590) | |
| Vues mensuelles | 8 000 (×2,5) | Accueil et suggestions |
| Meilleure vidéo | 10 000 vues | Le radar refait le format qui marche le mieux |
| Part des vues venant de France | 45 % | |
| Système | Documenté | Bibliothèque d'animations réutilisée d'une vidéo à l'autre ; radar tenu à chaque sortie |

### À 6 mois (~26 avril)
| Objectif | Cible | Action |
|---|---|---|
| Vidéos publiées depuis le 19/10 | 29 | |
| Abonnés | 4 500 | |
| Vues mensuelles | 20 000 | |
| Série reconnue | « Abonnement ou IA locale ? » et les vidéos calculées forment une série que les commentaires réclament | Chaque vidéo renvoie à celle qui explique une partie en détail, et annonce la suivante (la recette de Morgans Code ; dans la voix, pas de « épisode un ») |
| Monétisation | Heures de visionnage vérifiées | Si la chaîne n'est pas encore monétisée, viser les 4 000 heures sur 12 mois, soit environ 330 h par mois (110 h par mois au 22/10) |

---

## 7. Modèle de chaîne utilisé

**Type détecté** : Commentaire / essai (`templates/commentary-channel.md`), en version explication animée.
- **Équilibre Hero/Hub/Help** : appliqué via les trois piliers (voir l'équilibre plus haut).
- **Erreur classique « tout miser sur l'actu »** : seuls les épisodes d'IA suivent l'actualité ; les vidéos « génie » durent des années.
- **Erreur classique « personnalité qui s'efface »** : ta signature, c'est le dev qui ouvre le capot et qui teste chez lui, sur sa 5080. Garde le « je » dans chaque script.

---

# Idées de vidéos classées

**Sources** : vidIQ (vidéos qui dépassent la moyenne de leur chaîne), tes repérages, tes idées, ton vécu. Les idées 1 à 11 datent de la v3 ; les idées 12 à 19 ont été ajoutées le 21/10 (tes idées d'`idees.md` et le radar).
**Classement** : demande × potentiel de clic × facilité de production × cohérence avec la niche (chaque critère sur 10, total sur 40).

---

### Idée 1 : Claude ou mon PC ? (épisode 1 : Qwen sur RTX 5080)

| Attribut | Valeur |
|---|---|
| **Titre** | 16 Go de VRAM suffisent-ils pour remplacer Claude ? (depuis le 18/10 ; avant : *Claude Opus 5.5 ou mon PC ? J'ai fait coder une app par une IA 100 % locale*) |
| **Stratégie de trafic** | Accueil d'abord (+ recherche) |
| **Mot-clé** | ia en local / qwen |
| **Concurrence** | Moyenne |
| **Volume** | Élevé : « ia en local » 24,7 K/mois |
| **Tendance** | **En hausse, +215 %** |
| **Durée** | 10-12 min |
| **Niveau de RPM** | Élevé (tech/logiciel) |
| **Urgence** | Tendance : le modèle doit encore être récent à la sortie. Essais les 23 et 24/10, **publication le 16 novembre** (avancée au 2 nov. le 22/10, revenue au 16 nov. le 23/10 derrière la vidéo qui pose les bases, aujourd'hui celle de l'installation (24/10) ; Coût Claude, le 23 nov., réutilise ses mesures) |
| **Score** | **36/40** (demande 9 · clic 9 · production 8 · niche 10) |

**Hook** (ta structure) : « Cette app a été codée en quelques minutes par une IA. Claude Opus 5.5, tu penses ? … Non. Elle a été codée ici. [plan sur la 5080] Sans internet. Sans abonnement. »
**Miniature** : la RTX 5080 au centre avec une étiquette « 16 Go », le logo Claude, et en très gros « ÇA SUFFIT ? » (style Kai, sans visage).
**Pourquoi** : Red Stapler fait 588 K vues avec Qwen sur une carte de 8 Go, en 5 minutes. En français, Rudy IO (1,4 K abonnés) fait ×105 avec son setup d'IA. La révélation au début crée la curiosité, et la série se renouvelle à chaque nouveau modèle. **Montre aussi les ratés** : Red Stapler consacre un chapitre à ce qui n'a pas marché, et c'est ce qui le rend crédible.
**À vérifier** : le nom exact et la version du modèle (« Qwen3.8 Flash ») au moment du tournage.
**Source** : ton idée + Red Stapler.
**Mise à jour du 18/10** : le titre met en avant la carte de 16 Go, et la vidéo absorbe le guide (idée 7) pour sortir avant le Black Friday. Chez Kai, les vidéos sur le matériel et le coût font environ 2 fois plus de vues que les tests de modèles ([`etudes/kai.md`](etudes/kai.md)).

---

### Idée 2 : Le génie caché derrière la carte d'Uber

| Attribut | Valeur |
|---|---|
| **Titre** | Le génie caché derrière la carte en temps réel d'Uber |
| **Stratégie de trafic** | Accueil d'abord |
| **Mot-clé** | uber / comment fonctionne uber |
| **Concurrence** | Faible côté ingénierie en français (Jared a fait l'histoire business) |
| **Volume** | Non mesuré (sujet porté par l'accueil plutôt que la recherche) |
| **Tendance** | Stable : sujet intemporel |
| **Durée** | 10-12 min |
| **Niveau de RPM** | Moyen à élevé |
| **Urgence** | Evergreen. **Le 26 octobre** : montée en avance, en ligne en privé depuis le 21/10 |
| **Score** | **35/40** (demande 9 · clic 9 · production 7 · niche 10) |

**Hook** : « Ouvre Uber. Ces petites voitures qui bougent autour de toi ? Pour les afficher, Uber a dû découper la planète entière en hexagones. »
**Miniature** : carte sombre couverte d'hexagones lumineux, voitures en points blancs, texte « COMMENT ?! », noir et vert.
**Pourquoi** : c'est la vidéo la plus vue de la chaîne de Philipp Lackner (601 K, ×35,7), une chaîne de tutos Android comme l'était la tienne. Yeshendra Dhaker fait ×52 sur le même sujet.
**À vérifier** : la grille hexagonale H3 d'Uber (open source depuis 2018) et les chiffres de positions par seconde, sur le blog Uber Engineering.
**Source** : ton repérage + vidIQ.

---

### Idée 3 : WhatsApp et ses 50 ingénieurs

| Attribut | Valeur |
|---|---|
| **Titre** | Comment 50 ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes |
| **Stratégie de trafic** | Accueil d'abord |
| **Mot-clé** | whatsapp |
| **Concurrence** | Faible côté ingénierie en français (Thibaut Dcode a traité l'angle business le 4 oct.), forte en anglais |
| **Volume** | Non mesuré |
| **Tendance** | En hausse : Enrico Tartarotti vient de faire 1,5 M vues sur la messagerie (2 oct.) |
| **Durée** | 12-14 min |
| **Niveau de RPM** | Moyen |
| **Urgence** | Evergreen. **Le 11 janvier**, à bonne distance de la vidéo de Thibaut Dcode |
| **Score** | **35/40** (demande 9 · clic 9 · production 7 · niche 10) |

**Hook** : « 900 millions d'utilisateurs. 50 ingénieurs. Un ingénieur pour 18 millions de personnes. Comment c'est possible ? »
**Miniature** : logo WhatsApp géant, minuscule groupe de silhouettes en dessous, texte « 50 ? », vert et noir.
**Pourquoi** : « The Insane Design Of Messaging » fait ×23,5. Mais elle parle du **design** de la messagerie, pas des serveurs (2e vérif du 23/10) : elle prouve la demande, pas l'angle. WhatsApp est aussi l'appli n°1 de ton public africain : la vidéo sert tes deux audiences.
**Corrigé le 23/10** (`projets/whatsapp/sources.md`) : la cinquantaine d'ingénieurs pour 900 millions, c'est **en 2015** (Wired) ; au rachat de 2014, c'était une trentaine (32 ou 35 selon la source).
**À vérifier** : les chiffres (article de Wired de 2015 sur les 50 ingénieurs) et le rôle d'Erlang.
**Source** : ton repérage + vidIQ.

---

### Idée 4 : Ton pseudo est déjà pris

| Attribut | Valeur |
|---|---|
| **Titre** | Comment Google sait en une milliseconde que ton pseudo est déjà pris |
| **Stratégie de trafic** | Accueil + recherche |
| **Mot-clé** | pseudo déjà pris / comment ça marche |
| **Concurrence** | Faible en français |
| **Volume** | Non mesuré |
| **Tendance** | Stable |
| **Durée** | 8-10 min |
| **Niveau de RPM** | Élevé |
| **Urgence** | Evergreen. **Le 30 novembre** (reculé d'une semaine le 24/10), et joker du calendrier (il sort à la place d'une vidéo en retard) |
| **Score** | **33/40** (demande 7 · clic 9 · production 8 · niche 9) |

**Hook** : « Tape un pseudo. "Déjà pris." Réponse en une fraction de seconde, parmi des milliards de comptes. Le site ne les a pas tous vérifiés. Il a triché. »
**⚠️ À vérifier (21/10)** : aucune source ne montre que Google vérifie les pseudos avec un filtre de Bloom. C'est une technique classique (un tri rapide avant la base de données, qui décide toujours), mais les articles qui citent Google, Amazon ou Facebook ne donnent pas de source. Sans preuve, retirer Google du titre : *Comment un site sait en une milliseconde que ton pseudo est déjà pris*, et présenter le filtre de Bloom comme « la technique classique », pas comme celle de Google. Miniature retenue : `ressources/miniatures/rendus/noir-07.png` (« il triche. »), dont le « G » de Google suit la même règle.
**Miniature** : champ « pseudo » avec une croix rouge, chronomètre « 0,001 s », texte « IMPOSSIBLE ? ».
**Pourquoi** : ByteMonk fait 706 K vues (×22) sur ce sujet. C'est une seule astuce (le filtre de Bloom), donc des animations simples et une production légère.
**Source** : vidIQ (ByteMonk).

---

### Idée 5 : Le repo viral, version ArtCraft (le dev qui a recréé Adobe avec une IA)

| Attribut | Valeur |
|---|---|
| **Titre** | Il a recréé 7 logiciels Adobe avec une IA. J'ai testé son Photoshop. |
| **Stratégie de trafic** | Recherche (« artcraft ») + accueil |
| **Mot-clé** | artcraft / clone adobe gratuit |
| **Concurrence** | Forte en anglais (~45 vidéos en 5 jours), **faible en français** (3 ou 4 vidéos au 12 oct., aucune en récit) |
| **Volume** | Non mesuré |
| **Tendance** | En hausse : ArtCraft est sorti le 7 octobre |
| **Durée** | ~11 min (récit + un seul test : PhotoCraft) |
| **Niveau de RPM** | Élevé |
| **Urgence** | **Publiée le 19 octobre** sous le titre *Il a cloné TOUTES les applications ADOBE et c'est gratuit* |
| **Score** | **35/40** (demande 10 · clic 9 · production 8 · niche 8), rescorée le 12/10 : l'ancienne idée générique « repo viral » faisait 33/40 |

**Hook** : « Adobe lui a fait payer sa résiliation. Alors il a recréé Adobe. Sept logiciels, avec une IA. J'ai testé son Photoshop. » (l'histoire de la résiliation est à confirmer)
**Miniature** : un vrai PSD ouvert dans PhotoCraft, une facture « frais de résiliation » à côté, texte « GRATUIT ? ». Pas de logo Adobe.
**Pourquoi** : FUTC fait ×100 sa médiane avec ce sujet, Rough Cut Pete 292 K en un jour avec l'angle récit. REA (Eric Tech) avait déjà montré que « l'IA recrée un logiciel payant » surperforme. En français, personne ne raconte l'histoire.
**Garde-fou** : tu testes un projet open source publié, tu ne décompiles rien. Les noms Photoshop et Premiere servent seulement à comparer, sans logos Adobe.
**Source** : ton repérage (FUTC) + recherche YouTube du 12 oct.

---

### Idée 6 : Comment Waze voit les bouchons

| Attribut | Valeur |
|---|---|
| **Titre** | Comment Waze sait qu'il y a un bouchon avant que tu le voies |
| **Stratégie de trafic** | Accueil d'abord |
| **Mot-clé** | waze / comment fonctionne waze |
| **Concurrence** | Faible côté ingénierie ; l'angle business est pris (Thibaut Dcode, 1,09 M vues) |
| **Volume** | Non mesuré, mais **demande française prouvée** : 1,09 M vues sur Waze en un mois |
| **Tendance** | En hausse : la vidéo de Thibaut Dcode gagne encore environ 345 vues par heure |
| **Durée** | 10-12 min |
| **Niveau de RPM** | Moyen |
| **Urgence** | **Le 9 novembre** (avancée le 21/10), pendant que sa vidéo circule encore en suggestion |
| **Score** | **35/40** (demande 9 · clic 8 · production 8 · niche 10) |

**Hook** : « Waze t'a fait tourner à droite. Trois minutes plus tard, tu passes devant un accident que personne n'avait encore signalé. »
**Corrigé le 23/10** (`projets/waze/sources.md`) : Waze ne peut pas savoir qu'il y a un accident si personne ne le signale, il voit seulement que les voitures ralentissent. Le script dit « un ralentissement que personne n'avait signalé », sans « trois minutes ».
**Miniature** : écran Waze avec une route rouge, flèche qui l'évite, texte « IL SAVAIT », bleu clair.
**Pourquoi** : c'est la seule idée « génie » avec une preuve française directe (×4,6 chez Thibaut Dcode). La production est plus légère : tu réutilises les animations de carte faites pour Uber. **Ne refais pas l'angle « gratuité »** : toi, tu montres la machine (chaque téléphone sert de capteur de vitesse, les signalements, le calcul d'itinéraire).
**Source** : ton repérage (Thibaut Dcode).

---

### Idée 7 : Le guide IA en local 2027 (fusionnée dans l'idée 1)

| Attribut | Valeur |
|---|---|
| **Titre** | IA en local en 2027 : ce qu'il faut VRAIMENT pour la faire tourner |
| **Stratégie de trafic** | Recherche d'abord |
| **Mot-clé** | ia en local / ia local |
| **Concurrence** | Moyenne |
| **Volume** | Élevé : « ia en local » 24,7 K/mois, « ia local » 11 K/mois en France |
| **Tendance** | En hausse |
| **Durée** | 12-15 min |
| **Niveau de RPM** | Élevé |
| **Urgence** | **Fusionnée le 18/10 dans l'idée 1** (16 nov., avant le Black Friday). Fiche archivée dans `archive/guide-ia-local-2027/` |
| **Score** | **32/40** (demande 8 · clic 7 · production 8 · niche 9) |

**Hook** : « J'ai une RTX 5080. Et la moitié des IA que je voulais faire tourner ne rentrent pas dedans. »
**Miniature** : 3 cartes graphiques alignées, une barrée en rouge, texte « LE PIÈGE », fond sombre.
**Pourquoi** : Makertronic fait 23 K vues avec « IA Locale en 2026 : le hardware à acheter ». C'est ta vidéo de recherche durable, à mettre à jour chaque année.
**Source** : vidIQ (Makertronic).

---

### Idée 8 : Tu n'as jamais possédé tes jeux

| Attribut | Valeur |
|---|---|
| **Titre** | Tu n'as jamais possédé tes jeux |
| **Stratégie de trafic** | Accueil d'abord |
| **Mot-clé** | Sony PlayStation Store / Stop Killing Games |
| **Concurrence** | Moyenne |
| **Volume** | Non mesuré |
| **Tendance** | Stable : sujet récurrent |
| **Durée** | 14-18 min |
| **Niveau de RPM** | Moyen |
| **Urgence** | Evergreen. Provisoire : le 22 février |
| **Score** | **31/40** (demande 7 · clic 9 · production 7 · niche 8) |

**Hook** : « J'ai acheté ces jeux. J'ouvre la console : plus rien. Et c'est parfaitement légal. »
**⚠️ Corrigé (21/10)** : l'ancien titre disait « (et Sony vient de le prouver) ». C'est faux sur trois points :
- l'affaire date de décembre 2023, elle n'est pas récente ;
- elle concernait des **séries** Discovery achetées sur le PlayStation Store, pas des jeux ;
- Sony a fait marche arrière : un nouvel accord avec Warner Bros. garantissait l'accès « pendant au moins 30 mois », soit jusqu'à mi-2026 environ. Vérifier ce qui s'est passé depuis.

Pour prouver le titre avec un **jeu**, chercher un cas récent. Piste à sourcer : *The Crew* d'Ubisoft, rendu injouable en 2024, à l'origine de Stop Killing Games. Sony reste un bon exemple, à condition de dire « des séries » et « a failli », comme dans tes notes.
**Miniature** : manette PlayStation qui se désintègre en pixels, texte « PAS À TOI », fond bleu nuit.
**Pourquoi** : ARTE Info fait 53 K vues sur Stop Killing Games, et Hiz0 (1,4 K abonnés) 93 K avec un essai sur le jeu vidéo. C'est le premier récit à sortir si un créneau se libère.
**Source** : ton fichier `archive/autohebergement/notes.md`.

---

### Idée 9 : Le dev qui a mis un ChatGPT dans ton PC

| Attribut | Valeur |
|---|---|
| **Titre** | Le dev qui a mis un ChatGPT dans ton PC (l'histoire de llama.cpp) |
| **Stratégie de trafic** | Accueil d'abord |
| **Mot-clé** | ollama / lm studio |
| **Concurrence** | Faible (aucun récit français repéré) |
| **Volume** | Moyen : « ollama » 7,5 K/mois en France, « lm studio » 5,1 K/mois |
| **Tendance** | Stable |
| **Durée** | 15-18 min |
| **Niveau de RPM** | Élevé |
| **Urgence** | Evergreen. **Avancée au 8 févr.** le 23/10, à ta demande (à la place de Mobile Money) : le hook n'est donc plus l'anniversaire. Premier commit le 10/03/2023 (API GitHub) |
| **Score** | **29/40** (demande 6 · clic 7 · production 6 · niche 10) |

**Hook** : « Mars 2023. Un développeur bulgare publie un petit programme. Six mois plus tard, l'IA ne vit plus seulement dans les data centers. »
**Corrigé le 23/10** (`projets/llama-cpp/sources.md`) : « bulgare » n'est pas sourcé, on dit « de Sofia ». Deux actualités à revérifier avant la sortie : ggml.ai a rejoint Hugging Face (20/02/2026), et Nvidia a annoncé le rachat de Hugging Face (03/09/2026, accord annoncé, pas conclu).
**Miniature** : silhouette devant un écran de code, cerveau d'IA qui sort d'un PC, texte « IL A TOUT CHANGÉ ».
**⚠️ Corrigé (21/10)** : le titre disait « mis ChatGPT dans ton PC ». llama.cpp faisait tourner LLaMA, le modèle de Meta, pas ChatGPT ; « un ChatGPT » garde l'idée sans l'erreur. Vérifié : le README d'origine (mars 2023) dit « hacked in an evening ».
**Pourquoi** : il réunit tes deux piliers, et c'est un angle inédit en français.
**Source** : tes passions et l'écosystème Ollama.

---

### Idée 10 : Le génie caché du pixel

| Attribut | Valeur |
|---|---|
| **Titre** | Le génie caché du pixel : comment ton écran trompe tes yeux |
| **Stratégie de trafic** | Accueil d'abord |
| **Mot-clé** | pixel / comment fonctionne un écran |
| **Concurrence** | Moyenne |
| **Volume** | Non mesuré |
| **Tendance** | Stable |
| **Pilier** | Le génie derrière l'app (l'astuce cachée de l'écran ; [fiche](projets/ecran-blanc/fiche.md)) |
| **Durée** | 10-12 min |
| **Niveau de RPM** | Moyen |
| **Urgence** | Evergreen. Provisoire : **le 19 avril**. Le 14 déc. revient à l'hommage au jeu vidéo (idée 20), le 23/10 |
| **Score** | **27/40** (demande 7 · clic 8 · production 4 · niche 8) |

**Hook** : « Zoome sur l'écran de ton téléphone. Il n'y a pas un seul point blanc. Pourtant, tu vois du blanc partout. »
**Miniature** : macro d'un écran montrant des sous-pixels rouges, verts et bleus, texte « IL N'Y A PAS DE BLANC ».
**Pourquoi** : Andy Geers (1,1 K abonnés) fait ×431 avec « The Genius Trick Behind Exile's Impossible Map », et Enrico Tartarotti ×6,8 avec « The LIES That Make Hardware ACTUALLY Work ». L'angle « astuce cachée » est cliquable. Ton brouillon n'en fait plus partie : il raconte l'hommage au jeu vidéo (idée 20).
**À vérifier** : la structure des sous-pixels selon les écrans (certaines dalles de TV ont un sous-pixel blanc).
**Source** : ton idée + vidIQ.

---

### Idée 12 : Pourquoi tout paraît plus fluide sur un iPhone

| Attribut | Valeur |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) |
| **Stratégie de trafic** | Accueil + recherche |
| **Mot-clé** | iphone fluide / android qui rame (volume non mesuré) |
| **Urgence** | Evergreen. **Le 15 février**, provisoire (reculée du 7 déc. le 24/10, pour laisser la place à *IA en local*) ([fiche](projets/iphone-fluide/fiche.md)) |
| **Score** | **32/40** (demande 8 · clic 8 · production 7 · niche 9) |

**Hook** : « Pose ton doigt sur l'écran et fais défiler. La page colle à ton doigt. Ça n'a rien d'évident : Android a mis des années à y arriver. » (« des années » est à vérifier)
**Angle** : le génie du système, pas la guerre des marques : pourquoi l'affichage passe avant tout le reste quand ton doigt bouge, et ce qu'Android a changé pour rattraper son retard. Ton public africain est surtout sur Android : finis sur ce que son téléphone sait faire aujourd'hui.
**Pourquoi** : en français, les vidéos sur l'iPhone font des scores énormes (Nightech, « J'ai tenté d'utiliser le plus vieil iPhone encore à jour », 166,9 K en 3 jours). Le radar du 21/10 n'a trouvé aucune vidéo française sur la fluidité.
**À vérifier** : le rendu de l'interface sur iOS (Core Animation, priorité au rendu), le « Project Butter » d'Android 4.1 (2012), les écrans à 120 Hz des deux côtés.
**Source** : ton idée (`idees.md`).

---

### Idée 13 : Python, ou l'ennui d'un dev à Noël

| Attribut | Valeur |
|---|---|
| **Pilier** | Les grandes histoires de la tech (Hero) |
| **Stratégie de trafic** | Accueil |
| **Mot-clé** | python / histoire de python |
| **Urgence** | Saisonnier. **Le 28 décembre**, la semaine de Noël ([fiche](projets/python/fiche.md)) |
| **Score** | **31/40** (demande 7 · clic 8 · production 8 · niche 8) |

**Hook** (ta phrase) : « À quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation ? »
**Pourquoi** : en anglais, l'entretien de Guido van Rossum sur la chaîne GitHub fait 253 K vues (×40). Le récit se raconte sans essais, avec des animations simples, et la date de sortie colle à l'histoire.
**À vérifier** : la citation de Guido van Rossum sur le projet de loisir commencé pendant la semaine de Noël 1989 (préface de *Programming Python*, 1996) ; le nom tiré des Monty Python ; la date de la première version publique.
**Source** : ton idée (`idees.md`).

---

### Idée 14 : Ton téléphone est une brique (la preuve par Windows Phone)

| Attribut | Valeur |
|---|---|
| **Pilier** | Les grandes histoires de la tech (Hero) |
| **Stratégie de trafic** | Accueil |
| **Mot-clé** | windows phone / nokia lumia |
| **Urgence** | Evergreen. **Le 25 janvier** ([fiche](projets/windows-phone/fiche.md), ton texte dans le [brouillon](projets/windows-phone/brouillon.md)) |
| **Score** | **30/40** (demande 6 · clic 8 · production 7 · niche 9) |

**Hook** (ta phrase) : « Ton téléphone, quand tu le sors de la boîte, c'est une brique qui ne sert à rien. »
**Texte** : l'échec de Windows Phone. **Sous-texte** (recentré le 23/10) : ce sont nos applis qui font qu'on aime notre téléphone ; sans elles, c'est une brique.
**Angle** : Microsoft avait l'interface, Nokia avait les photos, et il manquait les applis que tout le monde utilise. Le cercle vicieux, c'est l'effet de réseau : sans applis, pas d'utilisateurs, et sans utilisateurs, pas d'applis. **Garde la partie « les applis étudient ton cerveau et vivent de tes données » courte** : c'est l'angle business de Thibaut Dcode. Elle peut faire une autre vidéo.
**Pourquoi** : c'est ton texte et ta passion. Pas de preuve française mesurée (le radar ne trouve que Windows 11), d'où le score de demande bas.
**À vérifier** (tes affirmations) : la date d'arrivée de WhatsApp sur Windows Phone (« des années ») ; l'absence d'appli Snapchat officielle ; le client Snapchat non officiel et son développeur (piste : 6snap, de Rudy Huyn, développeur français) ; l'anecdote « pour que sa copine puisse l'utiliser », à sourcer ou à retirer ; les ruptures entre Windows Phone 7, 8 et Windows 10 Mobile.
**Source** : ton idée (`idees.md`).

---

### Idée 15 : Louer, acheter ou s'abonner ?

| Attribut | Valeur |
|---|---|
| **Pilier** | IA chez moi, format **calculé** (Help) |
| **Stratégie de trafic** | Recherche + accueil |
| **Mot-clé** | ia en local rentable / abonnement claude prix |
| **Urgence** | Evergreen. **Le 4 janvier**, pour les bonnes résolutions (« je coupe mes abonnements ») ([fiche](projets/louer-acheter-ia/fiche.md)) |
| **Score** | **33/40** (demande 8 · clic 8 · production 8 · niche 9) |

**Hook** : « Un abonnement Claude, tous les mois. Ou une carte graphique, une seule fois. Au bout de combien de mois l'achat devient rentable ? » (les prix en euros se relèvent au moment du script)
**Pourquoi** : chez Kai, « Can a Mac Mini Replace your $200 AI Subscription? » fait 316 K vues (×8), et un fil de 52 likes demande « au bout de combien de temps ça devient rentable ? » ([`etudes/kai.md`](etudes/kai.md)). Pas d'électricité dans le calcul : le seul coût de l'achat est le prix de la carte (décidé le 23/10).
**Source** : étude Kai, idée 4.

---

### Idée 16 : Même carte, 2 fois plus rapide

| Attribut | Valeur |
|---|---|
| **Pilier** | IA chez moi, format **testé** (Hub) |
| **Stratégie de trafic** | Accueil + recherche |
| **Mot-clé** | ia en local plus rapide / llama.cpp |
| **Urgence** | Créneau radar (21/12 ou plus tard), quand un nouveau moteur ou une nouvelle compression fait parler |
| **Score** | **34/40** (demande 8 · clic 8 · production 8 · niche 10) |

**Hook** : « Même carte. Même modèle. Deux fois plus vite. Je n'ai rien acheté. »
**Pourquoi** : c'est le meilleur thème de Morgans Code (26,8 K vues médianes sur 7 vidéos ; « 6× Faster Than llama.cpp », 62,9 K). Lui le calcule, toi tu le mesures sur ta 5080 : moteur, compression, cache.
**Source** : [`etudes/morganscode.md`](etudes/morganscode.md).

---

### Idées 17 à 19 : génie, provisoires (février-avril)

| # | Idée | Preuve | Score | Créneau |
|---|---|---|---|---|
| 17 | ~~**Mobile Money : comment ton argent passe sans internet** (USSD)~~ **Abandonnée le 23/10** : elle ne te plaît pas (`archive/README.md`) | ByteMonk, « How UPI Works: Real-Time Payments in India » : 773 K, ×44. Le sujet parle aux 63 % de ton public en Afrique (Côte d'Ivoire, RDC, Cameroun) | 31/40 (7 · 8 · 7 · 9) | 8 févr. |
| 18 | **SQLite : sans cette base de données, ton téléphone ne marche pas** (corrigé le 23/10 : la bibliothèque fait 590 à 750 Ko, et DB-Engines classe Oracle 1er, SQLite 11e) | ByteMonk : 220 K, ×12,6 | 32/40 (7 · 8 · 8 · 9) | 22 mars |
| 19 | **Le génie caché du paiement sans contact** | ByteMonk, « The Hidden Security Magic Behind Mobile Payments » : 195 K, ×4,5 | 30/40 (7 · 7 · 7 · 9) | 5 avr. |

Chaque créneau se confirme au radar, deux semaines avant. Les faits (USSD et opérateurs, la page « Most Widely Deployed » de sqlite.org, la tokenisation des cartes) se vérifient à la source pendant l'écriture.

---

### Idée 20 : D'un pixel à 3,7 milliards de joueurs

| Attribut | Valeur |
|---|---|
| **Pilier** | Les grandes histoires de la tech (Hero) |
| **Stratégie de trafic** | Accueil |
| **Mot-clé** | jeux vidéo (24 K recherches/mois) ; « histoire du jeu vidéo » sous les 750/mois (vidIQ, 23/10) |
| **Urgence** | Evergreen. **Le 14 décembre**, juste avant Noël ([fiche](projets/pixel/fiche.md), ton texte dans le [brouillon](projets/pixel/brouillon.md)) |
| **Score** | **27/40** (demande 6 · clic 8 · production 6 · niche 7) |

**Hook** : « Un point blanc sur un écran noir. Cette année, 3,7 milliards de personnes jouent. »
**Texte** : l'histoire du jeu vidéo, de Pong aux MMORPG. **Sous-texte** : on est parti d'un pixel seul, et aujourd'hui des milliards de joueurs sont connectés (ta phrase : « ce pixel il ne peut pas exister seul dans ce monde »).
**Pourquoi** : c'est ton idée de départ et ta passion. En français, les essais sur le jeu vidéo dépassent souvent leur chaîne : Landry (7,6 K abonnés), « Les jeux vidéos sont une PERTE DE TEMPS. », 59 K, ×60 ; Kugen (1,2 K), 50 K, ×59 (vidIQ, 23/10). Aucun récit « de Pong à aujourd'hui » repéré sur les 6 derniers mois.
**À vérifier** : le nombre de joueurs (Newzoo : environ 3,58 milliards en 2025) ; Pong n'est pas le premier jeu vidéo (*Tennis for Two*, 1958 ; *Spacewar!*, 1962) ; les dates des premiers mondes en ligne. Le détail est dans la fiche.
**Source** : ton idée (`projets/pixel/brouillon.md`), précisée le 23/10.

---

### Idée 21 : Pourquoi tu meurs derrière un mur (le génie caché des jeux en ligne)

| Attribut | Valeur |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) : l'« appli », ici, c'est ton jeu en ligne |
| **Stratégie de trafic** | Accueil + suggestions |
| **Mot-clé** | lag / ping (« lag jeux en ligne » moins de 750 par mois en France ; « ping » 3,2 K en France, vidIQ 23/10) |
| **Urgence** | Evergreen. **Provisoire : le 8 mars**, choisi au radar du 23/10 à la place de Mobile Money ([fiche](projets/lag/fiche.md)) |
| **Score** | **32/40** (demande 7 · clic 9 · production 7 · niche 9) |

**Hook** : « Tu étais caché derrière un mur, et tu es mort. Sur l'écran de l'autre, tu n'étais pas encore caché : il t'a tiré dans ton passé, et le serveur lui a donné raison. » (confirmé par Bernier 2001, Riot et Respawn ; surtout vrai face à un gros ping)
**Texte** : comment un jeu en ligne fait croire que tout le monde est au même instant (prédiction, interpolation, compensation du lag, tick rate de 20 à 128).
**Sous-texte** : le jeu ment à tout le monde, et c'est ce mensonge qui le rend jouable ; le serveur décide quelle version devient la vérité.
**Pourquoi** :
- DeadInSperanza fait ×108 (13/10/2026) et Tariq10x 297 K sur ce thème ;
- aucune vidéo française ;
- un public de 18-24 ans joueurs ;
- Abidjan–Johannesburg est aussi loin qu'Abidjan–Paris, et cela parle aux 63 % d'Afrique.
**Source** : radar du 23/10 (`etudes/radar.md`).

---

### Idée 22 : IA en local : comment lire le nom d'un modèle (35B, A3B, Q4_K_M…)

| Attribut | Valeur |
|---|---|
| **Pilier** | IA chez moi (Help) : la vulgarisation, le guide de lecture de la série |
| **Stratégie de trafic** | Recherche (« ia en local ») + suggestions à côté des vidéos « IA locale pour débutants » |
| **Mot-clé** | ia en local (21 403 par mois, +91 % sur 30 jours ; « gguf » et « c'est quoi un llm » moins de 750 par mois en France, vidIQ 23/10) |
| **Urgence** | Evergreen. **Le 7 déc.**, la deuxième marche après la vidéo d'installation (idée 25) : ta décision du 24/10 (nuit). D'abord placée au 30 nov., puis au 2 nov. le 23/10 ([fiche](projets/bases-ia-locale/fiche.md)) |
| **Score** | **31/40** (demande 7 · clic 7 · production 8 · niche 9) |

**Hook** : « Qwen trois point six, trente-cinq B, A trois B, UD, IQ quatre XS, point gguf. On dirait un mot de passe Wi-Fi. En fait, c'est une IA, en local. Dix-huit gigas. Sauf que ma carte graphique en a seize. »
**Texte** : lire le nom d'un modèle morceau par morceau, puis tout ce qui l'entoure : modèle → fichier → moteur → API → (routeur) → harnais → toi ; local n'est pas open source (définition de l'OSI).
**Sous-texte** : ce vocabulaire a l'air d'un code d'initiés, c'est juste un code.
**Pourquoi** :
- aucune vidéo, ni en français ni en anglais, ne déchiffre un nom de fichier de modèle ;
- Tech With Tim fait 821 K (×11) avec un tour d'horizon de l'IA locale ;
- Mark Kashef montre qu'une vidéo de 44 min qui veut tout dire ne marche pas : on reste à 13 min, sur le fil du nom.
**Source** : recherche du 23/10 (`projets/bases-ia-locale/sources.md`).

---

### Idée 23 : Deux cartes d'occasion pour le max de VRAM

| Attribut | Valeur |
|---|---|
| **Pilier** | IA chez moi (Help) : **calculé** (pas d'achat, ta décision du 24/10) |
| **Stratégie de trafic** | Recherche (« ia en local ») + suggestions à côté des vidéos matériel anglaises (TinyTechGuy, Digital Spaceport, RepoChad) |
| **Mot-clé** | ia en local (21 403 par mois, +90,8 %) ; « carte graphique occasion ia » et « 2 cartes graphiques ia » : moins de 750 chacun (vidIQ 24/10) |
| **Urgence** | Evergreen, mais les prix bougent. **Le 21 déc.** (créneau radar IA, ta décision du 24/10) : avant Noël et avant Louer, acheter (4 janv.) ([fiche](projets/deux-cartes-occasion/fiche.md)) |
| **Score** | **29/40, estimation** (demande 6 · clic 7 · production 7 · niche 9) : sans test, le clic baisse un peu, la production monte |

**Hook** : d'après mon calcul, le modèle que ta 5080 refuse (le Q4 de Qwen3.8-27B, 16,46 Go) tiendrait sur deux cartes d'occasion, à [PRIX D'OCCASION À RELEVER].
**Texte** : combien de VRAM par euro d'occasion, comment llama.cpp répartit un modèle sur deux cartes (la mémoire s'additionne, pas la vitesse), ce qui tient à 24, 32, 40 et 48 Go, la garantie en France.
**Sous-texte** : la mémoire compte plus que la puissance, et elle se trouve d'occasion, à condition de savoir où sont les pièges.
**Pourquoi** :
- aucune vidéo française sur le multi-GPU d'occasion pour l'IA (vidIQ, 24/10) ;
- en anglais, TinyTechGuy fait 60 K vues en une semaine sur ce thème ;
- elle nourrit les conseils d'occasion de Claude #1 et de Louer, acheter.
**Source** : recherche et 2e vérification du 24/10 (`projets/deux-cartes-occasion/sources.md`).

---

### Idée 24 : Mac mini ou PC gamer pour l'IA en local ?

| Attribut | Valeur |
|---|---|
| **Pilier** | IA chez moi (Help), calculé : série « Abonnement ou IA locale ? » |
| **Stratégie de trafic** | Recherche (« mac mini ia », « ia en local ») + suggestions à côté de Locally et des vidéos sur le Mac mini M6 |
| **Mot-clé** | ia en local (21 403 par mois, +90,8 %, vidIQ 24/10) ; « mac mini ia » à mesurer |
| **Urgence** | Le Mac mini M6 est sorti fin août 2026 : **le 1er févr.**, provisoire (créneau radar IA, ta demande du 24/10) ([fiche](projets/mac-mini-ia/fiche.md)) |
| **Score** | **30/40, estimation** (demande 7 · clic 8 · production 7 · niche 8) |

**Hook** : « Ce modèle refuse de tourner sur ma RTX 5080. D'après mon calcul, un Mac mini le fait tenir. Sauf qu'il l'écrirait environ cinq fois moins vite. » (chiffres à vérifier)
**Texte** : pour l'IA en local, la taille de la mémoire décide de ce qui tourne, sa vitesse décide à quelle vitesse.
**Sous-texte** : le meilleur PC pour jouer n'est pas forcément le meilleur pour l'IA.
**Pourquoi** :
- Locally fait ×21,9 avec le Mac mini M6 pour l'IA locale (26/08/2026) ;
- rien en français dans la recherche YouTube (vidIQ, 24/10) ;
- elle relie les deux cartes d'occasion (21 déc.), Coût Claude (le Mac Studio) et la série.
**Source** : [vidéo de Locally](https://www.youtube.com/watch?v=evkv0_HrhFM) ; recherche et double vérification à faire.

---

### Idée 25 : Pourquoi avoir ta propre IA, et comment l'installer (LM Studio)

| Attribut | Valeur |
|---|---|
| **Pilier** | IA chez moi (Help), testé : la toute première marche de la série « Abonnement ou IA locale ? » |
| **Stratégie de trafic** | Recherche (« ia en local », « lm studio », « ollama ») + suggestions à côté des vidéos « IA locale pour débutants » du mois |
| **Mot-clé** | ia en local (18 376 à 21 403 par mois selon l'appel, vidIQ 24/10) ; installer ia en local (4 531, concurrence 28, vidIQ 24/10) ; ollama (9 849 en France) et lm studio (2 581 en France), vidIQ 23/10 |
| **Urgence** | Evergreen, mais c'est la base de tout le pilier : **le 2 nov.** (ta décision du 24/10, nuit) ([fiche](projets/installer-ia-locale/fiche.md)) |
| **Score** | **34/40, estimation** (demande 9 · clic 7 · production 9 · niche 9) |

**Hook** : « Je coupe le wifi. Et mon IA me répond quand même. Le 12 juin, Anthropic a coupé Fable 5, le modèle le plus puissant qu'il ait jamais ouvert au public. Pour tout le monde. Trois jours après sa sortie. » (vérifié deux fois le 24/10 : directive du gouvernement américain, retour 19 jours plus tard)
**Texte** : une IA en local, c'est un fichier chez toi et une appli qui le fait tourner ; avec LM Studio, ça s'installe comme un jeu.
**Sous-texte** : ce que tu ne possèdes pas, on peut te le retirer.
**Pourquoi** :
- un débutant n'a pas besoin des noms (« Q4_K_M ») avant d'avoir lancé un modèle : la vidéo des noms devient la deuxième marche (7 déc.) ;
- Claude #1, Coût Claude et les deux cartes peuvent renvoyer à « installe d'abord avec cette vidéo » ;
- Fable 5 coupé puis revenu : la preuve que ni toi ni même le fournisseur ne décidez toujours ;
- LM Studio est gratuit au travail : l'argument des données privées en entreprise tient sans licence.
**Source** : `projets/installer-ia-locale/sources.md` (recherche et double vérification du 24/10).

---

### Mises de côté
- **30 jours avec une IA locale** : trop lent face au rythme des sorties. Remplacé par la série « Claude ou mon PC ? ».
- **Windows 10** : ni vidéo longue ni Short (le Short n'est pas sorti ; archivé le 19/10).
- **Streaming +71 %, Plex, maison pilotée par IA, l'IA dans ta carte graphique** : en réserve. Ils resservent si un créneau se libère ou à 10 K abonnés.
- **Vieux PC → console, NAS** : pas ta passion.
- **Les Shorts** : arrêtés le 21/10, avant la fin du test (voir section 0). Le Short Vorssaint reste [archivé](archive/short-vorssaint/fiche.md).

---

### Classement

| Rang | Idée | Titre | Format | Score | Créneau |
|---|---|---|---|---|---|
| 1 | 1 | 16 Go de VRAM suffisent-ils pour remplacer Claude ? | IA testé | 36/40 | 16 nov |
| 2 | 2 | Le génie caché derrière la carte en temps réel d'Uber | Génie | 35/40 | 26 oct |
| 3 | 6 | Comment Waze sait qu'il y a un bouchon avant que tu le voies | Génie | 35/40 | 9 nov |
| 4 | 3 | Comment 50 ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes | Génie | 35/40 | 11 janv |
| 5 | 5 | ArtCraft : il a recréé 7 logiciels Adobe avec une IA | IA récit | 35/40 | Publiée le 19 oct |
| 6 | 11 | Combien coûte Claude en local ? ([fiche](projets/cout-claude-local/fiche.md)) | IA calculé | 34/40 (9 · 9 · 7 · 9) | 23 nov |
| 7 | 16 | Même carte, 2 fois plus rapide | IA testé | 34/40 | Radar |
| 8 | 4 | Comment un site sait en une milliseconde que ton pseudo est déjà pris (« en une milliseconde » gardé le 23/10 : tenu côté serveur, doc de Redis) | Génie | 33/40 | 30 nov (joker) |
| 9 | 15 | Louer, acheter ou s'abonner ? | IA calculé | 33/40 | 4 janv |
| 10 | 12 | Pourquoi tout paraît plus fluide sur un iPhone | Génie | 32/40 | 15 févr (provisoire, reculée le 24/10) |
| 11 | 18 | SQLite : *Sans cette base de données, ton téléphone ne marche pas* (titre du 23/10 ; « 300 Ko » et « battu Oracle » sont faux) | Génie | 32/40 | 22 mars (provisoire) |
| 12 | 8 | Tu n'as jamais possédé tes jeux | Histoire | 31/40 | 22 févr (provisoire) |
| 13 | 13 | *Python, le langage de l'IA, est un cadeau de Noël* (titre du 23/10 ; Guido ne dit jamais qu'il s'ennuyait, et Codabee a pris « Il s'ennuyait à Noël ») | Histoire | 31/40 | 28 déc |
| — | 17 | ~~Mobile Money : comment ton argent passe sans internet~~ | Génie | 31/40 | Abandonnée le 23/10 |
| 15 | 14 | Ton téléphone est une brique (la preuve par Windows Phone) | Histoire | 30/40 | 25 janv |
| 16 | 19 | Le génie caché du paiement sans contact | Génie | 30/40 | 5 avr (provisoire) |
| 17 | 9 | Le dev qui a mis un ChatGPT dans ton PC (llama.cpp) | Histoire | 29/40 | 8 févr (provisoire, avancée le 23/10) |
| — | 21 | Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne | Génie | 32/40 | 8 mars (provisoire, radar du 23/10) |
| — | 25 | Pourquoi avoir ta propre IA, et comment l'installer (LM Studio) | IA testé (vulgarisation) | 34/40 (estimation) | 2 nov (ta demande du 24/10 : la base d'abord) |
| — | 22 | IA en local : comment lire le nom d'un modèle (35B, A3B, Q4_K_M…) | IA calculé (vulgarisation) | 31/40 | 7 déc (après la vidéo d'installation, 24/10) |
| — | 23 | Deux cartes d'occasion pour le max de VRAM | IA calculé | 29/40 (estimation) | 21 déc (ta demande du 24/10) |
| — | 24 | Mac mini ou PC gamer pour l'IA en local ? | IA calculé | 30/40 (estimation) | 1er févr (provisoire, ta demande du 24/10) |
| 18 | 20 | D'un pixel à 3,7 milliards de joueurs | Histoire | 27/40 | 14 déc (passion) |
| 19 | 10 | Le génie caché du pixel : comment ton écran trompe tes yeux | Génie | 27/40 | 19 avr (provisoire) |
| — | 7 | ~~IA en local en 2027 : ce qu'il faut VRAIMENT pour la faire tourner~~ | — | — | Fusionnée dans l'idée 1 |
| — | — | Claude ou mon PC ? #2 (suite de l'idée 1, dernier modèle sorti) | IA testé | — | 18 janv |
| — | — | OpenCode piraté (actu, hors classement) | IA récit | — | Publiée le 21 oct |

Python et l'hommage au jeu vidéo passent devant des idées mieux notées pour des raisons de calendrier (Noël) et de passion.

### Ordre de production

**Cette semaine (21-25 oct.)** :
- **Uber**, en ligne en privé :
  - remplacer le titre « L'hisoire du temps réel derriere uber » par celui de la fiche ;
  - remplacer les tags Flutter par défaut ;
  - appliquer le kit d'upload ([`projets/uber/upload.md`](projets/uber/upload.md), prêt le 21/10) ;
  - programmer la vidéo lun. 26 à 18 h.
- **Essais sur la 5080 (ven. 23 et sam. 24)**, puis la **vidéo d'installation** (2 nov. : recherche, script et capture) et le script de **Claude #1** (16 nov.).
- Script v2 de **Combien coûte Claude en local ?** (23 nov.) : fait le 22/10, à compléter avec les essais.

**Ensuite** : l'ordre du [calendrier](calendrier.md), qui donne aussi le détail semaine par semaine jusqu'au 31 janvier. Les créneaux radar se remplissent à chaque sortie ([`etudes/radar.md`](etudes/radar.md)).
