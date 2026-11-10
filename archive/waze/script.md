# Waze : script final (v2)

**Titre** : *Comment Waze sait qu'il y a un bouchon avant que tu le voies*

**Durée** : environ 1 810 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft, pauses et improvisations comprises) : environ 12 min 30 ; en coupes serrées comme sur Uber (~180 mots/min) : 10 min plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : ton virage à droite. Le hook montre le détour et la route rouge que personne n'a signalée ; la vidéo démonte la machine dans l'ordre où elle travaille : le téléphone qui sert de capteur, la comparaison avec l'habitude, les signalements, puis le faux bouchon de 2014, qui prouve que ce sont bien les téléphones qui font le bouchon et qui débouche sur un détour, comme le tien. Le calcul du détour referme le virage à droite, et la fin retourne la situation : c'est toi, coincé, qui fais tourner quelqu'un d'autre.

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **ordre** : le faux bouchon (ex-section 5) passe avant le calcul. La coupure musicale tombe à 58 % au lieu de 73 %, et le détour des chercheurs sert de pont vers « pourquoi il t'a fait tourner » ;
- **serveur de sessions en réserve** (bas du fichier) : hors promesse, et la phrase « un million de fois par seconde, un serveur se demande » allait plus loin que le test de charge ;
- **hook** : « Tu râles » gardé et raccourci, parce que ton « d'habitude » est récolté en section 2 ; « la réponse est dans ta poche » devient « dans la poche des conducteurs devant toi, et dans la tienne » (c'est leur téléphone qui a vu le bouchon) ; le teaser des chercheurs est réécrit ;
- **section 1** : « quand une appli me fait un coup pareil » retiré (ça laissait croire que Waze t'avait fait le coup) ; FreeMap Israel retiré (rafale de faits, territoire de Thibaut Dcode) ; « exactement » retiré ;
- **section 2** : la rafale des 48 demi-heures reliée à ton mardi ; le niveau 0 à 5 et le retard décrits sans dire que la vitesse fluide « note la gravité » ; Monster Hunter remplacé par le niveau de recherche de GTA 5, qui va bien de 0 à 5 étoiles (à valider) ;
- **section 3** : « un objet sur la route » devient « un danger » (le nom du menu Waze) ; l'anecdote de Petreanu replacée « à ses débuts chez Waze » et reliée à la confiance, comme dans son article ; les deux minutes ne sont plus collées à la question du délai ; « J'ai cherché » devient « On a cherché » ; la question « combien de téléphones ? » ouvre le faux bouchon ;
- **faux bouchon** : la vraie chronologie de l'étude (immobiles, puis ralentissement progressif, puis départ à 70 km/h) ; les bots sont des téléphones Android simulés avec la vraie appli ; « quinze » dit comme ce qui a suffi sur leur campus, pas comme un seuil de Waze ;
- **calcul** : la prudence de l'heure d'arrivée sans dire que chaque avance « est voulue » ; le « parce que tu le désinstalles » n'est plus prêté à Waze ; « Voilà ton virage à droite » paie enfin le titre (« tu voyais encore une route dégagée ») ;
- **fin** : la phrase de Petreanu suivie de ce qu'il dit lui-même (« les gens derrière moi auront peut-être un itinéraire qui contourne le bouchon »), ce qui source « le Karim, c'est toi » ; le deuxième appel « sur Technovore, on les ouvre une par une » retiré (doublon de celui de 25 %).

**Boucles ouvertes** :
1. « Alors comment il savait ? » (hook, 0:14) : refermée en deux temps, section 2 (la comparaison) et section 5 (« voilà ton virage à droite »).
2. « Des chercheurs ont inventé des conducteurs qui n'existaient pas » (hook, 0:22) : refermée dans la section 4.
3. « Combien de temps, et combien de téléphones ? » (fin de la section 3) : refermée honnêtement (Waze ne le publie pas), puis relancée par les quinze bots de 2014.
4. « Comment il décide que ça vaut le coup ? » (fin de la section 4) : refermée par le calcul, section 5.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (la famille de cartes sombres d'Uber) ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de [`sources.md`](sources.md), et des ⚠️ avec la formulation qu'il donne.

---

## 0. Hook (0:00 – 0:31) · objectif : 75 % à 0:15

[VISUEL : un téléphone en gros plan, la carte sombre de la vidéo Uber, ta flèche qui roule. L'itinéraire bleu tourne d'un coup à droite. Pas de titre, pas de logo.]

Waze te fait tourner à droite. Toi, tu râles : d'habitude, c'est tout droit.

[VISUEL : dézoom : sur la route évitée, une file de points qui ne bougent plus, le tronçon vire au rouge. Aucune icône de signalement, aucun accident à l'écran.]
[SON : un « tic » sec quand le tronçon passe au rouge.]

Sauf que sur la route que tu viens d'éviter, tout le monde est à l'arrêt. Et personne ne l'avait signalé. Alors comment il savait ?

En fait, la réponse est dans la poche des conducteurs devant toi. Et dans la tienne.

[VISUEL : zoom sur les points arrêtés : chacun devient un petit téléphone. Puis ta flèche, qui envoie elle aussi un point.]

La preuve : en deux mille quatorze, des chercheurs ont inventé des conducteurs qui n'existaient pas. Et Waze a affiché leur bouchon.

[VISUEL : teaser d'une seconde : quinze points fantômes ralentissent, la route devient rouge, « 8 km/h ». Arrêt sur image.]

---

## 1. Ton téléphone, ce capteur (0:31 – 2:36)

Moi, je suis dev. Alors j'ai voulu voir la machine de l'intérieur, avec ce que Waze publie lui-même : la doc qu'il donne aux villes partenaires, un article d'un de ses ingénieurs, et même son brevet.

[VISUEL : défilement rapide des trois documents, seules les dates restent nettes. Texte : « Toutes les sources en description ».]

[TON EXPÉRIENCE AVEC WAZE, SI TU EN AS UNE : UN DÉTOUR QUI T'A SAUVÉ, OU UN QUI T'A ENVOYÉ DANS UN CHEMIN DE TERRE. DEUX PHRASES MAXIMUM. SINON, ON COUPE.]

Tu te rappelles la vidéo sur Uber ? Le téléphone de Karim, le chauffeur, envoyait sa position pour que tu le voies arriver sur ta carte. Chez Waze, c'est le même principe, sauf que tout le monde fait le Karim.

[VISUEL : la carte du trajet de la vidéo Uber revient ; la voiture de Karim se multiplie en des centaines de flèches Waze sur le périph.]

La doc de Waze le dit noir sur blanc : ses infos de bouchon sont fabriquées à partir des points GPS envoyés par les téléphones des gens qui conduisent avec l'appli. Et l'ingénieur le dit encore plus simplement : quand tu gardes l'appli ouverte, tu lui donnes, sans rien faire, la vitesse de la portion de route où tu es.

Tu n'as touché à rien, et tu bosses déjà pour lui.

[VISUEL : ta flèche émet un petit point à intervalles réguliers ; chaque point porte une heure.]

Mais comment on passe d'une position à une vitesse ? Pour faire simple, c'est du niveau collège. Le brevet de Waze, déposé en deux mille huit, décrit le truc : chaque conducteur envoie sa position à intervalles réguliers, avec l'heure. Le serveur regarde de combien tu as bougé entre deux envois, et il en tire ta vitesse. Genre, cent mètres en dix secondes : tu roules à trente-six kilomètres-heure.

[VISUEL : deux points sur la route, une règle « 100 m », un chrono « 10 s », puis « 36 km/h » (« exemple » en petit).]

Ensuite, il fait la moyenne de tous ceux qui sont sur la même route, et il obtient la vitesse du trafic. Bon, un brevet, ça décrit ce que le système peut faire, pas forcément ce que Waze fait aujourd'hui. Mais la doc actuelle va dans le même sens.

Et des capteurs, il en a : fin deux mille vingt-deux, Waze comptait environ cent cinquante millions d'utilisateurs par mois. Ça en fait, des téléphones qui roulent.

Du coup, Waze connaît ta vitesse. Sauf qu'une vitesse, toute seule, ça ne dit pas s'il y a un bouchon.

---

## 2. C'est quoi, un bouchon, pour une machine ? (2:36 – 5:04)

[VISUEL : deux routes côte à côte, un point à 20 km/h sur chacune : une petite rue avec des dos-d'âne, une voie rapide.]

Petite devinette. Tu roules à vingt kilomètres-heure. Bouchon ou pas ?

[VISUEL : deux secondes de silence, les deux points avancent.]

Bah ça dépend où. Dans une petite rue pleine de dos-d'âne, vingt, c'est normal. Sur une voie rapide, à vingt, c'est la catastrophe. Donc pour Waze, un bouchon, c'est une comparaison : on roule nettement moins vite que d'habitude, à cette heure-là, sur ce bout de route.

**Abonnement (≈ 3:00, 24 % de la vidéo, juste après la première révélation)**

Si tu aimes voir ce qui tourne vraiment derrière les applis de ta poche, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, les deux routes restent à l'écran.]

Et « d'habitude », tu te rappelles ? C'est ce que tu disais au début : d'habitude, c'est tout droit. Sauf que l'habitude de ta route, Waze la connaît mieux que toi.

En gros, pour chaque bout de route, il garde la vitesse moyenne de chaque demi-heure, pour chaque jour de la semaine. Ça fait quarante-huit mesures par jour, rien que pour ce tronçon. Et un jour normal, il s'appuie sur les huit dernières semaines environ. Donc pour ton mardi à huit heures et demie, il a à peu près les huit derniers mardis à huit heures et demie.

[VISUEL : une frise de 48 cases pour un mardi ; une courbe grise, la vitesse habituelle, qui creuse à 8 h 30 et à 18 h. Huit petites courbes de mardis passés se superposent pour former la grise.]

Franchement, c'est un peu flippant : il sait mieux que toi à quoi ressemble ta rue le mardi matin.

Et en effet, la doc de Waze donne la règle. Quand un tronçon roule sous sa vitesse moyenne habituelle pour cette heure et ce jour, Waze le marque comme ralentissement ou bouchon. Puis il recoupe avec les signaux GPS et les signalements.

[VISUEL : la courbe d'aujourd'hui, en rouge, plonge sous la courbe grise ; sur la carte, le tronçon vire au rouge au même instant.]
[SON : le même « tic » que dans le hook.]

Ensuite, pour chaque bouchon, il note deux choses. Un niveau, de zéro, fluide, à cinq, bloqué. Et le retard en secondes, par rapport à la vitesse fluide du tronçon, la plus haute qu'on y ait mesurée.

[VISUEL : une jauge de 0 à 5 en étoiles, façon niveau de recherche (motion design, pas d'image du jeu) ; « retard : +240 s » avec « exemple » en petit.]

C'est le niveau de recherche de GTA cinq. Zéro étoile, tu roules tranquille. Cinq étoiles, t'as tout Los Santos aux fesses.

Et avant de faire sa moyenne, Waze écarte les extrêmes : le conducteur qui se traîne et celui qui se prend pour Vin Diesel. Il tient même compte du type de véhicule, parce qu'une moto ou un bus ne roulent pas comme toi.

[VISUEL : deux points sortent du lot et sont barrés : un escargot, une voiture avec des flammes. Une moto et un bus ont leur propre couleur.]

Voilà comment Waze voit un bouchon sans que personne ne dise rien. Mais alors, les gens qui appuient sur « signaler », ils servent à quoi ?

---

## 3. Les signalements, le deuxième étage (5:04 – 7:17)

[VISUEL : le menu de signalement, reconstruit en motion design (pas la vraie appli) : accident, police, danger.]

Tu vois le bouton pour signaler un accident, la police ou un danger sur la route ? D'après la doc, tes signalements s'affichent comme des alertes, et ils pèsent aussi sur la façon dont Waze repère les bouchons.

Donc le bouchon sort d'abord des vitesses. Les signalements viennent ensuite le confirmer et le préciser.

[VISUEL : une maison à deux étages : au rez-de-chaussée, les vitesses ; au premier, les icônes de signalement qui se posent sur le tronçon rouge.]

Et ça explique un truc du début. Tu te rappelles la route où tout le monde était à l'arrêt ? Waze savait que ça bloquait. Par contre, il ne savait pas pourquoi. Accident, travaux, camion en panne : tant que personne ne le signale, pour lui, ce sont juste des téléphones qui n'avancent plus.

[VISUEL : retour sur la route rouge du hook ; un point d'interrogation au-dessus du tronçon.]

C'est comme ton pote qui voit que tu ne réponds plus depuis trois heures. Il sait qu'il se passe un truc. Mais réunion ou sieste, aucune idée.

Et quand quelqu'un signale, ça peut aller très vite. Yigal Petreanu, ingénieur chez Waze, raconte qu'à ses débuts dans la boîte, il recevait le signalement d'une voiture sur le bas-côté, et cinq secondes plus tard, il voyait la voiture.

[VISUEL : une alerte « voiture sur le bas-côté » s'affiche ; un compteur « 5 s » ; la voiture apparaît au bord de la route.]

Cinq secondes. Quelqu'un, un peu plus loin devant, avait pris le temps d'appuyer sur un bouton pour un inconnu. Et c'est comme ça, dit-il, qu'il a su qu'il pouvait faire confiance à l'appli. Toi, au début de la vidéo, tu râlais encore.

Alors forcément, tu dois te demander combien de temps il faut à Waze pour repérer un bouchon, et combien de téléphones. Eh bien, Waze ne le dit nulle part. On a cherché.

[VISUEL : les pages de la doc défilent, une loupe passe dessus ; texte : « délai de détection : non publié » ; « nombre de téléphones : non publié ».]

Le seul chiffre officiel, c'est le flux qu'il envoie à ses villes partenaires : il est mis à jour toutes les deux minutes. Attention, ça, c'est le rythme auquel il livre les infos aux villes. Le temps qu'il met à voir le bouchon, lui, reste secret.

Et pour le nombre de téléphones, le seul repère qu'on a vient de quatre chercheurs qui, en deux mille quatorze, ont fabriqué des faux téléphones. Et leurs faux téléphones, Waze les a crus.

---

## 4. Le bouchon qui n'existait pas (7:17 – 9:50) · relance forte

[SON : la musique coupe net, une seconde de silence, puis une basse sombre.]
[VISUEL : un campus vu du ciel, de nuit ; un texte « Haïfa, 2014 ».]

Les quatre chercheurs sont au Technion, une université israélienne à Haïfa. En gros, leur idée : si ce sont les téléphones qui font le bouchon, des faux téléphones devraient pouvoir en faire un aussi.

Donc ils lancent sur leurs serveurs des téléphones Android simulés, avec la vraie appli Waze dedans, et ils leur font envoyer des positions GPS truquées. Des « bots conducteurs ».

[VISUEL : une rangée de téléphones fantômes dans un serveur, chacun avec une petite flèche Waze ; un faux point GPS sort de chacun.]

Premier essai : ils posent leurs bots sur le campus, immobiles. Résultat, rien. Aucun bouchon. D'après eux, Waze voyait sans doute des gens qui venaient d'ouvrir l'appli sans avoir démarré.

[VISUEL : quinze points fantômes immobiles sur un parking ; la route reste grise.]

Deuxième essai : ils les font ralentir petit à petit. Toujours rien. Et là, ils comprennent : sur le campus, tout le monde roule doucement. Et ça, tu sais déjà pourquoi ça coince : rouler lentement là où on roule toujours lentement, pour Waze, c'est normal. Les chercheurs en déduisent que son calcul est relatif, une comparaison avec l'habitude. C'est ce que dit la doc.

Donc ils ajoutent une étape. Les bots démarrent à soixante-dix kilomètres-heure, puis ils ralentissent.

[VISUEL : les points fantômes filent, puis freinent ensemble ; la route vire au rouge, « 8 km/h ».]
[SON : le « tic » du hook, plus grave.]

Et cette fois, un bouchon apparaît. À huit kilomètres-heure. Il a suffi de quinze bots.

Un bouchon de PNJ.

Et derrière, Waze change l'itinéraire qu'il proposait aux chercheurs : avant, un kilomètre et demi et trois minutes ; après, un kilomètre six et quatre minutes. Un détour, pour des conducteurs qui n'existent pas. Le faux bouchon est même resté affiché une vingtaine de minutes après l'arrêt des bots.

[VISUEL : deux itinéraires superposés, « 1,5 km · 3 min » puis « 1,6 km · 4 min » ; un chrono « ~20 min » sur la route rouge vide.]

D'après l'étude, en deux mille quatorze, Waze ne faisait aucun effort visible pour distinguer un humain d'une machine.

Attention quand même à ce qu'on en fait. Ce qu'ils ont montré, c'est l'itinéraire de leur propre test qui change ; envoyer d'autres conducteurs ailleurs, ils écrivent qu'ils pourraient le faire, en théorie. Quinze, c'est ce qui a suffi sur leur campus ; Waze, lui, n'a jamais donné de seuil. Et c'était il y a plus de dix ans : l'algorithme a pu changer depuis.

[VISUEL : bandeau « Étude de 2014. Waze a pu changer depuis. »]

Mais cette expérience, c'est la meilleure preuve de tout ce qu'on vient de voir : chez Waze, ce sont les téléphones qui font le bouchon. Même quand ils sont faux.

Et t'as vu ce qu'il a fait, de ce faux bouchon ? Un détour. Comme ton virage à droite. Reste à savoir comment il décide que ça vaut le coup.

---

## 5. Le calcul : pourquoi il t'a fait tourner (9:50 – 11:18)

[VISUEL : la carte du hook revient, ta flèche et l'heure d'arrivée affichée en haut.]
[SON : la musique du début revient, ding de chapitre.]

En fait, pour te donner une heure d'arrivée, Waze a deux sources : ce qui se passe maintenant, et l'historique de ses demi-heures. Et il les mélange dans une équation qui calcule ta vitesse la plus probable. L'équation exacte, évidemment, il ne la publie pas.

[VISUEL : deux flux, « maintenant » et « habitude », qui se versent dans une boîte noire marquée « ? » ; il en sort une heure d'arrivée.]

Et il penche volontairement du côté prudent : pour Waze, mieux vaut que tu arrives pile à l'heure ou un peu en avance. Du coup, si tu arrives souvent un peu avant l'heure annoncée, désolé, c'est peut-être pas toi le Vin Diesel : Waze prévoit large exprès.

Une fois que tu roules, il refait le point toutes les quelques minutes. Si ça change un peu, il te prévient juste du retard. L'ingénieur le dit : pour une minute de retard, aucun intérêt à t'envoyer sur un tout nouvel itinéraire. Donc Waze garde exprès des trajets stables. Et heureusement, parce qu'un GPS qui change d'avis tous les cent mètres, tu le désinstalles. Mais si ça change beaucoup, là, il te trouve une autre route.

[VISUEL : ta flèche ; un compteur « +1 min » : l'itinéraire ne bouge pas. Puis un gros retard (« exemple » écrit en petit) : l'itinéraire bascule à droite.]
[SON : le clignotant.]

Voilà ton virage à droite. Toi, tu voyais encore une route dégagée. Les conducteurs devant toi, eux, étaient déjà à l'arrêt, et leurs téléphones l'avaient dit à Waze. La comparaison avec l'habitude a dit « bouchon », et le calcul a jugé que ça valait le coup de te dérouter.

---

## 6. Fin (11:18 – 12:30)

[VISUEL : la chaîne entière en accéléré : ta flèche envoie un point, la vitesse, la frise des 48 demi-heures, le tronçon rouge, les icônes de signalement, l'itinéraire qui bascule.]

Bref, ton téléphone envoie sa position, Waze en tire ta vitesse, il la compare à huit semaines d'habitude, les signalements précisent, et toutes les quelques minutes, il se demande si ça vaut le coup de te faire tourner.

Tout ça pour une flèche bleue qui tourne à droite.

Donc la prochaine fois que tu es coincé dans un bouchon, Waze ouvert, pense à la phrase que l'ingénieur de Waze se répète dans ces moments-là : « J'attends ici, mais j'aide ceux qui vont prendre Waze après moi. » Les gens derrière lui, dit-il, auront peut-être un itinéraire qui contourne le bouchon.

[VISUEL : ta flèche, immobile dans le rouge ; derrière, loin, une autre flèche tourne à droite.]

Ton téléphone qui avance à deux à l'heure, en fait, c'est peut-être lui qui fait tourner à droite quelqu'un, derrière toi. Ce jour-là, le Karim, c'est toi.

[OPTIONNEL : CE QUI T'A LE PLUS SURPRIS DANS LA MACHINE DE WAZE, ET POURQUOI. UNE OU DEUX PHRASES.]

Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et si tu n'as pas encore vu comment Uber fait glisser ses petites voitures sur ta carte, c'est la vidéo juste là. On y croise même des voitures qui n'existaient peut-être pas.

[VISUEL : écran de fin, 20 s : vidéo Uber à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Visuel | Dézoom : la route évitée vire au rouge, sans signalement |
| 0:14 | Question centrale | « Alors comment il savait ? » |
| 0:15 | Plant | « Et dans la tienne » (récolté à la fin) |
| 0:22 | Teaser | Les conducteurs qui n'existaient pas, le faux bouchon à 8 km/h, arrêt sur image |
| 0:45 | Rappel | La vidéo Uber : « tout le monde fait le Karim » (fiche vers Uber) |
| 1:25 | Réaction | « Tu n'as touché à rien, et tu bosses déjà pour lui » |
| 1:53 | Calcul | 100 m en 10 s = 36 km/h |
| 2:28 | Pont | « Sauf qu'une vitesse, toute seule… » |
| 2:36 | Devinette | « Tu roules à vingt. Bouchon ou pas ? » |
| 3:00 | Appel à l'action | Abonnement (24 %) |
| 3:09 | Récolte | « d'habitude, c'est tout droit » : Waze connaît mieux que toi l'habitude de ta route |
| 3:38 | Chiffre | Quarante-huit mesures par jour, les huit derniers mardis |
| 4:28 | Humour | GTA 5 : le bouchon cinq étoiles |
| 4:40 | Humour | Vin Diesel écarté de la moyenne |
| 4:54 | Question | « Les gens qui appuient sur « signaler », ils servent à quoi ? » |
| 5:26 | Boucle refermée (1/2) | Il savait que ça bloquait, pas pourquoi |
| 5:47 | Image | Le pote qui ne répond plus depuis trois heures |
| 5:58 | Anecdote | Les cinq secondes de Petreanu, et la confiance |
| 6:32 | Honnêteté | « Waze ne le dit nulle part. On a cherché. » |
| 7:04 | Pont | « Des faux téléphones. Et Waze les a crus. » |
| 7:17 | Coupure musique (58 %) | Haïfa, 2014 |
| 7:43 | Escalade | Premier essai raté, deuxième essai raté |
| 8:26 | Révélation | Le bouchon à 8 km/h, quinze bots, « un bouchon de PNJ » |
| 8:34 | Conséquence | Le détour des chercheurs |
| 9:26 | Bilan | Les téléphones font le bouchon, même faux |
| 9:38 | Pont | « Un détour. Comme ton virage à droite. » |
| 9:50 | Boîte noire | L'équation non publiée |
| 10:15 | Humour | « C'est peut-être pas toi le Vin Diesel » |
| 10:58 | Boucle refermée (2/2) | « Voilà ton virage à droite », le titre payé |
| 11:38 | Citation | Le mantra de Petreanu |
| 11:58 | Retournement | « Le Karim, c'est toi » |
| 12:10 | Question du pilier | « Quelle appli je décortique ensuite ? », écran de fin vers Uber |

**Total** : 32 relances en 12 min 30, environ une toutes les 25 secondes. Le plus long trou : 0:45-1:25 (40 s), tenu par l'animation de Karim qui se multiplie.

**La relance forte** tombe à 58 % (7:17), au lieu de 73 % en V1. Sortir seulement le serveur de sessions, comme le proposait la V1, ne suffisait pas : ces 25 s étaient avant la coupure, donc la vidéo raccourcissait autant que le début, et la coupure restait à 72 %. Il fallait déplacer le faux bouchon avant le calcul.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:00-0:05 | Faible | « Tu râles » retarde la route rouge de 2 s | Il plante le « d'habitude » récolté en section 2 ; la route rouge arrive avant 0:07 |
| Section 1, les sources et le brevet | Moyen | 0:30-0:45 sans image forte, puis un brevet | Défilement rapide des documents ; le calcul « 100 m en 10 s = 36 km/h » à l'écran ; pas de noms d'inventeurs à voix haute |
| Section 2, après l'abonnement | Moyen | La règle de la doc, puis le niveau et le retard | La récolte du « d'habitude », les huit mardis superposés, la courbe rouge qui plonge, puis GTA et Vin Diesel dans les 40 s |
| Fin de la section 3, les deux minutes | Moyen | Un chiffre suivi d'une réserve | Il est séparé de la question du délai ; la question « combien de téléphones ? » ouvre tout de suite le faux bouchon |
| Relance (~60 %) | Élevé | Chute classique | Coupure musicale, Haïfa 2014, teaser du hook enfin payé, « bouchon de PNJ » |
| Section 5, l'équation | Moyen | Abstrait, juste après le sommet | Le pont « comme ton virage à droite », la boîte noire, Vin Diesel qui revient, puis la boucle du hook refermée |
| Fin | Moyen | Récapitulatif = signal de sortie | Une seule phrase de récap ; « le Karim, c'est toi » arrive dans les 25 s |

## Notes de montage

- **Composants réutilisés d'Uber** : la carte sombre, la carte du trajet (section 1), la voiture de Karim. À construire : la frise des 48 demi-heures avec les deux courbes et les huit mardis, le tronçon qui vire au rouge (même animation dans le hook, la section 2 et la section 4), la jauge 0 à 5, les téléphones fantômes et leurs points.
- **Pas d'accident à l'écran dans le hook** (2e vérif, `sources.md`, ligne 31) : une route rouge et des points arrêtés. Le premier accident n'apparaît qu'en section 3, avec son icône de signalement.
- **Pas de vraie appli Waze à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Pas de logo Waze dans l'animation hors miniature ; captures autorisées : la doc Waze Partners, l'article du blog Waze, le brevet, le PDF arXiv.
- **GTA 5 et Vin Diesel** : noms dits à voix haute, motion design seulement (des étoiles, pas d'image du jeu). Si tu reprends Monster Hunter, un court extrait de bande-annonce officielle est possible (règle du 19/10).
- **Chiffres d'exemple** : le « 36 km/h », le « +240 s » de la jauge et le gros retard de la section 5 sont des illustrations ; écris « exemple » à l'écran.
- **Énergie** : montées sur le tronçon rouge du hook, la devinette des 20 km/h, GTA, Vin Diesel, les cinq secondes de Petreanu, la coupure à 60 %, le bouchon de PNJ, « Comme ton virage à droite », « le Karim, c'est toi ».
- **Fiche pendant le plateau de rétention** : la fiche vers la vidéo Uber au moment du rappel « Tu te rappelles la vidéo sur Uber ? » (section 1).
- **Musique** : coupée à l'entrée de la section 4, elle revient à l'entrée de la section 5 (et non plus à la fin), pour que le calcul ne reste pas sur la basse sombre.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1 | « ses infos de bouchon sont fabriquées à partir des points GPS envoyés par les téléphones des gens qui conduisent avec l'appli » |
| 9 | « quand tu gardes l'appli ouverte, tu lui donnes, sans rien faire, la vitesse de la portion de route où tu es » |
| 14 | « Le brevet de Waze, déposé en deux mille huit […] il en tire ta vitesse » ; « un brevet, ça décrit ce que le système peut faire, pas forcément ce que Waze fait aujourd'hui » |
| 21 ⚠️ | « fin deux mille vingt-deux, Waze comptait environ cent cinquante millions d'utilisateurs par mois » |
| 3, 16 | « un bouchon, c'est une comparaison : on roule nettement moins vite que d'habitude » ; « quand un tronçon roule sous sa vitesse moyenne habituelle pour cette heure et ce jour […] recoupe avec les signaux GPS et les signalements » |
| 7 | « la vitesse moyenne de chaque demi-heure, pour chaque jour de la semaine. Ça fait quarante-huit mesures par jour » |
| 8 | « il s'appuie sur les huit dernières semaines environ » ; « à peu près les huit derniers mardis à huit heures et demie » (déduction des faits 7 et 8 : une case par demi-heure et par jour de la semaine, sur huit semaines) |
| 2 ⚠️, 5 | « Un niveau, de zéro, fluide, à cinq, bloqué. Et le retard en secondes, par rapport à la vitesse fluide du tronçon, la plus haute qu'on y ait mesurée » |
| 40 | « le niveau de recherche de GTA cinq. Zéro étoile […] Cinq étoiles » |
| 11 | « Waze écarte les extrêmes […] Il tient même compte du type de véhicule » |
| 39 | « signaler un accident, la police ou un danger sur la route » |
| 4 ⚠️ | « tes signalements s'affichent comme des alertes, et ils pèsent aussi sur la façon dont Waze repère les bouchons » |
| 18 ⚠️ | « le bouchon sort d'abord des vitesses. Les signalements viennent ensuite le confirmer et le préciser » |
| 19 ⚠️, 29, 31 | « Waze savait que ça bloquait. Par contre, il ne savait pas pourquoi » ; hook : « personne ne l'avait signalé », sans accident ni délai |
| 32 ⚠️, 36 | l'anecdote de la voiture sur le bas-côté, « à ses débuts dans la boîte », placée dans la partie signalements ; « c'est comme ça […] qu'il a su qu'il pouvait faire confiance à l'appli » |
| 6, 28 | « le flux qu'il envoie à ses villes partenaires : il est mis à jour toutes les deux minutes » ; « Waze ne le dit nulle part » (délai et nombre de téléphones) |
| 15 ⚠️, 34 | « quatre chercheurs du Technion » ; « un bouchon apparaît. À huit kilomètres-heure. Il a suffi de quinze bots » ; « Waze change l'itinéraire qu'il proposait aux chercheurs » ; « une vingtaine de minutes » ; « ils pourraient le faire, en théorie » |
| 38 | « des téléphones Android simulés, avec la vraie appli Waze dedans […] positions GPS truquées » ; l'ordre des essais : immobiles, puis ralentissement progressif, puis départ à soixante-dix |
| 16 | bots immobiles, puis ralentissement sur un campus où l'on roule lentement, sans bouchon ; « son calcul est relatif » (déduction des chercheurs, dite comme telle) |
| 17 | « en deux mille quatorze, Waze ne faisait aucun effort visible pour distinguer un humain d'une machine » |
| 28 | « Quinze, c'est ce qui a suffi sur leur campus ; Waze, lui, n'a jamais donné de seuil » |
| 10 | « il les mélange dans une équation qui calcule ta vitesse la plus probable. L'équation exacte […] il ne la publie pas » |
| 13 | « il penche volontairement du côté prudent […] Waze prévoit large exprès » |
| 12 | « il refait le point toutes les quelques minutes […] pour une minute de retard, aucun intérêt » |
| 35, 30 | « Toi, tu voyais encore une route dégagée. Les conducteurs devant toi, eux, étaient déjà à l'arrêt » ; le titre et la miniature : le ralentissement se voit sans signalement ; aucune avance chiffrée |
| 33 ⚠️, 37 | « J'attends ici, mais j'aide ceux qui vont prendre Waze après moi » ; « Les gens derrière lui, dit-il, auront peut-être un itinéraire qui contourne le bouchon » |

**Non utilisés exprès** : 20 (serveur de sessions, passé en réserve) ; 22 (FreeMap Israel, coupé) ; 23 (rachat par Google, angle business de Thibaut Dcode) ; 24, 25, 26, 27 (interdits par la 2e vérif) ; « trois minutes plus tard » et « un accident » (ligne 29).

## Questions pour l'auteur

1. **Ton vécu avec Waze** : un détour qui t'a sauvé, ou un qui t'a envoyé dans un chemin de terre ? Si tu n'en as pas, on coupe le crochet de la section 1. Tu l'utilises en Côte d'Ivoire, en France, ailleurs ?
2. **« Moi, je suis dev. Alors j'ai voulu voir la machine de l'intérieur »** : ça te va, ou tu as une vraie raison de t'intéresser à Waze (une remarque d'un pote, un détour, un commentaire) ? Ta raison remplacerait la phrase.
3. **Les blagues** : j'ai remplacé Monster Hunter par le niveau de recherche de GTA 5, qui va pile de 0 à 5 étoiles et parle de route et de police. Dans Monster Hunter, les quêtes ne commencent pas à zéro étoile et cinq étoiles n'est pas le sommet : un joueur le relèvera. Tu gardes GTA ou tu reviens à Monster Hunter ? Vin Diesel revient deux fois (les extrêmes, puis « c'est peut-être pas toi le Vin Diesel ») : trop, ou ça fait running gag ? Et le « bouchon de PNJ » ?
4. **« Le Karim, c'est toi »** : il est maintenant appuyé par la phrase de l'ingénieur (« les gens derrière moi auront peut-être un itinéraire qui contourne le bouchon »). Le rappel au chauffeur d'Uber te parle, ou c'est trop appuyé ?
5. **Ton enjeu** (optionnel, fin) : qu'est-ce qui te fascine, toi, en tant que dev : que des millions d'inconnus fassent la carte sans le savoir, ou que ce soit au fond une simple comparaison avec l'habitude ?

## Bloc en réserve : le serveur de sessions (~25 s)

À remettre à la fin de la section 5, après « te dérouter », si la vidéo est trop courte au montage, ou en commentaire épinglé. Version corrigée (fait 20 ⚠️) :

> Sauf que ça, il le fait pour chaque conducteur en même temps. Ton itinéraire en cours, ta position, tes signalements : chez Waze, ça vit dans un serveur de sessions. Et en test de charge, il a encaissé des pointes jusqu'à un million de lectures par seconde, avec une réponse en moins d'une milliseconde.
>
> [VISUEL : la carte se dézoome, des milliers de flèches ; un compteur « 1 000 000 lectures / s » avec, en petit, « test de charge ».]

La V1 ajoutait « Un million de fois par seconde, un serveur se demande : « il en est où, lui ? » » : c'est un résultat de test de charge, pas le trafic réel, et une lecture n'est pas forcément une position. Ne la remets pas.
