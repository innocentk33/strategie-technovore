# Génération et provenance — artcraft — 19 novembre 2026

Portrait produit avec image_gen intégré (aucune clé API locale). Base de prompt : ressources/miniatures/prompts-chatgpt-31-12.md et skill miniature-kai local.

Image brute : johnwick-vert.png, conservée dans ce dossier avec les trois sorties de portrait.py. L’outil a livré 1254 × 1254 px malgré le format 2048 × 2048 demandé. Référence de personnage : capture locale John Wick, projets/artcraft/miniature/photocraft/john-wick-detoure.png, issue de la bande-annonce officielle de John Wick4 à1:09.6 selon les anciennes propositions. Cette image sert de référence de personnage ; le nouveau rendu est illustré.

Référence stylistique : projets/cout-claude-local/miniature/sources/michael-vert.png, image existante de la série. Les portraits sont des réactions illustrées ; aucune participation, citation ou recommandation des acteurs n’est annoncée. Les memes/visages d’acteurs sont autorisés par le brief de l’auteur.

## Prompt exact

Illustration éditoriale de John Wick, incarné par Keanu Reeves : homme adulte aux cheveux noirs mi-longs, barbe sombre, costume noir et chemise blanche, expression intense, sévère et déterminée, un sourcil un peu froncé, regard vers la gauche de l’image. Cadrage tête et épaules, trois quarts, toute la tête visible, marge 10% au-dessus et sur les côtés, coupe seulement en bas aux épaules. Les images de référence ont deux rôles : image1 Michael uniquement pour le style ; image2 John Wick pour le personnage et sa tenue. Reprendre le style de l’image1 : peinture numérique à aplats, contours noirs nets, facettes de lumière et d’ombre anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif #00FF00 sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou accessoires. Aucun texte, aucun logo, aucun objet, aucune arme. Carré 2048×2048px.

## Détourage reproductible

```sh
python3 -I ressources/miniatures/portrait.py projets/artcraft/miniature/sources/kai-2026-11-19/johnwick-vert.png projets/artcraft/miniature/sources/kai-2026-11-19 johnwick
```

Regard vers la gauche conservé ; pas d’option --miroir. Couleurs de peau gardées dans j. Habillage h : contour blanc et ombres rouge/bleue ; j : contour blanc et ombres Technovore. Les logos sont ajoutés depuis les vrais actifs locaux après génération, sans demander à image_gen de les reproduire.

Sortie originale image_gen : /Users/innocent/.codex/generated_images/01a1e5ab-b1d3-7520-ae68-7d300a61cd35/exec-bf7d2ca1-ee31-4a53-9f19-129534821c38.png ; copie locale pérenne dans ce dossier.

