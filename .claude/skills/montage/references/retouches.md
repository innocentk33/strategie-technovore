# Retouches après livraison

Deux sortes de retouches arrivent après une livraison :
- **montage** (un plan, un mème, un texte) : on modifie `montage.py`, on relance la boucle courte (`verifications.md`) sur les plans touchés, puis un 1080p ;
- **voix** : l'auteur renvoie des reprises (sa vraie voix, ou sa voix clonée) pour remplacer des passages, et souvent des prononciations de références de cartes.

## Retouches de voix par l'auteur

Méthode appliquée le 21/11/2026 à « 32 Go pour Qwen 27B » : 15 passages de sa **vraie voix** collés dans la voix **clonée** (11 phrases entières et 4 greffes en milieu de phrase, dont « 5060 Ti »). Script reproductible : `2026-11-qwen-27b-32go/scripts/reprises.py` (lis son en-tête). Rapport : `edit-plan/voice-retouches.json`. Bobine : `renders/controle-retouches.m4a` (+ `.txt`).

### Où ranger les reprises (la banque)
Tout ce que l'auteur enregistre resservira (un nom de carte bien dit une fois n'est plus à réenregistrer) :
- le **fichier entier**, brut, versionné : `<DEPOT>/ressources/voix/reprises/AAAA-MM-JJ-reprises-<video>.flac` (premier : `2026-11-21-reprises-32go.flac`, 165,6 s, 44,1 kHz, 16 bits, mono) ; une copie existe aussi dans `<PREMIUM>/style/voice-presets/prononciations/` ;
- **un FLAC brut par passage** dans `ressources/voix/reprises/AAAA-MM-JJ/` : 0,15 s de marge prise sur le silence, **sans tempo ni retouche** (les traitements se font à la vidéo, jamais dans la banque) ; noms `carte-<ref>.flac`, `phrase-<sujet>.flac`, `fin-<…>.flac`, `faux-depart-<…>.flac` ;
- `index.json` dans ce dossier : pour chaque passage, fichier, texte, étiquette, temps dans le fichier entier, classe (phrase de remplacement, nom de carte, passage non utilisé), `verifie` (vrai ou faux), et `a_servi` (vidéo, temps dans la voix, traitement) ;
- le guide lisible : `ressources/voix/prononciations.md` (cartes déjà enregistrées et vérifiées, fins réutilisables, conseils d'enregistrement à l'auteur). Mets-le à jour à chaque nouvelle série.
Le découpage de 2026-11-21 a été fait par `2026-11-qwen-27b-32go/retouches/banque.py` (outil de travail : chemins en dur, à adapter).

**Avant d'en demander une nouvelle**, regarde dans la banque : les fins (« Si cette vidéo t'a évité un mauvais achat, abonne-toi. », « Et on se dit à la prochaine, salut ! ») et plusieurs références de cartes y sont déjà.

### Déroulé
1. **Sauvegarde avant toute écriture**, dans `retouches/avant/` du projet : `assets/audio/voix.flac`, `sources/voix-avant-master.flac`, `sources/voix.words.json`, `sources/voix.phrases.json`, `edit-plan/voice-*.json`, `scripts/montage.py`, `chapitres.txt`, `index.html`, et, depuis le dépôt, `upload.md` et les deux `.srt`. `premium-noir/` n'est pas un dépôt git ; la 4K livrée ne s'écrase pas. `reprises.py` repart toujours de `retouches/avant/voix-avant-master.flac` (jamais réécrit) : on peut le relancer autant de fois qu'il faut.
2. **Range le fichier** dans la banque (fichier entier), puis **transcris-le** :
   ```bash
   uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py retouches/reprise-16k.wav retouches/reprise.words.json
   ```
   (après `ffmpeg -v error -y -i <fichier de l'auteur> -ar 16000 -ac 1 retouches/reprise-16k.wav`). wav2vec2 entend mal les références : le « Ti » devient « dix », « soixante- », « -ht », « i » ou « xt ». **Étiquette les noms d'après la liste des cartes du script** (l'ordre de sa liste aide), compare au besoin le timbre, et marque chaque étiquette `verifie: true` ou `false`.
3. **Range chaque segment dans une des trois classes**, en le rapprochant de `voix.phrases.json` et du téléprompteur :
   - **phrase du script**, même reformulée : elle remplace la phrase clonée, et **le texte de l'auteur prime** (sous-titres et mots suivent ce qu'il dit) ; vérifie qu'aucun détail n'est perdu par la reformulation (piège : « sur leboncoin » disparu en R3), et signale-le ;
   - **nom isolé** (une référence dite seule) : il va dans la banque, et ne se greffe que là où la voix est douteuse ; pour une greffe, prends plutôt le nom **dans une phrase dite à vitesse normale** (« 5060 Ti » pris dans la reprise de la phrase 41 pour la greffe G1), un mot isolé est plus lent et plus appuyé ;
   - **segment hors script** (fin longue, faux départ) : on ne l'insère pas, il va dans la banque et on le signale à l'auteur.
   S'il y a plusieurs prises d'un même passage, garde la meilleure ; les autres vont dans la banque (`…-prise1`).
4. **Remplis la table `REPL`** de `scripts/reprises.py` (copie-le depuis le 32 Go) : une entrée par passage, `dict(id='R3', kind='phrase', ph=[41], rep=(71.40, 78.32), text='…', why='…')` pour une phrase entière, `kind='greffe'` avec `words=(début, fin)` dans la voix pour une greffe ; `tempo=` et `tempo_note=` si le ×1,1 ne suffit pas.
5. **Lance** depuis la racine :
   ```bash
   uv run --no-project --with praat-parselmouth --with numpy --with scipy python scripts/reprises.py
   ```
   Réglages (ceux du 32 Go, à garder) :
   - préparation une fois : 48 kHz, déclippage (le fichier du 21/11 saturait à trois endroits), coupe sous 70 Hz, débruitage léger (`afftdn`), égaliseur d'appariement vers le spectre moyen de la voix clonée (75 % de l'écart, ±6 dB) ;
   - pauses entre mots ramenées aux cibles de la voix (point 0,38 s, deux-points 0,24, virgule 0,20 ou 0,26 après un long silence, sans ponctuation 0,12), souffles remplacés par le fond de la voix clonée : **aucun trou numérique** ;
   - **hauteur** : sa vraie voix est à 107 Hz de médiane, le clone à 119 Hz ; PSOLA (formants gardés) de **+1,82 demi-ton** pour une phrase entière, à la hauteur locale pour une greffe (2,5 au plus), et jamais plus de 1 demi-ton d'écart avec la voix autour ;
   - **tempo ×1,1** compté depuis le brut, demandé par l'auteur (« dans la reprise, le son doit être en 1.1 ») ; ×1,2 ou ×1,25 seulement si le passage reste nettement plus lent que la voix remplacée, **mesuré et noté** (32 Go : « ta conversation » ×1,25, « La paire de 9060 XT… » ×1,2) ;
   - niveau de parole calé sur les mots remplacés (écart final ±1,7 LU), collage dans la pause (ou au milieu de l'écart entre deux mots pour une greffe), fondus égale puissance de 12 ms, fond de la voix clonée continu dessous ;
   - même mastering que `voix.py` : −16 LUFS, LRA 9, −2,5 dBTP visés (32 Go : −16 LUFS, −2,4 dBTP mesurés).
   Il réécrit `voix.words.json` et `voix.phrases.json` (temps décalés, mots de l'auteur), `edit-plan/voice-retouches.json` et la bobine.
6. **Contrôle, sans nouvel agent de revue de voix** : nouvelle transcription wav2vec2 de `assets/audio/voix.flac`, vérification de **tous** les chiffres et références, `verif_texte.py` ; écoute par mesure de la bobine `renders/controle-retouches.m4a` (chaque passage repris de 3 s avant à 3 s après, séparés par un bip), hauteur et niveau de chaque raccord.
7. **Cascade** (la durée de la voix a changé, tout ce qui suit est périmé) :
   - avant de toucher la voix, enregistre les débuts de plans : `MC_DRY=1` du 32 Go les écrit dans `edit-plan/dry-starts.json` (`[["s-001", 0], ["s-002", 4.02], …]`) ; après, relance `MC_DRY=1` et compare : chaque plan doit rester sur sa phrase (à 0,06 s près du décalage attendu) ;
   - corrige les ancres `T()` cassées par une reformulation (un mot que l'auteur ne dit plus) ;
   - `check`, planches autour de **chaque** retouche, rendu 1080p (32 Go : `renders/q32-montage-v4.mp4`) ;
   - `chapitres.txt` et chapitres de `upload.md`, recalés dans les silences ;
   - `.fr.srt` et `.en.srt` : temps recalés sur les nouveaux mots, texte réécrit pour les phrases reformulées (outil de travail du 32 Go : `retouches/srt_reprises.py`) ;
   - temps de l'écran de fin dans `upload.md`.
8. **Pas de 4K sans l'accord de l'auteur** : la carte blanche couvrait la première livraison, pas les retouches.

### Contrôle systématique des noms (avant de livrer une voix clonée)
Le piège du 32 Go : le clone a dit « èr quatre-vingt-dix-sept cents » pour R9700 aux trois occurrences (le texte envoyé au moteur disait « R quatre-vingt-dix-sept cents »), et c'est l'auteur qui l'a entendu, au v5. Ce contrôle se fait **avant la première livraison** d'une voix clonée, puis après chaque lot de reprises :
1. **Liste chaque occurrence**, dans `sources/voix.words.json`, de chaque nom de carte, de produit ou de marque : RTX, RX, Arc, Radeon, les références (5060 Ti, 9060 XT, A770, B65, B70, R9700, 5090, 5080, V100, M6…), Ryzen AI Max+, NVIDIA, AMD, Intel, ASUS, Gigabyte, ASRock, GMKtec, Hugging Face, llama.cpp, CUDA, ROCm, PCIe, Qwen… Pense aux formes collées (« d'ASUS », « l'Intel »).
2. **Transcris en verbatim** avec wav2vec2 ±1 s autour de chacune (la transcription de toute la voix suffit), et compare :
   - à la **forme attendue** : les conventions d'écriture pour VoiceStudio (Ti = « té i », XT = « ix té », R9700 = « èr neuf mille sept cents », ASUS = « azus », B65 = « bé soixante-cinq », 9060 XT = « quatre-vingt-dix soixante ix té ») et le texte réellement envoyé au moteur (`voicestudio-stories.txt` du projet), qui peut lui-même être faux ;
   - à la **prononciation de l'auteur dans la banque** (`<DEPOT>/ressources/voix/reprises/2026-11-21-cartes/` et sa transcription) : mêmes nombres, durée, nombre de syllabes.
3. **Classe** chaque occurrence en trois verdicts :
   - **juste** ;
   - **faux** : on entend un autre nombre ou un autre mot, par exemple « quatre-vingt-dix » au lieu de « neuf mille » ;
   - **douteux**.

   wav2vec2 déforme tous les noms (« radion », « jigabait », « hertic ») : seul compte un **nombre ou un mot différent**.
   **Limite : wav2vec2 ne distingue pas « té » de « ti »** (« XT » transcrit « xt » dans les deux cas). Au 32 Go, le « 9060 XT » de 3:23 a été classé juste au v6 alors que l'auteur entendait « ix ti », avec un autre timbre. Pour chaque « XT » et chaque « Ti » en voix clonée, fais trois mesures :
   - **la durée de la dernière voyelle**, comparée à une occurrence validée par l'auteur : le fautif durait 20 ms, contre 80 ms pour le validé ;
   - **le timbre** : distance MFCC (moyenne des coefficients 1 à 19 sur la parole) à la voix qui l'entoure. Le fautif, dans un bloc strata, était à 50 de la greffe de l'auteur juste avant, contre 25 pour sa propre voix ;
   - **les formants F1/F2 de la voyelle**, qui ne tranchent pas seuls sur une voyelle aussi courte.

   En cas de doute, demande l'écoute à l'auteur plutôt que de conclure « juste ».
4. **Greffe la version de l'auteur sur tous les « faux »**, tirée du fichier brut de la banque (les réglages sont ceux de `reprises.py`, `LOT=3` du 32 Go). Pour les « douteux », ne greffe que si le raccord est propre : un mot voisin collé à moins de 50 ms (« 5090 a aussi ») donne un mauvais raccord. Dis-le.
5. **Écris le tableau** dans `edit-plan/verif-noms-vN.json` (temps, nom, attendu, entendu, verdict, action) et mets dans le rapport les faux et les douteux en détail, plus le compte des justes. 32 Go, v5 : 47 occurrences, 3 faux (les trois R9700, greffés), 1 douteux (RTX 5090, non greffé), 37 justes, et 6 occurrences déjà dans la voix de l'auteur.

### Choisir entre plusieurs candidats pour une greffe
Quand un mot a plusieurs sources possibles, essaie-les toutes avec le même pipeline et mesure-les dans la voix finale. Au 32 Go (lot 4, `LOT=4 CAND=a|b|r13`, résultats dans `retouches/candidats-xt.json`), il y avait trois sources pour un « 9060 XT » :
- **le clone validé ailleurs** : 47 de distance MFCC à la greffe de l'auteur juste avant, 33 au clone qui suit ;
- **sa banque de noms**, lue isolée et donc plus lente : 23 et 48 ;
- **sa reprise de phrase**, en parole liée : 25 et 46, une sonie plus proche des voisins, et la même forme que le reste de la vidéo (« quatre-vingt-dix soixante »).

On a retenu la reprise de phrase : il ne reste ainsi qu'**un seul** changement de voix, juste après le nom. Compare aussi la hauteur à ±1,5 s, la sonie et la durée par rapport au mot remplacé.

Si l'auteur s'excuse d'un raccord, le texte se met à l'écran sans tampon ni son : une petite ligne grise (34 px, `#c7c7cc`) en bas à droite, en fondu, pendant 3 à 4 s (32 Go, v7 : « Désolé pour mon souci de micro »). Pour la masquer, utilise des fondus `sc.tw` sans `opacity:0` écrit dans le style : sinon `check` lève l'erreur `gsap_cold_seek_hidden_fromto_missing_reveal`.

### Message à l'auteur
La liste des passages remplacés (temps dans la voix, texte), le tableau du contrôle des noms (faux et douteux), ce qui a été perdu ou changé par une reformulation, les étiquettes non vérifiées de la banque, les segments non utilisés, le chemin du 1080p, et la question de la 4K.
