# Qwen 27B sur 8 Go : plus rapide, mais à quel prix ?

Version 3 du 18/11/2026, corrigée après `grill-v3.md` (B1, B2, I1 à I9, détails). Sortie : lundi 23 novembre 2026. V2 dans `script-v2.md`, V1 dans `script-v1.md`. Seule source de faits : `sources.md` (F1 à F17 ; M2 = `recherche-mesures.md`).

**Production :** vidéo calculée et documentaire. Aucun essai de l'auteur, aucune manipulation de LM Studio à filmer.

**Voix : 1197 mots (`wc -w` du téléprompteur), soit 8:20 à 145 mots/min** (environ 9 min avec les nombres lus en lettres). **Liaisons strictes : 20, soit 1.65 pour 100 mots** (donc, du coup, en fait, sauf que, par contre, voilà, en gros). Aucun crochet.

| Partie | Début | Mots |
|---|---:|---:|
| Le résultat | 0:00 | 28 |
| L'aveu et la question | 0:12 | 46 |
| Le plan | 0:31 | 56 |
| Ce que les secondes changent | 0:54 | 136 |
| Pourquoi ça va plus vite | 1:50 | 163 |
| Le premier prix : la place | 2:58 | 265 |
| Le deuxième prix : la qualité | 4:47 | 248 |
| Et dans LM Studio ? | 6:30 | 65 |
| Le verdict par usage | 6:57 | 183 |
| Fin | 8:12 | 19 |

## Voix

### Le résultat

[VISUEL : deux barres 3,2 → 18 tok/s. « Mesure publiée, 13/11/2026, GTX 1080 Ti limitée à 8 Go, llama.cpp ». F2]

Sur une carte de 8 gigas, tu changes un seul fichier,
et Qwen 27B passe de 3,2 à 18 tokens par seconde.
Même modèle, même carte, rien acheté. [F2]

### L'aveu et la question

Sauf que c'est une seule mesure publiée,
sur une GTX 1080 Ti limitée à 8 gigas.
Du coup, la vraie question :
qu'est-ce que ce fichier te fait perdre en échange ? [F2]

### Le plan

[VISUEL : trois livrables à l'écran, puis « 9 fois sur 10 ? » en suspens. F4]

Dans cette vidéo, on va voir
comment ce fichier fait tout tenir dans 8 gigas,
ce qu'il te coûte en mémoire de conversation,
et ce qu'il te coûte en qualité.
Et reste jusqu'à la fin :
il y a un travail que ce fichier rate presque 9 fois sur 10,
dans les tests de ceux qui le fabriquent. [F4 : 100 − 12,8 = 87,2 % d'échecs]

### Ce que les secondes changent

[VISUEL : « exemple théorique : 500 tokens, vitesse constante ». 500 ÷ 3,2 = 2 min 36 ; 500 ÷ 18 = 28 s. F16]

D'abord, ce que ça change en vrai.
Prends une réponse de 500 tokens.
À 3,2 tokens par seconde, tu attends 2 minutes 36.
À 18, c'est 28 secondes.
Juste une division, mais ça donne l'idée. [F16]

Du coup, cet écart change ta façon de parler à l'IA.
Quand chaque réponse prend 2 minutes et demie,
tu n'oses plus demander une précision.
Tu prépares un gros pavé pour éviter les allers-retours.
À 28 secondes, tu peux relancer, corriger.
Ça redevient une discussion.

Par contre, ce gain ne touche que l'écriture.
Avant d'écrire, le modèle lit ta demande,
et cette lecture reste à peu près la même avec les 2 fichiers.
Et s'il réfléchit avant de répondre,
cette réflexion, ce sont aussi des tokens à écrire.
Une réponse courte à l'écran
peut donc cacher beaucoup plus de travail derrière. [F2 (lecture similaire), F16 (réflexion exclue)]

### Pourquoi ça va plus vite

[VISUEL : schéma ancien fichier RAM + GPU, puis nouveau tout GPU. F2, M2]

Mais alors, d'où vient ce gain ?
L'ancien fichier ne tenait pas dans la carte.
Une partie tournait dans la RAM du PC, avec le processeur.
Et la carte passait son temps à l'attendre.
En gros, c'est un cuisinier dont la moitié des ingrédients
est dans une autre pièce :
il a beau être rapide,
il passe son temps à courir chercher ce qui lui manque. [F2, M2 (33/65 couches sur le GPU)]

[VISUEL : page Hugging Face, nom complet Qwen3.8-27B-UD-IQ2_XS.gguf, 7,63 GB. F1]

En fait, le nouveau fichier, lui, tient entièrement dans la carte.
Il s'appelle UD-IQ2_XS, il fait 7,63 gigas,
et Unsloth l'a mis à jour le 11 novembre.
Le nom complet est à l'écran. [F1, M2]

Sauf que pour rentrer, le modèle a dû maigrir.
Ses nombres sont rangés avec moins de précision :
c'est la quantification.
Le modèle garde son nom,
mais il ne répond plus tout à fait pareil. [F1]

Au passage, le MTP,
le module qui doublait la vitesse dans la vidéo précédente,
est laissé de côté dans cette mesure, faute de place.
Ce 18, c'est sans lui. [F17]

### Le premier prix : la place

Voilà ce que t'as gagné.
Maintenant, ce que ça te coûte.
Et le premier prix, c'est la place.

[VISUEL : carte de 8 Go découpée « poids / conversation / moteur / bureau », proportions illustratives. F9]

Le fichier fait 7,63 gigas, ta carte en a 8.
Sauf que le modèle n'est pas seul dans la carte.
Le moteur a besoin d'espace pour travailler,
ton bureau en prend aussi,
et surtout, il faut garder la conversation quelque part.
La taille du fichier ne te dit donc pas
combien de discussion il te reste. [F9]

Cette mémoire de la conversation, c'est le cache KV.
Dans la mesure, avec un cache en 8 bits,
il reste environ 14 000 tokens.
Ta demande et tout ce que le modèle écrit, sa réflexion comprise,
se partagent cette place.
Pour discuter, c'est correct.
Pour coller un long document, ça part vite. [F3, F16]

Et la bonne nouvelle, c'est que ça tient la vitesse.
Avec presque 14 000 tokens dedans,
l'écriture est encore à 15 tokens par seconde. [F2 (15,3 à 13,8K, cache 8 bits)]

[VISUEL : deux cartes séparées « cache 8 bits : ≈14K, 15,3 tok/s à 13,8K » et « cache 4 bits : ≈22,5K, 11,6 tok/s plein ». Pas une courbe d'un seul réglage. F2, F3]

Tu peux aussi compresser ce cache encore plus, en 4 bits.
Là, celui qui a mesuré monte à environ 22 500 tokens.
Par contre, avec ce cache 4 bits plein,
l'écriture tombe autour de 12 tokens par seconde.
C'est un autre réglage, avec son propre prix. [F3 (11,6, cache 4 bits plein)]

Et quand il a rempli la mémoire au-delà de 24 000 tokens,
ça a planté.
Le modèle se charge,
c'est la discussion qui finit par ne plus rentrer. [F3]

Pour des échanges courts, tu ne vois même pas cette limite.
Sauf que pour une longue session,
avec des fichiers et un historique,
c'est elle qui commande.

Si cette vidéo t'aide à voir ce que ta carte peut vraiment faire,
abonne-toi.

### Le deuxième prix : la qualité

[VISUEL : « Campagne Unsloth, 11/11/2026 — 128K / 256K de contexte, réflexion xhigh ». F4]

Le deuxième prix, c'est la qualité.
Et là, les chiffres viennent d'Unsloth, ceux qui fabriquent le fichier.
C'est leur campagne de tests, pas une vérification indépendante.
Et leurs tests tournent avec une très longue conversation
et la réflexion poussée au maximum.
Rien à voir avec une carte de 8 gigas.
Ces scores montrent où ça casse,
ils ne te donnent pas ton taux de réussite à toi. [F4]

[VISUEL : graphique LiveCodeBench, « lecture arrondie ». F4]

Sur LiveCodeBench, des exercices de programmation,
le modèle complet, sans compression, est autour de 89,
le petit fichier autour de 85.
Franchement, pour un modèle compressé à ce point, il tient bien. [F4 (88,62 annoté ; ≈84,5 lu)]

Alors, à ton avis, ça tient aussi
quand on lui confie un vrai projet ?

[VISUEL : DeepSWE : 40 / 13 / 36, modèle complet / petit fichier / ancien fichier. F4]

Sur leur test d'agent,
où le modèle travaille seul dans un dépôt de code,
le modèle complet réussit environ 40 % des tâches.
Le petit fichier, environ 13 %.
Là, ça dégringole.
Et l'ancien fichier, celui qui tournait à 3,2 tokens par seconde,
reste autour de 36 %.
Donc sur ce travail-là,
le petit fichier réussit 3 fois moins souvent que le modèle complet. [F4 (40,40 annoté ; ≈12,8 et ≈36 lus ; 40,4/12,8 ≈ 3,2)]

En fait, quand tu lui demandes d'aider sur une fonction,
tu lis sa réponse, et tu juges toi-même.
Un agent, lui, enchaîne les décisions tout seul,
il modifie plusieurs fichiers,
et une erreur au début se paie à toutes les étapes d'après.

Le compteur du début ne suffit plus, du coup.
Une réponse en 28 secondes que tu dois réparer
peut te coûter plus cher qu'une réponse lente qui marche.

### Et dans LM Studio ?

[VISUEL : tableau tiré de la doc LM Studio : déchargement GPU / contexte / cache K-V / réflexion. F5–F7]

Et si tu es sur LM Studio ?
Sa documentation a les mêmes réglages :
la part du modèle sur la carte, la taille de la conversation,
et le cache en 8 ou en 4 bits.
Sauf que toutes ces vitesses ont été mesurées dans llama.cpp,
pas dans LM Studio.
Et l'option pour couper la réflexion
dépend de la façon dont le modèle est configuré. [F5, F6, F7, F2]

### Le verdict par usage

[VISUEL : trois profils, conclusions tirées des mesures publiées. F2, F4, F10]

Alors, verdict.

Pour discuter, te faire expliquer un truc :
c'est le bon fichier.
Dans la mesure, le modèle tient en entier dans les 8 gigas,
et il écrit plus de 5 fois plus vite.
Tant que la conversation reste courte, la place suffit. [F2, F14 (5,625 à vide ; 5,1 à 13,8K)]

Pour te faire aider sur un bout de code :
dans leurs tests, les exercices de programmation tiennent bien.
Par contre, tu relis tout,
et tu ne lui donnes pas tout ton projet d'un coup. [F4, F10]

Pour un agent qui travaille seul sur un projet entier :
garde l'ancien fichier, quitte à attendre à 3,2 tokens par seconde.
Parce que dans leurs tests, le petit fichier rate presque 9 fois sur 10.
L'ancien, à peu près 2 fois sur 3.
Aller plus vite pour se tromper plus souvent, ça sert à rien. [F2, F4 (87,2 % et 64 % d'échecs)]

Alors, ce que ce fichier te fait perdre, tu le sais maintenant :
pour discuter, un peu de place et un peu de qualité.
Pour un agent, beaucoup trop.
Donc la même carte de 8 gigas peut faire 2 métiers différents,
selon le fichier que tu lui donnes.

### Fin

Jeudi, on regarde les cartes par budget,
pour voir ce que plus de mémoire t'apporte vraiment.
Allez, salut ! [F15]

## Notes

- Aucun crochet ; l'ancien « avis personnel » est supprimé sans remplacement.
- Un seul renvoi dans le corps (MTP, « la vidéo précédente », F17) et l'annonce de jeudi 26/11 (F15).
- « Presque 9 fois sur 10 » = 87,2 % d'échecs, « 2 fois sur 3 » = 64 %, lectures graphiques Unsloth (F4), toujours attribués à « leurs tests ».
- « Plus de 5 fois plus vite » reste rattaché à « dans la mesure » (F14) ; aucun ×5 général.
