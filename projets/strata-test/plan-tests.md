# Plan de tests Strata (V2) : à suivre aujourd'hui (mer. 11/11/2026)

> Vidéo : [« Je teste le meilleur modèle possible avec Strata sur ma 5080 »](fiche.md), sortie **lun. 16/11, 18 h**. Machine : RTX 5080 16 Go, 32 Go de DDR5-6000, Ryzen 7 9700X, Windows. Commandes revérifiées le **11/11** dans la doc et le code de Strata et de Pi (faits : [`sources.md`](sources.md), T1…). Ce que tu notes en section 11 remplit les trous **R1 à R15** du [script](script.md). Critique de la V1 : [`grill-v1.md`](grill-v1.md) ; ancienne version : [`plan-tests-v1.md`](plan-tests-v1.md).
>
> **Règle du tournage** : le premier essai compte. Un plantage, un écran figé, une relance : tu les gardes et tu les filmes. Ne rejoue jamais un test pour qu'il soit propre.

**Changements depuis la V1**
- **Tes décisions du 11/11** : Strata s'installe avec **l'installeur Windows** de la v0.2.13 (l'appli télécharge le moteur et le modèle) ; le harnais est **Pi** (OpenCode passe en plan B, section 9.10). Le Terminal `strata` reste, mais seulement pour ce que l'appli ne fait pas (section 2.3).
- **Retiré** : le réglage de la réflexion (`--set reasoning-effort=medium` n'est confirmé nulle part), la relance à `--context 98304` (elle ne change pas la limite de réponse), `--mtp off` (un fichier IQ natif comme le Coder refuse sans doute de démarrer sans, T11), Claude Code branché sur Strata, l'écran sur l'iGPU, la Game Bar.
- **Ajouté** : la limite de réponse **montée à la main** avant le premier test (4.3) ; la recherche de la ligne du bug #5104 au démarrage (4.2), un bug plus large que ce que disait la V1.
- **Déplacé** : les trois essais de Claude et les captures web se font **pendant le téléchargement**. Si Strata casse, tu as déjà la moitié de la vidéo.
- **Simplifié** : une seule relance par test, faites toutes ensemble ; 18 plans indispensables au lieu de 41 ; 15 trous à remplir au lieu de 43 ; des prompts plus légers (le site passe de 6 sections à 4, le jeu perd l'angle de rebond, l'île garde ses 5 exigences en plus court), pour des fichiers bien sous la limite de réponse.

---

## 0. L'après-midi en 6 étapes

| # | Quoi | Durée | Plans |
|---|---|---|---|
| 1 | Préparer (pilote, disque, OBS, Pi), installer l'appli Strata, **lancer le téléchargement du Coder** | 30 min, puis le téléchargement tourne seul (1 h 30 à 3 h, selon ta connexion) | P04, P05, P07 |
| 2 | **Pendant le téléchargement** : les 3 essais de Claude, les captures web | 1 h | P30-P32, C1-C6 |
| 3 | Premier chargement dans l'appli, puis passage au Terminal, 3 vérifications, branchement de Pi | 30 min | P07, P06, P09 |
| 4 | Calibrage (non filmé), puis le plan de la vitesse | 15 min | P10 |
| 5 | Les 3 démos locales, **navigateur fermé** | 45 min à 1 h 15 | P12-P16 |
| 6 | Arrêt de Strata, ouverture des résultats, relances en lot, plan de fin | 45 min | P20-P23, P41 |

**Si le temps manque, coupe dans cet ordre** : les captures web (elles se font demain) → les relances → le test 3 (l'île). **Ne coupe jamais** : le plan de la vitesse (P10), le test 1 et son résultat (P12, P20), un plantage (P16).

**Si, 30 minutes après le début du téléchargement, il reste plus de 2 h** : continue l'étape 2, puis prépare le reste. Si le modèle n'est pas là ce soir, **décale la vidéo** plutôt que de changer de modèle : rien d'autre dans Strata ne tient avec 32 Go (T5).

---

## 1. Préparer (20 min)

- [ ] **Pilote NVIDIA 580 ou plus** (les paquets CUDA 13 l'exigent, T2) : `nvidia-smi` dans PowerShell. Note la version.
- [ ] **Disque** : **90 Go libres** sur le SSD des modèles (≈ 58 Go de modèle + ≈ 5 Go de couche de prédiction, T6, T33 ; un testeur a vu 87 Go occupés, T4). Prends `D:\Strata`.
- [ ] **Ferme tout** : Chrome, Edge, Discord, Steam, Docker, VS Code, Photoshop ; LM Studio par **Quit** près de l'horloge (pas juste la fenêtre) ; `llama-server` s'il tourne (même port 8080). Mode « Ne pas déranger ». Horloge de la barre des tâches **avec les secondes** (Paramètres > Heure et langue > Date et heure) : c'est ta preuve de durée.
- [ ] **OBS** : capture d'affichage 1920 × 1080, 60 i/s ; encodeur **NVENC H.264**, CQP 19, format **MKV** (survit à un plantage) ; enregistrement **sur un autre disque** que `D:\Strata` ; pas de micro, son du bureau activé. **Un fichier par étape** (`P12-jeu.mkv`), pas plus fin. À ne jamais montrer : une clé d'API, les onglets du navigateur, tes dossiers de travail.
- [ ] **Pi** (le harnais, section 4.3) : il lui faut **Node.js 22.19 ou plus** et, sous Windows, **Git for Windows** (Pi lance ses commandes dans Git Bash, T37). Vérifie `node --version` et `git --version`. Puis installe Pi avec l'installeur officiel :

```powershell
powershell -c "irm https://pi.dev/install.ps1 | iex"
```

  (ou `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`). Vérifie `pi --version` : Strata a testé sa config avec **pi 0.74.2** (T14). Lance-le dans **Windows Terminal**, pas dans l'ancienne console (la doc de Pi le recommande, T37).
- [ ] **Dossiers vides**, hors de `youtubeSkill` : `D:\strata-demo\calibrage`, `\jeu`, `\site`, `\voxel`, `\claude-jeu`, `\claude-site`, `\claude-voxel`.
- [ ] **Les prompts** : copie la section 6 dans un fichier texte sur le Bureau, pour ne rien retaper à la caméra.
- [ ] Revérifie en 10 s que « Tikaya » n'est pas une vraie appli de paiement (aucune trouvée le 11/11 ; sinon, prends un autre nom inventé et change-le partout).

---

## 2. Installer Strata avec l'appli et lancer le téléchargement

### 2.1 Ce que fait l'installeur (vérifié le 11/11, T38)

`Strata-0.2.13-windows-x64-setup.exe` (≈ 113 Mo, sur https://github.com/Niko1221/Strata/releases/tag/v0.2.13) installe **l'appli de bureau** pour ton utilisateur, sans droits d'administrateur. D'après la doc :
- **le moteur n'est pas dedans** : au premier démarrage, l'appli te montre celui de ta carte avec sa taille et un bouton **Download** ;
- **le modèle** se choisit dans la page **Models** de l'appli, avec sa taille et s'il tient sur ta machine, puis l'appli le télécharge dans le dossier que tu choisis ;
- **le mode RAM réduite** est choisi tout seul : l'appli et le Terminal utilisent la même installation (`setup.py`), et c'est elle qui choisit `resident` ou `mmap` (T5, T8) ;
- **le harnais** : l'appli contient un harnais de code à elle, le « DeepSeek Harness », que la doc ne présente qu'avec DeepSeek. Rien ne dit qu'il marche avec le Coder : **on ne l'utilise pas** ;
- **ce que la doc de l'appli ne montre pas** : brancher Pi (`strata connect` est une commande du Terminal), un compteur de tok/s hors navigateur (le moniteur du Terminal ; la page web de Strata en a un, mais le navigateur reste fermé), et le contournement du bug #5104 (`--set STRATA_PREFILL_LAYER_MAJOR=0`). L'appli a des « Expert settings » pour les options du moteur et un journal (Settings > Engine > Diagnostics > View logs), mais rien dans la doc ne dit qu'on peut y mettre ce contournement. **Pour ces trois choses, on prend le Terminal (2.3)**, où tout est documenté. La doc présente le Terminal comme une installation à part.

Fermer l'appli arrête son moteur (T38).

### 2.2 Installer et télécharger (à filmer : P05, P07)

- [ ] Télécharge `Strata-0.2.13-windows-x64-setup.exe` depuis la page de la release, lance-le. Si SmartScreen ou Smart App Control bloque un exécutable : le projet dit que certains ne sont pas encore signés (#735, T9) ; lis `docs/TROUBLESHOOTING.md` avant de toucher à la protection de Windows.
- [ ] Premier démarrage : **Download** sur le moteur proposé (CUDA 13 pour ta carte).
- [ ] Page **Models** : choisis le **Coder** (Qwen3.8-Flash-Next Coder, **IQ1_M**, ≈ 58 Go). C'est le seul fichier que la doc annonce pour « un PC de 32 Go avec une carte de 12 à 16 Go » (T5). Si l'appli te met en avant autre chose (Swift, Gyro), ne le prends pas : la doc dit qu'elle peut présélectionner un autre fichier (T5). **Filme** la ligne du Coder avec son libellé (depuis la 0.2.13 : « fits » ou « may run slower », T32) : c'est **P05**.
- [ ] Dossier : `D:\Strata`. **Images : non** si l'appli le demande (le lecteur d'images tourne sur le processeur sous 24 Go de VRAM et prend ≈ 0,9 Go, T5).
- [ ] Le téléchargement démarre (P07, accéléré au montage). Passe à l'étape 3.

### 2.3 Le Terminal, pour ce que l'appli ne fait pas

Pendant le téléchargement, ouvre un **nouveau** PowerShell et tape `strata --version`.
- La commande répond : l'installeur l'a mise, rien à faire.
- « commande introuvable » : installe le Terminal (sans droits d'administrateur, T2), puis ouvre une **nouvelle** fenêtre :

```powershell
irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```

Le Terminal partage le dossier d'installation de l'appli et retrouve les modèles qu'elle a téléchargés (T38). Note la version (attendu : **0.2.13**, publiée le 09/11, T1).

---

## 3. Pendant le téléchargement : Claude, puis les captures

Le téléchargement ne prend presque pas de RAM : le navigateur est permis **jusqu'au premier chargement**.

**Claude (P30, P31, P32)** : même prompt mot pour mot (section 6), **un seul essai, aucune relance**.
- [ ] Nouvelle fenêtre PowerShell, `cd D:\strata-demo\claude-jeu`, `claude`, puis `/model` : **note le nom exact et l'effort**. Colle le prompt du test 1. Note l'heure de début et de fin.
- [ ] Pareil dans `claude-site` (test 2) et `claude-voxel` (test 3).
- [ ] Ouvre les trois `index.html`, filme 20 s de chacun (P30-P32), note la durée et le score x / 5 (R12).
- [ ] **Ne lance jamais une commande qui modifie `~/.claude/settings.json`** : `strata connect claude-code --write` y écrirait (T14). C'est pour ça qu'on branche Pi, pas Claude Code, sur Strata.

**Captures web (C1 à C6, liste en bas du [storyboard](storyboard.md))** : les tickets #4997, #5104, #5046, `MODELS.md`, `DETAILS.md`, la page des versions, la fiche Hugging Face du Coder (P03), la page GitHub (P02). Puis **ferme le navigateur, tout entier** (Gestionnaire des tâches : plus aucun processus Chrome ou Edge).

**P04** : le Gestionnaire des tâches au repos, onglet Performances : la RAM (32 Go), la carte (16 Go). 15 s.

---

## 4. Premier chargement, passage au Terminal, 3 vérifications

### 4.1 Le premier chargement, dans l'appli (P07)

- [ ] Le téléchargement fini, **charge le Coder dans l'appli** (Load). L'étape « Preparing your model » prend environ 5,5 minutes sur une installation neuve en 0.2.13 (T3) et n'a lieu qu'une fois. **Ne touche à rien** : la souris peut se figer quelques minutes ; au-delà de 10 minutes figé, redémarre le PC, ferme tout, recommence (T9). **Filme** le Gestionnaire des tâches, la RAM qui monte. **Chronomètre** du clic à la fin du chargement (R4).
- [ ] Le modèle répond : **ferme l'appli complètement** (y compris près de l'horloge). Ça arrête son moteur et libère la RAM (T38).

### 4.2 Servir depuis le Terminal (P06)

Pourquoi : c'est le Terminal qui donne le compteur de tok/s, `strata connect pi` et le contournement du bug #5104. Il reprend le modèle que l'appli a téléchargé.

- [ ] D'abord, le plan : il dit ce qu'il téléchargerait (T2). **≈ 5 à 6 Go, c'est normal** (la couche de prédiction, si l'appli ne l'a pas déjà prise, T33) ; **0, c'est parfait** ; **≈ 58 Go, stop** : il n'a pas trouvé le modèle de l'appli.

```powershell
strata launch --plan --family coder --model IQ1_M --context 64k --vision off --parallel 1
```

  S'il veut retélécharger ≈ 58 Go, **ne lance rien** : ajoute `--data-dir D:\Strata` et refais le plan ; si ça ne change rien, passe au plan B 9.11 (servir depuis l'appli).
- [ ] Le lancement guidé (à filmer) : `strata launch`, puis :

| Écran | Choix |
|---|---|
| Start | « Set up from the beginning » |
| Model | **Coder** (IQ1_M) : il doit apparaître comme déjà installé |
| Folder | ne change rien : pour un modèle déjà installé (même par l'appli), il part du dossier du modèle et ne liste que ce qui manque (T38). « Use model files I already have » ne sert que si le Coder n'apparaît pas : pointe alors `D:\Strata` |
| Context | **64K**, mémoire en 8-bit (le défaut) |
| Pictures | **No** |
| Parallel | **1** |
| Tuning | **skip** (le « quick » prend 20 min : pas aujourd'hui) |
| Advanced | **Ne change rien.** Lis la commande affichée : **`--resident-experts`** ou **`--mmap-experts`** (R6, T8). Filme cette ligne. |
| Access | **This computer only** |
| Preset | nomme-le **`Coder 64K`** |

  Sans les écrans, la même chose en une ligne : `strata launch --family coder --model IQ1_M --context 64k --vision off --parallel 1 --tune skip --access local --save-preset "Coder 64K"`. Le moniteur s'ouvre dans cette fenêtre : laisse-la tourner. Dans une autre, `strata launch --status` doit montrer le modèle servi. Si le Terminal refait « Preparing your model », chronomètre-le aussi : R4 prend le premier chargement, celui de l'appli.

**Vérification 1 : le mode.** `--resident-experts` (les experts que la carte ne garde pas sont copiés en RAM, rien n'est lu sur le SSD pendant les réponses) ou `--mmap-experts` (une partie lue sur le SSD, beaucoup plus lent, T8). Si c'est `--mmap-experts` : plan B 9.2 une fois, sinon garde-le et filme.

**Vérification 2 : le bug #5104.** Ce bug fait planter le Coder quand il lit une demande longue (« could not copy experts 256.. », code de sortie **-6**). Il touche tous les fichiers à 256 experts, donc le Coder, mais seulement quand le moteur choisit une lecture « couche par couche » ; plusieurs utilisateurs l'ont eu sur des cartes de 8 et 12 Go, dont une RTX 5070 ; personne n'en parle sur 16 Go (T23). Dans la vue **6 (Logs)** du moniteur, cherche une ligne de démarrage qui contient **`layer-major walk`** :
- tu la vois → relance tout de suite avec le contournement :

```powershell
strata launch --preset "Coder 64K" --set STRATA_PREFILL_LAYER_MAJOR=0 --restart
```

- tu ne la vois pas, ou tu ne trouves pas les lignes de démarrage → ne cherche pas plus, le calibrage le dira.

### 4.3 Vérification 3 : brancher Pi et monter la limite de réponse (P09, à filmer)

**Pourquoi Pi** (ta préférence, confirmée par les chiffres de Strata, T14) : son prompt système et ses outils pèsent **≈ 1 500 tokens**, le plus petit des huit harnais que Strata sait brancher, contre **≈ 7 400** pour OpenCode. Ça fait **≈ 5 900 tokens de moins à chaque requête**, soit 9 % d'un contexte de 64K laissé à la conversation. Deux effets concrets :
- **le bug #5104** n'a été vu que sur des demandes de **3 300 tokens et plus** (T23) : la première requête de Pi (≈ 1 500 + ≈ 350 pour le prompt du test) passe en dessous, celle d'OpenCode (≈ 7 800) au-dessus. Les tours suivants sont plus longs : **le risque baisse, il ne disparaît pas** ;
- **la limite de réponse** : là, Pi ne change rien. Strata écrit **la même limite** pour les deux (un huitième du contexte, 8 192 à 64K, T13). La correction à la main ci-dessous est nécessaire dans les deux cas.
- Ce que ça ne change presque pas : le temps de lecture (≈ 6 000 tokens de moins à ≈ 2 500 tok/s, T7 : 2 à 3 s par requête).
- Le prix : Pi a besoin de Git Bash sous Windows (section 1).

```powershell
strata connect pi              # affiche la config (adresse, modèle, contexte)
strata connect pi --write      # écrit ~/.pi/agent/models.json et settings.json, après avoir demandé, avec une sauvegarde
```

Puis ouvre le fichier des modèles :

```powershell
notepad $HOME\.pi\agent\models.json
```

Dans le fournisseur `strata`, le modèle a **`"maxTokens": 8192`**. **Remplace 8192 par 32000**, enregistre. Pourquoi : la réponse est plafonnée à un huitième du contexte, **réflexion comprise**, et le serveur n'arrête la réflexion qu'au dernier quart de cette limite : il ne resterait qu'environ 2 000 tokens pour écrire le fichier (T13). Un jeu complet en fait plusieurs milliers. Le serveur adapte de lui-même la limite à la place qui reste dans le contexte (T31). **Attention** : chaque nouveau `strata connect pi --write` réécrit la liste des modèles et **remet 8192** (T31) : refais la correction après chaque `--write`.

```powershell
strata connect pi --check      # 1 prompt et 1 appel d'outil : les deux doivent passer
```

*La correction est déduite du code de Strata et de la doc de Pi (`maxTokens`, T37), pas d'un essai : le calibrage la vérifie.*

**Le moniteur** : Windows Terminal en deux volets (`Alt+Maj+D`). À droite, la fenêtre où tourne `strata launch` (son moniteur, vue **1 Overview** : vitesse, VRAM, RAM, requêtes récentes) ; si tu l'as fermée, `strata monitor --url http://127.0.0.1:8080`. À gauche, Pi. Pi n'affiche pas les tok/s : c'est le moniteur qui les donne. Après chaque génération, regarde la vue 1 (requêtes récentes) ou la vue 3 (Requests).

---

## 5. Calibrage (non filmé, 10 min max), puis le plan de la vitesse

**Le calibrage** vérifie trois choses avant les vrais tests : pas de plantage, un fichier écrit **en entier**, et la durée de la réflexion. Dans `D:\strata-demo\calibrage`, lance `pi`. S'il demande s'il peut faire confiance au dossier, réponds oui (il est vide). Vérifie avec `/model` que le modèle est celui de `strata`, puis :

```text
Create a single-file index.html: a to-do list with add, delete, mark as done, a counter of tasks left, and a dark mode toggle. All CSS and JavaScript inline, no libraries. About 150 lines.
```

| Ce que tu vois | Ce que tu fais |
|---|---|
| Le fichier existe et finit par `</html>` | Note « calibrage OK », la durée, le tok/s. Passe au plan de la vitesse. |
| Le moteur plante : `could not copy experts`, `exit code -6`, « running out of RAM » | C'est #5104. Relance avec `--set STRATA_PREFILL_LAYER_MAJOR=0` (commande en 4.2), refais le calibrage. **Note-le** : c'est un résultat (R14). |
| Le fichier est coupé ou jamais écrit | **Fais une capture d'écran de la fin du fichier** (V23b du storyboard). Rouvre `models.json` : `"maxTokens"` doit valoir 32000. Corrige, quitte et relance Pi, refais le calibrage. Si c'est encore coupé : plan B 9.4. |
| Pi ne trouve pas Bash | Installe Git for Windows, ou suis 9.10 (OpenCode). |
| Plus de 10 minutes sans fin | Arrête (`Échap` dans Pi). Regarde le moniteur : la réflexion tourne-t-elle en boucle ? Plan B 9.4. |

**Le plan de la vitesse (P10, à filmer, moniteur en grand)** : dans Pi, `Tell me a short story about a dragon who loves video games.` Garde 20 s lisibles du compteur pendant qu'il écrit. C'est le plan le plus propre pour afficher la vitesse.

---

## 6. Les trois démos (navigateur fermé)

**Protocole, pour chaque test**
1. `cd` dans le dossier du test, `pi`, modèle de `strata`. Lance l'enregistrement OBS.
2. Colle le prompt, Entrée. **Note l'heure** (secondes comprises).
3. Ne touche à rien. Le compteur de tok/s doit être lisible à l'écran. Toutes les 30 s environ, note la valeur (basse, typique, haute).
4. Note l'heure de fin (dernier fichier écrit). Garde 5 s d'image après.
5. **Limite : 25 minutes.** Au-delà, arrête, note « temps dépassé » et ce qui existe sur le disque. C'est filmable.
6. Pendant ce temps (un test sur les trois suffit) : **P15**, le Gestionnaire des tâches, la RAM presque pleine, 15 s. Note la RAM libre la plus basse (R5).

Les prompts sont en anglais (le Coder est « plus faible hors de l'anglais », T5). Chacun a **5 exigences numérotées** : le score est le nombre d'exigences qui marchent à l'écran, sur 5.

### 6.1 Test 1 : le jeu (P12)

```text
Create a complete Breakout game in one file, index.html. No libraries, no external files: all HTML, CSS and JavaScript inline. 800x600 canvas, dark background, neon colors.
1. 6 rows of colored bricks, a paddle moved with the mouse or the left/right arrow keys, and a ball that bounces off the walls, the paddle and the bricks.
2. A score, 3 lives, and a game over screen and a win screen that both say "Press SPACE to restart".
3. Some bricks drop a power-up when destroyed: either a wider paddle or 3 balls at once.
4. Short sound effects made with the Web Audio API, and small particles when a brick breaks.
5. It must run as soon as I open index.html, with no errors in the console.
Write the whole file in one go, then give me a two-line summary.
```

**Pour la voix** : un casse-briques complet dans un seul fichier, six rangées de briques, la raquette à la souris, trois vies, des bonus qui tombent, des bruitages, des étincelles quand une brique casse, zéro erreur dans la console.

### 6.2 Test 2 : le site (P13)

```text
Create a landing page for a fictional mobile-money app called "Tikaya" that lets friends split bills and send money in seconds. One file, index.html, all CSS and JavaScript inline, no libraries, no image files (inline SVG only). Dark theme with an orange accent.
1. A hero section: headline, short subtitle, a call-to-action button, and a phone mockup drawn in CSS or SVG.
2. Three feature cards with an SVG icon each.
3. A pricing section with 3 plans (Free, Plus, Pro), the middle one highlighted.
4. A FAQ of 4 questions that open and close when clicked, then a footer.
5. It must look right on a phone (375 px wide) and on a desktop, with no errors in the console.
Write the whole file in one go.
```

**Pour la voix** : une page de présentation pour une appli de paiement qui n'existe pas, un grand titre avec un téléphone dessiné, trois cartes, trois tarifs, une FAQ qui s'ouvre et se ferme, et ça doit tenir sur un téléphone.

### 6.3 Test 3 : l'île en 3D (P14)

Avant d'appuyer sur Entrée, **écris ton pronostic** en une phrase (R8). Après coup, on est toujours trop malin.

```text
Create a 3D voxel island in one file, index.html, using three.js r128 loaded with a classic script tag from exactly this URL: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js (no ES modules, no OrbitControls, no other library).
1. A procedural island from your own noise function: at least 48x48 columns of cubes drawn with THREE.InstancedMesh, colored by height (sand, grass, rock, snow).
2. A semi-transparent blue water plane around the island.
3. At least 15 trees made of cubes (trunk and leaves), only on grass.
4. Drag the mouse to orbit around the island and use the wheel to zoom (write this yourself); when the mouse is idle, the island turns slowly.
5. A sun with shadows, a sky-blue background, and the N key switches between day and night.
It must render as soon as I open index.html, with no errors in the console. Write the whole file in one go.
```

L'adresse de three.js répond (vérifiée le 11/11, T17) ; la page a besoin d'internet à l'ouverture pour la charger, pas pendant la génération.

**Pour la voix** : une île en cubes, en 3D, un relief généré, de l'eau, au moins quinze arbres, la souris pour tourner autour, et la touche N pour passer à la nuit.

---

## 7. Ouvrir les résultats, puis les relances

- [ ] Une fois les **trois** tests écrits : arrête Strata (`strata launch --stop`, ou `q` puis « stop » dans le moniteur). La RAM et la VRAM reviennent : **filme-le** (P41, plan de fin).
- [ ] Ouvre le navigateur, une fenêtre, et les trois `index.html` (double-clic). **Avant toute relance**, filme et note :
  - **P20** le jeu : 30 s de partie, un bonus qui tombe si possible, puis la console (F12) ;
  - **P21** le site : défilement lent, la FAQ qui s'ouvre, puis F12 → mode téléphone (375 px) ;
  - **P22** l'île : 15 s de rotation à la souris, le zoom, la touche N, la console. Fluide ou ça rame, à l'œil.
  - Pour chacun : premier coup oui ou non, le score x / 5, ce qui casse (copie l'erreur de la console).
- [ ] **Relances (une par test au maximum, toutes ensemble)** : ferme le navigateur, `strata launch --preset "Coder 64K"` (ajoute `--set STRATA_PREFILL_LAYER_MAJOR=0` si tu l'avais mis), puis dans chaque dossier cassé, `pi --continue` (reprend la dernière session du dossier, T37) et :

```text
It does not work: <colle l'erreur de la console, ou décris ce qui ne marche pas en une phrase>. Fix it in index.html.
```

  Ensuite, stop, navigateur, nouveau verdict. **P23** : la relance et son résultat. Ne corrige jamais le code à la main.

---

## 8. Plan de fin (P41)

`strata --version`, `strata launch --status` (sans afficher de clé), `nvidia-smi`, puis `strata launch --stop` et la RAM qui revient dans le Gestionnaire des tâches. 30 s. Si tu l'as déjà filmé en 7, garde juste les versions.

---

## 9. Plan B : quand ça casse

L'échec se filme (P16). Pour chaque cas, **un seul remède à la fois**, et tu notes ce qui a marché.

| # | Symptôme | Ce que tu fais |
|---|---|---|
| 9.1 | Le téléchargement n'avance pas | L'appli reprend un téléchargement coupé (T38). 58 Go à 100 Mbit/s ≈ 1 h 20, à 50 Mbit/s ≈ 2 h 40. Filme « ça télécharge » (P07) et avance l'étape 3. Pas de modèle ce soir : décale la vidéo. |
| 9.2 | `--mmap-experts` au lieu de `--resident-experts`, ou le PC figé plus de 10 min | (1) `strata launch --stop`, ferme tout (vérifie la RAM libre **avant** de relancer), `strata launch --preset "Coder 64K"`. (2) Contexte plus petit : `strata launch --preset "Coder 64K" --context 32k --restart`, puis `strata connect pi --write` et mets `"maxTokens"` à **16000** (32 000 ne tient plus dans 32K). (3) Si seul le mode lent démarre : **garde-le**, il marche, c'est lent ; un testeur sur 12 Go de VRAM et 32 Go de RAM y avait 41 à 46 tok/s sur du code (T4). La vidéo dit le prix. |
| 9.3 | `could not copy experts`, `exit code -6`, « running out of RAM » | Bug #5104 (T23) : `strata launch --preset "Coder 64K" --set STRATA_PREFILL_LAYER_MAJOR=0 --restart`. Note le message exact (vue 6, Logs) et si le contournement a marché : c'est R14. |
| 9.4 | Fichier coupé, ou réflexion en boucle | (1) Vérifie `"maxTokens": 32000` dans `models.json`. (2) Repli **après** les générations, navigateur permis : ouvre `http://127.0.0.1:8080`, colle le prompt dans la page de chat de Strata, copie le HTML dans `index.html`. Dis-le dans la vidéo : c'est un repli, pas un agent. |
| 9.5 | `non-finite logits` ou un seul mot répété en boucle | Rapporté sur 5080 avec d'autres fichiers (IQ3_S, IQ3_XXS), pas avec le Coder (T11). Ne ferme rien, filme le message, copie la ligne exacte (vue 6). Essaie `--restart`, puis `--context 32k`. Si ça revient, c'est ton résultat. **Pas de `--mtp off`** : un fichier IQ natif refuse de démarrer sans (T11). |
| 9.6 | La vitesse s'effondre (moins de la moitié des repères de 9.7) | Regarde dans l'ordre : la RAM (Gestionnaire, Mémoire : Windows écrit-il sur le disque ?) ; l'appli Strata est-elle vraiment fermée ? ; le mode (`mmap`) ; la VRAM libre dans le moniteur ; la température (`nvidia-smi`) ; OBS (refais 30 s sans OBS). Note ta cause probable (R11). |
| 9.7 | Repères pour juger ta vitesse | 70 tok/s en chat court sur une 5070 Ti, même processeur, 31 Go, **réflexion coupée**, sans test de justesse (T7) ; 41 à 46 tok/s sur du code en mode lent sur 12 Go (T4). Pas des promesses. |
| 9.8 | La RAM manque quand OBS tourne | Ferme l'aperçu d'OBS, passe à 30 i/s. Sinon, filme l'écran du moniteur **au téléphone** pour le plan de la vitesse. |
| 9.9 | Le code est livré mais ne marche pas | C'est un verdict, pas un problème : une relance (section 7), puis F12, l'erreur à l'écran. |
| 9.10 | **Pi ne marche pas** (pas de Bash, `--check` échoue, appels d'outil refusés) | Passe à **OpenCode** : `npm i -g opencode-ai`, lance `opencode` une fois (son premier lancement télécharge un plug-in, T14), puis `strata connect opencode --write`, `notepad $HOME\.config\opencode\opencode.json`, remplace `"output": 8192` par `"output": 32000` (celle-là, Strata la garde aux `--write` suivants, T31), puis `strata connect opencode --check`. Son prompt pèse ≈ 7 400 tokens : surveille #5104 (9.3). Relances : `opencode --continue` (non vérifié). Dis-le dans la vidéo, et change « Pi » dans le script. |
| 9.11 | Le Terminal veut retélécharger le modèle, ou ne démarre pas | Sers depuis **l'appli** : charge le Coder, lis l'adresse de son serveur dans ses réglages (par défaut `http://127.0.0.1:8080`, T2), puis écris `models.json` de Pi à la main (exemple ci-dessous). Tu perds le moniteur du Terminal : filme le compteur de l'appli s'il y en a un. *Non vérifié : où l'appli affiche son adresse et sa vitesse.* |

**Exemple de `models.json` de Pi écrit à la main (plan B 9.11)** : c'est ce que `strata connect pi` écrit (T14), avec la limite déjà montée. Le nom du modèle (`id`) est celui que renvoie `Invoke-RestMethod http://127.0.0.1:8080/v1/models` ; sans clé d'API, `strata-local` sert de clé factice (T14, T37).

```json
{
  "providers": {
    "strata": {
      "baseUrl": "http://127.0.0.1:8080/v1",
      "api": "openai-completions",
      "apiKey": "strata-local",
      "compat": { "supportsDeveloperRole": false, "supportsReasoningEffort": false },
      "models": [
        { "id": "<le nom renvoyé par /v1/models>", "name": "Qwen3.8-Flash-Next (Strata, local)", "reasoning": true,
          "input": ["text"], "contextWindow": 65536, "maxTokens": 32000,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 } }
      ]
    }
  }
}
```

Puis dans Pi, `/model` pour choisir ce modèle.

---

## 10. Les plans à filmer

**Indispensables (18)**
- [ ] **P04** Gestionnaire des tâches au repos (RAM 32 Go, carte 16 Go)
- [ ] **P05** la page Models de l'appli, la ligne du Coder et son libellé
- [ ] **P06** `strata launch`, l'écran Advanced, la ligne `--resident-experts` ou `--mmap-experts` lisible
- [ ] **P07** le téléchargement dans l'appli (accéléré), « Preparing your model », la RAM qui monte
- [ ] **P09** `strata connect pi --write`, la ligne `"maxTokens": 32000`, puis `--check` qui passe
- [ ] **P10** le plan de la vitesse (le dragon), compteur en grand
- [ ] **P12, P13, P14** les trois générations : terminal en deux volets, compteur, horloge
- [ ] **P15** la RAM au plus bas pendant une génération
- [ ] **P16** tout plantage ou blocage (si ça arrive)
- [ ] **P20, P21, P22** les trois résultats ouverts
- [ ] **P30, P31, P32** les trois résultats de Claude
- [ ] **P41** l'arrêt de Strata, la RAM qui revient, les versions

**En bonus, si tu as le temps (ou demain)** : **P01** la tour, la 5080 par la vitre (pas de visage) ; **P02** la page GitHub ; **P03** la fiche Hugging Face ; **P23** les relances ; les captures C1-C6.

L'écran partagé local / Claude (V24a, V25b du storyboard) se fait au montage, à partir de P20-P22 et P30-P32.

---

## 11. La fiche de résultats (15 trous)

Chaque ligne porte l'identifiant du trou dans le [script](script.md), le [storyboard](storyboard.md) et le [téléprompteur](teleprompteur.txt). Remplis-la en tournant, dans tes mots. Les lignes « à écrire » sont tes avis.

| Trou | Ce qu'il faut | Où le lire | Ta valeur |
|---|---|---|---|
| **R1** | tok/s typique pendant le jeu (pas le maximum) | moniteur, pendant P12 | |
| **R2** | combien des trois ont marché du premier coup (0 à 3) | section 7, avant les relances | |
| **R3** | le jeu en une phrase : durée, premier coup ou pas, score sur 5, ce qui casse, et la relance s'il y en a eu | horloge, P20, console | |
| **R4** | premier chargement : durée, et si le PC s'est figé (combien de temps) | chronomètre, P07 | |
| **R5** | RAM libre au plus bas pendant une génération | Gestionnaire ou moniteur, P15 | |
| **R6** | `resident` ou `mmap` | écran Advanced, P06 | |
| **R7** | le site en une phrase : durée, premier coup ou pas, score sur 5, ce qui casse | horloge, P21 | |
| **R8** | **à écrire, AVANT le test 3** : ton pronostic sur l'île | ta tête | |
| **R9** | l'île en une phrase : durée, premier coup ou pas, score sur 5, fluide ou pas | horloge, P22 | |
| **R10** | tok/s typiques du site et de l'île | moniteur, P13, P14 | |
| **R11** | ta vitesse face au repère de 70 (réflexion coupée chez lui) : plus ou moins, de combien, et ta cause probable si c'est moins (9.6) | R1 contre 70 | |
| **R12** | Claude, une phrase par test : durée et score sur 5 | section 3 | |
| **R13** | **à écrire** : la comparaison en une phrase, et ce qui sépare les deux à tes yeux | P20-P22 contre P30-P32 | |
| **R14** | ce qui a cassé chez toi (message exact, version de Strata), ou « rien n'a planté » | vue 6 (Logs), `strata --version` | |
| **R15** | **à écrire** : est-ce que ça remplace ton abonnement, et ce qui t'a le plus surpris | toi | |

**À noter aussi (pas des trous)** : versions de Strata, du moteur, de Pi, pilote, contexte ; si tu as dû mettre `STRATA_PREFILL_LAYER_MAJOR=0` ; résultat du calibrage ; modèle et effort de Claude (`/model`) ; si tu as dû passer à OpenCode ; écart de tok/s avec et sans OBS si tu l'as mesuré.
