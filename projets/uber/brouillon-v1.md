# Uber : brouillon V1 du script

**Titre** (celui de la fiche) : *Le génie caché derrière la carte en temps réel d'Uber*

**Durée** : environ 1 810 mots de voix off, soit 11 min 40 à 155 mots/min. Sans les deux blocs coupables (✂️ SSE/gRPC et Kalman), environ 1 690 mots, soit 10 min 55. À recaler après la première prise du clone.

**Fil rouge** : on suit la position d'un seul chauffeur, de son téléphone jusqu'à ton écran, en trois étapes : trouver, envoyer, afficher. Chaque étape pose un problème que personne ne voit. Le hook ouvre une question (« ces voitures existent-elles vraiment ? ») qui n'est résolue qu'à 9:50.

**Ce qui change par rapport à Philipp Lackner** :
- les hexagones passent en premier, parce que c'est la promesse de la miniature ;
- on ajoute le GPS qui se trompe de 50 m en ville (absent de sa vidéo) et la parenthèse sur le filtre de Kalman ;
- on retire la partie sur les serveurs « edge » : je n'ai pas trouvé de source Uber pour le chiffre de 100 ms ;
- tous les chiffres viennent du blog Uber Engineering (sources en bas).

**Conventions** (les mêmes que pour Claude #1) : texte normal = voix off. `[VISUEL : …]` = animation Remotion ou capture. `[SON : …]` = bruitage ou musique. `> ⚠️ À VÉRIFIER` = fait à confirmer avant d'enregistrer la voix. Les nombres sont écrits en lettres pour le clone vocal. On tutoie le spectateur, comme dans le hook validé (« Ouvre Uber »).

---

## 0. Hook (0:00 – 0:33) · objectif : 70 % de rétention à 0:30

**Accroche (0:00 – 0:05)**

[VISUEL : un téléphone en gros plan, une carte sombre, des petites voitures qui glissent autour du point bleu. Pas de titre, pas de logo.]

Ouvre Uber. Tu vois ces petites voitures qui bougent autour de toi ? Pour les afficher, Uber a dû découper la planète en hexagones.

**Promesse (0:05 – 0:15)**

[VISUEL : dézoom d'un coup : la rue, Paris, la France, puis la Terre entière couverte d'hexagones lumineux.]
[SON : whoosh sur le dézoom, un « tic » à chaque palier.]

Près de cinq cent soixante-dix mille milliards d'hexagones. Aujourd'hui, on suit une de ces voitures, du téléphone du chauffeur jusqu'à ton écran.

**Enjeu (0:15 – 0:30)**

Sur ce trajet, trois problèmes que tu ne vois jamais. Un serveur noyé sous les questions. Un GPS qui se trompe de cinquante mètres. Et une question posée en 2015 : est-ce que toutes ces voitures existent vraiment ?

[VISUEL : une des voitures devient transparente, clignote, puis disparaît.]

---

## 1. Le pote qui avait lu le blog (0:33 – 1:18)

Un jour, un pote m'a dit : « Les ingés d'Uber, c'est des génies. » Il avait lu leur blog d'ingénierie.

Moi, j'ai fait comme tout dev qui se respecte : je ne l'ai pas cru, et je suis allé vérifier. J'ai lu les articles, un par un.

Il avait raison.

[VISUEL : défilement rapide des articles du blog Uber Engineering, seules les dates restent nettes.]

Tout ce que je vais te montrer vient de ces articles, écrits par les ingénieurs eux-mêmes. Les liens sont en description.

Uber, aujourd'hui, c'est plus de quarante millions de courses et de livraisons par jour. Et toutes les quelques secondes, le téléphone de chaque chauffeur envoie sa position.

[VISUEL : Karim en 2D, dans sa voiture près de la gare de Lyon. Un petit point lumineux part de son téléphone.]

Prenons Karim, chauffeur à Paris. Sa position doit arriver sur ton écran, deux rues plus loin. Suivons-la.

[VISUEL : la « carte du trajet », trois étapes : Trouver, Envoyer, Afficher. Elle revient au début de chaque chapitre.]

---

## 2. Étape 1 : trouver les voitures autour de toi (1:18 – 4:23)

[VISUEL : carte du trajet, « Trouver » s'allume.]
[SON : ding de chapitre.]

Uber reçoit les positions de millions de chauffeurs. Toi, tu en veux une poignée : ceux qui sont autour de toi.

La solution naïve, c'est de calculer la distance entre toi et chaque chauffeur. Un million de chauffeurs, un million de calculs. Pour une seule personne. Et des gens qui ouvrent l'appli au même moment, il y en a des millions.

[VISUEL : des traits partent du point bleu vers toutes les voitures du monde ; un compteur de calculs s'emballe et passe au rouge.]

C'est comme chercher Karim dans un stade en demandant à chaque spectateur : « T'es Karim ? »

L'astuce, c'est de ranger. On découpe la carte en cases, et chaque chauffeur va dans la sienne. Quand tu ouvres l'appli, Uber ne regarde plus le monde entier. Juste ta case, et celles d'à côté.

Le réflexe, c'est de prendre des carrés. Sauf que les carrés ont un défaut. Regarde ta case : quatre voisines collées par un côté, et quatre collées par un coin. Celles du coin sont quarante et un pour cent plus loin.

[VISUEL : grille de carrés, case centrale allumée. Deux flèches : une droite marquée « 1 », une en diagonale marquée « 1,41 ».]

Donc « la case d'à côté », ça peut vouloir dire tout près… ou nettement plus loin. Pour trouver le chauffeur le plus proche, c'est embêtant.

L'hexagone, lui, a six voisins. Tous à la même distance.

[VISUEL : les carrés se transforment en hexagones ; six flèches identiques partent du centre.]
[SON : petit « clac » satisfaisant quand la grille se met en place.]

En 2018, Uber publie sa grille hexagonale en open source. Elle s'appelle H3.

Tu donnes une position GPS à H3, il te renvoie le numéro de ton hexagone. Ensuite, tu lui demandes ton hexagone plus un anneau autour. Ça fait sept cases. Deux anneaux ? Dix-neuf. Les devs appellent ça un k-ring.

[VISUEL : l'anneau 1 (7 hexagones) puis l'anneau 2 (19) s'allument ; le compteur passe de « 1 000 000 » à « ~100 ». En petit, pour les devs : « kRing, devenu grid_disk dans H3 v4 ».]

Uber ne parcourt plus un million de chauffeurs. Seulement ceux qui sont dans ces dix-neuf cases. Peut-être une centaine.

**Abonnement (≈ 3:00, 26 % de la vidéo, juste après la première révélation)**

Si t'aimes comprendre ce qui se cache derrière les applis que t'as dans la poche, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, les hexagones restent à l'écran.]

Maintenant, dézoome. H3 a seize niveaux de zoom, et à chaque niveau, les hexagones sont sept fois plus petits. Au plus large, un hexagone fait à peu près huit fois la France. Au plus fin, moins d'un mètre carré. Et là, il en faut près de cinq cent soixante-dix mille milliards pour couvrir la Terre.

[VISUEL : un hexagone géant qui se divise en sept, encore et encore, jusqu'à un hexagone de la taille d'une table basse. Compteur « 569 707 381 193 162 » en bas.]

Enfin… presque que des hexagones. On ne peut pas recouvrir une boule uniquement avec des hexagones : il faut tricher quelque part. Alors H3 cache douze pentagones à chaque niveau. Et pour qu'ils ne tombent pas au milieu d'une ville, la grille est tournée pour les placer dans l'océan.

> ⚠️ À VÉRIFIER : 12 pentagones par niveau (confirmé par le blog H3) ; leur placement en mer (orientation dite « Dymaxion ») est à confirmer dans la doc h3geo.org.

[VISUEL : un globe qui tourne, douze pentagones rouges qui clignotent, tous en pleine mer.]

Quelque part au milieu de l'eau, il y a douze cases à cinq côtés où aucun Uber ne passera jamais.

Et ces hexagones servent partout. Le prix dynamique, par exemple : Uber compare, hexagone par hexagone, les demandes de course et les chauffeurs libres. Le fameux « ×1,8 » un samedi à deux heures du mat ? C'est ton hexagone qui a décidé.

[VISUEL : Paris un samedi soir, les hexagones virent à l'orange puis au rouge, « ×1,8 » s'affiche.]

Uber sait maintenant quels chauffeurs sont autour de toi. Reste à te les envoyer, en direct. Et ça, pendant des années, Uber l'a mal fait.

---

## 3. Étape 2 : te les envoyer en direct (4:23 – 7:05)

[VISUEL : carte du trajet, « Envoyer » s'allume.]

Au début, l'appli d'Uber se comportait comme un gamin à l'arrière de la voiture. « On est arrivés ? On est arrivés ? On est arrivés ? »

[SON : voix de gamin accélérée, en boucle.]

Toutes les quelques secondes, ton téléphone demandait au serveur : « Du nouveau ? » Et la plupart du temps, la réponse était non. Ça s'appelle le polling.

[VISUEL : des bulles « Du nouveau ? » s'empilent côté téléphone, des « Non. » côté serveur, de plus en plus vite.]

Chaque « non » coûte de la batterie, du réseau, et du travail pour le serveur. Dans un article de 2020, Uber donne le chiffre : à un moment, huit requêtes sur dix reçues par leur porte d'entrée, l'API gateway, étaient du polling.

[VISUEL : « 80 % » plein écran.]

Huit sur dix. Pour rien, la plupart du temps.

Et sur un réseau 2G ou 3G qui coupe, chaque échec relançait des requêtes. Au démarrage, toute l'appli réclamait ses données en même temps, et l'écran restait bloqué. Si t'as déjà fixé une appli qui mouline avec une seule barre de réseau, tu vois le tableau.

La solution : retourner la conversation. Le téléphone arrête de demander, et c'est le serveur qui prévient quand il y a du nouveau. Du push. Pour ça, Uber a construit RAMEN.

[SON : bruit de nouilles aspirées.]
[VISUEL : un bol de ramen fumant, barré d'un trait rouge.]

Non, pas les nouilles. Realtime Asynchronous MEssaging Network : un réseau de messagerie en temps réel. Ils ont clairement trouvé le nom avant.

RAMEN, c'est trois pièces. Imagine un restaurant.

Fireball, c'est le serveur en salle. Il écoute tout ce qui se passe : un passager commande, un chauffeur accepte, une voiture bouge. Et pour chaque événement, il décide qui doit être prévenu, et quand.

L'API gateway, c'est la cuisine. Elle prépare l'assiette : toutes les données dont ton appli a besoin, au bon format.

Et le serveur RAMEN, c'est le livreur. Il garde une connexion ouverte avec ton téléphone et il livre, avec une promesse : chaque message arrive au moins une fois.

[VISUEL : trois personnages en 2D, un serveur, un cuisinier, un livreur ; le message passe de l'un à l'autre jusqu'au téléphone.]

En 2020, ça tenait plus d'un million et demi de connexions ouvertes en même temps.

> ✂️ **Bloc coupable (~30 s)** : si la vidéo dépasse 11 min 30, supprime d'ici jusqu'à « devient instantané ».

Mais il y avait un défaut. La première version reposait sur SSE, une technologie où seul le serveur parle. Le téléphone envoyait ses « bien reçu » par une autre porte, toutes les trente secondes. Donc pendant trente secondes, Uber ne savait pas si son message était arrivé.

[VISUEL : un livreur sonne, la porte reste fermée, un chrono « 30 s » tourne.]

Pour une offre de course envoyée à un chauffeur, c'est une éternité. En 2022, Uber passe donc à gRPC : les deux côtés parlent en même temps, et le « bien reçu » devient instantané.

La position de Karim arrive donc jusqu'à toi, en direct, sans vider ta batterie. Un seul problème : elle est peut-être fausse.

---

## Relance (≈ 7:05, 61 % de la vidéo)

Et honnêtement, c'est la partie que je préfère. Jusqu'ici, on parlait des serveurs d'Uber. Le vrai problème, lui, il est dans ta poche.

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : carte du trajet, « Afficher » s'allume.]

---

## 4. Étape 3 : l'afficher sans mentir (7:10 – 9:50)

Le GPS de ton téléphone, en ville, il se trompe. D'après les ingénieurs d'Uber, l'erreur peut atteindre cinquante mètres, voire plus. Cinquante mètres, c'est l'autre côté du boulevard. C'est Karim qui t'attend à la mauvaise sortie de la gare.

[VISUEL : le point bleu saute d'un trottoir à l'autre ; une règle « 50 m » s'étire en travers de la rue.]

Pourquoi ? Ton téléphone calcule sa position avec le temps que mettent les signaux des satellites pour lui arriver. Mais en ville, il y a des immeubles. Le signal tape contre une façade, rebondit, et arrive en retard. Ton téléphone croit alors que tu es plus loin.

[VISUEL : une rue entre deux tours ; un signal direct bloqué par un immeuble, un autre qui rebondit sur la façade d'en face.]

En 2018, des ingénieurs d'Uber publient une idée tordue. Et géniale. Ils se servent du problème comme d'un indice.

Sur Android, ton téléphone connaît la force du signal de chaque satellite. Signal faible ? Il y a sûrement un immeuble entre toi et lui. Signal fort ? La voie est libre. On compare ça à une carte 3D de la ville, et on en déduit de quel côté de la rue tu te trouves. Ils se repèrent grâce à l'ombre des immeubles.

[VISUEL : vue 3D de la rue, les « ombres radio » des immeubles projetées au sol ; le point se cale du bon côté.]

Et pour te suivre, ils lancent des milliers d'hypothèses à la fois. Des milliers de petits « toi » possibles, éparpillés dans la rue. À chaque mesure, ceux qui collent avec les signaux restent, les autres disparaissent. C'est un filtre à particules.

[VISUEL : un nuage de petits points dans la rue, qui se resserre sur le bon trottoir à chaque « tic ».]

> ✂️ **Bloc coupable (~20 s)** : ce paragraphe.

Petite parenthèse pour les devs. On lit souvent qu'Uber utilise un filtre de Kalman. Dans cet article, les ingénieurs expliquent pourquoi ils ne l'ont pas pris : Kalman suppose une erreur en forme de cloche, avec un seul pic. En ville, ta position possible en a plusieurs.

[VISUEL : une courbe en cloche, barrée ; à côté, une carte de chaleur avec plusieurs bosses. Bandeau « Pour les devs ».]

> ⚠️ À VÉRIFIER : l'article de 2018 décrit une méthode testée à San Francisco. Ne pas dire qu'elle tourne aujourd'hui dans l'appli sans source.

Même juste, la position arrive par à-coups. Le réseau coupe sous un pont, un message arrive en retard. Si l'appli affichait juste la dernière position reçue, la voiture se téléporterait. Comme ton pote qui lagge sur Monster Hunter et réapparaît trois mètres plus loin, en plein dans les pattes du Rathalos.

[VISUEL : la voiture saute d'un point à l'autre en saccadé, puis la même scène, fluide.]

Uber n'a pas détaillé comment l'appli anime ses voitures. Mais les jeux en ligne utilisent un principe connu depuis des années : entre deux positions, on fait glisser la voiture. Et si la suivante tarde, on devine où elle devrait être, avec sa dernière vitesse et sa direction. C'est la navigation à l'estime, dead reckoning en anglais. Les marins faisaient déjà ça avant le GPS.

[VISUEL : la voiture continue tout droit en pointillés, puis se recale doucement quand la vraie position arrive.]

Donc la voiture que tu vois sur ta carte, c'est souvent une estimation. Une bonne estimation. Mais une estimation.

Et ça nous ramène à la question du début.

---

## 5. Les voitures fantômes (9:50 – 10:50)

[SON : musique plus sombre, une basse qui tient.]

En juillet 2015, deux chercheurs, Alex Rosenblat et Luke Stark, publient une enquête sur Uber. Ils racontent qu'on peut voir quatre voitures autour de soi sur la carte… et dix-sept minutes d'attente pour la plus proche. Des voitures fantômes.

[VISUEL : scène reconstituée en motion design (pas la vraie appli) : quatre voitures autour du point bleu, « 17 min » s'affiche, les voitures deviennent translucides.]

Le plus drôle, c'est ce qu'un employé d'Uber a répondu à un chauffeur : la carte, ce serait « plutôt un effet visuel », pour montrer que des chauffeurs cherchent des courses. Il la compare à un économiseur d'écran.

Officiellement, Uber dément : l'objectif, c'est que le nombre et la position des voitures soient aussi précis que possible. Ils citent la latence, ce qu'on vient de voir. Et l'appli n'afficherait que les huit voitures les plus proches. Il y en aurait donc plutôt plus que ce que tu vois. Pas moins.

> ⚠️ À VÉRIFIER : citations exactes dans l'article original de Motherboard (Vice) et dans Fortune du 30/07/2015, avant l'enregistrement.

C'était en 2015, et l'appli a beaucoup changé depuis. Mais avoue : une voiture qui glisse sur ta carte, tu ne la regardes plus pareil.

---

## 6. Fin (10:50 – 11:40)

Récapitulons le trajet. Le téléphone de Karim envoie une position qui peut être fausse de cinquante mètres. Uber la range dans un hexagone. Fireball décide qu'elle mérite de te déranger. RAMEN te la livre. Et ton appli la fait glisser pour que tu ne voies jamais les trous.

[VISUEL : la carte du trajet en entier, les trois étapes allumées, le point qui la parcourt d'un bout à l'autre en accéléré.]

Tout ça pour un geste que tu fais en deux secondes.

Et le meilleur, c'est que H3 est open source. Trois lignes de Python, et tu découpes ta ville en hexagones.

[VISUEL : l'éditeur de code, puis la carte de Paris qui se couvre d'hexagones.]

```python
import h3
cell = h3.latlng_to_cell(48.8443, 2.3744, 9)  # gare de Lyon
voisins = h3.grid_disk(cell, 1)               # 7 hexagones
```

Sur Technovore, j'ouvre comme ça les applis que t'as dans la poche, une par une. Et toi, laquelle tu veux que j'ouvre ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et en attendant, la vidéo juste là, c'est un dev qui a recréé sept logiciels Adobe avec une IA. J'ai testé ses clones.

[VISUEL : écran de fin, 20 s : vidéo ArtCraft à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Visuel | Dézoom jusqu'à la Terre en hexagones |
| 0:30 | Boucle ouverte | La voiture fantôme disparaît (résolue à 9:50) |
| 1:18 | Visuel récurrent | Carte du trajet, étape « Trouver » |
| 1:35 | Visuel | Le compteur de calculs s'emballe |
| 2:05 | Schéma | Carré : 1 contre 1,41 |
| 2:25 | Son | « Clac » de la grille hexagonale |
| 3:15 | Chiffre | 570 000 milliards d'hexagones |
| 3:55 | Surprise | 12 pentagones cachés en mer |
| 4:15 | Lien au vécu | « ×1,8 » un samedi soir |
| 4:25 | Son + humour | Le gamin « On est arrivés ? » |
| 4:55 | Chiffre | 80 % de polling |
| 5:45 | Humour | RAMEN, pas les nouilles |
| 6:00 | Personnages | Le restaurant : serveur, cuisine, livreur |
| 6:50 | Visuel | Le livreur qui attend 30 s |
| 7:05 | Coupure musique | Relance à 61 % |
| 7:15 | Visuel | Le point bleu qui saute de 50 m |
| 8:10 | Visuel | Les ombres radio des immeubles |
| 8:55 | Parenthèse | Kalman, « Pour les devs » |
| 9:15 | Référence | Lag sur Monster Hunter |
| 9:50 | Changement de ton | Musique sombre, voitures fantômes |
| 11:15 | Code | Trois lignes de Python |

**Total** : 21 relances, environ une toutes les 33 secondes (le guide de rétention recommande une toutes les 30 s pour une vidéo montée).

Timecodes calculés à 155 mots/min. À recaler sur la première prise du clone.

## Points de décrochage

| Temps | Risque | Problème | Parade |
|---|---|---|---|
| 0:15 | Élevé | L'enjeu ressemble à un sommaire | Les trois problèmes vite, et la voiture qui disparaît comme image finale |
| 2:05 | Moyen | La géométrie des carrés peut perdre les non-devs | Un seul schéma, deux flèches, deux nombres, pas plus |
| 5:45 | Élevé | RAMEN est le bloc le plus dense (trois services, SSE, gRPC) | Le restaurant porte l'explication. Trop long ? Coupe d'abord le bloc SSE/gRPC (~30 s) |
| 7:05 | Élevé | Autour de 60 % : chute classique | La relance plus la coupure musicale ; le GPS qui se trompe est concret dès la première phrase |
| 8:55 | Moyen | La parenthèse Kalman ne parle qu'aux devs | Bandeau « Pour les devs », 20 s maximum, coupable au montage |

**Voix** : le guide de rétention attribue une rétention plus faible aux narrations IA. Ton clone a ta propre voix, mais le risque, c'est la monotonie : annote le script (pauses, emphases) avant la génération, surtout le hook et la relance de 7:05.

## Notes de montage

- **Composants Remotion à construire une fois** : la carte du trajet (3 étapes), la grille qui passe des carrés aux hexagones, le globe en hexagones. Le calendrier prévoit de réutiliser la carte pour Waze le 7 décembre.
- **Pas de vraie appli Uber à l'écran** : on reconstruit tout en motion design, comme le recommande `strategie.md` (point 5 de la partie juridique). Captures autorisées : le blog Uber Engineering, la doc H3.
- **Énergie** : calme, puis une montée toutes les 2-3 min (alternance « calme-burst » du guide). Montées sur le dézoom (0:05), les pentagones (3:55), le 80 % (4:55), la relance (7:05) et les voitures fantômes (9:50).
- **Images pour la miniature** : la Terre couverte d'hexagones (0:10) et le dézoom sur Paris. Elles collent à la miniature de la fiche.
- **Shorts** : #1 (12 nov) = le hook et le dézoom ; #2 (19 nov) = carrés contre hexagones (1:55-2:35) ; réserve = le lag et l'estime (9:15-9:50). Les voitures fantômes (9:50-10:50) feraient un quatrième Short.

## Sources

- Uber Engineering, [Uber's Real-Time Push Platform](https://www.uber.com/blog/real-time-push-platform/), 18 déc. 2020 : 80 % de polling, 2G/3G, démarrage, RAMEN, Fireball, API gateway, SSE, « au moins une fois », 1,5 M de connexions et 250 000 messages/s.
- Uber Engineering, [Uber's Next Gen Push Platform on gRPC](https://eng.uber.com/blog/ubers-next-gen-push-platform-on-grpc/), 16 août 2022 : accusés de réception toutes les 30 s avec SSE, passage à gRPC.
- Uber Engineering, [H3: Uber's Hexagonal Hierarchical Spatial Index](https://www.uber.com/blog/h3/), 27 juin 2018 : open source, une seule distance aux voisins (deux pour les carrés, trois pour les triangles), prix dynamique, 16 niveaux (chaque niveau divise la surface par 7), 12 pentagones, k-ring.
- Uber Engineering, [Rethinking GPS](https://www.uber.com/blog/rethinking-gps/), 19 avr. 2018 : erreur de 50 m ou plus en ville, force du signal (SNR) sur Android, carte 3D, filtre à particules, pourquoi pas Kalman.
- Uber, [résultats du T2 2026](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) : 3,9 milliards de courses et livraisons sur le trimestre, soit environ 43 millions par jour (calcul : 3,9 milliards ÷ 91 jours).
- Voitures fantômes : [Fortune, 30/07/2015](https://fortune.com/2015/07/30/uber-phantom-cars), [TIME](https://time.com/3979271/uber-phantom-cars). Article original : Motherboard (Vice), Rosenblat et Stark.
- Piste écartée faute de source primaire : le premier dispatch d'Uber aurait utilisé les cases carrées de S2 (Google), d'après [High Scalability](https://highscalability.com/how-uber-scales-their-real-time-market-platform/). Si le talk de Matt Ranney (QCon 2015) le confirme, ça peut remplacer « Le réflexe, c'est de prendre des carrés » à 2:00.
- Chiffres H3 calculés : 2 + 120 × 7¹⁵ = 569 707 381 193 162 cellules au niveau 15 ; surface de la Terre ÷ ce nombre ≈ 0,9 m². À recouper avec le tableau de surfaces de la doc h3geo.org (niveau 0 : environ 4,36 millions de km², soit ~8 fois les 552 000 km² de la France métropolitaine).

## Reste à vérifier avant la voix

1. Les 12 pentagones placés en mer (doc h3geo.org).
2. Les surfaces des niveaux 0 et 15 (tableau de la doc h3geo.org).
3. Les citations exactes sur les voitures fantômes (article de Motherboard).
4. La fréquence d'envoi des positions : aucun chiffre officiel trouvé, donc le script reste vague (« toutes les quelques secondes »).
5. L'animation des voitures dans l'appli : non documentée par Uber, le script le dit à l'écran.
