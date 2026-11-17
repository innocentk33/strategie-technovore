# Portrait nickyoung — provenance

Généré le 16 novembre 2026 avec l'outil intégré image_gen (aucune API externe ni clé locale).

Base demandée : ressources/miniatures/prompts-chatgpt-31-12.md et plan-kai-31-12.md. Pour DeepSeek, le plan prescrit Keanu « whoa », mais aucun fichier reçu n'était présent : portrait recréé dans ce style. Qwen et experts n'avaient pas encore de portrait prescrit ; Nick Young et Sherlock sont des choix de réaction distincts, hors acteurs déjà utilisés.

Référence stylistique locale : projets/cout-claude-local/miniature/sources/michael-vert.png, image existante de la série. Les portraits restent des illustrations de réaction : aucune participation ni recommandation de ces acteurs n'est suggérée.

Image brute : nickyoung-vert.png (1254 × 1254 px réellement livrés par l'outil malgré les 2048 px demandés). Aucun droit ou licence tiers spécifique n'a été vérifié ; aucune photo de presse ou capture de film n'a été téléchargée.

Détourage et habillage : ressources/miniatures/portrait.py. Option --miroir appliquée : l'image générée regardait à droite. Les couleurs de peau restent naturelles en j ; les ombres changent de palette en h.

## Prompt exact

Illustration d'un homme noir athlétique aux cheveux très courts, jeune adulte, en tee-shirt blanc (Nick Young dans le meme « confused »), qui penche légèrement la tête, fronce les sourcils, les lèvres entrouvertes et l'air perplexe, tête et regard vers la gauche de l'image. Cadrage tête et épaules, toute la tête visible, marge 10% au-dessus et aux côtés, coupe seulement en bas. Même style que la référence jointe : peinture numérique à aplats, contours noirs nets, facettes de lumière et d'ombre anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou accessoires. Aucun texte, aucun logo, aucun symbole. Format carré, 2048 × 2048 px, personnage centré. L'image fournie sert seulement de référence stylistique, pas de personnage à copier.

## Reproduction du détourage

```sh
python3 -I ressources/miniatures/portrait.py projets/qwen-27b-8go/miniature/sources/nickyoung-vert.png projets/qwen-27b-8go/miniature/sources nickyoung --miroir
```

