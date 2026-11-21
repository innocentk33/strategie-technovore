# Le moteur de montage (`scripts/montage.py`)

Le montage est un programme Python qui écrit le projet HyperFrames. Une scène (`Scene`) = un plan = une sous-composition `compositions/s-NNN.html`. Chaque plan est **ancré sur une phrase de la voix** : on ne tape jamais un temps à la main, on écrit `T("le début de la phrase")`.

## Lancer

Depuis la racine du projet :

```bash
MC_DRY=1 python3 scripts/montage.py 2>&1 | tail -2       # ancres seulement : « 68 plans (à blanc) »
python3 scripts/montage.py 2>&1 | tail -1                # génère tout : « 68 plans, 4 mèmes, 56 pistes audio ; fin 352.1 »
npx --yes hyperframes@0.9.47 check 2>&1 | grep -E "✗|⚠|error\(s\)|Check (passed|failed)|pins" | cut -c1-220
```

(Sorties réelles relevées le 21/11 sur une copie du projet 8 Go ; `check` y passe avec 0 erreur et des avertissements, qu'on lit : voir `verifications.md`.)

- `MC_DRY=1` construit les plans puis s'arrête avant l'assemblage : il attrape une ancre introuvable (`KeyError: phrase introuvable après …`) ou un plan trop court (`ValueError: plan trop court avant …`). Depuis le 21/11 (32 Go), il écrit aussi les débuts de plans dans `edit-plan/dry-starts.json`, pour comparer avant et après une retouche de voix (`retouches.md`). Il a besoin de `sources/voix.words.json` et des images et fichiers que les briques ouvrent (taille des photos, `afrique.json`…) : ils doivent exister.
- Variables : `STRATA_WORDS=<fichier>` remplace `sources/voix.words.json` (mots d'essai, le fichier peut être hors du projet) ; `MC_VOICE=<fichier>` remplace `assets/audio/voix.flac` à l'assemblage (**chemin dans le projet**, sinon `check` échoue en 404). Recette complète pour un projet sans voix : `demarrage.md`, « Tester un projet neuf avant d'avoir la voix ».
- Quand tu as supprimé ou renuméroté des plans, efface les anciens fichiers avant de régénérer, sinon des plans orphelins restent dans `compositions/` : `rm -f compositions/s-*.html compositions/meme-*.html && python3 scripts/montage.py 2>&1 | tail -1`.
- Sorties : `compositions/`, `index.html`, `STORYBOARD.md`, `chapitres.txt`, `edit-plan/timeline.json` (début, durée, chapitre et caméra de chaque plan) et `edit-plan/audio-timeline.json`.

## Les ancres : `T()` et `new()`

`T(phrase, after=None, end=False)` (dans `kit.py`) renvoie le début (ou la fin avec `end=True`) du **premier** passage de `phrase` dans `voix.words.json` **après le curseur**. La phrase est normalisée : minuscules, ponctuation retirée, apostrophes et tirets = séparateurs. On écrit donc `T('si t es malin')`, `T('c est de l or')`, `T('qwen 27b')`, `T('800')` (nombres en chiffres, comme dans les mots). « 32 000 » contient une espace insécable : il compte pour deux mots, `T('32 000')`.

`new(phrase, at=None, lead=.18, chap=None, cam=None)` ouvre un plan :
- début = `T(phrase) - lead` (ou `at`), arrondi à l'image (1/30 s) à l'assemblage ;
- refuse un plan qui commence moins de 0,55 s après le précédent ;
- **remet le curseur au début du plan** (`seek`) : les `T()` qui suivent cherchent dans ce plan, dans l'ordre. Une ancre trop courte (« exactement », « b70 ») peut tomber sur une occurrence plus loin ou plus tôt : prends 2 ou 3 mots, ou `T('…', after=…)` ;
- `chap='Titre'` : début de partie (écran de chapitre, ligne dans `chapitres.txt`, fondu de sortie du plan précédent) ;
- `cam='none'` fige la caméra (écran de fin).

## La `Scene` (kit.py)

- `sc.uid('pfx')` : identifiant unique d'élément ; `sc.add(html)` : ajoute du HTML (positions absolues dans un cadre 1920 × 1080, classe `ab` ; `ab center` = centré entre les marges de 96 px).
- `sc.enter(id, t, how)` : entrée au temps absolu `t` ; `how` = `blur` (défaut), `up`, `pop`, `left`, `right`, `down`.
- `sc.tw(id, de, vers, t, durée, courbe, kind)` : tween GSAP libre ; `kind='move'` pour un changement d'état après l'entrée (le second tween d'un même élément reçoit `immediateRender:false` tout seul).
- `sc.out(id, t)`, `sc.dim(id, t)`, `sc.punch(t)` (zoom bref sur le moment fort ; sinon un punch automatique sur la première entrée « pop » du plan).
- Une entrée n'est jamais avancée de plus de 0,4 s avant son mot ; le premier élément d'un plan arrive dès l'ouverture ; à l'image 0 de la vidéo, tout est déjà visible (c'est l'image que voient les lecteurs avant de lancer).
- Caméra de chaque plan (dérive continue) : `push`, `pull`, `left`, `right`, `rise`, `tilt`, `none`, assignées en cycle par l'assemblage (`MOVES`). Amplitude calculée pour qu'un texte à 96 px du bord reste à ~50 px dans l'image.

Couleurs des mots et pastilles : `'w'` blanc, `'g'` vert (possession), `'r'` rouge (perte), `'y'` jaune (surlignage, voix extérieure), `'gray'`. Variables CSS : `var(--ink)`, `var(--gray)`, `var(--ghost)`, `var(--loss)`, `var(--own)`, `var(--voice)`, `var(--panel)`. Classes de texte : `h` (titre), `h2`, `h3`, `eb` (surtitre en capitales espacées), `num` / `mono` (chiffres machine, Noir Mono), `price` (prix, Noir Display 700), `pill` (+ `r`, `g`, `y`).

## Les briques

Dans le haut de `montage.py` (génériques, à garder d'une vidéo à l'autre) :
- `P(key)` : photo de produit `assets/images/produits/*key*` (la version `-detoure.png` d'abord). **Si rien ne correspond, il renvoie une silhouette grise** (`placeholder-produit.png`) sans erreur : vérifie avant le rendu (`grep -l placeholder-produit compositions/*.html`).
- `shot(code, id, hl)` et `web(sc, code, id, url, t_hl, zoom='auto', …)` : capture dans le mini navigateur, version surlignée fondue au temps `t_hl`, zoom automatique sur la zone surlignée (`hl_box` compare les deux captures). **Renvoie `None` si la capture n'existe pas** : prévois le repli (`if F is None: hero(...)`), et vérifie qu'il n'a pas servi par erreur.
- `ln(texte, t, {mot: couleur})` + `ktg(sc, [ln(…), …], vis='icone:couleur')` : phrase posée en gris fantôme dès l'ouverture, qui s'allume mot à mot sur la voix (la grammaire de sa vidéo de référence).
- `side_text`, `pill_at(sc, texte, t, top, couleur, taille)`, `eb_at` (surtitre), `note` (mention de source en bas), `subscribe(sc, t_question, t_bouton)` (bouton S'abonner sur la phrase « Si cette vidéo t'a évité un mauvais achat, abonne-toi »).
- Vidéos de prix : `merchant(nom)` (pastille logo + nom ; LDLC sur fond sombre car ses lettres sont blanches), `status(texte, 'g'|'r'|'y'|'gray')`, `offer(...)` (grande carte d'offre : produit, nom, marchand, prix au mot, statut, total « × 2 »), `ladder(sc, rows)` (offres en lignes : fantômes dès l'ouverture, chacune s'allume sur son nom, le prix arrive sur son mot), `twin(...)` (même produit, deux marchands, l'écart entre les deux).

Dans `blocs.py` : `words`, `kt`, `pills`, `eyebrow`, `visual`, `stack`, `card`, `gpu` (produit sur le plateau), `bars` (barres qui poussent sur les mots), `gauge(sc, cap, segs, …)` (mémoire d'une carte : segments `(libellé, début, taille, couleur, t_in)` ; `ram=True` dessine le débordement en RAM **à la même échelle**, `ram_label`), `tiles`, `compare`.

Dans `blocs2.py` : `frame(sc, média, kind='browser'|'app'|'card', url=…, pos=…)` qui renvoie un cadre avec `.zoom(t, boîte)`, `.scroll`, `.reset`, `.mark`, `.swap(t, image2)`, `.dim` ; `tag`, `hero` (grand chiffre), `counter` (chiffre qui défile), `verdict`, `chapter(sc, num, titre, sub=…)` (écran de partie), `term` (lignes de terminal), `sfx(sc, t, nom, vol)`, `logo`, `backdrop`. `experts`, `tiers`, `budget` sont des schémas de Strata.

Dans `blocs3.py` : `speedo` (compteur), `switch`, `keyboard`, `tokens_row`, `linechart`, `checklist`, `logo3`. **`stamp()` est interdit.**

Les schémas propres à une vidéo (carte mère, alimentation, carte d'Afrique, routes…) s'écrivent dans `montage.py`, sous `# ───────────── schémas propres à cette vidéo ─────────────`, sur le modèle de `mobo()`, `psu()`, `layers()`, `cities()` du 32 Go.

## Écrire les plans

Un plan par idée, dans l'ordre du script, en suivant ses indications `[VISUEL]` :

```python
sc = new('première route', chap='Route 1 : deux cartes de 16 Go')
chapter(sc, '01', 'Route 1', sub='deux cartes de 16 Go')

sc = new('prends la rtx 5060 ti')
offer(sc, '5060', 'ASUS Dual RTX 5060 Ti OC · 16 Go', 'amazon', '799,99 €', T('800') - .1, ('En stock', 'g'), None, 'w', mult='× 2 = 1599,98 €', t_mult=T('1600') - .1)
```

Règles de composition (critiques et retours de l'auteur) :
- **un plan évolue sur les mots** ; jamais plus de 8 s sans changement visible, jamais une carte seule qui attend la suivante avec une moitié d'écran vide ;
- les **3 premières secondes montrent déjà la promesse** (la légende et la jauge de l'accroche dès 0,2 s, pas un cadre vide) ;
- le texte à l'écran **dit la même chose que la voix au même moment** (une légende qui dit l'inverse de la voix a été le défaut le plus grave d'une critique) ;
- texte de 28 px au moins ; rien d'important à moins de ~80 px du bas (la barre de lecture YouTube le couvre) ; marges de 96 px ; deux niveaux de texte et ~7 mots lisibles d'un coup au plus ;
- pas deux éléments qui se chevauchent, pas de texte qui passe sous un texte ; un mème laisse 30 à 40 px de marge à tout élément ;
- vrais logos avec leur nom ; prix en `price` ; la source en micro (`note`) quand c'est un chiffre ;
- schémas **à l'échelle** : une jauge de 64 Go et une de 32 Go partagent la même échelle, un débordement se dessine à la même échelle que la carte ;
- un chapitre par partie (`chap=`), avec son écran `chapter()` ; les titres de chapitre deviennent les chapitres YouTube.

## L'assemblage (bas de `montage.py`)

- `END = voix + 11 s` (écran de fin ≈ 12 s pour les éléments YouTube).
- Transitions : fondu à chaque changement de partie (et entrée `zoomin` du plan suivant), plan fouetté (`whip`) un sur quatre, `zoomin` un autre sur quatre, sinon fondu enchaîné de 0,25 s.
- `MEMES = [(fichier, t, durée, (x, y, w, h)), …]` : durée coupée automatiquement avant le plan suivant (−0,15 s). Voir `visuels.md`.
- `music = [(fichier, début, fin, volume, décalage), …]` et `cuts = [T('…') - .35, …]` (coupures avant les chutes) ; dédoublonnage des bruitages à 0,3 s. Voir `son.md`.
- `assemble(SC, END, voice=…, memes=…, music=…)` écrit tout, puis le script réécrit `STORYBOARD.md` et `chapitres.txt`.
- Écran de fin : « Merci d'avoir regardé / À la prochaine », deux cartes de vidéos (miniatures dans `assets/images/`) avec leur titre en pastille, et « Technovore » en surtitre.
