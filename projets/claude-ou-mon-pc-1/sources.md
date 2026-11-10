# Sources vérifiées : « 16 Go suffisent » (double vérification du 05/11/2026)

> Contre-vérification de [`recherche-strata-2026-11-05.md`](recherche-strata-2026-11-05.md) (S1 à S35). Chaque URL a été rouverte le **05/11/2026** (GitHub par l'API et les fichiers bruts, Hugging Face par les README bruts, YouTube par les métadonnées de la page, HN par l'API Algolia, Reddit par le miroir sentinel-team).
>
> **Statuts** : ✅ confirmé ; ⚠️ nuancé (je dis quoi) ; ❌ faux ou introuvable (retiré, à ne pas citer).
> **Types** (repris de la recherche) : `MESURE` d'un utilisateur ou d'un tiers ; `DEV` = affirmation du projet ou de l'auteur du modèle ; `AVIS` ; `CALCUL` = déduction, pas une source.
> **Ta machine** : RTX 5080 16 Go, 32 Go DDR5, Ryzen 7 9700X. Vidéo **calculée** : aucune mesure ici n'a été faite chez toi.

## A. Strata

**S1 ✅ [DEV]** Strata : moteur open source **MIT**, dépôt créé le **24/09/2026**, **40 317 étoiles**, version **v0.2.10 publiée le 02/11/2026**, **1 352** tickets et demandes de fusion ouverts (1 349 dans la recherche, ça bouge d'heure en heure).
→ https://github.com/Niko1221/Strata (API GitHub, 05/11/2026)

**S2 ✅ [DEV]** Le GPU garde les experts chauds, **la RAM garde les experts du premier fichier**, la table de 29 Go reste sur le SSD. Règle : « le modèle tient quand la RAM est au moins égale aux experts **plus environ 10 Go** pour le système et les autres programmes ». RAM + VRAM : Q2_0 37,6 Go ; IQ2_XS 39,2 ; IQ3_XXS 47,0 ; IQ3_S 54,8. Experts en RAM : 34 / 35,5 / 43 / 50 Go ; **Coder 23 Go**.
→ https://github.com/Niko1221/Strata/blob/main/docs/MODELS.md (sections « Pick by memory » et « Will it fit? »)

**S3 ✅ [DEV]** « Avec 64 Go, toutes les tailles passent ; avec 48 Go, Q2_0 et IQ2_XS ; **avec 32 Go, prends le Coder** ». « Une plus grosse carte rend plus rapide mais ne baisse pas la RAM nécessaire, sauf en mode RAM réduite. »
→ MODELS.md (« Will it fit? ») et https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md (« Which model? »).
⚠️ Petite incohérence de la doc : DETAILS.md compte « experts + ~6 Go » de RAM, MODELS.md « experts + ~10 Go ».

**S4 ⚠️ [DEV]** Flash-Next : « **125B avec 6B activés, plus 51B de table n-gram et 4B de MTP** » (= 180 milliards), 512 experts, 10 routés + 1 partagé, contexte 262 144. La fiche du Coder (ISTA) dit **176,9 milliards** pour le modèle de base : le « 177 » de Luke's Dev Lab vient de là.
→ https://huggingface.co/Qwen/Qwen3.8-Flash-Next ; https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF
À dire : « 125 milliards de paramètres, dont seulement 6 travaillent à chaque mot ».

## B. Strata avec 32 Go de RAM

**S5 ✅ [DEV]** Mode RAM réduite, texte exact : « A 32 GB PC with a 24 GB GPU runs Q2_0, IQ2_XS and the Coder this way, and **a 32 GB PC with a 12 to 16 GB GPU runs the Coder**. With a small card most experts come from the SSD and it is much slower. » Donc sur 16 Go de VRAM + 32 Go de RAM, **seul le Coder est annoncé**. La doc ajoute : « A 32 GB RAM computer also needs enough GPU memory and room for buffers; read the launch plan. »
→ MODELS.md, section « Coder » et « Big graphics card, little RAM » (05/11/2026)

**S6 ⚠️ [DEV]** Le Coder (ISTA-DASLab) garde **256 des 512 experts** de chaque couche (choisis sur code, agents, image), un seul fichier IQ1_M, **1,89 bit par paramètre** (dit par la fiche elle-même, pas seulement par un blog), **58,4 Go au total, dont 29,6 Go en mémoire** et 28,8 Go de table sur le SSD. La fiche : « **experimental release** » et « la dégradation hors de ce domaine est un coût accepté ». La phrase « plus faible hors du code et dans les langues autres que l'anglais et le CJK » vient de **MODELS.md de Strata**, pas de la fiche.
→ https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF ; MODELS.md
⚠️ Pour toi : **le français est hors du domaine optimisé** du Coder.

**S7 ✅ [DEV]** Mise à jour de la fiche du **17/10/2026** : SWE-bench Verified **75,60 → 79,20** (base 82,80, soit **95,7 %**) ; LiveCodeBench v6 **86,28 → 87,43** (base 87,43, **100 %**). MODELS.md de Strata affiche encore « 91 % et 99 % » (anciens chiffres).
→ fiche Hugging Face du Coder ; MODELS.md
À citer : « 95 % du score de code du modèle complet, **d'après ses auteurs** ».

**S8 ⚠️ [CALCUL refait] RAM nécessaire au Coder avec tes 32 Go.**
- Règle de MODELS.md : 23 Go d'experts + ~10 Go = **33 Go**. Règle de DETAILS.md : 23 + ~6 = **29 Go**.
- Tes 32 Go de DDR5 = 32 Gio = **34,4 Go** ; Windows en laisse voir environ **31,2 Gio = 33,5 Go** (chiffre relevé sur la machine de S9, même processeur, 32 Go).
- 33,5 − 23 = **10,5 Go** pour Windows, le navigateur, OBS, etc. C'est **pile la marge de 10 Go demandée**, à moins d'1 Go près. Si les « 23 Go » de Strata sont en fait des Gio (la doc mélange), il manque environ 1 Gio et c'est le **mode RAM réduite** qui prend le relais (la carte garde une partie des experts, S5).
- La table de 28,8 Go sur le SSD passe aussi par le cache de fichiers de Windows : elle se bat pour la même RAM libre.
- **Verdict** : le Coder **tient, à ras, navigateur fermé**, et c'est une configuration prévue par la doc (S5) et mesurée une fois sur 31,2 Gio (S9). Flash-Next complet : Q2_0 = 34 + 10 = **44 Go**, IQ3_S = 50 + 10 = **60 Go** → **exclus sur 32 Go** avec une carte de 16 Go (même en mode RAM réduite, il faut 24 Go de VRAM pour Q2_0, S5).

**S9 ✅ [MESURE] La plus proche de ta machine.** « guilleortas », ticket #4997, mesuré le **02/11/2026** : **RTX 5070 Ti 16 Gio, Ryzen 7 9700X, 31,2 Gio de RAM**, 990 PRO 2 To, Windows 11, pilote 621.01, Strata 0.1.55 (moteur 0.1.54), **Coder IQ1_M**, contexte 65 536, réglages d'installation inchangés (`--resident-experts`, cache KV int8, MTP). Médianes sur 3 essais : chat court **70,4 tok/s** (60,5-95,7), premier mot en 0,39 s ; lecture d'un prompt de 4 000 tokens **2 534 tok/s**, de 16 000 tokens **3 134 tok/s** ; session d'agent 5 tours (12 892 tokens de contexte au dernier) **78,7 tok/s** (59,0-88,5), 69 % de cache. Écrit en tête : « **Speed only: no correctness check was run** ».
→ https://github.com/Niko1221/Strata/issues/4997
Une 5070 Ti (672 Go/s), pas une 5080 (960 Go/s) : ta carte devrait faire au moins aussi bien, mais **ce n'est pas mesuré**.

**S10 ✅ [MESURE]** Ticket #2250 (13/10/2026) : Radeon 9600 XT 16 Go, Ryzen 7 5700X, **30,3 Gio de RAM**, Linux, Strata 0.1.43, Coder : **37,6 tok/s** en chat court, **41,7** en session d'agent, lecture de prompt 906-967 tok/s. Ticket fermé. ⚠️ Sa config comprend un « control vector » expérimental de vitesse (option manuelle).
→ https://github.com/Niko1221/Strata/issues/2250

**S11 ✅ [MESURE] Les 5080 mesurées sur Strata ont 64 Go de RAM ou plus.**
- « baiqvesse », #5115, 03/11/2026 : RTX 5080 16 Go, Ryzen 9 9950X, **2 × 32 Go DDR5-6400**, pilote 621.01, Flash-Next IQ3_S. Moyennes croisées : moteur 0.1.54 **114,1 tok/s**, moteur 0.1.56 **85,5 tok/s** → **−25,1 %** en écriture, −13,5 % en lecture de prompt. Contexte max réglé très haut (524 288), réglages avancés à la main.
→ https://github.com/Niko1221/Strata/issues/5115
- « robsop99-beep », #5121, 03/11/2026 : « 0.1.56 : 31 tok/s, 0.1.54 : 88 tok/s » sur RTX 5080 16 Go IQ3_S ; corps du ticket : « Strata 0.2.10, 64 GB RAM, Win11 Pro, 617.42 », rien d'autre. ⚠️ Rapport très maigre.
→ https://github.com/Niko1221/Strata/issues/5121

**S12 ✅ [MESURE]** « Retarel », #5237, 04/11/2026 : **RTX 5080 16 Go** (seule carte, branchée à l'écran), Ryzen 9 9950X3D, **96 Go DDR5**, Windows 11, Strata 0.2.10 (moteur 0.1.56), Flash-Next *Uncensored* IQ3_XXS (paquet tiers) : anglais **106 / 99 / 97 tok/s** (court / 4K / 16K), lecture 2 162 (4K) et 3 899 tok/s (16K). Zone d'experts en RAM **49,80 Gio**, « environ 25 Go de RAM restent libres ». Sans réserve de VRAM : alertes « 279-531 Mio libres » ; `--vram-reserve-mib 1472` les supprime à −0 à −4 %.
→ https://github.com/Niko1221/Strata/issues/5237

**S13 ✅ [MESURE]** « ShaggyDragon », #5291, 05/11/2026, RTX 5080, moteur 0.1.56 : fidélité de IQ3_S (83,60 Go, référence), UD-IQ4_XS (93,67 Go) et UD-Q4_K_XL (111,33 Go). UD-IQ4_XS est le mieux calibré, mais l'auteur précise que l'écart sur le premier mot prédit est « dans le bruit ». Mesure de précision, pas de vitesse, et **hors de portée de 32 Go**.
→ https://github.com/Niko1221/Strata/issues/5291

**S14 ⚠️ [MESURE d'un bug, non confirmé par le projet]** Tickets #5043, #5046 (compte « fengjiegithub ») et #5055 (compte « xiaojack49519 »), 03/11 : **deux comptes, même machine décrite** (Windows 11, **Intel Core Ultra 9 285K**, RTX 5080 16 Go, pilote 617.42, **95 Go de RAM**, Strata 0.2.9 + moteur 0.1.55) : IQ3_S et IQ3_XXS produisent des « non-finite logits » avec tous les moteurs essayés ; reproduit aussi sur 0.1.56 (commentaire du 03/11). Pas de réponse du développeur.
→ https://github.com/Niko1221/Strata/issues/5055 et /5043
À dire au plus : « un utilisateur de 5080 signale un bug ».

**S15 ⚠️ [DEV]** TROUBLESHOOTING.md : au premier lancement, Strata « charge 35 à 55 Go dans ta RAM » et **la souris peut se figer quelques minutes** (plus de 10 min : redémarrer) ; sans réglage, **1 536 Mio de VRAM** restent libres pour le bureau sur une carte de 16 Go ou moins qui affiche l'écran ; sur un PC à ~32 Go, `--resident-budget-gib N` peut bloquer (#649) et 0.1.40 ralentissait en lisant le disque (#1194, corrigé en 0.1.40.2) ; sous 24 Go de VRAM, le lecteur d'images tourne sur le processeur. ⚠️ La chute **100 → 14 tok/s** ne vient pas du réglage par défaut : elle arrive quand on force `--expert-cache N` trop grand et que la VRAM tombe à 0 Mio (#781, #831).
→ https://github.com/Niko1221/Strata/blob/main/docs/TROUBLESHOOTING.md

**S16 ✅ [DEV, ancien]** Vitesses de la doc (moteurs anciens) : RTX 5070 12 Go, Ryzen 5 7600, 64 Go, moteur 0.1.26 : Q2_0 94, IQ2_XS 79, IQ3_XXS 62, IQ3_S 53, **Coder 55 tok/s** (128K : 76 / 63 / 49 / 46 / 43). RX 9070 XT 16 Go, Ryzen 9 3900X, 47 Go, Linux : Q2_0 60, IQ2_XS 52, **Coder 44**. RTX 5060 Ti 16 Go : « **Not measured** », estimé à ±20 % (Q2_0 ~80, IQ3_XXS ~66), avant le moteur 0.1.13. La doc prévient : « pas remesuré en entier pour la version actuelle ». Aucun chiffre de 5080 dans la doc.
→ MODELS.md (« Speed ») et DETAILS.md (« Other GPUs (estimated) »)

**S17 ✅ [AVIS]** HN « Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s », 04/10/2026, **940 points**. Citations retrouvées mot pour mot :
- imnotr0b0t : « Does the "Coder" variant at 32 GB actually feel usable for real coding work? » ; **nacs** : « Coder is not as good and seems to have noticable loss. Use the normal one » ;
- 0xbadcafebee : Q1 « with half the experts ripped out », pas fiable pour du code long ;
- roscas : Coder **~30 tok/s**, RTX 3080 **10 Go**, Ryzen 3600X, 48 Go ;
- bitexploder : une 4080 « autour de 40 t/s » sur un « MoE caching build » (⚠️ pas forcément Strata, RAM non dite) ;
- theodorton : RTX 3090 + 64 Go DDR4, « Strata reserves ~28GB system RAM » ;
- Jackson__ : vision, erreur médiane **154,8 px** avec Strata contre **46,5 px** avec les mêmes poids dans llama.cpp ;
- XCSme : RTX 3090 + 128 Go DDR4 ; amitp85, ricardobeat, spockz : doutes sur la qualité.
→ https://news.ycombinator.com/item?id=49953495

## C. Autres Qwen sur cartes de 16 Go

**S18 ✅ [MESURE] Qwen3.8-27B sur RTX 5080 16 Go** (dépôt `sudoingX/qwen38-mtp`, contributeur @ChumBoxBaron) : **53,4 tok/s sans MTP → 101,3 avec MTP** (n-max 2, acceptation 0,53-0,95). La note de bas de page, **intitulée « RTX 5080 16GB »**, donne le fichier : **unsloth Q3_K_M**, contexte 65 536, cache KV q4_0, llama.cpp b10488, Windows 11 Pro / CUDA 13.3, VRAM 14 445 → 15 359 Mio, réflexion désactivée. Le lien ligne ↔ fichier est donc **explicite**, pas une déduction. Une seule mesure.
→ https://github.com/sudoingX/qwen38-mtp (README, branche master)

**S19 ⚠️ [MESURE]** Même dépôt, une seule carte de 16 Go, 27B :
- RTX 5060 Ti 16 Go, **26,3 → 59,5** (n4), fichier « Q4-XYZ-v2 » = **quimmedes/Qwen3.8-27B-XYZ, 15,06 Go** (identifié par la note) ; le « 50,0 → 59,3 » est le balayage **du même contributeur**, pas d'un autre utilisateur ; n-max 6 : mémoire pleine au chargement ;
- RTX 4060 Ti 16 Go, même fichier : **17,6 → 40,0** (n3) ;
- RX 9060 XT 16 Go : 15,2 → 28,7 ; RTX 3080 Ti Laptop 16 Go (UD-Q3_K_XL) : 14,8 → 28,6.
- Le dépôt écrit aussi : unsloth **Q4_K_M (17,11 Go)**, IQ4_NL (16,34) et UD-Q4_K_XL (17,92) « **ne tiennent pas** sur une seule carte de 16 Go ».
→ même page

**S20 ✅ [MESURE auto-déclarée + calcul]** **Kai**, « Is 16GB All You Need for Serious Local LLM? », **07/10/2026**, **511 842 vues** au 05/11. Description : « 16GB of VRAM now runs Qwen 3.8 27B at **45 tokens a second on an RTX 5060 Ti** » ; le GSQ-RCO d'ISTA fait **11,8 Go** ; Q4_K_M = 17,44 Go, ne tient pas ; cache KV **64 Ko par token** (128K = 8 Go de plus) ; deux réglages (vision désactivée, cache 8 bits) : **~47 000 → ~110 000 tokens** ; « de 3 à 70 tokens par seconde » selon que ça tient ou déborde ; Claude Code dépense **30 000 tokens** avant ton premier mot ; rentabilité : **~97 jours d'usage non-stop** ; 5060 Ti à 789 $ (+84 %). « Speeds are **self-reported** by the owners ».
→ https://www.youtube.com/watch?v=i9mRnbdDYxk

**S21 ⚠️ [MESURE] (corrigé le 07/11/2026)** La vidéo est sur la chaîne espagnole **Globalcobots** (1 730 abonnés, présentateur « Hugo ») : **« Hardware IA » n'est qu'un hashtag** de la description. « Qwen 3.8 27B en dos GPUs de 16 GB: de 13 a 66 tokens », **01/09/2026**, 18 948 vues au 07/11. Machine : Core Ultra 270K Plus, RTX 5080 et RTX 5060 Ti, **64 Go DDR5-6000**, LM Studio. Sous-titres auto (07/11) : contexte **8 000 tokens**, il décharge « algunas capas » de la GPU (01:42), garde ~15 Go de VRAM, MTP activé ; **13 tok/s** (03:14), puis à 03:23 : « es normal porque parte del modelo lo ha cargado en la memoria RAM ». Le fichier n'est pas nommé pour la 5080 ; pour la 5060 Ti, « el Q4 » (03:34), 14,74 tok/s (la description dit 14,5). Description : 5080 « 1.500 euros ». ❌ Le « 7,3 tok/s » attribué à llmrun.dev : introuvable, retiré.
→ https://www.youtube.com/watch?v=rH993Bf1sK8
À dire : « dans une vidéo espagnole, un utilisateur » (pas de nom de chaîne).

**S22 ✅ [MESURE]** Autodidacts (Curiositry, **23/08/2026**) : **ordinateur portable** RTX 3080 16 Go (« I just bought a new old laptop… 16gb of VRAM ») : 27B **UD-IQ3_XXS** + cache KV quantifié : « **about 20–30 tokens per second** », variable selon le contexte ; UD-Q5_K_M : **~1,5 t/s pendant 36 heures** pour un script.
→ https://www.autodidacts.io/how-to-fit-qwen3-8-27b-into-16gb-vram-run-with-llama-cpp-rtx-3080-flags-quantizations/

**S23 ✅ [MESURE, Qwen3.6]** dev.to (Rost, « May 24 ») : **RTX 4080 16 Go** ; Qwen3.6-27B IQ3_XXS **45 → 75 tok/s** avec MTP, mais contexte moyen **80K → 40K** ; Qwen3.6-35B-A3B IQ3_S **146 → 189 tok/s**, contexte moyen 10-15K, « impractical ». **Qwen3.6, pas 3.8.**
→ https://dev.to/rosgluk/qwen-36-27b-and-35b-mtp-vs-standard-on-16gb-gpu-42jd

**S24 ✅ [MESURE contestée, Qwen3.6]** r/LocalLLaMA (miroir, u/gaztrab, 109 points, ~mai 2026) : **RTX 5080 16 Go, Ryzen 9 9950X, 128 Go**, llama.cpp b9204 ; 35B-A3B UD-Q4_K_XL : **56 tok/s à 128K** (97 sans MTP en contexte court) ; 27B IQ3_XXS + MTP (12,45 Go, tout en VRAM) : **73 tok/s en moyenne**. **128 Go de RAM**, pas 32.
→ https://reddit.sentinel-team.org/posts/1tiixql/snapshots/2026-05-21T05%3A05%3A58.868571Z

**S25 ✅ [MESURE, Qwen3.6] La plus propre en 16 Go + 32 Go (sans Strata).** r/LocalLLaMA (miroir), u/marlang, **576 points**, ~avril 2026 : **RTX 5070 Ti 16 Go, Ryzen 9800X3D, 32 Go DDR5** (« DDR5-6000 » écrit par l'auteur dans sa 3e mise à jour), llama.cpp b8829, Windows : Qwen3.6-35B-A3B **UD-Q4_K_M (22,1 Go)**, `--n-cpu-moe 20` : **78,7 tok/s** (51,2 avec `--cpu-moe`), 12,7 Go de VRAM ; version finale mesurée avec `llama-bench` : **tg128 ~98 tok/s**, contexte 128K. Ses premiers chiffres de lecture de prompt étaient faux (il l'a corrigé).
→ https://reddit.sentinel-team.org/posts/1sor55y/snapshots/2026-04-25T00%3A46%3A56.728262Z

**S26 ✅ [AVIS]** HN (fil S17) : ohyes, « qwen3.8 quants (q3) effectively on a 5070 ti » ; latentsea, IQ3_S du 27B sur une 5060 Ti ; Moon_Y, installé en moins de 20 minutes sur une RTX 5070 ; 4ggr0 (RTX 3080 + 16 Go de RAM) → jonatron : « With that hardware, I wouldn't waste my time ».

**S27 ❌ retiré.** La phrase « UD-Q4_K_XL sur 16 Go de VRAM + 32 Go de RAM à plus de 15 tok/s » n'existe pas à la source. La page TakiTakiTa vise une RTX 3050 et annonce 5 à 10 tok/s. Ne pas citer.

**S28 ⚠️ [DEV, secondaire]** launchboosts.com (05/10/2026), article « researched and drafted with AI assistance » : Coder 1,89 bit, 32 Go minimum, 50,6 / 44,0 tok/s, chiffres repris de VRAM Calculator et mesurés sur une **RTX 5070 12 Go avec 64 Go**. Pas une mesure à 32 Go : **ne pas citer**, S2/S5/S16 suffisent.

## D. Qualité face à Claude

**S29 ✅ [DEV]** Fiche Qwen3.8-27B (publiée le **05/08/2026**), modèle complet, harnais de Qwen : Terminal Bench 2.1 **73,0** (Opus 4.6 Max 78,2) ; SWE-bench Pro **61,7** (53,4) ; GPQA Diamond 89,2 (91,3) ; HLE 30,8 (40,0) ; LiveCodeBench v6 **90,3** (88,8) ; IFBench 79,5 (62,5). Pas de GPT ; le seul Claude est **Opus 4.6 (Max)**.
→ https://huggingface.co/Qwen/Qwen3.8-27B

**S30 ✅ [DEV]** Fiche Flash-Next : SWE-bench Pro **62,5** (Opus 4.6 Max 53,4, chiffre officiel d'Anthropic, les autres via Claude Code) ; DeepSWE 1.1 58,7 ; GPQA 91,7 (91,3) ; HLE 35,9 (40,0) ; LiveCodeBench v6 91,9 (88,8).
→ https://huggingface.co/Qwen/Qwen3.8-Flash-Next

**S31 ✅ [MESURE indépendante]** Artificial Analysis, indice **v5.0.1**, Qwen3.8-27B (xhigh) contre **Claude Opus 5 (High)** : **Terminal-Bench 4.0 : 6 % contre 46 %** ; AutomationBench-AA 48 % / 54 % ; AA-Briefcase 1 391 / 1 557 ; vitesse API 46 / 76 tok/s ; sortie 3 $ / 25 $ le million de tokens ; indice du Qwen : **20**.
→ https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-claude-opus-5-high
⚠️ Le **52** des articles d'août est l'indice **v4.1.1** (Qubrid le dit) : ancienne échelle, ne pas comparer à 20. Qubrid : indice « agentique » **51, au-dessus d'Opus 4.8 de moins d'un point** (pas « un demi-point »).
→ https://www.qubrid.com/blog/qwen38-27b-benchmarks-official-and-independent-results

**S32 ✅ [MESURE]** Quesma (Piotr Migdał, **26/08/2026**), GPU loués L40S / H100 / H200, fichiers Unsloth : **Q4_K_M (17 Go) égale le BF16** sur Terminal-Bench 2.1 ; **UD-Q2_K_XL (10,7 Go)** : baisse nette, « still the level of Opus 4.7 or Gemini 3.1 Pro », environ **un quart de tokens en plus** ; **1 bit : effondrement**. Pas de fichier ISTA.
→ https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/

**S33 ✅ [DEV]** Fiche ISTA du 27B : **IQ3_XXS (10,1 Go)** LiveCodeBench v6 **84,57** contre **85,71** en BF16 ; **IQ3_S (11,8 Go)** : 85,71, « task-lossless » (AIME25 identique, GPQA à −0,51). ⚠️ Mesures d'ISTA, avec leur harnais (le BF16 y fait 85,71, Qwen annonce 90,3) : pas de comparaison indépendante trouvée.
→ https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF

**S34 ✅ [anecdote d'un tiers]** MindStudio (septembre 2026), un utilisateur sur **4 × RTX 3090** : 27B en FP16 meilleur que Flash-Next en INT4 pour l'agentique longue, Flash-Next préféré pour la conversation. Sans rapport avec 16 Go.
→ https://www.mindstudio.ai/blog/qwen-3-8-27b-vs-flash-next-local-agents

## E. Vidéos (vues relevées le 05/11/2026)

**S35 ⚠️ [vidéos, descriptions seulement]**

| Vidéo | Chaîne | Vues | Date | Vérifié |
|---|---|---|---|---|
| [A 125B Local Model on a 16GB GPU: Fast, But Is It Smart?](https://www.youtube.com/watch?v=B77LasklmZU) | Zero to MVP | 73 004 | 05/10 | ✅ RTX 4060 Ti 16 Go, Ryzen 7, **128 Go de RAM**, Strata compilé, agent Pi, 3 tâches. Pas de chiffre dans la description. |
| [Qwen 3.8 27B vs Strata Coder - Local LLM battle](https://www.youtube.com/watch?v=xiMAxAQAfC4) | Luke's Dev Lab | 85 111 | 23/10 | ✅ « both of which can run at reasonable speeds on a **16GB GPU with 32GB RAM** », 6 tests. ⚠️ « 40 contre 17 tok/s, carte à 70 W » : **pas vérifiable** (rien dans la description, pas de transcription). À revoir à l'œil avant de le citer. |
| [125B AI on a Gaming PC? Strata Tested on RTX 5090…](https://www.youtube.com/watch?v=PJmC9w47_sg) | Stef from Samayas | 13 317 | 06/10 | ✅ Claude Code + Strata, C#/.NET : « **The Coder variant failed** to complete the task » ; Q2 ~**56 min** ; Swift 1.5 ~5 min (règle non suivie) ; **IQ3_S 4 min 05**, appli qui marche ; IQ2_XS sur 5090 portable 6 min 26. « Not a universal benchmark. » RTX 5090, pas 16 Go. |
| [Is 16GB All You Need for Serious Local LLM?](https://www.youtube.com/watch?v=i9mRnbdDYxk) | Kai | 511 842 | 07/10 | ✅ voir S20. Pas de Strata. |
| [Qwen 3.8 Flash Next Tested - 16GB Local LLM setup](https://www.youtube.com/watch?v=s4cTVRH2ReA) | Luke's Dev Lab | 163 557 | 14/09 | ✅ titre, date, vues. |
| [Strata GitHub Explained…](https://www.youtube.com/watch?v=hJ_Iw2E7cnc) | Alex Hitt | 4 326 | 01/10 | ✅ chapitres « 95 tokens per second » et « Windows Task Scheduler's 14-minute bottleneck ». |

## F. Contradictions, après vérification

1. **Unsloth, « 32 Go » ou « 75 Go »** ⚠️ : la page dit « at least 75 GB of RAM » et « the smallest quant works on 32GB RAM » ; son tableau compte la **mémoire totale (RAM + VRAM)** et le plus petit fichier (UD-IQ1_S) fait **72,5 Go**, donc le reste se lit sur le SSD (mmap), sans vitesse publiée. Corrige la recherche : ce n'est pas « seulement avec Strata », mais **sans Strata, à 32 Go, ça lit le disque**. → https://unsloth.ai/docs/models/qwen3.8-next
2. **Coder 91 % ou 95,7 %** ✅ : 95,7 % depuis le 17/10 (S7).
3. **125, 177 ou 180 milliards** ✅ : S4.
4. **Indice AA 52 ou 20** ✅ : v4.1.1 contre v5.0.1 (S31).
5. **3 à 100 tok/s pour « 16 Go »** ✅ : Kai dit « 3 to 70 » ; sur 5080, 13 (Q4 qui déborde, vidéo espagnole de Globalcobots, S21) contre 53 → 101 (Q3_K_M, MTP, sudoingX).
6. **5080 sous Strata : 114 / 85 / 88 / 31 tok/s** ✅ : moteurs 0.1.54 contre 0.1.56, machines à 64 Go (S11).

---

## Ce que la vidéo peut affirmer

1. Sur une carte de 16 Go, **Qwen3.8-27B tient en entier en 3 bits** (fichier de 11,8 Go chez ISTA) ; sur une RTX 5080, un utilisateur publie **53 tok/s, et 101 avec la prédiction multi-tokens** (S18, S33).
2. **Le Q4 « par défaut » ne tient pas** dans 16 Go (17 Go et plus) ; quand il déborde, la vitesse s'effondre : **13 tok/s sur une 5080** d'après une vidéo espagnole (S19, S20, S21).
3. **Pour le 27B, tes 32 Go de RAM ne jouent presque aucun rôle** : tout est dans la carte. Le vrai plafond, c'est le contexte : 64 Ko par token, soit 8 Go de plus pour 128 000 tokens (S20).
4. Strata fait tourner un modèle de **125 milliards de paramètres** sur un PC de joueur en gardant les experts dans la RAM ; **avec 32 Go, la doc ne prévoit que le Coder**, une version réduite pour le code qui garde la moitié des experts (S2, S3, S5, S6).
5. Le Coder sur 32 Go, **ça passe à ras** : 23 Go d'experts + ~10 Go pour Windows, sur environ 33,5 Go visibles (S8, calcul) ; un utilisateur avec **le même processeur que toi, une 5070 Ti et 31,2 Gio de RAM** mesure **70 tok/s** (S9), **sans aucun test de qualité**.
6. Ses auteurs annoncent **95 % du score de code** du modèle complet (S7), mais un utilisateur de HN le juge « pas aussi bon, avec une perte notable » (S17), et dans le test Claude Code de Samayas (RTX 5090), **il a échoué** (S35).
7. Sur les tests de Qwen, le 27B bat **l'ancien Opus 4.6** en code ; sur ceux d'Artificial Analysis, il est **loin d'Opus 5** en agent de terminal : **6 % contre 46 %** (S29, S31).
8. Donc, honnêtement, « **16 Go suffisent** » veut dire : 16 Go suffisent pour **un bon modèle de 27B qui tient en entier dans la carte**, ou pour **la version réduite pour le code** de Flash-Next avec 32 Go de RAM, à ras. Pour le Flash-Next complet, il faut **48 à 64 Go de RAM**, pas une plus grosse carte.

## Ce qu'elle ne doit pas dire

- « J'ai testé », « sur ma 5080 » : **aucune mesure Strata n'existe sur une 5080 avec 32 Go de RAM**, et rien n'a été mesuré chez toi.
- « 16 Go suffisent pour Flash-Next » sans préciser que c'est **le Coder** (moitié des experts) et que le complet veut 48-64 Go de RAM.
- « Le Coder vaut le modèle complet » ou « vaut Claude » : 95 % est le chiffre de ses auteurs, sur du code en anglais ; aucun test de qualité indépendant, un échec documenté, et **le français est hors de son domaine optimisé**.
- « Le 27B est au niveau de Claude » : il bat Opus 4.6 **sur les tableaux de Qwen**, avec le modèle complet, pas le fichier de 12 Go ; contre Opus 5, c'est 6 % contre 46 % en terminal.
- « 70 tok/s sur une 5080 » : c'est une **5070 Ti**, une seule mesure ; et ne mélange pas les 114 tok/s des 5080 à 64-96 Go de RAM avec ta configuration.
- L'indice « 52 » d'Artificial Analysis (ancienne échelle), le « 7,3 tok/s » de llmrun (introuvable), les « 15 tok/s en 16 + 32 Go » (S27, inventé ailleurs), les chiffres de launchboosts (S28).
- « Strata est stable » : −25 % de vitesse entre deux versions du moteur (S11), un bug signalé sur 5080 (S14), un projet de six semaines avec plus de 1 300 tickets ouverts (S1).
- Les « 40 contre 17 tok/s à 70 W » de Luke's Dev Lab, tant que tu ne les as pas revus dans la vidéo.

## G. Ajouts du 07/11/2026 (script V3)

> Recherche de trois agents le 07/11, puis contre-vérification à la main de S36, S37, S38 (fichiers d'unsloth) et S40. Les autres faits viennent de pages lues par les agents (URL et citation données).

**S36 ✅ [MESURE]** Steam Hardware Survey, **octobre 2026**, VRAM : **8 Go 26,92 %** (+0,21), **16 Go 26,35 %** (−0,86), **12 Go 12,91 %**, 6 Go 5,20 %, 4 Go 5,54 %, 24 Go 5,40 %. Le 16 Go était premier en juillet (25,90 % contre 25,32 %, presse du 4-6 août).
→ https://store.steampowered.com/hwsurvey/ (relu le 07/11) ; https://www.club386.com/steam-hardware-survey-july-2026/

**S37 ✅ [DEV + CALCUL]** config.json de Qwen3.8-27B : **64 couches, dont 16 à attention complète** (les 48 autres en Gated DeltaNet, état de taille fixe), 4 têtes KV, head_dim 256. Cache KV en bf16 : 16 × 4 × 256 × 2 × 2 = **65 536 octets = 64 Kio par token** ; 8 192 tokens = 512 Mio ; 128K = 8 Gio. Mesure concordante : llama.cpp « added 3,640 MiB of VRAM for 57,344 tokens ».
→ https://huggingface.co/Qwen/Qwen3.8-27B/raw/main/config.json (relu le 07/11) ; https://computingforgeeks.com/run-qwen3-8-27b-locally/ (27/09/2026)

**S38 ✅ [DEV]** Tailles exactes (API Hugging Face, 07/11 ; Go = 10⁹ octets) : unsloth **UD-Q4_K_M 16,46 Go**, **UD-IQ4_XS 14,25 Go** (13,27 Gio, ton fichier), UD-Q3_K_XL 13,15, UD-IQ3_XXS 10,93 ; lmstudio-community **Q4_K_M 16,81 Go** ; bartowski Q4_K_M 17,44, Q3_K_M 13,40 ; ggml-org Q4_K_M **18,97 Go** ; ISTA **IQ3_S 11,77 Go**, **IQ3_S-mtp 12,12 Go**, **IQ3_XXS 10,09 Go**. Une carte de 16 Gio = 17,18 × 10⁹ octets. ⚠️ unsloth n'a plus de Q3_K_M simple (le fichier de S18 a pu être retiré ou renommé).
→ https://huggingface.co/api/models/unsloth/Qwen3.8-27B-GGUF/tree/main (et les dépôts cités)

**S39 ✅ [DEV + CALCUL]** Bande passante : RTX 5080 **960 Go/s** ; RTX 5060 Ti **448 Go/s** (page de comparaison NVIDIA) ; RX 9070 XT **640 Go/s** ; RX 9060 XT **320 Go/s** (pages AMD). DDR5-6000 double canal : 6 000 × 8 × 2 = **96 Go/s théoriques** (calcul). Plafonds avec IQ3_S-mtp (12,12 Go) : 26 / 37 / 53 / 79 tok/s (calcul).
→ https://www.nvidia.com/en-us/geforce/graphics-cards/compare/ ; https://www.amd.com/en/products/graphics/desktops/radeon/9000-series/amd-radeon-rx-9070xt.html ; …/amd-radeon-rx-9060xt.html

**S40 ✅ [MESURE] Ton fichier exact, sur une autre carte.** Paul's Programming Notes, **23/08/2026** : RTX 5060 Ti 16 Go, **unsloth UD-IQ4_XS**, llama.cpp, toutes les couches sur la carte, contexte 65 536, cache KV q4_0, flash attention : **≈ 24,9 tok/s** (21,9 après un prompt de 5 000 tokens), 15 769 Mio utilisés sur 16 311. « spilling to system RAM collapses throughput ». Plafond 448 ÷ 14,25 ≈ 31 : environ 80 %. Sur une 5080, le même rendement donnerait ~50 tok/s : **calcul, pas une mesure**.
→ https://www.paulsprogrammingnotes.com/2026/08/running-qwen-3-8-27b-16gb.html (relu le 07/11)

**S41 ✅ [MESURE, Qwen3.6]** Dépôt sudoingX/qwen38-mtp, `sweeps/rtx-5060-ti.md` (contributeur @jaisusx, llama.cpp b10472, 17/08/2026, contexte 32K) : fichier **Qwen3.8-27B** « Q4-XYZ-v2 » de 15,06 Go qui tient **26,3 tok/s** ; son ancien réglage, **Qwen3.6-27B** (version précédente) Q4_K_M qui « spilled ~3 GB of weights to host RAM on the same card » **7,7-9,2 tok/s**. Conclusion : « A file that fits VRAM is worth more than the MTP flag. » ⚠️ Les deux chiffres ne sont pas le même modèle (3.6 qui déborde, 3.8 qui tient) : dis-le comme un avant / après sur la même carte.
→ https://github.com/sudoingX/qwen38-mtp (README et sweeps, branche master)

**S42 [inspiration, pas une source de chiffres]** Bruno Vega, « What's the Best AI Model Your GPU Can Actually Run? (4GB to 16GB VRam) », **03/11/2026**, 61 806 vues au 07/11 (364 abonnés, lancée avec Kai). Repris pour la V3 : la carte vue comme un budget en trois lignes, Go contre Gio, plafond = bande passante ÷ taille. Tous les chiffres du script sont recalculés à partir de S36 à S41 ; ses exemples et ses phrases ne sont pas repris. Critiques de son public : 16 Go arrive tard (14 min), voix et script jugés « IA », la confusion Go / Gio demande un visuel.
→ https://www.youtube.com/watch?v=kKdhK2zRtto

**S43 ✅ [DEV]** NVIDIA, « System Memory Fallback » : depuis le pilote **536.40**, une appli qui épuise la VRAM utilise la mémoire partagée « albeit at lower speeds », dès qu'on approche du maximum ; le réglage **« CUDA - Sysmem Fallback Policy » → « Prefer No Sysmem Fallback »** (Panneau NVIDIA, Gérer les paramètres 3D, par programme) existe depuis le **546.01**. Le voir : Gestionnaire des tâches, Performances, GPU, « Mémoire GPU partagée » qui monte (guide tiers).
→ https://nvidia.custhelp.com/app/answers/detail/a_id/5490 (copie archivée du 14/10/2026) ; https://runaihome.com/blog/shared-gpu-memory-slow-local-ai-sysmem-fallback-fix-2026/

**S44 ✅ [DEV]** LM Studio, blog 0.3.14 : la mémoire partagée « can slow things down quite a bit » ; option « Limit Model Offload to Dedicated GPU Memory » (CUDA) ; « splitting model weights between dedicated GPU memory and system RAM is faster than using shared GPU memory ». Changelog 0.4.16 (08/06/2026) : **contexte par défaut 8 000 tokens**. ⚠️ Le nom de l'option n'a pas été retrouvé dans les changelogs de la 0.4.28 : à vérifier à l'écran.
→ https://lmstudio.ai/blog/lmstudio-v0.3.14 ; https://lmstudio.ai/changelog/lmstudio-v0.4.16

**S45 ✅ [DEV + MESURE]** Fiche de Qwen3.8-27B : « Thinking mode is on by default », `reasoning_effort` = **xhigh** par défaut (low / medium possibles). Simon Willison, **16/08/2026**, LM Studio : un pélican en SVG en xhigh = **22 276 tokens de réflexion** + 3 223 de sortie, 21 min (à 15-30 tok/s sur sa machine) ; il conseille de commencer en « low or even no reasoning ». À 50 tok/s : ~7 min 25 (calcul). ⚠️ Pas de « /no_think » documenté pour 3.8. Dans LM Studio, le réglage est dans **le panneau de droite** (ton relevé du 08/11).
→ https://huggingface.co/Qwen/Qwen3.8-27B ; https://simonwillison.net/2026/Aug/16/qwen-38-27b/

**S46 ⚠️ [MESURE d'un utilisateur]** XDA, **28/08/2026** : Claude Code, `/context`, **51 400 tokens avant la première requête** (prompt système 10 700, outils 28 500, skills ~6 300…), ~41 400 sans plugins ni mémoire automatique. Autres relevés : 16-25K (prompt + outils, claudecodecamp, 18/03/2026). Ça dépend de la version et de la config : dis « un utilisateur a relevé ». À 64 Kio par token : 51 400 tokens ≈ 3,37 Go ; 30 000 ≈ 2 Go (calcul).
→ https://www.xda-developers.com/claude-code-using-fifty-thousand-tokens-before-typed-prompt-fixed-it/

**Écartés le 07/11** : le 102,9 tok/s sur RTX 4080 d'un article Medium (403, non lu) ; « 5 à 10 fois plus lent » (estimation de blog) ; les chiffres Strata des commentaires YouTube (témoignages non vérifiés).
