# Miniature de la vidéo Strata (lun. 16/11/2026) : propositions du 11/11, v2 « grand public »

> Style imposé : celui d'OpenCode piraté (règle du 11/11, `.claude/rules/miniatures.md`). Maquette : [`propositions/miniature.html`](propositions/miniature.html) (`?v=a|b|c`), rendus 4K (3840×2160) dans [`rendus/`](rendus/) avec `./rendre.sh` ; PSD à calques (décor + 2 calques de texte) dans [`photocraft/`](photocraft/) avec `python3 -I ressources/miniatures/psd.py --page projets/strata-test/miniature/propositions/miniature.html projets/strata-test/miniature/photocraft a b`. Aperçus du coach : [`apercu/`](apercu/).
>
> **v2 (11/11, ta demande)** : plus de « MA 5080 » ni de photo de ta carte Inno3D. Une 5080 est chère et rare ; la miniature parle maintenant à **quiconque a une carte de 16 Go** (5060 Ti, 4060 Ti, RX 9060 XT…). La v1 est gardée : [`propositions/miniature-v1.html`](propositions/miniature-v1.html), [`rendus/v1/`](rendus/v1/), [`photocraft/v1/`](photocraft/v1/), [`apercu/v1/`](apercu/v1/) (§ 10).
>
> **Les tests ne sont pas encore faits** : a et b n'affirment aucun chiffre ni aucun verdict. La variante c est un gabarit à remplir après les tests.

> **12/11, ta décision : le test A/B oppose l'ancien texte au texte « PEAK »**, sur « TON PC / VS CLAUDE ? » et le même meme (The Rock). b (« AU NIVEAU ? ») sort du test.
> - **a** : [`rendus/a.png`](rendus/a.png), Inter 900, « TON PC » en blanc et « VS CLAUDE ? » en rouge.
> - **a-peak** : [`rendus/a-peak.png`](rendus/a-peak.png), les 2 lignes en blanc, en Anton, avec une copie rouge un peu plus grande et décalée vers le bas ([référence](../../../ressources/miniatures/images/reference-texte-peak.jpg)). PSD : [`photocraft/a-peak.psd`](photocraft/a-peak.psd) (4 calques de texte).
> - Maquette : `?v=a&txt=peak` ; rendu : `./rendre.sh "a&txt=peak"` → `rendus/a-peak.png`. Avant/après et 168 px : [`apercu/essai-peak.png`](apercu/essai-peak.png).
> - **Seul le texte change.** Après les tests, la variante c se rend aussi en PEAK (`./rendre.sh "c&txt=peak&rouge=…&toks=…"` → `rendus/c-peak.png`) si PEAK gagne.

> **14/11 au soir, ta demande : variante d, « PEAK + Qwen + carte + visage ».** [`rendus/d-peak.png`](rendus/d-peak.png), PSD [`photocraft/d-peak.psd`](photocraft/d-peak.psd) (4 calques de texte), maquette `?v=d&txt=peak`, test 168 px et 50 % : [`apercu/test-50-et-168px-d.png`](apercu/test-50-et-168px-d.png).
> - **Ce qui change par rapport à a-peak, et seulement ça** : l'objet. Le logo de Qwen sur une tuile blanche de 150 px (lisible à 168 px, le bleu de Qwen disparaîtrait sur le noir) et la vraie photo d'une 5080 FE (sans marque visible), au lieu de la carte et de la barrette dessinées. Même texte (« TON PC / VS CLAUDE ? », toujours la question du hook), même meme (The Rock, le doute).
> - **Pourquoi le logo** : la V3 nomme Qwen 3.8 Flash Next dès la première phrase et a une section sur sa puissance (l'avant-goût de Qwen 4) ; le logo dit « Qwen » à ceux qui le cherchent, sans le mot dans le texte.
> - **Ce qu'on perd** : la barrette « 32 GO », qui rappelait la condition de RAM ; le titre et la vidéo (section 5) le disent.
> - **Test A/B proposé** : a-peak contre d-peak, une seule chose change (l'objet). Si tu veux un autre texte (`?v=d&txt=peak&l1=…&l2=…`), ce sera une autre variante, à tester à part.
> - **Visage : The Rock est gardé** (14/11 au soir, ta décision), pas de visage généré.
>
> **14/11 au soir, ta demande : deux variantes de plus, avec les tokens par seconde ou un versus.** Même meme, même style PEAK ; test 168 px et 50 % : [`apercu/test-50-et-168px-dfg.png`](apercu/test-50-et-168px-dfg.png).
> - ~~**e**~~ (d + badge « ≈ 70 TOK/S · 5080 ») : **supprimée le 14/11 au soir** (« nulle », ta décision) ; rendu et PSD effacés.
> - **f** ([`rendus/f-peak.png`](rendus/f-peak.png), [`photocraft/f-peak.psd`](photocraft/f-peak.psd)) : le versus, logo de Qwen « VS » logo de Claude (sa vraie marque orange sur crème), sans carte. Comme « VS » est déjà dans les logos, le texte devient **« TON PC / SUFFIT ? »** : ton PC, avec Qwen, suffit-il face à Claude ? C'est la question du hook (« est-ce que ça remplace Claude ? ») et la réponse du verdict (« pas complètement, mais il n'en faut plus qu'un petit »).
> - **g, à la manière de Kai** ([`rendus/g-peak.png`](rendus/g-peak.png), [`photocraft/g-peak.psd`](photocraft/g-peak.psd), 14/11 au soir, ta demande) : **pas de visage**, une scène dessinée à plat à droite, comme chez Kai (`ressources/miniatures/concurrents/kai.jpg`, `etudes/kai.md` § 4.3) : contours noirs épais, ombres décalées rouge et bleue, tuiles inclinées de Qwen « VS » Claude, et une carte jaune avec l'étiquette « 16 GO ». Même texte que f (« TON PC / SUFFIT ? ») en PEAK, fond de code atténué. **Ce qu'on reprend de Kai** : le dessin plat, les ombres décalées, le jaune ; **ce qu'on ne copie pas** : aucune de ses scènes (pas de flèche Claude → carte comme « HERE WE GO. LOL », pas de signature), et le texte reste PEAK.
> - **Lecture du test** : f contre g ne change que l'image (meme contre dessin à la Kai), avec le même texte ; d sert de référence (« VS CLAUDE ? », la question du hook). YouTube teste jusqu'à 3 miniatures : **d, f et g**.
>
> **14/11 au soir, ta demande : 3 propositions de plus « à la manière de Kai »**, d'après 5 de ses miniatures (*284B on a potato?*, *Don't overpay*, *No more free lunch*, *It's here*, *LLMs are done*). Maquette à part : [`propositions/miniature-kai.html`](propositions/miniature-kai.html) (`?v=h|i|j`), rendu `./rendre.sh kai`, test 168 px et 50 % : [`apercu/test-50-et-168px-kai.png`](apercu/test-50-et-168px-kai.png). **Repris de Kai** : fond sombre et calme, un seul mot en couleur avec sa copie décalée (le mot blanc n'en a pas), une police large (Archivo Black, pas Anton), objets et visage cernés de blanc avec une ombre décalée, tuiles de logos inclinées, visage illustré à gauche et texte à droite. **Pas copié** : ses scènes (la patate, la main, la tête ouverte), ses visages, sa signature.
> - **h, Kai + visage** ([`rendus/h-kai.png`](rendus/h-kai.png), [`photocraft/h-kai.psd`](photocraft/h-kai.psd)) : The Rock « illustré » (photo lissée et postérisée, contour blanc, ombres rouge et bleue : `sources/the-rock-kai.png`), « TON PC / SUFFIT ? » en blanc et jaune, Qwen « VS » Claude dessous.
> - **i, Kai aux couleurs de Technovore** ([`rendus/i-kai.png`](rendus/i-kai.png), [`photocraft/i-kai.psd`](photocraft/i-kai.psd)) : fond ardoise `#34495e` avec une grille discrète, « TON PC SUFFIT ? » sur une ligne en blanc et menthe `#07c095`, la carte menthe avec l'autocollant Qwen et l'étiquette « 16 GO », « VS » la tuile Claude. Pas de visage.
> - **j, couleurs de Technovore + visage** ([`rendus/j-kai.png`](rendus/j-kai.png), [`photocraft/j-kai.psd`](photocraft/j-kai.psd)) : The Rock en duotone ardoise et menthe (`sources/the-rock-technovore.png`), texte à droite, la carte et Qwen dessous.
> - **Limite** : le visage « illustré » est un filtre sur la photo, pas un vrai dessin comme ceux de Kai. Si tu veux ce rendu-là, génère avec ChatGPT un portrait illustré (le même meme ou un autre visage autorisé), détouré sur fond uni, regard vers la droite : il remplace `the-rock-kai.png` sans toucher au reste.
> - **Lecture d'un test** : h contre j ne change que les couleurs (Kai contre Technovore) ; i contre j ne change que le visage.

> - *(Ancienne piste, écartée)* **Si tu génères des éléments avec ChatGPT** : le plus utile serait un visage plus expressif que The Rock (surpris ou bluffé, puisque la vidéo dit qu'« il s'en sort bien »), détouré sur fond uni, regard vers la gauche, ou une carte de 16 Go générique en 3D, sans marque. Pas de logo Qwen généré : on garde le vrai.

## 1. Le concept

- **Ce que la vidéo promet** (script V2) : la moitié d'un modèle géant tourne avec une carte de 16 Go **et 32 Go de RAM** ; elle code un jeu, un site et un mini-Minecraft en 3D (à la place de l'île depuis le 13/11) ; puis la question de la fin : « est-ce que ça remplace Claude ? ».
- **Question posée par l'image** : ton PC de joueur peut-il tenir tête à Claude ?
- **Émotion** : le doute, le défi. Dwayne Johnson lève le sourcil (« The People's Eyebrow ») et regarde le texte : « vraiment ? ». Ce doute marche que le local gagne ou perde ; un visage impressionné ou une grimace « yikes » donnerait déjà le verdict (§ 7). Il reste parce qu'il colle aussi au « TON PC » : c'est le spectateur qu'il met au défi.
- **Types combinés** (coach) : réaction (meme) + comparaison (« VS ») + question.
- **Pourquoi la RAM est sur l'image** : le script dit « il te faut au moins trente-deux gigas de RAM » (section 7) et que le modèle complet ne rentre pas dans 32 Go (0:25). Montrer seulement « 16 Go » laisserait croire que la carte suffit.

## 2. Les deux variantes (test A/B : seule la ligne rouge change)

| | Objet (en haut à gauche) | Ligne blanche | Ligne rouge | À droite |
|---|---|---|---|---|
| **a** ⭐ | une carte sans marque « 16 GO » + une barrette « 32 GO » | **TON PC** | **VS CLAUDE ?** | The Rock, sourcil levé |
| **b** | idem | **TON PC** | **AU NIVEAU ?** | idem |

- **L'objet** : dessiné en SVG dans la page, gris neutre, sans logo ni modèle (deux ventilateurs, une équerre, des contacts dorés), avec une pastille blanche « 16 GO » ; à côté, une barrette de RAM « 32 GO ». N'importe quel propriétaire d'une carte de 16 Go s'y reconnaît, et la RAM rappelle la condition. À 168 px, on voit une carte et une barrette, pas les chiffres : c'est le titre qui les donne.
- **Fond** : noir `#050505`, des lignes de « journal » de Strata très sombres (inventées, illisibles en petit), un halo rouge `#ff3b30` derrière la tête et un autre, très faible, derrière le texte.
- **Texte** : Inter 900 en capitales, 128 px (blanc) et 116 px (rouge `#ff3b30`), aligné à x = 54. Le rouge finit à y = 352 : tout le texte est dans la moitié haute.
- **Meme** : détouré d'une vidéo sur fond vert, retourné en miroir pour qu'il se tourne vers le texte, liseré rouge. Yeux vers y = 300 ; seule l'épaule entre dans le coin de la durée.
- **Hypothèse du test** : a gagne, parce qu'elle nomme l'adversaire (Claude est la boucle de la vidéo). Si b gagne, le public préfère le défi sans nom de marque.

## 3. Les titres proposés

1. ⭐ **Le meilleur modèle possible pour 16 Go de VRAM (et 32 Go de RAM)** : ta formulation, avec la RAM pour ne pas promettre trop.
2. **16 Go de VRAM, 32 Go de RAM : le meilleur modèle de code possible** : plus précis (« de code » : le Coder est fait pour ça, et sa doc le dit plus faible ailleurs, T5).

**Le duo** : le titre dit *quoi* (le modèle, la config), la miniature dit *l'enjeu* (ton PC contre Claude). Seul « 16 GO / 32 GO » se répète, en petit sur l'objet : le coach l'accepte, parce que ce n'est pas le message de l'image.

**À tenir dans la vidéo** :
- **« le meilleur modèle possible »** n'est pas un fait sourcé. Ce que la vidéo peut dire : c'est **le seul fichier de Flash-Next que la doc prévoit pour un PC de 32 Go avec une carte de 12 à 16 Go** (T5), avec 95 % du score de code du modèle complet d'après ses auteurs (T6). Dis-le vers 2:30 (section 2 du script), sinon le titre promet plus que la vidéo.
- **La vitesse vient d'une 5080.** La miniature ne promet aucune vitesse, mais le titre s'adresse à toutes les cartes de 16 Go : précise dans la vidéo qu'une carte de 16 Go moins rapide ira sans doute moins vite (la 5080 a plus de bande passante qu'une 5070 Ti, T7 ; pour la 5060 Ti ou la 4060 Ti, aucune mesure dans `sources.md`).

À éviter :
- **« 125 milliards sur 16 Go »** : `sources.md` l'interdit pour le Coder (256 experts sur 512) ; c'est aussi le cliché de Zero to MVP et Tech-Practice ;
- **un poids en Go en gros** (« 60 Go ») : la vidéo dit « une soixantaine » au téléchargement et « 29,6 Go > 16 Go » à l'écran ; c'est aussi le look de Red Stapler et de Lite AI Lab ;
- **« 16 Go suffisent »** : faux sans les 32 Go de RAM.

## 4. Les références (`refs/`, téléchargées le 11/11, vues relevées le 11/11)

| Fichier | Origine | Ce qu'on en retient |
|---|---|---|
| `technovore-opencode-reference.jpg` | Ta miniature *OpenCode piraté* (4,2 %) | Le modèle : logo, 2 lignes blanc/rouge, visage qui sort du cadre |
| `technovore-16go-contre-exemple.png` | Ta *16 Go de VRAM* (09/11, 1,5 % à J+2) | Le contre-exemple : fond plein, pas d'émotion, texte sans sujet |
| `redstapler-qwen27b-8go.jpg` | Red Stapler, *I ran Qwen3.8 27B on single 8GB Card!* (ye50BbXEczo) | Le chiffre géant et la carte sur un dégradé vif : à ne pas copier |
| `redstapler-177b-ssd.jpg` | Red Stapler, *I run 177B model on SSD* (_TCRH725hAM) | Même gabarit : objet + chiffre |
| `nocodeabode-coder-32go.jpg` | NoCodeAbode, *How Good Is Strata's Qwen Coder on 32GB RAM?* (xze2CeR2Zu0) | « VS » + visage + « CAN HALF COMPETE? » : notre « VS » doit rester sobre |
| `zerotomvp-125b-16go.jpg` | Zero to MVP, *A 125B Local Model on a 16GB GPU* (B77LasklmZU) | « 125B → 16GB » : le cliché à éviter |
| `nathaninline-fr-flashnext-16go.jpg` | Nathan Inline (FR), *QWEN 3.8 FLASH NEXT : Enfin utilisable sur 16GB VRAM !* (cxvI2lqSC6w) | Visage + logo + « > 60 tokens/sec » sur fond violet |
| `buildmind-fr-vieux-pc.jpg` | Build & Mind (FR), *Les géants de l'IA veulent votre RAM* (9IRXDZpU1mQ) | Mascotte 3D, autre angle : rien à reprendre |
| `theaihobbyguy-fr-strata.jpg` | TheAIHobbyGuy, *Strata : faites tourner des modèles d'IA géants…* (K01jRME8tLs, titre traduit, audio EN) | Le mot-symbole STRATA, visage, liste à cocher |
| `bijanbowen-5090-vs-opus.jpg` | Bijan Bowen, *RTX 5090 + Strata – Can Local AI REALLY Beat Opus 4.6?* (5F4wdtNbMt4) | Le même duel que nous (local contre Claude), en visage + PC + logos sur fond bleu |
| `lukesdevlab-27b-vs-coder.jpg` | Luke's Dev Lab, *Qwen 3.8 27B vs Strata Coder* (xiMAxAQAfC4) | Notre config exacte (« 16GB VRAM + 32GB RAM ») en texte cyan |
| `brunovega-kai-strata-cheatcode.jpg` | Bruno Vega and Kai, *Strata Is This the Ultimate LLM Cheat Code?* (0Vz8FBoCvTA, audio EN) | **Le plus proche de notre style** : noir, « Strata » en blanc, 2e ligne rose-rouge. D'où « TON PC » au lieu de « STRATA » en ligne blanche, et un visage |
| `codebear-avalon-vs-strata.jpg` | Code Bear, *Avalon bat Strata 9 fois plus vite sur AMD* (yXJog4kbJdk, audio EN) | Noir aussi, mais des puces et des tok/s : pas de visage |
| `techpractice-125b-12go.jpg` | Tech-Practice, *Strata - How a 125B AI Model Fits on a 12GB GPU?* (_QfCPDQx4mA) | « 125B on 12GB?! » : encore le cliché du chiffre |
| `liteailab-claudecode-12go.jpg` | Lite AI Lab, *Strata + Claude Code sur Windows 11* (Fh3zn5SSSTs) | « 58 GB / 12 GB / 32 GB » : le poids en Go, déjà pris |

**Miniatures françaises sur Strata** : la recherche du 11/11 (yt-dlp) ne trouve que des titres traduits automatiquement ; les vidéos réellement en français sont Nathan Inline et Build & Mind. **Aucune ne met un meme** : toutes les miniatures du sujet sont des chiffres, des cartes, des logos ou le visage du créateur. Le visage d'un meme sur fond noir est donc notre différence, et aucune n'emploie la scène « 2 lignes + sourcil levé ».

## 5. La critique du coach (grille de `/coach-miniature-youtube`), v2

**Test de la seconde (168 px)** : « Ton PC contre Claude ? », une carte graphique, et un type qui n'y croit pas.

| Axe | Note | En une phrase |
|---|---|---|
| Lisibilité | 🟢 | 3 éléments (objet, 2 lignes, visage) ; le texte se lit à 168 px |
| Composition | 🟢 | Texte sur le tiers gauche, visage sur le tiers droit, regard vers le texte, rien sous la durée |
| Contraste | 🟠 | Blanc et rouge sautent ; 75 % du pourtour reste quasi noir (alerte du script), comme OpenCode |
| Texte | 🟢 | 4 mots (« TON PC VS CLAUDE ? ») ; aucun mot du titre en gros |
| Émotion | 🟢 | Le doute se lit en petit ; « TON PC » met le spectateur dans la scène |
| Types | 🟢 | Réaction + comparaison + question |
| Duo titre-miniature | 🟢 | Le titre donne la config, l'image l'enjeu ; ensemble : « mon PC à 16 Go peut-il rivaliser ? » |
| Différenciation | 🟢 | Seule tuile noire avec un meme au milieu des dégradés vifs ; Bruno Vega and Kai (noir, 2 lignes) reste le plus proche, le visage l'en sépare |
| Identité | 🟢 | Celle d'OpenCode |
| Promesse et technique | 🟠 | La vidéo compare bien à Claude (section 5). Le coach signale un visage célèbre dont la vidéo ne parle pas : ta règle des memes prime. « TON PC » ne promet pas ta vitesse : la vidéo doit dire qu'elle vient d'une 5080 (§ 3). PNG de 4,2 Mo : à importer depuis l'ordinateur |

**Corrections faites en v2** :
1. **« MA 5080 » → « TON PC »** : le spectateur au lieu de l'auteur, n'importe quelle carte.
2. **La photo de la 5080 Inno3D → un objet dessiné sans marque**, et la barrette de RAM « 32 GO » ajoutée pour ne pas laisser croire que la carte suffit.
3. **L'objet était trop gros et plat** au premier rendu (400 px de large, des ventilateurs en « Y ») : réduit à 340 px, des pales courbes.
4. **Le badge tok/s de c** dit maintenant « · 5080 » : un chiffre mesuré sur ta carte ne doit pas se lire comme celui de toutes les cartes de 16 Go.

Gardé de la v1 (corrections du coach déjà faites) : le visage en miroir tourné vers le texte, la taille du texte, le texte dans la moitié haute, le fond discret, la peau désaturée.

**Test des 50 %** ([`apercu/test-50-et-168px.png`](apercu/test-50-et-168px.png)) : moitié basse cachée, on lit « TON PC VS CLAUDE ? » (ou « AU NIVEAU ? »), l'objet et l'œil au sourcil levé. ✅ pour a et b.

Aperçus : [`apercu/planche_a.png`](apercu/planche_a.png), [`apercu/comparaison.png`](apercu/comparaison.png), [`apercu/accueil_sombre.png`](apercu/accueil_sombre.png) (a et b au milieu de Bruno Vega and Kai, Red Stapler, Code Bear, NoCodeAbode, Zero to MVP et Nathan Inline, avec le titre 1).

## 6. Le choix recommandé

**a (« TON PC / VS CLAUDE ? ») avec le titre 1.** Depuis le 12/11, le test A/B oppose a à a-peak (même texte, même meme, seul le style du texte change) ; b n'est plus testé. Ancienne recommandation : a en test A/B contre b dans « Tester et comparer ». a est la plus claire sans le titre et annonce la vraie boucle de la vidéo ; b est le challenger, même scène sans nom de marque.

## 7. Après les tests : la variante c (gabarit)

- `?v=c` remplace la ligne rouge par **⟦verdict⟧** et ajoute un badge **⟦tok/s⟧ tok/s · 5080** à côté de l'objet ([`rendus/c-gabarit-a-remplir.png`](rendus/c-gabarit-a-remplir.png), à ne pas publier tel quel).
- Pour la remplir sans toucher au code : `./rendre.sh "c&rouge=A%20TENU&toks=72"` → `rendus/c.png`. Sans badge : `./rendre.sh "c&rouge=A%20TENU&toks="`. Sinon, change `VERDICT` et `TOKS` dans le HTML.
- **Le badge garde « · 5080 »** : la vitesse est celle de ta carte, pas celle d'une 4060 Ti. Il se devine à 168 px sans se lire.
- **Le verdict doit être celui que tu dis dans la vidéo (R13)** et tenir en 10 caractères :
  - le local tient : « A TENU » ;
  - c'est serré : « PRESQUE » ;
  - il perd : « PAS ENCORE » (plus juste que « K.O. » : la vidéo ne fait pas de classement et annonce la suite du 19/11).
- **Changer le visage seulement si le verdict le justifie** (une grimace s'il perd, un visage bluffé s'il tient). Si le résultat est mitigé, garde a et b.

## 8. Droits et crédits

- **The Rock** : image tirée de sa vidéo Instagram d'octobre 2019 (origine du meme d'après un résumé de recherche citant Daily Dot ; la page de Know Your Meme n'a pas pu être ouverte : à revérifier si tu dois le citer), récupérée sur une version fond vert publiée sur YouTube (`ujqg3jUJ_YI`, « the rock eyebrow raise green screen in 8K », image à 4,0 s, sans doute agrandie). Détourée par incrustation (Pillow et numpy, sans rembg) : `sources/the-rock-sourcil-detoure.png`, l'image d'origine dans `sources/the-rock-fond-vert-ujqg3jUJ_YI-4s.jpg`. Ce n'est pas une image libre : c'est le même risque, faible, que Michael Scott chez OpenCode (meme autorisé par toi).
- **La carte et la RAM** (v2) : dessinées dans la page, sans marque : aucun crédit. Les photos de la 5080 (Inno3D, ta carte, et Founders Edition) restent dans `sources/` pour la v1 seulement.
- **Le logo Strata** (`sources/strata-*.svg`, `strata-icon-512.png`, dépôt Niko1221/Strata, `apps/host/public/brand/`) : trois barres empilées, celle du milieu verte. Il n'est pas utilisé : à 168 px, il se lit comme une icône de menu (≡). Le nom Strata passe dans le titre.

## 9. Ce qu'il faut filmer ou capturer aujourd'hui (pour une version finale plus forte)

Prends des **captures PNG en pleine résolution** (Win + Impr. écran, ou « Capture d'écran » dans OBS), pas des images extraites de la vidéo :

1. **Le mini-Minecraft (P22)**, sans la console ni la barre d'outils du navigateur : une vue à la première personne sur le plus beau coin (relief, lac, arbres), puis une vue en hauteur après quelques sauts. C'est l'objet le plus fort pour un futur test « objet » : le monde en cubes à la place de la carte et de la barrette, en haut à gauche. Neutre aussi pour toutes les cartes, et il montre ce que le modèle fait. Pas de logo Minecraft sur la miniature.
2. **Le moniteur de Strata (P12 à P14)**, au moment où le compteur affiche le tok/s typique : il remplit ⟦tok/s⟧ et prouve le chiffre.
3. **Le jeu (P20)** en pleine action (des étincelles, un bonus qui tombe) et **le haut du site (P21)** : en réserve.
4. **Le mini-Minecraft de Claude (P32)**, au même cadrage que le tien : deux mondes côte à côte pour une variante « duel » si le résultat est parlant.
5. **Tout plantage (P16)** : le message d'erreur en entier. Si le local casse, c'est la meilleure image pour le verdict « K.O. ».
6. **Le Gestionnaire des tâches au plus bas (P15)** : la RAM libre presque à zéro, en réserve pour un texte sur la RAM.

Sur toutes : aucun onglet, aucune clé, aucun dossier personnel à l'écran (règle du plan de tests).

## 10. La v1 (« MA 5080 », abandonnée le 11/11)

- a : « MA 5080 / VS CLAUDE ? », b : « MA 5080 / AU NIVEAU ? », avec la photo de ta 5080 Inno3D en haut à gauche et le même meme. Rendus : [`rendus/v1/`](rendus/v1/) ; maquette : [`propositions/miniature-v1.html`](propositions/miniature-v1.html) ; PSD : [`photocraft/v1/`](photocraft/v1/) ; aperçus : [`apercu/v1/`](apercu/v1/).
- Titres de la v1 : *J'ai fait coder un jeu, un site et une île 3D à mon PC (Strata)* ; *Sans abonnement : mon PC code un jeu, un site et une île 3D*.
- **Pourquoi elle est abandonnée** : « MA 5080 » parle de ta carte, chère et rare, alors que la chaîne vise tous ceux qui ont une carte de 16 Go.
