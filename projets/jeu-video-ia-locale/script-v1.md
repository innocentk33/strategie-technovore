# Créer un petit jeu avec une IA locale sur 16 Go : jusqu'où ça va ?

V1 documentaire · 14 janvier 2027 · cible 10–12 min à 145 mots/minute. Réutilisation facultative des archives Strata déjà documentées ; aucune nouvelle génération ni capture demandée. Recherche publique du 16/11/2026.

| Partie | Repère |
|---|---|
| Le résultat jouable et sa limite | 0:00 |
| Ce que le code a vraiment produit | 0:30 |
| Sprites et textures | 2:30 |
| Les objets 3D | 4:30 |
| Sons, musique et licences | 6:10 |
| Un projet réaliste pour commencer | 8:10 |

## Voix

[VISUEL : archive T45 du casse-briques, ou schéma des vies/bonus si rush absent ; bandeau « archive Strata, novembre 2026 ».]

Un casse-briques avec des vies, des bonus et un game over, codé avec une IA locale sur une carte de 16 gigas. Les images viennent des archives Strata. Pour les autres outils, ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc, avec ta carte de joueur, jusqu'où tu peux aller entre ce prototype et un jeu que tu voudrais publier ?

On regarde ce que le code a réellement réussi, puis les images, les objets 3D et le son. Tu vas aussi voir ce qui peut tenir par étapes, ce qui réclame des retouches, et la licence qui peut arrêter ton projet commercial avant même le premier euro gagné.

[GRAPHIC] [VISUEL : chronologie des archives,8min12casse-briques ;34min58mini-Minecraft ;F1/F2.]

Le casse-briques documenté dans les archives a été produit en 8 minutes et 12 secondes, avec une seule demande. On voit la balle, les vies, les bonus et la fin de partie. Donc une carte de joueur peut déjà participer à la fabrication d'un petit jeu avec une boucle compréhensible.

Mais l'autre exemple raconte une histoire différente. Le mini-Minecraft a demandé près de 35 minutes et plusieurs relances. Au premier message, le modèle affirme même avoir écrit et vérifié le fichier sans avoir appelé l'outil d'écriture. Du coup, une réponse assurée ne prouve pas que le jeu existe sur le disque.

C'est un bon point de départ pour fixer ton objectif. Une balle qui rebondit, des blocs que tu places et un menu qui répond, ça donne une preuve concrète. Une promesse de monde ouvert avec inventaire, combat, sauvegarde et multijoueur réclame beaucoup plus de liens entre les systèmes.

Donc le premier projet gagne à tenir autour d'une action claire. Attraper, éviter, sauter, casser. Tu peux observer ce que le joueur fait et ce que le jeu lui renvoie. Si cette boucle n'est pas agréable avec des formes simples, de belles textures ne la rendent pas automatiquement meilleure.

La vitesse en tokens par seconde aide à attendre moins longtemps pendant le code. Elle ne mesure pas les collisions, la difficulté ou le plaisir de jouer. Un modèle rapide peut écrire un fichier qui se lance et contient encore des erreurs. Le résultat utile se juge aussi à ce qui fonctionne après la génération.

[VISUEL : carte«code»,puis cartes«images»,«3D»,«audio» ;la jauge mémoire se vide entre les étapes. F12.]

Et les 16 gigas du titre ne veulent pas dire que tous les outils restent chargés en même temps. Tu peux produire le code, libérer le modèle, puis travailler sur les images. Ensuite seulement, passer à un autre outil. Du coup, on compare une succession de tâches réalisables, avec leur budget, plutôt qu'une équipe entière installée à demeure sur la carte.

Cette séparation compte aussi pour le temps. Si tu dois changer d'outil à chaque petite correction, le workflow peut devenir moins confortable. Mais elle évite d'additionner artificiellement des besoins mémoire qui ne sont pas forcément simultanés.

[VISUEL : page officielle SDXL et planche dessinée«concept»,«sprite»,«animation». F4–F6.]

Pour les images, un modèle comme SDXL peut générer des concepts, des textures ou des éléments visuels à partir d'un texte. Sa version de base peut fonctionner seule. Par contre, une image réussie ne fournit pas automatiquement une série d'animations cohérentes.

Imagine un personnage vu de côté. Tu demandes ensuite la même pose avec le bras un peu plus haut. Si le casque, le visage et les proportions changent, tu as deux illustrations, mais ton animation saute. Donc il faut encore contrôler les silhouettes, les couleurs, les alignements et la transparence.

Le pixel art ajoute une autre contrainte. Une image qui ressemble à des pixels n'a pas forcément une grille propre ni une palette cohérente. Pour un petit jeu, quelques sprites retouchés peuvent être plus utiles qu'une centaine d'images presque compatibles. Et cette retouche peut rester une vraie partie du travail.

Côté mémoire, le modèle, la résolution et le pipeline comptent. La documentation Diffusers propose notamment de déplacer certains composants vers la RAM pour réduire la place sur la carte, avec un coût de performance. Donc on ne peut pas donner un seul minimum valable pour toutes les configurations d'images à partir du nom SDXL.

Sa licence autorise des usages sous conditions et ne se résume pas à un usage personnel uniquement. Mais elle ne garantit pas les droits de tous les contenus qui pourraient apparaître. Le plus simple pour ton projet reste de garder la provenance et la licence de chaque élément utilisé.

[GRAPHIC] [VISUEL : image d'un accessoire→maillage ;collision simplifiée dessinéeàcôté. F7/F12.]

Pour un petit objet 3D, TripoSR reconstruit une forme depuis une image. Le projet annonce environ 6 gigas de VRAM dans ses réglages par défaut, pour une image. C'est un besoin annoncé par les auteurs, pas une mesure sur toutes les cartes de 16 gigas.

Donc un accessoire simple peut devenir une piste intéressante. Par contre, la forme obtenue doit encore correspondre au jeu. Son échelle, ses matériaux et sa collision demandent un contrôle. Pour un personnage animé, il faut également penser à la déformation et au squelette ; reconstruire sa silhouette ne fournit pas automatiquement ces éléments.

Une caisse qui paraît correcte de face peut cacher un dos approximatif. Un objet très détaillé peut avoir une géométrie peu adaptée à ton nombre d'ennemis à l'écran. Du coup, le travail continue entre le fichier généré et l'asset intégré dans le moteur.

Le code et les poids de TripoSR sont annoncés sous licence MIT. C'est une information utile si tu compares les outils. Mais la licence du logiciel ne te donne pas les droits sur une image d'entrée prise à quelqu'un d'autre. Il faut regarder les deux côtés du trajet.

Et le temps de génération communiqué sur une grosse carte de datacentre ne devient pas celui de ton PC. Pour choisir un outil, on garde la capacité publiée et ses limites. On n'importe pas le chronomètre d'une A100 dans une miniature avec une carte de joueur.

[VISUEL : courbeaudio dessinée,étiquettes«modèle»,«code»,«poids». F8/F9.]

Pour la musique, MusicGen est une piste locale connue. Sa documentation recommande 16 gigas pour les modèles de taille moyenne. Un petit modèle ou une séquence plus courte peut demander moins. Donc, là encore, la référence exacte et la durée changent le travail que tu demandes à la machine.

Sauf que la licence peut décider avant la mémoire. Le code d'AudioCraft est sous MIT, tandis que les poids publiés sont sous une licence non commerciale. Tu ne peux donc pas conclure « le dépôt est MIT, tout mon workflow commercial est autorisé ». Il faut lire les conditions des poids que tu utilises.

Pour une première version destinée à être vendue, tu peux aussi choisir des sons existants avec une licence adaptée. Le kit de plateforme de Kenney, par exemple, documente des sprites, des modèles et des effets sonores sous CC0. Ce sont des assets préparés, avec une provenance connue, qui évitent de transformer chaque bruit de saut en projet de recherche.

Du coup, tu n'es pas obligé de tout générer pour créer avec une IA locale. Le modèle peut aider au code, les assets peuvent venir d'une bibliothèque, et toi tu relies les éléments. Cette combinaison peut même te rapprocher plus vite d'un jeu cohérent.

[GRAPHIC] [VISUEL : schéma du petitprojet ;nomsdefichiers fictifslégendés«exemple». F10–F12.]

Le moteur rassemble le résultat. Godot permet de créer des jeux commerciaux sous sa licence MIT, en conservant les mentions nécessaires. Mais les images, les musiques, les polices et les extensions ajoutées ont leurs propres conditions. Donc la licence du moteur ne remplace pas celle des éléments que tu importes.

Pour le code, garde aussi une cible précise. Le moteur choisi, sa version et les fonctionnalités attendues doivent être clairs. Sinon, le modèle peut proposer une fonction ancienne ou une structure qui ne correspond pas à ton projet. Plus tu relies de systèmes différents, plus leurs interfaces deviennent une partie du problème.

Un premier objectif concret pourrait être un écran, une action, une condition de victoire et une condition de défaite. Ce sont des limites de projet proposées, pas un benchmark qui garantirait le succès. Elles te permettent surtout de voir si la boucle tient avant de multiplier les fonctionnalités.

Ensuite, tu peux demander une correction avec un symptôme précis. « La balle traverse cette paroi » apporte davantage d'information que « le jeu ne marche pas ». Tu peux garder une version qui fonctionne avant le changement suivant. L'IA accélère une partie de l'écriture ; conserver un projet compréhensible reste utile à chaque étape.

Et quand le jeu semble fini, il reste des questions très visibles pour un joueur. Les contrôles se comprennent-ils ? Peut-on relancer après avoir perdu ? Le score se comporte-t-il correctement ? L'image reste-t-elle lisible quand plusieurs éléments bougent ? Une page qui s'ouvre ne répond pas à toutes ces questions.

[VISUEL : troisprofils«prototype»,«petitjeu2D»,«projet3Dambitieux».]

Donc, avec 16 gigas, tu peux viser un prototype de code local documenté, puis choisir tes outils d'assets par étapes. Pour un petit jeu en 2D, des formes simples et une bibliothèque à licence claire peuvent suffire à avancer. Pour une production 3D ambitieuse, la géométrie, l'animation et l'intégration demandent davantage de travail que la génération d'une première image.

Si tu veux commercialiser, ajoute les licences au même tableau que la VRAM. Si tu veux apprendre, choisis un jeu assez petit pour comprendre les changements du modèle. Et si tu veux seulement montrer une idée jouable, les archives du casse-briques donnent déjà un exemple concret de ce premier palier.

[CROCHET : ton avis de joueur sur le type de petit projet que tu aurais envie de pousser. Facultatif.]

La carte te donne une partie de l'atelier. Le jeu prend forme quand le code, les assets et les règles fonctionnent ensemble. Commence par une boucle qui donne envie de rejouer ; tu auras une bonne raison d'ajouter le reste. Allez, salut !

## Hors voix

Le montage réutilise seulement les archives documentées T45 si disponibles ; sinon schémas. Démonstrations officielles d'outils toujours légendées comme telles. Aucun faux jeu, asset ou rendu attribué à l'auteur. Risques : ne pas laisser croire au workflow simultané ; garder « besoin annoncé » avec 6 Go ; poids MusicGen non commerciaux distincts du code MIT. Aucun nouveau tournage obligatoire.
