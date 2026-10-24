# Deux cartes d'occasion pour avoir le maximum de VRAM

> Phase 1 (recherche) du 24/10/2026. Placée le 24/10 au **lun. 21 déc.** (créneau radar IA, ta décision), dans [`strategie.md`](../../strategie.md) (idée 23), le [`calendrier.md`](../../calendrier.md) et le [`README.md`](../../README.md). Vidéo **calculée** : tu n'achètes pas de cartes. Tous les faits (F…) et les sources sont dans [`sources.md`](sources.md). Machine de test : [`../claude-ou-mon-pc-1/fiche.md`](../claude-ou-mon-pc-1/fiche.md). **2e vérification le 24/10** : corrections listées en bas de `sources.md` ; les prix d'occasion sont à relever par toi ([PRIX D'OCCASION À RELEVER]).

**Origine** : ton idée du 24/10 : « une vidéo avec 2 cartes graphiques pas chères d'occasion pour avoir le max de VRAM ». Format **calculé** (ta décision du 24/10 : tu n'achètes pas de cartes, on en parle en théorie). Règles du calculé : [`strategie.md`](../../strategie.md), pilier 2 (« d'après mon calcul » dès le hook, aucune vitesse inventée).

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (Hub + Help) |
| **Format** | Longue, 11-13 min. **Calculée** : aucun achat, aucune mesure |
| **Trafic visé** | Recherche et suggestions, à côté des vidéos matériel de Locally, Digital Spaceport et RepoChad (sources.md) |
| **Mot-clé** | ia en local (21 403 recherches par mois estimées, +90,8 %). « carte graphique occasion ia » et « 2 cartes graphiques ia » : moins de 750 chacun. |
| **Type de hook** | Résultat chiffré (d'après mon calcul, le modèle qui ne tient pas dans ta 5080 tiendrait sur deux cartes d'occasion à [PRIX D'OCCASION À RELEVER]) |
| **Production estimée** | ~15-18 h (estimation, vidéo calculée) : relevé des prix, script, animations |

## Pourquoi cette vidéo

- **Rien en français** : aucune vidéo française sur le multi-GPU d'occasion pour l'IA dans vidIQ (24/10, sources.md). En anglais, c'est déjà un sujet : TinyTechGuy « deux déchets électroniques » 60,3 K vues (18/10), Lon.TV V100 32 Go 386 K (06/09), Digital Spaceport 137 K (16/09), RepoChad « 48 Go » 41 K (21/09).
- **Ton angle libre** : ce que personne ne fait, c'est **les prix et la garantie en France, en euros**, et **la comparaison à VRAM égale** (2 × 12 Go contre 1 × 24 Go), dans **une vraie carte mère micro-ATX** avec une 5080 déjà dedans. Tu ne copies ni le classement de Locally, ni les 5 routes de RepoChad, ni le rig de minage.
- **Elle prolonge « Abonnement ou IA locale ? #1 »** (ex-« Claude ou mon PC ? #1 », 16 nov.) : la 5080 de 16 Go ne tient pas un 27 B en Q4 (16,46 Go, F41) ; cette vidéo répond à « et si j'ajoute de la VRAM pas chère ? ».
- **Elle nourrit deux autres vidéos** : le guide d'achat d'avant le Black Friday (prix et pièges de l'occasion) et « Louer, acheter ou s'abonner » en janvier (section « Pour les conseils d'achat d'occasion » de `sources.md`).
- ⚠️ **Public** : 63 % de tes spectateurs sont en Afrique. leboncoin, la garantie légale française et les prix de la fiche ne s'appliquent pas à eux. [CROCHET : veux-tu un encart « si tu n'es pas en France », ou garder l'angle France pour la recherche française ?]

## Titres

1. Recherche : *IA en local : 2 cartes graphiques d'occasion pour 24 Go de VRAM, ça vaut le coup ?*
2. Curiosité : *Deux cartes d'occasion contre ma RTX 5080 : laquelle fait tenir la plus grosse IA ?*
3. Mixte (recommandé) : *2 cartes graphiques d'occasion pour l'IA que ma 5080 refuse : j'ai fait le calcul*

Pas de « j'ai acheté » ni de « j'ai testé » : la vidéo est calculée (24/10). « Refuse » reste vrai : le Q4 de Qwen3.8-27B (16,46 Go) ne tient pas dans 16 Go, mais l'IQ3_S de 11,77 Go y tient (F41, F43) : dis-le dans la vidéo.

## Miniature (charte verte)

Règles de la section 2 de [`propositions.md`](../../ressources/miniatures/propositions.md) : ardoise `#34495e` quadrillée, jamais assombrie ; dessin au trait ; **un grand objet** ; Archivo Black en capitales, 3 mots au plus pour la ligne principale, terminée par « . » ou « ? » ; contexte gris de 4 mots au plus ; la menthe `#07c095` est le seul accent ; pas de badge incliné ; **pas** la composition « logo → flèche → machine » de Kai.

- **Idée** : un seul grand dessin au trait de **deux cartes graphiques collées** qui forment une seule jauge de VRAM, remplie à la menthe. C'est le grand objet.
- **Texte** : contexte gris « 2 CARTES D'OCCASION » ; ligne principale « 24 GO ? » (le point d'interrogation en menthe : c'est un calcul, pas un test).
- **Ne répète pas le titre** : le titre dit « pour lancer l'IA que ma 5080 refuse », la miniature dit le chiffre.
- **À comparer** (planche des suggestions, `planches.py --suggestions`) à celles de TinyTechGuy et Locally pour ne pas leur ressembler à 168 px.
- Pas de visage obligatoire. Pas de photo de cartes : tu ne les as pas.

## Contenu (plan)

1. **Le résultat du calcul (0:00-0:15)** : voir plus bas.
2. **Le mur des 16 Go (0:15-1:30)** : ta 5080 ne lance pas le Q4 de Qwen3.8-27B (16,46 Go, F41). La question : et si on ajoutait de la mémoire pas chère ? Règle du calculé dite vers 0:30 : « je n'ai pas acheté ces cartes, tout ce qui suit est calculé ». Renvoi vers *IA en local* (2 nov.) pour « Q4 » et « 27B ».
3. **Combien de VRAM par euro, en France** (1:30-4:00) : le tableau « € par Go » (sources.md) avec tes relevés du jour. Ordre de grandeur ⚠️ : 3060 12 Go ≈ 20-25 €/Go, 3090 ≈ 33-42, RX 6800 XT ≈ 22-25, P40 et MI50 6-14, V100 14-28 (F1-F14). Les vrais chiffres viennent de tes relevés. Précise « prix demandés, pas des ventes » et la date.
4. **Comment deux cartes s'additionnent** (4:00-6:30) : llama.cpp découpe le modèle en tranches de couches (`--split-mode layer`, défaut, F20) ; chaque carte garde sa tranche ; **pour une seule conversation, elles travaillent chacune leur tour**. `--tensor-split` règle la part de chacune (F21). Image : deux bureaux, un modèle trop gros pour un seul. La VRAM s'additionne, la vitesse non (F33). Ollama et LM Studio le font tout seuls (F24, F26).
5. **Trois combinaisons, calculées** (6:30-9:30) : 2 × RTX 3060 (24 Go), ta 5080 + une RTX 3090 (40 Go), 2 × RTX 3090 (48 Go). Pour chacune : le prix [PRIX D'OCCASION À RELEVER], le prix par Go, et ce qu'elle demande au PC. Ta carte mère sert d'exemple : le 2e slot est un PCIe 3.0 x4 tout en bas, une carte de 2 slots y dépasse et demande un boîtier à 5 emplacements (F60, F63) ; ton alimentation n'a peut-être plus que deux 8 broches avec la 5080 branchée (F61). « Avant d'acheter, vérifie ça chez toi. »
6. **Ce qui tient dans 24, 32, 40 et 48 Go** (9:30-11:00) : le tableau de `sources.md` (section C), tailles de fichiers de Hugging Face. **Aucune vitesse à toi** : seulement les mesures publiées et datées marquées ✅ dans `sources.md`, ou le plafond calculé comme dans Coût Claude (bande passante ÷ Go lus par token), dit comme une estimation.
7. **Les pièges** (11:00-12:00) : cartes de minage et pads (F73), ventilateur et sortie vidéo des P40 et MI50 (F71, F72), fin de CUDA pour Pascal et Volta (F70), pas de ROCm pour la MI50 ni la RX 6800 XT (F70), garantie (F74-F77) et les 14 jours pour tester (F79).
8. **Le verdict par profil et ton avis** (12:00-13:00) : tu as une carte de 12 ou 16 Go ; tu pars de zéro ; tu n'as pas besoin de ça, reste sur l'abonnement. Le calcul en quatre cas de la série (« Abonnement ou IA locale ? ») avec la paire la moins chère. [CROCHET : TON AVIS, AVEC TES MOTS.] Pont vers le Mac mini (1er févr.) : l'autre façon d'avoir beaucoup de mémoire.

## Le calcul (sans achat)

Ta décision du 24/10 : **tu n'achètes pas de cartes**. Tout se calcule à partir de `sources.md` :

| Combinaison | VRAM | Prix | € par Go | Ce qui tient (section C de `sources.md`) | Ce que ça demande au PC |
|---|---|---|---|---|---|
| 2 × RTX 3060 12 Go (pas la 8 Go, F65) | 24 Go | [PRIX D'OCCASION À RELEVER] × 2 | ≈ 20-25 ⚠️ | Qwen3.8-27B Q4_K_M (16,46 Go, F41) | 2 slots, dont un en x4 sur beaucoup de micro-ATX (F60) |
| Ta 5080 + 1 RTX 3090 | 40 Go | [PRIX D'OCCASION À RELEVER] | ≈ 33-42 ⚠️ (la 3090) | Qwen3.6-35B-A3B Q6_K (30,01 Go), Nemotron Bolt UD-IQ3_XXS (31,56 Go) (F44-F46) | boîtier à 6 emplacements, prises 8 broches (F61, F63) |
| 2 × RTX 3090 | 48 Go | [PRIX D'OCCASION À RELEVER] × 2 | ≈ 33-42 ⚠️ | Llama 3.3 70B Q4_K_M (42,52 Go, F49) | un second PC, en pratique |

Vitesse : rien de mesuré. Ne cite pas les vitesses d'autres chaînes marquées ⚠️ (F28, F29, F31, F32). Pas d'électricité (décision du 23/10).

(Le protocole d'essais avec achat de la 1re version a été retiré le 24/10, à ta demande.)

## Les 15 premières secondes

Règle du 22/10 : le meilleur moment d'abord, aucun contexte, aucun « dans cette vidéo ». Brouillon (vidéo calculée : « d'après mon calcul » dès la première phrase, règle 4) :

> « Ce modèle ne rentre pas dans ma RTX 5080. [IMAGE : la barre de 16,46 Go qui dépasse de la jauge de 16 Go] D'après mon calcul, deux cartes d'occasion à [PRIX] euros le feraient tenir, avec de la place en plus. [IMAGE : deux cartes dessinées qui forment une jauge de 24 Go] Sauf que deux cartes, ça n'additionne pas la vitesse. »

- L'image promise par la miniature (les 24 Go) est dans les premières secondes.
- Les 30 premières secondes (règle du 23/10) : la question centrale (« est-ce que deux cartes pas chères valent une grosse ? ») arrive avant 30 s, puis la règle du calculé, puis un pont vers le prix par Go. Pas de présentation de la chaîne.

## Texte et sous-texte

- **Texte** : la VRAM s'additionne, la vitesse non ; avec deux cartes d'occasion, tu ferais tenir un modèle que ta carte neuve refuse.
- **Sous-texte** : l'IA en local n'est pas réservée à celui qui a une carte à 1 900 € (médiane RTX 5080 au 24/10, F15) ; on peut y arriver par l'occasion, à condition de savoir où on met les pieds. C'est le même fil que « les applis font le téléphone » : ici, c'est le logiciel (llama.cpp) qui transforme deux cartes bon marché en une grosse. [CROCHET : le sous-texte exact est le tien ; cette formulation est une proposition, ne la garde que si elle te ressemble]
- C'est un calcul, pas un test : ne dis jamais « j'ai essayé ». Les pièges se montrent avec des sources, pas avec ton vécu.

## Où la placer

- **Lun. 21 déc.**, ta décision du 24/10 (créneau radar IA) : pixel le 14, Python le 28, l'alternance tient. Vidéo **calculée**, sans achat.
- Le guide d'achat de Claude #1 (16 nov.) reprend déjà les conseils d'occasion vérifiés de `sources.md`. Louer, acheter (4 janv.) peut renvoyer vers celle-ci, et elle renvoie vers le Mac mini (1er févr.).

## Points à vérifier (avant le script)

1. **Slots de la carte mère** (F60) : ✅ vérifié dans le manuel Gigabyte (2e vérif, 24/10) : le second slot est un PCIe 3.0 x4 relié au chipset, en dernière position, environ 3 positions sous le x16 ; les deux M.2 sont reliés au processeur et ne prennent rien au slot x4.
2. **Place dans le boîtier** (pour l'exemple de la section 5, pas pour un achat) : nombre d'emplacements de slot, espace sous la carte mère, longueur des cartes. La 5080 X3 OC fait 2,5 slots, 50 mm (F63 : la page Inno3D le confirme ; le « 2 slots » du revendeur, c'est la X3 sans OC). Une carte de 2 slots dans le slot x4 demande 5 emplacements ; une 3090 Founders Edition (3 slots), 6.
3. **Alimentation** (même chose : un exemple pour le spectateur) (F61, F62) : la RM1000e 2025 (CP-9020297) a 4 connecteurs 8 broches PCIe, mais une seule prise 12V-2x6 sur le bloc, que le câble double semble partager avec le câble de la 5080. Regarde l'étiquette (référence) et le panneau de ton bloc : combien de 8 broches restent avec la 5080 branchée ? Une 3090 en demande 2 (Founders Edition) ou 3 selon le modèle.
4. **Prix** : relève de vraies annonces leboncoin, eBay.fr et boutiques (LDLC, rayons « seconde vie » ; l'annonce Grosbill de F78 n'existe plus) la veille du script : tous les prix d'occasion de la fiche sont à relever par toi. Prix de la MI50 contradictoire (F14), 4060 Ti 16 Go et A770 d'occasion non trouvées (F11, F12).
5. **Garantie** : ✅ vérifié (2e vérif, 24/10) : 2 ans même d'occasion, qu'un pro ne peut pas réduire (L217-3, L219-1 « d'ordre public »), défaut présumé 12 mois (L217-7) ; 14 jours de rétractation après réception pour un achat à distance chez un pro (L221-18) ; vices cachés 2 ans après la découverte (C. civ. 1648).
6. **Ce qui existe** : TinyTechGuy et Locally (« Two cheap GPUs against one expensive one ») traitent déjà le sujet en anglais, avec des tests : regarde-les en entier pour ne pas reprendre leur angle. Notre angle : les euros, la garantie en France, et ce que ça demande à un vrai PC.
7. **Versions** : llama.cpp (`--split-mode tensor` est « expérimental », F20), pilote NVIDIA 580 pour Pascal (F70), version de CUDA.
8. **Faits chiffrés de la vidéo** : chaque prix a une date et le mot « demandé ». Ne dis pas « une 3090 coûte X » sans la date.
9. **Modèles** : aucun modèle « uncensored » ou « abliterated » (les dépôts Hugging Face en proposent pour Qwen3.8-27B ; prends les versions d'Unsloth, d'ISTA ou de Bartowski listées dans `sources.md`).
