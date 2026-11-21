# Voix : voix clonée (VoiceStudio / OmniVoice)

Depuis le 21/11/2026, l'auteur peut fournir sa voix **clonée** (synthèse VoiceStudio, moteur OmniVoice) au lieu d'un enregistrement. Il génère souvent **deux versions complètes** du même texte. Pour « 32 Go pour Qwen 27B » :
- `complet` : la plus fidèle, débit posé et serré (≈ 210 mots/min hors pauses), mais certains mots coupés ou avalés ;
- `strata` : style plus vivant (celui de la vidéo Strata), ≈ 20 % plus lente, plus brillante (+3,5 dB à 1-4 kHz), plus haute d'environ 1,3 demi-ton (f0 médiane 127 Hz contre 119).

Ses mots : « fais le montage complet dans mon style avec les meilleures prises, en y rajoutant aussi certaines micro-pauses » ; « au plus 2 revues de la voix ». Le script de référence est `2026-11-qwen-27b-32go/scripts/voix.py` : lis son en-tête en entier.

Le texte réellement envoyé au moteur (nombres en lettres, liaisons écrites, balises `[sigh]`, `[laughter]`, `[pause 500ms]`) est dans `projets/<nom>/voicestudio-stories.txt` et ses notes dans `voicestudio.md`. Pour préparer ce texte, c'est le skill `voix-off-voicestudio`, pas celui-ci.

Fais faire ce travail par un sous-agent Opus (brief : `briefs/modele-voix-clonee.md`).

## Ce qui change par rapport à une vraie voix
- **Pas de bruit de fond** (pauses à −73/−77 dB) : rien ne s'atténue de plus de 35 dB, ça faisait des trous. Les souffles nets, les sons isolés, les clics et les **claquements de bouche de la synthèse** (5-20 ms dans une pause ou collés à l'attaque d'un mot) sont **remplacés** par du fond de la même source (pris sur un plateau calme tout proche, resynthétisé par petits morceaux), fondus de 15 ms. Jamais sur l'étendue d'un mot wav2vec2 (±30 ms) : l'attaque faible d'un /s/ était sinon prise pour un bruit.
- **On ajoute des pauses** au lieu de seulement resserrer (une synthèse enchaîne tout au même rythme). Cibles mesurées entre îlots de parole :
  - fin de phrase 0,32-0,42 s ; changement de partie (titre `###` du script) 0,58-0,68 s ; deux-points 0,16-0,24 s ; virgule 0,20 s au plus ;
  - un petit temps **avant les chutes** (« la VRAM, c'est de l'or », « Rien. C'est la même carte », « Noël sans cartes »…) ;
  - jamais de blanc au-delà de 0,8 s ; le silence ajouté est du fond de la même source inséré au creux le plus calme (jamais des zéros) ; s'il n'y a pas de creux propre, on n'allonge pas et on le note ;
  - liste dans `edit-plan/voice-pauses.json`.
- Une pause **à l'intérieur d'un mot** (fermeture avant le /k/ de « stock ») n'est jamais touchée ; l'écart de « 5060 | Ti » est gardé (resserré, on entend « soixante-dix »).
- **Débit** : la cible est 165-185 mots/min **hors pauses**, comme repère pour les passages lents. Une version déjà plus rapide (`complet` à ≈ 210 mots/min) **n'est ni ralentie ni accélérée** : on ne ralentit jamais une synthèse (ça déforme les voyelles), et c'est l'ajout des micro-pauses qui fait respirer le débit perçu (la voix du 32 Go est passée de 10 min 15 brut à 9 min 18 avec les pauses, mais sans un seul raccourcissement de mot). Au-dessus de la cible, on n'agit que sur les pauses. En dessous (version plus lente, comme `strata`), on accélère le bloc vers le débit de la version voisine, ×1,25 au plus (`tempo`), sauf sur les chiffres (`no_tempo`) : le but est que le changement de source ne s'entende pas, pas d'atteindre un chiffre.

## Étapes (deux versions)
1. Copie les deux fichiers dans `sources/voix-clone-complet.wav` et `sources/voix-clone-strata.wav` (24 kHz mono). Les noms `complet` / `strata` sont écrits dans les scripts : garde-les, ou remplace-les partout.
2. Transcris chaque version en verbatim (en arrière-plan) :
   ```bash
   uv run --no-project --with torch --with transformers --with numpy python scripts/w2v_transcrire.py sources/voix-clone-complet.wav sources/voix-clone-complet.w2v.json
   ```
   (idem pour `strata`).
3. **Note chaque phrase dans les deux versions** : `uv run --no-project --with torch --with transformers --with numpy python scripts/prises.py` (alignement forcé CTC du texte attendu, note par mot, niveau, hauteur, débit → `sources/prises.json`). Pour un mot ou un chiffre douteux : `scripts/w2v_cand_prises.py requetes.json`, lancé avec le même `uv run … python` (classe par perte CTC des transcriptions candidates données la bonne en premier ; format des requêtes dans son en-tête).
4. **Choisis la prise de chaque phrase** : `python3 scripts/choix_prises.py` écrit `edit-plan/voice-keep.json` (chaque morceau dit sa source `src`, ses `phrases`, ses temps dans cette source, la raison `cut`, et pour `strata` son `tempo`). Par défaut `complet` ; `strata` quand `complet` a un mot coupé, avalé, déformé ou un chiffre changé. **Change de source entre deux phrases**, pas au milieu (sauf greffe propre d'un mot).
5. **Hauteur** des blocs `strata` ramenée à celle de `complet` par PSOLA, formants et durée gardés :
   `uv run --no-project --with praat-parselmouth --with numpy python scripts/strata_psola.py` → `sources/voix-clone-strata-psola.wav`, `edit-plan/strata-psola.json` (décalage par bloc borné à [−2,5 ; 0] demi-ton).
6. **Voix** : `python3 scripts/voix.py` (égaliseur d'appariement sur `strata`, gain par bloc, fond des pauses commun pris sur `complet`, fondus égale puissance de 30 ms, mastering −16 LUFS / LRA 9 / −2,5 dBTP / 48 kHz).
7. **Mesure chaque changement de source** : `python3 scripts/verif_sources.py` (sonie BS.1770, hauteur médiane, débit des 3 s avant et après) → `edit-plan/verif-sources.json`. Si un écart s'entend : `python3 scripts/cale_gains.py` et `python3 scripts/cale_hauteur.py` (rampes d'entrée et de sortie par bloc, cumulées dans `edit-plan/strata-gain-adj.json` et `strata-pitch-adj.json`), puis on reprend à l'étape 5.
   Ordre complet : `choix_prises.py → strata_psola.py → voix.py → verif_sources.py (→ cale_gains.py / cale_hauteur.py, et on recommence)`.
8. Contrôles de l'agent lui-même : les mêmes que pour une vraie voix (`voix-reelle.md`, étape 6), avec `verif_voix.py` du 32 Go (deux sources).
9. **Revue indépendante n° 1** (`verifications.md`), corrections, **revue n° 2**, et c'est la dernière.

### Une seule version clonée
Pas de choix de source, donc ni `prises.py`, ni `choix_prises.py`, ni `strata_psola.py`, ni `verif_sources.py`, ni `cale_*.py`. Prends le `voix.py` **du 32 Go** (il sait traiter une synthèse : fond, claquements, micro-pauses) et mets toute la voix dans la source `complet` : copie le fichier en `sources/voix-clone-complet.wav` et écris un `edit-plan/voice-keep.json` dont tous les morceaux ont `"src": "complet"` (découpe par phrases comme pour une vraie voix, `voix-reelle.md` étape 2, pour pouvoir écarter un mot raté). **Non testé à ce jour** : `voix.py` (`SRCS`, égaliseur d'appariement) et `verif_voix.py` (boucle sur `('complet', 'strata')`) chargent les deux sources. Le contournement le plus simple est de donner aussi le même fichier aux noms qu'ils lisent pour `strata` (`SRCS` de `voix.py` lit `sources/voix-clone-strata-psola.wav`, `verif_voix.py` lit `sources/voix-clone-strata.w2v.json` ; aucun morceau n'y renvoie) et de vérifier que les deux scripts tournent ; sinon, retire `strata` de `SRCS` et de la boucle, et écris-le dans leur en-tête. Les mots ratés sans autre version se signalent à l'auteur, qui peut renvoyer une reprise (`retouches.md`).

### Deux versions qui ne s'appellent pas « complet » / « strata »
Les deux noms sont écrits en dur dans `voix.py`, `prises.py`, `choix_prises.py`, `strata_psola.py`, `verif_sources.py`, `verif_voix.py`, `cale_gains.py`, `cale_hauteur.py`. Le plus sûr : **nomme les fichiers** `sources/voix-clone-complet.wav` (la version la plus fidèle, la source par défaut) et `sources/voix-clone-strata.wav` (l'autre), et note dans l'en-tête de `voix.py` ce que chaque nom désigne vraiment (« strata = version "posée 2" de l'auteur »). Ne renomme pas dans le code, sauf si tu changes tous ces fichiers d'un coup (`grep -n "complet\|strata" scripts/*.py`).

## Erreurs typiques de la synthèse (vues le 21/11)
- sigles et références de cartes : « Ti » de « 5060 Ti » qui sonne « dix », « 5090 » faible, « 27B » entendu « vincent b » ;
- un mot proche d'un autre : « sans » → « sin », « en stock » → « stop », « deux » → « de », « c'est de l'or » → « cède » ;
- une version ajoute un mot (« pour » en trop) ou en coupe un ;
- les balises `[sigh]` et `[laughter]` sonnent faux : on les a coupées ;
- les fins de blocs `strata` gardent un saut de débit de 26 à 69 % même après ×1,25 ; un bloc traité par PSOLA peut sonner un peu plus lisse.
Une machine ne juge pas tout le naturel : liste à l'auteur les passages à écouter au casque, avec leurs temps.

Quand l'auteur renvoie des reprises pour ces mots, voir `retouches.md`.

## Résultat de référence (32 Go, 21/11)
30 morceaux, 28 changements de source ; voix finale de 9 min 18 (contre 10 min 15 pour `complet` brut) ; −16,2 LUFS, −2,4 dBTP. Revue 1 : 5 sauts de hauteur audibles, corrigés par PSOLA, tempo, gains et deux phrases reprises dans `complet`. Revue 2 : plus aucun saut audible, aucun prix faux.
