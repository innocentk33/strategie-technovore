# LM Studio et Steam : relevé du 16/11/2026

Deux ouvertures séparées de chaque URL ci-dessous effectuées via web. Aucune manipulation locale de LM Studio, aucune mesure.

- **I1 ✅** https://store.steampowered.com/hwsurvey/ : édition affichée October 2026, rubrique VRAM, 8 GB = **26,92 %**, variation **+0,21 point**. Première lecture puis réouverture section 1666. Enquête volontaire anonyme ; ne représente ni tout le parc mondial ni spécialement l'Afrique. Formulation : plus d'un quart des configurations de l'enquête Steam.
- **I2 ✅** https://lmstudio.ai/docs/app/advanced/per-model : My Models, roue dentée, paramètres par modèle. GPU offload, context size, Flash Attention explicitement listés. Page non datée ; consultée et rouverte 16/11/2026. Présence des contrôles, pas preuve de fonctionnement du GGUF précis.
- **I3 ✅** https://github.com/lmstudio-ai/localization/blob/main/en/config.json : K Cache Quantization Type et V Cache Quantization Type ; valeurs plus basses économisent mémoire mais peuvent dégrader qualité ; V quantifié exige Flash Attention. Lu puis rouvert et retrouvé aux lignes web 1772-1781. Branche main mobile ; date du commit non relevée. Ne pas en déduire un contexte garanti sur 8 Go.
- **I4 ⚠️** https://lmstudio.ai/ufnd01/qwen3.8-27b : fiche communautaire LM Studio Hub, mise à jour affichée 11 septembre (année non affichée), expose Enable Thinking et Reasoning Effort, défauts true et xhigh. Deux ouvertures. MAIS les fichiers liés sont MLX : ce n'est pas une validation du GGUF Unsloth dans LM Studio. Ne pas donner le chemin exact du bouton pour ce GGUF comme vérifié. Mention conditionnelle et contrôle de template requis.

## Corrections à apporter à la fiche

1. Pas « une carte sur quatre chez les joueurs » comme recensement universel : 26,92 % des configurations participantes Steam, octobre 2026.
2. Séparer réglages LM Studio documentés et recette 14K/22K issue d'un seul essai llama.cpp. Aucun benchmark équivalent LM Studio identifié par cette recherche.
3. Le contrôle de réflexion d'une fiche MLX ne prouve pas sa présence pour un GGUF importé. Ne pas utiliser /no_think par souvenir.
