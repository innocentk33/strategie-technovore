# Sources : « Même carte, 2 fois plus rapide » (jeu. 19/11/2026)

> Faits numérotés **M1, M2…**, relevés le **15/11/2026** (vers 21 h UTC) sur la page d'origine, sauf ceux marqués « repris de B, non rouvert » : API GitHub (`gh api`) pour les PR, tickets, commits et versions ; `raw` de Hugging Face pour les fiches de modèles ; page HTML téléchargée et lue en texte brut pour les blogs (pas de résumé par un modèle). Ils vérifient les recherches [`recherche/A-nathan.md`](recherche/A-nathan.md), [`B-mesures.md`](recherche/B-mesures.md) et [`C-strata-auteur.md`](recherche/C-strata-auteur.md) ; les corrections sont en section **E**.
>
> **Vidéo calculée (décision du 15/11)** : aucune vitesse de ce fichier n'est à toi, sauf la section **F** (vidéo Strata), qui n'est **jamais un avant/après**.
>
> **Types** : `MESURE` (chiffre publié par un utilisateur ou un tiers, avec sa machine) · `DEV` (le projet ou l'auteur du code, pas indépendant) · `AVIS` · `CALCUL` (déduction de ma part).
> **Statut** : ✅ vérifié deux fois (le chiffre relu aujourd'hui à la source primaire **et** une autre mesure indépendante qui va dans le même sens, ou un fait déjà vérifié dans un autre projet et relu aujourd'hui ; pour un fait `DEV` : relu sur la page du projet) · ⚠️ une seule mesure, ou chiffre relayé, ou nuance (dite) · ❌ faux ou introuvable.
> **D** = decode (vitesse d'écriture), **P** = prefill (lecture du prompt). Jamais mélangés.
> **Règle de la voix** : aucun nom de chaîne, de créateur ni de pseudo (« un utilisateur », « un testeur sur une 5060 Ti », « une chaîne française »). Les noms restent ici.

---

## A. Le levier qui tient le « ×2 » : le MTP, sur un modèle qui tient dans la carte

Toutes les lignes M1 à M6 : **Qwen3.8-27B (dense)**, **une seule carte de 16 Go**, llama.cpp, même fichier dans les deux bras, **seul le MTP change**, D (écriture).

| Id | Carte | Fichier | Moteur | Sans MTP | Avec MTP | Gain D | Auteur | Statut |
|---|---|---|---|---:|---:|---:|---|---|
| Id | Carte | Fichier | Moteur | Sans MTP | Avec MTP | Gain D | Auteur, date d'ajout | Statut |
|---|---|---|---|---:|---:|---:|---|---|
| **M1** | RTX 5080 16 Go | unsloth Q3_K_M, ctx 65 536, KV q4_0 | llama.cpp b10488, Windows 11 | 53,4 | 101,3 (n-max 2) | **×1,90** | @ChumBoxBaron, ligne ajoutée le **21/08/2026** | ✅ avec M5 (seul : S18) |
| **M2** | RTX 5060 Ti 16 Go | « Q4-XYZ-v2 » 15,06 Go, ctx 32K | b10472 (17/08/2026) | 26,3 | 59,5 (n-max 4) | **×2,26** | @jaisusx (PR #52), fiche du **18/08/2026** | ✅ avec M5 (seul : S19 ⚠️) |
| **M3** | RTX 4060 Ti 16 Go | Q4-XYZ-v2, ctx 32K | — | 17,6 | 40,0 (n-max 3) | **×2,27** | @CeIest2, fiche des **21-22/08/2026** | ✅ avec M5 |
| **M4** | RX 9060 XT 16 Go | AtomicChat IQ3_XXS, ctx 128K, KV q4_0, ROCm | — | 15,2 | 28,7 (n-max 2) | **×1,89** | @kdrapel (PR #17), ajoutée vers le **16/08/2026** | ✅ avec M5 |
| **M5** | RTX 5060 Ti 16 Go (OCuLink) | unsloth UD-IQ3_XXS, KV q4_0, FA, médiane de 5 | llama.cpp `ad1de39e0` | 29,18 (4K) · 23,62 (32K) · 19,77 (64K) | 63,89 · 45,48 · 39,06 (n-max 3) | **×2,19 · ×1,93 · ×1,98** | NJannasch.Dev, **15/08/2026** | ✅ |
| **M6** | RTX 3080 Ti portable 16 Go | unsloth UD-Q3_K_XL | — | 14,8 | 28,6 (n-max 2) | ×1,93 | @salibam99, ligne du **18/08/2026** (corrigée le jour même : 33,9 → 28,6) | ✅ avec M5 |

→ M1 à M4 et M6 : https://github.com/sudoingX/qwen38-mtp (README, tableau des résultats ; `sweeps/rtx-5060-ti.md`, `sweeps/rtx-4060-ti.md`, `sweeps/radeon.md` ; dates = commits du dépôt ; dernier commit le 26/09/2026). Chaque ligne a son propre contributeur. M5 : https://njannasch-dev-astro.pages.dev/blog/qwen-3-8-27b-5060ti-mtp-coding/ (publié le 15/08/2026).

**Conclusion ✅** : **6 mesures de 6 auteurs, 5 modèles de carte de 16 Go, de ×1,9 à ×2,3 en écriture.** C'est le seul « ×2 » tenu par les sources. **Attention à l'indépendance** : cinq lignes sur six viennent du même dépôt et du même script de mesure (`probe.py`) ; la seule mesure tout à fait indépendante est **M5**, qui concorde (×1,9 à ×2,2).

Conditions à dire avec le chiffre :
- **Le ×2 est une moyenne sur du code, du texte et des commandes, réflexion coupée.** Sur du texte seul, c'est moins : 4060 Ti 17,6 → 32,3 (**×1,8**, M3) ; 5080 + 3090 54,0 → 79,2 (×1,5, README du même dépôt). Le code gagne le plus (4060 Ti : 17,6 → 49,0). À dire : « jusqu'à 2 fois, surtout sur du code ».
- **M7 ✅ [MESURE] Le MTP fait baisser la lecture du prompt** (mesures de **mai 2026**, sur la branche de la PR, avant sa fusion). PR #22673 (llama.cpp), commentaire de **cturan** du 04/05/2026 : Qwen3.6-27B Q6_K, RTX 3090 + 3060, même fichier : D 22,97 → 42,45 (×1,85), **P 1 315 → 665 (×0,51)**, +2,49 Gio de VRAM. Commentaire de **kknddandy** du 05/05/2026 : RTX 5070 Ti + 3080, D 39,06 → 72,58 (×1,86), **P 1 542 → 930 (×0,60)**. → https://github.com/ggml-org/llama.cpp/pull/22673#issuecomment-4372285675 ; …#issuecomment-4376989966. ⚠️ Deux machines à **deux cartes** et Qwen3.6, pas 3.8 : à dire « la lecture du prompt, elle, ralentit », sans chiffre sur 16 Go.
- **M8 ✅ [DEV]** MTP fusionné dans llama.cpp le **16/05/2026** (PR #22673 « llama + spec: MTP Support », `merged_at` 2026-05-16T12:06Z). Il faut un fichier **qui contient les têtes MTP** (S38 : ISTA IQ3_S-mtp 12,12 Go contre IQ3_S 11,77 Go).
- **M9 ✅ [MESURE] Le MTP prend de la VRAM** : +2,49 Gio (cturan, M7) ; @jaisusx 14 514 → 15 704 Mio (M2) ; @lsunay, RX 7900 GRE 16 Go (`sweeps/radeon.md`) 13,77 → 15,35 Go. Sur 16 Go, c'est ce qui limite (n-max 4 = OOM chez @CeIest2).
- **M10 ⚠️ [MESURE] Pas toujours.** NJannasch.Dev, 25/04/2026, **Qwen3.6-27B dense** sur 5060 Ti : « the dense model gets 42% slower » avec le MTP (mise à jour de l'article, sans chiffre), quand le MoE 35B-A3B passe de 98 à **144 tok/s (×1,47)**. → https://njannasch-dev-astro.pages.dev/blog/speculative-decoding-qwen-27b-dense-5060ti/. Le même auteur obtient ×2,19 sur Qwen3.8-27B quatre mois plus tard (M5) : le contre-exemple est **ancien et sur l'ancien modèle**.
- **M11 ⚠️ [MESURE] Sur un MoE, le MTP rapporte moins** : ×1,47 (M10, 35B-A3B, 5060 Ti) ; ×1,28 (PR #22673, GloballyUniquePlaceholder, 3060 portable 6 Go, 35B-A3B : repris de B, non rouvert). À dire : « sur les gros modèles à experts, c'est moins ».

## B. Faire tenir le modèle dans la carte (au lieu de déborder)

| Id | Source | Carte | Avant → après | Gain D | Statut |
|---|---|---|---|---:|---|
| **M12** | Rost Glukhov, https://www.glukhov.org/llm-performance/benchmarks/best-llm-on-gb-vram-gpu/ (publié le **04/04/2026**, modifié le **23/10/2026**) | RTX 4080 16 Go, i7-14700, 64 Go DDR5-6000, llama-cli | Qwen3.5-27B **IQ4_XS 15,0 Go** (charge CPU/GPU 49/406 %) **20,5** → **UD-IQ3_XXS 11,5 Go** (98/100 %) **45,3** à 19K ; 17,4 → 45,1 à 32K | **×2,2** (×2,6 à 32K) | ✅ même modèle, deux fichiers |
| M12b | même page | idem | Qwen3.6-35B-A3B UD-IQ4_XS 17,7 Go **95,0** → UD-IQ3_XXS 13,2 Go **147,5** | ×1,55 | ✅ |
| **M13** | InventiveHQ, https://inventivehq.com/blog/vram-offload-cliff-gpu-layers-benchmark (**26/06/2026**) | RTX 5060 Ti 16 Go (PCIe 3.0 ×8), 64 Go DDR4-2400 | Qwen2.5-Coder-14B Q4_K_M : `-ngl 40` (40 couches sur 48) **12,5** → toutes **43,18** ; tout sur CPU 2,89 | **×3,45** | ✅ ⚠️ débordement **forcé** (le fichier tient) : montre la falaise, pas un choix de fichier |
| **M14** | Curiositry (The Autodidacts), https://www.autodidacts.io/how-to-fit-qwen3-8-27b-into-16gb-vram-run-with-llama-cpp-rtx-3080-flags-quantizations/ (**23/08/2026**, modifié le 28/08) | **RTX 3080 de PC portable, 16 Go** | Qwen3.8-27B UD-Q5_K_M (`-n-gpu-layers 24`, déborde) « like 1.5 t/s » → UD-IQ3_XXS tout sur la carte « about 20–30 tokens per second » | ≈ ×13 à ×20 | ⚠️ ordres de grandeur écrits, pas un banc |
| **M15** | @jaisusx (S41) | RTX 5060 Ti 16 Go | Qwen**3.6**-27B Q4_K_M qui déborde de ~3 Go **7,7–9,2** → Qwen**3.8**-27B Q4-XYZ-v2 qui tient **26,3** | ≈ ×3 | ⚠️ deux modèles différents ; sa phrase : « A file that fits VRAM is worth more than the MTP flag » |

**Conclusion ✅** : « fichier qui tient » contre « fichier qui déborde » = **au moins ×2 en écriture** (M12 ×2,2 sur le même modèle ; M13, M14, M15 vont plus loin mais sont moins propres). Ne dis pas « ×20 ». Prix à dire : un fichier plus petit = plus compressé ; **aucune de ces pages ne mesure la qualité perdue**.
- **M16 ✅ [MESURE]** Paul's Programming Notes, 23/08/2026 (= S40) : Qwen3.8-27B UD-IQ4_XS, tout sur une 5060 Ti 16 Go, 64K, KV q4_0 : **≈ 24,9 tok/s**, 15 769 Mio sur 16 311 ; « spilling to system RAM collapses throughput » (aucun chiffre de débordement). Image Docker `server-cuda-v0.5.0` (tag llama.cpp **v0.5.0**, il existe). → https://www.paulsprogrammingnotes.com/2026/08/running-qwen-3-8-27b-16gb.html

## C. Les gros modèles à experts (MoE) qui débordent : régler les experts

- **M17 ⚠️ [MESURE] `--n-cpu-moe` ajusté.** InsiderLLM (Mark Bartlett), « A 177B Model on a 3060 », **08/09/2026, mis à jour le 05/10** : Qwen3.8-Flash-Next UD-IQ3_XXS, llama.cpp (tag v0.4.0, il existe). **RTX 3090 24 Go, 62 Go DDR4** : `-ncmoe 48` **16,85** → `-ncmoe 29` **22,60** (**+34 %**, d=0) ; `-ncmoe 26` = OOM. **RTX 3060 12 Go, 31 Go** : 8,66 → 9,64 (d=0), 10,92 → 12,22 (d=4096) (**+12 %**) ; `-ncmoe 38` = OOM. → https://insiderllm.com/guides/qwen3-8-flash-next-rtx-3090-3060-32gb/. ⚠️ Un seul auteur, pas de carte de 16 Go.
- **M18 ✅ [DEV] Le cache d'experts de llama.cpp** (`--moe-cache-mib`), PR #29887 d'am17an, **fusionnée le 07/10/2026** : Flash-Next Q4_0 93,7 Gio, sans MTP, EPYC 7742. **RTX 4090** : 25,0 → 39,4 (**×1,57**) ; **RTX 5090** : 30,8 → 67,8 (**×2,20**, `-cmoe --moe-cache-mib 19000`). → https://github.com/ggml-org/llama.cpp/pull/29887 (corps de la PR). ⚠️ Mesures de l'auteur du code, cartes de 24 et 32 Go.
- **M19 ⚠️ [MESURE] Le seul chiffre sur 16 Go.** Commit d'un fork (pieceofmindcloud/llama.cpp `6b99580`, Jair Pereira, **05/10/2026**) qui porte la PR : Flash-Next UD-IQ3_XXS 78 Go entier, **RTX 5060 Ti 16 Go, 62 Go de RAM**, `--cpu-moe` : D **14,95 → 19,26** (`--moe-cache-mib 8000`, **×1,29**), P inchangé (~89 tok/s). → https://github.com/pieceofmindcloud/llama.cpp/commit/6b99580c2cf7b20fce03e6e38be1b43c744166f5 (message du commit) ; relayé par DevelopersDigest, 09/10/2026 (https://www.developersdigest.tech/blog/llama-cpp-moe-offload-n-cpu-moe-vs-moe-cache-2026). **Une seule mesure.**
- **M20 ⚠️ [MESURE] Le « 4× » de la vidéo américaine** (Code Unpacked, « llama.cpp Just Made Huge MoE Models 4× Faster », 21/10/2026). Sa description : « 9.7 tokens per second became 37.2 ». **Source primaire** : ticket llama.cpp **#29949** de lich-77 (04/10/2026, **toujours ouvert le 15/11**), une branche **expérimentale non fusionnée** : **Radeon RX 7900 XTX 24 Go**, UD-IQ3_XXS, 9,7 → 37,2 tok/s (**×3,8**, sans MTP), 44,8 à 50 avec MTP ; même machine, cache fusionné #29887 **20,1** contre **31,2** pour la branche. La description elle-même dit : test indépendant sur PCIe 3.0 « roughly tied with the merged cache ». → https://github.com/ggml-org/llama.cpp/issues/29949 ; https://www.youtube.com/watch?v=ohp15NcKDhA. **Ce n'est pas la PR #29887, pas une carte de 16 Go, pas dans llama.cpp officiel.**
- **M21 ✅ [DEV] llama.cpp v1.0.0** (13/11/2026) intègre « a host-memory MoE expert cache with a configurable CPU share » (PR #30966, #31233, #31888) et le cache KV FP8 (`-ctk/-ctv f8_e4m3`) ; aucune vitesse chiffrée dans les notes. → https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0

**Conclusion** : sur 16 Go, le réglage des experts n'a **qu'une mesure** (M19, ×1,29). À dire : « sur les gros modèles à experts, régler où vont les experts a fait gagner de 10 à 30 % sur une carte de 12 à 16 Go, et beaucoup plus sur les grosses cartes » (M17 +12 % sur 12 Go, M19 +29 % sur 16 Go, M18 ×1,6 à ×2,2 sur 24-32 Go), en précisant **« une mesure chacune »** : ⚠️. **Ne dis pas 4×.**

## D. Contexte, cache KV, moteur, versions

**Contexte qui grandit : la vitesse baisse ✅**
- **M22 ✅** M5 (NJannasch, Qwen3.8-27B, 5060 Ti, sans MTP) : 29,18 (4K) → 23,62 (32K) → **19,77 (64K), −32 %** ; avec MTP 63,89 → 39,06 (−39 %).
- **M23 ✅** M12 (Glukhov, Qwen3.5-27B UD-IQ3_XXS, 4080) : 45,3 (19K) → **22,7 (64K)** → **9,6 (128K)** ; la charge CPU passe de 100 à 410 % à 64K : le cache du contexte **pousse le modèle hors de la carte**. Le MoE 35B-A3B reste plat (147,5 → 145,8 à 64K).
- **M24 ✅** M16 (Paul, 5060 Ti) : 24,9 → 21,9 après un prompt de 5 000 tokens (−12 %), prompt lu à 888 tok/s.
- **M25 ⚠️** NJannasch 25/04/2026 (relu), Qwen3.6 sur 5060 Ti : 27B 31 → 18 à 108K (−42 %), P 893 → 646 ; MoE 35B-A3B 98 → 53 à 108K (−46 %, « similar percentage »).
→ À dire : « sur un modèle de 27 milliards, passer de 4 000 à 64 000 tokens de conversation coûte un tiers de la vitesse, et plus si ça déborde ». Pour un MoE, les sources ne concordent pas (plat chez M23, −46 % chez M25) : **ne généralise pas**.

**Cache KV quantisé : pas de vitesse en plus ✅, de la place en plus ✅**
- **M26 ✅ [MESURE]** InventiveHQ, https://inventivehq.com/blog/kv-cache-quantization-quality-benchmark (26/06/2026), RTX 5060 Ti 16 Go, Qwen2.5-Coder-7B, 8K : f16 **81,8** · q8_0 **76,4** (−6,6 %) · q4_0 **80,3** (−1,8 %) ; VRAM −208 et −320 Mo ; similarité de sortie avec f16 : **81,6 %** (q8_0), **8,3 %** (q4_0, « quality cliff »).
- **M27 ✅ [MESURE]** nmaine, forum NVIDIA, 31/03/2026, DGX Spark, Nemotron-3-Nano-30B-A3B, llama.cpp b8399 : D f16 → q4_0 : −3,4 % (8K) à **−35,3 % (64K)** ; P à 64K **282,7 → 21,3 (−92,5 %)**. → https://forums.developer.nvidia.com/t/kv-cache-quantization-benchmarks-on-dgx-spark-q4-0-vs-q8-0-vs-f16-llama-cpp-nemotron-30b-128k-context/365138. ⚠️ Pas une carte de joueur.
- **M28 ✅ [MESURE] La place** : Autodidacts (M14) « without KV quantization, I can't get above ~32000 context. With it, I can get to 128000+ » ; Kai (S20 de `claude-ou-mon-pc-1`) : ~47 000 → ~110 000 tokens (cache 8 bits + vision coupée).
→ À dire : « le cache compressé ne va pas plus vite ; il fait tenir plus de conversation dans la carte, et c'est ça qui évite de ralentir ». q8_0 : risque faible mesuré ; q4_0 : à éviter sans test (M26).

**Changer de moteur**
- **M29 ⚠️ [MESURE]** InventiveHQ, https://inventivehq.com/blog/ollama-vs-llama-cpp-vs-lm-studio-benchmark (26/06/2026, maj 13/08) : RTX 5060 Ti, llama.cpp **77,0**, LM Studio **76,8**, Ollama **69,1** tok/s (−10,3 %). Modèle (Qwen2.5-Coder-7B) et « temps réel qui mêle D et P » : repris de B, non relus dans la page.
- **M30 ✅ [MESURE]** Arsen Apostolov, dev.to, **05/07/2026**, RTX 3090, 1 requête : Ollama → llama.cpp 129,3 → 157,2 (Qwen3-Coder 30B-A3B, ×1,22), 84,5 → 118,8 (Gemma 4 26B, ×1,41). Quand le modèle déborde : D identique (4,59 / 4,58 ; 7,6 / 7,65), mais **temps avant le premier mot 274 s contre 7,3 s** (GPT-OSS-120B). → https://dev.to/sikamikanikobg/vllm-vs-llamacpp-vs-ollama-what-happens-when-your-model-doesnt-fit-in-24gb-vram-56eb
→ À dire : « Ollama a été mesuré de 10 à 30 % plus lent que llama.cpp quand tout tient (deux testeurs) ; LM Studio, presque pareil que llama.cpp (un testeur) ».
- **M30b ✅ [DEV] LM Studio et le MTP** : 0.4.22 (28/08/2026) « Support for DFlash, DSpark, and MTP assistant drafters », moteur llama.cpp 2.29.1 ou plus ; 0.4.27 (29/10) « Fixed switching to bundled MTP retaining a previously selected draft model ». → https://lmstudio.ai/changelog/lmstudio-v0.4.22 ; …-v0.4.27. **Non vérifié** : que le MTP soit éteint ou allumé par défaut dans LM Studio.

**Une mise à jour peut ralentir ✅**
- **M31 ✅ [MESURE]** Strata, ticket #5115 (baiqvesse, 03/11/2026) : RTX 5080 16 Go, 2 × 32 Go DDR5-6400, Flash-Next IQ3_S, quatre bras en miroir : moteur 0.1.54 **117,0 / 111,2** contre 0.1.56 **86,1 / 84,9** (−25 % ; P 60K −14 %). Ticket #5121 (robsop99-beep, 03/11) : 88 contre 31 tok/s, même carte, 64 Go (ticket maigre). (= S11)
- **M32 ⚠️ [DEV]** Strata **0.2.14** (15/11/2026, 18:08 UTC ; moteurs 0.1.60 ; correctif 0.2.14.1 le même jour) : la lecture du prompt passe sur les noyaux de Strata. Sur **RTX 5070 Ti 16 Go, IQ3_S** : P à 20 000 tokens **1 408 contre 953** tok/s (0.2.13), mais **écriture plus lente : chat 17,5 (19,4), code 21,8 (23,8)**, soit environ −10 %. → https://github.com/Niko1221/Strata/releases/tag/v0.2.14. Chiffres du projet.

**Versions du jour (15/11/2026, vers 21 h UTC)**
- **M33 ✅** llama.cpp : **v1.0.0** stable, publiée le **13/11/2026** (= build nocturne b12359) ; dernier build nocturne **b12425** (15/11, 20:22 UTC). → https://github.com/ggml-org/llama.cpp/releases
- **M34 ✅** Ollama : **v0.40.16** stable (09/11/2026) ; v0.40.17-rc0 en préversion (10/11). → https://github.com/ollama/ollama/releases
- **M35 ✅** LM Studio : **0.4.28** (31/10/2026, build 2), lue sur https://lmstudio.ai/changelog/lmstudio-v0.4.28 ; aucune 0.4.29 trouvée. La version du moteur llama.cpp embarqué (« runtime ») **n'a pas été revérifiée** : ne la cite pas.
- **M36 ✅** Strata : **0.2.14** (15/11), moteurs 0.1.60. Ta vidéo : 0.2.13 / 0.1.59 (T1).

**Le modèle**
- **M37 ✅ [DEV] Paramètres de Qwen3.8-Flash-Next** (fiche officielle, `README.md`, dépôt créé le 24/08/2026) : « **125B with 6B activated, plus 51B n-gram embedding and 4B MTP** » ; 48 couches ; 512 experts, **10 routés + 1 partagé** ; total des poids (API) 179 999 981 459. La fiche du Coder d'ISTA écrit « The base model has **176.9B** parameters ». → https://huggingface.co/Qwen/Qwen3.8-Flash-Next ; https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF. **Tranché** : 125 et 177 sont justes tous les deux, ils ne comptent pas la même chose (177 ≈ 125 + la table de mots de 51 ; 180 avec le MTP). À dire, comme dans la vidéo Strata (T25) : « 125 milliards, 180 avec la table de mots ».

## E. La vidéo concurrente française et les erreurs des recherches

**M38 ⚠️ [AVIS / MESURE non vérifiable] Nathan Inline**, « Mon IA locale va 11 fois plus vite (même PC) », https://www.youtube.com/watch?v=VFC16Tb3lwU, **14/11/2026** (transcription relue en entier : `etudes/transcriptions/nathaninline-VFC16Tb3lwU.md`). RTX 5060 Ti 16 Go (+ RTX 3070 8 Go), Ryzen 9 3900X, « 46 Go » de DDR4 (0:44) mais « deux barrettes de 16 Go et deux barrettes de 8 Go » à 7:07, soit **48 Go** (incohérence non expliquée). Chiffres dits : llama.cpp **7,9** (1:22) → 2e carte 9,5 → moteur à cache d'experts 24,5 (1:51) → moteur MTP 58, 64, 70 (2:42-2:48) → Basalt 57 puis 94, P 2 200 (3:35-3:55) → tous les quants à 63, couche convertie **83** (4:15) → final « **83 en décode et 2200 en préfile** » (6:59). « 11 fois » (7:18) = 83 / 7,9 = **10,5**. Aucune version, aucun réglage, aucun nombre d'essais.
- **Ce qu'il nomme existe** (contrairement à `A-nathan.md`) : **Basalt** = moteur pour Flash-Next, « Linux with any NVIDIA Blackwell GPU (sm_120) » (d'où « les cartes qui commencent par 50 »), « a fork of Strata (MIT) », fichiers `.basalt` dont `UD-IQ2_XS` → https://huggingface.co/jesdga/Qwen3.8-Flash-Next-Basalt (créé le 06/10/2026), code https://github.com/jesdga95/basalt (non ouvert). **Tinfield-1** = fine-tune de Flash-Next → https://huggingface.co/badtheorylabs/Tinfield-1 (21/09/2026). **Swift** = https://huggingface.co/ukisai/Swift1.5-Qwen3.8-Flash-Next. **Edge Zero** = https://huggingface.co/Edge0/Edge0-145B-NVFP4. Existence seulement (API Hugging Face, 15/11) ; **aucune de ses vitesses n'est vérifiée**. Le « moteur à cache d'experts » et le « moteur dédié MTP » de septembre ne sont pas nommés (Strata probable, **non affirmé**).
- **83 contre 68** : au duel (6:01), « Tinfield gagne, 80 tokens par seconde contre 68 » pour Flash Next. **Il ne l'explique pas** (moteur, quant ou conditions non dits). Ne pas supposer de raison.
- **177 milliards** (0:06) : juste au sens d'ISTA (M37). « Plus de 48 couches » (0:59) : la fiche dit 48. « Seuls 10 travaillent » : 10 routés + 1 partagé.
- Sa perplexité 3,285 contre 3,273 (UD-IQ2_XS, 4:33-4:39) : une seule mesure, fichier non ouvert.
→ Usage : une phrase de contexte anonyme (« une chaîne française vient de passer de 8 à 83 tokens par seconde sur une 5060 Ti, en changeant surtout de moteur, avec un moteur qui ne marche que sur les cartes RTX 50 et sous Linux »). **Jamais son ×11 comme promesse** : une seule machine, partie d'un llama.cpp de fin août, sans versions ni réglages.

**Erreurs trouvées dans les recherches (corrigées ci-dessus)**

| Doc | Erreur | Correction |
|---|---|---|
| B §0 | « llama.cpp **b12425** » comme version du jour | Il y a une **v1.0.0 stable du 13/11** (M33, M21) ; b12425 n'est que le dernier build nocturne |
| B §0, §6a | Strata 0.2.14 « mesurée seulement sur Strix Halo » | Aussi RTX 4090, 5090, Mac et **RTX 5070 Ti 16 Go**, où l'écriture **baisse** d'environ 10 % (M32) |
| B §2 | ×1,29 sur 5060 Ti = « commentaire du fil de la PR » | C'est un **commit de fork** (M19), relayé par DevelopersDigest |
| B, `outliers` | Le « 4× » rattaché à la PR #29887 | Il vient du ticket **#29949** (branche non fusionnée, RX 7900 XTX 24 Go, ×3,8) (M20) |
| B §1, §4 | Autodidacts : « RTX 3080 16 Go, modèle douteux » | C'est une **3080 de PC portable**, qui existe en 16 Go (M14) |
| B §1, §3 | Glukhov « non datée » | Publiée le 04/04/2026, modifiée le 23/10/2026 (M12) |
| B §5a | « S19 : @jaisusx et autres » ; « 13 mesures » puis « 15 mesures » | Quatre contributeurs différents (M1 à M4, M6) ; le décompte change d'un paragraphe à l'autre ; **oublie** la mesure Qwen3.8 de NJannasch (M5, ×2,19), qui rend le −42 % (M10) ancien |
| B, classement | « Tout en VRAM : oui (4 sources) » | Une seule paire propre (M12) ; les autres changent de modèle ou forcent le débordement (M13, M15) : ✅ pour « au moins ×2 », pas pour « ×2 à ×3 » |
| A §1 | « 46 Go de DDR4 » | Il dit aussi 2 × 16 + 2 × 8 = 48 Go (M38) |
| A §2 | Basalt, Swift, Edge0, Tinfield-1 « introuvables » | **Ils existent tous** sur Hugging Face ; Basalt est un fork de Strata pour cartes Blackwell sous Linux (M38) |
| A §5 | « ×2 avec MTP » tiré de Nathan | Chez lui 24,5 → 58 change **de moteur** en même temps : ce n'est pas un ×2 du MTP seul |
| A §3 | 125 contre 177 « non tranché » | Tranché (M37) |
| C §4 | Propose trois nouveaux tests | **Contraire à la décision du 15/11** (vidéo calculée) : à ignorer |

## F. Chiffres de l'auteur (vidéo Strata du lun. 16/11)

**Un seul état, aucun avant/après** : Strata 0.2.13, moteur 0.1.59, Qwen3.8-Flash-Next **Coder IQ1_M**, contexte 128K, Pi 1.5.2, réflexion « high », RTX 5080 16 Go, Ryzen 7 9700X, 32 Go DDR5-6000. Détails : `../strata-test/sources.md` **T1** (version), **T41** (sessions), **T45** (moniteur), `recherche/C-strata-auteur.md`.

| Ce que tu as mesuré | Où (renvoi exact) |
|---|---|
| ≈ 70 tok/s en moyenne (69,4 / 67,8 / 66,1), de 43 à 84 selon la requête | T45 ; srt **3:14-3:18** (« Près de 70 en moyenne, et selon le test, ça va de 43 à 84 ») |
| 51 tok/s (50,8) sur l'histoire du dragon, cause non expliquée | T45 ; srt **3:06-3:11** |
| RAM 30,8 / 31 Go, lecture disque ≈ 165 à 183 Mo/s pendant le dragon | T45 ; srt **4:36-4:51** |
| « La vitesse baisse quand la conversation grandit » (chiffre du projet, 59 → 43, autre machine, T30) | srt **3:56-4:06** |
| Version : « note bien ta version » (aucun numéro dit) | srt **8:06** ; T1 |

Renvoi proposé dans la voix : « Lundi, dans la vidéo sur Strata, j'avais près de 70 tokens par seconde sur ma 5080. Aujourd'hui, pas de nouveau test : on regarde ce que les autres ont mesuré, réglage par réglage. » Ne présente **jamais** ces 70 comme un « avant ». Ton réglage de brouillon (MTP ou autre) dans Strata **n'a pas été relevé** : ne dis pas que le MTP te ferait passer à 140.

## G. Ce que le script peut dire / ne doit pas dire

| Peut dire | Ne doit pas dire |
|---|---|
| « Sur une carte de 16 Go, le MTP fait écrire un modèle de 27 milliards **jusqu'à 2 fois plus vite**, surtout sur du code : six testeurs, de ×1,9 à ×2,3 » (M1-M6) | « Ta carte ira 2 fois plus vite » sans condition : c'est l'**écriture**, sur un modèle **qui tient dans la carte**, avec un fichier qui contient le MTP |
| « La lecture du prompt, elle, ralentissait avec le MTP dans les premiers tests de mai » (M7) | « Tout va 2 fois plus vite » (M7 : P ×0,5 à ×0,6) |
| « Un fichier qui tient dans la carte va au moins 2 fois plus vite qu'un fichier qui déborde » (M12, M13, M14) | « ×20 » (M14, ordre de grandeur) ; ou que le petit fichier est aussi bon (non mesuré) |
| « Sur les gros modèles à experts, bien placer les experts a fait gagner de 10 à 30 % sur 12-16 Go, d'après une mesure chacune » (M17, M19) | « llama.cpp rend les MoE 4 fois plus rapides » (M20 : branche non fusionnée, carte de 24 Go) |
| « Le cache compressé ne va pas plus vite, il fait tenir 2 à 4 fois plus de conversation » (M26-M28) | « Compresse le cache pour aller plus vite » ; « q4_0 sans perte » (M26 : 8,3 % de similarité) |
| « Plus la conversation grandit, plus ça ralentit : un tiers de vitesse en moins à 64 000 tokens » (M22) | Une baisse chiffrée pour les MoE (M23 et M25 se contredisent) |
| « Ollama a été mesuré 10 à 30 % plus lent que llama.cpp quand tout tient » (M29, M30) | « Change de moteur et va 10 fois plus vite » (M38, non reproductible) |
| « Une mise à jour peut aussi ralentir » (M31, M32) | « Mets toujours à jour » sans réserve |
| « 125 milliards de paramètres, 180 avec la table de mots » (M37) | Que la chaîne française se trompe sur 177 (M37 : c'est un autre décompte) |
| Les gains ne s'additionnent pas : le MTP prend de la VRAM (M9), qui peut faire déborder (CALCUL) | Multiplier les leviers (« ×2 × ×2 × 1,3 = ×5 ») |
| Nommer les versions du 15/11 : llama.cpp v1.0.0, LM Studio 0.4.28, Ollama 0.40.16, Strata 0.2.14 (M33-M36), avec la date | Le numéro de runtime de LM Studio (non revérifié) |

## H. Le « ×N » du titre et de la miniature

**Tenable : « 2× » (ou « 2 fois »), et rien au-delà.** C'est le seul gain avec au moins deux mesures publiées concordantes sur 16 Go, même modèle, un seul réglage : **le MTP, en écriture** (six mesures, ×1,9 à ×2,3). Le « fichier qui tient » soutient aussi « au moins ×2 », mais avec une seule paire propre. Pas de « 3× », « 4× » ni « 10× ».

La miniature (compteur à « 2× », « TA CARTE BRIDÉE ? ») tient, **à condition** que la vidéo dise dans la première minute : écriture, modèle qui tient dans la carte, mesures d'autres testeurs. « Bridée » reste une question, pas un fait : dans llama.cpp, le MTP ne s'allume pas tout seul (`--spec-type draft-mtp`, M8) ; LM Studio le gère depuis la 0.4.22 (M30b), mais **son réglage par défaut n'est pas vérifié** ; dans Strata, un brouillon est choisi en « Auto » (notes 0.2.14).

Titres tenus par les sources :
1. **« Même carte, 2 fois plus rapide : le réglage mesuré sur 6 cartes de 16 Go »** (M1-M6)
2. **« Ton IA locale peut écrire 2 fois plus vite, sans changer de carte »** (M1-M6 ; « écrire » = decode)
3. **« 16 Go de VRAM : le réglage qui fait écrire 2 fois plus vite, et celui qui ne sert à rien »** (MTP M1-M6 ; cache KV M26-M27)

## Pages non ouvertes ou non retrouvées (15/11)

- Le ×1,54 sur RTX 5070 Ti (`--n-cpu-moe 20`, « r/LocalLLaMA ») de B §2 : source primaire non retrouvée par B, pas recherchée de nouveau ici : **❌ à ne pas citer**.
- Le ×1,28 de GloballyUniquePlaceholder (M11) et les ×2,2-2,4 d'USBhost (PR #22673) : non rouverts aujourd'hui.
- Giles Thomas (B §2, ×1,64) et Ian L. Paterson (B §3, §5a) : non rouverts ; ils ne servent pas au script.
- La perplexité du UD-IQ2_XS de Nathan (M38) : fichier non ouvert.
