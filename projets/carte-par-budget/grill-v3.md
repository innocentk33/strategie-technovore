# Grill de la V3 : carte à 600 € pour l'IA (débit mémoire)

Relecture du 18/11/2026, variante storytelling du skill `youtube-script-grill`. Fichiers lus : `teleprompteur.txt` (= `.md`), `script.md` (V3), `tableau-offres.md`, `sources.md`, les trois fichiers de `recherche/`, `.claude/rules/script.md`, et le téléprompteur de `qwen-27b-8go` comme référence de ton. Pages rouvertes sur le web le 18/11 au soir (compte rendu en fin de fichier). Rien n'a été modifié ailleurs.

## Note : 6/10

Le fond est solide : tous les prix dits en voix se retrouvent sur les fiches rouvertes, les débits et les dates tiennent, le motif « ligne 1 / ligne 2 » se plante et se récolte bien, et l'image du livre est claire. Mais quatre choses empêchent de tourner tel quel :
1. le plan tombe à 47 s ;
2. le contraste « jeu contre IA » du hook n'est pas sourcé ;
3. le Qwen 27B « dans 8, encore moins » contredit ta vidéo précédente ;
4. le verdict ne dit pas pourquoi la RTX 3060 plutôt que l'Arc B580, alors que la règle que tu viens d'enseigner désigne la B580.

---

## Test des 30 secondes

Débit : 145 mots/min, nombres comptés comme un mot (donc en vrai un peu plus lent).

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-12 s (30 mots) | > « Tu t'apprêtes à mettre 600 euros dans une carte graphique, / parce que c'est bientôt le Black Friday, / et tu veux faire tourner une IA chez toi ? / Alors regarde ça. » | 🟠 Le clic est confirmé et le « tu » arrive dès le premier mot, c'est bien. Par contre, il n'y a aucune tension pendant 12 s, et « Alors regarde ça » est un pont vide. Dans la référence Qwen 27B, le résultat est **fini à 9 s**. |
| 12-27 s | > « Dans une série de mesures publiées, même testeur, même modèle, / une RTX 3060 sortie en 2021 / écrit plus vite qu'une RTX 4060 Ti 16 gigas sortie en 2023. / 42 tokens par seconde contre 34. » | 🟢 pour le contraste, qui est fort et juste. 🟠 pour la place : 10 mots de provenance passent avant la chute, et le chiffre ne tombe qu'à 26 s. La règle demande le meilleur moment dans les 15 premières secondes. |
| 27-45 s | > « En fait, la plus récente, celle qui a le plus de mémoire, / écrit moins vite. / Du coup, si tu choisis ta carte comme pour le jeu, / en prenant la mieux classée sur un comparateur de prix, / tu peux payer plus cher une IA plus lente. » | 🟠 La première phrase redit la précédente. La deuxième porte l'angle mais n'est pas sourcée (bloquant 2). La question centrale (« qu'est-ce qui fait écrire une IA vite ? ») n'est jamais posée en mots simples. |
| Plan, 47-70 s | > « Dans cette vidéo, on va voir / les 2 lignes de la fiche technique… » | 🔴 Il arrive 17 s après la cible des 30 s (référence Qwen 27B : plan à 25 s). Les livrables sont concrets, c'est bien. |
| Pont | > « D'abord, une autre série de mesures, encore plus parlante. » | 🟢 La première partie commence par un résultat, comme demandé. |

**Budget :** 115 mots avant le plan, soit environ 47 s. Il faut descendre à 75-80 mots.

**À couper :** « Alors regarde ça. » ; « Dans une série de mesures publiées » placé avant la chute ; « En fait, la plus récente, celle qui a le plus de mémoire, écrit moins vite. », qui redit le chiffre.

**Réécriture des 30 s** (81 mots ≈ 33 s, plan à 33 s ; à toi de reprendre avec tes mots) :

```
Tu t'apprêtes à mettre 600 euros dans une carte graphique au Black Friday,
pour faire tourner une IA chez toi ?
Regarde ça :
une RTX 3060, sortie en 2021,
écrit plus vite qu'une RTX 4060 Ti 16 gigas, sortie en 2023.
42 tokens par seconde contre 34, dans des mesures publiées.
Même testeur, même modèle.
La plus vieille, avec moins de mémoire, écrit plus vite.
Du coup, si tu prends juste la plus récente,
tu peux te retrouver avec une IA plus lente.
Dans cette vidéo, on va voir…
```

Si tu tiens à « comme pour le jeu » (c'est ton angle), garde-le, mais seulement après avoir ajouté une source de jeu (bloquant 2).

**Promesses du plan, tenues ou non :**

| Promesse | Où | Tenue ? |
|---|---|---|
| « les 2 lignes de la fiche technique » | 2:27 | Oui, et c'est le meilleur passage. |
| « pourquoi la RTX 4060 n'est pas l'affaire qu'elle a l'air d'être » | 4:49 à 6:20 | En partie. Le débit est plus bas et le prix d'occasion n'est pas meilleur, mais le passage finit sur trois réserves d'affilée (voir I-8). |
| « un chiffre que les sites n'affichent jamais » | 4:28 | Le calcul est tenu, mais « jamais » est faux (voir I-4). |
| « quelle carte prendre avec 600 euros » | 8:00 | Oui, mais le verdict a un trou : la B580 (bloquant 4). |

---

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Le titre implicite (600 €, Black Friday, IA) est tenu, mais trop tard pour le plan. |
| 2. Alignement | 🟢 | Tu veux éviter un mauvais achat au spectateur, et c'est ce que fait le script. |
| 3. Problème profond | 🟢 | La peur de se faire avoir par une « bonne affaire » est posée dès la 1re phrase et résolue au verdict. |
| 4. Public & complexité | 🟢 | Le calcul bus × fréquence ÷ 8 passe bien après l'image du livre. |
| 5. Valeur & originalité | 🟢 | La règle « mémoire d'abord, débit ensuite », preuves à l'appui, n'est pas dans les guides d'achat jeu. |
| 6. Structure | 🟠 | Bonne progression, mais la thèse « mémoire d'abord » n'est jamais montrée sur les cartes du hook. |
| 7. Histoire | 🟠 | Pas de crise, c'est normal pour un guide. Le seul retournement fort reste celui du hook. |
| 8. Mais / donc | 🟢 | « Sauf que pour écrire la réponse… Pareil. » est un vrai retournement. |
| 9. Engagement actif | 🟠 | Un seul « tu te souviens ? ». Le spectateur ne devine rien avant le verdict. |
| 10. Rythme & liaisons | 🟠 | 25 liaisons strictes sur 1 287 mots (1,94 pour 100), dont 4 creuses ; une liste de prix de 74 s. |
| 11. Tics d'IA | 🟠 | « C'est là que ça devient intéressant », « Pas le double, mais c'est énorme », « ce n'est pas une règle magique ». |
| S1. 30 premières secondes | 🔴 | Le plan arrive à 47 s ; pas de question centrale en mots simples. |
| S2. Pont | 🟢 | La série 4070 ouvre une deuxième question (« même débit, même vitesse ? »). |
| S3. Retournements | 🟢 | Environ un toutes les 30 à 40 s, sauf dans la liste de prix (6:34 à 7:48). |
| S4. Planté / récolté | 🟢 | « Reprends la série du début », « ses 29 % », « Ligne 1 d'abord, tu te souviens ? ». |
| S5. Personnage | 🟠 | Le spectateur et ses 600 € sont là au début, puis disparaissent jusqu'au verdict. |
| S6. Fin | 🟠 | Elle résume. Elle ne revient pas sur la 3060 du hook. |

---

## Bloquants

### B1. Le plan à 47 s, le résultat à 26 s
> « Tu t'apprêtes à mettre 600 euros… / Alors regarde ça. / Dans une série de mesures publiées, même testeur, même modèle, »

**Pourquoi ça coince :** ton cadre demande le plus fort dans les 15 premières secondes et le plan vers 30 s. Ici, le chiffre tombe à 26 s et le plan à 47 s. Ta vidéo de référence fait 9 s et 25 s.

**Correction :** la réécriture des 30 s ci-dessus. Elle garde le même contraste, place la provenance après la chute et coupe la redite.

### B2. « Comme pour le jeu, la mieux classée sur un comparateur, payer plus cher » : rien de tout ça n'est sourcé
> « Du coup, si tu choisis ta carte comme pour le jeu, / en prenant la mieux classée sur un comparateur de prix, / tu peux payer plus cher une IA plus lente. »
> « Voilà pourquoi le classement en jeu ne t'aide pas ici. / Il ne te dit ni combien de mémoire tu as, / ni à quelle vitesse elle se lit. »

**Pourquoi ça coince :**
- `sources.md` n'a **aucun** résultat de jeu pour la paire du hook (3060 / 4060 Ti 16 Go). F33 a même écarté l'opposition jeu/IA sur la paire 3060 Ti / 4060.
- Le seul comparateur lu (PX §4) met en tête la RTX 5070 : 12 Go et 672 de débit, ce qui n'est pas un piège pour l'IA.
- « Payer plus cher » n'a pas de prix français pour la paire du hook : la 4060 Ti 16 Go est introuvable en neuf. La page des mesures affiche 250 $ contre 409 $, mais en dollars et sans date.
- La phrase de 7:48 conclut un raisonnement que la vidéo ne fait jamais, puisqu'aucun classement en jeu n'est montré. Et beaucoup de comparateurs affichent bien la quantité de mémoire.

**Correction :** c'est ton angle, donc on le source, on ne le supprime pas.
- Ajoute une page de test multi-jeux, ouverte et datée, où la 4060 Ti (8 ou 16 Go) passe devant la 3060 12 Go. Dis-le alors en une phrase : « En jeu, la 4060 Ti passe devant. Pour l'IA, c'est l'inverse. » Je n'ai trouvé que des agrégateurs, non ouverts, aux écarts qui ne collent pas entre eux : ça ne vaut pas source.
- En attendant, appuie le contraste sur ce que tu as déjà : la carte la plus récente (dates F32) et la plus « musclée ». La page de la série 4070 donne la puissance de calcul : 29,15 TFLOPS pour la 4070, 40,09 pour la 4070 Ti, en FP16.
- Remplace « payer plus cher » par « te retrouver avec une IA plus lente ».
- Coupe 7:48 (« Voilà pourquoi le classement en jeu… »), ou remplace-le par la phrase de jeu sourcée.

### B3. Qwen 27B « Dans 8, encore moins » contredit ta vidéo précédente
> « prends la version compressée de Qwen 27B : / rien que son fichier fait 14,4 gigas. / Ça rentre dans 16 gigas. / Dans 12, non. / Dans 8, encore moins. »

**Pourquoi ça coince :** il n'y a pas *une* version compressée. Ta vidéo précédente fait tourner Qwen 27B **sur 8 gigas** avec le fichier UD-IQ2_XS de 7,63 Go. Sur Hugging Face, j'ai aussi vu un UD-IQ3_XXS de 10,93 Go qui entre dans 12. Le spectateur qui a vu la vidéo d'avant va le relever tout de suite. La phrase n'est juste que pour le fichier de 14,4 Go.

**Correction :** c'est ton seul renvoi autorisé, et il tombe bien. Pas besoin d'ajouter de chiffre de qualité.

```
Un exemple concret :
Qwen 27B, dans sa version en 4 bits,
rien que son fichier fait 14,4 gigas.
Ça rentre dans 16 gigas.
Dans 12, non.
Pour le faire tenir dans 8, il faut le compresser beaucoup plus,
et tu as vu dans la vidéo précédente ce que ça coûte.
```

### B4. Le verdict ne règle pas le cas de l'Arc B580, que ta propre règle désigne
> « Ligne 2 : à mémoire égale, le débit mémoire. »
> « En 12 gigas, tu as la RTX 3060, dès 509,99 euros chez Cdiscount. / Et l'Arc B580, 499,99 chez TopAchat, en stock limité. »
> « Prends la RTX 3060 12 gigas, à 509,99 euros chez Cdiscount. »

**Pourquoi ça coince :** sous 600 € en neuf, le plus de mémoire, c'est 12 Go, et deux cartes en ont 12. À mémoire égale, ta ligne 2 désigne la B580 : 456 de débit contre 360, et 10 € de moins. Le spectateur qui applique ta méthode arrive à l'inverse de ton verdict. Les lignes 91 à 93 donnent la réponse (« d'une marque à l'autre, ça ne marche pas »), mais le verdict ne la rappelle pas. Et la ligne 93 dit « dans des tests publiés » pour un tableau à testeurs différents, alors que tout le reste s'appuie sur « même testeur ».

**Correction :** ferme la boucle dans le verdict, avec ce que disent les sources : seule la 3060 a une mesure à testeur unique ; la B580 n'a qu'un chiffre de testeur différent.

```
Et l'Arc B580 ? Plus de débit, et 10 euros de moins.
Sauf que, tu te souviens, d'une marque à l'autre la règle ne marche plus.
Dans un tableau de mesures publiées, sur des machines différentes,
elle écrit un peu moins vite que la 3060,
et elle lit ta question presque 3 fois moins vite.
```

Chiffres vérifiés sur la page (Vulkan, Llama 2 7B, testeurs différents) :
- écriture : B580 70,14 contre 3060 75,94 sans flash attention, et 72,00 contre 80,59 avec ;
- lecture : 620,94 contre 1 815,70, soit 2,9 fois.

Ce n'est pas un test contrôlé : la ligne 93 doit le dire pareil (« sur des machines différentes »). Si tu ne veux pas trancher, dis franchement « à 10 euros près, c'est l'une ou l'autre ». C'est défendable aussi.

---

## Importants

### I-1. La thèse « mémoire d'abord » n'est jamais montrée sur les cartes du hook
> « En fait, la plus récente, celle qui a le plus de mémoire, / écrit moins vite. »

Le hook fait gagner la carte qui a **moins** de mémoire. Ta ligne 1 dit le contraire. Ensuite, la seule preuve de la ligne 1 est la taille d'un fichier. Et l'égalité en 14B (ligne 95) affaiblit encore le hook sans le relier à la mémoire.

**Correction :** récolte le hook dans la ligne 1, en une phrase. Elle est sourcée par F8 (fichier de 14,35 Go) et F6 (28 tokens/s sur une 5060 Ti 16 Go avec ce fichier) :

```
Et c'est pour ça que la 4060 Ti du début n'est pas une mauvaise carte :
ses 16 gigas font rentrer ce Qwen 27B. La 3060, non.
```

À la fin (S6), reviens sur la 3060 du hook : « La 3060 du début, tu sais maintenant pourquoi elle écrivait plus vite, et ce qu'elle ne peut pas faire. »

Note pour toi, pas pour la voix : sur la page des mesures, la 4060 Ti 16 Go a des chiffres que la 3060 n'a pas (14B à 32K de contexte : 17,86 ; 8B à 65K : 13,01 ; gpt-oss 20B : 57,76). Un tiret veut seulement dire « pas de valeur » ; en conclure que le modèle « ne tient pas » serait une déduction. Ne l'utilise pas tel quel.

### I-2. Le piège de la RTX 3060 **8 Go**, au même prix, n'est pas signalé
> « Prends la RTX 3060 12 gigas, à 509,99 euros chez Cdiscount. »

Le même jour, la 3060 **8 Go** est à 499,99 € chez TopAchat, en stock (PX §1, rouverte), et à 519,95 € chez Materiel.net. Elle s'appelle « RTX 3060 » comme l'autre et coûte 10 € de moins. Elle a un bus de 128 bits (page Nvidia) et 224 de débit (Wikipédia), moins que la 4060 Ti du hook. Wikipédia ne donne pas sa fréquence : le « 14 » est un calcul (224 × 8 ÷ 128). Ajoute-le à `sources.md` avant de le dire en voix. C'est exactement le « mauvais achat » de ta phrase d'abonnement. Et c'est la meilleure démo de ton calcul.

**Correction :** ajoute au verdict, puis une ligne au tableau (`RTX 3060 8 Go | 8 Go | 128 × 14 ÷ 8 | 224 | 499,99 € | neuf | TopAchat`) :

```
Attention, il existe une 3060 8 gigas, au même prix.
128 bits, mémoire à 14 : 224 de débit.
Sur la fiche, vérifie bien les 12 gigas.
```

Selon le résumé de l'outil (non vérifié), la fiche TopAchat de cette 3060 8 Go indiquerait « 192 bit ». Si c'est confirmé, c'est un bon exemple de fiche marchande fausse, à recouper avec la page du fabricant.

### I-3. L'occasion manque dans le verdict
Tu parles d'occasion pour la 4060 et la 3060 Ti, mais pas pour la carte que tu recommandes. F35 : RTX 3060 12 Go d'occasion entre 250 et 496 €, et le cœur du marché entre 250 et 400 €. C'est 110 à 260 € de moins que les 509,99 € du neuf, pour la même carte.

**Correction :** « Et d'occasion, la même se trouve entre 250 et 400 euros. »

### I-4. « Un chiffre que les sites n'affichent jamais » est faux
> « et comment calculer un chiffre que les sites n'affichent jamais. »
> « Bon, le problème, c'est que les sites ne l'affichent presque jamais. »

Les pages officielles d'Intel (B580 : « 456 GB/s ») et d'AMD (9060 XT : « Up to 320 GB/s ») l'affichent. Le plan dit « jamais », la suite dit « presque jamais ». Ce qui est vrai et rouvert : **les pages de Nvidia n'écrivent ni le débit ni la fréquence**, seulement la largeur du bus (vérifié sur 3060, 4060 et 5060).

**Correction :** au plan, « comment calculer un chiffre que Nvidia n'écrit même pas sur ses propres pages » (c'est plus fort). À 4:28, « Le problème, c'est que Nvidia ne l'écrit même pas. »

### I-5. « Au-dessus de 1 000 euros dans les boutiques spécialisées »
> « et au-dessus de 1 000 euros dans les boutiques spécialisées. »

TopAchat est à 999,99 € (rouvert), donc 1 centime **sous** 1 000. Le tableau, lui, est juste.

**Correction :** « et autour de 1 000 euros dans les boutiques spécialisées. »

### I-6. « Elles ont un bon débit » inclut la RX 9060 XT 8 Go
> « Elles ont un bon débit, 448 pour les Nvidia, »

La RX 9060 XT 8 Go est à 320, moins que la 3060 (360) que tu recommandes. La page AMD de la version 8 Go le confirme.

**Correction :** « Les 2 Nvidia ont un bon débit, 448, / mais seulement 8 gigas. »

### I-7. La liste de prix (6:34 à 7:48) : 74 s de fiche, avec des centimes
> « La RTX 5060 dès 519,99 euros, chez Amazon et Cdiscount. / La 5060 Ti 8 gigas, entre 586,78 et 599,99, chez Amazon. / La RX 9060 XT 8 gigas, 539,99, chez Amazon. »

Ce sont trois faits empilés sans réaction. Lu à voix haute, « cinq cent quatre-vingt-six euros soixante-dix-huit » fait décrocher. C'est le plus long trou sans question du script.

**Correction :** en voix, arrondis (« 520 euros », « 590 à 600 », « 540 », « 510 », « 500 », « 670 à 700 », « 800 ») et garde les prix exacts et les marchands à l'écran et dans le tableau. Ajoute une réaction : « Donc à 600 euros, en neuf, 8 gigas, c'est la norme. » Le verdict peut garder « 509,99 chez Cdiscount », un seul prix exact.

### I-8. La fin du passage 4060 s'effondre sous trois réserves, dont une qui parle de ta méthode
> « Attention quand même : / dans les recherches pour cette vidéo, aucun test contrôlé ne les oppose. / Là, on compare leurs fiches, pas leur vitesse mesurée. / Sauf que la 3060 Ti n'a que 8 gigas. »

« Dans les recherches pour cette vidéo » n'est pas un aveu interdit, mais il parle des coulisses. Trois réserves de suite cassent la promesse du plan.

**Correction :**
```
Attention : là, on compare des fiches, pas des mesures.
Et surtout, la 3060 Ti n'a que 8 gigas.
Donc avant de foncer, ligne 1 d'abord, tu te souviens ?
```

Tu peux aussi muscler le « souvent » de la ligne 129 avec un comptage (PX §3) : « Aucune 4060 relevée sous 360 euros. Les 3060 Ti, presque toutes en dessous. » (8 annonces sur 9.)

### I-9. La RTX 3060 mesurée : 12 Go déduit, pas écrit
> « une RTX 3060 sortie en 2021 »

La page des mesures n'écrit nulle part « 12 GB ». La seule mention de mémoire pour la 3060 est une coquille : « RTX 3060 16GB ». Mais le 12 Go se déduit bien :
- elle a fait tourner Qwen3 14B en UD-Q4_K_XL (fichier de 9,16 Go sur Hugging Face) à 16K de contexte, à 22,66 tokens/s, à égalité avec la 4060 Ti : impossible sur 8 Go sans déborder ;
- elle fait aussi le 8B à 32K ;
- et une 3060 8 Go (224) serait derrière la 4060 Ti (288), pas devant.

« Sortie en 2021 » dépend de cette déduction : la version 8 Go est sortie fin 2022.

**Correction :** la voix peut rester telle quelle. Écris la déduction dans F26 de `sources.md`, et mets « RTX 3060 12 Go (déduit) » sur le visuel du hook.

### I-10. Le passage à 700 € ne fait pas le lien avec le hook
> « la RX 9060 XT 16 gigas, à 699,99 chez Amazon, / te donne 4 gigas de plus, / avec un débit plus bas. »

C'est le profil de la 4060 Ti du hook : plus de place, moins de débit. Il faut le dire, sinon l'option semble contredire le début. Et c'est une AMD, donc la règle du débit ne permet pas de prédire sa vitesse face à la 3060 (tu l'as dit à la ligne 91).

**Correction :**
```
C'est le même choix que la 4060 Ti du début :
plus de place, moins de débit.
Tu la prends si tu veux des modèles qui ne rentrent pas dans 12,
comme le Qwen 27B de tout à l'heure.
```

---

## Détails

- **Ligne 35** « exactement à la même vitesse » : 141 contre 143, ce n'est pas « exactement ». Écris « à la même vitesse, à 2 tokens près ».
- **Ligne 29** « 29 % » : c'est juste d'après le graphique (5 733 ÷ 4 458 = 1,286). Le texte de la même page dit « 25 % ». Garde 29, mais sache-le si un commentaire le relève.
- **Ligne 73** « Et du coup, c'est là que ça devient intéressant. » : c'est un faux suspens (anti-IA §2). Coupe, et commence par « Reprends la série de mesures du début. »
- **Lignes 82 à 85** « En fait, je te les mets dans le même ordre. / … / Exactement le même ordre. » : la phrase se mord la queue et le « en fait » est creux. Écris « Maintenant, leur débit mémoire, carte par carte : / 936, 672, 448, 360, 288. / Ça descend pareil. »
- **Ligne 117** « Pas le double, mais c'est énorme. » : fausse opposition, puisque personne n'a parlé du double dans la vidéo. Écris « Presque 2 tiers de plus. »
- **Ligne 87** « ce n'est pas une règle magique » : homme de paille. Écris « Par contre, attention, il y a des limites. »
- **Lignes 44-45** « ce n'est pas la force de la carte, / c'est la vitesse à laquelle elle tourne les pages » : c'est une opposition, mais elle est méritée (la série 4070 vient de la prouver). Garde-la, c'est la seule.
- **« Attention »** revient 3 fois et **« par contre »** 2 fois, dont deux fois « par contre, attention ». Varie.
- **Liaisons creuses :** l. 28 (« Et en fait »), l. 73, l. 83, l. 115 (« Du coup, la 3060 Ti… » ne découle de rien). Sans elles, on est à environ 1,65 pour 100 : ça tient, mais c'est juste.
- **Ligne 103** « la vitesse de la mémoire, en gigabits par seconde » : « vitesse » sert déjà pour les tokens/s et le débit (« la vitesse à laquelle elle tourne les pages »). Pour garder un seul nom par chose, écris « la fréquence de la mémoire, en gigabits par seconde », comme sur les fiches marchandes (« Fréquence mémoire »).
- **Ligne 173** « au même prix » : la 5060 Ti 8 Go coûte 77 à 90 € de plus. Écris « pour moins cher ».
- **Ligne 127** « entre 249 et 430 » : le 249 repose sur une seule annonce eBay qui affichait 369,82 € dans la liste (PX §3.1). « Entre 260 et 430 » est plus solide. Il existe aussi une 3060 Ti GDDR6X à 608 de débit (Nvidia, Wikipédia) : ton « mémoire à 14 » vaut pour la GDDR6. Pas besoin de le dire, mais ne l'écris pas « toutes les 3060 Ti ».
- **Ligne 66** « Ça rentre dans 16 gigas » : le fichier fait 13,37 Gio, il reste environ 2,6 Gio pour la conversation. « De justesse » serait plus honnête et rappelle la vidéo précédente.
- **Lignes trop longues** (14 mots, avec des prix à centimes) : l. 125 (« La seule offre neuve vue : 923,84 euros… »), l. 164, l. 173. Coupe chacune en 2 souffles.
- **Ligne 79** « La 3060 : 42. » : les autres lignes ont leur mémoire (« 16 gigas »). Si I-9 est documenté, écris « La 3060 12 gigas : 42. »
- **Visuel du hook** : il cite le logiciel, ça va (aucun nom de site ni de testeur). Ajoute « 12 Go (déduit) ».

## Ce qu'il faut garder

- « Sauf que pour écrire la réponse, / 141, 142 et 143 tokens par seconde. / Pareil. » : c'est le meilleur retournement de la vidéo, preuve à l'appui.
- L'image du livre et « Pas un chapitre : tout. » : claire et brève.
- « En gros, le calcul, lui, sert surtout à lire ta question. / C'est là que la 4070 Ti gagnait ses 29 %. » : un vrai planté-récolté.
- Le motif « Ligne 1 / Ligne 2 » et « Ligne 1 d'abord, tu te souviens ? ».
- « Donc le débit, tu t'en sers pour départager des cartes proches. / Pas pour prédire un chiffre. » : c'est honnête et c'est utile.
- Les limites (proportion, marque, 14B) sont dites franchement et sans aveu.

## Plan d'action

1. Réécris les 30 s : plan vers 33 s, chiffre avant 20 s (B1). Dans le même temps, enlève ou source « comme pour le jeu / comparateur / plus cher » (B2).
2. Corrige Qwen 27B avec le renvoi à la vidéo précédente (B3), puis récolte le hook dans la ligne 1 (I-1).
3. Ferme le verdict : la B580 (B4), le piège de la 3060 8 Go (I-2), l'occasion à 250-400 € (I-3), le lien avec la 4060 Ti pour l'option à 700 € (I-10).
4. Corrige les faits : « Nvidia n'écrit même pas » (I-4), « autour de 1 000 » (I-5), « les 2 Nvidia » (I-6). Arrondis les prix en voix (I-7).
5. Mets à jour `sources.md` (F26 : 12 Go déduit ; ajoute le tableau Vulkan pour la B580) et le tableau (ligne 3060 8 Go), puis recompte les mots et les liaisons.

---

## Tableau des faits (voix et tableau)

✅ = conforme aux sources et rouvert ce soir ; ☑️ = conforme aux sources, non rouvert ; ⚠️ = juste mais à nuancer ; ❌ = faux ou non sourcé.

| Ligne | Phrase | Source | Calcul / contrôle | Verdict |
|---|---|---|---|---|
| 1-3 | 600 €, Black Friday, IA chez toi | F11, fiche | — | ✅ cadre |
| 6-9 | 3060 (2021) plus rapide que 4060 Ti 16 Go (2023), 42 contre 34 | F26, F32 | 41,97 ; 34,31 ; dates du 25/02/2021 et du 18/07/2023 | ✅ (12 Go déduit, I-9) |
| 11-12 | « celle qui a le plus de mémoire, écrit moins vite » | F26 | vrai en 8B ; faux en 14B (égalité) | ⚠️ (I-1) |
| 13-15 | « comme pour le jeu… mieux classée… plus cher » | aucune | F33 écarte l'opposition jeu/IA ; pas de prix FR pour la paire | ❌ (B2) |
| 20 | « que les sites n'affichent jamais » | BP | Intel et AMD l'affichent ; Nvidia non | ❌ (I-4) |
| 27-29 | 4070 / Super / Ti : lecture +29 % | F27 | 5 733 ÷ 4 458 = 1,286 (le texte de la page dit 25 %) | ✅ |
| 32 | 141, 142, 143 tokens/s | F27 | graphique rouvert | ✅ |
| 35 | « exactement à la même vitesse » | F27 | +1,4 % | ⚠️ détail |
| 42 | relire tout le livre à chaque mot | F28 | paraphrase ; pages non rouvertes | ☑️ |
| 59-61 | le modèle qui déborde : la RAM et le processeur donnent le rythme | F31 | principe seulement | ☑️ |
| 64-68 | Qwen 27B : 14,4 Go ; rentre dans 16, pas dans 12, « dans 8 encore moins » | F8 | UD-IQ4_XS = 14,35 Go (HF) ; mais IQ3_XXS = 10,93 et IQ2_XS = 7,63 | ❌ formulation (B3) |
| 75-80 | 87 / 59 / 51 / 42 / 34 | F26 | 87,45 ; 59,13 ; 51,41 ; 41,97 ; 34,31 | ✅ |
| 84 | 936, 672, 448, 360, 288 | F23, F24 | 384×19,5÷8 = 936 ; 192×28÷8 = 672 ; 128×28÷8 = 448 ; 192×15÷8 = 360 ; 128×18÷8 = 288 | ✅ |
| 89-90 | 3090 : 2 fois plus de débit, 1,7 fois plus vite que la 5060 Ti | F24, F26 | 936 ÷ 448 = 2,09 ; 87,45 ÷ 51,41 = 1,70 | ✅ |
| 92-93 | B580 : plus de débit que la 3060, écrit un peu moins vite | F25, F29 | 456 > 360 ; 70,14 contre 75,94 (−7,6 %), testeurs différents | ⚠️ « tests publiés » sans dire « machines différentes » (B4) |
| 94-95 | 14B : égalité 3060 / 4060 Ti | F26 | 22,66 contre 22,36 | ✅ |
| 104 | bus × fréquence ÷ 8 | F20 | — | ✅ |
| 107-108 | 4060 : 128 × 17 ÷ 8 = 272 | F21 | 2 176 ÷ 8 = 272 ; bus de 128 bits rouvert chez Nvidia | ✅ |
| 111-112 | 3060 Ti : 256 × 14 ÷ 8 = 448 | F22 | 3 584 ÷ 8 = 448 ; bus de 256 bits rouvert | ✅ (version GDDR6) |
| 115 | 3060 Ti sortie 2 ans et demi plus tôt | F32 | du 02/12/2020 au 29/06/2023 = 2 ans 7 mois | ✅ |
| 116 | +65 % | F22 | 448 ÷ 272 = 1,647 | ✅ |
| 117 | « Pas le double » | — | — | ⚠️ tic (détail) |
| 119-120 | toute la série 4060 en 128 bits ; 4060 Ti 16 Go à 288 | F23 | page Nvidia rouverte : « 128-bit » pour 4060 et 4060 Ti 8/16 | ✅ |
| 123-125 | 4060 neuve introuvable ; seule offre neuve 923,84 €, vendeur tiers Amazon | F34 | fiche rouverte : 923,84 €, vendeur ASALIA, 3 exemplaires | ✅ (absence chez les autres marchands non recherchée de nouveau) |
| 126 | 4060 d'occasion 360-480 € | F35 | PX §3.3 | ☑️ |
| 127 | 3060 Ti d'occasion 249-430 € | F35 | le 249 repose sur une annonce douteuse | ⚠️ détail |
| 146 | RTX 5060 dès 519,99 €, Amazon et Cdiscount | F36 | 2 fiches rouvertes, vendues par Amazon et par Cdiscount | ✅ |
| 147 | 5060 Ti 8 Go 586,78 à 599,99 €, Amazon | F36 | fiches rouvertes (vendu par Amazon) | ✅ |
| 148 | RX 9060 XT 8 Go 539,99 €, Amazon | F36 | fiche rouverte, en stock | ✅ |
| 150 | « Elles ont un bon débit, 448 pour les Nvidia » | F24, F25 | la 9060 XT 8 Go est à 320 < 360 | ⚠️ (I-6) |
| 154 | RTX 3060 12 Go dès 509,99 €, Cdiscount | F36 | fiche rouverte : Gigabyte Windforce OC 12 Go, vendu par Cdiscount, 16 offres dès 509,99 € | ✅ |
| 155 | Arc B580 499,99 €, TopAchat, stock limité | F13, F36 | fiche rouverte : « STOCK LIMITÉ » | ✅ |
| 158-161 | 16 Go sous 700 € : RX 9060 XT 669,99-699,99 €, une seule en stock | F37 | 699,99 (ASUS Prime, en stock, vendu par Amazon, livraison le 25/11) ; 669,99 (ASUS Dual, vendu par Amazon, livraison du 31/12 au 2/01) | ✅ (la date de livraison a bougé) |
| 162 | débit de la 9060 XT 16 Go : 320 | F25 | page AMD rouverte : « Up to 320 GB/s », 128 bits, 20 Gbps | ✅ |
| 164 | 5060 Ti 16 Go à 799 €, Amazon et Cdiscount | F38 | 2 fiches rouvertes (Amazon vendeur ; Cdiscount, 24 offres dès 799) | ✅ |
| 165 | « au-dessus de 1 000 € en boutique » | F38 | TopAchat 999,99 (rouvert) ; LDLC 1 099,95 (rouvert) | ⚠️ (I-5) |
| 167-169 | le classement en jeu ne dit ni la mémoire ni le débit | aucune | — | ❌ (B2) |
| 172-175 | verdict 3060 12 Go 509,99 € ; 360 ; plus vite que la 4060 Ti au début | F36, F23, F26 | — | ✅, mais il manque la B580, l'occasion et la 3060 8 Go (B4, I-2, I-3) |
| 173 | « plus que les 5060 et 5060 Ti 8 gigas au même prix » | F36 | 509,99 contre 519,99 et 586,78 | ⚠️ « pour moins cher » |
| 178-181 | RX 9060 XT 16 Go à 699,99 € ; 4 Go de plus ; débit plus bas | F37, F25 | 16 − 12 = 4 ; 320 < 360 | ✅ |
| Tableau | 13 lignes : calculs et prix | F21-F25, F34-F38 | les 13 calculs refaits sont justes ; les prix collent avec PX | ✅ ; à ajouter : une ligne 3060 8 Go (I-2) |

**Format :**
- Aucun crochet dans le téléprompteur.
- `script.md` : seulement des `[VISUEL…]` et `[F…]`, aucun crochet à remplir.
- La voix de `script.md` (sans les visuels ni les F) est identique au `.txt`, et `.txt` = `.md`.
- Aucune annonce de la vidéo suivante, aucun renvoi (B3 propose le seul autorisé).
- Aucune phrase d'aveu. Aucun nom de site de tests, de testeur ou de chaîne en voix.
- La phrase d'abonnement est exacte et placée à 6:20, après la règle et le piège 4060 : c'est conforme.
- Nombres en chiffres : conforme.
- 1 287 mots, soit 8:53 à 145 mots/min (environ 9:30 avec les nombres lus) : conforme.

---

## Compte rendu des pages rouvertes (18/11/2026, soir)

**(a) Mesures du hook, page de classement de Hardware Corner** (`https://www.hardware-corner.net/gpu-ranking-local-llm/`). Ouverte en HTML brut et en résumé.
- Date : « Updated December 9, 2025 ». Protocole : llama-bench de llama.cpp, « latest » (version non précisée), CUDA 12.8, Ubuntu 24.04, « 4-bit (Q4_K_XL) » pour toutes les mesures de génération, tableaux à 16K, 32K, 65K et 131K de contexte.
- Chiffres identiques à F26 : 87,45 ; 59,13 ; 51,41 ; 41,97 ; 34,31 en Qwen3 8B à 16K, et 22,66 contre 22,36 en 14B.
- La 4060 Ti est bien la 16 Go (« the RTX 4060 Ti 16GB's 34.31 t/s »).
- **Quelle RTX 3060 ?** La page ne le dit jamais. La seule mention de mémoire est « RTX 3060 16GB », une carte qui n'existe pas. Le 12 Go est déduit (I-9) : le 14B en Q4_K_XL fait 9,16 Go sur Hugging Face, et il a tourné à 22,66 tokens/s à 16K de contexte.
- Autres chiffres utiles : à 32K, 8B 31,86 (3060) contre 25,53 (4060 Ti) ; le 14B à 32K, le 8B à 65K et gpt-oss 20B ont un tiret pour la 3060 et un chiffre pour la 4060 Ti (17,86 ; 13,01 ; 57,76). Prix de la page, en dollars et sans date : 3060 250 $, 4060 Ti 409 $.

**Série 4070, Puget Systems** (`https://www.pugetsystems.com/labs/articles/llm-inference-consumer-gpu-performance/`, 22/08/2024). Graphiques téléchargés et lus : écriture 141 / 142 / 143, lecture 4 458 / 5 165 / 5 733, Phi-3-mini q4, llama.cpp b3140, Windows 11, débit de 504,2 pour les trois. Le texte dit « 25 % » pour la lecture ; le graphique donne 28,6 %.

**(b) Débits mémoire**

| Carte | Ce que j'ai lu | Verdict |
|---|---|---|
| RTX 4060 | Wikipédia 40 : 128 bits, 17 Gb/s, 272 GB/s ; Nvidia : « 128-bit », sans débit ni fréquence | ✅ 272 |
| RTX 4060 Ti 8 et 16 Go | Wikipédia : 18 Gb/s, 288 (cellules fusionnées) ; Nvidia : « 16 GB or 8 GB », « 128-bit » | ✅ 288 |
| RTX 3060 12 Go et 8 Go | Wikipédia 30 : 12 Go 192 bits, 15, 360 ; 8 Go 128 bits, 224 ; Nvidia : « 192-bit / 128-bit » | ✅ 360 (et 224 pour la 8 Go) |
| RTX 3060 Ti | Wikipédia : GDDR6 256 bits, 14, 448 ; il existe une GDDR6X à 608 ; Nvidia : « 256-bit » | ✅ 448 (GDDR6) |
| RTX 5060 / 5060 Ti / 5070 | wikitext brut de la page 50 : colonnes 5060 et 5060 Ti à 128 bits, 28 Gb/s, 448 ; 5070 à 192 bits, 28, 672 ; Nvidia : « 128-bit » pour les deux 5060, sans débit | ✅ 448 et 672 (le résumé de l'outil disait « déduit » : c'est le wikitext qui tranche) |
| RX 9060 XT 16 Go | page AMD : 20 Gbps, 128 bits, « Up to 320 GB/s » | ✅ 320 |
| RX 9060 XT 8 Go | page AMD de la 8 Go (`…amd-radeon-rx-9060xt-8gb.html`) : « Up to 320 GB/s », 8 Go ; le 288 de Wikipédia est celui de la RX 9060 sans XT | ✅ 320 |
| Arc B580 | page Intel : 12 Go, 192 bits, 19 Gbps, « 456 GB/s », Q4'24 | ✅ 456 |
| RTX 3090 | Wikipédia : 936 (« 9,75 GT/s » en PAM4) ; la page des mesures écrit 936,2, 384 bits, 19,5 Gbps | ✅ 936 |

**(c) Prix du verdict et de la voix.** Amazon lu en HTML (curl), Cdiscount dans le navigateur, TopAchat et LDLC par WebFetch.

| Offre | 18/11, soir | Écart avec le relevé |
|---|---|---|
| Cdiscount, Gigabyte RTX 3060 Windforce OC 12 Go | 509,99 €, vendu par Cdiscount, « 16 offres neuves à partir de 509,99 € » | aucun |
| Amazon, ASUS Prime RX 9060 XT 16 Go | 699,99 €, en stock, vendu par Amazon, livraison le 25/11 | aucun |
| Amazon, ASUS Dual RX 9060 XT 16 Go | 669,99 €, vendu par Amazon, livraison du 31/12 au 2/01 | livraison avancée (avant : 2-3/01) |
| Amazon, MSI RTX 5060 Ventus | 519,99 €, en stock, vendu par Amazon | aucun |
| Cdiscount, PNY RTX 5060 | 519,99 €, vendu par Cdiscount, 3 offres | aucun |
| Amazon, PNY 5060 Ti 8 Go | 586,78 €, 6 exemplaires, vendu par Amazon | aucun |
| Amazon, ASUS Dual 5060 Ti 8 Go | 599,99 €, en stock | aucun |
| Amazon, Sapphire RX 9060 XT 8 Go | 539,99 €, en stock | aucun |
| Amazon, ASUS Dual 5060 Ti 16 Go | 799,00 €, en stock, vendu par Amazon | aucun |
| Cdiscount, ASUS Dual 5060 Ti 16 Go | 799,00 €, vendu par Cdiscount, 24 offres | aucun |
| Amazon, MSI RTX 4060 Ventus 2X Black | 923,84 €, vendeur ASALIA, 3 exemplaires | aucun |
| TopAchat, ASRock Arc B580 Challenger | 499,99 €, « STOCK LIMITÉ » | aucun |
| TopAchat, Gainward 5060 Ti 16 Go | 999,99 €, en stock | aucun |
| LDLC, ASUS Prime 5060 Ti 16 Go | 1 099,95 €, en stock | aucun |
| TopAchat, Gigabyte 3060 Gaming OC **8G** | 499,99 €, en stock, selon un résumé de l'outil (« Interface mémoire 192 bit », non vérifié, contredit par Nvidia) | aucun pour le prix |

**(d) Années de sortie** (Wikipédia, rouvert) : 3060 12 Go le 25/02/2021 ; 3060 Ti le 02/12/2020 ; 3090 le 24/09/2020 ; 4060 le 29/06/2023 ; 4060 Ti 8 Go le 24/05/2023 ; 4060 Ti 16 Go le 18/07/2023 ; 3060 8 Go en octobre 2022. Tout ce qui est dit en voix est juste, avec la réserve de I-9 pour « 3060 sortie en 2021 ».

**Autres réouvertures**
- Tableau Vulkan de llama.cpp, discussion 10879 : B580 70,14 et 3060 75,94 sans flash attention ; 72,00 et 80,59 avec ; lecture 620,94 et 1 815,70. Testeurs et commits différents.
- Hugging Face : Qwen3.8-27B UD-IQ4_XS 14,35 Go, UD-IQ3_XXS 10,93 Go, UD-IQ2_XS 7,63 Go ; Qwen3 14B UD-Q4_K_XL 9,16 Go ; Qwen3 8B UD-Q4_K_XL 5,14 Go.

**Non rouvert, donc non validé par moi :**
- les annonces d'occasion (Leboncoin, eBay, Materiel.net) ;
- les fiches 3060 12 Go à 579,95 € de LDLC et Materiel.net ;
- l'absence de 4060 neuve chez LDLC, Materiel.net, TopAchat et Cdiscount (pas refait de recherche) ;
- la B580 chez LDLC à 519,95 € ;
- la page gpupoet (F33) ;
- les pages de F28 (discussion llama.cpp 17621, blog Nvidia) ;
- la discussion llama.cpp 15013 (pas en voix).

Aucune page de jeu n'a été ouverte. Les résultats de recherche (agrégateurs) ne valent pas source.
