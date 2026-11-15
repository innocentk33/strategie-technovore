# Prompts ChatGPT des miniatures, jusqu'au 31/12/2026

> 15/11, ta demande : toutes les images qui restent à générer, avec les prompts complets, prêts à copier. Le contexte de chaque vidéo (texte, scène, rechanges) est dans [`plan-kai-31-12.md`](plan-kai-31-12.md).

## Déjà faites

| Image | Vidéo | État |
|---|---|---|
| Fry | 23/11 | dans `meme-carte-plus-rapide/miniature/sources/` (retourné par `--miroir`) |
| M1, les 3 cartes | 26/11 | reçue dans la conversation : à enregistrer en `projets/carte-par-budget/miniature/sources/cartes-vert.png` |
| V1, Keanu | 30/11 | reçue : à enregistrer en `projets/cout-deepseek-flash/miniature/sources/keanu-vert.png` |
| V2, Roll Safe | 3/12 | reçue : à enregistrer en `projets/ram-vram-unifiee/miniature/sources/rollsafe-vert.png` |
| Les 9 ci-dessous | 7/12 → 28/12 | générées le 15/11 ([`generations-31-12.md`](generations-31-12.md)), détourées et maquettées (voir le suivi du plan) |

## Garder le même style d'une image à l'autre

1. Génère tout dans **une seule conversation ChatGPT**.
2. Envoie d'abord ce message, avec **ton image de Keanu en pièce jointe** (pour le matériel, joins plutôt celle des 3 cartes) :

```
Je vais te demander une série d'illustrations pour des miniatures YouTube. Toutes doivent avoir exactement le style de l'image jointe : peinture numérique à aplats, contours noirs nets, facettes de lumière et d'ombre anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Toujours sur un fond uni vert vif (#00FF00), sans dégradé ni ombre portée, sans aucune trace de vert sur le sujet, sans texte ni logo, au format carré 2048 × 2048 px. Réponds seulement « OK » ; les demandes suivent.
```

3. Puis colle les prompts ci-dessous, un par message. Chacun répète l'essentiel du style, au cas où ChatGPT l'oublierait.
4. Si ChatGPT refuse une ressemblance avec une célébrité, renvoie le même prompt sans le nom entre parenthèses : l'expression compte plus que le visage.

**Le sens du regard** : le texte sera à gauche, donc les visages regardent **vers la gauche de l'image**. Si une image arrive dans l'autre sens, ne la refais pas : `portrait.py --miroir` la retourne. Pour les compositions Severance (V6, V9), le visage est **de face, les yeux levés**.

## Les 9 images à générer, dans l'ordre des dates

### V3 · lun. 7/12 · Deux cartes graphiques → `projets/multi-gpu/miniature/sources/boromir-vert.png`

```
Illustration d'un guerrier médiéval aux cheveux mi-longs châtains et à la barbe rousse, cape de fourrure sur les épaules (Boromir dans le meme « one does not simply ») qui explique d'un air grave, une main levée à hauteur du menton, le pouce et l'index joints en cercle. Cadrage tête et épaules, de trois quarts, le regard tourné vers la gauche de l'image, toute la tête visible avec un peu de marge au-dessus. Même style que l'image de référence : peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou ses accessoires. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

### M2 et M3 · jeu. 10/12 · Mac mini ou PC gamer (joins l'image des 3 cartes comme référence de style)

→ `projets/mac-mini-ia/miniature/sources/macmini-vert.png`

```
Illustration d'un petit ordinateur de bureau carré et plat en aluminium argenté, aux coins arrondis, avec deux ports ronds et une petite fente sur la face avant (type Mac mini), sans logo, vu de trois quarts face, légèrement de dessus. Même style que l'image de référence : illustration à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune LED, aucun logo ni aucune pièce de couleur verte. Aucun texte. Format carré, 2048 × 2048 px, l'objet bien centré avec de la marge autour.
```

→ `projets/mac-mini-ia/miniature/sources/pcgamer-vert.png`

```
Illustration d'une grosse tour de PC gamer avec une paroi vitrée, éclairée de l'intérieur en rouge et en violet, une carte graphique à trois ventilateurs visible à l'intérieur, sans logo de marque, vue de trois quarts face. Même style que l'image de référence : illustration à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune LED, aucun logo ni aucune pièce de couleur verte. Aucun texte. Format carré, 2048 × 2048 px, l'objet bien centré avec de la marge autour.
```

### V4 · lun. 14/12 · Coût de Kimi (fusionnée dans Coût de Claude le 15/11 : rechange de V9) → `projets/cout-claude-local/miniature/sources/krabs-vert.png`

```
Illustration de M. Krabs, le crabe rouge de Bob l'éponge, qui sourit, les yeux brillants d'avidité, les pinces serrées l'une contre l'autre comme s'il comptait son argent. Garde son allure de dessin animé, avec le même traitement que l'image de référence : contours noirs nets, aplats, facettes de lumière anguleuses, couleurs vives. Cadrage tête et pinces, de trois quarts, le regard tourné vers la gauche de l'image, toute la tête visible avec un peu de marge au-dessus. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas sous les pinces.
```

### V5 · jeu. 17/12 · Prix après le Black Friday → `projets/prix-apres-black-friday/miniature/sources/jim-vert.png`

```
Illustration d'un grand homme brun aux cheveux courts en bataille, en chemise blanche et cravate de bureau (Jim Halpert dans la série The Office) qui fixe le spectateur, un sourcil levé, l'air blasé et sceptique, les lèvres pincées. Cadrage tête et épaules, de trois quarts, la tête tournée vers la gauche de l'image et les yeux vers le spectateur, toute la tête visible avec un peu de marge au-dessus. Même style que l'image de référence : peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou ses accessoires. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

### V6 · lun. 21/12 · Le nom d'un modèle · Severance → `projets/bases-ia-locale/miniature/sources/mathlady-vert.png`

```
Illustration d'une femme blonde d'âge mûr, aux cheveux mi-longs coiffés, maquillée (la « Math Lady » du meme, Renata Sorrah) qui plisse les yeux, perdue et concentrée, comme devant un calcul impossible. Cadrage tête et épaules, de face, le visage bien droit, les yeux levés vers le haut de l'image, toute la tête visible avec de la marge au-dessus, aucune main au-dessus des sourcils. Même style que l'image de référence : peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou ses accessoires. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

### V7 · jeu. 24/12 · Le cadeau IA locale → `projets/cadeau-ia-locale/miniature/sources/bean-vert.png`

```
Illustration d'un homme aux cheveux bruns courts, en veste de tweed marron et cravate fine (Mr Bean) qui sourit de toutes ses dents, ravi, en serrant contre lui un petit paquet cadeau rouge avec un ruban blanc. Cadrage tête et épaules avec le paquet visible, de trois quarts, le regard tourné vers la gauche de l'image, toute la tête visible avec un peu de marge au-dessus. Même style que l'image de référence : peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou le paquet. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas sous le paquet.
```

### V8 · lun. 28/12 · Louer, acheter ou s'abonner → `projets/louer-acheter-ia/miniature/sources/drake-vert.png`

```
Illustration d'un rappeur barbu aux cheveux très courts, en doudoune orange (le meme de Drake, image du haut) qui détourne la tête avec une grimace de refus, une main levée paume ouverte devant lui. Cadrage tête et épaules, de trois quarts, la tête tournée vers la droite de l'image comme s'il refusait ce qui est à gauche, la main levée du côté gauche, toute la tête visible avec un peu de marge au-dessus. Même style que l'image de référence : peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage ou ses vêtements. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

Drake est l'exception : il refuse le texte (« TU PAIES TROP ? »), donc il s'en détourne, la main levée vers lui.

La première image touchait le bord gauche. Elle a été régénérée le 15/11 avec de la marge sur les côtés (`drake-vert-dezoome.png`, prompt dans le `.json` à côté) : si tu refais un portrait, demande toujours une marge à gauche et à droite, avec une coupe seulement en bas.

### V9 · lun. 14/12 (au lieu du jeu. 31/12, 15/11) · Coût de Claude Fable 5.2 · Severance → `projets/cout-claude-local/miniature/sources/michael-vert.png`

```
Illustration d'un homme brun d'une quarantaine d'années aux cheveux courts coiffés sur le côté, en costume gris et cravate de bureau (Michael Scott dans la série The Office) horrifié, les yeux écarquillés, les sourcils très relevés, la bouche ouverte. Cadrage tête et épaules, de face, le visage bien droit, les yeux levés vers le haut de l'image, toute la tête visible avec de la marge au-dessus, aucune main au-dessus des sourcils. Même style que l'image de référence : peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou ses accessoires. Aucun texte, aucun logo. Format carré, 2048 × 2048 px, le personnage bien centré, coupé en bas au niveau des épaules.
```

## Après la génération

Dépose chaque image à son chemin ; je la détoure (`portrait.py`, avec `--miroir` si elle regarde du mauvais côté, `--coupe` pour V6 et V9) et je fais les 3 miniatures de la vidéo. Les dossiers `miniature/sources/` qui n'existent pas encore peuvent être créés par toi ou par moi.
