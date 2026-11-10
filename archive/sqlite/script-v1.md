# SQLite : script v1

**Titre** (provisoire, à choisir au grill) : *SQLite : la base de données qui est partout, et qui n'a pas de serveur* (titre 3 de la fiche, recommandé). Le titre de travail de `strategie.md` (« le fichier de 300 Ko qui a battu Oracle ») tombe : la bibliothèque fait 590 à 750 Ko (fait 5), et Oracle est 1er en popularité (fait 30). Autres titres dans « Questions pour l'auteur ».

**Durée** : 1 677 mots de voix off (`controle.py`, 23/10 ; 2,5 liaisons pour 100 mots). À 145 mots/min (ton débit mesuré sur ArtCraft, pauses et improvisations comprises) : environ 11 min 35 ; à 165 mots/min : 10 min 10 ; en coupes serrées comme sur Uber (~180 mots/min) : 9 min 20, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : ton téléphone. Le hook ouvre le téléphone et y trouve des centaines de bases SQLite ; la vidéo remonte d'où vient ce logiciel (un destroyer et un serveur qui tombe), ce qu'il a d'étrange (pas de serveur), ce qu'il y a dans le fichier, et pourquoi on lui confie autant (les tests, le domaine public, 2050). La fin revient au téléphone : maintenant, tu sais ce qui dort dedans.

**Boucles ouvertes** :
1. « Comment un logiciel sans serveur s'est retrouvé partout ? » (hook, 0:30) : refermée par étapes (sections 2, 3 et 5), puis dans la fin.
2. « Le serveur qui tombe sur un destroyer » (pont de la section 1) : refermée dans la section 2.
3. « Ton téléphone s'éteint en plein message » (relance forte, fin de la section 4) : refermée dans la section 5 (les tests de coupure de courant).
4. « Un an à soixante heures par semaine » (teaser de la section 4) : refermé dans la section 5.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (charte noire du pilier génie) ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de la colonne « 2e vérif » de [`sources.md`](sources.md), et des ⚠️ avec la formulation qu'il donne. Aucune capture de tes applis de travail : une maquette générique avec le logo Flutter suffit.

---

## 0. Hook (0:00 – 0:29) · objectif : 75 % à 0:15

[VISUEL : un téléphone en gros plan, écran noir. Des petites icônes de fichiers « .db » apparaissent une par une, puis par dizaines, jusqu'à remplir l'écran. Compteur en bas : « des centaines ». Pas de titre, pas de logo.]
[SON : un « tic » par fichier, qui s'accélère jusqu'à devenir un grésillement.]

Dans ton téléphone, là, maintenant, il y a probablement des centaines de petites bases de données. Et toutes viennent du même logiciel : SQLite.

[VISUEL : dézoom : le téléphone devient un point au milieu de milliers d'autres, puis d'une planète entière de téléphones. Texte : « 4 000 000 000+ smartphones ».]

Du coup, avec plus de quatre milliards de smartphones sur Terre, sqlite.org estime qu'il y a probablement plus de mille milliards de bases SQLite en service.

[VISUEL : « 1 000 000 000 000 » plein écran. En petit : « estimation de sqlite.org ».]

Sauf que ce logiciel n'a même pas de serveur. Alors comment un truc pareil s'est retrouvé à peu près partout ?

[VISUEL : retour sur le téléphone ; un seul fichier « .db » clignote au centre, avec un point d'interrogation.]

---

## 1. Partout, sauf sur ton radar (0:29 – 2:02)

En fait, tout commence sur un bateau de guerre, avec un serveur qui tombe en panne. On y vient. D'abord, je veux te montrer où il se cache.

[VISUEL : teaser d'une seconde : la silhouette d'un destroyer dans la nuit, un écran d'ordinateur qui s'éteint à son bord. Arrêt sur image.]

Imagine la liste des endroits où SQLite tourne. D'après sqlite.org, il est dans chaque appareil Android, chaque iPhone, chaque Mac, et chaque Windows dix et onze. Et dans Chrome, Firefox et Safari.

[VISUEL : la liste se remplit à l'écran, logo par logo, façon succès débloqués dans un jeu. Texte : « Source : sqlite.org, Most Widely Deployed ».]
[SON : un « ding » de succès débloqué à chaque ligne.]

Et la liste continue : Skype, Dropbox, Python, la plupart des téléviseurs et des box, et même la plupart des systèmes multimédias des voitures. Donc ta télé aussi, probablement.

Moi, je suis dev, et SQLite, je l'ai rangé dans mes propres applis. [TON VÉCU : DANS QUEL GENRE D'APPLI, POUR STOCKER QUOI, ET CE QUE TU EN PENSAIS À L'ÉPOQUE. DEUX PHRASES MAXIMUM.]

[VISUEL : maquette générique d'une appli avec le logo Flutter, un petit fichier « .db » qui se range dedans. Aucune capture de tes vraies applis.]

Sur Android, par exemple, Google donne aux développeurs une boîte à outils toute prête pour ça, et la base est rangée dans le dossier privé de l'appli. Personne d'autre n'y touche.

Et WhatsApp, alors ? D'après des analyses forensiques, sur Android, WhatsApp range tes messages dans un fichier SQLite. Tes conversations, tes groupes, tout ça finit dans une petite base au fond du téléphone.

[VISUEL : une bulle de message verte qui glisse dans un fichier « msgstore.db ». Texte : « d'après des analyses forensiques (Magnet Forensics) ».]

Résultat, sqlite.org pense que SQLite est probablement utilisé plus que tous les autres moteurs de bases de données réunis. Et pour eux, c'est la deuxième bibliothèque logicielle la plus déployée au monde, juste après libz, celle qui compresse les fichiers.

[VISUEL : un podium : « 1. libz », « 2. SQLite ». Texte : « d'après sqlite.org ».]

Le truc le plus installé de ta vie, et tu n'as jamais vu son nom. Alors d'où il sort ?

---

## 2. Le destroyer et le serveur qui tombe (2:02 – 3:53)

[VISUEL : charte noire ; un chantier naval la nuit, un destroyer en construction. Texte : « ~2000 · Bath Iron Works ».]
[SON : bruit sourd de coque métallique, vent.]

On est vers l'an deux mille. D. Richard Hipp est sous-traitant pour Bath Iron Works, un chantier naval qui construit des navires pour l'US Navy. Et lui, il écrit un logiciel pour un destroyer, le USS Oscar Austin.

Son logiciel sert au contrôle des avaries. Pour faire simple : si un tuyau casse à bord, il aide à isoler la partie touchée.

[VISUEL : coupe du bateau en schéma ; un tuyau rouge qui fuit, des vannes qui se ferment autour.]

Sauf que l'appli s'appuie sur une base de données, Informix, qui tourne sur un serveur. Et ce serveur, de temps en temps, il tombe. Et quand il tombe, l'appli de Hipp ne marche plus.

[VISUEL : le serveur s'éteint, l'écran de contrôle du bateau passe au gris. Texte : « Connexion perdue ».]
[SON : bip d'erreur, puis silence.]

Imagine : un logiciel fait pour gérer une avarie, qui s'arrête parce qu'une autre machine a planté. C'est comme perdre ta partie en ligne parce que le serveur du jeu a lâché, alors que toi, tu n'as rien fait.

[VISUEL : petit gag : un écran de jeu figé « Connexion au serveur perdue », la manette qui tombe des mains.]

Du coup, un collègue lui sort une phrase toute simple. Hipp la raconte dans le podcast CoRecursive : « Richard, pourquoi tu n'en écris pas une toi-même ? »

[VISUEL : bulle de dialogue en motion design. Texte : « d'après Hipp, CoRecursive #066 ».]

Et le timing tombe bien. D'après Hipp, à ce moment-là, les contrats publics sont gelés, et il se retrouve quelques mois sans travail. Donc il en profite. Le projet SQLite démarre le neuf mai deux mille, et la version un point zéro sort le dix-sept août.

[VISUEL : un calendrier : « 9 mai 2000 » s'entoure, puis les pages défilent jusqu'au « 17 août 2000 · v1.0 ».]

Trois mois. Pendant qu'un gouvernement mettait ses contrats en pause, un type s'ennuyait, et il a écrit le logiciel le plus installé de ta poche.

**Abonnement (≈ 3:35, ~30 % de la vidéo, juste après la première révélation : l'histoire du destroyer)**

Si tu aimes découvrir ce qui se cache derrière les applis que tu as dans la poche, abonne-toi : sur Technovore, je les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, le destroyer reste à l'écran.]

Mais il reste la question de départ : sans serveur, comment ça marche ?

---

## 3. Pas de serveur (3:53 – 5:31)

[VISUEL : charte noire ; carte du chapitre « Pas de serveur ».]

Normalement, une base de données, c'est un programme qui tourne à part, sur une machine. Ton appli lui envoie une question, elle attend, et la réponse revient. C'est exactement ce qui tombait sur le destroyer.

[VISUEL : à gauche, un téléphone ; à droite, une grosse machine « serveur » ; une flèche aller, une flèche retour. Puis la machine s'éteint et la flèche reste en l'air.]

SQLite fait l'inverse. En gros, c'est une bibliothèque : un bout de code que l'appli embarque avec elle. Pas de programme à côté, rien à configurer. La base, c'est un fichier, posé sur le disque, et l'appli le lit elle-même.

[VISUEL : la grosse machine rétrécit et rentre à l'intérieur du téléphone ; il ne reste qu'un fichier « .db ».]
[SON : « shlok » d'aspiration quand la machine rentre dans le téléphone.]

Tu te rappelles le jeu en ligne de tout à l'heure ? SQLite, c'est la sauvegarde sur la carte mémoire. Personne ne peut la couper à ta place.

[VISUEL : une carte mémoire de console qui s'enfonce dans un téléphone.]

Et la bibliothèque entière pèse moins d'un mégaoctet. En deux mille vingt-trois, sqlite.org mesurait entre cinq cent quatre-vingt-dix et sept cent cinquante kilo-octets, selon la machine.

[VISUEL : une jauge « < 1 Mo », avec trois barres : « Raspberry Pi 4 · 590 Ko », « Ubuntu x64 · 650 Ko », « Mac M1 · 750 Ko ». Texte : « mesures de 2023 ».]

Donc si tu as vu passer « trois cents kilo-octets » quelque part, c'est faux aujourd'hui. Ça reste minuscule, mais en fait, pas aussi minuscule.

Et un seul fichier, ça tient beaucoup. La taille maximale d'une base SQLite, c'est deux cent quatre-vingt-un téraoctets.

[VISUEL : un tout petit fichier qui gonfle jusqu'à remplir l'écran. Texte : « max : 281 To ».]

J'ai envie de voir la tête de celui qui atteint la limite.

Et en fait, pour lire et écrire plein de petits morceaux de données, SQLite peut aller plus vite que de les ranger dans des fichiers séparés. Dans un essai de deux mille dix-sept, sqlite.org mesurait environ trente-cinq pour cent de gagné.

[VISUEL : deux couloirs de course : « 100 000 fichiers » contre « 1 fichier SQLite ». Texte : « ≈ 35 %, essai de 2017, chiffre approximatif ».]

Bon. Un fichier qui fait le boulot d'un serveur. Mais qu'est-ce qu'il y a dedans ?

---

## 4. Dans le fichier (5:31 – 7:18)

[VISUEL : un fichier « .db » qui s'ouvre comme une boîte. Texte en police mono : « SQLite format 3 ».]

Si tu ouvres un fichier SQLite, les cent premiers octets, c'est une carte d'identité. Et dedans, il y a écrit en clair : « SQLite format 3 ».

Ensuite, le fichier est découpé en pages, toutes de la même taille. Par défaut, quatre mille quatre-vingt-seize octets.

[VISUEL : le fichier se découpe en une pile de pages identiques, numérotées.]

Et ces pages sont rangées en arbre. Pour faire simple, c'est comme chercher un mot dans le dictionnaire : tu ne lis pas tout depuis la lettre A. Tu ouvres au milieu, tu vois si c'est avant ou après, et tu recommences.

[VISUEL : un arbre de pages ; un chemin s'allume de la racine jusqu'à une feuille en trois sauts. Texte : « B-arbre ».]
[SON : trois « clics » au rythme des sauts.]

Du coup, même dans une grosse base, SQLite retrouve une ligne en quelques sauts, sans tout parcourir.

Maintenant, imagine que deux choses se passent en même temps. Ton appli écrit un nouveau message, et au même moment, elle relit l'historique.

Pour ça, depuis deux mille dix, SQLite a un mode qui s'appelle le WAL. En fait, au lieu de toucher à la base, il écrit les changements dans un fichier à côté, comme un brouillon. Et plus tard, il les reverse dans la base. Ça s'appelle un checkpoint.

[VISUEL : à gauche, la base ; à droite, un fichier « -wal » qui se remplit de lignes. Une flèche « checkpoint » les reverse d'un coup dans la base.]

Résultat : ceux qui lisent ne bloquent plus celui qui écrit, et l'inverse non plus.

[VISUEL : deux personnages, un qui lit, un qui écrit, qui ne se marchent plus dessus.]

Sauf que tout ça repose sur un fichier, posé sur un disque. Et un disque, ça peut s'arrêter n'importe quand.

**Relance forte (≈ 7:00, ~60 % de la vidéo)**

[SON : la musique coupe net. Une seconde de silence.]
[VISUEL : le téléphone du hook ; la batterie passe à 1 %, puis l'écran s'éteint d'un coup.]

Ton téléphone qui s'éteint pile pendant que WhatsApp écrit ton message. Pour une base de données, c'est le pire moment possible. Et ça arrive sur des milliards d'appareils.

Si SQLite tient le coup, c'est grâce à un type qui a passé un an, à soixante heures par semaine, à chasser ses propres bugs.

---

## 5. Testé pour les avions (7:18 – 9:19)

[VISUEL : charte noire ; carte du chapitre « Les tests ».]

À un moment, des bugs remontent depuis Android. Donc Hipp se lance dans un chantier énorme : tester chaque branche du code. Chaque « si », chaque « sinon ».

[VISUEL : un bout de code en C ; chaque « if » s'allume en vert quand un test passe dessus.]

Il le raconte sur CoRecursive : ça lui a pris un an de semaines à soixante heures. Un an de grind. Même un boss de Dark Souls ne te demande pas ça.

[VISUEL : une barre de vie de boss, « BUGS », qui descend pixel par pixel sur un calendrier de cinquante-deux semaines.]
[SON : coups d'épée en boucle, de plus en plus lents.]

Et à la fin, il dit une phrase que tout dev rêve de prononcer : « On a arrêté de recevoir des rapports de bugs d'Android. »

[VISUEL : une boîte de réception « Android » qui se vide. Texte : « d'après Hipp, CoRecursive #066 ».]

Aujourd'hui, le cœur de SQLite est couvert à cent pour cent : chaque branche testée, et une mesure encore plus stricte, le MC/DC, à cent pour cent aussi.

[VISUEL : deux jauges pleines : « Branches · 100 % », « MC/DC · 100 % ».]

Et là, regarde la taille de la pile. En deux mille vingt-trois, pour cent cinquante-six mille lignes de code, il y avait quatre-vingt-douze millions de lignes de tests. Cinq cent quatre-vingt-dix fois plus.

[VISUEL : une toute petite pile « code · 156 000 lignes » à côté d'une tour qui sort du cadre, « tests · 92 000 000 lignes ». Texte : « ×590 · chiffres de 2023 ».]

Ouais, t'as bien entendu. Pour chaque ligne de code, presque six cents lignes pour vérifier qu'elle marche.

Et ces tests, ils font exprès de casser le logiciel : plus de mémoire, erreurs de disque, et plantages en plein milieu d'une écriture, coupures de courant comprises. Tu vois le téléphone qui s'éteint de tout à l'heure ? Il est dans les tests.

[VISUEL : retour sur le téléphone éteint ; il se rallume, le fichier « .db » est intact, coche verte.]

Mais l'histoire ne s'arrête pas aux téléphones. Des constructeurs d'avionique s'intéressent à SQLite. Du coup, les développeurs construisent une deuxième suite de tests, TH3, pensée pour les normes de l'aviation.

[VISUEL : deux classeurs : « TCL · 51 445 cas », « TH3 · 50 362 cas ». Texte : « version 3.42.0 (2023) ».]

Attention, je pèse mes mots : rien ne dit que SQLite est certifié pour les avions. Ce qui est sourcé, c'est une suite de tests pensée pour leurs normes.

Et pourtant, d'après sqlite.org, Airbus confirme que SQLite tourne dans le logiciel de vol de l'A trois cent cinquante.

[VISUEL : un Airbus A350 en silhouette ; un petit fichier « .db » qui s'allume dans le cockpit. Texte : « d'après sqlite.org ».]

Donc le même logiciel que dans ton téléphone vole au-dessus de ta tête.

---

## 6. À tout le monde, jusqu'en 2050 (9:19 – 10:28)

[VISUEL : charte noire ; une feuille de licence vierge, sans signature.]

Et le plus étrange, c'est peut-être qu'il n'appartient à personne. Le code de SQLite est dans le domaine public : n'importe qui peut le prendre.

Sauf que pour y contribuer, c'est l'inverse. Le projet n'accepte pas de correctif sans une déclaration écrite où tu verses ta contribution au domaine public.

[VISUEL : un formulaire « Je renonce à mes droits », avec un tampon.]
[SON : coup de tampon.]

Et pour les entreprises qui veulent un papier en règle, Hwaci, la société qui emploie les développeurs, vend aussi des garanties juridiques.

Du coup, même la Bibliothèque du Congrès américain range les fichiers SQLite parmi ses formats préférés pour conserver des jeux de données, à côté du CSV et du JSON.

[VISUEL : un tampon « format préféré » sur un fichier « .sqlite ». Texte : « Library of Congress, d'après sqlite.org (2018) ».]

Et les développeurs ont pris un engagement que presque personne ne prend : soutenir SQLite jusqu'en deux mille cinquante. Un fichier créé aujourd'hui doit encore pouvoir être lu et écrit par les versions futures.

[VISUEL : un fichier « .db » qui traverse une frise : 2000, 2026, 2050. Il ne change pas.]

Voilà ce que je trouve fou. En octobre deux mille vingt-six, on en est à la version trois point cinquante-quatre point un, et un fichier de ta toute première appli s'ouvrira encore dans vingt-quatre ans.

---

## 7. Fin (10:28 – 11:34)

[SON : la musique du début revient.]
[VISUEL : le téléphone du hook, rempli de fichiers « .db » ; cette fois, chacun porte une petite étiquette : messages, navigateur, photos, réglages.]

Bref, si je reprends : un serveur qui tombe sur un destroyer, un type au chômage technique pendant trois mois, un fichier à la place d'un serveur, et des tests qui font exprès de couper le courant. Voilà comment un logiciel sans serveur s'est retrouvé à peu près partout.

Et pour tes propres projets ? Voilà comment je le vois. [TON AVIS DE DEV : QUAND TU PRENDS SQLITE, QUAND TU PRENDS UN VRAI SERVEUR. UNE OU DEUX PHRASES.] La doc le dit elle-même : le mode WAL ne marche pas sur un système de fichiers en réseau.

Donc la prochaine fois que ton téléphone s'éteint en plein message, et que tout est encore là quand il se rallume, tu sauras qui remercier.

[VISUEL : le téléphone se rallume ; la conversation est intacte. Le nom « SQLite » s'écrit en petit en bas de l'écran, puis s'efface.]

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et WhatsApp, justement, celui qui range tes messages dans SQLite : comment une cinquantaine d'ingénieurs le faisaient tourner pour neuf cents millions de personnes, c'est dans cette vidéo, juste là.

[VISUEL : écran de fin, 20 s : vidéo WhatsApp (11 janv.) à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel | Le téléphone qui se remplit de fichiers « .db » |
| 0:11 | Chiffre | Plus de mille milliards de bases, dézoom sur la planète |
| 0:28 | Question centrale | « Alors comment un truc pareil s'est retrouvé à peu près partout ? » |
| 0:38 | Teaser | Le destroyer, l'écran qui s'éteint (refermé à 2:02) |
| 0:57 | Gamification | La liste façon « succès débloqués » |
| 1:15 | Vécu | Crochet : SQLite dans tes applis |
| 1:44 | Lien au quotidien | WhatsApp range tes messages dans un fichier SQLite |
| 1:55 | Podium | « 2. SQLite », juste après libz |
| 2:02 | Changement de décor | Le chantier naval la nuit |
| 2:50 | Humour gamer | La partie perdue parce que le serveur a lâché |
| 3:09 | Citation | « Richard, pourquoi tu n'en écris pas une toi-même ? » |
| 3:35 | Appel à l'action | Abonnement (~30 %) |
| 4:05 | Animation | Le serveur qui rentre dans le téléphone |
| 4:29 | Image | La sauvegarde sur la carte mémoire |
| 4:43 | Correction | « Trois cents kilo-octets, c'est faux aujourd'hui » |
| 5:02 | Humour | 281 To, « la tête de celui qui atteint la limite » |
| 5:44 | Révélation | « SQLite format 3 » écrit en clair |
| 6:08 | Analogie | Le dictionnaire, le B-arbre en trois sauts |
| 6:36 | Animation | Le WAL, le brouillon à côté |
| 7:04 | Coupure musique | Le téléphone qui s'éteint (60 %) |
| 7:18 | Teaser | « Un an, à soixante heures par semaine » |
| 7:52 | Humour gamer | La barre de vie du boss sur 52 semaines |
| 8:06 | Citation | « On a arrêté de recevoir des rapports de bugs d'Android » |
| 8:29 | Chiffre + réaction | 92 millions contre 156 000, « Ouais, t'as bien entendu » |
| 8:48 | Boucle refermée | Le téléphone éteint est dans les tests |
| 9:16 | Surprise | Le logiciel de vol de l'A350 |
| 9:40 | Son | Le tampon du domaine public |
| 10:13 | Frise | Le fichier qui traverse 2000-2050 |
| 10:41 | Boucle refermée | Le récap répond à la question du hook |
| 11:14 | Question du pilier | « Quelle appli je décortique ensuite ? », écran de fin vers WhatsApp |

**Total** : 30 relances en 11 min 35, environ une toutes les 23 secondes. Aucun trou de plus de 60 s. Ponts en fin de bloc : « d'où il sort ? » (1), « sans serveur, comment ça marche ? » (2), « qu'est-ce qu'il y a dedans ? » (3), « un an à soixante heures » (4), « le même logiciel vole au-dessus de ta tête » (5).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Section 1, la liste | Moyen | Une énumération de marques | Format « succès débloqués » avec un son, puis WhatsApp (ton quotidien) et le podium |
| Section 3, serveur contre bibliothèque | Élevé | Le cœur technique, abstrait pour les non-devs | Une seule animation (le serveur qui rentre dans le téléphone), rattachée au destroyer et au jeu en ligne déjà vus |
| Section 4, pages et B-arbre | Élevé | Le passage le plus « cours » | Le dictionnaire, trois sauts et trois clics ; aucune autre notion technique avant le WAL |
| Relance (~60 %) | Élevé | Chute classique | Coupure musicale, le téléphone qui s'éteint, puis le teaser des soixante heures |
| Section 5, les chiffres de tests | Moyen | Trois chiffres d'affilée | La tour qui sort du cadre, « Ouais, t'as bien entendu », puis la boucle refermée du téléphone |
| Section 6, la licence | Moyen | Sujet juridique, peu visuel | Le tampon, puis la frise jusqu'en 2050 ; la section dure à peine plus d'une minute |
| Fin | Moyen | Récapitulatif = signal de sortie | La phrase sur le téléphone qui se rallume arrive dans les 30 s |

## Notes de montage

- **Charte** : noire, celle du pilier génie. Le vert de WhatsApp sert seulement à la bulle de la section 1.
- **Composants réutilisés** : l'écran de fin et la bulle verte de WhatsApp ; la barre de vie du boss (WhatsApp, section 3). À construire : le téléphone qui se remplit de fichiers « .db » (hook, section 4, fin), la liste « succès débloqués », le serveur qui rentre dans le téléphone, le fichier découpé en pages et l'arbre, le WAL et son checkpoint, la tour des tests.
- **Pas de vraie appli WhatsApp, Android ou Airbus à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Captures autorisées : les pages de sqlite.org (mostdeployed, testing, footprint, lts), la transcription de CoRecursive.
- **Tes applis** : jamais de capture de tes applis de travail. Une maquette générique avec le logo Flutter.
- **Pas d'analogie du restaurant** (ByteMonk) : on utilise le serveur de jeu en ligne et la carte mémoire.
- **Mentions à l'écran** : « estimation de sqlite.org » sur le mille milliards, « mesures de 2023 » sur la taille, « chiffres de 2023 » sur les tests, « d'après des analyses forensiques » sur WhatsApp, « d'après Hipp » sur l'histoire du destroyer et les soixante heures, « d'après sqlite.org » sur Airbus et la Bibliothèque du Congrès.
- **Énergie** : montées sur le dézoom du hook, la liste des succès, le serveur qui tombe, la sauvegarde sur la carte mémoire, la coupure à 60 %, la barre de vie, la tour des tests, l'A350.
- **Fiche pendant le plateau de rétention** : une fiche vers la vidéo WhatsApp à 1:50 (« WhatsApp range tes messages dans un fichier SQLite »). L'écran de fin pointe aussi WhatsApp.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1, 32 | « il y a probablement des centaines de petites bases de données » ; « avec plus de quatre milliards de smartphones sur Terre, sqlite.org estime qu'il y a probablement plus de mille milliards de bases SQLite en service » |
| 26 | « ce logiciel n'a même pas de serveur » ; « une bibliothèque […] rien à configurer. La base, c'est un fichier » ; « la taille maximale d'une base SQLite, c'est deux cent quatre-vingt-un téraoctets » |
| 4 | « dans chaque appareil Android, chaque iPhone, chaque Mac, et chaque Windows dix et onze. Et dans Chrome, Firefox et Safari » ; « Skype, Dropbox, Python, la plupart des téléviseurs et des box, et même la plupart des systèmes multimédias des voitures » |
| 20 | « Google donne aux développeurs une boîte à outils toute prête […] la base est rangée dans le dossier privé de l'appli » |
| 22 ⚠️ | « D'après des analyses forensiques, sur Android, WhatsApp range tes messages dans un fichier SQLite » |
| 2 | « SQLite est probablement utilisé plus que tous les autres moteurs de bases de données réunis » |
| 3 ⚠️ | « pour eux, c'est la deuxième bibliothèque logicielle la plus déployée au monde, juste après libz » (jamais « la plus déployée de toutes ») |
| 14 | « sous-traitant pour Bath Iron Works » ; « un destroyer, le USS Oscar Austin » ; « contrôle des avaries […] isoler la partie touchée » ; « Informix […] ce serveur, de temps en temps, il tombe […] l'appli de Hipp ne marche plus » ; « Richard, pourquoi tu n'en écris pas une toi-même ? » |
| 15 | « D'après Hipp, à ce moment-là, les contrats publics sont gelés, et il se retrouve quelques mois sans travail » |
| 12, 13 | « Le projet SQLite démarre le neuf mai deux mille, et la version un point zéro sort le dix-sept août » |
| 5 | « moins d'un mégaoctet. En deux mille vingt-trois, sqlite.org mesurait entre cinq cent quatre-vingt-dix et sept cent cinquante kilo-octets » ; « "trois cents kilo-octets" […] c'est faux aujourd'hui » |
| 23 | « Dans un essai de deux mille dix-sept, sqlite.org mesurait environ trente-cinq pour cent de gagné » (dit comme un essai, pas une mesure générale) |
| 24 | « les cent premiers octets […] "SQLite format 3" » ; « découpé en pages, toutes de la même taille. Par défaut, quatre mille quatre-vingt-seize octets » ; « ces pages sont rangées en arbre » |
| 25 | « depuis deux mille dix, SQLite a un mode qui s'appelle le WAL » ; « il écrit les changements dans un fichier à côté […] il les reverse dans la base. Ça s'appelle un checkpoint » ; « ceux qui lisent ne bloquent plus celui qui écrit » ; « le mode WAL ne marche pas sur un système de fichiers en réseau » |
| 27 | « un an de semaines à soixante heures » ; « On a arrêté de recevoir des rapports de bugs d'Android » (Android seulement, pas Symbian) |
| 7 | « le cœur de SQLite est couvert à cent pour cent : chaque branche testée, et […] le MC/DC, à cent pour cent aussi » |
| 6 | « En deux mille vingt-trois, pour cent cinquante-six mille lignes de code, il y avait quatre-vingt-douze millions de lignes de tests. Cinq cent quatre-vingt-dix fois plus » |
| 8 | « plus de mémoire, erreurs de disque, et plantages en plein milieu d'une écriture, coupures de courant comprises » |
| 10 (formulation juste) | « des constructeurs d'avionique s'intéressent à SQLite. Du coup, les développeurs construisent une deuxième suite de tests, TH3, pensée pour les normes de l'aviation » ; « rien ne dit que SQLite est certifié pour les avions » |
| 9 | À l'écran : « TCL · 51 445 cas », « TH3 · 50 362 cas » |
| 11 | « d'après sqlite.org, Airbus confirme que SQLite tourne dans le logiciel de vol de l'A trois cent cinquante » |
| 16 | « Le code de SQLite est dans le domaine public » ; « Le projet n'accepte pas de correctif sans une déclaration écrite où tu verses ta contribution au domaine public » |
| 17 ⚠️ | « Hwaci, la société qui emploie les développeurs, vend aussi des garanties juridiques » (jamais « ces revenus financent SQLite ») |
| 18 | « la Bibliothèque du Congrès américain range les fichiers SQLite parmi ses formats préférés pour conserver des jeux de données, à côté du CSV et du JSON » ; à l'écran : « d'après sqlite.org (2018) » |
| 19 | « soutenir SQLite jusqu'en deux mille cinquante. Un fichier créé aujourd'hui doit encore pouvoir être lu et écrit par les versions futures » |
| 31 | « on en est à la version trois point cinquante-quatre point un » (à relever avant le tournage) |
| WhatsApp (`projets/whatsapp/script-v1.md`) | « comment une cinquantaine d'ingénieurs le faisaient tourner pour neuf cents millions de personnes » |

**Non utilisés exprès** : 28 (MySQL, PostgreSQL) et 29 (« deux ingénieurs », ni même « une petite équipe ») : ❓ ; 30 et 34 (« battu Oracle », DB-Engines) : ❌, voir la question 5 ; « General Dynamics » et « Symbian » ; « le composant le plus déployé de tous » (fait 3) ; la date de la page Bibliothèque du Congrès autre que 2018.

**Déductions et illustrations, à garder à l'œil au grill** :
- « Donc ta télé aussi, probablement » : déduit de « most television sets » (fait 4).
- « Trois mois » : du 9 mai au 17 août 2000 (faits 12 et 13).
- « un type s'ennuyait » : lecture de « quelques mois sans travail » (fait 15) ; à adoucir si tu la trouves injuste pour Hipp.
- « Personne d'autre n'y touche » : lecture de « your app's private folder » (fait 20).
- « dans vingt-quatre ans » : calcul de 2026 à 2050 (fait 19).
- Le jeu en ligne, la carte mémoire, le dictionnaire et le boss de Dark Souls : des illustrations, pas des faits.
- « Ça arrive sur des milliards d'appareils » : déduit des quatre milliards de smartphones (fait 1) ; aucune source ne compte les coupures.

## Questions pour l'auteur

1. **Ton vécu avec SQLite** (section 1) : tu l'as bien utilisé dans tes applis ? Pour stocker quoi, et avec quel paquet (sqflite, Drift, Room) ? Si tu n'as rien à dire, on garde seulement « je l'ai rangé dans mes propres applis », ou on coupe la phrase.
2. **Ton avis de dev** (fin) : quand tu prends SQLite, et quand tu prends un vrai serveur ? C'est la partie « ce que ça change pour toi » de la fiche ; je n'ai rien écrit à ta place, car `sources.md` ne tient que la limite du WAL en réseau.
3. **À sourcer** : la date des bugs d'Android qui ont lancé l'année de tests (section 5). CoRecursive la donne peut-être (~12:57 à 18:11) ; sinon on dit « à un moment ».
4. **Le sous-texte** : la fiche propose « le plus utilisé n'est pas le plus impressionnant, c'est celui qui a supprimé le problème et qui tient sa promesse ». Le script le porte par le destroyer et les tests, sans le dire en morale. C'est bien ce que tu veux dire, ou il y a autre chose ?
5. **« Battu Oracle »** : tu veux une minute « légende à corriger » (ByteMonk dit qu'il a battu Oracle ; chez DB-Engines, en octobre 2026, Oracle est 1er et SQLite 11e) ? La ligne est ❌ dans `sources.md`, donc je ne l'ai pas mise ; à valider avec la règle des faits.
6. **Les blagues** : la partie perdue en ligne, la carte mémoire, « la tête de celui qui atteint la limite », le boss de Dark Souls : lesquelles sont dans ton humour ?
7. **Le titre** (provisoire) :
   - *SQLite : la base de données qui est partout, et qui n'a pas de serveur* (recommandé par la fiche) ;
   - *Le logiciel le plus installé du monde n'a pas de serveur* (attention : « le plus installé » est plus fort que « 2e bibliothèque après libz » ; préférer « le plus installé de ton téléphone » ou garder « probablement ») ;
   - *SQLite : le fichier de moins d'1 Mo qui est dans ton téléphone*.
