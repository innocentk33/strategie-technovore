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

On ne copie jamais : ses scènes (la patate tenue par une main, sa tête ouverte d'où sortent des objets, la flèche Claude → carte), ses visages, sa signature `<kaiexplainsyt>`. La composition « Severance » ci-dessous est autre chose : une coupe nette, façon affiche, demandée par l'auteur le 15/11. Chaque vidéo a son objet à elle (Strata : la carte et Qwen VS Claude ; « même carte » : la carte et un compteur de vitesse).

## Les trois variantes

| | Palette | Visage | Mise en page |
|---|---|---|---|
| **h** | Kai : noir, blanc, jaune `#ffcc33`, ombres rouge `#ff3b30` et bleue `#2f6bff` | `portrait-kai.png` | **texte à gauche** (2 lignes), visage à droite tourné vers lui ; ou texte sur une ligne en haut, selon la vidéo |
| **i** | Technovore : fond sombre et uni `#141e27` (depuis le 15/11 ; avant, ardoise en dégradé avec une grille), menthe `#07c095`, ombres blanche et `#34495e` | aucun | texte sur une seule ligne en haut, centré ; la scène en grand dessous |
| **j** | Technovore | `portrait-technovore.png` : **couleurs de peau gardées** | comme h |

Lecture du test : h contre j = la palette ; i contre j = le visage.

**Plan jusqu'au 31/12** (décision de l'auteur, 15/11) : toutes les vidéos ont leurs h, i, j et un test A/B à 3. Les textes, les visages et le suivi sont dans [`ressources/miniatures/plan-kai-31-12.md`](../../../ressources/miniatures/plan-kai-31-12.md), les prompts complets dans [`prompts-chatgpt-31-12.md`](../../../ressources/miniatures/prompts-chatgpt-31-12.md) (une seule conversation ChatGPT, une image déjà faite jointe comme référence de style). Tiens-le à jour à chaque miniature faite. Pour ces vidéos, une seule maquette : [`ressources/miniatures/propositions/kai-31-12.html`](../../../ressources/miniatures/propositions/kai-31-12.html)`?d=<projet>&v=h|i|j` ; une nouvelle vidéo = une entrée de plus dans son objet `V` (textes, mise en page `gauche`, `materiel` ou `severance`, scènes h/j et i). Severance : `--coupe 0.21` sur une tête avec des cheveux.

**Vidéo de matériel pur** (Mac mini, cartes par budget…) : pas de visage. Une illustration du matériel, générée avec ChatGPT sur fond vert et détourée par `portrait.py`, prend la place du visage dans h et j. i garde sa scène à plat.

**Le texte d'abord** (auteur, 15/11) : on lit de gauche à droite, donc le texte va **à gauche ou en haut**, jamais à droite d'un visage. Le visage regarde le texte (prompt « regard vers la gauche », ou `portrait.py --miroir`). Strata et le 19/11 avaient encore le visage à gauche.

**Ombre blanche** (auteur, 15/11) : en Technovore (i, j), la copie décalée du mot en couleur est blanche (`--echo:#ffffff`), sans contour. Un contour blanc (`-webkit-text-stroke`) a été essayé et écarté.

**Composition « Severance »** (option pour certaines vidéos, pas pour toutes ; version de l'auteur, 15/11 ; références : `ressources/miniatures/images/reference-tete-ouverte-kai.webp`, `reference-tete-en-bas.jpg`, `reference-tete-anneau.jpg` ; prototype : `ressources/miniatures/propositions/severance-prototype.html` et `images/prototype-severance.png`) :
- le visage est de face, en très grand, centré, coupé en bas sous les yeux, le regard levé ; le texte tient sur une ligne en haut ;
- `portrait.py … --coupe 0.17` ouvre la tête (ovale sombre) et sort aussi un calque `-devant` (bord avant et visage). Dans la maquette, l'ordre est : portrait `-coupe-*.png`, puis le SVG des objets, puis `-coupe-*-devant.png` par-dessus ; les objets ont l'air dans la tête ;
- 1 à 3 gros objets, qui débordent vers le haut ;
- le portrait se génère de face, les yeux levés, sans main au-dessus des sourcils (prompts V6 et V9 de `prompts-chatgpt-31-12.md`) ;
- c'est la composition de la miniature « Don't overpay » de Kai, demandée par l'auteur : on reprend l'idée, pas son visage, ses lunettes ni sa signature.

**Fond de Technovore (i et j)**, 15/11, demande de l'auteur : sombre et uni (`#141e27`), sans grille ni dégradé, pour plus de contraste. Ombre décalée du mot menthe : blanche (l'ardoise foncée disparaît sur ce fond). Ombres des objets : blanche et `#34495e`.

## Étapes

1. **Le texte** : 2 à 4 mots, une question ou un mot choc, qui dit le problème quand le titre dit le gain (Strata : « TON PC / SUFFIT ? » ; même carte : « TA CARTE / BRIDÉE ? »). Le mot en couleur est le second. Il doit être tenu par la vidéo : vérifie dans le script ou la fiche, sinon signale-le.
2. **Le portrait** : demande-le à l'auteur, à générer avec ChatGPT (prompt ci-dessous). Il le dépose dans `projets/<nom>/miniature/sources/`, puis :
   `python3 -I ressources/miniatures/portrait.py <image fond vert> projets/<nom>/miniature/sources/`
   → `portrait-illustre-detoure.png`, `portrait-kai.png`, `portrait-technovore.png`. Avec plusieurs visages, ajoute un nom en 3e argument (`… sources/ fry` → `portrait-fry-kai.png`…) et choisis-le dans la maquette par `?p=fry` (modèle : `meme-carte-plus-rapide`). Vérifie qu'il ne reste aucun pixel vert sur le rendu. En attendant le portrait, on peut maquetter avec celui de Strata, marqué « provisoire ».
3. **La maquette** : copie `miniature-kai.html` du dernier projet dans `projets/<nom>/miniature/propositions/`, change l'en-tête, `#l1` / `#l2` et les trois groupes de la scène (`.duel` pour h, `.duo` pour i, `.solo` pour j). Les objets (`#card`, `#fan`, `#tq`, `#tc`, `#tag`, `#gauge`) prennent les couleurs de la variante par `var(--card)`, `var(--sh1)`, `var(--sh2)`. La taille du texte s'ajuste seule à la place disponible.
4. **Le rendu** : un `rendre.sh` dans le dossier (modèle : celui de `meme-carte-plus-rapide`) → `rendus/h-kai.png`, `i-kai.png`, `j-kai.png` en 3840×2160.
5. **Le contrôle** : planche à 168 px et test des 50 % (moitié basse cachée) dans `apercu/test-50-et-168px-kai.png` ; rien dans le coin de la durée (x > 1130, y > 650 à 1x) ; le visage regarde vers le texte, qui est à gauche ou en haut.
6. **Le PSD** : `python3 -I ressources/miniatures/psd.py --page projets/<nom>/miniature/propositions/miniature-kai.html "v=h" projets/<nom>/miniature/photocraft/h-kai.psd` (idem i et j ; 3 calques de texte chacun).
7. **La trace** : `projets/<nom>/miniature/propositions.md` (texte, scène, ce qui est tenu par la vidéo, droits du visage, test proposé), puis le test A/B h, i, j dans « Tester et comparer » à l'upload (le skill `upload` le reporte dans `upload.md`).

## Le prompt du portrait (ChatGPT)

**Le visage vient d'un meme connu ou d'un personnage connu** (règle de l'auteur, 15/11) : il a rejeté un « jeune joueur » générique. Choisis le meme dont l'émotion colle au texte (doute → Fry de Futurama qui plisse les yeux, The Rock au sourcil levé ; reconnaissance → DiCaprio qui pointe du doigt ; complicité → Jim Halpert qui regarde la caméra…), et pas celui de la vidéo précédente. Propose 2 ou 3 memes à l'auteur avant de lui donner le prompt.

Adapte le personnage et l'expression, garde le reste :

```
Illustration d'un [personnage du meme, décrit : homme chauve et musclé (The Rock) / jeune homme roux aux yeux plissés, style dessin animé (Fry) / …] qui [expression : lève un sourcil, l'air sceptique / écarquille les yeux, choqué / …]. Cadrage tête et épaules, de trois quarts, le regard tourné vers la gauche de l'image. Style illustration éditoriale, comme une peinture numérique à aplats : contours nets, ombres franches, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou ses accessoires. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

Le détourage mange tout ce qui est vert (`(g>r+60)&(g>b+60)`) : jamais de personnage vert (le Grinch, Shrek), ni de LED ou de logo vert sur le matériel. On écarte aussi les enfants acteurs et les personnalités politiques.

Si ChatGPT refuse une ressemblance avec une célébrité, retire la référence au meme : l'émotion compte plus que le visage. Les memes et visages d'acteurs sont autorisés par l'auteur ; « faceless » veut dire seulement sans le visage de l'auteur.
