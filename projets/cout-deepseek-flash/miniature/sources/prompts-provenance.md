# Portrait keanu — provenance

Généré le 16 novembre 2026 avec l'outil intégré image_gen (aucune API externe ni clé locale).

Base demandée : ressources/miniatures/prompts-chatgpt-31-12.md et plan-kai-31-12.md. Pour DeepSeek, le plan prescrit Keanu « whoa », mais aucun fichier reçu n'était présent : portrait recréé dans ce style. Qwen et experts n'avaient pas encore de portrait prescrit ; Nick Young et Sherlock sont des choix de réaction distincts, hors acteurs déjà utilisés.

Référence stylistique locale : projets/cout-claude-local/miniature/sources/michael-vert.png, image existante de la série. Les portraits restent des illustrations de réaction : aucune participation ni recommandation de ces acteurs n'est suggérée.

Image brute : keanu-vert.png (1254 × 1254 px réellement livrés par l'outil malgré les 2048 px demandés). Aucun droit ou licence tiers spécifique n'a été vérifié ; aucune photo de presse ou capture de film n'a été téléchargée.

Détourage et habillage : ressources/miniatures/portrait.py. Regard généré vers la gauche, conservé. Les couleurs de peau restent naturelles en j ; les ombres changent de palette en h.

## Prompt exact

Illustration d'un homme brun aux cheveux mi-longs et à la barbe brune courte, en veste noire (Keanu Reeves dans le meme « whoa »), qui ouvre légèrement la bouche, les yeux écarquillés, l'air surpris et incrédule. Cadrage tête et épaules, de trois quarts, regard vers la gauche de l'image, toute la tête visible avec marge 10% au-dessus et sur les côtés, coupe seulement en bas. Même style que la référence jointe : peinture numérique à aplats, contours noirs nets, facettes de lumière et d'ombre anguleuses, couleurs vives mais naturelles, pas de photoréalisme. Fond uni vert vif (#00FF00), sans dégradé ni ombre portée. Aucune trace de vert sur le personnage, ses vêtements ou accessoires. Aucun texte, aucun logo, aucun symbole. Format carré, 2048 × 2048 px, personnage centré. L'image fournie sert seulement de référence stylistique, pas de personnage à copier.

## Reproduction du détourage

```sh
python3 -I ressources/miniatures/portrait.py projets/cout-deepseek-flash/miniature/sources/keanu-vert.png projets/cout-deepseek-flash/miniature/sources keanu
```

