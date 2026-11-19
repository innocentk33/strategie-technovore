# Bande passante mémoire des cartes graphiques (recherche du 18/11/2026)

Formule : bande passante (GB/s) = bus (bits) × débit par broche (Gbps) ÷ 8.

Chaque chiffre vient d'une page ouverte le 18/11/2026. Quand la bande passante n'est pas écrite sur la page, elle est recalculée et marquée « calcul ».

## Sources ouvertes

- **W30** : https://en.wikipedia.org/wiki/GeForce_RTX_30_series (tableau « Desktop », colonnes Memory GT/s, Size, Bandwidth, Type, Bus width)
- **W40** : https://en.wikipedia.org/wiki/GeForce_RTX_40_series (idem)
- **W50** : https://en.wikipedia.org/wiki/GeForce_RTX_50_series (idem)
- **WR9** : https://en.wikipedia.org/wiki/Radeon_RX_9000_series (idem)
- **NV30** : https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3060-3060ti/ (taille, type, largeur du bus ; pas de GB/s)
- **NV40a** : https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4060-4060ti/ (idem)
- **NV40b** : https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4070-family/ (idem)
- **NV50a** : https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/ (idem)
- **NV50b** : https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/ (idem)
- **NV50c** : https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/ (idem)
- **AMD7600** : https://www.amd.com/en/products/graphics/desktops/radeon/7000-series/amd-radeon-rx-7600-xt.html (Memory Speed, Memory Interface, Memory Bandwidth)
- **AMD9060** : https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9060xt.html (idem)
- **AMD9070** : https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9070xt.html (idem)
- **INTEL** : https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html (fiche officielle B580)
- **PCG** : https://www.pcgamer.com/uk/nvidia-rtx-4060-ti-review-benchmarks-performance/ (tableau 4060 Ti contre 3060 Ti)
- **LCPP** : https://github.com/ggml-org/llama.cpp/discussions/15013 (« Performance of llama.cpp on Nvidia CUDA »)

TechPowerUp (GPU database) n'a pas pu être ouverte : la page renvoie un 403, ou une page de vérification JavaScript avec curl. Aucun chiffre ne vient de TechPowerUp.

## Tableau

La colonne « lu / calcul » dit d'où vient le GB/s. Les Gbps des cartes NVIDIA viennent des tableaux Wikipédia (NVIDIA ne les écrit pas sur ses pages). Les bus NVIDIA ont été recoupés avec les pages NVIDIA quand c'est indiqué.

| Carte | VRAM | Type | Bus (bits) | Gbps | GB/s | Source | lu / calcul |
|---|---|---|---|---|---|---|---|
| RTX 3050 6 Go | 6 Go | GDDR6 | 96 | 14 | 168 | W30 | lu (96 × 14 ÷ 8 = 168, cohérent) |
| RTX 3060 12 Go | 12 Go | GDDR6 | 192 | 15 | 360 | W30 ; bus 192 bits confirmé par NV30 | lu (192 × 15 ÷ 8 = 360) |
| RTX 3060 Ti 8 Go | 8 Go | GDDR6 | 256 | 14 | **448** | W30 ; bus 256 bits confirmé par NV30 ; 448 confirmé par PCG | lu (256 × 14 ÷ 8 = 448) |
| RTX 3070 | 8 Go | GDDR6 | 256 | 14 | 448 | W30 (cellules fusionnées avec la 3060 Ti GA103, voir limites) | lu + calcul (256 × 14 ÷ 8 = 448) |
| RTX 3080 10 Go | 10 Go | GDDR6X | 320 | 19 (Wikipédia écrit « 9,5 GT/s ») | 760 | W30 | GB/s lu ; Gbps calcul (760 × 8 ÷ 320 = 19) |
| RTX 3090 | 24 Go | GDDR6X | 384 | 19,5 (Wikipédia écrit « 9,75 GT/s ») | 936 | W30 | GB/s lu ; bus et Gbps calcul (936 × 8 ÷ 384 = 19,5) |
| RTX 4060 | 8 Go | GDDR6 | 128 | 17 | **272** | W40 ; bus 128 bits confirmé par NV40a | lu (128 × 17 ÷ 8 = 272) |
| RTX 4060 Ti 8 Go | 8 Go | GDDR6 | 128 | 18 | **288** | W40 ; bus confirmé par NV40a ; 288 confirmé par PCG | lu (128 × 18 ÷ 8 = 288) |
| RTX 4060 Ti 16 Go | 16 Go | GDDR6 | 128 | 18 | 288 | W40 (cellule fusionnée avec la 8 Go) ; bus confirmé par NV40a | lu (128 × 18 ÷ 8 = 288) |
| RTX 4070 | 12 Go | GDDR6X | 192 | 21 | 504 | W40 ; bus confirmé par NV40b | lu (192 × 21 ÷ 8 = 504) |
| RTX 4070 Super | 12 Go | GDDR6X | 192 | 21 | 504 | W40 (cellules fusionnées) ; bus confirmé par NV40b | lu + calcul (192 × 21 ÷ 8 = 504) |
| RTX 4070 Ti Super | 16 Go | GDDR6X | 256 | 21 | 672 | W40 ; bus confirmé par NV40b | lu (256 × 21 ÷ 8 = 672) |
| RTX 5060 | 8 Go | GDDR7 | 128 | 28 | 448 | W50 ; bus 128 bits confirmé par NV50a | lu (128 × 28 ÷ 8 = 448) |
| RTX 5060 Ti 8 Go | 8 Go | GDDR7 | 128 | 28 | 448 | W50 ; bus confirmé par NV50a | lu (128 × 28 ÷ 8 = 448) |
| RTX 5060 Ti 16 Go | 16 Go | GDDR7 | 128 | 28 | 448 | W50 ; bus confirmé par NV50a | lu (128 × 28 ÷ 8 = 448) |
| RTX 5070 | 12 Go | GDDR7 | 192 | 28 | 672 | W50 ; bus 192 bits confirmé par NV50b | lu (192 × 28 ÷ 8 = 672) |
| RTX 5070 Ti | 16 Go | GDDR7 | 256 | 28 | 896 | W50 ; bus 256 bits confirmé par NV50b | lu (256 × 28 ÷ 8 = 896) |
| RTX 5080 | 16 Go | GDDR7 | 256 | 30 | 960 | W50 ; bus 256 bits confirmé par NV50c | lu (256 × 30 ÷ 8 = 960) |
| Intel Arc B580 | 12 Go | GDDR6 | 192 | 19 | 456 | INTEL (page officielle) | lu (192 × 19 ÷ 8 = 456) |
| Radeon RX 9060 XT 16 Go | 16 Go | GDDR6 | 128 | 20 (AMD : « up to 20 Gbps » ; Wikipédia : 20,1) | 320 | AMD9060 ; WR9 | lu (« Up to 320 GB/s » ; 128 × 20 ÷ 8 = 320) |
| Radeon RX 7600 XT 16 Go | 16 Go | GDDR6 | 128 | 18 | 288 | AMD7600 | lu (« Up to 288 GB/s » ; 128 × 18 ÷ 8 = 288) |
| Radeon RX 9070 XT | 16 Go | GDDR6 | 256 | 20 | 640 | AMD9070 ; WR9 | lu (« Up to 640 GB/s » ; 256 × 20 ÷ 8 = 640) |

Les chiffres de ce tableau se recoupent tous avec la formule bus × Gbps ÷ 8.

## Ce que ça dit de la phrase de l'auteur

La phrase : « la RTX 4060 a environ 200, la RTX 3060 Ti a presque le double ».

**Verdict : la direction est juste, les chiffres sont faux.**

- La RTX 4060 n'a pas « environ 200 » mais **272 GB/s** (128 bits × 17 Gbps ÷ 8). C'est 36 % de plus que 200.
- La RTX 3060 Ti a bien **448 GB/s** (256 bits × 14 Gbps ÷ 8).
- Rapport exact **3060 Ti / 4060 = 448 ÷ 272 = 1,647**, soit environ **+65 %** (la 4060 a 39 % de bande passante en moins). Ce n'est pas « presque le double » (×2), c'est « les deux tiers de plus ».
- Rapport exact **3060 Ti / 4060 Ti = 448 ÷ 288 = 1,556**, soit environ **+56 %**.
- Pour tomber sur « presque le double », il faudrait que la 4060 soit à environ 230 GB/s ou moins. Avec 272, le rapport reste loin de 2.
- Formulation qui tient : « la 3060 Ti a environ 65 % de bande passante en plus que la 4060 (448 contre 272 GB/s), et environ 56 % de plus que la 4060 Ti (448 contre 288) ».
- La 3060 12 Go (360 GB/s) dépasse aussi la 4060 (272) et la 4060 Ti (288). La 4060 Ti ne fait mieux que la 3060 Ti sur aucun des deux critères, bus ou GB/s.
- Cause : Nvidia a réduit le bus de 256 à 128 bits sur toute la série 4060. La 4060 Ti 16 Go a le même bus de 128 bits et les mêmes 288 GB/s que la 8 Go (NV40a, W40).

### Lien avec les tokens par seconde

La bande passante suit bien l'ordre de vitesse d'écriture dans ce que j'ai trouvé. Test public de llama.cpp, modèle « llama 7B Q4_0 » (3,56 GiB), test tg128 (génération de texte), flash attention désactivée (LCPP) :

| Carte | GB/s | tg128 (tokens/s) |
|---|---|---|
| RTX 3060 Ti | 448 | 92,23 |
| RTX 3060 12 Go | 360 | 72,09 (test sous WSL2) |
| RTX 4060 Ti 8 Go | 288 | 63,86 |

- Rapport tg128 3060 Ti / 4060 Ti : 92,23 ÷ 63,86 = 1,44, contre 1,556 pour la bande passante. L'ordre est respecté, l'écart de vitesse est un peu plus faible que l'écart de bande passante.
- La RTX 4060 (sans Ti) n'a pas de ligne dans cette page : non trouvé.
- Pour la même taille de modèle, les cartes à plus de bande passante écrivent plus vite : RTX 3090 (936 GB/s) 171,19 t/s, RTX 3080 (760) 139,65 t/s, RTX 4070 Ti Super (672) 132,26 t/s.

## Limites

- **Pas de TechPowerUp** : bloqué (403 ou page de vérification JavaScript). Pas de deuxième source indépendante pour les Gbps des cartes NVIDIA : ils viennent de Wikipédia. Les bus (bits) des cartes 3060, 3060 Ti, 4060, 4060 Ti, 4070, 4070 Super, 4070 Ti Super, 5060, 5060 Ti, 5070, 5070 Ti, 5080 sont recoupés avec les pages NVIDIA officielles. Les bus des 3050, 3070, 3080 et 3090 ne viennent que de Wikipédia (le bus de la 3070 est déduit de la cellule fusionnée du tableau et des 448 GB/s).
- **Pages NVIDIA** : elles écrivent taille, type et largeur du bus, mais jamais les GB/s ni les Gbps. Pour NVIDIA, les GB/s sont donc lus sur Wikipédia et recoupés par la formule. Pour la 4060 et la 3060 Ti, le recoupement indépendant est PC Gamer (4060 Ti : 288 GB/s, 128 bits ; 3060 Ti : 448 GB/s, 256 bits). La 4060 (272) n'a que la source Wikipédia plus la formule.
- **Tableaux Wikipédia fusionnés** : les cellules de la 3070, de la 4070 Super et de la 4060 Ti 16 Go sont fusionnées avec une carte voisine. Les valeurs données pour elles sont celles de la cellule fusionnée, confirmées par la formule.
- **Wikipédia écrit « 9,5 » et « 9,75 GT/s » pour les 3080 et 3090** (GDDR6X en signal PAM4) : les vrais débits par broche sont 19 et 19,5 Gbps, déduits des GB/s et du bus (calcul). La page NVIDIA ne les confirme pas.
- **Variantes de la même carte** : la RTX 3060 existe en 12 Go (192 bits, 360 GB/s) et en 8 Go (128 bits, 224 GB/s) (NV30, W30) ; la RTX 4070 a une révision GDDR6 en plus de la GDDR6X (NV40b), dont la bande passante n'est pas relevée ici : non trouvé (pas de calcul fiable sans le Gbps publié). Les chiffres du tableau sont ceux de la version la plus courante, donc la RTX 3060 12 Go et la RTX 4070 en GDDR6X.
- **AMD** : AMD écrit « Up to » (jusqu'à). La page AMD de la RX 7600 XT affiche aussi « Effective Memory Bandwidth : Up to 477 GB/s » : c'est un chiffre marketing qui tient compte du cache Infinity Cache, pas la bande passante physique de la VRAM. Wikipédia écrit 20,1 Gbps pour les 9060 XT et 9070 XT, AMD écrit « Up to 20 Gbps », les deux donnent 320 et 640 GB/s.
- **Cache L2 et bande passante « effective »** : Nvidia met en avant le cache L2 de la série 40 pour parler de bande passante « effective ». Un test sur TechRadar rapporte, pour la 4060 Ti, « 288.0 GB/s memory bandwidth, but 32MB L2 cache boosts effective bandwidth to 554.0 GB/s (according to Nvidia) » (https://www.techradar.com/reviews/nvidia-geforce-rtx-4060-ti). C'est un chiffre de marketing de Nvidia, pas une mesure : je n'ai pas trouvé de mesure indépendante ouverte. Pour la RTX 4060, le chiffre de 453 GB/s cité par un résumé de recherche n'a pas pu être vérifié sur la page d'origine : non trouvé.
- **Bande passante et tokens par seconde** : la relation est approximative. Les tests llama.cpp ci-dessus viennent de PC différents, de pilotes différents et d'un seul modèle de 7B en Q4_0 : à lire comme une tendance, pas comme une mesure contrôlée. Les modèles qui ne tiennent pas dans la VRAM ou le calcul (traitement du prompt) changent le tableau. La phrase « la bande passante compte beaucoup pour les tokens par seconde » est cohérente avec ces chiffres pour l'écriture (tg), mais pas pour la lecture du prompt (pp), que je n'ai pas étudiée.
- **« Moins chère »** : je n'ai pas vérifié le prix. Au lancement, Wikipédia donne 399 $ pour la 3060 Ti et 299 $ pour la 4060 (W30, W40). Le prix d'occasion n'a pas été relevé : non trouvé.
- **Dates** : tous les chiffres sont lus le 18/11/2026. Les spécifications ne bougent pas, mais les tableaux Wikipédia sont modifiables.
