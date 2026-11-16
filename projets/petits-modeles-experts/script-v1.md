# Un petit modèle peut-il remplacer ton IA du cloud ?

V1 documentaire, 28 janvier 2027. Sources arrêtées au 16 novembre 2026. Cible : 10–12 minutes, 145 mots/minute. Aucun essai personnel ou entraînement nécessaire.

## Voix

[VISUEL : ChartQA test, LFM3-VL-2B 92,7 / GPT-5.6 Luna 90,2 ; « résultats Liquid AI, octobre 2026, sans réplication indépendante ». F1–F2.]

Un modèle de 2 milliards dépasse GPT-5.6 Luna sur un test de lecture de graphiques : 92,7 contre 90,2, selon son éditeur. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc, pour ton travail précis, un petit modèle local peut-il remplacer celui du cloud ?

On va séparer trois tâches : lire un document, résoudre un problème de maths et modifier du code. Puis on regardera ce qui peut tenir sur une carte de 8 ou 12 gigas. Le retournement arrive dès qu'on change de ligne dans le même tableau : le vainqueur peut changer aussi.

[VISUEL : graphique fictif simple portant « illustration de la tâche, aucun test effectué », puis deux lignes de benchmark. F2–F3.]

Sur ChartQA, le modèle répond à des questions sur des graphiques. Il doit reconnaître les éléments visibles, retrouver des valeurs et parfois les comparer. On peut imaginer une question comme : quelle catégorie a le plus progressé ? La tâche mélange lecture de l'image et raisonnement sur ce qu'elle montre.

Le petit modèle du début, LFM3-VL, contient environ 1,92 milliard de paramètres au total. L'éditeur le compare à plusieurs modèles, dont des services du cloud. Son score est meilleur sur cette ligne. Par contre, cette mesure ne suffit pas à lui confier automatiquement un PDF de cent pages et une synthèse complète.

Changeons seulement de tâche : les infographies. Dans la même publication, le petit modèle obtient 86,2, tandis que GPT-5.6 Luna monte à 92,4. Donc une victoire sur les graphiques ne devient pas une victoire sur toutes les images documentaires. La différence se voit sans même changer de laboratoire ou chercher un contre-exemple ailleurs.

Du coup, pour tes factures, tes cours ou tes tableaux scannés, la question utile est plus précise : faut-il extraire une date, lire un graphique, reconnaître un tableau ou relier plusieurs pages ? Le mot « document » peut cacher ces quatre travaux. Un seul score ne les remplace pas.

Ces résultats viennent de l'équipe qui publie le modèle. Les conditions de réflexion sont décrites, mais les budgets de calcul des concurrents ne sont pas rendus identiques. Et on ne dispose pas ici d'une reproduction indépendante. On garde donc une piste sérieuse sur une tâche bornée, avec la marge nécessaire autour du résultat.

[VISUEL : une facture fictive, champ montant, puis flèche vers un calcul séparé. Mention « exemple de méthode ». F11.]

Prenons une chaîne de travail très simple. Un modèle extrait un montant et une date. Un programme additionne ensuite les montants. Un autre modèle peut rédiger la présentation. Chaque étape a un résultat vérifiable : les champs, le calcul, puis le texte. On peut donc limiter ce que l'on demande au modèle le plus petit.

Sauf que la première erreur peut traverser toute la chaîne. Si le montant extrait est faux, un calcul parfaitement exécuté donnera quand même un mauvais total. Ajouter un deuxième modèle ne corrige pas automatiquement la première lecture. La provenance de chaque valeur reste utile jusqu'au bout.

Imagine maintenant une facture avec une remise et plusieurs taux de taxe. Lire le chiffre imprimé, comprendre à quelle ligne il appartient et recalculer le total sont trois opérations. Un modèle peut réussir la lecture et se tromper dans l'interprétation. Donc le résultat utile garde le lien entre le champ extrait et sa ligne d'origine. On peut montrer cette différence dans un schéma sans prétendre qu'un modèle a passé cet exemple.

Le spécialiste devient intéressant quand la tâche est fréquente, précise et contrôlable. Il peut garder tes données sur la machine pendant cette opération locale. En revanche, si ton application appelle ensuite un service externe, le caractère local du premier modèle ne décrit plus tout le trajet des données.

[VISUEL : frise « exemple historique — janvier 2025 », noms exacts des versions ; AIME 2024 pass@1. F6–F7.]

Passons aux maths avec un exemple historique, publié en janvier 2025. DeepSeek a distillé une partie des capacités de raisonnement dans un modèle Qwen de 7 milliards. Sur AIME 2024, son tableau donne 55,5, contre 9,3 pour la version de GPT-4o datée de mai 2024.

Ce résultat montrait déjà qu'un petit modèle pouvait dépasser un grand service sur un examen précis. Par contre, le même tableau donne 63,6 à o1-mini. La conclusion reste donc attachée au concurrent et à sa version. Elle ne décrit pas le classement des services disponibles aujourd'hui.

La distillation consiste ici à entraîner le petit modèle avec des exemples de raisonnement produits à partir d'un modèle plus puissant. C'est une manière de transmettre des comportements utiles sur certaines tâches. Elle ne copie pas tout le savoir ni toutes les capacités du grand modèle dans un fichier réduit.

Du coup, le budget de réponse compte aussi. L'article autorise jusqu'à 32 768 tokens de sortie. Le modèle peut consacrer beaucoup de texte à chercher une solution. Si on réduit fortement ce budget pour attendre moins longtemps, le score publié ne suit pas automatiquement.

Et le tableau contient une autre colonne, obtenue en comparant plusieurs réponses et en votant. En fait, ce résultat répond à une autre question : que gagne-t-on avec plusieurs essais ? On ne peut pas le présenter comme la réussite d'une réponse unique. Pour tes devoirs, la démonstration et la vérification du calcul restent nécessaires.

Si tu veux choisir tes modèles selon ce qu'ils savent faire, abonne-toi.

[VISUEL : code, deux tâches séparées ; LiveCodeBench v6 et SWE-bench Verified/OpenCode, jamais une moyenne commune. F4–F5.]

Pour le code, on retrouve le même changement de classement avec une publication plus récente. Le LFM3 texte de 1,7 milliard dépasse Qwen3.5-9B sur LiveCodeBench version 6 : environ 73,5 contre 69,9. Sur des problèmes de programmation de ce test, le plus petit arrive devant.

Sauf que sur SWE-bench Verified, avec OpenCode, l'ordre s'inverse : environ 43,4 contre 51,2. Là, le système doit résoudre un problème dans un dépôt de code. Il faut identifier les fichiers, comprendre le comportement attendu et produire un correctif. Donc la tâche dépasse l'écriture d'une fonction isolée.

Les outils autour du modèle font aussi partie de ce deuxième résultat. Le programme qui lui permet de lire les fichiers, de modifier le code et de vérifier les changements influence le travail. On ne peut pas attribuer tout le score à la seule taille des poids.

Du coup, un petit modèle peut convenir pour une transformation bien définie : expliquer une fonction courte, préparer un fragment ou remplir un format régulier. Pour une correction qui traverse plusieurs fichiers, la preuve nécessaire change. Le tableau récent nous donne justement les deux situations, au lieu d'un vainqueur unique.

Prenons deux demandes fictives. La première : convertir une petite liste en un format imposé. La seconde : retrouver pourquoi une application échoue après une mise à jour. Dans la deuxième, il manque souvent des informations au départ. Le système doit les chercher et réviser son hypothèse. Du coup, le nombre de paramètres ne raconte pas à lui seul la difficulté de la mission. Le type de preuve à regarder change avec cette autonomie.

Cette différence évite un achat inutile. Si ton usage consiste surtout à répéter une petite opération, chercher le modèle le plus général peut te coûter de la mémoire sans répondre à ton besoin. Par contre, une longue mission autonome demande une capacité que le premier score ne mesure pas.

[VISUEL : tailles de fichiers, sans confondre texte/vision ; poids + cache + exécution + images. F8–F10.]

Reste ta carte de 8 ou 12 gigas. Les fichiers existent réellement : la version texte LFM3 en Q4 occupe environ 1,1 giga. Le modèle vision possède un fichier BF16 d'environ 3,84 gigas. Et une version Q4 du DeepSeek distillé de 7 milliards fait environ 4,68 gigas.

Donc on a des candidats beaucoup plus accessibles qu'un grand modèle impossible à charger dans ta machine. Sauf que la taille du fichier n'est pas l'occupation complète. Le cache de conversation, les images et les besoins du moteur utilisent encore de la mémoire. Un document plus long peut changer la marge disponible.

Et une copie compressée peut produire une autre qualité que celle évaluée dans la publication. En fait, le score et le fichier doivent rester reliés à leurs conditions. On peut vérifier qu'une variante légère existe sans lui attribuer automatiquement la note de la variante d'origine.

Sur une petite carte, les modèles peuvent aussi travailler successivement. Charger le lecteur, récupérer son résultat, puis charger le modèle de texte évite de réserver toute la mémoire en même temps. Par contre, on ajoute du temps de chargement et une transmission entre étapes. Cette organisation n'a pas été mesurée ici comme une équipe supérieure au cloud.

[VISUEL : trois profils : extraction répétitive / problème spécialisé / mission ouverte. F11.]

Si tu extrais toujours les mêmes champs, le petit modèle spécialisé mérite une place dans ta comparaison. Si tu fais des maths ou du code, le benchmark doit correspondre au type de problème et au budget de réponse. Et si ta demande change constamment, un généraliste plus capable peut rester utile pour les étapes difficiles.

[CROCHET : ton avis sur la tâche répétitive que tu confierais volontiers à un petit modèle local, facultatif.]

Les chiffres du départ ont maintenant une place précise : ils montrent qu'une petite machine peut faire une partie du travail à un bon niveau. Donc tu peux choisir ton modèle à partir de la tâche, du fichier et de la mémoire disponible. La question pour la suite, c'est celle que tu lui confieras vraiment chaque semaine. Allez, salut !

## Hors voix

Faits F1–F11. Comparaisons d'éditeurs, absence de réplication dite une fois ; résultat historique maths clairement daté. Pas de protocole à réaliser ni de score personnel à inventer. Les exemples de facture et de graphique sont des illustrations fictives, pas de fausses captures. Aucun prix, abonnement ou achat demandé. La spécialisation n'est pas assimilée au routage interne d'un MoE ni à un entraînement personnel déjà réalisé.
