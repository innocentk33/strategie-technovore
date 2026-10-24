# WhatsApp : script v1

**Titre** : *Comment une cinquantaine d'ingénieurs faisaient tourner WhatsApp pour 900 millions de personnes* (titre 4 de la fiche avec la miniature `noir-06` : *Le génie caché de WhatsApp : une équipe minuscule*)

**Durée** : environ 1 860 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft, pauses et improvisations comprises) : environ 12 min 50 ; à 165 mots/min : 11 min 15 ; en coupes serrées comme sur Uber (~180 mots/min) : 10 min 20, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : un seul serveur. Le hook pose le chiffre impossible (en 2015, environ 50 ingénieurs pour plus de 900 millions de personnes) ; la vidéo descend dans la machine : le langage (Erlang), un serveur qui passe de 200 000 à plus de 2 millions de connexions, le jour où il s'emballe tout seul, puis la façon de travailler de l'équipe. La fin remplace la question du début par une meilleure : et si c'était parce qu'ils étaient peu que ça tenait ?

**Boucles ouvertes** :
1. « Comment cinquante personnes font tenir un truc pareil ? » (hook, 0:25) : refermée par étapes, sections 2 à 5, puis dans la fin.
2. « Un serveur qui, en 2012, a battu un record par accident » (hook, 0:30) : relancée à la fin de la section 3, refermée dans la section 4 (2,8 millions).
3. « Tes photos de bonne année » (hook) : récoltée dans la section 4 (la photo téléchargée 32 millions de fois le soir du Nouvel An).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (charte noire du pilier génie, cartes sombres d'Uber) ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de la colonne « 2e vérif » de [`sources.md`](sources.md), et des ⚠️ avec la formulation qu'il donne.

---

## 0. Hook (0:00 – 0:37) · objectif : 75 % à 0:15

[VISUEL : écran noir. Une bulle de message verte apparaît, puis des centaines, puis un mur de bulles qui remplit l'écran. Compteur « 900 000 000 ». Pas de titre, pas de logo.]

En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs. Donc à peu près dix-huit millions de personnes par ingénieur.

[VISUEL : le mur de bulles se resserre d'un coup ; en dessous, une petite salle avec cinquante silhouettes. Texte : « 2015 · ~50 ingénieurs ».]
[SON : un « tic » sec quand la salle apparaît.]

Tes vocaux de quatre minutes, tes photos de bonne année : tout ça passait par les machines d'une équipe qui tient dans une salle de classe.

Alors comment cinquante personnes font tenir un truc pareil ?

En fait, tout part d'un langage des années quatre-vingt, fait pour le téléphone. Et d'un serveur qui, en deux mille douze, a battu un record par accident.

[VISUEL : teaser d'une seconde : un compteur de connexions qui s'emballe, « 2 800 000 », alarme rouge. Arrêt sur image.]

---

## 1. Le chiffre tient (0:37 – 2:28)

Je suis dev, et un chiffre pareil, j'ai besoin de le vérifier avant d'y croire. Donc je suis remonté aux sources : un article de Wired de deux mille quinze, le blog de WhatsApp lui-même, et les diapos d'un de leurs ingénieurs, Rick Reed, présentées dans des conférences sur Erlang.

[VISUEL : défilement rapide de l'article de Wired, du billet de blog de 2012 et des diapositives de Rick Reed ; seules les dates restent nettes. Texte : « Toutes les sources en description ».]

[TES GROUPES WHATSAPP : LE GROUPE DE LA FAMILLE, CELUI DU QUARTIER OU DE LA PROMO, COMBIEN DE MESSAGES PAR JOUR. DEUX PHRASES MAXIMUM.]

Et le chiffre tient. En septembre deux mille quinze, Jan Koum, le cofondateur, annonce sur sa page Facebook que WhatsApp dépasse les neuf cents millions. Sous son post, Mark Zuckerberg répond avec une photo de Jan en train de taper ce message : « voilà une photo de toi en pleine action ». Le patron de Facebook qui fait le paparazzi, j'avoue, je ne m'y attendais pas.

[VISUEL : reconstitution en motion design (pas de vraie capture de Facebook) : un post « 900 millions », une réponse avec une photo floutée et l'appareil photo qui flashe.]

Le même mois, Wired écrit que WhatsApp emploie environ cinquante ingénieurs. Et ça devient encore plus bizarre quand tu recules d'un an.

En février deux mille quatorze, au moment où Facebook rachète WhatsApp, ils sont une trentaine d'ingénieurs pour plus de quatre cent cinquante millions d'utilisateurs. Du coup, entre les deux, les utilisateurs ont doublé, et l'équipe a pris à peine quinze ou vingt personnes.

[VISUEL : chronologie : « 2014 · ~30 ingénieurs · 450 M », puis « 2015 · ~50 ingénieurs · 900 M ». La barre des utilisateurs double, celle des ingénieurs bouge à peine.]

Donc s'ils tiennent, c'est que la machine encaisse à leur place.

Et elle encaisse quoi, exactement ? Début deux mille quatorze, Rick Reed donne les chiffres : dix-neuf milliards de messages reçus chaque jour, et quarante milliards envoyés. Plus six cents millions de photos, deux cents millions de messages vocaux et cent millions de vidéos. Par jour.

[VISUEL : quatre compteurs qui tournent côte à côte : messages, photos, vocaux, vidéos. Texte : « début 2014, par jour ».]

Ouais, t'as bien entendu. Et je suis sûr que dans le lot, il y avait des vocaux de quatre minutes.

Bref, pour comprendre comment une petite équipe tient ça, il faut revenir au langage du début.

---

## 2. Un langage fait pour le téléphone (2:28 – 4:38)

[VISUEL : la « carte de la machine », trois étages : le langage, le serveur, l'équipe. « Le langage » s'allume. Elle revient au début de chaque chapitre.]
[SON : ding de chapitre.]

Côté serveur, WhatsApp est écrit en Erlang. Tu n'en as peut-être jamais entendu parler, et c'est normal : c'est un langage né chez Ericsson, dans les années quatre-vingt, pour des réseaux de téléphone à haut débit.

Et en fait, le problème d'un réseau de téléphone, c'est celui de WhatsApp. Des millions de gens qui se parlent en même temps, et un réseau qui n'a pas le droit de tomber. Francesco Cesarini, un spécialiste d'Erlang, le résume dans Wired : le problème, c'était la scalabilité massive et la fiabilité.

[VISUEL : un vieux central téléphonique des années 80 en motion design, ses câbles qui deviennent des bulles vertes.]

**Abonnement (≈ 3:13, 25 % de la vidéo, juste après la première révélation)**

Si tu aimes voir ce qu'il y a sous le capot des applis que tu as dans la poche, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, le central téléphonique reste à l'écran.]

Pour faire simple, imagine des milliers de petites boîtes. Chaque boîte s'occupe d'une seule chose, et les boîtes s'envoient des lettres pour se parler. Tu vois l'idée : beaucoup de petites conversations en parallèle, exactement ce que fait une messagerie.

[VISUEL : des milliers de petites boîtes qui s'envoient des enveloppes. Bandeau : « Illustration ».]

Et Erlang a un pouvoir que les joueurs vont comprendre tout de suite : on peut déployer du nouveau code pendant que le système tourne. Imagine un patch installé en pleine partie, sans que personne soit renvoyé au menu. Pour une messagerie qui ne doit jamais s'arrêter, forcément, c'est de l'or.

[VISUEL : une partie en ligne, une barre « Mise à jour 100 % » passe en haut de l'écran, les joueurs continuent de jouer.]
[SON : petit « ding » de mise à jour, la musique ne s'arrête pas.]

Ce choix remonte loin. En deux mille neuf, Jan Koum pose déjà des questions sur la liste de diffusion d'ejabberd, un serveur de messagerie écrit en Erlang.

Là, tu te dis sûrement qu'ils ont recruté des experts d'Erlang. Et pourtant, WhatsApp ne recrute pas ses ingénieurs parce qu'ils connaissent le langage. D'après Jamshid Mahdavi, un de leurs ingénieurs, un nouveau passe sa première semaine à apprendre le langage.

Une semaine pour un langage entier. Il y a des devs qui mettent plus longtemps à choisir le nom d'une variable.

Bon, Erlang, c'est le moteur. Mais un bon moteur, il faut encore le régler. Et pour ça, on va regarder une seule machine.

---

## 3. Deux millions de connexions sur une machine (4:38 – 7:28)

[VISUEL : carte de la machine, « Le serveur » s'allume.]

Tu te rappelles le livreur de RAMEN, dans la vidéo sur Uber ? Il gardait une connexion ouverte avec ton téléphone, pour te livrer les messages sans que tu aies à demander. Chez WhatsApp, les téléphones sont branchés de la même façon sur des serveurs de chat. Donc chaque téléphone connecté, c'est une connexion que la machine doit tenir.

[VISUEL : le livreur à vélo de la vidéo Uber traverse l'écran ; derrière lui, un serveur auquel se branchent des milliers de petits téléphones.]

Au début, un serveur de WhatsApp en tient environ deux cent mille. Et Rick Reed ne cache rien : sur ses diapos, il écrit que leur cluster est fragile face aux pannes et aux surcharges.

Du coup, ils se fixent un objectif : un million de connexions par serveur. Sur la diapo, il y a même un point d'exclamation.

[VISUEL : la diapo reconstituée, « 1 million de connexions par serveur … ! », le point d'exclamation qui grossit.]

Mais vers quatre cent vingt-cinq mille, ça bloque.

[VISUEL : un compteur qui monte de « 200 000 » à « 425 000 », puis se fige ; la barre passe au rouge.]
[SON : un bruit de frein.]

Normalement, quand ton serveur sature, tu en ajoutes un deuxième. Eux, ils ont cherché pourquoi la machine bloquait. Et sur la diapo de Rick Reed, la réponse tient en un mot : contention.

En gros, imagine un supermarché avec vingt-quatre caisses ouvertes, mais une seule machine à carte bleue. Les caissiers sont là, ils sont prêts, et ils passent leur temps à attendre leur tour. Leur serveur avait vingt-quatre processeurs, et à l'intérieur, des petits embouteillages de ce genre les faisaient attendre.

[VISUEL : vingt-quatre caisses, une seule machine à carte qui passe de main en main ; une file se forme à chaque caisse. Puis les caisses deviennent vingt-quatre cœurs de processeur.]

Résultat : un premier lot de corrections, et ils passent le million. Un mois plus tard, deux millions.

Rick Reed l'écrit noir sur blanc : de deux cent mille à deux millions, tout était de la chasse à la contention. Et la plupart de ces corrections, il a fallu les faire dans la machine virtuelle d'Erlang elle-même.

Tu vois le niveau ? Quand le langage les freinait, ils ont ouvert le moteur du langage, et ils l'ont patché.

[VISUEL : le capot d'une voiture s'ouvre ; dessous, écrit « BEAM » (la machine virtuelle d'Erlang) ; une clé à molette entre dans le moteur.]

Et le système en dessous, c'est FreeBSD. Pas Linux, frère : FreeBSD. Sur la même diapo, Rick Reed écrit que FreeBSD « brille aussi ».

[VISUEL : le logo de FreeBSD qui brille, le pingouin de Linux qui sort du cadre en boudant.]

Le six janvier deux mille douze, WhatsApp publie un billet sur son blog. Le titre : « Un million, c'est tellement deux mille onze ». Dedans, ils collent les chiffres d'un de leurs serveurs : deux millions deux cent soixante-dix-sept mille huit cent quarante-cinq connexions ouvertes. Sur une seule machine.

[VISUEL : le compteur « 2 277 845 » qui se fige, la date « 06/01/2012 » en petit. Sous le compteur : « 24 processeurs · ~100 Go de RAM ».]

Et sur la même machine, il reste quarante et un virgule neuf pour cent de processeur libre. Donc elle n'est même pas à bout. Pour un joueur, c'est finir le boss avec encore presque la moitié de ta barre de vie.

[VISUEL : une barre de vie de boss de jeu vidéo, remplie à 41,9 %, qui clignote en vert.]

Ça, c'était le record officiel. Sauf qu'en février, un de leurs serveurs a fait mieux. Et personne ne lui avait demandé.

---

## 4. Le serveur qui s'est emballé (7:28 – 9:47) · relance forte à 58 %

[SON : la musique coupe net, une seconde de silence, puis une basse qui tient.]
[VISUEL : un serveur seul dans le noir, son compteur allumé.]

Février deux mille douze. Sur un des serveurs de WhatsApp, le compteur monte. Deux millions. Deux millions et demi. Deux millions huit cent mille connexions. Et là, les ingénieurs interviennent.

[VISUEL : le teaser du hook, enfin en entier : le compteur s'emballe jusqu'à « 2 800 000 », l'alarme rouge, une main qui tire le frein.]
[SON : alarme, puis coupure.]

Rick Reed appelle ça une tentative de record involontaire : eux n'avaient rien prévu, la machine est montée toute seule avec le trafic.

Et des vagues de trafic, il en montre d'autres. Dans sa conférence de deux mille douze, il y a une diapo géniale. Le titre : « La croissance, les séismes et le foot ! ». Dessus, une courbe de trafic avec des pics annotés : un séisme au Mexique, et les buts d'un match de foot, avec la mi-temps et la fin du match.

[VISUEL : la courbe reconstituée ; un pic marqué « séisme au Mexique », puis une série de petits pics marqués « but », « mi-temps », « fin du match ».]

Imagine. Un but est marqué, et des millions de gens dégainent leur téléphone au même moment pour réagir. Un séisme, et tout le monde écrit à sa famille pour savoir si ça va. Pour un serveur, c'est une vague qui arrive d'un coup.

[UN MOMENT OÙ TES GROUPES WHATSAPP ONT EXPLOSÉ EN MÊME TEMPS : UN MATCH DE LA CAN, UN RÉSULTAT D'EXAMEN, UNE COUPURE DE COURANT. UNE PHRASE.]

Et deux ans plus tard, la vague est devenue un océan. Début deux mille quatorze, d'après les diapos de Rick Reed : quatre cent soixante-cinq millions d'utilisateurs par mois, et cent quarante-sept millions de connexions ouvertes en même temps au pic. Pour tenir ça, environ cinq cent cinquante serveurs, et plus de onze mille cœurs de processeur.

[VISUEL : le serveur seul se multiplie en une salle entière ; compteurs « 465 M », « 147 M connexions », « ~550 serveurs », « > 11 000 cœurs ». Texte : « début 2014 ».]

Tu te rappelles les photos de bonne année du début ? Le soir du Nouvel An, une seule photo a été téléchargée trente-deux millions de fois. Imagine par combien de groupes elle est passée.

[VISUEL : une seule image de feu d'artifice qui se duplique en cascade de groupe en groupe ; compteur « 32 000 000 ».]

Sur environ cent cinquante serveurs de chat, chacun tient à peu près un million de téléphones. Donc un million par serveur, alors qu'ils avaient montré qu'une machine pouvait en tenir plus de deux. Pourquoi ? Les diapos ne le disent pas, et je ne vais pas l'inventer.

Et sur la diapo qui parle de l'équipe, il y a écrit : petite, environ dix personnes sur Erlang.

[VISUEL : « ~10 » en plein écran, puis dix silhouettes devant la salle des cinq cent cinquante serveurs.]

Dix. Dix personnes sur le code qui reçoit dix-neuf milliards de messages par jour.

Alors forcément, la question, c'est comment on bosse quand on est si peu sur un truc pareil.

---

## 5. Presque zéro réunion (9:47 – 11:20)

[VISUEL : carte de la machine, « L'équipe » s'allume.]

Jamshid Mahdavi, l'ingénieur de tout à l'heure, l'a expliqué en deux mille quinze, à San José. Pour lui, la leçon numéro un, c'est de rester très concentré sur ce que tu dois faire. De ne pas te laisser distraire par d'autres activités, d'autres technologies, et même par des trucs de bureau comme les réunions.

Et en effet, d'après Wired, chez WhatsApp, les employés n'assistent presque jamais à une réunion.

[VISUEL : un agenda de la semaine, entièrement vide ; une seule case « réunion » qui s'efface.]
[SON : un « pop » quand la case disparaît.]

Franchement, rien que pour ça, j'ai envie d'envoyer mon CV.

Mahdavi parle aussi d'une approche minimaliste : résoudre seulement les problèmes qu'il fallait résoudre. Tu te rappelles le serveur bloqué à quatre cent vingt-cinq mille ? C'est exactement ça : ils ont cherché les embouteillages, un par un, et ils ont corrigé ceux-là.

[VISUEL : retour sur les vingt-quatre caisses ; les files se vident une par une.]

Mais Erlang, Facebook l'avait aussi utilisé. Son chat était écrit en Erlang, puis ils l'ont réécrit. Jay Parikh, vice-président de l'ingénierie chez Facebook, raconte dans Wired que c'était une petite île d'Erlang, et qu'il était difficile de construire assez de bateaux pour la relier au reste.

[VISUEL : une petite île marquée « Erlang » au milieu d'un océan marqué « Facebook » ; des petits bateaux qui font des allers-retours et n'arrivent pas à suivre.]

Voilà comment je le vois. Chez le géant, Erlang était une île. Chez WhatsApp, c'était tout le continent. Quand toute ton équipe travaille sur la même île, tu n'as pas besoin de bateaux.

[VISUEL : l'île grossit jusqu'à devenir un continent ; les bateaux disparaissent.]

Et du coup, une petite équipe peut tout comprendre, de l'appli jusqu'au moteur du langage. C'est ce qu'ils ont fait avec la machine virtuelle d'Erlang.

---

## 6. Fin (11:20 – 12:50)

[SON : la musique du début revient.]
[VISUEL : la carte de la machine en entier, les trois étages allumés, une bulle verte qui la traverse de haut en bas en accéléré.]

Bref, si je reprends : un langage pensé pour des réseaux de téléphone, une équipe qui chasse les embouteillages jusque dans le moteur d'Erlang, des serveurs qui tiennent un million de téléphones chacun, et presque pas de réunions. Voilà comment une cinquantaine d'ingénieurs faisaient tourner WhatsApp pour neuf cents millions de personnes en deux mille quinze.

Aujourd'hui, d'après Meta, en deux mille vingt-cinq, WhatsApp dépasse les trois milliards d'utilisateurs par mois.

[VISUEL : le compteur « 900 000 000 » du hook grimpe jusqu'à « 3 000 000 000+ ». Texte : « d'après Meta, 2025 ».]

Donc la prochaine fois que tu envoies un vocal dans le groupe de la famille, pense au serveur de chat au bout de la connexion. En deux mille quatorze, un serveur comme lui tenait environ un million de téléphones en même temps que le tien, et il avait été réglé par une équipe qui aurait tenu dans une salle de classe.

Au début, je te demandais comment cinquante personnes font tenir un truc pareil. Sauf qu'après tout ça, je me pose une autre question : et si ça tenait justement parce qu'ils étaient cinquante ?

[VISUEL : la petite salle de cinquante silhouettes du hook, cette fois avec la salle des serveurs derrière elle.]

[OPTIONNEL : CE QUI T'A LE PLUS SURPRIS, TOI, EN TANT QUE DEV : LE PATCH DU MOTEUR D'ERLANG, LES 41,9 % LIBRES, OU LES RÉUNIONS. UNE OU DEUX PHRASES.]

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et si tu veux revoir le livreur de RAMEN, celui qui garde la connexion ouverte avec ton téléphone, c'est dans la vidéo sur Uber, juste là.

[VISUEL : écran de fin, 20 s : vidéo Uber à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Chiffre | 900 millions, environ 50 ingénieurs, en 2015 : le mur de bulles et la petite salle |
| 0:25 | Question centrale | « Alors comment cinquante personnes font tenir un truc pareil ? » |
| 0:33 | Teaser | Le compteur qui s'emballe à 2,8 M, arrêt sur image (refermé à 7:28) |
| 1:15 | Anecdote | Zuckerberg en paparazzi sous le post de Jan Koum |
| 1:45 | Contraste | 2014 → 2015 : les utilisateurs doublent, l'équipe bouge à peine |
| 2:10 | Chiffres + réaction | 19 + 40 milliards de messages, « Ouais, t'as bien entendu » |
| 2:28 | Chapitre | Carte de la machine, « Le langage » |
| 3:00 | Retournement | Le problème du téléphone, c'est celui de WhatsApp |
| 3:13 | Appel à l'action | Abonnement (25 %) |
| 3:45 | Humour gamer | Le patch installé en pleine partie |
| 4:15 | Surprise | Une semaine pour apprendre Erlang ; la blague du nom de variable |
| 4:38 | Rappel | Le livreur de RAMEN de la vidéo Uber (fiche vers Uber) |
| 5:15 | Blocage | Le compteur se fige à 425 000, bruit de frein |
| 5:35 | Analogie | Vingt-quatre caisses, une seule machine à carte |
| 6:15 | Révélation | Ils ont patché le moteur du langage |
| 6:35 | Humour | « Pas Linux, frère : FreeBSD », le pingouin qui boude |
| 7:00 | Chiffre + jeu vidéo | 2 277 845 connexions, 41,9 % libre, la barre de vie du boss |
| 7:28 | Coupure musique | Février 2012 : le serveur qui s'emballe (58 %) |
| 8:05 | Image | Séisme et buts de foot sur la courbe de trafic |
| 8:30 | Vécu | Crochet : le jour où tes groupes ont explosé |
| 9:05 | Boucle refermée | La photo de bonne année téléchargée 32 millions de fois |
| 9:35 | Honnêteté + chiffre | « Je ne vais pas l'inventer », puis « environ dix personnes sur Erlang » |
| 10:10 | Humour | Presque zéro réunion, « envoyer mon CV » |
| 10:45 | Image | L'île d'Erlang de Facebook contre le continent de WhatsApp |
| 11:55 | Retournement de fin | « Et si ça tenait justement parce qu'ils étaient cinquante ? » |
| 12:25 | Question du pilier | « Quelle appli je décortique ensuite ? », écran de fin vers Uber |

**Total** : 26 relances en 12 min 50, environ une toutes les 30 secondes. Aucun trou de plus de 60 s. Ponts en fin de bloc : « revenir au langage du début » (1), « regarder une seule machine » (2), « un de leurs serveurs a fait mieux » (3), « comment on bosse quand on est si peu » (4).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Section 1, les sources | Moyen | « Je suis remonté aux sources » peut sonner comme du contexte après le hook | Le défilement dure 3 s ; l'anecdote Zuckerberg arrive dans les 20 s suivantes |
| Section 1, les chiffres de 2014 | Moyen | Quatre chiffres d'affilée | Quatre compteurs à l'écran, puis la réaction et la blague des vocaux de quatre minutes |
| Section 2, Erlang | Élevé | Un langage que le public ne connaît pas | Le central téléphonique, les petites boîtes (bandeau « Illustration »), puis le patch en pleine partie |
| Section 3, la contention | Élevé | Le mot technique de la vidéo | Le supermarché d'abord, le mot ensuite, puis les caisses qui deviennent des cœurs |
| Relance (~60 %) | Élevé | Chute classique | Coupure musicale, le teaser du hook enfin payé, puis le séisme et le foot dans les 40 s |
| Section 5, après les chiffres | Moyen | Plus de compteurs, que des propos rapportés | L'agenda vide, la blague du CV, puis l'image de l'île |
| Fin | Moyen | Récapitulatif = signal de sortie | La question retournée arrive moins de 40 s après le début du récap |

## Notes de montage

- **Charte** : noire, celle du pilier génie (miniature `noir-06`). Le vert de WhatsApp sert seulement aux bulles de messages.
- **Composants réutilisés d'Uber** : le livreur à vélo de RAMEN (section 3) et l'écran de fin. À construire : la carte de la machine (3 étages : le langage, le serveur, l'équipe), le compteur de connexions (même composant dans le hook, la section 3 et la section 4), les vingt-quatre caisses, la barre de vie, l'île d'Erlang.
- **Pas de vraie appli WhatsApp ni de vraie page Facebook à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Captures autorisées : l'article de Wired, le billet du blog WhatsApp du 06/01/2012, les diapositives de Rick Reed (2012 et 2014). Le post de Jan Koum et la réponse de Zuckerberg sont une reconstitution, photo floutée.
- **Les petites boîtes d'Erlang** : c'est notre illustration, pas une source. Bandeau « Illustration » à l'écran.
- **Dates à l'écran** : chaque chiffre porte son année (2012, 2014, 2015, 2025). C'est la condition de la 2e vérif pour « 50 ingénieurs ».
- **Énergie** : montées sur le mur de bulles du hook, le compteur figé à 425 000, le patch du moteur, la barre de vie, la coupure à 58 %, le séisme et le foot, la photo à 32 millions.
- **Fiche pendant le plateau de rétention** : la fiche vers la vidéo Uber au rappel du livreur de RAMEN (4:38). L'écran de fin pointe aussi Uber.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1, 24 | « En deux mille quinze, plus de neuf cents millions de personnes utilisent WhatsApp. Et derrière, environ cinquante ingénieurs » ; « Le même mois, Wired écrit que WhatsApp emploie environ cinquante ingénieurs » |
| 2 | « à peu près dix-huit millions de personnes par ingénieur » |
| 28 | « Jan Koum […] annonce sur sa page Facebook que WhatsApp dépasse les neuf cents millions. Sous son post, Mark Zuckerberg répond avec une photo de Jan en train de taper ce message » |
| 3 ⚠️, 4 | « En février deux mille quatorze, au moment où Facebook rachète WhatsApp, ils sont une trentaine d'ingénieurs pour plus de quatre cent cinquante millions d'utilisateurs » ; « l'équipe a pris à peine quinze ou vingt personnes » (calcul : de 32-35 à environ 50) |
| 13 ⚠️ (diapos de 2014) | « dix-neuf milliards de messages reçus chaque jour, et quarante milliards envoyés » ; « quatre cent soixante-cinq millions d'utilisateurs par mois […] cent quarante-sept millions de connexions […] environ cinq cent cinquante serveurs, et plus de onze mille cœurs » ; « environ dix personnes sur Erlang » |
| 29 | « six cents millions de photos, deux cents millions de messages vocaux et cent millions de vidéos » ; « une seule photo a été téléchargée trente-deux millions de fois » |
| 5 | « un langage né chez Ericsson, dans les années quatre-vingt, pour des réseaux de téléphone à haut débit » ; citation de Cesarini ; « on peut déployer du nouveau code pendant que le système tourne » |
| 18 ⚠️ | « En deux mille neuf, Jan Koum pose déjà des questions sur la liste de diffusion d'ejabberd, un serveur de messagerie écrit en Erlang » (rien de plus) |
| 16 | « WhatsApp ne recrute pas ses ingénieurs parce qu'ils connaissent le langage […] un nouveau passe sa première semaine à apprendre le langage » |
| 14 ⚠️ | « Sur environ cent cinquante serveurs de chat, chacun tient à peu près un million de téléphones » ; « Les diapos ne le disent pas » (pas d'interprétation) ; fin : « En deux mille quatorze, un serveur comme lui tenait environ un million de téléphones » |
| 8 | « Au début, un serveur de WhatsApp en tient environ deux cent mille » ; « fragile face aux pannes et aux surcharges » ; objectif d'un million avec le point d'exclamation ; « vers quatre cent vingt-cinq mille, ça bloque » ; « un premier lot de corrections, et ils passent le million. Un mois plus tard, deux millions » ; le pic involontaire à 2,8 millions en février 2012 |
| 9 | « de deux cent mille à deux millions, tout était de la chasse à la contention » ; « la plupart de ces corrections, il a fallu les faire dans la machine virtuelle d'Erlang » ; « FreeBSD brille aussi » |
| 10 | « Leur serveur avait vingt-quatre processeurs » ; à l'écran : « ~100 Go de RAM » |
| 6 | « Le système en dessous, c'est FreeBSD. Pas Linux » |
| 7 | « Le six janvier deux mille douze […] deux millions deux cent soixante-dix-sept mille huit cent quarante-cinq connexions ouvertes » ; « quarante et un virgule neuf pour cent de processeur libre » |
| 11 | « La croissance, les séismes et le foot ! » ; « un séisme au Mexique, et les buts d'un match de foot, avec la mi-temps et la fin du match » (aucun chiffre) |
| 15 | « la leçon numéro un, c'est de rester très concentré […] même par des trucs de bureau comme les réunions » ; « les employés n'assistent presque jamais à une réunion » ; « en deux mille quinze, à San José » |
| 26 ⚠️ | « une approche minimaliste : résoudre seulement les problèmes qu'il fallait résoudre » (jamais « faire peu, mais très bien ») |
| 17 | « Son chat était écrit en Erlang, puis ils l'ont réécrit […] une petite île d'Erlang […] assez de bateaux pour la relier au reste » |
| 20 ⚠️ | « d'après Meta, en deux mille vingt-cinq, WhatsApp dépasse les trois milliards d'utilisateurs par mois » |
| Uber (`projets/uber/script.md`) | « le livreur de RAMEN […] gardait une connexion ouverte avec ton téléphone » |

**Non utilisés exprès** : 12 (« 8 000 cœurs » du résumé : on garde « plus de 11 000 » des diapositives, sans mélanger) ; 19 (citation d'Acton sur FreeBSD) ; 21, 22 (64 et 100 milliards) ; 23 (effectif actuel) ; le « 40 millions par ingénieur » du fait 13 ; le prix du rachat (fait 4) : c'est l'angle business de Thibaut Dcode ; 27 (vidéo d'Enrico Tartarotti).

**Déductions dites comme telles, à garder à l'œil au grill** : « Chez WhatsApp, les téléphones sont branchés de la même façon sur des serveurs de chat » (analogie avec RAMEN, appuyée sur les « ~1M phones each » du fait 14) ; « la machine est montée toute seule avec le trafic » (lecture de « unintentional record attempt ») ; les réactions au but et au séisme (illustration de la diapo, sans chiffre) ; « imagine par combien de groupes elle est passée » (question, pas affirmation) ; l'île devenue continent (« Voilà comment je le vois »).

## Questions pour l'auteur

1. **Tes groupes WhatsApp** (sections 1 et 4) : lesquels tu veux citer, et est-ce qu'un jour ils ont tous explosé en même temps (un match de la CAN, des résultats d'examen, une coupure) ? Si tu n'as rien, on coupe les deux crochets.
2. **Ton enjeu de dev** : pour Uber, c'était « mon pote avait raison ? ». Ici, qu'est-ce qui te fascine le plus : qu'ils aient patché le moteur d'Erlang, les 41,9 % de processeur libre, ou les réunions ? Ta réponse remplace le crochet optionnel de la fin, et elle peut remonter dans la section 1.
3. **La fin** : la question retournée (« et si ça tenait justement parce qu'ils étaient cinquante ? ») te ressemble, ou tu préfères un verdict franc ?
4. **Les blagues** : le patron de Facebook en paparazzi, le nom de variable, « Pas Linux, frère », la barre de vie du boss, le CV : lesquelles sont dans ton humour ? Tu as mieux pour les vingt-quatre caisses ?
5. **L'écran de fin** : Uber (rappel du livreur de RAMEN) ou le pseudo (la vidéo génie la plus récente, le 23 nov.) ?
