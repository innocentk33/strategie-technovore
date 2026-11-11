# Vidéos de référence : tester Strata sur un PC de joueur

> Recherche du **11/11/2026** (yt-dlp : recherche YouTube, métadonnées et sous-titres automatiques lus le jour même). Vues relevées le 11/11. **Seules les 5 meilleures sont gardées** ; les autres sont listées plus bas avec la raison. Pour la structure à suivre, voir aussi la référence de la fiche : Red Stapler, *I ran Qwen3.8 27B on single 8GB Card!* (https://www.youtube.com/watch?v=ye50BbXEczo, 764 K vues, 24/08/2026), lue en sous-titres le 11/11.
>
> **Limites** : transcriptions lues en sous-titres automatiques (erreurs de chiffres et de noms, ex. « Qwen 2.5 » pour 3.8) ; l'accès YouTube a renvoyé des erreurs 429 par moments, je n'ai donc pas pu lire toutes les transcriptions en entier. Pour la langue, je me suis fié au champ `language` de la vidéo, pas au titre : **les titres français de la recherche sont souvent traduits automatiquement** (ex. la vidéo de Red Stapler apparaît avec un titre français alors que la voix est anglaise).

## Ce qu'on retient pour la nôtre

- **Aucune vidéo ne fait exactement notre test** : Strata, **Coder**, **RTX 5080**, **32 Go de RAM**, jeu + site + 3D, avec la comparaison à Claude. La plus proche (n° 1) est faite sur 12 Go de VRAM, sans les trois démos.
- **Vidéos françaises** : la recherche du 05/11 n'en avait pas trouvé ; **le 11/11 j'en trouve deux** (n° 4 et n° 5), mais aucune ne teste du code généré. Le créneau « test filmé de Strata en français, avec du vrai code » reste libre.
- **La structure de Red Stapler reste la meilleure base** : résultat tout de suite, plan à 0:15, puis la config, les essais, la comparaison avec Opus.

## Les 5 gardées

### 1. NoCodeAbode : le plus proche de notre machine (le Coder sur 32 Go)

- **Titre** : *How Good Is Strata's Qwen Coder on 32GB RAM? (The Brutally Honest Test)*
- **Chaîne** : NoCodeAbode · **6 min 30** · **40 536 vues** · **02/10/2026** (relevé 11/11)
- **URL** : https://www.youtube.com/watch?v=xze2CeR2Zu0
- **Machine** : 32 Go de RAM, carte de 12 Go.
- **Ce que sa structure fait bien**
  - **0:00** : « Je n'ai que 32 Go de RAM », puis l'enjeu : « la page dit 32 Go : prends le Coder, la moitié du modèle ». **0:30** : « Personne ne l'a lancé sur une carte comme la mienne. Alors je l'ai fait », avec la promesse qu'il a réussi la tâche que le 27B a ratée trois fois.
  - **1:00 : trois questions précises** (« qu'est-ce que ça me coûte sur 32 ? À quelle vitesse ? Peut-il faire du vrai travail ? »), plus « une de ces réponses n'est pas celle que j'espérais » : le défi et une tension.
  - Il montre **les accrocs** (téléchargement de 58 Go, 87 Go sur le disque ; le mode rapide ne tient pas en RAM, bascule en mode lent) au lieu de les cacher, puis le tok/s par type de tâche (8,7 en chat, 41 à 46 sur du code), la RAM libre qui tombe à 49 Mo.
  - **Six tâches identiques** pour le Coder, le 27B et Opus, notées « passe / partiel / raté » : 5 / 1 / 0 pour le Coder. Une grille simple, comme la nôtre.
  - Il termine par « à qui cette vidéo ne s'adresse pas » et rappelle « une exécution par tâche, réflexion coupée : chez toi ça peut changer ».
- **À reprendre** : les trois questions à 1:00, les accrocs montrés, la grille de verdict, le « pour qui ce n'est pas ».
- **À éviter** : il n'affiche pas ses résultats avant 3:30 ; chez nous, les trois démos passent d'abord.

### 2. Zero to MVP : trois tâches de code sur 16 Go (horloge, éditeur de pixels, pyramide 3D)

- **Titre** : *A 125B Local Model on a 16GB GPU: Fast, But Is It Smart?*
- **Chaîne** : Zero to MVP · **7 min 13** · **74 500 vues** · **05/10/2026**
- **URL** : https://www.youtube.com/watch?v=B77LasklmZU
- **Machine** : RTX 4060 Ti 16 Go, **128 Go de RAM** (donc pas la nôtre), agent Pi.
- **Ce que sa structure fait bien**
  - Plan clair en chapitres : comment ça tient (1:15, deux phrases d'explication, « assez de théorie, passons à la pratique » à 1:30), vitesse mesurée (≈ 65 tok/s par script), puis **trois tâches par difficulté croissante** : la plus facile (« vérifier que ça marche chez moi »), la moyenne (5 min 20, réussie du premier coup, « je ne m'y attendais pas »), la difficile (échec honnête, « il a bien essayé »).
  - Il montre la charge système pendant la génération (le GPU plein, environ 40 Go de RAM, la moitié du CPU).
  - Conclusion sobre : « premières impressions très positives, je continue les tests ».
- **À reprendre** : l'échelle de difficulté facile → moyen → difficile, l'échec raconté sans drame, la charge système montrée.
- **À éviter** : théorie à 1:15 avant toute démonstration ; première démo à 3:45 ; **128 Go de RAM** : ne pas présenter ses chiffres comme les nôtres.

### 3. Red Stapler : la même chaîne que notre modèle de structure

- **Titre** : *I run 177B model on SSD (It's Fast!) | Qwen 3.8 Flash Next Test*
- **Chaîne** : Red Stapler · **3 min 46** · **191 348 vues** · **17/09/2026**
- **URL** : https://www.youtube.com/watch?v=_TCRH725hAM
- **Machine** : deux cartes économiques (24 Go de VRAM au total) + 32 Go de RAM, llama.cpp sous Linux.
- **Ce que sa structure fait bien**
  - **0:00 : le résultat et le contraste** : « 24 Go de VRAM, 32 Go de RAM, et on va lancer un modèle de 85 Go, presque le double de ma mémoire : 22 tokens par seconde ». **0:15** : la promesse en un chiffre.
  - Puis le contexte en 30 s, les réglages montrés, les mesures (22 tok/s, 14 à long contexte, et la baisse de 20 % sous Windows), la conclusion en une phrase.
- **À reprendre** : le chiffre en tête, le contraste « plus gros que ma mémoire », la franchise sur Windows.
- C'est aussi la chaîne de la vidéo de référence de la fiche (*I ran Qwen3.8 27B on single 8GB Card!*, 764 K vues, 24/08) : **résultats → config → essais → comparaison avec Opus**.

### 4. Nathan Inline (français) : la vitesse montrée en 60 secondes

- **Titre** : *QWEN 3.8 FLASH NEXT : Enfin utilisable sur 16GB VRAM !*
- **Chaîne** : Nathan Inline · **14 min 47** · **22 205 vues** · **06/10/2026** · langue de la vidéo : `fr-FR`
- **URL** : https://www.youtube.com/watch?v=cxvI2lqSC6w
- **Ce que sa structure fait bien**
  - À **0:50**, il dit « regardez la vitesse », tape « Hi, how are you? » puis « raconte-moi une histoire » : le tok/s (≈ 60) et la vitesse de lecture du prompt (> 900) sont lisibles à l'écran en 15 s. **C'est le plan P10 de notre plan de tests.**
  - Il rattache la vidéo à ses deux précédentes (« de 5 tok/s inutilisable à 30 »), comme nous le faisons avec le 02/11 et le 09/11.
- **À éviter** : 50 secondes de rappel avant le premier résultat ; une vidéo de 15 minutes sans test de code.
- *Lu en sous-titres automatiques traduits en anglais (la piste française n'était pas disponible) : les chiffres sont à revérifier à l'écran avant de les citer.*

### 5. Build & Mind (français) : le résultat en 15 s, puis « dans cette vidéo »

- **Titre** : *Les géants de l'IA veulent votre RAM : ce qu'un vieux PC fait VRAIMENT tourner (Qwen, RTX 5060 Ti)*
- **Chaîne** : Build & Mind · **17 min 36** · **4 607 vues** · **10/11/2026** · langue : `fr`
- **URL** : https://www.youtube.com/watch?v=9IRXDZpU1mQ
- **Ce que sa structure fait bien**
  - **0:00 : un résultat qui surprend** : la voix d'une personnalité, doublée en français, avec l'annonce « traduit, doublé et sous-titré chez moi par une IA, en local, sur une carte de 16 Go ». À 0:30 il pose la **question centrale**, à 1:00 sa promesse (combien coûte un PC de récupération pour faire ça) et la structure en deux vidéos.
  - Description avec un **plan de livrables chiffré** (trois paniers de prix, le mur des 16 Go, Strata face à llama.cpp, le verdict) : un modèle de ce que nous voulons annoncer vers 0:30.
- **À éviter** : 17 minutes, nettement plus long que les 8 à 10 de notre vidéo ; peu de vues (4,6 K en 1 jour).
- **Attention** : cette vidéo parle d'un *autre angle* (le prix d'un PC d'occasion pour l'IA) : ne pas reprendre son visuel.

## Vues et non retenues

| Vidéo | Chaîne · vues · date | Pourquoi pas |
|---|---|---|
| *RTX 5090 + Strata – Can Local AI REALLY Beat Opus 4.6?* (https://www.youtube.com/watch?v=5F4wdtNbMt4) | Bijan Bowen · 86 985 · 16/10 | Une comparaison avec Opus 4.6 existe (chapitre à 19:37), mais l'ouverture passe 90 s sur du matériel prêté par un fabricant ; 26 min ; RTX 5090 |
| *Strata Coder vs Qwen 3.8 Flash Next: 9 Real Tests* (https://www.youtube.com/watch?v=S5RmGAlXgvY) | Lukasz Gawenda · 10 700 · 25/10 | 28 min ; contient un **test 3D voxel** (château de Wawel) et un test de physique : utile pour juger la difficulté du nôtre, trop long pour la structure |
| *Qwen 3.8 Flash Next vs Flash Next Coder* (https://www.youtube.com/watch?v=iE4aexQuzv0) | No place like localhost · 49 715 · 14/10 | 36 min ; deux défis de code comparés |
| *Qwen 3.8 27B vs Strata Coder - Local LLM battle* (https://www.youtube.com/watch?v=xiMAxAQAfC4) | Luke's Dev Lab · 88 460 · 23/10 | Déjà dans `sources.md` de *16 Go suffisent* (S35) ; 21 min, six tests ; seule vidéo trouvée avec « 16 Go + 32 Go de RAM » |
| *A 125B AI Model on a Gaming PC? Strata Tested on RTX 5090…* (https://www.youtube.com/watch?v=PJmC9w47_sg) | Stef from Samayas · 13 317 (05/11) · 06/10 | Claude Code branché sur Strata ; le Coder y a échoué (d'après la description, S35) ; RTX 5090 |
| *Is 16GB All You Need for Serious Local LLM?* | Kai · 511 821 (05/11) | Pas de Strata |
| *I Didn't See the Point of Strata. Then I Tested It.* (https://www.youtube.com/watch?v=a65dhPnjoAQ) | Manolo Remiddi · 29 694 · 03/11 | Non lu (pas de chapitres) |
| *Strata : faites tourner des modèles d'IA géants avec peu de VRAM !* (https://www.youtube.com/watch?v=K01jRME8tLs) | TheAIHobbyGuy · 3 483 · 07/11 | Tutoriel d'installation, l'audio est en anglais malgré le titre traduit |

## Verdict sur la structure à suivre

Il n'y a pas de bonne vidéo qui fasse nos trois démos sur ce matériel : **on suit la structure de Red Stapler**, enrichie de trois choses prises ici :
1. les **trois questions à 1:00** et les accrocs montrés de NoCodeAbode ;
2. l'**échelle de difficulté** (facile → moyen → difficile) de Zero to MVP ;
3. le **plan de vitesse propre** (« Hi », puis une histoire) de Nathan Inline.

Ce qu'on ne fait pas : 50 secondes de rappel, 90 secondes de présentation de matériel, ni théorie avant la première démo.
