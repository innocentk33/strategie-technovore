# Miniatures du 9 nov. 2026 : *16 Go de VRAM suffisent (si tu prends le bon fichier)*

> **05/11/2026.** Trois miniatures pour « Tester et comparer » (règle du 24/10, `CLAUDE.md`), dans le style décidé le 03/11 d'après OpenCode (4,2 % de CTR, le meilleur de la chaîne) : un objet fort et net, un fond très contrasté, un gros texte court.
> - **Rendus 4K (3840×2160)** : [`rendus/a.png`](rendus/a.png), [`rendus/b.png`](rendus/b.png), [`rendus/c.png`](rendus/c.png), la 4e proposition [`rendus/d.png`](rendus/d.png) et la 5e [`rendus/e.png`](rendus/e.png). Plus de 2 Mo : importe-les depuis l'ordinateur.
> - **PSD PhotoCraft** : [`photocraft/a.psd`](photocraft/a.psd), `b.psd`, `c.psd` (décor + calques de texte), `d.psd` (décor seul), `e.psd` (décor + calque de texte).
> - **Maquette** : [`propositions/miniature.html`](propositions/miniature.html) (`?v=a|b|c|d|e`).
> - **Tests** : [`apercu/`](apercu/) (planches du coach, comparaison, accueil clair et sombre parmi 6 concurrents, [`test-50.png`](apercu/test-50.png)).
> - **Références** : [`refs/`](refs/), 15 miniatures.
> - **Série « IA chez moi »** : la charte par défaut est **b** (vert), et la vidéo commence sur sa scène.
> - **L'ancien gabarit `vert-02`** (Claude à côté de la carte, bandeau de série) est abandonné pour cette vidéo : le script s'ouvre sur ta carte seule, sans Claude.

## La carte : la 5080 Founders Edition que tu as fournie (05/11)

- **L'image** : [`sources/rtx5080-fe-auteur.webp`](sources/rtx5080-fe-auteur.webp), une RTX 5080 Founders Edition de face. C'est une **image produit de NVIDIA**, que tu as fournie le 05/11 et préférée à ta carte (plus reconnaissable). Elle remplace la photo de Geekerwan dans a, b, c, d (et sert à e).
  - Elle arrive déjà détourée (canal alpha propre, équerre et connecteur PCIe compris, sans liseré blanc). `photocraft/detoure.py` la recadre seulement → `photocraft/rtx5080-detoure.png` (1463 × 699 px).
  - Sa gravure dit bien « RTX 5080 » : plus besoin de retouche.
  - **Plus de crédit Geekerwan** : sa photo n'est plus utilisée (l'original reste dans `sources/` pour mémoire). L'image NVIDIA n'est pas sous licence libre : c'est une image de presse, en général permise pour parler du produit, mais vérifie ses conditions et écris « Image de la carte : NVIDIA » dans la description.
  - **Limite** : 1463 px de large, agrandie ×1,85 dans a et b en 4K. Douce à 100 %, invisible à la taille d'une miniature.
- **Recalage** : l'image inclut l'équerre (format 2,09 au lieu de 2,28), donc la pastille « 16 Go » de a et b est recentrée sur le X (`left:345px;top:423px`), et les deux cartes de c sont réduites (600 → 570 px) pour ne pas se toucher.
- ⚠️ **Piège à régler avant de publier** : le script dit « **Cette carte, c'est la mienne** », alors que **ta carte est une Inno3D** (`sources/rtx5080-inno3d-auteur.webp`), pas une Founders Edition. Deux sorties :
  - **montrer l'Inno3D en vidéo** (le premier plan) et garder la FE en miniature : la miniature montre « une 5080 », la vidéo « ta 5080 » ;
  - **ou adapter la phrase** sur le plan de la FE, par exemple « Une 5080, comme la mienne ».

## Le brief (skill `/youtube thumbnail`)

- **Le titre dit** : 16 Go suffisent, à condition de prendre le bon fichier.
- **La miniature ajoute** : l'écart et la question. Sur la même carte, avec la même IA, on a publié 101 tokens par seconde, et ailleurs 13. Pourquoi ?
  - Le spectateur se demande d'où vient l'écart, et le titre lui souffle la réponse (« le bon fichier »).
  - Elle ne répète aucun mot du titre, sauf le petit « 16 Go » sur la carte, qui vient de la scène du script (0:00).
- **Émotion** : l'incrédulité, avec un écart de 1 à 8 sur le même matériel.
- **Faits** :
  - 101,3 tok/s : RTX 5080, Qwen3.8-27B en Q3_K_M (S18) ;
  - 13 tok/s : RTX 5080, Qwen 3.8 27B dans LM Studio, en Q4 d'après les chapitres (S21) ;
  - ce sont **deux mesures publiées par d'autres** ; aucune ne vient de toi. « Même carte, même IA » est exact : deux 5080, le même modèle de 27 B. Les réglages diffèrent aussi, et la vidéo le dit (« je fais pas de soustraction »).
  - La miniature n'écrit **ni « ×8 », ni « j'ai testé », ni « ma 5080 : 101 »**.
- **Différenciation** (vérifiée le 05/11 sur la recherche YouTube, `refs/`) :
  - Code Bear met une carte dans une poubelle avec « 16 GB is enough for local AI? » ;
  - Tech Business Club (*Why Your Qwen 3.8 27B Model is Slow?*) montre un visage, une jauge et un escalier de tok/s de 10 à 63 ;
  - Kai, RepoChad, Codacus et Hardware IA sont sur fond noir, avec des cartes plates ou des logos Qwen.
  - **Aucun ne met deux chiffres face à face sur la même carte.** Pas de jauge chez nous (c'est celle de Tech Business Club), pas de logo Qwen.

## a · noir premium (charte `noir.html`)

- **Scène** : ta carte en gros plan, à gauche (de 0 à 830 px, 65 % de la largeur), légèrement inclinée, détourée en couleur réelle sur un halo menthe qui va jusqu'aux bords. Une pastille menthe « 16 Go » est posée au centre du X.
- **Texte** : « même carte, même IA : » en gris, puis « **101** ou **13** ? », avec 101 en menthe (ce que tu gagnes), 13 en rouge `#ff453a` (ce qu'on te prend), en Inter ExtraBold.
- **Test des 50 %** : réussi. La ligne principale finit à y ≈ 260, sous la limite de 360.

## b · couleurs de Technovore (charte `vert.html`), par défaut pour la série

- **Exactement la même scène que a** : la carte, le texte, le cadrage.
- **Ce qui change** : l'ardoise `#34495e` quadrillée, Archivo Black pour la ligne principale, la marque en JetBrains Mono.
- **13 en blanc** : la menthe reste le seul accent de la charte verte, comme le veut le § 2 de `ressources/miniatures/propositions.md`. C'est la seule différence de sens avec a. Si b perd, essaie 13 en rouge avant de conclure contre le vert.

## c · hors niche : le « drag race » de l'automobile

- **D'où elle vient** : la chaîne **carwow**, vidéo *Are TUNED cars a WASTE of MONEY? Honda Civic Type R DRAG RACE* (`I85lipyYTAo`, 1,9 M de vues, `refs/horsniche-carwow-tuned-…`). On y retrouve le même ressort : des machines identiques, une seule différence de réglage, et une étiquette par couloir.
- **Ce qu'on en reprend** :
  - le plein jour ;
  - la piste en perspective avec sa ligne jaune ;
  - les étiquettes rouges à pointe ;
  - les capitales étroites avec un contour noir.
- **Ce qu'on n'en reprend pas** : leurs photos, leur mise en page exacte, leurs voitures.
- **Visuel** : deux fois la même 5080 sur la ligne de départ, une étiquette menthe « 101 TOK/S » d'un côté, une rouge « 13 TOK/S » de l'autre. En haut, « **MÊME CARTE ?!** » (Anton blanc, contour noir).
- **Pourquoi** : c'est la seule tuile claire et colorée parmi des concurrents tous sombres (voir `apercu/accueil_sombre.png`). Elle se lit à 168 px.
- **Limites** :
  - elle quitte la charte, et la vidéo ne commence pas sur cette scène ;
  - les deux cartes sont la même photo : avec ta photo, garde deux fois la même carte ;
  - la marque technovore est masquée (les cartes la recouvraient).
  - **PSD** : Anton n'est pas installée dans `~/Library/Fonts`, donc les textes de c restent dans le décor. Pour les éditer, change le HTML et refais le rendu.

## d · les mains et le contre-jour rouge (ta référence du 05/11)

- **D'où elle vient** : ta référence [`refs/ref-mains-console-rouge.jpg`](refs/ref-mains-console-rouge.jpg) (une console noire à contre-jour, fond rouge, fumée rose, deux mains qui avancent sans la toucher). On en reprend l'ambiance et le geste, pas l'image : ni la console, ni ses mains, ni son cadrage exact.
- **Scène** : ta 5080 au centre, en gros (640 px de large, de x = 320 à 960), de face, à contre-jour : bord rouge lumineux, aberration chromatique légère. La chaleur monte d'elle en fumée rose. Deux mains entrent par les bords gauche et droit, doigts tendus, et s'arrêtent à 20 px de la carte. Fond rouge monochrome `#e0122c`, vignettage léger.
- **Ce qu'elle raconte** : tout le monde veut cette carte, et elle chauffe à fond. Le texte pose le doute du spectateur, et le titre y répond.
- **Texte** : « **TROP PETITE ?** » (Anton blanc, centré, de y = 40 à 175).
  - **Duo avec le titre** : la miniature demande « 16 Go, c'est trop petit ? », le titre répond « 16 Go suffisent, si tu prends le bon fichier ». Aucun mot répété.
  - **Aucune affirmation à sourcer** : c'est une question. La fumée est une image (la carte à pleine charge), pas une mesure ; la vidéo ne parle pas de température, donc pas de « °C » ni de « elle surchauffe ».
  - Écartés : « 16 Go ? » (répète le titre), « TROP CHAUD ? » (promet une vidéo sur la chaleur, que la vidéo ne tient pas), aucun texte (la scène seule dit « objet convoité », pas « 16 Go suffisent-ils ? »).
- **Règles communes** : texte dans la moitié haute, rien d'important dans le coin de la durée (seul l'avant-bras droit, fondu, y passe), 4K. **Exception assumée** : l'objet est au centre et non à gauche, comme dans ta référence. Comme c, elle quitte la charte et la vidéo ne commence pas sur cette scène.
- **Images et licences** :
  - **La carte** : la 5080 FE que tu as fournie (image NVIDIA, voir plus haut), assombrie et éclairée en rouge en CSS.
  - **Les mains** : « Hands Darkness », [StockSnap](https://stocksnap.io/photo/hands-darkness-62ZEVNXMHK), **CC0** (aucune attribution requise), original dans `sources/mains-darkness-stocksnap-cc0.jpg`. On n'en garde que la main gauche, détourée par `photocraft/detoure-main.py` → `photocraft/main-detouree.png` ; la main droite est la même, retournée. Étalonnage rouge et aberration en CSS (`.d .main`).
  - **La fumée** : dessinée (bruit SVG), aucune image.
- **Coach (`/coach-miniature-youtube`)** :
  - **Test de la seconde (v1)** : « une carte graphique que des mains veulent attraper ; trop petite ? ». C'est la seule tuile rouge parmi les concurrents ([`apercu/accueil_sombre_d.png`](apercu/accueil_sombre_d.png)).
  - **Alertes de la v1, corrigées** :
    1. **72 % du pourtour était quasi noir** (vignettage trop fort, comme la référence) : la tuile se fondait dans le mode sombre. Rouge étendu jusqu'aux bords, vignettage allégé : 8 %.
    2. **La carte était un pavé noir à 168 px** : éclaircie (0,32 → 0,6) et bord rouge plus large ; les deux ventilateurs se lisent.
    3. **Les mains touchaient la carte et les manches s'arrêtaient net** : carte réduite de 740 à 640 px, mains reculées, avant-bras fondus vers le bas.
    4. **La fumée faisait des vers et un bord droit** : remplacée par un panache de bruit flouté.
    5. **Le texte rétrécissait à 30 px** (l'ajustement `data-w` sur une boîte de 1280 px) : retiré, le texte fait 128 px.
  - **Test des 50 %** ([`apercu/test-50-d.png`](apercu/test-50-d.png)) : réussi, la question finit à y = 175. Planche : [`apercu/planche_d.png`](apercu/planche_d.png).
  - **Limite** : la main ne vient que d'une photo de 960 px de large, agrandie ×3 : douce en 4K, invisible à la taille d'une miniature. Le contre-jour rouge de la référence est moins sombre ici, pour la lisibilité.
- **PSD** : comme c, Anton n'est pas installée, donc « TROP PETITE ? » reste dans le décor (vérifié : `photocraft-cli convert photocraft/d.psd` donne exactement le rendu). Pour le changer, édite le HTML et refais le rendu.
- **À fournir pour la version finale** :
  - **tes mains**, en deux photos : main gauche puis main droite, chacune entrant par le bord du cadre, paume vers le bas, doigts écartés et légèrement pliés comme pour saisir, poignet et avant-bras visibles (manche sombre). Fond uni sombre, une seule lumière forte de face ou de trois quarts, au moins 3000 px de large. Détoure-les dans PhotoCraft, enregistre-les en PNG à la place de `photocraft/main-detouree.png` (la droite en `main-droite.png`, et change la 2e `<img class="main">` de la maquette), puis `./rendre.sh d`.

## e · la gravure sur rouge (ta référence du 05/11)

- **D'où elle vient** : ta référence [`refs/ref-napoleon-rouge.jpg`](refs/ref-napoleon-rouge.jpg) (un portrait de profil gravé en noir et blanc, sur un rouge vif uni, un mot blanc en capitales en haut). On en reprend le traitement et la mise en page, pas l'image ni son mot (« WORK-MAXXING »).
- **Scène** :
  - fond rouge uni `#e3120b`, grain de papier léger (bruit SVG en `multiply`) ;
  - la 5080 FE en noir et blanc très contrasté, avec une trame de lignes discrète, façon taille-douce (`photocraft/gravure.py` → `photocraft/rtx5080-gravure.png`) ;
  - la carte est grande (1060 px de large, de x = 110 à 1170), centrée, et **coupée par le bas du cadre** comme le buste de la référence : le connecteur et le bas de la carte sortent du cadre.
- **Texte** : « **ÇA RENTRE ?** » (Archivo Black blanc, 132 px, centré, de y = 52 à 184).
  - **Duo avec le titre** : la miniature demande si ça rentre, le titre répond « 16 Go suffisent, si tu prends le bon fichier ». Aucun mot répété.
  - **Tenu par la vidéo** : c'est la question du chapitre 1, « Un fichier qui rentre, un fichier qui déborde » (le Q3_K_M de 27 B rentre en entier dans 16 Go, le Q4_K_M de 17 Go déborde, S18 à S20). C'est une question : rien à sourcer en plus.
  - **Écartés par le coach** : « ASSEZ ? » (synonyme de « suffisent » : il répète le titre) ; « VRAM-MAXXING » (le plus lisible, mais c'est la formule exacte de la référence, et de l'argot anglais).
  - **Différent de d** : d demande si la carte est trop petite, e si le modèle rentre dedans.
- **Coach (`/coach-miniature-youtube`)** :
  - **Test de la seconde** : « une carte graphique, est-ce que ça rentre ? ». C'est la seule tuile rouge parmi les concurrents ([`apercu/accueil_sombre_e.png`](apercu/accueil_sombre_e.png), [`apercu/accueil_clair_e.png`](apercu/accueil_clair_e.png)) ; à 168 px, le texte et les deux ventilateurs se lisent ([`apercu/planche_e.png`](apercu/planche_e.png)).
  - **Corrections de la v1** :
    1. **La carte flottait au-dessus du bas du cadre** (960 px, entière) : agrandie à 1060 px et descendue pour être coupée, comme dans la référence.
    2. **Le texte ne disait rien de plus que le titre** (« ASSEZ ? ») : remplacé par « ÇA RENTRE ? ».
    3. **Le grain de papier était invisible** (bruit blanc en `multiply`) : passé en grain sombre, et les fibres horizontales sont atténuées (elles faisaient des vagues).
  - **Test des 50 %** ([`apercu/test-50-e.png`](apercu/test-50-e.png)) : réussi, la question finit à y = 184.
  - **Exceptions assumées** : comme dans la référence, l'objet est au centre et non à gauche. Le coin de la durée tombe sur le bas du ventilateur droit : seulement de la carte, rien à lire. Pas de marque technovore.
  - **Limite** : en niveaux de gris, le rouge et le gris de la carte se rapprochent ; c'est la teinte et le liseré blanc de la carcasse qui détachent la carte.
- **Poids** : 8,8 Mo (la trame est très détaillée) : importe-la depuis l'ordinateur.
- **PSD** : `photocraft/e.psd`, décor + un calque de texte « ÇA RENTRE ? » en Archivo Black (installée). Vérifié avec `photocraft-cli convert` : identique au rendu. Comme c et d, elle quitte la charte, et la vidéo ne commence pas sur cette scène.

## Critique (`/coach-miniature-youtube`) et corrections

- **Test de la seconde (v1)** :
  - a et b : « une carte graphique, 101 ou 13, pourquoi ? » ;
  - c : « deux cartes identiques, une rapide, une lente ».
- **Alertes de la v1**, avec ce qu'on a corrigé :
  1. **La carte était trop petite et le coin bas à droite vide** (a, b) : carte agrandie de 720 à 900 px de large et inclinée de 6°, ligne principale passée de 150 à 178 px.
  2. **83 % du pourtour était quasi noir** dans a : la tuile se fondait dans le mode sombre. Le halo menthe est élargi jusqu'aux bords (comme `noir-01` le 21/10), et l'alerte a disparu.
  3. **Faible contraste de valeurs** (a, b) : la carte est noire et grise, et c'est le halo qui la détache. Avec ta photo, si ta carte a des LED ou un dos coloré, montre-les.
  4. **Les étiquettes de c étaient trop petites** : passées de 74 à 96 px.
  5. **Le PSD perdait les tailles mixtes** (« ou » plus petit) : la ligne principale est coupée en 3 calques de texte. Le PSD et le rendu sont identiques (vérifié avec `photocraft-cli convert`).
- **Test des 50 %** ([`apercu/test-50.png`](apercu/test-50.png)) : les trois passent. La ligne principale et les chiffres sont dans la moitié haute.
- **Rien dans le coin de la durée** (x > 1100, y > 610).
- **Classement (hypothèse, le public tranche)** :
  - **c** pour le clic : la plus lisible, et la seule claire de la page ;
  - **a** pour le contraste ;
  - **b** pour la série.
- **Test proposé** : a, b, c ensemble, critère de la part de durée de visionnage. Publie avec b (charte de la série, et c'est la scène d'ouverture).
- **Compte des victoires** (série « IA chez moi ») : à remplir après le test.

## Refaire

| Pour… | Faire (depuis `miniature/`) |
|---|---|
| Changer un texte, la position de la carte | éditer `propositions/miniature.html`, puis `./rendre.sh` (ou `./rendre.sh b`, `./rendre.sh e`) |
| Refaire les PSD | `python3 -I ../../../ressources/miniatures/psd.py --page propositions/miniature.html photocraft a b c d e` |
| Refaire le détourage | `python3 -I photocraft/detoure.py` (recadre ta 5080 FE), puis `python3 -I photocraft/gravure.py` pour la gravure de e ; `python3 -I photocraft/detoure-main.py` pour la main de d |
| Refaire les aperçus | le script `apercu_miniature.py` du skill coach, avec `--contexte` sur 6 miniatures de `refs/` |
