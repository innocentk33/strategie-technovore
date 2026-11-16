# Grill indépendant — Un jeu local sur 16 Go

Revue du 16/11/2026 de la V1, sources F1–F12 et archive Strata T41/T45. Méthode `youtube-script-grill`, onze axes et variante storytelling. Pas de nouveau test ni de production d'asset requis.

## Verdict : 7,0/10

L'opposition entre **8 min 12, une demande**, et **34 min 58, trois relances**, apporte de la preuve et du relief. Le mini-Minecraft qui prétend écrire sans outil est un vrai retournement. Ensuite, le récit devient un catalogue SDXL/TripoSR/MusicGen/Godot. Le budget de 16 Go est documenté de façon inégale : **SDXL n'a pas de seuil établi dans le dossier**, et l'ensemble du workflow n'a pas été testé. La V1 le reconnaît localement mais promet encore trop largement des « tâches réalisables ». Moyenne des axes : 77/110 = 7,0 ; S non recomptés.

## Test des trente secondes

| Tranche | Citation | Verdict |
|---|---|---|
| 0–5 s | « Un casse-briques avec des vies, des bonus… » | Résultat concret dès le départ. |
| 5–15 s | « … codé… carte de 16 gigas. Les images viennent des archives Strata. » | Bonne attribution si rush affiché ; changer la voix si le montage utilise un schéma. |
| 15–30 s | « Pour les autres outils… jusqu'où… publier ? » | Limite des preuves et question claire ; titre commercial augmente l'exigence des licences. |
| Pont | « … la licence qui peut arrêter ton projet commercial… » | Boucle réelle, récoltée avec MusicGen ; la formuler comme condition du workflow, pas comme interdiction automatique de toute sortie. |

Ouverture environ **64 mots, 26,5 s**. Six contrôles : sujet/tension oui ; meilleur moment oui ; question unique oui ; seconde boucle oui ; phrases utiles oui sous réserve des images disponibles ; trente secondes oui. Le chiffre de 8:12 pourrait apparaître au visuel dès ce hook sans ajouter de phrase.

## Tableau de bord

| Axe | /10 | État | Diagnostic |
|---|---:|---|---|
| 1. Promesse | 7 | 🟠 | Prototype démontré ; chaîne complète d'assets sur 16 Go non validée. |
| 2. Alignement | 8 | 🟢 | Explique ce qu'un joueur peut raisonnablement viser, sans vendre un outil. |
| 3. Problème profond | 8 | 🟢 | Confondre fichier généré, jeu qui se lance et jeu prêt à publier. |
| 4. Public/complexité | 7 | 🟠 | Cas visuels parlants ; références de licences et pipeline s'accumulent. |
| 5. Valeur/originalité | 8 | 🟢 | Archives propres, faux appel d'écriture et licences distinctes apportent une valeur réelle. |
| 6. Structure/transformation | 7 | 🟠 | Prototype → assets → publication ; fin glisse vers guide de démarrage. |
| 7. Histoire | 7 | 🟠 | Les deux jeux portent le début puis disparaissent au profit des outils. |
| 8. Mais/donc | 7 | 🟠 | Chaque asset ajoute une contrainte ; transitions souvent rubriques successives. |
| 9. Engagement actif | 6 | 🟠 | Imagine le sprite cohérent ; peu de choix actif face aux licences. |
| 10. Oralité/liaisons | 5 | 🟠 | 17/1 555 = 1,09 liaison stricte/100 mots ; avec six « mais », 1,48. |
| 11. Tics d'IA | 7 | 🟠 | Réserves utiles mais métadiscours « pas un benchmark… » et morale d'atelier finale. |
| S1. Trente secondes | 8 | 🟢 | Résultat et question à temps ; variante sans rush nécessaire. |
| S2. Pont | 8 | 🟢 | Une licence peut rendre inadéquat l'outil qui tient en mémoire. |
| S3. Retournements | 6 | 🟠 | Bonne bascule casse-briques/Minecraft, puis longues descriptions >45–60 s. |
| S4. Planté/récolté | 7 | 🟠 | Licence récoltée ; le jeu initial devrait revenir pour relier les assets. |
| S5. Personnages/enjeu | 8 | 🟢 | Deux projets réels et un joueur ; pas de défi personnel fabriqué. |
| S6. Fin | 5 | 🟠 | Résumé et conseil de pratique, sans CTA ni vidéo suivante. |

## Le grill et quatre réécritures ciblées

### 1. La preuve de code doit conserver son matériel et son modèle

> « une carte de joueur peut déjà participer à la fabrication d'un petit jeu »

Juste mais imprécis pour un titre centré sur la mémoire. Les archives T41/T45 concernent **Coder IQ1_M, Pi 1.5.2, réflexion high, contexte 131 072 et machine dotée d'environ 32 Go de RAM en plus des 16 Go de VRAM**. Le chiffre public de T7 ne doit pas servir de preuve de ce casse-briques. Ajouter ces éléments au visuel, sans réciter le protocole entier.

**Réécriture 1 :**

> Dans ces archives, le Coder de Strata écrit le casse-briques en 8 minutes et 12 secondes, après une seule demande. La machine a aussi 32 gigas de RAM. On voit les vies, les bonus et la fin de partie : c'est une boucle jouable documentée, avec cette configuration.

Si rush absent : remplacer au hook « Les images viennent des archives » par « Ce résultat est documenté dans les archives Strata », et légender le schéma « reconstitution du fonctionnement ». Ne pas attribuer à une image officielle la création de l'auteur.

### 2. Des outils étudiés séparément ne valident pas une chaîne complète

> « on compare une succession de tâches réalisables, avec leur budget »

F4 n'établit pas de minimum SDXL ; F7 donne une exigence annoncée TripoSR ; F8 recommande 16 Go pour MusicGen moyen. Cela soutient une sélection de pistes, pas une démonstration complète sur la carte du titre.

**Réécriture 2 :**

> Ces outils peuvent être étudiés séparément : le code, puis les images, la 3D et le son. Pour chacun, on va distinguer la mémoire annoncée de ce qui a réellement été montré. Le casse-briques est notre résultat de code ; les autres étapes restent des pistes documentées, avec leurs contraintes.

Garder les 6 Go annoncés de TripoSR et les 16 Go recommandés de MusicGen. Pour SDXL, dire directement que le dossier ne permet pas de certifier un seuil commun à tous les pipelines. Aucune mesure à faire exécuter pour combler ce manque.

### 3. Faire du jeu le fil du catalogue d'assets

> « Pour les images… Pour un petit objet 3D… Pour la musique… »

La succession est claire mais interchangeable. Le casse-briques peut porter l'histoire : changer la balle en personnage, ajouter un objet, puis du son. Ce sont des illustrations de besoin, jamais des assets prétendument produits.

**Réécriture 3 :**

> Si on veut donner un personnage à ce prototype, une belle image ne suffit plus. Il faut retrouver le même casque et les mêmes proportions d'une pose à l'autre. C'est là que la génération d'images devient un travail d'animation cohérente, avec des retouches à prévoir.

Même raccord ensuite pour un accessoire 3D, puis un bruit de saut. Une question active avant MusicGen : « L'outil tient sur la carte ; est-ce qu'on peut maintenant l'utiliser pour le jeu qu'on veut vendre ? » La licence apporte alors un changement réel de décision.

### 4. Sortir du mini-tutoriel final

> « Ensuite, tu peux demander une correction… Tu peux garder une version… »
> « Ce sont des limites de projet proposées, pas un benchmark… »

Le spectateur reçoit des consignes au lieu d'une conclusion tirée des preuves. Les principes restent utiles, mais peuvent être racontés à travers le mini-Minecraft déjà observé.

**Réécriture 4 :**

> Le mini-Minecraft montre ce qui reste à faire après la première réponse : obtenir le fichier, corriger les erreurs et vérifier les actions du joueur. Le casse-briques atteint plus vite une boucle plus petite. Donc le périmètre du jeu compte autant que la vitesse d'écriture du modèle.

Conclure sur cette différence, CTA bref après une valeur déjà livrée, puis renvoi au **18 janvier, modèles par VRAM**, sans demander au spectateur de réaliser un essai.

## Contrôles factuels et rythme

- **1 555 mots, 10:43** à 145 mots/min hors balises et crochet. Liaisons : donc 10, du coup 4, sauf que 1, par contre 2. Ajouter des conséquences entre chapitres, pas du remplissage.
- 8:12 et 34:58 proviennent des sessions T41 ; le second comprend les relances, pas seulement 23:08 de travail du modèle. La V1 n'assimile pas ces deux chronomètres.
- T45 décrit ce qui est visible ; absence de console F12 ou version mobile filmées. Ne pas étendre « jouable » à absence de bugs ou qualité commerciale.
- F4/F6 : fonctionnement SDXL non chiffré dans le dossier ; offload CPU réduit la VRAM avec un compromis, pas une preuve universelle sur 16 Go.
- F7 : 6 Go est une annonce du projet. Bon retrait du temps A100. MIT code/poids ne résout pas les droits de l'image d'entrée.
- F9 : code MIT, poids non commerciaux. Conserver la distinction et éviter d'énoncer une règle universelle sur la propriété de toutes les sorties. Le script examine la permission d'utiliser les poids dans un workflow commercial.
- F11 : kit Kenney précisément identifié, assets CC0 ; pas toute bibliothèque internet supposée libre. F10 : licence du moteur distincte des assets.
- Le paragraphe « on n'importe pas le chronomètre d'une A100 dans une miniature » parle du travail éditorial. Remplacer par « le temps annoncé sur A100 ne prédit pas celui de ta carte ».
- Les vrais tournants : jeu simple réussi → projet plus complexe relancé ; code → cohérence visuelle ; maillage → intégration ; mémoire suffisante → conditions de licence. Les réserves techniques consécutives ne sont pas autant de tournants.
- CTA absent dans la V1. Fin « Allez, salut ! » présente. Aucune nouvelle capture ou génération nécessaire.

## À garder

> « … avoir écrit et vérifié le fichier sans avoir appelé l'outil d'écriture. »

Un échec réel qui explique la différence entre affirmation et résultat.

> « Si le casque, le visage et les proportions changent… ton animation saute. »

Conséquence concrète, compréhensible par un joueur.

> « Le code… MIT… les poids… non commerciale. »

Un pivot de décision utile, à conserver dans son périmètre exact.

## Plan d'action

1. Compléter l'identité de l'archive code et prévoir la variante de voix sans rush.
2. Limiter la promesse du workflow sur 16 Go aux preuves disponibles ; conserver les inconnues SDXL.
3. Faire revenir le prototype entre les outils, ajouter la question active sur la licence.
4. Remplacer la fin procédurale par ce que montrent les deux jeux ; couper les commentaires de fabrication du script.
5. Ajouter CTA et renvoi au 18 janvier, puis recompter durée/liaisons/timecodes.


## Corrections appliquées après cet audit — 16 novembre 2026

- Archive identifiée : Coder IQ1_M, Pi 1.5.2, paramètres et RAM ; T7 n'est pas une preuve de ce jeu.
- Voix valable sans rush : résultat d'archive, reconstitution légendée si nécessaire.
- Chaîne complète sur 16 Go non revendiquée ; SDXL sans minimum certifié, exigences annoncées TripoSR/MusicGen conservées.
- Prototype gardé comme fil des assets ; question active sur l'usage commercial des poids, sans règle inventée sur toutes les sorties.
- Fin procédurale remplacée par les résultats des deux jeux, CTA ajouté et renvoi au 18 janvier.

Livrables : `script.md` et `teleprompteur.txt`, V1 conservée. Voix seule hors crochets : **1560 mots**, **10:46** à 145 mots/minute ; **27 liaisons strictes**, **1.73/100 mots**. Hook incluant question et disclaimer : **49 mots**, environ **0:20**. Timecodes recalculés sur les débuts réels des parties. Prompteur : nombres en chiffres, une ligne par souffle, lignes vides entre paragraphes, balises non dites. Ces métriques décrivent la correction ; elles ne modifient pas la note de l’audit indépendant.
