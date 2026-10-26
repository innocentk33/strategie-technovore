# Uber : script v2

**Titre** : *Le génie caché derrière la carte en temps réel d'Uber* (titre de publication depuis le 26/10 : *La carte d'Uber est une illusion (et c'est génial)*)

**Durée** : environ 1 840 mots de voix off. À ton débit mesuré sur ArtCraft (145 mots/min, pauses et improvisations comprises) : environ 12 min 40, ou 12 min 20 sans la parenthèse Kalman. À 155 mots/min : 11 min 50. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : on suit la position de Karim, chauffeur à Paris, de son téléphone jusqu'à celui du passager, en trois étapes : trouver, envoyer, afficher. Deux boucles ouvertes : « est-ce que toutes ces voitures existent vraiment ? » (hook, refermée dans la section 5) et « mon pote avait raison ? » (section 1, refermée dans la fin).

**Changements depuis le brouillon v1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- tutoiement, comme dans le brouillon v1 (choix de l'auteur, 19/10) ;
- ton pote et ses blogs tech, l'article sur le polling qu'il t'a envoyé, tes cartes en Flutter ;
- hook recalé sur les sources : H3 sert à trouver un chauffeur (dispatch) ; 570 000 milliards devient une limite de la grille ;
- section 4 centrée sur le téléphone de Karim, avec le retournement « depuis le début, je fais comme si sa position était juste » ;
- ton gag Fast and Furious : teaser dans le hook, gag complet dans la section 4 ;
- le restaurant devient Uber Eats ; devinette sur les carrés ; seize niveaux justifiés par le prix ;
- voitures fantômes raccordées au décalage de 30 à 60 s cité par les chauffeurs ;
- tics d'IA du grill retirés ;
- environ 320 mots coupés pour tenir la durée, dont le bloc SSE/gRPC, passé en réserve en bas du fichier.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation Remotion ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture.

---

## 0. Hook (0:00 – 0:37) · objectif : 70 % de rétention à 0:30

[VISUEL : un téléphone en gros plan, une carte sombre, des petites voitures qui glissent autour du point bleu. Pas de titre, pas de logo.]

Ouvre Uber. Tu vois ces petites voitures autour de toi ? Pour te trouver un chauffeur, Uber a découpé la planète en hexagones.

[VISUEL : dézoom d'un coup : la rue, Paris, la France, puis la Terre entière couverte d'hexagones lumineux.]
[SON : whoosh sur le dézoom, un « tic » à chaque palier.]

Une grille qui peut descendre jusqu'à cinq cent soixante-dix mille milliards de cases. Aujourd'hui, on suit une de ces voitures, du téléphone du chauffeur jusqu'au tien.

Sur ce trajet, sa position passe par un serveur bombardé de questions et par un GPS qui se trompe de cinquante mètres.

[VISUEL : teaser d'une seconde : la voiture part en dérapage et traverse un immeuble. Arrêt sur image.]
[SON : crissement de pneus, coupé net.]

Et en 2015, deux chercheurs ont posé une question gênante : est-ce que toutes ces voitures existent vraiment ?

[VISUEL : une des voitures devient transparente, clignote, puis disparaît.]

---

## 1. Mon pote et ses blogs (0:37 – 1:31)

J'ai un pote qui lit les blogs tech des grosses boîtes, pour voir comment elles construisent des produits utilisés par des millions de personnes. Un jour, il m'envoie un article d'Uber sur un truc qui s'appelle le polling. Pour lui, les ingés d'Uber, c'est des génies.

Moi, des cartes avec des éléments dessus, j'en ai affiché dans mes applis Flutter. Mais jamais pour des millions de personnes en même temps. Alors j'ai lu son article, puis les autres.

[VISUEL : défilement rapide des articles du blog Uber Engineering, seules les dates restent nettes. Texte : « Toutes les sources en description ».]

À la fin, je te dirai si mon pote avait raison.

[VISUEL : Karim en 2D, dans sa voiture près de la gare de Lyon. Un petit point lumineux part de son téléphone.]

Uber, c'est plus de quarante millions de courses et de livraisons par jour. On en prend une. Karim, chauffeur à Paris : toutes les quelques secondes, son téléphone envoie sa position, et elle doit arriver sur ton écran, deux rues plus loin. On la suit.

[VISUEL : la « carte du trajet », trois étapes : Trouver, Envoyer, Afficher. Elle revient au début de chaque chapitre.]

---

## 2. Étape 1 : trouver les voitures autour de toi (1:31 – 4:43)

[VISUEL : carte du trajet, « Trouver » s'allume.]
[SON : ding de chapitre.]

Uber reçoit les positions de millions de chauffeurs. Toi, tu en veux une poignée : ceux qui sont autour de toi.

La solution naïve, c'est de calculer la distance entre toi et chaque chauffeur. Un million de chauffeurs, un million de calculs. Pour une seule personne. Et des gens qui ouvrent l'appli au même moment, il y en a des millions.

[VISUEL : des traits partent du point bleu vers toutes les voitures du monde ; un compteur de calculs s'emballe et passe au rouge.]

C'est comme chercher Karim dans un stade en demandant à chaque spectateur : « T'es Karim ? »

L'astuce, c'est de ranger. On découpe la carte en cases, et chaque chauffeur va dans la sienne. Quand tu ouvres l'appli, Uber regarde ta case et celles d'à côté.

Le réflexe, c'est de prendre des carrés. Regarde la grille deux secondes : tu vois le défaut ?

[VISUEL : grille de carrés, case centrale allumée, sans flèches, deux secondes de silence.]

Ta case a quatre voisines collées par un côté, et quatre collées par un coin. Celles du coin sont quarante et un pour cent plus loin.

[VISUEL : deux flèches apparaissent : une droite marquée « 1 », une en diagonale marquée « 1,41 ».]

Donc « la case d'à côté », ça peut vouloir dire tout près… ou nettement plus loin.

L'hexagone, lui, a six voisins. Tous à la même distance.

[VISUEL : les carrés se transforment en hexagones ; six flèches identiques partent du centre.]
[SON : petit « clac » satisfaisant quand la grille se met en place.]

En 2018, Uber publie sa grille hexagonale en open source. Elle s'appelle H3.

Tu donnes une position GPS à H3, il te renvoie ton hexagone. Ajoute un anneau autour : sept cases. Deux anneaux : dix-neuf. Les devs appellent ça un k-ring.

[VISUEL : l'anneau 1 (7 hexagones) puis l'anneau 2 (19) s'allument ; le compteur passe de « 1 000 000 » à « ~100 ». En petit, pour les devs : « kRing, devenu grid_disk dans H3 v4 ».]

Du coup, au lieu d'un million de chauffeurs, Uber n'en parcourt plus qu'une centaine : ceux de ces dix-neuf cases.

**Abonnement (≈ 3:11, 25 % de la vidéo, juste après la première révélation)**

Si tu aimes comprendre ce qui se cache derrière les applis que tu as dans la poche, abonne-toi : sur Technovore, on les ouvre une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, les hexagones restent à l'écran.]

Sept cases, ça suffit pour trouver Karim. Mais pour fixer un prix, Uber compare, hexagone par hexagone, les demandes de course et les chauffeurs libres de toute la ville. Le fameux « ×1,8 » un samedi à deux heures du mat ? C'est ton hexagone qui a décidé.

[VISUEL : Paris un samedi soir, les hexagones virent à l'orange puis au rouge, « ×1,8 » s'affiche.]

Donc H3 a seize niveaux de zoom, et à chaque niveau, les hexagones sont sept fois plus petits. Au plus large, un hexagone fait à peu près huit fois la France. Au plus fin, moins d'un mètre carré. Et là, il en faut près de cinq cent soixante-dix mille milliards pour couvrir la Terre.

[VISUEL : un hexagone géant qui se divise en sept, encore et encore, jusqu'à un hexagone de la taille d'une table basse. Compteur « 569 707 381 193 162 » en bas.]

Enfin… presque que des hexagones. On ne peut pas recouvrir une boule uniquement avec des hexagones : il faut tricher quelque part. Alors H3 cache douze pentagones à chaque niveau. Et pour qu'ils ne tombent pas au milieu d'une ville, la grille est orientée pour les placer tous dans l'océan.

[VISUEL : un globe qui tourne, douze pentagones rouges qui clignotent, tous en pleine mer.]

Quelque part au milieu de l'eau, il y a douze cases à cinq côtés où aucun Uber ne passera jamais.

Uber sait maintenant quels chauffeurs sont autour de toi. Reste à te les envoyer, en direct. Et ça, pendant des années, Uber l'a mal fait.

---

## 3. Étape 2 : te les envoyer en direct (4:43 – 6:57)

[VISUEL : carte du trajet, « Envoyer » s'allume.]

Au début, l'appli d'Uber se comportait comme un gamin à l'arrière de la voiture. « On est arrivés ? On est arrivés ? On est arrivés ? »

[SON : voix de gamin accélérée, en boucle.]

Toutes les quelques secondes, ton téléphone demandait au serveur : « Du nouveau ? » Et la plupart du temps, la réponse était non. Ça s'appelle le polling. C'est de ça que parlait l'article de mon pote.

[VISUEL : des bulles « Du nouveau ? » s'empilent côté téléphone, des « Non. » côté serveur, de plus en plus vite.]

Chaque « non » coûte de la batterie et du travail pour le serveur. Dans cet article de 2020, Uber donne le chiffre : à un moment, huit requêtes sur dix reçues par leur porte d'entrée, l'API gateway, étaient du polling.

[VISUEL : « 80 % » plein écran.]

Et sur un réseau 2G ou 3G qui coupe, chaque échec relançait des requêtes. Si tu as déjà fixé une appli qui mouline avec une seule barre de réseau, tu vois le tableau.

La solution : retourner la conversation. Le téléphone arrête de demander, et c'est le serveur qui prévient quand il y a du nouveau. Du push. Pour ça, Uber a construit RAMEN.

[SON : bruit de nouilles aspirées.]
[VISUEL : un bol de ramen fumant, barré d'un trait rouge.]

Non, pas les nouilles. Realtime Asynchronous MEssaging Network : un réseau de messagerie en temps réel. Ils ont clairement trouvé le nom avant.

RAMEN, c'est trois pièces. Pour les comprendre, prends Uber Eats.

Fireball, c'est le gérant. Il voit passer chaque événement : un passager commande, un chauffeur accepte, une voiture bouge. Et pour chacun, il décide qui doit être prévenu, et quand.

L'API gateway, c'est la cuisine. Elle prépare la commande : toutes les données dont ton appli a besoin, au bon format.

Et le serveur RAMEN, c'est le livreur. Il garde une connexion ouverte avec ton téléphone, et il livre avec une promesse : chaque message arrive au moins une fois.

[VISUEL : trois personnages en 2D, un gérant, un cuisinier, un livreur à vélo ; le message passe de l'un à l'autre jusqu'au téléphone.]

En 2020, ça tenait plus d'un million et demi de connexions ouvertes en même temps.

> ↩️ Le bloc SSE/gRPC (~45 s) est passé en réserve, en bas du fichier. À remettre ici si la vidéo est trop courte.

La position de Karim arrive jusqu'à toi, en direct, sans vider ta batterie. Mais depuis le début, je fais comme si elle était juste.

---

## 4. Étape 3 : l'afficher sans mentir (6:57 – 9:59) · relance à 55 %

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : carte du trajet, « Afficher » s'allume.]

En ville, elle peut être fausse de cinquante mètres. Ce sont les ingénieurs d'Uber qui le disent, et parfois c'est pire. Cinquante mètres, c'est l'autre côté du boulevard. Sur ta carte, Karim t'attend devant la gare. En vrai, il est garé en face.

[VISUEL : la voiture de Karim saute d'un trottoir à l'autre ; une règle « 50 m » s'étire en travers de la rue.]

Si l'appli faisait glisser la voiture d'une position fausse à l'autre, Karim arriverait comme dans Fast and Furious : à fond, en dérapage, à travers les immeubles. Un saut de cinquante mètres en une seconde, à l'écran, c'est du cent quatre-vingts à l'heure.

[VISUEL : la voiture de Karim fonce sur la carte, dérape, traverse un immeuble en ligne droite et ressort de l'autre côté. Compteur « 180 km/h ».]
[SON : crissement de pneus, moteur qui hurle.]

Pourquoi le GPS se trompe autant ? Le téléphone de Karim calcule sa position avec le temps que mettent les signaux des satellites à lui arriver. Mais en ville, il y a des immeubles. Un signal tape contre une façade, rebondit, et arrive en retard. Le téléphone croit alors que le satellite est plus loin qu'en réalité, et il se place au mauvais endroit.

[VISUEL : une rue entre deux tours ; un signal direct bloqué par un immeuble, un autre qui rebondit sur la façade d'en face.]

En 2018, des ingénieurs d'Uber ont une idée tordue : se servir du problème comme d'un indice.

Sur Android, le téléphone connaît la force du signal de chaque satellite. Signal faible ? Il y a sûrement un immeuble entre lui et le satellite. Signal fort ? La voie est libre. On compare ça à une carte 3D de la ville, et on en déduit de quel côté de la rue il se trouve. Ils se repèrent grâce à l'ombre des immeubles.

[VISUEL : vue 3D de la rue, les « ombres radio » des immeubles projetées au sol ; le point se cale du bon côté.]

Et pour suivre la voiture, ils éparpillent dans la rue des milliers de voitures possibles. À chaque mesure, celles qui collent avec les signaux restent, les autres disparaissent. C'est un filtre à particules, testé à San Francisco.

[VISUEL : un nuage de petits points dans la rue, qui se resserre sur le bon trottoir à chaque « tic ».]

> ✂️ **Bloc coupable (~20 s)** : ce paragraphe.

Petite parenthèse pour les devs. On lit souvent qu'Uber utilise un filtre de Kalman. Dans cet article, les ingénieurs expliquent pourquoi ils ne l'ont pas pris pour ce problème-là : Kalman suppose une erreur en forme de cloche, avec un seul pic. En ville, la position possible en a plusieurs.

[VISUEL : une courbe en cloche, barrée ; à côté, une carte de chaleur avec plusieurs bosses. Bandeau « Pour les devs ».]

Même juste, la position arrive par à-coups. Le réseau coupe sous un pont, un message arrive en retard. Si l'appli affichait juste la dernière position reçue, la voiture se téléporterait. Comme un coéquipier qui lagge sur Monster Hunter et réapparaît trois mètres plus loin, en plein dans les pattes du Rathalos.

[VISUEL : la voiture saute d'un point à l'autre en saccadé, puis la même scène, fluide.]

Uber n'a pas détaillé comment l'appli anime ses voitures. Mais les jeux en ligne utilisent un vieux principe : entre deux positions, on fait glisser la voiture. Et si la suivante tarde, on devine où elle devrait être, avec sa dernière vitesse et sa direction. C'est la navigation à l'estime, dead reckoning en anglais. Les marins faisaient déjà ça avant le GPS.

[VISUEL : la voiture continue tout droit en pointillés, puis se recale doucement quand la vraie position arrive.]

Et ça nous ramène à la question du début.

---

## 5. Les voitures fantômes (9:59 – 11:23)

[SON : musique plus sombre, une basse qui tient.]

En juillet 2015, deux chercheurs, Alex Rosenblat et Luke Stark, publient une enquête sur les chauffeurs Uber. Ils racontent l'histoire d'une chauffeuse qui ouvre l'appli côté passager. Sur la carte, quatre voitures juste à côté de son point de départ. Et dix-sept minutes d'attente pour la plus proche.

[VISUEL : scène reconstituée en motion design (pas la vraie appli) : quatre voitures autour du point bleu, « 17 min » s'affiche, les voitures deviennent translucides.]

Le support d'Uber lui répond que la carte, c'est « plutôt un effet visuel ». Et même : « Mieux vaudrait voir ça comme un économiseur d'écran. »

Officiellement, Uber dément. D'après eux, le but, c'est des voitures aussi précises que possible, et la latence peut les décaler. Et l'appli n'afficherait que les huit plus proches, donc il y en aurait plutôt plus que ce que tu vois.

Sur les forums, certains chauffeurs avaient leur explication : un décalage de trente à soixante secondes. Ce décalage, tu sais maintenant d'où il peut venir : des messages en retard, et une appli qui fait glisser les voitures en devinant. Mais d'autres chauffeurs voyaient des fantômes partout où le passager posait son épingle. Ça, aucun décalage ne l'explique.

[VISUEL : une épingle se pose à trois endroits de la carte ; à chaque fois, des voitures translucides apparaissent autour.]

Cette enquête date de 2015, et l'appli a beaucoup changé depuis. Mais la voiture qui glisse sur ta carte, maintenant, tu sais ce que c'est : au mieux, la position d'un chauffeur d'il y a quelques secondes, en partie devinée.

---

## 6. Fin (11:23 – 12:40)

On récapitule le trajet. Le téléphone de Karim envoie une position qui peut être fausse de cinquante mètres. Uber la range dans un hexagone. Fireball décide qu'elle mérite de te déranger. RAMEN te la livre. Et ton appli la fait glisser pour que tu ne voies jamais les trous.

[VISUEL : la carte du trajet en entier, les trois étapes allumées, le point qui la parcourt d'un bout à l'autre en accéléré.]

Tout ça pour un geste que tu fais en deux secondes.

Alors, mon pote avait raison ? Afficher des éléments sur une carte, je l'ai fait dans mes applis Flutter. Tout ce qu'on vient de voir, c'est ce qu'il faut en plus quand des millions de personnes regardent la même carte en même temps. Donc oui, les ingés d'Uber, c'est des génies.

[OPTIONNEL : LA PARTIE QUI T'A LE PLUS SURPRIS, ET POURQUOI. UNE OU DEUX PHRASES.]

Et H3 est open source. Trois lignes de Python, et tu découpes ta ville en hexagones d'environ deux cents mètres de côté.

[VISUEL : l'éditeur de code, puis la carte de Paris qui se couvre d'hexagones.]

```python
import h3
cell = h3.latlng_to_cell(48.8443, 2.3744, 9)  # gare de Lyon, niveau 9 (~200 m de côté)
voisins = h3.grid_disk(cell, 1)               # 7 hexagones
```

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. Laquelle tu veux que j'ouvre ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et en attendant, la vidéo juste là, c'est un dev qui a recréé sept logiciels Adobe avec une IA. J'ai testé ses clones.

[VISUEL : écran de fin, 20 s : vidéo ArtCraft à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:10 | Visuel | Dézoom jusqu'à la Terre en hexagones |
| 0:25 | Teaser | La voiture qui dérape à travers un immeuble |
| 0:35 | Boucle ouverte | La voiture fantôme disparaît (refermée à 9:59) |
| 1:05 | Boucle ouverte | « Je te dirai si mon pote avait raison » (refermée à 11:47) |
| 1:31 | Visuel récurrent | Carte du trajet, étape « Trouver » |
| 2:19 | Devinette | « Tu vois le défaut ? » sur la grille de carrés |
| 2:41 | Son | « Clac » de la grille hexagonale |
| 3:11 | Appel à l'action | Abonnement (25 %) |
| 3:34 | Lien au vécu | « ×1,8 » un samedi soir |
| 4:04 | Surprise | 12 pentagones cachés en mer |
| 4:43 | Son + humour | Le gamin « On est arrivés ? » |
| 5:15 | Chiffre | 80 % de polling |
| 5:54 | Humour | RAMEN, pas les nouilles |
| 6:07 | Personnages | Uber Eats : gérant, cuisine, livreur |
| 6:57 | Coupure musique | Retournement : « je fais comme si elle était juste » (55 %) |
| 7:15 | Gag | Fast and Furious, 180 km/h |
| 8:29 | Surprise | L'ombre des immeubles |
| 8:48 | Parenthèse | Kalman, « Pour les devs » |
| 9:21 | Référence | Lag sur Monster Hunter |
| 9:59 | Changement de ton | Musique sombre, voitures fantômes |
| 10:42 | Rappel | Le décalage de 30 à 60 s, expliqué par ce qu'on vient de voir |
| 11:47 | Boucle fermée | Le verdict sur le pote |
| 12:08 | Code | Trois lignes de Python |

**Total** : 23 relances en 12 min 40, environ une toutes les 33 secondes.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, enjeu | Moyen | Deux problèmes et une question en 15 s | Le teaser du dérapage et la voiture qui disparaît portent l'enjeu à l'image |
| Carrés contre hexagones | Moyen | La géométrie peut perdre les non-devs | La devinette d'abord, puis un seul schéma : deux flèches, deux nombres |
| RAMEN | Élevé | Le bloc le plus dense (trois pièces) | Uber Eats porte l'explication ; SSE/gRPC déjà passé en réserve |
| Relance (~60 %) | Élevé | Chute classique | Coupure musicale, retournement « je fais comme si elle était juste », puis le gag Fast and Furious dans les 20 s |
| Parenthèse Kalman | Moyen | Ne parle qu'aux devs | Bandeau « Pour les devs », 20 s maximum, coupable au montage |

## Notes de montage

- **Composants Remotion à construire une fois** : la carte du trajet (3 étapes), la grille qui passe des carrés aux hexagones, le globe en hexagones, la voiture qui dérape. La carte du trajet resservira pour Waze le 7 décembre.
- **Fast and Furious** : uniquement en motion design. Aucun extrait du film, aucune musique de la saga, pas de logo. Le nom dit à voix haute suffit. La même animation sert au teaser du hook (1 s) et au gag de la section 4.
- **Pas de vraie appli Uber à l'écran** : tout est reconstruit en motion design (`strategie.md`, partie juridique). Captures autorisées : le blog Uber Engineering, la doc H3.
- **Énergie** : calme, puis une montée toutes les 2-3 min. Montées sur le dézoom du hook, les pentagones, le 80 %, le gag Fast and Furious et les voitures fantômes.
- **Miniature** : la Terre couverte d'hexagones et le dézoom sur Paris, comme dans la fiche.
- **Short** : un seul, le 12 novembre (1 Short par vidéo longue) : le hook et le dézoom. En réserve : carrés contre hexagones, le dérapage Fast and Furious, les voitures fantômes.

## Sources (relues le 19/10/2026)

- Uber Engineering, [Uber's Real-Time Push Platform](https://www.uber.com/blog/real-time-push-platform/), 18 déc. 2020 : 80 % des requêtes vers l'API gateway en polling, 2G/3G et relances, démarrage à froid bloqué, RAMEN, Fireball (« quand pousser »), API gateway (« quoi pousser »), livraison « au moins une fois », plus de 1,5 M de connexions simultanées et 250 000 messages/s.
- Uber Engineering, [Uber's Next Gen Push Platform on gRPC](https://www.uber.com/blog/ubers-next-gen-push-platform-on-grpc/), 16 août 2022 : avec SSE, accusés de réception groupés toutes les 30 s par un autre point d'accès ; gRPC choisi pour le streaming bidirectionnel.
- Uber Engineering, [H3: Uber's Hexagonal Hierarchical Spatial Index](https://www.uber.com/blog/h3/), 27 juin 2018 : prix et dispatch, prix dynamique calculé par hexagone, open source en 2018, 16 niveaux, 12 pentagones, kRing.
- H3, [Overview](https://h3geo.org/docs/core-library/overview) : orientation Dymaxion, les 12 sommets de l'icosaèdre (donc les pentagones) dans l'océan, 12 pentagones à chaque niveau.
- H3, [tableau des résolutions](https://h3geo.org/docs/core-library/restable) : niveau 0 = 4,36 M km² (~8 fois les 544 000 km² de la France métropolitaine) ; niveau 9 = côté de ~200 m ; niveau 15 = 0,895 m², 569 707 381 193 162 cellules.
- Uber Engineering, [Rethinking GPS](https://www.uber.com/blog/rethinking-gps/), 19 avr. 2018 : erreur de 50 m ou plus en ville, réflexions sur les immeubles, rapport signal/bruit exposé par Android, carte 3D, « des milliers » de particules, pourquoi pas Kalman (distribution en cloche), démonstration à San Francisco.
- Uber, [résultats du T2 2026](https://www.sec.gov/Archives/edgar/data/0001543151/000154315126000027/uberq226earningspressrelea.htm) : 3 867 millions de courses et livraisons au trimestre clos le 30/06/2026, soit environ 42,5 millions par jour (÷ 91 jours).
- Alex Rosenblat et Luke Stark (Data & Society), [Uber's Phantom Cabs](https://www.vice.com/en/article/ubers-phantom-cabs/), Motherboard, juillet 2015 : la chauffeuse qui voit 4 voitures et 17 min d'attente sur l'appli passager, l'e-mail du support (« visual effect », « screen saver on a computer »), le décalage de 30 à 60 s avancé sur les forums, les fantômes autour de l'épingle du passager.
- [Fortune, 30/07/2015](https://fortune.com/2015/07/30/uber-phantom-cars) : démenti d'Uber (via The Guardian), latence, huit voitures les plus proches.

## Ce qui reste non documenté (et le script le dit)

1. La fréquence d'envoi des positions : aucun chiffre officiel, d'où « toutes les quelques secondes ».
2. L'animation des voitures dans l'appli : Uber ne l'a pas détaillée, le script parle des jeux en ligne.
3. Le filtre à particules dans l'appli actuelle : l'article décrit une démonstration à San Francisco, le script ne dit rien de plus.
4. Le 180 km/h est un calcul (50 m en 1 s) ; la phrase est au conditionnel.

## Bloc en réserve : SSE et gRPC (~45 s)

À remettre après « En 2020, ça tenait plus d'un million et demi de connexions ouvertes en même temps. » si la vidéo est trop courte, ou à recycler en commentaire épinglé pour les devs.

Mais il y avait un défaut. La première version reposait sur SSE, une technologie où seul le serveur parle. Le téléphone envoyait ses « bien reçu » par une autre porte, toutes les trente secondes. Donc pendant trente secondes, Uber ne savait pas si son message était arrivé.

[VISUEL : un livreur sonne, la porte reste fermée, un chrono « 30 s » tourne.]

Pour une offre de course envoyée à un chauffeur, c'est une éternité. Dans un article de 2022, Uber raconte son passage à gRPC : les deux côtés parlent en même temps, et le « bien reçu » peut repartir tout de suite, par la même connexion.
