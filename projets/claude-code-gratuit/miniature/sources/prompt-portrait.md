# Portrait — prompt et provenance

Outil intégré `image_gen.imagegen`, génération du 16/11/2026, `transparent_background=false`.
Original copié depuis `/Users/innocent/.codex/generated_images/01a1e5ab-e660-73e1-a36b-d09539ed62e0/exec-b0179c3c-ca94-4a9a-a5a6-bae803db2560.png` vers `morpheus-vert.png`.

## Prompt utilisé — exact

Use case: stylized-concept. Asset type: portrait découpable pour miniature YouTube. Illustration de Morpheus dans Matrix, homme noir chauve en manteau noir et petites lunettes de soleil ovales noires, expression très sérieuse et interrogative, un sourcil légèrement levé, tête tournée de trois quarts vers la gauche de l'image. Cadrage tête et épaules, toute la tête visible, marge généreuse au-dessus et sur les côtés, coupé seulement en bas sous les épaules. Peinture numérique à aplats, contours noirs nets, facettes de lumière et d'ombre anguleuses, couleurs vives mais peau naturelle, pas de photoréalisme. Fond entièrement uni vert vif #00FF00, aucun dégradé, aucune ombre portée. Aucune trace de vert sur le personnage, ses lunettes ou vêtements. Aucun texte ni logo. Format carré 2048x2048. Image d'un seul personnage, sans autres objets.

## Détourage

`python3 -I ressources/miniatures/portrait.py projets/claude-code-gratuit/miniature/sources/morpheus-vert.png projets/claude-code-gratuit/miniature/sources/`

L’outil a renvoyé 1254×1254 pixels malgré le format demandé ; la miniature 4K compose ce portrait avec texte vectoriel et scène SVG. Pas de photographie source.
