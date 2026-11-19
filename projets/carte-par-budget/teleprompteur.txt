Tu t'apprêtes à mettre 600 euros dans une carte graphique au Black Friday,
pour faire tourner une IA chez toi ?
Regarde : une RTX 3060 de 2021 écrit à 42 tokens par seconde.
Une RTX 4060 Ti 16 gigas de 2023, à 34.
Même testeur, même modèle, dans des mesures publiées.

La plus vieille, avec moins de mémoire, écrit plus vite.
Pourtant, en jeu, c'est la 4060 Ti qui gagne,
avec environ 45 % d'images par seconde en plus.
Du coup, si tu choisis ta carte comme pour le jeu,
tu peux te retrouver avec une IA plus lente.

Dans cette vidéo, on va voir
les 2 lignes de la fiche technique qui comptent pour l'IA,
pourquoi la RTX 4060 n'est pas l'affaire qu'elle a l'air d'être,
et comment calculer un chiffre que Nvidia n'écrit même pas sur ses pages.
Et reste jusqu'à la fin :
je te dis quelle carte prendre avec 600 euros,
aux prix relevés le 18 novembre.

D'abord, une autre série de mesures, encore plus parlante.
3 cartes de la même famille :
la RTX 4070, la 4070 Super et la 4070 Ti.
Sur le papier, la Ti a près de 40 %
de puissance de calcul en plus.
Du coup, pour lire ta question,
elle va bien 29 % plus vite que la 4070.

Sauf que pour écrire la réponse,
141, 142 et 143 tokens par seconde.
Pareil, à 2 tokens près.
Tu paies la carte la plus musclée,
et ton IA écrit à la même vitesse.

Leur point commun, c'est une ligne que presque personne ne regarde :
le débit mémoire.

Pour comprendre, imagine que le modèle est un énorme livre,
rangé dans la mémoire de la carte.
À chaque mot qu'elle écrit, la carte doit relire tout le livre.
Pas un chapitre : tout.
Donc ce qui compte, ce n'est pas la force de la carte,
c'est la vitesse à laquelle elle tourne les pages.
Ça, c'est le débit mémoire.

En gros, le calcul, lui, sert surtout à lire ta question.
C'est là que la 4070 Ti gagnait ses 29 %.
Mais une fois que l'IA écrit,
c'est la mémoire qui donne le rythme.

Alors, pour l'IA, sur une fiche technique,
tu regardes 2 lignes, et dans cet ordre.

Ligne 1 : la quantité de mémoire.
C'est elle qui décide de ce qui rentre.
Si le modèle ne tient pas dans la carte,
une partie part dans la RAM du PC,
et là, c'est le processeur qui donne le rythme.
Le débit de ta carte ne sert plus à grand-chose.

Un exemple concret : Qwen 27B.
Dans sa version en 4 bits, rien que le fichier fait 14,4 gigas.
Ça rentre dans 16 gigas, de justesse.
Dans 12, non.
Pour le faire tenir dans 12, il faut un fichier plus compressé, 10,9 gigas.
Et dans la vidéo précédente, on l'a fait tenir dans 8,
avec un fichier de 7,6 gigas.
Sauf que plus tu compresses, plus le modèle perd en qualité.
Donc plus de mémoire, c'est un fichier moins compressé, et de meilleures réponses.

Voilà ce que les 16 gigas de la 4060 Ti du début
t'apportent quand même : la place.
Donc elle écrit moins vite, mais elle peut charger un fichier
que la 3060 doit compresser davantage.

Ligne 2 : à mémoire égale, le débit mémoire.
C'est lui qui décide à quelle vitesse ça écrit.

Reprends la série de mesures du début.
Même testeur, même logiciel, même modèle, qui rentre partout.
La 3090 : 87 tokens par seconde.
La 5070 : 59.
La 5060 Ti 16 gigas : 51.
La 3060 12 gigas : 42.
La 4060 Ti 16 gigas : 34.

Maintenant, leur débit mémoire, carte par carte :
936, 672, 448, 360, 288.
Ça descend pareil.

Par contre, il y a des limites.
Ce n'est pas proportionnel :
la 3090 a 2 fois plus de débit que la 5060 Ti,
mais elle n'écrit que 1,7 fois plus vite.
Ça ne marche pas non plus d'une marque à l'autre,
on va le voir avec Intel au moment du verdict.
Et sur un modèle plus gros, un 14B,
la 3060 et la 4060 Ti finissent à égalité.
Donc le débit, tu t'en sers pour départager des cartes proches.
Par contre, pas pour prédire un chiffre.

Le problème, c'est que Nvidia ne l'écrit même pas sur ses fiches.
Du coup, tu vas le calculer toi-même.
Tu cherches 2 chiffres.
La largeur du bus mémoire, en bits.
Et la fréquence de la mémoire, en gigabits par seconde.
Tu multiplies les 2, et tu divises par 8.

On le fait sur la RTX 4060.
Bus de 128 bits, mémoire à 17.
128 fois 17, divisé par 8 : 272 gigas par seconde.

Maintenant la RTX 3060 Ti.
Bus de 256 bits, mémoire à 14.
256 fois 14, divisé par 8 : 448.

448 contre 272.
La 3060 Ti est sortie 2 ans et demi plus tôt,
et pourtant elle a 65 % de débit mémoire en plus.
Presque 2 tiers de plus.
En fait, sur toute la série 4060,
Nvidia est passé à un bus de 128 bits.
Même la 4060 Ti 16 gigas reste à 288.

Et côté prix, la 4060, tu la trouves où ?
En neuf, chez les marchands consultés le 18 novembre,
introuvable à prix normal.
La seule offre neuve vue : 924 euros,
chez un vendeur tiers sur Amazon.
D'occasion, elle se trouve entre 360 et 480 euros.
La 3060 Ti d'occasion, entre 260 et 430.
Donc pour le même budget, tu as souvent plus de débit.

Attention : là, on compare des fiches, pas des mesures.
Et surtout, la 3060 Ti n'a que 8 gigas.
Ligne 1 d'abord, tu te souviens ?

Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Le calcul de chaque carte est dans le tableau à l'écran.
Mémoire, débit, prix relevé, marchand.
Mets pause et fais une capture si tu veux.

Maintenant, ce que tu trouves vraiment autour de 600 euros en neuf.
La RTX 5060 dès 520 euros.
La 5060 Ti 8 gigas, entre 590 et 600.
La RX 9060 XT 8 gigas, 540.
Donc à 600 euros, en neuf, 8 gigas, c'est la norme.
Les 2 Nvidia ont un bon débit, 448,
mais seulement 8 gigas.
On retombe sur la ligne 1.

En 12 gigas, tu as la RTX 3060, dès 510 euros.
Et l'Arc B580 d'Intel, 500 euros, en stock limité.

Et en 16 gigas ?
Sous 700 euros, une seule carte :
la RX 9060 XT 16 gigas, sur Amazon,
entre 670 et 700 euros,
et une seule de ces offres est en stock tout de suite.
Son débit mémoire, c'est 320.
La 5060 Ti 16 gigas, elle, est à 800 euros chez Amazon et Cdiscount,
et autour de 1 000 euros dans les boutiques spécialisées.

Alors, le verdict, à 600 euros, aux prix du 18 novembre.
Prends la RTX 3060 12 gigas, à 510 euros chez Cdiscount.
12 gigas, plus que les 5060 et 5060 Ti 8 gigas, pour moins cher.
Et avec 360 de débit, c'est elle
qui écrivait plus vite que la 4060 Ti au début.
D'occasion, la même se trouve entre 250 et 400 euros.

Attention, il existe aussi une RTX 3060 8 gigas, au même prix.
128 bits, mémoire à 14 : 224 de débit.
Donc sur la fiche, vérifie bien que c'est la version 12 gigas.

Et l'Arc B580 ? Plus de débit, et 10 euros de moins.
Sauf que d'une marque à l'autre, la règle ne marche plus.
Dans un tableau de mesures publiées, de testeurs différents,
elle écrit un peu moins vite que la 3060,
et elle lit ta question presque 3 fois moins vite.
Voilà pourquoi je te mets la 3060 devant.

Et si tu peux monter à 700 euros,
la RX 9060 XT 16 gigas, à 700 euros chez Amazon.
C'est le même choix que la 4060 Ti du début :
plus de place, moins de débit.
En fait, tu la prends si tu veux des modèles
qui ne rentrent pas dans 12,
comme le Qwen 27B en 4 bits.

Les prix vont bouger d'ici le Black Friday,
alors refais le calcul avant de payer :
mémoire d'abord, débit ensuite.

Allez, salut !
