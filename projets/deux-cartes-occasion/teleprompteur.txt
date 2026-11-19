Tu peux payer 1000 euros de plus pour la même quantité de mémoire :
32 gigas sur une seule carte,
chez le même marchand, le même jour.
Et même avec ces 32 gigas, Qwen 27B en 4 bits,
avec sa conversation la plus longue,
te laisse moins d'un giga de marge.

Du coup, pour faire tourner Qwen 27B chez toi,
quelle route vers 32 gigas tu prends,
et quel piège elle te cache ?

Aujourd'hui, on va voir combien de mémoire Qwen 27B prend vraiment,
conversation comprise.
Ensuite, 3 routes vers 32 gigas,
avec leurs prix relevés chez LDLC le 16 novembre,
et le piège de chacune, celui qui n'est pas écrit sur l'étiquette.
Et à la fin, ce que ces 1000 euros de plus t'achètent vraiment,
et la route que je prendrais selon le PC que tu as déjà.

Première réponse, et elle peut déjà t'économiser une carte :
pour Qwen 27B en 4 bits, avec une conversation courte,
24 gigas suffisent.
Donc les 32, en fait, c'est pour lui laisser une longue mémoire.

Parce que voilà le truc :
pendant que tu discutes, le modèle garde des notes sur tout ce qui a été dit.
Ton fichier, lui, ne bouge pas.
Sauf que cette réserve-là grossit à chaque message.

Et on peut la calculer, à partir de la configuration officielle du modèle.
Avec un cache en 16 bits,
c'est environ 2 gigas pour 32 000 tokens,
8 pour 128 000,
et 16 pour la fenêtre complète de 262 000.

Alors fais l'addition avec moi.
Le fichier 4 bits, c'est 16 gigas et demi sur Hugging Face.
Mais compté comme ta carte compte, c'est un peu plus de 15.
Tu ajoutes 16 pour la conversation complète.
Ça fait 31,3.
Sur une carte de 32.
Et ça, c'est avant les tampons et tout le reste du moteur.
Bon, la boîte dit 32 gigas, mais ta marge, elle est déjà partie.

Du coup, avec 32 gigas, le contexte complet, il faut aller le chercher :
en compressant le cache,
ou en raccourcissant un peu la conversation.

Et si t'as qu'une carte de 8 gigas,
on a vu lundi dernier comment Qwen 27B y tourne quand même,
juste en changeant de fichier.
Là, on parle de ceux qui veulent la place.

Première route, la plus tentante :
2 cartes de 16 gigas, et hop, 32.
La moins chère du relevé, c'est l'Intel Arc A770 :
460 euros chez LDLC le 16 novembre.
Donc 2, ça fait 920 euros.
Moins de 1000 euros pour 32 gigas !
Sauf que… ce jour-là, la page affichait une rupture en ligne.
Bref, ta paire à 920 euros, le 16 novembre, tu ne pouvais pas la commander.

Côté NVIDIA, la RTX 5060 Ti de 16 gigas d'ASUS est bien en stock :
1080 euros.
Ça ferait 2160 la paire.
Sauf qu'il y a une petite ligne sous le prix :
limitée à une par client.
En gros, le boss de fin, c'est pas le prix, c'est la règle du magasin.

Et deux RTX 3090 ?
Ça fait 48, mais aucune offre d'occasion vérifiable ce jour-là
pour te donner un vrai prix.

Maintenant, le vrai piège de cette route, c'est ta tour.
Prends la mienne : une carte mère micro-ATX, comme beaucoup d'autres.
D'après son manuel, le deuxième slot a la même longueur que le premier.
Pourtant, il n'a que 4 lignes en PCIe 3.0,
et il passe par le chipset.
Et en plus, il est tout en bas.
Du coup, une carte de 2 slots dedans dépasse sous la carte mère,
et il te faut un boîtier à 5 emplacements.

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
Plus de deuxième slot, plus de câbles en double,
et là, d'un coup, le PC redevient simple.
Et c'est là qu'on retrouve nos 1000 euros du début.

Chez LDLC, toujours le 16 novembre,
la moins chère en stock de mon relevé,
c'est l'Intel Arc Pro B65 d'ASRock :
1800 euros, à 5 centimes près.
Sa grande sœur, la B70, est à 2300.
Côté AMD, la Radeon AI PRO R9700 de Gigabyte est à 2800, en stock.

Donc 32 gigas des 2 côtés, et jusqu'à 1000 euros d'écart.
Alors, ces 1000 euros, ils t'achètent quoi ?
Pas un giga de plus, en tout cas.
Et la vitesse, le prix ne te la dit pas.
Ce que la R9700 a en plus sur le papier,
c'est un guide officiel d'AMD pour y faire tourner ses outils d'IA.
Sauf que, même là, 32 gigas et un guide
ne prouvent pas que chaque moteur la prend en charge.
Du coup, voilà le vrai piège de cette route :
avant de comparer les prix, tu vérifies que ton logiciel gère la carte.

Et chez NVIDIA ?
La RTX 5090 a aussi 32 gigas.
Sauf que la TUF d'ASUS s'affichait à 9400 euros,
avec un seul exemplaire en stock.
Ouais.
Pour ce prix-là, on change carrément de catégorie.

Reste la Tesla V100 de 32 gigas d'occasion,
la carte de serveur qui fait des centaines de milliers de vues en anglais.
Pas d'offre vérifiable dans ce relevé, donc pas de prix.
Par contre, son piège, on le connaît :
NVIDIA a fait du pilote 580 la dernière branche qui la gère,
et CUDA 13 ne compile plus pour elle.
En plus, comme les autres cartes de serveur,
elle n'a ni ventilateur ni sortie vidéo :
tout est à refaire autour.
En fait, elle peut paraître pas chère, et te coûter tout un week-end.

Troisième route, et c'est là que ça devient bizarre.
Le Mac mini M6 avec 32 gigas de mémoire unifiée et 512 de stockage
est affiché 1709 euros chez LDLC le 16 novembre.
Donc un ordinateur complet coûte moins cher
que la carte de 32 gigas la moins chère du relevé.

Sauf que, déjà, le délai dépasse 15 jours.
Et surtout, cette mémoire, elle est partagée :
le système et tes applis se servent dedans.

Côté PC, il y a les mini-PC Ryzen AI Max+,
avec 64 ou même 128 gigas de mémoire partagée.
Celui que j'ai regardé affiche presque 2000 euros en 64 gigas,
sauf que sa page ne dit pas clairement si la TVA est dedans.
Et là encore, la mémoire est fixe :
tu choisis à l'achat, et c'est pour toujours.

Du coup, le piège de cette route, c'est la facture :
tu remplaces ton PC entier,
celui qui te sert aussi à jouer et à bosser.

Et avant de payer, un dernier piège, qui n'est pas technique.
En France, chez un vendeur professionnel, neuf ou d'occasion,
tu as 2 ans de garantie légale, et il ne peut pas les réduire.
Le défaut est présumé exister dès la vente
pendant ces 2 ans pour du neuf, et 12 mois pour de l'occasion.
Et pour un achat à distance,
tu as 14 jours après la réception pour te rétracter.
Donc ces 14 jours, c'est ta fenêtre pour tester la carte.

Par contre, entre particuliers, il te reste seulement les vices cachés,
et c'est à toi de les prouver.

Et si tu regardes depuis Abidjan, Dakar ou Kinshasa :
ces prix sont des prix français,
et ces garanties, c'est le droit français.
Donc chez toi, renseigne-toi sur le recours du vendeur avant de payer.
Par contre, l'addition de la mémoire, les slots et l'alimentation,
ça, c'est valable partout.

Alors, quelle route ?
Ça dépend de ce que tu as déjà.

Si tu as déjà une carte NVIDIA de 16 gigas,
et une tour qui accueille une deuxième carte,
c'est le seul cas où je prendrais une paire :
la moitié est déjà payée.
Regarde la 5060 Ti de 16 gigas, à 1080 euros.
Et du coup, la limite d'une par client ne te gêne plus,
puisque t'en achètes qu'une.
Mais vérifie d'abord ton slot, ton boîtier et tes câbles.

Si tu pars de zéro, moi, je ne commencerais pas par une paire.
Sur le papier, c'est la moins chère,
mais en vrai, c'est elle qui a le plus de pièges.
Donc je prendrais la B65, à 1800 euros :
la moins chère des offres en stock du relevé,
avec la même quantité de mémoire que la R9700 à 2800.
Sauf que, avant de cliquer, tu vérifies que ton logiciel la gère.
S'il ne la gère pas, là, les 1000 euros de la R9700
et son guide officiel peuvent avoir un sens.

Et si tu veux remplacer tout l'ordinateur,
le Mac mini à 1709 euros entre dans la course.
Par contre, souviens-toi de l'addition du début :
31,3 gigas pour la conversation complète.
Sur un Mac de 32 gigas, dont le système prend sa part, en cache 16 bits,
ça ne rentre pas :
tu compresses le cache, ou tu raccourcis.
Et si c'est vraiment la conversation complète que tu veux,
la seule route chiffrée de mon relevé qui dépasse 32 gigas,
c'est le mini-PC Ryzen AI Max+ en 64.

Et en fait, si tu as déjà 24 gigas
et qu'une conversation courte te suffit, garde ton argent.
La meilleure carte, parfois, c'est celle que tu n'achètes pas.

Allez, salut !
