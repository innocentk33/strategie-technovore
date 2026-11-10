# iPhone fluide : script final

**Titre** : *Pourquoi tout paraît plus fluide sur un iPhone*

**Durée** : 1 760 mots de voix off (contrôle du 23/10, contre 1 819 dans la V1). À ton débit mesuré sur ArtCraft (145 mots/min, pauses et improvisations comprises) : environ 12 min 10. Avec des coupes serrées (175 à 180 mots/min, comme Uber) : environ 9 min 55, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : le battement de l'écran. Toutes les seize millisecondes, « toc », une nouvelle image doit être prête : faire défiler une page, c'est un jeu de rythme, et une image en retard, c'est un « MISS » de Guitar Hero. On suit qui tient ce rythme sur iPhone (les calques, le serveur de rendu, le doigt deviné), puis comment Android l'a appris en trois marches (3.0, 2012, 2014), jusqu'au téléphone Android du spectateur aujourd'hui. Le métronome revient à chaque chapitre ; le « MISS » revient dans la section 4 et dans Perfetto ; le FPS de la section 2 revient côté Android dans la section 4.

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **Faits corrigés** :
  - l'iPad Air 2 n'est pas sorti « cette année-là » (2015) mais le 16 octobre 2014 : la phrase est coupée ;
  - « Android a ouvert le bal » des 120 Hz devient « sur les téléphones » : l'iPad Pro d'Apple passe à 120 Hz dès juin 2017 ;
  - le Razer Phone n'est plus dit « premier » : le Sharp Aquos R Compact, un Android lui aussi, était en vente avant ;
  - le DJ ne promet plus que l'animation continue « pendant un gros calcul » : on garde la phrase de Google (« même quand le fil principal a du retard ») ;
  - « l'étudiant finit par corriger son post » devient « mettre son post à jour » (le mot des sources) ;
  - « trois ans avant qu'Apple l'ouvre aux développeurs » devient « côté iPhone, la prédiction n'arrive dans la doc des développeurs qu'avec iOS 9 ».
- **Faits ajoutés et sourcés** (faits 32 à 37 de `sources.md`) : Jay Freeman est le créateur de Cydia ; Dianne Hackborn rejette elle aussi la priorité temps réel ; la doc d'Android parle encore aujourd'hui du Choreographer et du RenderThread, et dit qu'une appli saccade souvent parce que son fil principal est bloqué ; Core Animation ne redessine pas un calque qui bouge.
- **Coupes** : les deux proposées par le rédacteur (la phrase sur Android 4.0, le troisième tampon d'image), plus l'iPad Air 2, la phrase sur Android 11 et `setFrameRate()`, et quelques redites (« l'explication est simple », « et ça répond à la question du début »).
- **Promesse du titre** : le titre dit « paraît », au présent. La section 6 répond maintenant au présent : pourquoi un Android peut encore saccader en 2026 (la doc de Google, puis ton avis).
- **Guitar Hero devient un vrai fil** : le « MISS » revient avec l'orchestre (section 4) et avec Perfetto (section 6).
- **Hook** : « Tu vois ? » et « sans jamais rater le temps » resserrés pour que le contraste 2007 → 2012 tombe à 13 s ; le pont finit sur un « et pourtant », pour ne pas répéter le « sauf que » de la deuxième phrase.
- **Abonnement** avancé de 3:31 (28 %) à 2:50 (23 %), juste avant le « sauf que » du serveur de rendu.
- **Tics** : « une phrase qui dit tout », la rafale « simple, elle fait plaisir, et… », « Et aucune priorité magique. Juste… », le « Du coup » sans conséquence, et les phrases qui commençaient par « Et » (27 dans la V1, 14 ici).
- **Ton vécu** : la question Flutter est recentrée (un gel du fil principal), et le logo Flutter n'illustre plus le RenderThread d'Android, qui n'a rien à voir avec Flutter.

**Boucles ouvertes** :
1. « Qu'est-ce que l'iPhone avait compris, et qu'Android a mis des années à rattraper ? » (hook, refermée dans la section 5).
2. « Fin 2011, un ancien stagiaire d'Android croit avoir trouvé… des ingénieurs la démontent » (hook, refermée dans la section 3).
3. « Garde ce FPS en tête » (section 2, refermée dans la section 4).
4. « Et ton téléphone à toi ? » (implicite dès le hook, refermée dans la section 6).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = motion design (HyperFrames ou Remotion). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture, sauf les années. Aucune vraie interface d'appli : tout est reconstruit en motion design.

---

## 0. Hook (0:00 – 0:35) · objectif : 75 % à 0:15

[VISUEL : gros plan d'un doigt qui fait défiler une liste sur un iPhone. Pas de titre, pas de logo. La liste suit le doigt au pixel près.]

Pose ton doigt sur l'écran et fais défiler. La page colle à ton doigt.

[SON : un « toc » sourd et régulier démarre, comme un métronome.]

Sauf que pour ça, ton téléphone doit sortir une nouvelle image toutes les seize millisecondes, sans en rater une.

[VISUEL : arrêt sur image ; sous le doigt, une ligne du temps coupée en cases de 16 ms, une case s'allume à chaque « toc ».]

L'iPhone sort en 2007. Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran.

[VISUEL : deux dates, « 29 juin 2007 » et « 2012 », une flèche entre elles.]

Alors qu'est-ce que l'iPhone avait compris, et qu'Android a mis des années à rattraper ?

Fin 2011, un ancien stagiaire d'Android croit avoir trouvé. La presse tech reprend sa réponse. Et pourtant, des ingénieurs la démontent.

[VISUEL : un post de blog générique (pas la vraie page) qui se couvre de tampons « PARTAGÉ », puis d'un tampon rouge « FAUX ? ».]

---

## 1. Le cœur de ton écran (0:35 – 2:01)

[SON : le métronome continue, un peu plus présent.]

Pour comprendre, il faut écouter ton écran. Un écran classique se rafraîchit soixante fois par seconde. Donc toutes les seize virgule six sept millisecondes, toc, il affiche une nouvelle image. Et sur un écran à cent vingt hertz, c'est toutes les huit virgule trois trois.

[VISUEL : compteur « 16,67 ms », puis « 8,33 ms » ; la ligne du temps se resserre de moitié.]

En fait, faire défiler une page, c'est un jeu de rythme. Comme dans Guitar Hero : la note descend, et tu dois taper pile sur le temps. Ici, la note, c'est l'image. Si elle est prête à temps, la page avance avec ton doigt. Mais si elle arrive en retard, l'écran garde l'ancienne image, et la page saute pour rattraper.

[VISUEL : piste de jeu de rythme ; des images de la liste tombent sur la ligne ; une arrive après, « MISS » en rouge, la liste fait un petit saut.]
[SON : le « clonk » d'une note ratée.]

Chez Apple, ce raté a un nom : un hitch. Une image qui arrive à l'écran plus tard que prévu. Apple a même fait un barème. Moins de cinq millisecondes de retard par seconde, c'est presque invisible. Entre cinq et dix, tu commences à sentir des accrocs. Au-delà de dix, pour Apple, c'est grave.

[VISUEL : jauge verte, orange, rouge : « < 5 ms/s », « 5-10 », « > 10 ». En petit : « Apple, Tech Talk 2020 ».]

Cinq millisecondes sur toute une seconde. Ouais, ils sont exigeants. Du coup, être fluide, ça revient à tenir le rythme, image après image, tant que ton doigt bouge.

Normalement, tu te dis que c'est ton appli qui redessine la page à chaque image. Sur iPhone, c'est plus malin que ça.

---

## 2. Ce que l'iPhone fait de ton doigt (2:01 – 4:29)

[VISUEL : un iPhone qui s'éclate en couches, vu de profil, comme un mille-feuille.]

En fait, dès le premier iPhone, l'interface est faite de calques assemblés par la puce graphique. C'est Nick Lockwood qui le raconte, l'auteur d'un livre sur Core Animation. Et la doc d'Apple le dit encore aujourd'hui : sur iOS, chaque élément de l'écran repose sur un calque.

Si tu as déjà ouvert Photoshop, tu vois le principe. Ta liste de messages, c'est une feuille. La barre du haut, c'en est une autre.

Core Animation, le moteur d'animation d'Apple, garde le contenu de ces calques en mémoire, sous forme d'images, et c'est le matériel graphique qui les manipule directement. Donc quand tu fais défiler, l'iPhone peut se contenter de faire glisser la feuille, sans redessiner ta liste à chaque image.

[VISUEL : la liste de messages glisse comme une feuille de papier sur une table ; seul le cadre bouge.]

**Abonnement (≈ 2:50, 23 % de la vidéo, juste après la feuille qui glisse ; le « sauf que » du serveur de rendu sert de relance juste derrière)**

Si tu aimes voir ce qui tourne sous le capot des applis que tu utilises tous les jours, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; le métronome reste à l'écran.]

Sauf que le dessin final, sur iPhone, ne se fait même pas dans ton appli. Apple l'explique dans une conférence pour développeurs de 2020 : chaque image suit une boucle en cinq temps, calée sur le battement de l'écran. L'appli reçoit ton toucher et met à jour son interface. Puis elle envoie tout ça à un processus à part, le serveur de rendu, et c'est lui qui prépare et dessine l'image.

[VISUEL : la ligne du temps de 16,67 ms coupée en cinq cases : Événement, Commit, Préparation, Exécution, Affichage. Les deux premières dans une boîte « Ton appli », les deux suivantes dans une boîte « Serveur de rendu ».]

En gros, ton appli écrit la partition, et c'est un autre musicien qui la joue en rythme.

Pendant ce temps, iOS s'occupe de ton doigt. Parce que quand tu poses le doigt sur une liste, il ne sait pas encore ce que tu veux : faire défiler, ou ouvrir un message. Du coup, il lance un petit minuteur. Si ton doigt bouge avant la fin, c'est un défilement, et il annule le toucher sur le message.

[VISUEL : le doigt se pose sur un message ; un petit chrono circulaire apparaît ; le doigt glisse, le surlignage du message s'éteint, la liste part.]

Depuis iOS 9, en 2015, l'iPhone va plus loin : il prédit où sera ton doigt. C'est ce que tu fais dans un FPS quand tu vises devant un ennemi qui court. Garde ce FPS en tête, on va le recroiser côté Android.

[VISUEL : un doigt fantôme, translucide, légèrement en avance sur le vrai ; un réticule de visée façon FPS sur sa trajectoire.]

Voilà pour l'iPhone. Maintenant, retour fin 2011, côté Android. À l'époque, la presse tech se pose une question : pourquoi les animations d'Android traînent derrière celles de l'iPhone ?

---

## 3. La légende du temps réel (4:29 – 6:16)

[SON : la musique passe en mode enquête, une basse qui tient.]

Tu te rappelles le stagiaire du début ? D'après la presse de l'époque, c'est un étudiant. Fin 2011, il publie un long post avec son explication : sur iOS, l'interface serait dessinée dans un fil à part, avec une priorité temps réel. En gros, dès que ton doigt touche l'écran, l'interface passerait devant tout le reste, comme une ambulance sur l'autoroute.

[VISUEL : une ambulance marquée « Interface » double toutes les voitures marquées « tâches ». Un tampon « LÉGENDE » tombe dessus.]

Sauf que des ingénieurs la démontent vite. Bob Lee, ancien responsable des bibliothèques d'Android, parle d'erreurs de raisonnement. Jay Freeman, le créateur de Cydia, l'appli des iPhone jailbreakés, dit que c'est tout simplement faux. Résultat, l'étudiant finit par mettre son post à jour.

[VISUEL : deux bulles de citation sans photo : « erreurs de raisonnement » (Bob Lee), « tout simplement faux » (Jay Freeman). Le post générique se couvre d'un bandeau « MIS À JOUR ».]

De notre côté, dans la doc d'Apple qu'on a lue, aucune page ne parle de priorité temps réel. Donc il faut chercher ailleurs.

Côté Google, une ingénieure d'Android, Dianne Hackborn, rejette elle aussi cette idée. Et elle avait déjà remis les pendules à l'heure sur un autre point. On pourrait croire qu'Android, à l'époque, n'utilisait pas la puce graphique. En fait, d'après elle, Android assemble les fenêtres à l'écran avec le matériel graphique depuis avant la version 1.0.

Ce qui lui manquait, c'était le contenu des fenêtres : les boutons, les listes. Tu te rappelles la feuille qui glisse sur l'iPhone ? Côté Android, ce contenu-là, la puce graphique ne s'en charge qu'à partir d'Android 3.0.

[VISUEL : une fenêtre Android générique ; le cadre s'allume en vert « GPU, avant 1.0 », le contenu reste gris, puis s'allume avec « 3.0 ».]

Elle prévient quand même : la puce graphique n'est pas une solution miracle pour une interface fluide.

Mais alors, si la puissance ne suffit pas, il manquait quoi ? La réponse arrive quelques mois plus tard, avec un jeu de mots.

---

## 4. 2012 : tout Android sur le même temps (6:16 – 8:51) · relance forte à 60 %

[VISUEL : un orchestre en 2D où chaque musicien joue à son propre tempo.]
[SON : cacophonie, chaque instrument décalé.]

Avant Android 4.1, les animations et les dessins d'Android n'étaient pas calés sur le battement de l'écran. Imagine un orchestre où chaque musicien joue quand il veut, sans regarder le chef. Chaque musicien peut être très bon, et pourtant le morceau sonne faux. Et dans notre Guitar Hero, sans battement commun, rien ne garantit que l'image tombe sur le temps. Bonjour les « MISS ».

[VISUEL : la piste de jeu de rythme revient, sans ligne de temps commune ; les « MISS » s'enchaînent.]

Fin juin 2012, à la conférence Google I/O, deux ingénieurs de Google, Chet Haase et Romain Guy, montent sur scène. Leur conférence s'appelle « For Butter or Worse ». Pour le beurre ou pour le pire. Oui, chez Google aussi, on aime les jeux de mots. Et ce chantier, la presse l'appelle Project Butter, le projet Beurre : l'idée, c'est une interface qui glisse comme du beurre.

[VISUEL : une diapo reconstituée avec le titre de la conférence ; une plaquette de beurre glisse dans une poêle.]

**Relance forte (≈ 7:08, 59 % de la vidéo)** : la cacophonie s'arrête net, une seconde de silence, puis un seul « toc ». C'est la réponse au « il manquait quoi ? » de 6:06.

[SON : silence, puis le métronome, seul.]

Résultat, avec Android 4.1, Jelly Bean, tout le système avance au même pas, sur un battement de seize millisecondes : le dessin des applis, le toucher, l'assemblage de l'écran et son rafraîchissement. Le mot « battement », c'est Google qui l'emploie. Un battement de cœur.

[VISUEL : l'orchestre se cale ; tous les musiciens jouent sur le même « toc ». Citation à l'écran : « a 16 millisecond vsync heartbeat », Google.]
[SON : la cacophonie se range sur le métronome.]

Pour donner le tempo aux applis, Google crée une nouvelle pièce : Choreographer. Le chorégraphe. Concrètement, c'est lui qui prévient au moment du battement, et Android fait passer ses animations et ses redessins par lui. Cinq, six, sept, huit.

Android 4.1 s'occupe aussi de ton doigt. D'abord, le toucher est calé lui aussi sur le battement. Ensuite, Android essaie de deviner où sera ton doigt au prochain rafraîchissement. Oui, la visée en avance du FPS ! Sauf que là, on est en 2012 : côté iPhone, cette prédiction n'arrive dans la doc des développeurs qu'avec iOS 9, trois ans plus tard.

[VISUEL : le réticule FPS de la section 2 revient, cette fois sur un Android générique ; frise « Android 4.1, 2012 » puis « iOS 9, 2015 ».]

Dernier truc : quand tu touches l'écran après une pause, le système donne un coup d'accélérateur au processeur. Et en effet, ce coup d'accélérateur, on le retrouve dans le code d'Android. Une modif du 3 mai 2012, pour le Galaxy Nexus, qui s'intitule « Boost pulse CPU speeds » : une impulsion de vitesse dès que tu interagis. Ton processeur somnolait, et il se réveille d'un coup, comme toi au fond de la classe quand le prof dit ton prénom.

[VISUEL : la modif dans le code source public d'Android, date « 3 mai 2012 » surlignée ; un processeur en 2D qui se réveille en sursaut.]

Bref, en 2012, Android tient enfin le rythme. Sauf qu'il reste un trou. Quand l'appli elle-même prend du retard sur son fil principal, les animations trinquent avec elle.

[SON : la musique coupe net, une seconde de silence.]

---

## 5. 2014 : le DJ qui ne coupe jamais le son (8:51 – 9:48)

[VISUEL : un DJ en 2D ; la platine tourne pendant qu'il fouille dans ses disques.]
[SON : le métronome reprend, sous un beat.]

Fin 2014, Android 5.0, Lollipop, ajoute un fil géré par le système : le RenderThread, le fil de rendu. D'après Google, il garde les animations fluides même quand le fil principal de l'appli a du retard.

Tu vois le DJ en soirée ? Pendant qu'il cherche le prochain disque, il laisse tourner le morceau. Là, c'est pareil : l'appli prend du retard, et le fil de rendu continue de faire tourner l'animation sur le battement.

[VISUEL : maquette générique d'une appli (sans logo) ; une animation qui continue de tourner pendant qu'une barre « fil principal : en retard » clignote.]

Et là, je te parle en dev. [TON VÉCU DE DEV, SI TU EN AS UN : UNE INTERFACE QUI A GELÉ PARCE QUE TU FAISAIS UN GROS CALCUL SUR LE FIL PRINCIPAL, ET CE QUE TU AS FAIT. SINON, SUPPRIME CETTE PHRASE.]

Voilà comment Android a rattrapé son retard.

[VISUEL : un escalier à trois marches qui monte vers le métronome (pas vers un iPhone : on ne fait pas de podium) : « 3.0 : la puce graphique pour le contenu », « 2012 : le battement commun », « 2014 : le fil de rendu ».]

L'iPhone, d'après Lockwood, est parti avec ses calques sur la puce graphique dès le premier modèle. Android, lui, a monté ces trois marches une par une. Et la priorité temps réel du stagiaire ? Elle n'apparaît nulle part dans cette histoire. Aujourd'hui, les deux systèmes se calent sur le battement de l'écran.

---

## 6. Ton Android aujourd'hui (9:48 – 12:08)

Et ton téléphone à toi ? Si tu regardes depuis l'Afrique, il y a de bonnes chances que ce soit un Android : d'après StatCounter, en septembre 2026, environ huit téléphones sur dix qui vont sur le web en Afrique sont des Android. Et parmi les smartphones vendus en Afrique en 2025, environ la moitié sont des Tecno, des Infinix ou des itel, d'après Canalys et Omdia.

[VISUEL : carte de l'Afrique qui se remplit de petits téléphones verts ; « 83 % du trafic web mobile (StatCounter, sept. 2026) ».]

Forcément, un téléphone de 2025 tourne sur un Android bien plus récent que la version 5.0. Donc il a hérité du battement de 2012 et du fil de rendu de 2014 : la doc d'Android parle encore aujourd'hui du chorégraphe et du RenderThread.

Pour les écrans, sur les téléphones, c'est même Android qui ouvre le bal. En novembre 2017, Razer présente le Razer Phone, un Android avec un écran à cent vingt hertz. L'iPhone, lui, y passe en septembre 2021, avec l'iPhone 13 Pro. Quatre ans plus tard. Pour une fois, c'est l'iPhone qui arrive après.

[VISUEL : frise : « Razer Phone, nov. 2017 » puis « iPhone 13 Pro, sept. 2021 » ; la ligne du temps passe de 16,67 à 8,33 ms.]

En fait, aujourd'hui, Google le dit lui-même : beaucoup de téléphones Android ont des écrans à quatre-vingt-dix ou cent vingt hertz.

Alors pourquoi un Android peut encore saccader en 2026 ? Google donne une piste dans sa propre doc : souvent, l'image saute parce que le fil principal de l'appli est bloqué. Le DJ peut faire durer le morceau, mais à un moment, il faut bien changer de disque.

[TON AVIS DE DEV : AU-DELÀ DU FIL PRINCIPAL BLOQUÉ, D'OÙ ÇA VIENT SELON TOI ? L'APPLI, LA PUCE, LA SURCOUCHE DU FABRICANT ? UNE OU DEUX PHRASES, DITES COMME UN AVIS, SANS CHIFFRE.]

Et si tu es dev, Google te donne même de quoi voir ton appli rater le temps : Perfetto, un outil de traçage, intégré depuis Android 10. En gros, c'est ton « MISS » de Guitar Hero, en vrai.

[VISUEL : une trace Perfetto stylisée (reconstituée), une image en rouge qui dépasse son créneau de 16 ms ; le « MISS » de la section 1 apparaît dessus.]

Bref, la prochaine fois que la page colle à ton doigt, sur un iPhone ou sur ton Android, tu sauras qu'il y a un battement derrière. Seize millisecondes. Toc.

[SON : un dernier « toc », puis silence.]

Sur Technovore, j'ouvre comme ça les applis et les systèmes que tu as dans la poche. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et la vidéo juste là, c'est Waze : comment il sait qu'il y a un bouchon devant toi.

[VISUEL : écran de fin, 20 s : vidéo Waze à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Geste banal | Le doigt fait défiler, la page colle (l'image de la miniature) |
| 0:05 | Chiffre | Une image toutes les seize millisecondes, le métronome démarre |
| 0:13 | Contraste daté | 2007 contre 2012 |
| 0:21 | Question centrale | « Qu'est-ce que l'iPhone avait compris ? » |
| 0:26 | Boucle ouverte | Le stagiaire de 2011 et sa réponse démontée (refermée à 4:29-5:05) |
| 0:54 | Référence gamer | Faire défiler = un jeu de rythme, Guitar Hero |
| 1:08 | Visuel + son | « MISS » et la note ratée |
| 1:18 | Chiffre | Le barème d'Apple : 5 et 10 ms par seconde |
| 2:01 | Visuel | L'iPhone qui s'éclate en calques |
| 2:50 | Appel à l'action | Abonnement (23 %) |
| 3:01 | Surprise | Le dessin final ne se fait pas dans ton appli |
| 3:37 | Devinette implicite | Défiler ou ouvrir le message ? Le minuteur caché |
| 4:01 | Référence gamer + boucle | Prédire le doigt = viser devant l'ennemi dans un FPS ; « garde ce FPS en tête » |
| 4:29 | Changement de ton | Musique d'enquête, la légende du temps réel |
| 4:50 | Visuel + humour | L'ambulance « Interface » et le tampon « LÉGENDE » |
| 4:54 | Retournement | Les ingénieurs démontent, jusqu'au créateur de Cydia |
| 5:21 | Retournement | Hackborn : Android avait la puce graphique depuis avant la 1.0 |
| 6:06 | Question | « Il manquait quoi ? » + teaser du jeu de mots |
| 6:16 | Son + récolte | Cacophonie de l'orchestre, les « MISS » de Guitar Hero |
| 6:42 | Humour | « For Butter or Worse », le projet Beurre |
| 7:08 | Relance forte (59 %) | Silence, puis le métronome seul : tout Android sur le même battement |
| 7:27 | Humour | Le chorégraphe, « cinq, six, sept, huit » |
| 7:55 | Récolte + retournement | Le FPS revient : Android prédit le doigt dès 2012, trois ans avant la doc d'iOS 9 |
| 8:20 | Preuve à l'écran | La modif du 3 mai 2012 dans le code d'Android |
| 8:34 | Humour | Le processeur qui se réveille comme toi au fond de la classe |
| 8:43 | Coupure musique | « Sauf qu'il reste un trou » (72 %) |
| 9:06 | Image | Le DJ qui laisse tourner le morceau |
| 9:21 | Vécu | Ton passage de dev (à écrire) |
| 9:24 | Boucle fermée | Les trois marches d'Android, la légende du stagiaire refermée |
| 9:48 | Lien au spectateur | « Et ton téléphone à toi ? », l'Afrique en chiffres |
| 10:33 | Retournement | Sur les téléphones, le 120 Hz arrive d'abord sur Android (2017 contre 2021) |
| 11:03 | Question | « Pourquoi un Android peut encore saccader en 2026 ? », puis ton avis |
| 11:22 | Récolte | Perfetto, le « MISS » de Guitar Hero en vrai |
| 11:37 | Rappel | « Seize millisecondes. Toc. » |

**Total** : 34 relances en 12 min 10, environ une toutes les 21 secondes. Le plus long trou est entre 9:24 et 9:48 (récap) : 24 s.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:35-0:54 | Moyen | On quitte le doigt pour l'écran et les hertz | Le métronome du hook continue sans coupure, et Guitar Hero arrive avant 0:55 |
| 3:01-3:25 | Élevé | La boucle en cinq temps, le passage le plus technique, juste après l'abonnement | Une seule image (la ligne du temps en cinq cases, deux boîtes) puis la phrase de la partition ; ne nomme pas les cinq temps à voix haute |
| 5:21-6:06 | Moyen | Dianne Hackborn, les versions 1.0 et 3.0 | La phrase sur Android 4.0 est coupée ; le visuel de la fenêtre (cadre vert, contenu gris) et le rappel de la feuille portent l'explication |
| 8:43-9:06 | Élevé | Après le pic Butter, on croit l'histoire finie | Coupure musicale sur « il reste un trou », puis le DJ dans les 20 s |
| 9:24-9:48 | Moyen | Le récap peut sonner comme une fin | Il est court, il referme la légende du stagiaire, et il enchaîne direct sur « Et ton téléphone à toi ? » |
| 9:48-10:33 | Moyen | Chiffres de marché | Deux chiffres seulement, la question sur ton téléphone avant, et la conséquence (« il a hérité ») juste après |

## Notes de montage

- **Composants à construire une fois** : le métronome et la ligne du temps de 16 ms (fil rouge, il revient à chaque chapitre) ; la piste de jeu de rythme avec le « MISS » (sections 1, 4 et 6) ; le réticule FPS (sections 2 et 4) ; l'orchestre décalé puis calé. La ligne du temps resservira pour toute vidéo sur la performance.
- **Pas de vraie interface** : iOS, Android, les applis de messages, Perfetto et le post de 2011 sont reconstruits en motion design (`strategie.md`, partie juridique). Captures autorisées : la doc d'Apple et de Google, la diapo publique de Romain Guy (Speaker Deck), la modif du code d'Android (AOSP, public).
- **Les personnes citées** : aucune photo de Bob Lee, Jay Freeman, Dianne Hackborn ni de l'étudiant ; des bulles de citation suffisent.
- **Flutter** : le logo Flutter n'apparaît que si ton vécu (section 5) parle de Flutter, sur une maquette générique. Jamais tes applis de travail. Le RenderThread est une pièce d'Android, pas de Flutter : ne les mélange pas à l'image.
- **Guitar Hero et le FPS** : le nom dit à voix haute suffit ; la piste de rythme et le réticule sont faits en motion design, sans logo ni extrait. Si tu veux un vrai extrait, prends quelques secondes d'une bande-annonce officielle.
- **Ne pas copier Enrico Tartarotti** (*The Ridiculous Engineering Of Animations*, 17/10/2026) : pas de courbes d'accélération ni de ressorts, pas de leçon sur l'easing. Notre angle, c'est le rythme de l'écran et l'histoire 2007 → 2012 → 2014, avec la légende de 2011.
- **Énergie** : calme, puis une montée toutes les 2 min. Montées sur le « MISS », le serveur de rendu, l'ambulance, l'orchestre qui se cale (7:08), le FPS côté Android et le Razer Phone.
- **Le ton envers Android** : jamais de moquerie. L'orchestre décalé parle d'Android avant 2012, pas de ton téléphone ; la fin donne à Android la prédiction du doigt en 2012 et le 120 Hz en 2017.
- **Miniature** : la piste de la fiche (le doigt, l'iPhone net, l'Android flou) dit « Android rame aujourd'hui », ce que la vidéo ne tient pas. Pistes qui collent : le doigt sur une liste avec la ligne du temps et une image « MISS », ou « 2007 → 2012 » sur le doigt. À trancher à la phase miniature, après la planche des vidéos hôtes.

## Faits utilisés

| N° | Phrase du script |
|---|---|
| 1 | « Avec Android 4.1, Jelly Bean, tout le système avance au même pas, sur un battement de seize millisecondes… » ; « Le mot "battement", c'est Google qui l'emploie. » |
| 2 | « Avant Android 4.1, les animations et les dessins d'Android n'étaient pas calés sur le battement de l'écran. » |
| 3 | Non utilisé : le troisième tampon est coupé |
| 4 | « Le toucher est calé lui aussi sur le battement. Ensuite, Android essaie de deviner où sera ton doigt… coup d'accélérateur au processeur. » |
| 5 (⚠️) | « Leur conférence s'appelle "For Butter or Worse" » ; « ce chantier, la presse l'appelle Project Butter » |
| 6 | « Choreographer… c'est lui qui prévient au moment du battement, et Android fait passer ses animations et ses redessins par lui. » |
| 7 (⚠️) | « Fin juin 2012, à la conférence Google I/O » (sans jour de sortie) |
| 8 | « la puce graphique ne s'en charge qu'à partir d'Android 3.0 » (la phrase sur Android 4.0 est coupée) |
| 9 (⚠️) | « d'après elle, Android assemble les fenêtres… depuis avant la version 1.0 » ; « pas une solution miracle pour une interface fluide » ; le titre de 9to5Google pour « les animations d'Android traînent derrière celles de l'iPhone » |
| 10 | « Fin 2014, Android 5.0… le RenderThread… garde les animations fluides même quand le fil principal de l'appli a du retard. » ; le DJ reprend cette phrase, sans « gros calcul » |
| 11 (⚠️) | « Fin 2014 » (sans jour) |
| 12 (⚠️) | « L'iPhone sort en 2007. Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran. » |
| 13 (❌, légende corrigée) | Section 3 : la priorité temps réel racontée comme une légende, « d'après la presse de l'époque », sans nommer ni citer l'étudiant ; Bob Lee (« erreurs de raisonnement »), Jay Freeman (« tout simplement faux ») ; le récap : « Elle n'apparaît nulle part dans cette histoire » |
| 14 | « chaque image suit une boucle en cinq temps, calée sur le battement de l'écran… un processus à part, le serveur de rendu » ; « Aujourd'hui, les deux systèmes se calent sur le battement de l'écran » (avec le fait 1) |
| 15 | « Chez Apple, ce raté a un nom : un hitch… Moins de cinq millisecondes de retard par seconde, c'est presque invisible… Au-delà de dix, c'est grave. » |
| 16 | « toutes les seize virgule six sept millisecondes… huit virgule trois trois » |
| 17 | « Core Animation… garde le contenu de ces calques en mémoire sous forme d'images, et c'est le matériel graphique qui les manipule directement » ; « sur iOS, chaque élément de l'écran repose sur un calque » |
| 18 | « il lance un petit minuteur. Si ton doigt bouge avant la fin, c'est un défilement, et il annule le toucher sur le message. » |
| 19 | « Depuis iOS 9, en 2015, l'iPhone… prédit où sera ton doigt » ; « côté iPhone, cette prédiction n'arrive dans la doc des développeurs qu'avec iOS 9, trois ans plus tard » (`predictedTouches` depuis iOS 9.0). L'iPad Air 2 est coupé |
| 20 | « L'iPhone, lui, y passe en septembre 2021, avec l'iPhone 13 Pro. » |
| 21 | « beaucoup de téléphones Android ont des écrans à quatre-vingt-dix ou cent vingt hertz » (la phrase sur Android 11 est coupée) |
| 22 (⚠️) | « En novembre 2017, Razer présente le Razer Phone, un Android avec un écran à cent vingt hertz. » Sans « premier » (fait 36) |
| 23 | « environ huit téléphones sur dix qui vont sur le web en Afrique sont des Android » (StatCounter, septembre 2026, trafic web) |
| 24 (⚠️) | « environ la moitié sont des Tecno, des Infinix ou des itel, d'après Canalys et Omdia » (2025) |
| 25 | « Une modif du 3 mai 2012, pour le Galaxy Nexus, qui s'intitule "Boost pulse CPU speeds" » |
| 26 (❓) | Non utilisé : aucune latence tactile chiffrée |
| 27 (⚠️) | « dès le premier iPhone, l'interface est faite de calques assemblés par la puce graphique. C'est Nick Lockwood qui le raconte » ; repris dans le récap avec « d'après Lockwood ». Pas de VSync en 2007 |
| 28 (⚠️) | Partout : « se caler sur le battement de l'écran », jamais « l'affichage passe avant tout » |
| 29 | « Perfetto, un outil de traçage, intégré depuis Android 10 » |
| 30 | « L'iPhone sort en 2007 » ; « 29 juin 2007 » à l'écran |
| 31 (⚠️) | Implicite (« Android a mis des années ») ; la date de 2008 n'est pas dite |
| 32 (ajouté au grill) | « Jay Freeman, le créateur de Cydia, l'appli des iPhone jailbreakés » ; « l'étudiant finit par mettre son post à jour » |
| 33 (ajouté au grill) | « Côté Google, une ingénieure d'Android, Dianne Hackborn, rejette elle aussi cette idée. Et elle avait déjà remis les pendules à l'heure sur un autre point. » |
| 34 (ajouté au grill) | « l'iPhone peut se contenter de faire glisser la feuille, sans redessiner ta liste à chaque image » |
| 35 (ajouté au grill) | « la doc d'Android parle encore aujourd'hui du chorégraphe et du RenderThread » ; « souvent, l'image saute parce que le fil principal de l'appli est bloqué » |
| 36 (ajouté au grill) | « sur les téléphones, c'est même Android qui ouvre le bal » (l'iPad Pro passe à 120 Hz en juin 2017, le Sharp Aquos R Compact, un Android, est en vente avant le Razer Phone) |
| Déduction | « un téléphone de 2025 tourne sur un Android bien plus récent que la version 5.0 » : logique (Android 5.0 date de 2014), pas sourcé ligne à ligne. « Quatre ans plus tard » : 2017 → 2021. « Trois ans plus tard » : 2012 → 2015 |

## Questions pour l'auteur

1. **Ton vécu de dev** (9:21) : as-tu déjà vu une interface geler parce qu'un calcul tournait sur le fil principal (en Flutter, en Kotlin), et qu'as-tu fait ? Sinon, la phrase saute.
2. **Ton avis** (11:12) : au-delà du fil principal bloqué, si un Android rame encore en 2026, d'où ça vient selon toi ? On le dit comme un avis, sans chiffre. C'est ce qui tient le « paraît » du titre au présent.
3. **Ton téléphone** : tu tournes sous quoi ? Si c'est un Android à 120 Hz, une phrase sur lui au moment du Razer Phone rendrait la fin plus personnelle.
4. **Les noms** : on nomme Bob Lee et Jay Freeman (cités par la presse de 2011), pas l'étudiant. Ça te va ? Pour info, Bob Lee est mort en avril 2023 : des commentaires pourraient le rappeler, sans que ça change la phrase, qui parle de 2011.
5. **La miniature** : on abandonne l'« Android flou » ? Pistes : le doigt et la ligne du temps avec un « MISS », ou « 2007 → 2012 ».
