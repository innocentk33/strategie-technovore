# Les 33 miniatures Technovore

Série du 16 novembre 2026 : trois variantes pour chacune des onze vidéos demandées, dans la charte `miniature-kai`, d’après la base de prompts du projet.

[Ouvrir la galerie](index.html) · [Plan de production](PLAN.md) · [Planche à 168 px](planche-168px.png)

La galerie propose les PNG 4K, les PSD, les concepts et les critiques indépendantes. Le bouton « Tester à 168 px » affiche les images à leur taille mobile. Les fichiers sont aussi accessibles dans chaque dossier `projets/<nom>/miniature/` et détectés par la régie.

**Correction des logos, 16/11 :** les variantes de Qwen, DeepSeek, Claude Code et « TON IA / 3 OUTILS » utilisent maintenant les véritables logos. Le texte et les tuiles des trois moteurs sont séparés par une marge visible. Les sources de marque sont conservées dans chaque projet et dans la [bibliothèque de logos](../logos/README.md). La [planche dédiée](planche-logos.jpg) rassemble ces douze variantes.

| Vidéo | Accroche | Sources et critique |
|---|---|---|
| Qwen 27B sur 8 Go | 8 GO / ÇA RENTRE ? | [Concept](../../../projets/qwen-27b-8go/miniature/propositions.md) · [Critique](../../../projets/qwen-27b-8go/miniature/critique-independante.md) |
| Carte graphique par budget | PAYER PLUS / POUR RIEN ? | [Concept](../../../projets/carte-par-budget/miniature/propositions.md) · [Critique](../../../projets/carte-par-budget/miniature/critique-independante.md) |
| DeepSeek sans carte graphique | ET LA / QUALITÉ ? | [Concept](../../../projets/cout-deepseek-flash/miniature/propositions.md) · [Critique](../../../projets/cout-deepseek-flash/miniature/critique-independante.md) |
| RAM, VRAM ou mémoire unifiée | LA RAM / TROP LENTE ? | [Concept](../../../projets/ram-vram-unifiee/miniature/propositions.md) · [Critique](../../../projets/ram-vram-unifiee/miniature/critique-independante.md) |
| Claude Code avec une IA locale | LE MÊME / CERVEAU ? | [Concept](../../../projets/claude-code-gratuit/miniature/propositions.md) · [Critique](../../../projets/claude-code-gratuit/miniature/critique-independante.md) |
| IA locale et confidentialité | TES DONNÉES / SORTENT ? | [Concept](../../../projets/ia-locale-privee/miniature/propositions.md) · [Critique](../../../projets/ia-locale-privee/miniature/critique-independante.md) |
| Créer un petit jeu localement | UN JEU / COMPLET ? | [Concept](../../../projets/jeu-video-ia-locale/miniature/propositions.md) · [Critique](../../../projets/jeu-video-ia-locale/miniature/critique-independante.md) |
| Modèle par VRAM | TON MODÈLE / RENTRE ? | [Concept](../../../projets/modele-par-vram/miniature/propositions.md) · [Critique](../../../projets/modele-par-vram/miniature/critique-independante.md) |
| Cartes de minage | BONNE / AFFAIRE ? | [Concept](../../../projets/cartes-minage/miniature/propositions.md) · [Critique](../../../projets/cartes-minage/miniature/critique-independante.md) |
| Ollama, LM Studio ou llama.cpp | TON IA / 3 OUTILS | [Concept](../../../projets/choisir-moteur/miniature/propositions.md) · [Critique](../../../projets/choisir-moteur/miniature/critique-independante.md) |
| Petits modèles experts | PETIT / MAIS FORT ? | [Concept](../../../projets/petits-modeles-experts/miniature/propositions.md) · [Critique](../../../projets/petits-modeles-experts/miniature/critique-independante.md) |

## Fichiers modifiables

- `rendus/{h,i,j}-kai.png` : PNG 3840 × 2160.
- `photocraft/{h,i,j}-kai.psd` : décor composé et textes principaux modifiables en calques PhotoCraft. Les scènes ne sont pas entièrement décomposées en calques PSD.
- `propositions/miniature-kai.html` : composition HTML/CSS/SVG, avec `?v=h`, `?v=i` ou `?v=j`.
- `sources/` : illustrations originales générées, détourages et habillages. Les prompts exacts sont conservés dans le projet.
- `rendre.sh` : reproduction du rendu ; les options propres au projet figurent dans `propositions.md`.
- `apercu/` : comparaisons, tests à 168 px et moitié basse masquée, contrôles d’export.

Les illustrations manquantes ont été générées avec l’outil intégré `image_gen`, en reprenant les aplats, les contours noirs, le fond vert et le cadrage de la base utilisateur. Les scènes schématiques utilisent les objets SVG de la charte et leurs adaptations. PhotoCraft CLI a produit les PSD.

## Relecture et test public

Chaque variante est critiquée par un agent GPT‑6.1 Sol, effort élevé, distinct de son producteur. Les réserves, corrections et versions relues sont consignées dans les onze critiques. Les avis de préférence sont des hypothèses, pas des prédictions de CTR.

h/j comparent les palettes à scène conservée. i propose une scène sans portrait et change aussi sa composition : i/j ne mesure donc pas exclusivement l’effet d’un visage. Aucun test YouTube ni publication n’a été lancé.
