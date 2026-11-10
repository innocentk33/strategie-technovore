# Grill du script WhatsApp v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Grille : `youtube-script-grill`, mode B (après l'écriture), variante storytelling (test des 30 secondes, axe 10, axes S1 à S6).
> Hypothèses : titre *Comment une cinquantaine d'ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes* (ou le titre 4 avec la miniature `noir-06`, « 900 millions, 50 ingénieurs. ») ; public de 18-30 ans, surtout africain, pour qui WhatsApp est l'appli n° 1, avec une bonne part de devs ; objectif : la 3e vidéo du pilier « Le génie derrière l'app », sortie le lun. 11 janv. 2027.
> Faits revérifiés à la source le 23/10 : les diapositives de Rick Reed de 2012 et de 2014 (texte extrait des PDF) et l'article de Wired (archive de 2016). Voir « Vérification des faits » en bas, et les lignes 30 à 36 ajoutées à [`sources.md`](sources.md).
> Version finale : [`script.md`](script.md).

## Verdict

Le squelette est bon, et c'est le meilleur hook des scripts génie à ce jour : le chiffre de la miniature tombe en 12 secondes, daté, et la question centrale arrive à 25 s. La carte « langage, serveur, équipe » donne une raison d'avancer, le teaser des 2,8 millions est payé pile à 58 %, et les récoltes marchent (les photos de bonne année, le serveur bloqué à 425 000, le livreur de RAMEN). Les liaisons sont déjà là : 2,1 pour 100 mots, contre 0,7 à 0,9 dans tes téléprompteurs.

Les problèmes sont ailleurs, et ils sont trois :
- **des faits qui débordent les sources** : la V1 dit que le pic de 2,8 millions est « monté tout seul avec le trafic » (la diapo n'en dit pas la cause), et son image finale de l'île affirme que « toute ton équipe travaille sur la même île », alors que la diapo de 2014, citée deux minutes plus tôt, met une dizaine de personnes seulement sur Erlang ;
- **une fin pas préparée** : la question retournée (« et si ça tenait justement parce qu'ils étaient cinquante ? ») tombe à 11:55 sans avoir été semée, et sans ton avis ;
- **pas de personnage** : Rick Reed et Mahdavi sont des sources qu'on cite, pas des gens qui veulent quelque chose. Or les diapos de Reed contiennent sa propre histoire : il arrive en 2011 « nouveau sur Erlang », et c'est lui qui pousse un serveur au-delà de deux millions.

Rien de bloquant. La V2 corrige les faits, plante la fin dans la section 1 et fait de Rick Reed le fil de la section 3.

**Note globale : 🟠, 7/10.** 11 🟢, 6 🟠, 0 🔴 sur les 17 axes (11 de la grille, S1 à S6), plus 🟠 sur les faits : 6 inexactitudes et une action inventée, toutes corrigées dans la V2.

## Promesse, problème profond, « mais / donc »

- **Promesse** (titre + miniature) : « 900 millions de personnes, 50 ingénieurs : comment ? ». Le spectateur veut le *comment*, en mots simples. La V1 le livre en trois étages (langage, serveur, équipe). 🟢
- **Problème de surface** : comment une équipe minuscule fait tenir un service géant.
- **Problème profond** : la croyance que pour grandir, il faut grossir (plus d'utilisateurs = plus d'ingénieurs, plus de réunions, plus de couches). C'est le sous-texte de la fiche (« faire peu, mais très bien », reformulé en « résoudre seulement les problèmes qu'il fallait résoudre ») et de la phrase de Wired : « ils ne sont que quelques dizaines. Mais c'est justement le sujet. » La V1 ne le pose jamais : il apparaît en une phrase à la fin. **V2** : « Normalement, quand une appli double son nombre d'utilisateurs, l'équipe grossit avec. » est planté à 1:29, contredit tout de suite par 2014 → 2015, et récolté dans la question finale.
- **La chaîne « mais / donc »** de la V1, telle qu'elle est :
  1. 900 millions, 50 ingénieurs, **donc** 18 millions par ingénieur ;
  2. le chiffre tient, **et** il est encore plus bizarre un an avant, **donc** c'est la machine qui encaisse ;
  3. la machine, c'est Erlang, fait pour le téléphone, **et pourtant** on ne recrute pas pour Erlang ;
  4. un serveur tient 200 000 connexions, **mais** il bloque à 425 000, **donc** ils chassent la contention, **résultat** 2 millions ;
  5. **sauf qu'**en février, un serveur monte à 2,8 millions ;
  6. **et** deux ans plus tard, 550 serveurs, une dizaine de personnes sur Erlang, **donc** comment on bosse ?
  7. presque zéro réunion, **mais** Facebook, lui, a lâché Erlang.

  Le maillon faible est le 7 : « Mais Erlang, Facebook l'avait aussi utilisé » n'oppose rien à ce qui précède (les réunions). **V2** : « Sauf qu'Erlang, Facebook l'avait essayé aussi », puis la phrase de Wired qui relie l'île à WhatsApp (« WhatsApp, lui, n'avait pas d'infrastructure existante à raccorder »).

## Test des 15 premières secondes

> « En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs. Donc à peu près dix-huit millions de personnes par ingénieur. »

29 mots, 12 s à ton débit de 145 mots/min. Relu seul : c'est bien le moment le plus fort *pour le clic*, puisque c'est la promesse de la miniature, avec sa preuve (la date). Aucun contexte, aucune présentation. Les autres candidats (le pic de 2,8 millions, le moteur d'Erlang patché, « une dizaine de personnes sur Erlang ») sont plus forts pour un dev, mais ils demandent une explication ; le teaser de 2,8 M à 0:32 les annonce sans les gâcher. 🟢

Une option, pas appliquée : commencer par le chiffre et poser la date en fin de phrase (« Plus de neuf cents millions de personnes. Et derrière, environ cinquante ingénieurs. C'était WhatsApp, en deux mille quinze. »). Le choc arrive une seconde plus tôt ; la fiche demande la date « dès la première phrase », les deux versions la respectent. À toi de voir à l'oreille.

## Test des 30 secondes

| Tranche | Ce que dit la V1 | Verdict |
|---|---|---|
| 0-5 s | > « En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs. » | 🟢 Le sujet (WhatsApp) et la tension (900 M contre 50), raccord avec la miniature. |
| 5-15 s | > « Donc à peu près dix-huit millions de personnes par ingénieur. » | 🟢 Le chiffre le plus fou, avec sa liaison et à l'écran « 1 ingénieur = 18 000 000 » (ajouté en V2). |
| 15-30 s | > « Tes vocaux de quatre minutes, tes photos de bonne année : tout ça passait par les machines d'une équipe qui tient dans une salle de classe. / Alors comment cinquante personnes font tenir un truc pareil ? » | 🟢 L'enjeu devient personnel (tes vocaux), et il plante la récolte des 32 millions. La question centrale arrive au 57e mot (~24 s), une seule, en mots simples. « cinquante » sans « environ » : passé à « une cinquantaine ». |
| Pont | > « En fait, tout part d'un langage des années quatre-vingt, fait pour le téléphone. Et d'un serveur qui, en deux mille douze, a battu un record par accident. » | 🟢 Deux nouvelles questions (quel langage ? quel record ?) avant la réponse à la première. « Tout part » promet un peu trop (la section 5 parle des méthodes de l'équipe) : « la réponse commence avec… » en V2. |

**Budget :** 89 mots ≈ 37 s à 145 mots/min, 30 s à 180 (tes coupes serrées d'Uber). Un peu au-dessus des 75 à 90 mots de `strategie.md`, section 5 ; la V2 est à 91 mots, avec la question au 49e (~20 s).
**À couper :** rien de vide. Chaque phrase confirme, ouvre ou monte. « les machines d'une » saute (« tout ça passait par une équipe de la taille d'une classe »).
**Réécriture des 30 s :** pas nécessaire, seulement les deux retouches ci-dessus.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | Le chiffre de la miniature en 12 s, daté, et les trois étages qui livrent le « comment ». |
| 2. Alignement | 🟢 | Aucune vente ; l'appel à l'abonnement est court. L'angle business de Thibaut Dcode (prix du rachat, gratuité, vie privée) et le design d'Enrico Tartarotti sont absents. |
| 3. Problème profond | 🟠 | « Pour grandir, il faut grossir » n'est jamais posé : il arrive en une phrase à 11:55. |
| 4. Public & complexité | 🟢 | Erlang par le central téléphonique, la contention par le supermarché, BEAM après l'analogie du moteur : chaque mot technique arrive après son image. |
| 5. Valeur & originalité | 🟢 | Aucune vidéo française ne fait l'ingénierie de WhatsApp ; les diapos de Reed (425 000, 2,8 M, la contention) sont introuvables ailleurs en français. |
| 6. Structure & transformation | 🟢 | La carte « langage, serveur, équipe » ; on part d'un chiffre impossible, on arrive à une meilleure question. |
| 7. Histoire | 🟠 | Tout réussit : 425 000 est le seul obstacle, et il est franchi en deux phrases. Les plantages du noyau (diapo 13) sont la crise qui manquait. |
| 8. Mais / donc | 🟢 | Très bon dans les sections 3 et 4 ; un « Mais » qui n'oppose rien à 10:45. |
| 9. Engagement actif | 🟠 | On ne demande jamais rien au spectateur. « Pourquoi ? Les diapos ne le disent pas » ferme la seule vraie question ouverte. |
| 10. Rythme, oralité & liaisons | 🟢 | 2,1 liaisons pour 100 mots ; deux rafales de faits (sections 1 et 3), détaillées plus bas. |
| 11. Tics d'IA | 🟠 | Une dizaine d'occurrences légères, dont une phrase recopiée du skill (« Ouais, t'as bien entendu »). Aucune fausse opposition grave. |
| Faits (hors grille) | 🟠 | 6 inexactitudes : la cause du pic, l'île, « au pic », « vingt-quatre processeurs », « sur la même diapo », « recule d'un an », plus une action inventée (« je suis remonté aux sources »). |
| S1. Les 30 premières secondes | 🟢 | Les 6 questions passent ; budget un peu juste (37 s à 145 mots/min). |
| S2. Le pont | 🟢 | Le langage du téléphone et le record « par accident » ouvrent deux boucles. |
| S3. Les retournements | 🟢 | Un toutes les 30 s environ, sauf la section 1 (0:37-1:15) et la fin. |
| S4. Planté / récolté et motif | 🟢 | Les photos de bonne année, le teaser des 2,8 M, le serveur à 425 000, le livreur de RAMEN, la carte de la machine en motif. |
| S5. Personnages et enjeu | 🟠 | Rick Reed et Mahdavi citent, ils ne veulent rien. « L'équipe » et « la machine » font le reste. |
| S6. La fin | 🟠 | Le bon mécanisme (la meilleure question), mais pas semé, sans ton avis, et précédé d'une image fausse. |

## Le grill

### 1. La cause du pic de 2,8 millions est inventée

> « Rick Reed appelle ça une tentative de record involontaire : eux n'avaient rien prévu, la machine est montée toute seule avec le trafic. »

La diapo 16 (relue le 23/10) dit seulement : « Unintentional record attempt in Feb / Peaked at 2.8M conns before we intervened ». Elle ne dit pas ce qui l'a causé. Et la diapo 13 montre qu'ils *détournaient exprès* du trafic réel vers un serveur pour le tester (« Diverted workload : Add additional production load to server ») : le pic peut aussi bien venir d'un de ces tests. « Toute seule avec le trafic » est une interprétation présentée comme un fait, au moment le plus regardé de la vidéo (la relance à 58 %).

**Correction (appliquée) :**
> Sur sa diapo, Rick Reed appelle ça une tentative de record involontaire. Il ne raconte pas comment c'est arrivé, seulement qu'ils ont dû intervenir. Et une diapo plus loin, il en veut encore : ils courent toujours après les trois millions, et il écrit que la Saint-Patrick n'a pas porté autant chance qu'espéré.

La Saint-Patrick (diapo 17, « St. Patrick's Day wasn't as lucky as hoped ») remplace l'explication inventée par une vraie chute, sourcée et drôle. « Et personne ne lui avait demandé », à la fin de la section 3, reste : c'est le sens de « involontaire ».

### 2. L'île devenue continent contredit le script lui-même

> « Voilà comment je le vois. Chez le géant, Erlang était une île. Chez WhatsApp, c'était tout le continent. Quand toute ton équipe travaille sur la même île, tu n'as pas besoin de bateaux. »
> « Et du coup, une petite équipe peut tout comprendre, de l'appli jusqu'au moteur du langage. »

Deux minutes plus tôt, le script cite la diapo de 2014 : « petite, environ dix personnes sur Erlang ». Sur une trentaine d'ingénieurs, toute l'équipe n'était donc pas sur l'île. Le « Voilà comment je le vois » signale bien l'image, mais l'image affirme un fait faux. Et « tout comprendre, de l'appli jusqu'au moteur » n'est sourcé nulle part : rien ne dit que l'équipe Erlang touchait aux applis.

Ce que Wired dit vraiment, juste après la phrase de Parikh : « Of course, WhatsApp didn't have to integrate with an existing infrastructure in this way. » L'image tient avec ça, et elle est plus juste.

**Correction (appliquée) :**
> Et Wired le note juste après : WhatsApp, lui, n'avait pas d'infrastructure existante à raccorder. Donc pas de bateaux à construire. Voilà comment je le vois : chez Facebook, Erlang était une île à côté d'un continent. Chez WhatsApp, il n'y avait pas de continent, le service entier était construit sur l'île.

Bandeau « Illustration » à l'écran, comme pour les petites boîtes. La phrase « une petite équipe peut tout comprendre » est coupée ; ce qu'elle voulait dire est remplacé par un fait de la diapo de 2014 : la dizaine d'Erlang fait « development and ops », le code *et* l'exploitation.

### 3. La fin n'est pas préparée

> « Au début, je te demandais comment cinquante personnes font tenir un truc pareil. Sauf qu'après tout ça, je me pose une autre question : et si ça tenait justement parce qu'ils étaient cinquante ? »

Le mécanisme est le bon : c'est « la meilleure question » de `storytelling.md` (section 6), et elle évite la morale assénée. Mais telle quelle, elle tombe de nulle part :
- rien dans les sections 1 à 4 ne fait croire au spectateur que plus de monde, ce serait mieux : il n'a donc pas de croyance à retourner ;
- la seule preuve est l'île de Facebook, et elle arrive 70 s avant, avec l'erreur du point 2 ;
- elle reste sans ta réponse. Une question ouverte peut finir une vidéo, mais ici c'est ta chaîne de dev : le spectateur attend ton avis.

Et pourtant, la preuve existe, dans Wired : « Mahdavi says that the trick is as much about attitude as technology » et, sur les réunions, « Yes, there are only a few dozen of them. But that too is the point. » C'est presque mot pour mot ta question finale, dite par la source.

**Correction (appliquée) :**
- Section 1, avant 2014 : « Normalement, quand une appli double son nombre d'utilisateurs, l'équipe grossit avec. Sauf qu'en février deux mille quatorze… » (la croyance, puis le fait qui la casse).
- Section 1 : « Et Wired ajoute un détail : même après le rachat, cette petite équipe fait encore tourner le service presque entièrement seule. »
- Section 5 : « Pour lui, le secret, c'est autant l'attitude que la technique » ; « Wired le précise lui-même : oui, ils ne sont que quelques dizaines. Et c'est justement le sujet. »
- Fin : le récap passe à une phrase, la question « et aujourd'hui ? » reçoit sa réponse honnête (« Combien d'ingénieurs derrière ? Ça, Meta ne le publie pas. »), puis la question retournée reprend le mot planté : « Normalement, quand une appli grossit, l'équipe grossit avec. Et si chez WhatsApp, ça tenait justement parce qu'ils étaient si peu ? » ; ton verdict va dans le crochet qui suit.

« Cinquante » devient « si peu » : en 2014, au moment des diapos qu'on vient de montrer, ils étaient une trentaine, et une dizaine sur Erlang.

### 4. Personne ne veut rien : Rick Reed est un personnage caché

> « les diapos d'un de leurs ingénieurs, Rick Reed » ; « Rick Reed ne cache rien » ; « Rick Reed l'écrit noir sur blanc »

Reed revient sept fois, toujours comme une source. Or sa diapo de présentation de 2012 (relue le 23/10) dit : « Joined WhatsApp in 2011 / New to Erlang / Background in performance of C-based systems on FreeBSD and Linux / Prior work at Yahoo!, SGI ». Et celle de 2014 : « Learned Erlang at WhatsApp ». Le type qui pousse un serveur de 200 000 à plus de 2 millions de connexions était nouveau sur Erlang. C'est la preuve vivante du « on ne recrute pas pour Erlang » de Mahdavi, qui précède, et ça donne un héros à la section 3.

**Correction (appliquée)**, juste après la blague du nom de variable :
> Et le meilleur exemple, c'est Rick Reed, le type des diapos. Il arrive chez WhatsApp en deux mille onze, il vient du C, il a bossé chez Yahoo. Et sur la diapo où il se présente, en deux mille douze, il écrit lui-même : « nouveau sur Erlang ».
>
> Sauf que son boulot chez WhatsApp, c'est justement la montée en charge. Et c'est lui qui va raconter comment ils ont emmené un seul serveur au-delà de deux millions de connexions.

Ça devient aussi le pont vers la section 3, à la place de « on va regarder une seule machine ».

### 5. Il manque une crise

> « Mais vers quatre cent vingt-cinq mille, ça bloque. » … « Résultat : un premier lot de corrections, et ils passent le million. Un mois plus tard, deux millions. »

Le seul obstacle de la vidéo est franchi en deux phrases. La diapo 13 en contient un vrai : pour tester, ils envoient du trafic réel en plus sur un serveur, et « Ran into a few kernel panics at high conn counts ». Et la diapo 14 avoue que les premières corrections étaient faciles : « Fruit was hanging pretty low ».

**Correction (appliquée) :**
> Pour tester, ils envoient exprès du vrai trafic en plus sur une machine, pour la charger plus que les autres. Et à force de pousser, ils se prennent quelques plantages du noyau.
>
> Et vers quatre cent vingt-cinq mille connexions, ça bloque.

Puis « la réponse tient en un mot, répété trois fois : contention, contention, contention » (le titre exact de la diapo 20), et « Rick Reed l'avoue lui-même : les fruits étaient bas ».

### 6. Une action inventée et une réaction prêtée

> « Je suis dev, et un chiffre pareil, j'ai besoin de le vérifier avant d'y croire. Donc je suis remonté aux sources : un article de Wired de deux mille quinze, le blog de WhatsApp lui-même, et les diapos… »
> « Le patron de Facebook qui fait le paparazzi, j'avoue, je ne m'y attendais pas. »

La recherche a été faite pendant la préparation, pas par toi. C'est le même piège que le « j'ai résilié Netflix » d'ArtCraft, en plus petit : si un spectateur te demande en commentaire ce que tu as pensé des diapos de 2014, il faut que ce soit vrai. Même chose pour « je ne m'y attendais pas ».

**Correction (appliquée) :**
> Moi, je suis dev, et un chiffre pareil, je ne le prends pas sur parole. Donc on va le vérifier ensemble, avec les sources de l'époque : un article de Wired, le blog de WhatsApp lui-même, et les diapos d'un de leurs ingénieurs, Rick Reed.

La blague du paparazzi reste, sans réaction inventée : « Le patron de Facebook en mode paparazzi. » Si tu as lu les sources, dis-le, et on remet ta phrase (question 3).

### 7. Le spectateur ne participe jamais

> « Donc un million par serveur, alors qu'ils avaient montré qu'une machine pouvait en tenir plus de deux. Pourquoi ? Les diapos ne le disent pas, et je ne vais pas l'inventer. »

C'est la seule vraie énigme de la vidéo, et la V1 la ferme elle-même en un faux suspens (question, réponse immédiate). L'honnêteté est bonne ; il suffit de la tourner vers le spectateur.

**Correction (appliquée) :**
> Un million, alors qu'ils savaient en faire tenir plus de deux. À ton avis, pourquoi ? Les diapos ne le disent pas, donc je ne vais pas l'inventer. Mets ta théorie en commentaire.

Les devs vont répondre (marge pour les pannes, machines différentes, multimédia), et c'est du commentaire de qualité dans les deux premières heures.

### 8. Les tics d'IA

| Passage de la V1 | Problème | V2 |
|---|---|---|
| « Ouais, t'as bien entendu. » | La réaction d'exemple de `storytelling.md` (Cam), recopiée telle quelle. Le skill dit : reprendre le mécanisme, jamais la phrase. | « Deux cents millions de vocaux par jour. Et je suis sûr que dans le lot, il y en avait de quatre minutes. » (ta blague des vocaux, devenue la réaction) |
| « Tu vois le niveau ? Quand le langage les freinait… » | Question rhétorique suivie de la réponse. | « Tu vois le niveau : quand le langage les freinait… » |
| « Pourquoi ? Les diapos ne le disent pas » | Faux suspens. | Vraie question au spectateur (point 7). |
| « il y a une diapo géniale » | Intensif qui annonce au lieu de montrer. | « il y a une diapo avec ce titre » : le titre suffit. |
| « forcément, c'est de l'or » | Cliché. | « c'est le rêve » |
| « C'est exactement ça : » | Formule de conclusion. | « C'est ça, en vrai : » |
| « Chez le géant, Erlang était une île. Chez WhatsApp, c'était tout le continent. » | Parallélisme mécanique, et faux (point 2). | Réécrit sur la phrase de Wired. |
| « Bref, si je reprends : » + 4 éléments + « Voilà comment… » | Récap annoncé : signal de sortie à 11:20. | Récap en une phrase, sans annonce. |
| « Le patron de Facebook qui fait le paparazzi, j'avoue, je ne m'y attendais pas. » | Réaction prêtée (point 6). | « Le patron de Facebook en mode paparazzi. » |
| « Deux millions. Deux millions et demi. Deux millions huit cent mille connexions. » | Cascade de fragments. | **Gardée** : c'est la seule du script, et c'est une scène (le compteur qui monte). |
| « Dix. Dix personnes sur le code… » | Fragment dramatique. | Adouci : « Dix personnes. Celles qui écrivent le code… sont aussi celles qui surveillent les machines. » (avec le fait nouveau) |
| « Pas Linux, frère : FreeBSD. » | Forme « pas A : B ». | **Gardée** : la croyance est réelle (la plupart des serveurs tournent sous Linux) et c'est ton expression. |
| « Normalement, quand ton serveur sature, tu en ajoutes un deuxième. Eux, ils ont cherché pourquoi… » | Contraste. | **Gardé** : une pratique réelle, puis ce qu'ils ont fait ; ce n'est pas un homme de paille. |

Passe de vérification sur la V2 : aucun « ce n'est pas », « pas juste », « pas seulement » ; aucune question suivie d'une réponse en un mot ; « exactement » ramené de trois à une occurrence.

### 9. Les rafales de faits (axe 10)

Liaisons comptées par `controle.py` (liste du skill), sur la voix off seule :

| Section | Mots | Liaisons | Pour 100 mots |
|---|---|---|---|
| 0. Hook | 89 | 2 (donc, en fait) | 2,2 |
| 1. Le chiffre tient | 269 | 4 | 1,5 |
| 2. Le langage | 315 | 8 | 2,5 |
| 3. Deux millions | 409 | 11 | 2,7 |
| 4. Le serveur qui s'emballe | 338 | 6 | 1,8 |
| 5. Presque zéro réunion | 223 | 5 | 2,2 |
| 6. Fin | 218 | 3 | 1,4 |
| **Total V1** | **1 861** | **39** | **2,1** |

Le compte est bon. Deux rafales quand même :
- Section 1 : « Début deux mille quatorze, Rick Reed donne les chiffres : dix-neuf milliards de messages reçus chaque jour, et quarante milliards envoyés. Plus six cents millions de photos, deux cents millions de messages vocaux et cent millions de vidéos. Par jour. » Sept chiffres sans réaction, puis la réaction recopiée. **V2** : la question « Et elle encaisse quoi ? » avant, ta blague des vocaux après.
- Section 3 : « Le six janvier deux mille douze, WhatsApp publie un billet sur son blog. Le titre : « Un million, c'est tellement deux mille onze ». Dedans, ils collent les chiffres… » Trois phrases-fiches. **V2** : « avec un titre qui frime un peu », « Et dedans », puis la comparaison avec RAMEN (« Pour te donner l'échelle… »).

La fin (1,4) est sous la barre : c'est le récap. Il passe à une phrase en V2.

**V2 : 2 018 mots, 1,8 liaison pour 100 mots.** Le taux baisse un peu parce que la V2 ajoute sept faits, mais chacun arrive avec sa liaison ou sa réaction (« Sauf que son boulot… », « Pour te donner l'échelle… », « Et une diapo plus loin, il en veut encore… »).

### 10. Petites inexactitudes

- « Leur serveur avait vingt-quatre processeurs » : la diapo dit « 24 logical CPUs » (deux processeurs de six cœurs, chacun en double fil). **V2** : « vingt-quatre processeurs logiques », et à l'écran les caisses deviennent « vingt-quatre processeurs », pas « cœurs ».
- « Sur la même diapo, Rick Reed écrit que FreeBSD « brille aussi » » : « FreeBSD shines as well » est sur la diapo 18 (« General Findings »), la contention sur la diapo 20. **V2** : « D'ailleurs, Rick Reed écrit… »
- « cent quarante-sept millions de connexions ouvertes en même temps au pic » : la diapo 4 de 2014 dit « 147M concurrent connections » ; le mot « peak » n'y est que pour les connexions par seconde et les messages par seconde. **V2** : « au pic » supprimé.
- « Et ça devient encore plus bizarre quand tu recules d'un an » : de février 2014 à septembre 2015, il y a dix-neuf mois. **V2** : « d'un an et demi ».
- « Ce choix remonte loin. En deux mille neuf, Jan Koum pose déjà des questions sur la liste de diffusion d'ejabberd » : la phrase respecte la formulation de `sources.md` (fait 18 ⚠️), mais « ce choix remonte loin » lui fait dire que WhatsApp a choisi Erlang en 2009, ce que le billet ne dit pas. Et elle ne sert aucune relance. **V2** : coupée.

## Rétention

- **Relances** : 26 dans la V1, environ une toutes les 30 s ; la V2 en a 34. Un trou de 38 s dans la section 1 (les sources), un de 45 s entre l'île et le récap.
- **Ponts en fin de bloc** : tous présents. Le pont 2 (« on va regarder une seule machine ») devient Rick Reed « nouveau sur Erlang », plus fort parce qu'il donne quelqu'un à suivre.
- **Appel à l'abonnement** : à 3:13 (25 %), mais entre le central téléphonique et les petites boîtes, en plein milieu d'une explication. **V2** : à 3:38 (26 %), après les petites boîtes, avant le patch en pleine partie.
- **Relance forte vers 60 %** : la coupure musicale et le teaser payé, à 58 % dans la V1, 59 % dans la V2. 🟢 La V2 l'enchaîne avec la Saint-Patrick (une chute), puis le séisme et le foot.
- **Fiche et écran de fin** : vers Uber au rappel du livreur de RAMEN. La V2 ajoute à cet endroit la comparaison chiffrée avec RAMEN (1,5 M de connexions pour tout le système d'Uber en 2020, plus de 2 M sur un serveur de WhatsApp en 2012) : les spectateurs d'Uber ont déjà ce chiffre en tête.

## Les blagues à valider

| Blague | Avis |
|---|---|
| Zuckerberg en paparazzi | Garde-la : l'anecdote est sourcée (« Here's an action shot of you writing this update », Wired), la blague est légère. La réaction prêtée est retirée. |
| Le nom de variable | Garde-la : humour de dev, courte, juste après le fait. |
| « Pas Linux, frère » | Garde-la : c'est ton expression (« Linux frère »). |
| La barre de vie du boss | Garde-la : la traduction gamer de 41,9 %. « finir le boss » devient « battre le boss ». |
| Le CV | À toi de voir : c'est drôle, mais tu as un poste (tes applis Flutter sont des projets du boulot). Si ça te gêne, « rien que pour ça, je signe » marche aussi. |
| Nouvelles, sourcées : le titre « qui frime un peu », la Saint-Patrick | La Saint-Patrick vient de Reed lui-même (« wasn't as lucky as hoped ») : la blague est dans la source. |

## Ce qu'il faut garder

- **Le hook entier** : le meilleur des scripts génie à ce jour. Le chiffre de la miniature, daté, en 12 s ; tes vocaux de quatre minutes ; la question à 24 s ; un pont qui ouvre deux boucles.
- **« Imagine un patch installé en pleine partie, sans que personne soit renvoyé au menu. »** : l'idée la plus difficile de la vidéo (le code déployé à chaud), réglée en une image de joueur.
- **Le supermarché aux vingt-quatre caisses et une seule machine à carte** : la contention comprise par n'importe qui, avec le bon chiffre (24).
- **« Quand le langage les freinait, ils ont ouvert le moteur du langage, et ils l'ont patché. »** : la vraie révélation pour un dev.
- **« Ça, c'était le record officiel. Sauf qu'en février, un de leurs serveurs a fait mieux. Et personne ne lui avait demandé. »** : la relance à 58 %, parfaite.
- **« Les diapos ne le disent pas, et je ne vais pas l'inventer. »** : l'honnêteté sur ce qu'on ne sait pas, gardée et tournée vers le spectateur.
- **Les récoltes** : les photos de bonne année (32 millions), le serveur bloqué à 425 000 dans la section 5, le livreur de RAMEN.

## Vérification des faits

Chaque phrase de la voix off de la V1 qui porte un fait, contre `sources.md` et, quand le fait est absent ou douteux, contre la source primaire relue le 23/10 (diapos de Reed 2012 et 2014 extraites des PDF, Wired dans l'archive de 2016, blog d'Uber).

| Phrase de la V1 | Source | Statut | Dans la V2 |
|---|---|---|---|
| « En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs. » | Faits 1, 24 | ✅ daté, « environ » | Gardée |
| « à peu près dix-huit millions de personnes par ingénieur » | Fait 2 | ✅ | Gardée |
| « Alors comment cinquante personnes… » | Fait 1 | ⚠️ sans « environ » | « une cinquantaine de personnes » |
| « un serveur qui, en deux mille douze, a battu un record par accident » | Fait 8 (« Unintentional record attempt in Feb », conférence de mars 2012) | ✅ | « sans le faire exprès » |
| « je suis remonté aux sources » | Aucune | ❌ action inventée | « on va le vérifier ensemble » |
| Jan Koum annonce les 900 millions ; Zuckerberg répond avec la photo, « voilà une photo de toi en pleine action » | Fait 28, Wired relu | ✅ | Gardée |
| « Le même mois, Wired écrit que WhatsApp emploie environ cinquante ingénieurs » | Fait 1 | ✅ | Gardée |
| « Et ça devient encore plus bizarre quand tu recules d'un an. » | Faits 1, 3 (février 2014 → septembre 2015) | ⚠️ 19 mois | « d'un an et demi » |
| « En février deux mille quatorze, au moment où Facebook rachète WhatsApp, ils sont une trentaine d'ingénieurs pour plus de quatre cent cinquante millions d'utilisateurs » | Faits 3 ⚠️, 4 | ✅ formulation « une trentaine » | Gardée |
| « l'équipe a pris à peine quinze ou vingt personnes » | Calcul : 32-35 → ~50 | ✅ | Gardée |
| (ajout) « même après le rachat, cette petite équipe fait encore tourner le service presque entièrement seule » | Wired : « continues to run things almost entirely on its own » | ✅ ajouté, ligne 30 | Ajoutée |
| « dix-neuf milliards de messages reçus chaque jour, et quarante milliards envoyés » | Fait 13, diapo 4 de 2014 | ✅ | Gardée |
| « six cents millions de photos, deux cents millions de messages vocaux et cent millions de vidéos » | Fait 29, diapo 4 | ✅ | Gardée |
| « c'est un langage né chez Ericsson, dans les années quatre-vingt, pour des réseaux de téléphone à haut débit » | Fait 5 (« for use with high-speed phone networks ») | ✅ | Gardée |
| Cesarini : « le problème, c'était la scalabilité massive et la fiabilité » | Fait 5 | ✅ | Gardée |
| « on peut déployer du nouveau code pendant que le système tourne » | Fait 5 (« deploy new code on the fly ») | ✅ | Gardée |
| Les petites boîtes qui s'envoient des lettres | Notre image | ✅ signalée (bandeau) | Gardée |
| « En deux mille neuf, Jan Koum pose déjà des questions sur la liste de diffusion d'ejabberd » | Fait 18 ⚠️ | ⚠️ « ce choix remonte loin » déborde | Coupée |
| « WhatsApp ne recrute pas ses ingénieurs parce qu'ils connaissent le langage […] sa première semaine à apprendre le langage » ; « Jamshid Mahdavi, un de leurs ingénieurs » | Fait 16 ; Wired : « WhatsApp software engineer Jamshid Mahdavi » | ✅ | Gardée |
| (ajout) Rick Reed : arrivé en 2011, « nouveau sur Erlang », passé par le C et Yahoo ; montée en charge | Diapo 2 de 2012 et diapo 2 de 2014 | ✅ ajouté, ligne 31 | Ajoutée |
| « Il gardait une connexion ouverte avec ton téléphone » (RAMEN) | `projets/uber/script.md` | ✅ | Gardée |
| « Chez WhatsApp, les téléphones sont branchés de la même façon sur des serveurs de chat » | Faits 7, 14 (connexions TCP ouvertes, « ~1M phones each ») | ✅ comme principe | « c'est le même principe : chaque téléphone connecté, c'est une connexion ouverte » |
| « Au début, un serveur de WhatsApp en tient environ deux cent mille » ; « fragile face aux pannes et aux surcharges » ; « un million… ! » | Fait 8, diapos 5 et 6 | ✅ | Gardée |
| (ajout) le trafic détourné exprès, les plantages du noyau, « les fruits étaient bas », « à force d'attaquer les mêmes bouchons » | Diapos 13 à 15 | ✅ ajouté, ligne 32 | Ajoutée |
| « vers quatre cent vingt-cinq mille, ça bloque » | Fait 8, diapo 14 (« Initial bottlenecks appeared around 425k ») | ✅ | Gardée |
| « la réponse tient en un mot : contention » | Fait 9, diapo 20 (« Contention, contention, contention ») | ✅ | « répété trois fois » |
| « Leur serveur avait vingt-quatre processeurs » | Fait 10 (« 24 logical CPUs ») | ⚠️ | « processeurs logiques » |
| « un premier lot de corrections, et ils passent le million. Un mois plus tard, deux millions » | Fait 8, diapos 14-15 | ✅ | Gardée |
| « de deux cent mille à deux millions, tout était de la chasse à la contention » ; « la plupart… dans la machine virtuelle d'Erlang » | Fait 9, diapo 20 (« Most required BEAM patches ») | ✅ | Gardée |
| « Sur la même diapo, Rick Reed écrit que FreeBSD « brille aussi » » | Fait 9 : diapo 18, pas 20 | ⚠️ | « D'ailleurs, Rick Reed écrit… » |
| « Le six janvier deux mille douze… « Un million, c'est tellement deux mille onze »… deux millions deux cent soixante-dix-sept mille huit cent quarante-cinq connexions » | Fait 7 | ✅ | Gardée |
| (ajout) « RAMEN annonçait plus d'un million et demi de connexions pour tout son système, en deux mille vingt » | Blog d'Uber, 18/12/2020 (« this system with more than 1.5M concurrent connections ») | ✅ ajouté, ligne 36 | Ajoutée, dite comme une comparaison système / serveur |
| « quarante et un virgule neuf pour cent de processeur libre » | Fait 7 | ✅ | Gardée |
| « Février deux mille douze… deux millions huit cent mille connexions. Et là, les ingénieurs interviennent. » | Fait 8, diapo 16 | ✅ | Gardée |
| « eux n'avaient rien prévu, la machine est montée toute seule avec le trafic » | Diapo 16 : aucune cause | ❌ | Remplacée (point 1) |
| (ajout) les trois millions, la Saint-Patrick ; les « événements du monde » rangés avec les pannes | Diapos 6 et 17 | ✅ ajouté, ligne 33 | Ajoutée |
| « La croissance, les séismes et le foot ! » ; séisme au Mexique, buts, mi-temps, fin du match | Fait 11, diapo 4 de 2012 | ✅ sans chiffre | « il y a une diapo avec ce titre » |
| « quatre cent soixante-cinq millions d'utilisateurs par mois […] cent quarante-sept millions de connexions ouvertes en même temps au pic » | Fait 13, diapo 4 de 2014 | ⚠️ « au pic » absent | « au pic » supprimé |
| « environ cinq cent cinquante serveurs, et plus de onze mille cœurs » | Fait 13, diapo 10 | ✅ | Gardée |
| « une seule photo a été téléchargée trente-deux millions de fois » | Fait 29, diapo 5 | ✅ | Gardée |
| « Sur environ cent cinquante serveurs de chat, chacun tient à peu près un million de téléphones » | Fait 14 ⚠️, diapo 10 | ✅ formulation juste, sans interprétation | Gardée, puis question au spectateur |
| « petite, environ dix personnes sur Erlang » | Fait 13, diapo 2 de 2014 | ✅ | Gardée |
| (ajout) « ces dix-là s'occupent à la fois du développement et de l'exploitation » | Diapo 2 de 2014 (« Handle development and ops ») | ✅ ajouté, ligne 34 | Ajoutée |
| Mahdavi, « en deux mille quinze, à San José » ; la leçon numéro un ; les réunions | Fait 15, Wired relu | ✅ | Gardée |
| « les employés n'assistent presque jamais à une réunion » | Fait 15 (« almost never attend a meeting ») | ✅ | Gardée |
| (ajout) « autant l'attitude que la technique » ; « ils ne sont que quelques dizaines. Et c'est justement le sujet » ; « WhatsApp n'avait pas d'infrastructure existante à raccorder » | Wired relu | ✅ ajouté, ligne 35 | Ajoutée |
| « une approche minimaliste : résoudre seulement les problèmes qu'il fallait résoudre » | Ligne 26 ; Wired : la phrase est bien de Mahdavi | ✅ | Gardée |
| « Son chat était écrit en Erlang, puis ils l'ont réécrit » ; Parikh, la petite île, les bateaux | Fait 17 (« rebuilt so that it would better fit with the rest of its infrastructure ») | ✅ | « pour qu'il colle au reste de leur infrastructure » |
| « Chez WhatsApp, c'était tout le continent. Quand toute ton équipe travaille sur la même île… » | Contredit le fait 13 (~10 sur Erlang) | ❌ | Remplacée (point 2) |
| « une petite équipe peut tout comprendre, de l'appli jusqu'au moteur du langage » | Aucune | ❌ | Coupée |
| « d'après Meta, en deux mille vingt-cinq, WhatsApp dépasse les trois milliards d'utilisateurs par mois » | Fait 20 ⚠️ (annonce de Zuckerberg aux résultats du 1er trimestre 2025, rapportée par la presse) | ✅ formulation juste | Gardée |
| (ajout) « Combien d'ingénieurs derrière ? Ça, Meta ne le publie pas. » | Fait 23 (aucun effectif récent trouvé) | ✅ | Ajoutée |
| « En deux mille quatorze, un serveur comme lui tenait environ un million de téléphones » | Fait 14 | ✅ | Gardée |

**Bilan** : 3 phrases retirées ou remplacées parce que fausses ou non sourcées (la cause du pic, l'île devenue continent, « tout comprendre de l'appli au moteur »), 1 action inventée retirée, 5 phrases recalées (« une cinquantaine », « d'un an et demi », « processeurs logiques », « sur la même diapo », « au pic »), 1 phrase coupée (ejabberd). 7 lignes ajoutées à `sources.md` (30 à 36), toutes lues à la source primaire le 23/10. Les « interdits » de `sources.md` sont respectés : ni « 40 millions par ingénieur », ni 64 ou 100 milliards, ni « construit sur ejabberd », ni citation d'Acton, ni « faire peu, mais très bien » entre guillemets, ni 8 000 et 11 000 cœurs mélangés, ni prix du rachat.

## Plan d'action (appliqué dans `script.md`)

1. Recaler les faits : la cause du pic, l'île, « au pic », « processeurs logiques », « sur la même diapo », « d'un an et demi » (points 1, 2 et 10).
2. Retirer l'action inventée et la réaction prêtée (point 6).
3. Faire de Rick Reed le personnage de la section 3, et ajouter la crise des plantages du noyau (points 4 et 5).
4. Planter « l'équipe grossit avec l'appli » dans la section 1 et le récolter dans la fin, avec les phrases de Mahdavi et de Wired (point 3).
5. Tourner la question des un million vers le spectateur, déplacer l'abonnement, retirer les tics (points 7 et 8).

Reste à toi : ton verdict sur la question finale, tes groupes WhatsApp, et le tri des blagues (voir « Questions pour l'auteur » dans `script.md`).
