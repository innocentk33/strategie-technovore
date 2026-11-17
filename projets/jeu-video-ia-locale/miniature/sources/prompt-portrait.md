# Portrait — prompt et provenance

Outil intégré `image_gen.imagegen`, génération du 16/11/2026, `transparent_background=false`.
Original copié depuis `/Users/innocent/.codex/generated_images/01a1e5ab-e660-73e1-a36b-d09539ed62e0/exec-4d1a9cf2-28c5-4e24-94a9-5a84ed6abb8b.png` vers `cage-vert.png`.

## Prompt utilisé — exact

Use case: stylized-concept. Asset type: portrait illustré pour miniature YouTube. Portrait de Nicolas Cage dans le meme « You don't say », homme blanc d'âge mûr aux cheveux bruns courts et front dégagé, sourcils très relevés, yeux grands ouverts, sourire crispé incrédule, il regarde vers la gauche de l'image avec une expression de surprise sceptique. Tête de trois quarts, chemise bleu foncé. Cadrage tête et épaules, tête entière avec marge généreuse autour, coupé seulement en bas. Peinture numérique éditoriale à aplats, contours noirs nets, facettes de lumière et d'ombre anguleuses, couleurs vives mais peau naturelle, pas de photoréalisme. Fond entièrement uni vert vif #00FF00, aucun dégradé ni ombre portée. Aucune trace de vert sur le personnage. Aucun texte ni logo. Format carré 2048x2048.

## Détourage

`python3 -I ressources/miniatures/portrait.py projets/jeu-video-ia-locale/miniature/sources/cage-vert.png projets/jeu-video-ia-locale/miniature/sources/`

L’outil a renvoyé 1254×1254 pixels malgré le format demandé ; la miniature 4K compose ce portrait avec texte vectoriel et scène SVG. Pas de photographie source.

La première demande Mario a été rejetée par le filtre automatique de génération (catégorie other, étape output). Remplacement par le meme Nicolas Cage ; aucun contournement du refus.
