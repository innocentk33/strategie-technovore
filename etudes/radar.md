# Radar Technovore

> À chaque sortie d'une vidéo, on refait le radar : la procédure est dans [`CLAUDE.md`](../CLAUDE.md), section « Radar ». L'entrée la plus récente est en haut. Tous les chiffres viennent de vidIQ et sont datés.

## Liste de surveillance

À passer en un seul appel `vidiq_outliers` par langue (`channelIds`, `publishedWithin: thisMonth`).

| Chaîne | Langue | Pourquoi | ID |
|---|---|---|---|
| Kai | EN | IA locale : coût et matériel ([étude](kai.md)) | `UCgUfJoPtkt7-RiiuYh4vmGA` |
| Morgans Code | EN | IA locale : calculs sans tests ([étude](morganscode.md)) | `UCetGP9xk9LYIxzYO9Id3o6g` |
| Code Unpacked | EN | IA locale : « même carte, plus rapide » ([étude](outliers-2026-10-22.md)) | `UCuXX9B1kSwRTQE2BIhK7Khw` |
| ByteMonk | EN | Le génie derrière l'app | `UCzCsyvyrq38R6TnztEzOmgg` |
| Thibaut Dcode | FR | Applis et marques, angle business | `UCNew6vrycRR0QnlYmLoMRZg` |
| Makertronic Tech | FR | Matériel, IA, histoire de la tech | `UCjBWE9WaXEtkqad7F68W5OQ` |
| Le Lab IA (Jerome Fortias) | FR (BE) | IA en local | `UC4PY6oWBZjLg32a3z2zrUKw` |
| Baptiste Simard | FR | Claude Code, vibe coding | `UCzabGLybo9x307MkDtqTyFQ` |
| Machine Learning Lab | FR | « Comment ça marche » sur l'IA | `UCu34JW8lOyx_1vElmxqyUew` |
| Bricolo2.0 | FR | IA gratuite à la maison | `UCPC2ZL10br9fuhvhvuKh13g` |
| FEU | FR | IA en local, agents | `UCvgcGOW3UQskqWboU1VDX9A` |
| RepoChad | EN | IA locale : matériel et VRAM (« Every Way to Get X GB of VRAM… ») | `UCtyEhOTxGx45sljlfryc6jw` |
| Weights & Wonders | EN | IA locale : GPU et prix, voix IA, actu Qwen | `UC6dYyJvl6mj6Xu1vCFsl-6A` |

**Mots-clés français** (`vidiq_outliers`, `language: fr`, `threeMonths`) : « IA en local », « comment ça marche », « Qwen 4 », « VRAM », « carte graphique IA », et le nom de l'appli ou du modèle des prochains créneaux.

---

## 21/11/2026 — Radar evergreen du jeudi 7 janvier

**Décision.** [Un assistant vocal sans Internet : que peut faire ton PC ?](../projets/assistant-vocal-local/fiche.md) prend le créneau de 18 h. La question reste valable quand les modèles changent. L’angle calculé rend possible le sujet « JARVIS » de la réserve, auparavant écarté à cause de la charge du test filmé. Le spectateur pourra choisir entre une commande domestique et une conversation libre.

**Signaux disponibles.** Aucun accès vidIQ dans cette session. Le relevé du 19/11 ci-dessous donne deux vidéos du Lab IA sur un assistant local à 14,7 k vues chacune (×2,43 et ×2,36). Le relevé YouTube du 15/11 donne 75,5 k vues en sept jours pour [l’assistant sur PC de Parlons Cyber](https://www.youtube.com/watch?v=7Y-IU77_ZF0). Sur notre chaîne, Strata avait atteint 348 vues à J+3, avec 47,7 % du public encore là à 30 secondes. D’où le choix d’ouvrir sur une commande et son temps de traitement. Les relevés disponibles ne donnent ni le J+7 de Strata ni les performances de la sortie du 19/11.

| Candidat | Demande | Clic | Production | Niche | Total et arbitrage éditorial |
|---|---:|---:|---:|---:|---|
| Assistant vocal hors ligne | 8 | 9 | 9 | 10 | **36/40**. Signal français et comparaison documentée, sans tournage. |
| Choisir son modèle selon sa VRAM | 9 | 8 | 8 | 10 | **35/40**. Besoin durable déjà couvert le 21 janvier. |
| Cartes de minage pour l’IA | 7 | 9 | 7 | 9 | **32/40**. Bon clic, mais le prix d’un lot exceptionnel se généralise mal. Épisode au 25 janvier. |

Les scores sont des estimations éditoriales. Les mesures techniques à utiliser pour le sujet retenu sont liées dans sa fiche.

## 19/11/2026 : sortie de Strata (16/11) à J+3, radar allégé et volet « 32 Go », calendrier inchangé

**Contexte** : « Le meilleur modèle possible pour 16 Go de VRAM » est sortie le lun. 16/11 à 18 h : https://youtu.be/892vB0mRY8U. Le radar du 16/11 n'avait pas été fait ; celui-ci le remplace. Le forfait vidIQ est gratuit : 830 crédits avant, 780 après, **50 dépensés** (1 appel `vidiq_user_videos` + 9 chaînes à 5 crédits ; 55 renouvelables, 725 en bonus). Comme le 12/11, `vidiq_outliers`, `vidiq_channel_analytics` et `vidiq_channel_stats` manquent : les concurrents passent par `vidiq_channel_videos` (vues, vues/h, multiplicateur « breakout » donné par vidIQ). Les vidéos hors liste de surveillance (volet 32 Go) viennent de recherches web et des pages YouTube du 19/11 : leurs multiplicateurs sont **non mesurés**.

### Notre chaîne

**Studio (relevé du 19/11 vers 6 h 50 UTC, via vidIQ, déjà fait avant ce radar)** :

- Strata, du 16 au 19/11 : **877 impressions, CTR 6,73 %** (Studio affiche 822 et 7,2 %) ; **348 vues**.
- Sources des impressions : accueil et navigation 687 (7,71 %), recherche 106 (4,72 %), suggestions 31 (0 %), page de chaîne 16 (0 %). Sources des vues : navigation 88,5 %, recherche 5,7 %, suggestions 2,0 %.
- Durée moyenne 2:30 à 2:46 sur 9:35 (28 %), **47,7 % des spectateurs restants à 0:30**.
- Comparaison : « 16 Go » (jMZFDNbwRNI) : 3 347 impressions et 3,29 % du 9 au 19/11, mais 2 264 impressions et 1,99 % sur ses trois premiers jours ; Qwen 4 (JuiZAwEiX-o) : 2 683 impressions, 3,32 %.
- Test A/B de Strata : il porte sur le **titre et la miniature** (le kit prévoyait l'image seule) ; en cours, trop peu de données. Sur la page publique du 19/11, le titre affiché est *Le meilleur modèle possible pour 16 Go de VRAM (Qwen 3.8 Flash-Next/Strata)* et non « (Strata, testé) » comme dans le README et le calendrier : c'est peut-être la variante du test A/B (non vérifié : `upload.md` ne contient pas ce titre) ; à ne pas recopier dans les tableaux avant le verdict.

**Vues et likes (`vidiq_user_videos`, 19/11)** :

| Vidéo | Sortie | Recul | Vues | Likes / commentaires | Likes pour 100 vues |
|---|---|---|---|---|---|
| Strata, « Le meilleur modèle possible pour 16 Go de VRAM » | 16/11 | J+3 | 331 | 2 / 0 | 0,6 |
| Qwen 4 quelle carte graphique acheter (ou pas) ? | 12/11 | J+7 | 452 | 2 / 1 | 0,4 |
| 16 Go de VRAM : est-ce vraiment suffisant pour les LLM ? | 09/11 | J+10 | 662 | 12 / 4 | 1,8 |
| Comment utiliser une IA sans internet sur ton PC | 02/11 | J+17 | 375 | 6 / 7 | 1,6 |
| Uber : l'illusion parfaite du temps réel | 26/10 | J+24 | 227 | 6 / 0 | 2,6 |
| OpenCode a été gravement piraté | 21/10 | J+29 | 494 | 4 / 1 | 0,8 |
| ArtCraft (« Il a cloné toutes les applications Adobe ») | 19/10 | J+31 | 618 | 7 / 1 | 1,1 |

(Les deux compteurs de Strata diffèrent : 331 vues pour vidIQ (public), 348 pour le relevé de Studio de 6 h 50 UTC ; je n'explique pas l'écart. Les likes pour 100 vues sont un calcul de ma part.)

- **Strata à J+3 : 331 vues**, contre 285 pour « 16 Go » au même recul (radar du 12/11). Le volume tient, mais les likes sont à **0,6 pour 100 vues contre 1,8** pour « 16 Go » : le public touché est plus froid. Cela colle au diagnostic de Studio : bon CTR (6,73 %) sur un public restreint, et c'est la rétention à 30 s qui freine.
- **« 16 Go » à J+10 : 662 vues** (285 à J+3), la meilleure vidéo récente. **Qwen 4 à J+7 : 452 vues**, 2 likes.
- **Aucune vidéo publique n'a un statut faux** dans le README : Qwen 4 et Strata sont « Publié ». Il reste le Short du 11/10 (*Ce PC à 70 € remplace mes abonnements*, 804 vues, 2 likes), antérieur à la décision « zéro Short » du 21/10, qui n'est pas dans le tableau ; je n'y ai pas touché.
- **Non mesuré** : la rétention de Strata au-delà de 0:30, les 5 premières sources de suggestions, la part de la France (`vidiq_channel_analytics` manque ; `vidiq_channel_analytics_extended` n'a pas été rappelé : le CTR et les impressions venaient déjà de Studio).

### Concurrents (`vidiq_channel_videos`, 19/11)

Ce qui fait ×2 ou plus sur les trois dernières semaines (vues à la date du relevé, multiplicateur donné par vidIQ) :

- **Kai** (EN) : *Basalt Runs Qwen 3.8 Flash Next At 224 Token/sec* (86,0 K, **3 594 vues/h**, ×2,94, 18/11) ; *Apple's Local AI App for Mac Is Coming (Harbor)* (133,4 K, ×2,43, 12/11) ; *I Tested Every Uncensored Local AI Model (8GB to 32GB VRAM)* (89,7 K, ×2,02, 15/11) ; *You Don't Need an Expensive GPU Anymore (Strata 100 tok/s)* (289,1 K, ×3,38, 01/11) ; *Your Local AI Is Not as Private as You Think* (613,7 K, ×5,33, 21/10). Sous le seuil : *I ran Qwen3.8 27B on $78 Card!* (70,9 K, ×1,76, 17/11).
- **Weights & Wonders** (EN) : *Watch This Before Building a Multi-GPU Local AI Setup!* (50,2 K, ×5,04, 12/11) ; *11 GPUs You Should Get for Local AI Before Qwen 4's Release!* (106,8 K, ×14,98, 08/11). *I Built THE BEST Local AI Stack for 32GB VRAM!* (12,4 K, ×1,26, 10/11) reste sous le seuil.
- **Morgans Code** (EN) : *Don't Buy a GPU for Local AI Until You See This (3090, P100, V100)* (23,6 K, ×2,42, 02/11) ; *Someone Built the Qwen MoE Alibaba Hasn't Released. I Tested It.* (12,2 K, ×2,11, 16/11) ; *You Don't Need an Expensive GPU Anymore? Strata Changes Local AI* (42,0 K, ×4,32, 31/10). Nouvelle vidéo sur notre créneau du 23/11 : *Can an 8GB GPU Finally Match Qwen 3.8 27B? (SenseNova Loop)* (1,2 K, 18/11, multiplicateur non disponible, 104 vues/h). Et sur notre créneau du 14/12 : *What Would It Cost to Run Claude Fable 5.2 Locally?* n'a fait que **1,3 K vues** en 7 jours (12/11) : le signal « combien coûte Fable » est faible pour l'instant.
- **RepoChad** (EN) : *Run FULL DeepSeek v4.1 Flash on a 12GB GPU* (56,4 K, ×2,51, 02/11, utile au DeepSeek du 03/12) ; *I Actually Spied on My "Local AI". Didn't Expect This!* (105,9 K, ×4,88, 25/10, proche de notre « IA locale privée » du 11/01) ; *Every Way to Get 256 GB of VRAM for Local AI* (208,5 K, ×9,56, 19/10). Plus récent : *Qwen 4 27B is Coming: Buy a GPU Now or Wait?* (12,8 K en un jour, 283 vues/h, 18/11) et *Tencent Hy4 Flash Is Out. Time to Ditch Qwen 3.8 Flash Next?* (18,0 K, ×1,67, 18/11).
- **Code Unpacked** (EN, petite chaîne : les multiplicateurs sont gonflés par une base minuscule, à ne pas lire comme des ×) : *llama.cpp 1.0 Is Here — Can It Finally Catch Strata?* (39,7 K, 14/11) ; *Qwen 4 Is Here — 2.4 Trillion Parameters, Just 71B Active* (3,7 K, 18/11) : d'après ce seul titre, un très gros modèle Qwen 4 serait disponible (RepoChad titre déjà sur Qwen4-Max le 16/11), **pas le 27B** (RepoChad le dit « en approche » le 18/11) ; aucune date de sortie à en tirer, à vérifier avant d'écrire quoi que ce soit.
- **Makertronic Tech** (FR) : *NVIDIA a BRIDÉ ta RTX… on la débloque et c'est violent !* (52,8 K, ×2,53, 25/10), le même sujet que Kai (146,5 K, ×1,58, 27/10) et Morgans Code (26,1 K, ×2,6, 25/10) ; depuis, rien à ×2 (*FUITE AMD : de la GDDR7 dans un APU…*, 11,9 K, 114 vues/h, 15/11 ; *192 Go de VRAM*, 26,4 K, ×1,44, 08/11).
- **Le Lab IA** (FR, BE) : *Dispo sur Github votre IA locale à la sauce Jarvis (Kaonomi)* (14,7 K, ×2,43, 01/11) et *Démonstration REELLE de mon Jarvis Kaonomi* (14,7 K, ×2,36, 23/10) : un assistant vocal local plaît au public français, même sur une petite chaîne. Rien à ×2 en novembre sinon.
- **FEU** (FR) et **Bricolo2.0** (FR) : rien à ×2 en novembre (FEU : 0,6 à 1,3 K vues sur ses dernières vidéos ; Bricolo2.0 : 1,0 K, hors IA).

**Strata chez les concurrents** : Kai (289 K), Morgans Code (42 K) et Code Unpacked (plusieurs vidéos, dont celle du 14/11) en parlent tous. La demande existe en anglais ; chez nous, 331 vues à J+3.

### Public français

Pas d'appel `vidiq_outliers` possible. Seuls signaux : Makertronic sur « NVIDIA bridé » (×2,53, 25/10) et Le Lab IA sur le « Jarvis » local (×2,4, deux vidéos).

### Volet « 32 Go » (pour la vidéo du lun. 30/11, d'après RepoChad)

> Méthode : les 9 chaînes de la liste de surveillance par `vidiq_channel_videos` (vues du 19/11, multiplicateur « breakout » de vidIQ), plus des recherches web (US) et les pages YouTube du 19/11 pour les autres chaînes. **Non mesuré** : tout multiplicateur absent du tableau ; les descriptions ne sont pas des mesures ; je n'ai pas vu le contenu détaillé des vidéos hors liste.

**Notre source, RepoChad** : *Best Ways to Get 32GB VRAM for Qwen3.8-27B (Full Context)*, 15/09, **277,6 K vues, ×11,38**, 17 min. Son sujet n'a pas été repris en français dans ce que j'ai vu.

| Vidéo | Chaîne | Date | Vues | Multiplicateur | Ce que ça apporte |
|---|---|---|---|---|---|
| *I ran Qwen3.8 27B on $78 Card! (Better than expected)* | Kai | 17/11 | 70,9 K | ×1,76 | Deux Tesla P100 16 Go = 32 Go ; d'après la description, 67 tok/s avec un fork de llama.cpp, MTP et tensor split, contre 17 tok/s un mois avant, et **le prix a bougé après la vidéo virale** |
| *Every Ways to Get 32GB VRAM for Local AI at Full Context* | Kai | 03/10 | 147,7 K | ×1,61 | Description : une carte Tesla d'occasion à ~19 $ le Go dont **le pilote actuel ne gère plus la carte** ; un Mac de 32 Go ne donne que 21,3 Go au GPU ; deux cartes de 16 Go ≈ 28 Go utiles ; la lecture du prompt est 5 fois plus rapide sur une carte que sur une autre |
| *I Tested Every Uncensored Local AI Model (8GB to 32GB VRAM)* | Kai | 15/11 | 89,7 K | ×2,02 | Le palier 32 Go sert de repère haut ; pas un test de matériel |
| *54GB VRAM For $35 The Cheapest Local AI Hack?* | Kai | 14/11 | 47,0 K | non disponible | Voie « ancienne carte bon marché » (même sujet que *cartes-minage*, 21/01) |
| *Don't Buy a GPU Instead Build This 32GB Free AI Server Instead* | Kai | 12/10 | 448,0 K | ×5,95 | 32 Go « gratuits » (deux Tesla T4 sur Kaggle, hors de chez soi) : le chiffre « 32 Go » seul porte, même sans achat |
| *I Built THE BEST Local AI Stack for 32GB VRAM! ($20 Plan is Gone!)* | Weights & Wonders | 10/11 | 12,4 K | ×1,26 | Palier 32 Go, comparé à un abonnement à 20 $ |
| *Watch This Before Building a Multi-GPU Local AI Setup!* | Weights & Wonders | 12/11 | 50,2 K | ×5,04 | Les pièges du multi-GPU : c'est notre vidéo du 07/12 |
| *Don't Buy a GPU for Local AI Until You See This (3090, P100, V100)* | Morgans Code | 02/11 | 23,6 K | ×2,42 | Compare V100 et P100 d'occasion à une 3090 |
| *AMD R9700 vs RTX 5090 for Local AI: Worth 2.5x the Price?* | RepoChad | 23/10 | 25,6 K | ×1,16 | R9700 32 Go contre RTX 5090 : « 2,5 fois le prix » |
| *AMD R9700 vs Intel Arc Pro B70 for Local AI: Which Is Worth It?* | RepoChad | 30/09 | 50,1 K | ×1,05 | Les deux cartes pro de 32 Go face à face |
| *Best Ways to Run Qwen3.8-27B on Dual RTX 5060 Ti Cards* | RepoChad | 25/09 | 25,0 K | non disponible | La route « deux cartes de 16 Go » |
| *Intel Arc Pro B70: Qwen3.8 on One and Two GPUs with vLLM, llama.cpp and Strata* | Donato Capitella | 02/11 | 37,8 K | non mesuré | B70 seule et à deux, avec Strata |
| *Qwen3.8 27B and Flash Next on Single/Dual AMD Radeon 9700: Engine Benchmarks and Setup* | Donato Capitella | 16/10 | 41,4 K | non mesuré | R9700 seule et à deux ; description : sponsoring AMD |
| *nVidia Tesla V100 als LLM Grafikkarte mit 32 GB: KI-Schnäppchen oder teurer Fehlkauf?* | Mario Alka (DE) | 17/10 | 10,0 K | non mesuré | V100 32 Go : « affaire ou erreur » |
| *The Cheapest 32GB Nvidia GPU You Can Buy for Local AI (Tesla V100)* | Lon.TV | 06/09 | 465,2 K | non mesuré | La plus grosse vidéo « V100 32 Go » trouvée, plus ancienne (septembre) |
| *How much VRAM does Qwen 3.8 27B really need? Every GB, 8GB to 32GB..* | KernelBrief | 10/10 | 31,5 K | non mesuré | Titre : un calcul de VRAM par Go, de 8 à 32 Go |
| *Qwen Just Fit 1 Million Tokens on a 24GB GPU* | Code Unpacked | 29/09 | 4,4 K | ×16,9 (petite chaîne) | Contexte très long sur une carte de 24 Go |
| *Qwen3.8 27B at Long Context: 755% Faster on One GPU?!* | Token Race | 17/08 | 8,4 K | non mesuré | 98 K de contexte, cache KV en q8_0 (d'après la description) |

**Par route** :

- **RTX 5090 (32 Go)** : *Une 5090, Qwen 3.8 27B, 4 sessions en parallèle : voici la config* (**Nicefox, FR**, 15/09, 7,7 K vues, non mesuré), puis des vidéos anglaises d'août (Square Pc : 108 tok/s sur une 5090, 12,3 K ; 880 tok/s cumulés en parallèle, 4,6 K). La plus récente : RepoChad, *AMD R9700 vs RTX 5090* (25,6 K, 23/10, voir le tableau). En français, titre seul et à vérifier : Makertronic, *PANIQUE TOTALE : NVIDIA tue la RTX 5090… et prépare le pire !* (15,9 K, 22/10) : actualité, pas un test de 27B.
- **Ryzen AI Max** : rien de récent sur Qwen 27B ; seulement *Qwen 3.6 vs 3.8-27B vs Flash-Next, lokal auf Strix Halo* (Nick Wolf, DE, 01/09, 1,5 K) et, en français, *ENORME : Le Ryzen AI 495+ ECRASE le Nvidia RTX spark ?* (Makertronic, 06/09, 5,7 K), qui ne porte pas sur le 27B. **Pas de signal** pour ce palier.
- **R9700 / Arc Pro B65 et B70** : couverts par RepoChad (deux vidéos, ×1,05 et ×1,16), Donato Capitella et Mario Alka (DE, *Intel Arc Pro B70 vs. AMD R9700 – 32 GB VRAM für 1.500 € – Das Ergebnis ist erschreckend*, 21/08, 19,7 K). Je n'ai trouvé **aucune vidéo sur la B65**.
- **V100 32 Go** : Lon.TV (465 K), Mario Alka (10 K), Morgans Code (×2,42) : la route d'occasion la plus regardée.
- **Deux cartes** : deux 5060 Ti (RepoChad, *Beyond VRAM* 14,3 K le 14/08), deux P100 (Kai, 17/11), deux R9700 et deux B70.
- **En français**, sur le 32 Go : Makertronic *32 Go pour 1500 € : où est le piège de cette carte AMD ?* (27/09, **6,5 K vues**, non mesuré) et *ÉNORME ! RTX 5090 SE = 32 Go de VRAM pour 1500 € ?!* (21/07, 4,3 K, ×1,20), Nicefox (ci-dessus). **Aucune vidéo française à 100 K ou plus** sur ce palier dans ce que j'ai vu (le français n'est couvert que par les chaînes de la liste et par des recherches web américaines : pas exhaustif).

**Ce que ça change pour notre angle** :

- **Euros.** Les prix en euros n'apparaissent que chez Makertronic (« 1500 € » pour une carte AMD de 32 Go) et chez Mario Alka (« 1.500 € » pour la B70 et la R9700). Les gros titres anglais parlent en dollars ou en routes d'occasion (Kai : 78 $ pour une P100). L'angle « 32 Go en euros, avec ton budget de 600 € » n'est donc pas pris. Mais **Kai écrit lui-même que le prix a bougé après sa vidéo virale** : nos prix du 18/11 sont à **relever à nouveau** juste avant la voix (le calendrier prévoit déjà le 20 et le 26/11).
- **Garantie.** D'après les descriptions, le seul point d'occasion documenté est la fin du support pilote pour les cartes Tesla (Kai, 03/10). Rien dans les titres ni les descriptions vus ne traite la garantie, le retour ou le vendeur ; ce n'est pas vérifié dans le contenu des vidéos. Le tableau « route, prix, garantie, piège » reste donc un angle non pris.
- **Encart Afrique.** Aucune de ces vidéos ne parle d'envoi, de douane, d'alimentation ni de disponibilité en Afrique (d'après les titres et descriptions ; le contenu n'a pas été regardé). L'encart reste un angle propre à la chaîne ; je n'ai aucun chiffre à y ajouter, **non mesuré**.
- **Qwen 4.** RepoChad titre « Qwen 4 27B is Coming: Buy a GPU Now or Wait? » (18/11) : le public se demande s'il faut acheter avant. Une phrase « ce qui change si le 27B de Qwen 4 sort » protège la vidéo du 30/11.
- **Faits à sourcer avant de les reprendre** (venant de la description de Kai, pas de nos sources) : 21,3 Go utiles sur un Mac de 32 Go, ~28 Go utiles sur deux cartes de 16 Go, 5 fois plus de vitesse de lecture du prompt d'une carte à l'autre, fin du support pilote Tesla. Le premier est aussi utile au Mac mini du 10/12.

### Décision

- **Calendrier inchangé, aucun créneau déplacé.** Tous les lundis et jeudis jusqu'au jeu. 31/12 ont leur vidéo ; le prochain créneau libre est le **lun. 4 janvier** (n° 15, « Radar »).
- **Proposition pour le 4 janvier** (à valider par toi, rien n'est écrit dans le calendrier) : *Qwen 4 27B sur ta carte*, **si le 27B est sorti d'ici le 28/12**. Notation sur 40, estimation de ma part : demande 10 · clic 9 · production 8 · niche 9 = **36**. Sinon, *Ton propre JARVIS : un assistant vocal 100 % local* (idée en réserve, écartée le 15/11 au profit du jeu vidéo, et peu compatible avec la règle « tout est calculé » : à rouvrir seulement si tu veux un essai filmé), car deux vidéos du Lab IA à ×2,4 donnent un signal français : demande 7 · clic 8 · production 6 · niche 8 = **29**. Pas d'autre candidat noté ; le sujet « Combien coûte Fable chez toi » est faible chez Morgans Code (1,3 K vues).
- **Vidéo du 30/11, à transmettre à l'auteur du script** : le volet ci-dessus.
- **Strata, test A/B** : laisser tourner jusqu'à des données suffisantes ; **la variante C dit « 125 milliards de paramètres sur une carte de 16 Go »**, un chiffre que `projets/strata-test/sources.md` interdit pour le Coder testé (c'est le modèle d'origine qui a 125 milliards de paramètres, le Coder n'en garde que 256 experts sur 512) et que `upload.md` écarte déjà. À retirer du test si elle est encore active.
- **Leçon de rétention pour les prochains scripts** : 47,7 % des spectateurs restants à 0:30 (intro passive, outils expliqués avant le premier résultat) : le premier résultat avant les outils, dès les 15 premières secondes.
- **Signaux pour les vidéos déjà prévues** : lun. 23/11 (8 Go) : Morgans Code vient de sortir sa vidéo 8 Go (1,2 K vues, ne change rien à notre angle « à quel prix ») ; jeu. 3/12 (DeepSeek) : Kai a 70,3 K vues (×1,26, 13/11) ; lun. 7/12 (deux cartes) : Weights & Wonders à ×5,04 confirme la demande ; jeu. 10/12 (Mac mini) : le chiffre des 21,3 Go utiles d'un Mac de 32 Go est à sourcer.
- **Report du radar du 12/11** : *The Best Local AI GPU For Every Budget (November 2026)* (Locally, sortie le 14/11) est à **3,9 K vues au 19/11** (page YouTube), contre 1,6 K quelques heures après sa sortie : le signal derrière la vidéo du 26/11 se confirme, sans multiplicateur (non mesuré).
- **Chaînes de la liste non relevées cette fois** : ByteMonk, Thibaut Dcode, Baptiste Simard, Machine Learning Lab (hors sujet IA locale et matériel) : non mesuré.
- **Liste de surveillance** : ajouter **Donato Capitella** (EN, B70 et R9700, 37 à 76 K vues par test) si tu veux le suivre ; son ID n'est pas relevé, donc non ajouté.

**Prochain radar** : à la sortie de *Même carte, 2 fois plus rapide* (jeu. 19/11) ou de la vidéo 8 Go (lun. 23/11) ; mesurer Strata à J+10 avec Studio, et le verdict du test A/B.

---

## 12/11/2026 (soir) : sortie de Qwen 4, radar allégé, calendrier inchangé

**Contexte** : « Qwen 4 quelle carte graphique acheter (ou pas) ? » est sortie le 12/11 à 21 h 45 (heure de Paris) : https://youtu.be/JuiZAwEiX-o. Le forfait vidIQ est gratuit depuis ce jour : 875 crédits avant le radar (150 renouvelables le 08/12, 725 en bonus), **20 dépensés**. Deux outils de la procédure manquent dans la connexion vidIQ : `vidiq_outliers` (concurrents et public français) et `vidiq_channel_analytics` (rétention, sources). Les concurrents passent donc par `vidiq_channel_videos`, une chaîne à la fois (5 crédits chacune).

### Notre chaîne (`vidiq_user_videos`, 12/11 à 20 h 50 UTC)

| Vidéo | Sortie | Recul | Vues | Likes / commentaires |
|---|---|---|---|---|
| Qwen 4 quelle carte graphique acheter (ou pas) ? | 12/11 | J+0 (5 min) | 0 | 0 / 1 |
| 16 Go de VRAM : est-ce vraiment suffisant pour les LLM ? | 09/11 | J+3 | 285 | 10 / 3 |
| Comment utiliser une IA sans internet sur ton PC | 02/11 | J+10 | 333 | 5 / 7 |
| Uber : l'illusion parfaite du temps réel | 26/10 | J+17 | 224 | 7 / 0 |
| OpenCode a été gravement piraté | 21/10 | J+22 | 492 | 4 / 1 |
| ArtCraft (« Il a cloné toutes les applications Adobe ») | 19/10 | J+24 | 612 | 7 / 1 |

- **16 Go** est à 285 vues à J+3, presque autant que l'installation à J+10 (333) : la meilleure entrée récente, avec 10 likes.
- **Non mesuré** : le CTR, les tests A/B de miniatures (16 Go, Qwen 4) et la rétention. `vidiq_channel_analytics_extended` répond « channel_mismatch » : l'extension vidIQ du navigateur est connectée à un autre compte Google que celui de Technovore. À refaire au prochain radar, après avoir choisi le bon compte dans Studio (ou avec une capture de Studio).

### Concurrents (`vidiq_channel_videos`, 12/11)

- **Weights & Wonders** (EN) : *Watch This Before Building a Multi-GPU Local AI Setup!* (19 K vues, **1 562 vues/h**, ×2,2, sortie le 12/11) ; *11 GPUs You Should Get for Local AI Before Qwen 4's Release!* (45 K, ×5,9, 08/11, notre inspiration) ; *I Built THE BEST Local AI Stack for 32GB VRAM!* (7 K, 10/11).
- **Kai** (EN) : *Qwen 4 27b: What to Expect from the next local LLM King?* (50 K, 11/11) ; *Apple's Local AI App for Mac Is Coming (Harbor)* (11,9 K, **2 374 vues/h**, 12/11) ; *The Local AI Hardware Mistake Almost Everyone Makes* (52 K, ×2, 07/11) ; *I Run Full DeepSeek v4.1 Flash on a 12GB GPU* (60,6 K, 06/11).
- **Makertronic Tech** (FR) : *PRIX DES GPU : Pourquoi les cartes vont devenir INTOUCHABLES !* (1,2 K, **299 vues/h**, 12/11) ; *192 Go de VRAM : NVIDIA a un ÉNORME PROBLÈME !* (18,4 K, ×2,1, 08/11).

### Public français

Pas d'appel `vidiq_outliers` possible. Seul signal : Makertronic sur le prix des cartes, sorti le même jour que Qwen 4.

### Décision

- **Calendrier inchangé.** Le créneau habituel du radar (jeu. 19/11) a déjà sa vidéo, *Même carte, 2 fois plus rapide*. Le seul créneau libre reste le lun. 7/12.
- **Les signaux nourrissent les vidéos déjà prévues** :
  - **lun. 23/11, 32 Go de VRAM** : le multi-GPU marche (Weights & Wonders, 1 562 vues/h). Ajoute « ce qu'il faut vérifier avant de monter 2 cartes » : alimentation, lignes PCIe, tensor split encore expérimental (déjà mesuré dans Qwen 4) ;
  - **jeu. 10/12, Mac mini ou PC gamer** : surveiller Harbor, l'appli d'IA locale d'Apple, si elle sort d'ici là ;
  - **jeu. 17/12, prix après le Black Friday** : le prix des cartes intéresse le public français (Makertronic) ;
  - **lun. 7/12** : la candidate « petits budgets » se renforce, avec un angle 8 à 12 Go. Kai fait 60 K vues avec un modèle sur 12 Go, et 8 Go est la VRAM d'un joueur sur quatre (Steam, octobre). À noter au prochain radar.
- **Prochain radar** : à la sortie de Strata (lun. 16/11). On y mesure 16 Go à J+7 et Qwen 4 à J+4, avec Studio sur le bon compte.

> **16/11, ta demande** : le lun. 23/11 va à *Qwen 27B sur une carte de 8 Go, 5 fois plus vite* (SimplyExplain : 8,7 K vues en 3 jours avec 2,07 K abonnés ; Red Stapler : 788 K vues ; pages YouTube, 16/11), ce qui répond au signal « 8 à 12 Go » noté plus haut. « 32 Go de VRAM » passe au lun. 30/11, DeepSeek au jeu. 3/12, « RAM, VRAM ou mémoire unifiée » au jeu. 31/12 (créneau radar).
>
> **Remplacé le 14/11, ta demande** : le « calendrier inchangé » ci-dessus ne tient plus. Le multi-GPU a sa propre vidéo (lun. 7/12, 32,9 K vues en 3 jours chez Weights & Wonders, page YouTube du 14/11) ; « petits budgets » devient *Quel modèle ta carte peut faire tourner ? De 4 à 16 Go* (25/01, provisoire, d'après Codacus) ; la meilleure carte par budget prend le jeu. 26/11 et RAM, VRAM ou mémoire unifiée le jeu. 3/12 (deux vidéos de Locally). IA locale privée recule au 11/01 et DeepSeek V4.1 Flash au 18/01. Au radar du 16/11 : remesurer *The Best Local AI GPU For Every Budget* (1,6 K vues après quelques heures), dont le signal n'est pas encore prouvé. Détail dans [`calendrier.md`](../calendrier.md).

---

## 10/11/2026 : passage à 2 vidéos IA/semaine (lun. + jeu.), « 16 Go » à J+1, l'installation à J+8, Qwen 4 et deux nouvelles chaînes EN

**Décision du jour (ta demande) :** la chaîne passe à **2 vidéos par semaine, lundi et jeudi, 18 h, uniquement IA / IA locale**, du jeu. 12/11 au lun. 4/01/2027, puis retour à 1 vidéo/semaine (lundi). Les piliers « génie » et « histoires » sont **archivés** pour cette période : plus de règle 3 pour 1. Chaque vidéo se fait en 1-2 jours, reste calculée (sources, mesures publiées, études, calculs) sauf exceptions filmées déjà décidées (installation du 2/11, test Strata du 16/11).

### Notre chaîne

| | 16 Go de VRAM (09/11, **J+1**) | Installation IA locale (02/11, **J+8**) |
|---|---|---|
| Vues (Studio) | 79 | 297 |
| Likes / commentaires | 5 / 3 | 3 / 7 |
| `vidiq_channel_analytics` (totaux) | **Vide : retard de l'API**, comme au 21/10. Rien de plus fiable que le compteur Studio à J+1. | Traffic sources et rétention ci-dessous |
| Sources de trafic (02-10/11, ~273 vues) | — | **Abonnés 46 %**, externe (EXT_URL) 24 %, recherche YouTube 16 %, suggestions (RELATED_VIDEO) seulement 6 %, notifications 3 % |
| Rétention (courbe) | — | **0:15 ≈ 74 %** (cible 75 %, presque atteinte), **1:00 ≈ 59 %** (cible 50 %, dépassée) ; creux à ~40 % vers le milieu puis remontée à ~65 % (55-65 % de la vidéo), puis descente classique en fin de vidéo |
| Suggestions détaillées | — | 5 vidéos sources, 1-2 vues chacune : **rien d'exploitable**, échantillon trop petit |

- **L'installation reste le meilleur format retenu de la chaîne** après celui du 05/11 : la rétention à 1:00 dépasse largement la cible, et les abonnés (46 % du trafic) regardent encore. Les suggestions ne nous portent presque pas (6 %) : le classement Flutter pèse toujours.
- **16 Go** n'a qu'un jour de recul : pas de verdict avant le prochain radar (J+7, vers le 16/11).

### Concurrents EN (liste de surveillance, `thisMonth`, 13 chaînes dont les 2 nouvelles)

- **Kai** reste la référence du format « X Go de VRAM » : *Don't Buy a GPU Instead Build This 32GB Free AI Server* (419,7 K, ×5,8, 12/10), *Your Local AI Is Not as Private as You Think* (573,1 K, ×5,3, 21/10), *512GB VRAM* (193,1 K, ×2,3), *How I Got Frontier Performance on 16GB VRAM (Qwen 3.8 27B)* (112,6 K, ×1,1, 18/10) — très proche de notre « 16 Go ».
- **RepoChad** (14 200 abonnés, 2,53 M vues, 55 vidéos, Inde) : *Every Way to Get 256 GB of VRAM for Local AI* (162,4 K, **×7,4**, 19/10) — le format visé par l'idée (a) ; *Run FULL DeepSeek v4.1 Flash on a 12GB GPU* (53,7 K, ×2,6, 02/11) ; *China's AI Bubble Just Burst! Will GPU Prices Finally Drop?* (40 K, ×1,9, 28/10).
- **Weights & Wonders** (1 220 abonnés, 172,7 K vues, 22 vidéos, Inde) : ***Don't Miss Out on These GPUs Before Qwen 4's Release!*** (25,6 K, **×4,2**, 272,7 vues/h, publiée le 08/11, il y a 2 jours) — l'idée (b) ; *I asked Qwen 3.8 27B to Optimise Itself* (33,3 K, ×16) ; *I Forced Qwen to Use All Its Experts* (19,2 K, ×4,1).
- **Morgans Code** : *Qwen 4 27B: What to Expect From the Next Local AI King* (28 K, ×3,8, 16/10, rumeur/attente) ; *Uncensored Qwen 3.8 27B Isn't the Hacker You Think* (6,2 K, **×20**, 08/11) ; *DeepSeek V4.1 1017 Flash Is Opus-Level: What Does It Really Cost to Run?* (15,3 K, ×1,6, 19/10).

### Public français

- **« Qwen 4 » en français (`vidiq_outliers`, fr, thisMonth)** : **aucun résultat pertinent** — les 15 vidéos qui sortent sont des faux positifs sur le chiffre « 4 » (MW4, saisons 4, épisodes 4…). **Personne n'en parle encore en français.**
- **« VRAM carte graphique IA » (fr, threeMonths)** : signal direct — **Makertronic Tech**, *TAXE VRAM, la Chine dit NON : elle double la VRAM de tes RTX !* (20,1 K, ×2,1, **05/11**, 115,5 vues/h) : la chaîne de notre liste de surveillance couvre déjà l'angle « VRAM + Chine », pas encore « deux cartes d'occasion » ni l'actu Qwen 4. Sinon, rien de spécifique IA locale (bruit gaming/matériel général).

### Qwen 4 : confirmé ou rumeur ? (recherche web, sources datées)

**Confirmé (annonces officielles Alibaba/Qwen)** :
- **22/09/2026, conférence Apsara (Hangzhou)** : Alibaba a dévoilé les noms **Qwen 4 Max, Qwen 4 Flash, Qwen 4 Plus, Qwen 4 27B**, et confirmé que Qwen 4 est en entraînement. Aucune date de sortie, aucun prix, aucun poids téléchargeable à cette date.
  - **Corrigé le 11/11 (relecture du script Qwen 4, sources dans `projets/qwen-4-cartes/sources.md`)** : le communiqué officiel du 22/09 dit seulement que Qwen 4 est « en entraînement ». Le nom « Qwen 4 27B » vient de la presse sur la conférence (36Kr, 23/09) : c'est un nom annoncé, sans fichier ni caractéristiques, pas une fiche officielle. « Qwen4-Max » est officiel depuis la préversion cloud du 11/11 (Token Plan d'Alibaba, jusqu'au 25/11), sans rien à télécharger.
- **26/08/2026** : Qwen a publié **Qwen3.8-Flash-Next** sur Hugging Face, explicitement présenté comme un aperçu de l'architecture de Qwen 4 (Gated DeltaNet + Qwen Sparse Attention).
- **06/11/2026** : le compte officiel Qwen a posté un teaser (« The becoming begins ») qui a relancé les spéculations, sans date précise.
- Alibaba a aussi annoncé une feuille de route **Qwen 4.5 et Qwen 5** (5 à 10 000 milliards de paramètres).

**Rumeur / non confirmé** :
- Une sortie en **novembre 2026** « semble de plus en plus probable » selon un participant à une conférence Alibaba du 29/10 qui rapporte des propos du CTO — information de seconde main, non officielle.
- Des identifiants de code (« qwen4-max », « qwen4-plus », « qwen4-coder-plus ») trouvés dans des mises à jour de code du 28/10 (fuite non confirmée par Alibaba).
- **Aucun checkpoint Qwen 4 n'est disponible sur Hugging Face** à la date du radar.

**Verdict pour nos vidéos** : on peut dire « Qwen 4 Max/Flash/Plus/27B existent déjà comme noms officiels, en entraînement depuis le 22/09, mais sans date, prix ni poids confirmés » — c'est vérifiable et sourcé. Tout le reste (date de sortie, tailles exactes en Go) doit être présenté comme rumeur.

### Proposition de grille (jeu. 12/11 → lun. 4/01/2027, lundis ET jeudis, uniquement IA)

**Créneaux déjà pourvus en IA, inchangés** : lun. 16/11 (Strata, filmée, exception déjà décidée), lun. 30/11 (Combien coûte Claude en local), lun. 7/12 (Strata petits budgets — angle à revoir sans Strata si Strata recule), lun. 14/12 (IA en local : lire le nom d'un modèle), lun. 28/12 (Louer, acheter), lun. 4/01 (Abonnement ou IA locale #2).

**Créneaux à sortir de la règle 2×/semaine IA (non-IA, pilier archivé) :** lun. 23/11 (Waze, génie) et lun. 21/12 (Python) ne sont plus « IA / IA locale » strictes. Python garde un lien ténu (« le langage de l'IA ») : à trancher avec toi. Waze n'a aucun lien IA : à décaler vers un créneau post-04/01, quand les piliers reviennent.

| Créneau | Vidéo proposée | /40 | Justification (une ligne) |
|---|---|---|---|
| **Jeu. 12/11** | **Qwen 4 : les cartes graphiques à acheter avant sa sortie** (inspirée de Weights & Wonders, angle Technovore : prix FR/Afrique, confirmé vs rumeur) | **32/40** (demande 8 · clic 8 · production 7 · niche 9) | W&W fait ×4,2 en 2 jours (272 vues/h) sur cet angle précis ; fenêtre courte avant que Qwen 4 sorte vraiment (teaser du 06/11) — à produire vite (1-2 j) |
| **Lun. 23/11** (remplace Waze) | **32 Go de VRAM avec deux cartes d'occasion** (inspirée de RepoChad, reprend `deux-cartes-occasion`) | **35/40** (demande 9 · clic 8 · production 8 · niche 10) | RepoChad fait 162 K vues ×7,4 sur « Every Way to Get X GB VRAM » ; sources déjà vérifiées deux fois (24/10), aucun achat réel, rien d'équivalent en français |
| **Jeu. 19/11** | **Même carte, 2 fois plus rapide** (idée 16, réserve `idees.md`) | **34/40** (demande 8 · clic 9 · production 8 · niche 9) | Déjà scorée en réserve ; Code Unpacked avait fait 11,2 K en un jour sur l'angle « plus rapide, pas plus grosse » (22/10), rien en français |
| **Jeu. 26/11** | **Ton IA locale est-elle vraiment privée ?** (idée réserve, sécurité : Ollama exposé, modèles piégés) | **34/40** (demande 9 · clic 9 · production 7 · niche 9) | Kai fait 573 K vues ×5,3 sur l'angle proche ; aucun équivalent français trouvé dans ce radar ni le précédent |
| **Jeu. 3/12** | **Combien coûte DeepSeek V4.1 Flash chez toi ?** (série « combien coûte [modèle] », idées réserve) | **30/40** (demande 7 · clic 7 · production 7 · niche 9) | Morgans Code fait 15,3 K ×1,6 sur ce calcul ; angle Technovore en euros/FCFA, calculée, réutilise la méthode de Coût Claude |
| **Jeu. 10/12** | **Mac mini ou PC gamer pour l'IA en local ?** (avancée du 11/01, `mac-mini-ia`) | **33/40** (demande 8 · clic 8 · production 7 · niche 10) | Fiche déjà posée (24/10), inspirée de Locally (40 K, ×21,9) ; recherche et double vérification restent à faire — avancer la date densifie le bloc IA sans nouvelle idée |
| **Jeu. 17/12** | **Le dev qui a mis un ChatGPT dans ton PC** (llama.cpp, avancée du 18/01) | **31/40** (demande 7 · clic 8 · production 7 · niche 8) | Script déjà écrit (23/10) ; limite avec la nouvelle règle (plus « histoire d'outil » que calcul pur) — à confirmer avec toi avant de le déplacer ici |
| **Jeu. 24/12** (veille de Noël) | **Pause recommandée**, ou rediffusion/compilation plutôt qu'une nouvelle vidéo | — | Faible trafic habituel la veille de Noël ; mieux vaut garder la vidéo du 21/12 (ou son remplaçant) en avant plutôt qu'un nouveau sujet qui se perdra |
| **Jeu. 31/12** (veille du Nouvel An) | **Pause recommandée**, même raison | — | Idem : veille de jour férié, faible audience attendue |

**Stock restant si tu veux garder le rythme sans pause le 24 et le 31/12** : les deux idées réserve non encore datées (« Combien coûte [modèle] » peut se refaire modèle par modèle, p. ex. DeepSeek V4.1 ou Qwen 3.8 27B) ou une 2e vidéo Qwen 4 dès qu'il sort réellement (si la sortie confirmée tombe avant le 04/01, elle mérite un créneau dédié, probablement en remplaçant un des candidats ci-dessus plutôt qu'en ajout).

**Crédits vidIQ utilisés dans ce radar : 45** (~~balance 0~~ **corrigé le 10/11, 2e passe : la balance affichée ce jour-là n'était pas 0, voir ci-dessous** · `vidiq_user_videos` 5 · 4× `vidiq_channel_analytics` 20 · `vidiq_get_channels_by_ids` 5 · `vidiq_outliers` ×3 15).

---

## 10/11/2026 (2e passe) : DeepSeek Super-Agent (verdict), Qwen 4 (toujours rumeur) et les 4 créneaux de fin décembre

**Correction des crédits** : le « balance 0 » noté dans l'entrée du 10/11 ci-dessus était faux. Le solde réel, vérifié ce jour (`vidiq_balance`, 0 crédit) : **4 454 crédits** (3 829 renouvelables sur 6 000, renouvellement le 12/11 ; 625 crédits bonus sur 700). Il restait donc largement de quoi faire ce 2e passage. Budget utilisé ici : **10 crédits** (`vidiq_balance` 0 · 2× `vidiq_outliers` 10), sur un budget de ~60.

### DeepSeek Super-Agent : les faits (sources datées)

- **Ce que c'est** : `dsh-superagent`, publié le **31/10/2026** par DeepSeek sur `deepseek-ai/dsh-superagent-prototype` (GitHub), **licence MIT**, écrit en TypeScript. C'est un agent de codage qui vit dans un dépôt GitHub (et optionnellement les discussions Feishu de l'équipe), pas un nouveau modèle : il s'ajoute à **DeepSeek Harness (`dsh`)**, le framework d'agents sorti en août 2026. DeepSeek le présente lui-même comme « un prototype de recherche, pas un produit fini ». Sources : [MarkTechPost, 01/11](https://marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent), [datastudios.org](https://www.datastudios.org/post/deepseek-dsh-superagent-mit-proactive-coding-agent-github-feishu).
- **Peut-il tourner en local ?** Oui, mais pas avec « DeepSeek » comme modèle local : `dsh` accepte n'importe quel serveur compatible OpenAI (protocole `openai-completions`), donc un modèle **local, pas DeepSeek** — le guide d'installation documente un test concluant avec **Qwen3.5-4B** (2,74 Go en GGUF Q4_K_M) via **llama.cpp ou Ollama** (Ollama 0.32.11 a l'intégration directe `ollama launch dsh`). Sans cette config, `dsh` utilise par défaut l'API cloud `deepseek-flash`. Source : [jacar.es](https://jacar.es/?p=7252).
- **Quelle machine ?** Node.js, 5 Go de RAM libres minimum pour le serveur local, Docker ou llama.cpp. Sur CPU sans GPU, une fonction simple a pris **entre 171 secondes et 45 minutes** selon la charge — un modèle 4B, lent, avec une fidélité faible sur les accents et les caractères non-latins. Pour `dsh-superagent` lui-même, DeepSeek recommande en plus une **machine dédiée ou un compte système isolé**, parce que les sessions « worker » exécutent des commandes sans validation préalable (risque de sécurité).
- **Tendance mesurée** (`vidiq_outliers`, ce mois) :
  - **EN** : très couvert — Sam Witteveen (140 K abonnés) à 195,7 K vues (×4, 03/11) ; AI LABS (180 K) à 72,6 K vues (×2,1, 05/11) ; Julian Goldie SEO (439 K) a sorti **5 vidéos** sur le sujet en une semaine.
  - **FR** : déjà traité par au moins **3 chaînes** avec un angle proche du nôtre si on le ferait : Julien Massey (39,1 K abonnés, FR), *« DeepSeek vient de TUER Claude Code »*, 41,2 K vues, ×5,9, **07/11** ; Pentiminax (30,1 K, FR), **2 vidéos** (*« il travaille à ta place »*, 20,4 K vues, 02/11, et une mise à jour le 20/10) ; IA Technologie (8 K), *« l'IA qui bosse dans ton équipe »*, 26,7 K vues, ×18, 03/11. Confirme et précise le « trois grosses chaînes françaises » du 05/11.
  - Recherche FR directe sur « DeepSeek Super Agent » : les résultats sont dominés par ces mêmes vidéos de créateurs IA/dev — pas de vide à combler.

**Verdict : (c) on ne le fait pas**, pour trois raisons qui se cumulent :
1. ce n'est pas vraiment de l'IA **locale** : l'angle « je le fais tourner sans cloud » obligerait à montrer un petit modèle Qwen 4B, lent (jusqu'à 45 min pour une fonction) et pas fiable, sous le nom « DeepSeek », ce qui induirait le public en erreur (« les faits comptent », `CLAUDE.md`) ;
2. l'angle (b), IA non locale, est déjà traité par au moins 3 chaînes françaises avec le même cadrage (« ça tue Claude Code », « il bosse à ta place ») et des dizaines de vidéos anglaises : aucune place pour ne pas copier l'angle ;
3. c'est un agent de codage pour des équipes de dev, pas un sujet qui parle à notre audience grand public (63 % Afrique francophone, 94 % moins de 35 ans), contrairement aux séries « combien ça coûte » ou « combien de VRAM ».

Score, si on le forçait quand même en angle (a) « je le fais tourner sans cloud » : **22/40** (demande 6 · clic 7 · production 4 : contredit la règle « calculé, sans essai » puisqu'il faudrait démontrer la lenteur réelle · niche 5 : agent de code, pas IA locale grand public). Sous le seuil des créneaux retenus (29-35/40) : confirme qu'on laisse tomber, comme le 05/11.

### Qwen 4 : toujours une rumeur au 10/11

Rien de neuf depuis l'entrée du 10/11 ci-dessus : le teaser du **06/11** (« The becoming begins ») n'a ni nommé Qwen 4 ni donné de date, d'accès API ou de poids téléchargeable. Un participant à la conférence Alibaba du 29/10 rapporte qu'une sortie « la semaine suivante » aurait été évoquée par le CTO — toujours de seconde main, non officiel. Aucun checkpoint Qwen 4 sur Hugging Face à ce jour. **La vidéo du jeudi 12/11 parle bien de l'attente (cartes graphiques à acheter avant la sortie), pas d'une sortie confirmée** : le script reste correct en l'état. Sources : [emergent.sh](https://emergent.sh/news/alibaba-teases-qwen4-lineup-apsara-due-next), [af.net](https://af.net/realtime/alibaba-teaser-sparks-qwen-4-speculation-as-release-date-and-checkpoints-remain-unverified/).

### Les 4 créneaux à remplir (jeu. 17/12, lun. 21/12, jeu. 24/12, jeu. 31/12)

Aucun doublon avec la grille déjà posée. Toutes calculées (sources, prix relevés, pas d'essai), dans la règle 2×/semaine IA jusqu'au 4/01.

| Créneau | Vidéo proposée | /40 | Justification |
|---|---|---|---|
| **Jeu. 17/12** | **Le Black Friday a-t-il vraiment fait baisser les prix de l'IA en local ?** (bilan prix, GPU et RAM) | **33/40** (demande 8 · clic 8 · production 8 · niche 9) | Contre-pied vérifiable : en 2026 les prix de la DRAM/GDDR/NAND montent d'environ 20 %/trimestre, donc le Black Friday (27/11) n'a pas vraiment baissé le prix des cartes et de la RAM pour l'IA locale (sources : [runaihome.com](https://runaihome.com/blog/black-friday-2026-local-ai-hardware-buy-now-or-wait/), [tomsguide.com](https://www.tomsguide.com/computing/gpus/gpu-price-hikes-are-coming-in-2026-so-now-is-the-best-time-to-buy-ive-found-the-best-deals-for-you-to-get-ahead-of-it)) ; sert les acheteurs avant Noël, aucun équivalent français trouvé, et relie Claude #1, 32 Go de VRAM et Louer/acheter |
| **Lun. 21/12** | **Combien coûte Kimi K3.1 Pro chez toi ?** (série « combien coûte [modèle] ») | **31/40** (demande 7 · clic 7 · production 8 · niche 9) | Kimi K3.1 Pro est sorti sur Hugging Face vers le **05/11/2026** et grimperait en tête des classements selon les premiers retours ; la série a déjà marché 2 fois (Coût Claude, DeepSeek V4.1 Flash), méthode éprouvée, pas de nouvel essai |
| **Jeu. 24/12** (veille de Noël) | **Le cadeau IA locale : quel budget pour s'offrir une machine qui tourne sans le cloud** | **34/40** (demande 8 · clic 8 · production 9 · niche 9) | Intemporel et cadeau, comme demandé : synthétise les calculs déjà faits (Mac mini, 32 Go de VRAM, Louer/acheter) en guide d'achat de fin d'année ; aucune actu à vérifier, production très légère (montage de sources existantes) |
| **Jeu. 31/12** (veille du Nouvel An) | **Résolution 2027 : ce que coûte vraiment de quitter le cloud pour de bon** | **32/40** (demande 7 · clic 8 · production 9 · niche 8) | Thème « résolution de janvier » (quitter les abonnements), intemporel ; referme la série « Abonnement ou IA locale ? » avant l'épisode #2 du 4/01, recycle les chiffres déjà vérifiés de Coût Claude et DeepSeek V4.1 Flash |

**2 remplaçants** (si un sujet ci-dessus doit bouger, ou en réserve pour un futur créneau radar) :

| Remplaçant | /40 | Justification |
|---|---|---|
| **L'IA cachée dans ta carte graphique** (NPU, Tensor Cores : ce qu'ils changent vraiment pour toi) — reprend l'idée mise de côté dans `strategie.md` | **30/40** (demande 6 · clic 7 · production 8 · niche 9) | Intemporel, calculé (specs publiées), complète la série matériel sans répéter VRAM/Mac mini |
| **Combien coûte GLM-5.3 chez toi ?** (2e itération de la série « combien coûte », si Kimi K3.1 Pro est pris pour un autre créneau) | **29/40** (demande 6 · clic 7 · production 8 · niche 8) | GLM-5.3 (Z.ai) est cité en tête des classements open source de novembre 2026 ; méthode déjà rodée, risque de production le plus faible de tous les candidats |

**DeepSeek Super-Agent dans ces créneaux ?** Non : voir le verdict ci-dessus (22/40, sous le seuil). Il ne mérite aucun des 4 créneaux ni les remplaçants.

---

## 05/11/2026 : bilan d'Uber, de l'IA locale et d'OpenCode (captures de Studio)

| | IA locale (2/11) | Uber (26/10) | OpenCode (21/10) | ArtCraft (19/10) |
|---|---|---|---|---|
| Vues | 195-209 | 221 | 479 | 608 |
| Impressions | 1,3 K | 4,4 K | 2,3 K | 10,5 K (21/10) |
| CTR | 2,0 % | 1,3 % | **4,2 %** | 0,9 % |
| % regardé | **41,2 %** (3:53) | 26,8 % (2:41) | 21,3 % (1:50) | 28 % |
| Rétention 0:15 / 1:00 (courbe) | ~70 % / **~50 %** | ~65 % / ~45 % | ~65 % / ~35 % | 66 % / 47 % |
| Commentaires | **7** | 0 | 1 | 1 |
| Part des suggestions | 8,6 % | 24 % | 4,2 % (Accueil 79 %) | 98 % |

- **IA locale** : le meilleur contenu de la chaîne (1:00 à 50 %, remontée entre 1:00 et 2:00, plateau à 50 % jusqu'à 3:30). Elle pèche par le clic.
- **Uber** : YouTube l'a beaucoup montrée, mais personne n'a cliqué. Le titre est trop abstrait. **On la laisse tomber** (décision du 05/11) et on optimise les vidéos suivantes.
- **OpenCode** : le drame fait cliquer, mais le contenu ne tient pas la promesse (plateau à 15 %).
- **Suggestions** : les vidéos qui nous suggèrent n'ont rien à voir avec nous (JDG, trading, foot, Edenred…). YouTube n'a pas encore classé le nouveau format.

**Décision (05/11)** : 3 vidéos « IA chez moi » pour 1 vidéo « histoire / génie ». La règle « pas deux fois le même pilier de suite » tombe. La prochaine vidéo est une vidéo IA locale : elle garde le fond de la vidéo d'installation et l'emballage d'OpenCode (enjeu, question, verdict), et vise 75 % à 0:15.

**Ajout du 05/11 (recherche sur le web ; `vidiq_outliers` indisponible dans cette session)** :
- **DeepSeek Super-Agent** (`dsh-superagent`, MIT, 31/10) : un prototype de recherche, un agent de code pour les équipes qui lit les discussions Feishu, sans benchmark publié. Trois grosses chaînes françaises l'ont déjà traité (selon l'auteur), et ce n'est pas de l'IA locale pour notre public. **On ne le fait pas.**
- **Higgsfield contre ComfyUI** (fin octobre) : un concours à environ 25 K$ pour recréer Higgsfield en open source, suivi d'une mise en demeure sous 48 h. La vidéo envoyée par l'auteur (`znrYe8yVQ_Q`, en anglais, 85 K vues, 3/11) en parle. C'est un bon récit « open source contre géant », mais sur la vidéo IA, pas les LLM locaux. **Candidat pour un créneau histoire** (15 févr.), pas pour un créneau proche.
- Calendrier : Claude #1 (« 16 Go suffisent », avec Strata) passe au 9 nov., « nom d'un modèle » au 16 nov.

## 23/10/2026 : radar des idées (le 8 mars, à la place de Mobile Money)

Pas une sortie de vidéo : l'auteur a abandonné Mobile Money (« je n'aime pas l'idée ») et llama.cpp a pris son créneau du 8 févr. Il fallait une vidéo pour le 8 mars, entre deux créneaux IA, donc **génie ou histoire**. Environ 15 appels vidIQ.

### Signaux
- **Génie, en anglais** (chaînes de la liste et voisines, 6 mois) :
  - Enrico Tartarotti : *The Insane Design Of Messaging* (1,7 M, ×17), *The LIES That Make Hardware ACTUALLY Work* (793 K, ×7,1), *The Ridiculous Engineering Of Animations* (288 K en 5 jours, pour l'iPhone du 7 déc.) et *…Of Text* (302 K) ;
  - ByteMonk : SQLite (221 K, ×12) ;
  - Hussein Nasser : Postgres (235 K, ×14) ;
  - Low Level : *I Tested The Viral Reverse Engineering Repo* (3,1 M, ×9,1).
- **Objets du quotidien** :
  - PawelCodeStuff, *The Most Overengineered Part of Your iPhone* (Face ID, 713 K, ×32, 15/10) ;
  - History of Simple Things, *How Do QR Codes Work?* (1,35 M, ×113) ;
  - Factron Process, câbles sous-marins (509 K, ×162).
- **Jeux en ligne** :
  - DeadInSperanza, *Hidden Players: Why Don't Servers Just Hide Enemies?* (52 K, ×108, 13/10) ;
  - Outscal, lag (38 K, ×35) ;
  - Tariq10x (297 K) ;
  - Surnex, *Once you see this, You'll see Competitive Games Differently* (2,5 M, ×356).
  - **Aucune vidéo française** sur le netcode.
- **En français** :
  - V2F (overfl0w), *Ce que tes yeux ne voient pas dans un QR Code* (214 K, sept. 2026) : l'angle du QR code est pris ;
  - Face ID : seulement Micode (2017, 428 K) et des tutos de dépannage.
- **Mots-clés** :
  - « how qr codes work » : 19,6 K par mois, +129 % ;
  - « lag jeux en ligne » et « câble sous-marin internet » : moins de 750 par mois en France ;
  - « shazam » est pollué par le film.

### Décision
- **Lun. 8/03 : *Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne*** ([fiche](../archive/lag/fiche.md)), choisie par l'auteur. 32/40 (demande 7 · clic 9 · production 7 · niche 9). C'est un sujet d'accueil, pour un public de 18-24 ans joueurs, et il n'existe pas en français.
- **En réserve** (`idees.md`) :
  - Face ID (32/40), à garder loin de l'iPhone du 7 déc. ;
  - le QR code (30/40), seulement quand la vidéo de V2F ne circulera plus ;
  - le jour où l'Afrique de l'Ouest a perdu internet (29/40), à envisager pour le 14 mars 2027 (3 ans).

---

## 21/10/2026 : sortie d'OpenCode (radar n° 1)

### Notre chaîne
- **2 610 abonnés**, +20 en 30 jours ; ~3 200 vues en 30 jours (169 312 au total).
- **ArtCraft** (19/10) : 285 vues à J+2. CTR de 0,9 % pour 10,5 K impressions, dont 98 % viennent des suggestions (relevé Studio du 21/10). Sous les 3 %, le guide de l'algorithme dit qu'il faut corriger : tes 3 miniatures memes (Toy Story, Clawd, Solo Leveling) sont là pour ça.
- **OpenCode** (21/10, 13 h) : 3 vues à H+2.
- **Uber** est en ligne en privé, avec un titre à corriger (« L'hisoire du temps réel derriere uber ») et les **tags Flutter par défaut**. Il faut les remplacer avant le 26/10 ; le kit d'upload n'existe pas encore.
- Les statistiques par vidéo (`vidiq_channel_analytics`) sont vides pour ces trois jours : l'API a du retard. À reprendre au prochain radar.

### Concurrents
- **Kai** : 49 400 abonnés, **+11 400 en 7 jours**, 8 vidéos. Ses meilleures vidéos du mois parlent toutes de matériel : « Every Ways to Get 128GB VRAM… » (821 K), « Don't Buy a Mac Mini For Local AI » (409 K), « Is 16GB All You Need… » (386 K), « Can a Mac Mini Replace your $200 AI Subscription? » (316 K), « Don't Buy a GPU Instead Build This 32GB Free AI Server » (258 K).
- **Morgans Code** : 2 020 abonnés (+240 en 7 jours). « Is $1,500 All You Need to Run DeepSeek V4.1 Flash? » : 17,7 K en un jour. « Qwen 4 27B: What to Expect » : 22,2 K. Étude complète : [`morganscode.md`](morganscode.md).
- **Thibaut Dcode** : « L'effrayante vérité sur l'empire WhatsApp » a 204 K vues (×0,6). Sur sa chaîne, c'est sous la moyenne.
- **Makertronic Tech** (5 900 abonnés, chaîne en pleine montée) : « NVIDIA sous le CHOC : la RX 10700 XT détruit la RTX 5080 ! » (35 K, ×2,6) ; « 512 Go pour l'IA : la Chine veut casser les prix ! » (17,9 K en 2 jours).
- **Baptiste Simard** : « J'ai cloné une application payante avec Claude Code (Fin du SAAS ?) » (36,5 K, ×6,7) ; « 11 repos GitHub indispensables à brancher sur Claude Code » (29,3 K en 4 jours).

### Public français
- **IA en local** : « Adieu le cloud pour les LLM ! Vive le local » (Le Lab IA, 47,8 K, ×24) ; « Gérer HomeAssistant avec une IA 100 % gratuite » (Bricolo2.0, 25,9 K, ×31) ; « L'IA sur CPU et sans GPU, avec Openvino » (Le Lab IA, 26,6 K, ×9,1).
- **« Comment ça marche » sur l'IA** : « L'IA laisse une trace invisible dans vos textes. Voici comment ça marche » (Machine Learning Lab, 2 200 abonnés, **177,8 K, ×539**) ; « 10 termes IA que tout le monde utilise sans vraiment les comprendre » (même chaîne, ×59).
- **Smartphones** : « J'ai tenté d'utiliser le plus vieil iPhone encore à jour » (Nightech, 166,9 K en 3 jours).
- Aucune vidéo française en format « combien ça coûte en local » ni « même carte, plus rapide ».

### Décision
- **Lun. 2/11 : « Combien coûte Claude en local ? »** (avancée du 4 janvier). C'est le format qui marche le mieux chez Kai (4 de ses plus gros succès) et que Morgans vient de refaire avec DeepSeek V4.1 Flash. Il n'existe pas en français, et il se produit sans gros essais. Le calcul part de DeepSeek V4.1 Flash, le modèle ouvert au niveau d'Opus 5 en code d'après le tableau de DeepSeek (à revérifier à la source).
- **Lun. 16/11 : Claude ou mon PC ? #1 (16 Go)**, avancée d'une semaine : 11 jours avant le Black Friday au lieu de 4. Kai « Is 16GB All You Need… » en est à 386 K.
- **À surveiller** :
  - la sortie de **Qwen 4 27B** : si elle tient dans 16 Go, c'est un épisode testé pour un créneau IA ;
  - le thème **« même carte, plus rapide »** (idée 16), le meilleur de Morgans, testable sur ta 5080 ;
  - le CTR d'ArtCraft après le changement de miniature.
- **Modifié le 22/10 au soir, par l'auteur** : les deux vidéos IA sont inversées. Claude #1 sort le 2/11 (essais sur la 5080 les 23-24/10) et Coût Claude le 16/11, pour réutiliser ces mesures.
