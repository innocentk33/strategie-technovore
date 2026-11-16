# Grill indépendant — Avant la deuxième carte

Revue du **16/11/2026**, [`script-v1.md`](script-v1.md), [`sources.md`](sources.md) F1–F10 et calendrier fourni. Méthode [`youtube-script-grill`](../../ressources/skills-gpt/youtube-script-grill.md), mode B, variante storytelling complète. Le sujet est une décision d'achat documentée ; aucun benchmark ni montage matériel de l'auteur n'est requis.

## Verdict : 7,1/10

Le hook **36 → 34 → 47** pose une vraie anomalie. Le corps explique surtout une nuance précieuse : une seconde carte peut accélérer même en répartition par couches **si elle supprime un débordement en RAM**. Les deux situations ne sont pas confondues, et les vitesses restent attribuées.

La faiblesse vient du milieu : ports, boîtier, alimentation, marques et trois logiciels forment un long inventaire. Il faut faire revenir la décision du départ à chaque obstacle et raccourcir les réserves répétées. L'oralité est correcte mais le rythme manque de liaisons variées. La fin doit ouvrir la vidéo suivante.

Moyenne des onze axes : **78/110**, soit 7,1/10. Les S détaillent le récit sans double comptage.

## Test des trente secondes

| Tranche | Citation | Verdict |
|---|---|---|
| 0–5 s | « Une carte écrit à 36 tokens par seconde. Le même testeur en ajoute une deuxième… » | 🟢 Sujet et expérience clairement attribués. |
| 5–15 s | « … il tombe à 34. Puis il change la répartition, et monte à 47. » | 🟢 Contraste et meilleure valeur livrés avant quinze secondes ; le visuel donne protocole/date. |
| 15–30 s | « Ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc… qu'est-ce qui décide si elle t'aide vraiment ? » | 🟢 Transparence et question unique à temps. |
| Pont | « Le piège, c'est qu'un deuxième port long peut cacher une liaison beaucoup plus étroite. » | 🟢 Seconde boucle concrète, récoltée par le manuel de carte mère. |

L'ouverture compte environ **55 mots**, soit **23 secondes** à 145 mots/min ; le plan prend ensuite un peu plus de vingt secondes. Les six critères passent : sujet/tension, meilleur moment, question unique avant trente secondes, deuxième boucle, utilité des phrases et budget. **Pas de réécriture du hook nécessaire.** Conserver « écrit » pour la génération, et les arrondis 36/34/47 comme ceux de F1.

## Tableau de bord

| Axe | /10 | État | Diagnostic |
|---|---:|---|---|
| 1. Promesse | 8 | 🟢 | Les points avant achat sont présents, et le paradoxe initial expliqué. |
| 2. Alignement | 9 | 🟢 | « Ajouter, remplacer, ou garder ton argent » sert le besoin ; pas de vente forcée. |
| 3. Problème profond | 8 | 🟢 | Payer une deuxième carte qui n'aide pas est une peur concrète, résolue par la situation de départ. |
| 4. Public/complexité | 7 | 🟠 | Métaphores utiles ; couche/tensor, lignes, moteurs et cache s'accumulent. |
| 5. Valeur/originalité | 8 | 🟢 | F3 évite le slogan faux « deux cartes n'accélèrent jamais » ; version logicielle et contraintes matérielles bien distinguées. |
| 6. Structure/transformation | 7 | 🟠 | Départ achat incertain → quatre critères ; inventaire central trop long. |
| 7. Histoire | 7 | 🟠 | L'anomalie des deux cartes est un fil ; le récit s'efface pendant les chapitres logiciels. |
| 8. Mais / donc | 7 | 🟠 | Bons raccords RAM/VRAM et couches/tensor, mais liste de matériels et logiciels. |
| 9. Engagement actif | 6 | 🟠 | Question initiale et classification des besoins ; peu d'anticipation explicite au milieu. |
| 10. Oralité/liaisons | 5 | 🟠 | **17/1 576 = 1,08 liaison stricte/100 mots** ; « donc » porte presque tout. |
| 11. Tics d'IA | 6 | 🟠 | « Le bon benchmark… », « la vraie addition », « personne ne gagne… » donnent plusieurs petites sentences. |
| S1. Trente secondes | 9 | 🟢 | Six contrôles réussis, chiffre immédiatement utile. |
| S2. Pont | 8 | 🟢 | Le port long/liaison étroite crée une deuxième attente. |
| S3. Retournements | 6 | 🟠 | Plusieurs séquences d'exposé dépassent 45–60 s sans changement de diagnostic. |
| S4. Planté/récolté | 8 | 🟢 | 36/34/47 expliqué, port long révélé, mémoire supplémentaire distinguée de vitesse. |
| S5. Personnages/enjeu | 7 | 🟠 | Deux testeurs et acheteur identifiable ; pas de biographie ou incident inventé. |
| S6. Fin | 6 | 🟠 | Verdict clair, mais surtout checklist ; renvoi au Mac/PC du 10 décembre absent. |

## Le grill

### 1. La nuance la plus utile mérite d'être sourcée directement et mise au premier plan

> « Sur le même Qwen en 4 bits, le testeur passe d'environ 11 à 12 tokens par seconde à environ 21, en répartition par couches. Le modèle débordait auparavant en RAM. »

**Pourquoi ça coince :** le contenu est bon ; le visuel qui précède renvoie à F4/F6, alors que cette mesure est **F3**. La distinction entre gain de capacité et coopération des cartes est le cœur de la vidéo ; elle mérite un raccord plus vivant au premier graphique.

**Réécriture ciblée 1 :**

> Le résultat de 34 tokens ne condamne donc pas la deuxième carte. Dans un autre rapport, le fichier débordait en RAM : son auteur passe d'environ 11 à 12 tokens par seconde à environ 21 quand deux cartes le gardent en mémoire graphique. Même mode par couches, autre problème de départ. [F3]

Cette réécriture n'assimile pas les deux machines : « autre rapport » et la condition de débordement sont indispensables.

### 2. L'explication des modes ne prouve pas séparément la cause de chaque gain

> « C'est ce qui explique notre premier graphique. »

**Pourquoi ça coince :** F1 compare bien les répartitions sur le même matériel. En revanche, le rapport ne mesure pas isolément la part du lien PCIe, du calcul parallèle ou des autres paramètres dans chaque écart. La transition peut attribuer le résultat au changement de mode observé sans prétendre avoir isolé tout le mécanisme.

**Réécriture ciblée 2 :**

> Le premier graphique compare justement ces deux modes sur la même paire de Radeon : environ 34 en couches, 47 en tensor. Le rapport précise aussi les ports PCIe 4 à huit lignes chacun. Ce résultat montre l'effet de cette configuration ; il ne donne pas une règle pour toutes les liaisons.

Garder F1, le modèle et la génération visibles. Ne pas transformer le gain observé sur une machine en facteur universel, ni en recette de commande actuelle.

### 3. Le chapitre des moteurs répète cinq fois que les conditions comptent

> « Deux marques différentes peuvent participer à certains montages… »
> « Dans Ollama… »
> « LM Studio propose aussi… »
> « La documentation actuelle de llama.cpp ajoute une réserve utile… »

**Pourquoi ça coince :** chaque précision est défendable, mais l'ensemble forme un inventaire d'interfaces. Le public doit retenir **qui décide du placement** et **ce que la version autorise**, sans ouvrir aucun logiciel. La phrase « des projets explorent aussi les assemblages de moteurs » n'est pas précisément étayée par F8, qui documente Vulkan multi-GPU ; la retirer ou lui fournir son propre renvoi.

**Réécriture ciblée 3 :**

> Le logiciel décide aussi comment les cartes travaillent. Ollama privilégie une seule carte si tout y tient. LM Studio documente la sélection et la priorité des GPU ; cela ne signifie pas qu'un mode tensor est activé. Et dans llama.cpp, ce mode garde ses restrictions de cache et de modèles. Donc un résultat publié avec une ancienne version ne devient pas automatiquement une recette pour celle d'aujourd'hui. [F4–F7]

La possibilité de marques différentes reste une courte ligne distincte, limitée au support documenté par F8. Pas de promesse de compatibilité universelle.

### 4. La checklist doit rester une décision documentaire, pas un rite à accomplir

> « Pas besoin de transformer cette étape en séance de bricolage. Une feuille suffit… »

**Pourquoi ça coince :** le principe du tableau est utile ; « une feuille suffit » peut minimiser les inconnues de compatibilité. Le spectateur n'a pas besoin de réaliser une tâche pour que la vidéo ait un résultat. Le montage peut présenter les quatre critères déjà documentés.

**Réécriture ciblée 4 :**

> Le tableau peut donc garder quatre cases : dimensions, ports utilisables, câbles compatibles et marge d'alimentation. Une case inconnue laisse une dépense ou une incompatibilité possible. La facture de la deuxième carte commence là, avant son prix affiché.

Conserver les critères précis et la référence du manuel. Aucun stress-test, branchement ou relevé personnel à ajouter.

## Anti-IA et oralité

Passages à alléger : « Ça paraît évident, mais c'est précisément ce qu'un slogan trop court… » oppose le texte à un slogan non identifié ; « Personne ne gagne un multiplicateur universel… » répète la réserve déjà dite ; « Voilà la vraie addition » annonce une révélation ; « le giga le moins cher… le plus encombrant » peut rester comme unique chute, sans ajouter une morale après chaque section.

Les négations sur **32 Go physiques/32 Go libres**, **priorité d'allocation/mode tensor** et **connecteur long/nombre de lignes** corrigent de vraies confusions : les conserver. Les analogies du colis et du jeu coopératif ne doivent pas être réexpliquées une seconde fois.

**1 576 mots**, environ **10:52** à 145 mots/min, hors balises et crochet. Liaisons strictes : donc 12, du coup 3, par contre 2 = **17, soit 1,08/100**. Avec quatre « mais », **1,33/100**. Varier les raccords explicatifs et les réactions aux résultats ; ne pas ajouter mécaniquement « donc » pour atteindre un score.

Pour S3, les vrais changements sont : RAM qui déborde → gain possible ; fichier déjà en VRAM → autre attente ; mode tensor → communications ; port long → lignes actives ; logiciel → placement choisi. Les paragraphes de boîtier/alimentation et l'inventaire des moteurs prolongent l'explication sans nouveau retournement. Les coupes proposées doivent rapprocher ces déplacements du sens, plutôt que fabriquer du suspense.

## Faits et limites

- F1 : 36,05 / 34,03 / 47,06 sont correctement arrondis et concernent la génération ; le prefill instable n'est pas utilisé comme preuve.
- F2 est une autre expérience, pas une reproduction du même facteur. F3 vient du même auteur que F2 ; ne pas le compter comme un troisième testeur indépendant.
- Ajouter **F3 au 11–12 →21**, et F1/F2 à leurs paragraphes respectifs : les références de visuels génériques ne doivent pas remplacer une association nette chiffre/source.
- La documentation actuelle et les builds des essais sont distingués. Les restrictions du tensor ne sont pas transposées rétroactivement aux anciens rapports.
- Les exemples PCIe/boîtier sont fournis par le dossier prévalidé F9 ; aucune pénalité chiffrée universelle n'est inventée.
- Les cartes de marques différentes sont une possibilité conditionnelle, pas une preuve de vitesse sur tous les assemblages. F8 ne suffit pas à étayer vaguement tous les « assemblages de moteurs ».
- Aucun coût complet d'installation n'est chiffré ici ; le titre parle de points avant achat, pas d'un prix minimum.
- Aucun essai personnel ou protocole à faire exécuter à l'utilisateur. Les impératifs de choix portent sur les caractéristiques d'achat.

## À garder

> « Une carte écrit à 36… une deuxième… 34… répartition… 47. »

L'anomalie suffit à donner envie de comprendre.

> « Le modèle débordait auparavant en RAM. »

La condition qui empêche une conclusion fausse sur le mode par couches.

> « La forme du connecteur » et « les lignes actives ».

Deux notions faciles à montrer par schéma, avec une conséquence concrète sur l'achat.

> « Priorité d'allocation ne veut pas dire… mode tensor. »

Confusion réelle corrigée, utile pour le public LM Studio sans faire de tutoriel.

## Plan d'action

1. Conserver le hook et renforcer le lien explicite avec le contre-exemple de F3.
2. Ajouter les renvois précis aux trois mesures ; limiter la causalité aux comparaisons effectivement faites.
3. Condenser l'inventaire logiciel et supprimer la mention non sourcée d'assemblages de moteurs.
4. Améliorer les raccords entre obstacles, garder la checklist comme visuel documentaire et recompter oralité/durée.
5. Ajouter un renvoi bref à la vidéo **Mac mini ou PC gamer du 10 décembre**, selon le calendrier fourni : autre route quand ajouter une carte complique trop la machine. Aucun problème matériel bloquant repéré dans les chiffres retenus.


## Corrections appliquées après cet audit — 16 novembre 2026

- F3 associé directement au gain 11–12 → 21 ; F1/F2 explicitement associés à leurs graphiques.
- Causalité bornée à la configuration comparée ; aucune part isolée du lien PCIe prétendument mesurée.
- Inventaire logiciel condensé, mention non sourcée des assemblages de moteurs retirée, compatibilité conservée comme condition.
- Checklist documentaire, retour au problème d'achat et renvoi au Mac mini / PC du 10 décembre.
- Raccords oraux variés ajoutés et espaces des sources nettoyés, sans changer les faits.

Livrables : `script.md` et `teleprompteur.txt`, V1 conservée. Voix seule hors crochets : **1512 mots**, **10:26** à 145 mots/minute ; **28 liaisons strictes**, **1.85/100 mots**. Hook incluant question et disclaimer : **55 mots**, environ **0:23**. Timecodes recalculés sur les débuts réels des parties. Prompteur : nombres en chiffres, une ligne par souffle, lignes vides entre paragraphes, balises non dites. Ces métriques décrivent la correction ; elles ne modifient pas la note de l’audit indépendant.
