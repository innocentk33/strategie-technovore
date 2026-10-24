# iPhone fluide : script v1

**Titre** : *Pourquoi tout paraît plus fluide sur un iPhone*

**Durée** : environ 1 820 mots de voix off. À ton débit mesuré sur ArtCraft (145 mots/min, pauses et improvisations comprises) : environ 12 min 30 (un peu au-dessus des 12 min visées : la section 3 a de quoi être resserrée au grill). À 165 mots/min : 11 min. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : le battement de l'écran. Toutes les seize millisecondes, « toc », une nouvelle image doit être prête : faire défiler une page, c'est un jeu de rythme. On suit qui tient ce rythme sur iPhone (les calques, le serveur de rendu, le doigt deviné), puis comment Android l'a appris en trois marches (3.0, 2012, 2014), jusqu'au téléphone Android du spectateur aujourd'hui. Le métronome revient à chaque chapitre.

**Boucles ouvertes** :
1. « Qu'est-ce que l'iPhone avait compris, et qu'Android a mis des années à rattraper ? » (hook, refermée dans la section 5).
2. « Fin 2011, un ancien stagiaire d'Android publie sa réponse… des ingénieurs la démontent » (hook, refermée dans la section 3).
3. « Et ton téléphone à toi ? » (implicite dès le hook, refermée dans la section 6).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = motion design (HyperFrames ou Remotion). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture, sauf les années (comme dans Uber). Aucune vraie interface d'appli : tout est reconstruit en motion design.

---

## 0. Hook (0:00 – 0:36) · objectif : 75 % à 0:15

[VISUEL : gros plan d'un doigt qui fait défiler une liste sur un iPhone. Pas de titre, pas de logo. La liste suit le doigt au pixel près.]

Pose ton doigt sur l'écran et fais défiler. Tu vois ? La page colle à ton doigt.

[SON : un « toc » sourd et régulier démarre, comme un métronome.]

Sauf que pour ça, ton téléphone doit fabriquer une nouvelle image toutes les seize millisecondes, sans jamais rater le temps.

[VISUEL : arrêt sur image ; sous le doigt, une ligne du temps coupée en cases de 16 ms, une case s'allume à chaque « toc ».]

L'iPhone sort en 2007. Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran.

[VISUEL : deux dates, « 29 juin 2007 » et « 2012 », une flèche entre elles.]

Alors qu'est-ce que l'iPhone avait compris, et qu'Android a mis des années à rattraper ?

Fin 2011, un ancien stagiaire d'Android publie sa réponse. La presse tech la reprend. Et des ingénieurs la démontent.

[VISUEL : un post de blog générique (pas la vraie page) qui se couvre de tampons « PARTAGÉ », puis d'un tampon rouge « FAUX ? ».]

---

## 1. Le cœur de ton écran (0:36 – 2:09)

[SON : le métronome continue, un peu plus présent.]

Pour comprendre, il faut écouter ton écran. Un écran classique se rafraîchit soixante fois par seconde. Donc toutes les seize virgule six sept millisecondes, toc, il affiche une nouvelle image. Et sur un écran à cent vingt hertz, c'est toutes les huit virgule trois trois.

[VISUEL : compteur « 16,67 ms », puis « 8,33 ms » ; la ligne du temps se resserre de moitié.]

Seize millisecondes pour savoir où est ton doigt et dessiner la page au bon endroit. À chaque image.

En fait, faire défiler une page, c'est un jeu de rythme. Comme dans Guitar Hero : la note descend, et tu dois taper pile sur le temps. Ici, la note, c'est l'image. Si elle est prête à temps, la page avance avec ton doigt. Mais si elle arrive en retard, l'écran garde l'ancienne image, et la page saute pour rattraper.

[VISUEL : piste de jeu de rythme ; des images de la liste tombent sur la ligne ; une arrive après, « MISS » en rouge, la liste fait un petit saut.]
[SON : le « clonk » d'une note ratée.]

Chez Apple, ce raté a un nom : un hitch. Une image qui arrive à l'écran plus tard que prévu. Et Apple a même fait un barème. Moins de cinq millisecondes de retard par seconde, c'est presque invisible. Entre cinq et dix, tu commences à sentir des accrocs. Au-delà de dix, pour Apple, c'est grave.

[VISUEL : jauge verte, orange, rouge : « < 5 ms/s », « 5-10 », « > 10 ». En petit : « Apple, Tech Talk 2020 ».]

Cinq millisecondes sur toute une seconde. Ouais, ils sont exigeants. Du coup, être fluide, ça revient à tenir le rythme, image après image, tant que ton doigt bouge.

Normalement, tu te dis que c'est ton appli qui dessine chacune de ces images. Sur iPhone, c'est plus malin que ça.

---

## 2. Ce que l'iPhone fait de ton doigt (2:09 – 4:49)

[VISUEL : un iPhone qui s'éclate en couches, vu de profil, comme un mille-feuille.]

D'après Nick Lockwood, l'auteur d'un livre sur Core Animation, dès le premier iPhone, l'interface est faite de calques assemblés par la puce graphique. Et aujourd'hui encore, la doc d'Apple le dit : sur iOS, chaque élément de l'écran repose sur un calque.

Si tu as déjà ouvert Photoshop, tu vois le principe. Ta liste de messages, c'est une feuille. La barre du haut, c'en est une autre.

Core Animation, le moteur d'animation d'Apple, garde le contenu de ces calques en mémoire sous forme d'images, et c'est le matériel graphique qui les manipule directement. Donc quand tu fais défiler, l'iPhone peut se contenter de faire glisser la feuille, sans redessiner ta liste à chaque image.

[VISUEL : la liste de messages glisse comme une feuille de papier sur une table ; seul le cadre bouge.]

Sauf que le dessin final, sur iPhone, ne se fait même pas dans ton appli. Apple l'explique dans une conférence pour développeurs de 2020 : chaque image suit une boucle en cinq temps, calée sur le battement de l'écran. L'appli reçoit ton toucher et met à jour son interface. Puis elle envoie tout ça à un processus à part, le serveur de rendu, et c'est lui qui prépare et dessine l'image.

[VISUEL : la ligne du temps de 16,67 ms coupée en cinq cases : Événement, Commit, Préparation, Exécution, Affichage. Les deux premières dans une boîte « Ton appli », les deux suivantes dans une boîte « Serveur de rendu ».]

En gros, ton appli écrit la partition, et c'est un autre musicien qui la joue en rythme.

**Abonnement (≈ 3:31, 25 % de la vidéo, juste après la première révélation)**

Si tu aimes voir ce qui tourne sous le capot des applis que tu utilises tous les jours, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; le métronome reste à l'écran.]

Et pendant ce temps, iOS s'occupe de ton doigt. Parce que quand tu poses le doigt sur une liste, il ne sait pas encore ce que tu veux : faire défiler, ou ouvrir un message. Du coup, il lance un petit minuteur. Si ton doigt bouge avant la fin, c'est un défilement, et il annule le toucher sur le message. Ce moment d'hésitation, tu ne l'as jamais remarqué.

[VISUEL : le doigt se pose sur un message ; un petit chrono circulaire apparaît ; le doigt glisse, le surlignage du message s'éteint, la liste part.]

Depuis iOS 9, en 2015, l'iPhone va plus loin : il prédit où sera ton doigt. C'est ce que tu fais dans un FPS quand tu vises devant un ennemi qui court. Et cette année-là, Apple présente l'iPad Air 2 : son écran tourne à soixante hertz, mais il lit le tactile à cent vingt. Deux fois plus vite que tous les autres iPhone et iPad de l'époque.

[VISUEL : un doigt fantôme, translucide, légèrement en avance sur le vrai ; un réticule de visée façon FPS sur sa trajectoire.]

Voilà pour l'iPhone. Du coup, retour fin 2011, côté Android. À l'époque, la presse tech se pose une question : pourquoi les animations d'Android traînent derrière celles de l'iPhone ?

---

## 3. La légende du temps réel (4:49 – 6:37)

[SON : la musique passe en mode enquête, une basse qui tient.]

Tu te rappelles le stagiaire du début ? D'après la presse de l'époque, c'est un étudiant, ancien stagiaire dans l'équipe Android. Fin 2011, il publie un long post avec son explication : sur iOS, l'interface serait dessinée dans un fil à part, avec une priorité temps réel. En gros, dès que ton doigt touche l'écran, l'interface passerait devant tout le reste, comme une ambulance sur l'autoroute.

[VISUEL : une ambulance marquée « Interface » double toutes les voitures marquées « tâches ». Un tampon « LÉGENDE » tombe dessus.]

L'explication est simple, elle fait plaisir, et la presse tech la relaie. Et pourtant, des ingénieurs la démontent vite. Bob Lee, ancien responsable des bibliothèques d'Android, parle d'erreurs de raisonnement. Un autre, Jay Freeman, dit que c'est tout simplement faux. Et l'étudiant finit par corriger son post.

De notre côté, on a fouillé la doc d'Apple : dans les pages qu'on a lues, aucune ne parle d'une priorité temps réel pour l'interface. Donc il faut chercher ailleurs.

On pourrait croire qu'Android, à l'époque, n'utilisait pas la puce graphique. En fait, d'après Dianne Hackborn, ingénieure Android chez Google, en 2011, Android assemble les fenêtres à l'écran avec le matériel graphique depuis avant la version 1.0. Ce qui lui manquait, c'était le contenu des fenêtres : les boutons et les listes. Ça, la puce graphique ne s'en charge qu'à partir d'Android 3.0. Et par défaut, seulement pour les applis qui visent Android 4.0 ou plus.

[VISUEL : une fenêtre Android générique ; le cadre s'allume en vert « GPU, avant 1.0 », le contenu reste gris, puis s'allume avec « 3.0 ».]

Et elle ajoute une phrase qui dit tout : la puce graphique n'est pas une solution miracle pour une interface fluide.

Mais alors, si la puissance ne suffit pas, il manquait quoi ? La réponse arrive quelques mois plus tard, avec un jeu de mots.

---

## 4. 2012 : tout Android sur le même temps (6:37 – 9:19)

[VISUEL : un orchestre en 2D où chaque musicien joue à son propre tempo.]
[SON : cacophonie, chaque instrument décalé.]

Avant Android 4.1, les animations et les dessins d'Android n'étaient pas calés sur le battement de l'écran. Imagine un orchestre où chaque musicien joue quand il veut, sans regarder le chef. Chaque musicien peut être très bon, et pourtant le morceau sonne faux. Et dans notre jeu de rythme, sans battement commun, rien ne garantit que l'image tombe sur le temps.

Fin juin 2012, à la conférence Google I/O, deux ingénieurs de Google, Chet Haase et Romain Guy, montent sur scène. Leur conférence s'appelle « For Butter or Worse ». Pour le beurre ou pour le pire. Oui, chez Google aussi, on aime les jeux de mots. Et ce chantier, la presse l'appelle Project Butter, le projet Beurre : l'idée, c'est une interface qui glisse comme du beurre.

[VISUEL : une diapo reconstituée avec le titre de la conférence ; une plaquette de beurre glisse dans une poêle.]

**Relance forte (≈ 7:30, 60 % de la vidéo)** : la cacophonie s'arrête net, une seconde de silence, puis un seul « toc ». C'est la réponse au « il manquait quoi ? » de 6:30.

[SON : silence, puis le métronome, seul.]

Résultat, avec Android 4.1, Jelly Bean, tout le système avance au même pas, sur un battement de seize millisecondes : le dessin des applis, le toucher, l'assemblage de l'écran et son rafraîchissement. Et le mot « battement », c'est Google qui l'emploie. Un battement de cœur.

[VISUEL : l'orchestre se cale ; tous les musiciens jouent sur le même « toc ». Citation à l'écran : « a 16 millisecond vsync heartbeat », Google.]
[SON : la cacophonie se range sur le métronome.]

Pour donner le tempo aux applis, Google crée une nouvelle pièce, avec un nom qui ne laisse aucun doute : Choreographer. Le chorégraphe. Concrètement, c'est lui qui prévient au moment du battement, et Android fait passer ses animations et ses redessins par lui. Cinq, six, sept, huit.

Android 4.1 ajoute aussi un troisième tampon d'image. Pour faire simple, une feuille de plus pour préparer les images suivantes.

Et il s'occupe de ton doigt. D'abord, le toucher est calé lui aussi sur le battement. Ensuite, Android essaie de deviner où sera ton doigt au prochain rafraîchissement : la visée en avance du FPS, trois ans avant qu'Apple l'ouvre aux développeurs de l'iPhone, avec iOS 9. Et quand tu touches l'écran après une pause, le système donne un coup d'accélérateur au processeur.

Et en effet, ce coup d'accélérateur, on le retrouve dans le code d'Android. Une modif du 3 mai 2012, pour le Galaxy Nexus, qui s'intitule « Boost pulse CPU speeds » : une impulsion de vitesse dès que tu interagis. Ton processeur somnolait, tu poses le doigt, il se réveille d'un coup. Comme toi au fond de la classe quand le prof dit ton prénom.

[VISUEL : la modif dans le code source public d'Android, date « 3 mai 2012 » surlignée ; un processeur en 2D qui se réveille en sursaut.]

Bref, en 2012, Android tient enfin le rythme. Sauf qu'il reste un trou. Quand l'appli elle-même prend du retard sur son fil principal, les animations trinquent avec elle.

[SON : la musique coupe net, une seconde de silence.]

---

## 5. 2014 : le DJ qui ne coupe jamais le son (9:19 – 10:29)

[VISUEL : un DJ en 2D ; la platine tourne pendant qu'il fouille dans ses disques.]
[SON : le métronome reprend, sous un beat.]

Fin 2014, Android 5.0, Lollipop, ajoute un fil géré par le système : le RenderThread, le fil de rendu. Et d'après Google, il garde les animations fluides même quand le fil principal de l'appli a du retard.

Tu vois le DJ en soirée ? Pendant qu'il cherche le prochain disque, il laisse tourner le morceau. Là, c'est pareil : ton appli peut aller chercher ses données ou faire un gros calcul, l'animation continue de tourner sur le battement.

[VISUEL : maquette générique d'une appli avec le logo Flutter (jamais tes applis de travail) ; un chargement qui tourne pendant qu'une barre « calcul » se remplit.]

Et là, je te parle en dev. [TON VÉCU EN FLUTTER, SI TU EN AS UN : UNE INTERFACE QUI A GELÉ PENDANT UN CALCUL, ET CE QUE TU AS FAIT. SINON, SUPPRIME CETTE PHRASE.]

Voilà comment Android a rattrapé son retard. Et ça répond à la question du début.

[VISUEL : un escalier à trois marches qui monte vers un iPhone posé en haut : « 3.0 : la puce graphique pour le contenu », « 2012 : le battement commun », « 2014 : le fil de rendu ».]

L'iPhone, d'après Lockwood, est parti avec une interface en calques, assemblés par la puce graphique dès le premier modèle. Android, lui, a construit tout ça en trois marches : la puce graphique pour le contenu des applis avec la version 3.0, le battement commun en 2012, puis le fil de rendu en 2014. Et aucune priorité magique là-dedans. Juste des systèmes qui ont appris à se caler sur le battement de l'écran.

---

## 6. Ton Android aujourd'hui (10:29 – 12:32)

Et ton téléphone à toi ? Si tu regardes depuis l'Afrique, il y a de bonnes chances que ce soit un Android. D'après StatCounter, en septembre 2026, environ huit téléphones sur dix qui vont sur le web en Afrique sont des Android. Et d'après Canalys et Omdia, environ la moitié des smartphones vendus en Afrique en 2025 sont des Tecno, des Infinix ou des itel.

[VISUEL : carte de l'Afrique qui se remplit de petits téléphones verts ; « 83 % du trafic web mobile (StatCounter, sept. 2026) ».]

Forcément, un Tecno de 2025 tourne sur un Android bien plus récent que la version 5.0. Donc le battement de 2012 et le fil de rendu de 2014, il les a.

Et pour les écrans, Android a même ouvert le bal. En novembre 2017, Razer présente son Razer Phone, un Android, comme le premier écran à cent vingt hertz. L'iPhone, lui, passe à cent vingt hertz en septembre 2021, avec l'iPhone 13 Pro. Quatre ans plus tard. Pour une fois, c'est l'iPhone qui arrive après.

[VISUEL : frise : « Razer Phone, nov. 2017 » puis « iPhone 13 Pro, sept. 2021 » ; la ligne du temps passe de 16,67 à 8,33 ms.]

En fait, aujourd'hui, Google le dit lui-même : beaucoup de téléphones Android ont des écrans à quatre-vingt-dix ou cent vingt hertz. Et depuis Android 11, une appli peut dire au système à quel rythme elle veut être affichée, puis le téléphone choisit le mode d'écran qui va avec.

Et si tu es dev, Google te donne même de quoi voir ton appli rater le temps : Perfetto, un outil de traçage, intégré depuis Android 10.

[VISUEL : une trace Perfetto stylisée (reconstituée), une image en rouge qui dépasse son créneau de 16 ms.]

[TON AVIS DE DEV : SI UN ANDROID RAME ENCORE EN 2026, D'OÙ ÇA VIENT SELON TOI ? L'APPLI, LA PUCE, LA SURCOUCHE DU FABRICANT ? UNE OU DEUX PHRASES, DITES COMME UN AVIS.]

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
| 0:08 | Chiffre | Une image toutes les seize millisecondes, le métronome démarre |
| 0:20 | Contraste daté | 2007 contre 2012 |
| 0:25 | Question centrale | « Qu'est-ce que l'iPhone avait compris ? » |
| 0:30 | Boucle ouverte | Le stagiaire de 2011 et sa réponse démontée (refermée à 4:49-5:40) |
| 1:02 | Référence gamer | Faire défiler = un jeu de rythme, Guitar Hero |
| 1:15 | Visuel + son | « MISS » et la note ratée |
| 1:26 | Chiffre | Le barème d'Apple : 5 et 10 ms par seconde |
| 2:09 | Visuel | L'iPhone qui s'éclate en calques |
| 2:55 | Surprise | Le dessin final ne se fait pas dans ton appli |
| 3:31 | Appel à l'action | Abonnement (28 %) |
| 3:43 | Devinette implicite | Défiler ou ouvrir le message ? Le minuteur caché |
| 4:10 | Référence gamer | Prédire le doigt = viser devant l'ennemi dans un FPS |
| 4:49 | Changement de ton | Musique d'enquête, la légende du temps réel |
| 5:00 | Visuel + humour | L'ambulance « Interface » et le tampon « LÉGENDE » |
| 5:47 | Retournement | Android avait la puce graphique depuis avant la 1.0 |
| 6:30 | Question | « Il manquait quoi ? » + teaser du jeu de mots |
| 6:45 | Son | Cacophonie de l'orchestre |
| 7:03 | Humour | « For Butter or Worse », le projet Beurre |
| 7:30 | Relance forte (60 %) | Silence, puis le métronome seul : tout Android sur le même battement |
| 7:48 | Humour | Le chorégraphe, « cinq, six, sept, huit » |
| 8:41 | Preuve à l'écran | La modif du 3 mai 2012 dans le code d'Android |
| 9:00 | Humour | Le processeur qui se réveille comme toi au fond de la classe |
| 9:10 | Coupure musique | « Sauf qu'il reste un trou » (73 %) |
| 9:34 | Image | Le DJ qui laisse tourner le morceau |
| 9:50 | Vécu | Ton passage de dev Flutter (à écrire) |
| 9:59 | Boucle fermée | Les trois marches d'Android, réponse à la question centrale |
| 10:29 | Lien au spectateur | « Et ton téléphone à toi ? », l'Afrique en chiffres |
| 11:09 | Retournement | Le 120 Hz arrive d'abord sur Android (2017 contre 2021) |
| 12:01 | Rappel | « Seize millisecondes. Toc. » |

**Total** : 30 relances en 12 min 30, environ une toutes les 25 secondes. Le plus long trou est entre 9:59 et 10:29 (récap), à surveiller.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:30-1:00 | Moyen | On quitte le doigt pour l'écran et les hertz | Le métronome du hook continue sans coupure, et Guitar Hero arrive avant 1:05 |
| 2:55-3:30 | Élevé | La boucle en cinq temps, le passage le plus technique, juste avant l'abonnement | Une seule image (la ligne du temps en cinq cases, deux boîtes) puis la phrase de la partition ; ne nomme pas les cinq temps à voix haute |
| 5:47-6:30 | Moyen | Dianne Hackborn, les versions 1.0, 3.0 et 4.0 s'empilent | Le visuel de la fenêtre (cadre vert, contenu gris) porte l'explication ; si le grill trouve ça lourd, coupe la phrase sur Android 4.0 |
| 9:10-9:30 | Élevé | Après le pic Butter, on croit l'histoire finie | Coupure musicale sur « il reste un trou », puis le DJ dans les 20 s |
| 9:59-10:29 | Moyen | Le récap peut sonner comme une fin | Il est court et enchaîne direct sur « Et ton téléphone à toi ? » |
| 10:29-11:09 | Moyen | Chiffres de marché | Deux chiffres seulement, et la question sur ton téléphone avant |

## Notes de montage

- **Composants à construire une fois** : le métronome et la ligne du temps de 16 ms (fil rouge, il revient à chaque chapitre) ; la piste de jeu de rythme avec le « MISS » ; l'orchestre décalé puis calé. La ligne du temps resservira pour toute vidéo sur la performance.
- **Pas de vraie interface** : iOS, Android, les applis de messages, Perfetto et le post de 2011 sont reconstruits en motion design (`strategie.md`, partie juridique). Captures autorisées : la doc d'Apple et de Google, la diapo publique de Romain Guy (Speaker Deck), la modif du code d'Android (AOSP, public).
- **Flutter** : une maquette générique avec le logo Flutter. Jamais tes applis de travail.
- **Guitar Hero et le FPS** : le nom dit à voix haute suffit ; la piste de rythme et le réticule sont faits en motion design, sans logo ni extrait. Si tu veux un vrai extrait, prends quelques secondes d'une bande-annonce officielle.
- **Ne pas copier Enrico Tartarotti** (*The Ridiculous Engineering Of Animations*, 17/10/2026) : pas de courbes d'accélération ni de ressorts, pas de leçon sur l'easing. Notre angle, c'est le rythme de l'écran et l'histoire 2007 → 2012 → 2014, avec la légende de 2011.
- **Énergie** : calme, puis une montée toutes les 2 min. Montées sur le « MISS », le serveur de rendu, l'ambulance, l'orchestre qui se cale (7:30) et le Razer Phone.
- **Le ton envers Android** : jamais de moquerie. L'orchestre décalé parle d'Android avant 2012, pas de ton téléphone ; le final est le moment où Android ouvre le bal.
- **Miniature** : la piste de la fiche (le doigt, l'iPhone net, l'Android flou) dit « Android rame aujourd'hui », ce que la vidéo ne tient pas. Une piste qui colle mieux : le doigt sur une liste et un métronome, ou la ligne du temps avec une image « MISS ». À voir à la phase miniature.

## Faits utilisés

| N° | Phrase du script |
|---|---|
| 1 | « Avec Android 4.1, Jelly Bean, tout le système avance au même pas, sur un battement de seize millisecondes… » ; « Et le mot "battement", c'est Google qui l'emploie. » |
| 2 | « Avant Android 4.1, les animations et les dessins d'Android n'étaient pas calés sur le battement de l'écran. » |
| 3 (⚠️) | « Android 4.1 ajoute aussi un troisième tampon d'image. » (sans dire quand il sert) |
| 4 | « Le toucher est calé lui aussi sur le battement. Ensuite, Android essaie de deviner où sera ton doigt… coup d'accélérateur au processeur. » |
| 5 (⚠️) | « Leur conférence s'appelle "For Butter or Worse" » ; « ce chantier, la presse l'appelle Project Butter » |
| 6 | « Choreographer… c'est lui qui prévient au moment du battement, et Android fait passer ses animations et ses redessins par lui. » |
| 7 (⚠️) | « Fin juin 2012, à la conférence Google I/O » (sans jour de sortie) |
| 8 | « la puce graphique ne s'en charge qu'à partir d'Android 3.0. Et par défaut, seulement pour les applis qui visent Android 4.0 ou plus. » |
| 9 (⚠️) | « d'après Dianne Hackborn, ingénieure Android chez Google, en 2011, Android assemble les fenêtres… depuis avant la version 1.0 » ; « pas une solution miracle pour une interface fluide » ; le titre de 9to5Google pour « les animations d'Android traînent derrière celles de l'iPhone » |
| 10 | « Fin 2014, Android 5.0… le RenderThread… garde les animations fluides même quand le fil principal de l'appli a du retard. » |
| 11 (⚠️) | « Fin 2014 » (sans jour) |
| 12 (⚠️) | « L'iPhone sort en 2007. Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran. » |
| 13 (❌, légende corrigée) | Section 3 en entier : la priorité temps réel racontée comme une légende, « d'après la presse de l'époque », sans nommer ni citer l'étudiant ; Bob Lee (« erreurs de raisonnement »), Jay Freeman (« tout simplement faux »), le post corrigé |
| 14 | « chaque image suit une boucle en cinq temps, calée sur le battement de l'écran… un processus à part, le serveur de rendu » |
| 15 | « Chez Apple, ce raté a un nom : un hitch… Moins de cinq millisecondes de retard par seconde, c'est presque invisible… Au-delà de dix, c'est grave. » |
| 16 | « toutes les seize virgule six sept millisecondes… huit virgule trois trois » |
| 17 | « Core Animation… garde le contenu de ces calques en mémoire sous forme d'images, et c'est le matériel graphique qui les manipule directement » ; « sur iOS, chaque élément de l'écran repose sur un calque » |
| 18 | « il lance un petit minuteur. Si ton doigt bouge avant la fin, c'est un défilement, et il annule le toucher sur le message. » |
| 19 | « Depuis iOS 9, en 2015, l'iPhone… prédit où sera ton doigt… l'iPad Air 2 : son écran tourne à soixante hertz, mais il lit le tactile à cent vingt. Deux fois plus vite que tous les autres iPhone et iPad » ; « trois ans avant qu'Apple l'ouvre aux développeurs de l'iPhone, avec iOS 9 » (2012 → 2015, `predictedTouches` depuis iOS 9.0) |
| 20 | « L'iPhone, lui, passe à cent vingt hertz en septembre 2021, avec l'iPhone 13 Pro. » |
| 21 | « beaucoup de téléphones Android ont des écrans à quatre-vingt-dix ou cent vingt hertz… depuis Android 11, une appli peut dire au système à quel rythme elle veut être affichée » |
| 22 (⚠️) | « En novembre 2017, Razer présente son Razer Phone, un Android, comme le premier écran à cent vingt hertz. » |
| 23 | « environ huit téléphones sur dix qui vont sur le web en Afrique sont des Android » (StatCounter, septembre 2026, trafic web) |
| 24 (⚠️) | « environ la moitié des smartphones vendus en Afrique en 2025 sont des Tecno, des Infinix ou des itel » (Canalys et Omdia) |
| 25 | « Une modif du 3 mai 2012, pour le Galaxy Nexus, qui s'intitule "Boost pulse CPU speeds" » |
| 26 (❓) | Non utilisé : aucune latence tactile chiffrée |
| 27 (⚠️) | « D'après Nick Lockwood… dès le premier iPhone, l'interface est faite de calques assemblés par la puce graphique » ; repris dans le récap avec « d'après Lockwood ». Pas de VSync en 2007 |
| 28 (⚠️) | Partout : « se caler sur le battement de l'écran », jamais « l'affichage passe avant tout » |
| 29 | « Perfetto, un outil de traçage, intégré depuis Android 10 » |
| 30 | « L'iPhone sort en 2007 » ; « 29 juin 2007 » à l'écran |
| 31 (⚠️) | Implicite (« Android a mis des années ») ; la date de 2008 n'est pas dite |
| Déduction | « un Tecno de 2025 tourne sur un Android bien plus récent que la version 5.0 » : logique (Android 5.0 date de 2014), mais pas sourcé ligne à ligne. « Quatre ans plus tard » : 2017 → 2021 |

## Questions pour l'auteur

1. **Ton vécu de dev** (9:50) : en Flutter, as-tu déjà vu une interface geler pendant un calcul, et qu'as-tu fait ? Sinon, la phrase saute.
2. **Ton avis** (fin) : si un Android rame encore en 2026, d'où ça vient selon toi ? On le dit comme un avis, sans chiffre.
3. **Ton téléphone** : tu tournes sous quoi, `[TON TÉLÉPHONE ACTUEL]` ? Si c'est un Android à 120 Hz, une phrase sur lui au moment du Razer Phone rendrait la fin plus personnelle.
4. **Les noms** : on nomme Bob Lee et Jay Freeman, mais pas l'étudiant de 2011. Ça te va, ou tu préfères ne nommer personne ?
5. **La miniature** : la piste « Android flou » de la fiche promet un Android qui rame aujourd'hui, ce que la vidéo ne dit pas. Tu gardes, ou on passe au doigt et au métronome ?
6. **La durée** : 12 min 30 à 145 mots/min. Si tu veux tenir 12 min, la phrase sur Android 4.0 (6:10) et le troisième tampon (8:11) se coupent sans rien casser.
