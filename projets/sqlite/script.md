# SQLite : script v2 (version finale)

**Titre** (ton choix du 23/10) : *Sans cette base de données, ton téléphone ne marche pas*. La section 1 le tient : sur Android, tes contacts, tes SMS et ton historique d'appels sont des bases SQLite (fait 41). Variante B pour « Tester et comparer » : *SQLite : la base de données cachée dans ton téléphone* (recommandé au grill). Le titre de travail de `strategie.md` (« le fichier de 300 Ko qui a battu Oracle ») reste abandonné (faits 5, 30, 34).

**Durée** : 1 777 mots de voix off (`controle.py`, 23/10 au soir : 42 liaisons, soit 2,4 pour 100 mots, 0 « vous », hook de 88 mots avec la question centrale au 88e mot). À 145 mots/min (ton débit mesuré sur ArtCraft, pauses et improvisations comprises) : environ 12 min 15 ; à 165 mots/min : 10 min 46 ; en coupes serrées comme sur Uber (~180 mots/min) : 9 min 52, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise. Ton vécu et ton avis de dev (crochets) ajouteront 20 à 40 s.

**Fil rouge** : ton téléphone. Le hook y trouve des centaines de bases SQLite, plante l'Airbus et pose la question : comment un logiciel né d'un serveur en panne et d'un développeur sans contrat s'est retrouvé partout ? La vidéo répond en trois temps : le serveur supprimé (sections 2 et 3), le fichier qui tient le coup (section 4), la claque d'Android et l'année de tests (section 5). La fin revient au téléphone qui se rallume.

**Boucles ouvertes** :
1. « Comment un truc né comme ça s'est retrouvé à peu près partout ? » (hook, 0:30) : refermée par étapes (sections 3 et 5), puis dans la fin.
2. « Ce serveur en panne, c'est la clé de toute l'histoire » (pont, 0:35) : refermée dans les sections 2 et 3 (« le serveur qui tombait, il n'existe plus »).
3. L'Airbus du hook : récolté à la fin de la section 5.
4. « Ton téléphone s'éteint en plein message » (relance forte, fin de la section 4) : refermée dans la section 5 (les tests de coupure de courant), puis dans la fin.
5. « Tout commence quand Android lui donne tort » (teaser de la section 4) : refermé dans la section 5.

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **Section 5 réécrite sur la vraie chronologie**, vérifiée au grill (faits 35 et 36) : Hipp se vantait, « naïvement », que SQLite n'avait pas de bugs ; Android, sur des millions de téléphones, plante « sans arrêt » ; la norme de l'aviation (DO-178B, connue par Rockwell Collins) donne la méthode ; TH3 démarre le 25/09/2008 et atteint 100 % MC/DC le 25/07/2009. Le V1 disait « À un moment » et présentait l'aviation comme un chapitre d'après (« Mais l'histoire ne s'arrête pas aux téléphones »), alors que c'est le même chantier : TH3, 2008-2009.
- **« Je l'ai rangé dans mes propres applis » retiré** : c'était une anecdote inventée. Il reste un crochet à remplir, ou à couper.
- **Hook** : le mille milliards tombe vers 0:15 et l'Airbus monte dans le hook (≈ 0:20, et à l'image dès le dézoom) ; le contraste devient « un développeur sans contrat et un serveur qui plantait », au lieu de « n'a même pas de serveur », qui ne dit rien à un non-dev.
- **Surclassements corrigés** : « le truc le plus installé de ta vie » et « le logiciel le plus installé de ta poche » deviennent « un des logiciels les plus installés » (sqlite.org le classe 2e après libz, fait 3).
- **Skype retiré** de la liste : sqlite.org le cite encore, mais Microsoft l'a fermé le 5 mai 2025 (fait 38).
- **« Battu Oracle »** : une légende corrigée de deux phrases, accrochée à « trois cents kilo-octets » (section 3), pas une minute entière. À valider.
- **Liaisons à contresens retirées** : « Résultat, sqlite.org pense… » (après WhatsApp) et « Du coup, même la Bibliothèque du Congrès… » ne découlaient de rien.
- **Opinions et phrases empruntées** : « Voilà ce que je trouve fou » (avis prêté) et « Ouais, t'as bien entendu » (phrase de Cam, citée dans le skill) remplacés.
- **Abonnement avancé** à ~23 % (≈ 2:43 au lieu de 3:35), glissé dans la boucle ouverte : entre la question du collègue et la réponse de Hipp.
- **Coupés** : la boîte à outils d'Android, Hwaci, la version 3.54.1 et « dans vingt-quatre ans » (la vidéo sort en 2027). La taille de page par défaut devient « en général » (elle dépend de la plateforme, fait 24).
- **Une devinette** (axe 9) : « à ton avis, combien de lignes de tests ? » avant les 92 millions.
- WhatsApp : fin datée (« en deux mille quinze ») ; le fichier SQLite des messages est confirmé par une analyse de 2026 (fait 39).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (charte noire du pilier génie) ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de [`sources.md`](sources.md) (colonne « 2e vérif » et lignes ajoutées au grill), et des ⚠️ avec la formulation qu'il donne. Aucune capture de tes applis de travail : une maquette générique avec le logo Flutter suffit.

---

## 0. Hook (0:00 – 0:36) · objectif : 75 % à 0:15

[VISUEL : un téléphone en gros plan, écran noir. Des petites icônes de fichiers « .db » apparaissent une par une, puis par dizaines, jusqu'à remplir l'écran. Compteur en bas : « des centaines ». Pas de titre, pas de logo.]
[SON : un « tic » par fichier, qui s'accélère jusqu'à devenir un grésillement.]

Dans ton téléphone, là, il y a probablement des centaines de petites bases de données. Et toutes, c'est SQLite.

[VISUEL : dézoom : le téléphone devient un point au milieu de milliers d'autres, puis d'une planète entière de téléphones. Texte : « 4 000 000 000+ smartphones », puis « 1 000 000 000 000 de bases · estimation de sqlite.org ».]

Du coup, avec plus de quatre milliards de smartphones, sqlite.org estime qu'il y a probablement plus de mille milliards de bases SQLite en service. Et il tourne même dans le logiciel de vol de l'A trois cent cinquante.

[VISUEL : coupe nette : une silhouette d'A350 qui traverse l'écran, un petit fichier « .db » qui s'allume dans le cockpit. Texte : « d'après sqlite.org ».]

Sauf qu'au départ, c'est juste un développeur sans contrat et un serveur qui plantait, pour un destroyer. Alors comment un truc né comme ça s'est retrouvé à peu près partout ?

[VISUEL : retour sur le téléphone ; un seul fichier « .db » clignote au centre, avec un point d'interrogation.]

---

## 1. Partout, même là où tu ne regardes pas (0:36 – 1:39)

En fait, ce serveur en panne, c'est la clé de toute l'histoire. Mais avant, regarde à quel point SQLite s'est bien caché.

[VISUEL : teaser d'une seconde : la silhouette d'un destroyer dans la nuit, un écran d'ordinateur qui s'éteint à son bord. Arrêt sur image.]

D'après sqlite.org, il est dans chaque appareil Android, chaque iPhone, chaque Mac et chaque Windows dix et onze. Pareil dans Chrome, Firefox et Safari.

[VISUEL : la liste se remplit à l'écran, logo par logo, façon succès débloqués dans un jeu. Texte : « Source : sqlite.org, Most Widely Deployed ».]
[SON : un « ding » de succès débloqué à chaque ligne.]

Et sur Android, il ne fait pas de la figuration. Tes contacts, tes SMS, ton historique d'appels : chacun est rangé dans sa propre base SQLite. Donc sans lui, ton téléphone n'a plus ni contacts, ni SMS, ni historique d'appels.

[VISUEL : trois fichiers sortent du téléphone : « contacts2.db » (un répertoire), « mmssms.db » (une bulle), « calllog.db » (un combiné). Texte : « d'après le code source d'Android (AOSP) ».]

Et ça continue : Dropbox, Python, la plupart des téléviseurs et des box, et même la plupart des systèmes multimédias des voitures. Donc ta télé aussi, probablement.

[TON VÉCU, SI TU EN AS UN : TU AS DÉJÀ UTILISÉ SQLITE DANS TES APPLIS ? POUR STOCKER QUOI, ET CE QUE TU EN PENSAIS. DEUX PHRASES MAXIMUM. SINON, ON PASSE DIRECTEMENT À WHATSAPP.]

[VISUEL : si tu remplis le crochet, maquette générique d'une appli avec le logo Flutter, un petit fichier « .db » qui se range dedans. Aucune capture de tes vraies applis.]

Et WhatsApp, alors ? D'après des analyses forensiques, sur Android, WhatsApp range tes messages dans un fichier SQLite.

[VISUEL : une bulle de message verte qui glisse dans un fichier « msgstore.db ». Texte : « d'après des analyses forensiques ».]

Voilà pourquoi sqlite.org pense que SQLite est probablement utilisé plus que tous les autres moteurs de bases de données réunis. Et parmi tous les logiciels de ce genre, ils le classent deuxième, juste après libz, celle qui compresse les fichiers.

[VISUEL : un podium : « 1. libz », « 2. SQLite ». Texte : « bibliothèques les plus déployées, d'après sqlite.org ».]

Un des logiciels les plus installés de ta vie, et tu n'avais sans doute jamais vu son nom. Alors d'où il sort ?

---

## 2. Le destroyer et le serveur qui tombe (1:39 – 3:36)

[VISUEL : charte noire ; un chantier naval la nuit, un destroyer en construction. Texte : « ~2000 · Bath Iron Works ».]
[SON : bruit sourd de coque métallique, vent.]

On est vers l'an deux mille. D. Richard Hipp est sous-traitant pour Bath Iron Works, un chantier naval qui construit des navires pour l'US Navy. Lui, il écrit un logiciel pour un destroyer, l'USS Oscar Austin.

Pour faire simple, son logiciel sert au contrôle des avaries : si un tuyau casse à bord, il aide à isoler la partie touchée.

[VISUEL : coupe du bateau en schéma ; un tuyau rouge qui fuit, des vannes qui se ferment autour.]

Sauf que l'appli s'appuie sur une base de données, Informix, qui tourne sur un serveur. Et ce serveur, de temps en temps, il tombe. Du coup, l'appli de Hipp ne marche plus.

[VISUEL : le serveur s'éteint, l'écran de contrôle du bateau passe au gris. Texte : « Connexion perdue ».]
[SON : bip d'erreur, puis silence.]

Imagine : un logiciel fait pour gérer une avarie, qui s'arrête parce qu'une autre machine a planté. C'est comme perdre ta partie en ligne parce que le serveur du jeu a lâché, alors que toi, tu jouais bien.

[VISUEL : petit gag : un écran de jeu figé « Connexion au serveur perdue », la manette qui tombe des mains.]

Donc un collègue lui sort une phrase toute simple. Hipp la raconte dans le podcast CoRecursive : « Richard, pourquoi tu n'en écris pas une toi-même ? »

[VISUEL : bulle de dialogue en motion design. Texte : « d'après Hipp, CoRecursive #066 ».]

**Abonnement (≈ 2:43, ~23 % de la vidéo, dans la boucle ouverte : la question du collègue reste sans réponse le temps de l'appel)**

Et avant que je te dise ce qu'il a répondu : si tu aimes voir ce qui se cache derrière les applis de ta poche, abonne-toi. Sur Technovore, je les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, la bulle du collègue reste à l'écran.]

Bon, Hipp lui répond : « OK, je vais essayer. » Et le timing tombe bien, enfin, pour nous. D'après lui, à ce moment-là, les contrats publics sont gelés, et il se retrouve quelques mois sans travail. Donc il en profite. Le projet SQLite démarre le neuf mai deux mille, et la version un point zéro sort le dix-sept août.

[VISUEL : un calendrier : « 9 mai 2000 » s'entoure, puis les pages défilent jusqu'au « 17 août 2000 · v1.0 ».]

Trois mois. Un gouvernement met ses contrats en pause, un développeur se retrouve sans boulot, et il écrit le moteur qui finira dans mille milliards de bases.

Mais il reste la question de départ : sans serveur, comment ça marche ?

---

## 3. Pas de serveur (3:36 – 5:33)

[VISUEL : charte noire ; carte du chapitre « Pas de serveur ».]

Normalement, une base de données, c'est un programme qui tourne à part, sur une machine. Ton appli lui envoie une question, elle attend, et la réponse revient. C'est exactement ce qui tombait pour le destroyer.

[VISUEL : à gauche, un téléphone ; à droite, une grosse machine « serveur » ; une flèche aller, une flèche retour. Puis la machine s'éteint et la flèche reste en l'air.]

SQLite fait l'inverse. En gros, c'est une bibliothèque : un bout de code que l'appli embarque avec elle. Pas de programme à côté, rien à configurer. La base, c'est un fichier posé sur le disque, et l'appli le lit elle-même.

[VISUEL : la grosse machine rétrécit et rentre à l'intérieur du téléphone ; il ne reste qu'un fichier « .db ».]
[SON : « shlok » d'aspiration quand la machine rentre dans le téléphone.]

Tu te rappelles la partie en ligne de tout à l'heure ? SQLite, c'est la sauvegarde sur la carte mémoire. Personne ne peut la couper à ta place.

[VISUEL : une carte mémoire de console qui s'enfonce dans un téléphone.]

Voilà comment Hipp a réglé son problème : le serveur qui tombait, il n'existe plus.

Tout ça pèse moins d'un mégaoctet. En deux mille vingt-trois, sqlite.org mesurait entre cinq cent quatre-vingt-dix et sept cent cinquante kilo-octets, selon la machine. Donc si tu as vu passer « trois cents kilo-octets » quelque part, c'est faux aujourd'hui.

[VISUEL : une jauge « < 1 Mo », avec trois barres : « Raspberry Pi 4 · 590 Ko », « Ubuntu x64 · 650 Ko », « Mac M1 · 750 Ko ». Texte : « mesures de 2023 ». Le « 300 Ko » barré en rouge.]

[LÉGENDE ORACLE, À VALIDER : LES DEUX PHRASES SUIVANTES. SI TU N'EN VEUX PAS, COUPE-LES.]

Et si on t'a dit qu'il avait « battu Oracle » : chez DB-Engines, le classement de popularité, Oracle est premier et SQLite onzième, en octobre deux mille vingt-six. En fait, les deux font un boulot différent : Oracle, c'est un gros serveur, et SQLite, un fichier dans ton appli.

[VISUEL : le classement DB-Engines en motion design : « 1. Oracle », « … », « 11. SQLite ». Texte : « DB-Engines, oct. 2026 · popularité, pas installations ». Le « battu Oracle » barré.]

Normalement, là, tu te dis : un simple fichier, c'est petit et c'est lent. Sauf qu'une base SQLite peut monter jusqu'à deux cent quatre-vingt-un téraoctets. J'aimerais bien voir la tête de celui qui atteint la limite.

[VISUEL : un tout petit fichier qui gonfle jusqu'à remplir l'écran. Texte : « max : 281 To ».]

Et pour lire et écrire plein de petits morceaux de données, SQLite peut même aller plus vite que des fichiers séparés : environ trente-cinq pour cent, dans un essai de sqlite.org en deux mille dix-sept.

[VISUEL : deux couloirs de course : « 100 000 fichiers » contre « 1 fichier SQLite ». Texte : « ≈ 35 %, essai de 2017, chiffre approximatif ».]

Bon. Un fichier qui fait le boulot d'un serveur. Mais qu'est-ce qu'il y a dedans ?

---

## 4. Dans le fichier (5:33 – 7:20) · relance forte à ~58 %

[VISUEL : un fichier « .db » qui s'ouvre comme une boîte. Texte en police mono : « SQLite format 3 ».]

Si tu ouvres un fichier SQLite, les cent premiers octets, c'est sa carte d'identité. Dedans, c'est écrit en clair : « SQLite format 3 ».

Ensuite, le fichier est découpé en pages, toutes de la même taille : en général, quatre mille quatre-vingt-seize octets.

[VISUEL : le fichier se découpe en une pile de pages identiques, numérotées.]

Ces pages sont rangées en arbre. Pour faire simple, c'est comme chercher un mot dans le dictionnaire : tu ne lis pas tout depuis la lettre A. Tu ouvres au milieu, tu regardes si c'est avant ou après, et tu recommences.

[VISUEL : un arbre de pages ; un chemin s'allume de la racine jusqu'à une feuille en trois sauts. Texte : « B-arbre ».]
[SON : trois « clics » au rythme des sauts.]

Du coup, même dans une grosse base, SQLite retrouve une ligne en quelques sauts, sans tout parcourir.

Maintenant, imagine que deux choses se passent en même temps. Ton appli écrit un nouveau message, et au même moment, elle relit l'historique.

Pour ça, depuis deux mille dix, SQLite a un mode qui s'appelle le WAL. En fait, au lieu de toucher à la base, il écrit les changements dans un fichier à côté, comme un brouillon. Plus tard, il les reverse dans la base : ça s'appelle un checkpoint.

[VISUEL : à gauche, la base ; à droite, un fichier « -wal » qui se remplit de lignes. Une flèche « checkpoint » les reverse d'un coup dans la base.]

Résultat : ceux qui lisent ne bloquent plus celui qui écrit, et l'inverse non plus.

[VISUEL : deux personnages, un qui lit, un qui écrit, qui ne se marchent plus dessus.]

Sauf que tout ça repose sur un fichier, posé sur un disque. Et un téléphone, ça peut s'éteindre n'importe quand.

**Relance forte (≈ 6:55, ~58 % de la vidéo)**

[SON : la musique coupe net. Une seconde de silence.]
[VISUEL : le téléphone du hook ; la batterie passe à 1 %, puis l'écran s'éteint d'un coup.]

Ton téléphone qui s'éteint pile pendant que WhatsApp écrit ton message : pour une base de données, c'est le pire moment possible.

Et si SQLite tient le coup aujourd'hui, c'est parce qu'un type a passé un an, à soixante heures par semaine, à chasser ses propres bugs. Et tout commence le jour où Android lui donne tort.

---

## 5. Android lui donne tort (7:20 – 10:02)

[VISUEL : charte noire ; carte du chapitre « Android lui donne tort ».]

Hipp le raconte lui-même sur CoRecursive : à l'époque, ils allaient dire à tout le monde, je cite, « naïvement », que SQLite n'avait pas de bugs.

[VISUEL : un badge « 0 BUG » qui brille, un peu trop fier.]

Et là, d'un coup, SQLite se retrouve sur des millions de téléphones Android. Ça plante sans arrêt. Sa phrase, c'est : « Android nous a clairement donné tort. »

[VISUEL : le badge « 0 BUG » se fissure ; une pluie de notifications « crash » sur des téléphones Android génériques. Texte : « d'après Hipp, CoRecursive #066 ».]
[SON : verre qui se fêle, puis une rafale de notifications.]

Du coup, il ressort un truc qu'il venait de découvrir en bossant pour Rockwell Collins, un constructeur d'avionique : une norme de l'aviation, la DO-178B. Elle demande des tests qui passent par chaque embranchement du code, dans un sens et dans l'autre. Chaque « si », chaque « sinon ». Ça s'appelle le MC/DC, et elle en veut cent pour cent.

[VISUEL : un bout de code en C ; chaque « if » s'allume en vert quand un test passe dessus, d'abord côté « oui », puis côté « non ».]

D'après sqlite.org, des constructeurs d'avionique s'intéressaient justement à SQLite, et c'est pour suivre cette norme qu'ils montent une nouvelle suite de tests, TH3. La première ligne est écrite le vingt-cinq septembre deux mille huit.

[VISUEL : un calendrier : « 25 sept. 2008 · TH3 ». Texte : « d'après sqlite.org ».]

Hipp, lui, raconte des journées de douze heures, tous les jours. Un an de semaines à soixante heures. Un an de grind. Même un boss de Dark Souls ne te demande pas ça.

[VISUEL : une barre de vie de boss, « BUGS », qui descend pixel par pixel sur un calendrier de cinquante-deux semaines.]
[SON : coups d'épée en boucle, de plus en plus lents.]

Et en effet, le vingt-cinq juillet deux mille neuf, c'est bon : cent pour cent de MC/DC. À la fin, il dit une phrase que tout dev rêve de prononcer : « On a arrêté de recevoir des rapports de bugs d'Android. »

[VISUEL : la barre de vie tombe à zéro, « 25 juil. 2009 · 100 % MC/DC » ; une boîte de réception « Android » qui se vide. Texte : « d'après Hipp, CoRecursive #066 ».]

Mais attention : ce qui suit les règles de l'aviation, ce sont ses tests. Rien ne dit que SQLite lui-même est certifié pour voler.

Aujourd'hui encore, le cœur de SQLite est couvert à cent pour cent. Du coup, petite question : à ton avis, pour cent cinquante-six mille lignes de code, il faut combien de lignes de tests ? Garde ton chiffre en tête.

[VISUEL : la petite pile « code · 156 000 lignes » seule à l'écran, un « ? » à côté. Compte à rebours de 3 secondes.]

En deux mille vingt-trois, il y en avait quatre-vingt-douze millions. Cinq cent quatre-vingt-dix fois plus.

[VISUEL : une toute petite pile « code · 156 000 lignes » à côté d'une tour qui sort du cadre, « tests · 92 000 000 lignes ». Texte : « ×590 · chiffres de 2023 ».]

En gros, pour chaque ligne de code, presque six cents lignes rien que pour la surveiller. Chaque ligne a ses six cents gardes du corps.

Ces tests font exprès de casser le logiciel : plus de mémoire, erreurs de disque, plantages en plein milieu d'une écriture, coupures de courant comprises. Tu vois le téléphone qui s'éteint de tout à l'heure ? Il est dans les tests.

[VISUEL : retour sur le téléphone éteint ; il se rallume, le fichier « .db » est intact, coche verte.]

Et l'Airbus du début, tu t'en souviens ? D'après sqlite.org, Airbus confirme que SQLite tourne dans le logiciel de vol de l'A trois cent cinquante. Donc le même logiciel que dans ton téléphone vole au-dessus de ta tête.

[VISUEL : l'A350 du hook revient ; le petit fichier « .db » s'allume dans le cockpit. Texte : « d'après sqlite.org ».]

---

## 6. À tout le monde, jusqu'en 2050 (10:02 – 10:52)

[VISUEL : charte noire ; une feuille de licence vierge, sans signature.]

Ce logiciel, en fait, il n'appartient à personne. Le code de SQLite est dans le domaine public : n'importe qui peut le prendre.

Sauf que pour y contribuer, c'est l'inverse. Le projet n'accepte pas de correctif sans une déclaration écrite où tu verses ta contribution au domaine public.

[VISUEL : un formulaire « Je renonce à mes droits », avec un tampon.]
[SON : coup de tampon.]

Même la Bibliothèque du Congrès américain range les fichiers SQLite parmi ses formats préférés pour conserver des jeux de données, à côté du CSV et du JSON.

[VISUEL : un tampon « format préféré » sur un fichier « .sqlite ». Texte : « Library of Congress, d'après sqlite.org (2018) ».]

Les développeurs ont même pris un engagement : soutenir SQLite jusqu'en deux mille cinquante. Un fichier créé aujourd'hui doit encore pouvoir être lu et écrit par les versions futures.

[VISUEL : un fichier « .db » qui traverse une frise : 2000, 2027, 2050. Il ne change pas. Le téléphone, lui, finit dans une vitrine de musée.]

Deux mille cinquante, hein. Ton téléphone actuel sera dans un musée, et le fichier, lui, devra encore s'ouvrir.

---

## 7. Fin (10:52 – 11:58)

[SON : la musique du début revient.]
[VISUEL : le téléphone du hook, rempli de fichiers « .db » ; cette fois, chacun porte une petite étiquette : messages, navigateur, photos, réglages.]

Bref, voilà comment un logiciel né d'un serveur en panne s'est retrouvé à peu près partout. Hipp a supprimé le serveur, il a tout mis dans un fichier, et quand Android lui a donné tort, il a passé un an à tout tester.

Et pour tes propres projets ? Voilà comment je le vois. [TON AVIS DE DEV : QUAND TU PRENDS SQLITE, QUAND TU PRENDS UN VRAI SERVEUR. UNE OU DEUX PHRASES.] Et une limite que la doc donne elle-même : le mode WAL ne marche pas sur un système de fichiers en réseau.

Donc la prochaine fois que ton téléphone s'éteint en plein message, et que tout est encore là quand il se rallume, tu sauras qui remercier.

[VISUEL : le téléphone se rallume ; la conversation est intacte. Le nom « SQLite » s'écrit en petit en bas de l'écran, puis s'efface.]

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et WhatsApp, justement, celui qui range tes messages dans SQLite : comment, en deux mille quinze, une cinquantaine d'ingénieurs le faisaient tourner pour neuf cents millions de personnes, c'est dans cette vidéo, juste là.

[VISUEL : écran de fin, 20 s : vidéo WhatsApp (11 janv.) à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel | Le téléphone qui se remplit de fichiers « .db » |
| 0:15 | Chiffre | Plus de mille milliards de bases, dézoom sur la planète |
| 0:20 | Surprise (plantée) | L'A350 traverse l'écran |
| 0:30 | Contraste + question centrale | Un développeur sans contrat, un serveur qui plantait ; « comment un truc né comme ça… » |
| 0:38 | Pont + teaser | « Ce serveur en panne, c'est la clé de toute l'histoire », le destroyer dans la nuit |
| 0:50 | Gamification | La liste façon « succès débloqués » |
| 1:15 | Lien au quotidien | WhatsApp range tes messages dans un fichier SQLite |
| 1:30 | Podium | « 2. SQLite », juste après libz |
| 1:39 | Changement de décor | Le chantier naval la nuit |
| 2:20 | Humour gamer | La partie perdue parce que le serveur a lâché |
| 2:38 | Citation | « Richard, pourquoi tu n'en écris pas une toi-même ? » |
| 2:43 | Appel à l'action | Abonnement (~23 %), dans la boucle ouverte |
| 3:20 | Chute | « Trois mois », le moteur qui finira dans mille milliards de bases |
| 3:50 | Animation | Le serveur qui rentre dans le téléphone |
| 4:15 | Récolte | La sauvegarde sur la carte mémoire ; « le serveur qui tombait, il n'existe plus » |
| 4:35 | Correction | « Trois cents kilo-octets », puis « battu Oracle » (si gardé) |
| 5:05 | Mais / donc + humour | « Un simple fichier, c'est petit et lent » → 281 To |
| 5:45 | Révélation | « SQLite format 3 » écrit en clair |
| 6:05 | Analogie | Le dictionnaire, le B-arbre en trois sauts |
| 6:30 | Animation | Le WAL, le brouillon à côté |
| 6:55 | Coupure musique | Le téléphone qui s'éteint (~58 %) |
| 7:15 | Teaser | « Tout commence le jour où Android lui donne tort » |
| 7:30 | Crise | Le badge « 0 BUG » qui se fissure, « Android nous a clairement donné tort » |
| 8:00 | Mentor | La norme de l'aviation, le MC/DC |
| 8:40 | Humour gamer | La barre de vie du boss sur 52 semaines |
| 8:55 | Victoire + citation | 25 juillet 2009, « On a arrêté de recevoir des rapports de bugs d'Android » |
| 9:10 | Devinette | « À ton avis, combien de lignes de tests ? », compte à rebours |
| 9:20 | Chiffre + réaction | 92 millions contre 156 000, les six cents gardes du corps |
| 9:35 | Boucle refermée | Le téléphone éteint est dans les tests |
| 9:45 | Récolte | L'Airbus du début |
| 10:15 | Son | Le tampon du domaine public |
| 10:40 | Frise + humour | 2050, le téléphone au musée |
| 10:55 | Boucle refermée | Le bilan répond à la question du hook |
| 11:35 | Question du pilier | « Quelle appli je décortique ensuite ? », écran de fin vers WhatsApp |

**Total** : 34 relances en 11 min 58, environ une toutes les 21 secondes. Aucun trou de plus de 45 s. Ponts en fin de bloc : « d'où il sort ? » (1), « sans serveur, comment ça marche ? » (2), « qu'est-ce qu'il y a dedans ? » (3), « Android lui donne tort » (4), « le même logiciel vole au-dessus de ta tête » (5).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Section 1, la liste | Moyen | Une énumération de marques | Une minute à peine, format « succès débloqués » avec un son, puis WhatsApp (ton quotidien) et le podium |
| Section 3, serveur contre bibliothèque | Élevé | Le cœur technique, abstrait pour les non-devs | Une seule animation (le serveur qui rentre dans le téléphone), rattachée au destroyer et à la partie en ligne déjà vus, puis la récolte « le serveur qui tombait, il n'existe plus » |
| Section 3, la taille et Oracle | Moyen | Deux corrections d'affilée | Le « 300 Ko » et le « battu Oracle » barrés à l'écran, en 25 s ; coupe Oracle si tu trouves que ça traîne |
| Section 4, pages et B-arbre | Élevé | Le passage le plus « cours » | Le dictionnaire, trois sauts et trois clics ; aucune autre notion technique avant le WAL |
| Relance (~58 %) | Élevé | Chute classique | Coupure musicale, le téléphone qui s'éteint, puis le teaser d'Android |
| Section 5, MC/DC | Moyen | Un sigle barbare | « Chaque si, chaque sinon » et l'animation des « if » qui s'allument des deux côtés ; le sigle arrive après l'explication |
| Section 5, les chiffres de tests | Moyen | Trois chiffres d'affilée | La tour qui sort du cadre, les six cents gardes du corps, puis la boucle refermée du téléphone et l'Airbus |
| Section 6, la licence | Moyen | Sujet juridique, peu visuel | Le tampon, puis la frise jusqu'en 2050 ; la section dure moins d'une minute |
| Fin | Moyen | Bilan = signal de sortie | Deux phrases de bilan, puis ton avis de dev et le téléphone qui se rallume dans les 30 s |

## Notes de montage

- **Charte** : noire, celle du pilier génie. Le vert de WhatsApp sert seulement à la bulle de la section 1.
- **Composants réutilisés** : l'écran de fin et la bulle verte de WhatsApp ; la barre de vie du boss (WhatsApp, section 3). À construire : le téléphone qui se remplit de fichiers « .db » (hook, section 4, fin), la silhouette de l'A350 (hook et section 5), la liste « succès débloqués », le serveur qui rentre dans le téléphone, le fichier découpé en pages et l'arbre, le WAL et son checkpoint, le badge « 0 BUG » qui se fissure, les « if » qui s'allument, la tour des tests.
- **Pas de vraie appli WhatsApp, Android ou Airbus à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Les téléphones Android de la section 5 sont génériques, sans marque. Captures autorisées : les pages de sqlite.org (mostdeployed, testing, th3, footprint, lts), la transcription de CoRecursive.
- **Tes applis** : jamais de capture de tes applis de travail. Une maquette générique avec le logo Flutter, seulement si tu remplis le crochet de la section 1.
- **Pas d'analogie du restaurant** (ByteMonk) : on utilise la partie en ligne et la carte mémoire.
- **Mentions à l'écran** : « estimation de sqlite.org » sur le mille milliards, « d'après sqlite.org » sur l'A350 (hook et section 5) et la Bibliothèque du Congrès, « mesures de 2023 » sur la taille, « DB-Engines, oct. 2026 · popularité » sur Oracle, « chiffres de 2023 » sur les tests, « d'après des analyses forensiques » sur WhatsApp, « d'après Hipp, CoRecursive #066 » sur le destroyer, la vantardise, Android et les soixante heures, « d'après sqlite.org » sur les dates de TH3.
- **Énergie** : montées sur le dézoom du hook, la liste des succès, le serveur qui tombe, la sauvegarde sur la carte mémoire, la coupure à 58 %, le badge qui se fissure, la barre de vie, la tour des tests, l'A350.
- **Fiche pendant le plateau de rétention** : une fiche vers la vidéo WhatsApp à 1:20 (« WhatsApp range tes messages dans un fichier SQLite »). L'écran de fin pointe aussi WhatsApp.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1, 32 | « il y a probablement des centaines de petites bases de données » ; « avec plus de quatre milliards de smartphones, sqlite.org estime qu'il y a probablement plus de mille milliards de bases SQLite en service » |
| 11, 33 | « il tourne même dans le logiciel de vol de l'A trois cent cinquante » (hook, avec « d'après sqlite.org » à l'écran) ; « D'après sqlite.org, Airbus confirme que SQLite tourne dans le logiciel de vol de l'A trois cent cinquante » |
| 14, 15 | « un développeur sans contrat et un serveur qui plantait, pour un destroyer » (hook) |
| 4 | « dans chaque appareil Android, chaque iPhone, chaque Mac et chaque Windows dix et onze. Et dans Chrome, Firefox et Safari » ; « Dropbox, Python, la plupart des téléviseurs et des box, et même la plupart des systèmes multimédias des voitures » (Skype retiré, fait 38) |
| 22 ⚠️, 39 ⚠️ | « D'après des analyses forensiques, sur Android, WhatsApp range tes messages dans un fichier SQLite » |
| 2 | « SQLite est probablement utilisé plus que tous les autres moteurs de bases de données réunis » |
| 3 ⚠️ | « ils le classent deuxième, juste après libz, celle qui compresse les fichiers » ; « Un des logiciels les plus installés de ta vie » (jamais « le plus installé ») |
| 14 | « sous-traitant pour Bath Iron Works » ; « un destroyer, l'USS Oscar Austin » ; « contrôle des avaries […] isoler la partie touchée » ; « Informix […] ce serveur, de temps en temps, il tombe. Du coup, l'appli de Hipp ne marche plus » ; « Richard, pourquoi tu n'en écris pas une toi-même ? » ; « OK, je vais essayer » (« Okay, I'll give it a try. », fait 36) |
| 15 | « D'après lui, à ce moment-là, les contrats publics sont gelés, et il se retrouve quelques mois sans travail » |
| 12, 13 | « Le projet SQLite démarre le neuf mai deux mille, et la version un point zéro sort le dix-sept août » |
| 26 | « une bibliothèque […] rien à configurer. La base, c'est un fichier » ; « une base SQLite peut monter jusqu'à deux cent quatre-vingt-un téraoctets » |
| 5, 34 | « moins d'un mégaoctet. En deux mille vingt-trois, sqlite.org mesurait entre cinq cent quatre-vingt-dix et sept cent cinquante kilo-octets » ; « "trois cents kilo-octets" […] c'est faux aujourd'hui » |
| 30, 34 | « chez DB-Engines, le classement de popularité, Oracle est premier et SQLite onzième, en octobre deux mille vingt-six » (légende corrigée, à relire avant le tournage) |
| 23 | « environ trente-cinq pour cent, dans un essai de sqlite.org en deux mille dix-sept » |
| 24 | « les cent premiers octets […] "SQLite format 3" » ; « découpé en pages, toutes de la même taille : en général, quatre mille quatre-vingt-seize octets » ; « ces pages sont rangées en arbre » |
| 25 | « depuis deux mille dix, SQLite a un mode qui s'appelle le WAL » ; « il écrit les changements dans un fichier à côté […] il les reverse dans la base : ça s'appelle un checkpoint » ; « ceux qui lisent ne bloquent plus celui qui écrit » ; « le mode WAL ne marche pas sur un système de fichiers en réseau » |
| 36 | « ils allaient dire à tout le monde, je cite, "naïvement", que SQLite n'avait pas de bugs » ; « SQLite se retrouve sur des millions de téléphones Android. Et ça plante sans arrêt » ; « Android nous a clairement donné tort » ; « un truc qu'il venait de découvrir en bossant pour Rockwell Collins, un constructeur d'avionique : […] la DO-178B » ; « elle en veut cent pour cent » ; « des journées de douze heures, tous les jours » |
| 10 (formulation juste) | « des constructeurs d'avionique s'intéressaient justement à SQLite, et c'est pour suivre cette norme qu'ils montent une nouvelle suite de tests, TH3 » ; « ce qui suit les règles de l'aviation, ce sont ses tests. Rien ne dit que SQLite lui-même est certifié pour voler » |
| 35 | « La première ligne est écrite le vingt-cinq septembre deux mille huit » ; « le vingt-cinq juillet deux mille neuf, c'est bon : cent pour cent de MC/DC » |
| 27 | « Un an de semaines à soixante heures » ; « On a arrêté de recevoir des rapports de bugs d'Android » (Android seulement) |
| 7 | « Aujourd'hui encore, le cœur de SQLite est couvert à cent pour cent » |
| 6 | « pour cent cinquante-six mille lignes de code, il faut combien de lignes de tests ? » ; « En deux mille vingt-trois, il y en avait quatre-vingt-douze millions. Cinq cent quatre-vingt-dix fois plus » |
| 8 | « plus de mémoire, erreurs de disque, plantages en plein milieu d'une écriture, coupures de courant comprises » |
| 16 | « Le code de SQLite est dans le domaine public » ; « Le projet n'accepte pas de correctif sans une déclaration écrite où tu verses ta contribution au domaine public » |
| 18 | « la Bibliothèque du Congrès américain range les fichiers SQLite parmi ses formats préférés pour conserver des jeux de données, à côté du CSV et du JSON » ; à l'écran : « d'après sqlite.org (2018) » |
| 19 | « soutenir SQLite jusqu'en deux mille cinquante. Un fichier créé aujourd'hui doit encore pouvoir être lu et écrit par les versions futures » |
| WhatsApp (`projets/whatsapp/sources.md`, faits 1 et 2) | « comment, en deux mille quinze, une cinquantaine d'ingénieurs le faisaient tourner pour neuf cents millions de personnes » |

**Non utilisés exprès** : 9 (nombre de cas de test : à l'écran seulement si tu veux) ; 17 (Hwaci, coupé) ; 20 (la boîte à outils d'Android, coupée) ; 28 et 29 (MySQL, PostgreSQL, « deux ingénieurs ») : ❓ ; 31 (la version 3.54.1 : la vidéo sort en 2027) ; « General Dynamics » ; « le composant le plus déployé de tous » (fait 3) ; Skype (fait 38) ; Symbian (th3.html dit que TH3 est née d'un effort pour tester SQLite sur SymbianOS, mais le récit de Hipp parle d'Android : on garde Android).

**Déductions et illustrations, à garder à l'œil** :
- « Donc ta télé aussi, probablement » : déduit de « most television sets » (fait 4).
- « Trois mois » : du 9 mai au 17 août 2000 (faits 12 et 13).
- « Un développeur sans contrat » : lecture de « out of work for a few months » pendant le gel des contrats (fait 15).
- « Le moteur qui finira dans mille milliards de bases » : la v1.0 de 2000 n'est pas la version d'aujourd'hui, c'est le même projet (faits 1, 12).
- « Dans un sens et dans l'autre » : la définition de Hipp (« to be taken and to fall through at least once », fait 36), qui décrit les branches ; le MC/DC demande aussi que chaque condition joue seule sur la décision. Le script simplifie.
- « Un an » (Hipp) et « dix mois » (sqlite.org, du 25/09/2008 au 25/07/2009) : on dit les deux sources sans les mélanger.
- « Six cents gardes du corps », le dictionnaire, la partie en ligne, la carte mémoire, le boss de Dark Souls, le téléphone au musée : des illustrations, pas des faits.
- « Pour une base de données, c'est le pire moment possible » : un avis, pas un fait mesuré ; « ça arrive sur des milliards d'appareils » (V1) est retiré.

## Questions pour l'auteur

1. **Ton vécu avec SQLite** (section 1) : tu l'as déjà utilisé dans tes applis ? Pour stocker quoi, avec quel paquet (sqflite, Drift, Room) ? Le V1 te faisait dire « je l'ai rangé dans mes propres applis » : rien ne le dit, donc c'est un crochet. Si tu n'as rien, coupe-le.
2. **Ton avis de dev** (fin) : quand tu prends SQLite, et quand tu prends un vrai serveur ? Une ou deux phrases à toi.
3. **« Battu Oracle »** (section 3) : je l'ai mis en légende corrigée de deux phrases (25 s), accrochée au « 300 Ko ». Tu le gardes, ou tu coupes ? Si tu le gardes, relis le classement DB-Engines avant le tournage.
4. **Les blagues** : la partie perdue en ligne, la carte mémoire, « la tête de celui qui atteint la limite », le boss de Dark Souls, les six cents gardes du corps, le téléphone au musée. Lesquelles sont dans ton humour ? Remplace les autres par les tiennes.
5. **Le sous-texte** : la fiche propose « le plus utilisé, c'est celui qui a supprimé le problème et qui tient sa promesse ». La section 5 en ajoute un, sourcé : on ne devient fiable qu'après avoir eu tort (la vantardise, puis la claque d'Android). Le script les porte par le destroyer, Android et 2050, sans le dire en morale. Lequel est le tien, ou c'est autre chose ?
6. **Le titre** : tranché le 23/10 (*Sans cette base de données, ton téléphone ne marche pas*), tenu par la section 1 (fait 41). La variante B sert au test A/B.
7. **Avant le tournage** : relève la version de SQLite, la page testing.html (ses chiffres datent de 2023) et le classement DB-Engines.
