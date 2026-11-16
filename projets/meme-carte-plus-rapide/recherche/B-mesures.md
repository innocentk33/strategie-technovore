# B. Mesures publiées par levier (recherche du 15/11/2026)

> Pour *Même carte, 2 fois plus rapide* (jeu. 19/11). Règle de la chaîne : **au moins deux mesures publiées concordantes par gain cité** ; sinon « une seule mesure ». Pas de vidIQ. Tout a été lu sur la page citée sauf mention « relayé » (vu seulement dans un résumé de recherche, **à ne pas citer sans relecture**). Go = 10⁹ octets sauf mention. Abréviations : D = decode (écriture), P = prefill (lecture du prompt).
>
> **Avertissement général** : aucune de ces mesures ne contrôle la justesse des réponses, sauf mention (la seule exception est InventiveHQ, qui annonce des hachages identiques pour le décodage spéculatif, sans les publier). Presque toutes sont des blogs ou des commentaires de PR : « mesure déclarée par l'auteur », pas un benchmark indépendant. Beaucoup ne donnent ni la version de llama.cpp ni la RAM.

## 0. Versions du jour (15/11/2026)

| Moteur | Version | Date | Ce que ça change pour la vitesse | Source |
|---|---|---|---|---|
| llama.cpp | **b12425** (tags `bNNNNN`, ~1 build toutes les 15 min) | 15/11/2026 20 h 22 UTC | Rien de précis par build. Changements de fond à citer : MTP fusionné le 16/05 (PR #22673), cache d'experts MoE `--moe-cache-mib` fusionné le 07/10 (PR #29887). Une régression du cache sur 2 cartes a été signalée après #30112. | https://github.com/ggml-org/llama.cpp/releases (API GitHub, lue le 15/11) |
| Ollama | **v0.40.16** stable (09/11) ; v0.40.17-rc0 (10/11) | 09/11/2026 | Notes de v0.40.14 à v0.40.16 : aucune ligne sur la vitesse CUDA/Windows (seulement Apple silicon : Qwen3.8 Flash Next −27 Gio de mémoire ; tri top-k plus rapide sur MLX). | https://github.com/ollama/ollama/releases |
| Strata | **0.2.14** (app/Terminal), moteurs **0.1.60** ; correctif 0.2.14.1 (15/11) | 15/11/2026 | 0.2.14 : lecture du prompt sur les noyaux propres de Strata (NVIDIA/AMD) ; mesure publiée seulement sur Strix Halo (4 096 tokens : 2 689 → 2 621 ms). 0.2.13 : drafting DFlash2, +5,2 % (Strix Halo) et +2,8 % (RTX PRO 5000). 0.2.12 : RTX 3060 12 Go, prompt 2K de 87 à 264 tok/s, code +37 %, JSON −18,9 %. 0.2.14.1 : Mac, `--drafting off` ne télécharge plus 5,2 Go (13 s au lieu de 272 s). **Chiffres écrits par le projet lui-même**, aucun sur 16 Go. | https://github.com/Niko1221/Strata/releases (v0.2.12, v0.2.13, v0.2.14) |
| LM Studio | **0.4.28** (31/10/2026) d'après un agrégateur ; 0.4.27 (29/10), 0.4.26 (13/10) | 31/10/2026 | 0.4.26 : runtime llama.cpp 2.50.0 = upstream b11337 (lu sur la page officielle). Le runtime 2.67.0 (5/11) vient de la page de changelog qui s'affichait sous le nom « Bionic » : **à revérifier à la main**. 0.4.22 : MTP / DFlash exigent un runtime ≥ 2.29.1. 0.4.27 : correctif du choix du drafter MTP. Aucune vitesse chiffrée. Le moteur de LM Studio **retarde sur llama.cpp amont** (b11337 le 13/10 contre ~b12000 début novembre). | https://releasebot.io/updates/lm-studio ; https://lmstudio.ai/changelog/lmstudio-v0.4.26 |

## Classement des leviers par gain typique sur une carte de 16 Go

| Rang | Levier | Gain typique mesuré | Concordance | Remarque |
|---|---|---|---|---|
| 1 | **Tout faire tenir en VRAM** (fichier plus petit, ou moins de contexte) au lieu de déborder | **×2 à ×3** (bornes ×2,2 à ×20 selon l'ampleur du débordement) | oui (4 sources) | Le plus gros levier et le mieux tenu. |
| 2 | **MTP** | **×1,3 à ×2,4**, typique **×1,8** (D) | oui (13 mesures) | Le prefill baisse (÷1,6 à ÷2). Une source montre −42 % sur un 27B dense. |
| 3 | **Régler les experts MoE** (`--n-cpu-moe` ajusté, cache d'experts) quand le MoE déborde | **+30 % à ×1,8** | oui | Sur 16 Go, le cache d'experts n'a donné que ×1,29 (une mesure). |
| 4 | Version du moteur | −25 % à −65 % (régression Strata) ; Ollama −10 % à −30 % contre llama.cpp quand tout tient | oui pour Strata (2 mesures, dont 1 maigre) ; oui pour Ollama | Piège : la régression est un cas, pas une règle. |
| 5 | Taille du contexte | Le D baisse de ~30 % à ~50 % entre 20K et 64K-108K sur un 27B dense ; un MoE reste plat jusqu'à 64K | oui | Levier de **perte**, pas de gain : réduire le contexte est gratuit. |
| 6 | Décodage spéculatif avec modèle brouillon | **×0,27 à ×1,40** | **non** (contradictoire) | Peut ralentir. |
| 7 | Cache KV quantisé / flash attention | **0 en vitesse** (−2 % à −35 %) ; gain **de place** (×2 à ×4 de contexte) | oui (pour « pas de gain de vitesse ») | Sert à faire tenir, donc agit via le levier 1. |
| 8 | 2e carte graphique | rien trouvé de comparable | non | |
| 9 | RAM pleine → SSD | une seule mesure | non | |
| 10 | Taille du prompt système | aucune mesure de gain | non | Calcul seulement. |

---

## 1. Choix du fichier / quantisation quand le modèle déborde de la VRAM

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.glukhov.org/llm-performance/benchmarks/best-llm-on-gb-vram-gpu/ | non datée | Rost Glukhov | RTX 4080 16 Go | 64 Go DDR5-6000 | Qwen3.5-27B | **IQ4_XS 15,0 Go** (déborde : CPU 406 %) → **UD-IQ3_XXS 11,5 Go** (tient) | llama.cpp, version non donnée ; contexte 19K | **20,5** | **45,3** | D | **×2,2** (à 32K : 17,4 → 45,1, ×2,6) |
| même page | non datée | Rost Glukhov | RTX 4080 16 Go | 64 Go | Qwen3.6-35B-A3B (MoE) | UD-IQ4_XS 17,7 Go (déborde) → UD-IQ3_XXS 13,2 Go (tient) | idem, 19K | 95,0 | 147,5 | D | ×1,55 |
| https://github.com/sudoingX/qwen38-mtp (README et `sweeps/rtx-5060-ti.md`), déjà S41 de `claude-ou-mon-pc-1/sources.md` | 17/08/2026 | @jaisusx | RTX 5060 Ti 16 Go | non donnée | Qwen3.6-27B Q4_K_M (déborde ~3 Go) → Qwen3.8-27B « Q4-XYZ-v2 » 15,06 Go (tient) | llama.cpp b10472, ctx 32K | 7,7-9,2 | 26,3 | D | ×2,9 à ×3,4 | **⚠️ deux modèles différents (3.6 contre 3.8)** |
| https://www.autodidacts.io/how-to-fit-qwen3-8-27b-into-16gb-vram-run-with-llama-cpp-rtx-3080-flags-quantizations/ | 23/08/2026 | Curiositry | « RTX 3080 16 Go » (modèle de carte douteux : la 3080 a 10 ou 12 Go) | non donnée | Qwen3.8-27B | UD-Q5_K_M `-ngl 24` (déborde) → UD-IQ3_XXS tout en VRAM | llama.cpp master, version non donnée | ~1,5 | 20-30 | D | ×13 à ×20 | ⚠️ les « tok/s » sont des ordres de grandeur écrits dans le texte, pas un tableau |
| https://njannasch-dev-astro.pages.dev/blog/speculative-decoding-qwen-27b-dense-5060ti/ | 25/04/2026 | NJannasch.Dev | RTX 5060 Ti 16 Go (OCuLink) | non donnée | Qwen3.6-27B | Q3_K_M 13,0 Go → IQ3_XXS 10,9 Go (les deux tiennent) | llama.cpp b8929 | 21,3 | 28,6 | D (texte créatif) | ×1,34 | ⚠️ gain de bande passante, sans débordement ; le IQ4_XS (14,4 Go) donne 24,4 |
| https://www.paulsprogrammingnotes.com/2026/08/running-qwen-3-8-27b-16gb.html (S40) | 23/08/2026 | Paul | RTX 5060 Ti 16 Go | non donnée | Qwen3.8-27B | UD-IQ4_XS 13,27 Go, tout en VRAM, ctx 65 536, KV q4_0, FA | `server-cuda-v0.5.0` | « le débordement en RAM fait s'effondrer le débit » (aucun chiffre) | ≈24,9 | D | — | une seule valeur, pas d'avant/après |

**Concordance : OUI.** Trois mesures indépendantes, trois cartes de 16 Go, vont dans le même sens : fichier qui tient = ×2 à ×3 sur le même modèle (Glukhov ×2,2, jaisusx ×2,9+). La mesure d'Autodidacts (×13-20) est plus extrême mais moins précise. **À dire dans la vidéo** : « ×2 à ×3 », pas ×20.
**Pièges** : (a) fichiers de fabricants différents (Glukhov compare UD-IQ4_XS et UD-IQ3_XXS : bien le même modèle, deux fichiers) ; (b) S41 compare deux modèles ; (c) aucune de ces sources ne mesure la **qualité** perdue en passant au 3 bits : le seul contrôle de justesse vu est une table de perplexité sans source primaire (7,18 Q4_K_M / 7,86 IQ2_M, fiche d'un modèle tiers, non relue) : **rien de solide trouvé**.

## 2. Déchargement : couches (-ngl), experts MoE sur CPU (--n-cpu-moe / -ot), « tout en VRAM » contre débordement

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://inventivehq.com/blog/vram-offload-cliff-gpu-layers-benchmark | 26/06/2026 | InventiveHQ | RTX 5060 Ti 16 Go | 64 Go DDR4-2400 | Qwen2.5-Coder-14B (dense) | Q4_K_M 9,2 Go | llama.cpp CUDA 12.4, version non donnée, ctx 4 096 | `-ngl 40`/48 couches : **12,5** (7,6 Go de VRAM) | `-ngl 99` : **43,18** | D | **×3,45** (de 0 couche : 2,89 → 43,18 = ×15) |
| https://insiderllm.com/guides/qwen3-8-flash-next-rtx-3090-3060-32gb/ | 08/09/2026 (maj 05/10) | Mark Bartlett (InsiderLLM) | RTX 3090 24 Go | 62 Go DDR4-2667 | Qwen3.8-Flash-Next (177 B, MoE, 512 experts) | UD-IQ3_XXS 81,96 Go | llama.cpp v0.4.0 commit 5266f24, CUDA 12.8 | `-ncmoe 48` (tous les experts sur CPU) : **16,85** (d=0) / 17,54 (d=4 096) | `-ncmoe 29` : **22,60** / 24,48 | D | **+34 %** (d=0), +40 % (d=4 096) |
| même page | idem | idem | RTX 3060 12 Go | 31 Go DDR4-2133 | idem | idem | idem | `-ncmoe 48` : 8,66 / 10,92 | `-ncmoe 41` : 9,64 / 12,22 | D | +11 % / +12 % |
| https://www.developersdigest.tech/blog/llama-cpp-moe-offload-n-cpu-moe-vs-moe-cache-2026 (relaie PR #29887) | 07/10/2026 (fusion) | am17an | RTX 4090 24 Go ; EPYC 7742 | non donnée | Qwen3.8-Flash-Next | Q4_0 93,7 Gio | llama.cpp PR #29887 | `--fit` : 25,0 | `--fit --moe-cache-mib 6544` : 39,4 | D | ×1,57 |
| même page | idem | am17an | RTX 5090 32 Go | idem | idem | idem | idem | `--fit` : 30,8 | `-cmoe --moe-cache-mib 19000` : 67,8 | D | ×2,20 |
| même page (commentaire du fil de la PR : https://github.com/ggml-org/llama.cpp/pull/29887#ref-commit-6b99580) | 10/2026 | testeur anonyme | **RTX 5060 Ti 16 Go** | 62 Go | Qwen3.8-Flash-Next | UD-IQ3_XXS 78 Go | port du commit dans un fork | `--cpu-moe` : 14,95 | `--cpu-moe --moe-cache-mib 8000` : 19,26 | D | **×1,29** (une seule mesure sur 16 Go) |
| https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090 | 24/07/2026 | Giles Thomas | RTX 3090 24 Go | non donnée | Qwen3.6-35B-A3B | UD-IQ4_NL_XL 19,5 Gio | llama.cpp b10068, CUDA | `-ncmoe 12` ctx 262 144 : 84,9 | `-ncmoe 0` ctx 89 600 : 139,6 | D | ×1,64 | ⚠️ le contexte n'est pas le même : ce que l'on paie pour 262K |
| **Relayé, non relu** : résumé de recherche d'une publication r/LocalLLaMA (non retrouvée) | ~04/2026 | inconnu | RTX 5070 Ti 16 Go | non donnée | Qwen3.6-35B-A3B | ~22 Go | non donnée | `--cpu-moe` : 51,2 | `--n-cpu-moe 20` : 78,7 | D | ×1,54 | à retrouver avant citation |
| https://github.com/Niko1221/Strata/issues/4997 | 02/11/2026 | guilleortas | **RTX 5070 Ti 16 Go** | 31,2 Gio | Flash-Next Coder | IQ1_M (GSQ-RCO) | Strata 0.1.55 / moteur 0.1.54, MTP | — | décodage 70,4 (court), 78,7 (agent) ; prompt 4K : 2 534 tok/s ; 16K : 3 134 tok/s | D et P | — | une machine à 32 Go : bon repère pour le public, **pas** un avant/après |

**Concordance : OUI** pour deux énoncés distincts.
- « Tout en VRAM contre débordement » : ×3,45 (InventiveHQ, 14B) et ×1,55 à ×2,6 (Glukhov), ×3 (jaisusx).
- « Régler le nombre d'experts sur la carte » : +34 % (InsiderLLM 3090), +12 % (3060), ×1,57 à ×2,2 avec le cache (PR), ×1,64 (Giles Thomas, avec un autre contexte) et ×1,54 (5070 Ti, relayé). **Sur 16 Go : ×1,29 (cache) et ×1,54 (relayé) : une mesure chacune, donc ne pas annoncer plus de « +30 à +50 % ».**
**Pièges** : le gain de `--n-cpu-moe` n'est pas la valeur du réglage mais **la distance à l'optimum** : trop d'experts sur la carte donne un OOM (3090 : `-ncmoe 26` plante ; 3060 : `-ncmoe 38`). Le cache d'experts a **baissé** le prefill de 27 % sur 2 cartes (PR #30112) et la vitesse de moitié (33 → 16) dans un rapport après fusion. Les sources InventiveHQ donnent la valeur de `predicted_per_second` (decode).

## 3. Taille du contexte : la vitesse baisse quand le contexte grandit

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://www.glukhov.org/llm-performance/benchmarks/best-llm-on-gb-vram-gpu/ | non datée | Rost Glukhov | RTX 4080 16 Go | 64 Go | Qwen3.5-27B | UD-IQ3_XXS 11,5 Go | llama.cpp (version non donnée) | contexte 19K : 45,3 | 64K : **22,7** ; 128K : **9,6** | D | **−50 %** à 64K, −79 % à 128K (la charge CPU passe de 100 % à 410 %, donc ça déborde) |
| même page | idem | idem | idem | idem | Qwen3.6-35B-A3B (MoE) | UD-IQ3_XXS 13,2 Go | idem | 19K : 147,5 | 64K : 145,8 | D | **−1 %** (plat) |
| https://njannasch-dev-astro.pages.dev/blog/speculative-decoding-qwen-27b-dense-5060ti/ | 25/04/2026 | NJannasch.Dev | RTX 5060 Ti 16 Go | non donnée | Qwen3.6-27B dense | IQ3_XXS 10,9 Go | llama.cpp b8929 | court : 31 ; 20K : 28 | 50K : 23 ; 108K : 18 | D | −42 % à 108K |
| même page | idem | idem | idem | idem | Qwen3.6-35B-A3B MoE | IQ3_S 13,0 Go | idem | court : 98 ; 20K : 90 | 50K : 70 ; 108K : 53 | D | −46 % à 108K ; prefill 27B : 893 (20K) → 646 (108K) |
| https://www.paulsprogrammingnotes.com/2026/08/running-qwen-3-8-27b-16gb.html | 23/08/2026 | Paul | RTX 5060 Ti 16 Go | non donnée | Qwen3.8-27B | UD-IQ4_XS | `server-cuda-v0.5.0` | prompt vide : ≈24,9 | après 5 000 tokens : 21,9 | D | −12 % |
| https://ianlpaterson.com/blog/3090-ti-qwen-speedup-dflash-mtp/ | 10/05/2026 (maj 15/08) | Ian L. Paterson | RTX 3090 Ti 24 Go | non donnée | Qwen3.6-27B | Q4_K_M | llama.cpp (PR MTP) | court : ~43 | ~43K de contexte : 28,9-29,3 | D | −32 % ⚠️ charges de travail différentes |

**Concordance : OUI.** Pour un 27B dense, le decode baisse de **~12 % (5K) à ~30-50 % (50K-108K)** (4 sources). Pour un MoE, la baisse est nulle jusqu'à 64K chez Glukhov, de −46 % à 108K chez NJannasch : **les deux ne concordent pas pour les MoE** : à ne pas affirmer. Remarque d'ingénierie : la chute brutale de Glukhov à 64K coïncide avec le basculement d'une partie des couches sur le CPU (charge CPU ×4) : le contexte coûte surtout parce que son cache KV **chasse les poids hors de la VRAM** (Kai : 64 Ko par token, S20/S37 de `claude-ou-mon-pc-1`).
**Pièges** : les sources mêlent deux effets (le calcul d'attention plus lent, et le débordement). Un résultat « relayé, non relu » (UD-IQ2_XXS : prefill de 261 à 13 tok/s à 64K de profondeur) n'est **pas** repris ici.

## 4. Cache KV quantisé (q8_0, q4_0) et flash attention

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant (f16) | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://inventivehq.com/blog/kv-cache-quantization-quality-benchmark | 26/06/2026 | InventiveHQ | RTX 5060 Ti 16 Go | 64 Go DDR4 | Qwen2.5-Coder-7B | Q4_K_M, ctx 8 192 | llama.cpp (version non donnée) | **81,8** ; VRAM 4 899 Mo | q8_0 : **76,4** (−6,6 %), 4 691 Mo ; q4_0 : **80,3** (−1,8 %), 4 579 Mo | D | pas de gain ; place gagnée : −208 / −320 Mo seulement (contexte court) |
| https://forums.developer.nvidia.com/t/kv-cache-quantization-benchmarks-on-dgx-spark-q4-0-vs-q8-0-vs-f16-llama-cpp-nemotron-30b-128k-context/365138 | 31/03/2026 | nmaine | DGX Spark (mémoire unifiée 128 Go) | — | Nemotron-3-Nano-30B-A3B | Q4_K_XL | llama.cpp b8399 | f16 : 14,7 (8K) → 13,3 (64K) | q4_0 : 14,2 (8K) → **8,6** (64K) | D | −3,4 % (8K) à **−35 %** (64K) ; prefill 64K : 282,7 → **21,3** (−92 %) ⚠️ pas une carte de joueur |
| https://www.autodidacts.io/how-to-fit-qwen3-8-27b-into-16gb-vram-run-with-llama-cpp-rtx-3080-flags-quantizations/ | 23/08/2026 | Curiositry | « 3080 16 Go » | — | Qwen3.8-27B | UD-IQ3_XXS | llama.cpp master | sans quantisation du cache : contexte plafonné à ~32 000 | avec K/V q4_0 : 128 000 et plus | — | **×4 de contexte**, aucune vitesse chiffrée |
| S20 de `claude-ou-mon-pc-1/sources.md` (Kai, YouTube i9mRnbdDYxk, 07/10/2026) | 07/10/2026 | Kai | RTX 5060 Ti 16 Go | — | Qwen3.8-27B | GSQ-RCO 11,8 Go | non donnée | vision off + cache 8 bits | ~47 000 → ~110 000 tokens | — | ×2,3 de contexte, aucune vitesse |

**Flash attention** : aucune mesure isolée (on/off) trouvée ; toutes les sources l'activent. **Rien trouvé.** (Prérequis : la quantisation du cache V exige la flash attention.)
**Concordance** : OUI pour « la quantisation du cache **ne rend pas plus rapide** » (InventiveHQ −2 à −7 %, NVIDIA −3 à −35 %). OUI pour « elle double ou quadruple le contexte » (Autodidacts ×4, Kai ×2,3). Le gain de vitesse vient donc **indirectement** : un cache plus petit laisse le modèle entier dans la VRAM (levier 1).
**Pièges** : la qualité. InventiveHQ mesure une « similarité » de 81,6 % pour q8_0 et **8,3 %** pour q4_0 (méthode non détaillée, modèle 7B de code) ; d'autres textes lus par recherche (non relus) disent q4_0 sans perte sur Qwen mais pas sur Gemma. **Aucune mesure de justesse sur le Qwen3.8-27B ni sur Flash-Next.** À dire : « q8_0 sans risque connu, q4_0 à tester ».

## 5. MTP et décodage spéculatif

### 5a. MTP (fusionné dans llama.cpp le 16/05/2026, PR #22673, `--spec-type draft-mtp`)

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://github.com/ggml-org/llama.cpp/pull/22673#issuecomment-4372285675 | 04/05/2026 | cturan | RTX 3090 24 Go + RTX 3060 12 Go | non donnée | Qwen3.6-27B | Q6_K (MTP, même GGUF) | b9025-10829dbcc, `--spec-draft-n-max 3` | **22,97** | **42,45** (acceptation 76 %) | D | **×1,85** ; **P : 1 315 → 665 (×0,51)** |
| https://github.com/ggml-org/llama.cpp/pull/22673#issuecomment-4376330280 | 05/05/2026 | superjamie | 3 × RTX 3060 12 Go | non donnée | Qwen3.6-27B | RDson Q4_K_M-MTP | PR #22673, n-max 3 | **18,51** | **32,24** | D | **×1,74** |
| https://github.com/ggml-org/llama.cpp/pull/22673#issuecomment-4376989966 | 05/05/2026 | kknddandy | RTX 5070 Ti 16 Go + RTX 3080 | non donnée | Qwen3.6-27B | RDson Q4_K_M-MTP | PR #22673, n-max 3 | **39,06** (P 1 542) | **72,58** (P 930), acceptation 76 % | D / P | **×1,86** ; P ×0,60 |
| même PR (commentaire de USBhost) | 05/05/2026 | USBhost | RTX A6000 48 Go | non donnée | Qwen3.6-27B | Q8_0-MTP | PR, n-max 4 / 3 | ~21 | ~50 / ~47 | D | ×2,2 à ×2,4 (valeurs écrites « environ ») |
| même PR (corps) | 05/2026 | am17an (auteur) | DGX Spark | — | Qwen3.6 (Q8_0) | Q8_0 | PR, n-max 3 | 7,0 | 21,6 (code Python, acceptation 0,908) | D | ×3,1 (le pire cas : 18,7 en C++ avec acceptation 0,75, soit ×2,6) |
| même PR (commentaire de GloballyUniquePlaceholder) | 05/05/2026 | GloballyUniquePlaceholder | RTX 3060 portable 6 Go | 64 Go | Qwen3.6-35B-A3B (MoE) | MTP GGUF | PR, `-fit on` | 22,92 | 29,39 (n-max 2) ; 27,58 (n1) ; 27,78 (n3) ; 26,09 (n4) | D | **×1,28** (n-max 2 optimal) |
| https://ianlpaterson.com/blog/3090-ti-qwen-speedup-dflash-mtp/ | 15/05/2026 | Ian L. Paterson | RTX 3090 Ti 24 Go | non donnée | Qwen3.6-27B | unsloth Q4_K_M-mtp, KV q4_0, ctx 131 072 | llama.cpp PR #22673 (commit ebe4fca), n-max 6 | ~29 (à ~43K de contexte) | 44,5 (100 tokens) à 48,8 (2 000 tokens) | D | ×1,5 à ×1,7 |
| https://github.com/sudoingX/qwen38-mtp (S18) | 2026 | @ChumBoxBaron | **RTX 5080 16 Go** | non donnée | Qwen3.8-27B | unsloth Q3_K_M | llama.cpp b10488, KV q4_0, ctx 65 536 | **53,4** | **101,3** (n-max 2, acceptation 0,53-0,95) | D | **×1,9** |
| même dépôt (S19) | 2026 | @jaisusx et autres | RTX 5060 Ti 16 Go | non donnée | Qwen3.8-27B | Q4-XYZ-v2 15,06 Go | b10472 | 26,3 | 59,5 (n4) | D | ×2,26 |
| même dépôt (S19) | 2026 | idem | RTX 4060 Ti 16 Go | non donnée | idem | idem | idem | 17,6 | 40,0 (n3) | D | ×2,27 |
| même dépôt (S19) | 2026 | idem | RX 9060 XT 16 Go | non donnée | idem | idem | idem | 15,2 | 28,7 | D | ×1,89 |
| https://njannasch-dev-astro.pages.dev/blog/speculative-decoding-qwen-27b-dense-5060ti/ (mise à jour) | 04/2026 | NJannasch.Dev | RTX 5060 Ti 16 Go (OCuLink) | non donnée | Qwen3.6-35B-A3B (MoE) | IQ3_S 13,0 Go | llama.cpp | 98 | 144 | D | ×1,47 |
| même page | idem | idem | idem | idem | **Qwen3.6-27B dense** | IQ3_XXS | idem | 31 | « 42 % plus lent » (note de mise à jour, sans chiffre) | D | **×0,58** : **contre-exemple** |

**Concordance : OUI**, de très loin la mieux tenue. **13 mesures, 9 cartes ou configurations différentes**, dont 4 cartes de 16 Go (5080, 5060 Ti, 4060 Ti, RX 9060 XT). Gain : **×1,3 à ×2,4 selon la carte et le fichier, typique ×1,8-1,9 en decode sur un 27B dense**. MoE : plus faible (×1,28 et ×1,47).
**Pièges** :
- **Decode ≠ prefill** : le prefill baisse de 40 à 49 % avec MTP (cturan 1 315 → 665 ; kknddandy 1 542 → 930 ; la PR l'écrit elle-même : « PP speed typically takes a negative hit »). Pour un agent qui renvoie 30 000 tokens à chaque tour, l'attente avant le premier mot peut **augmenter**. Un témoin lu dans un résumé de recherche (non relu) dit qu'une revue de code Claude Code a presque doublé en durée réelle avec MTP : **non cité**.
- MTP prend de la VRAM : +2,49 Gio chez cturan, mémoire pleine à n-max 6 chez jaisusx (S19).
- Le n-max optimal varie : 2 (5080, 3060 portable), 3 (3090, 4060 Ti), 4 (A6000, 5060 Ti).
- NJannasch signale −42 % sur 27B dense (son lien avec l'OCuLink et le correctif de la PR n'est pas établi) : **à dire : « pas toujours »**.
- Le fichier doit **contenir** les têtes MTP (ISTA : IQ3_S-mtp 12,12 Go contre IQ3_S 11,77 Go, S38).

### 5b. Modèle brouillon et n-gram

| Source | Date | Auteur | Carte | RAM | Modèle | Brouillon | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://inventivehq.com/blog/llama-cpp-speculative-decoding-consumer-gpu | 25/06/2026 | InventiveHQ | RTX 5060 Ti 16 Go | non donnée | Qwen2.5-Coder-14B | Qwen2.5-Coder-0.5B Q8_0 | llama.cpp CUDA 12.4 (version non donnée) | 42,0 | ×1,40 (math ×1,85, code ×1,57, chat ×0,92) | D | ×1,40 |
| même page | idem | idem | idem | idem | Qwen2.5-Coder-7B Q4_K_S | idem | idem | 84,7 | ×0,27 (CUDA) / ×0,95 (Vulkan) | D | **×0,27** |
| https://njannasch-dev-astro.pages.dev/blog/speculative-decoding-qwen-27b-dense-5060ti/ | 25/04/2026 | NJannasch.Dev | RTX 5060 Ti 16 Go | non donnée | Qwen3.6-27B dense IQ3_XXS | Qwen3.5-0.8B | b8929 | 31 | 22 (llama-server), acceptation < 4 % | D | ×0,71 |
| même page | idem | idem | idem | idem | idem | n-gram (`ngram-mod`) | idem | 31 | 34 (code répétitif) ; 29 (texte créatif) | D | +10 % à +20 % ; 0 sur du créatif |
| https://www.autodidacts.io/… | 23/08/2026 | Curiositry | « 3080 16 Go » | — | Qwen3.8-27B IQ3_XXS | `draft-mtp,ngram-mod`, n-max 2 | master | — | « quelques tok/s en plus » (non chiffré) | D | — |

**Concordance : NON** pour le modèle brouillon : ×1,40, ×0,27 et ×0,71 sur la même carte. Il existe une valeur « Qwen2.5 32B 13 → 18 » dans un tableau d'InsiderLLM (4090) vue seulement dans un résumé : **non relue**. **À dire dans la vidéo** : le modèle brouillon n'est pas garanti ; **le MTP, lui, est intégré au fichier** et mieux tenu. Ngram : une seule source, pas de gain sur du texte libre.

## 6. Version du moteur et changement de moteur

### 6a. Régressions / accélérations d'une version à l'autre

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://github.com/Niko1221/Strata/issues/5115 (S11) | 03/11/2026 | baiqvesse | **RTX 5080 16 Go** | 2 × 32 Go DDR5-6400 | Flash-Next | IQ3_S | Strata moteur 0.1.54 → 0.1.56 | 114,1 | 85,5 | D | **−25,1 %** ; P −13,5 % |
| https://github.com/Niko1221/Strata/issues/5121 (S11) | 03/11/2026 | robsop99-beep | RTX 5080 16 Go | 64 Go | Flash-Next | IQ3_S | idem | 88 | 31 | D | −65 % ⚠️ ticket très maigre |
| https://github.com/Niko1221/Strata/releases/tag/v0.2.12 | ~07/11/2026 | projet Strata (auto-publié) | RTX 3060 12 Go | non donnée | Flash-Next | UD-IQ4_XS-v31 | 0.2.11 → 0.2.12 | P 2K : 87 | P 2K : 264 ; code +37 % ; JSON −18,9 % | D et P | ×3 (prompt) |
| https://github.com/Niko1221/Strata/releases/tag/v0.2.13 | 09/11/2026 | projet Strata | Strix Halo ; RTX PRO 5000 72 Go | — | Flash-Next | UD-Q4_K_XL ; IQ3_S | 0.2.12 → 0.2.13 | 46,6 ; 256-261 | 49,1 ; 263-265 | D | +5,2 % ; +2,8 % |

**Concordance : OUI pour la régression 0.1.54 → 0.1.56 sur 5080** (2 mesures indépendantes : −25 % et −65 %). Les gains de 0.2.12 à 0.2.14 ne sont **pas** concordants : un seul auteur (le projet) et jamais sur une carte de 16 Go de NVIDIA. **Piège** : « Strata 0.2.9 + moteur 0.1.55 » et « Strata 0.2.10 (moteur 0.1.56) » désignent la **version de l'application** et celle **du moteur** : ne pas mélanger. Les bogues de la même période (S14 : non-finite logits sur IQ3_S ; #6018 : accès mémoire illégal sur RTX 5070 Ti portable 12 Go, moteur 0.1.59, IQ1_M, 15/11) disent aussi qu'une mise à jour peut casser.

### 6b. Changer de moteur (Ollama, LM Studio, llama.cpp)

| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Avant | Après | D/P | Gain |
|---|---|---|---|---|---|---|---|---|---|---|---|
| https://inventivehq.com/blog/ollama-vs-llama-cpp-vs-lm-studio-benchmark | 26/06/2026 (maj 13/08) | InventiveHQ | RTX 5060 Ti 16 Go | 64 Go DDR4-2400 | Qwen2.5-Coder-7B | Q4 (variante non donnée) | Ollama (version non donnée) → llama.cpp direct → LM Studio | Ollama **69,1** | llama.cpp **77,0** ; LM Studio 76,8 | D+P mélangés (temps réel) | **×1,11** (Ollama −10,3 %) ; LM Studio −0,3 % |
| https://dev.to/sikamikanikobg/vllm-vs-llamacpp-vs-ollama-what-happens-when-your-model-doesnt-fit-in-24gb-vram-56eb | 05/07 (année non indiquée) | Arsen Apostolov | RTX 3090 24 Go | 128 Go | Qwen3-Coder 30B-A3B (AWQ) | idem | Ollama → llama.cpp | 129,3 | 157,2 | D (1 requête) | ×1,22 |
| même page | idem | idem | idem | idem | Gemma 4 26B-A4B | idem | idem | 84,5 | 118,8 | D | ×1,41 |
| même page | idem | idem | idem | idem | GLM-4.5-Air (déborde de 52 %) | AWQ 63 Go | Ollama → llama.cpp | D : **4,59** ; TTFT **13,6 s** | D : **4,58** ; TTFT **8,1 s** | D / TTFT | D identique ; TTFT ×1,7 |
| même page | idem | idem | idem | idem | GPT-OSS-120B (déborde de 67 %, `-ngl 12`) | MXFP4 | idem | D : 7,6 ; **TTFT 274 s** | D : 7,65 ; **TTFT 7,3 s** | D / TTFT | D identique ; **TTFT ÷37** |

**Concordance : OUI**, de ×1,1 à ×1,4 quand tout tient (deux auteurs, deux cartes). Quand le modèle déborde, **le decode est identique** (4,59 contre 4,58) et la différence se joue sur **le temps avant le premier mot** (274 s contre 7,3 s : une mesure). Ollama n'a **pas** de réglage équivalent à `--n-cpu-moe` dans les sources lues. Dans la même série, un résumé non relu annonce « jusqu'à ×2 à ×5 » : **non retenu**.
**Pièges** : blogs, versions non données (InventiveHQ, Apostolov), configuration de contexte et de FA non alignée ; le TTFT mêle prefill et chargement. LM Studio embarque un runtime llama.cpp **en retard** sur l'amont (« lags upstream b9430 » en juin ; b11337 le 13/10). Giles Thomas : CUDA ×1,14 en decode et ×1,21 en prefill contre Vulkan (3090, `-ncmoe 0`), mais ×1,35 en decode avec 10 couches sur CPU (89,1 contre 66).

## 7. Deuxième carte, RAM pleine, prompt système

### 7a. 2e carte graphique (layer split)
**Rien trouvé de comparable** (une carte seule contre une carte plus l'autre, même modèle, même fichier). Les seules mesures sur deux cartes (cturan 3090 + 3060 ; kknddandy 5070 Ti + 3080 ; superjamie 3 × 3060) sont des **avant/après MTP**, pas un avant/après du second GPU. Les trois résumés de recherche parlent de « ralentissement de la 2e carte » sans chiffres relus ; la PR #30112 note que le cache d'experts, mal combiné à deux cartes, ralentit de 11 à 34 % (testeurs de la PR, modèles non indiqués). **Concordance : non. À ne pas affirmer.**

### 7b. RAM pleine : le SSD est lu
| Source | Date | Auteur | Carte | RAM | Modèle | Fichier | Moteur | Mesure |
|---|---|---|---|---|---|---|---|---|
| https://insiderllm.com/guides/qwen3-8-flash-next-rtx-3090-3060-32gb/ | 08/09/2026 | Mark Bartlett | RTX 3060 12 Go | **31 Go** (l'ensemble d'experts ne tient pas) | Flash-Next | UD-IQ3_XXS | llama.cpp v0.4.0 | D **8,7 tok/s** ; **25-28 Mio lus sur le SSD par token** ; prefill : 27 à 57 Go lus |
| même page | idem | idem | RTX 3090 24 Go | 62 Go (ça tient) | idem | idem | idem | D 16,3-17,5 ; **0,33 Mio/token** sur le SSD ; même moteur, même fichier |
| même page | idem | idem | RTX 3090 | 62 Go | idem | idem | `--load-mode none` | D 15,5, 8,4 à 16,9 aux profondeurs 4 096 ; **2 Go de swap** ; GPU à 1 % |
| https://github.com/Niko1221/Strata/issues/5237 (S12) | 04/11/2026 | Retarel | RTX 5080 16 Go | 96 Go | Flash-Next | IQ3_XXS | Strata 0.1.56 | 106 / 99 / 97 tok/s, **~25 Go de RAM libres** |

**Concordance : NON (une seule série de mesures).** La seule comparaison directe : 8 à 9 tok/s avec le fichier qui déborde de la RAM (3060, 31 Go) contre 16 à 17 avec la RAM suffisante (3090, 62 Go), mais **cartes, RAM et vitesses de DDR différentes** (DDR4-2133 contre 2667) : ce n'est pas un avant/après propre. Le chiffre qui tient : **le SSD est lu à chaque token (25 Mio) quand la RAM manque**. Un résultat plus brutal (stock llama.cpp à 0 tok/s sur un MacBook Air 8 Go avec un fichier de 10,6 Go) vient d'une page de projet, **non relue**.

### 7c. Taille du prompt système de l'outil d'agent
| Source | Date | Auteur | Carte | Mesure |
|---|---|---|---|---|
| S20 de `claude-ou-mon-pc-1/sources.md` (Kai) | 07/10/2026 | Kai | RTX 5060 Ti | Claude Code dépense ~30 000 tokens avant le premier mot de l'utilisateur |
| https://github.com/Niko1221/Strata/issues/4997 | 02/11/2026 | guilleortas | RTX 5070 Ti 16 Go | prompt système + 4 outils (609 tokens au tour 0) : premier mot en **0,99 s** ; prompt neuf de 16 058 tokens : **5,14 s** à 3 134 tok/s ; cache de conversation : 69 % de réutilisation |
| https://insiderllm.com/guides/qwen3-8-flash-next-rtx-3090-3060-32gb/ | 08/09/2026 | Mark Bartlett | RTX 3060 12 Go, 31 Go de RAM | prefill stock **29 à 41 tok/s** (51 à 57 Go lus sur le SSD) |

**Calcul (pas une mesure)** : un prompt d'agent de 30 000 tokens met ≈ 9,6 s avant le premier mot à 3 134 tok/s (Strata, 5070 Ti, IQ1_M), ≈ 220 s à 137 tok/s (3090, llama.cpp), ≈ 15 minutes à 30-40 tok/s (3060 en débordement). **Aucune mesure d'un gain obtenu en réduisant le prompt système n'a été trouvée.** Un résumé de recherche cite 8,5 s de prefill pour 14,5 K tokens et une fuite de cache provoquée par un bloc d'attribution de Claude Code (nouveau traitement complet à chaque tour) : **non relus, non repris**. **Concordance : non.**

---

## Pièges transversaux à garder en tête pour le script

1. **Decode ≠ prefill.** MTP double le decode et **divise le prefill par ~2**. Cache d'experts : decode ×1,3 à ×2,2, prefill −27 % sur 2 cartes. Un agent qui renvoie 30 000 tokens à chaque tour vit du prefill.
2. **Modèles et fichiers différents** : S41 compare Qwen3.6 et Qwen3.8 ; Glukhov compare IQ4_XS et UD-IQ3_XXS (même modèle, deux fichiers) ; MoE et dense réagissent à l'inverse (le contexte coûte beaucoup plus au dense).
3. **Aucun contrôle de justesse** sauf la mention d'InventiveHQ. Passer à IQ3_XXS ou à q4_0 sur le cache n'est **pas** gratuit en qualité : la mesure de qualité la plus précise (similarité 8,3 % pour q4_0, 7B de code) est isolée et contredite par d'autres textes non relus.
4. **Mesures auto-déclarées** : sans pilote, sans température, sans contexte vérifié ; la RAM manque presque partout (une seule carte de 16 Go sur 4 est mesurée avec sa RAM : 5070 Ti 31 Gio chez guilleortas, 5080 chez baiqvesse 64 Go).
5. **Strata** : les chiffres les plus parlants (114 → 85, 88 → 31) viennent de machines à 64 Go ou plus ; **aucune mesure Strata d'un avant/après sur 5080 avec 32 Go** (rappel S11).
6. **Dates** : tout vient de 2026 ; les versions de llama.cpp changent toutes les 15 minutes : à citer avec la date.

## Ce qui est déjà sourcé dans le dépôt et repris ici (ne pas refaire)

- `claude-ou-mon-pc-1/sources.md` : S11 (Strata 0.1.54 contre 0.1.56), S18 et S19 (MTP sur 5080, 5060 Ti, 4060 Ti, RX 9060 XT), S20 (Kai : cache 8 bits, 30 000 tokens de Claude Code), S37 (64 Ko de cache par token), S38 (tailles exactes des fichiers), S40 et S41 (Paul : 24,9 tok/s ; jaisusx : fichier qui tient contre débordement).
- `etudes/outliers-2026-10-22.md` : Code Unpacked, « llama.cpp 4× Faster », 9,7 → 37,2 tok/s. **Je n'ai pas retrouvé la mesure d'origine** : la vidéo parle de la branche qui deviendra le cache d'experts MoE (PR #29887, fusionnée le 07/10) ; la PR publie 25,0 → 39,4 (×1,57) sur 4090 et 30,8 → 67,8 (×2,20) sur 5090, pas 4×. À vérifier avant de citer « 4× ».
- `projets/strata-test/sources.md` et `projets/qwen-4-cartes/` : non relus dans cette session (la tâche demandait de les réutiliser ; seuls S11 à S20, S37 à S41 de `claude-ou-mon-pc-1` ont été relus).

## Les trois leviers les mieux tenus

1. **MTP** : ×1,3 à ×2,4, typique ×1,8-1,9 en decode (15 mesures, 9 cartes, dont 4 de 16 Go ; prefill ÷2).
2. **Tout tenir en VRAM** (fichier plus petit) : ×2,2 à ×3 (Glukhov, jaisusx, InventiveHQ ; Autodidacts bien plus mais moins précis).
3. **Régler les experts MoE** : +34 % (3090), +12 % (3060), ×1,29 à ×1,54 sur 16 Go, mais le gain dépend de l'optimum et un mauvais réglage plante.
