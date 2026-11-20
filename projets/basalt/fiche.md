# Basalt peut-il accélérer Qwen sur ton PC ?

**Sortie prévue le jeudi 3 décembre 2026 à 18 h (Paris).** Titre de travail.

Après la vidéo sur les 32 Go pour Qwen 27B, la question change. Quand le modèle tient sur la machine, que peut apporter un autre moteur d’inférence ? Le sujet porte ici sur Qwen 3.8 Flash Next avec Basalt.

## Références pour préparer la vidéo

- [Basalt: The Strata Fork Hitting 500 Tokens/s on One Gaming PC](https://www.youtube.com/watch?v=-tQJ7NlQkdo)
- [Basalt Runs Qwen 3.8 Flash Next At 224 Token/sec](https://www.youtube.com/watch?v=wC6jsOU4jII)

## Chiffres des miniatures

- **500 tokens/s ?** H et J reprennent le titre d’AgenticEngineering. À 6 min 50, la vidéo situe Qwen3.8-Flash-Next entre **environ 370 et 560 tokens/s** sur une seule RTX 5090, selon la quantification. Le score combine conversation, sorties structurées et prose. Pour la prose seule, l’auteur donne environ **200 à 240 tokens/s**. Un protocole distinct a mesuré 500,4 tokens/s en génération avec Basalt 0.3.0, Q2_0 et MTP, sur neuf essais de 700 tokens. [Passage d’AgenticEngineering](https://www.youtube.com/watch?v=-tQJ7NlQkdo&t=410s) · [Résultats communautaires de Basalt](https://github.com/jesdga95/basalt/blob/main/docs/community/benchmarks.json) · [Essai indépendant à 500,4](https://github.com/notwitcheer/llm-bench-rig/tree/main/toolcall/basalt93)
- **224 tokens/s ?** I reprend le titre de Kai. Vers 3 min 35, Kai cite une plage de **223 à 231 tokens/s en génération**. Fabio Akita l’a mesurée avec Basalt sur RTX 5090 et Qwen3.8-Flash-Next IQ3_S, avec des réponses de 256 tokens. [Passage de Kai](https://www.youtube.com/watch?v=wC6jsOU4jII&t=215s) · [Mesures de Fabio Akita](https://www.akitaonrails.com/en/2026/10/27/llm-benchmark-best-open-source-llms-for-home-hardware/)

Les deux accroches portent sur Basalt. La présence de Strata rappelle l’origine du moteur. Pour illustrer l’effet d’un changement de moteur sur une même machine, le comparatif d’Akita fournit les mesures des deux moteurs pour chaque quantification. [Notes sur un autre cas avec la RTX 5060 Ti](../meme-carte-plus-rapide/sources.md)

[Miniature H](miniature/rendus/h-kai.png) · [Miniature I](miniature/rendus/i-kai.png) · [Miniature J](miniature/rendus/j-kai.png) · [Critique indépendante](miniature/critique-kai.md)
