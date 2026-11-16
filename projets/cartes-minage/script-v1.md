# 54 Go pour 35 dollars : quelle vieille carte pour ton IA ?

V1 documentaire, 21 janvier 2027. Cible : 10–12 minutes à 145 mots/minute. Faits vérifiés le 16 novembre 2026. Les repères sont provisoires ; aucune manipulation à tourner.

## Voix

[VISUEL : neuf rectangles de 6 Go ; « Achat déclaré : 3 000 RUB, environ 35 USD, Russie, octobre 2026 ». F1–F2. Résultat attribué au propriétaire, pas à la chaîne.]

Neuf vieilles cartes, 54 gigas de mémoire, et plus de 30 tokens par seconde annoncés pour 35 dollars. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc, avec un petit budget en euros ou en francs CFA, quelle partie de cette affaire peux-tu vraiment espérer retrouver ?

On va regarder le modèle qui rend ce résultat possible, puis trois routes d'occasion : les P106, la Tesla P40 et la BC-250. Et on va compter ce qui manque autour. Parce que le prix de neuf cartes trouvées dans un garage ne donne pas encore le prix d'une machine utilisable chez toi.

[VISUEL : texte du propriétaire, prix et SSD manquant surlignés ; schéma original du rig. F1.]

L'histoire commence par une annonce en Russie. Un propriétaire récupère une ancienne ferme de minage dans un garage. Il négocie le lot à 3 000 roubles, environ 35 dollars selon son récit. Les neuf cartes fonctionnent. Par contre, il manque le SSD : il démarre la machine sur une clé USB.

Du coup, on a un achat exceptionnel, situé dans un pays et une négociation précis. Aucun vendeur ne propose automatiquement le même lot à ce tarif. Et le récit ne nous donne ni une facture complète livrée chez toi, ni une garantie sur neuf autres cartes du même âge.

Le résultat annoncé reste intéressant : Qwen3.6, 35 milliards de paramètres au total, dont environ 3 milliards activés pour chaque token. Dans Ollama, le propriétaire indique dépasser 30 tokens par seconde. Il pense utiliser la quantification par défaut, probablement en 4 bits. Le contexte et les répétitions ne sont pas précisés.

Donc on garde le résultat comme un témoignage. On peut expliquer pourquoi ce type de modèle convient à ce matériel, sans promettre la même vitesse à tout le monde. Le détail qui change la lecture de l'histoire, c'est ce petit « 3 » dans le nom du modèle.

[GRAPHIC] [VISUEL : 35 milliards stockés, environ 3 milliards activés ; ne pas dessiner une mémoire occupée de 3 Go. F3.]

Un mélange d'experts conserve beaucoup de poids disponibles, mais n'en sollicite qu'une partie pour produire chaque token. Il peut donc profiter d'une grande capacité mémoire tout en limitant le travail actif. En revanche, les poids qui ne participent pas à ce token doivent rester accessibles pour les suivants.

Imagine une bibliothèque avec plusieurs spécialistes. Tu gardes leurs livres sur les étagères, même quand un seul groupe répond à ta question. C'est pour ça que « 3 milliards actifs » ne veut pas dire « un modèle de 3 milliards à télécharger ». La capacité nécessaire et le travail de chaque réponse restent deux choses différentes.

Sauf que cette propriété ne se transfère pas automatiquement à un modèle dense. Dans ce dernier, beaucoup plus de poids participent à chaque étape. Une grosse réserve de mémoire lente peut alors charger le modèle tout en te laissant attendre sa réponse. Les gigas et les tokens par seconde racontent deux parties du résultat.

[VISUEL : calcul pédagogique « 192 / 42,5 ≈ 4,5 », immense étiquette « ESTIMATION — AUCUN TEST 70B ». F4–F6.]

Tu as peut-être vu passer un autre chiffre : un modèle dense de 70 milliards tournerait à environ 4,5 tokens par seconde sur ce montage. En fait, ce chiffre vient d'un calcul théorique dans un article. Le propriétaire ne publie pas ce test-là.

Le calcul suppose un fichier de 42,5 gigas et environ 192 gigas par seconde de bande passante mémoire par carte. On répartit les tranches du modèle, puis un token traverse ces tranches successivement. Diviser 192 par 42,5 donne environ 4,5. On a encore ignoré les autres coûts.

Donc les neuf capacités s'additionnent, mais on ne multiplie pas simplement la vitesse d'une carte par neuf dans ce scénario. Et cette estimation ne décrit ni tous les moteurs ni les optimisations possibles. Elle sert à comprendre pourquoi « ça rentre » ne suffit pas à prédire « ça répond vite ».

Si tu veux d'autres choix d'IA locale expliqués avec les conditions des chiffres, abonne-toi.

[VISUEL : P106 schématique, six blocs mémoire ; caractéristiques Gigabyte, révision précisée. F4/F8.]

Première route : une P106 à bas prix. La référence Gigabyte documentée possède 6 gigas de GDDR5. À l'unité, cette capacité te limite vite ; en groupe, elle devient intéressante pour un modèle dont le moteur sait répartir les poids. Du coup, le lot complet et sa compatibilité comptent davantage que le prix d'une carte isolée.

Le nom exact mérite aussi ton attention. Une P106-090 et une P106-100 ne sont pas une seule référence. Même dans la famille P106-100, la fiche d'une révision ne prouve pas les caractéristiques de toutes les autres. Une annonce qui écrit seulement « équivalent GTX 1060 » laisse encore des questions ouvertes.

Par contre, le logiciel ajoute une limite que le nombre de gigas ne montre pas. Ces cartes appartiennent à une ancienne génération. NVIDIA a retiré de CUDA 13 la compilation destinée à plusieurs anciennes architectures. Les programmes déjà construits avec une version antérieure peuvent continuer avec le pilote compatible.

Donc ce matériel ne s'est pas arrêté de fonctionner le jour de CUDA 13. En revanche, la prochaine version du programme que tu veux utiliser peut demander un autre chemin. La documentation actuelle d'Ollama impose aussi des conditions de pilote pour les anciennes générations ; elle ne nomme pas toutes les cartes de minage.

Pour un premier PC destiné à travailler chaque jour, cette incertitude a un coût pratique. Si tu récupères déjà un rig fonctionnel et documenté, le pari change. Voilà pourquoi une affaire pertinente pour un passionné équipé peut devenir une dépense pénible pour quelqu'un qui doit tout assembler.

[VISUEL : P40, 24 Go, flux d'air dessiné ; « serveur / 250 W maximum constructeur ». F9.]

Deuxième route : la Tesla P40. Elle offre 24 gigas sur une seule carte. On réduit donc le nombre de cartes nécessaires pour obtenir cette capacité. Elle figure aussi dans la documentation matérielle d'Ollama, sous les conditions de sa génération.

Sauf que son refroidissement a été conçu pour recevoir le flux d'air d'un serveur. Une carte passive ne crée pas elle-même ce flux. Le boîtier et la ventilation deviennent une partie du projet. Et son connecteur d'alimentation est décrit précisément dans le manuel : la forme seule ne permet pas de choisir un câble.

Du coup, le prix d'une P40 nue doit se comparer à une solution refroidie et alimentée correctement. Ce choix peut intéresser quelqu'un qui possède déjà un environnement compatible. Dans une petite tour silencieuse, la même carte demande d'autres compromis. Aucun résultat de la ferme à neuf P106 ne donne directement la vitesse de cette P40.

[VISUEL : BC-250 = carte complète CPU/GPU ; un seul réservoir de 16 Go, partagé avec le système. F10.]

Troisième route : la BC-250. Ici, on achète une carte complète avec processeur et circuit graphique, autour d'une mémoire partagée de 16 gigas. On ne l'ajoute donc pas au PC comme une carte graphique classique. Elle constitue la base d'une autre machine.

Des propriétaires documentent son usage avec Linux et Vulkan. Leurs configurations peuvent employer un BIOS communautaire et des réglages particuliers de mémoire. En fait, ces détails expliquent une partie du travail caché derrière les vidéos où tout semble déjà prêt.

Les 16 gigas servent au système, aux poids, au contexte et aux autres besoins. Deux tas de mémoire affichés par le pilote peuvent désigner la même mémoire physique. Il faut donc éviter de les additionner. Et une vidéo de jeu sur BC-250 ne valide pas automatiquement ton logiciel d'IA.

Cette route intéresse surtout quelqu'un qui accepte une machine communautaire, avec ses versions et sa documentation. Le prix de la carte seule laisse encore le stockage, l'alimentation, le refroidissement et les accessoires à compter. Par contre, elle peut avoir du sens quand tu veux construire une petite machine séparée pour apprendre.

[GRAPHIC] [VISUEL : budget d'exemple 100 € = environ 65 600 FCFA BCEAO ; « conversion, hors livraison et importation ». Tableau des prix marchands : [PRIX À RELEVER]. F11–F12.]

Pour le budget, prenons un exemple rond : 100 euros représentent environ 65 600 francs CFA en zone BCEAO. C'est une conversion de budget. Elle ne prouve pas qu'une carte affichée à 100 euros en France arrivera chez toi pour cette somme.

Donc le tableau utile ajoute les pièces manquantes, la livraison, les frais éventuels et la possibilité de retour. Un lot moins cher mais impossible à renvoyer peut exposer une plus grande part de ton budget. Et une machine complète disponible localement peut changer la comparaison avec une carte nue importée.

Au moment de cette recherche, je n'ai pas de relevé suffisamment vérifié pour te donner un vainqueur TTC livré en France et dans plusieurs pays africains. Les emplacements de prix restent donc indiqués dans le dossier. Le critère reste applicable : comparer des machines utilisables pour ton modèle, avec le même contexte et les mêmes pièces comprises.

[CROCHET : ton avis personnel sur le temps que tu accepterais de consacrer à une machine d'occasion, facultatif.]

Si tu as déjà le rig et un modèle MoE adapté, récupérer ces cartes peut ouvrir des possibilités. Si tu veux surtout travailler sans gérer des versions anciennes, une carte plus récente et documentée mérite sa place dans la comparaison. Et si ton budget est très serré, le petit modèle qui tient dans ta machine actuelle reste une option à regarder avant l'achat.

La semaine prochaine, on pousse justement cette piste : jusqu'où un petit modèle spécialisé peut-il aller face à un géant, sur ton travail précis ? Allez, salut !

## Hors voix

Sources F1–F12. Aucune mesure personnelle nouvelle, aucune pièce à acheter et aucun plan de manipulation. L'anecdote est située en Russie ; ne pas illustrer un prix de 35 dollars par une fausse annonce française. Le calcul 4,5 tok/s est explicitement séparé du résultat déclaré >30. Prix non vérifiés : [PRIX À RELEVER], aucune recommandation de vendeur. La comparaison de profils reste valable sans annoncer un classement de tarifs.
