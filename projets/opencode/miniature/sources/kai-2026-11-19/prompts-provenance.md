# Génération et provenance — opencode — 19 novembre 2026

Portrait produit avec image_gen intégré (aucune clé API locale). Base de prompt : ressources/miniatures/prompts-chatgpt-31-12.md et skill miniature-kai local.

Image brute : kevinhart-vert.png, conservée dans ce dossier avec les trois sorties de portrait.py. L’outil a livré 1254 × 1254 px malgré le format 2048 × 2048 demandé. Personnage demandé : Kevin Hart dans une réaction de meme sidérée, sans réutiliser une photo de presse.

Référence stylistique : projets/cout-claude-local/miniature/sources/michael-vert.png, image existante de la série. Les portraits sont des réactions illustrées ; aucune participation, citation ou recommandation des acteurs n’est annoncée. Les memes/visages d’acteurs sont autorisés par le brief de l’auteur.

## Prompt exact

Illustration d’un homme noir adulte aux cheveux noirs très courts et à la barbe courte (Kevin Hart, réaction de meme sidérée), les sourcils très relevés, les yeux écarquillés, bouche légèrement ouverte, l’air de découvrir une facture ou un vol incompréhensible. Vêtement noir simple. Cadrage tête et épaules, de trois quarts avec la tête et le regard vers la gauche de l’image. Toute la tête visible et marge de 10% au-dessus et sur les côtés ; coupe seulement en bas aux épaules. Référence fournie uniquement pour le style, ne pas reprendre son personnage : peinture numérique à aplats, contours noirs nets, facettes de lumière et d’ombre anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif #00FF00 sans dégradé ni ombre portée. Aucune trace de vert sur le personnage ni les vêtements. Aucun texte, aucun logo, aucun objet. Carré 2048×2048px.

## Détourage reproductible

```sh
python3 -I ressources/miniatures/portrait.py projets/opencode/miniature/sources/kai-2026-11-19/kevinhart-vert.png projets/opencode/miniature/sources/kai-2026-11-19 kevinhart
```

Regard vers la gauche conservé ; pas d’option --miroir. Couleurs de peau gardées dans j. Habillage h : contour blanc et ombres rouge/bleue ; j : contour blanc et ombres Technovore. Les logos sont ajoutés depuis les vrais actifs locaux après génération, sans demander à image_gen de les reproduire.

Sortie originale image_gen : /Users/innocent/.codex/generated_images/01a1e5ab-b1d3-7520-ae68-7d300a61cd35/exec-d0eadaa0-0992-4782-91f4-ef78290b72de.png ; copie locale pérenne dans ce dossier.

