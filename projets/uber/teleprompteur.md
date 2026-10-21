# Téléprompteur — Uber (v2, 19/10)

> Une ligne = un souffle. Ligne vide = respiration. Les [MARQUEURS], ⟦à écrire⟧ et (indications) ne se lisent pas.

## Hook

Ouvre Uber.  
Tu vois ces petites voitures autour de toi ?  
Pour te trouver un chauffeur,  
Uber a découpé la planète en hexagones.  

Une grille qui peut descendre  
jusqu'à 570 000 milliards de cases.  
Aujourd'hui, on suit une de ces voitures,  
du téléphone du chauffeur jusqu'au tien.  

Sur ce trajet, sa position passe par un serveur bombardé de questions  
et par un GPS qui se trompe de 50 mètres.  

Et en 2015, deux chercheurs ont posé une question gênante :  
est-ce que toutes ces voitures existent vraiment ?  

## Mon pote et ses blogs

J'ai un pote qui lit les blogs tech des grosses boîtes,  
pour voir comment elles construisent des produits  
utilisés par des millions de personnes.  
Un jour, il m'envoie un article d'Uber  
sur un truc qui s'appelle le polling.  
Pour lui, les ingés d'Uber, c'est des génies.  

Moi, des cartes avec des éléments dessus,  
j'en ai affiché dans mes applis Flutter.  
Mais jamais pour des millions de personnes en même temps.  
Alors j'ai lu son article, puis les autres.  

À la fin, je te dirai si mon pote avait raison.  

Uber, c'est plus de 40 millions de courses et de livraisons par jour.  
On en prend une.  
Karim, chauffeur à Paris :  
toutes les quelques secondes, son téléphone envoie sa position,  
et elle doit arriver sur ton écran, deux rues plus loin.  
On la suit.  

## Étape 1 : trouver

Uber reçoit les positions de millions de chauffeurs.  
Toi, tu en veux une poignée :  
ceux qui sont autour de toi.  

La solution naïve,  
c'est de calculer la distance entre toi et chaque chauffeur.  
Un million de chauffeurs, un million de calculs.  
Pour une seule personne.  
Et des gens qui ouvrent l'appli au même moment,  
il y en a des millions.  

C'est comme chercher Karim dans un stade  
en demandant à chaque spectateur : « T'es Karim ? »  

L'astuce, c'est de ranger.  
On découpe la carte en cases,  
et chaque chauffeur va dans la sienne.  
Quand tu ouvres l'appli,  
Uber regarde ta case et celles d'à côté.  

Le réflexe, c'est de prendre des carrés.  
Regarde la grille deux secondes :  
tu vois le défaut ?  

Ta case a quatre voisines collées par un côté,  
et quatre collées par un coin.  
Celles du coin sont 41 % plus loin.  

Donc « la case d'à côté »,  
ça peut vouloir dire tout près…  
ou nettement plus loin.  

L'hexagone, lui, a six voisins.  
Tous à la même distance.  

En 2018, Uber publie sa grille hexagonale en open source.  
Elle s'appelle H3.  

Tu donnes une position GPS à H3,  
il te renvoie ton hexagone.  
Ajoute un anneau autour : sept cases.  
Deux anneaux : dix-neuf.  
Les devs appellent ça un k-ring.  

Du coup, au lieu d'un million de chauffeurs,  
Uber n'en parcourt plus qu'une centaine :  
ceux de ces dix-neuf cases.  

## Mid-CTA

Si tu aimes comprendre ce qui se cache  
derrière les applis que tu as dans la poche,  
abonne-toi :  
sur Technovore, on les ouvre une par une.  

## Étape 1, suite : le prix et la grille

Sept cases, ça suffit pour trouver Karim.  
Mais pour fixer un prix, Uber compare, hexagone par hexagone,  
les demandes de course et les chauffeurs libres de toute la ville.  
Le fameux « fois 1,8 » un samedi à deux heures du mat ?  
C'est ton hexagone qui a décidé.  

Donc H3 a seize niveaux de zoom,  
et à chaque niveau, les hexagones sont sept fois plus petits.  
Au plus large, un hexagone fait à peu près huit fois la France.  
Au plus fin, moins d'un mètre carré.  
Et là, il en faut près de 570 000 milliards  
pour couvrir la Terre.  

Enfin… presque que des hexagones.  
On ne peut pas recouvrir une boule uniquement avec des hexagones :  
il faut tricher quelque part.  
Alors H3 cache douze pentagones à chaque niveau.  
Et pour qu'ils ne tombent pas au milieu d'une ville,  
la grille est orientée pour les placer tous dans l'océan.  

Quelque part au milieu de l'eau,  
il y a douze cases à cinq côtés  
où aucun Uber ne passera jamais.  

Uber sait maintenant quels chauffeurs sont autour de toi.  
Reste à te les envoyer, en direct.  
Et ça, pendant des années, Uber l'a mal fait.  

## Étape 2 : envoyer

Au début, l'appli d'Uber se comportait  
comme un gamin à l'arrière de la voiture.  
« On est arrivés ? On est arrivés ? On est arrivés ? »  

Toutes les quelques secondes,  
ton téléphone demandait au serveur : « Du nouveau ? »  
Et la plupart du temps, la réponse était non.  
Ça s'appelle le polling.  
C'est de ça que parlait l'article de mon pote.  

Chaque « non » coûte de la batterie  
et du travail pour le serveur.  
Dans cet article de 2020, Uber donne le chiffre :  
à un moment, huit requêtes sur dix  
reçues par leur porte d'entrée, l'API gateway,  
étaient du polling.  

Et sur un réseau 2G ou 3G qui coupe,  
chaque échec relançait des requêtes.  
Si tu as déjà fixé une appli qui mouline  
avec une seule barre de réseau,  
tu vois le tableau.  

La solution : retourner la conversation.  
Le téléphone arrête de demander,  
et c'est le serveur qui prévient quand il y a du nouveau.  
Du push.  
Pour ça, Uber a construit RAMEN.  

Non, pas les nouilles.  
Realtime Asynchronous MEssaging Network :  
un réseau de messagerie en temps réel.  
Ils ont clairement trouvé le nom avant.  

RAMEN, c'est trois pièces.  
Pour les comprendre, prends Uber Eats.  

Fireball, c'est le gérant.  
Il voit passer chaque événement :  
un passager commande, un chauffeur accepte, une voiture bouge.  
Et pour chacun, il décide qui doit être prévenu, et quand.  

L'API gateway, c'est la cuisine.  
Elle prépare la commande :  
toutes les données dont ton appli a besoin, au bon format.  

Et le serveur RAMEN, c'est le livreur.  
Il garde une connexion ouverte avec ton téléphone,  
et il livre avec une promesse :  
chaque message arrive au moins une fois.  

En 2020, ça tenait plus d'un million et demi  
de connexions ouvertes en même temps.  

La position de Karim arrive jusqu'à toi, en direct,  
sans vider ta batterie.  
Mais depuis le début, je fais comme si elle était juste.  

## Étape 3 : afficher

En ville, elle peut être fausse de 50 mètres.  
Ce sont les ingénieurs d'Uber qui le disent,  
et parfois c'est pire.  
50 mètres, c'est l'autre côté du boulevard.  
Sur ta carte, Karim t'attend devant la gare.  
En vrai, il est garé en face.  

Si l'appli faisait glisser la voiture d'une position fausse à l'autre,  
Karim arriverait comme dans Fast and Furious :  
à fond, en dérapage, à travers les immeubles.  
Un saut de 50 mètres en une seconde, à l'écran,  
c'est du 180 à l'heure.  

Pourquoi le GPS se trompe autant ?  
Le téléphone de Karim calcule sa position  
avec le temps que mettent les signaux des satellites à lui arriver.  
Mais en ville, il y a des immeubles.  
Un signal tape contre une façade, rebondit,  
et arrive en retard.  
Le téléphone croit alors que le satellite est plus loin qu'en réalité,  
et il se place au mauvais endroit.  

En 2018, des ingénieurs d'Uber ont une idée tordue :  
se servir du problème comme d'un indice.  

Sur Android, le téléphone connaît la force du signal de chaque satellite.  
Signal faible ?  
Il y a sûrement un immeuble entre lui et le satellite.  
Signal fort ?  
La voie est libre.  
On compare ça à une carte 3D de la ville,  
et on en déduit de quel côté de la rue il se trouve.  
Ils se repèrent grâce à l'ombre des immeubles.  

Et pour suivre la voiture,  
ils éparpillent dans la rue des milliers de voitures possibles.  
À chaque mesure, celles qui collent avec les signaux restent,  
les autres disparaissent.  
C'est un filtre à particules, testé à San Francisco.  

## Parenthèse Kalman : coupable au montage

Petite parenthèse pour les devs.  
On lit souvent qu'Uber utilise un filtre de Kalman.  
Dans cet article, les ingénieurs expliquent  
pourquoi ils ne l'ont pas pris pour ce problème-là :  
Kalman suppose une erreur en forme de cloche, avec un seul pic.  
En ville, la position possible en a plusieurs.  

## Fin de la parenthèse

Même juste, la position arrive par à-coups.  
Le réseau coupe sous un pont, un message arrive en retard.  
Si l'appli affichait juste la dernière position reçue,  
la voiture se téléporterait.  
Comme un coéquipier qui lagge sur Monster Hunter  
et réapparaît trois mètres plus loin,  
en plein dans les pattes du Rathalos.  

Uber n'a pas détaillé comment l'appli anime ses voitures.  
Mais les jeux en ligne utilisent un vieux principe :  
entre deux positions, on fait glisser la voiture.  
Et si la suivante tarde, on devine où elle devrait être,  
avec sa dernière vitesse et sa direction.  
C'est la navigation à l'estime,  
dead reckoning en anglais.  
Les marins faisaient déjà ça avant le GPS.  

Et ça nous ramène à la question du début.  

## Les voitures fantômes

En juillet 2015, deux chercheurs, Alex Rosenblat et Luke Stark,  
publient une enquête sur les chauffeurs Uber.  
Ils racontent l'histoire d'une chauffeuse  
qui ouvre l'appli côté passager.  
Sur la carte, quatre voitures juste à côté de son point de départ.  
Et dix-sept minutes d'attente pour la plus proche.  

Le support d'Uber lui répond que la carte,  
c'est « plutôt un effet visuel ».  
Et même :  
« Mieux vaudrait voir ça comme un économiseur d'écran. »  

Officiellement, Uber dément.  
D'après eux, le but, c'est des voitures aussi précises que possible,  
et la latence peut les décaler.  
Et l'appli n'afficherait que les huit plus proches,  
donc il y en aurait plutôt plus que ce que tu vois.  

Sur les forums, certains chauffeurs avaient leur explication :  
un décalage de 30 à 60 secondes.  
Ce décalage, tu sais maintenant d'où il peut venir :  
des messages en retard,  
et une appli qui fait glisser les voitures en devinant.  
Mais d'autres chauffeurs voyaient des fantômes  
partout où le passager posait son épingle.  
Ça, aucun décalage ne l'explique.  

Cette enquête date de 2015, et l'appli a beaucoup changé depuis.  
Mais la voiture qui glisse sur ta carte,  
maintenant, tu sais ce que c'est :  
au mieux, la position d'un chauffeur d'il y a quelques secondes,  
en partie devinée.  

## Outro

On récapitule le trajet.  
Le téléphone de Karim envoie une position  
qui peut être fausse de 50 mètres.  
Uber la range dans un hexagone.  
Fireball décide qu'elle mérite de te déranger.  
RAMEN te la livre.  
Et ton appli la fait glisser  
pour que tu ne voies jamais les trous.  

Tout ça pour un geste que tu fais en deux secondes.  

Alors, mon pote avait raison ?  
Afficher des éléments sur une carte,  
je l'ai fait dans mes applis Flutter.  
Tout ce qu'on vient de voir, c'est ce qu'il faut en plus  
quand des millions de personnes regardent la même carte en même temps.  
Donc oui, les ingés d'Uber, c'est des génies.  

**⟦optionnel : la partie qui t'a le plus surpris, et pourquoi, en une ou deux phrases⟧**

Et H3 est open source.  
Trois lignes de Python,  
et tu découpes ta ville en hexagones  
d'environ 200 mètres de côté.  

Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche,  
une par une.  
Laquelle tu veux que j'ouvre ensuite ?  
Dis-le en commentaire,  
et abonne-toi pour la voir.  

Et en attendant, la vidéo juste là,  
c'est un dev qui a recréé sept logiciels Adobe avec une IA.  
J'ai testé ses clones.  

## En réserve : SSE et gRPC (~45 s)
*(à enregistrer seulement pour garder l'option au montage ; se place après « un million et demi de connexions ouvertes en même temps »)*

Mais il y avait un défaut.  
La première version reposait sur SSE,  
une technologie où seul le serveur parle.  
Le téléphone envoyait ses « bien reçu » par une autre porte,  
toutes les trente secondes.  
Donc pendant trente secondes,  
Uber ne savait pas si son message était arrivé.  

Pour une offre de course envoyée à un chauffeur,  
c'est une éternité.  
Dans un article de 2022, Uber raconte son passage à gRPC :  
les deux côtés parlent en même temps,  
et le « bien reçu » peut repartir tout de suite,  
par la même connexion.  
