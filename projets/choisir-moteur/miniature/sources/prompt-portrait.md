# Portrait — prompt et provenance

Outil intégré `image_gen.imagegen`, génération du 16/11/2026, `transparent_background=false`.
Original copié depuis `/Users/innocent/.codex/generated_images/01a1e5ab-e660-73e1-a36b-d09539ed62e0/exec-a4e956ec-422f-41fa-8c07-2fbb4262a804.png` vers `travolta-vert.png`.

## Prompt utilisé — exact

Use case: stylized-concept. Asset type: portrait illustré pour miniature YouTube. Illustration de Vincent Vega (John Travolta dans le meme « confused Travolta » de Pulp Fiction), homme blanc aux cheveux noirs mi-longs peignés en arrière, costume noir, chemise blanche et fine cravate noire. Il paraît perdu et indécis, sourcils froncés, lèvres légèrement entrouvertes, la tête de trois quarts tournée vers la gauche de l'image et les yeux cherchant une réponse à gauche. Cadrage tête et épaules sans mains, toute la tête visible avec marge généreuse sur les côtés et en haut, coupé seulement en bas. Peinture numérique à aplats, contours noirs nets, facettes de lumière et d'ombre anguleuses, couleurs vives mais peau naturelle, pas de photoréalisme. Fond uni vert vif #00FF00 sans dégradé ni ombre portée. Aucune trace de vert sur le personnage ou les vêtements. Aucun texte, aucun logo. Format carré 2048x2048.

## Détourage

`python3 -I ressources/miniatures/portrait.py projets/choisir-moteur/miniature/sources/travolta-vert.png projets/choisir-moteur/miniature/sources/`

L’outil a renvoyé 1254×1254 pixels malgré le format demandé ; la miniature 4K compose ce portrait avec texte vectoriel et scène SVG. Pas de photographie source.
