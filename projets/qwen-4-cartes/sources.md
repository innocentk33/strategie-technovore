# Sources : Qwen 4 et les cartes graphiques (recherche du 11/11/2026)

> Fiche : [`fiche.md`](fiche.md). Script : [`script.md`](script.md). Toutes les pages ont été ouvertes **le 11/11/2026** (HTTP, jour de l'enregistrement ; la vidéo sort le 12/11). Types : `MESURE` (mesure d'un utilisateur ou d'un tiers), `DEV` (affirmation officielle ou constat sur une page officielle), `AVIS`, `CALCUL` (déduction, pas une source), `RUMEUR`.
> `[À REVÉRIFIER]` = à relever de nouveau le jour de la voix, puis la veille de la sortie.
> **Relecture du 11/11 (grill V1, [`grill-v1.md`](grill-v1.md))** : les faits qui portent le script ont été rouverts à la source le même jour. Chaque fait touché porte « revérifié le 11/11 par la relecture ». Corrections : Q6 (statut du 27B), Q9 (calcul des 4 bits), Q12 (autres versions), Q14 (source de première main), Q15 (même utilisateur), Q22 (même modèle), Q23 (fourchette). Nouveau : Q25. Type ajouté : `RAPPORTÉ` (dit par l'entreprise à l'oral, d'après la presse, mais écrit nulle part par elle).
> **Limites** : leboncoin, eBay.fr et Back Market renvoient une erreur 403 aux lectures automatiques, et la page de Qwen sur X renvoie 402 : **aucun prix d'occasion n'a été relevé le 11/11**. Les pages LDLC et les agrégateurs ont été lus par un outil de résumé automatique : ouvre les fiches toi-même et prends des captures à l'écran, elles servent aussi de `[VISUEL]`.

## A. Qwen 4 : ce qui est sûr

**Q1 `DEV` Alibaba, communiqué du 22/09/2026 (conférence Apsara).** Phrase exacte : « its next-generation model, **Qwen 4**, is currently in training ». Feuille de route : Qwen 4.5 et Qwen 5, « 5 à 10 000 milliards de paramètres ». Aucune date de sortie, aucune taille. **Le communiqué ne nomme ni Max, ni Plus, ni Flash, ni 27B** (relecture de la page entière le 11/11).
→ https://www.alibabacloud.com/blog/603589 (consulté le 11/11/2026)
**Revérifié le 11/11 par la relecture** : page relue, aucune occurrence de « 27B », « Plus » ou « Flash » ; le seul « Max » est Qwen3.8-Max. Source de confusion possible : dans son discours, Eddie Wu parle de « our open-source Qwen-27B », c'est-à-dire **Qwen3.8-27B** (rapporté par RITS, URL de Q6).

**Q2 `DEV` Fiche Hugging Face de Qwen3.8-Flash-Next** (organisation Qwen) : « This experimental preview of the architecture that will underpin Qwen4… ». 125 milliards de paramètres dont 6 activés, licence qwen-community-1.0. Publié le 24/08/2026 (API Hugging Face).
→ https://huggingface.co/Qwen/Qwen3.8-Flash-Next (11/11/2026)
**Revérifié le 11/11 par la relecture** : phrase et date (24/08) confirmées ; la fiche disait 26/08, corrigé. Coupé du script V2 (ne sert pas l'achat).

**Q3 `DEV` Qwen4-Max-Preview, ouvert le 11/11/2026.** Documentation officielle d'Alibaba Cloud : aperçu du **11/11 à 10 h au 25/11 à 24 h** (UTC+8), puis retrait ; « currently in preview and is available through Token Plan only » (abonnement d'Alibaba, **pas de paiement à l'usage**) ; contexte 1 million de tokens, sortie 393 216 tokens maximum. La page **ne dit rien des poids ni des autres modèles Qwen 4**, et n'affiche aucun prix. Le compte officiel Qwen a annoncé « Qwen4 is coming » le même jour (page X illisible : texte relayé par des sites tiers et par la recherche web).
→ https://www.alibabacloud.com/help/en/model-studio/qwen4-max-preview ; https://x.com/Alibaba_Qwen/status/2120335993643684315 (402, relayé) [À REVÉRIFIER le 12/11]
**Revérifié le 11/11 par la relecture** : la doc confirme mot pour mot la période (« 10:00 on November 11, 2026 to 24:00 on November 25, 2026 (UTC+8) »), « available through Token Plan only. Pay-as-you-go access is not supported », 1 M de contexte, 393 216 tokens de sortie ; rien sur les poids, les autres modèles ni le prix. Le post X reste illisible et n'est pas cité dans le script. Les moteurs de recherche n'indexent pas encore la page : ouvre l'URL directement.

**Q4 `DEV` Aucun modèle Qwen 4 dans l'organisation Qwen de Hugging Face au 11/11/2026.** Les 15 derniers dépôts (API, tri par date) : Qwen-Image-2.1-Turbo (09/10), Qwen-Image-2.1 (14/09), Qwen-Drive-1.0-4B (27/08), Flash-Next et Flash-Next-FP8 (24/08), Qwen3.8-27B-FP8 (13/08), Qwen3.8-2.4T-A95B (08/08), **Qwen3.8-27B (05/08)**… Aucun nom ne contient « Qwen4 ». Sur GitHub, l'organisation QwenLM (61 dépôts) ne mentionne pas Qwen 4 (dernières mises à jour : qwen-code, 11/11).
→ https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1 ; https://github.com/QwenLM (11/11/2026) [À REVÉRIFIER le 12/11, avant la mise en ligne]
**Revérifié le 11/11 par la relecture** : même liste (dernier dépôt : Qwen-Image-2.1-Turbo, 09/10), aucun « Qwen4 » ; `Qwen/Qwen4-27B` n'existe pas (l'API répond par une erreur). **Attention** : une recherche « qwen4 » sur tout Hugging Face remonte des dépôts d'inconnus nommés « Qwen4-27B » (Q25). Le constat du script porte donc sur la page officielle de Qwen ; ne montre jamais un « 0 résultat » à l'écran.

**Q5 `DEV` Teaser officiel du 06/11/2026** : « The becoming begins » (compte Qwen), sans nom de modèle ni date. Relayé par le radar du 10/11 et par la recherche web ; page X illisible. (Non cité dans le script : contexte seulement.)
→ [`etudes/radar.md`](../../etudes/radar.md) ; https://www.yottalabs.ai/post/qwen-4-release-date-what-is-known-how-to-prepare-2026 (11/11/2026)

## B. Qwen 4 : ce qu'on raconte

**Q6 `RAPPORTÉ` Le nom « Qwen 4 27B » (et Max, Plus, Flash).** **Revérifié le 11/11 par la relecture**, qui **corrige à la fois le radar du 10/11 et la fiche** (« confirmé ») **et la V1 de cette page** (« rumeur, tirée d'un post sur X »).
- **Rien d'écrit par Alibaba** : ni le communiqué (Q1) ni la doc (Q3) ne nomment Plus, Flash ou 27B. Le seul nom Qwen 4 écrit par Alibaba est `qwen4-max-preview` (Q3) : « Max » est donc devenu officiel le 11/11.
- **Mais le 27B a été présenté à la conférence, d'après la presse.** 36Kr (presse tech chinoise, 23/09), résumant la feuille de route présentée au Yunqi : « 基于新一代架构的Qwen4已进入训练阶段，开源侧优先安排Qwen4-27B » (Qwen 4 est en entraînement ; côté open source, priorité à Qwen4-27B). Yottalabs et OrcaRouter disent que Liu Dayiheng, responsable de Qwen LLM, a montré les quatre noms sur scène, sans taille, date, licence ni prix.
- **Une source dit le contraire** : RITS (NYU Shanghai) attribue la liste à « a post on X that was widely shared after the keynote » et ajoute que les documents d'Alibaba ne nomment pas ces variantes.
- **Verdict** : un nom **annoncé à l'oral selon la presse, écrit nulle part par Alibaba**, sans aucune caractéristique. « Confirmé » est trop fort, « rumeur » trop faible. À dire : « d'après la presse chinoise, il a été montré à la conférence, comme la version ouverte de Qwen quatre ; Alibaba ne l'a écrit nulle part ». La phrase de la V1 « Alibaba n'a même pas promis que les fichiers seraient publics » est retirée : à l'oral, d'après 36Kr, c'est la version ouverte prévue.
→ https://eu.36kr.com/zh/p/3995489380849281 (23/09/2026) ; https://www.yottalabs.ai/post/qwen-4-max-vs-plus-vs-flash-vs-27b-tiers-2026 (29/09/2026) ; https://www.orcarouter.ai/blog/qwen-4-max-lineup-announced-apsara-2026 ; https://c.m.163.com/news/a/L7E8KGS30550WHYR.html (Caiwen, 22/09/2026 : « Qwen4已投入训练 », sans 27B) ; tous lus le 11/11/2026.

Texte de la V1 de Q6, gardé pour l'historique : il est absent du communiqué (Q1). Il vient d'un **post sur X partagé après la conférence**, repris ensuite par des sites secondaires qui le disent eux-mêmes non confirmé. Le seul nom Qwen 4 présent dans la documentation officielle est `qwen4-max-preview` (Q3).
→ https://rits.shanghai.nyu.edu/ai/alibaba-at-apsara-2026-qwen-4-in-training-10t-models-next/ (22/09/2026) ; https://tech-insider.org/qwen4-four-variants-no-confirmed-open-weights-alibaba-2026/ (03/11/2026) ; https://www.yottalabs.ai/post/qwen-4-release-date-what-is-known-how-to-prepare-2026 (11/11/2026)

**Q7 `RUMEUR` « Une demande de fusion du code d'Intel parle d'un modèle dense Qwen 4 de 27 milliards, d'environ 15 Go ».** Rapporté par une vidéo américaine (08/11) et par un article chinois ; la demande de fusion n'a **pas été retrouvée** (le numéro testé, vllm-xpu-kernels #22, est une autre PR, de septembre 2025). Attribution contradictoire entre les sites. Aucun poids Qwen 4 n'a servi à valider ce code. À dire : « une estimation tirée du code d'un logiciel, pas un fichier ».
→ https://www.huxiu.com/article/4900440.html ; https://kie.ai/blog/qwen4-27b-architecture-analysis (jugé peu fiable) ; https://github.com/vllm-project/vllm-xpu-kernels/pull/22 (11/11/2026, ne correspond pas)

**Q8 `RUMEUR` « Qwen 4 sort la semaine prochaine »** : propos du directeur technique d'Alibaba lors d'une conférence du 29/10 à Amsterdam, rapportés de seconde main. Au 11/11 : aperçu cloud uniquement (Q3), pas de poids.
→ https://www.yottalabs.ai/post/qwen-4-release-date-what-is-known-how-to-prepare-2026 ; [`etudes/radar.md`](../../etudes/radar.md) (10/11/2026)

## C. Le modèle de référence : Qwen3.8-27B

**Q9 `DEV` Tailles des fichiers** (API Hugging Face, dépôt unsloth/Qwen3.8-27B-GGUF, lu le 11/11/2026 ; Go = 10⁹ octets) : UD-IQ3_XXS **10,93** ; UD-IQ3_S 12,04 ; UD-Q3_K_XL 13,15 ; **UD-IQ4_XS 14,35** ; UD-Q4_K_S 15,36 ; **UD-Q4_K_M 16,56** ; UD-Q5_K_M 19,87 ; UD-Q6_K 21,98 ; Q8_0 29,05.
⚠️ **Écart avec les relevés du 24/10 (F40, F41) et du 07/11 (S38)** : IQ4_XS 14,25 → 14,35 et Q4_K_M 16,46 → 16,56, soit +0,10 Go ; les fichiers semblent republiés (dépôt modifié le 11/11). Le script dit « seize gigas et demi » et « quatorze gigas » : vrai dans les deux relevés. [À REVÉRIFIER]
**Revérifié le 11/11 par la relecture** (API, dépôt modifié le 11/11 à 15:33 UTC) : UD-IQ4_XS **14,35**, UD-Q4_K_S **15,36**, Q4_0 16,06, UD-Q4_K_M **16,56**, UD-Q4_K_XL **17,66** ; module MTP à part : **1,37 Go** (`MTP/mtp-Qwen3.8-27B-Q4_0.gguf`). Les quatre bits vont donc de **14,35 à 17,66 Go** : le script V2 dit « entre quatorze et dix-huit gigas selon le fichier ». **Correction** : le calcul de la V1 « 27 milliards × ~4 bits ≈ 15 à 17 Go » est faux. 27,78 milliards × 4 bits / 8 = **13,9 Go** ; les fichiers « quatre bits » pèsent plus parce qu'ils gardent certaines couches en plus haute précision (4,1 à 5,1 bits par paramètre en moyenne). On montre la vraie liste des fichiers à la place.
→ https://huggingface.co/api/models/unsloth/Qwen3.8-27B-GGUF?blobs=true

**Q10 `DEV` Qwen3.8-27B** : 27,78 milliards de paramètres (BF16), licence Apache-2.0, publié le 05/08/2026, 55,6 Go en pleine précision (page Hugging Face).
→ https://huggingface.co/Qwen/Qwen3.8-27B (11/11/2026)

**Q11 `CALCUL` Ce qui rentre.** Une carte de 16 Go = 16 Gio = 17,18 milliards d'octets ; Windows prend environ 1 Go (hypothèse, comme S15 et S38 de `claude-ou-mon-pc-1`). 16 Go : 17,18 − 1 = 16,2 ; le Q4_K_M (16,56) ne rentre pas, l'IQ4_XS (14,35) laisse environ 1,8 Go. 24 Go = 25,77 milliards d'octets ; 25,77 − 1 − 16,56 = environ **8,2 Go** de marge avec le Q4_K_M (cache KV de Qwen3.8-27B : 2,3 Go à 32 K, 8,7 Go à 128 K, F34 de `deux-cartes-occasion`). 32 Go = 34,36 milliards d'octets : environ 16,8 Go de marge. Deux cartes de 16 Go : même total que 32 Go.

## D. Vitesses mesurées (toutes sur Qwen3.8-27B, jamais sur Qwen 4)

**Q12 `MESURE` RTX 5090 (32 Go).** **75,19 tok/s** (Q4_K_M, contexte 4 K, llama.cpp b11669, relevé du 15/10/2026) ; **74,83 tok/s** à 4 K sur un autre banc d'essai (Q4_K_S, llama.cpp b10364, page du 17/08/2026). ⚠️ Les mêmes bancs donnent aussi **65** (autres versions du logiciel) et le second tombe à 52 à 8 K, sans explication : on dit « jusqu'à soixante-quinze » et on cite le 4 K. Sans MTP.
→ https://llm-speed.com/m/qwen3-8-27b ; https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/ (11/11/2026)
**Revérifié le 11/11 par la relecture** : 75,19 (b11669, 4 K) et 74,83 (Q4_K_S, 4 K) confirmés. Sur llm-speed, les autres passes donnent **65,1 à 65,7** (commit 9725a31) et **43,12** en « chat-short » avec la version la plus récente (b12157), sans explication ; le second banc tombe à 52,23 à 8 K. Le script V2 dit donc partout « **jusqu'à** soixante-quinze ».

**Q13 `MESURE` RTX 3090 (24 Go).** **40,31 tok/s** à 4 K et **33,95** à 64 K (Q4_K_S 16,68 Gio, llama.cpp, Flash Attention, sans MTP, 17/08/2026) ; **38,6** (Q4_K_M, 4 K, llm-speed, 22/10/2026). Avec MTP : **40,4 → 72,5 tok/s** sur une invite de code, mesure d'un projet tiers relevée dans un article du 24/10, et sudoingX **31,0 → 41,3** à 131 K de contexte : le gain **baisse quand le contexte grandit**.
→ https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/ ; https://llm-speed.com/m/qwen3-8-27b ; https://dev.to/rigbase/what-gpu-do-you-need-for-qwen38-qwen36-gemma-4-and-gpt-oss-locally-measured-oct-2026-1eg6 ; https://openclawdc.com/blog/qwen-3-8-27b-rtx-3090/ (11/11/2026)
**Revérifié le 11/11 par la relecture** : 40,31 (4 K) et 33,95 (64 K) confirmés ; le 40,4 → 72,5 vient du projet OpenJet (« on a code prompt », 50,9 sur une invite de raisonnement), relayé par l'article du 24/10. La table sudoingX donne aussi, avec le Q4_K_M à 131 K, 41,3 → 63,5 (@hauntedhost) : « plus de soixante-dix sur du code » reste juste, comme valeur haute.

**Q14 `MESURE` RTX 5060 Ti 16 Go (une seule carte).** **28,0 tok/s** (UD-IQ4_XS, contexte 8 K, llama.cpp, sans MTP), mesure de « JESVS » relevée dans l'article du 24/10. **Revérifié le 11/11 par la relecture** **à la source primaire** : billet de JESVS du **06/10/2026**, « Plain generation: 28.0 tok/s, which is 96% of that GPU's roofline », avec « UD-IQ4_XS (14.3 GB) squeezes onto the 5060 Ti with 8K of q8 KV cache ». **Avec MTP**, même carte : **51,4 tok/s** en texte libre, **58,1** sur des modifications de code. Le script V2 cite le 28 (hook, section 2) et le 51 (section 3, « sur une conversation courte »). → https://jesvs.com/posts/llama-cpp-dual-gpu-optimization/ (11/11/2026). Autre mesure, primaire : discussion llama.cpp n° 28894 (« wangleye », 14/09/2026), 256 K de contexte avec MTP et un fork du logiciel (KVMem) : **30 tok/s** en IQ3_S et **33** en IQ4_XS, mémoire de la carte à 15,5 Go, 37 à 41 tok/s sur une tâche courte.
→ https://dev.to/rigbase/what-gpu-do-you-need-for-qwen38-qwen36-gemma-4-and-gpt-oss-locally-measured-oct-2026-1eg6 ; https://github.com/ggml-org/llama.cpp/discussions/28894 (11/11/2026)

**Q15 `MESURE` Deux RTX 5060 Ti 16 Go (32 Go au total).** Table publique du dépôt sudoingX/qwen38-mtp (**non datée**, lue le 11/11/2026) : répartition **par couches (défaut) 22,1 tok/s, 42,8 avec MTP** ; **tensor split (`-sm tensor`) 37,1 → 65,9** (@Jackwwg83, UD-Q4_K_XL, 131 K, cache q4_0) et **38,3 → 76,0** (@mgoswick, Q4_K_M, 131 K). Un banc d'essai indépendant donne **22,47 tok/s** à 4 K en répartition par couches (Q4_K_S, sans MTP, 17/08), cohérent avec le 22,1. ~~⚠️ Mesures d'utilisateurs différents, réglages différents~~ **Corrigé, revérifié le 11/11 par la relecture** : les trois chiffres **22,1 → 37,1 → 65,9 sont du même utilisateur (@Jackwwg83), avec le même fichier (UD-Q4_K_XL, 17,66 Go) et le même contexte (131 K)** ; seul le 76,0 vient d'un autre (@mgoswick, Q4_K_M). La comparaison 22 → 37 → 66 est donc propre (×1,7 avec le tensor split, ×1,8 avec le MTP, ×3,0 au total). Le script V2 le dit. Le mode tensor est étiqueté expérimental dans llama.cpp (F20 de `deux-cartes-occasion`).
→ https://github.com/sudoingX/qwen38-mtp ; https://www.hardware-corner.net/qwen3-8-27b-hardware-tests/

**Q16 `MESURE` RX 7900 XTX (24 Go).** Même table : sans MTP **28,8 à 41,0 tok/s** selon le logiciel et le système (30,7 @Jqianggu ; 28,8 Vulkan/RADV @Splizard, build du 17/08/2026 ; 41,0 Windows/Vulkan @pparuzel ; 36,3 ROCm @vijay-14), avec MTP **43,9 à 85,4**. Contexte 131 K. Pas de date, sauf une ligne.
→ https://github.com/sudoingX/qwen38-mtp (11/11/2026)

**Q17 `MESURE` RTX 5080 (16 Go)** : **53,4 → 101,3 tok/s** avec MTP, @ChumBoxBaron, fichier Q3_K_M (3 bits), contexte 65 536 : **une seule mesure**, déjà S18 de [`claude-ou-mon-pc-1`](../claude-ou-mon-pc-1/sources.md). 3 bits, donc qualité moindre.
→ https://github.com/sudoingX/qwen38-mtp (11/11/2026)
**Revérifié le 11/11 par la relecture** : la ligne « RTX 5080 16GB, @ChumBoxBaron, 53.4 → 101.3 » est là ; le Q3_K_M et le 65 536 de contexte viennent d'une note de bas de tableau que la page ne relie pas clairement à cette ligne. Le script garde « un fichier trois bits » et « une seule mesure » ; ne l'écris pas en gros à l'écran.

**Q18 `MESURE` RTX 3060 12 Go : 5,2 à 6,7 tok/s** (llama-bench, une partie du modèle déborde hors de la carte), d'après llamabench.ai relevé dans l'article du 24/10 (secondaire).
→ https://dev.to/rigbase/what-gpu-do-you-need-for-qwen38-qwen36-gemma-4-and-gpt-oss-locally-measured-oct-2026-1eg6 (11/11/2026)

**Q19 `MESURE` Steam, octobre 2026, VRAM : 8 Go 26,92 %, 16 Go 26,35 %, 12 Go 12,91 %, 24 Go 5,40 %.** Repris de S36 de [`claude-ou-mon-pc-1/sources.md`](../claude-ou-mon-pc-1/sources.md) (vérifié le 05 et 07/11).

## E. Prix en France (relevés du 11/11/2026, TTC) `[À REVÉRIFIER]`

> Les prix sont typés `MESURE` : ce sont des relevés datés, pas des affirmations de fabricant.

**Q20 `MESURE` comparateur-gamer.fr, page « Évolution des prix des cartes graphiques », mise à jour le 11/11/2026** (médianes chez les marchands français, **toutes déclinaisons confondues** : la 5060 Ti compte 64 références, 8 Go et 16 Go mélangés) :

| Carte | Médiane | 30 jours | 3 mois | Plus bas relevé |
|---|---|---|---|---|
| RTX 5060 Ti | 786 € | **+21,8 %** | +20,2 % | 452 € (01/07) |
| RTX 5070 Ti | 1 600 € | +12,9 % | +37,5 % | 995 € (01/07) |
| RTX 5080 | 2 200 € | **+20,2 %** | +32,9 % | 1 409 € (01/07) |
| RTX 5090 | **9 300 €** | +38,8 % | **+89,8 %** | 3 550 € (03/06) |
| RX 9070 XT | 1 117 € | +6,0 % | +29,7 % | 763 € (03/06) |

→ https://www.comparateur-gamer.fr/evolution-prix/carte-graphique (11/11/2026). La RTX 3090, la 4090 et la 7900 XTX n'y figurent pas.
**Revérifié le 11/11 par la relecture** : page « Mis à jour le 11 novembre 2026 », chiffres identiques. Rappel : la ligne 5060 Ti mélange 8 et 16 Go (64 déclinaisons). Le « presque doublé en trois mois » de la 5090 vient du +89,8 %.

**Q21 `MESURE` gpuprix.com (agrégateur), pages France mises à jour le 11/11/2026** : RTX 5060 Ti **16 Go** neuve **694 €** (Amazon.fr, ASUS PRIME OC) ; médiane sur 3 mois 557 €, sur 12 mois 590 € ; RTX 5090 neuve **7 900 €** (Amazon.fr, ASUS TUF OC, « en stock » ; des fiches moins chères, jusqu'à 4 583 €, sont en rupture) ; RTX 3090 **neuve 2 990 €** (Amazon.fr, ROG Strix OC) et « occasion » 3 303 € (reconditionnée Amazon.fr : **aberrant**, plus cher que le neuf, à ne pas citer comme prix d'occasion) ; RX 7900 XTX neuve **1 417 €** (Amazon.fr, Sapphire Nitro+ ; une XFX à 1 049 € est en rupture).
→ https://gpuprix.com/fr/france/gpus/geforce-rtx-5060-ti-16gb ; …/geforce-rtx-5090 ; …/geforce-rtx-3090 ; …/radeon-rx-7900-xtx (11/11/2026)
**Revérifié le 11/11 par la relecture** (pages `?show=listings`, mises à jour le 11/11 ; la page simple renvoyait 502 dans l'après-midi) :
- **5060 Ti 16 Go** : la moins chère en stock reste l'**ASUS Prime OC à 694 €** (Amazon.fr) ; puis ASUS Dual OC 727 €, MSI Ventus 2X OC Plus 742 € ; 15 modèles sur 21 en stock, de 694 à 1 130 €.
- **5090** : moins chère en stock **7 900 €** (ASUS TUF, Amazon.fr), puis 7 950 et 7 995 € ; la plupart des offres en stock entre 7 900 et 9 600 € ; les fiches de 4 583 à 7 000 € sont en rupture.
- **3090** neuve : 2 990 € (ROG Strix OC et MSI Suprim X, Amazon.fr) ; la « reconditionnée » à 3 303 € reste aberrante.
- **7900 XTX** : 1 417 € (Sapphire Nitro+, Amazon.fr) ; une Sapphire Pulse à 6 273 € est une erreur de données.
- Calcul du script : 2 × 694 = 1 388 € (« à partir de mille quatre cents euros environ ») ; 7 900 / 1 388 = 5,7 (« plus de cinq paires »).

**Q22 `MESURE` LDLC, fiches ouvertes le 11/11/2026** : RTX 5060 Ti 16 Go **MSI Ventus 2X OC Plus 1 029,95 €** (page : « Rupture » avec retrait en magasin, une unité par client) ; **ASUS Prime OC 1 099,95 €** (en stock). ⚠️ **Écart avec Q21 (694 €)** : ce n'est pas la même enseigne ni le même modèle ; une recherche web remonte aussi d'anciennes fiches LDLC (Gigabyte Windforce OC à 489,95 €, plus en vente ; MSI Ventus 3X OC à 739,95 € ; Gigabyte Gaming OC à 819,95 €), **sans date** : non retenues. Le script V1 disait « de sept cents à mille cent euros selon le marchand ».
**Revérifié le 11/11 par la relecture** : l'ASUS Prime OC 16 Go est **en stock à 1 099,95 €** chez LDLC (« Dispo dans 12 boutiques »). **Correction** : la V1 écrivait « ce n'est pas la même enseigne ni le même modèle ». C'est **le même modèle** (ASUS PRIME GeForce RTX 5060 Ti OC Edition 16GB) à 694 € chez Amazon.fr et à 1 099,95 € chez LDLC : l'écart vient seulement du marchand. Le script V2 le dit (« la même carte, de la même marque »).
→ https://www.ldlc.com/fiche/PB00676216.html ; https://www.ldlc.com/fiche/PB00676842.html (11/11/2026)

**Q23 `MESURE` Occasion : non relevé le 11/11.** Repli daté **24/10/2026** (F4, F5 de [`deux-cartes-occasion/sources.md`](../deux-cartes-occasion/sources.md), annonces et agrégateur, prix demandés) : RTX 3090 d'occasion en France, **moyenne 834 €**, annonces de 800 à 1 190 € ; RTX 3060 12 Go médiane 280 €. Le marché a monté depuis (Q20). **À remplacer par tes relevés du jour** (`⟦à écrire⟧` du script).
**Revérifié le 11/11 par la relecture** : le repli de la V1 disait « huit cents à mille euros » ; les annonces relevées allaient jusqu'à 1 190 €. Le repli V2 dit « de huit cents à mille deux cents euros », daté « fin octobre ».

**Q24 `AVIS` La hausse est attribuée à la pénurie de mémoire, pas à Qwen 4** (« GPUs +35 % en trois mois… rien à voir avec Qwen 4 »), vidéo américaine du 08/11, **prix américains**. Le script reprend seulement la cause avancée, dite « d'après une chaîne américaine ».
Relecture du 11/11 : non rouverte (déjà dite comme un avis). Une recherche remonte un article de Cowcotland qui parle aussi de « tension sur la mémoire GDDR7 », mais la page renvoie 403 : non citée.
→ https://www.youtube.com/watch?v=kQKCp7PlVxY (transcription, 11/11/2026)

## B bis. Ajouté par la relecture

**Q25 `DEV` Des pages « Qwen4-27B » vides sur Hugging Face** (constat sur les pages, 11/11/2026, revérifié le 11/11 par la relecture). Une recherche « qwen4 » remonte des dépôts créés par des inconnus, hors de l'organisation Qwen :
- un dépôt « Qwen4-27B-NVFP4 » (14/10) : « No model weights are available in this repository. It is not ready for inference » ;
- un dépôt « Qwen4-27B-Uncensored-v3-FP8 » (09/11) : « Coming soon » ;
- un dépôt « Qwen4-27B-1bit-GGUF » (09/11), qui se déclare dérivé de `Qwen/Qwen4-27B`, un dépôt qui n'existe pas.
Les trois ne contiennent qu'un `README.md` et un `.gitattributes`, sans aucun fichier de modèle. Le script dit « des gens réservent juste la place » et « méfie-toi ». **Ne nomme pas les comptes** dans la voix, et floute-les à l'écran.
→ https://huggingface.co/api/models?search=qwen4 ; https://huggingface.co/api/models/IteraCompute/Qwen4-27B-NVFP4?blobs=true (et les deux autres) (11/11/2026) [À REVÉRIFIER le 12/11]

## F. Renvois internes

- *16 Go de VRAM suffisent* : sortie le lun. 09/11 (calendrier).
- Strata sur ta 5080 : lun. 16/11 (`claude-ou-mon-pc-1`, section 3).
- La vidéo sur les 32 Go de VRAM : lun. 23/11 (`deux-cartes-occasion`).

## Faits dont je ne suis pas sûr

État après la relecture du 11/11 :
- **Q22 contre Q21 : expliqué.** C'est le même modèle, l'écart vient du marchand. Il peut disparaître d'un jour à l'autre : capture les deux fiches le jour de la voix.
- **Q9 : confirmé** (14,35 et 16,56 Go, dépôt modifié le 11/11).
- **Q12 : l'écart 65 / 75 reste inexpliqué.** D'où le « jusqu'à » du script.
- **Q3 : le post X officiel reste illisible.** Le script ne s'en sert pas : la doc suffit.
- **Q6 : la presse se contredit** sur l'origine du nom (scène ou post). Le script s'en tient à ce qui est sûr : rien d'écrit par Alibaba, et « montré à la conférence d'après la presse chinoise ».

Version d'avant la relecture :


- Q22 contre Q21 : l'écart de prix de la 5060 Ti 16 Go (694 contre 1 029,95 et 1 099,95) n'est pas expliqué ; les deux lectures passent par un outil de résumé.
- Q9 : les tailles de fichiers ont bougé de 0,10 Go entre le 07/11 et le 11/11.
- Q12 : l'écart 65 / 75 selon la version de llama.cpp.
- Q3 : le texte du post X officiel n'a pas pu être lu directement.

**Q26 `DEV` Annonce de Qwen4-Max sur X (11/11/2026).** Le compte officiel @Alibaba_Qwen (https://x.com/Alibaba_Qwen) annonce « Qwen4 is coming » : Qwen4-Max est en aperçu sur le Token Plan d'Alibaba, avec un accès anticipé sur QwenWork, Qoder, l'appli Qwen et QwenStudio. Aucun fichier à télécharger. Relevé par l'auteur le 11/11 (post copié dans la conversation) ; ça complète Q3 : la doc dit « Token Plan only » pour l'API, mais le modèle s'essaie aussi dans les applis de Qwen.

**Q27 `MESURE` Prix d'occasion relevés par l'auteur sur Leboncoin, le 11/11/2026** (captures d'annonces, prix demandés, pas des prix de vente) :
- RTX 3060 12 Go (Gigabyte Eagle OC, Gigabyte Gaming) : 280 € et 320 € ; fourchette vue : 280 à 310-320 € ;
- RTX 3090 24 Go : 850 € (≈ 28 % des 2 990 € neufs d'Amazon.fr, Q21 : « moins d'un tiers ») ;
- AMD Radeon RX 6800 XT 16 Go GDDR6 (PowerColor Red Dragon) : 280 € ;
- NVIDIA V100 16 Go : 498 € (carte de serveur, non citée dans la vidéo : refroidissement passif) ;
- RTX 5080 : 1 899 € (non citée).
Remplace le repli du 24/10 (Q23) pour la 3090. **Aucune mesure de Qwen3.8-27B sur RX 6800 XT trouvée** : la vidéo ne donne pas de vitesse pour cette carte.

