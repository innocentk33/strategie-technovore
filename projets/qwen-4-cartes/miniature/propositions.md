# Miniatures du 12 nov. 2026 : *Qwen 4 arrive : quelle carte graphique acheter (ou pas) ?*

> **11/11/2026.** Deux miniatures pour un test A/B, dans le **style OpenCode piraté** (règle du 11/11, `.claude/rules/miniatures.md`). Le titre est celui que recommande le grill et que tu n'as pas encore validé ; la miniature marche aussi avec celui du calendrier (*… les cartes graphiques qui le feront tourner*).
> - **Rendus 4K (3840×2160)** : [`rendus/a.png`](rendus/a.png) (4,9 Mo) et [`rendus/b.png`](rendus/b.png) (2,2 Mo). Les deux dépassent 2 Mo : importe-les depuis l'ordinateur.
> - **PSD PhotoCraft** : [`photocraft/a.psd`](photocraft/a.psd), [`photocraft/b.psd`](photocraft/b.psd) (le décor, plus 2 calques de texte modifiables).
> - **Maquette** : [`propositions/miniature.html`](propositions/miniature.html) (`?v=a|b`), rendue par [`rendre.sh`](rendre.sh) (`./rendre.sh` ou `./rendre.sh a`). PSD : `python3 -I ressources/miniatures/psd.py --page projets/qwen-4-cartes/miniature/propositions/miniature.html projets/qwen-4-cartes/miniature/photocraft a b`.
> - **Tests** : [`apercu/`](apercu/) (planches du coach, comparaison, accueil clair et sombre parmi 6 concurrents, `test-50-a.png`, `test-50-b.png`, `168-a.png`, `168-b.png`).
> - **Références** : [`refs/`](refs/), 15 miniatures.
> - **Recommandée : a** (Harold). La raison est à la fin.

## Le concept

| | a | b |
|---|---|---|
| En haut à gauche, petit | logo Qwen + une vraie RTX 5090 (ASUS TUF) | idem |
| Ligne 1, blanc | **RTX 5090** | idem |
| Ligne 2, rouge `#ff3b30` | **7 900 €** | idem |
| À droite, détouré, sort du cadre | **Harold** (*Hide the Pain Harold*), le sourire crispé | **Jackie Chan** (le dessin « WTF »), mains sur la tête |
| Fond | noir texturé : un faux journal de llama.cpp, très sombre (sans chiffre de vitesse ni nom de carte), et un halo rouge derrière le meme | idem |

**Seul le meme change** : le test dit quelle émotion fait cliquer, la douleur de payer (a) ou l'incompréhension (b).

- **La question posée sans le titre** : « 7 900 € pour une carte graphique ? Il faut vraiment ça pour Qwen ? » Le titre répond : laquelle acheter, ou pas.
- **L'émotion** : le choc du prix. Le spectateur voit le montant et la grimace de quelqu'un qui va payer.
- **Texte exact** : `RTX 5090` / `7 900 €` (espace fine insécable entre 7 et 900, espace insécable avant €). Police : Archivo Black, en capitales.

## Le brief (skill `/youtube thumbnail`)

- **Le titre dit** : Qwen 4 arrive, quelle carte acheter, et peut-être aucune.
- **La miniature ajoute** : le modèle de carte et son prix. Aucun mot du titre n'est répété : « Qwen » est porté par le logo, « carte graphique » par la photo.
- **Les faits** (tous dans la vidéo, dès 0:00) :
  - « RTX 5090 » à « 7 900 € » : la première image du script V2 (0:00-0:04) est la fiche Amazon.fr de l'**ASUS TUF OC** à 7 900 €, la moins chère en stock le 11/11 (Q21, gpuprix.com ; des fiches à partir de 4 583 € sont en rupture). La carte de la miniature est **cette ASUS TUF**, pas une Founders Edition.
  - **Rien ne dit que Qwen 4 tourne en local** : ni « Qwen 4 », ni chiffre de tok/s, ni « 27B ». Le logo est celui de Qwen (la marque), sans le chiffre 4. Le prix est celui de la carte, pas de Qwen.
  - Écartés : « QWEN 4 / 7 900 € » (on croirait que Qwen 4 coûte 7 900 €, ou qu'il tourne sur cette carte) ; « +20 % » (vrai seulement pour la 5060 Ti et la 5080, Q20 : il aurait fallu changer de carte, donc deux changements dans le test) ; « J'ACHÈTE OU J'ATTENDS ? » (répète le titre).
- **Différenciation** (vérifiée le 11/11 sur la recherche YouTube, `refs/`) :
  - **Plain Spoken Tech** (FR, *Qwen 4 arrive : quel GPU bon marché choisir ?*, presque notre titre) : grille sombre, texte à gauche « BUY BEFORE QWEN 4? », une carte et **une flèche rouge qui monte**. Chez nous : pas de flèche, pas d'anglais, un visage.
  - **Weights & Wonders** (*11 GPUs You Should Get…*) : une carte dessinée en personnage paniqué, des mains de cartoon, le mot-symbole « Qwen 4 » en haut à droite. Chez nous : ni carte-personnage, ni mot-symbole « Qwen 4 ».
  - **Reboot** (« +40 % ») et **Manuizine** (« TROP TARD ») : des flèches qui montent ; **DiscoverID** : une étiquette de prix « +300 $ » accrochée à la carte, avec son visage. Chez nous : le prix est en texte, sans étiquette sur la carte.
  - **Kai, Locally, KernelBrief** : des cartes et des logos Qwen, sans visage.
  - **Parmi les 15 références, aucune ne met un meme à côté d'un prix.**
- **Le style OpenCode** : on garde sa structure (le logo petit au-dessus, 2 lignes blanc puis rouge, le visage détouré à droite), mais pas Michael Scott, pour que les deux miniatures ne soient pas interchangeables.

## Les références (`refs/`, téléchargées le 11/11 depuis `i.ytimg.com`, sauf OpenCode, copiée depuis `projets/claude-ou-mon-pc-1/miniature/refs/`)

| Fichier | Chaîne, vidéo | Pourquoi |
|---|---|---|
| `nous-opencode-LeZ9hgwvXy0.jpg` | Technovore, *OpenCode a été gravement piraté* | le modèle (4,2 % de CTR) |
| `nous-16go-jMZFDNbwRNI.jpg` | Technovore, *16 Go de VRAM suffisent* | le contre-exemple (1,5 % à J+2) |
| `ww-11gpus-kQKCp7PlVxY.jpg` | Weights & Wonders, *11 GPUs You Should Get for Local AI Before Qwen 4's Release!* | l'inspiration de la fiche, à ne pas copier |
| `fr-plainspoken-qwen4-WhzokIS84Cw.jpg` | Plain Spoken Tech, *Qwen 4 arrive : quel GPU bon marché choisir ?* | le concurrent français le plus proche |
| `fr-mg-qwen4-XA7eTCP-CLg.jpg` | MG, *Qwen 4 gratuit vs Claude Opus 5.5 ?* | Qwen 4 en français ; le logo Qwen bleu |
| `kai-qwen4-27b-TPo53fFYwYY.jpg` | Kai, *Qwen 4 27b: What to Expect…* | concurrent direct |
| `locally-qwen4-pmkA8bWJDdI.jpg` | Locally, *Can Your Local AI Machine Run Qwen 4.0?* | concurrent direct |
| `kernelbrief-qwen4-h9NcapUz6sk.jpg` | KernelBrief, *Qwen 4 27B: can your local AI machine run it?* | concurrent direct |
| `amplify-qwen4max-Ie-k0mGntDA.jpg` | Amplify Imagination, *It's Here: Qwen 4 Max Preview (No 27B Yet)* | la préversion cloud |
| `fr-makertronic-hardware-ddoE9U1tT8s.jpg` | MAKERTRONIC TECH, *IA Locale en 2026 : le Hardware à acheter* | le matériel IA en français |
| `fr-guillaume-prix-GCAayy4azRc.jpg` | GUILLAUME, *Le prix des CARTES GRAPHIQUES va EXPLOSER !* | hausse des prix, visage choqué |
| `fr-reboot-prix-_b1TvWOXlsY.jpg` | Reboot, *Le PRIX des CARTES GRAPHIQUES EXPLOSE : Que Faire ?* | le cliché « +40 % » et la flèche |
| `fr-discoverid-5090-Tz3_nenS4Dc.jpg` | DiscoverID, *Le Prix de la RTX 5090 va EXPLOSER* | prix de la 5090, étiquette sur la carte |
| `manuizine-toolate-IAFmgW6Xm0s.jpg` | Manuizine, *TOO LATE! GPUs are even more expensive* | le cliché « trop tard » |
| `horsniche-graham-wtf-LCbVikmmBls.jpg` | Graham Stephan (finance, hors niche), *WTF Is Happening To The Housing Market?!* | un visage inquiet, une étiquette de prix, le mot-choc : le prix fait peur |

## Les images (`sources/`)

- **La carte** : `tuf-rtx5090-asus-1.png`, ASUS TUF Gaming GeForce RTX 5090, vue de trois quarts. Image de presse d'ASUS, PNG transparent de 2400 px, prise sur `press.asus.com` (album RTX 50). Recadrée dans `tuf-rtx5090-recadree.png`. L'autre vue (de face) est `tuf-rtx5090-asus.png`.
- **Le logo Qwen** : `qwen-color.svg`, LobeHub Icons, `@lobehub/icons-static-svg@1.102.0`. Il est en bleu `#082dff` : le paquet est passé du dégradé violet (`#6336E7` → `#6F69F7`, jusqu'à la 1.90 de mai) au bleu entre mai et octobre, et le logo bleu est aussi celui de MG et, d'après une recherche, celui du compte Hugging Face de Qwen. Posé sur une tuile blanche, comme une icône d'appli, parce que le bleu foncé se perd sur le noir.
- **Harold** : `harold-original-kym.jpg` (1410×793, image principale de l'article Know Your Meme). C'est une **photo de banque d'images** d'András Arató (pas le patron de Klubrádió qui porte le même nom sur Wikimedia). Détourée avec Vision de macOS (`detoure.swift`, `swift detoure.swift entree sortie.png`) → `harold-detoure.png`, bord propre. Retournée en miroir pour regarder vers le texte ; le téléphone sort du cadre à droite.
- **Jackie Chan** : `jackie-chan-wtf-original-kym.jpg` (1500×843, le dessin « My Brain Is Full of F… » de Know Your Meme, un dessin au trait d'après une photo de l'acteur). Détouré par remplissage depuis les coins, les trous du trait étant d'abord bouchés (Pillow) → `jackie-chan-wtf-detoure.png`. La manche gauche, restée ouverte, est fondue au noir.

## La critique du coach (`/coach-miniature-youtube`, mode A, comparaison)

### Le test de la seconde
- **a** : « Une RTX 5090 à 7 900 €, et un vieux monsieur qui sourit en serrant les dents. » Ça coûte cher, et ça fait mal.
- **b** : « Une RTX 5090 à 7 900 €, et Jackie Chan qui ne comprend pas. »
- Les deux disent ce que promet la vidéo (un achat de carte, un prix qui choque) sans dire que Qwen 4 est sorti.

### Tableau de bord (après corrections)

| Axe | a | b | En une phrase |
|---|---|---|---|
| Lisibilité | 🟢 | 🟢 | 3 éléments : petit objet, 2 lignes, un visage ; « RTX 5090 » et « 7 900 € » se lisent à 168 px |
| Composition | 🟢 | 🟢 | texte sur le tiers gauche, visage sur les deux tiers droits ; rien d'important sous la durée (a : la chemise, b : le col) |
| Contraste, couleurs | 🟠 | 🟠 | a : peau chaude contre noir et rouge ; b : blanc pur, plus contrasté ; mais 52 % (a) et 61 % (b) du pourtour quasi noir, comme OpenCode |
| Texte | 🟢 | 🟢 | 3 mots, aucun du titre ; en niveaux de gris, le rouge reste nettement plus clair que le fond |
| Émotion, curiosité | 🟢 | 🟠 | a : la douleur de payer, exactement le sujet ; b : l'incompréhension, plus vague |
| Types | 🟢 | 🟢 | chiffre choc + visage réaction + objet, comme OpenCode |
| Duo titre-miniature | 🟢 | 🟢 | le titre pose la question d'achat, la miniature donne le prix qui la rend urgente |
| Différenciation | 🟢 | 🟢 | aucun meme à côté d'un prix parmi les 15 références, ni flèche, ni étiquette |
| Identité | 🟢 | 🟢 | reconnaissable comme la suite d'OpenCode sans le recopier |
| Promesse, technique | 🟠 | 🟠 | prix tenu à 0:00 mais à revérifier le 12/11 ; 4K, PNG au-dessus de 2 Mo |

### Les corrections faites
1. **Les memes débordaient du cadre** (premier rendu : on ne voyait que le téléphone d'Harold et la moitié de Jackie). Ils étaient dimensionnés à la hauteur : passés en largeur fixe, Harold retourné et collé en haut (sa tête est déjà coupée dans l'original), Jackie recentré.
2. **Le journal en fond gênait la lecture** du texte (trop clair près des lignes) : opacité ramenée à 4-12 % et dégradé plus fort vers la droite.
3. **Le fond se fondait dans le mode sombre** (alerte du script : plus de la moitié du pourtour quasi noir) : halo rouge agrandi derrière le meme (1100 px, plus intense) et fond relevé de `#050506` à `#0a0a0c`. L'alerte baisse un peu (56 → 52 % pour a) ; on la garde, comme OpenCode, qui avait le même noir.
4. **Le test des 50 % de b** : le visage de Jackie était presque entièrement dans la moitié basse. Agrandi (1280 px) et remonté en haut du cadre : ses yeux passent dans la moitié haute.
5. **Des coupes verticales dures** : à gauche de Jackie (le reste de la manche) et à gauche d'Harold (le bord de la photo d'origine, une fois retournée, coupait sa chemise en ligne droite vers x = 560). Les deux sont remplacées par un fondu ; le bout de téléphone flou au bord droit d'Harold est fondu aussi.
6. **Le journal du fond affirmait des choses fausses** : une ligne « NVIDIA GeForce RTX 5090 » et une ligne « 28.48 tokens per second », lisibles en grand. Or 28 tok/s, c'est la 5060 Ti dans le script, et la 5090 fait jusqu'à 75. Les deux lignes sont remplacées par du bruit neutre (taille de contexte, nombre de tenseurs). Il reste « model size = 16.56 GiB », qui est le vrai poids du Q4_K_M de Qwen3.8-27B (Q9).

### Le test des 50 % (`apercu/test-50-a.png`, `test-50-b.png`)
- **Le texte passe** : le logo, la carte, « RTX 5090 » et « 7 900 € » finissent au-dessus de y = 360 (bas du « 7 900 € » vers y = 355).
- **Le visage passe à moitié** :
  - a : les yeux plissés et le front sont en haut, le sourire crispé en bas ;
  - b : les mains, les sourcils froncés et les yeux sont en haut.
- Sur la télé (2,2 % des vues), on lit le prix et un regard inquiet. Pour remonter le sourire d'Harold, il faudrait l'agrandir au-delà de la moitié droite, et l'original s'arrête à la poitrine : on garde.

### Lisibilité à 168 px (`apercu/168-a.png`, `168-b.png`, `comparaison.png`)
- « RTX 5090 » et « 7 900 € » se lisent tous les deux ; la grimace d'Harold aussi.
- Le logo et la carte deviennent une petite tache : c'est voulu (le contexte, comme le logo d'OpenCode).
- À cette taille, Jackie devient une masse blanche où l'on devine le geste, moins le visage.

### Limites (vérifiées à 100 % sur le rendu 4K)
- Les memes sont agrandis environ 2,6 fois en 4K (Harold vient d'une image de 1410 px, Jackie de 1500 px) : les cheveux d'Harold et le trait de Jackie sont doux à 100 %, sans liseré ni escalier visible ; invisible à la taille d'une miniature.
- Jackie garde un fin liseré blanc le long du trait extérieur (le blanc du dessin d'origine) : il passe pour un contour.
- Le téléphone d'Harold, fondu au bord droit, laisse une bande beige floue de 30 px : seulement visible en grand.

## La recommandation : a (Harold)

- C'est l'émotion juste : **la douleur de payer**, cachée derrière un sourire, pour un prix de 7 900 €. Jackie dit « je ne comprends pas », ce qui colle moins à un prix.
- C'est le plus proche de ce qui a marché : **un vrai visage qui grimace**, comme Michael Scott sur OpenCode (4,2 %), sans être le même.
- Il se lit mieux en petit : peau chaude sur fond noir et rouge, grimace visible à 168 px.
- b reste un bon challenger : plus de contraste (blanc pur), et un meme très diffusé (non mesuré auprès de notre public). Si b gagne, ce sera un signal pour les memes dessinés.

**Le test** : a par défaut, b en challenger dans « Tester et comparer ». Seul le meme change ; texte, objet, fond et cadrage sont identiques.

## À vérifier avant de publier

- **Le prix** : « 7 900 € » est marqué `[À REVÉRIFIER]` dans le script. Si la fiche Amazon.fr de l'ASUS TUF OC a changé le 12/11, change le texte (`.t2` dans le HTML, ou le calque dans le PSD) et la capture de 0:00 **ensemble**. Si une 5090 en stock est nettement moins chère ailleurs, quelqu'un le dira en commentaire : la vidéo doit dire « la moins chère en stock chez Amazon.fr, ce jour-là ».
- **La carte montrée** est l'ASUS TUF, celle de la fiche à 7 900 € : garde ce modèle à l'écran à 0:00.
- **Droits du meme** :
  - Harold : photo de banque d'images (vendue sous licence, d'après Know Your Meme), utilisée partout comme meme ; la photo reste à son photographe et à la banque d'images (non vérifié : la position d'András Arató sur le meme). Risque faible, à connaître.
  - Jackie Chan : dessin anonyme d'après une photo de l'acteur ; même statut que les autres memes.
- **Le logo Qwen** : en bleu (`#082dff`, LobeHub 1.102.0). Si tu vois encore le dégradé violet sur qwen.ai, dis-le et je change.
- **La fiche** (`fiche.md`, section « Miniature ») parle encore de la charte verte et de « 24 GO ? » : elle date d'avant le 11/11. Je n'y ai pas touché.
- **Le titre** n'est pas encore validé : la miniature ne répète ni « Qwen 4 », ni « carte graphique », ni « acheter », donc elle marche avec les deux titres.
