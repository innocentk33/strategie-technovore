# Miniatures Technovore : une charte par pilier

> **v2 du 21/10/2026**, après la critique du coach ([`coach.md`](coach.md)) : **noir** pour « Le génie derrière l'app » et les grandes histoires de la tech, **vert** pour « IA chez moi ».
> - **Images** : [`rendus/`](rendus/), 11 miniatures en 4K (3840×2160, depuis le 23/10). La v1 (20 propositions, deux chartes par sujet) est dans [`rendus/v1/`](rendus/v1/).
> - **PhotoCraft** : [`photocraft/`](photocraft/), un PSD par miniature : le décor en calque d'image, chaque texte droit en calque de texte modifiable.
> - **Tests de lisibilité** : [`planches/`](planches/). `flux-vert.png` et `flux-noir.png` placent 4 des nôtres parmi 8 miniatures concurrentes, sur le fond sombre de YouTube ; `168.png` les montre à la taille des suggestions.

## 1. Ce que font Kai et les 5 chaînes proches

Chaînes trouvées par vidIQ (concurrents de Kai), plus AIex pour le matériel. 16 miniatures téléchargées par chaîne : les 12 plus vues et les 4 dernières. Planches dans [`concurrents/`](concurrents/).

| Chaîne | Abonnés (30 j) | Ce qu'on reconnaît avant de lire | Cohérence |
|---|---|---|---|
| **Kai** | 48 K (+135 %) | Illustration plate de l'objet acheté (Mac mini, RTX) avec un **décalage rouge et bleu façon sérigraphie**, 1 à 3 mots énormes (« USELESS. », « DON'T OVERPAY »), signature `<kaiexplainsyt>●` | 15/15 |
| **RepoChad** | 11,7 K (+35 %) | **Tout à la craie sur un tableau noir** : un schéma par miniature | 16/16 |
| **Codacus** | 45 K (+10 %) | Bleu nuit, **chiffres néon énormes**, **la même carte graphique plate** dans 9 miniatures sur 14, autocollants jaunes « HOW?! » | 14/14 |
| **The Stack** | 14,7 K (+13 %) | Noir, **logo ou produit en 3D brillant sur un sol mouillé**, texte blanc condensé à gauche | 16/16 |
| **RandomAI** | 12,9 K (+36 %) | **Bandeau vert-jaune fluo en haut** (« X is Insane »), 2 ou 3 captures dessous | 15/15 |
| **WeeklyHow** | 38,7 K (+5 %) | Logos des IA, flèche avant/après, captures de jeux ; parfois un visage | Faible |
| **AIex** | 1,35 K (+90 %) | Visage pensif et bandeaux rouges et noirs | Moyenne |

**Ce qu'on en retient :**
1. **Une chaîne se reconnaît à un élément fixe qu'on voit avant de lire** : une surface (le tableau de RepoChad, le bandeau de RandomAI), un traitement (le décalage de Kai, le sol mouillé de The Stack) ou un objet récurrent (la carte graphique de Codacus).
2. **1 à 3 mots, et des chiffres énormes.**
3. **Le noir ne distingue plus personne dans l'IA en local** : 5 chaînes sur 7 sont sur fond noir ou bleu nuit.
4. **L'objet est celui du spectateur** : sa carte graphique, son Mac, son appli.

## 2. Les règles figées (au moins 5 vidéos sans y toucher)

### Communes aux deux chartes

- **Mise en page** : un objet héros à gauche (au moins 40 % de la largeur), le texte aligné à gauche vers x = 640-700, centré en hauteur. Exception : la série « Claude ou mon PC ? ».
- **Texte, 2 lignes au plus** :
  - une ligne de contexte grise de 4 mots au plus, seulement si elle dit ce que le titre ne dit pas ;
  - une ligne principale de 3 mots au plus, d'au moins 110 px, terminée par « . » ou « ? ».
- **Jamais la même information que le titre.**
- **Logos dans leurs vraies couleurs** : Uber noir, Waze cyan, WhatsApp vert, Claude orange.
- **Rien d'important sous 50 px de haut**, ni dans le coin de la durée (x > 1100, y > 610).
- **Export en 4K** (décidé le 23/10, nos vidéos étant longues) : 3840×2160 en 16:9. On dessine toujours dans une page de 1280×720, et `rendre.sh` et `psd.py` la rendent à ×3 ; toutes les cotes de ce document restent en 1280×720. YouTube accepte 50 Mo depuis un ordinateur, mais seulement 2 Mo depuis l'appli mobile : importe la miniature depuis l'ordinateur (aide YouTube « Ajouter des miniatures de vidéo », lue le 23/10).
- **La menthe `#07c095` dans les deux chartes** : c'est le fil qui relie les piliers (ponctuation « gagnée » et voyant de la marque en noir).
- **Polices libres** : Inter, Archivo Black, JetBrains Mono (OFL). SF Pro n'est plus utilisée (voir § 5).

### Noir : génie derrière l'app, grandes histoires

- Noir, **grille sombre et halo** de la couleur d'accent derrière l'objet (comme `uber-b`) : la tuile se détache du mode sombre de YouTube.
- Objet réel, en couleur, **sans reflet au sol** (la signature de The Stack).
- Inter ExtraBold en minuscules, interlettrage −4 %, contexte gris `#8e8e93`.
- **Ponctuation finale** : rouge `#ff453a` pour ce qu'on te prend, menthe pour ce que tu as ou gagnes.
- Pour Uber et Waze, le gabarit « téléphone incliné + icône d'appli sur le coin » devient la signature du pilier ; la couleur dominante change à chaque vidéo.

### Vert : IA chez moi

- Ardoise `#34495e` quadrillée, jamais assombrie (sinon elle rejoint Codacus).
- Dessin au trait de la vidéo, **un grand objet plutôt que trois petits**, pas d'établi décoratif.
- Archivo Black en capitales pour la ligne principale, Inter 800 gris pour le contexte. La menthe est le seul accent, hors logos.
- **Badges droits** (inclinés, c'est le tic de Kai et Codacus). **Jamais la composition « logo dans un cadre → flèche → machine »** (celle de Kai).
- **Série « Claude ou mon PC ? »** : bandeau « CLAUDE OU MON PC » à hauteur fixe, Claude à gauche, ton PC à droite, « ? » au centre. Ce qui change à chaque épisode est toujours **dans la baie du haut du PC** (« 16 Go », puis le logo du modèle).

## 3. Les 11 miniatures retenues

| Fichier | Vidéo | Ce qu'on voit | Corrigé par rapport à la v1 |
|---|---|---|---|
| [`noir-01`](rendus/noir-01.png) | Uber, 26 oct. | `uber-b` : téléphone, voiture fantôme désignée par une flèche, « **elle existe ?** » | Reprise en Inter, puis corrigée le 21/10 : voiture fantôme agrandie et teintée de rouge, vrai logo Uber, halo élargi jusqu'aux bords (pourtour quasi noir : 97 % → 66 %) |
| [`noir-01b`](rendus/noir-01b.png) | Uber, variante A/B | Même décor, « sa position est / **devinée.** » | Variante de texte pour le test |
| [`vert-02`](rendus/vert-02.png) | Claude ou mon PC ? #1, 2 nov. | Gabarit de série, « 16 Go » dans la baie du PC | Plus de composition Kai, ni de cédille flottante, ni d'établi |
| [`noir-03`](rendus/noir-03.png) | Waze, 9 nov. | Bouchon rouge, détour bleu, icône Waze, « personne ne l'a signalé, / **il savait.** » | « avant toi » répétait le titre ; rivière retirée |
| [`noir-04`](rendus/noir-04.png) | Pixel, 14 déc. | Un écran blanc, une loupe sur ses sous-pixels, « il n'y a pas / **de blanc.** » | L'écran blanc montre la contradiction sans lire |
| [`vert-05`](rendus/vert-05.png) | Coût de Claude en local, 16 nov. | Ta 5080 minuscule au pied d'une baie géante, « Claude chez moi, » + étiquette de prix | Nouveau concept (l'ancien copiait la série de Kai) |
| [`noir-06`](rendus/noir-06.png) | WhatsApp, 11 janv. | Icône WhatsApp, « 900 millions, / **50** / ingénieurs. » | Pas de reflet ; **c'est le titre qui change** (fiche WhatsApp, titre 4) |
| [`noir-07`](rendus/noir-07.png) | Pseudo pris, 23 nov. | Formulaire, « technovore » en erreur, « Ce nom est déjà pris. », « **il triche.** » | Ligne grise et petits textes retirés ; « G » de Google ajouté (voir § 5) |
| [`noir-08`](rendus/noir-08.png) | Jeux, 22 févr. (provisoire) | PS5 éteinte en gris, « acheté. / **pas à toi.** » | Les trois cartes illisibles retirées |
| [`vert-09`](rendus/vert-09.png) | llama.cpp, 8 mars (provisoire) | Grand portable, une ligne de commande, « llama.cpp », « codé en **1 SOIRÉE.** » | Calendrier retiré, ordinateur agrandi |
| [`vert-10`](rendus/vert-10.png) | Claude ou mon PC ? #2, 18 janv. | Gabarit de série, emplacement du logo du modèle dans la baie | Mettre le logo réel (en couleurs) quand le modèle sera choisi |

## 4. Tester les deux chartes et le lien avec la DA de la vidéo

### Deux miniatures par vidéo : oui, avec un protocole

« Tester et comparer » (YouTube Studio, sur ordinateur) : jusqu'à 3 miniatures, gagnant choisi sur la **part de durée de visionnage** (pas le taux de clic), test de 2 semaines au plus, résultat « gagnante », « équivalentes » ou « non concluant ».

1. **Une seule variable par test.** Pour savoir quelle **charte** gagne, les deux miniatures ont le même objet, la même idée et le même texte : seule la charte change. Si l'idée change aussi, tu sauras quelle idée a gagné, pas quelle charte.
2. **2 variantes, pas 3** : à ta taille, chaque variante supplémentaire divise les impressions et rend le résultat « non concluant » plus probable.
3. **Un test ne décide pas d'un format.** Compte les victoires sur 4 à 6 vidéos par pilier avant de changer la règle.
4. **Ordre proposé** :
   - **Uber (26/10)** : test de **texte** (`noir-01` contre `noir-01b`), voir [`projets/uber/upload.md`](../../projets/uber/upload.md).
   - **À partir de Claude ou mon PC ? #1 (2/11)** : test de **charte** sur chaque vidéo (`vert-02` contre la même scène en noir), puis Waze, pixel, coût de Claude, WhatsApp. La jumelle de chaque miniature, dans l'autre charte, se fait à partir de l'HTML (compter environ 30 à 60 min, estimation).
5. **Ne touche ni au titre ni à la miniature pendant le test** : ça l'arrête.

### La DA de la vidéo doit-elle correspondre à la miniature ?

**Pas toute la vidéo, mais ses 5 premières secondes, oui.** Sur l'accueil, la vidéo démarre seule au survol : son début prolonge la miniature (guide du skill YouTube). Le premier plan doit donc reprendre l'objet et la question de la miniature, comme tu l'as fait pour Uber (plan #1 = le même téléphone). Ensuite, la DA est libre.

**Garder le noir ou passer au vert ? Ni l'un ni l'autre pour toute la chaîne : une DA par pilier, comme les miniatures.**
- **Génie derrière l'app → noir premium.** Uber est déjà enregistré et découpé en noir, et Waze et WhatsApp réutiliseront ses animations de carte.
- **IA chez moi → vert explainer.** Le template a été construit pour ça : axe gradué, carte graphique, étiquette de prix, mesure de VRAM. Il entre en service avec Claude ou mon PC ? #1 (2/11).
- **Pendant les tests de charte**, la miniature perdante n'a pas de premier plan assorti. C'est un handicap réel : si elle gagne malgré tout, le signal est d'autant plus fort.

## 5. À vérifier avant de publier

- **Uber** (`noir-01b`) : « devinée » simplifie le script (« en partie devinée »). Vérifié le 21/10 : la vidéo le dit et l'affiche à 9:00.
- **Coût de Claude** : « ?? ??? € » est un emplacement pour le prix calculé. L'étiquette tient jusqu'à « 999 999 € » (la taille du texte s'ajuste). Anthropic ne publie pas les poids de Claude : dire dans la première minute que le calcul utilise le plus gros modèle ouvert du même niveau.
- **Pseudo pris** (`noir-07`) : **aucune source ne montre que Google utilise un filtre de Bloom** pour les pseudos (recherche du 21/10). Sans preuve, retirer le « G » et Google du titre (voir `strategie.md`, idée 4).
- **Jeux** (`noir-08`) : le cas Sony de décembre 2023 concernait des **séries** Discovery, et Sony a fait marche arrière. La vidéo doit le dire ainsi, ou s'appuyer sur un cas de **jeu** (voir `strategie.md`, idée 8).
- **llama.cpp** : vérifié, le README de mars 2023 dit « hacked in an evening ». La commande affichée est tronquée (`./main -m ./models/7B/…`).
- **SF Pro** : sa licence Apple réserve l'usage aux maquettes d'interfaces Apple, d'après le coach (à confirmer). Les miniatures Uber et OpenCode existantes l'utilisent ; la v2 est passée à Inter.
- **Logos** : tracés simple-icons (CC0), mais les marques restent à leurs propriétaires, comme sur toutes les miniatures tech. Le « G » de Google est le logo officiel en couleurs. La photo de la PS5 vient de `essais V2F/premium/assets/`.

## 6. Modifier et refaire

| Pour… | Faire |
|---|---|
| Changer un texte ou un dessin | Éditer `noir.html` (`?n=1`, `1b`, `3`, `4`, `6`, `7`, `8`) ou `vert.html` (`?n=2`, `5`, `9`, `10`), puis `./rendre.sh noir 3` (ou `./rendre.sh` pour toutes) |
| Retoucher dans PhotoCraft | Ouvrir `photocraft/noir-03.psd`. Les textes inclinés ou dans un badge font partie du décor : les changer dans le HTML |
| Refaire les PSD après une modification du HTML | `python3 -I psd.py noir 3` (ou sans argument pour toutes) |
| Comparer une miniature aux vidéos où elle sera suggérée | Mettre leurs `.jpg` dans `projets/<nom>/miniature/hotes/`, puis `python3 -I planches.py --suggestions <notre miniature> projets/<nom>/miniature/hotes` → `planches/suggestions-<nom>.png` (colonne de 168 px). Pourquoi : `etudes/suggestions-2026-10-23.md` |
| Refaire les planches de test | `python3 -I planches.py <dossier>`, avec un sous-dossier de miniatures `.jpg` par chaîne concurrente (téléchargées avec `yt-dlp --flat-playlist` puis `i.ytimg.com/vi/<id>/maxresdefault.jpg`) |

Polices : Archivo Black, Inter et JetBrains Mono sont dans [`fonts/`](fonts/) pour le HTML. Pour PhotoCraft, elles sont installées dans `~/Library/Fonts` (Archivo Black, Inter Bold, ExtraBold et Black, JetBrains Mono variable ; toutes sous licence OFL). La version d'Inter fournie avec PhotoCraft s'arrête à SemiBold.
