# Plan de tests Strata : à suivre aujourd'hui (mer. 11/11/2026), case par case

> Vidéo : [« Je teste le meilleur modèle possible avec Strata sur ma 5080 »](fiche.md), sortie **lun. 16/11, 18 h**. Machine : RTX 5080 16 Go, 32 Go de DDR5-6000, Ryzen 7 9700X, Windows. Les docs de Strata ont été relues le **11/11/2026** (faits : [`sources.md`](sources.md), numéros T1, T2…). Ce que tu notes ici remplit les `⟦résultat : …⟧` du [script](script.md).
>
> **Règle du tournage** : tout ce que tu filmes est un matériau. Un plantage, un écran figé, une relance : garde-les. L'échec fait partie de l'histoire, et le script a une variante pour chaque cas. **Ne rejoue jamais un test « pour qu'il soit propre »** : le premier essai est celui qui compte, les relances se comptent.

**Ordre de la journée (durées relatives : tu fais ce tournage ce soir, pas à une heure fixe)**

| Quand | Quoi | Durée estimée |
|---|---|---|
| Dès maintenant | 1. Préparation + téléchargement du modèle (lance-le **en premier**, il tourne pendant que tu prépares le reste) | 1 h 30 à 3 h selon ta connexion (T3) |
| Ensuite | 2. Démarrage, premier chargement, vérifications | 15 à 30 min |
| Puis | 3. Les trois tests de génération (navigateur **fermé**) | 1 h à 1 h 30 |
| Puis | 4. Stop de Strata, ouverture des résultats, relances | 45 min |
| Puis | 5. La comparaison avec Claude | 30 min |
| Fin | 6. Plans de coupe (PC, GitHub, Gestionnaire des tâches) | 20 min |

**Le risque n° 1 est le temps** (le téléchargement, puis les générations qui durent chacune jusqu'à 25 minutes). **Si tu manques de temps, coupe dans cet ordre** :
1. d'abord les plans de coupe P01 à P05, P40 et les captures web : ils se font demain, le modèle n'a pas besoin de tourner ;
2. puis les relances (une seule par test) et le « tuning » ;
3. puis le test 3 (voxel) et sa comparaison avec Claude (P32) ;
4. **ne coupe jamais** : le plan vitesse P10, le test 1 (jeu) avec sa comparaison Claude (P30), et tout plantage (P16).

Si, **30 minutes après le début du téléchargement**, la barre indique plus de 2 h restantes, passe au **plan B n° 1** (section 4).

---

## 1. Préparation

### 1.1 La version à installer

- [ ] **Strata 0.2.13** (publiée le 09/11/2026, moteurs 0.1.59). C'est la dernière : `v0.2.13` sur https://github.com/Niko1221/Strata/releases/latest (T1). La 0.2.13 corrige des choses de démarrage (Strix Halo, Arc), rien de spécifique à ta carte : ne t'attends pas à un gain, **note la version** (T1).
- [ ] **Terminal, pas l'appli** : l'appli de bureau marche aussi, mais le Terminal te donne le moniteur de vitesse (`strata monitor`), la connexion à OpenCode (`strata connect`) et `strata launch --plan`. Les notes de version précisent que sur Windows, le Terminal peut rester en 0.2.12 après `strata update` (« le Terminal avance à la prochaine version ») : **note `strata --version` ET la version du moteur**, ne suppose pas que c'est 0.2.13 partout (T1).
- [ ] Pilote NVIDIA **580 ou plus** (les paquets CUDA 13 l'exigent, T2) : `nvidia-smi` dans PowerShell, **note la version du pilote**. Avant de continuer, regarde si un autre pilote est proposé : des rapports d'erreurs sur 5080 donnent « pilote 617.42 » (T11).
- [ ] **Disque** : ≥ 90 Go libres sur le SSD des modèles (téléchargement ≈ 58 Go ; un testeur a vu 87 Go occupés sur son disque, T4). Prends `D:\Strata`.
- [ ] Installe le Terminal (PowerShell, sans droits d'administrateur) :

```powershell
irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```

  Ouvre une **nouvelle** fenêtre PowerShell (Windows Terminal), puis :

```powershell
strata --version
strata doctor
```

- [ ] Si SmartScreen ou Smart App Control bloque `strata.exe` : lis `docs/TROUBLESHOOTING.md` (le projet dit que ses exécutables ne sont pas encore signés, T9). Ne désactive pas la protection de Windows en grand sans lire.

### 1.2 Le fichier du modèle et les réglages

**Le modèle : le Coder.** Avec 32 Go de RAM, c'est le seul fichier de Flash-Next que la doc annonce pour ta configuration (« 32 Go de RAM avec 12 à 16 Go de GPU : le Coder », T5). C'est **une version coupée de moitié (256 experts sur 512), faite pour le code, expérimentale** ; ses auteurs annoncent 95,7 % du score SWE-bench Verified du modèle complet (T6). Fichier : `ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF`, un seul quant, **IQ1_M** (29,6 Go + 28,8 Go de table qui reste sur le SSD ; fiche inchangée depuis le 19/10, T6). **Ne choisis pas Swift 1.5, qu'il risque de te proposer** (ses experts ne tiennent pas dans ta RAM).

- [ ] Regarde d'abord ce qui se passerait, sans rien télécharger :

```powershell
strata launch --plan --family coder --model IQ1_M --context 64k --vision off --parallel 1 --data-dir D:\Strata
```

  Note : taille du téléchargement, le mot « fits / tight / does not fit », ce que le plan dit de la RAM. **Filme cet écran** (plan P05).

- [ ] **Premier lancement guidé (à filmer, plan P06)** : `strata launch --data-dir D:\Strata`, puis dans les écrans :

| Écran | Choix | Pourquoi |
|---|---|---|
| Model | **Coder** (famille `coder`, IQ1_M) | Seul qui tient avec 32 Go (T5) |
| Folder | `D:\Strata` | Le SSD rapide |
| Context | **64K**, mémoire en **8-bit** (la touche `m` change le format) | 64K est le contexte qu'a mesuré l'utilisateur de la 5070 Ti, 16 Go de VRAM et 31,2 Gio de RAM, **avec `--resident-experts`** (T7). Voir 4.5 si les fichiers générés sont coupés |
| Pictures | **No** | Inutile pour coder, et ça économise de la RAM (le lecteur d'images tourne sur le CPU sous 24 Go, T5) |
| Parallel | **1** | Une requête à la fois |
| Tuning | **skip** | Vérifier d'abord que ça démarre ; le « quick » prend ≈ 20 min, à faire seulement si tout marche et s'il te reste du temps |
| Advanced | **Ne change rien, lis la commande exacte** | Cherche **`--resident-experts`** (les experts que la carte ne garde pas sont copiés en RAM, rien n'est lu sur le SSD pendant les réponses) ou **`--mmap-experts`** (une partie lue sur le SSD, beaucoup plus lent). **Note lequel des deux** (T8) |
| Access | **This computer only** (127.0.0.1) | Pas de clé à cacher à l'écran |
| Preset | `Coder 64K` | Pour relancer : `strata launch --preset "Coder 64K"` |

  Il n'y a **pas d'option `--low-ram`** dans `strata launch` : le mode (résident ou lu sur le SSD) est choisi tout seul par l'installation (T5). C'est pour ça qu'il faut lire l'écran Advanced.

- [ ] **Au premier chargement, ne touche à rien** : la souris peut se figer 1 à 3 minutes (jusqu'à 10 ; au-delà de 10, redémarre, ferme tout, recommence, T9). Les notes de la 0.2.13 donnent **≈ 5,5 minutes** pour l'étape « Preparing your model » sur deux PC (T3), sans cause trouvée. **Filme ça** : le Gestionnaire des tâches (RAM qui monte), le curseur qui saccade (plan P07).
- [ ] Une fois servi : `strata launch --status` doit répondre « serving ».

**Réflexion du modèle (décide-le maintenant, une fois).** Par défaut, ce modèle réfléchit au niveau « high » (T10). La réflexion compte dans la limite de réponse que `strata connect` écrit pour OpenCode : à 64K de contexte, **8 192 tokens, réflexion comprise** (T13), et le serveur arrête la réflexion quand il ne reste qu'un quart de la limite. Un fichier HTML de 5 à 8 mille tokens peut donc se faire **couper**. Le test de calibrage (2.0) te le dit avant les vrais essais.

**Attention : les « Chat settings » de la page web de Strata ne servent pas ici.** La doc dit que les chats et les réglages de la page « restent dans le navigateur » (T10) : ils règlent la page, pas OpenCode. Les leviers qui comptent pour OpenCode :
- **côté serveur** : la clé `reasoning_effort` de la configuration du modèle. La doc dit qu'un `--reasoning-effort` dans les arguments du moteur y est déplacé (T10). À tester : `strata launch --preset "Coder 64K" --set reasoning-effort=medium --restart` ; si Strata refuse la clé, dis-le à l'écran et passe au levier suivant ;
- **côté OpenCode** : choisir un niveau de réflexion plus bas dans OpenCode, si l'interface l'offre pour ce modèle (à vérifier, non testé).

  Plan : lance le calibrage avec **« medium »**. Vérifie le réglage avec une demande courte dans OpenCode (« Write a haiku about RAM ») : la réflexion visible doit être courte, et la vue 6 (Logs) du moniteur donne le nombre de tokens. Dis le réglage dans la vidéo. Si aucun levier ne marche, garde le défaut et passe à 4.5 dès qu'un fichier est coupé.

- [ ] Note : réflexion = ⟦…⟧ (fiche, section 6).

### 1.3 Le harnais : OpenCode branché sur Strata

**Pourquoi OpenCode et pas Claude Code** : `strata connect claude-code --write` **fusionne** `ANTHROPIC_BASE_URL` et le nom du modèle dans `~/.claude/settings.json` (le code de `strata connect`, T14), c'est-à-dire dans **le Claude Code de ton abonnement**, celui dont tu as besoin pour la comparaison de la section 3. OpenCode a son propre fichier (`~/.config/opencode/opencode.json`), donc **aucun risque pour Claude**. Le prompt système d'OpenCode pèse ≈ 7,4 K tokens, celui de Claude Code ≈ 15,6 K (T14).

- [ ] Installe OpenCode s'il n'est pas là : `npm i -g opencode-ai`. **Son premier lancement télécharge un plug-in depuis npm** (internet nécessaire une fois, plus d'une minute possible, T14) : lance-le **maintenant**, avant de couper quoi que ce soit.
- [ ] Une fois Strata servi :

```powershell
strata connect opencode              # affiche la config (adresse, modèle, contexte)
strata connect opencode --write      # l'écrit après avoir demandé, avec sauvegarde
strata connect opencode --check      # envoie 1 prompt et 1 appel d'outil
```

  Le `--check` doit dire « passed » pour les deux. **Filme-le** (plan P09).
- [ ] **Si tu veux quand même Claude Code sur Strata** : ne fais PAS `--write`. Ouvre une fenêtre PowerShell dédiée, copie les variables que `strata connect claude-code` affiche, vérifie ensuite dans une **autre** fenêtre que `echo $env:ANTHROPIC_BASE_URL` est vide. (Tes fonctions `claude-ref` / `claude-local` du profil PowerShell, citées dans `modeles-5080.md`, font peut-être déjà ça : à vérifier.)
- [ ] **Terminal en deux volets** (Windows Terminal, `Alt+Maj+D` pour couper) : à gauche OpenCode, à droite `strata monitor --url http://127.0.0.1:8080`, vue **1 (Overview)**. C'est là que tu lis les **tok/s** (OpenCode n'en affiche pas). La vue **6 (Logs)** garde la vitesse par requête : regarde-la à la fin de chaque génération.

### 1.4 Ce qu'il faut fermer, et ce qu'il faut noter

Fermer **avant** de lancer Strata, et le laisser fermé pendant les générations (la doc : la RAM est le verrou ; le Coder demande 23 Go d'experts + environ 10 Go pour le reste, T5, T15) :

- [ ] **Chrome / Edge / Firefox** (tout, y compris les processus en arrière-plan : Gestionnaire des tâches, trier par mémoire)
- [ ] LM Studio : **Quit** dans l'icône près de l'horloge, pas juste la fenêtre (il garde de la VRAM et de la RAM)
- [ ] `llama-server` s'il tourne (même port 8080), Discord, Steam, launchers, Docker, VS Code, Photoshop/Photopea
- [ ] Mode « Ne pas déranger » de Windows (pas de notification dans le film) ; barre des tâches sans applis de travail
- [ ] Si ton écran est branché sur l'iGPU du 9700X (à ta convenance) : Strata garde alors 512 Mio de VRAM pour l'affichage au lieu de 1 536 (T5). Note sur quoi est branché l'écran.
- [ ] Horloge de la barre des tâches **avec les secondes** (Paramètres > Heure et langue > Date et heure > « Afficher les secondes ») : c'est ta preuve de durée à l'écran.

À **noter avant les tests** (fiche, section 6) : version de Strata + moteur ; pilote ; Windows ; contexte ; mode `resident` ou `mmap` ; RAM libre et VRAM utilisée au repos (Gestionnaire des tâches) ; RAM libre et VRAM une fois le modèle chargé (moniteur + Gestionnaire).

### 1.5 Réglages OBS

- [ ] Scène « Écran 1 » : capture d'affichage, **1920 × 1080**, 60 images/s. Désactive l'aperçu s'il gêne.
- [ ] Sortie avancée : encodeur **NVENC H.264** (il décharge le processeur, que Strata occupe pour calculer les experts ; un encodage x264 fausserait les tok/s), contrôle **CQP 19**, préréglage qualité, format **MKV** (survit à un plantage), à remuxer en MP4 après.
- [ ] **Enregistre sur un autre disque** que celui des experts (si Strata passe en lecture SSD, ne mélange pas les écritures).
- [ ] **Pas de micro** : la voix sera générée. Son du bureau activé (le jeu et le site font des bruits).
- [ ] **Test de 1 minute** avant de commencer : lance Strata, enregistre 30 s, regarde dans le moniteur si le tok/s change quand OBS tourne. Note l'écart ⟦…⟧. Si la RAM libre tombe trop bas avec OBS ouvert, plan B n° 8.
- [ ] **Un fichier par plan** (`P12-test1-jeu.mkv`) : arrête et relance l'enregistrement entre les plans ; plus simple pour le montage.
- [ ] À ne **pas** montrer : `strata launch --show-key`, une clé d'API, les onglets du navigateur, tes dossiers de travail.

### 1.6 Les dossiers de test

- [ ] Crée trois dossiers vides, **hors de `youtubeSkill`** : `D:\strata-demo\jeu`, `D:\strata-demo\site`, `D:\strata-demo\voxel`. Chaque test s'exécute dans **son** dossier vide, `index.html` à écrire.
- [ ] Prépare les trois prompts dans un fichier texte sur le Bureau (copie-colle depuis la section 2), pour ne rien retaper à la caméra.

---

## 2. Les trois tests de démo

**Protocole commun**
1. `cd` dans le dossier du test, lance `opencode`, vérifie que le modèle choisi est celui de Strata (`strata/…`).
2. Colle le prompt. **Note l'heure (secondes comprises) à Entrée.** Lance l'enregistrement avant.
3. Ne touche à rien. Filme le volet du moniteur. Note le tok/s **pendant** l'écriture : valeur basse, typique, haute (regarde le moniteur toutes les 30 s ; à la fin, la vue Logs a la vitesse par requête).
4. Note l'heure de fin (« done » ou dernier fichier écrit). Durée totale = fin − début.
5. **Le navigateur reste fermé** (section 4 du déroulé : tu ouvres les résultats après avoir arrêté Strata).
6. **Limite de temps par test : 25 minutes** (réelles). Au-delà, arrête, note « temps dépassé » et ce qui existe sur le disque. C'est filmable.
7. Relances (après ouverture du résultat, section 2.4) : **2 au maximum** par test, message type : `It does not work: <copie l'erreur de la console>. Fix it.` Compte-les. Si tu as dû redémarrer le moteur toi-même, c'est une « relance technique » à noter à part.

**Verdict à 4 niveaux** (par test) :

| Verdict | Critère |
|---|---|
| **OK du premier coup** | S'ouvre sans erreur dans la console et les 5 points du prompt marchent, sans relance |
| **OK après N relance(s)** | Les 5 points marchent après 1 ou 2 relances |
| **Partiel** | S'ouvre mais x points sur 5 ne marchent pas, ou le fichier est coupé |
| **Raté** | Ne s'ouvre pas, écran noir ou blanc, ou rien d'utilisable après 2 relances |

Pour chaque test, note le score **x / 5** : un point par exigence du prompt qui marche à l'écran.

### 2.0 Avant le test 1 : le calibrage (non filmé pour la vidéo, ne compte pas)

Le premier essai compte (règle du tournage), donc on vérifie **d'abord** que le harnais n'a pas un défaut qui couperait tout. Un fichier d'environ 300 lignes, **différent des trois tests** :

```text
Create a single-file index.html: a to-do list app with add, edit, delete, mark as done, filters (all / active / done), a counter, local storage persistence and a dark mode toggle. Put comments in the code. About 300 lines. All CSS and JavaScript inline, no libraries.
```

- [ ] Dossier `D:\strata-demo\calibrage`. Chronomètre : **10 minutes maximum**. Note la durée, le tok/s, et **si le fichier est complet** (il finit par `</html>`).
- [ ] **Fichier coupé ou jamais fini** : relance Strata avec un contexte plus grand **avant** les trois tests : `strata launch --preset "Coder 64K" --context 98304 --restart` (la doc donne `32k`, `64k`, `128k`, `256k` « ou un nombre de tokens » : écris le nombre, pas « 96k »). La réponse maximale passe à 12 288 tokens (T13). Puis `strata connect opencode --write` **de nouveau** (il met le contexte à jour dans OpenCode). Refais le calibrage ; au besoin `128k`.
- [ ] **Ça marche** : note « calibrage OK à 64K » et passe au test 1.

**Avant d'appuyer sur Entrée pour chaque test, écris une phrase : « mon pronostic : … »** dans la fiche (section 6). Le script en a besoin pour la 3D (`⟦à écrire : ton pronostic avant le test 3D⟧`), et ce qu'on écrit après coup est toujours trop malin.

### 2.1 Test 1 : le jeu (un seul fichier HTML)

**Prompt exact (anglais, mieux tenu par le modèle ; le Coder est « plus faible hors de l'anglais », T5) :**

```text
Create a complete Breakout / Arkanoid game in a single file named index.html. No external libraries and no external files: all HTML, CSS and JavaScript inline. Use an 800x600 canvas with a dark neon look.
Requirements:
1. 6 rows of colored bricks, a paddle controlled by the mouse and by the left/right arrow keys, and a ball that bounces on the walls, the paddle and the bricks (the bounce angle depends on where the ball hits the paddle).
2. A score, 3 lives, a game over screen and a win screen, both showing "Press SPACE to restart".
3. Two power-ups that fall from some destroyed bricks: a wider paddle, and a multi-ball (3 balls).
4. Short sound effects made with the Web Audio API (no audio files).
5. The game must work as soon as I open index.html in a browser, with no errors in the console.
Write the whole file in one go, then give me a two-line summary.
```

**Pour la voix (traduction)** : « Fais-moi un casse-briques complet dans un seul fichier : 6 rangées de briques colorées, la raquette à la souris et aux flèches, un score, 3 vies, un écran de défaite et de victoire, deux bonus (raquette large, multi-balles), des bruitages sans fichier audio, et ça doit marcher du premier coup, sans erreur dans la console. »

**À filmer** : (P12) le prompt collé et Entrée, l'horloge visible ; le volet moniteur qui défile, **le compteur de tok/s lisible** ; un accéléré de la génération (garde l'horloge) ; (P20, après coup) le jeu ouvert dans le navigateur, **30 secondes de partie**, un bonus qui tombe, la console F12 (vide ou en erreur). Le plan du jeu **qui tourne** est le premier plan du hook.

**À mesurer** (fiche) : tok/s bas / typique / haut ; vitesse de lecture du prompt (affichée par le moniteur au début) ; durée totale ; la réponse a-t-elle été **coupée** (le fichier finit au milieu d'une fonction) ; nombre de relances ; **premier coup oui/non** ; score x / 5 ; RAM libre et VRAM au pic.

**Repère** : la version de ta carte en Q4 débordant était tombée à 13 tok/s sur le même genre de test chez un autre testeur (T16) : si tu retrouves un Arkanoid, tu peux comparer, **sans** prétendre que c'est le même prompt.

### 2.2 Test 2 : le site web (landing page)

**Prompt exact :**

```text
Create a modern, responsive landing page for a fictional mobile-money app called "Tikaya" that lets friends split bills and send money to each other in seconds. Single file index.html, all CSS and JavaScript inline, no external libraries and no image files (use inline SVG for icons and illustrations). Dark theme with a warm orange accent.
Requirements:
1. A hero section with a headline, a sub-headline, a call-to-action button and a phone mockup made with CSS or SVG.
2. A "How it works" section with 3 steps, and a features section with 6 cards.
3. A pricing section with 3 plans (Free, Plus, Pro), the middle one highlighted.
4. A FAQ with 5 questions as an accordion that really opens and closes, and a footer.
5. It must look good on a phone (375 px wide) and on a desktop, with smooth scrolling and subtle scroll animations, and no errors in the console.
Write the whole file in one go.
```

**« Tikaya » est un nom inventé et vérifié le 11/11** : aucune société ni appli de paiement trouvée sous ce nom dans une recherche web. J'ai écarté « Kora » : c'est une vraie société de paiement, active en Afrique, y compris en zone francophone. Revérifie « Tikaya » en 10 secondes avant de filmer ; sinon prends un autre nom inventé.

**Pour la voix** : « Une page de présentation pour une appli de paiement mobile qui n'existe pas : une présentation avec un bouton, 3 étapes, 6 cartes, 3 tarifs, une FAQ qui s'ouvre et se ferme, et ça doit tenir sur un téléphone. »

**À filmer** : (P13) le prompt collé, l'horloge, le moniteur ; (P21) la page ouverte, **défilement lent de haut en bas**, ouverture de la FAQ, puis F12 → mode téléphone (375 px) pour la version mobile.

**À mesurer** : mêmes champs qu'au test 1. Vérifie le point 5 en vrai (F12, largeur 375).

### 2.3 Test 3 : la démo 3D voxel (three.js)

Pour que le modèle n'invente pas une adresse de bibliothèque inexistante, le prompt impose **une adresse qui répond** (testée le 11/11 : réponse 200, T17) et une version classique (sans modules, donc ouvrable par double-clic).

**Prompt exact :**

```text
Create a 3D voxel island demo in a single file index.html using three.js r128, loaded with a classic script tag from exactly this URL: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js (no ES modules, no OrbitControls, no other library).
Requirements:
1. Generate a procedural island with your own noise function: a grid of at least 48x48 columns of cubes, drawn efficiently with THREE.InstancedMesh, colored by height (sand, grass, rock, snow).
2. A semi-transparent water plane around the island.
3. At least 15 voxel trees (trunk and leaves made of cubes), placed on the grass only.
4. Camera: the user drags the mouse to orbit around the island and uses the wheel to zoom (implement it yourself); the island also rotates slowly when idle.
5. Soft lighting with shadows, a sky-colored background, and the key N toggles day and night.
It must render as soon as I open index.html, with no errors in the console. Write the whole file in one go.
```

**Pour la voix** : « Une île en cubes, en 3D : relief généré, eau, au moins 15 arbres, caméra qu'on tourne à la souris, lumière et ombres, touche N pour la nuit. Un seul fichier. »

**À filmer** : (P14) prompt + moniteur ; (P22) l'île ouverte, **rotation à la souris 15 s**, zoom, touche N ; la console.

**À mesurer** : mêmes champs ; en plus **fluide ou pas** (la page tient-elle 30 images/s ? onglet Performance de la F12, ou « ça rame » à l'œil). Écran noir = « Raté » : regarde d'abord la console (adresse de la bibliothèque refusée ? erreur d'API three.js r128 ?).

### 2.4 Après les trois générations : l'ouverture des résultats

- [ ] **Arrête Strata** (`strata launch --stop`) une fois les trois premiers essais **tous** écrits : ça libère la RAM et la VRAM.
- [ ] **Alors** ouvre le navigateur (une seule fenêtre) et les trois `index.html` (double-clic). Filme : P20, P21, P22. Note le verdict et le score pour chacun, **avant** toute relance.
- [ ] **Relances** (si besoin) : `strata launch --preset "Coder 64K"` (le modèle est prêt en ≈ 30 s chez un testeur, T4 ; mais compte jusqu'à plusieurs minutes), puis `opencode --continue` dans le dossier du test pour reprendre la session (à vérifier : sinon colle ta demande de correction dans une nouvelle session en citant l'erreur). Compte les relances, **ferme le navigateur** avant de relancer.

### 2.5 Une mesure de vitesse propre (le plan du hook)

Juste après que Strata sert (avant le test 1), plan court, moniteur **en plein écran** :
- [ ] **Dans OpenCode** (pas dans la page web : le navigateur reste fermé) : « Hi, how are you? », puis « Tell me a short story about a dragon who loves video games. » Garde la vue 1 du moniteur lisible pendant les 20 s d'écriture. Note le tok/s (court / après quelques lignes). C'est le plan P10, le plus propre pour afficher la vitesse (et le tok/s du hook si les tests sont trop moches).

---

## 3. La comparaison : le même prompt à Claude

**Principe** : même texte (copie exacte des trois prompts), **une seule tentative**, aucune relance, dossier vide, chronomètre. On compare avec le local au même niveau de demande, comme la référence le fait avec Opus.

- [ ] Ouvre une **nouvelle** fenêtre PowerShell sans variable Strata : `echo $env:ANTHROPIC_BASE_URL` doit rester vide. Ne touche pas à `~/.claude/settings.json`.
- [ ] Dans `D:\strata-demo\claude-jeu`, `claude-site`, `claude-voxel` (dossiers vides) : `claude`, vérifie le modèle avec `/model` (note **le nom exact et le niveau d'effort**), colle le prompt, note l'heure de début et de fin.
- [ ] Alternative : l'interface web de Claude, si Claude Code te gêne : dis-le dans la vidéo, car ce n'est pas le même outil que OpenCode (la demande est la même, pas le harnais).
- [ ] Ouvre les trois résultats **côte à côte avec ceux du local** (deux fenêtres de navigateur). Filme-les (P30 à P32).
- [ ] Verdict : mêmes critères (x / 5, relances = 0 puisqu'il n'y en a pas), durée, et **ton avis**, noté dans `⟦à écrire⟧` : « lequel je garderais ? ».
- [ ] Ne donne **pas** un classement de qualité global à partir de 3 essais : c'est « sur ces trois demandes, une tentative ».

---

## 4. Plan B : que faire quand ça casse

L'échec se filme. Pour chaque cas : le symptôme, ce que tu fais, ce que tu notes.

**4.1 Le téléchargement n'avance pas ou le disque est plein**
- Strata reprend un téléchargement interrompu. 58 Go à 100 Mbit/s ≈ 1 h 18 ; à 50 Mbit/s ≈ 2 h 36 (calcul : 58,4 Go × 8 ÷ débit). Si, 30 minutes après le début, il reste plus de 2 h : continue les plans de coupe (section 5, P01 à P05), prépare OBS, et filme pendant que ça télécharge ; ce **temps d'attente est un plan** (« ça télécharge… »).
- Rien d'autre dans Strata ne remplace le Coder sur 32 Go (T5). Si le modèle n'est pas là à la fin de la soirée : **décale la vidéo** (une vidéo calculée peut prendre le créneau du lundi) plutôt que de changer de modèle. Note-le, ce n'est pas un échec de tournage.

**4.2 Le modèle est « trop gros » pour la RAM**
- Symptômes : le plan dit « does not fit » ou « may run slower » ; au démarrage, le moteur parle de lecture sur le SSD ; le PC se fige plus de 10 minutes ; l'écran Advanced montre `--mmap-experts` au lieu de `--resident-experts` (T8).
- Ordre des remèdes (relance après chacun, **un seul à la fois**, note le tok/s) :
  1. Re-ferme tout (navigateur, Gestionnaire des tâches : RAM libre au repos, **avant** de lancer Strata).
  2. Écran branché sur l'iGPU (réserve 512 Mio au lieu de 1 536 Mio, T5).
  3. Contexte **32K** : `strata launch --preset "Coder 64K" --context 32k --restart` (moins de mémoire de conversation).
  4. Sans la couche de prédiction : `--mtp off` (≈ 1 Go de VRAM gagné, plus lent ; un rapporteur dit que certains fichiers IQ natifs refusent de démarrer sans, T11).
  5. Machine qui rame une fois lancée : `--set STRATA_RESIDENT_PIN=0` (problème connu des PC de 32 Go, ticket #649, T9).
- **Si le mode lu sur le SSD est le seul qui démarre : garde-le.** Il fonctionne, c'est lent. Un testeur sur 12 Go de VRAM et 32 Go de RAM a eu ce mode lent : 8,7 tok/s en chat et 41 à 46 sur du code (T4). Filme, note tok/s. La vidéo dit « ça rentre, à ras, et voilà le prix ».

**4.3 « non-finite logits » (le moteur sort des valeurs invalides)**
- Ce qu'on sait : des rapports sur **RTX 5080** (Windows, pilote 617.42, 95 Go de RAM) avec **IQ3_S et IQ3_XXS** (pas le Coder), les tickets #5043, #5046 et #5055, fermés pour mise en forme et **non résolus** ; le ticket général #879 (dégénérescence « un seul mot répété ») est fermé et le moteur a une protection pour les cartes NVIDIA et AMD (T11). On dit **« un utilisateur de 5080 rapporte »**, jamais « Strata ne marche pas sur 5080 ».
- Si ça t'arrive : **ne ferme pas la fenêtre**, filme le message. Copie la ligne exacte du journal (vue 6, Logs). Note la version, le pilote, le contexte. Essaie dans l'ordre : relancer le moteur (`--restart`) ; contexte 32K ; `strata update` puis relancer ; `--mtp off`. Si ça revient, c'est ton **résultat** : « ça casse ici ».

**4.4 La vitesse s'effondre**
- Repères publiés (T7, T4, T19) : 70 tok/s en chat court sur une 5070 Ti (**réflexion coupée, température 0**, donc pas comparable à tes tests avec réflexion) ; 41 à 46 sur du code en mode lent sur 12 Go ; 40 tok/s environ pour le Coder sur 16 Go + 32 Go dans une comparaison. **Ce sont des repères, pas des promesses.**
- Si tu es à moins de la moitié d'un de ces repères : (a) VRAM libre à 0 : la doc dit que le décodage peut tomber de 100 à 14 tok/s sous Windows (T9) → regarde la VRAM dans le moniteur, ferme ce qui l'utilise ; (b) RAM saturée, Windows écrit sur le disque → Gestionnaire des tâches, onglet Performances → Mémoire ; (c) `mmap` au lieu de `resident` (4.2) ; (d) la température de la carte (`nvidia-smi`) ; (e) la version : une régression de 25 % entre deux versions du moteur a été rapportée sur 5080 (T20) : **note la version**, compare avec le tok/s de ta mesure P10. (f) OBS : refais la mesure sans OBS, 30 s.

**4.5 Le fichier est coupé, ou le modèle tourne en boucle**
- Le code s'arrête au milieu : la réponse est plafonnée à ⅛ du contexte (8 192 tokens à 64K) et la réflexion en fait partie (T13). Remèdes : (1) baisse la réflexion (1.2, côté serveur) ; (2) relance avec `--context 98304` (réponse maximale ≈ 12 288) ou `128k` (16 384, mais ≈ +0,9 Go de RAM de conversation, T21), puis `strata connect opencode --write` de nouveau ; (3) **repli sans harnais**, une fois les générations finies et le navigateur autorisé : ouvre la page de chat de Strata (`http://127.0.0.1:8080`), colle le prompt, copie le HTML dans `index.html`. Dis-le : c'est un repli, pas un agent.
- Boucle de réflexion : arrête, relance avec la réflexion plus basse ; `reasoning_loop_recovery` existe (désactivé par défaut) mais peut confondre du code répété avec une boucle (T10).
- Appel d'outil refusé par OpenCode (« invalid tool call » ou rien n'est écrit) : Strata lit plusieurs formes d'appels d'outil depuis la 0.2.8 (T22). Si ça persiste, repli chat (ci-dessus) et note-le.

**4.6 Le moteur plante (« exit code -6 »), surtout après un long prompt**
- Le ticket **#5104** (ouvert) décrit exactement ça avec le **Coder IQ1_M** : une lecture de prompt de plusieurs milliers de tokens fait planter le moteur (« could not copy experts 256.. », code -6), avec un message qui parle à tort de manque de RAM (T23). Le prompt système d'OpenCode (≈ 7,4 K tokens) est dans cette zone. Contournement du rapporteur : `--set STRATA_PREFILL_LAYER_MAJOR=0` au lancement (la lecture du prompt devient lente chez lui, sur une carte de 8 Go ; sur la tienne ça reste à mesurer). Un correctif candidat existe, il n'est pas dans la 0.2.13.
- Note : le texte exact du message, et si le contournement a marché.

**4.7 Le code est livré mais ne marche pas**
- Applique le protocole (2 relances max). Une fois les 2 relances faites, **ne corrige pas à la main**. Note les erreurs de la console ; c'est le verdict.
- L'échec vaut une scène : ouvre la console F12, montre l'erreur, ouvre l'éditeur et montre la ligne si c'est lisible.

**4.8 La RAM manque quand OBS tourne**
- Mesure : la RAM libre que le moniteur affiche avec et sans OBS. Si Strata bascule en mode lent à cause d'OBS : ferme l'aperçu OBS, baisse à 1080p30, ou essaie l'enregistreur de la barre de jeu de Windows (`Win+Alt+R`, à tester sur 30 s). Si rien ne marche : **filme avec ton téléphone** l'écran du moniteur (tok/s) pour le plan de la vitesse. Ce n'est pas joli, mais c'est vrai.

---

## 5. La checklist des plans à enregistrer, dans l'ordre du tournage

Les numéros P01… sont ceux du [storyboard](storyboard.md). **Un fichier par plan.**

**Avant de lancer le modèle (la RAM est libre, le PC est calme)**
- [ ] **P01** : la tour allumée, la 5080 vue par la vitre (téléphone, 10 s, **pas de visage**).
- [ ] **P02** : https://github.com/Niko1221/Strata, défilement lent du README, étoiles, version `0.2.13` dans les releases (15 s).
- [ ] **P03** : la fiche Hugging Face du Coder (« experimental release », les deux fichiers de 29,6 et 28,8 Go) (15 s).
- [ ] **P04** : Gestionnaire des tâches au repos : RAM (utilisée / disponible), GPU 16 Go ; `nvidia-smi` avec la version du pilote (15 s).
- [ ] **P05** : l'installation (PowerShell), `strata doctor`, `strata launch --plan …` avec « fits / tight » (60 s, accélérable).

**Le premier lancement**
- [ ] **P06** : `strata launch` guidé, écran par écran (Model → Coder, Context, Advanced : la ligne `--resident-experts` ou `--mmap-experts` bien lisible).
- [ ] **P07** : téléchargement (accéléré) puis « Preparing your model », le curseur qui saccade, la RAM qui monte dans le Gestionnaire des tâches (garde 20 s en temps réel, le reste en accéléré).
- [ ] **P08** : le moniteur vue 1 une fois servi : état « serving », VRAM et RAM utilisées (10 s).
- [ ] **P09** : `strata connect opencode --write`, puis `--check` avec les deux validations.
- [ ] **P10** : le plan vitesse propre (section 2.5) : « Hi », l'histoire du dragon, moniteur en grand (20 s).

**Les générations (navigateur fermé, un enregistrement par test)**
- [ ] **P11** : OpenCode ouvert, le modèle choisi (`strata/…`), dossier vide.
- [ ] **P12** : test 1 (jeu) : prompt, génération, moniteur, horloge. Garde 5 s à l'arrivée du dernier fichier.
- [ ] **P13** : test 2 (site) : idem.
- [ ] **P14** : test 3 (voxel) : idem.
- [ ] **P15** : le Gestionnaire des tâches pendant une génération (RAM presque pleine, VRAM, la carte au travail ; 15 s) et la RAM libre minimale lue dans le moniteur.
- [ ] **P16** : tout plantage, blocage, message d'erreur : le moment exact (`non-finite logits`, `exit -6`, écran figé).

**Après avoir arrêté Strata et ouvert le navigateur**
- [ ] **P20** : le jeu, ouvert, 30 s de partie, console F12.
- [ ] **P21** : le site, défilement, FAQ, version téléphone.
- [ ] **P22** : l'île voxel, rotation, zoom, touche N, console.
- [ ] **P23** : les relances si tu en as fait (prompt de correction, nouveau résultat).

**La comparaison**
- [ ] **P30** : Claude, le jeu : prompt, durée, résultat côte à côte avec le local (P12/P20).
- [ ] **P31** : Claude, le site : idem.
- [ ] **P32** : Claude, la 3D : idem.
- [ ] **P33** : un plan à deux fenêtres qui résume : les trois résultats locaux et les trois résultats Claude.

**Captures web (5 min, à tout moment, hors tournage)** : voir la liste C1 à C6 en bas du [storyboard](storyboard.md) (les tickets GitHub #4997, #5104, #5046, les pages de doc, les miniatures des vidéos du 09/11 et du 02/11).

**Plans de fin**
- [ ] **P40** : `strata --version`, `strata status --json` (**sans la clé**), `nvidia-smi` : pour afficher les versions dans la vidéo.
- [ ] **P41** : `strata launch --stop` (la RAM et la VRAM qui reviennent dans le Gestionnaire des tâches) : un plan de conclusion.

---

## 6. La fiche de résultats (tu la remplis en tournant)

**Chaque ligne porte le texte exact d'un `⟦…⟧` du [script](script.md)** (croisement fait le 11/11 : 43 trous distincts, une ligne chacun ou groupés quand ils se lisent au même endroit). Remplis sans reformuler ; la colonne de droite dit où lire la valeur. Les lignes marquées « AVANT » se remplissent **avant** de lancer le test.

| Trou du script | Où le lire | Ta valeur |
|---|---|---|
| **Avant : mon pronostic avant le test 3D** (`à écrire`) | AVANT d'appuyer sur Entrée au test 3 | |
| **Avant : réglage de réflexion** | la commande de lancement / la demande courte | |
| tok/s typique (hook) | = la valeur typique du **jeu** (test 1), pas un maximum | |
| tok/s du jeu, bas / typique / haut | moniteur vue 1, vue 6 (Logs) à la fin | |
| tok/s du site | idem | |
| tok/s de la 3D | idem | |
| durée du jeu / du site / de la 3D | horloge de la barre des tâches, début → dernier fichier | |
| a marché du premier coup ? oui/non (jeu, site, 3D) | navigateur, avant toute relance | |
| points du jeu qui marchent, sur 5 / du site / de la 3D | les 5 exigences du prompt | |
| ce qui ne marche pas dans le jeu | console F12, à l'écran | |
| ce qui ne va pas dans le site, y compris s'il est coupé | idem + la fin du fichier | |
| relances du site et résultat | nombre de relances, verdict après | |
| nombre de relances (jeu) / verdict final du jeu | | |
| l'île s'affiche ? premier coup oui/non, durée | | |
| le relief est-il crédible ? / eau et arbres ok ? / fluide ou pas | à l'œil, onglet Performance de F12 si besoin | |
| ce qui s'affiche à la place de l'île, premier coup oui/non | si écran noir : la console | |
| relances et verdict final de la 3D | | |
| combien sur trois ont marché (B) | | |
| ce qui a cassé, en une phrase (hook B) | | |
| ce qui a cassé, message exact, version de Strata (section 6) | vue 6 Logs + `strata --version` | |
| durée du premier chargement | du lancement à « serving » | |
| le PC s'est-il figé ? combien de temps | curseur qui saccade, chronomètre | |
| RAM libre au plus bas | moniteur vue 1 ou Gestionnaire des tâches, au pic d'une génération | |
| resident ou mmap | écran Advanced de `strata launch` | |
| plus rapide ou plus lent que le repère, et de combien | ton tok/s du jeu contre ≈ 70 (réflexion coupée chez eux : dis-le) | |
| cause probable de la lenteur (si plus lent) | ton diagnostic parmi 4.4 (a à f) | |
| réglage de réflexion (voix) | = la ligne « Avant » | |
| Claude : durée et verdict du jeu / du site / de la 3D | horloge + 5 points | |
| verdict de la comparaison, en une phrase | | |
| ton avis sur la 3D (`à écrire`) | | |
| ton avis sur ce qui sépare les deux (`à écrire`) | | |
| ta vraie raison d'avoir pris OpenCode (`à écrire`, si autre que « son propre fichier ») | | |
| ton verdict, en une ou deux phrases (`à écrire`) | | |
| la chose qui t'a le plus surpris (`à écrire`) | | |
| ce qui t'a manqué (`à écrire`) | | |

**À noter aussi (pas des trous, mais pour 4.4 et le montage)** : version de Strata (Terminal) / moteur / pilote NVIDIA / Windows ; fichier, contexte ; RAM libre au repos / une fois chargé ; VRAM une fois chargé / au pic ; vitesse de lecture du prompt ; écart avec / sans OBS ; modèle et effort de Claude (`/model`) ; nom exact du modèle chargé dans OpenCode ; résultat du calibrage.
