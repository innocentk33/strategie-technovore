# Waze : script v1

**Titre** : *Comment Waze sait qu'il y a un bouchon avant que tu le voies*

**Durée** : environ 1 740 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft, pauses et improvisations comprises) : environ 12 min ; à 165 mots/min : 10 min 30 ; en coupes serrées comme sur Uber (~180 mots/min) : 9 min 40 plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : ton virage à droite. Le hook montre le détour et la route rouge que personne n'a signalée ; la vidéo démonte la machine dans l'ordre où elle travaille : le téléphone qui sert de capteur, la comparaison avec l'habitude, les signalements, puis le calcul qui décide de te faire tourner. Le faux bouchon de 2014 prouve que ce sont bien les téléphones qui font le bouchon, et la fin retourne la situation : c'est toi, coincé, qui fais tourner quelqu'un d'autre.

**Boucles ouvertes** :
1. « Alors comment il savait ? » (hook, 0:15) : refermée en deux temps, section 2 (la comparaison) et section 4 (« voilà ton virage à droite »).
2. « Des chercheurs ont fabriqué un bouchon qui n'existait pas » (hook, 0:25) : refermée dans la section 5.
3. « Combien de temps il lui faut pour repérer un bouchon ? » (section 3) : refermée honnêtement, Waze ne le publie pas.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (la famille de cartes sombres d'Uber) ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de [`sources.md`](sources.md), et des ⚠️ avec la formulation qu'il donne.

---

## 0. Hook (0:00 – 0:30) · objectif : 75 % à 0:15

[VISUEL : un téléphone en gros plan, la carte sombre de la vidéo Uber, ta flèche qui roule. L'itinéraire bleu tourne d'un coup à droite. Pas de titre, pas de logo.]

Waze te fait tourner à droite. Tu râles, ton trajet habituel, c'est tout droit.

[VISUEL : dézoom : sur la route évitée, une file de points qui ne bougent plus, le tronçon vire au rouge. Aucune icône de signalement, aucun accident à l'écran.]
[SON : un « tic » sec quand le tronçon passe au rouge.]

Sauf que sur la route que tu viens d'éviter, tout le monde est à l'arrêt. Et personne ne l'avait signalé. Alors comment il savait ?

En fait, la réponse est dans ta poche : ton téléphone fait partie de la machine. Et en deux mille quatorze, des chercheurs s'en sont servis pour fabriquer un bouchon qui n'existait pas. Waze l'a affiché.

[VISUEL : teaser d'une seconde : quinze points fantômes ralentissent, la route devient rouge, « 8 km/h ». Arrêt sur image.]

---

## 1. Ton téléphone, ce capteur (0:30 – 2:50)

Je suis dev, et quand une appli me fait un coup pareil, j'ai besoin de savoir comment elle a fait. Donc j'ai lu ce que Waze publie lui-même : la doc qu'il donne aux villes partenaires, un article d'un de ses ingénieurs, et même son brevet.

[VISUEL : défilement rapide des trois documents, seules les dates restent nettes. Texte : « Toutes les sources en description ».]

[TON EXPÉRIENCE AVEC WAZE, SI TU EN AS UNE : UN DÉTOUR QUI T'A SAUVÉ, OU UN QUI T'A ENVOYÉ DANS UN CHEMIN DE TERRE. DEUX PHRASES MAXIMUM.]

Tu te rappelles la vidéo sur Uber ? Le téléphone de Karim, le chauffeur, envoyait sa position pour que tu le voies arriver sur ta carte. Chez Waze, c'est le même principe, sauf que tout le monde fait le Karim.

[VISUEL : la carte du trajet de la vidéo Uber revient ; la voiture de Karim se multiplie en des centaines de flèches Waze sur le périph.]

La doc de Waze le dit noir sur blanc : ses infos de bouchon sont fabriquées à partir des points GPS envoyés par les téléphones des gens qui conduisent avec l'appli. Et l'ingénieur le dit encore plus simplement : quand tu gardes l'appli ouverte, tu lui donnes, sans rien faire, la vitesse de la portion de route où tu es.

Sans rien faire. Tu n'as touché à rien, et tu bosses déjà pour lui.

[VISUEL : ta flèche émet un petit point à intervalles réguliers ; chaque point porte une heure.]

Mais comment on passe d'une position à une vitesse ? Pour faire simple, c'est du niveau collège. Le brevet de Waze, déposé en deux mille huit, décrit le truc : chaque conducteur envoie sa position à intervalles réguliers, avec l'heure. Le serveur regarde de combien tu as bougé entre deux envois, et il en tire ta vitesse. Cent mètres en dix secondes ? Tu roules à trente-six kilomètres-heure.

[VISUEL : deux points sur la route, une règle « 100 m », un chrono « 10 s », puis « 36 km/h ».]

Ensuite, il fait la moyenne de tous ceux qui sont sur la même route, et il obtient la vitesse du trafic. Bon, un brevet, ça décrit ce que le système peut faire, pas forcément ce que Waze fait aujourd'hui. Mais la doc actuelle va exactement dans ce sens.

Et ça colle avec ses origines. Waze est né d'une carte communautaire israélienne, FreeMap Israel, lancée en deux mille six. Dès le départ, ce sont les conducteurs qui font la carte. Fin deux mille vingt-deux, ils étaient environ cent cinquante millions par mois. Ça fait un paquet de capteurs qui roulent.

Du coup, Waze connaît ta vitesse. Sauf qu'une vitesse, toute seule, ça ne dit pas s'il y a un bouchon.

---

## 2. C'est quoi, un bouchon, pour une machine ? (2:50 – 5:00)

[VISUEL : deux routes côte à côte, un point à 20 km/h sur chacune : une petite rue avec des dos-d'âne, une voie rapide.]

Petite devinette. Tu roules à vingt kilomètres-heure. Bouchon ou pas ?

[VISUEL : deux secondes de silence, les deux points avancent.]

Bah ça dépend où. Dans une petite rue pleine de dos-d'âne, vingt, c'est normal. Sur une voie rapide, à vingt, c'est la catastrophe. Donc pour Waze, un bouchon, c'est une comparaison : on roule nettement moins vite que d'habitude, à cette heure-là, sur ce bout de route.

**Abonnement (≈ 3:25, 28 % de la vidéo, juste après la première révélation)**

Si tu aimes voir ce qui tourne vraiment derrière les applis de ta poche, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, les deux routes restent à l'écran.]

Du coup, « d'habitude », Waze le sait avec une précision un peu flippante. Pour chaque tronçon de route, il garde la vitesse moyenne de chaque demi-heure de chaque jour de la semaine. Quarante-huit mesures par jour, et par tronçon. Un jour normal, il s'appuie sur les huit dernières semaines environ.

[VISUEL : une frise de 48 cases pour un mardi ; une courbe grise, la vitesse habituelle, qui creuse à 8 h 30 et à 18 h.]

En gros, Waze sait mieux que toi à quoi ressemble ta rue le mardi à huit heures et demie.

Et en effet, la doc de Waze donne la règle. Quand un tronçon roule sous sa vitesse moyenne habituelle pour cette heure et ce jour, Waze le marque comme ralentissement ou bouchon. Puis il recoupe avec les signaux GPS et les signalements.

[VISUEL : la courbe d'aujourd'hui, en rouge, plonge sous la courbe grise ; sur la carte, le tronçon vire au rouge au même instant.]
[SON : le même « tic » que dans le hook.]

Et pour noter la gravité, il garde une deuxième référence : la vitesse fluide du tronçon, la plus haute qu'on y ait mesurée. Et chaque bouchon reçoit une note, de zéro, fluide, à cinq, bloqué, avec le retard en secondes par rapport à cette vitesse fluide.

[VISUEL : une jauge de 0 à 5 en étoiles, façon écran de quête ; « retard : +240 s » en exemple.]

C'est le niveau de quête de Monster Hunter. Zéro étoile, tu passes. Cinq étoiles, prépare tes potions.

Et avant de faire sa moyenne, Waze écarte les extrêmes : le conducteur qui se traîne et celui qui se prend pour Vin Diesel. Il tient même compte du type de véhicule, parce qu'une moto ou un bus ne roulent pas comme toi.

[VISUEL : deux points sortent du lot et sont barrés : un escargot, une voiture avec des flammes. Une moto et un bus ont leur propre couleur.]

Voilà comment Waze voit un bouchon sans que personne ne dise rien. Mais alors, les gens qui appuient sur « signaler », ils servent à quoi ?

---

## 3. Les signalements, le deuxième étage (5:00 – 6:55)

[VISUEL : le menu de signalement, reconstruit en motion design (pas la vraie appli) : accident, police, objet sur la route.]

Tu vois le bouton pour signaler un accident, la police ou un objet sur la route ? D'après la doc, tes signalements s'affichent comme des alertes, et ils pèsent aussi sur la façon dont Waze repère les bouchons.

Donc le bouchon sort d'abord des vitesses. Les signalements viennent ensuite le confirmer et le préciser.

[VISUEL : une maison à deux étages : au rez-de-chaussée, les vitesses ; au premier, les icônes de signalement qui se posent sur le tronçon rouge.]

Et ça explique un truc du début. Tu te rappelles la route où tout le monde était à l'arrêt ? Waze savait que ça bloquait. Par contre, il ne savait pas pourquoi. Accident, travaux, camion en panne : tant que personne ne le signale, pour lui, ce sont juste des téléphones qui n'avancent plus.

[VISUEL : retour sur la route rouge du hook ; un point d'interrogation au-dessus du tronçon.]

C'est ton pote qui voit que tu n'as pas répondu depuis trois heures. Il sait que tu es occupé. Il ne sait pas si tu es en réunion ou au lit.

Et quand quelqu'un signale, ça peut aller très vite. Yigal Petreanu, ingénieur chez Waze, raconte qu'au début, il recevait le signalement d'une voiture sur le bas-côté, et cinq secondes plus tard, il voyait la voiture.

[VISUEL : une alerte « voiture sur le bas-côté » s'affiche ; un compteur « 5 s » ; la voiture apparaît au bord de la route.]

Cinq secondes. Quelqu'un, un peu plus loin devant, avait pris le temps d'appuyer sur un bouton pour un inconnu.

Alors forcément, tu dois te demander combien de temps il faut à Waze pour repérer un bouchon. Pour ses villes partenaires, il envoie toutes ces infos dans un flux mis à jour toutes les deux minutes. Mais le délai de détection, ou le nombre de téléphones qu'il faut pour déclencher un bouchon, Waze ne le dit nulle part. J'ai cherché.

[VISUEL : les pages de la doc défilent, une loupe passe dessus ; texte : « délai de détection : non publié ».]

Bref, Waze sait où ça coince. Reste la question qui t'a fait cliquer : pourquoi il t'a fait tourner à droite, à ce moment-là ?

---

## 4. Le calcul : pourquoi il t'a fait tourner (6:55 – 8:45)

[VISUEL : la carte du hook revient, ta flèche et l'heure d'arrivée affichée en haut.]
[SON : ding de chapitre.]

En fait, pour te donner une heure d'arrivée, Waze a deux sources : ce qui se passe maintenant, et l'historique de ses quarante-huit demi-heures. Et il les mélange dans une équation qui calcule ta vitesse la plus probable. L'équation exacte, évidemment, il ne la publie pas.

[VISUEL : deux flux, « maintenant » et « habitude », qui se versent dans une boîte noire marquée « ? » ; il en sort une heure d'arrivée.]

Et il penche volontairement du côté prudent : pour Waze, mieux vaut que tu arrives pile à l'heure ou un peu en avance. Du coup, quand tu arrives deux minutes avant l'heure annoncée, c'est voulu.

Une fois que tu roules, il refait le point toutes les quelques minutes. Si ça change un peu, il te prévient juste du retard. L'ingénieur le dit : pour une minute de retard, aucun intérêt à t'envoyer sur un tout nouvel itinéraire. Waze garde exprès des trajets stables, parce qu'un GPS qui change d'avis tous les cent mètres, tu le désinstalles. Mais si ça change beaucoup, il te trouve une autre route.

[VISUEL : ta flèche ; un compteur « +1 min » : l'itinéraire ne bouge pas. Puis un gros retard (« exemple » écrit en petit) : l'itinéraire bascule à droite.]
[SON : le clignotant.]

Voilà ton virage à droite. Les téléphones devant toi ont ralenti, la comparaison avec l'habitude a dit « bouchon », et le calcul a jugé que ça valait le coup de te dérouter.

Sauf que ça, il le fait pour chaque conducteur en même temps. Ton itinéraire en cours, ta position, tes signalements : chez Waze, ça vit dans un serveur de sessions. En test de charge, il a encaissé des pointes jusqu'à un million de lectures par seconde, avec une réponse en moins d'une milliseconde.

[VISUEL : la carte se dézoome, des milliers de flèches ; un compteur « 1 000 000 lectures / s » avec, en petit, « test de charge ».]

Un million de fois par seconde, un serveur se demande : « il en est où, lui ? »

Bon. Si je reprends : chez Waze, ce sont les téléphones qui fabriquent le bouchon. Et si quelqu'un fabriquait des faux téléphones ?

---

## 5. Le bouchon qui n'existait pas (8:45 – 10:45) · relance forte

[SON : la musique coupe net, une seconde de silence, puis une basse sombre.]
[VISUEL : un campus vu du ciel, de nuit ; un texte « Haïfa, 2014 ».]

En deux mille quatorze, quatre chercheurs du Technion, une université israélienne à Haïfa, se posent exactement cette question. Ils fabriquent des « bots conducteurs » : des faux téléphones, qui envoient à Waze des positions GPS truquées.

Premier essai : ils posent leurs bots sur le campus, immobiles. Et là, rien. Aucun bouchon. D'après eux, Waze voyait sans doute des gens qui venaient d'ouvrir l'appli sans avoir démarré.

[VISUEL : quinze points fantômes immobiles sur un parking ; la route reste grise.]

Ils essaient aussi de les faire ralentir dans une zone déjà lente. Toujours rien. Et ça, tu sais déjà pourquoi : sur une route lente depuis toujours, rouler lentement, c'est normal. Les chercheurs en déduisent que le calcul de Waze est relatif, une comparaison avec l'habitude. Exactement ce que dit la doc.

Donc ils changent de méthode. Ils font rouler leurs bots à soixante-dix kilomètres-heure, puis ils les font ralentir.

[VISUEL : les points fantômes filent, puis freinent ensemble ; la route vire au rouge, « 8 km/h ».]
[SON : le « tic » du hook, plus grave.]

Et cette fois, sur la carte, un bouchon apparaît. À huit kilomètres-heure. Il a suffi de quinze bots.

Un bouchon de PNJ.

En effet, l'itinéraire que Waze proposait aux chercheurs a changé : un kilomètre et demi et trois minutes avant, un kilomètre six et quatre minutes après. Le faux bouchon est même resté affiché une vingtaine de minutes après l'arrêt des bots.

[VISUEL : deux itinéraires superposés, « 1,5 km · 3 min » puis « 1,6 km · 4 min » ; un chrono « ~20 min » sur la route rouge vide.]

Et d'après l'étude, en deux mille quatorze, Waze ne faisait aucun effort visible pour distinguer un humain d'une machine.

Attention à ce qu'on en fait, quand même. Ce qu'ils ont montré, c'est l'itinéraire de leur propre test qui change ; ils écrivent qu'ils pourraient, en théorie, envoyer d'autres conducteurs ailleurs. Et c'était il y a plus de dix ans : l'algorithme a pu changer depuis.

[VISUEL : bandeau « Étude de 2014. Waze a pu changer depuis. »]

Mais cette expérience, c'est la meilleure preuve de tout ce qu'on vient de voir. Chez Waze, le bouchon, ce sont les téléphones qui le font. Même quand ces téléphones sont faux.

---

## 6. Fin (10:45 – 12:00)

[SON : la musique du début revient.]
[VISUEL : la chaîne entière en accéléré : ta flèche envoie un point, la vitesse, la frise des 48 demi-heures, le tronçon rouge, les icônes de signalement, l'itinéraire qui bascule.]

Bref, si je reprends depuis le début : ton téléphone envoie sa position, Waze en tire ta vitesse, il la compare à huit semaines d'habitude, les signalements précisent, et toutes les quelques minutes, il se demande si ça vaut le coup de te faire tourner.

Tout ça pour une flèche bleue qui tourne à droite.

Donc la prochaine fois que tu es coincé dans un bouchon, Waze ouvert, pense à la phrase que se répète l'ingénieur de Waze : « J'attends ici, mais j'aide ceux qui vont prendre Waze après moi. »

[VISUEL : ta flèche, immobile dans le rouge ; derrière, loin, une autre flèche tourne à droite.]

Parce que ton téléphone qui avance à deux à l'heure, en fait, c'est lui qui fait tourner à droite quelqu'un derrière toi. Ce jour-là, le Karim, c'est toi.

[OPTIONNEL : CE QUI T'A LE PLUS SURPRIS DANS LA MACHINE DE WAZE, ET POURQUOI. UNE OU DEUX PHRASES.]

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et si tu n'as pas encore vu comment Uber fait glisser ses petites voitures sur ta carte, c'est la vidéo juste là. On y croise même des voitures qui n'existaient peut-être pas.

[VISUEL : écran de fin, 20 s : vidéo Uber à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Visuel | Dézoom : la route évitée vire au rouge, sans signalement |
| 0:15 | Question centrale | « Alors comment il savait ? » |
| 0:25 | Teaser | Le faux bouchon à 8 km/h, arrêt sur image |
| 1:05 | Rappel | La vidéo Uber : « tout le monde fait le Karim » (fiche vers Uber) |
| 1:50 | Calcul | 100 m en 10 s = 36 km/h |
| 2:50 | Devinette | « Tu roules à vingt. Bouchon ou pas ? » |
| 3:25 | Appel à l'action | Abonnement |
| 3:45 | Chiffre | Quarante-huit mesures par jour, huit semaines |
| 4:25 | Humour | Monster Hunter : le bouchon cinq étoiles |
| 4:40 | Humour | Vin Diesel écarté de la moyenne |
| 5:00 | Changement de chapitre | Les signalements, le deuxième étage |
| 5:30 | Boucle refermée (1/2) | Il savait que ça bloquait, pas pourquoi |
| 5:55 | Image | Le pote qui ne répond pas depuis trois heures |
| 6:15 | Anecdote | Les cinq secondes de Petreanu |
| 6:35 | Honnêteté | « Waze ne le dit nulle part. J'ai cherché. » |
| 7:00 | Boîte noire | L'équation non publiée |
| 7:50 | Boucle refermée (2/2) | « Voilà ton virage à droite » |
| 8:15 | Chiffre | Un million de lectures par seconde (test de charge) |
| 8:40 | Question | « Et si quelqu'un fabriquait des faux téléphones ? » |
| 8:45 | Coupure musique | Haïfa, 2014 |
| 9:35 | Révélation | Le bouchon à 8 km/h, quinze bots, « un bouchon de PNJ » |
| 10:30 | Bilan | Les téléphones font le bouchon, même faux |
| 11:20 | Retournement | « Le Karim, c'est toi » |
| 11:45 | Question du pilier | « Quelle appli je décortique ensuite ? », écran de fin vers Uber |

**Total** : 24 relances en 12 min, environ une toutes les 30 secondes. Aucun trou de plus de 60 s.

**À propos de la relance forte** : à 145 mots/min, la coupure tombe à 8:45, soit 73 % de la vidéo. Le vrai creux de 60 % (≈ 7:10) est tenu par la boîte noire et par la fermeture de la boucle « voilà ton virage à droite ». Si le grill veut la coupure à 60 %, déplace le paragraphe du serveur de sessions dans la réserve ou en commentaire épinglé (≈ 25 s gagnées).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:00-0:05 | Moyen | « Tu râles » peut sonner comme du remplissage | La phrase dit l'enjeu (on doute de Waze) ; si le grill la juge molle, la couper et ouvrir sur « Waze te fait tourner à droite. Sur la route que tu viens d'éviter… » |
| Section 1, le brevet | Moyen | Un brevet et des noms, c'est sec | Le calcul « 100 m en 10 s = 36 km/h » à l'écran ; pas de noms d'inventeurs à voix haute |
| Section 2, après l'abonnement | Élevé | La règle de la doc, la vitesse fluide et la note de 0 à 5 s'enchaînent | La courbe rouge qui plonge, puis le gag Monster Hunter et Vin Diesel dans les 40 s |
| Section 4, l'équation | Moyen | Abstrait | La boîte noire « ? », puis le retour au virage à droite du hook |
| Relance (~60 %) | Élevé | Chute classique | Coupure musicale, question « et si quelqu'un fabriquait des faux téléphones ? », teaser du hook enfin payé |
| Fin | Moyen | Récapitulatif = signal de sortie | Le retournement « le Karim, c'est toi » arrive juste après, en moins de 30 s |

## Notes de montage

- **Composants réutilisés d'Uber** : la carte sombre, la carte du trajet (section 1), la voiture de Karim. À construire : la frise des 48 demi-heures avec les deux courbes, le tronçon qui vire au rouge (même animation dans le hook, la section 2 et la section 5), la jauge 0 à 5, les points fantômes.
- **Pas d'accident à l'écran dans le hook** (2e vérif, `sources.md`, ligne 31) : une route rouge et des points arrêtés. Le premier accident n'apparaît qu'en section 3, avec son icône de signalement.
- **Pas de vraie appli Waze à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Pas de logo Waze dans l'animation hors miniature ; captures autorisées : la doc Waze Partners, l'article du blog Waze, le brevet, le PDF arXiv.
- **Vin Diesel et Monster Hunter** : nom dit à voix haute, motion design seulement ; pour Monster Hunter, un court extrait de bande-annonce officielle est possible (règle du 19/10).
- **Chiffres d'exemple** : le « +240 s » de la jauge et le gros retard de la section 4 sont des illustrations ; écris « exemple » à l'écran.
- **Énergie** : montées sur le tronçon rouge du hook, la devinette des 20 km/h, Vin Diesel, les cinq secondes de Petreanu, la coupure à 60 %, le bouchon de PNJ, « le Karim, c'est toi ».
- **Fiche pendant le plateau de rétention** : la fiche vers la vidéo Uber au moment du rappel « Tu te rappelles la vidéo sur Uber ? » (section 1).

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1 | « ses infos de bouchon sont fabriquées à partir des points GPS envoyés par les téléphones des gens qui conduisent avec l'appli » |
| 9 | « quand tu gardes l'appli ouverte, tu lui donnes, sans rien faire, la vitesse de la portion de route où tu es » |
| 14 | « Le brevet de Waze, déposé en deux mille huit […] il en tire ta vitesse » ; « un brevet, ça décrit ce que le système peut faire, pas forcément ce que Waze fait aujourd'hui » |
| 22 ⚠️ | « Waze est né d'une carte communautaire israélienne, FreeMap Israel, lancée en deux mille six » |
| 21 ⚠️ | « Fin deux mille vingt-deux, ils étaient environ cent cinquante millions par mois » |
| 3, 16 | « un bouchon, c'est une comparaison : on roule nettement moins vite que d'habitude » ; « quand un tronçon roule sous sa vitesse moyenne habituelle pour cette heure et ce jour […] recoupe avec les signaux GPS et les signalements » |
| 7 | « la vitesse moyenne de chaque demi-heure de chaque jour de la semaine. Quarante-huit mesures par jour, et par tronçon » |
| 8 | « il s'appuie sur les huit dernières semaines environ » |
| 2 ⚠️ | « la vitesse fluide du tronçon, la plus haute qu'on y ait mesurée » |
| 5 | « une note, de zéro, fluide, à cinq, bloqué, avec le retard en secondes » |
| 11 | « Waze écarte les extrêmes […] Il tient même compte du type de véhicule » |
| 4 ⚠️ | « tes signalements s'affichent comme des alertes, et ils pèsent aussi sur la façon dont Waze repère les bouchons » |
| 18 ⚠️ | « le bouchon sort d'abord des vitesses. Les signalements viennent ensuite le confirmer et le préciser » |
| 19 ⚠️, 29, 31 | « Waze savait que ça bloquait. Par contre, il ne savait pas pourquoi » ; hook : « personne ne l'avait signalé », sans accident ni délai |
| 32 ⚠️ | l'anecdote de la voiture sur le bas-côté, placée dans la partie signalements |
| 6, 28 | « un flux mis à jour toutes les deux minutes » pour les villes partenaires ; « le délai de détection […] Waze ne le dit nulle part » |
| 10 | « il les mélange dans une équation qui calcule ta vitesse la plus probable. L'équation exacte […] il ne la publie pas » |
| 13 | « il penche volontairement du côté prudent » |
| 12 | « il refait le point toutes les quelques minutes […] pour une minute de retard, aucun intérêt » |
| 20 ⚠️ | « En test de charge, il a encaissé des pointes jusqu'à un million de lectures par seconde, avec une réponse en moins d'une milliseconde » |
| 15 ⚠️, 34 | « quatre chercheurs du Technion » ; « un bouchon apparaît. À huit kilomètres-heure. Il a suffi de quinze bots » ; « l'itinéraire que Waze proposait aux chercheurs a changé » ; « une vingtaine de minutes » |
| 16 | bots immobiles et zone déjà lente sans bouchon ; « le calcul de Waze est relatif » (déduction des chercheurs, dite comme telle) |
| 17 | « en deux mille quatorze, Waze ne faisait aucun effort visible pour distinguer un humain d'une machine » |
| 33 ⚠️ | « J'attends ici, mais j'aide ceux qui vont prendre Waze après moi » |
| 35, 30 | le titre et la miniature : le ralentissement se voit sans signalement ; aucune avance chiffrée |

**Non utilisés exprès** : 23 (rachat par Google, angle business de Thibaut Dcode) ; 24, 25, 26, 27 (interdits par la 2e vérif) ; « trois minutes plus tard » et « un accident » (ligne 29).

## Questions pour l'auteur

1. **Ton vécu avec Waze** : un détour qui t'a sauvé, ou un qui t'a envoyé dans un chemin de terre ? Si tu n'en as pas, on coupe le crochet de la section 1. Tu l'utilises en Côte d'Ivoire, en France, ailleurs ?
2. **Ton enjeu** : pour Uber, c'était « mon pote avait raison ? ». Ici, qu'est-ce qui te fascine, toi, en tant que dev : que des millions d'inconnus fassent la carte sans le savoir, ou que ce soit au fond une simple comparaison avec l'habitude ? Ta réponse peut remplacer le crochet optionnel de la fin.
3. **Les blagues** : Monster Hunter (le niveau de quête), Vin Diesel (rappel du gag Fast and Furious d'Uber) et le « bouchon de PNJ » sont-ils dans ton humour ? Tu as mieux pour les quinze bots ?
4. **« Le Karim, c'est toi »** : le rappel au chauffeur d'Uber te parle, ou c'est trop appuyé ?
5. **Le hook** : tu gardes « Tu râles, ton trajet habituel, c'est tout droit », ou tu préfères aller directement à la route rouge ?
