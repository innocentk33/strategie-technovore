# Recherche modèle, vidéo 1

Relevé du 16 novembre 2026. Document de recherche, aucun essai personnel. Sources ouvertes avec l’outil web. Statuts : ✅ source primaire lue ; ⚠️ mesure unique ou limite de lecture ; ❌ affirmation non établie ou extrapolation contredite.

## Hugging Face : fichiers

**M1 — ✅** Le dépôt demandé existe : [unsloth/Qwen3.8-27B-GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF). L’[arborescence](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main) affiche :

| Fichier | Taille affichée |
|---|---:|
| UD-IQ2_XS | 7,63 GB |
| UD-IQ2_S | 8,42 GB |
| UD-IQ2_XXS | 7,21 GB |
| UD-IQ3_XXS | 10,9 GB |
| UD-IQ3_S | 12 GB |
| UD-IQ4_XS | 14,4 GB |
| UD-Q2_K_XL | 9,95 GB |

**M2 — ✅** La [page individuelle UD-IQ2_XS](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-UD-IQ2_XS.gguf) confirme 7,63 GB et le commit `acb953b`, intitulé « New UD3.1 quants ». Téléchargement : [fichier GGUF](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/resolve/main/Qwen3.8-27B-UD-IQ2_XS.gguf). Taille affichée arrondie ; octets exacts non obtenus.

**M3 — ✅** La [page individuelle UD-Q2_K_XL](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-UD-Q2_K_XL.gguf) affiche 9,95 GB. Le [dossier MTP](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main/MTP) affiche 1,37 GB pour `mtp-Qwen3.8-27B-Q4_0.gguf`.

**M4 — ⚠️** Une taille de téléchargement ne prouve pas la mémoire totale pendant l’inférence. Ne pas transformer « 7,63 GB » en garantie universelle de fonctionnement sur une carte de 8 Go.

## Unsloth : publication et qualité

Source exacte : [Qwen3.8 - How to Run Locally](https://unsloth.ai/docs/models/qwen3.8), consultée et rouverte le 16/11/2026.

**M5 — ✅** La section Dynamic V3.1 porte explicitement la date du **11 novembre 2026**. Cette date établit celle de la mise à jour annoncée ; la date du commit HF individuel n’a pas été relue.

**M6 — ✅** Protocole déclaré par Unsloth : Terminal Bench 2.1, DeepSWE v1.1 ; LiveCodeBench v6 et autres évaluations. Contexte **256K** pour les tâches d’agent, **128K** pour les autres. Température **1,0**, top_p **0,95**, top_k **20**, min_p **0**, sans pénalité de présence/répétition ; `preserve_thinking` et effort `xhigh`.

**M7 — ✅** Unsloth indique ne pas renouveler les quants 3 bits, jugées suffisamment proches. Leurs mesures ne constituent pas une validation indépendante.

**M8 — ⚠️ NON VÉRIFIÉ** Les scores exacts de qualité sont dans des images, sans tableau numérique lisible dans l’extraction. Les « 95 % sur LiveCodeBench », « 94 à 97 % » et « moins de 13 % contre environ 40 % sur DeepSWE » de la fiche ne sont **pas validés** par cette recherche. Ne pas les étiqueter ✅.

Le [PNG de synthèse lié par la model card](https://cdn-uploads.huggingface.co/production/uploads/62ecdc18b72a69615d6bd857/4dsqjPC5agfiUudfeW_df.png) a été ouvert puis rouvert ; l’outil n’a pas rendu les pixels. Le téléchargement local a échoué faute de résolution DNS. Le repli par navigateur n’a pas permis la lecture et a été interrompu. Aucune approximation de graphique n’a donc été inventée.

## CompressionBench : ce que l’article établit

**M9 — ✅** [arXiv 2611.06858](https://arxiv.org/abs/2611.06858) existe : *CompressionBench: How can your coding agents compress LLMs?* Soumis **4 novembre 2026**, version **v2 le 9 novembre 2026**. [Texte intégral v2](https://arxiv.org/html/2611.06858v2).

**M10 — ✅** Tableau 1 : Qwen3.8-27B sous contrainte de stockage **8 GiB**, sur **H200 NVL**. Génération : **23,4 tokens/s** pour Sonnet 5.5, **26,2** pour Opus 5.5, **75,5** pour la référence publiée **GSQ-RCO**. Ce sont des mesures de décodage, batch 1, prompt **2 048 tokens**, sortie **128 tokens** ; préremplissage exclu.

**M11 — ❌** Cet article ne démontre pas un fonctionnement sur une véritable carte de 8 Go. La contrainte porte sur le modèle stocké et résident ; caches et allocations temporaires sont supplémentaires. Il ne fournit pas une seconde mesure du « ×5 » annoncé dans la fiche.

**M12 — ⚠️** Le « environ trois fois plus lent » est calculable face à GSQ-RCO dans ce protocole : 75,5 / 23,4 ≈ **3,23**, ou 75,5 / 26,2 ≈ **2,88**. Ne pas le présenter comme une comparaison directe avec notre UD-IQ2_XS sur une carte de joueur. L’absence d’un fichier téléchargeable n’a pas été établie.

## Deuxième vérification réellement effectuée

- Dépôt/model card : ouverture initiale ; arborescence ouverte puis rouverte, tailles relues.
- UD-IQ2_XS : taille recoupée entre arborescence et page individuelle. Page individuelle non rouverte séparément.
- UD-Q2_K_XL : même recoupement ; page individuelle non rouverte séparément.
- MTP : dossier ouvert puis rouvert ; 1,37 GB relu.
- Documentation Unsloth : ouverte puis rouverte, protocole et date relus. Scores graphiques toujours illisibles.
- arXiv : résumé et texte intégral ouverts, puis tous deux rouverts ; date, matériel et chiffres du tableau 1 relus.
- Image de synthèse HF : ouverte puis rouverte, résultat toujours sans pixels exploitables.

Corrections à appliquer : distinguer taille du fichier et VRAM totale ; ne pas confondre 8 GiB de stockage et GPU 8 Go ; attribuer le ratio CompressionBench à GSQ-RCO ; retirer les scores de qualité précis tant que les graphiques ne sont pas lus. Aucun script rédigé dans ce sous-travail.

## Addendum transmis par l’agent principal

L’agent principal a finalement obtenu l’image via un téléchargement réseau autorisé, puis l’a téléchargée et visualisée deux fois (`/tmp/qwen-quality.png` et `/tmp/qwen-quality-second.png`). Il rapporte : **DeepSWE BF16 40,40** et **LiveCodeBench BF16 88,62**, annotations exactes ; **UD-IQ2_XS environ 12,8 sur DeepSWE** et **environ 84,5 sur LiveCodeBench**, lectures de points non étiquetés. Ces deux derniers nombres restent des approximations graphiques. L’agent principal intègre la validation détaillée à F4 dans `sources.md`. Cet addendum remplace donc la limite d’accès de M8 pour la consolidation, sans prétendre que le présent sous-agent a lu les pixels.
