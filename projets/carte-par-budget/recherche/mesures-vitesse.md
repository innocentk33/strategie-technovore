# Mesures publiées : la vitesse d'écriture d'un LLM suit-elle la bande passante mémoire ?

Recherche faite le 18/11/2026. Chaque chiffre vient d'une page ouverte (HTML brut analysé en local, ou graphique lu à l'image) ; les cas où je n'ai que le résumé d'un outil sont signalés. « non trouvé » = pas de page lue qui l'établit. Les ratios et pourcentages marqués (calcul) sont les miens, pas ceux des sources.

Abréviations : tg = génération (tokens/s, `tg128` dans llama-bench), pp = lecture du prompt (tokens/s, `pp512`), BP = bande passante mémoire officielle (Go/s), FA = flash attention.

## 0. Résumé

1. Quatre jeux de mesures par UN MÊME testeur, même modèle, même logiciel, plusieurs cartes, modèle entier en VRAM : Hardware Corner (9 cartes à 16K de contexte, dont 5 à BP connue, Qwen3 8B/14B), Puget Systems (12 cartes, Phi-3-mini), un contributeur de la discussion llama.cpp n°15013 (RTX 5060 Ti contre RTX 4060 Ti 8 Go), un contributeur de la discussion n°10879 (RX 9060 XT contre RX 6800).
2. Chez Hardware Corner, l'ordre de la génération suit exactement l'ordre des bandes passantes (BP) sur les cinq cartes à BP imprimée ou officielle : 3090 (936) 87,45 > 5070 (672) 59,13 > 5060 Ti (448) 51,41 > 3060 12 Go (360) 41,97 > 4060 Ti 16 Go (288) 34,31 tokens/s.
3. Chez Puget, RTX 4070, 4070 SUPER et 4070 Ti ont la même BP (504,2 Go/s) : 141, 142, 143 tokens/s en génération, mais 4 458, 5 165, 5 733 en lecture du prompt. Le calcul change la lecture, pas l'écriture.
4. Le lien est réel mais pas proportionnel : le rapport de vitesse est plus petit que le rapport de BP dès qu'on monte en gamme (voir §5 et §6).
5. Contre-exemples publiés : GTX 1080 Ti (484 Go/s) à 23 tokens/s et RTX 2080 Ti (616 Go/s) à 96, contre 141 pour une RTX 4070 (504 Go/s) chez Puget ; Intel Arc B580 (456) sous la RTX 3060 (360) en Vulkan ; RTX 5070 seulement 15 % devant la 5060 Ti chez Hardware Corner (672 contre 448) mais 40 % sur le tableau llama.cpp (autres testeurs).
6. Non trouvé : test contrôlé RTX 3060 Ti / 3070 contre RTX 4060 de bureau (seulement LocalScore, source faible) ; test contrôlé de la B580 et de la RX 7600 XT contre une RTX.
7. Explication : un collaborateur de llama.cpp écrit que la génération est limitée par la mémoire et la lecture du prompt par le calcul (§2).
8. Les chiffres LocalScore (moyennes de la foule) sont les moins fiables : indication seulement.

## 1. Débits mémoire retenus (BP, Go/s) et d'où ils viennent

| Carte | BP | Source (page ouverte) |
|---|---|---|
| RTX 4060 | 272 | Puget Systems (tableau des BP), Wikipédia « GeForce 40 series » |
| RTX 4060 Ti (8 ou 16 Go) | 288 | Puget (8 Go) ; Hardware Corner, page classement (16 Go : « limited 288 GB/s ») |
| RTX 3060 12 Go | 360 | Wikipédia « GeForce 30 series » (bus 192 bits ; tableau découpé en lignes, valeur cohérente avec bus × débit) |
| RTX 3060 8 Go | 224 | même page Wikipédia (128 bits) |
| RTX 3060 Ti | 448 | Club386 (comparatif 5060 Ti / 3060 Ti, 17/04/2025) ; Wikipédia |
| RTX 3070 | non trouvé | la page Wikipédia lue ne donne pas la ligne de la 3070 sans ambiguïté |
| RTX 3070 Ti | 608 | Wikipédia « GeForce 30 series » |
| RTX 3090 | 936 / 936,2 | Hardware Corner (deux pages) ; Wikipédia |
| RTX 4070 | 504 / 504,2 | Puget ; Wikipédia |
| RTX 4090 | 1 008,4 | Puget |
| RTX 5060 Ti 16 Go | 448 | Club386 ; Hardware Corner (comparatif double 5060 Ti / 3090) |
| RTX 5070 | 672 (calcul) | Wikipédia « GeForce 50 series » liste 672 mais le tableau est mal aligné : attribution par bus 192 bits × 28 Gb/s ÷ 8 (calcul) |
| RTX 5070 Ti / 5090 | 896 / 1 792 (calcul) | même page, même réserve |
| GTX 1080 Ti | 484,4 | Puget |
| Intel Arc B580 | 456 (12 Go, 192 bits) | Wikipédia « Intel Arc » |
| RX 6800 | 512 (256 bits) | Wikipédia « Radeon RX 6000 series » |
| RX 9060 XT 16 Go | 320 (déduit) | Wikipédia « Radeon RX 9000 series » : 288 et 320 listés sans étiquette ; 320 = 128 bits × 20,1 Gb/s ÷ 8 (calcul) ; le testeur écrit « 16 GB GDDR6, 128-bit » |
| RX 7600 XT | non trouvé | |

La 5060 Ti a la même BP (448) que la 3060 Ti, avec un bus deux fois plus étroit mais une mémoire GDDR7 deux fois plus rapide (Club386).

## 2. Pourquoi la génération est limitée par la mémoire (explications)

- **am17an, collaborateur du dépôt llama.cpp**, discussion « Optimizing Token Generation in llama.cpp's CUDA Backend », n°17621, 30/11/2025 : https://github.com/ggml-org/llama.cpp/discussions/17621. Il écrit que, pour les LLM décodeur seul, « PP is compute-bound and TG is memory-bound ». Il ajoute que, la génération étant limitée par la mémoire, la fusion de noyaux (moins de trafic mémoire) y aide le plus. Dans le même fil, un commentateur (coder543, 02/01/2026) calcule un plafond théorique (BP ÷ octets lus par token) et mesure 82,64 tokens/s sur un GB10 là où il calcule environ 85 : le mainteneur juge « +/-10 % » correct comme erreur d'estimation. Preuve que la formule « tokens/s ≈ BP ÷ taille du modèle » est un plafond, pas une prédiction exacte.
- **NVIDIA Technical Blog**, « Mastering LLM Techniques: Inference Optimization », Shashank Verma et Neal Vaidya, 17/11/2023 : https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ . Paraphrase : la phase de décodage produit un token à la fois (produit matrice-vecteur), le temps dépend surtout de la vitesse à laquelle poids et cache clé-valeur arrivent de la mémoire vers le GPU, pas de la vitesse de calcul ; la phase de remplissage (lecture du prompt) traite tous les tokens en parallèle et sature le GPU.
- **Puget Systems** (§1.B) : explique la 3080 Ti rapide en génération par sa BP, et rappelle que la BP n'est pas le seul facteur (1080 Ti).
- Non ouvertes (apparues en recherche seulement) : guide Arm « llama-roofline », blog am17an. Ne pas les citer.

## 3. Sources détaillées

### A. Hardware Corner, « The Definitive GPU Ranking for LLMs » (meilleur jeu : un labo, 5 cartes, mêmes réglages)

- URL : https://www.hardware-corner.net/gpu-ranking-local-llm/ ; auteur Allan Witt ; « Updated: December 9, 2025 » (mises à jour intermédiaires 9, 10 et 18 novembre). Page relue le 18/11/2026.
- Logiciel : `llama-bench` de llama.cpp « latest » (version non précisée), CUDA 12.8, Ubuntu 24.04. Quantification 4 bits « Q4_K_XL » pour toutes les mesures de génération (la page cite Q4_K pour le test de lecture du prompt de la 3090). Contexte : 16K tokens (les débits de génération sont donc mesurés avec 16 000 tokens déjà en cache, plus bas qu'à contexte vide).
- Prix de la page (non daté précisément) : 3060 250 $, 4060 Ti 409 $ (la page parle de la 4060 Ti 16 Go), 5060 Ti 430 $, 5070 579 $.

Génération à 16K de contexte, tokens/s (valeurs extraites du HTML brut) :

| Carte | BP | Qwen3 8B | Qwen3 14B | gpt-oss 20B | pp Qwen3 8B | pp Qwen3 14B |
|---|---|---|---|---|---|---|
| RTX 3090 24 Go | 936 | 87,45 | 52,14 | 128,51 | 2 572 | 1 679 |
| RTX 5070 Ti 16 Go | 896 | 87,54 | 57,98 | 133,05 | 3 654 | 2 304 |
| RTX 4080 SUPER 16 Go | 736 | 79,36 | 52,76 | 122,96 | 3 858 | 2 527 |
| RTX 4070 Ti SUPER 16 Go | 672 | 72,20 | 47,18 | 113,60 | 3 051 | 2 003 |
| RTX 5070 12 Go | 672 (calcul) | 59,13 | 40,59 | non testé | 1 601 | 1 315 |
| RTX 4070 12 Go | 504 | 52,07 | 32,66 | non testé | 2 064 | 1 356 |
| RTX 5060 Ti 16 Go | 448 | 51,41 | 32,91 | 82,42 | 1 448 | 943 |
| RTX 3060 12 Go | 360 | 41,97 | 22,66 | non testé | 1 119 | 678 |
| RTX 4060 Ti 16 Go | 288 | 34,31 | 22,36 | 57,76 | 1 481 | 918 |

Les BP de ce tableau ne sont pas toutes imprimées par la page : seules 3090 (936,2) et 4060 Ti (288) le sont ; les autres viennent du §1. Les BP des 4080 SUPER, 4070 Ti SUPER, 5070 Ti sont données ici d'après Puget / Wikipédia et non d'après cette page ; à ne pas utiliser sans les revérifier.

Lecture (calculs) :
- L'ordre de génération Qwen3 8B sur les cinq cartes à BP connue (3090, 5070, 5060 Ti, 3060, 4060 Ti) est identique à l'ordre des BP.
- 5060 Ti contre 4060 Ti 16 Go : 51,41 / 34,31 = 1,50 ; BP 448 / 288 = 1,56. Sur Qwen3 14B : 32,91 / 22,36 = 1,47 ; sur gpt-oss 20B : 82,42 / 57,76 = 1,43.
- 3060 12 Go contre 4060 Ti 16 Go : 41,97 / 34,31 = 1,22 ; BP 360 / 288 = 1,25. En 14B, 22,66 contre 22,36 (1,01) : l'avantage de BP disparaît (voir contre-exemples).
- 3090 contre 5060 Ti : 87,45 / 51,41 = 1,70 ; BP 936 / 448 = 2,09.
- 5070 contre 5060 Ti : 59,13 / 51,41 = 1,15 ; BP 672 / 448 = 1,50 (calcul).
- La 5070 Ti (896) égale la 3090 (936) : 87,54 contre 87,45, avec 3 654 contre 2 572 en lecture du prompt (la page le relève elle-même).
- Lecture du prompt : la 4060 Ti 16 Go (1 481) devance la 3060 12 Go (1 119) et la 5060 Ti est à 1 448 : l'ordre de pp n'est pas celui de tg. La 5070 (1 601) est derrière la 4070 (2 064).
- Erreur de la page : le texte dit que la 4060 Ti lit le prompt moins vite qu'une « RTX 3060 16GB » ; cette carte n'est pas dans le tableau et la 3060 12 Go du tableau est derrière la 4060 Ti (1 481 contre 1 119 pour la 3060 12 Go). À ne pas reprendre.
- La page attribue la faible vitesse de la 4060 Ti à sa BP limitée de 288 Go/s.

### B. Puget Systems, « LLM Inference - Consumer GPU performance » (12 cartes, un seul modèle)

- URL : https://www.pugetsystems.com/labs/articles/llm-inference-consumer-gpu-performance/ ; auteur Jon Allman ; publié et mis à jour le 22/08/2024 (la page avertit que le contenu peut dater).
- Logiciel : llama.cpp build 3140 (b3140), CUDA 12.2.0, pilote NVIDIA 560.70, Windows 11 Pro 23H2. Modèle : Phi-3-mini-4k-instruct en GGUF 4 bits (variante exacte non précisée ; le graphique dit « q4 »). 512 tokens pour pp, 128 pour tg, 25 répétitions moyennées. Modèle ~2 Go : tient dans toutes les cartes testées.
- Les chiffres ne sont pas dans le texte : je les ai lus sur les images des graphiques (https://wp-cdn.pugetsystems.com/2024/08/Token-Generation-GeForce.png et https://wp-cdn.pugetsystems.com/2022/08/Prompt-Processing-GeForce.png). Valeurs entières imprimées sur les barres.

| Carte | BP | tg | pp |
|---|---|---|---|
| RTX 4090 24 Go | 1 008,4 | 225 | 10 324 |
| RTX 3080 Ti 12 Go | 912,4 | 192 | 5 456 |
| RTX 4080 SUPER 16 Go | 736,3 | 189 | 8 033 |
| RTX 4080 16 Go | 716,8 | 180 | 7 563 |
| RTX 4070 Ti SUPER 16 Go | 672,3 | 175 | 6 566 |
| RTX 4070 Ti 12 Go | 504,2 | 143 | 5 733 |
| RTX 4070 SUPER 12 Go | 504,2 | 142 | 5 165 |
| RTX 4070 12 Go | 504,2 | 141 | 4 458 |
| RTX 2080 Ti 11 Go | 616 | 96 | 3 373 |
| RTX 4060 Ti 8 Go | 288 | 93 | 3 250 |
| RTX 4060 8 Go | 272 | 89 | 2 527 |
| GTX 1080 Ti 11 Go | 484,4 | 23 | 511 |

Lecture (calculs) :
- Trois cartes à BP identique (4070, 4070 SUPER, 4070 Ti) : tg 141 / 142 / 143, soit +1,4 % entre la première et la dernière ; pp 4 458 / 5 165 / 5 733, soit +29 %.
- 4060 Ti 8 Go contre 4060 : tg 93 / 89 = 1,045 ; BP 288 / 272 = 1,059. pp 3 250 / 2 527 = 1,29 : la lecture du prompt écarte beaucoup plus les deux cartes que l'écriture.
- 3080 Ti (912) : 192 en tg, au niveau de la 4080 SUPER (736, 189) ; mais en pp elle est à 5 456 contre 8 033. Le texte de Puget l'explique par la BP (environ 25 % de plus que les 4080), malgré moins de calcul FP16 (environ 35 contre 50 TFLOPS d'après l'article).
- 4090 contre 4080 SUPER : tg 225 / 189 = 1,19 pour une BP de 1,37 : le gain est inférieur au gain de BP.
- Texte de Puget : la GTX 1080 Ti a une BP comparable à la famille 4070 mais des résultats très inférieurs ; l'article en conclut que le calcul FP16 compte aussi. La RTX 2080 Ti (616 Go/s) est à 96 tokens/s, sous la 4070 (504 Go/s) à 141.

### C. Discussion llama.cpp n°15013, « Performance of llama.cpp on Nvidia CUDA » (tableau communautaire, deux paires du même testeur)

- URL : https://github.com/ggml-org/llama.cpp/discussions/15013 ; ouverte le 01/08/2025 par olegshulyakov (qui tient le tableau) ; commentaires jusqu'en octobre 2026 relevés. HTML brut lu le 18/11/2026.
- Protocole fixé dans le fil : `llama-bench -m llama-2-7b.Q4_0.gguf -ngl 99 -fa 0,1` (Llama 2 7B, Q4_0 : 3,56 GiB, 6,74 Md de paramètres), une seule carte. Le tableau rassemble des testeurs différents, avec des commits différents ; le teneur du fil précise lui-même que « performance may vary depending on driver, operating system, board manufacturer ».

**Paire du même testeur (mike-llamacpp, 02/08/2025, même build 89d10295 (6002)) :**

| Carte | BP | pp512 (FA off) | tg128 (FA off) | pp512 (FA on) | tg128 (FA on) |
|---|---|---|---|---|---|
| RTX 5060 Ti 16 Go (GDDR7, 128 bits) | 448 | 3 737,25 | 90,94 ± 0,02 | 4 195,53 | 93,46 ± 0,01 |
| RTX 4060 Ti **8 Go** (GDDR6, 128 bits) | 288 | 3 394,63 | 63,86 ± 0,01 | 3 803,45 | 64,03 ± 0,53 |

- Précautions : la 4060 Ti de ce test est la version 8 Go (même BP que la 16 Go) ; la 5060 Ti a été lancée sur une machine à 4 cartes 5060 Ti (le testeur indique « found 4 CUDA devices » et une exécution sur carte unique), la 4060 Ti sur une machine à une carte : pas le même hôte.
- Calculs : tg 90,94 / 63,86 = 1,42 (FA on : 1,46) ; BP 448 / 288 = 1,56 ; pp 3 737 / 3 395 = 1,10 seulement. La lecture du prompt est presque à égalité, la génération s'écarte de 42 %.

**Autres lignes du tableau (testeurs et commits différents ; ne pas les présenter comme un test contrôlé), FA off :**

| Carte | BP | tg128 | pp512 | Commit / testeur |
|---|---|---|---|---|
| RTX 5090 | 1 792 (calcul) | 290,02 | 14 073 | 8cf6b42 / totaldev |
| RTX 4090 | 1 008 | 186,21 | 11 993 | 2241453 / lhl |
| RTX 5070 Ti 16 Go | 896 (calcul) | 176,85 | 6 952 | 933414c / TinyServal |
| RTX 3090 | 936 | 158,16 | 5 175 | c76b420 / m18coppola |
| RTX 3080 10 Go | non trouvé | 139,65 | 5 014 | 9c35706 / slaren |
| RTX 5070 12 Go | 672 (calcul) | 127,54 | 5 185 | commit non indiqué / Spyro000 |
| RTX 5060 Ti 16 Go | 448 | 90,94 | 3 737 | 89d1029 / mike-llamacpp |
| RTX 3060 12 Go | 360 | 75,57 | 2 138 | baa9255 / QuantiusBenignus |
| RTX 4060 Ti 8 Go | 288 | 63,86 | 3 395 | 89d1029 / mike-llamacpp |
| GTX 1080 Ti | 484,4 | 62,49 | 1 084 | 9c35706 / ariya |

Autres commentaires du même fil :
- RTX 3060 Ti 8 Go (testeur selfup, 19/09/2026, build e613ef2c8 (11056), CUDA, Ryzen 3800X, DDR4) : tg128 92,23 (FA off) et 96,50 (FA on) ; pp512 2 675 et 2 991. Le message ne précise pas si la carte est la version GDDR6 ou GDDR6X. Comparaison à titre indicatif avec la 5060 Ti du tableau (même BP 448) : 92,23 contre 90,94 ; ce n'est pas un test contrôlé (testeurs, commits, machines différents).
- RTX 3060 12 Go sous WSL2 (grgsim, 21/08/2026, build bb4caa7, pilote 610.53 / CUDA 13.3) : tg128 72,09 (FA off) et 75,58 (FA on). Il note que sous WSL2 une charge GPU en arrière-plan fait passer la génération de 75,58 à 67,27 (environ −11 %).
- Débit apparent (calcul : tg × 3,82 Go, taille du modèle, ÷ BP) pour le tableau FA off : 4060 Ti 244 Go/s soit 85 % de 288 ; 3060 289 soit 80 % de 360 ; 5060 Ti 347 soit 78 % de 448 ; 5070 Ti 676 soit 75 % ; 4090 711 soit 71 % de 1 008 ; 3090 604 soit 65 % de 936 ; 5090 1 108 soit 62 % de 1 792. Le rendement baisse quand la BP monte.

### D. Discussion llama.cpp n°10879, « Performance of llama.cpp with Vulkan » (Vulkan, mêmes protocole, une paire du même testeur)

- URL : https://github.com/ggml-org/llama.cpp/discussions/10879 ; même protocole (Llama 2 7B Q4_0, `-ngl 100 -fa 0,1`). Date d'ouverture du fil non relevée ; commentaires d'octobre 2026 lus le 18/11/2026.
- **Paire du même testeur (ozdogar2, 01 et 02/10/2026, même commit f1cee99, Arch Linux, Mesa RADV 26.2.2, `RADV_PERFTEST=nogttspill`, Resizable BAR actif ; processeurs différents : Ryzen 7 5700X pour la 6800, Ryzen 5 7600X pour la 9060 XT) :**

| Carte | BP | pp512 (FA off) | tg128 (FA off) | pp512 (FA on) | tg128 (FA on) |
|---|---|---|---|---|---|
| RX 6800 16 Go (RDNA 2, 256 bits) | 512 | 1 593,97 | 101,47 ± 0,35 | 1 597,95 | 106,49 ± 0,23 |
| RX 9060 XT 16 Go (RDNA 4, 128 bits) | 320 (déduit) | 2 844,80 | 71,07 ± 0,10 | 3 228,15 | 74,01 ± 0,03 |

  La carte plus ancienne mais au bus plus large écrit 1,43 fois plus vite (101,47 / 71,07 ; BP 512 / 320 = 1,60) ; la carte plus récente lit le prompt 1,78 fois plus vite (2 845 / 1 594). Le même testeur donne aussi, FA on, gpt-oss-20b MXFP4 : 145,9 (6800) contre 105,8 (9060 XT) en génération.
- Lignes du tableau Vulkan (FA off, testeurs et commits différents) : RTX 5060 Ti 93,51 (89f10ba, coopmat2) ; RTX 3060 Ti 86,74 (b42c7fa) ; RTX 3070 78,71 (1b8fb81) ; RTX 3060 75,94 (92c0b38) ; RX 9060 XT 71,07 ; Intel Arc B580 70,14 (pp512 621 ; commit 7f76692) ; RX 7600 XT 53,02 (01d8eaa) ; RTX 4070 92,29 (9a48399).
- Avec BP : B580 (456) à 70,14 est sous la 3060 (360) à 75,94 et sous la 3060 Ti (448) à 86,74 : voir contre-exemples. RX 7600 XT : BP non trouvée.

### E. LocalScore (crowdsourcing, indication seulement)

- URL : https://www.localscore.ai/model/1 (Llama 3.1 8B Instruct, Q4_K_M), /model/2 (Qwen2.5 14B, Q4_K_M), /model/3 (Llama 3.2 1B, Q4_K_M). Projet Mozilla Builders ; aucune date de publication : consulté le 18/11/2026. Logiciel : outil `localscore` de llamafile (basé sur llama.cpp) ; version non trouvée. Chaque ligne est une moyenne de soumissions d'utilisateurs aux machines, limites de puissance et charges variées. Deux lignes pour une même carte avec des mémoires affichées différentes (15 Go / 16 Go) donnent des résultats différents.
- Llama 3.1 8B Q4_K_M (tient dans les 8 Go), tg / pp (tokens/s), valeurs lues dans le HTML brut :

| Carte | BP | tg | pp |
|---|---|---|---|
| RTX 3090 24 Go | 936 | 96,6 | 3 538 |
| RTX 3070 Ti 8 Go | 608 | 83,2 | 2 509 |
| RTX 4070 12 Go | 504 | 76,3 | 3 192 |
| RTX 3060 Ti 8 Go | 448 | 60,2 | 1 839 |
| RTX 3070 8 Go | non trouvé | 60,1 | 2 020 |
| RTX 5060 Ti (affiché 15 Go) | 448 | 59,0 | 2 365 |
| RTX 5070 12 Go | 672 (calcul) | 55,9 | 2 927 |
| RTX 5060 Ti 16 Go | 448 | 51,2 | 2 314 |
| RTX 3060 12 Go | 360 | 50,1 | 1 478 |
| RTX 4060 Ti 16 Go | 288 | 48,3 | 2 233 |
| RTX 4060 Ti 8 Go | 288 | 38,3 | 2 087 |
| RTX 4060 8 Go | 272 | 38,3 | 1 544 |
| RTX 3060 8 Go | 224 | 37,0 | 1 340 |

- Seule source trouvée pour les cartes de bureau « 3060 Ti / 3070 contre 4060 » : 60,2 et 60,1 contre 38,3 (rapport 1,57 ; BP 448 / 272 = 1,65). Mais la pp va dans l'autre sens pour la 4060 Ti 8 Go (2 087) contre la 3060 Ti (1 839). Même source, même modèle et même logiciel, mais machines de la foule différentes : à présenter comme une tendance.
- Paire 3060 12 Go contre 3060 8 Go : 50,1 / 37,0 = 1,35 ; BP 360 / 224 = 1,61.
- Incohérences visibles : 5060 Ti à 59,0 ou 51,2 selon la ligne ; 4060 Ti 8 Go à 38,3 contre 48,3 pour la 16 Go (même BP) ; 5070 (672) à 55,9, sous la 4070 (504) à 76,3 et sous la 3070 Ti. 14B Q4_K_M : 4060 Ti 16 Go 25,6 ; 3060 12 Go 25,1 ; 5060 Ti 16 Go 22,6 (ou 32,9 sur la ligne 15 Go) ; 5070 Ti 25,6 (ligne 16 Go) contre 37,0 (ligne 15 Go) ; 4060 Ti 8 Go, 3060 Ti 8 Go et 3070 8 Go à 3,5, 7,5 et 5,6 (modèle de 9 Go hors VRAM : à ignorer).
- À éviter : les lignes du modèle 1B : la RTX 5070 Ti 16 Go y est à 92,8 tokens/s contre 198 pour la ligne 15 Go ; cause non étudiée.

### F. Hardware Corner, « I Tested Dual RTX 5060 Ti 16GB vs RTX 3090 » (modèles denses, avec deux cartes)

- URL : https://www.hardware-corner.net/guides/dual-rtx-5060-ti-16gb-vs-rtx-3090-llm/ ; « Last updated: Nov 3, 2025 » (ajouts ExLlamaV3 du 09/06/2025) ; auteur Allan Witt. HTML brut lu le 18/11/2026.
- Logiciel : llama.cpp server (version non précisée), pilote NVIDIA 575.57.08, Ubuntu 24.04. Modèles : Qwen3-32B-UD-Q4_K_XL (dense) et Qwen3-30B-A3B-128K-UD-Q4_K_XL (MoE). BP imprimées : 448 par 5060 Ti, 936 pour la 3090.
- Attention : deux cartes contre une ; le test ne donne aucun chiffre pour une 5060 Ti seule.

| Modèle, contexte | 2 × 5060 Ti : tg | 3090 : tg | Rapport |
|---|---|---|---|
| Qwen3 32B dense, ~4K | 18,2 | 35,1 | 1,93 |
| Qwen3 32B dense, ~16K | 14,4 | 30,3 | 2,10 |
| Qwen3 30B-A3B MoE, ~4K | 101,0 | 153,6 | 1,52 |
| Qwen3 30B-A3B MoE, ~16K | 64,6 | 113,8 | 1,76 |

  pp (4K) dense : 544,4 contre 1 087,9 ; MoE : 1 763,4 contre 2 988,6. La page annonce un avantage de 114 % pour la 3090 ; ses propres chiffres donnent +93 % à +110 % sur le dense, le 114 % ne vient pas du tableau (à ne pas reprendre). La page présente la BP comme le facteur décisif pour les modèles denses ; le modèle MoE (peu de paramètres actifs par token) écarte moins les cartes.

## 4. Paires demandées : ce que les sources donnent

| Paire | Mesure, source | Verdict |
|---|---|---|
| RTX 3060 Ti / 3070 contre RTX 4060 | Test contrôlé : non trouvé. Indication : LocalScore 8B, 60,2 / 60,1 contre 38,3 (§3.E). Puget a la 4060 et la 4060 Ti 8 Go mais pas la 3060 Ti | Tendance nette, mais source faible (foule) |
| RTX 3060 12 Go contre RTX 4060 Ti 16 Go | Hardware Corner, Qwen3 8B : 41,97 contre 34,31 ; Qwen3 14B : 22,66 contre 22,36 (§3.A) | La carte au débit le plus haut gagne à 8B (+22 %), à égalité à 14B |
| RTX 4060 Ti 16 Go contre RTX 5060 Ti 16 Go | Hardware Corner : 34,31 contre 51,41 (8B), 22,36 contre 32,91 (14B), 57,76 contre 82,42 (gpt-oss 20B). llama.cpp n°15013 (4060 Ti 8 Go) : 63,86 contre 90,94 | +43 à +50 % pour +56 % de BP |
| RTX 5060 Ti 16 Go contre RTX 5070 12 Go | Hardware Corner : 51,41 contre 59,13 (+15 %). n°15013 : 90,94 contre 127,54 (+40 %, testeurs différents). LocalScore : 51,2 ou 59,0 contre 55,9 | Fourchette de +15 % à +40 % pour +50 % de BP : le gain varie beaucoup d'une source à l'autre |
| RTX 3090 contre cartes 16 Go récentes | Hardware Corner : 87,45 contre 51,41 (5060 Ti) et 87,54 (5070 Ti, BP 896). n°15013 : 158,16 contre 176,85 (5070 Ti) | La 3090 domine les 5060 Ti / 4060 Ti, mais pas la 5070 Ti malgré une BP plus haute |
| Intel Arc B580, RX 9060 XT 16 Go, RX 7600 XT | Vulkan n°10879 (§3.D) : 70,14 ; 71,07 ; 53,02. Paire contrôlée : 9060 XT contre RX 6800 | Test contrôlé B580 / 7600 XT : non trouvé. La B580 est sous sa BP attendue |
| RTX 4060 contre RTX 4060 Ti (8 Go) | Puget : 89 contre 93 (+4,5 %, BP +5,9 %) | Cohérent |

## 5. Ce qu'on peut affirmer

- Sur des mesures d'un même testeur, même modèle, même logiciel, modèle entièrement en VRAM, l'ordre de vitesse de génération des cartes NVIDIA suit l'ordre de leur bande passante : Hardware Corner (5 cartes sur 5, Qwen3 8B) ; Puget : toutes les cartes sauf deux suivent l'ordre des BP (4060, 4060 Ti, trois 4070 à égalité, 4070 Ti SUPER, 4080, 4080 SUPER, 3080 Ti, 4090) ; les deux exceptions sont les cartes plus anciennes GTX 1080 Ti et RTX 2080 Ti (voir §7).
- La BP explique mieux la génération que la génération de la carte ou son calcul : trois cartes de la famille 4070 à BP identique écrivent à 141, 142, 143 tokens/s (Puget) pendant que leur lecture du prompt va de 4 458 à 5 733.
- Une RTX 5060 Ti (448 Go/s) écrit environ 1,4 à 1,5 fois plus vite qu'une RTX 4060 Ti (288 Go/s), pour un rapport de BP de 1,56 (Hardware Corner 8B/14B/20B ; llama.cpp n°15013).
- Une RTX 3060 12 Go (360 Go/s) écrit plus vite qu'une RTX 4060 Ti (288 Go/s), carte pourtant plus récente : 75,6 contre 63,9 sur le tableau n°15013 (deux testeurs, 4060 Ti 8 Go) ; 41,97 contre 34,31 chez Hardware Corner (même testeur, 4060 Ti 16 Go).
- Un mainteneur de llama.cpp décrit la génération comme limitée par la mémoire (« TG is memory-bound ») et la lecture du prompt comme limitée par le calcul ; NVIDIA donne la même explication.
- La BP donne un plafond (tokens/s maximal ≈ BP ÷ taille du modèle lue par token) que les cartes atteignent à 60-85 % sur le test Llama 2 7B Q4_0 (calcul, §3.C).
- Avec un même testeur, l'ordre de la lecture du prompt ne suit pas celui de la génération (4060 Ti devant 3060 en pp à Hardware Corner ; 9060 XT devant RX 6800 en pp, derrière en tg).

## 6. Ce qu'on ne peut pas affirmer

- Que la vitesse soit proportionnelle à la BP : à Hardware Corner, tg ÷ BP passe de 0,12 (4060 Ti) à 0,093 (3090) ; la 3090 écrit 1,70 fois plus vite que la 5060 Ti pour 2,09 fois plus de BP ; la 5070 n'écrit que 15 % plus vite que la 5060 Ti pour 50 % de BP en plus.
- Que cela vaille d'une marque ou d'un logiciel à l'autre : B580 (Intel, Vulkan), RX (AMD, Vulkan) et RTX n'ont pas le même rendement par Go/s.
- Un test contrôlé de la RTX 3060 Ti / 3070 contre la RTX 4060 de bureau : non trouvé (seulement LocalScore).
- Un test contrôlé de la Arc B580 et de la RX 7600 XT contre une RTX : non trouvé. La BP de la RX 7600 XT n'a pas été relevée.
- Un test contrôlé 5060 Ti / 5070 qui concilie les écarts entre sources (+15 % contre +40 %).
- Que les chiffres de LocalScore, des sites de conseils (insiderllm, craftrigs, specpicks, etc. : apparus en recherche, non ouverts, non cités) soient fiables.
- Un classement valable avec un modèle qui déborde de la VRAM (les 14B sur 8 Go chez LocalScore, 3 à 8 tokens/s : la limite devient la RAM et le processeur).

## 7. Contre-exemples et nuances

1. **GTX 1080 Ti (484 Go/s) : 23 tokens/s** et **RTX 2080 Ti (616 Go/s) : 96** contre 141 pour la RTX 4070 (504 Go/s), Puget ; 62,49 contre 75,57 pour la 3060 (360 Go/s), tableau n°15013 (testeurs différents). Puget l'attribue au calcul FP16.
2. **Intel Arc B580 (456 Go/s) : 70,14 tokens/s en Vulkan**, sous la RTX 3060 (360) à 75,94 et la 3060 Ti (448) à 86,74 (tableau Vulkan n°10879, testeurs différents). Je n'ai pas trouvé de source sérieuse qui chiffre la cause (affirmations sur SYCL et les pilotes vues seulement dans des blogs).
3. **RX 6800 (512) devant RX 9060 XT (320) en génération** mais derrière en lecture du prompt (même testeur, §3.D) : la génération la plus récente ne gagne pas en écriture.
4. **RTX 5070 Ti (896) à égalité avec la RTX 3090 (936)** à Hardware Corner (87,54 contre 87,45) alors que la 5070 Ti lit le prompt 42 % plus vite (3 654 contre 2 572). Le même écart de BP (896 contre 936) ne donne pas d'avantage à la 3090.
5. **3060 12 Go ≈ 4060 Ti 16 Go en 14B** à Hardware Corner (22,66 contre 22,36) alors que l'avantage de BP est de 25 % : un modèle de 14B à 16K de contexte sature la 3060 de 12 Go (hypothèse non vérifiée).
6. **5070 contre 5060 Ti** : +15 % (Hardware Corner), +40 % (n°15013), de −5 % à +9 % (LocalScore) : à ne pas annoncer comme proportionnel à la BP.
7. **Lecture du prompt** : l'ordre diffère de celui de la génération (4060 Ti devant 3060 ; 4070 devant 5070 ; 3080 Ti loin derrière 4080 SUPER en pp mais égale en tg  ; sur n°15013, 4060 Ti 8 Go et 5060 Ti sont à 10 % l'une de l'autre en pp (3 395 contre 3 737) mais à 42 % en tg (64 contre 91)).
8. **Charge parasite** : sous WSL2, la génération d'une 3060 perd environ 11 % si le GPU sert aussi à l'affichage (grgsim, n°15013).
9. **Écart de contexte** : Hardware Corner mesure à 16K de contexte (plus lent qu'à contexte vide) : ne pas comparer ces nombres avec ceux de Puget ou de llama-bench à `tg128`.
10. **Page Hardware Corner (§3.A)** : phrase fausse sur la 3060 16 Go ; **page double 5060 Ti (§3.F)** : « 114 % » non retrouvé dans le tableau.

## 8. Liste des sources ouvertes

1. https://www.hardware-corner.net/gpu-ranking-local-llm/ (mise à jour 09/12/2025)
2. https://www.pugetsystems.com/labs/articles/llm-inference-consumer-gpu-performance/ (22/08/2024)
3. https://github.com/ggml-org/llama.cpp/discussions/15013 (CUDA, ouverte 01/08/2025)
4. https://github.com/ggml-org/llama.cpp/discussions/10879 (Vulkan)
5. https://www.localscore.ai/model/1 , /model/2 , /model/3 (consulté 18/11/2026)
6. https://www.hardware-corner.net/guides/dual-rtx-5060-ti-16gb-vs-rtx-3090-llm/ (03/11/2025)
7. https://github.com/ggml-org/llama.cpp/discussions/17621 (30/11/2025)
8. https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ (17/11/2023)
9. https://www.club386.com/nvidia-geforce-rtx-5060-ti-16gb-vs-rtx-3060-ti/ (17/04/2025 : BP 448 des deux cartes ; Procyon Text Generation 2 557 contre 1 774 points, soit 44 % d'écart entre deux cartes à BP égale, sans tokens/s ni détail du test)
10. Wikipédia (séries GeForce 30, 40, 50, Radeon RX 6000, 7000, 9000, Intel Arc), pages ouvertes pour les BP.
11. Tentés sans succès : TechPowerUp (page de vérification anti-robot, non contournée), page Tom's Hardware (corps de l'article absent), Arm « llama-roofline » (non ouverte).
