---
name: miniature-kai
description: Les 3 miniatures Technovore « à la manière de Kai » (h, i, j) d'une vidéo : h = palette de Kai + visage illustré, i = couleurs de Technovore sans visage, j = couleurs de Technovore + visage. Maquette HTML, portrait illustré généré avec ChatGPT et détouré par portrait.py, rendu 4K, PSD, test à 168 px, test A/B. À utiliser dès qu'on prépare les miniatures d'une nouvelle vidéo, qu'on parle du style de Kai, ou qu'il faut un portrait illustré pour une miniature.
---

# Miniatures à la manière de Kai (h, i, j)

Méthode mise au point sur Strata le 14 et le 15/11/2026, en test A/B sur sa vidéo (h, i, j, lancé le 15/11). Modèle de départ : [`projets/strata-test/miniature/propositions/miniature-kai.html`](../../../projets/strata-test/miniature/propositions/miniature-kai.html) ; premier réemploi : [`projets/meme-carte-plus-rapide/miniature/`](../../../projets/meme-carte-plus-rapide/miniature/). Les règles communes restent celles de `.claude/rules/miniatures.md` (moitié haute, zone de la durée, 4K, jamais la même info que le titre, faits tenus par la vidéo).

## Ce qu'on reprend de Kai, et ce qu'on ne copie pas

Kai (`etudes/kai.md` § 4.3, `ressources/miniatures/concurrents/kai.jpg`) :
- fond sombre et calme (pas de code ni de texture chargée) ;
- **un seul mot en couleur**, avec sa copie décalée en bas à droite (0,055 em) ; le mot blanc n'en a pas ;
- une police large : **Archivo Black** (`ressources/miniatures/fonts/`), pas Anton ;
- objets dessinés à plat, contour noir épais, **ombres décalées** (rouge puis bleu chez Kai) ; tuiles de logos inclinées ;
- un **visage illustré**, cerné de blanc, à gauche, et le texte à droite.

On ne copie jamais : ses scènes (la patate tenue par une main, la tête ouverte, la flèche Claude → carte), ses visages, sa signature `<kaiexplainsyt>`. Chaque vidéo a son objet à elle (Strata : la carte et Qwen VS Claude ; « même carte » : la carte et un compteur de vitesse).

## Les trois variantes

| | Palette | Visage | Mise en page |
|---|---|---|---|
| **h** | Kai : noir, blanc, jaune `#ffcc33`, ombres rouge `#ff3b30` et bleue `#2f6bff` | `portrait-kai.png` | visage à gauche, 2 lignes à droite, l'objet sous le texte |
| **i** | Technovore : fond ardoise (`#3d566e` → `#1a252f`) avec une grille discrète, menthe `#07c095`, ombres blanche et ardoise foncée | aucun | texte sur une seule ligne en haut, centré ; la scène en grand dessous |
| **j** | Technovore | `portrait-technovore.png` : **couleurs de peau gardées** | comme h |

Lecture du test : h contre j = la palette ; i contre j = le visage.

**Visage dans j** : jamais de duotone ardoise et menthe (essayé le 14/11 : pas de contraste, le visage ne se détache pas). Le visage garde sa peau ; ce sont le contour blanc épais, l'ombre menthe, l'ombre ardoise et un halo sombre qui le détachent du fond.

## Étapes

1. **Le texte** : 2 à 4 mots, une question ou un mot choc, qui dit le problème quand le titre dit le gain (Strata : « TON PC / SUFFIT ? » ; même carte : « TA CARTE / BRIDÉE ? »). Le mot en couleur est le second. Il doit être tenu par la vidéo : vérifie dans le script ou la fiche, sinon signale-le.
2. **Le portrait** : demande-le à l'auteur, à générer avec ChatGPT (prompt ci-dessous). Il le dépose dans `projets/<nom>/miniature/sources/`, puis :
   `python3 -I ressources/miniatures/portrait.py <image fond vert> projets/<nom>/miniature/sources/`
   → `portrait-illustre-detoure.png`, `portrait-kai.png`, `portrait-technovore.png`. Vérifie qu'il ne reste aucun pixel vert sur le rendu. En attendant le portrait, on peut maquetter avec celui de Strata, marqué « provisoire ».
3. **La maquette** : copie `miniature-kai.html` du dernier projet dans `projets/<nom>/miniature/propositions/`, change l'en-tête, `#l1` / `#l2` et les trois groupes de la scène (`.duel` pour h, `.duo` pour i, `.solo` pour j). Les objets (`#card`, `#fan`, `#tq`, `#tc`, `#tag`, `#gauge`) prennent les couleurs de la variante par `var(--card)`, `var(--sh1)`, `var(--sh2)`. La taille du texte s'ajuste seule à la place disponible.
4. **Le rendu** : un `rendre.sh` dans le dossier (modèle : celui de `meme-carte-plus-rapide`) → `rendus/h-kai.png`, `i-kai.png`, `j-kai.png` en 3840×2160.
5. **Le contrôle** : planche à 168 px et test des 50 % (moitié basse cachée) dans `apercu/test-50-et-168px-kai.png` ; rien dans le coin de la durée (x > 1130, y > 650 à 1x) ; le visage regarde vers le texte.
6. **Le PSD** : `python3 -I ressources/miniatures/psd.py --page projets/<nom>/miniature/propositions/miniature-kai.html "v=h" projets/<nom>/miniature/photocraft/h-kai.psd` (idem i et j ; 3 calques de texte chacun).
7. **La trace** : `projets/<nom>/miniature/propositions.md` (texte, scène, ce qui est tenu par la vidéo, droits du visage, test proposé), puis le test A/B h, i, j dans « Tester et comparer » à l'upload (le skill `upload` le reporte dans `upload.md`).

## Le prompt du portrait (ChatGPT)

**Le visage vient d'un meme connu ou d'un personnage connu** (règle de l'auteur, 15/11) : il a rejeté un « jeune joueur » générique. Choisis le meme dont l'émotion colle au texte (doute → Fry de Futurama qui plisse les yeux, The Rock au sourcil levé ; reconnaissance → DiCaprio qui pointe du doigt ; complicité → Jim Halpert qui regarde la caméra…), et pas celui de la vidéo précédente. Propose 2 ou 3 memes à l'auteur avant de lui donner le prompt.

Adapte le personnage et l'expression, garde le reste :

```
Illustration d'un [personnage du meme, décrit : homme chauve et musclé (The Rock) / jeune homme roux aux yeux plissés, style dessin animé (Fry) / …] qui [expression : lève un sourcil, l'air sceptique / écarquille les yeux, choqué / …]. Cadrage tête et épaules, de trois quarts, le regard tourné vers la droite de l'image. Style illustration éditoriale, comme une peinture numérique à aplats : contours nets, ombres franches, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

Si ChatGPT refuse une ressemblance avec une célébrité, retire la référence au meme : l'émotion compte plus que le visage. Les memes et visages d'acteurs sont autorisés par l'auteur ; « faceless » veut dire seulement sans le visage de l'auteur.
