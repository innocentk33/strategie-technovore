# Grill indépendant — DeepSeek sans GPU

Revue du **16/11/2026**, [`script-v1.md`](script-v1.md) et [`sources.md`](sources.md), F1–F12. Méthode : [`youtube-script-grill`](../../ressources/skills-gpt/youtube-script-grill.md), mode B, variante storytelling : onze axes, S1–S6, test des trente secondes, anti-IA, réécritures et actions. Format documentaire ; aucun essai de l'auteur ni du spectateur à ajouter.

## Verdict : 6,3/10

La V1 a trouvé les vrais pièges : **le résultat appartient à V4 Flash 0731**, les 56,93 sont des **GiB**, la perplexité n'est pas un taux d'erreurs et les kits DIMM de bureau ne décrivent pas le portable mesuré. Ces précisions apportent une valeur réelle.

Mais le texte raconte trop souvent comment la recherche a corrigé le brief, puis défend ce qu'il refuse d'inventer. Cela ralentit l'histoire. La grille de qualité par palier mémoire et le seuil de rentabilité local/API restent non établis ; il faut les remplacer dans la promesse par les comparaisons effectivement disponibles. Les nombreuses concaténations rendent la V1 difficile à lire à voix haute.

Moyenne des onze axes : **69/110**, soit 6,3/10. Les axes S ne doublent pas cette note.

## Test des trente secondes

| Tranche | Citation | Verdict |
|---|---|---|
| 0–5 s | « Un DeepSeek de 284 milliards de paramètres écrit sans carte graphique… » | 🟢 Résultat surprenant et sujet immédiatement identifiés. |
| 5–15 s | « … sur une machine avec 64 gigas de RAM. Une mesure publiée donne environ 9 tokens par seconde. » | 🟢 Meilleur résultat attribué ; il s'agit bien de génération. |
| 15–30 s | « Sauf que le fichier est fortement compressé… Ces chiffres sont les leurs, je n’ai rien testé chez moi. Alors, acheter de la RAM… ? » | 🟠 Question proche de la limite, avec une réserve de prix encore abstraite. |
| Pont | « … on compare des kits 64,96 et 128 gigas… l’API qui porte presque le même nom. » | 🟢 Trois livrables et une seconde boucle sur l'identité de l'API. |

L'ouverture approche les **30 secondes à 145 mots/min** ; le nettoyage des mots collés peut encore l'allonger. Sujet/tension et meilleur moment passent ; question et budget sont à recalculer après normalisation. Le plan ouvre bien un problème supplémentaire. Chaque phrase a une fonction, mais « mémoire peut coûter plus cher que prévu » est moins concrète que le contraste portable/kits.

**Réécriture ciblée 1 :**

> Un DeepSeek de 284 milliards de paramètres écrit sans carte graphique, sur 64 gigas de RAM. Une mesure publiée donne environ 9 tokens par seconde. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Sauf que la compression dégrade le modèle. Donc acheter la mémoire pour le faire tourner, est-ce que ça vaut le coût ?

Environ soixante mots, autour de 25 secondes. Garder matériel, version et date du rapport à l'écran. Pas de promesse de vitesse pour tous les PC à 64 Go.

## Tableau de bord

| Axe | /10 | État | Diagnostic |
|---|---:|---|---|
| 1. Promesse | 7 | 🟠 | Coût de trois kits documenté ; qualité par palier et rentabilité complète non établies. |
| 2. Alignement | 8 | 🟢 | L'achat inutile de RAM est évité, CTA après distinction DIMM/portable. |
| 3. Problème profond | 7 | 🟠 | Autonomie contre nouvelle dépense ; cette tension arrive surtout à la fin. |
| 4. Public/complexité | 7 | 🟠 | Image de l'équipe d'experts claire ; juxtaposition unités/perplexité/prix dense. |
| 5. Valeur/originalité | 7 | 🟢 | Correction de modèle, unités et kits français : apport réel au résultat publié. |
| 6. Structure/transformation | 6 | 🟠 | Départ « sans GPU » → choix de dépense ; trop de commentaires de rédaction entre les preuves. |
| 7. Histoire | 6 | 🟠 | Bonnes objections, mais sections encore proches d'un relevé annoté. |
| 8. Mais / donc | 6 | 🟠 | « Maintenant, le prix… », « Maintenant, comparons… » marquent des rubriques. |
| 9. Engagement actif | 6 | 🟠 | Question initiale ; l'écart entre plus de RAM et meilleure qualité pourrait faire anticiper. |
| 10. Oralité/liaisons | 4 | 🟠 | **14/1 443 = 0,97 liaison stricte/100 mots**, nombreuses concaténations. |
| 11. Tics d'IA | 5 | 🟠 | Faux adversaires « conversion en douce », médailles mémoire, commentaire sur le titre. |
| S1. Trente secondes | 7 | 🟠 | Bon résultat ; question trop proche du plafond une fois les noms prononcés. |
| S2. Pont | 8 | 🟢 | Le modèle local et celui de l'API ouvrent une différence à découvrir. |
| S3. Retournements | 5 | 🟠 | MoE, unités et perplexité s'enchaînent en blocs ; relances irrégulières. |
| S4. Planté/récolté | 7 | 🟢 | 64 Go deviennent capacité précise puis dépense ; identité du modèle revient avec l'API. |
| S5. Personnages/enjeu | 6 | 🟠 | Acheteur déjà équipé ou devant étendre sa RAM ; aucun faux récit personnel. |
| S6. Fin | 6 | 🟠 | Profils présents, renvoi à la prochaine vidéo absent ; conclusion un peu morale. |

## Le grill

### 1. Le spectateur entend le brief corrigé

> « LeV4.1 de la promesse de départ correspond à un autre modèle. Donc le titre doit suivre le fichier qui a produit le résultat… »

> « L’échelle complète qu’on avait comme piste n’a pas été vérifiée… »

**Pourquoi ça coince :** le spectateur ne connaît ni la fiche initiale ni les pistes abandonnées. Il lui faut la version exacte et les comparaisons disponibles. Ces phrases le sortent du sujet pour lui expliquer la rédaction de la vidéo.

**Réécriture ciblée 2 :**

> Le fichier mesuré est DeepSeek V4 Flash 0731. Le rapport utilise un Ryzen 9 9955HX avec 64 gigas de DDR5. Donc ce résultat décrit cette machine et ce fichier. L'API actuelle sert une autre version ; on gardera cette différence dans le calcul de prix.

Le nom du processeur doit être corrigé : **Ryzen 9 9955HX**, jamais « Ryzen 99955 HX ».

### 2. Les kits sont des exemples de prix, pas une échelle de qualité

> « Mais acheter 96 ou 128 gigas ne rend pas automatiquement le même fichier plus intelligent. »
> « Donc 96 gigas n’obtiennent pas magiquement une médailleargent, et 128 une médailleor. »

**Pourquoi ça coince :** la première idée est utile ; la seconde caricature une croyance et répète l'avertissement. Surtout, le plan « chiffrer le compromis de qualité puis comparer les kits » peut faire attendre une correspondance coût/qualité que F11 ne fournit pas.

**Réécriture ciblée 3 :**

> Ces trois prix comparent la mémoire achetée. Pour le même fichier, davantage de RAM apporte de la marge. Un autre niveau de qualité demanderait un autre fichier et une évaluation comparable. Cette échelle-là n'est pas établie dans les sources retenues.

Dire ce manque une fois. Garder les kits comme exemples marchands, avec format DIMM, délais/rupture et conversion du prix français. Ne pas leur inventer un score de qualité.

### 3. La différence de modèle suffit à limiter le calcul API

> « Je ne convertis pas ce montant en euros en douce pour annoncer un nombre d’années de rentabilité. »

**Pourquoi ça coince :** l'honnêteté est déjà visible dans les données. Cette phrase introduit un mauvais calcul imaginaire et donne une tonalité défensive. Les entrées manquantes sont plus utiles que le refus de tricher.

**Réécriture ciblée 4 :**

> L'exemple API reste en dollars, et il porte sur une autre version du modèle. Pour calculer une rentabilité en euros, il manque encore le volume réel, les taxes et le change. On peut comparer l'ordre des dépenses ; on ne peut pas donner un nombre d'années valable pour tout le monde.

L'opposition ici corrige une confusion réelle entre exemple de facture et seuil de rentabilité. Ne pas répéter ensuite les mêmes limites sous une autre forme.

### 4. La fin referme le sujet, mais ne prépare pas la suite

> « Le piège, c’est d’en déduire que la machine, le fichier et la qualité sont devenus gratuits. »

Personne n'a prétendu que la qualité était « gratuite » ; l'image peut être remplacée par le choix déjà établi : mémoire existante ou dépense nouvelle, fichier compressé ou autre version. Le calendrier fourni place **multi-GPU le 7 décembre**, après cette vidéo du 3. Un renvoi naturel peut annoncer l'autre route matérielle, sans prétendre qu'une deuxième carte est nécessaire ou toujours meilleure.

## Faits, oralité et production

- **1 443 mots à espaces**, environ **9:57**, hors notes et balises. Les concaténations sous-estiment la prononciation ; recompter après nettoyage. La cible 10–12 min est atteignable sans ajouter de remplissage.
- Liaisons strictes : donc 7, du coup 3, en fait 1, sauf que 1, par contre 1, voilà pourquoi 1 = **14, soit 0,97/100**. Avec sept « mais », **1,46/100**. Les raccords entre capacité, unités, qualité et coût doivent être renforcés.
- Nettoyer notamment `DeepSeekV4`, `DDR5`, `vieuxPCen`, `61%de`, `chezLDLCle`, `kitCorsairretenu`, `FCFApar`, `RAMachetée`, `APIindique`, `Àl’inverse`. Une marque ou unité collée au mot voisin n'est pas une notation technique utile.
- F1/F2 soutiennent V4 Flash 0731, 56,93 GiB ≈61,13 Go, 284B et environ 9 tokens/s sur le matériel donné. La source est une seule équipe ; dire clairement qu'aucune reproduction indépendante correspondante n'est retenue.
- F3 soutient la hausse de perplexité arrondie à 61 %, **pas 61 % d'erreurs**. La V1 fait correctement cette distinction.
- Les prix F5–F7 sont des kits **de bureau**, pas la facture du portable benchmarké. Cette différence doit rester visible dès le tableau, pas seulement dans une note après les trois prix.
- Les conversions FCFA sont des calculs au taux fourni, pas des prix livrés localement. Le kit 128 Go en rupture n'est pas une offre commandable.
- F9/F10 : 0,75/1,50 dollar pour l'exemple entrée+sortie, autre modèle API ; aucune comparaison à qualité identique ni seuil de rentabilité établi.
- F11 : paliers de qualité 96/128 Go et certaines valeurs de compression restent non validés. Le script ne doit pas vendre leur résolution.
- Aucun essai personnel ni capture à demander ; tableaux, schémas d'experts et extraits publics suffisent.

## À garder

> « Les autres spécialistes restent dans le bâtiment, mais ils ne travaillent pas tous sur ce mot. »

Explique pourquoi le stockage reste nécessaire même si une partie des poids travaille.

> « Ça ne veut pas dire 61 % de réponses fausses… »

Correction indispensable, appuyée par l'explication de la perplexité.

> « Ces trois kits sont des barrettes pour PC de bureau. Ils ne sont pas la liste de courses du portable qui a produit la mesure. »

Évite un mauvais achat concret et justifie le CTA demandé.

## Plan d'action

1. Nettoyer les concaténations et le nom du processeur, puis recalculer ouverture et durée.
2. Remplacer les commentaires sur le brief par la version exacte du modèle et les limites directement utiles.
3. Présenter les kits comme exemples de coût, sans prétendre à une échelle qualité/mémoire non établie.
4. Raccourcir les précautions API et ajouter de vrais raccords causaux ; garder le calcul borné en dollars.
5. Refermer les profils sur la dépense utile et annoncer la vidéo multi-GPU du 7 décembre. Aucun problème matériel bloquant repéré dans les chiffres retenus ; les limites de comparaison restent explicites.

## Corrections appliquées après la revue

- Version locale donnée directement, commentaires sur le brief et refus de conversion supprimés.
- Processeur corrigé en Ryzen 9 9955HX ; voix et notes espacées et relues.
- Kits présentés comme exemples de bureau, sans score qualité inventé ; délais et rupture conservés.
- Coût marginal expliqué ; renvoi multi-GPU du 7 décembre ajouté.
- Résultat final : 1597 mots hors balises, 11.01 minutes à145 mots/min ; ouverture 58 mots≈24.0s ; 25 liaisons strictes, 1.57/100.
- Téléprompteur produit avec nombres en chiffres et lignes de souffle. Les limites factuelles du rapport sont maintenues.

Contrôle ciblé supplémentaire : répétitions et analogie redondante retirées. Final actualisé : 1529 mots, 10:33, 24 liaisons strictes soit 1.57/100 ; timecodes et TP régénérés.
