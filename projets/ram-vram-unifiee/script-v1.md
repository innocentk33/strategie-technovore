# RAM, VRAM ou mémoire unifiée : laquelle aide vraiment ton IA ?

V1 documentaire · 31 décembre 2026 · cible 10–12 min à 145 mots/minute. Chiffres publics et calculs, sans nouveau test ni capture à produire. Sources datées du 16/11/2026.

| Partie | Repère |
|---|---|
| Un gros modèle avec une petite carte | 0:00 |
| Capacité et vitesse de circulation | 0:30 |
| Le calcul pour un modèle dense | 2:00 |
| Ce que change un MoE | 4:00 |
| La mémoire unifiée | 6:10 |
| Les trois achats possibles | 8:30 |

## Voix

[VISUEL : schéma « 16 Go de VRAM + 32 Go de RAM », puis mesure publique « 70,4 tok/s en chat court, 5070 Ti, 02/11 ». F6.]

Un utilisateur fait écrire un gros modèle local à environ 70 tokens par seconde, avec une carte de 16 gigas et 32 gigas de RAM. Donc la RAM peut servir à autre chose qu'attendre. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Mais pour ton prochain achat, faut-il plus de RAM, plus de VRAM, ou une mémoire unifiée ?

On va séparer ce qui fait tenir le modèle de ce qui le fait répondre vite. Tu vas voir le calcul de débit, pourquoi les modèles à experts changent l'addition, puis les achats utiles selon ton PC. Et on termine avec le cas où ajouter de la RAM peut laisser ta réponse presque aussi lente.

[GRAPHIC] [VISUEL : une grande réserve, un robinet ; capacité en Go et débit en Go/s. F1–F3.]

Si ton modèle tient déjà entièrement sur une bonne carte graphique, ajouter de la RAM ne transforme pas automatiquement son débit. Par contre, si la machine manque de mémoire pour charger le fichier ou garder la conversation, cette RAM supplémentaire peut rendre possible ce qui bloquait. Voilà les deux bénéfices à distinguer avant le panier.

La capacité, c'est la taille de la réserve. Le débit, c'est la quantité qui peut en sortir chaque seconde. Tu peux avoir un énorme réservoir avec une petite arrivée au moteur. Et dans une IA locale, il faut à la fois garder les bonnes données et les apporter assez vite au calcul.

Donc « j'ai 64 gigas » ne suffit pas à prévoir une vitesse. Il faut connaître leur type, leur organisation et la machine qui les utilise. Une seule barrette, une paire bien configurée et une mémoire partagée intégrée au processeur ne racontent pas le même trajet.

Prenons un exemple calculé avec de la DDR5 à 5 600 mégatransferts par seconde. Sur deux canaux de 64 bits, le débit théorique atteint 89,6 gigaoctets par seconde. C'est une estimation depuis les caractéristiques ; la machine n'utilisera pas forcément tout ce débit en permanence. Et augmenter seulement le nombre de gigas ne change pas cette formule.

En face, la fiche d'une RTX 5080 annonce 960 gigaoctets par seconde pour sa mémoire graphique. Le nombre est beaucoup plus élevé. Sauf que cette réserve fait 16 gigas : tu ne peux pas y installer n'importe quel modèle avec n'importe quelle conversation. La vitesse et la place doivent être utiles en même temps.

[VISUEL : livre dense dont toutes les pages sont parcourues, puis calcul « 89,6 ÷ 17 ». F4.]

Pour comprendre un modèle dense, imagine qu'on doive parcourir environ 17 gigaoctets de poids à chaque token. Avec notre débit théorique de RAM, la simple division donne environ 5 tokens par seconde. C'est un scénario simplifié, pas une mesure. On suppose une lecture complète, une conversation et aucun autre coût.

Le calcul sert à expliquer pourquoi davantage de capacité ne suffit pas toujours. Si les mêmes données doivent toujours traverser le même passage, une réserve plus grande ne les transporte pas plus vite. Du coup, ton modèle peut enfin se charger tout en continuant à écrire lentement.

Par contre, on ne va pas prédire chaque moteur avec cette division. Le calcul, le cache, la quantification et la manière de produire les tokens changent les coûts. Certains procédés vérifient plusieurs propositions ensemble. Plusieurs utilisateurs peuvent aussi partager une partie du travail. Donc la formule éclaire un cas précis, elle ne remplace pas les mesures.

Un rapport publié sur une carte de 12 gigas montre bien l'effet du placement. Un fichier qui déborde dans la RAM écrit autour de 13 tokens par seconde. Une copie plus compacte, entièrement sur le GPU, dépasse 42 dans ses essais. Mais le fichier et les réglages ont aussi changé : ce résultat ne permet pas d'accuser la RAM de tout l'écart.

Voilà pourquoi la question « combien de gigas ? » arrive avec une deuxième : « où sont les données utilisées pendant la réponse ? » Si une petite partie reste sur un chemin lent et qu'on doit l'attendre à chaque token, elle peut peser lourd dans le résultat.

[GRAPHIC] [VISUEL : grand classeur d'experts ; quelques dossiers seulement s'allument par token. F7/F9.]

Avec un modèle à mélange d'experts, une partie seulement des poids est activée pour chaque token. Tous les experts doivent rester accessibles, mais chaque étape ne demande pas le travail de tout le monde. C'est ce qui permet d'envisager une grande réserve en RAM à côté d'une carte plus petite.

Imagine une équipe de spécialistes. Pour une question donnée, on appelle seulement ceux dont on a besoin. Les autres restent disponibles pour la suite. Donc le nombre total de paramètres peut être grand sans que chaque token réclame le calcul de tous ces paramètres.

Il reste pourtant deux contraintes. Il faut garder les experts quelque part, et apporter les bons au bon moment. Si le routage change beaucoup, si les experts utiles ne sont pas en mémoire rapide ou si le moteur les déplace mal, le trajet peut encore te faire attendre. Le mot MoE ne supprime aucun de ces coûts.

Strata, par exemple, garde certains éléments et des experts sur la carte, les autres experts dans la RAM, et une table particulière sur le SSD. Le processeur peut calculer les experts hors GPU pendant que la carte traite sa partie. Du coup, le logiciel organise une coopération entre plusieurs ressources qui ont chacune leurs limites.

C'est le contexte du résultat du début : un utilisateur sur une 5070 Ti de 16 gigas et environ 32 gigas de RAM publie 70,4 tokens par seconde en chat court. Sa réflexion est coupée. C'est une médiane de plusieurs essais, et il précise ne pas avoir vérifié la justesse. Donc cette mesure prouve une vitesse dans ce scénario, sans promettre la même qualité sur ton travail.

On ne la compare pas directement au dense précédent pour déclarer la RAM victorieuse. On a changé de modèle et de moteur. Ce qu'elle montre, c'est qu'un gros fichier réparti intelligemment peut devenir utilisable avec une carte de joueur. La RAM sert alors à faire tenir l'ensemble, tout en participant au calcul.

[VISUEL : CPU et GPU autour d'une même réserve ; une partie est réservée au système. F3.]

La mémoire unifiée change encore l'organisation. Sur les machines concernées, le processeur et le GPU accèdent à une réserve commune. Tu n'as plus la même séparation physique entre des barrettes d'un côté et la mémoire d'une carte dédiée de l'autre.

Du coup, un gros modèle peut profiter d'une capacité qui serait coûteuse à obtenir sur une seule carte graphique. Mais le système, les applications et le modèle partagent cette réserve. Une machine annoncée avec 64 gigas ne promet pas 64 gigas entièrement libres pour ton IA.

Et unifiée ne signifie pas une vitesse unique. Apple annonce par exemple 307 gigaoctets par seconde sur le Mac mini M5 Pro. Certaines configurations M6 du même Mac mini annoncent un autre débit. Donc le nom de la mémoire ne dispense pas de lire la fiche de la puce précise.

Compare aussi la capacité réellement accessible au moteur. Le système peut garder une marge, et les outils n'utilisent pas tous la mémoire de la même manière. Ce qui compte pour toi, c'est le fichier, son contexte et le logiciel qui vont ensemble sur cette configuration.

En fait, la mémoire unifiée peut répondre à un besoin de grosse capacité dans une machine compacte. Une carte dédiée peut rester très intéressante pour sa bande passante et les logiciels qui l'exploitent. Ce sont des compromis à relier à ton usage, avec une mesure sur le modèle choisi.

[VISUEL : stockage, RAM et VRAM ; une flèche de disque apparaît uniquement pour les éléments concernés. F7/F8.]

Le SSD mérite aussi sa place dans le schéma. Il peut servir au chargement initial, à des données gardées sur disque ou à un débordement quand la mémoire manque. Ces situations n'ont pas le même coût. Donc voir une activité disque pendant la génération ne prouve pas que tout le modèle manque de RAM.

Dans un moteur qui lit une table particulière sur le SSD, une partie du trafic est prévue. Dans un autre cas, le système doit récupérer constamment des pages qu'il n'arrive plus à garder en mémoire. Le symptôme visible se ressemble ; l'explication peut changer. Et l'achat utile peut changer avec elle.

C'est pour ça qu'un conseil comme « ajoute 32 gigas et tout ira deux fois plus vite » est trop court. Si le disque intervenait faute de place, davantage de RAM peut aider beaucoup. Si les poids étaient déjà en RAM et que son débit limitait la réponse, tu n'as pas forcément élargi le passage.

[GRAPHIC] [VISUEL : trois profils, sans tarif inventé.]

Alors, pour choisir, pars du matériel que tu as. Avec une bonne carte dont le modèle tient déjà en VRAM, regarde d'abord le moteur, le contexte et les réglages documentés. Ajouter de la RAM peut donner du confort aux autres applications ; le gain de génération n'est pas acquis.

Avec une carte plus petite et un modèle à experts, la RAM peut devenir la réserve qui manque. Vérifie la capacité recommandée pour le fichier, la marge du système et le moteur capable de l'exploiter. La carte, le processeur et les échanges continuent de compter.

Si tu pars de zéro et que tu veux de grands modèles dans un ordinateur compact, regarde les configurations à mémoire unifiée. Compare le coût complet, la capacité utile et les vitesses publiées sur ton modèle. La quantité de mémoire seule ne départage pas deux machines.

Si ce choix t'a évité d'acheter la mauvaise mémoire, abonne-toi.

[CROCHET : ton avis sur le compromis entre vitesse, capacité et simplicité. Facultatif.]

La vidéo sur les modèles par taille de carte reprend ce calcul par paliers concrets. Pour aujourd'hui, garde ces trois lignes avant d'acheter : la place du fichier, la place de la conversation et le trajet des données pendant la réponse. C'est là que tes gigas deviennent utiles. Allez, salut !

## Hors voix

Visuels documentaires uniquement. Les mesures déjà filmées de Strata ne sont pas requises pour tenir cette version ; ne pas demander à l'auteur d'en refaire. Risques : afficher « calcul théorique » pendant la division ; conserver modèle/moteur avec70,4 ; présenter les profils avant toute comparaison de prix. Aucun classement CPU/GPU/Mac à partir de fichiers différents.
