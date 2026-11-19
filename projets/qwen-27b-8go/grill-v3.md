# Grill V3 : Qwen 27B sur 8 Go

Relecture indépendante du 18/11/2026, faite sur `teleprompteur.txt` et `script.md` (V3). Méthode : skill `youtube-script-grill`, variante storytelling. Faits recoupés avec `sources.md` (F1 à F16), `recherche-mesures.md` (M2) et la transcription `etudes/transcriptions/simplyexplain-u_DYZhTZ2IM.md`. Aucun autre fichier n'a été modifié.

## Note : 7/10

Le squelette est bon. Le chiffre arrive dès la première phrase, la limite est dite tout de suite et franchement, et le plan est tenu point par point. Le passage sur les 2 min 36 qui « redeviennent une discussion » est le meilleur moment humain du script. Il y a pourtant **une erreur de calcul dans le verdict**, justement sur le chiffre qui doit faire basculer la décision. Il y a aussi **une promesse sur la carte du spectateur** que le cadre interdit. Plusieurs points importants restent derrière : un mélange de conditions de mesure, un MTP absent de `sources.md`, un « enfin » qui ramène le superlatif retiré, et des sources et visuels décalés d'un paragraphe dans `script.md`. Corrige les 2 bloquants et les 4 premiers points importants, et tu es à 8,5.

---

## Test des 30 secondes

Débit : 145 mots/min, soit 2,4 mots par seconde. Les temps viennent de `wc -w` cumulé ligne par ligne. Les nombres lus en toutes lettres (« trois virgule deux », « mille quatre-vingts ») allongent chaque repère de 1 à 3 s.

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | « Sur une carte de 8 gigas, tu changes un seul fichier, » | 🟢 Le sujet, le « tu » et la tension (un seul fichier) sont là dès les 11 premiers mots. |
| 5-15 s | « et Qwen 27B passe de 3,2 à 18 tokens par seconde. / Même modèle, même carte, rien acheté. / Sauf que c'est une seule mesure publiée, » | 🟢 Le meilleur chiffre tombe à 9 s, puis le contraste arrive à 14 s. Le visuel daté (F2) sert de preuve. |
| 15-30 s | « sur une GTX 1080 Ti limitée à 8 gigas. / Moi, j'ai rien testé : ce sont ses chiffres. / Et dans cette mesure, ça fait plus de 5 fois et demie plus vite. / Du coup, la vraie question : » | 🟠 Les 2 premières lignes sont imposées par le cadre et passent bien. La 3e redit en ratio ce que le spectateur a entendu 18 s plus tôt : elle ne confirme rien de neuf et coûte 6 s. « ses chiffres » n'a pas d'antécédent. |
| Question centrale | « qu'est-ce que ce fichier te fait perdre en échange ? » | 🟠 C'est une bonne question, unique et en mots simples, mais elle se termine à **34 s** (≈ 36 s avec les nombres lus). |
| Plan + pont | l. 12-16, de 34 à **58 s** | 🟠 Les 4 livrables sont concrets et tous tenus. Par contre, la ligne 12 fait 18 mots, et « Reste jusqu'à la fin, on va voir si ces 18 tokens valent le coup » rejoue la question au lieu d'ouvrir une 2e boucle. Le plan dure 24 s. |

**Budget :** 73 mots à 30 s, 83 à la fin de la question, 140 à la fin du plan.
**À couper :** la ligne 8 (le ratio reviendra au verdict) et « on va voir si ces 18 tokens valent le coup ».
**Première partie :** elle commence par un résultat (« Prends une réponse de 500 tokens »), pas par une définition. 🟢

**Réécriture des 30 s et du plan** (tout est sourcé : F2, F4, F14) :

```
Sur une carte de 8 gigas, tu changes un seul fichier,
et Qwen 27B passe de 3,2 à 18 tokens par seconde.
Même modèle, même carte, rien acheté.

Sauf que c'est une seule mesure publiée,
sur une GTX 1080 Ti limitée à 8 gigas.
Moi, j'ai rien testé : ce sont les chiffres de celui qui a mesuré.
Du coup, la vraie question :
qu'est-ce que ce fichier te fait perdre en échange ?

Donc on va voir le fichier qui fait tout tenir dans 8 gigas,
ce qu'il te coûte en mémoire de conversation,
et ce qu'il te coûte en qualité.
Et reste jusqu'à la fin :
il y a un travail que ce fichier rate presque 9 fois sur 10,
dans les tests de ceux qui le fabriquent.
```

Compté avec le même `awk` : la question se termine à 74 mots, soit 30,6 s. `wc` compte les 2 « : » comme des mots, donc on est en vrai à environ 30 s. Le plan se termine à environ 130 mots, soit 53 s, contre 58 s aujourd'hui. Aucune ligne ne dépasse 14 mots. Le « 9 fois sur 10 » se calcule ainsi : 100 − 12,8 = 87,2 % d'échecs sur DeepSWE (F4). Il reste attribué au fabricant et à ses tests. Il ouvre une 2e boucle, chiffrée, qui se ferme au verdict.

**Calibrage avec la vidéo précédente (validée) :**
- Son ouverture a la même forme : chiffre, « Même fichier, même carte, rien acheté », provenance, « Moi, j'ai rien testé », puis la question vers 30 s.
- Sa ligne de ratio (« entre 1,9 et 2,3 fois plus vite ») apportait une information nouvelle, les 6 mesures. Ici, la l. 8 répète le chiffre du hook : c'est pour ça qu'elle saute, et pas la ligne de ratio en général.
- Son « Et reste jusqu'à la fin, parce qu'on va démystifier un réglage… » promettait une révélation précise. Ici, « on va voir si ces 18 tokens valent le coup » n'en promet aucune.

---

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | « Plus rapide, mais à quel prix ? » : le gain est dit en 9 s, et les 2 prix sont payés en entier. |
| 2. Alignement | 🟢 | C'est honnête : la provenance, le conflit d'intérêt d'Unsloth et l'absence de test sont dits clairement. |
| 3. Problème profond | 🟢 | Le piège de la fausse vitesse : il est posé l. 25-30 et récolté l. 125-127 (« une réponse en 28 secondes que tu dois réparer »). |
| 4. Public & complexité | 🟠 | « 4 bits » sert à la fois au cache et au fichier, « le modèle complet » n'est jamais défini et le MTP n'est pas rappelé. |
| 5. Valeur | 🟢 | La traduction en temps d'attente, le contexte réel et le verdict par usage apportent plus que la source. |
| 6. Structure | 🟢 | Le gain, pourquoi, prix 1, prix 2, puis le verdict : la progression est claire. |
| 7. Histoire | 🟠 | C'est un essai calculé : la « crise » (13 %) est bien placée, mais elle tombe sans réaction. |
| 8. Mais / donc | 🟢 | « Sauf que » et « par contre » relancent bien chaque partie. |
| 9. Engagement | 🟢 | « Alors, à ton avis, ça tient aussi quand on lui confie un vrai projet ? » est placé au bon endroit. |
| 10. Rythme & liaisons | 🟠 | Il y a 1,77 liaison pour 100 mots, mais 7 paragraphes se ferment sur un « Donc » ou un « Du coup » conclusif, et 6 lignes dépassent 14 mots. |
| 11. Tics d'IA | 🟠 | 6 rafales de trois, une morale finale et une fausse opposition légère. |
| S1. 30 secondes | 🟠 | La question se termine à 34 s et le plan à 58 s, avec une ligne redondante. |
| S2. Pont | 🟢 | « D'abord, ce que ça change en vrai » démarre sur un résultat. |
| S3. Retournements | 🟠 | En général, il y en a un toutes les 25 à 40 s. Il reste 2 trous d'environ 50 s : de 3:22 (« Sauf que le modèle n'est pas seul ») à 4:12 (« Par contre, une fois cette conversation pleine »), et de 6:05 à 6:51, où seul « Une précision, quand même » coupe. |
| S4. Planté / récolté | 🟢 | « Même modèle » revient l. 56, « 28 secondes » revient l. 126 et « le compteur du début » l. 125. Seule la réflexion (l. 35-36) n'est pas récoltée. |
| S5. Personnages | 🟠 | « Celui qui a fait la mesure » existe (« quand il a poussé la conversation trop loin, ça a planté »), mais il est peu utilisé. |
| S6. Fin | 🟠 | Elle résume et se clôt sur une morale. La question « ces 18 tokens valent le coup ? » n'a pas de réponse explicite. |

---

## Problèmes bloquants

### B1. « 3 fois plus d'échecs » est faux

> « 13 % contre 36 %, sur ce travail, c'est presque 3 fois plus d'échecs. » (l. 157)

**Pourquoi ça coince :** c'est le rapport des **réussites** : 36 / 12,8 = 2,8. Les **échecs** donnent autre chose : 87 % contre 64 %, soit seulement 1,36 fois plus. C'est la phrase qui doit trancher le verdict, et elle est fausse. Un spectateur qui fait le calcul en commentaire la démonte.

**Correction :**
```
13 % contre 36 %, sur ce travail, c'est presque 3 fois moins de tâches réussies.
```
Ou, plus parlant :
```
Dans leurs tests, sur ce travail, le petit fichier rate presque 9 fois sur 10.
L'ancien, à peu près 2 fois sur 3.
```
(87,2 % et 64 % d'échecs, d'après les lectures graphiques F4 ≈ 12,8 et ≈ 36.)

### B2. « Le modèle rentre dans ta carte » est une promesse sur SA carte

> « Le modèle rentre dans ta carte, / et dans la mesure, il écrit plus de 5 fois plus vite. / Tant que la conversation reste courte, la place suffit. » (l. 147-149)

**Pourquoi ça coince :** la vitesse est bien rattachée à « dans la mesure », mais le chargement complet est promis à la carte du spectateur. F9 dit exactement l'inverse : 7,63 GB affichés ne garantissent pas un chargement complet sur toute carte « 8 Go ». La mesure tient avec 7 955 MiB libres et un bureau léger. C'est la seule phrase du script qui viole le cadre « rien ne promet au spectateur que SA carte fera ces chiffres ».

**Correction :**
```
Dans la mesure, le modèle tient en entier dans les 8 gigas,
et il écrit plus de 5 fois plus vite.
Tant que la conversation reste courte, la place suffit.
```

---

## Problèmes importants

### I1. Le passage de 18 à 12 mélange deux conditions de mesure

> « Par contre, une fois cette conversation pleine, / l'écriture tombe autour de 12 tokens par seconde. / Parce que les 18 du début, c'était avec une conversation vide. » (l. 84-86)

**Pourquoi ça coince :** les 18 tok/s sont mesurés avec un **cache 8 bits**, conversation vide (M2, `-ctk q8_0`). Les 11,6 sont mesurés avec un **cache 4 bits**, plein à environ 22,5K (F3). La phrase attribue toute la chute au remplissage, alors que le type de cache change aussi. En plus, le script laisse de côté la comparaison propre que donne F2 : en 8 bits, à 13,8K, ça tient encore 15,3. C'est pourtant la meilleure nouvelle de la partie.

**Correction :**
```
Par contre, en 4 bits, une fois cette conversation pleine,
l'écriture tombe autour de 12 tokens par seconde.
En 8 bits, même avec presque 14 000 tokens dedans,
elle tenait encore 15.
```

### I2. Le MTP n'est pas dans `sources.md`, et la phrase va au-delà de la source

> « Et au passage, le MTP de la vidéo précédente / est éteint dans cette mesure, pour garder de la place. / Donc les 2 gains ne s'additionnent pas. / Ici, tout vient du fichier qui rentre. » (l. 58-61)

**Pourquoi ça coince :**
- `script.md` cite « [F2 (MTP désactivé)] », mais F2 n'en dit rien. Le fait n'existe que dans `recherche-mesures.md` (M2, l. 38 : laisser de côté le projecteur vision et le fichier MTP) et dans la transcription (06:52 : ensemble, ils demandent plus de 2 Go).
- On ne sait pas si l'ancien essai à 3,2 tournait avec ou sans MTP. « Tout vient du fichier » et « les 2 gains ne s'additionnent pas » dit en général sont donc des déductions. Le grill V1 prévenait déjà : ne pas laisser entendre que le MTP est impossible sur 8 Go.
- Le spectateur qui n'a pas vu la vidéo du 19/11 ne sait pas ce qu'est le MTP.

**Correction :** ajoute ce fait à F2 dans `sources.md` (avec M2 l. 38 et la transcription 06:52), puis dans la voix :
```
Et au passage, le MTP,
le module qui doublait la vitesse dans la vidéo précédente,
est laissé de côté dans cette mesure, pour garder de la place.
Donc ce 18, c'est sans lui : n'additionne pas les 2 gains.
```

### I3. « Enfin rentrer » ramène le superlatif retiré

> « Donc on va voir le fichier qui fait enfin rentrer un modèle de 27 milliards dans 8 gigas, » (l. 12)

**Pourquoi ça coince :** F13 marque ❌ « le premier 2 bits qui tient ». Un IQ2_XXS à 7,21 GB est aussi listé, et F11 cite un UD-IQ1_M sur des cartes de 8 Go. « Enfin » veut dire « pour la première fois ». En plus, la ligne fait 18 mots, trop pour un seul souffle.

**Correction :** « Donc on va voir le fichier qui fait rentrer tout le modèle dans 8 gigas, » (15 mots, voir la réécriture des 30 s).

### I4. Les sources et les visuels de `script.md` sont décalés d'un paragraphe à partir du « deuxième prix »

**Constat :**
- Le titre « ### Et dans LM Studio ? » coiffe le paragraphe « Une précision, quand même : leurs tests tournent… », qui parle d'Unsloth. Ce paragraphe est sourcé [F5, F6, F7, F2] au lieu de F4.
- Le vrai paragraphe LM Studio (l. 189-195 de `script.md`) se retrouve sous « ### Le verdict par usage », avec le visuel « trois profils ».
- Le visuel « tableau tiré de la doc LM Studio » s'affiche donc pendant la phrase sur les conditions d'Unsloth.
- D'autres renvois sont aussi décalés :
  - [F4 (40,40 annoté ; ≈13 et ≈36…)] est placé après la question, pas après les chiffres ;
  - [F4 (36/13 ≈ 2,8)] est sur le verdict « bout de code », pas sur celui de l'agent ;
  - [F2, F14] est sur « Alors, verdict. » ;
  - [F15] est sur la morale finale, pas sur « Jeudi » ;
  - [F2 (lecture similaire), F7] est collé au calcul de 500 tokens, pas au paragraphe sur la lecture.
- Le CTA d'abonnement est rangé sous le titre « Le deuxième prix ».
- La table « Partie / Début / Mots » en tête repose sur ces titres : elle est à recalculer.

**Pourquoi ça coince :** le storyboard et le montage partent de `script.md`. Un visuel au mauvais endroit, c'est un tableau LM Studio à l'écran pendant qu'on parle des tests d'Unsloth.

**Correction :**
- Déplace « ### Et dans LM Studio ? » et son [VISUEL] juste avant « Et si tu es sur LM Studio ? ».
- Rattache « Une précision, quand même… » à la partie qualité, avec [F4].
- Mets le visuel « trois profils » juste avant « Alors, verdict ».
- Replace chaque renvoi sur la phrase qu'il prouve.
- Remonte le CTA à la fin de la partie « place ».
- Recalcule la table.

### I5. La réserve sur les tests d'Unsloth ne couvre que le mauvais score

> « Franchement, pour un modèle compressé à ce point, il tient bien. » (l. 106) … « Une précision, quand même : leurs tests tournent avec une très longue conversation et la réflexion poussée au maximum. » (l. 129-130) … « les exercices de programmation tiennent bien. » (l. 152)

**Pourquoi ça coince :** les 85 sur LiveCodeBench viennent de la même campagne, à 128K et en réflexion xhigh (F4). F4 et F10 disent explicitement que ces scores ne valident pas un usage à contexte court. Placée après l'agent seulement, la réserve laisse croire que le bon score s'applique tel quel sur 8 Go, et que seul le mauvais est « hors conditions ».

**Correction :** déplace la précision juste après « pas une vérification indépendante », avant les 2 scores, et ajoute un mot dans le verdict :
```
Et leurs tests tournent avec une très longue conversation
et la réflexion poussée au maximum.
Rien à voir avec une carte de 8 gigas.
Donc ces scores montrent où ça casse,
ils ne te donnent pas ton taux de réussite à toi.
```
Puis, au verdict :
```
Pour te faire aider sur un bout de code :
dans leurs tests, les exercices de programmation tiennent bien.
```

### I6. « 4 bits » et « le modèle complet » embrouillent la partie qualité

> « En fait, on peut compresser cette mémoire encore plus, en 4 bits. » (l. 82) … « Et le fichier en 4 bits, celui qui tournait à 3,2 tokens par seconde, » (l. 114) … « le modèle complet est autour de 89, » (l. 104)

**Pourquoi ça coince :**
- Le spectateur vient d'entendre « 4 bits » pour le cache. Trente secondes plus tard, « le fichier en 4 bits » désigne autre chose.
- « Le modèle complet » n'est jamais présenté : il pourrait le confondre avec l'ancien fichier, qui est « complet » par rapport au petit.
- Le même fichier a 3 noms dans la vidéo : « l'ancien fichier » (l. 41), « le fichier en 4 bits » (l. 114) et « le fichier plus lent » (l. 156).

**Correction :** garde un seul nom, « l'ancien fichier ».
```
le modèle complet, sans compression, est autour de 89,
```
```
Et l'ancien fichier, celui qui tournait à 3,2 tokens par seconde,
reste autour de 36 %.
```

### I7. Le verdict « agent » ne dit pas ce qu'il coûte, et la question de départ reste sans réponse

> « Pour un agent qui travaille seul sur un projet entier : / garde le fichier plus lent. » (l. 155-156) … « Et quand c'est la place ou la qualité qui bloque, / la vitesse ne règle plus rien. » (l. 162-163)

**Pourquoi ça coince :**
- « Le fichier plus lent » ne dit ni lequel, ni ce que ça coûte : 3,2 tokens par seconde, pour un agent qui écrit beaucoup.
- La question centrale (« qu'est-ce que ce fichier te fait perdre en échange ? ») ne reçoit pas de réponse en clair à la fin, et le « 9 fois sur 10 » du plan réécrit doit y être récolté.
- La dernière phrase est une morale assénée (S6).

**Correction** (à utiliser avec la réécriture du plan) :
```
Pour un agent qui travaille seul sur un projet entier :
garde l'ancien fichier, quitte à attendre à 3,2 tokens par seconde.
Parce que dans leurs tests, le petit fichier rate presque 9 fois sur 10.
Et là, aller plus vite pour se tromper plus souvent, ça ne sert à rien.

Alors, ce que ce fichier te fait perdre, tu le sais maintenant :
pour discuter, un peu de place et un peu de qualité,
pour un agent, beaucoup trop.
Donc la même carte de 8 gigas peut faire 2 métiers différents,
selon le fichier que tu lui donnes.
```
Supprime « Et quand c'est la place ou la qualité qui bloque, la vitesse ne règle plus rien. » Si tu gardes ton plan actuel, avec « on va voir si ces 18 tokens valent le coup », la même fin marche en remplaçant la 1re ligne par « Alors, ces 18 tokens, pour discuter, ils valent le coup. » La vidéo précédente finissait déjà sur une question et une réponse courte (« Alors, ta carte, bridée ? »).

### I8. Une petite morale en « Donc » à la fin de presque chaque paragraphe (axes 10 et 11)

> l. 37 « Donc une réponse courte à l'écran… », l. 60 « Donc les 2 gains… », l. 72 « Du coup, la taille du fichier… », l. 93 « Donc pour des échanges courts… », l. 116 « Donc sur ce travail-là… », l. 132 « Donc ces scores montrent… », l. 160 « Donc la même carte… »

**Pourquoi ça coince :** 8 lignes commencent par « Donc », et 7 d'entre elles concluent un paragraphe. Le taux de liaisons est bon (1,77 pour 100 mots), mais leur place est mécanique : on entend « bloc de faits, puis morale », toujours dans le même ordre. La vidéo précédente variait davantage, avec des réactions (« Donc même la Radeon double presque ») et un « En gros, c'est comme… ».

**Correction :** garde les « Donc » des l. 60, 116 et 160. Pour les autres :
- l. 93 → « Pour des échanges courts, tu ne vois même pas cette limite. »
- l. 37 → « Une réponse courte à l'écran peut donc cacher beaucoup plus de travail derrière. »
- Ajoute une réaction après le chiffre le plus dur de la vidéo, qui tombe aujourd'hui à plat :
```
Le petit fichier, environ 13 %.
Là, ça dégringole.
```

### I9. Les rafales de trois (axe 11)

> l. 3 « Même modèle, même carte, rien acheté. » · l. 29 « tu peux relancer, corriger, redemander. » · l. 69-71 « Le moteur… ton bureau… et surtout… la conversation » · l. 77 « Ta demande, l'historique, et tout ce que le modèle écrit » · l. 136-138 « la part du modèle…, la taille de la conversation, et la compression du cache » · l. 145 « discuter, poser une question, te faire expliquer un truc »

**Pourquoi ça coince :** une ou deux rafales passent, six se remarquent. Garde l. 3, qui frappe et qu'on récolte l. 56, et l. 69-71, qui liste un vrai budget mémoire.

**Correction :**
- l. 29 → « À 28 secondes, tu peux relancer, corriger. »
- l. 145 → « Pour discuter, te faire expliquer un truc : »
- l. 77 → « Ta demande et tout ce que le modèle écrit, sa réflexion comprise, / se partagent cette place. » Cette version récolte en plus la réflexion plantée l. 35-36, voir D4.

---

## Détails

- **D1. « ses chiffres » (l. 7)** n'a pas d'antécédent. Écris « ce sont les chiffres de celui qui a mesuré », la même formule que l. 83, qui reste anonyme.
- **D2. Fausse opposition légère (l. 52-53)** : « Sauf que ta carte n'a pas gagné de mémoire. / C'est le modèle qui a maigri. » Personne ne croit que la carte a gagné de la mémoire. L'image « a maigri » est bonne, alors garde-la seule : « Sauf que pour rentrer, le modèle a dû maigrir. »
- **D3. « En fait » (l. 82)** n'explique rien. Écris « Et tu peux compresser cette mémoire encore plus, en 4 bits. »
- **D4. La réflexion est plantée (l. 35-36) mais jamais récoltée.** L. 140, « l'option pour couper la réflexion » arrive sans que la voix ait dit pourquoi la couper. Récolte-la l. 77 (I9). La raison chiffrée de la transcription (environ 20 000 tokens de réflexion pour une page web) n'est pas dans F1-F16 : ne l'ajoute qu'après l'avoir sourcée.
- **D5. Le cuisinier (l. 44-45)** : « il peut être rapide, il fait des allers-retours » boite, et « allers-retours » sert déjà l. 28 dans un autre sens. Écris « il a beau être rapide, il passe son temps à courir chercher ce qui lui manque. » La « moitié » colle bien : 33 couches sur 65 sur la carte (M2).
- **D6. « Le modèle se charge sans problème » (l. 90)** : la source dit « se charge » (« will often still load »), pas « sans problème ». Écris « Le modèle se charge, / c'est la conversation qui finit par ne plus rentrer. » Tu peux aussi donner le seuil : « Et quand il a rempli la conversation au-delà de 24 000 tokens, ça a planté. » (F3)
- **D7. « conversation » revient 11 fois**, dont 4 en 8 lignes (l. 84-91). Remplace-le une ou deux fois par « la mémoire » ou « la discussion ».
- **D8. Lignes trop longues pour un souffle** (plus de 14 mots) : l. 12 (18), l. 72 (16), l. 116 (16), l. 153 (16), l. 44 (15), l. 158 (15). Le CTA de la l. 97 fait 14 mots : il passe, mais se coupe facilement en 2 (« Si cette vidéo t'aide à voir ce que ta carte peut vraiment faire, / abonne-toi. »).
- **D9. 14 lignes commencent par « Et ».** C'est oral et ça passe, mais enlève-en 3 ou 4 (l. 25, 88, 140).
- **D10. Ligne 1 :** « Sur une carte de 8 gigas » décrit en réalité une 1080 Ti de 11 Go bridée. La correction arrive à 14 s (« limitée à 8 gigas »), donc ça reste dans le cadre.
- **D11. LM Studio (l. 135-141)** n'apporte rien à faire au cœur du public. Sans tomber dans le tuto, raccroche-le à ce qu'il vient d'entendre : « Sa documentation a les mêmes réglages : la part du modèle sur la carte, la taille de la conversation, et le cache en 8 ou en 4 bits. »
- **D12. Notes périmées dans `sources.md`** (à corriger là-bas, pas dans la voix) :
  - F3 dit que le script n'utilise que 14000 et le plantage, alors que la V3 cite 22 500 et 12 ;
  - F4 dit LiveCodeBench « non chiffré en voix », alors que la V3 dit 89 et 85 (le recentrage du bas le signale, mais pas F4) ;
  - F10 parle d'un « crochet facultatif » qui a été supprimé ;
  - F2 ne mentionne pas le MTP (I2).
- **D13. README et calendrier :** la ligne de cette vidéo affiche encore le statut du 16/11. La note de tête du calendrier titre « 5 fois plus vite », alors que `sources.md` exclut une promesse ×5 dans le titre.
- **D14. Durée :** 1184 mots selon `wc -w`, soit 8:10. Avec les nombres lus en toutes lettres, compte environ 1 250 mots, soit à peu près 8:40. Tu restes dans la cible de 8 à 10 min.

---

## Promesses du hook et du plan : où elles sont tenues

| Promesse | Où | Verdict |
|---|---|---|
| « passe de 3,2 à 18 tokens par seconde » (l. 2) | l. 18-30 (ce que ça change), l. 40-50 (pourquoi), l. 148 | 🟢 |
| « Même modèle » (l. 3) | l. 52-56 (« il ne répond plus tout à fait pareil ») | 🟢 C'est nuancé, comme il faut. |
| « qu'est-ce que ce fichier te fait perdre en échange ? » (l. 10) | l. 63-133 (place, puis qualité) | 🟠 Elle est traitée, mais aucune phrase de la fin n'y répond en clair (I7). |
| « le fichier qui fait enfin rentrer… » (l. 12) | l. 47-50 | 🟢 C'est tenu, sauf « enfin » (I3). |
| « ce qu'il te coûte en mémoire de conversation » (l. 13) | l. 65-95 | 🟢 |
| « ce qu'il te coûte en qualité » (l. 14) | l. 99-133 | 🟢 |
| « le seul travail qu'il ne faut pas lui confier » (l. 15) | l. 111-127, puis l. 155-158 | 🟢 C'est l'agent. Le verdict « bout de code » ajoute une réserve, mais pas un 2e interdit. |
| « on va voir si ces 18 tokens valent le coup » (l. 16) | jamais explicitement | 🟠 (I7) |
| « Jeudi, les cartes par budget » (l. 165) | F15, calendrier | 🟢 |

## Où le spectateur risque de décrocher, et les passages trop prudents

**Décrochages probables :**
- **3:22 à 4:12** (l. 67-83) : le budget mémoire et la définition du cache KV arrivent sans retournement pendant 50 s. Le correctif I1 (« elle tenait encore 15 ») et un « Sauf que » plus tôt sur le 4 bits relancent la partie.
- **6:05 à 6:58** (l. 125-143) : 4 précautions s'enchaînent juste avant le verdict, celle sur les tests d'Unsloth, puis llama.cpp, LM Studio et la réflexion. C'est le moment où le spectateur attend la réponse. Le correctif I5 déplace la 1re plus tôt, et D11 raccourcit LM Studio.

**Trop prudent ou récité :**
- l. 22-23 « C'est juste une division, à vitesse constante, / mais ça donne l'idée. » Le cadre F16 exige le mot « division », mais en 2 lignes ça sonne comme une excuse. Écris « Juste une division, mais ça donne l'idée. » et laisse « vitesse constante » au visuel.
- l. 129 « Une précision, quand même : » est une annonce avant une réserve (voir I5).
- l. 146 « ce fichier a du sens. » C'est mou pour un verdict. Écris « c'est le bon fichier. » Ce n'est pas une promesse de résultat : c'est un choix par usage, appuyé sur F2 et F4.
- l. 118 « Et ça s'explique. » annonce au lieu de livrer. Supprime-le : « Quand tu lui demandes d'aider sur une fonction… » tient seul.

## Le verdict par usage : net et utile ?

- **Discuter, te faire expliquer** 🟢 : la réponse est nette, et la condition (« tant que la conversation reste courte ») est la bonne. Il ne reste qu'à remplacer « a du sens » et à corriger la promesse de B2.
- **Aide sur du code** 🟠 : le verdict est utile (« tu relis tout »), mais il s'appuie sur un score obtenu à 128K, avec réflexion xhigh, sans le dire (I5).
- **Agent** 🟠 : le sens est juste et appuyé par F4. Par contre, le chiffre est faux (B1), le fichier n'est pas nommé et son coût n'est pas dit (I7).
- **Ensemble** : 3 profils clairs, que le public peut reconnaître. Il manque une phrase finale qui réponde à la question de départ. Avec B1, B2 et I7, le verdict devient la partie la plus forte.

---

## Ce qu'il faut garder

- « Même modèle, même carte, rien acheté. » (l. 3), récolté l. 56 par « Le modèle garde son nom, mais il ne répond plus tout à fait pareil. » Le hook est honnête après coup.
- « Tu prépares un gros pavé pour éviter les allers-retours. / À 28 secondes, tu peux relancer… / Ça redevient une discussion. » C'est le passage qui fait sentir le chiffre.
- « Et là, les chiffres viennent d'Unsloth, ceux qui fabriquent le fichier. » La provenance est dite sans détour.
- « Alors, à ton avis, ça tient aussi quand on lui confie un vrai projet ? », un vrai moment d'engagement juste avant le chiffre qui fait mal.
- « Une réponse en 28 secondes que tu dois réparer / peut te coûter plus cher qu'une réponse lente qui marche. » La récolte du hook est la meilleure ligne du script.
- « Moi, j'ai rien testé », dit une fois, tôt, sans s'excuser pendant toute la vidéo.

---

## Plan d'action

1. Corrige B1 (« 3 fois moins de tâches réussies » ou « presque 9 fois sur 10 ») et B2 (« dans la mesure, le modèle tient… »).
2. Corrige I1 (le 8 bits contre le 4 bits, et ajoute le 15) et I2 (MTP : la source dans F2 et la formulation prudente).
3. Reprends les 30 s et le plan avec la réécriture : supprime « enfin » et la l. 8, et ajoute le pont « 9 fois sur 10 ».
4. Remets d'aplomb `script.md` : titres, visuels, renvois et table des parties (I4).
5. Fais ensuite la passe de style : réserve d'Unsloth avant les 2 scores, un seul nom pour l'ancien fichier, fin qui répond à « ça vaut le coup ? », moins de « Donc » conclusifs et moins de rafales.

---

## Format

| Contrôle | Résultat |
|---|---|
| Crochets, `⟦⟧`, parenthèses, `#` dans le téléprompteur | Aucun 🟢 |
| `teleprompteur.txt` et `.md` | Identiques (`diff` vide) 🟢 |
| Nombres en chiffres | Oui, aucun nombre écrit en lettres (« un seul » est permis) 🟢 |
| Nom de chaîne ou de créateur dans la voix | Aucun : « celui qui a fait la mesure », « ses chiffres » 🟢 |
| « J'ai testé », tutoriel (« ouvre », « clique ») | Aucun. « Moi, j'ai rien testé » est explicite 🟢 |
| Renvois | 1 dans le corps (« le MTP de la vidéo précédente », l. 58) et l'annonce de jeudi (l. 165) 🟢 |
| Liaisons strictes | 21 pour 1184 mots, soit 1,77 pour 100 mots : donc 8, sauf que 4, du coup 3, par contre 3, en fait 2, voilà 1. Avec alors (3), mais (3), parce que (1), et là (2), franchement, quand même et au passage : environ 33, soit 2,8 pour 100 mots 🟢. Leur place est mécanique (I8). |
| CTA abonnement | Placé après la partie « place » (4:47), hors des 30 s, et le service rendu est adapté 🟢 |
| Durée | 8:10 selon `wc`, environ 8:40 lu 🟢 |

---

## Tableau des faits

Les calculs ont été refaits. « Desc. » renvoie à la description de la vidéo source (F2/F3, M2). « Transcr. » renvoie aux sous-titres automatiques. La description dit 3,2 et 18,0, la voix dit « three » et « about five times » : le script s'appuie à juste titre sur la description.

| L. | Phrase de la voix | Source | Verdict |
|---|---|---|---|
| 1-2 | « tu changes un seul fichier, et Qwen 27B passe de 3,2 à 18 tokens par seconde » | F2 (desc. 3,2 et 18,0) | ✅ La mesure est unique, mais la l. 5 le dit aussitôt. « Un seul fichier » simplifie : le placement des poids change aussi (limites M2). |
| 3 | « Même modèle, même carte, rien acheté » | F2 | ✅ C'est la même carte physique. « Même modèle » est nuancé l. 56. |
| 5-6 | « une seule mesure publiée, sur une GTX 1080 Ti limitée à 8 gigas » | F2 (3 Go réservés, 7955 MiB) | ✅ |
| 7 | « Moi, j'ai rien testé » | Cadre | ✅ Voir D1 pour « ses ». |
| 8 | « plus de 5 fois et demie plus vite » | F14 : 18 / 3,2 = 5,625 | ✅ Le calcul est juste, mais il fait doublon dans les 30 s. |
| 12 | « le fichier qui fait enfin rentrer un modèle de 27 milliards dans 8 gigas » | F1, F13 ❌ | ⚠️ « Enfin » est un superlatif non établi (I3). |
| 19-21 | « 500 tokens… 2 minutes 36… 28 secondes » | F16 : 500 / 3,2 = 156,25 s = 2 min 36 ; 500 / 18 = 27,8 s | ✅ C'est présenté comme une division, à vitesse constante. |
| 26 | « 2 minutes et demie » | 2 min 36 ≈ 2,5 min | ✅ |
| 32-34 | « ce gain ne touche que l'écriture… la lecture reste à peu près la même » | F2 (210-280 tok/s, similaire) | ✅ |
| 35-36 | « cette réflexion, ce sont aussi des tokens à écrire » | F16 (exclusions) | ✅ C'est le mécanisme général, sans chiffre. |
| 41-43 | « L'ancien fichier ne tenait pas dans la carte. Une partie tournait dans la RAM… » | M2 (33/65 couches sur le GPU, i9-9900K), transcr. 01:01 | ✅ « La carte passait son temps à l'attendre » est une image, acceptable. |
| 47 | « Le nouveau fichier, lui, tient entièrement dans la carte » | M2 (64 couches sur le GPU) | ✅ Dans la mesure, oui. |
| 48-49 | « UD-IQ2_XS, 7,63 gigas, Unsloth, le 11 novembre » | F1 (7,63 GB, Dynamic V3.1 annoncé le 11/11), transcr. 00:00 | ✅ « Sorti » le 11/11 : c'est la date d'annonce de la mise à jour, ce qui suffit. |
| 54-55 | « nombres rangés avec moins de précision : c'est la quantification » | F1 (limite « 2 bits ») | ✅ |
| 58-61 | « le MTP… éteint dans cette mesure, pour garder de la place. Donc les 2 gains ne s'additionnent pas. Ici, tout vient du fichier » | Absent de `sources.md`. M2 l. 38 et transcr. 06:52 | ⚠️ Le fait vrai n'est pas tracé dans F2. La conclusion va au-delà de la source (I2). |
| 67-71 | « 7,63 gigas, ta carte en a 8. Sauf que le modèle n'est pas seul… » | F9 | ✅ La voix ne fait pas de soustraction, conformément à F9. |
| 74-76 | « cache KV… en 8 bits… environ 14 000 tokens » | F3 (≈ 14K, `-c 14336`) | ✅ |
| 82-83 | « en 4 bits… environ 22 500 tokens » | F3 (≈ 22,5K) | ✅ |
| 84-85 | « une fois cette conversation pleine, l'écriture tombe autour de 12 tokens par seconde » | F3 (11,6, cache 4 bits plein) | ✅ L'arrondi 11,6 → 12 est correct. |
| 86 | « les 18 du début, c'était avec une conversation vide » | F2 / M2 (18,0 : cache 8 bits, vide) | ⚠️ C'est exact pris seul, mais la phrase donne comme seule cause ce qui mélange aussi le type de cache. Le 15,3 en 8 bits à 13,8K n'est pas utilisé (I1). |
| 88-91 | « quand il a poussé la conversation trop loin, ça a planté. Le modèle se charge sans problème » | F3 (fenêtre de 25,6K, plantage au-delà d'environ 24K), transcr. 06:52-07:13 | ✅ « Sans problème » en fait un peu trop (D6). |
| 97 | CTA | Règle du 12/11 | ✅ |
| 100-101 | « les chiffres viennent d'Unsloth… pas une vérification indépendante » | F4 | ✅ |
| 103-105 | « LiveCodeBench… complet autour de 89, petit fichier autour de 85 » | F4 (88,62 annoté ; point ≈ 84,5 lu sur le graphique), transcr. 05:08 (« 84 and 1/2 ») | ✅ Les arrondis sont annoncés par « autour ». |
| 106 | « il tient bien » | F4 : 84,5 / 88,62 = 95 % | ✅ L'avis est fondé, mais la réserve sur les conditions arrive trop tard (I5). |
| 111-113 | « test d'agent… complet environ 40 %… petit fichier environ 13 % » | F4 (40,40 annoté ; ≈ 12,8 lu sur le graphique), transcr. 05:30 | ✅ |
| 114-115 | « le fichier en 4 bits, celui qui tournait à 3,2… autour de 36 % » | F4 (UD-IQ4_XS ≈ 36), F2 (UD-IQ4_XS = ancien fichier) | ✅ Le fait est juste, mais « 4 bits » est ambigu (I6). |
| 116 | « le petit fichier réussit 3 fois moins souvent que le modèle complet » | 40,4 / 12,8 = 3,16 | ✅ |
| 130 | « une très longue conversation et la réflexion poussée au maximum » | F4 (256K pour les agents, 128K pour le reste, xhigh) | ✅ Valable pour les 2 scores, pas seulement l'agent (I5). |
| 136-138 | « Sa documentation décrit les mêmes leviers » | F5 (déchargement GPU, contexte), F6 (cache K/V) | ✅ |
| 139 | « toutes ces vitesses ont été mesurées dans llama.cpp » | F2, M2 | ✅ |
| 140-141 | « l'option pour couper la réflexion dépend de la façon dont le modèle est configuré » | F7 (template `enable_thinking`) | ✅ |
| 147 | « Le modèle rentre dans ta carte » | F9 contredit | ❌ C'est une promesse sur la carte du spectateur (B2). |
| 148 | « dans la mesure, il écrit plus de 5 fois plus vite » | F14 : 5,625 à vide, 15,3 / 3,0 = 5,1 à 13,8K | ✅ C'est vrai dans les 2 conditions. |
| 152 | « les exercices de programmation tiennent bien » | F4, F10 | ⚠️ C'est vrai dans leurs tests seulement, et ça ne certifie pas une aide sur un vrai fichier (I5). |
| 156 | « garde le fichier plus lent » | F4 (36 contre 13), transcr. 05:30 | ✅ Le sens est juste, mais le fichier n'est pas nommé et le coût n'est pas dit (I7). |
| 157 | « 13 % contre 36 %… presque 3 fois plus d'échecs » | 36 / 12,8 = 2,8 (réussites) ; 87,2 / 64 = 1,36 (échecs) | ❌ C'est faux (B1). |
| 165 | « Jeudi, on regarde les cartes par budget » | F15 (jeudi 26/11), calendrier l. 26 | ✅ |
