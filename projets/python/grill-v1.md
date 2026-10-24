# Grill du script Python v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Version finale : [`script.md`](script.md).
> Grille : `youtube-script-grill`, mode B (après l'écriture), **variante storytelling** (test des 30 secondes, axe 10 des liaisons, axes S1 à S6).
> Hypothèses : titre à choisir (voir « Le titre »), miniature dans la charte noire (`noir.html`), public de 18-30 ans curieux de tech, surtout africain, arrivé par l'accueil la semaine de Noël ; objectif : la 2e « grande histoire » du pilier, après le pixel (14 déc.).
> Faits revérifiés à la source le 23/10 : voir « Vérification des faits » en bas, et les lignes 27 à 34 ajoutées à [`sources.md`](sources.md).

## Note globale : 6,5/10

8 🟢, 9 🟠, 0 🔴. Rien de bloquant, et les faits de `sources.md` sont bien tenus. Mais la V1 rate sa propre question : elle pose « à quel moment tu t'ennuies assez… », puis répond par un crochet, alors qu'il existe un vrai fait qui y répond (le tweet de 2020, fait 34). Quatre phrases affirment des choses qu'aucune source ne tient, dont la légende « créé en une semaine ».

## Verdict

Le squelette marche : une légende posée puis corrigée par la vraie phrase de Guido, des récoltes bien plantées (« titre de travail », « à vie », les vacances), une analogie gamer qui fait comprendre Python 2 / 3 en une phrase, et une fin qui reprend le décor du hook. Les liaisons sont déjà à 2,5 pour 100 mots, bien au-dessus de la cible.

Le plus gros problème : la vidéo n'a pas de fin à la hauteur de sa question. Après la relance de 66 %, la section 8 répond à « Python peut-il tenir sans lui ? » par le copyright de la PSF (qui ne dit rien de qui décide), enchaîne quatre chiffres, se dégonfle sur « le projet de vacances ne gagne plus tout », puis la section 9 confie la réponse à un crochet. Or l'histoire a une vraie chute : en novembre 2020, Guido tweete que « la retraite, c'était ennuyeux » et retourne bosser sur Python. Le seul « ennui » de l'histoire, il est là, et il répond à ta question mieux que n'importe quel verdict. Deuxième problème : ta question, qui ouvre ton brouillon, arrive au 50e mot, derrière une scène.

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** : un projet pour occuper une semaine de Noël est devenu le langage que tout le monde utilise, IA comprise. Le hook la pose ; la vidéo la tient sur la naissance (sections 1 à 4), beaucoup moins sur le « devenu » : l'IA tient en une phrase (section 8), et le dernier tiers parle de gouvernance sans le dire.
- **Le problème de surface** : comment est né Python, et comment il a grandi.
- **Le problème profond** (ton sous-texte) : ce qu'un dev fait d'une semaine où personne ne lui demande rien. Il est semé (ta question), développé (« Moi, j'appelle ça s'ennuyer. Lui, il appelle ça un projet de loisir ») et devait se résoudre à la fin. La V1 le laisse en crochet. Le tweet de 2020 le résout avec un fait : quand Guido n'a vraiment plus rien à faire, il le dit enfin, et il recode.
- **La chaîne** (V1) : il s'ennuyait, **sauf qu'**il n'a jamais dit ça → **mais** il avait déjà un langage en tête, **donc** ABC → ABC arrêté, **et pourtant** inspiration clé → il manque un nom → Monty Python → **et** la légende de la semaine, **sauf que** quatorze mois → **et** du monde, **donc** quelqu'un pour trancher → BDFL → **et** Python 2 / 3 → **mais** le PEP 572 → vacances permanentes, **donc** tient-il sans lui ? → **et** la PSF, **et** les chiffres, **et** TypeScript, **et** TIOBE → retour à la question.
  Le « et ensuite » est visible à la fin : la section 8 empile au lieu de répondre. Dans `script.md` : tient-il sans lui ? → **oui** : un conseil de cinq, **et** Barry Warsaw (planté en 5) s'y assoit → **et** les chiffres, **sauf que** TypeScript, **mais** TIOBE → **mais** Guido, il devient quoi ? → retraite, **sauf qu'**un an plus tard, « ennuyeux » → retour à ta question.

## La fidélité au brouillon

Ton brouillon fait deux lignes. Ce que la V1 en fait :

| Ta phrase | Dans la V1 | Verdict |
|---|---|---|
| « A quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation » | Gardée mot pour mot, mais placée au 50e mot, après la scène de Noël, introduite par « Du coup, j'ai une question » | 🟠 Ta phrase est ton hook (la fiche dit « Type de hook : Question ») et elle a déjà tout ce qu'il faut à 0-5 s : le sujet et une tension (créer un langage par ennui, c'est absurde). `script.md` la remet en **première phrase**. « Du coup » ne reliait rien : on ne pose pas une question « du coup » d'une scène |
| « Lui c'est... » | Complété par « le dev en question, Guido van Rossum » (section 1) | 🟢 Le nom arrive après le contraste, c'est bien |
| « Et il se fesait tellement chier qu'il a décidé de créer un langage de programmation » | Gardée comme légende (« je te cache pas que c'était la mienne au début »), tamponnée, puis corrigée par la préface | 🟢 C'est juste (fait 5 : ni « bored » ni « ennui » dans la préface), et ça passe à l'oral : ta phrase arrive en entier, avec ton mot, et la correction vient de la bouche de Guido, pas d'un prof. Deux réglages dans `script.md` : la légende est attribuée à une vraie page (Interesting Engineering, « he found himself bored », fait 27), et la fin te donne raison à moitié, puisqu'il finit par dire qu'il s'ennuie, mais à la retraite |

**Ce qui a été perdu** : ton titre de travail, « l'ennui d'un dev à Noël », n'a plus de réponse dans la V1 ; ton brouillon promettait une vidéo sur l'ennui, la V1 finit sur un classement GitHub. `script.md` remet l'ennui au centre, du hook au tweet.

**Le « tellement chier » marche-t-il face à la vraie phrase ?** Oui, à une condition : que ta phrase sorte avec ton ton (rire, exagération), et que la citation de Guido soit lue plus posément. Le contraste « il se faisait tellement chier » / « pas grand-chose d'autre sur les bras » est drôle tout seul. Et « Moi, une semaine sans rien sur les bras, j'appelle ça s'ennuyer » garde ta lecture sans la mettre dans sa bouche.

## Le test des 15 premières secondes

Relues seules, à 145 mots/min (environ 36 mots) :

> « Noël mille neuf cent quatre-vingt-neuf. Un dev d'Amsterdam a son bureau fermé, un ordi à la maison, et pas grand-chose d'autre sur les bras. Ce qu'il commence cette semaine-là, aujourd'hui, ça s'appelle Python. »

🟠 **Presque.** Le contraste (une semaine de vacances → Python) est bien le moment le plus fort qui tienne sans préparation, et rien n'y est du remplissage. Deux manques :
- la première phrase n'a pas de tension : un bureau fermé, ce n'est pas un enjeu. Ta question en a une ;
- la moitié « aujourd'hui » du contraste arrive vers 0:17, et sous une forme abstraite (« GitHub en parle comme de la colonne vertébrale de l'IA »). À l'oral, « colonne vertébrale » ne fait pas d'image ; un chiffre, si : presque six devs sur dix (Stack Overflow 2025, fait 18).

Dans `script.md`, les 15 s deviennent : ta question (0-5 s), puis « Noël quatre-vingt-neuf. Un dev a son bureau fermé, et pas grand-chose d'autre sur les bras. Du coup, il commence un projet pour s'occuper. » Le « 57,9 % » s'affiche à l'écran dès 0:10, et la voix le dit à 0:16 (0:13 en coupes serrées). « Quatre-vingt-neuf » au lieu de « mille neuf cent quatre-vingt-neuf » gagne une seconde ; la date complète est à l'écran.

## Le test des 30 secondes

| Tranche | Ce que dit la V1 | Verdict |
|---|---|---|
| 0-5 s | > « Noël mille neuf cent quatre-vingt-neuf. Un dev d'Amsterdam a son bureau fermé… » | 🟠 Raccord avec le sujet, mais sans tension. |
| 5-15 s | > « Ce qu'il commence cette semaine-là, aujourd'hui, ça s'appelle Python. Et GitHub en parle comme de la colonne vertébrale de l'IA. » | 🟠 Le bon contraste, avec une preuve abstraite. |
| 15-30 s | > « Du coup, j'ai une question : à quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation ? » | 🟢 La question centrale, une seule, en mots simples, au 50e mot (règle : avant le 90e). « Du coup, j'ai une question » : 5 mots qui ne servent à rien. |
| Pont | > « Sauf que lui, il n'a jamais dit qu'il s'ennuyait. » | 🟠 Il ouvre une question (« alors, qu'a-t-il dit ? »), mais elle est refermée à 1:17 par la préface. Il n'ouvre rien qui tienne jusqu'au bout. |

**Budget :** 73 mots ≈ 30 s à 145 mots/min. 🟢
**À couper :** « Du coup, j'ai une question ».
**Réécriture des 30 s** (dans `script.md`, 83 mots ≈ 34 s à 145, 28 s à 180) :

> À quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation ?
> Noël quatre-vingt-neuf. Un dev a son bureau fermé, et pas grand-chose d'autre sur les bras. Du coup, il commence un projet pour s'occuper.
> Aujourd'hui, presque six devs sur dix disent s'en servir. Et c'est le langage de l'IA. Ça s'appelle Python.
> Sauf que lui, ce Noël-là, il ne parle jamais d'ennui. Le mot, il finira par l'écrire, mais plus de trente ans plus tard. Et pas à Noël.

Le pont ouvre maintenant une boucle qui court jusqu'à 11:30 (quand ? pourquoi ?), et il est vrai : le tweet date du 12/11/2020, trente ans et onze mois après décembre 1989 (fait 34). « Le langage de l'IA » est tenu par Octoverse (faits 16 et 24), sans « numéro un ».

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | La naissance est tenue ; le « devenu le langage de l'IA » tient en une phrase, et le titre de l'en-tête est trop proche de Codabee. |
| 2. Alignement | 🟢 | Aucune vente ; un appel à l'abonnement court, glissé dans le récit (« Et avant de te le donner »). |
| 3. Problème profond | 🟠 | Ton sous-texte est semé et développé, puis laissé à un crochet au moment de le résoudre. |
| 4. Public & complexité | 🟢 | PEP et BDFL expliqués avant d'être utilisés ; seul « interpréteur » arrive sans explication (corrigé). |
| 5. Valeur & originalité | 🟠 | Codabee raconte déjà décembre 1989, ABC, Monty Python et l'IA ; la V1 ajoute la légende corrigée, les quatorze mois, le BDFL et le mail de 2018, mais pas la gouvernance d'après ni le tweet de 2020, qui sont l'angle que personne n'a en français. |
| 6. Structure & transformation | 🟠 | Une chronologie propre, mais la section 8 répond à côté de sa propre question (le copyright au lieu de qui décide). |
| 7. Histoire (ascension) | 🟠 | Guido veut s'occuper, rien ne l'en empêche jusqu'en 2018 ; la crise est là, mais sans sa phrase la plus dure (« tant de gens méprisent mes décisions », fait 28). |
| 8. Mais / donc | 🟢 | Très bon jusqu'à la section 7 ; la section 8 empile en « et ». |
| 9. Engagement actif | 🟢 | Ta question, « Imagine », « Tu te rappelles ? », la sauvegarde corrompue, l'appel au commentaire de la fin. |
| 10. Rythme, oralité & liaisons | 🟢 | 2,5 liaisons pour 100 mots, mais « en gros » cinq fois, et deux sections faibles (4 et 9). |
| 11. Tics d'IA | 🟠 | Une dizaine de tics légers, dont deux hommes de paille (ABC « a changé le monde », « on lit souvent… en une semaine »). |
| S1. Les 30 premières secondes | 🟠 | Question avant 30 s, mais pas en tête, et une preuve abstraite. |
| S2. Le pont | 🟠 | Il ouvre une question refermée 50 s plus tard. |
| S3. Les retournements | 🟢 | Un toutes les 26 s en moyenne ; plus long trou 4:17 → 5:11. |
| S4. Planté / récolté et motif | 🟢 | « Titre de travail », « à vie », les vacances : trois récoltes et un motif. |
| S5. Personnages et enjeu | 🟠 | Guido a une envie (s'occuper), mais pas d'obstacle avant 2018 ; les autres sont des noms (Meertens, Pemberton, Manheimer, Warsaw) sans rôle. |
| S6. La fin | 🟠 | Elle revient à la question et au décor, mais elle résume et confie la réponse à un crochet ; juste avant, « ne gagne plus tout » la dégonfle. |

## L'axe 10 : les liaisons

Compte de `controle.py` sur la V1 : **45 liaisons pour 1 789 mots, soit 2,5 pour 100** (cible : 1,5). Par fonction : « mais » 7, « en gros » 5, « sauf que » 4, « donc » 4, « du coup » 3, « parce que » 3, « imagine » 3, « en fait » 3, puis « tu vois », « normalement », « et pourtant », « forcément », « bref » (2 chacun), « voilà pourquoi », « résultat », « tu te rappelles » (1 chacun).

| Section | Mots | Liaisons / 100 |
|---|---|---|
| 0. Hook | 73 | 2,7 |
| 1. La légende | 204 | 2,5 |
| 2. Le langage qui a raté | 208 | 2,9 |
| 3. Pas de serpent | 136 | 2,9 |
| 4. En une semaine ? | 201 | **1,5** |
| 5. Dictateur à vie | 163 | 2,5 |
| 6. Deux Python | 200 | 3,0 |
| 7. Vacances permanentes | 207 | 2,4 |
| 8. Et aujourd'hui ? | 242 | 3,3 |
| 9. Alors, il s'ennuyait ? | 155 | **1,3** |

**Les problèmes, au-delà du chiffre :**
- **« En gros » cinq fois** (« En gros, Python, c'est le fils… », « En gros, c'est un nom provisoire », « En gros, le titre dit ce qu'il veut dire », « Un PEP, en gros », « En gros, presque six devs sur dix »). Le garde-fou du skill : varier. `script.md` en garde deux, et passe les autres en « pour faire simple » ou les supprime.
- **« Du coup, j'ai une question »** : une liaison qui ne relie rien compte dans le chiffre, mais pas à l'oreille.
- **Les rafales de faits** :
  - section 6 : « Python deux point zéro sort le seize octobre deux mille. Huit ans plus tard, le trois décembre deux mille huit, arrive Python trois. Et Python trois, sa propre page de téléchargement le dit… » : trois dates au jour près, reliées par « et ». `script.md` garde les années et met un « sauf que » sur l'incompatibilité ;
  - section 8 : Stack Overflow, Octoverse +48 %, TypeScript, TIOBE −5,23, le documentaire, en une minute. `script.md` en fait des phrases séparées, chacune avec sa liaison (« Et pour le reste, les chiffres répondent », « Tu vois, les presque six sur dix du début », « Alors oui, si t'as vu passer… », « Du coup, sur GitHub, Python est deuxième ») et retire le −5,23 ;
  - section 9 : quatre phrases d'affilée sans liaison entre « Guido, lui, ne parle jamais d'ennui » et « Tu vois où je veux en venir ».

`script.md` : **2,5 pour 100** sur 1 869 mots, aucune section sous 1,6 (la section 9 passe de 1,3 à 2,0).

## Les tics d'IA

| Citation de la V1 | Tic | Dans `script.md` |
|---|---|---|
| « Normalement, c'est le moment où je te dis qu'ABC a changé le monde. » | Homme de paille : personne ne pense qu'ABC a changé le monde | « ABC, t'en as sûrement jamais entendu parler. Et c'est normal : … » |
| « On lit souvent qu'il a créé Python en une semaine. C'est une belle histoire, sauf qu'elle est fausse. » | Homme de paille, et non sourcé (aucune page trouvée qui le dise, fait 27) | « Là, tu dois te demander : en une semaine, il a fait un langage entier ? » (c'est le hook qui fait naître la question) |
| « Il lui fallait du temps devant lui. Et cette semaine-là, du temps, il en a. » | Chiasme d'écrit, et non sourcé (Guido ne dit pas qu'il manquait de temps) | « Et là, il a une semaine devant lui. » |
| « Et c'est là que la légende en rajoute une couche. » | Annonce (faux suspens léger) | retirée |
| « Et regarde la boucle. » | Annonce | retirée : la phrase des vacances suffit |
| « Normalement, avec un hook comme le mien, tu t'attends à ce que Python soit premier partout. » | Le script invente l'attente du spectateur, et parle de lui-même | « Alors oui, si t'as vu passer que TypeScript l'a doublé sur GitHub : c'est vrai. » (une info que le spectateur a pu croiser) |
| « Bref, le projet de vacances ne gagne plus tout. » | Petite morale de fin de paragraphe | « Bref, Python tient très bien sans son dictateur. Mais Guido, lui, il devient quoi ? » |
| « un truc que peu de langages ont vécu » | Superlatif non sourcé | « un truc bien pénible » |
| « Et qui a trouvé le surnom ? Même Guido ne sait plus. » | Question suivie de sa réponse | gardée : la réponse est l'info (même lui ne sait pas), ce n'est pas un faux suspens |
| « Il avait un bureau fermé, un ordi, une idée qui lui venait d'un langage raté, et pas grand-chose d'autre sur les bras. » | Énumération de récap | gardée en trois éléments, avec « qui n'a pas percé » |

Aucune fausse opposition « ce n'est pas A, c'est B » dans la V1 ni dans `script.md` (recherche faite).

## La rétention

- **Relances** : 28 dans la V1, une toutes les 26 s ; le plus long trou, 4:17 → 5:11 (54 s), dans la section 4. Dans `script.md`, 31 relances, plus long trou 42 s.
- **Ponts** : chaque section finit sur ce qui rend la suivante nécessaire. Le seul pont faible était celui du hook (voir le test des 30 s).
- **Abonnement** : à 3:08 (25 %) dans la V1, glissé entre « Il lui manque juste un nom » et la révélation du nom. C'est le bon endroit : on ne coupe pas une question, on la retarde de 8 secondes. Gardé (3:18, 26 % dans `script.md`).
- **La relance forte à 66 %** : la coupure musicale tombe à 8:10, alors que la règle la veut vers 60 %, et les 11 % qui précèdent sont des dates (Python 2 / 3). Dans `script.md`, la coupure passe à **62 % (7:53)** : sections 1 à 6 resserrées (dates sans les jours, la 2.7.18 et le copyright retirés), et la fin rallongée par du récit (le conseil de 2019, la retraite, le tweet). La relance porte aussi la phrase la plus dure du mail, qui manquait : « et découvrir que tant de gens méprisent mes décisions » (fait 28). C'est le seul moment bas de Guido dans toute l'histoire ; sans lui, la crise est un changement d'organigramme.
- **Après la relance** : la V1 n'avait plus de sommet (des chiffres, puis un crochet). `script.md` en a deux : Barry Warsaw à la table qui remplace le dictateur (9:55), puis le tweet (11:17).

## Le grill

### 1. La fin ne répond pas à ta question, alors que l'histoire y répond

> « Moi, j'appelle toujours ça s'ennuyer. [TON VERDICT, AVEC TES MOTS : ENNUI OU PAS ? …] »

**Pourquoi ça coince :** toute la vidéo est bâtie sur ta question. Arrivé à 11:15, le spectateur attend une réponse, et il reçoit un crochet. Ton verdict compte, mais il ne peut pas porter seul la chute.
**Correction :** le tweet du 12/11/2020, vérifié (fait 34, TechCrunch et InfoWorld le citent, Microsoft confirme l'arrivée) : « I decided that retirement was boring and have joined the Developer Division at Microsoft. » Après la retraite d'octobre 2019 (fait 33), c'est la première fois, dans nos sources, que Guido parle d'ennui. Ça donne une vraie fin :

> En octobre deux mille dix-neuf, il quitte Dropbox et prend sa retraite. Les vacances permanentes, pour de vrai.
> Sauf qu'un an plus tard, le douze novembre deux mille vingt, il tweete, je cite : « J'ai décidé que la retraite, c'était ennuyeux, et j'ai rejoint la division développeurs de Microsoft. »
> Le voilà, le mot. Plus de trente ans après Noël quatre-vingt-neuf. Et pas pendant les fêtes : à la retraite.

Puis ta question, ton verdict, et une phrase qui retourne : « Et en effet, le jour où il dit enfin qu'il s'ennuie, il retourne bosser sur Python. » Ton crochet reste ; il n'a plus à tout porter. Le hook plante la boucle (« Le mot, il finira par l'écrire… »).

### 2. La section 8 répond à côté de sa question

> « Donc la question que tout le monde se pose à ce moment-là, c'est : est-ce que Python peut tenir sans le mec qui l'a inventé ? »
> « En fait, sur le papier, Python ne dépend plus d'un seul homme depuis longtemps. Depuis la version deux point un, son copyright appartient à la Python Software Foundation… »

**Pourquoi ça coince :** la question porte sur qui décide. Le copyright ne dit pas qui tranche un PEP. La vraie réponse est dans les PEP 13 et 8100 : en décembre 2018, les développeurs du cœur votent pour un conseil de cinq personnes, et le premier, élu début 2019, compte Guido lui-même et Barry Warsaw (faits 31 et 32). Barry Warsaw est l'un des deux « suspects » du surnom BDFL (fait 14) : la récolte est toute trouvée.
**Correction :** dans `script.md`, « Du coup, retiens Barry Warsaw » (section 5), puis « En gros, le mec qui a peut-être inventé le dictateur à vie s'assoit à la table qui le remplace » (section 8). La PSF sort du script.

### 3. Le contrepied « Python n'est plus premier » dégonfle la fin

> « Bref, le projet de vacances ne gagne plus tout. »

**Pourquoi ça coince :** tu me demandais s'il fallait le garder. Il est vrai (fait 16), mais il arrive juste avant la chute et lui coupe l'élan : « il ne gagne plus tout », puis « alors, il s'ennuyait ? ». Ton sous-texte, c'est la semaine de libre, pas le classement, et la question de la section est « tient-il sans lui ? » : la réponse honnête est oui (+48 % sur GitHub, 57,9 % chez Stack Overflow, n° 1 chez TIOBE en octobre 2026).
**Correction :** on garde l'info, on la dit honnêtement, en une phrase, comme une nuance : « Alors oui, si t'as vu passer que TypeScript l'a doublé sur GitHub : c'est vrai. […] Du coup, sur GitHub, Python est deuxième. » Puis TIOBE, le documentaire, « Pas mal, pour un nom provisoire », et on finit sur un Python qui tient. Aucune phrase ne dit « premier partout ».

### 4. Quatre affirmations sans source

> « On lit souvent qu'il a créé Python en une semaine. »
> « Il lui fallait du temps devant lui. »
> « Python va vivre un truc que peu de langages ont vécu »
> « Python a un truc qu'ABC n'a jamais eu : du monde. »

**Pourquoi ça coince :** « Les faits comptent ». La légende de l'ennui existe (fait 27) ; celle de la semaine, aucune page trouvée ne la donne. Les trois autres sont des généralisations.
**Correction :** voir la vérification des faits. La semaine devient la question du spectateur (le hook la fait naître : « il commence un projet »), le « du monde » s'appuie sur la réunion de huit personnes de 1995 (fait 30), les deux autres sont retirées.

### 5. Ta question n'est pas en tête

Voir « La fidélité au brouillon » et le test des 30 s.

### 6. Le titre de l'en-tête

Voir « Le titre ».

### 7. Petits points

- « un langage qui a raté » (section 2 et titre de section) : Guido écrit « lack of obvious success ». « Qui n'a pas percé » dit la même chose, sans aller plus loin que lui.
- « interpréteur » arrive sans explication pour un public qui ne code pas tous en Python : ajouté « pour faire simple, le programme qui lit ton code et l'exécute ».
- « Et c'est Guido lui-même qui l'écrit, sur son blog, en deux mille neuf » : juste (fait 8), gardé.
- La section 6 imagine « une boîte qui a des milliers de lignes écrites en Python deux » : il y a un vrai exemple, la boîte de Guido lui-même. Dropbox écrit en 2019 qu'il a lancé le passage de son code serveur à Python 3 (fait 33). Plus concret, et ça plante Dropbox pour la retraite de la section 9.

## Le titre

Codabee a sorti *Il s'ennuyait à Noël: Il a créé Python* le 18/09/2026 (fait 22). Les trois titres de la V1 :

| Titre | Verdict |
|---|---|
| *Il voulait juste s'occuper à Noël. Il a créé Python.* (celui de l'en-tête) | ❌ Même squelette que Codabee (« Il [verbe] à Noël. Il a créé Python. ») : vidIQ et les suggestions les rapprocheront, et la règle est de ne pas copier un concurrent. Et « Il a créé Python » collé à « à Noël » se lit « créé pendant Noël », la lecture que le fait 26 interdit. |
| *Noël 1989 : un bureau fermé, et Python est né* | 🟠 Juste (« né » = commencé), distinct, avec la saison et l'année. Mais « un bureau fermé » ne donne pas envie de cliquer : il n'y a ni contraste ni enjeu. |
| *Il a créé Python pendant ses vacances de Noël* | ❌ « Pendant » dit que tout s'est fait pendant les vacances : c'est le « créé en une semaine » (fait 26). |

**Recommandé : *Python, le langage de l'IA, est né d'un projet de vacances*** (le titre 3 de la fiche, avec le mot-clé « Python » en tête). Pourquoi :
- tout est tenu : « projet de vacances » (« a hobby programming project » pour « la semaine autour de Noël », fait 1), « est né » (il a commencé là), « le langage de l'IA » (« the backbone of applied AI work », faits 16 et 24, sans « numéro un ») ;
- le contraste est dans le titre (projet de vacances → langage de l'IA), et c'est exactement le hook ;
- rien de commun avec Codabee : ni « s'ennuyait », ni « Il… Il a créé » ;
- il marche toute l'année, alors que la vidéo vivra surtout par l'accueil ;
- la contrepartie : la vidéo doit tenir « le langage de l'IA ». `script.md` le dit dans le hook et cite Octoverse en section 8. Si tu veux plus d'IA à l'écran, il faudra des faits de plus dans `sources.md`.

Si tu tiens à la saison, le titre 2 est le seul des trois à garder.

## Vérification des faits du script

Chaque phrase de la V1 qui affirme quelque chose, contre `sources.md` (colonne « 2e vérif ») ou, à défaut, la source primaire relue le 23/10/2026.

| Phrase de la V1 | Fait | Verdict | Dans `script.md` |
|---|---|---|---|
| « Noël 1989. Un dev d'Amsterdam a son bureau fermé, un ordi à la maison, et pas grand-chose d'autre sur les bras » | 1, 2 | ✅ | gardé, raccourci (« Amsterdam » vient avec la préface) |
| « Ce qu'il commence cette semaine-là, aujourd'hui, ça s'appelle Python » | 1, 9 | ✅ « commence » | « il commence un projet pour s'occuper » |
| « GitHub en parle comme de la colonne vertébrale de l'IA » | 16 | ✅ (« of applied AI work ») | déplacé en section 8 ; le hook dit « le langage de l'IA » (fait 24) |
| (ajouté) « presque six devs sur dix disent s'en servir » | 18 | ✅ 57,9 % des répondants, 2025 | hook, avec la source à l'écran |
| « Sauf que lui, il n'a jamais dit qu'il s'ennuyait » | 5, 34 | ⚠️ vrai pour 1989, faux pour 2020 : il dit que la retraite était « boring » | « ce Noël-là, il ne parle jamais d'ennui » |
| « l'histoire qu'on raconte, c'est celle-là » ; « c'était la mienne au début » | 27 ; brouillon | ✅ la légende existe (Interesting Engineering) ; ta phrase du brouillon | gardé, attribué à « un site de biographies d'ingénieurs » |
| La préface, 1996, *Programming Python*, la citation traduite | 1, 2 | ✅ | gardé |
| « un nouveau langage de script auquel il pensait ces derniers temps… descendant d'ABC… hackers Unix et C » | 3 | ✅ | gardé (« depuis quelque temps ») |
| « reculer de sept ans. Fin 1982, Guido entre au CWI » | 7 | ✅ (1989 − 1982) ; le billet ajoute « fresh out of university » | ajouté « sort de la fac » |
| « un institut de recherche en maths et en informatique » | 7 | ✅ c'est le nom (Centrum Wiskunde & Informatica) | gardé |
| « groupe d'ABC, celui de Lambert Meertens et Steven Pemberton » | 7 | ✅ | gardé |
| « Normalement, c'est le moment où je te dis qu'ABC a changé le monde » | — | tic, sans contenu | retiré |
| « arrêté au bout de quatre ou cinq ans, faute de succès évident » ; « sur son blog, en 2009 » | 8 | ✅ relu le 23/10 : « terminated due to the lack of obvious success » | gardé |
| « l'inspiration clé » | 8 | ✅ | gardé |
| « le fils d'un langage qui a raté » | 8 | ⚠️ plus fort que « lack of obvious success » | « qui n'a pas percé » |
| « Il lui fallait du temps devant lui » | — | ❌ non sourcé | « Et là, il a une semaine devant lui » |
| « titre de travail », « humeur un peu irrévérencieuse », fan du *Flying Circus* | 4 | ✅ | gardé |
| « il lisait les scripts publiés… BBC années 70… court, unique, un peu mystérieux » | 6 | ✅ (« When he began implementing Python ») | « Quand il commence à coder, il lit… » |
| « Trente-sept ans plus tard » | calcul | ✅ décembre 1989 → décembre 2026 | gardé |
| « Forcément, tout le monde pense au serpent » | — | blague, sans fait | « tu penses au serpent » |
| « On lit souvent qu'il a créé Python en une semaine » | 26, 27 | ❌ aucune source ne le dit (recherche du 23/10) | devenu la question du spectateur |
| « fin décembre 1989… une version qui marche dans les premiers mois de 1990 » | 9 | ✅ | gardé |
| 0.9.0 sur alt.sources le 20/02/1991, forum Usenet | 10 | ✅ | gardé |
| « Pas de GitHub… le code arrive dans des messages » | — | ✅ c'est ce qu'est alt.sources (un groupe Usenet de code source) ; GitHub naît en 2008 | gardé |
| « Quatorze mois » | 26 | ✅ | gardé |
| Python 1.0 le 26/01/1994 | 11 | ✅ | « en janvier quatre-vingt-quatorze » |
| « Python a un truc qu'ABC n'a jamais eu : du monde » | — | ⚠️ « jamais eu » non sourcé | « Python commence à avoir du monde autour », tenu par la réunion de huit personnes d'avril 1995 (fait 30) |
| CNRI, Reston, avril 1995 ; préface signée en mai 1996 | 1, 14 | ✅ | gardé (« un an plus tard ») |
| « le dix-huit avril, pendant une réunion, on lui trouve un titre » | 14, 30 | ✅ ; la réunion visait à monter une organisation autour de Python, huit présents | précisé |
| « sur Python, le dernier mot, c'est lui » | 14 | ✅ sens du titre | gardé |
| « sans doute Ken Manheimer ou Barry Warsaw, peut-être toute la salle… plus personne ne s'en souvient » | 14 | ✅ | gardé |
| « un truc que peu de langages ont vécu » | — | ❌ non sourcé | « un truc bien pénible » |
| « deux versions incompatibles, côte à côte, pendant onze ans » | 11, 12, 13 | ✅ | gardé |
| Python 2.0 le 16/10/2000, 3.0 le 03/12/2008, incompatible avec la branche 2 | 11, 12 | ✅ | gardé (années seulement) |
| « ton programme écrit pour Python deux peut ne plus tourner sur Python trois » | 12 | ✅ | gardé |
| fin de Python 2 le 01/01/2020, onze ans après Python 3 | 11, 13 | ✅ | gardé |
| 2.7.18 en avril 2020, après la date de fin | 13 | ✅ | retiré (rafale) |
| « pense à une boîte qui a des milliers de lignes écrites en Python deux » | — | hypothèse | remplacé par Dropbox (fait 33) |
| Un PEP = une proposition pour faire évoluer Python ; PEP 572, `:=` | 15 | ✅ | gardé |
| « que les devs surnomment le morse » | 29 | ✅ et mieux : c'est la doc officielle (What's New 3.8) qui le dit | « la doc officielle le surnomme elle-même » |
| mail du 12/07/2018, « Transfer of power », « me battre autant pour un PEP », « vacances permanentes » | 15, 28 | ✅ | gardé, avec la suite de la phrase : « et découvrir que tant de gens méprisent mes décisions » |
| « t'en es le chef depuis plus de vingt ans » | 14, 15 | ✅ (1995 → 2018 : 23 ans) | gardé |
| « la vie, elle aura duré vingt-trois ans » | 14, 15 | ✅ | gardé |
| « pas de successeur… il reste développeur du cœur » | 15, 28 | ✅ (« an ordinary core dev ») | « simple développeur du cœur » |
| « Donc la question que tout le monde se pose » | — | ⚠️ « tout le monde » | « Donc la vraie question, à ce moment-là » |
| copyright de la PSF depuis la 2.1 | 19 | ✅ mais ne répond pas à la question | retiré |
| (ajouté) vote de décembre 2018, conseil de cinq, réélu après chaque grande version ; premier conseil début 2019 avec Guido et Barry Warsaw | 31, 32 | ✅ PEP 13, PEP 8100 | section 8 |
| Stack Overflow 2025 : 57,9 %, +7 points | 18 | ✅ | gardé |
| Octoverse : +48 % ; « la colonne vertébrale » de l'IA appliquée | 16 | ✅ | gardé |
| « Normalement, avec un hook comme le mien, tu t'attends à ce que Python soit premier partout » | — | tic | retiré |
| TypeScript devant en août 2025, ~42 000 contributeurs par mois ; « numéro deux sur GitHub, en nombre de contributeurs » | 16 | ✅ | gardé |
| TIOBE octobre 2026 : n° 1, 19,23 %, −5,23 points | 17 | ✅ | « encore numéro un », daté ; pourcentage et baisse retirés (rafale) |
| documentaire de 2025, plus d'un million de vues | 21 | ✅ vidIQ du 23/10 | gardé, à redater avant la voix |
| (ajouté) retraite en octobre 2019, Dropbox | 33 | ✅ blog de Dropbox, 29/10/2019 | section 9 |
| (ajouté) tweet du 12/11/2020, « la retraite, c'était ennuyeux », Microsoft | 34 | ✅ cité par TechCrunch et InfoWorld, Microsoft confirme ; l'original n'a pas pu être ouvert | section 9 ; capture de l'original à faire |
| « ton bureau, ta fac ou ton école soit fermé » | — | « il y a des chances » : hypothèse dite comme telle | gardé |
| « l'histoire du jeu vidéo, d'un seul pixel à des milliards de joueurs » | projet pixel | ✅ (fiche du pixel) | gardé |

**Corrigé au total** : 4 affirmations non sourcées retirées ou reformulées (la semaine, « du temps devant lui », « peu de langages », « jamais eu du monde ») ; 3 formulations ramenées à la source (« raté », « jamais dit qu'il s'ennuyait », « que les devs surnomment ») ; 1 réponse hors sujet remplacée (la PSF) ; 8 faits ajoutés à `sources.md` (lignes 27 à 34), tous vérifiés le 23/10/2026.

## Ce qu'il faut garder

- **La légende tamponnée** : « il se faisait tellement chier… », puis la vraie phrase. C'est ta voix et c'est la meilleure scène de la première minute.
- **« Moi, une semaine sans rien sur les bras, j'appelle ça s'ennuyer. Lui, il appelle ça un projet de loisir. »** : ta lecture, sans trahir la sienne.
- **« Trente-sept ans plus tard, personne n'a trouvé mieux. »** : la meilleure blague, et une récolte.
- **La sauvegarde corrompue** : Python 2 / 3 compris en deux phrases, avec ton humour gamer.
- **« Pour le Nouvel An, les devs Python ont eu droit à un enterrement. »** : le motif des fêtes, au bon moment pour une vidéo du 28 décembre.
- **« Eh ben la vie, elle aura duré vingt-trois ans. »** : la récolte de « à vie ».
- **La fin dans le même appartement, en 2026** : la semaine de Noël du spectateur. C'est l'engagement le plus naturel de la chaîne à ce jour.

## Plan d'action (appliqué dans `script.md`)

1. Ta question en première phrase ; le chiffre de Stack Overflow à la place de « colonne vertébrale » ; un pont qui plante le tweet de 2020.
2. La fin sur le tweet « la retraite, c'était ennuyeux », avec ton verdict à la suite.
3. La section 8 répond à sa question : le conseil de 2019, Barry Warsaw récolté, les chiffres un par un, le contrepied en une phrase.
4. Les quatre affirmations sans source corrigées, les tics retirés, « en gros » ramené à deux.
5. Les dates de la section 6 allégées pour que la relance tombe à 62 %, avec la phrase « tant de gens méprisent mes décisions ».

Contrôle de `script.md` (`controle.py`) : **1 869 mots** de voix off (12 min 55 à 145 mots/min, 10 min 25 à 180), **2,5 liaisons pour 100 mots**, hook de 83 mots avec la question au 1er mot, **0 « vous »**, 11 crochets à remplir (dont tes 5 crochets de vécu et de verdict).

## Les questions pour toi

1. **Le titre** : *Python, le langage de l'IA, est né d'un projet de vacances* te va ? Sinon, *Noël 1989 : un bureau fermé, et Python est né*.
2. **La fin avec le tweet de 2020** : d'accord pour qu'elle réponde à ta question avant ton verdict ? Fais une capture du tweet original (@gvanrossum) avant le montage.
3. **Ton verdict** (section 9) : ennui ou pas, avec tes mots.
4. **Ton vécu** : premier script Python, Python 2 ou 3, un projet raté qui t'a servi. Rien de vrai : on coupe.
5. **L'URL de l'entretien de Guido sur la chaîne GitHub** (253 K vues), pour `upload.md`.
