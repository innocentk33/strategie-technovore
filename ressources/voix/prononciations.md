# Banque de reprises et de prononciations

Ici sont rangées tes reprises de voix, celles que tu enregistres pour remplacer des passages de la voix clonée. Elles servent pour la vidéo du jour, et ensuite pour toutes les autres : un nom de carte bien dit une fois n'est plus à réenregistrer.

## Où sont les fichiers

Deux enregistrements, tous deux du 21/11 :

### 1. Les noms de cartes, nettoyés : `reprises/2026-11-21-cartes/`, la banque à utiliser en premier

- **Le fichier brut** est [`reprises/2026-11-21-cartes-graphiques-brut.flac`](reprises/2026-11-21-cartes-graphiques-brut.flac) : 344,8 s, 44,1 kHz, 16 bits, mono, ta vraie voix. C'est la liste de noms que tu as lue pour cette vidéo et pour les suivantes.
- **Les noms découpés** sont dans [`reprises/2026-11-21-cartes/`](reprises/2026-11-21-cartes/) : 117 FLAC, un par nom ou par prise, en 48 kHz et 24 bits. Ils sont **nettoyés** :
  - déclippage ;
  - coupe sous 70 Hz, débruitage léger ;
  - égaliseur de la voix de la chaîne : −2 dB à 260 Hz, +1 dB à 3,4 kHz, de-esser ;
  - compresseur doux de la même chaîne (seuil −22 dB, 2:1) ;
  - parole à −16 LUFS, crête à −1,5 dBFS au plus, avec un limiteur doux si besoin (de 1 dB en médiane) ;
  - 0,15 s de silence de chaque côté ;
  - **ni tempo ni changement de hauteur**.

  Les noms coupés dans un enchaînement (« Intel, ASUS, Gigabyte », « 8 12 16… ») ont une marge plus courte du côté du mot voisin.
- **L'index** est [`reprises/2026-11-21-cartes/index.json`](reprises/2026-11-21-cartes/index.json). Pour chaque fichier, il donne :
  - l'étiquette et le texte dit ;
  - le groupe : cette vidéo, NVIDIA, AMD, Intel, mémoire ou noms ;
  - les temps dans le brut ;
  - le numéro de la prise, le nombre de prises et `meilleure` : la prise sans saturation, puis la vérifiée, puis la plus récente ;
  - `verifie` ;
  - le gain, la réduction du limiteur ;
  - la vidéo où le nom a servi, avec son temps et le traitement d'insertion.

### 2. Les reprises de phrases : `reprises/2026-11-21/`

- **Le fichier entier**, tel que tu l'as enregistré, est [`reprises/2026-11-21-reprises-32go.flac`](reprises/2026-11-21-reprises-32go.flac). Il fait 165,6 s, en 44,1 kHz, 16 bits, mono, et c'est ta vraie voix, sans aucun traitement.
- **Les passages découpés** sont dans [`reprises/2026-11-21/`](reprises/2026-11-21/) : 30 fichiers FLAC bruts. Chacun garde 0,15 s de silence de chaque côté et n'a reçu ni accélération ni retouche.
- **L'index** est [`reprises/2026-11-21/index.json`](reprises/2026-11-21/index.json). Pour chaque passage, il donne :
  - le fichier, le texte dit et une étiquette ;
  - les temps dans le fichier entier ;
  - la classe : phrase de remplacement, nom de carte ou passage non utilisé ;
  - `verifie` ;
  - la vidéo où le passage a servi, avec son temps dans la voix et le traitement appliqué.

Les FLAC sont versionnés, pas les WAV. Pour une prochaine série de reprises, crée un dossier `reprises/AAAA-MM-JJ/` sur le même modèle.

## Les noms de la banque nettoyée (`2026-11-21-cartes/`)

**Pour cette vidéo** : RTX 5060 Ti, 5060 Ti, RX 9060 XT, 9060 XT, Arc A770, Arc Pro B65, Arc Pro B70, Radeon AI PRO R9700, R9700 seul, RTX 5090, RTX 5080, Tesla V100, Mac mini M6, Ryzen AI Max+, « 16 gigas et demi ».

**Pour les prochaines vidéos** :
- **NVIDIA** :
  - en « trois mille / quatre mille » : RTX 3060, RTX 3060 Ti, RTX 3070, 3080, 3090, 4060, 4060 Ti, 4070, 4070 Super, 4070 Ti Super ;
  - en « quarante » : 4080, 4080 Super, 4090 ;
  - en « cinquante » : 5060, 5070, 5070 Ti ;
  - puis toute la série avec « RTX » devant, en « trois mille / quatre mille / cinq mille » : RTX 3060 à RTX 4090, RTX 5060, RTX 5070, RTX 5070 Ti.
- **AMD** : RX 7600 XT (2 prises), RX 7800 XT, RX 7900 XT, RX 7900 XTX, RX 9060, RX 9070, RX 9070 XT, puis sans « RX » : 7600, 7600 XT, 7800, 7800 XT, 7900, 7900 XT, 7900 XTX, 9060, 9070, 9070 XT.
- **Intel** : Intel Arc B580, Intel Arc B570, Arc B580 (2 prises), Arc B570, Arc A750, B570, A750.
- **Mémoire** : 8, 12, 16, 24, 32, 48, 64 et 128 seuls, puis « 8 gigas de VRAM » à « 128 gigas de VRAM ».
- **Noms** : NVIDIA, AMD, Intel (2 prises chacun), ASUS, Gigabyte, ASRock, MSI, GMKtec, GMKtec EVO-X2, Hugging Face, llama.cpp, LM Studio, Ollama, CUDA, ROCm, PCIe, Qwen, DeepSeek, et Claude Fable (hors de la liste).

**Absents du fichier** : « Ti » seul, « XT » seul, « Super » seul.

**Incertains** (`verifie: false`, à confirmer à l'oreille) :
- 5070 Ti Super et RTX 5070 Ti Super : cette carte n'existe pas, tu as sans doute lu « 5070 Ti » puis « Super » d'un trait ;
- la 2e prise de RX 7600 XT, dont le « XT » est faible ;
- Intel Arc A750, dont le « Arc » ne s'entend pas ;
- la 2e prise de RX 9060 XT, dont la fin est incertaine ;
- DeepSeek, coupé au plus près du mot précédent.

**Ta prononciation a changé pour deux séries** : tu dis maintenant « trois mille soixante » (3060) et « quatre mille soixante », là où la banque précédente avait « trente soixante ». Pour les 40, tu as gardé « quarante quatre-vingts » (4080) ; pour les 50, « cinquante soixante » dans la liste sans « RTX », et « cinq mille soixante » avec « RTX ».

Les noms de l'ancienne banque que celle-ci remplace sont marqués `remplace_par` dans `reprises/2026-11-21/index.json`.

## Les noms de l'ancienne banque (`2026-11-21/`, bruts)

La transcription automatique (wav2vec2) entend mal les noms de cartes. Elle transcrit ton « Ti » par « i », « it », « dix » ou « xt ». Les étiquettes marquées `verifie: false` ont donc été déduites de l'ordre de ta liste et d'une comparaison de timbre. Confirme-les à l'oreille avant de t'en servir.

| Fichier | Ce que tu dis | Vérifié |
|---|---|---|
| `carte-5060.flac` | « cinquante soixante » (5060) | oui |
| `carte-5070.flac` | 5070, probablement | non |
| `carte-5070-ti.flac` | 5070 Ti, probablement | non |
| `carte-5060-ti.flac` | 5060 Ti, mot isolé, probablement | non |
| `carte-3060.flac` | « trente soixante » (3060) | oui |
| `carte-3070.flac` | 3070, probablement | non |
| `carte-3070-ti.flac` | 3070 Ti, probablement | non |
| `carte-5080.flac` | 5080, probablement. À la comparaison de timbre, il est plus proche de « 5080 » que de « 5090 ». | non |
| `carte-9060.flac` | « neuf mille soixante » (9060) | oui |
| `carte-9060-xt.flac` | « neuf mille soixante XT » (9060 XT) | oui |
| `carte-r9700.flac` | « R neuf mille sept cents » (R9700) | oui |
| `carte-rtx-5060-ti.flac` | « RTX cinquante soixante Ti » | oui |
| `carte-rtx-5060-ti-prise2.flac` | RTX 5060 Ti, 2e prise, probablement : une syllabe suit « soixante », la transcription ne l'a pas notée | non |

Dans une phrase, ton « Ti » est court et se lie au chiffre : « cinquante soixante-Ti ». Pour greffer un nom dans une phrase, prends-le dans une phrase dite à vitesse normale, par exemple dans `phrase-occasion-5060-ti.flac` ou `phrase-pas-encore-de-carte.flac`. Un mot isolé est plus lent et plus appuyé. C'est ce qui avait été fait pour « Et les 5060 Ti et 9060 XT » dans la vidéo 32 Go, à 3:24, avant que le 2e lot ne remplace tous les « 5060 Ti » par le nouvel enregistrement.

Tous ces noms sont maintenant dans la banque nettoyée (`2026-11-21-cartes/`), qui les remplace, sauf `carte-3070-ti`.

## Les phrases et les fins

- Les **phrases** (`phrase-*.flac`) ont été dites pour la vidéo 32 Go. Elles ne resservent telles quelles que si le même texte revient.
- Les **fins** sont réutilisables d'une vidéo à l'autre :
  - `fin-mauvais-achat.flac` : « Si cette vidéo t'a évité un mauvais achat, abonne-toi. »
  - `fin-a-la-prochaine.flac` : « Et on se dit à la prochaine, salut ! »
  - `fin-abonne-toi-booste.flac` : la fin longue (« n'oublie pas de t'abonner à la chaîne, booste la vidéo, ça m'aide vraiment… »). Elle n'a pas été mise dans la vidéo 32 Go, et son tout début est mal transcrit, donc à réécouter.
- `faux-depart-en-france.flac` et `phrase-prix-francais-prise1.flac` sont des prises non utilisées, gardées au cas où.

## Comment réutiliser un passage dans une vidéo

Le script qui le fait est `scripts/reprises.py`, dans le projet HyperStudio de la vidéo 32 Go (`~/HyperStudio/premium-noir/2026-11-qwen-27b-32go/`). Il a deux lots : `LOT=1` pour les phrases, `LOT=2` pour les « 5060 Ti », « 16 gigas et demi » et le hook en ×1,1. Copie-le dans le projet de la nouvelle vidéo et remplis une liste comme `REPL` ou `REPL2`. Pour chaque passage, tu donnes :
- la phrase à remplacer, ou les mots exacts pour une greffe ;
- la fenêtre dans le fichier de reprises ;
- le texte que tu dis.

Voici ce qu'il fait, dans l'ordre :

Le script part toujours du **fichier brut**, pas de la version nettoyée de la banque : il fait son propre nettoyage, réglé pour la voix clonée. La banque nettoyée sert à écouter, à choisir la prise, et aux vidéos où ta voix n'est pas mélangée à un clone.

1. **Préparation du fichier** : passage en 48 kHz, déclippage, coupe sous 70 Hz, débruitage léger (`afftdn`), puis égaliseur d'appariement vers le spectre moyen de la voix clonée (75 % de l'écart, ±6 dB au plus).
2. **Pauses** : il ramène les silences entre tes mots aux cibles de la voix, mesurées après tempo :
   - fin de phrase : 0,38 s ;
   - deux-points : 0,24 s ;
   - virgule : 0,20 s (0,26 s après un long silence) ;
   - sans ponctuation : 0,12 s.

   Les souffles et les bruits de ces pauses sont remplacés par le fond de la voix clonée, si bien qu'il n'y a jamais de trou de silence numérique.
3. **Hauteur** : ta voix est environ 1,8 demi-ton plus grave que le clone (107 Hz de médiane contre 119). Le script la remonte par PSOLA, en gardant les formants : de 1,82 demi-ton pour une phrase entière, en restant à 1 demi-ton au plus de la voix autour, et à la hauteur locale pour une greffe en milieu de phrase (2,5 au plus).
4. **Tempo ×1,1**, à cette étape et jamais dans la banque. Tu l'as demandé : « dans la reprise, le son doit être en 1.1 ». Si un passage reste nettement plus lent que la voix autour, ajoute un peu de tempo pour ce passage, mesure-le et note-le, sans dépasser ×1,25. Dans la vidéo 32 Go, « ta conversation » est passée à ×1,25, « La paire de 9060 XT… » à ×1,2, les six « 5060 Ti » à ×1,2 et « 16 gigas et demi » à ×1,25. Un nom lu dans une liste est plus lent qu'un nom dit dans une phrase. Une greffe de nom se prend donc dans la version avec préfixe, plus liée : le « 5060 Ti » de `rtx-5060-ti`, pas `5060-ti` isolé.
5. **Niveau et fond** : le niveau de parole est calé sur celui des mots remplacés. Le collage se fait dans la pause, ou au milieu de l'écart entre deux mots pour une greffe, avec des fondus de 12 ms. Le fond de la voix clonée reste continu dessous.
6. **Sorties** : le même mastering que la voix (−16 LUFS, −2,5 dBTP), puis une nouvelle écriture de `voix.words.json` et `voix.phrases.json` avec tes mots. Le script note tout dans `edit-plan/voice-retouches.json` et produit une bobine d'écoute, `renders/controle-retouches.m4a`.

Ensuite, la durée de la voix a changé, donc tout ce qui en dépend est à refaire :
- les ancres de `montage.py` (lance `MC_DRY=1`) ;
- `check` et les instantanés ;
- le rendu 1080p ;
- les chapitres, les sous-titres et les temps de l'écran de fin dans `upload.md`.

## Conseils pour tes prochaines reprises

- **Enchaîne les phrases** : dis chaque phrase en entier, d'une traite, avec un silence d'au moins une seconde avant et après. C'est plus facile à couper proprement qu'un bout de phrase.
- **Moins de bruit** : enregistre un peu moins près du micro, ou baisse le gain. Le fichier du 21/11 sature à trois endroits (vers 47,6 s, 64,7 s et 95,9 s) et son bruit de pièce est à −66 dBFS. Le déclippage et le débruitage l'ont rattrapé, mais un fichier propre au départ sonnera plus naturel.
- **Mélange de voix** : une greffe de ta vraie voix au milieu d'une phrase clonée s'entend plus qu'une phrase entière. Préfère réenregistrer la phrase complète.
