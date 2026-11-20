# 54 Go pour 35 dollars : à qui cette récupération peut-elle servir ?

Version finale après revue indépendante du 16 novembre 2026. Publication : 25 janvier 2027. Angle documentaire par profils, sans classement d’offres ni tarif reproductible. Base : 145 mots/minute, voix seule. V1 conservée.

Voix : **1 581 mots** (hors crochets), **10:54 à 145 mots/minute**. Liaisons strictes : **24**, soit **1,52/100 mots**. Question et disclaimer dans les **42 premiers mots**, soit environ **0:17**. Les repères ci-dessous sont calculés sur la voix, sans ajouter de pauses de montage.

| Partie | Début calculé |
|---|---|
| Résultat et question | 0:00 |
| Achat déclaré et limites | 0:40 |
| Experts et capacité | 2:02 |
| Calcul dense | 3:08 |
| Lot de P106 | 4:07 |
| Une carte P40 | 5:55 |
| Machine BC-250 | 6:58 |
| Budget et profils | 8:18 |

## Voix

[VISUEL : neuf rectangles de 6 Go ; « Achat déclaré : 3 000 RUB, environ 35 USD, Russie, octobre 2026 ». F1–F2. Résultat attribué au propriétaire, pas à la chaîne.]

Neuf cartes, 54 gigas et plus de 30 tokens par seconde annoncés, pour 35 dollars selon leur propriétaire en Russie. Donc, à quel profil ce genre de récupération peut-il convenir ?

On va regarder pourquoi son modèle convient à ce matériel, puis trois routes de récupération : les P106, la Tesla P40 et la BC-250. Et on va compter ce qui manque autour. Parce que le prix de neuf cartes trouvées dans un garage ne donne pas encore le prix d'une machine utilisable chez toi.

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

Si on remplaçait ce MoE par un dense de 70 milliards, les neuf capacités donneraient-elles neuf fois le débit ? Le chiffre de 4,5 tokens par seconde vient d'un calcul théorique dans un article. En fait, le propriétaire ne publie pas ce test-là.

Le calcul suppose un fichier de 42,5 gigas et environ 192 gigas par seconde de bande passante mémoire par carte. On répartit les tranches du modèle, puis un token traverse ces tranches successivement. Diviser 192 par 42,5 donne environ 4,5. On a encore ignoré les autres coûts.

Donc les neuf capacités s'additionnent, mais on ne multiplie pas simplement la vitesse d'une carte par neuf dans ce scénario. Et cette estimation ne décrit ni tous les moteurs ni les optimisations possibles. Elle sert à comprendre pourquoi « ça rentre » ne suffit pas à prédire « ça répond vite ».

[VISUEL : P106 schématique, six blocs mémoire ; caractéristiques Gigabyte, révision précisée. F4/F8.]

La récupération la plus proche de cette histoire serait un lot de P106. La référence Gigabyte documentée possède 6 gigas de GDDR5. À l'unité, cette capacité te limite vite ; en groupe, elle devient intéressante pour un modèle dont le moteur sait répartir les poids. Du coup, le lot complet et sa compatibilité comptent davantage que le prix d'une carte isolée.

Le nom exact mérite aussi ton attention. Une P106-090 et une P106-100 ne sont pas une seule référence. Même dans la famille P106-100, la fiche d'une révision ne prouve pas les caractéristiques de toutes les autres. Une annonce qui écrit seulement « équivalent GTX 1060 » laisse encore des questions ouvertes.

Par contre, le logiciel ajoute une limite que le nombre de gigas ne montre pas. Ces cartes appartiennent à une ancienne génération. NVIDIA a retiré de CUDA 13 la compilation destinée à plusieurs anciennes architectures. Les programmes déjà construits avec une version antérieure peuvent continuer avec le pilote compatible.

Donc ce matériel ne s'est pas arrêté de fonctionner le jour de CUDA 13. En revanche, la prochaine version du programme que tu veux utiliser peut demander un autre chemin. La documentation actuelle d'Ollama impose aussi des conditions de pilote pour les anciennes générations ; elle ne nomme pas toutes les cartes de minage.

Pour un premier PC destiné à travailler chaque jour, cette incertitude a un coût pratique. Si tu récupères déjà un rig fonctionnel et documenté, le pari change. Voilà pourquoi une affaire pertinente pour un passionné équipé peut devenir une dépense pénible pour quelqu'un qui doit tout assembler.

[VISUEL : P40, 24 Go, flux d'air dessiné ; « serveur / 250 W maximum constructeur ». F9.]

Si le nombre de cartes devient le problème, la Tesla P40 concentre 24 gigas sur une seule carte. On réduit donc le nombre de cartes nécessaires pour obtenir cette capacité. Elle figure aussi dans la documentation matérielle d'Ollama, sous les conditions de sa génération.

Sauf que son refroidissement a été conçu pour recevoir le flux d'air d'un serveur. Une carte passive ne crée pas elle-même ce flux. Le boîtier et la ventilation deviennent une partie du projet. Et son connecteur d'alimentation est décrit précisément dans le manuel : la forme seule ne permet pas de choisir un câble.

Du coup, le prix d'une P40 nue doit se comparer à une solution refroidie et alimentée correctement. Ce choix peut intéresser quelqu'un qui possède déjà un environnement compatible. Dans une petite tour silencieuse, la même carte demande d'autres compromis. Aucun résultat de la ferme à neuf P106 ne donne directement la vitesse de cette P40.

[VISUEL : BC-250 = carte complète CPU/GPU ; un seul réservoir de 16 Go, partagé avec le système. F10.]

Et si tu envisages une machine séparée, la BC-250 change encore le projet. Ici, on achète une carte complète avec processeur et circuit graphique, autour d'une mémoire partagée de 16 gigas. On ne l'ajoute donc pas au PC comme une carte graphique classique. Elle constitue la base d'une autre machine.

Des propriétaires documentent son usage avec Linux et Vulkan. Leurs configurations peuvent employer un BIOS communautaire et des réglages particuliers de mémoire. En fait, ces détails expliquent une partie du travail caché derrière les vidéos où tout semble déjà prêt.

Sauf que les 16 gigas servent au système, aux poids, au contexte et aux autres besoins. Deux tas de mémoire affichés par le pilote peuvent désigner la même mémoire physique. Il faut donc éviter de les additionner. Et une vidéo de jeu sur BC-250 ne valide pas automatiquement ton logiciel d'IA.

Cette route intéresse surtout quelqu'un qui accepte une machine communautaire, avec ses versions et sa documentation. Le prix de la carte seule laisse encore le stockage, l'alimentation, le refroidissement et les accessoires à compter. Par contre, elle peut avoir du sens quand tu veux construire une petite machine séparée pour apprendre.

[GRAPHIC] [VISUEL : budget d'exemple 100 € = environ 65 600 FCFA BCEAO ; « conversion, hors livraison et importation ». Budget d’exemple uniquement, aucune offre commerciale. F12.]

Pour le budget, prenons un exemple rond : 100 euros représentent environ 65 600 francs CFA en zone BCEAO. C'est une conversion de budget. Elle ne prouve pas qu'une carte affichée à 100 euros en France arrivera chez toi pour cette somme.

Donc le tableau utile ajoute les pièces manquantes, la livraison, les frais éventuels et la possibilité de retour. Un lot moins cher mais impossible à renvoyer peut exposer une plus grande part de ton budget. Et une machine complète disponible localement peut changer la comparaison avec une carte nue importée.

L'achat russe ne donne donc pas un tarif reproductible. Sans les éléments du système complet, le prix de la carte seule ne départage pas ces routes. Une annonce peut décrire une carte qui fonctionne pour le minage sans documenter le moteur d'IA que tu veux utiliser. Du coup, la compatibilité reste une partie du choix, même quand le vendeur connaît son matériel.

Reprenons les 54 gigas du début. Une partie de cette capacité sert au cache de conversation et aux tampons du moteur. Un fichier qui rentre avec un prompt court peut laisser moins de marge quand la conversation grandit. En fait, comparer la seule taille des poids oublierait encore une partie de la machine utilisable.

Le SSD manquant dans l'histoire rappelle la même chose à une autre étape : la réponse du modèle et le démarrage de la machine ne décrivent pas le même moment. Le propriétaire a réussi à démarrer sur USB. Cela ne prouve pas le temps de chargement ou le confort quotidien d'un autre lot récupéré. Donc le résultat annoncé reste utile, à condition de garder son périmètre.

Si cette vidéo t'a évité un mauvais achat, abonne-toi.

[CROCHET : ton avis personnel sur le temps que tu accepterais de consacrer à une machine d'occasion, facultatif.]

Si tu as déjà le rig et un modèle MoE adapté, récupérer ces cartes peut ouvrir des possibilités. Si tu veux surtout travailler sans gérer des versions anciennes, une carte plus récente et documentée mérite sa place dans la comparaison. Et si ton budget est très serré, le petit modèle qui tient dans ta machine actuelle reste une option à regarder avant l'achat.

Le 28 janvier, on regarde justement le choix du moteur : celui qui sait utiliser ta machine et ton fichier. Puis on revient aux petits modèles spécialisés le 1er février. Allez, salut !

## Hors voix

Sources F1–F12. Aucun prix TTC livré établi : limite conservée dans sources.md, sans tableau vide dans la voix ni promesse d’achat à 35 dollars. Budget BCEAO explicitement illustratif. Plus de 30 tok/s : témoignage incomplet du propriétaire ; 4,5 tok/s : estimation sous hypothèses, aucun essai dense. Aucun montage, achat, câblage ou flash demandé. Visuels publics crédités ou schémas originaux.
