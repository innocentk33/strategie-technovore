Qwen 27B, c'est l'un des meilleurs modèles
que tu peux faire tourner sur ta machine :
plus de 6 millions de téléchargements en un mois.
Sauf que si tu veux faire autre chose que lui demander la météo,
il lui faut de la place pour ta conversation.
Pour être à l'aise : 32 gigas de VRAM.
Et en 2026, la VRAM, c'est de l'or.
Ces 32 gigas, tu peux les payer 2800 euros…
ou, si t'es malin, beaucoup moins.

Du coup, quelle route vers 32 gigas tu prends,
et quel piège elle te cache ?

Dans cette vidéo, on va voir combien de mémoire Qwen 27B prend vraiment.
Ensuite, 3 routes vers 32 gigas,
avec les meilleurs prix relevés le 20 novembre, et le piège de chacune.
La même carte, 400 euros plus chère selon le site où tu cliques,
et un ordinateur entier moins cher qu'une carte de 32 gigas en stock.
Et à la fin, la route que je prendrais selon ton PC.

Première réponse, et elle peut déjà t'économiser une carte :
pour Qwen 27B en 4 bits, avec une conversation courte,
24 gigas suffisent.
Donc les 32, en fait, c'est pour lui laisser une longue mémoire.

Parce que pendant que tu discutes,
le modèle garde des notes sur tout ce qui a été dit.
Ton fichier, lui, ne bouge pas.
Mais ces notes-là, elles grossissent à chaque message.

Et on peut les calculer, à partir de la configuration officielle du modèle.
Avec un cache en 16 bits,
c'est environ 2 gigas pour 32 000 tokens,
8 pour 128 000,
et 16 pour la fenêtre complète de 262 000.

Alors fais l'addition avec moi.
Le fichier 4 bits, c'est 16 gigas et demi sur Hugging Face.
Mais compté comme ta carte compte, c'est un peu plus de 15.
Tu ajoutes 16 pour la conversation complète.
Ça fait 31,4.
Sur une carte de 32.
Et ça, c'est avant les tampons et tout le reste du moteur.
Bon, la boîte dit 32 gigas, mais ta marge, elle est déjà partie.

Du coup, avec 32 gigas, le contexte complet, il faut aller le chercher :
en compressant le cache,
ou en raccourcissant un peu la conversation.

Et si t'as qu'une carte de 8 gigas,
on a vu dans une vidéo précédente
comment Qwen 27B y tourne quand même,
juste en changeant de fichier.
Là, on parle de ceux qui veulent la place.

Première route, la plus tentante :
2 cartes de 16 gigas, et hop, 32.
Prends la RTX 5060 Ti de 16 gigas, la Dual d'ASUS.
Le 20 novembre, sur Amazon, elle était à 800 euros, en stock.
Donc 1600 la paire, sans limite affichée sur la page.
Chez LDLC, le même modèle était à 1080 euros,
avec une petite ligne au-dessus du bouton panier :
limitée à une par client.
280 euros de plus pour le même modèle, le même jour.
En gros, le boss de fin, c'est le site où tu cliques.

Et chez AMD ?
La Radeon RX 9060 XT de 16 gigas d'ASUS
était à 700 euros sur Amazon, donc 1400 la paire.
Moins cher, mais ce jour-là, la livraison était annoncée du 3 au 5 janvier.
Bref : Noël sans cartes.
L'Intel Arc A770 ? 460 euros chez LDLC, mais en rupture en ligne.

Et en occasion, le 20 novembre, une 5060 Ti de 16 gigas
tournait autour de 600 à 670 euros sur leboncoin.
Entre particuliers, par contre : garde ça en tête pour tout à l'heure.

Maintenant, le vrai piège de cette route, c'est ta tour.
Prends la mienne : une carte mère micro-ATX, comme beaucoup d'autres.
D'après son manuel, le deuxième slot a la même longueur que le premier.
Pourtant, il n'a que 4 lignes en PCIe 3.0,
et il passe par le chipset.
Et en plus, il est tout en bas.
Du coup, une carte de 2 slots dedans dépasse sous la carte mère,
et il te faut un boîtier à 5 emplacements.
Et les 5060 Ti et 9060 XT du relevé sont plus épaisses :
2 slots et demi, donc mesure la place sous ta carte mère.

Ensuite, l'alimentation.
La mienne fait 1000 watts.
Sauf qu'avec ma RTX 5080 branchée,
il ne me resterait peut-être que 2 prises 8 broches.
Donc avant d'acheter la deuxième carte,
tu regardes ton boîtier, et tu comptes tes câbles.

Et le dernier piège, c'est la vitesse.
Par défaut, llama.cpp coupe le modèle en tranches de couches,
une tranche par carte.
Et pour une seule conversation, elles travaillent chacune leur tour.
En fait, la mémoire s'additionne,
mais la vitesse, elle, ne double pas.

Bref, 2 cartes, c'est de la place, pas de la vitesse.
Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Deuxième route : une seule carte de 32 gigas.
Plus de deuxième slot, et d'un coup, le PC redevient simple.

Le 20 novembre, la moins chère en stock de mon relevé,
c'était l'Intel Arc Pro B65 d'ASRock : 1900 euros chez LDLC.
Sur Amazon, des B65 de vendeurs tiers descendaient à 1483 euros,
mais livrées en décembre.
Sa grande sœur, la B70 d'ASUS, était à 2016 euros sur Amazon, en stock.
Côté AMD, la Radeon AI PRO R9700 de Gigabyte : 2400 euros sur Amazon.
Et chez LDLC, exactement la même référence : 2800.

Alors, ces 400 euros de plus, ils t'achètent quoi ?
Rien. C'est la même carte.
Donc le vrai match, c'est Intel à 1900 contre AMD à 2400.
Et là, 500 euros de plus ne t'achètent pas un giga de plus.
Côté AMD, j'ai trouvé un guide officiel
pour faire tourner ses outils d'IA sur la R9700.
Mais 32 gigas et un guide
ne prouvent pas que chaque moteur la prend en charge.
Du coup, voilà le vrai piège de cette route :
avant de comparer les prix, tu vérifies que ton logiciel gère la carte.

Et chez NVIDIA ?
La RTX 5090 a aussi 32 gigas.
Sur Amazon, elle partait à presque 7000 euros, chez un vendeur tiers,
livrée fin décembre.
Et chez LDLC, 9400 euros, en rupture.
Pour ce prix-là, on change carrément de catégorie.

Reste la Tesla V100 de 32 gigas d'occasion.
Pas d'offre vérifiable dans ce relevé, donc pas de prix.
Par contre, son piège, on le connaît :
NVIDIA a fait du pilote 580 la dernière branche qui la gère,
et CUDA 13 ne compile plus pour elle.
En plus, comme les autres cartes de serveur,
elle n'a ni ventilateur ni sortie vidéo :
tout est à refaire autour.
En fait, elle peut paraître pas chère, et te coûter tout un week-end.

Troisième route : changer carrément d'ordinateur.
Le Mac mini M6 avec 32 gigas de mémoire unifiée et 512 de stockage
était affiché 1709 euros chez LDLC le 20 novembre.
Donc un ordinateur complet coûtait moins cher
que n'importe quelle carte de 32 gigas en stock de mon relevé.

Premier hic : lui, il n'était pas en stock : plus de 15 jours.
Et en acceptant d'attendre, une B65 de vendeur tiers descendait à 1483.
Et surtout, cette mémoire, elle est partagée :
le système et tes applis se servent dedans.

Côté PC, il y a les mini-PC Ryzen AI Max+,
avec 64 ou même 128 gigas de mémoire partagée.
Celui que j'ai regardé affichait autour de 2000 euros en 64 gigas,
en précommande.
Seulement, sa page ne dit pas clairement si la TVA est dedans.
Et sa mémoire est fixe, pour toujours.

Du coup, le piège de cette route, c'est la facture :
tu remplaces ton PC entier.

Et avant de payer, un dernier piège, qui n'est pas technique.
En France, chez un vendeur professionnel, neuf ou d'occasion,
tu as 2 ans de garantie légale, et il ne peut pas les réduire.
Le défaut est présumé exister dès la vente
pendant ces 2 ans pour du neuf, et 12 mois pour de l'occasion.
Et pour un achat à distance,
tu as 14 jours après la réception pour te rétracter.
Donc ces 14 jours, c'est ta fenêtre pour tester la carte.

Par contre, entre particuliers, comme sur leboncoin,
pas de rétractation, pas de garantie légale :
il te reste seulement les vices cachés, et c'est à toi de les prouver.
Donc ta 5060 Ti d'occasion, tu la vois tourner avant de payer.

Et si tu regardes depuis Abidjan, Dakar ou Kinshasa :
ces prix sont des prix français,
et ces garanties, c'est le droit français.
Donc chez toi, renseigne-toi sur le recours du vendeur avant de payer.
Par contre, l'addition de la mémoire, les slots et l'alimentation,
ça, c'est valable partout.

Alors, quelle route ?
Ça dépend de ce que tu as déjà.
Et les prix, c'est ceux du 20 novembre.

Si t'as déjà une NVIDIA de 16 gigas, et la place pour une autre,
ajoute une 5060 Ti de 16 gigas :
800 euros neuve sur Amazon, ou autour de 600 à 670 d'occasion.
La moitié de tes 32 gigas est déjà payée.

Si t'as pas encore de carte, et que ta tour en accepte 2,
la paire de 5060 Ti à 1600 euros
était le chemin en stock le moins cher vers 32 gigas.
Avec tous les pièges de la route :
la place, les câbles, et une vitesse qui ne double pas.
La paire de 9060 XT coûtait moins, mais arrivait en janvier.

Pour une seule carte, je prendrais la moins chère en stock :
la B65, à 1900 euros chez LDLC.
Regarde juste sa prise d'alimentation, une 12V-2x6 :
il te faut ce câble, ou un adaptateur.
Si tu préfères Amazon, sa grande sœur, la B70, était à 2016, en stock.
Et dans tous les cas, tu vérifies que ton logiciel gère la carte.
S'il ne gère pas Intel, regarde la R9700 de Gigabyte :
2400 euros sur Amazon, pas 2800.

Si tu veux remplacer tout l'ordinateur,
le Mac mini à 1709 euros entre dans la course.
Par contre, souviens-toi de l'addition du début :
31,4 gigas pour la conversation complète.
Sur un Mac de 32 gigas, dont le système prend sa part,
en cache 16 bits, ça ne rentre pas :
tu compresses le cache, ou tu raccourcis.
Et si c'est vraiment la conversation complète que tu veux,
la seule route chiffrée de mon relevé qui dépasse 32 gigas,
c'est le mini-PC Ryzen AI Max+ en 64, autour de 2000 euros.

Et en fait, si tu as déjà 24 gigas
et qu'une conversation courte te suffit, garde ton argent.
La meilleure carte, parfois, c'est celle que tu n'achètes pas.

Allez, salut !
