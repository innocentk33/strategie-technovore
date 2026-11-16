# Qwen 27B sur 8 Go : plus rapide, mais à quel prix ?

Nouvelle V1 documentaire du 16/11/2026, après clarification du format. Sortie : 23 novembre. Durée cible : 8–10 min à 145 mots/min. Ancienne version conservée dans `archive-avant-recentrage/`. Sources : `sources.md`. Méthode : `ressources/skills-gpt/youtube-script-et-hook.md`, puis grill storytelling indépendant.

**Production :** voix ou face caméra, extraits de sources publiques, graphiques et schémas. Tous les essais évoqués sont ceux des sources. Aucun logiciel à ouvrir, aucun modèle à télécharger, aucun test ni capture personnelle à fournir par l'auteur. Les visuels sont des consignes de montage documentaire, pas des démonstrations à reproduire.

**Voix : 1396 mots, soit 9:38 à 145 mots/min**, hors pauses et crochet facultatif. **Liaisons strictes : 21, soit 1.50 pour 100 mots**. Liste : donc, du coup, en fait, sauf que, en effet, par contre, voilà pourquoi, voilà comment. Timecodes indicatifs à recaler au montage.

| Partie | Début | Mots |
|---|---:|---:|
| Le résultat et le prix caché | 0:00 | 61 |
| Le plan | 0:25 | 38 |
| Ce que les secondes changent | 0:41 | 261 |
| Le modèle rentre, mais il a changé | 2:29 | 215 |
| La qualité ne baisse pas partout pareil | 3:58 | 279 |
| La place qui manque après le chargement | 5:53 | 239 |
| Ce que ça signifie dans LM Studio | 7:32 | 131 |
| Le verdict par usage | 8:26 | 172 |

## Voix

### Le résultat et le prix caché

[VISUEL : deux barres 3,2 et 18 tokens/s. Attribution : mesure publiée, 13/11/2026, GTX 1080 Ti limitée à 8 Go, llama.cpp. F2]

Sur une carte limitée à 8 gigas, un testeur change de fichier.
Qwen 27B passe de 3,2 à 18 tokens par seconde pour écrire sa réponse.
Ces chiffres sont les leurs, je n'ai rien testé chez moi.
Sauf que le petit fichier perd aussi des capacités.
Du coup, qu'est-ce que tu gagnes vraiment, si tu gardes ta carte de joueur ?

### Le plan

On va traduire cette vitesse en temps d'attente, regarder ce que le fichier perd en qualité et combien de conversation il peut garder.
À la fin, tu sauras pour quel usage le plus lent reste le meilleur choix.

### Ce que les secondes changent

[VISUEL : calcul affiché, « exemple théorique : 500 tokens générés, vitesse constante, hors lecture et démarrage ». 500 ÷ 3,2 et 500 ÷ 18. F16]

Pour 500 tokens à écrire, ça donne environ 2 minutes 36 contre 28 secondes.
C'est une division des vitesses publiées, pas un chronomètre lancé chez moi.
Et un token, c'est un morceau de texte, pas forcément un mot entier.
Donc on compare la même quantité à écrire, sans prétendre que toutes les réponses ont cette longueur.

L'écart peut changer la façon de discuter avec l'IA.
Quand chaque relance prend longtemps, demander une précision devient pénible.
Tu finis par préparer un gros message pour éviter les allers-retours.
Une écriture plus rapide rend les échanges courts moins laborieux.
Voilà l'intérêt pour quelqu'un qui veut comprendre une erreur ou retravailler un paragraphe.

Sauf que ces secondes commencent après la lecture de la demande.
Le logiciel doit d'abord lire ton texte, puis produire sa réponse.
Dans l'essai publié, la lecture reste du même ordre avec les deux fichiers. [F2]
Donc le gain ne raccourcit pas de la même façon toute l'attente.
Et si le modèle produit une longue réflexion avant sa réponse, il doit aussi écrire cette réflexion.

[VISUEL : « lire la demande → générer », avec réflexion et réponse dans le second bloc. Aucun faux chat animé. F2, F7]

Mais il y a une limite plus importante : ce résultat vient d'une seule machine.
Le testeur utilise une GTX 1080 Ti dont il réserve une partie de la mémoire pour se rapprocher d'un budget de 8 gigas. [F2]
On n'a pas trouvé de deuxième reproduction du nouveau fichier sur une vraie carte de 8 gigas. [F11]
Du coup, les 28 secondes illustrent son débit, elles ne prédisent pas celui de ton PC.

Ce qu'on peut expliquer, en revanche, c'est pourquoi changer de fichier fait un tel écart chez lui.

### Le modèle rentre, mais il a changé

[VISUEL : schéma ancien fichier partagé RAM/GPU, puis nouveau fichier tout GPU. Encadré nom et taille sur page Hugging Face. F1, F2]

L'ancien fichier travaille en partie dans la RAM du PC.
Le nouveau tient entièrement sur la carte dans son essai. [F2]
En fait, c'est comme un cuisinier qui a enfin tous ses ingrédients sur son plan de travail.
Il peut avancer sans attendre ce qui se trouve dans l'autre pièce.

Le fichier s'appelle UD-IQ2_XS, pour Qwen 3.8 27B.
Hugging Face affiche 7,63 gigas, et Unsloth annonce cette mise à jour le 11 novembre. [F1]
Le nom complet est à l'écran, avec la source en description.

Donc la carte n'a pas gagné de mémoire : la copie du modèle prend moins de place.
Pour y arriver, certains nombres sont stockés avec moins de précision.
C'est ce qu'on appelle la quantification.
Le modèle garde son nom, mais ses réponses peuvent changer.

Et le MTP de la vidéo précédente reste désactivé dans cet essai, pour garder de la place. [F2]
Ici, le gain vient du nouveau fichier et de son chargement complet sur la carte.
On ne peut pas empiler les gains des deux vidéos comme des bonus d'équipement.

Si ces comparaisons t'aident à comprendre ce que ton PC peut faire, abonne-toi.

Sauf que jusqu'ici, on a seulement compté la vitesse.
Une réponse produite en 28 secondes peut être une mauvaise affaire si elle te donne davantage de travail à corriger.

### La qualité ne baisse pas partout pareil

[VISUEL : graphiques Unsloth, 11/11/2026. LiveCodeBench puis DeepSWE ; annotations et lectures arrondies distinguées. F4]

Sur les exercices de programmation de LiveCodeBench, les scores publiés par Unsloth restent assez proches.
Le modèle complet est autour de 89, le petit fichier autour de 85, en lecture arrondie du graphique. [F4]
Donc il ne s'effondre pas sur toutes les tâches parce qu'il est plus compressé.

Mais dès qu'il faut travailler dans un vrai dépôt de code, leur autre test raconte une histoire différente.
Le modèle complet réussit environ 40 % des tâches.
Le petit fichier, environ 13 %.
Et le fichier 4 bits de leur graphique reste autour de 36 %. [F4]
Là, l'écart se voit même sans sortir la calculatrice.

[VISUEL : changement de cadrage ; garder uniquement 40 / 13 / 36 et les trois variantes. Mention « campagne Unsloth, pas test indépendant ».]

En fait, demander une aide sur une fonction et confier tout un projet à un agent, ce sont des travaux très différents.
Dans le premier cas, tu peux lire la proposition et juger si elle t'aide.
Dans l'autre, les décisions s'enchaînent, avec des modifications à suivre dans plusieurs fichiers.
Une erreur peut entraîner du travail supplémentaire derrière.

Donc le compteur du début ne suffit plus.
Finir d'écrire plus vite ne veut pas forcément dire finir le travail plus vite.
Pour quelqu'un qui attend une explication, le gain peut compter.
Pour quelqu'un qui délègue un projet entier, les échecs supplémentaires peuvent coûter bien plus que l'attente économisée.

Par contre, ces chiffres sont ceux d'Unsloth, qui fabrique le fichier.
Et leurs évaluations utilisent de grands contextes, avec une réflexion élevée. [F4]
Elles ne mesurent pas exactement l'usage limité à 8 gigas dont on parle ici.
Donc elles signalent un risque, elles ne donnent pas un taux de réussite pour ton travail à toi.

Et même une réponse correcte peut être inutilisable si la conversation manque de place avant la fin.

### La place qui manque après le chargement

[VISUEL : schéma « poids / conversation / travail du moteur / autres usages ». Proportions illustratives, sans soustraire des unités incompatibles. F9]

Le fichier de 7,63 gigas doit partager la carte avec autre chose.
Le moteur a besoin d'espace pour travailler et conserver la conversation.
Le bureau peut aussi en occuper. [F9]
Du coup, la taille du téléchargement ne dit pas combien de discussion il reste.

Cette mémoire de conversation, c'est le cache KV.
Dans le même essai, un cache en 8 bits laisse environ 14000 tokens de contexte. [F3]
Ta demande, l'historique et ce que le modèle génère occupent cette fenêtre.
Donc plus la conversation grossit, moins il reste de place pour la suite.

Sauf qu'on peut aussi compresser cette mémoire.
Le testeur rapporte environ 22500 tokens avec un cache en 4 bits.
Mais quand cette fenêtre est remplie, son débit tombe autour de 12 tokens par seconde. [F3]
Les 18 du début correspondent à une conversation vide.
Voilà pourquoi une seule vitesse affichée raconte mal une longue session.

[VISUEL : retour aux barres du début ; ajouter « contexte vide » sous 18 et une carte séparée « cache 4 bits plein : ≈12 ». Conditions différentes, pas courbe d'un seul réglage. F2, F3]

Et il rapporte un plantage quand il pousse le contexte trop loin. [F3]
Le modèle se charge, mais la conversation finit par dépasser la mémoire disponible.
C'est le genre de détail qui disparaît derrière un joli « ça tourne sur 8 gigas ».
Ça tourne, oui, dans une enveloppe précise.

Du coup, pour des échanges courts, cette limite peut rester discrète.
Pour une longue session avec des documents et un historique à conserver, elle devient centrale.
Le fichier qui rentre apporte une possibilité de plus, mais il ne transforme pas la carte en modèle supérieur.

### Ce que ça signifie dans LM Studio

[VISUEL : tableau documentaire tiré de la documentation : chargement GPU / contexte / cache / réflexion. Aucun écran à capturer chez l'auteur. F5–F7]

Si tu utilises LM Studio, tu retrouves les mêmes questions de fond.
Combien du modèle tient sur la carte, et quelle place reste pour la conversation.
Sa documentation décrit les réglages de chargement et de contexte, ainsi que les contrôles de cache. [F5, F6]

Mais les mesures qu'on vient de voir ont été faites avec llama.cpp.
On ne peut pas leur coller une étiquette LM Studio et annoncer le même résultat.
Le principe aide à comprendre le compromis ; le débit exact reste celui de l'essai publié.

Et couper la réflexion pour économiser du contexte change encore les conditions.
Les scores de qualité qu'on a montrés ont été obtenus avec une réflexion élevée. [F4, F7]
Donc on ne peut pas prendre la vitesse d'une configuration et lui ajouter la qualité d'une autre.
Faut pas abuser.

### Le verdict par usage

[VISUEL : trois profils, conclusions issues des mesures, pas tests d'usage réalisés par l'auteur. F4, F10]

Pour discuter brièvement ou demander une explication, ce fichier ouvre une piste intéressante : le modèle peut tenir sur la carte, avec une écriture nettement accélérée dans l'essai publié.
La qualité de ces usages précis reste à confirmer indépendamment.

Pour de l'aide sur un fichier de code, le résultat proche sur les exercices de programmation est encourageant.
Sauf que ça reste une proposition à relire, avec un contexte limité.

Pour un agent chargé d'un projet entier, le fichier moins compressé garde un avantage net dans les tests d'Unsloth.
Donc le plus lent peut être le choix le plus utile.
C'est le compromis que les 18 tokens par seconde ne montraient pas au début.

[CROCHET : ton avis personnel sur ce compromis, en une ou deux phrases. Aucun essai ni vécu à inventer. Le texte tient sans cet avis.]

La même carte peut rendre un autre service selon le fichier et le travail demandé.
Mais quand la qualité ou la place pour la conversation deviennent le blocage, gagner en vitesse ne suffit plus.
Jeudi, on compare les cartes par budget et leurs prix affichés en France, pour voir ce qu'acheter plus de mémoire apporte vraiment. [F15]
Allez, salut !

## Crochets et questions

- Un seul crochet facultatif : avis de l'auteur. Aucun manque factuel reporté sur lui.
- Aucune manipulation ni capture LM Studio nécessaire pour tourner cette vidéo.
- Aucune question bloquante : format calculé confirmé par l'auteur, référence SimplyExplain.

## Notes de méthode

Structure : explication documentaire portée par l'avant/après, puis l'objection la plus forte (qualité), le budget de conversation, et le verdict. L'auteur interprète les preuves publiées ; aucun parcours d'essai personnel. Le calcul de durée est une illustration, pas une nouvelle mesure.

Les références méthodologiques retention-scripting-guide.md et algorithm-guide.md ont été retrouvées dans le dossier local claude-youtube et lues. Leurs statistiques générales de rétention ne servent ni de faits dans la voix ni de promesses de résultat. Les règles explicites de l'auteur priment : 145 mots/min, résultat avant 15s, disclaimer avant30s, plan après question centrale, pas de longue introduction générique.
