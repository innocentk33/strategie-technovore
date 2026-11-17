# Portrait — prompt et provenance

Outil intégré `image_gen.imagegen`, génération du 16/11/2026, `transparent_background=false`.
Original copié depuis `/Users/innocent/.codex/generated_images/01a1e5ab-e660-73e1-a36b-d09539ed62e0/exec-6b195e98-17f2-4a1f-9902-691415dca2f3.png` vers `gandalf-vert.png`.

## Prompt utilisé — exact

Use case: stylized-concept. Asset type: portrait illustré pour miniature YouTube. Illustration de Gandalf le Gris dans Le Seigneur des Anneaux, vieux magicien à longue barbe blanche, nez aquilin, cheveux blancs et chapeau pointu gris, robe grise. Il regarde sévèrement et méfiant vers la gauche de l'image, tête de trois quarts, sourcils froncés, bouche fermée comme s'il surveillait un passage. Cadrage tête et épaules, tout le chapeau visible avec une marge autour, buste coupé uniquement en bas. Peinture numérique à aplats, contours noirs nets, facettes de lumière anguleuses, couleurs vives mais peau naturelle, pas de photoréalisme. Fond uni vert vif #00FF00 sans dégradé ni ombre portée. Aucun vert sur le sujet. Aucun texte, aucun logo, aucune main, aucun bâton, aucune scène. Format carré 2048x2048.

## Détourage

`python3 -I ressources/miniatures/portrait.py projets/ia-locale-privee/miniature/sources/gandalf-vert.png projets/ia-locale-privee/miniature/sources/`

L’outil a renvoyé 1254×1254 pixels malgré le format demandé ; la miniature 4K compose ce portrait avec texte vectoriel et scène SVG. Pas de photographie source.
