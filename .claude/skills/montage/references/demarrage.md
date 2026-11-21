# Démarrer le montage d'une vidéo

## Où sont les choses

| Quoi | Où |
|---|---|
| Script, sources, téléprompteur, relevé de prix, kit d'upload | `<DEPOT>/projets/<nom-depot>/` (`fiche.md`, `script.md`, `sources.md`, `teleprompteur.txt`, `voicestudio-stories.txt`, `recherche/…`, `upload.md`) |
| Titre, date de sortie, statut | `<DEPOT>/calendrier.md` (« Grille des publications » : colonnes `#`, `Date, 18 h`, `Vidéo`, `Pilier`, `Format`, `Charge`, `Statut`) et `README.md` (« Suivi des projets » : `Projet`, `Format`, `Publication`, `Statut`) |
| Projets de montage (un par vidéo) | `<PREMIUM>/<AAAA-MM-sujet>/` |
| Style commun de la série | `<PREMIUM>/style/` (`RECETTE.md`, `tokens.css`, `components/`, `fonts/`, `media.json`) ; chaque projet en garde une copie dans son `style/` |
| Prononciations et reprises de l'auteur | `<DEPOT>/ressources/voix/prononciations.md` et `ressources/voix/reprises/` ; fichiers bruts aussi dans `<PREMIUM>/style/voice-presets/prononciations/` (voir `retouches.md`) |
| Projet modèle (voix clonée) | `2026-11-qwen-27b-32go/` (21/11/2026) |
| Projet modèle (vraie voix) | `2026-11-qwen-27b-8go/` (19/11/2026) ; avant : `2026-11-meme-carte-plus-rapide/`, `2026-11-strata-test/` |

`premium-noir/` n'est pas un dépôt git : **sauvegarde avant d'écraser** (copie dans `retouches/avant/` ou `sources/…-avant-….flac`), rien ne permet de revenir en arrière sinon.

## Relier le projet de montage et le dossier du dépôt

Les deux noms ne se ressemblent pas toujours : le dossier du dépôt garde le nom de l'idée (`strategie.md`, `idees.md`), le projet de montage prend le mois et un nom court du titre final.

| Vidéo | Dépôt `projets/` | Montage `premium-noir/` |
|---|---|---|
| 32 Go pour Qwen 27B : les prix, les routes et leurs pièges | `deux-cartes-occasion` | `2026-11-qwen-27b-32go` |
| Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? | `qwen-27b-8go` | `2026-11-qwen-27b-8go` |
| Même carte, 2 fois plus rapide | `meme-carte-plus-rapide` | `2026-11-meme-carte-plus-rapide` |

Pour trouver l'un depuis l'autre : la ligne de la vidéo dans `calendrier.md` ou `README.md` donne le lien `projets/<nom-depot>/fiche.md`, le titre, la date (`lun. 30 nov`, toujours 18 h) et le statut. Dans le projet de montage, la docstring de `scripts/montage.py` et celle de `scripts/teleprompteur.py` citent le dossier du dépôt (`projets/deux-cartes-occasion/…`). Nomme un nouveau projet `AAAA-MM-<nom court>` d'après le mois de sortie, et écris dans la docstring de `montage.py` le titre, la date de sortie et le chemin `projets/<nom-depot>/`.

## Le projet modèle doit être figé

Ne copie jamais un projet sur lequel un agent travaille encore (retouches, rendu, revue) : tu copierais une voix ou un `montage.py` à moitié modifiés. Avant la copie :
- vérifie qu'aucun sous-agent ni tâche de fond ne tourne (`sous-agents.md`, « Vérifier que rien ne tourne ») ;
- en cas de doute, copie depuis le dernier projet **livré et fini** (le 32 Go une fois ses retouches du 21/11 terminées ; sinon le 8 Go, figé depuis sa livraison du 19/11).

## Structure d'un projet

```
<projet>/
  index.html            généré par montage.py (ne pas éditer)
  compositions/         un fichier par plan s-001.html… et par mème meme-1.html… (générés)
  STORYBOARD.md         généré : temps, plan, début de la phrase dite, durée
  chapitres.txt         généré : un chapitre par plan qui porte chap=
  scripts/              tout le code (voir plus bas)
  sources/              voix d'origine, téléprompteur, transcriptions, mots de la voix finale
  edit-plan/            décisions et rapports : voice-*.json, captures.md, timeline.json, audio-timeline.json, verif-*.json
  assets/audio/         voix.flac (voix finale), music-minimal(-long).flac, music-tension(-long).flac
  assets/captures/      captures PNG nettes (3840×2160) ; assets/shots/ : les JPEG 2240 px utilisés par le montage
  assets/images/        images de la vidéo ; assets/images/produits/ : photos (+ -detoure.png)
  assets/logos/ memes/ sfx/ fonts/ lib/   (logos, mèmes mp4, bruitages flac, Inter + JetBrains Mono, gsap.min.js)
  renders/              rendus mp4, logs, planches d'images, bobine des raccords
  retouches/            sauvegardes et travail des retouches (avant/)
  critique*/ verif*/    dossiers de travail des sous-agents de critique et de revue
  style/ DESIGN.md tokens.local.css style.local.md hyperframes.json package.json meta.json AGENTS.md CLAUDE.md
```

## Créer le projet d'une nouvelle vidéo

1. **Copie** le projet modèle sans ce qui est propre à sa vidéo. Les exclusions sont ancrées par `/` à la racine, sinon `verif*` exclut aussi `scripts/verif_*.py` (piège vérifié le 21/11) :
   ```bash
   cd "$PREMIUM" && N=2026-12-nouveau-sujet && mkdir -p $N && rsync -a --exclude /renders --exclude '/critique*' --exclude '/verif*' --exclude /retouches --exclude '/.hyperframes' --exclude '/.thumbnails' --exclude '/.transcode-cache' --exclude '/.waveform-cache' --exclude /compositions --exclude /assets/shots --exclude /assets/captures --exclude /assets/images --exclude /assets/audio/voix.flac --exclude /sources --exclude /edit-plan --exclude /STORYBOARD.md --exclude /chapitres.txt --exclude /index.html --exclude /.git 2026-11-qwen-27b-32go/ $N/ && mkdir -p $N/{renders,sources,edit-plan,compositions,assets/shots,assets/captures,assets/images/produits}
   ```
   Vérifié le 21/11 sur une copie : tous les scripts y sont, dont les `verif_*.py` ; environ 310 Mo (surtout les musiques).
2. **Renomme le projet** dans `package.json` et `meta.json` (ils portent encore « starter-long », le gabarit d'origine), et remplace l'épingle `hyperframes@0.9.75` par `hyperframes@0.9.47` dans les trois scripts de `package.json`. Testé le 21/11 sur une copie :
   ```bash
   sed -i '' -e 's/hyperframes@0\.9\.75/hyperframes@0.9.47/g' -e 's/"name": "starter-long"/"name": "2026-12-nouveau-sujet"/' package.json && sed -i '' -e 's/"id": "starter-long"/"id": "2026-12-nouveau-sujet"/' -e 's/"name": "starter-long"/"name": "2026-12-nouveau-sujet"/' meta.json
   ```
   Sans ça, chaque `npx --yes hyperframes@0.9.47 check` finit par « This is hyperframes 0.9.47, but this project pins hyperframes@0.9.75 ». Dans les anciens projets (8 Go, 32 Go) cet avertissement est **attendu et sans effet** : tous leurs rendus ont été faits en 0.9.47 et on ne change pas de version au milieu d'un projet ; l'épingle 0.9.75 vient du gabarit et n'a jamais servi.
3. **Téléprompteur** : `cp "$DEPOT"/projets/<nom-depot>/teleprompteur.txt $N/sources/teleprompteur.txt` (lignes à lire seulement, une ligne vide entre les blocs, nombres en chiffres).
4. **Voix reçue** dans `sources/` : vraie voix → `sources/prise-originale.flac` ; voix clonée → `sources/voix-clone-<version>.wav` (voir `voix-clonee.md` pour les noms).
5. **Scripts de voix** : vraie voix → remplace `scripts/voix.py` et `scripts/verif_voix.py` par ceux de `2026-11-qwen-27b-8go/scripts/` (une source, `sources/prise-originale.*`). Deux voix clonées → garde ceux du 32 Go. Les autres scripts communs aux deux projets sont identiques (vérifié le 21/11 : `kit.py`, `blocs2.py`, `blocs3.py`, `build.py`, `verif_raccords.py`, `verif_souffles.py`, `verif_begaiements.py`, `w2v_*.py`, `retouche_voix.py`) ; `teleprompteur.py` du 32 Go est le plus complet (sections).
6. **Images à recopier** depuis l'ancien projet (le `rsync` exclut `assets/images/`) : seulement ce que ton `montage.py` citera :
   - les miniatures des deux vidéos de l'écran de fin (ex. `miniature-8go.jpg`, `miniature-budget.jpg`, `miniature-meme-carte.jpg` dans le 32 Go), ou les nouvelles ;
   - `afrique.json` et `afrique-LICENCE-CC-BY-4.0.md` si la carte d'Afrique revient ;
   - pas `placeholder-produit.png` (recréé tout seul par `P()`), pas les photos de produits ni les captures de l'ancienne vidéo.
   Les logos, mèmes, bruitages, polices, gsap et musiques viennent déjà avec le `rsync`.
7. **Réécris `scripts/montage.py`** (section suivante).

## Réécrire `montage.py` : la coupe exacte

Le fichier du 32 Go a quatre parties :

| Lignes (32 Go) | Partie | Que faire |
|---|---|---|
| docstring | titre, date, sources | **réécrire** : titre, date de sortie, `projets/<nom-depot>/`, type de vidéo (calculée, testée), type de voix |
| des `import` jusqu'à `# ───────────── marchands, statuts, cartes de prix ─────────────` et cette section entière | aides génériques (`new`, `P`, `shot`, `web`, `ln`, `ktg`, `pill_at`, `note`, `subscribe`, `merchant`, `status`, `offer`, `ladder`, `twin`) | **garder** ; ajuste seulement la liste des logos de marchands de `MLOGO` |
| de `# ───────────── schémas propres à cette vidéo ─────────────` jusqu'à la ligne juste avant `# ═════════════════════════ ASSEMBLAGE ═════════════════════════` | schémas propres (`gold`, `routes`, `mobo`, `psu`, `cities`…) et **tous les plans** (`sc = new(...)`) | **remplacer** entièrement par tes schémas et tes plans |
| de `# ═══ ASSEMBLAGE ═══` jusqu'à la fin | transitions, mèmes, musique, coupures, bruitages, storyboard | **garder** la mécanique, **adapter** les lignes ci-dessous |

À adapter dans ASSEMBLAGE :
- `MEMES = [...]` : tes mèmes, ancrés sur des phrases de **ta** voix (`T('…') - .1`) ; un `T()` de l'ancienne vidéo lève `KeyError`.
- `starts[...]` : les clés sont **exactement** les titres passés à `chap=` ; `t_r1` / `t_r3` (début et fin de la musique de tension) renvoient à tes parties ; `t_fin` du 32 Go n'est pas utilisé, supprime-le.
- `music = [...]` : bornes, volumes, décalages (`son.md`).
- `cuts = [...]` : tes 3 ou 4 chutes.
- la première ligne de `lines = ['# Storyboard du montage — …']` : le titre de ta vidéo.
- l'écran de fin (dernier plan, avant ASSEMBLAGE) : les deux miniatures et leurs titres.

Exemple minimal à 3 plans (testé le 21/11 sur une copie neuve avec voix et mots fictifs : `3 plans, 1 mèmes, 6 pistes audio`, `check` passé). Ce qui remplace la troisième partie :

```python
# ───────────── schémas propres à cette vidéo ─────────────
sc = new(at=0, chap='Introduction')
t = sc.uid('t'); sc.add(f'<div id="{t}" class="ab center" style="top:420px"><div class="h">Test <span style="color:var(--own)">froid</span></div></div>'); sc.enter(t, sc.start + .1, 'up')

sc = new('première route', chap='Route 1')
chapter(sc, '01', 'Route 1', sub='une carte de 16 Go')

sc = new('et on se dit à la prochaine', chap='À la prochaine', cam='none')
i = sc.uid('jd'); sc.add(f'<div id="{i}" class="ab center" style="top:90px"><div class="h">À la <span style="color:var(--own)">prochaine</span></div></div>'); sc.enter(i, sc.start + .1, 'up')
```

et dans ASSEMBLAGE :

```python
MEMES = [('omg-wow.mp4', T('teste') - .1, 1.8, (1520, 640, 290, 290))]
...
t_r1 = starts['Route 1']; t_r3 = starts['À la prochaine']
...
cuts = [T('une carte') - .35]
...
lines = ['# Storyboard du montage — Test froid (premium noir)', '', …]
```

Le premier plan porte `chap='Introduction'` : YouTube veut un premier chapitre à 00:00.

## Tester un projet neuf avant d'avoir la voix

`MC_DRY=1` a besoin de `sources/voix.words.json` (toutes les ancres) et des images que les briques ouvrent (taille des photos, `afrique.json`…). L'assemblage a besoin d'un fichier de voix. Avant de recevoir la voix, fabrique une voix et des mots fictifs (testé le 21/11) :

```bash
ffmpeg -v error -y -f lavfi -i anullsrc=r=48000:cl=mono -t 20 -c:a flac assets/audio/voix-fictive.flac
STRATA_WORDS=/chemin/mots-fictifs.json MC_VOICE=assets/audio/voix-fictive.flac MC_DRY=1 python3 scripts/montage.py 2>&1 | tail -1
STRATA_WORDS=/chemin/mots-fictifs.json MC_VOICE=assets/audio/voix-fictive.flac python3 scripts/montage.py 2>&1 | tail -1
```

- `mots-fictifs.json` : `[{"text": "salut", "start": 0.5, "end": 0.8}, …]`, les mots des phrases-ancres avec des temps croissants. Il peut être hors du projet (seul Python le lit).
- **La voix fictive doit être dans le projet** (`assets/audio/…`) : avec un chemin hors du projet, `check` échoue en `http_error: 404` sur la voix (le navigateur de rendu ne sert que le dossier du projet).
- `check` signale alors `audio_clip_silent` sur la voix fictive : attendu.
- Supprime `assets/audio/voix-fictive.flac` et relance sans les variables dès que la vraie voix est là.

## Scripts : génériques ou propres à la vidéo

Copie d'abord **ceux du projet modèle**. Les génériques ne se modifient que pour corriger un défaut qui vaudra pour toutes les vidéos ; écris alors la date et la raison dans leur en-tête, comme le font déjà les fichiers.

| Script | Statut | Rôle |
|---|---|---|
| `kit.py` | générique | `Scene`, `T()`, `seek()`, `icon()`, CSS commun (polices Noir Display / Noir Mono), caméra, entrées, sorties |
| `blocs.py`, `blocs2.py`, `blocs3.py` | génériques | briques de plans (texte mot à mot, jauges, barres, tuiles, mini navigateur, chapitres, compteurs, checklist…). `stamp()` de `blocs3.py` est interdit |
| `build.py` | générique | assemblage : sous-compositions, mèmes muets, pistes audio, placement des bruitages, `index.html`, `edit-plan/timeline.json` et `audio-timeline.json` |
| `captures-web.mjs` | moteur générique, liste `JOBS` propre à la vidéo | captures surlignées (voir `visuels.md`) |
| `w2v_transcrire.py`, `w2v_candidats.py`, `w2v_cand_prises.py` | génériques | transcription verbatim wav2vec2, test de transcriptions candidates par perte CTC |
| `verif_texte.py`, `verif_raccords.py`, `verif_begaiements.py`, `verif_souffles.py` | génériques | contrôles de la voix finale |
| `verif_voix.py` | deux variantes | celle du 8 Go pour une vraie voix (une source), celle du 32 Go pour deux voix clonées |
| `verif_sources.py`, `prises.py`, `psola.py`, `strata_psola.py`, `cale_gains.py`, `cale_hauteur.py` | génériques pour une voix clonée en deux versions | voir `voix-clonee.md` (les noms de source `complet` / `strata` y sont écrits en dur) |
| `reprises.py` | **méthode générique, table `REPL` propre à la vidéo** (32 Go, 21/11) | remplace des phrases de la voix finale par des reprises de l'auteur : préparation, calage sur les mots, pauses, PSOLA, ×1,1, niveau, collage, mastering, réécriture des mots ; part de `retouches/avant/` (voir `retouches.md`). Lancement : `uv run --no-project --with praat-parselmouth --with numpy --with scipy python scripts/reprises.py` |
| `mots.py`, `vue.py` | génériques pour une vraie voix | lecture des mots et des îlots d'énergie de `sources/prise-originale.*` |
| `test_slice.py` | outil, **dangereux** | essai de briques à temps fixes, sans voix. **Il écrase `index.html` et écrit `compositions/test-*.html`** : ne le lance jamais sur un projet dont le montage n'est pas regénérable, relance `montage.py` juste après, et efface `compositions/test-*.html` |
| `teleprompteur.py` | à adapter | ajoute à `SPOKEN` les noms, sigles et références de cartes de la vidéo sous la forme entendue par wav2vec2, et mets à jour `SECTIONS` (titres `###` du script) |
| `voix.py` | à adapter | chemins, `PARTIES` (débuts de partie), règles de pauses (`PAUSES`, chutes), texte de la bobine ; réglages remesurés sur la nouvelle voix |
| `choix_prises.py` | à réécrire (voix clonée) | décisions de prise phrase par phrase (`POURQUOI`) |
| `retouche_voix.py` | propre à une voix | retouches à des temps précis : à refaire ou à supprimer |
| `montage.py` | à réécrire (voir plus haut) | le montage lui-même (voir `moteur.md`) |

## Ce qui prime quand les documents se contredisent

Les documents de `style/` datent du Short « abonnements » (octobre). La pratique a changé depuis, sur retour de l'auteur. **La pratique du dernier projet et ce skill priment**, parce qu'ils intègrent ses retours :

| Vieux document | Ce qu'il dit | Ce qui prime | Pourquoi |
|---|---|---|---|
| `style/AGENT.md` | voix Kokoro | sa vraie voix ou sa voix clonée VoiceStudio ; jamais de voix de synthèse générique | c'est sa chaîne, sa voix ; il fournit les fichiers |
| `style/AGENT.md` | « n'utilise que des fournisseurs locaux », jamais HeyGen | **toujours valable** : pas de `hyperframes auth`, `cloud` ni `publish` | |
| `style/AGENT.md` | « lance `npm run check` » | `npx --yes hyperframes@0.9.47 check` (ou `npm run check` une fois l'épingle passée en 0.9.47) | même version partout |
| `RECETTE.md` § 8, `CLAUDE.md` du projet | minutage par Whisper large-v3, `transcript.json` | wav2vec2 verbatim (`scripts/w2v_transcrire.py`) et `sources/voix.words.json` | Whisper efface les répétitions et avance les premiers mots (12/11) |
| `RECETTE.md` § 2, `style/tokens.css` | SF Pro par la police système | Inter et JetBrains Mono embarquées (`assets/fonts/`), déclarées dans `kit.py` comme « Noir Display » et « Noir Mono » | rendu identique sur toute machine ; c'est ce qu'ont rendu toutes les vidéos depuis Strata |
| `RECETTE.md` § 7 | `powerdown` avant le mot choc, impacts | interdits (`BAN` de `build.py` : impact, impact-doux, riser-court, powerdown, whoosh-long) | « pas de boum, pas de son d'extinction » |
| `RECETTE.md` § 7 | musique à −19 dB (volume 0,112) | volumes 0,2 à 0,24 sous la voix (0,794), 0,42 sur l'écran de fin ; viser 15 à 22 dB sous la voix | une critique l'a trouvée inaudible sur téléphone (voir `son.md`) |
| `RECETTE.md` § 7 | crête −2 dBTP | −2,5 dBTP pour la voix | marge sous −2,2 depuis le 15/11 |
| `RECETTE.md` § 4, 5 | pub-mème avec son, karaoké incrusté | mèmes muets ; pas de sous-titres incrustés dans les vidéos longues (fichiers `.srt` à l'upload) | demande de l'auteur |
| `RECETTE.md` § 7 | silences ramenés à 0,25-0,45 s | vraie voix : 0,34 s au plus entre deux phrases ; voix clonée : on **ajoute** des micro-pauses (voir `voix-clonee.md`) | retours du 12/11 et du 21/11 |
| `package.json`, `meta.json` | « starter-long », `hyperframes@0.9.75` | nom du projet, `hyperframes@0.9.47` | version de tous les rendus depuis Strata ; ne mélange pas deux versions dans un projet |
| `.claude/rules/script.md` | storyboard calé sur `voix-off-montee.wav` | `STORYBOARD.md` généré par `montage.py`, calé sur `assets/audio/voix.flac` | |
| ancienne note de style du 12/11 (mémoire de Claude, voir `SKILL.md`, « Style de montage de l'auteur ») | générateur dans `2026-11-qwen-4-arrive/scripts/*_v3.py` | scripts du projet le plus récent | ceux de Qwen 4 sont trois générations en arrière |

Ce qui reste valable dans `RECETTE.md` : le noir pur, l'encre et les gris, les trois accents (rouge = perte, vert = possession, jaune = voix extérieure ou surlignage), deux accents au plus par plan, les courbes de mouvement, les marges de 96 px, « une idée à la fois ».
