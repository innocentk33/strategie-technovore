# WhatsApp : script v2

**Titre** : *Comment une cinquantaine d'ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes* (titre 4 de la fiche avec la miniature `noir-06` : *Le génie caché de WhatsApp : une équipe minuscule*)

**Durée** : environ 2 020 mots de voix off (`controle.py`). À 145 mots/min (ton débit mesuré sur ArtCraft, pauses et improvisations comprises) : environ 13 min 55 ; à 165 mots/min : 12 min 15 ; en coupes serrées comme sur Uber (~180 mots/min) : 11 min 15, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : un seul serveur. Le hook pose le chiffre impossible (en 2015, environ 50 ingénieurs pour plus de 900 millions de personnes) ; la vidéo descend dans la machine : le langage (Erlang), un ingénieur « nouveau sur Erlang » qui pousse un serveur de 200 000 à plus de 2 millions de connexions, le jour où ce serveur s'emballe, puis la façon de travailler de l'équipe. La fin remplace la question du début par une meilleure : et si ça tenait justement parce qu'ils étaient si peu ?

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **Faits recalés sur les diapositives de Rick Reed (relues le 23/10)** : le pic de 2,8 millions n'est plus « monté tout seul avec le trafic » (la diapo ne dit pas pourquoi) ; « cent quarante-sept millions de connexions » perd son « au pic » (absent de la diapo) ; « vingt-quatre processeurs » devient « vingt-quatre processeurs logiques ».
- **L'île devenue continent est corrigée** : la V1 disait que toute l'équipe travaillait « sur la même île », alors que la diapo de 2014 ne met qu'une dizaine de personnes sur Erlang. L'image s'appuie maintenant sur la phrase de Wired : WhatsApp n'avait pas d'infrastructure existante à raccorder.
- **Plus d'action inventée** : « je suis remonté aux sources » (c'est la recherche qui l'a fait, pas toi) devient une promesse, « on va le vérifier ensemble ». Ta réaction de paparazzi (« j'avoue, je ne m'y attendais pas ») est retirée ; la blague reste.
- **« Ouais, t'as bien entendu » retiré** : c'est l'exemple de Cam recopié depuis le skill.
- **Sept faits nouveaux, tous relus à la source** (lignes 30 à 36 de `sources.md`) : Rick Reed « nouveau sur Erlang » en arrivant ; le trafic détourné exprès et les plantages du noyau ; « les fruits étaient bas » ; les trois millions qu'il poursuit encore ; la dizaine d'Erlang qui fait aussi l'exploitation ; « ils ne sont que quelques dizaines, et c'est justement le sujet » (Wired) ; le million et demi de connexions de RAMEN chez Uber.
- **La fin est préparée** : « normalement, l'équipe grossit avec l'appli » est planté dans la section 1 et récolté dans la question finale ; la phrase de Mahdavi (« autant l'attitude que la technique ») et celle de Wired (« c'est justement le sujet ») la soutiennent. Le récap est raccourci, et la question « combien d'ingénieurs aujourd'hui ? » reçoit une réponse honnête : Meta ne le publie pas.
- **Engagement** : « Pourquoi ? Les diapos ne le disent pas » devient une vraie question au spectateur, avec commentaire.
- **Appel à l'abonnement** déplacé après les petites boîtes (3:38, 26 %), entre deux idées sur Erlang, au lieu de couper en deux l'explication du central téléphonique.
- **Coupé** : la question de Jan Koum sur la liste d'ejabberd en 2009 (un fait ⚠️ qui ne servait aucune relance) ; « une petite équipe peut tout comprendre, de l'appli jusqu'au moteur » (non sourcé).

**Boucles ouvertes** :
1. « Comment une cinquantaine de personnes font tenir un truc pareil ? » (hook, 0:20) : refermée par étapes, sections 2 à 5, puis remplacée par une meilleure question à la fin.
2. « Un serveur qui, en 2012, a battu un record sans le faire exprès » (hook, 0:30) : relancée à la fin de la section 3, refermée dans la section 4 (2,8 millions).
3. « Tes photos de bonne année » (hook) : récoltée dans la section 4 (la photo téléchargée 32 millions de fois le soir du Nouvel An).
4. « Normalement, quand une appli double, l'équipe grossit avec » (section 1) : récoltée dans la question finale.
5. « Une semaine pour apprendre Erlang » (section 2) : récoltée tout de suite par Rick Reed, « nouveau sur Erlang », qui porte la section 3.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (charte noire du pilier génie, cartes sombres d'Uber) ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de [`sources.md`](sources.md) (colonne « 2e vérif », et lignes ajoutées au grill), et des ⚠️ avec la formulation qu'il donne.

---

## 0. Hook (0:00 – 0:38) · objectif : 75 % à 0:15

[VISUEL : écran noir. Une bulle de message verte apparaît, puis des centaines, puis un mur de bulles qui remplit l'écran. Compteur « 900 000 000 ». Pas de titre, pas de logo.]

En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs. Donc à peu près dix-huit millions de personnes par ingénieur.

[VISUEL : le mur de bulles se resserre d'un coup ; en dessous, une petite salle avec cinquante silhouettes. Texte : « 2015 · ~50 ingénieurs ». Puis « 1 ingénieur = 18 000 000 ».]
[SON : un « tic » sec quand la salle apparaît.]

Tes vocaux de quatre minutes, tes photos de bonne année : tout ça passait par une équipe de la taille d'une classe.

Alors comment une cinquantaine de personnes font tenir un truc pareil ?

En fait, la réponse commence avec un langage des années quatre-vingt fait pour le téléphone, et un serveur qui, en deux mille douze, a battu un record sans le faire exprès.

[VISUEL : teaser d'une seconde : un compteur de connexions qui s'emballe, « 2 800 000 », alarme rouge. Arrêt sur image.]

---

## 1. Le chiffre tient (0:38 – 2:38)

Moi, je suis dev, et un chiffre pareil, je ne le prends pas sur parole. Donc on va le vérifier ensemble, avec les sources de l'époque : un article de Wired, le blog de WhatsApp lui-même, et les diapos d'un de leurs ingénieurs, Rick Reed.

[VISUEL : défilement rapide de l'article de Wired, du billet de blog de 2012 et des diapositives de Rick Reed ; seules les dates restent nettes. Texte : « Toutes les sources en description ».]

[TES GROUPES WHATSAPP : LE GROUPE DE LA FAMILLE, CELUI DU QUARTIER OU DE LA PROMO, COMBIEN DE MESSAGES PAR JOUR. DEUX PHRASES MAXIMUM, OU ON COUPE.]

Et le chiffre tient. En septembre deux mille quinze, Jan Koum, le cofondateur, annonce sur Facebook que WhatsApp dépasse les neuf cents millions. Et sous son post, Mark Zuckerberg répond avec une photo de Jan… en train de taper ce message. « Voilà une photo de toi en pleine action. » Le patron de Facebook en mode paparazzi.

[VISUEL : reconstitution en motion design (pas de vraie capture de Facebook) : un post « 900 millions », une réponse avec une photo floutée et l'appareil photo qui flashe.]

Le même mois, Wired écrit que WhatsApp emploie environ cinquante ingénieurs. Et ça devient encore plus bizarre quand tu recules d'un an et demi.

Normalement, quand une appli double son nombre d'utilisateurs, l'équipe grossit avec. Sauf qu'en février deux mille quatorze, au moment où Facebook rachète WhatsApp, ils sont une trentaine d'ingénieurs pour plus de quatre cent cinquante millions d'utilisateurs. Du coup, entre les deux, les utilisateurs doublent, et l'équipe prend à peine quinze ou vingt personnes.

[VISUEL : chronologie : « 2014 · ~30 ingénieurs · 450 M », puis « 2015 · ~50 ingénieurs · 900 M ». La barre des utilisateurs double, celle des ingénieurs bouge à peine.]

Et Wired ajoute un détail : même après le rachat, cette petite équipe fait encore tourner le service presque entièrement seule.

Donc s'ils tiennent, c'est que la machine encaisse à leur place. Et elle encaisse quoi ? Début deux mille quatorze, d'après les diapos de Rick Reed : dix-neuf milliards de messages reçus chaque jour, et quarante milliards envoyés. En plus, six cents millions de photos, deux cents millions de vocaux et cent millions de vidéos. Par jour.

[VISUEL : quatre compteurs qui tournent côte à côte : messages, photos, vocaux, vidéos. Texte : « début 2014, par jour ».]

Deux cents millions de vocaux par jour. Et je suis sûr que dans le lot, il y en avait de quatre minutes.

Bref, pour comprendre comment si peu de monde tient tout ça, on revient au langage du début.

---

## 2. Un langage fait pour le téléphone (2:38 – 5:00)

[VISUEL : la « carte de la machine », trois étages : le langage, le serveur, l'équipe. « Le langage » s'allume. Elle revient au début de chaque chapitre.]
[SON : ding de chapitre.]

Côté serveur, WhatsApp est écrit en Erlang. Si tu n'en as jamais entendu parler, c'est normal : c'est un langage né chez Ericsson, dans les années quatre-vingt, pour des réseaux de téléphone à haut débit.

Et en fait, le problème d'un réseau de téléphone, c'est déjà celui de WhatsApp : des millions de gens qui se parlent en même temps, et un réseau qui n'a pas le droit de tomber. Francesco Cesarini, un spécialiste d'Erlang, le dit dans Wired : le problème, c'était la scalabilité massive et la fiabilité.

[VISUEL : un vieux central téléphonique des années 80 en motion design, ses câbles qui deviennent des bulles vertes.]

Pour faire simple, imagine des milliers de petites boîtes. Chaque boîte s'occupe d'une seule chose, et les boîtes s'envoient des lettres pour se parler. Tu vois l'idée : plein de petites conversations en parallèle, exactement ce que fait une messagerie.

[VISUEL : des milliers de petites boîtes qui s'envoient des enveloppes. Bandeau : « Illustration ».]

**Abonnement (≈ 3:35, 26 % de la vidéo, entre deux idées sur Erlang)**

Si tu aimes voir ce qu'il y a sous le capot des applis que tu as dans la poche, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, les petites boîtes continuent derrière.]

Et surtout, Erlang a un pouvoir que les joueurs vont comprendre tout de suite : on peut déployer du nouveau code pendant que le système tourne. Imagine un patch installé en pleine partie, sans que personne soit renvoyé au menu. Pour une messagerie qui ne doit jamais s'arrêter, c'est le rêve.

[VISUEL : une partie en ligne, une barre « Mise à jour 100 % » passe en haut de l'écran, les joueurs continuent de jouer.]
[SON : petit « ding » de mise à jour, la musique ne s'arrête pas.]

Bon, là, tu te dis sûrement qu'ils ont recruté des experts d'Erlang. Et pourtant, d'après Jamshid Mahdavi, un ingénieur de WhatsApp, ils ne recrutent pas les gens parce qu'ils connaissent le langage. Un nouveau passe sa première semaine à l'apprendre.

Une semaine pour un langage entier. Il y a des devs qui mettent plus longtemps à choisir le nom d'une variable.

Et le meilleur exemple, c'est Rick Reed, le type des diapos. Il arrive chez WhatsApp en deux mille onze, il vient du C, il a bossé chez Yahoo. Et sur la diapo où il se présente, en deux mille douze, il écrit lui-même : « nouveau sur Erlang ».

[VISUEL : la diapo « About » reconstituée : « Joined WhatsApp in 2011 · New to Erlang » ; « New to Erlang » se surligne en vert.]

Sauf que son boulot chez WhatsApp, c'est justement la montée en charge. Et c'est lui qui va raconter comment ils ont emmené un seul serveur au-delà de deux millions de connexions.

---

## 3. Deux millions de connexions sur une machine (5:00 – 8:12)

[VISUEL : carte de la machine, « Le serveur » s'allume.]

Tu te rappelles le livreur de RAMEN, dans la vidéo sur Uber ? Il gardait une connexion ouverte avec ton téléphone pour te livrer les messages. Chez WhatsApp, c'est le même principe : chaque téléphone connecté, c'est une connexion ouverte que le serveur doit tenir.

[VISUEL : le livreur à vélo de la vidéo Uber traverse l'écran ; derrière lui, un serveur auquel se branchent des milliers de petits téléphones.]

Au début, un serveur de WhatsApp en tient environ deux cent mille. Et Rick Reed ne cache rien : sur ses diapos, il écrit que leur cluster est fragile face aux pannes et aux surcharges. Du coup, ils se fixent un objectif : un million de connexions par serveur. Sur la diapo, il y a même un point d'exclamation.

[VISUEL : la diapo reconstituée, « 1 million de connexions par serveur … ! », le point d'exclamation qui grossit.]

Pour tester, ils envoient exprès du vrai trafic en plus sur une machine, pour la charger plus que les autres. Et à force de pousser, ils se prennent quelques plantages du noyau.

[VISUEL : des flèches de trafic détournées vers un seul serveur ; écran de « kernel panic » en texte blanc sur noir, deux fois.]
[SON : un « bzzt » de court-circuit à chaque plantage.]

Et vers quatre cent vingt-cinq mille connexions, ça bloque.

[VISUEL : un compteur qui monte de « 200 000 » à « 425 000 », puis se fige ; la barre passe au rouge.]
[SON : un bruit de frein.]

Normalement, quand ton serveur sature, tu en ajoutes un deuxième. Eux, ils ont cherché pourquoi celui-là bloquait. Et sur la diapo de Rick Reed, la réponse tient en un mot, répété trois fois : contention, contention, contention.

En gros, imagine un supermarché avec vingt-quatre caisses ouvertes, mais une seule machine à carte bleue. Les caissiers sont prêts, et ils passent leur temps à attendre leur tour. Leur serveur avait vingt-quatre processeurs logiques, et à l'intérieur, des petits embouteillages de ce genre les faisaient attendre.

[VISUEL : vingt-quatre caisses, une seule machine à carte qui passe de main en main ; une file se forme à chaque caisse. Puis les caisses deviennent vingt-quatre processeurs.]

Résultat : un premier lot de corrections, et ils passent le million. Rick Reed l'avoue lui-même : les fruits étaient bas. Un mois plus tard, à force d'attaquer les mêmes bouchons, deux millions.

Et la plupart de ces corrections, il a fallu les faire dans la machine virtuelle d'Erlang elle-même. Tu vois le niveau : quand le langage les freinait, ils ont ouvert le moteur du langage, et ils l'ont patché.

[VISUEL : le capot d'une voiture s'ouvre ; dessous, écrit « BEAM » (la machine virtuelle d'Erlang) ; une clé à molette entre dans le moteur.]

Et le système en dessous, c'est FreeBSD. Pas Linux, frère : FreeBSD. D'ailleurs, Rick Reed écrit que FreeBSD « brille aussi ».

[VISUEL : le logo de FreeBSD qui brille, le pingouin de Linux qui sort du cadre en boudant.]

Le six janvier deux mille douze, WhatsApp publie un billet sur son blog, avec un titre qui frime un peu : « Un million, c'est tellement deux mille onze ». Et dedans, ils collent les chiffres d'un de leurs serveurs : deux millions deux cent soixante-dix-sept mille huit cent quarante-cinq connexions ouvertes. Sur une seule machine.

[VISUEL : le compteur « 2 277 845 » qui se fige, la date « 06/01/2012 » en petit. Sous le compteur : « 24 processeurs logiques · ~100 Go de RAM ».]

Pour te donner l'échelle : dans la vidéo Uber, RAMEN annonçait plus d'un million et demi de connexions pour tout son système, en deux mille vingt. WhatsApp en tenait plus de deux millions sur un seul serveur, huit ans plus tôt.

[VISUEL : deux jauges côte à côte : « Uber, tout le système, 2020 : 1,5 M+ » et « WhatsApp, 1 serveur, 2012 : 2,28 M ».]

Et sur cette machine, il reste quarante et un virgule neuf pour cent de processeur libre. Donc elle n'est même pas à bout. Pour un joueur, c'est battre le boss avec encore presque la moitié de ta barre de vie.

[VISUEL : une barre de vie de boss de jeu vidéo, remplie à 41,9 %, qui clignote en vert.]

Ça, c'était le record officiel. Sauf qu'en février, un de leurs serveurs a fait mieux. Et personne ne lui avait demandé.

---

## 4. Le serveur qui s'est emballé (8:12 – 11:00) · relance forte à 59 %

[SON : la musique coupe net, une seconde de silence, puis une basse qui tient.]
[VISUEL : un serveur seul dans le noir, son compteur allumé.]

Février deux mille douze. Sur un des serveurs de WhatsApp, le compteur monte. Deux millions. Deux millions et demi. Deux millions huit cent mille connexions. Et là, les ingénieurs interviennent.

[VISUEL : le teaser du hook, enfin en entier : le compteur s'emballe jusqu'à « 2 800 000 », l'alarme rouge, une main qui tire le frein.]
[SON : alarme, puis coupure.]

Sur sa diapo, Rick Reed appelle ça une tentative de record involontaire. Il ne raconte pas comment c'est arrivé, seulement qu'ils ont dû intervenir. Et une diapo plus loin, il en veut encore : ils courent toujours après les trois millions, et il écrit que la Saint-Patrick n'a pas porté autant chance qu'espéré.

[VISUEL : un trèfle à quatre feuilles posé sur le compteur bloqué sous « 3 000 000 » ; une feuille tombe.]

Des vagues de trafic, il en montre d'autres. Dans la même conférence, il y a une diapo avec ce titre : « La croissance, les séismes et le foot ! ». Dessus, une courbe de messages avec des pics annotés : un séisme au Mexique, et les buts d'un match de foot, avec la mi-temps et la fin du match.

[VISUEL : la courbe reconstituée ; un pic marqué « séisme au Mexique », puis une série de petits pics marqués « but », « mi-temps », « fin du match ».]

Imagine. Un but est marqué, et des millions de gens dégainent leur téléphone au même moment. Un séisme, et tout le monde écrit à sa famille pour savoir si ça va. Pour un serveur, c'est une vague qui arrive d'un coup. Et dans sa liste d'objectifs, Rick Reed range les événements du monde, le sport et les séismes, juste à côté des pannes de matériel.

[UN MOMENT OÙ TES GROUPES WHATSAPP ONT EXPLOSÉ EN MÊME TEMPS : UN MATCH DE LA CAN, UN RÉSULTAT D'EXAMEN, UNE COUPURE DE COURANT. UNE PHRASE, OU ON COUPE.]

Et deux ans plus tard, la vague est devenue un océan. Début deux mille quatorze, d'après les diapos de Rick Reed : quatre cent soixante-cinq millions d'utilisateurs par mois, et cent quarante-sept millions de connexions ouvertes en même temps. Pour tenir ça, environ cinq cent cinquante serveurs, et plus de onze mille cœurs de processeur.

[VISUEL : le serveur seul se multiplie en une salle entière ; compteurs « 465 M », « 147 M connexions », « ~550 serveurs », « > 11 000 cœurs ». Texte : « début 2014 ».]

Tu te rappelles les photos de bonne année du début ? Le soir du Nouvel An, une seule photo a été téléchargée trente-deux millions de fois. Imagine par combien de groupes elle est passée.

[VISUEL : une seule image de feu d'artifice qui se duplique en cascade de groupe en groupe ; compteur « 32 000 000 ».]

Et chacun des quelque cent cinquante serveurs de chat tient à peu près un million de téléphones. Un million, alors qu'ils savaient en faire tenir plus de deux. À ton avis, pourquoi ? Les diapos ne le disent pas, donc je ne vais pas l'inventer. Mets ta théorie en commentaire.

[VISUEL : « ~1 M par serveur » à côté du « 2 277 845 » de 2012 ; un point d'interrogation entre les deux.]

Et sur la diapo où Rick Reed parle de l'équipe, il écrit : petite, environ dix personnes sur Erlang. Et ces dix-là s'occupent à la fois du développement et de l'exploitation.

[VISUEL : « ~10 » en plein écran, puis dix silhouettes devant la salle des cinq cent cinquante serveurs ; elles tapent du code, puis l'une d'elles se retourne vers un écran d'alerte.]

Dix personnes. Celles qui écrivent le code qui reçoit dix-neuf milliards de messages par jour sont aussi celles qui surveillent les machines.

Alors forcément, la question, c'est comment on bosse quand on est si peu sur un truc pareil.

---

## 5. Presque zéro réunion (11:00 – 12:46)

[VISUEL : carte de la machine, « L'équipe » s'allume.]

Jamshid Mahdavi, l'ingénieur de la semaine d'Erlang, l'a expliqué en deux mille quinze, sur une scène à San José. Pour lui, le secret, c'est autant l'attitude que la technique. Et sa leçon numéro un, c'est de rester très concentré sur ce que tu dois faire. De ne pas te laisser distraire par d'autres activités, d'autres technologies, et même par des trucs de bureau comme les réunions.

Et en effet, d'après Wired, chez WhatsApp, les employés n'assistent presque jamais à une réunion. Wired le précise lui-même : oui, ils ne sont que quelques dizaines. Et c'est justement le sujet.

[VISUEL : un agenda de la semaine, entièrement vide ; une seule case « réunion » qui s'efface.]
[SON : un « pop » quand la case disparaît.]

Franchement, rien que pour ça, j'ai envie d'envoyer mon CV.

Mahdavi parle aussi d'une approche minimaliste : résoudre seulement les problèmes qu'il fallait résoudre. Tu te rappelles le serveur bloqué à quatre cent vingt-cinq mille ? C'est ça, en vrai : ils ont cherché les embouteillages, un par un, et ils ont corrigé ceux-là.

[VISUEL : retour sur les vingt-quatre caisses ; les files se vident une par une.]

Sauf qu'Erlang, Facebook l'avait essayé aussi. Son premier chat était écrit en Erlang, et ils ont fini par le réécrire pour qu'il colle au reste de leur infrastructure. Jay Parikh, vice-président de l'ingénierie chez Facebook, le raconte dans Wired : c'était une petite île d'Erlang, et c'était dur de construire assez de bateaux pour la relier au reste.

[VISUEL : une petite île marquée « Erlang » au milieu d'un océan marqué « Facebook » ; des petits bateaux qui font des allers-retours et n'arrivent pas à suivre.]

Et Wired le note juste après : WhatsApp, lui, n'avait pas d'infrastructure existante à raccorder. Donc pas de bateaux à construire. Voilà comment je le vois : chez Facebook, Erlang était une île à côté d'un continent. Chez WhatsApp, il n'y avait pas de continent, le service entier était construit sur l'île.

[VISUEL : l'océan « Facebook » disparaît ; l'île reste seule, avec une ville entière dessus. Bandeau : « Illustration ».]

---

## 6. Fin (12:46 – 13:56)

[SON : la musique du début revient.]
[VISUEL : la carte de la machine en entier, les trois étages allumés, une bulle verte qui la traverse de haut en bas en accéléré.]

Bref : un langage pensé pour le téléphone, des ingénieurs qui l'apprennent en une semaine, une équipe qui patche jusqu'au moteur d'Erlang, et presque pas de réunions. Voilà comment une cinquantaine d'ingénieurs faisaient tourner WhatsApp pour neuf cents millions de personnes, en deux mille quinze.

Et aujourd'hui ? D'après Meta, en deux mille vingt-cinq, WhatsApp dépasse les trois milliards d'utilisateurs par mois. Combien d'ingénieurs derrière ? Ça, Meta ne le publie pas.

[VISUEL : le compteur « 900 000 000 » du hook grimpe jusqu'à « 3 000 000 000+ ». Texte : « d'après Meta, 2025 ». En dessous, la salle des silhouettes devient un « ? ».]

Au début, je te demandais comment une cinquantaine de personnes font tenir un truc pareil. Sauf qu'après tout ça, je me pose une autre question. Normalement, quand une appli grossit, l'équipe grossit avec. Et si chez WhatsApp, ça tenait justement parce qu'ils étaient si peu ?

[VISUEL : la petite salle de cinquante silhouettes du hook, cette fois avec la salle des serveurs derrière elle.]

[TON VERDICT, UNE OU DEUX PHRASES : TU Y CROIS, OU C'EST SURTOUT ERLANG QUI FAIT LE TRAVAIL ? CE QUI T'A LE PLUS SURPRIS, TOI, EN TANT QUE DEV. SANS INVENTER DE VÉCU.]

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et si tu veux revoir le livreur de RAMEN, celui qui garde la connexion ouverte avec ton téléphone, c'est dans la vidéo sur Uber, juste là.

[VISUEL : écran de fin, 20 s : vidéo Uber à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Chiffre | 900 millions, environ 50 ingénieurs, en 2015 : le mur de bulles et la petite salle |
| 0:20 | Question centrale | « Alors comment une cinquantaine de personnes font tenir un truc pareil ? » |
| 0:32 | Teaser | Le compteur qui s'emballe à 2,8 M, arrêt sur image (refermé à 8:12) |
| 1:07 | Anecdote | Zuckerberg en paparazzi sous le post de Jan Koum |
| 1:29 | Contraste | « Normalement, l'équipe grossit avec » ; 2014 → 2015 : les utilisateurs doublent, l'équipe bouge à peine |
| 2:10 | Chiffres + réaction | 19 + 40 milliards de messages, les vocaux de quatre minutes |
| 2:38 | Chapitre | Carte de la machine, « Le langage » |
| 2:55 | Retournement | Le problème du téléphone, c'est déjà celui de WhatsApp |
| 3:38 | Appel à l'action | Abonnement (26 %) |
| 3:50 | Humour gamer | Le patch installé en pleine partie |
| 4:15 | Surprise | Une semaine pour apprendre Erlang ; la blague du nom de variable |
| 4:31 | Retournement | Rick Reed, « nouveau sur Erlang », sera celui des deux millions |
| 5:03 | Rappel | Le livreur de RAMEN de la vidéo Uber (fiche vers Uber) |
| 5:30 | Détail | L'objectif d'un million par serveur, avec son point d'exclamation |
| 5:54 | Crise | Le trafic détourné exprès, les plantages du noyau |
| 6:00 | Blocage | Le compteur se fige à 425 000, bruit de frein |
| 6:12 | Analogie | « Contention, contention, contention » ; vingt-quatre caisses, une seule machine à carte |
| 7:01 | Révélation | Ils ont patché le moteur du langage |
| 7:05 | Humour | « Pas Linux, frère : FreeBSD », le pingouin qui boude |
| 7:20 | Chiffre + rappel | 2 277 845 connexions ; plus qu'Uber sur tout son système, huit ans plus tôt |
| 7:50 | Jeu vidéo | 41,9 % libre, la barre de vie du boss |
| 8:12 | Coupure musique | Février 2012 : le serveur qui s'emballe (59 %) |
| 8:43 | Humour sourcé | La Saint-Patrick qui n'a pas porté chance |
| 9:02 | Image | Séisme et buts de foot sur la courbe de trafic |
| 9:30 | Vécu | Crochet : le jour où tes groupes ont explosé |
| 10:03 | Boucle refermée | La photo de bonne année téléchargée 32 millions de fois |
| 10:31 | Engagement | « À ton avis, pourquoi ? Mets ta théorie en commentaire » |
| 10:40 | Chiffre | Dix personnes sur Erlang, qui font aussi l'exploitation |
| 11:34 | Humour | Presque zéro réunion, « c'est justement le sujet », « envoyer mon CV » |
| 12:19 | Image | L'île d'Erlang de Facebook ; WhatsApp n'avait pas de continent à rejoindre |
| 12:38 | Image | L'île sans continent (bandeau « Illustration ») |
| 13:05 | Réponse honnête | Trois milliards aujourd'hui ; le nombre d'ingénieurs, Meta ne le publie pas |
| 13:25 | Retournement de fin | « Et si ça tenait justement parce qu'ils étaient si peu ? » (récolte de la section 1) |
| 13:41 | Question du pilier | « Quelle appli je décortique ensuite ? », écran de fin vers Uber |

**Total** : 34 relances en 13 min 55, environ une toutes les 25 secondes. Aucun trou de plus de 45 s. Ponts en fin de bloc : « on revient au langage du début » (1), « emmené un seul serveur au-delà de deux millions » (2), « un de leurs serveurs a fait mieux » (3), « comment on bosse quand on est si peu » (4).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Section 1, les sources | Moyen | « On va le vérifier ensemble » peut sonner comme du contexte après le hook | Deux phrases, défilement de 3 s ; l'anecdote Zuckerberg arrive dans les 15 s suivantes |
| Section 1, les chiffres de 2014 | Moyen | Quatre chiffres d'affilée | Quatre compteurs à l'écran, puis la réaction sur les vocaux de quatre minutes |
| Section 2, Erlang | Élevé | Un langage que le public ne connaît pas | Le central téléphonique, les petites boîtes (bandeau « Illustration »), le patch en pleine partie, puis Rick Reed « nouveau sur Erlang » |
| Section 3, la contention | Élevé | Le mot technique de la vidéo | Les plantages du noyau d'abord (une crise), le mot répété trois fois comme sur la diapo, puis le supermarché |
| Relance (~58 %) | Élevé | Chute classique | Coupure musicale, le teaser du hook enfin payé, la Saint-Patrick, puis le séisme et le foot dans les 40 s |
| Section 5, après les chiffres | Moyen | Plus de compteurs, que des propos rapportés | L'agenda vide, « c'est justement le sujet », la blague du CV, puis l'île |
| Fin | Moyen | Récapitulatif = signal de sortie | Récap d'une phrase ; la question « et aujourd'hui ? » arrive 15 s après, la question retournée 15 s plus tard |

## Notes de montage

- **Charte** : noire, celle du pilier génie (miniature `noir-06`). Le vert de WhatsApp sert seulement aux bulles de messages.
- **Composants réutilisés d'Uber** : le livreur à vélo de RAMEN (section 3), la jauge « 1,5 M connexions » (même chiffre que dans la vidéo Uber) et l'écran de fin. À construire : la carte de la machine (3 étages : le langage, le serveur, l'équipe), le compteur de connexions (même composant dans le hook, la section 3 et la section 4), les vingt-quatre caisses, la barre de vie, le trèfle, l'île d'Erlang.
- **Pas de vraie appli WhatsApp ni de vraie page Facebook à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Captures autorisées : l'article de Wired, le billet du blog WhatsApp du 06/01/2012, les diapositives de Rick Reed (2012 et 2014). Le post de Jan Koum et la réponse de Zuckerberg sont une reconstitution, photo floutée.
- **Illustrations à signaler** (bandeau « Illustration ») : les petites boîtes d'Erlang et l'île sans continent. Ce sont nos images, pas des sources.
- **Dates à l'écran** : chaque chiffre porte son année (2012, 2014, 2015, 2020 pour Uber, 2025). C'est la condition de la 2e vérif pour « 50 ingénieurs ».
- **Énergie** : montées sur le mur de bulles du hook, les plantages du noyau, le compteur figé à 425 000, le patch du moteur, la jauge Uber contre WhatsApp, la barre de vie, la coupure à 58 %, le séisme et le foot, la photo à 32 millions.
- **Fiche pendant le plateau de rétention** : la fiche vers la vidéo Uber au rappel du livreur de RAMEN (5:03). L'écran de fin pointe aussi Uber.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1, 24 | « En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs » ; « Le même mois, Wired écrit que WhatsApp emploie environ cinquante ingénieurs » |
| 2 | « à peu près dix-huit millions de personnes pour un seul ingénieur » |
| 28 | « Jan Koum […] annonce sur Facebook que WhatsApp dépasse les neuf cents millions. Et sous son post, Mark Zuckerberg répond avec une photo de Jan… en train de taper ce message » |
| 3 ⚠️, 4 | « En février deux mille quatorze, au moment où Facebook rachète WhatsApp, ils sont une trentaine d'ingénieurs pour plus de quatre cent cinquante millions d'utilisateurs » ; « l'équipe prend à peine quinze ou vingt personnes » (calcul : de 32-35 à environ 50) ; « un an et demi » (février 2014 → septembre 2015) |
| 30 | « même après le rachat, cette petite équipe fait encore tourner le service presque entièrement seule » |
| 13 ⚠️ (diapos de 2014) | « dix-neuf milliards de messages reçus chaque jour, et quarante milliards envoyés » ; « quatre cent soixante-cinq millions d'utilisateurs par mois […] cent quarante-sept millions de connexions ouvertes en même temps […] environ cinq cent cinquante serveurs, et plus de onze mille cœurs » ; « environ dix personnes sur Erlang » |
| 29 | « six cents millions de photos, deux cents millions de vocaux et cent millions de vidéos » ; « une seule photo a été téléchargée trente-deux millions de fois » |
| 5 | « un langage né chez Ericsson, dans les années quatre-vingt, pour des réseaux de téléphone à haut débit » ; citation de Cesarini ; « on peut déployer du nouveau code pendant que le système tourne » |
| 16 | « ils ne recrutent pas les gens parce qu'ils connaissent le langage. Un nouveau passe sa première semaine à l'apprendre » ; « Jamshid Mahdavi, un ingénieur de WhatsApp » |
| 31 | « Il arrive chez WhatsApp en deux mille onze, il vient du C, il a bossé chez Yahoo […] « nouveau sur Erlang » » ; « son boulot chez WhatsApp, c'est justement la montée en charge » |
| 8 | « Au début, un serveur de WhatsApp en tient environ deux cent mille » ; « fragile face aux pannes et aux surcharges » ; objectif d'un million avec le point d'exclamation ; « vers quatre cent vingt-cinq mille connexions, ça bloque » ; « un premier lot de corrections, et ils passent le million. […] Un mois plus tard […] deux millions » ; le pic de 2,8 millions en février 2012, « tentative de record involontaire », « ils ont dû intervenir » |
| 32 | « ils envoient exprès du vrai trafic en plus sur une machine […] quelques plantages du noyau » ; « les fruits étaient bas » ; « à force d'attaquer les mêmes bouchons » |
| 33 | « ils courent toujours après les trois millions […] la Saint-Patrick n'a pas porté autant chance qu'espéré » ; « Rick Reed range les événements du monde, le sport et les séismes, juste à côté des pannes de matériel » |
| 9 | « contention, contention, contention » ; « la plupart de ces corrections, il a fallu les faire dans la machine virtuelle d'Erlang » ; « FreeBSD brille aussi » |
| 10 | « Leur serveur avait vingt-quatre processeurs logiques » ; à l'écran : « ~100 Go de RAM » |
| 6 | « Le système en dessous, c'est FreeBSD. Pas Linux » |
| 7 | « Le six janvier deux mille douze […] deux millions deux cent soixante-dix-sept mille huit cent quarante-cinq connexions ouvertes » ; « quarante et un virgule neuf pour cent de processeur libre » |
| 36 | « RAMEN annonçait plus d'un million et demi de connexions pour tout son système, en deux mille vingt » |
| 11 | « La croissance, les séismes et le foot ! » ; « un séisme au Mexique, et les buts d'un match de foot, avec la mi-temps et la fin du match » (aucun chiffre) |
| 14 ⚠️ | « chacun des quelque cent cinquante serveurs de chat tient à peu près un million de téléphones » ; « Les diapos ne le disent pas » (pas d'interprétation) |
| 34 | « ces dix-là s'occupent à la fois du développement et de l'exploitation » |
| 15 | « sa leçon numéro un, c'est de rester très concentré […] même par des trucs de bureau comme les réunions » ; « les employés n'assistent presque jamais à une réunion » ; « en deux mille quinze, sur une scène à San José » |
| 35 | « le secret, c'est autant l'attitude que la technique » ; « oui, ils ne sont que quelques dizaines. Et c'est justement le sujet » ; « WhatsApp, lui, n'avait pas d'infrastructure existante à raccorder » |
| 26 ⚠️ | « une approche minimaliste : résoudre seulement les problèmes qu'il fallait résoudre » (jamais « faire peu, mais très bien ») |
| 17 | « Son premier chat était écrit en Erlang, et ils ont fini par le réécrire pour qu'il colle au reste de leur infrastructure […] une petite île d'Erlang […] assez de bateaux pour la relier au reste » |
| 20 ⚠️ | « D'après Meta, en deux mille vingt-cinq, WhatsApp dépasse les trois milliards d'utilisateurs par mois » |
| 23 | « Combien d'ingénieurs derrière ? Ça, Meta ne le publie pas » |
| Uber (`projets/uber/script.md`) | « le livreur de RAMEN […] gardait une connexion ouverte avec ton téléphone » |

**Non utilisés exprès** : 12 (« 8 000 cœurs » du résumé : on garde « plus de 11 000 » des diapositives, sans mélanger) ; 18 (ejabberd, coupé depuis la V1) ; 19 (citation d'Acton sur FreeBSD) ; 21, 22 (64 et 100 milliards) ; le « 40 millions par ingénieur » du fait 13 ; le prix du rachat (fait 4) : c'est l'angle business de Thibaut Dcode ; 27 (vidéo d'Enrico Tartarotti, le design).

**Déductions et images dites comme telles** : « chez WhatsApp, c'est le même principe » (connexion ouverte, appuyée sur les faits 7 et 14) ; le supermarché et ses vingt-quatre caisses (analogie) ; les réactions au but et au séisme (illustration de la diapo, sans chiffre) ; « imagine par combien de groupes elle est passée » (question) ; l'île sans continent (« Voilà comment je le vois », appuyée sur la phrase de Wired du fait 35) ; la question finale (une question, pas une affirmation, soutenue par Mahdavi et Wired, fait 35).

## Questions pour l'auteur

1. **La fin** : la question retournée (« et si ça tenait justement parce qu'ils étaient si peu ? ») est maintenant préparée dès la section 1. Il lui manque ton verdict : tu y crois, ou pour toi c'est surtout Erlang ? Une ou deux phrases dans le crochet de la fin, sinon la question reste ouverte et ça marche aussi.
2. **Tes groupes WhatsApp** (sections 1 et 4) : lesquels tu veux citer, et est-ce qu'un jour ils ont tous explosé en même temps (un match de la CAN, des résultats d'examen, une coupure) ? Si tu n'as rien de vrai, on coupe les deux crochets : le script tient sans eux.
3. **« Je suis dev, et un chiffre pareil, je ne le prends pas sur parole »** : c'est ton attitude, ou tu préfères une autre entrée ? Je n'ai pas écrit que tu avais lu les sources toi-même ; si tu les as lues, dis-le et on remet « je suis remonté aux sources ».
4. **Les blagues** : le patron de Facebook en paparazzi, le nom de variable, « Pas Linux, frère », la barre de vie du boss, le CV, et deux nouvelles (le titre « qui frime un peu », le trèfle de la Saint-Patrick) : lesquelles sont dans ton humour ? Le CV, en particulier : ça te va de le dire alors que tu as un poste ?
5. **La comparaison avec Uber** (section 3) : elle est juste (deux chiffres publiés), mais elle compare un système entier à un seul serveur, avec des besoins différents. Tu la gardes comme clin d'œil à la vidéo Uber, ou c'est trop injuste pour Uber ?
6. **L'écran de fin** : Uber (rappel du livreur de RAMEN) ou une vidéo génie plus récente (le pseudo, le 30 nov., ou l'iPhone, le 7 déc.) ?
