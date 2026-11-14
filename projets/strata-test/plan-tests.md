# Plan de tests Strata (V2) : à suivre aujourd'hui (mer. 11/11/2026)

> Vidéo : [« Je teste le meilleur modèle possible avec Strata sur ma 5080 »](fiche.md), sortie **lun. 16/11, 18 h**. Machine : RTX 5080 16 Go, 32 Go de DDR5-6000, Ryzen 7 9700X, Windows. Commandes revérifiées le **11/11** dans la doc et le code de Strata et de Pi (faits : [`sources.md`](sources.md), T1…). Ce que tu notes en section 11 remplit les trous **R1 à R15** du [script](script.md). Critique de la V1 : [`grill-v1.md`](grill-v1.md) ; ancienne version : [`plan-tests-v1.md`](plan-tests-v1.md).
>
> **Règle du tournage** : le premier essai compte. Un plantage, un écran figé, une relance : tu les gardes et tu les filmes. Ne rejoue jamais un test pour qu'il soit propre.

**Mis à jour le 13/11 (soir), ta décision : le test 3 devient un mini-Minecraft** (6.3) : un monde en cubes où l'on marche, casse et pose des blocs, à la place de l'île qu'on regarde tourner. Même format (5 exigences, three.js r128), même place de boss final ; Claude refait le test 3 avec ce prompt. Script, storyboard, téléprompteur et notes de miniature suivent.

**Mis à jour le 13/11 : tout passe par l'appli, sans le Terminal** (le plan ci-dessous est réécrit dans ce sens)
- **Déjà fait le 13/11** : l'appli est installée, le Coder est téléchargé et chargé ; Pi 1.4.0 est installé et branché (4.3).
- **L'appli a son propre moniteur** (page Monitor ; la doc ne le montrait pas, T38) : vitesse de sortie (« Decode ») et de lecture (« Prefill ») de la dernière requête, charge et température de la carte, VRAM avec les experts en cache, lecture disque, RAM, remplissage du contexte, et un tableau des requêtes (prompt, sortie, tok/s, durée) avec la moyenne en bas. Il remplace le moniteur du Terminal.
- **L'adresse du serveur de l'appli est `http://127.0.0.1:47831/v1`** (page Serving), pas `8080`. Le nom du modèle est `coder-iq1_m`.
- **La commande `strata` n'existe pas** avec l'installeur seul, et on n'installe pas le Terminal. Il ne revient qu'en plan B (9.3, 9.11).
- **Contexte : 128K** (réglé dans l'appli le 13/11 ; elle avait d'abord pris 200K). `models.json` de Pi est à 131072.
- **Ce qu'on perd** : le contournement du bug #5104 (`STRATA_PREFILL_LAYER_MAJOR=0`) était une option du Terminal. Cherche-le dans les « Expert settings » de l'appli **avant** le calibrage (4.2).

**Changements depuis la V1**
- **Tes décisions du 11/11** : Strata s'installe avec **l'installeur Windows** de la v0.2.13 (l'appli télécharge le moteur et le modèle) ; le harnais est **Pi** (OpenCode passe en plan B, section 9.10). Le Terminal `strata` devait rester pour ce que l'appli ne faisait pas : depuis le 13/11, il n'est plus qu'un plan B (9.3).
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
| 3 | Premier chargement dans l'appli, 2 vérifications, branchement de Pi | 30 min | P07, P06, P09 |
| 4 | Calibrage (non filmé), puis le plan de la vitesse | 15 min | P10 |
| 5 | Les 3 démos locales, **navigateur fermé** | 45 min à 1 h 15 | P12-P16 |
| 6 | Arrêt de Strata, ouverture des résultats, relances en lot, plan de fin | 45 min | P20-P23, P41 |

**Si le temps manque, coupe dans cet ordre** : les captures web (elles se font demain) → les relances → le test 3 (le mini-Minecraft). **Ne coupe jamais** : le plan de la vitesse (P10), le test 1 et son résultat (P12, P20), un plantage (P16).

**Si, 30 minutes après le début du téléchargement, il reste plus de 2 h** : continue l'étape 2, puis prépare le reste. Si le modèle n'est pas là ce soir, **décale la vidéo** plutôt que de changer de modèle : rien d'autre dans Strata ne tient avec 32 Go (T5).

---

## 1. Préparer (20 min)

- [ ] **Pilote NVIDIA 580 ou plus** (les paquets CUDA 13 l'exigent, T2) : `nvidia-smi` dans PowerShell. Note la version.
- [ ] **Disque** : **90 Go libres** sur le SSD des modèles (≈ 58 Go de modèle + ≈ 5 Go de couche de prédiction, T6, T33 ; un testeur a vu 87 Go occupés, T4). Prends `D:\Strata`.
- [ ] **Ferme tout** : Chrome, Edge, Discord, Steam, Docker, VS Code, Photoshop ; LM Studio par **Quit** près de l'horloge (pas juste la fenêtre) ; `llama-server` s'il tourne (il prend de la RAM et de la VRAM). Mode « Ne pas déranger ». Horloge de la barre des tâches **avec les secondes** (Paramètres > Heure et langue > Date et heure) : c'est ta preuve de durée.
- [ ] **OBS** : capture d'affichage 1920 × 1080, 60 i/s ; encodeur **NVENC H.264**, CQP 19, format **MKV** (survit à un plantage) ; enregistrement **sur un autre disque** que `D:\Strata` ; pas de micro, son du bureau activé. **Un fichier par étape** (`P12-jeu.mkv`), pas plus fin. À ne jamais montrer : une clé d'API, les onglets du navigateur, tes dossiers de travail.
- [ ] **Pi** (le harnais, section 4.3) : il lui faut **Node.js 22.19 ou plus** et, sous Windows, **Git for Windows** (Pi lance ses commandes dans Git Bash, T37). Vérifie `node --version` et `git --version`. Puis installe Pi avec l'installeur officiel :

```powershell
powershell -c "irm https://pi.dev/install.ps1 | iex"
```

  (ou `npm install -g --ignore-scripts @earendil-works/pi-coding-agent`). Vérifie `pi --version` : Strata a testé sa config avec **pi 0.74.2** (T14) ; chez toi, **1.5.2** (mise à jour seule le 13/11, branchement vérifié avec 1.4.0). Lance-le dans **Windows Terminal**, pas dans l'ancienne console (la doc de Pi le recommande, T37).
- [ ] **Dossiers vides**, hors de `youtubeSkill` : `D:\strata-demo\calibrage`, `\jeu`, `\voyage` (avec ses photos, déjà prêt), `\voxel`, `\claude-jeu`, `\claude-voyage` (copie `_photos\*.jpg` dans `images\`), `\claude-voxel`.
- [ ] **Les prompts** : copie la section 6 dans un fichier texte sur le Bureau, pour ne rien retaper à la caméra.
- [ ] Revérifie en 10 s que « Sanaka Voyages » n'est pas une vraie agence (aucune trouvée le 13/11 ; sinon, prends un autre nom inventé et change-le partout).

---

## 2. Installer Strata avec l'appli et lancer le téléchargement

### 2.1 Ce que fait l'installeur (vérifié le 11/11, T38)

`Strata-0.2.13-windows-x64-setup.exe` (≈ 113 Mo, sur https://github.com/Niko1221/Strata/releases/tag/v0.2.13) installe **l'appli de bureau** pour ton utilisateur, sans droits d'administrateur. D'après la doc :
- **le moteur n'est pas dedans** : au premier démarrage, l'appli te montre celui de ta carte avec sa taille et un bouton **Download** ;
- **le modèle** se choisit dans la page **Models** de l'appli, avec sa taille et s'il tient sur ta machine, puis l'appli le télécharge dans le dossier que tu choisis ;
- **le mode RAM réduite** est choisi tout seul : l'appli et le Terminal utilisent la même installation (`setup.py`), et c'est elle qui choisit `resident` ou `mmap` (T5, T8) ;
- **le harnais** : l'appli contient un harnais de code à elle, le « DeepSeek Harness », que la doc ne présente qu'avec DeepSeek. Rien ne dit qu'il marche avec le Coder : **on ne l'utilise pas** ;
- **ce que la doc de l'appli ne montrait pas, et qu'on a vu le 13/11** : une page **Serving** (adresse `http://127.0.0.1:47831/v1`, nom du modèle, état, accès réseau local, clé d'API facultative) et une page **Monitor** (tok/s, VRAM, RAM, lecture disque, requêtes). Pi se branche donc à la main sur cette adresse (4.3), sans `strata connect`.
- **ce qui reste incertain** : le contournement du bug #5104 (`STRATA_PREFILL_LAYER_MAJOR=0`). L'appli a des « Expert settings » pour les options du moteur et un journal (Settings > Engine > Diagnostics > View logs), mais rien dans la doc ne dit qu'on peut y mettre ce contournement (4.2).

Fermer l'appli arrête son moteur (T38) : **laisse-la ouverte** pendant tous les tests.

### 2.2 Installer et télécharger (à filmer : P05, P07)

- [ ] Télécharge `Strata-0.2.13-windows-x64-setup.exe` depuis la page de la release, lance-le. Si SmartScreen ou Smart App Control bloque un exécutable : le projet dit que certains ne sont pas encore signés (#735, T9) ; lis `docs/TROUBLESHOOTING.md` avant de toucher à la protection de Windows.
- [ ] Premier démarrage : **Download** sur le moteur proposé (CUDA 13 pour ta carte).
- [ ] Page **Models** : choisis le **Coder** (Qwen3.8-Flash-Next Coder, **IQ1_M**, ≈ 58 Go). C'est le seul fichier que la doc annonce pour « un PC de 32 Go avec une carte de 12 à 16 Go » (T5). Si l'appli te met en avant autre chose (Swift, Gyro), ne le prends pas : la doc dit qu'elle peut présélectionner un autre fichier (T5). **Filme** la ligne du Coder avec son libellé (depuis la 0.2.13 : « fits » ou « may run slower », T32) : c'est **P05**.
- [ ] Dossier : `D:\Strata`. **Images : non** si l'appli le demande (le lecteur d'images tourne sur le processeur sous 24 Go de VRAM et prend ≈ 0,9 Go, T5).
- [ ] Le téléchargement démarre (P07, accéléré au montage). Passe à l'étape 3.
- [ ] Note la version de l'appli et du moteur (attendu : **0.2.13**, publiée le 09/11, T1) : elle sert pour R14.

---

## 3. Pendant le téléchargement : Claude, puis les captures

Le téléchargement ne prend presque pas de RAM : le navigateur est permis **jusqu'au premier chargement**.

**Claude (P30, P31, P32)** : même prompt mot pour mot (section 6), **un seul essai, aucune relance**.
- [ ] Nouvelle fenêtre PowerShell, `cd D:\strata-demo\claude-jeu`, `claude`, puis `/model` : **note le nom exact et l'effort**. Colle le prompt du test 1. Note l'heure de début et de fin.
- [ ] Pareil dans `claude-voyage` (test 2, avec les photos dans `images\`) et `claude-voxel` (test 3, **le prompt du mini-Minecraft** du 13/11 ; si Claude a déjà fait l'île, refais-le avec le nouveau prompt dans un dossier vide).
- [ ] Ouvre les trois `index.html`, filme 20 s de chacun (P30-P32), note la durée et le score x / 5 (R12).
- [ ] **Ne lance jamais une commande qui modifie `~/.claude/settings.json`** : `strata connect claude-code --write` y écrirait (T14). C'est pour ça qu'on branche Pi, pas Claude Code, sur Strata.

**Captures web (C1 à C6, liste en bas du [storyboard](storyboard.md))** : les tickets #4997, #5104, #5046, `MODELS.md`, `DETAILS.md`, la page des versions, la fiche Hugging Face du Coder (P03), la page GitHub (P02). Puis **ferme le navigateur, tout entier** (Gestionnaire des tâches : plus aucun processus Chrome ou Edge).

**P04** : le Gestionnaire des tâches au repos, onglet Performances : la RAM (32 Go), la carte (16 Go). 15 s.

---

## 4. Premier chargement, 2 vérifications, branchement de Pi

### 4.1 Le premier chargement, dans l'appli (P07)

- [ ] Le téléchargement fini, **charge le Coder dans l'appli** (Load), contexte **128K**. L'étape « Preparing your model » prend environ 5,5 minutes sur une installation neuve en 0.2.13 (T3) et n'a lieu qu'une fois. **Ne touche à rien** : la souris peut se figer quelques minutes ; au-delà de 10 minutes figé, redémarre le PC, ferme tout, recommence (T9). **Filme** le Gestionnaire des tâches, la RAM qui monte. **Chronomètre** du clic à la fin du chargement (R4). *Fait le 13/11 : si tu ne l'as pas chronométré, dis seulement si le PC s'est figé.*
- [ ] Page **Serving** : « API listening · Model ready », Model ID `coder-iq1_m`. **Laisse l'appli ouverte** jusqu'à la fin des tests.

### 4.2 Deux vérifications dans l'appli (P06)

**Vérification 1 : le mode (R6).** `--resident-experts` (les experts que la carte ne garde pas sont copiés en RAM, rien n'est lu sur le SSD pendant les réponses) ou `--mmap-experts` (une partie lue sur le SSD, beaucoup plus lent, T8). Dans l'appli :
- ouvre le journal (Settings > Engine > Diagnostics > View logs) et cherche `resident` et `mmap` (Ctrl+F) : la ligne de démarrage du moteur doit en contenir un ;
- et surtout, **regarde la case « Disk read » du moniteur pendant une génération** (le calibrage, section 5) : si elle reste près de 0 Mo/s, rien n'est lu sur le SSD, c'est le mode resident. Si elle monte à des centaines de Mo/s pendant qu'il écrit, c'est le mode mmap. C'est ce plan-là que tu filmes : il se comprend sans commande.

**Vérification 2 : le bug #5104.** Ce bug fait planter le Coder quand il lit une demande longue (« could not copy experts 256.. », code de sortie **-6**). Il touche tous les fichiers à 256 experts, donc le Coder, mais seulement quand le moteur choisit une lecture « couche par couche » ; plusieurs utilisateurs l'ont eu sur des cartes de 8 et 12 Go, dont une RTX 5070 ; personne n'en parle sur 16 Go (T23).
- [ ] Dans le même journal, cherche **`layer-major`**. Pas de ligne : rien à faire, le calibrage confirmera.
- [ ] Ligne trouvée : cherche `STRATA_PREFILL_LAYER_MAJOR` (ou « prefill ») dans les **Expert settings** de l'appli, mets-le à **off** (ou 0), recharge le modèle. Si l'appli ne l'a pas, ne fais rien encore : le calibrage dira si le bug frappe vraiment (plan B 9.3).

### 4.3 Brancher Pi sur l'appli (P09, à filmer) : fait et vérifié le 13/11

**Pourquoi Pi** (ta préférence, confirmée par les chiffres de Strata, T14) : son prompt système et ses outils pèsent **≈ 1 500 tokens**, le plus petit des huit harnais que Strata sait brancher, contre **≈ 7 400** pour OpenCode. Ça fait **≈ 5 900 tokens de moins à chaque requête**. Deux effets concrets :
- **le bug #5104** n'a été vu que sur des demandes de **3 300 tokens et plus** (T23) : la première requête de Pi (≈ 1 500 + ≈ 350 pour le prompt du test) passe en dessous, celle d'OpenCode (≈ 7 800) au-dessus. Les tours suivants sont plus longs : **le risque baisse, il ne disparaît pas** ;
- moins à relire à chaque requête : la vitesse baisse quand le contexte grandit (T30).
- Le prix : Pi a besoin de Git Bash sous Windows (section 1).

**Comment c'est branché.** Sans le Terminal, pas de `strata connect pi` : on écrit à la main le fichier que cette commande aurait écrit, `~/.pi/agent/models.json` (format de la doc de Pi, T37). Trois valeurs comptent : l'**adresse** de la page Serving, le **nom du modèle** de la même page, la **limite de réponse**.

```json
{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "strata": {
      "baseUrl": "http://127.0.0.1:47831/v1",
      "api": "openai-completions",
      "apiKey": "strata-local",
      "compat": { "supportsDeveloperRole": false, "supportsReasoningEffort": false },
      "models": [
        {
          "id": "coder-iq1_m",
          "name": "Qwen3.8-Flash-Next Coder IQ1_M (Strata, local)",
          "reasoning": true,
          "input": ["text"],
          "contextWindow": 131072,
          "maxTokens": 32000,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
        }
      ]
    }
  }
}
```

- `apiKey` : une clé factice ; l'appli n'en demande pas tant que « API key » n'est pas réglée (T37).
- `contextWindow` : 131072 = les 128K choisis dans l'appli. Si tu changes le contexte dans l'appli, change-le ici.
- **`maxTokens` : 32000**, la limite de réponse. Sans cette ligne, Pi demande au plus **16 384** tokens (son défaut, T37), et c'est aussi ce que `strata connect pi` aurait écrit à 128K (un huitième du contexte, T13). Or **la réflexion compte dans cette limite**, et le serveur ne l'arrête qu'au dernier quart (T13) : il pourrait ne rester qu'environ 4 000 tokens pour le fichier. Un jeu complet en fait plusieurs milliers. Le serveur adapte de lui-même la limite à la place qui reste dans le contexte (T31). *Déduit du code et des docs, pas d'un essai : le calibrage le vérifie.*

**Vérifié le 13/11** : `pi --list-models strata` affiche `strata  coder-iq1_m  …  32K  thinking yes`, et `pi -p --model strata/coder-iq1_m "Reply with exactly: OK"` répond `OK` en 9 s. Si un jour le nom du modèle change, la page Serving (Model ID) ou `Invoke-RestMethod http://127.0.0.1:47831/v1/models` le donne.

**Le filmer, sans voix (P09).** La voix vient après, donc l'image doit se comprendre seule et **chaque plan tenir immobile 3 à 5 s** (le temps d'une phrase au montage). Souris lente, pas de défilement rapide, police du terminal agrandie (Ctrl + molette).
1. **L'appli, page Serving** : 5 s immobile, puis passe la souris sur « API base URL » et sur « Model ID ». *(Rien à cacher : aucune clé n'est réglée.)*
2. **Windows Terminal** : `notepad $HOME\.pi\agent\models.json`. Le fichier entier 3 s, puis **sélectionne** une à une `"baseUrl"`, `"id"` et `"maxTokens": 32000` (3 s chacune). Au montage : zoom et surlignage sur ces trois lignes.
3. Ferme le Bloc-notes, `pi --list-models strata` : la ligne du modèle, 4 s.
4. `cd D:\strata-demo\calibrage`, `pi`, puis `/model` et **choisis `strata/coder-iq1_m`** : 4 s sur le choix.
5. Écran partagé : Pi à gauche, la page **Monitor** de l'appli à droite (`Win + ←` et `Win + →`). Vérifie que les cases restent lisibles à demi-largeur ; sinon, mets le moniteur en plein écran pour les plans de vitesse.

Ce que la voix dira dessus (script, section 4 et point quatre de la liste du soir) : l'appli te donne une adresse ; tu la mets dans le fichier de Pi avec le nom du modèle ; tu montes la limite de réponse. Mets le fichier entier dans la description.

**Le moniteur** : la page **Monitor** de l'appli. Pi n'affiche pas les tok/s : c'est le moniteur qui les donne. Après chaque génération, regarde le tableau **Recent requests** (une ligne par requête de Pi : prompt, sortie, tok/s, durée) et la phrase en bas (« In N requests your average output was … tok/s »). Une tâche de Pi fait **plusieurs requêtes** (une par appel d'outil) : pour R1 et R10, note la moyenne des lignes du test, pas une seule ligne.

---

## 5. Calibrage (non filmé, 10 min max), puis le plan de la vitesse

**Le calibrage** vérifie trois choses avant les vrais tests : pas de plantage, un fichier écrit **en entier**, et la durée de la réflexion. Dans `D:\strata-demo\calibrage`, lance `pi`. S'il demande s'il peut faire confiance au dossier, réponds oui (il est vide). Vérifie avec `/model` que le modèle est celui de `strata`, puis :

```text
Create a single-file index.html: a to-do list with add, delete, mark as done, a counter of tasks left, and a dark mode toggle. All CSS and JavaScript inline, no libraries. About 150 lines.
```

| Ce que tu vois | Ce que tu fais |
|---|---|
| Le fichier existe et finit par `</html>` | Note « calibrage OK », la durée, le tok/s. Passe au plan de la vitesse. |
| Le moteur plante : `could not copy experts`, `exit code -6`, « running out of RAM » (dans Pi ou dans le journal de l'appli) | C'est #5104. **Filme l'erreur** (P16), copie la ligne exacte du journal, puis plan B 9.3. **Note-le** : c'est un résultat (R14). |
| Le fichier est coupé ou jamais écrit | **Fais une capture d'écran de la fin du fichier** (V23b du storyboard). Rouvre `models.json` : `"maxTokens"` doit valoir 32000. Corrige, quitte et relance Pi, refais le calibrage. Si c'est encore coupé : plan B 9.4. |
| Pi répond « connection refused » ou rien | L'appli est-elle ouverte, page Serving « Model ready » ? L'adresse est-elle toujours `47831` ? |
| Pi ne trouve pas Bash | Installe Git for Windows, ou suis 9.10 (OpenCode). |
| Plus de 10 minutes sans fin | Arrête (`Échap` dans Pi). Regarde le moniteur : la réflexion tourne-t-elle en boucle ? Plan B 9.4. |

**Calibrage du 13/11, 19 h (128K, Opera ouvert)** : réussi. `index.html` de 148 lignes, qui finit par `</html>`, écrit vers 19:03. Pas de plantage, mais la première requête faisait 1 884 tokens, sous le seuil de #5104 (3 300). Moniteur : **77,2 tok/s** sur la requête finie, 81,5 en cours d'écriture ; lecture du prompt **102 à 216 tok/s**, très loin des ≈ 2 500 de T7 (1 884 tokens lus en ≈ 8 s) ; carte à 90 %, 139 W, 48 °C ; **RAM 29,7 / 31 Go** (barre rouge) ; 2 973 experts en VRAM (5,7 Go). « Disk read » à 239 Mo/s **avec 247 Mo/s d'écriture** au même moment : c'est le fichier d'échange de Windows (3,3 Go utilisés juste après), pas une preuve du mode mmap. Opera prenait **3,8 Go** (20 processus). **Réflexion** : le niveau par défaut du serveur, **high** (T10). Pi ne l'envoie pas (`"supportsReasoningEffort": false` dans `models.json`), donc son propre réglage de réflexion ne change rien (vérifié dans son code, `openai-completions.js` : `reasoning_effort` n'est envoyé que si `supportsReasoningEffort` est vrai). Pi affichait « medium », son défaut : `~/.pi/agent/settings.json` a maintenant `"modelThinkingLevels": { "strata/coder-iq1_m": "high" }`, pour que l'écran montre le vrai niveau. Garde ce niveau pour les trois tests et dis-le dans la vidéo. → **Ferme Opera** avant les tests, puis refais la mesure de R6 navigateur fermé. Pendant les tests, regarde la colonne **REUSED** : si elle reste à 0, Pi fait relire tout le prompt à chaque tour, et ces relectures lentes vont allonger les tests.

**Le plan de la vitesse (P10, à filmer, moniteur en grand)** : dans Pi, `Tell me a short story about a dragon who loves video games.` Garde 20 s lisibles du compteur pendant qu'il écrit. C'est le plan le plus propre pour afficher la vitesse.

---

## 6. Les trois démos (navigateur fermé)

**Protocole, pour chaque test**
1. `cd` dans le dossier du test, `pi`, modèle de `strata`. Lance l'enregistrement OBS.
2. Colle le prompt, Entrée. **Note l'heure** (secondes comprises).
3. Ne touche à rien. Le compteur de tok/s doit être lisible à l'écran. Toutes les 30 s environ, note la valeur (basse, typique, haute).
4. Note l'heure de fin (dernier fichier écrit). Garde 5 s d'image après.
   **Le chrono exact vient de Pi** : il note l'heure de chaque message. Après le test (pas pendant), dans une autre fenêtre : `node D:\Dev\strategie-technovore\projets\strata-test\chrono.mjs` → pour chaque dossier, l'heure de ta demande, celle de la dernière réponse, la durée, le nombre de requêtes, les tokens écrits et lus, et une ligne par relance. L'horloge de la barre des tâches reste la **preuve à l'image** ; `chrono.mjs` donne les chiffres de R3, R7 et R9. Sa ligne « fichiers » liste ce que le modèle a **vraiment** écrit avec les outils de Pi (⚠️ s'il n'a rien écrit, même s'il prétend l'avoir fait : c'est arrivé au mini-Minecraft) ; s'il y a des relances, une ligne TOTAL donne la durée à l'horloge et le temps de travail du modèle. Calibrage du 13/11 : **2 min 42 s**, 17 requêtes, 9 315 tokens écrits, ≈ 57,7 tok/s lecture comprise, et le cache marche (143 377 tokens repris : Pi ne fait pas tout relire).
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

### 6.2 Test 2 : le site d'agence de voyage (P13)

> **13/11, ta décision** : la page « Tikaya » (appli de paiement, icônes dessinées en SVG, aucune image) est remplacée par le site d'une agence de voyage **avec de vraies photos**, plus spectaculaire à l'écran. Le premier essai « Tikaya » reste dans `D:\strata-demo\test2` : **14 min 50 s** (20:06:46 → 20:21:36, `chrono.mjs`), 26 requêtes, 62 037 tokens écrits, ≈ 69,9 tok/s, `index.html` de 800 lignes. Tu peux t'en servir en plan de coupe ; le test filmé, c'est celui-ci.

**Prêt le 13/11** :
- le dossier **`D:\strata-demo\voyage`**, avec `images/` : 12 photos de Wikimedia Commons (« Featured pictures », 1 600 px de large, 8,9 Mo en tout) aux noms qui disent ce qu'elles montrent (`namibie-deadvlei-arbres-dunes-rouges.jpg`, `maroc-chefchaouen-ruelle-bleue.jpg`, `seychelles-la-digue-rochers-coucher-de-soleil.jpg`…) ;
- la réserve et les crédits dans `D:\strata-demo\_photos` (`credits.txt`). **Les 12 sont sous licence CC BY-SA** : recopie `credits.txt` dans la description de la vidéo (auteur, licence, lien), c'est la condition pour les montrer. J'ai écarté une photo de Zanzibar dont l'auteur demande d'être contacté avant tout usage commercial ;
- « **Sanaka Voyages** » : nom inventé, aucune agence trouvée sous ce nom le 13/11 (recherche web).

**Le modèle ne voit pas les images** (il ne lit que du texte) : le prompt lui dit de lister le dossier et de se fier aux noms des fichiers. Le voir taper `ls images` au début est un bon plan. Les textes du site sont demandés en français (le Coder est plus faible hors de l'anglais, T5 : c'est un risque, et un résultat à noter s'il se trompe).

```text
Create a stunning, premium website for a fictional travel agency called "Sanaka Voyages" that sells trips across Africa and the Indian Ocean. One file, index.html, all CSS and JavaScript inline, no libraries. All visible text in French. Use the real photos in the images/ folder: list it first. You cannot see them, but each file name says what it shows.
1. A full-screen hero with a photo slowly zooming in the background, a big headline, and a search bar (destination, date, travellers).
2. At least 6 destination cards with a photo, the place, the trip length and a price; the photo zooms when the mouse is over the card.
3. A full-width photo band with a parallax effect, then 3 traveller testimonials in a slider that moves on its own.
4. A photo gallery: clicking a photo opens it full screen with previous/next arrows, and Escape closes it.
5. A header that stays on top and becomes solid when I scroll, sections that fade in as they appear, and it must look right on a phone (375 px wide) and on a desktop, with no errors in the console.
Write the whole file in one go.
```

**Pour Claude** : copie `D:\strata-demo\_photos\*.jpg` dans `D:\strata-demo\claude-voyage\images` avant de coller le même prompt.

**Pour la voix** : Le site d'une agence de voyage qui n'existe pas, avec de vraies photos : un écran d'accueil qui zoome doucement, six destinations, des avis qui défilent tout seuls, une galerie qui s'ouvre en plein écran, et ça doit tenir sur un téléphone. Les photos, c'est moi qui les ai données ; tout le reste, c'est lui.

### 6.3 Test 3 : le mini-Minecraft (P14)

> **13/11, ta décision** : l'île en 3D est remplacée par un mini-Minecraft, plus spectaculaire. Une île qu'on regarde tourner ressemble à un économiseur d'écran ; marcher dans un monde que le modèle vient d'inventer, casser un bloc, en poser un, ton public le comprend en une seconde. L'ancien prompt de l'île est dans l'historique git.
>
> **Pourquoi pas ton prompt Minecraft complet** (monde infini, grottes, minerais, artisanat, monstres, lumière par bloc…) : (1) il pèse à lui seul ≈ 6 000 tokens (estimé), donc la première requête de Pi dépasserait 7 500 tokens, plus du double des 3 349 où les plantages de #5104 commencent (T23) ; (2) le fichier demandé ferait plusieurs milliers de lignes, bien au-delà de la limite de réponse de 32 000 tokens, réflexion comprise (T13) ; (3) avec plus de 60 exigences, le score sur 5 ne veut plus rien dire à l'écran. Celui-ci pèse **≈ 330 tokens** (≈ 1 850 avec Pi, comme le calibrage).

Avant d'appuyer sur Entrée, **écris ton pronostic** en une phrase (R8). Après coup, on est toujours trop malin.

```text
Create a small playable Minecraft-style voxel game in one file, index.html, using three.js r128 loaded with a classic script tag from exactly this URL: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js (no ES modules, no PointerLockControls, no other library, no image files).
1. A 64x64 world, 32 blocks high, from your own noise function: hills, a lake at sea level with sand around it, grass on top of dirt, stone below, and at least 10 trees.
2. Minecraft-style pixel textures drawn in code on 16x16 canvases (grass top and side, dirt, stone, sand, wood, leaves), with NearestFilter so they stay crisp. Semi-transparent blue water.
3. First-person controls: click to lock the mouse, mouse look, WASD, space to jump, gravity, and collision so I cannot walk through blocks.
4. A crosshair; left click breaks the block I look at, right click places the block chosen with keys 1 to 5, shown in a hotbar at the bottom of the screen.
5. One mesh per 16x16 chunk with only the visible faces, rebuilt when a block changes, so it stays smooth. Sky-blue background with fog.
It must run as soon as I open index.html, with no errors in the console. Write the whole file in one go.
```

L'adresse de three.js répond (vérifiée le 11/11, T17) ; la page a besoin d'internet à l'ouverture pour la charger, pas pendant la génération.

**À surveiller** : le jeu devrait faire 600 à 900 lignes (estimation, sans essai), 1,5 à 2 fois le casse-briques (493 lignes, 8 min 12 s). Avec « in one go », un fichier aussi long peut être coupé si la réflexion prend trop de place dans la limite (T13) : garde-le et filme-le, c'est un résultat (9.4 après coup, pas avant). La limite de 25 minutes devrait tenir.

**Pour la voix** : un mini-Minecraft dans un seul fichier, un monde en cubes généré, des textures en pixels dessinées par le code, je marche dedans, je saute, je casse et je pose des blocs.

---

## 7. Ouvrir les résultats, puis les relances

- [ ] Une fois les **trois** tests écrits : arrête Strata (décharge le modèle dans l'appli, ou ferme l'appli complètement, y compris près de l'horloge : ça arrête son moteur, T38). La RAM et la VRAM reviennent : **filme-le** dans le Gestionnaire des tâches (P41, plan de fin).
- [ ] Ouvre le navigateur, une fenêtre, et les trois `index.html` (double-clic). **Avant toute relance**, filme et note :
  - **P20** le jeu : 30 s de partie, un bonus qui tombe si possible, puis la console (F12) ;
  - **P21** le site : l'accueil qui zoome, défilement lent (cartes au survol, bande en parallaxe, avis qui défilent), une photo de la galerie ouverte en plein écran puis flèches et Échap, puis F12 → mode téléphone (375 px) ;
  - **P22** le mini-Minecraft : 30 s de jeu (clic dans la page, marche, saut, un tour sur toi-même pour montrer le monde, un bloc cassé, un bloc posé avec les touches 1 à 5, le lac), puis Échap et la console. Fluide ou ça rame, à l'œil.
  - **P24** l'île (`test4`, ajouté le 14/11) : la génération si tu l'as filmée, puis 20 s d'île (rotation à la souris, zoom à la molette, la rotation seule quand la souris ne bouge plus, la touche N et les étoiles), puis la console ;
  - **P21b** l'essai 1 du site (`voyage\index.html`, ajouté le 14/11) : 10 s de défilement **sans la barre d'adresse**, un titre anglais bien lisible ; **P21** devient Sillage (`voyage\sillage.html`) : l'accueil et son diaporama, une fiche de destination ouverte puis Échap, F12 en 375 px ;
  - Pour chacun : premier coup oui ou non, le score x / 5, ce qui casse (copie l'erreur de la console).
- [ ] **Relances (une par test au maximum, toutes ensemble)** : ferme le navigateur, recharge le Coder dans l'appli (mêmes réglages, 128K ; attends « Model ready » sur la page Serving), puis dans chaque dossier cassé, `pi --continue` (reprend la dernière session du dossier, T37) et :

```text
It does not work: <colle l'erreur de la console, ou décris ce qui ne marche pas en une phrase>. Fix it in index.html.
```

  Ensuite, stop, navigateur, nouveau verdict. **P23** : la relance et son résultat. Ne corrige jamais le code à la main.

---

## 8. Plan de fin (P41)

La version de l'appli et du moteur (dans ses réglages), `nvidia-smi`, puis l'arrêt du modèle dans l'appli et la RAM qui revient dans le Gestionnaire des tâches. 30 s. Si tu l'as déjà filmé en 7, garde juste les versions.

---

## 9. Plan B : quand ça casse

L'échec se filme (P16). Pour chaque cas, **un seul remède à la fois**, et tu notes ce qui a marché.

| # | Symptôme | Ce que tu fais |
|---|---|---|
| 9.1 | Le téléchargement n'avance pas | L'appli reprend un téléchargement coupé (T38). 58 Go à 100 Mbit/s ≈ 1 h 20, à 50 Mbit/s ≈ 2 h 40. Filme « ça télécharge » (P07) et avance l'étape 3. Pas de modèle ce soir : décale la vidéo. |
| 9.2 | Mode mmap (la case « Disk read » monte pendant qu'il écrit), ou le PC figé plus de 10 min | (1) Décharge le modèle, ferme tout (vérifie la RAM libre **avant** de recharger), recharge. (2) Contexte plus petit : recharge dans l'appli à **64K**, mets `"contextWindow": 65536` dans `models.json` (garde `"maxTokens": 32000`), quitte et relance Pi. (3) Si seul le mode lent démarre : **garde-le**, il marche, c'est lent ; un testeur sur 12 Go de VRAM et 32 Go de RAM y avait 41 à 46 tok/s sur du code (T4). La vidéo dit le prix. |
| 9.3 | `could not copy experts`, `exit code -6`, « running out of RAM » | Bug #5104 (T23). Copie le message exact (journal de l'appli). Remède : `STRATA_PREFILL_LAYER_MAJOR=0`. (1) Dans les Expert settings de l'appli s'il y est, puis recharge. (2) Sinon, installe le Terminal (sans droits d'administrateur, T2 ; il partage le dossier de l'appli et retrouve le Coder, T38), **ferme l'appli**, puis dans une nouvelle fenêtre : `irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 \| iex`, puis `strata launch --family coder --model IQ1_M --context 128k --vision off --parallel 1 --tune skip --access local --set STRATA_PREFILL_LAYER_MAJOR=0`. Le Terminal sert sur **une autre adresse** : lis-la à l'écran (par défaut `8080`, T2) et mets-la dans `"baseUrl"` de `models.json`. Note si le contournement a marché : c'est R14. |
| 9.4 | Fichier coupé, ou réflexion en boucle | (1) Vérifie `"maxTokens": 32000` dans `models.json`. (2) Repli **après** les générations, navigateur permis : ouvre `http://127.0.0.1:47831`, colle le prompt dans la page de chat de Strata s'il y en a une à cette adresse, copie le HTML dans `index.html`. Dis-le dans la vidéo : c'est un repli, pas un agent. |
| 9.5 | `non-finite logits` ou un seul mot répété en boucle | Rapporté sur 5080 avec d'autres fichiers (IQ3_S, IQ3_XXS), pas avec le Coder (T11). Ne ferme rien, filme le message, copie la ligne exacte (journal de l'appli). Recharge le modèle, puis essaie 64K (9.2). Si ça revient, c'est ton résultat. **Ne coupe pas la couche de prédiction (MTP)** si l'appli le propose : un fichier IQ natif refuse de démarrer sans (T11). |
| 9.6 | La vitesse s'effondre (moins de la moitié des repères de 9.7) | Regarde dans l'ordre : la RAM (Gestionnaire, Mémoire : Windows écrit-il sur le disque ?) ; un seul moteur tourne-t-il (pas le Terminal en plus de l'appli) ? ; le mode (case « Disk read ») ; la VRAM libre et la température dans le moniteur ; OBS (refais 30 s sans OBS). Note ta cause probable (R11). |
| 9.7 | Repères pour juger ta vitesse | 70 tok/s en chat court sur une 5070 Ti, même processeur, 31 Go, **réflexion coupée**, sans test de justesse (T7) ; 41 à 46 tok/s sur du code en mode lent sur 12 Go (T4). Pas des promesses. |
| 9.8 | La RAM manque quand OBS tourne | Ferme l'aperçu d'OBS, passe à 30 i/s. Sinon, filme l'écran du moniteur **au téléphone** pour le plan de la vitesse. |
| 9.9 | Le code est livré mais ne marche pas | C'est un verdict, pas un problème : une relance (section 7), puis F12, l'erreur à l'écran. |
| 9.10 | **Pi ne marche pas** (pas de Bash, appels d'outil refusés) | Passe à **OpenCode** : `npm i -g opencode-ai`, lance `opencode` une fois (son premier lancement télécharge un plug-in, T14). Sans le Terminal, sa config s'écrit aussi à la main dans `~/.config/opencode/opencode.json` : un fournisseur compatible OpenAI sur `http://127.0.0.1:47831/v1`, le modèle `coder-iq1_m`, une limite de sortie (`"output"`) de 32000. *Format non vérifié ici : demande-le-moi le moment venu.* Son prompt pèse ≈ 7 400 tokens : surveille #5104 (9.3). Relances : `opencode --continue` (non vérifié). Dis-le dans la vidéo, et change « Pi » dans le script. |
| 9.11 | Le Coder ne se charge pas dans l'appli | Installe le Terminal et sers depuis lui (commandes en 9.3, sans `--set …` s'il n'y a pas de #5104). Change `"baseUrl"` dans `models.json` pour l'adresse qu'il affiche. |

---

## 10. Les plans à filmer

**Indispensables (18)**
- [ ] **P04** Gestionnaire des tâches au repos (RAM 32 Go, carte 16 Go)
- [ ] **P05** la page Models de l'appli, la ligne du Coder et son libellé
- [ ] **P06** le moniteur de l'appli pendant une génération, la case « Disk read » lisible (près de 0 = resident) ; en plus, la ligne `resident` ou `mmap` du journal si tu la trouves
- [ ] **P07** le téléchargement dans l'appli (accéléré), « Preparing your model », la RAM qui monte
- [ ] **P09** le branchement de Pi, en 5 plans immobiles (4.3) : la page Serving, `models.json` et ses trois lignes, `pi --list-models strata`, `/model`, l'écran partagé
- [ ] **P10** le plan de la vitesse (le dragon), compteur en grand
- [ ] **P12, P13, P14** les trois générations : Pi à gauche, le moniteur de l'appli à droite, horloge
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

> **14/11 (après-midi) : tous les trous sont remplis** dans le script, le téléprompteur et le storyboard, à partir des sessions de Pi, des captures du moniteur et des vidéos de `D:\_Technovore\Youtube\Strata test` (`sources.md`, T41 et T45). R8 (ton pronostic) est coupé : il n'a pas été écrit avant le test. R12 et R13 disparaissent avec la nouvelle section 5 (une seule comparaison, le site de Claude). R15 est une proposition à valider. Le tableau ci-dessous garde les notes du tournage.

| Trou | Ce qu'il faut | Où le lire | Ta valeur |
|---|---|---|---|
| **R1** | tok/s de **l'histoire du dragon** (14/11 : c'est ta mesure de vitesse, dite dans le hook et en section 4) | moniteur, ton enregistrement du 13/11 | 13/11 19:45:59 (`calibrage`, `chrono.mjs`) : 590 tokens écrits en 13,7 s (≈ 43 tok/s **lecture comprise**, 1 849 tokens lus), 161 caractères de réflexion. Le chiffre à dire est celui du moniteur sur ton enregistrement. |
| **R2** | combien des quatre ont marché du premier coup (0 à 4) | section 7, avant les relances | En une seule demande : l'île et le casse-briques ; pas le mini-Minecraft (3 relances), ni le site (essai 1 en anglais, Sillage avec un plan). Reste : ce que donnent l'île et le casse-briques à l'écran. |
| **R3** | le casse-briques (montré en dernier depuis le 14/11) en une phrase : durée, premier coup ou pas, score sur 5, ce qui casse | horloge, P20, console |13/11 (`chrono.mjs`) : **8 min 12 s** (19:33:15 → 19:41:27), 26 requêtes, 30 296 tokens écrits, `index.html` de 493 lignes fini à 19:38 ; les 3 dernières minutes, le modèle **a testé son propre jeu** avec un script (« zero exceptions », bonus, fin de partie et redémarrage vérifiés, d'après son résumé). Reste : premier coup, score sur 5, ce qui casse (P20). |
| **R4** | premier chargement : durée, et si le PC s'est figé (combien de temps) | chronomètre, P07 | |
| **R5** | RAM libre au plus bas pendant une génération | Gestionnaire ou moniteur, P15 | |
| **R6** | `resident` ou `mmap`, et la lecture disque pendant une génération | case « Disk read » du moniteur, journal de l'appli, P06 | |
| **R7** | le site en une phrase : durée, premier coup ou pas, score sur 5, ce qui casse | horloge, P21 | Deux essais dans `voyage`, **à ne pas mélanger** (`chrono.mjs voyage`). **Essai 1, le prompt de la section 6.2** (`index.html`, « Sanaka Voyages », 13/11) : demande 21:12:04, page écrite et corrigée jusqu'à 21:43:37 (**31 min 33 s**), 53 requêtes, 140 468 tokens écrits (≈ 71,6 tok/s lecture comprise), 1 282 lignes. En route : trois réécritures complètes, dont une coupée net par la limite de 32 000 tokens de sortie (7 min perdues), puis le fichier monté par morceaux avec `cat >>` ; contexte plein, compacté par Pi à 21:42. **Tout le texte visible est en anglais** (« The latitudes we cross ») alors que le prompt exige le français. Les fonctions demandées sont dans le code (parallaxe, avis qui défilent, galerie plein écran), pas vérifiées à l'écran. À 21:46:19, son propre test dans Chrome ne rend jamais la main : **bloqué 1 h 50 min 51 s** jusqu'à ton arrêt à 23:37:10 ; la relance « is it finish ? » se bloque pareil (arrêtée à 23:38:43). Jamais terminé proprement. **Essai 2, avec un plan de Claude** (`sillage.html`, « Sillage », 14/11) : **pas le même test**. Claude Code (session de `D:\Dev\demo-claude-strata`, 13/11 23:49 → 14/11 00:44) a écrit `AGENTS.md` (51 Ko, des blocs de code à recopier tels quels), `i18n.js` (les 228 textes français) et `qa-sillage.js` (contrôle après chaque étape). Qwen a suivi le plan : demande 10:34:43, page écrite en 8 étapes jusqu'à 10:51:40 (**16 min 57 s**) ; puis deux blocages sur Chrome (20 min 14 s et 10 min 57 s) ; la relance 2 « dont test with chrome » livre le fichier final à 11:29:24. **Total 54 min 41 s à l'horloge, dont 20 min 59 s de travail du modèle et 31 min 11 s bloqué**, 78 110 tokens, 2 relances ; 1 354 lignes, 85,8 Ko, 0 erreur au contrôle final. Le plan a changé la page : **ni bande en parallaxe, ni galerie plein écran, avis en grille fixe** ; à la place, un diaporama dans l'accueil et une fiche qui s'ouvre par destination. Si tu montres Sillage, la phrase de la voix (« tout le reste, c'est lui ») devient fausse : les textes et le plan viennent de Claude. Reste : ouvrir les deux (P21), score sur 5. Pour mémoire, « Tikaya » (`test2`) : 14 min 50 s, 26 requêtes, 62 037 tokens écrits, 800 lignes, aucune relance. |
| **R8** | **à écrire, AVANT le test 3** : ton pronostic sur le mini-Minecraft | ta tête | Si tu ne l'as pas écrit avant le test du 13/11, laisse vide : le script coupe alors la phrase et la carte V19c. |
| **R9** | le mini-Minecraft en une phrase : durée, premier coup ou pas, score sur 5, fluide ou pas | horloge, P22 | 13/11 (`test3`, `chrono.mjs`) : **raté du premier coup, aucun fichier écrit**. Demande 20:30:31 → 20:36:50 (6 min 19 s) : une seule requête, ≈ 75 000 caractères de réflexion, puis « `index.html` written and verified (184 balanced lines) » **alors qu'aucun outil n'a été appelé** et que le bloc de code finit sur un vide (`"useraw"`) : il **dit** avoir écrit le fichier, il ne l'a pas fait. Relance 1 « continue » (6 min 34 s) : il télécharge three.js r128 et fouille son code pour vérifier l'API, annonce « Writing the file: »… et s'arrête, toujours aucun fichier. Relance 2 « contie » (7 min 23 s) : il écrit enfin `index.html` (665 lignes), le teste avec un faux three.js en Node : « All checks pass ». Relance 3 « continue » (3 min 00 s) : à la relecture, il trouve **un vrai bug que ses propres tests n'avaient pas vu** (`pos.concat(...)` jeté, les chunks auraient été vides à l'écran), le corrige, revérifie, efface ses fichiers de test : 666 lignes. **Total : 34 min 58 s à l'horloge (20:30:31 → 21:05:28), dont 23 min 08 s de travail du modèle, 86 123 tokens écrits, 3 relances** : au-delà de la limite de 25 min et de la règle « une relance par test » (à dire tel quel). Reste : l'ouvrir (P22), score sur 5, fluide ou pas. |
| **R9b** | l'île, **la première démo depuis le 14/11** (section 1 du script) : ce qu'elle donne à l'écran, score sur 5, fluide ou pas | horloge, P24 | 13/11 (`test4`, `chrono.mjs`) : **15 min 32 s** (23:42:35 → 23:58:07), une seule demande, **aucune relance**, 51 requêtes, 55 489 tokens écrits (≈ 60,0 tok/s lecture comprise), réflexion ≈ 114 000 caractères. `index.html` de 472 lignes écrit **dès le début** (cette fois il appelle l'outil), puis vérifié contre le vrai three.js r128 téléchargé (7 erreurs d'outils en route, rattrapées seul) ; il dit avoir trouvé et corrigé une inversion jour/nuit. D'après son résumé : 5 824 cubes dans un seul InstancedMesh, 33 arbres, orbite et zoom écrits à la main, ombres, N pour la nuit avec des étoiles. Fichiers de test effacés. Reste : l'ouvrir, premier coup ou pas, score sur 5, fluide ou pas. Contraste à montrer : **même modèle, même soir, l'île passe en une fois, le mini-Minecraft a demandé 3 relances.** |
| **R10** | tok/s typiques pendant les vrais tests (14/11 : dit juste après le dragon, « avec tout le code à relire ») | moniteur, P12-P14, P24 | `chrono.mjs` (lecture comprise, pas le chiffre du moniteur) : Tikaya ≈ 69,9 ; site de voyage ≈ 71,6 (essai 1), Sillage 63,6 / 49,3 / 50,9 selon la manche ; mini-Minecraft 65,4 / 60,2 / 64,3 / 53,2 selon la manche ; île ≈ 60,0. Le chiffre du moniteur pendant l'écriture reste à relever sur P13 et P14. |
| **R11** | ta vitesse face au repère de 70 (réflexion coupée chez lui) : plus ou moins, de combien, et ta cause probable si c'est moins (9.6) | R1 contre 70 | |
| **R12** | Claude, une phrase par test : durée et score sur 5 | section 3 | Site de voyage, 13/11 : `latitude-sud.html` (rangé dans `voyage`, pas dans `claude-voyage`), **avec un autre prompt** que celui de la section 6.2 (« avec ces images … fait un beau site de voyage un seul fichier html design moderne », en français, sans liste de fonctions) : fichier écrit 2 min 23 s après la demande (23:41:41 → 23:44:04), 528 lignes, textes en français. Pas comparable tel quel à l'essai 1 de Qwen : pour R13, refais-le avec le prompt de la section 6.2 dans `claude-voyage`, ou dis à l'écran que les prompts diffèrent. Reste : score sur 5, et les deux autres tests. |
| **R13** | **à écrire** : la comparaison en une phrase, et ce qui sépare les deux à tes yeux | P20-P22 contre P30-P32 | |
| **R14** | ce qui a cassé chez toi (message exact, version de Strata), ou « rien n'a planté » | journal de l'appli, sa version | 14/11, d'après les sessions de Pi : **aucune erreur du moteur**. Les arrêts sont tes Échap sur les blocages de Chrome (2 h 22 min en tout) et une réponse coupée à 32 000 tokens. Regarde le journal de l'appli avant de dire « rien n'a planté ». |
| **R15** | **à écrire** : est-ce que ça remplace ton abonnement, et ce qui t'a le plus surpris | toi | **Ton verdict du 14/11, écrit dans le script (section 7)** : pas complètement ; un abonnement à 20 $ suffit, Claude écrit le plan et le modèle local l'exécute ; même sans plan il s'en sort bien, le gros du temps perdu vient de Chrome ; la limite de 32 000 n'a pas suffi une fois. Reste à écrire : ce qui t'a le plus surpris. |

**À noter aussi (pas des trous)** : versions de l'appli Strata, du moteur, de Pi (1.5.2), pilote, contexte (128K) ; la vitesse de lecture (« Prefill ») d'une vraie requête de Pi ; si tu as dû mettre `STRATA_PREFILL_LAYER_MAJOR=0` ; résultat du calibrage ; modèle et effort de Claude (`/model`) ; si tu as dû passer à OpenCode ; écart de tok/s avec et sans OBS si tu l'as mesuré.
