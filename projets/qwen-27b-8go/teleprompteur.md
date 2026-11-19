Sur une carte de 8 gigas, tu changes un seul fichier,
et Qwen 27B passe de 3,2 à 18 tokens par seconde.
Même modèle, même carte, rien acheté.

Sauf que c'est une seule mesure publiée,
sur une GTX 1080 Ti limitée à 8 gigas.
Du coup, la vraie question :
qu'est-ce que ce fichier te fait perdre en échange ?

Dans cette vidéo, on va voir
comment ce fichier fait tout tenir dans 8 gigas,
ce qu'il te coûte en mémoire de conversation,
et ce qu'il te coûte en qualité.
Et reste jusqu'à la fin :
il y a un travail que ce fichier rate presque 9 fois sur 10,
dans les tests de ceux qui le fabriquent.

D'abord, ce que ça change en vrai.
Prends une réponse de 500 tokens.
À 3,2 tokens par seconde, tu attends 2 minutes 36.
À 18, c'est 28 secondes.
Juste une division, mais ça donne l'idée.

Du coup, cet écart change ta façon de parler à l'IA.
Quand chaque réponse prend 2 minutes et demie,
tu n'oses plus demander une précision.
Tu prépares un gros pavé pour éviter les allers-retours.
À 28 secondes, tu peux relancer, corriger.
Ça redevient une discussion.

Par contre, ce gain ne touche que l'écriture.
Avant d'écrire, le modèle lit ta demande,
et cette lecture reste à peu près la même avec les 2 fichiers.
Et s'il réfléchit avant de répondre,
cette réflexion, ce sont aussi des tokens à écrire.
Une réponse courte à l'écran
peut donc cacher beaucoup plus de travail derrière.

Mais alors, d'où vient ce gain ?
L'ancien fichier ne tenait pas dans la carte.
Une partie tournait dans la RAM du PC, avec le processeur.
Et la carte passait son temps à l'attendre.
En gros, c'est un cuisinier dont la moitié des ingrédients
est dans une autre pièce :
il a beau être rapide,
il passe son temps à courir chercher ce qui lui manque.

En fait, le nouveau fichier, lui, tient entièrement dans la carte.
Il s'appelle UD-IQ2_XS, il fait 7,63 gigas,
et Unsloth l'a mis à jour le 11 novembre.
Le nom complet est à l'écran.

Sauf que pour rentrer, le modèle a dû maigrir.
Ses nombres sont rangés avec moins de précision :
c'est la quantification.
Le modèle garde son nom,
mais il ne répond plus tout à fait pareil.

Au passage, le MTP,
le module qui doublait la vitesse dans la vidéo précédente,
est laissé de côté dans cette mesure, faute de place.
Ce 18, c'est sans lui.

Voilà ce que t'as gagné.
Maintenant, ce que ça te coûte.
Et le premier prix, c'est la place.

Le fichier fait 7,63 gigas, ta carte en a 8.
Sauf que le modèle n'est pas seul dans la carte.
Le moteur a besoin d'espace pour travailler,
ton bureau en prend aussi,
et surtout, il faut garder la conversation quelque part.
La taille du fichier ne te dit donc pas
combien de discussion il te reste.

Cette mémoire de la conversation, c'est le cache KV.
Dans la mesure, avec un cache en 8 bits,
il reste environ 14 000 tokens.
Ta demande et tout ce que le modèle écrit, sa réflexion comprise,
se partagent cette place.
Pour discuter, c'est correct.
Pour coller un long document, ça part vite.

Et la bonne nouvelle, c'est que ça tient la vitesse.
Avec presque 14 000 tokens dedans,
l'écriture est encore à 15 tokens par seconde.

Tu peux aussi compresser ce cache encore plus, en 4 bits.
Là, celui qui a mesuré monte à environ 22 500 tokens.
Par contre, avec ce cache 4 bits plein,
l'écriture tombe autour de 12 tokens par seconde.
C'est un autre réglage, avec son propre prix.

Et quand il a rempli la mémoire au-delà de 24 000 tokens,
ça a planté.
Le modèle se charge,
c'est la discussion qui finit par ne plus rentrer.

Pour des échanges courts, tu ne vois même pas cette limite.
Sauf que pour une longue session,
avec des fichiers et un historique,
c'est elle qui commande.

Si cette vidéo t'aide à voir ce que ta carte peut vraiment faire,
abonne-toi.

Le deuxième prix, c'est la qualité.
Et là, les chiffres viennent d'Unsloth, ceux qui fabriquent le fichier.
C'est leur campagne de tests, pas une vérification indépendante.
Et leurs tests tournent avec une très longue conversation
et la réflexion poussée au maximum.
Rien à voir avec une carte de 8 gigas.
Ces scores montrent où ça casse,
ils ne te donnent pas ton taux de réussite à toi.

Sur LiveCodeBench, des exercices de programmation,
le modèle complet, sans compression, est autour de 89,
le petit fichier autour de 85.
Franchement, pour un modèle compressé à ce point, il tient bien.

Alors, à ton avis, ça tient aussi
quand on lui confie un vrai projet ?

Sur leur test d'agent,
où le modèle travaille seul dans un dépôt de code,
le modèle complet réussit environ 40 % des tâches.
Le petit fichier, environ 13 %.
Là, ça dégringole.
Et l'ancien fichier, celui qui tournait à 3,2 tokens par seconde,
reste autour de 36 %.
Donc sur ce travail-là,
le petit fichier réussit 3 fois moins souvent que le modèle complet.

En fait, quand tu lui demandes d'aider sur une fonction,
tu lis sa réponse, et tu juges toi-même.
Un agent, lui, enchaîne les décisions tout seul,
il modifie plusieurs fichiers,
et une erreur au début se paie à toutes les étapes d'après.

Le compteur du début ne suffit plus, du coup.
Une réponse en 28 secondes que tu dois réparer
peut te coûter plus cher qu'une réponse lente qui marche.

Et si tu es sur LM Studio ?
Sa documentation a les mêmes réglages :
la part du modèle sur la carte, la taille de la conversation,
et le cache en 8 ou en 4 bits.
Sauf que toutes ces vitesses ont été mesurées dans llama.cpp,
pas dans LM Studio.
Et l'option pour couper la réflexion
dépend de la façon dont le modèle est configuré.

Alors, verdict.

Pour discuter, te faire expliquer un truc :
c'est le bon fichier.
Dans la mesure, le modèle tient en entier dans les 8 gigas,
et il écrit plus de 5 fois plus vite.
Tant que la conversation reste courte, la place suffit.

Pour te faire aider sur un bout de code :
dans leurs tests, les exercices de programmation tiennent bien.
Par contre, tu relis tout,
et tu ne lui donnes pas tout ton projet d'un coup.

Pour un agent qui travaille seul sur un projet entier :
garde l'ancien fichier, quitte à attendre à 3,2 tokens par seconde.
Parce que dans leurs tests, le petit fichier rate presque 9 fois sur 10.
L'ancien, à peu près 2 fois sur 3.
Aller plus vite pour se tromper plus souvent, ça sert à rien.

Alors, ce que ce fichier te fait perdre, tu le sais maintenant :
pour discuter, un peu de place et un peu de qualité.
Pour un agent, beaucoup trop.
Donc la même carte de 8 gigas peut faire 2 métiers différents,
selon le fichier que tu lui donnes.

Jeudi, on regarde les cartes par budget,
pour voir ce que plus de mémoire t'apporte vraiment.
Allez, salut !
