# Grill indépendant de la V1 : Qwen 27B sur 8 Go

Revue du **16 novembre 2026**. Texte critiqué : [`script-v1.md`](script-v1.md), conservé intact. Grille : les dix axes du [`prompt-reprise-gpt.md`](../../prompt-reprise-gpt.md) et les règles de [script](../../.claude/rules/script.md). Comparaison avec les deux transcriptions fournies et avec le script/grill de `meme-carte-plus-rapide`. Aucun essai matériel effectué.

## Verdict : 7,3/10

La V1 protège correctement la confiance : le résultat est attribué dès la première phrase, la carte est « limitée » à 8 Go, l'absence d'essai personnel arrive avant 20 secondes et le titre abandonne la promesse universelle du ×5. La construction diffère déjà du tutoriel d'inspiration grâce aux réglages LM Studio placés tôt et à la comparaison sur une tâche familière.

Mais elle **explique beaucoup pourquoi elle est prudente et montre trop peu le prix réel du compromis**. La section qualité, qui doit faire basculer la décision, ne donne aucun écart chiffré. Plusieurs commentaires sur la méthode prennent la place d'une réaction naturelle. Le lien avec la vidéo précédente sur le MTP manque. Le résultat est sérieux, mais plus proche d'un conseil documenté que d'une démonstration mémorable.

## Comptage et chronométrage

Méthode : uniquement le texte sous `## Voix`, sans les titres, les blocs entre crochets ni les références. Mots séparés par espaces ; les noms techniques et nombres décimaux peuvent prendre davantage de temps à prononcer. Débit demandé : **145 mots/minute**.

**1 423 mots parlés, soit environ 9 min 49 s**, avant pauses, manipulation à l'écran et crochet personnel. La V1 est donc déjà en haut de la cible de 8 à 10 minutes. Toute insertion doit s'accompagner de coupes. Les timecodes provisoires de l'en-tête ne suivent pas la longueur réelle.

| Partie | Mots | Début calculé | Durée calculée |
|---|---:|---:|---:|
| Résultat et enjeu | 65 | 0:00 | 0:27 |
| Plan | 33 | 0:27 | 0:14 |
| Le bon fichier | 242 | 0:41 | 1:40 |
| Réglages LM Studio | 307 | 2:21 | 2:07 |
| Ce que prouve la mesure | 188 | 4:28 | 1:18 |
| Conversation | 190 | 5:45 | 1:19 |
| Qualité | 211 | 7:04 | 1:27 |
| Verdict | 187 | 8:31 | 1:17 |

Le retour sur la qualité annoncé « juste après » intervient en réalité environ 2 min 40 s plus tard. Et le verdict commence vers 8:31, pas 7:15 comme dans le tableau provisoire.

## Les dix axes

| Axe | Note /10 | Diagnostic |
|---|---:|---|
| 1. Les 15 premières secondes | 8 | Le meilleur chiffre est immédiatement livré et attribué ; la formulation reste un peu technique. |
| 2. Les 30 premières secondes | 8 | Pas de salutation, disclaimer à temps, question avant 30 s ; « perd des capacités » manque d'image. |
| 3. Le plan | 7 | Fichier, réglages, contexte sont concrets ; « décider combien » dépasse ce que la vidéo peut réellement garantir. |
| 4. Promesse du titre | 7 | Le fichier est donné ; le compromis principal est expliqué très tard et sans son ampleur. |
| 5. Problème profond | 8 | Garder sa carte et obtenir un travail utile plutôt qu'un beau compteur est bien posé. |
| 6. Enchaînement mais/donc | 7 | Bons raccords mémoire/qualité ; retour au protocole après les réglages et faux « juste après ». |
| 7. Liaisons et ton d'ami | 7 | Ton globalement juste ; liaisons juste sous le repère strict et nombreuses précautions de rédacteur. |
| 8. Tics d'IA | 6 | Métadiscours, oppositions répétées, une fausse annonce de retour ; pas de vocabulaire pompeux. |
| 9. Faits et traçabilité | 7 | Bonne prudence et renvois cohérents, mais qualité non quantifiée et lien MTP omis. |
| 10. Fin | 8 | Trois profils, crochet et prochaine vidéo ; trois paragraphes après le verdict étirent la sortie. |

Moyenne arithmétique : **73/100, soit 7,3/10**. Il s'agit d'une appréciation éditoriale, pas d'une mesure d'efficacité sur YouTube.

### 1. Les quinze premières secondes

> « Un testeur fait passer Qwen 27B de 3,2 à 18 tokens par seconde en écriture, sur une carte limitée à 8 gigas. Il change le fichier du modèle. »

Le résultat complet et son attribution tiennent dans environ 13 secondes. C'est bien le moment le plus fort. « En écriture » protège la distinction avec la lecture du prompt, mais alourdit la phrase. Et « carte limitée » mérite d'être conservé : dire simplement « carte de 8 gigas » ferait disparaître la simulation du budget mémoire.

**Réécriture :** « Sur une carte limitée à 8 gigas, un testeur change de fichier. Son IA passe de 3,2 à 18 tokens par seconde pour écrire sa réponse. »

Ne pas rajouter « cinq fois » : le rapport au contexte vide est **18 / 3,2 = 5,625**, calcul tiré de la mesure F2, et ce résultat n'a pas de seconde reproduction vérifiée sur une vraie carte de 8 Go.

### 2. Les trente premières secondes

> « Ces chiffres sont les leurs, je n'ai rien testé chez moi. Sauf que le fichier plus petit perd aussi des capacités. »

La transparence arrive vers 0:13–0:18. La question centrale se termine vers 0:27. C'est conforme. « Les leurs » suit pourtant « un testeur », et « des capacités » ne fait voir aucun risque concret.

**Réécriture :** « Ces chiffres sont ceux du testeur, je n'ai rien testé chez moi. Sauf que le fichier plus petit réussit moins bien certains travaux. Donc tu peux lui confier quoi, sur ta carte ? »

Variante plus forte si F4 permet une attribution courte : annoncer le décrochage sur les projets entiers, sans introduire un deuxième tableau de chiffres avant le plan.

### 3. Le plan

> « On va choisir le fichier, repérer les réglages dans LM Studio et décider combien de conversation lui laisser. »

Les livrables sont identifiables. Cependant, la vidéo ne détermine pas une capacité réellement soutenable sur la machine du spectateur : elle propose 4 096 tokens comme départ. Le verbe « décider » vend plus de certitude que la suite.

**Réécriture :** « Voilà le fichier, les réglages à repérer dans LM Studio et un point de départ pour la conversation. Et le travail pour lequel je garderais l'ancien, même plus lent. »

Le plan se place correctement de 0:27 à 0:41. La partie suivante commence bien par le nom du fichier, pas par une définition.

### 4. La promesse du titre

> « Sur certains exercices de code, le petit fichier reste proche du modèle complet. Sur leur test de travail autonome dans un dépôt de code, il décroche beaucoup plus. »

Le fichier promis est identifié dès 0:41. En revanche, « le compromis à connaître » reste abstrait jusqu'à environ 7:04, puis son ampleur demeure floue. Le spectateur a attendu sept minutes pour entendre « proche » et « beaucoup plus ».

**Réécriture après contrôle direct du graphique primaire F4 :** « Sur leur test de travail autonome dans un dépôt, le modèle complet réussit environ 40 % des tâches. Le petit fichier, environ 13 %. Voilà pourquoi je sépare l'aide sur une fonction et l'agent auquel tu confies le projet. »

Si les nombres proviennent seulement d'une lecture graphique, dire « environ » et l'indiquer à l'écran. Ne pas remplacer le ratio d'un benchmark par « il garde 95 % de son intelligence ». Garder l'attribution Unsloth et les conditions différentes de celles proposées sur 8 Go.

### 5. Le problème profond

> « Donc avant de condamner ta carte, ça mérite de regarder ce qu'un autre fichier permet. »

L'enjeu financier est présent sans prétendre donner un prix. Mais cette phrase reste impersonnelle, alors que le spectateur veut savoir s'il peut travailler avec le matériel qu'il possède.

**Réécriture :** « Donc avant de mettre de l'argent dans une autre carte, regarde si celle que tu as peut déjà t'aider sur ton travail. »

La meilleure phrase de cette V1 mérite d'être conservée : « Une réponse rapide que tu dois réparer peut te coûter plus de temps que l'ancienne réponse lente. » Elle traduit le benchmark en usage réel sans inventer un résultat personnel.

### 6. Les raccords entre les parties

> « Et réflexion coupée ne veut pas dire qualité identique. On revient là-dessus juste après. »

La section suivante traite du protocole, puis vient le contexte. La qualité arrive seulement après ces deux détours. L'annonce est factuellement mauvaise dans le déroulé.

**Réécriture :** « Sauf que couper la réflexion change aussi les réponses. Garde ça en tête quand on regardera les scores. » Ou supprimer l'annonce et traiter cette condition avec les scores.

> « Enfin, regarde le contrôle de réflexion. »

« Enfin » termine une liste, sans montrer pourquoi ce réglage suit le contexte.

**Réécriture :** « Et cette place peut aussi être mangée par sa réflexion. Pour commencer avec des demandes simples, regarde si tu peux la désactiver. » Ne pas transformer cette proposition en promesse de maintien de qualité.

### 7. L'oralité et les liaisons

Comptage reproductible, insensible à la casse : **donc 9, du coup 3, en fait 1, sauf que 4, en effet 0, par contre 1, voilà pourquoi 1, voilà comment 0**. Soit **19 liaisons pour 1 423 mots = 1,34 pour 100 mots**. En ajoutant les cinq « mais », le total monte à **24 = 1,69 pour 100**. Le seuil de 1,5 est donc atteint seulement avec cette liste élargie ; ne pas annoncer un succès sans donner la méthode.

> « Nous avons retrouvé ses notes »

C'est un passage à « nous » dans un texte qui doit employer « on ». **Réécriture :** « On a retrouvé ses notes. »

> « L'image explique le principe, elle ne prédit pas la vitesse de ta machine. »

Cette explication de l'analogie casse le ton d'ami. **Réécriture :** supprimer. La limite sur la future vitesse est déjà dite dans la partie consacrée à la mesure.

Deux ou trois vrais raccords causaux, ajoutés aux endroits utiles, suffisent. Inutile d'ajouter mécaniquement « donc » devant toutes les phrases.

### 8. Les tics repérés

Les mots bannis comme « plongeons », « décortiquons », « en résumé » et les triplets d'adjectifs sont absents. Les répétitions de forme restent audibles :

- **Commentaire sur le statut de l'exemple :** « C'est une proposition pour ton essai, pas un résultat que j'aurais obtenu. » → supprimer après avoir gardé l'absence d'essai personnel dans l'ouverture et la proposition au conditionnel.
- **Commentaire sur l'analogie :** « L'image explique le principe… » → supprimer.
- **Précaution centrée sur le narrateur :** « Je ne vais pas te promettre qu'il apparaît sur tous les fichiers importés. » → « Ce bouton dépend du fichier et de sa configuration. »
- **Oppositions répétées :** « pas un plafond à battre », « pas une capacité mesurée », « pas un bouton magique », « pas une confirmation indépendante », « pas dans celle des assistants… », « pas de farmer les tokens ». Certaines sont utiles, mais leur accumulation ressemble à une liste de garde-fous. Garder celles qui évitent une confusion réelle et raccourcir les autres.
- **Annonce au lieu de raccord :** « On revient là-dessus juste après » → correction axe 6.
- **Conclusion abstraite :** « Voilà le choix réel. » → supprimer après le choix déjà expliqué.

La formule « pas de farmer les tokens » est, elle, adaptée à la voix et au public ; elle vaut mieux que trois précautions autour de l'analogie du coffre.

### 9. Les faits

La V1 ne présente aucune estimation personnelle comme une mesure et ne prononce aucun nom de chaîne. Le hook possède F2 dans son visuel. Les nombres 7,63, 14 000 et 4 096 sont référencés ; 4 096 est correctement présenté comme une proposition. Les métadonnées de durée et les timecodes doivent être recalculés, mais ne sont pas des mesures matérielles.

**Corrections importantes :**

1. Le lien avec le MTP de la vidéo précédente manque, alors que la fiche le demande. **Insertion courte :** « Et le MTP de la vidéo précédente ? Dans cet essai, il reste coupé pour garder de la place. Ici, la priorité, c'est de faire tenir le modèle. » Ne pas dire « le MTP ne marche pas sur 8 Go » : les essais avec une partie du modèle en RAM peuvent l'utiliser. F2 suffit à sourcer son absence dans la recette visée ; le supplément mémoire précis doit avoir sa propre source si on le chiffre.
2. La section qualité doit donner une preuve concrète, mais **seulement les valeurs effectivement vérifiées dans F4**. Le modèle complet face au 2 bits ne suffit pas, à lui seul, à mesurer le gain du fichier 4 bits recommandé en fin ; si aucune valeur du 4 bits n'est relevée, conserver ce verdict comme jugement prudent explicite.
3. Les tests Unsloth à grand contexte et réflexion élevée ne valident pas le contexte court avec réflexion coupée : la V1 l'explique, à conserver.
4. Les contrôles LM Studio documentés ne prouvent pas le fonctionnement du GGUF précis : la réserve de la V1 est juste. Pour une recette réellement exécutable, afficher les libellés K/V et les valeurs du protocole, en distinguant clairement sa reproduction llama.cpp d'un point de départ LM Studio.
5. « La lecture du prompt reste du même ordre » doit rester attaché à **son essai**, comme dans la V1, sans généralisation.

Le manuscrit V1 annonçait `sources.md` « en cours de consolidation ». Le fichier a depuis été lu : F1 à F15 correspondent aux usages de la V1. **Contrôle complémentaire du graphique primaire F4 le 16/11 :** annotation BF16 DeepSWE **40,40**, point vert UD-IQ2_XS lu à **environ 12,8**, point UD-IQ4_XS à **environ 36,2** ; annotation BF16 LiveCodeBench **88,62**, point UD-IQ2_XS à **environ 84,5**. Les points n'ont pas d'étiquette numérique exacte : les décimales issues de leur lecture restent des estimations. Le contraste oral « environ 40 % contre environ 13 % » est donc autorisé, avec attribution à Unsloth et mention de lecture arrondie. Ce contrôle confirme aussi le sens de la préférence pour un fichier moins compressé ; il ne valide pas tous les travaux réels.

### 10. La fin

> « Pour un agent qui doit travailler longtemps dans tout un projet : je garderais un fichier moins compressé, quitte à attendre davantage. »

Le verdict par profil est clair. L'avis est au conditionnel et le crochet ne porte pas une information indispensable. Le renvoi au jeudi suivant est cohérent avec le 26 novembre annoncé dans le prompt. « Allez, salut ! » est présent.

> « Ta carte de 8 gigas n'est donc pas automatiquement bonne à remplacer. Mais le fichier ne lui ajoute pas de mémoire. Tu échanges de la précision et de la place pour la conversation contre une chance de tout faire tenir dessus. Voilà le choix réel. »

C'est une deuxième conclusion après les trois profils. **Réécriture :** « Donc garde ta carte tant qu'elle rend le service dont tu as besoin. Si le contexte ou la qualité te bloquent, jeudi on compare les cartes selon ton budget. »

Le sens de « tu échanges de la place pour la conversation » pourrait aussi se comprendre à l'envers : réduire le fichier libère de la place par rapport à un autre fichier entièrement sur GPU, mais la recette full-GPU limite le contexte par rapport à l'ancien partage RAM/GPU. Les profils évitent ce raccourci causal.

## Originalité face aux deux inspirations

La V1 ne reproduit pas les démonstrations de pages web, l'opposition à Opus ou le récit d'incidents de Red Stapler. Elle ne doit surtout pas présenter ces résultats comme ceux de l'auteur.

L'écart avec SimplyExplain est plus fragile : le nouveau fichier, le passage RAM → GPU, les limites de contexte, la perte en agent et le crash sont déjà toute sa progression. Les raconter dans le même ordre avec « LM Studio » ajouté ne suffirait pas. La V1 fait mieux : elle place le retour à l'ancien fichier et le contrôle sur une tâche familière avant les détails du benchmark ; elle met les réglages tôt, puis construit une décision par profil. **À conserver comme colonne vertébrale.**

Pour renforcer cet écart, le visuel récurrent devrait suivre la décision du spectateur : « ça tient ? / ça répond assez bien ? / la conversation suffit ? ». Ce serait un dispositif éditorial, pas un résultat de test à fabriquer.

## Priorités pour la version corrigée

1. Donner l'écart de qualité réellement vérifié, avec son attribution et son approximation éventuelle.
2. Ajouter le pont MTP sans affirmer son impossibilité universelle sur 8 Go.
3. Couper les précautions qui répètent l'ouverture, corriger « nous » et le faux « juste après ».
4. Garder une distinction lisible entre contrôles LM Studio documentés, mesures llama.cpp publiées et proposition de départ.
5. Recompter la voix et recaler les timecodes après ces changements ; viser une marge sous dix minutes pour respirations et captures.

## Contrôles indépendants effectués pour la revue

Pages ouvertes le 16/11/2026, en plus des fichiers de recherche :

- [Dépôt Unsloth, liste de fichiers](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main) : présence de l'IQ2_XS à 7,63 GB et d'autres petites quantifications ; ne pas inventer « premier 2 bits qui tient ».
- [Guide Unsloth Qwen3.8](https://unsloth.ai/docs/models/qwen3.8) : évaluations internes, contexte 256K pour l'agent et 128K pour le reste, réflexion xhigh dans le protocole décrit.
- [Réglages par modèle LM Studio](https://lmstudio.ai/docs/app/advanced/per-model) : chemin My Models/engrenage, offload, contexte, Flash Attention.
- [Configuration model.yaml](https://lmstudio.ai/docs/app/modelyaml) : le contrôle de réflexion repose sur une configuration et une variable du template ; pas de bouton universel garanti pour tout import.
- [Libellés officiels LM Studio](https://github.com/lmstudio-ai/localization/blob/main/en/config.json) : contrôles K/V ; Flash Attention requis pour le cache V quantifié.
- [CompressionBench](https://arxiv.org/html/2611.06858v2) : page officielle, dates v1/v2, section 3.1 et tableau A3 relus ; H200 NVL confirmé, contrainte de stockage des poids distincte du pic mémoire total. L'absence du détour dans la voix est une bonne coupe pour cette vidéo.


## Contrôle de la version corrigée

Compte rendu final ajouté par l'agent principal à partir du retour indépendant d'Astra : les principaux défauts sont corrigés, sans attribuer une nouvelle note à la version finale. Astra a inspecté le PNG primaire : BF16 DeepSWE 40,40 annoté, UD-IQ2_XS environ 13 lu graphiquement, IQ4_XS autour de 36. Le contraste chiffré soutient maintenant le verdict par usage. Le pont MTP est présent, les précautions redondantes ont été raccourcies et le faux retour « juste après » a disparu.

Contrôle final de la voix par l'agent principal : **1406 mots**, **9 min 42 s à 145 mots/min**, hors pauses et crochet ; **24 liaisons strictes, soit 1,71 pour 100 mots**. La question centrale et le plan restent avant/vers 30 secondes. Les timecodes de `script.md` sont recalculés ; le téléprompteur reprend cette version avec nombres en chiffres et coupures de souffle. Le « les leurs » du disclaimer est conservé pour respecter la formulation demandée dans le prompt.
