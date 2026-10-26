# Modèles à tester sur ta 5080 (essais des 23 et 24 oct.)

> Pour la vidéo [« 16 Go de VRAM suffisent-ils pour remplacer Claude ? »](fiche.md) (sortie le 16 nov. depuis le 23/10). Recherche du 22/10/2026. Les chiffres sans source sont des **estimations** et sont marqués comme tels. `⚠️ à vérifier` = je n'ai pas pu le confirmer à la source.

> **25/10 : plus d'essais** (ta décision : ça te prend trop de temps). Ce plan ne se lance plus. Le document reste la base du calcul de la vidéo, maintenant calculée ([fiche](fiche.md)) : les tailles de fichiers, ce que tes 32 Go de RAM permettent, et les mesures de tiers sur une 5080 (Hardware IA : 13 tok/s pour le Q4 qui déborde ; sudoingX : 53,4 tok/s sans MTP et 101,3 avec ; Luke's Dev Lab : 17 et 40 tok/s sur une carte bridée à 70 W). Les sections 2 à 5 (ordre des essais, installation, mesures, planning) restent pour mémoire.

**Ta machine** : Ryzen 7 9700X (8 cœurs), B850M AORUS ELITE WIFI6E ICE, **32 Go** de DDR5-6000 (2 × 16 Go, EXPO déjà activé), RTX 5080 16 Go (Inno3D X3 OC), SSD 990 EVO Plus 2 To + P3 Plus 1 To, alimentation RM1000e. Tout ce document est calé sur cette machine.

**Ce que ça change, en une phrase** : avec 32 Go de RAM, tout ce qui demande 40 Go ou plus (Qwen3.8-Flash-Next complet, DeepSeek) est exclu, sauf le Coder de Flash-Next via Strata, à tenter (correction du 24/10, section 0.2). Il reste les modèles qui tiennent dans la carte, plus les « petits » modèles à experts (MoE) dont on pose 5 à 10 Go d'experts en RAM.

---

## 0. À retenir avant tout

1. **Le titre de la vidéo tient sur Qwen3.8-27B**, le modèle dense de Qwen sorti en août 2026, en quantification ISTA IQ3_S (11,77 Go). Son Q4 par défaut (16,46 Go) ne tient pas : d'après Hardware IA, le Q4 tombe à **13 tokens/s** sur une 5080 seule parce qu'il déborde en RAM. C'est ta scène « raté puis solution ».
2. **Le brouillon doit changer** : Qwen3.8-Flash-Next complet ne tourne pas avec 32 Go de RAM (voir 1.3). Il passe en modèle « calculé » pour « Combien coûte Claude en local ? » (23 nov.). **24/10** : sa version Coder via Strata est à tenter (section 0.2).
3. **Qwen 4 27B n'est pas sorti** au 22/10 : il a été annoncé (à l'Apsara du 22/09, d'après des sources secondaires), mais aucun poids n'est publié. Revérifie samedi matin.
4. **Ollama** : la version actuelle est la **0.40.8** (21/10), pas la 0.40.6. La faille Bleeding Llama (CVE-2026-7482) est corrigée depuis la 0.17.1. Ollama n'a pas de clé d'API intégrée : ne l'expose pas sur le réseau.
5. **Claude Code sur un modèle local fonctionne, mais Anthropic ne le prend pas en charge** : sa documentation dit qu'elle « ne prend pas en charge le routage de Claude Code vers des modèles autres que Claude ». Dis-le dans la vidéo : c'est du bricolage, et pi ou OpenCode sont prévus pour ça.

### 0.1 Mise à jour du 24/10 : le modèle à lancer dans LM Studio

- **Qwen3.8-Flash-Next ne passe pas dans LM Studio** : le plus petit fichier d'Unsloth (UD-IQ1_S) fait **72,5 Go**, et Unsloth demande « au moins 75 Go de RAM ou de mémoire unifiée ». Toi, tu as 16 + 32 = 48 Go, dont environ 40 utilisables.
- **Mais avec Strata, sa version Coder est à tenter** (correction du 24/10, voir 0.2).
- **Qwen 4 27B n'est toujours pas sorti** (annoncé à l'Apsara le 22/09, « en entraînement » au 13/10 d'après des sources secondaires).
- **Le choix : Qwen3.8-27B ISTA `GSQ-RCO-IQ3_S-mtp`** (11,8 Go + 0,35 Go de tête MTP). D'après ISTA, ses fichiers « tournent sans modification dans llama.cpp, Ollama et LM Studio ». Dans LM Studio, cherche `ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF` et choisis le fichier dans la liste.
  - Si l'écran reste branché sur la 5080, prends **`IQ3_XXS-mtp`** (10,1 Go) : il perd très peu (LiveCodeBench v6 à 84,6 contre 85,7 en BF16, mesure d'ISTA).
- **Vitesse mesurée sur une RTX 5080 16 Go** (llama.cpp, pas LM Studio, Q3_K_M avec 64 K de contexte, dépôt communautaire sudoingX/qwen38-mtp) : **53,4 tok/s sans MTP, 101,3 avec MTP** (n-max 2), pour 15,4 Go de VRAM. Ça confirme le haut de l'estimation du tableau 1.1.
- **MTP dans LM Studio** : il existe depuis la version 0.4.14, sur les GGUF seulement. Les exemples officiels sont des Qwen3.6 ; aucune source ne confirme Qwen3.8. `⚠️ à vérifier` : au chargement, l'option MTP doit apparaître. Si elle n'apparaît pas, mets à jour le moteur llama.cpp (Settings → Runtime) ; si elle manque toujours, la commande llama.cpp de la section 3.4 fait la même chose.
- **Réglages de chargement dans LM Studio** : GPU Offload au maximum, Flash Attention activée, contexte à 32 K (64 K seulement si l'écran est sur l'iGPU), cache KV en q8_0 à essayer contre f16 (voir l'issue #27623). Pour la mesure du « raté » : `unsloth/Qwen3.8-27B-GGUF`, fichier `UD-Q4_K_M` (16,46 Go).
- **« Répond vite »** : le mode thinking est actif par défaut en `xhigh`, donc le modèle réfléchit longtemps avant d'écrire. Garde-le pour les 3 tâches (c'est dans ce mode qu'ont été mesurés les scores de Qwen). Pour un plan de chat rapide, Qwen permet de le couper (`enable_thinking: false`, avec température 0,7, top-p 0,8, top-k 20 et presence penalty 1,5). Où se trouve cet interrupteur dans LM Studio : `⚠️ à vérifier`.
- **Pour plus de vitesse, mais moins de niveau** : Qwen3.6-35B-A3B (tableau 1.1, ligne 2). Dans LM Studio, le réglage « Force model expert weights onto CPU » pose ses experts en RAM.
- **Le concurrent : Swift 1.5 27B** (ajouté le 24/10, fiches Hugging Face lues ce jour-là). UkisAI a réentraîné Qwen3.8-27B pour qu'il réfléchisse moins.
  - **La version à prendre** : `ukisai/Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF`, fichier `IQ3_S-mtp` (12,12 Go). Ce sont exactement les tailles et le découpage des fichiers d'ISTA, appliqués à Swift. Évite `ukisai/Swift-Qwen3.8-27B-GGUF` : c'est Swift **1.0**, avec des tailles classiques (IQ3_XS à 13,0 Go, Q4_K_M à 18,0 Go).
  - **Ce qu'annonce UkisAI** (en BF16, réflexion en xhigh, 5 graines) : LiveCodeBench v6 à 81,7 % contre 76,8 % pour Qwen3.8-27B, Terminal-Bench 2.1 à 72,1 % contre 69,2 %, et environ 24 % de jetons en moins en code. En maths, il perd un peu (AIME 2026 : 96,0 % contre 98,7 %). Leur 76,8 % de base ne se compare pas au 85,7 d'ISTA : les deux bancs d'essai sont différents.
  - **Les limites** :
    - les seuls scores de code viennent d'UkisAI ;
    - le seul test indépendant ([MindStudio](https://www.mindstudio.ai/blog/qwen3-8-27b-swift-vs-original-thinking), 19/09, une seule tâche avec un agent) porte sur Swift **1.0**. Swift a fini plus vite (35 min 52 contre 47 min 07), mais avec 5 fois plus de jetons, et son animation est restée bloquée. Celle de Qwen marchait jusqu'au bout ;
    - sa compression est un peu moins fidèle que celle d'ISTA : en IQ3_S, l'écart (KLD) est plus grand sur 5 des 7 types de texte mesurés ;
    - sa licence : Swift Open License 1.0, gratuite jusqu'à 1 M$ de revenus par an ;
    - son MTP n'a pas été évalué. Pour la vitesse par jeton, il a la même architecture que Qwen3.8-27B, donc la même vitesse.
  - **À faire** : la tâche 1 de la grille 4.4 avec les deux modèles, puis garder le meilleur. Si Swift ne gagne pas nettement, reste sur ISTA, dont le nom « Qwen3.8-27B » est plus simple à expliquer au public.

### 0.2 Correction du 24/10 : Strata et le Coder de Flash-Next

> **Décision du 24/10** : pas de démo Strata dans cette vidéo. La démo reste sur Qwen3.8-27B dans LM Studio, comparée à Claude Code en `--safe-mode` (fonctions `claude-ref` et `claude-local` dans ton profil PowerShell). Strata passe en calculé dans [Combien coûte Claude en local ?](../cout-claude-local/fiche.md). Raison : [Luke's Dev Lab, Qwen 3.8 27B vs Strata Coder](https://www.youtube.com/watch?v=xiMAxAQAfC4) (23/10), sur 16 Go de VRAM et 32 Go de RAM : le Coder écrit environ 2 fois plus vite (40 contre 17 tok/s, carte bridée à 70 W), mais le 27B est plus soigné et plus autonome. La section 3.7 reste pour mémoire.

Le 22/10, j'avais écarté Strata en lisant seulement « 35 à 55 Go de RAM ». Sa doc (`docs/MODELS.md` et `docs/DETAILS.md`, lus le 24/10) prévoit ton cas.

- **Ce qui tient** : le **Coder** d'ISTA-DASLab (`Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF`).
  - C'est un Flash-Next **élagué** : il garde 256 des 512 experts de chaque couche, choisis sur du code (10 actifs par mot).
  - D'après ses auteurs : 91,3 % du score SWE-bench Verified du modèle complet et 98,7 % de son LiveCodeBench v6.
  - Le fichier chargé fait 29,6 Go, dont 23 Go d'experts. La table de 29 Go (Ngram) reste sur le SSD.
  - Strata : « a 32 GB PC with a 12-16 GB GPU [runs] the Coder » en mode RAM réduite **résident**. Les experts que la carte ne garde pas sont copiés en RAM au démarrage, et rien n'est lu sur le SSD pendant les réponses.
- **Dans la vidéo, ce n'est pas « Flash-Next »** mais « une version de Flash-Next réduite pour le code ». Les faits comptent.
- **Les limites** :
  - **Le français** : le Coder est « plus faible hors du code et dans les langues autres que l'anglais ». Un utilisateur a vu des réponses en chinois fausses ou qui bouclent (issue #438). Écris les prompts des 3 tâches en anglais ; un prompt en français peut faire une scène.
  - **Pas de mesure publique sur ta config** : les mesures avec 32 Go de RAM sont sous Linux. Exemple : une RTX 3060 12 Go fait tourner Flash-Next IQ2_XS (modèle complet) à **43 à 50 tok/s**, avec 20,5 Gio d'experts en RAM. Le Coder fait 55 tok/s sur une RTX 5070 avec 64 Go de RAM (mesure de l'auteur).
  - **Windows** : selon le README, Windows ne verrouille qu'environ la moitié de la RAM pour la carte graphique (d'où l'option `STRATA_PIN_BY_NEED`). Le premier chargement peut figer le PC 1 à 3 minutes.
  - **Ce n'est pas LM Studio** : Strata a son propre moteur, qui reprend des parties de llama.cpp. Il sert les API OpenAI et Anthropic sur `127.0.0.1:8080`, le même port que llama-server dans ce plan : n'en lance qu'un à la fois.
  - **Projet jeune** : créé le 24/09, environ 32 000 étoiles, 840 tickets ouverts, une version presque chaque jour (0.2.4 le 24/10). Note la version exacte dans la fiche d'essai. L'installeur n'est pas signé (SmartScreen).
- **Le préréglage à corriger** : Strata compte RAM + VRAM − 5 Go = 43 Go et te range dans la tranche 40 Go. Il te propose donc Swift 1.5 IQ2_XS (39,2 Go). Or ses experts (35,5 Go) ne tiennent pas en RAM : ils seraient lus en partie sur le SSD, beaucoup plus lentement. Choisis le Coder : `START-HERE.bat --setup --family coder`. Dans le journal, vérifie que le mode est **resident** et non **mmap**.
- **Disque** : environ 59 Go à télécharger (le fichier du Coder plus la table Ngram), et jusqu'à 23 Go de plus pour `experts.bin` en mode RAM réduite. Mets-le sur le 990 EVO Plus.
- **Ce que ça change si ça tourne** : Flash-Next passe de « calculé » à « testé » (règle du pilier 2), et [Combien coûte Claude en local ?](../cout-claude-local/script.md) (23 nov.) peut le montrer. À décider après la mesure.

Sources (24/10) : [Strata, README](https://github.com/Niko1221/Strata), [MODELS.md](https://github.com/Niko1221/Strata/blob/main/docs/MODELS.md), [DETAILS.md](https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md), [versions](https://github.com/Niko1221/Strata/releases), [ISTA-DASLab, Coder](https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF).

Sources du 24/10 : [Unsloth, Qwen3.8-Flash-Next](https://unsloth.ai/docs/models/qwen3.8-next) ; [ISTA-DASLab, GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF) ; [Qwen, fiche Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) ; [sudoingX/qwen38-mtp](https://github.com/sudoingX/qwen38-mtp) ; [LM Studio 0.4.14](https://lmstudio.ai/changelog/lmstudio-v0.4.14) ; [cellcog, Qwen 4](https://cellcog.ai/blog/qwen-4-release-date/).

---

## 1. Synthèse : quoi installer

### 1.1 Tableau

Place en VRAM : la 5080 a 16 Gio, soit **environ 17,1 Go** en unités décimales (celles de Hugging Face). Je retire environ 1 Go pour CUDA et les tampons de calcul (estimation), et 1 à 2,3 Go pour le bureau Windows si l'écran est branché sur la 5080.

| # | Modèle | Fichier (dépôt HF) | Taille | Contexte possible (estimation) | Vitesse d'écriture | Niveau en code (source) | Moteur |
|---|---|---|---|---|---|---|---|
| 1 | **Qwen3.8-27B** (dense) | `Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf` ([ISTA-DASLab](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)) | 12,12 Go | Écran sur l'iGPU : 64 K (cache KV q8_0) ou environ 48 K (f16). Écran sur la 5080 : environ 32 K (f16) | **Estimation** : 55 à 70 tok/s sans MTP. **Mesure** sur 5080 en Q4 qui déborde : 13 tok/s (d'après Hardware IA) | Terminal-Bench 2.1 : 73,0 ; SWE-bench Pro : 61,7 (Qwen, harnais Claude Code). Indice AA : 34 (xhigh) | llama.cpp |
| 1b | idem, plus léger | `Qwen3.8-27B-GSQ-RCO-IQ3_XXS-mtp.gguf` (ISTA) | 10,44 Go | Écran sur la 5080 : 64 K (q8_0) | **Estimation** : 65 à 80 tok/s | ISTA mesure LiveCodeBench v6 à 84,6 contre 85,7 en BF16 | llama.cpp |
| 2 | **Qwen3.6-35B-A3B** (MoE, 3 milliards de paramètres actifs) | `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf` ([unsloth MTP](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF)) | 18,21 Go | 64 K, avec environ 5 Go d'experts en RAM | **Estimation** : 40 à 80 tok/s. **Mesure** sur une 5070 Ti 16 Go, tout en VRAM, avec une autre quantification de 10,9 Go : 121 tok/s (d'après magnus919) | SWE-bench Verified : 73,4 (Qwen), 66,2 (harnais OpenCode, mesuré par Liquid AI) ; Terminal-Bench 2.1 : 44,4 (mesuré par NVIDIA) | llama.cpp (`--n-cpu-moe`) |
| 2b | idem, en Q4 | `Qwen3.6-35B-A3B-UD-Q4_K_M.gguf` (même dépôt) | 22,66 Go | 64 K, avec environ 10 Go d'experts en RAM | **Estimation** : 30 à 60 tok/s | idem (c't 3003 conseille ce Q4_K_M avec OpenCode, d'après ta note) | llama.cpp |
| 3 | **Nemotron 3.5 Bolt 74B-A9B** (MoE, 9 milliards actifs, sorti le 15/10) | `NVIDIA-Nemotron-3.5-Bolt-74B-A9B-IQ2_XXS.gguf` ([unsloth](https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF)) | 22,02 Go | 32 K pour commencer | **Estimation** : 15 à 35 tok/s. Aucune mesure publique sur 16 Go | Terminal-Bench 2.1 : 51,0 (NVIDIA, version IQ2) | llama.cpp (expérimental) |
| 4 | **Gemma 4 12B** (dense) | `gemma-4-12b-it-Q6_K.gguf` ([unsloth](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF)) | 9,79 Go | 64 K et plus | **Estimation** : 70 à 80 tok/s | LiveCodeBench v6 : 72,0 (Google, chiffre annoncé par l'éditeur). En agent, faible : un test indépendant a vu les 4 tâches échouer par dépassement de délai | llama.cpp ou LM Studio |
| 5 | **LFM2.5-24B-A2B** (MoE, 2,45 milliards actifs, sorti le 13/10) | `LFM2.5-24B-A2B-QAD-Q4_0.gguf` ([LiquidAI](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF)) | 13,58 Go | 32 à 64 K | **Estimation** : plus de 150 tok/s (estimation grossière) | SWE-bench Verified : 51,0 (harnais OpenCode, Liquid AI, chiffre de l'éditeur) | llama.cpp |

Comment j'estime les vitesses : un modèle qui tient en VRAM écrit à peu près à `bande passante × rendement ÷ taille lue par token`. La 5080 a 960 Go/s : 30 Gbit/s × 256 bits. Le bus de 256 bits et la GDDR7 sont confirmés par NVIDIA ; les 30 Gbit/s viennent de la presse (`⚠️ à vérifier` dans GPU-Z). Le rendement d'environ 0,8 vient d'une mesure sur une 4090 : 47 tok/s avec 17,6 Go de poids (computingforgeeks). Le MTP (prédiction de plusieurs tokens) a fait passer cette 4090 de 47 à 109 tok/s avec 8 K de contexte. Sur ta 5080, le gain du MTP reste `⚠️ à mesurer`.

### 1.2 Pourquoi ces 5-là, et pas les autres

- **Qwen3.8-27B** : le meilleur modèle ouvert de moins de 40 milliards de paramètres sur l'indice d'Artificial Analysis (34 contre 18 pour Qwen3.6-35B-A3B). C'est le seul qui fait un vrai « Claude ou mon PC ? ».
  - Ce que vaut la quantification : ISTA mesure son IQ3_S au niveau du BF16 (AIME25 100, GPQA-D 89,4 contre 89,9, LiveCodeBench v6 85,7 contre 85,7).
  - Chez Quesma (indépendant), le Q4_K_M égale le BF16 sur Terminal-Bench 2.1, et le Q2 perd nettement. Quesma n'a testé ni ISTA, ni Ridge, ni Bartowski.
- **Qwen3.6-35B-A3B** : le plus rapide des modèles sérieux, et celui que tout le monde conseille pour 16 Go. Il montre la technique des experts en RAM.
- **Nemotron 3.5 Bolt** : le plus récent (15/10). NVIDIA le présente comme « 74 milliards dans 24 Go ». Sur 16 Go, c'est un essai limite, donc une bonne scène (ça passe, ou pas).
- **Gemma 4 12B** et **LFM2.5** : des témoins rapides pour le chat. Kai les cite ; ne leur consacre qu'une heure.

Écartés :

| Modèle | Raison |
|---|---|
| **Qwen3.8-Flash-Next** (125 milliards, 6 actifs, licence Qwen Community) | Les fichiers Unsloth font 72,5 Go et plus. Strata demande « au moins 32 Go de RAM et de VRAM ensemble », mais son premier chargement « peut figer le PC 1 à 3 minutes et demande 35 à 55 Go de RAM ». Sa version Coder « demande 32 Go de RAM ». Avec 32 Go dont 6 à 8 pris par Windows : **exclu**. |
| **Strata** en général | ~~Même raison.~~ **Corrigé le 24/10** : le Coder de Flash-Next tient en mode RAM réduite résident (section 0.2). Son autre modèle, Qwen3.6-35B-A3B, se fait aussi bien avec llama.cpp (et les notes de version disent « Qwen3.6 sur Windows non testé »). |
| **DeepSeek V4 Flash**, **GLM-5.x** | Faits pour 128 Go et plus. FreeToken (moteur MoE pour Windows et Linux, RTX 30/40/50) les vise, mais pas avec 32 Go. |
| **Gemma 4 26B-A4B** | Faisable (MoE, 3,8 milliards actifs), mais faible en code : 25,8 sur SWE-bench Verified avec OpenCode (Liquid AI) et 37,2 sur Terminal-Bench 2.1 (NVIDIA). Qwen3.6 fait mieux en code au même prix. |
| **Nemotron 3.5 Lightning 30B-A3B** | Terminal-Bench 2.1 : 24,6 (NVIDIA). Derrière Qwen3.6. |
| **Devstral Small 2 24B** | Sorti en décembre 2025 (SWE-bench Verified 68,0 selon Mistral), donc pas récent. Son Q4_K_M d'environ 14 à 15 Go est trop juste. |
| **gpt-oss-20b** | Sorti en 2025. Utile seulement comme témoin si tu as du temps. |
| **Qwen 4 27B** | Pas sorti. |

### 1.3 Ce que permettent tes 32 Go de RAM

Windows prend 6 à 8 Go (ton chiffre ; vérifie dans le Gestionnaire des tâches). Il reste environ 24 Go pour les experts posés en RAM.

| Modèle | Experts en RAM | RAM restante | Verdict |
|---|---|---|---|
| Qwen3.6-35B-A3B UD-IQ4_XS (18,2 Go) | environ 5 Go | large | ✅ |
| Qwen3.6-35B-A3B UD-Q4_K_M (22,7 Go) | environ 10 Go | correcte | ✅ |
| Nemotron Bolt IQ2_XXS (22 Go) | environ 9 à 10 Go | correcte (Unsloth annonce 24 à 32 Go au minimum, RAM et VRAM comprises) | ⚠️ à tenter |
| Flash-Next complet (40 Go et plus) | plus de 25 Go | insuffisante | ❌ |
| Flash-Next **Coder** via Strata (29,6 Go, mode RAM réduite résident) | ce que la carte ne garde pas, sur 23 Go d'experts | juste (Strata garde environ 10 Go pour Windows) | ⚠️ à tenter (24/10, section 0.2) |

La vitesse de ta RAM limite celle des modèles MoE.
- Théorie : DDR5-6000 en double canal = 96 Go/s.
- En pratique, un Ryzen à un seul CCD comme le 9700X lit moins vite : environ 68 Go/s à 6000 d'après un utilisateur d'overclock.net (`⚠️ à vérifier`, mesure possible avec AIDA64).
- Plus tu poses d'experts en RAM, plus l'écriture ralentit : sur une 3090, Qwen3.6 passe de 158 tok/s sans experts en RAM à 36 tok/s avec tous en RAM (balayage cité par une recherche ; la page n'a pas été ouverte).

---

## 2. Ordre des essais (et pourquoi)

1. **Le circuit Windows → Mac avec Gemma 4 12B** : petit, rapide à télécharger, il tient sans réglage. Il valide le serveur, Tailscale, la clé et l'agent avant de perdre du temps sur les gros modèles.
2. **Claude (référence)** sur les 3 tâches de la grille (section 4.4) : il te faut le point de comparaison avant tout.
3. **Qwen3.8-27B** : le cœur de la vidéo. Dans l'ordre :
   - le raté (Q4_K_M qui déborde, environ 13 tok/s) ;
   - ISTA IQ3_S, puis IQ3_XXS ;
   - avec et sans MTP ;
   - cache KV f16 contre q8_0 ;
   - les 3 tâches dans Claude Code, puis dans pi.
4. **Qwen3.6-35B-A3B** : la vitesse et les experts en RAM. Balayage de `--n-cpu-moe`, puis l'essai du cache d'experts (`--moe-cache-mib`), puis les 3 tâches.
5. **Nemotron Bolt** : bonus de nouveauté. Si ça tient, la tâche 1 seulement.
6. **LFM2.5 et Gemma 4 12B** : vitesse et Arkanoid seulement.
7. **LM Studio** pour les plans de chat (interface plus jolie à filmer) et le plan sécurité (activer l'authentification).

---

## 3. Plan d'installation pas à pas

### 3.1 Windows : préparer la machine (vendredi matin)

**a. Pilote NVIDIA**
- Mets à jour le pilote Game Ready ou Studio depuis l'application NVIDIA, puis vérifie dans PowerShell avec `nvidia-smi` (en tête : version du pilote, version CUDA).
- Minimum : le build CUDA 13.x de llama.cpp demande un pilote **580 ou plus** (compatibilité des versions mineures de CUDA 13.x, notes de version NVIDIA). Les recettes Windows de NVIDIA ont été validées avec le pilote **610.88** et CUDA 13.4.
- Vise donc au moins 610.88 (`⚠️` aucun minimum officiel par plateforme n'est publié pour 13.x).
- À partir de novembre 2026, les nouveaux pilotes demanderont Windows 11 (`⚠️` à vérifier si tu es encore sous Windows 10).

**b. Repli en mémoire système**
- Panneau de configuration NVIDIA → Gérer les paramètres 3D → « CUDA - Sysmem Fallback Policy » → **Prefer No Sysmem Fallback**.
- Sans ça, quand un modèle déborde, Windows le fait discrètement tourner en partie sur la RAM partagée : ça ressemble au 13 tok/s de Hardware IA (c'est mon interprétation, `⚠️`). Avec ce réglage, tu obtiens une vraie erreur de mémoire.
- Pour filmer le raté exprès, remets « Driver Default » le temps de la scène.
- `⚠️` la page d'aide NVIDIA (a_id 5490) m'a renvoyé une erreur 403 ; les intitulés viennent de sources tierces.

**c. Libérer la VRAM du bureau (fortement conseillé)**
- Branche l'écran sur la sortie HDMI ou DisplayPort de la **carte mère** : la B850M en a une de chaque, qui passe par la puce graphique intégrée du 9700X.
- Vérifie dans le BIOS que la puce graphique intégrée est activée (`⚠️` le nom du réglage dépend du BIOS).
- Tu gagnes 1 à 2 Go sur la 5080 : c'est la différence entre 32 K et 64 K de contexte sur Qwen3.8-27B.
- Comme tu pilotes depuis le Mac, l'affichage du PC compte peu.
- Vérification : Gestionnaire des tâches → Performances → GPU 1 (la 5080) → « Mémoire GPU dédiée » doit rester presque à 0 avant de lancer un modèle.
- Tes deux écrans sont sur la 5080 (23/10) : un sur le HDMI de la carte mère, l'autre sur son DisplayPort. **Avant** de les débrancher, note `memory.used` au repos avec les deux écrans sur la 5080 : c'est ce que perd un spectateur dont les écrans sont sur sa carte, un chiffre à donner dans la vidéo. `⚠️` HDMI 1.4 et DisplayPort 1.4 d'après une fiche revendeur : un écran 4K en HDMI 1.4 plafonne à 30 Hz, préfère le DisplayPort pour lui.

**d. Outils**
- **llama.cpp** : sur https://github.com/ggml-org/llama.cpp/releases, prends la dernière version qui n'est **pas** marquée « pre-release ». Au 22/10, b11827 est une pre-release.
  - Télécharge `llama-bXXXXX-bin-win-cuda-13.4-x64.zip` **et** `cudart-llama-bin-win-cuda-13.4-x64.zip`.
  - Dézippe les deux dans le même dossier, par exemple `C:\llama`.
  - Vérifie avec `C:\llama\llama-server.exe --version`, puis `--help | findstr moe-cache` : la ligne `--moe-cache-mib` doit apparaître (fusionnée le 7/10).
- **CLI Hugging Face** : `pip install -U huggingface_hub` → commande `hf`. Si Python n'est pas installé : `winget install Python.Python.3.12`.
- **Tailscale** : https://tailscale.com/download (Windows et Mac), avec le même compte sur les deux machines.
- **Pas de mesure électrique** (décidé le 23/10) : ni wattmètre ni HWiNFO. Le seul coût de la vidéo est l'achat du matériel.
- **LM Studio** (facultatif, pour les plans de chat) : https://lmstudio.ai. L'API compatible Anthropic existe depuis la version 0.4.1.

**e. Dossier des modèles** sur le 990 EVO Plus (le plus rapide pour le chargement), par exemple `D:\models`.

### 3.2 Télécharger les modèles (lance-le dès vendredi 9 h, environ 105 Go)

```powershell
cd D:\models
hf download ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf Qwen3.8-27B-GSQ-RCO-IQ3_XXS-mtp.gguf --local-dir .
hf download unsloth/Qwen3.8-27B-GGUF Qwen3.8-27B-UD-Q4_K_M.gguf --local-dir .          # le « raté » de 16,46 Go
hf download unsloth/Qwen3.6-35B-A3B-MTP-GGUF Qwen3.6-35B-A3B-UD-IQ4_XS.gguf --local-dir .
hf download unsloth/gemma-4-12b-it-GGUF gemma-4-12b-it-Q6_K.gguf --local-dir .
hf download LiquidAI/LFM2.5-24B-A2B-GGUF LFM2.5-24B-A2B-QAD-Q4_0.gguf --local-dir .
hf download unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF NVIDIA-Nemotron-3.5-Bolt-74B-A9B-IQ2_XXS.gguf --local-dir .
# facultatif : hf download unsloth/Qwen3.6-35B-A3B-MTP-GGUF Qwen3.6-35B-A3B-UD-Q4_K_M.gguf --local-dir .
```

Les noms de fichiers ont été relevés le 22/10 dans les listes de fichiers des dépôts. Ne fais pas `--include "*IQ2_XXS*"` sur Bolt : il y a deux fichiers de 22 Go qui y correspondent.

### 3.3 La clé d'API (une seule, partagée par tous les serveurs)

Sur le Mac :
```bash
openssl rand -hex 24                      # copie le résultat
security add-generic-password -a "$USER" -s llama-5080 -w 'COLLE_LA_CLE_ICI'
```
Sur Windows, mets la même clé, seule sur une ligne, dans `C:\llama\cle.txt`. `--api-key-file` évite que la clé apparaisse dans la commande, et donc à l'écran.

### 3.4 Lancer le serveur, modèle par modèle (PowerShell, dans `C:\llama`)

Réglages communs, présents dans toutes les commandes ci-dessous :
- `--host 127.0.0.1` : le serveur n'écoute que la machine. C'est Tailscale qui l'ouvre au Mac (section 3.5).
- `--port 8080` : précise-le toujours. Le README de llama-server annonce maintenant 9931 par défaut.
- `--api-key-file` et `--metrics`.
- `-fa on` (flash attention), `--jinja` (gabarit de chat avec appels d'outils), `--parallel 1`.

**1. Qwen3.8-27B, plan A (écran sur l'iGPU)**
```powershell
.\llama-server.exe -m D:\models\Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf --alias qwen3.8-27b `
  -ngl 999 -fa on -c 65536 -ctk q8_0 -ctv q8_0 `
  --spec-type draft-mtp --spec-draft-n-max 2 `
  --jinja --parallel 1 --temp 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 `
  --host 127.0.0.1 --port 8080 --api-key-file C:\llama\cle.txt --metrics
```

Plan B (écran sur la 5080) : même commande avec `Qwen3.8-27B-GSQ-RCO-IQ3_XXS-mtp.gguf`. Autre option : IQ3_S avec `-c 32768` sans `-ctk/-ctv` (cache f16).

Variantes à mesurer :
- **Sans MTP** : retire les deux options `--spec-*`.
- **Cache KV en f16** : retire `-ctk q8_0 -ctv q8_0`. Un utilisateur a vu le cache q8_0 ralentir l'écriture de 13 à 6 tok/s sur une carte sm_89 (issue llama.cpp #27623, non résolue). Mesure les deux.
- Le cache KV de ce modèle est petit : seules 16 couches sur 64 en gardent un, soit environ 2,3 Go par tranche de 32 K tokens en f16 (Quesma). Le cache q8_0 occupe environ 63 % du f16, et non 50 % (d'après une mesure tierce).
- Les échantillonneurs sont ceux du mode « thinking » de la fiche Qwen. Le raisonnement est à `xhigh` par défaut ; Artificial Analysis note 34 en xhigh, 28 en medium et 26 en low. Garde la valeur par défaut. La façon de la changer dans llama.cpp est `⚠️ à vérifier`.

**Le raté à filmer (Q4 qui déborde)** :
- Lance `Qwen3.8-27B-UD-Q4_K_M.gguf` dans LM Studio, avec le repli mémoire de NVIDIA remis sur « Driver Default ».
- Affiche le Gestionnaire des tâches : la « mémoire GPU partagée » monte.
- Note les tok/s, qu'on peut comparer aux 13 tok/s de Hardware IA.

**2. Qwen3.6-35B-A3B (experts en RAM)**
```powershell
.\llama-server.exe -m D:\models\Qwen3.6-35B-A3B-UD-IQ4_XS.gguf --alias qwen3.6-35b-a3b `
  -ngl 999 --n-cpu-moe 14 -fa on -c 65536 -t 8 `
  --spec-type draft-mtp --spec-draft-n-max 2 `
  --jinja --parallel 1 --temp 0.6 --top-p 0.95 --top-k 20 --presence-penalty 0.0 `
  --host 127.0.0.1 --port 8080 --api-key-file C:\llama\cle.txt --metrics
```
- `--n-cpu-moe N` garde en RAM les experts des N premières couches (le modèle a 40 couches).
- Valeurs de départ (estimation) : **14** si l'écran est sur la 5080, **10 à 11** s'il est sur l'iGPU.
- Trouve le bon N avec le balayage ci-dessous, puis prends la plus petite valeur qui ne sature pas la VRAM au contexte voulu :
  ```powershell
  .\llama-bench.exe -m D:\models\Qwen3.6-35B-A3B-UD-IQ4_XS.gguf -ngl 999 -fa 1 -ncmoe 10,12,14,16,18 -p 512 -n 128 -r 3
  ```
  (`⚠️` vérifie avec `llama-bench --help` que l'option `-ncmoe` existe bien dans llama-bench.)
- Autre réglage, automatique : retire `-ngl` et `--n-cpu-moe` et laisse `--fit` (actif par défaut) répartir. Lis dans le journal où il a posé les experts.
- Essai bonus du cache d'experts (PR #29887) : remplace `--n-cpu-moe 14` par `-cmoe --moe-cache-mib 8000`.
  - Tous les experts vont en RAM (environ 16 Go, c'est possible avec tes 32 Go), et 8 Go de VRAM servent de cache.
  - Sur une 5090, ce mode a donné 67,8 tok/s contre 30,8 avec `--fit`, mais sur un autre modèle.
  - Le cache ne sert qu'à l'écriture (lots de 32 tokens au plus) et dépend du PCIe : vérifie dans GPU-Z que la carte est en PCIe 5.0 x16 (`⚠️` la génération du slot de la B850M n'est pas vérifiée).
- `-t 8` = tes 8 cœurs physiques. Essaie aussi 16.

**3. Nemotron 3.5 Bolt (expérimental)**
```powershell
.\llama-server.exe -m D:\models\NVIDIA-Nemotron-3.5-Bolt-74B-A9B-IQ2_XXS.gguf --alias nemotron-bolt `
  -fa on -c 32768 -t 8 --jinja --parallel 1 `
  --host 127.0.0.1 --port 8080 --api-key-file C:\llama\cle.txt --metrics
```
- Pas de `-ngl` ni de `--n-cpu-moe` : je ne connais pas son nombre de couches, donc laisse `--fit` décider.
- Si le chargement échoue, ajoute `-cmoe`.
- La recette NVIDIA pour Windows vise 28 Go (RTX 5090) : rien n'est garanti sur 16 Go.

**4. Gemma 4 12B**
```powershell
.\llama-server.exe -m D:\models\gemma-4-12b-it-Q6_K.gguf --alias gemma-4-12b `
  -ngl 999 -fa on -c 65536 --jinja --parallel 1 --temp 1.0 --top-p 0.95 --top-k 64 `
  --host 127.0.0.1 --port 8080 --api-key-file C:\llama\cle.txt --metrics
```

**5. LFM2.5-24B-A2B**
```powershell
.\llama-server.exe -m D:\models\LFM2.5-24B-A2B-QAD-Q4_0.gguf --alias lfm2.5-24b `
  -ngl 999 -fa on -c 32768 --jinja --parallel 1 `
  --host 127.0.0.1 --port 8080 --api-key-file C:\llama\cle.txt --metrics
```
Les échantillonneurs (température 0,1, top-k 50) sont inscrits dans le GGUF.

**LM Studio (pour le chat)** :
- Developer → Server Settings : active **Require Authentication**, puis Manage Tokens → Create Token.
- Laisse **Serve on Local Network** désactivé : Tailscale fera le pont (`tailscale serve --bg 1234`).
- Un seul serveur à la fois sur le pont Tailscale : `tailscale serve reset` entre les deux.

### 3.5 Le réseau : Tailscale, sans rien ouvrir

Le choix retenu : le serveur reste sur `127.0.0.1`, et **Tailscale Serve** le rend accessible **seulement aux appareils de ton tailnet**, en HTTPS. Aucun port n'est ouvert sur la box ni sur le réseau local, et aucune règle de pare-feu n'est à créer. La clé d'API protège en plus.

1. Installe Tailscale sur les deux machines et connecte-les au même compte. Sur la console web, active **MagicDNS** et les **certificats HTTPS** (Serve les demande ; la commande te propose de les activer).
2. Sur Windows (PowerShell), une fois `llama-server` lancé :
   ```powershell
   tailscale serve --bg 8080
   tailscale serve status        # affiche https://<nom-du-pc>.<tailnet>.ts.net
   ```
   Pour fermer : `tailscale serve reset`. N'utilise **jamais** `tailscale funnel`, qui publie sur Internet. (`⚠️` la syntaxe `--bg` vient d'une documentation tierce ; la doc officielle montre `tailscale serve 3000`. Lance `tailscale serve --help` pour confirmer.)
3. Test depuis le Mac :
   ```bash
   export LLAMA_5080_URL=https://<nom-du-pc>.<tailnet>.ts.net
   export LLAMA_5080_KEY="$(security find-generic-password -s llama-5080 -w)"
   curl -s "$LLAMA_5080_URL/v1/models" -H "Authorization: Bearer $LLAMA_5080_KEY"
   curl -s "$LLAMA_5080_URL/v1/chat/completions" -H "Authorization: Bearer $LLAMA_5080_KEY" \
     -H "content-type: application/json" \
     -d '{"model":"qwen3.8-27b","messages":[{"role":"user","content":"Dis bonjour en une phrase."}],"max_tokens":300}' \
     | python3 -m json.tool
   # le format Anthropic, celui qu'utilise Claude Code :
   curl -sS "$LLAMA_5080_URL/v1/messages" -H "Authorization: Bearer $LLAMA_5080_KEY" \
     -H "anthropic-version: 2023-06-01" -H "content-type: application/json" \
     -d '{"model":"qwen3.8-27b","max_tokens":50,"messages":[{"role":"user","content":"Bonjour"}]}'
   ```
   Sans clé, `/v1/models` doit répondre 401 : vérifie-le une fois.

**Plan B sans Tailscale (réseau local seulement)** :
- Lance le serveur avec `--host <IP du PC sur le réseau local>`, par exemple 192.168.1.20, et non 0.0.0.0.
- Le réseau Windows doit être en profil « Privé ».
- N'autorise que l'IP du Mac :
  ```powershell
  New-NetFirewallRule -DisplayName "llama-server (Mac seulement)" -Direction Inbound -Protocol TCP `
    -LocalPort 8080 -RemoteAddress 192.168.1.42 -Profile Private -Action Allow
  ```
- Ici le trafic passe en clair (HTTP) sur ton réseau local, et la clé aussi : c'est une raison de préférer Tailscale.

**Ollama, si tu l'utilises quand même** :
- Version 0.17.1 au minimum (Bleeding Llama), 0.40.8 aujourd'hui.
- Laisse `OLLAMA_HOST` à sa valeur par défaut (127.0.0.1:11434). Ollama n'a pas de clé d'API : passe par `tailscale serve --bg 11434`, jamais `OLLAMA_HOST=0.0.0.0`.
- Son contexte par défaut est de 4 096 tokens : règle `OLLAMA_CONTEXT_LENGTH=65536`.
- Tu ne peux pas régler finement les experts en RAM avec Ollama, d'où le choix de llama.cpp ici.

### 3.6 Le Mac : brancher l'agent

**Claude Code**
- llama-server parle le format Anthropic Messages (`/v1/messages`, depuis la PR #17570). LM Studio aussi (depuis 0.4.1), ainsi qu'Ollama et Strata.
- Pour ne **pas** toucher à ton abonnement Claude, qui sert de référence, crée une fonction plutôt que de modifier `settings.json`. Ajoute-la à `~/.zshrc` :
  ```bash
  claude-5080() {
    ANTHROPIC_BASE_URL="https://<nom-du-pc>.<tailnet>.ts.net" \
    ANTHROPIC_AUTH_TOKEN="$(security find-generic-password -s llama-5080 -w)" \
    ANTHROPIC_MODEL="${MODELE_5080:-qwen3.8-27b}" \
    CLAUDE_CODE_MAX_CONTEXT_TOKENS=65536 \
    CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1 \
    CLAUDE_CODE_ATTRIBUTION_HEADER=0 \
    CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 \
    claude "$@"
  }
  ```
- Ce que fait chaque variable (documentation de Claude Code) :
  - `ANTHROPIC_AUTH_TOKEN` envoie `Authorization: Bearer`, ce que lit `--api-key`. Il prend le pas sur ta connexion claude.ai, qui reste enregistrée.
  - `CLAUDE_CODE_MAX_CONTEXT_TOKENS` : pour un identifiant de modèle inconnu, Claude Code suppose 200 K de contexte ; on lui donne le vrai.
  - `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` évite les erreurs 400 sur les champs que le serveur ne connaît pas.
  - `CLAUDE_CODE_ATTRIBUTION_HEADER=0` : conseillé par LM Studio ; garde le début du prompt identique, donc le cache utile.
  - `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` coupe la télémétrie et les mises à jour pendant la session.
- Vérification : `claude-5080`, puis `/status` → la ligne « Anthropic base URL » doit montrer ton URL. **Floute-la au montage.**
- Limite `⚠️` :
  - Le compactage automatique ne descend pas sous 100 K (`CLAUDE_CODE_AUTO_COMPACT_WINDOW` est ramené à 100 K au minimum).
  - Avec 64 K côté serveur, une longue session finira en erreur « contexte dépassé » au lieu de se compacter : lance `/compact` à la main.
  - Que `CLAUDE_CODE_MAX_CONTEXT_TOKENS` règle ce problème n'est pas confirmé par la doc.
  - Ollama conseille 64 K au minimum pour Claude Code, LM Studio plus de 25 K.

**pi** (`@earendil-works/pi-coding-agent`, version 1.4.0 du 21/10 ; l'ancien paquet `@mariozechner/...` est obsolète)
```bash
npm install -g @earendil-works/pi-coding-agent
```
`~/.pi/agent/models.json` :
```json
{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "pc5080": {
      "baseUrl": "https://<nom-du-pc>.<tailnet>.ts.net/v1",
      "api": "openai-completions",
      "apiKey": "!security find-generic-password -s llama-5080 -w",
      "models": [
        { "id": "qwen3.8-27b", "contextWindow": 65536, "maxTokens": 16384, "reasoning": true },
        { "id": "qwen3.6-35b-a3b", "contextWindow": 65536, "maxTokens": 16384, "reasoning": true }
      ]
    }
  }
}
```
- Le `!commande` est lu à chaque requête, d'après la doc de pi.
- Lance `pi`, puis `/model` → `qwen3.8-27b`.
- pi a aussi un fournisseur llama.cpp intégré (`/login llama.cpp`, variables `LLAMA_BASE_URL` et `LLAMA_API_KEY`), mais il attend le **mode routeur** de llama-server (sans `-m`, avec `--models-preset`). Le fichier `models.json` ci-dessus est plus simple pour des essais modèle par modèle.

**OpenCode** (version 1.19.4 au 22/10) : `npm install -g opencode-ai`, puis `~/.config/opencode/opencode.json` :
```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "pc5080": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "RTX 5080",
      "options": { "baseURL": "https://<nom-du-pc>.<tailnet>.ts.net/v1", "apiKey": "{env:LLAMA_5080_KEY}" },
      "models": {
        "qwen3.8-27b": { "name": "Qwen3.8 27B (5080)", "limit": { "context": 65536, "output": 16384 } },
        "qwen3.6-35b-a3b": { "name": "Qwen3.6 35B A3B (5080)", "limit": { "context": 65536, "output": 16384 } }
      }
    }
  }
}
```
Avant de lancer `opencode`, exporte la clé avec `export LLAMA_5080_KEY="$(security find-generic-password -s llama-5080 -w)"`. (`⚠️` la place de `apiKey` dans `options` vient de la doc des fournisseurs personnalisés et n'a pas été testée.)

**Hermes Agent et DeepSeek Harness** (à garder pour plus tard) :
- **Hermes Agent** refuse les modèles de moins de **64 K** de contexte. Il passe avec Qwen3.6 et avec Qwen3.8 en plan A. Configuration : `hermes model` → Custom Endpoint (URL en `/v1` + clé).
- **DeepSeek Harness** est en developer preview, sous licence MIT, avec des changements cassants annoncés. Sa configuration pour un modèle local (`settings.yaml`, `openai-completions`) ne vient que de guides tiers (`⚠️`). D'après une revue, il envoie les journaux de session à DeepSeek par défaut avec l'API officielle.
- Pas pour ces deux jours.

**Premier test de bout en bout** : dans un dossier vide, lance `claude-5080 -p "Crée hello.py qui affiche Bonjour, puis exécute-le"`. Le fichier doit apparaître et s'exécuter. Refais le même test dans pi.

### 3.7 Strata sur Windows : le Coder de Flash-Next (ajouté le 24/10)

Pourquoi ce modèle et ses limites : section 0.2. Docs lues le 24/10 : `INSTALL.md`, `TERMINAL_LAUNCH.md`, `MODELS.md`, `DETAILS.md`, `TROUBLESHOOTING.md` du dépôt Niko1221/Strata.

**a. Avant d'installer**
- **Ferme LM Studio pour de bon** (icône près de l'horloge → Quit), sinon il garde de la VRAM et de la RAM. Strata a besoin des deux. S'il tourne en service : `lms unload --all` puis `lms server stop`. Les ports ne se gênent pas (LM Studio 1234, Strata 8080), c'est la mémoire qui compte.
- **Arrête llama-server** s'il tourne : il prend le même port 8080.
- **Ferme Chrome** et les gros programmes : avec 32 Go, chaque Go de RAM compte.
- Pilote NVIDIA **580 ou plus** (`nvidia-smi`).
- Au moins **90 Go libres** sur `D:` (990 EVO Plus).
- Écran sur l'iGPU si possible : Strata garde alors 512 Mio de VRAM pour l'affichage au lieu de 1 536.

**b. Installer le Terminal** (sans droits d'administrateur, dans `%LOCALAPPDATA%\Strata\terminal`)
```powershell
irm https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex
```
Pour le lire avant : `irm https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 -OutFile $env:TEMP\strata-install.ps1`, puis `notepad $env:TEMP\strata-install.ps1`.

Ouvre ensuite une **nouvelle** fenêtre PowerShell, puis lance `strata doctor` (il vérifie le PC et la carte).

**c. Lancer le Coder** : `strata launch --data-dir D:\Strata`, puis dans les écrans :

| Écran | Choix | Pourquoi |
|---|---|---|
| 2. Model | **Coder** (pas Swift 1.5, qu'il risque de proposer) | Seul modèle qui tient en RAM avec 32 Go (section 0.2) |
| 3. Folder | `D:\Strata` | Le SSD rapide |
| 4. Context | **64K**, mémoire en **8-bit** (`m`) ; 32K si l'écran dit « does not fit » | Le prompt système de Claude Code est long ; Strata teste ses connexions à 32K |
| 5. Pictures | **No** | Inutile pour le code, et 0,9 Go de RAM gagnés |
| 6. Parallel | **1** | Une requête à la fois |
| 7. Tuning | **skip** au premier lancement, puis **quick** (environ 20 min, une seule fois) | Vérifier d'abord que ça démarre |
| 8. Advanced | Ne touche à rien. Lis la commande exacte : elle doit contenir **`--resident-experts`**, pas `--mmap-experts` | En `mmap`, une partie des experts est lue sur le SSD, beaucoup plus lentement |
| 9. Access | **This computer only** (127.0.0.1) si Claude Code tourne sur le PC ; **Tailscale** avec clé s'il tourne sur le Mac | « This computer only » n'a pas besoin de clé |
| 10. Preset | `Coder 64K` | Pour relancer avec `strata launch --preset "Coder 64K"` |

- **Premier chargement** : le PC peut figer 1 à 3 minutes, jusqu'à 10. N'y touche pas. S'il est encore figé après 10 minutes : redémarre, ferme tout, recommence.
- **Si le moteur s'arrête au démarrage** : relance sans la couche MTP (environ 1 Go de VRAM), avec `--mtp off`.
- **Si le PC rame une fois lancé** : le problème connu des PC de 32 Go se règle avec `--set STRATA_RESIDENT_PIN=0` (issue #649).
- **Vérifier** :
  - `strata status --url http://127.0.0.1:8080 --json` ;
  - `strata monitor --url http://127.0.0.1:8080` : vitesses de lecture et d'écriture en direct, un bon plan à filmer ;
  - `strata launch --show-key` affiche la clé si tu en as mis une. Ne la filme pas.
- **Note dans la fiche d'essai** : la version (`strata update --check`), le mode `resident` ou `mmap`, le contexte et le MTP.

**d. Brancher Claude Code**
- Strata le prend en charge depuis la 0.1.17 : `ANTHROPIC_BASE_URL=http://127.0.0.1:8080` (sans `/v1`), un nom de modèle Claude que Claude Code connaît (Strata l'ignore), n'importe quel `ANTHROPIC_AUTH_TOKEN` (ou ta clé), et `CLAUDE_CODE_MAX_CONTEXT_TOKENS`.
- Pour avoir la configuration exacte : `strata connect` affiche la liste des applications ; `strata connect <nom affiché pour Claude Code>` donne les variables ; ajoute `--check` pour envoyer un prompt et un appel d'outil de test.

**e. Une comparaison équitable, sans clé d'API et sans tes MCP**
- **`claude --safe-mode`** lance Claude Code sans CLAUDE.md, skills, plugins, hooks, serveurs MCP, commandes et mémoire auto. Ta connexion à l'abonnement, le choix du modèle et les outils de base marchent normalement (doc de Claude Code, `cli-reference`).
  - Ne prends pas `--bare` : ce mode ne lit pas ta connexion claude.ai et demande une clé d'API.
  - Utilise le **même** mode pour Claude (référence) et pour Strata : les deux ont alors exactement les mêmes outils.
- **La tâche 3 teste une règle du CLAUDE.md**, que `--safe-mode` ne charge pas. Donne-la aux deux de la même façon : `--append-system-prompt-file .\CLAUDE.md`.
- **Aucune requête ne part chez Anthropic avec Strata**, aucune clé d'API n'est demandée : tout va vers `127.0.0.1:8080`. Côté référence, c'est ton abonnement. Vérifie une fois que `$env:ANTHROPIC_API_KEY` est vide : s'il est rempli, Claude Code paierait à l'usage au lieu de passer par l'abonnement.
- Deux fonctions pour ton profil PowerShell (`notepad $PROFILE`) :
  ```powershell
  # Référence : ton abonnement Claude, sans tes MCP ni tes plugins
  function claude-ref { claude --safe-mode @args }

  # Strata : même Claude Code, cerveau local
  function claude-strata {
    $vars = @{
      ANTHROPIC_BASE_URL                       = "http://127.0.0.1:8080"
      ANTHROPIC_AUTH_TOKEN                     = "strata"   # ou la clé de `strata launch --show-key`
      ANTHROPIC_MODEL                          = "claude-sonnet-5-5"   # ignoré par Strata
      CLAUDE_CODE_MAX_CONTEXT_TOKENS           = "65536"   # = le contexte choisi à l'écran 4
      CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS   = "1"
      CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC = "1"
    }
    try {
      foreach ($k in $vars.Keys) { Set-Item "env:$k" $vars[$k] }
      claude --safe-mode @args
    } finally {
      foreach ($k in $vars.Keys) { Remove-Item "env:$k" -ErrorAction SilentlyContinue }
    }
  }
  ```
  Le `finally` retire les variables en sortant, pour que `claude-ref` ne parte pas par erreur vers Strata.
- **Vérifier** : dans `claude-strata`, `/status` doit montrer `http://127.0.0.1:8080` ; dans `claude-ref`, ta connexion claude.ai. Les deux sessions sans MCP : `/mcp` ne doit rien lister.
- **Pour les 3 tâches** (section 4.4), écris les prompts **en anglais** : le Coder est plus faible dans les autres langues. Exemple pour la tâche 3 : `claude-strata --append-system-prompt-file .\CLAUDE.md`, puis le prompt.
- Le niveau de réflexion par défaut de Strata est `high` : garde-le pour les mesures.

---

## 4. Mesures

### 4.1 Avant de filmer (checklist)

- [ ] RAM à 6000 MT/s : Gestionnaire des tâches → Performances → Mémoire → « Vitesse ».
- [ ] Pilote ≥ 610.88 (`nvidia-smi`) et repli mémoire réglé (section 3.1 b).
- [ ] Écran sur l'iGPU, et la 5080 presque vide au repos.
- [ ] GPU-Z : bus PCIe de la carte (5.0 x16 ?) et débit de la mémoire.
- [ ] Journal GPU lancé avant chaque essai (PowerShell) :
  ```powershell
  nvidia-smi --query-gpu=timestamp,memory.used,utilization.gpu,temperature.gpu,clocks.mem --format=csv -l 1 > D:\mesures\gpu-<modele>-<essai>.csv
  ```
- [ ] Clé et nom du tailnet hors du champ, ou flous au montage.
- [ ] Capture d'écran du Mac (le terminal de l'agent) et du PC (Gestionnaire des tâches → GPU) en même temps.

### 4.2 Le protocole (le même pour chaque modèle)

1. **Vitesse brute** : `llama-bench.exe -m <fichier> -ngl 999 -fa 1 -p 512,4096 -n 128 -r 3` (ajoute `-ncmoe N` pour les MoE). Note `pp512`, `pp4096` (lecture) et `tg128` (écriture), moyenne de 3 passes.
2. **En situation réelle** : chaque réponse de llama-server contient un bloc `timings`, avec `prompt_per_second` (lecture) et `predicted_per_second` (écriture). Le journal du serveur les affiche aussi. Note-les pour la tâche 1 à contexte court, puis à environ 30 K tokens de contexte (la tâche 3) : la vitesse baisse quand le contexte grandit.
3. **VRAM** : le maximum de `memory.used` dans le CSV. **RAM** : le Gestionnaire des tâches.
4. **Reproductible** :
   - Pour la vitesse, l'échantillonnage compte peu.
   - Pour comparer à Hardware IA, refais leur Arkanoid avec la température à 0 et la graine 42 (`--temp 0 --seed 42`).
   - Pour la qualité, garde les échantillonneurs conseillés par chaque éditeur : Qwen déconseille le mode glouton (température 0) en mode thinking.

### 4.3 La fiche à remplir pour chaque essai

| Champ | Exemple |
|---|---|
| Date et heure | 23/10 15 h 10 |
| Moteur et version | llama.cpp b11xxx (CUDA 13.4) / LM Studio x.y |
| Fichier exact | Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp.gguf |
| Réglages | `-c 65536 -ctk q8_0 -ctv q8_0`, MTP n=2, écran sur l'iGPU |
| Lecture / écriture (tok/s) | pp512 = … / tg128 = … |
| Vitesse à 30 K de contexte | … |
| VRAM max / RAM utilisée | … / … |
| Tâche : réussite ? | oui / non, nombre de coups de pouce |
| Durée de la tâche | … |
| Remarques (ratés, plantages) | … |

### 4.4 La grille de 3 tâches, identiques pour Claude et pour la 5080

Prépare-les vendredi matin dans un dépôt de test à part, pas dans `youtubeSkill`. Fais un `git commit` de l'état de départ, et un `git reset --hard && git clean -fd` entre deux essais.

1. **Arkanoid en un seul fichier** (le prompt de Hardware IA, traduit) : « Arkanoid jouable dans un seul fichier HTML, sans bibliothèque. Briques de couleurs, raquette à la souris, score, vies et fin de partie. Fond sombre. Seulement le code. »
   - Critère : le jeu se lance et fonctionne.
   - C'est le plan le plus visuel, et il se compare à leur 5080.
2. **Corriger des bugs dans un petit projet** : un module d'environ 150 lignes (Python ou JS) avec 3 bugs plantés et une suite de tests qui échoue. Prompt : « Les tests échouent. Trouve et corrige les bugs sans modifier les tests. »
   - Critère : tous les tests passent, sans toucher aux tests.
   - Ça teste la boucle agent : lire, éditer, exécuter.
3. **Une fonctionnalité sur plusieurs fichiers, avec une règle du projet** : une copie de ton outil de miniatures (`ressources/miniatures/`) dans le dépôt de test, avec son `CLAUDE.md`. Prompt : « Ajoute une variante `?n=11` à la charte verte. »
   - Critère : la variante est ajoutée **et** les listes en dur de `rendre.sh` et de `psd.py` sont mises à jour. Cette règle est écrite dans le CLAUDE.md : tu vérifies si le modèle la suit.
   - Ce contexte long (environ 20 à 30 K tokens, estimation) sert aussi à la mesure de vitesse « à 30 K ».

Pour chaque tâche, note la réussite, le nombre de tes interventions, la durée et les tok/s. Côté Claude, note le modèle et le mode utilisés.

---

## 5. Planning indicatif

**Vendredi 23**

| Heure | Quoi |
|---|---|
| 9 h – 9 h 30 | Pilote, repli mémoire, écran sur l'iGPU, vérification de la RAM. Lancer **tous** les téléchargements (3.2). |
| 9 h 30 – 10 h 30 | llama.cpp, `hf`, Tailscale (deux machines), clé d'API (3.3), dossier `D:\mesures`. |
| 10 h 30 – 11 h 30 | Circuit complet avec Gemma 4 12B : serveur → `tailscale serve` → curl depuis le Mac → Claude Code, pi, OpenCode (3.5 et 3.6). |
| 11 h 30 – 12 h 30 | Préparer le dépôt des 3 tâches. Faire passer les 3 tâches à **Claude** (référence). |
| 14 h – 14 h 45 | Qwen3.8-27B : le raté Q4_K_M dans LM Studio (à filmer), puis ISTA IQ3_S avec llama-bench. |
| 14 h 45 – 15 h 30 | Qwen3.8-27B : MTP oui/non, cache f16/q8_0, 32 K/64 K, IQ3_S/IQ3_XXS. Choisir la meilleure configuration. |
| 15 h 30 – 17 h 30 | Qwen3.8-27B : les 3 tâches dans Claude Code, puis dans pi. |
| 17 h 30 – 19 h | Qwen3.6-35B-A3B : balayage de `-ncmoe`, essai de `-cmoe --moe-cache-mib`, tâche 1. |
| Soir | Copier les CSV et les rushes sur le 2e SSD. Relire les fiches de mesures. |

**Samedi 24**

| Heure | Quoi |
|---|---|
| 9 h – 9 h 15 | Vérifier si Qwen 4 27B est sorti (si oui, l'ajouter en tête de la journée). |
| 9 h 15 – 10 h 30 | Qwen3.6-35B-A3B : tâches 2 et 3 (Claude Code ou OpenCode). |
| 10 h 30 – 12 h | Nemotron Bolt : chargement, llama-bench, tâche 1 si ça tient. |
| 12 h – 12 h 45 | LFM2.5 et Gemma 4 12B : vitesse et Arkanoid seulement. |
| 14 h – 15 h 30 | Plans propres pour le montage : l'agent qui code depuis le Mac, `nvidia-smi` (VRAM) en gros plan, Arkanoid côte à côte (Claude contre 5080). |
| 15 h 30 – 16 h 15 | LM Studio : plans de chat et plan sécurité (Require Authentication, `tailscale serve`). |
| 16 h 15 – 17 h | Refaire les mesures douteuses (3 passes). |
| 17 h – 18 h | Tableau final des résultats + sauvegarde. Relever les prix des cartes (prévu les 24 et 25 oct. dans la fiche). |

---

## 6. Points ⚠️ les plus importants

1. **La place du contexte sur Qwen3.8-27B** est une estimation (taille du fichier + cache KV mesuré par Quesma + environ 1 Go de tampons). Vérifie-la avec `nvidia-smi` avant de promettre « 64 K » à l'écran.
2. **Les vitesses sur ta 5080 sont toutes des estimations**, sauf le 13 tok/s du Q4 qui déborde (Hardware IA). Il n'existe aucune mesure publique d'ISTA IQ3_S ou de Nemotron Bolt sur une 5080.
3. **Claude Code avec un modèle local** :
   - non pris en charge par Anthropic ;
   - compactage automatique pas en dessous de 100 K ;
   - effet réel de `CLAUDE_CODE_MAX_CONTEXT_TOKENS` sur un serveur à 64 K non vérifié.
4. **Cache KV q8_0** : un ralentissement possible sous CUDA a été signalé (issue #27623) ; mesure f16 contre q8_0.
5. **Nemotron Bolt sur 16 Go + 32 Go** : non documenté ; les recettes NVIDIA visent 28 Go de mémoire vidéo.
6. **Le repli mémoire de NVIDIA** est la cause probable du 13 tok/s (mon interprétation) ; la page d'aide officielle n'a pas pu être lue.
7. **La bande passante réelle de ta RAM** (un seul CCD) et la **génération PCIe du slot** : à lire dans AIDA64 et GPU-Z.
8. **La syntaxe `tailscale serve --bg`** : à confirmer avec `tailscale serve --help`.

---

## 7. Sources (consultées le 22/10/2026)

**Modèles**
- ISTA-DASLab, Qwen3.8-27B-GSQ-RCO-GGUF (fichiers, tailles, LCB/GPQA par quantification) : https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
- Qwen, fiche Qwen3.8-27B (architecture, Terminal-Bench 2.1, SWE-bench Pro, échantillonneurs) : https://huggingface.co/Qwen/Qwen3.8-27B
- Unsloth, Qwen3.8-27B-GGUF (UD-Q4_K_M 16,46 Go, fichier MTP) : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
- Empero AI, Qwen3.8-27B-Ridge-GGUF (12,59 Go ; 54 tok/s sur une RTX PRO 6000) : https://huggingface.co/empero-ai/Qwen3.8-27B-Ridge-GGUF
- Quesma, « Qwen3.8 27B quantizations benchmarked » (26/08/2026 ; cache KV f16 d'environ 2,3 Go par 32 K) : https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/
- computingforgeeks, Qwen3.8-27B sur une 4090 (47 tok/s, 109 avec MTP ; mis à jour le 27/09/2026) : https://computingforgeeks.com/run-qwen3-8-27b-locally/
- Hardware IA, « Qwen 3.8 27B en dos GPUs de 16 GB » (01/09/2026 ; 13 tok/s sur une 5080 seule, protocole Arkanoid avec température 0 et graine 42, d'après la description de la vidéo) : https://www.youtube.com/watch?v=rH993Bf1sK8
- llama.cpp, issue #27623 (cache KV et décodage sur Qwen3.8-27B, ouverte) : https://github.com/ggml-org/llama.cpp/issues/27623
- Qwen, fiche Qwen3.6-35B-A3B (avril 2026, Apache 2.0) : https://huggingface.co/Qwen/Qwen3.6-35B-A3B
- Unsloth, Qwen3.6-35B-A3B-GGUF (benchmarks Qwen, échantillonneurs) : https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF et la variante MTP : https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF
- magnus919, Qwen3.6 sur une 5070 Ti 16 Go (27/05/2026, 121 tok/s, mesure) : https://magnus919.com/2026/05/running-a-35b-moe-model-on-a-16gb-consumer-gpu/
- dev.to, choisir `--n-cpu-moe` pour Qwen3.6 sur 12, 16 et 24 Go (estimations) : https://dev.to/donald_lee_707b59c456e304/how-to-pick-n-cpu-moe-in-llamacpp-qwen36-35b-a3b-on-12-16-and-24-gb-gpus-43f3
- Unsloth, Nemotron 3.5 Bolt GGUF (15/10/2026, OpenMDW-1.1, Terminal-Bench 2.1 de 50,98) : https://huggingface.co/unsloth/NVIDIA-Nemotron-3.5-Bolt-74B-A9B-GGUF ; guide : https://unsloth.ai/docs/models/nemotron-3.5-bolt
- Unsloth, gemma-4-12b-it-GGUF : https://huggingface.co/unsloth/gemma-4-12b-it-GGUF ; LiveCodeBench 72,0 d'après des relais du chiffre de Google (benchmarklist.com) ; test agent raté d'après haimaker.ai
- Liquid AI, LFM2.5-24B-A2B (tableau SWE-bench Verified avec OpenCode, comparaison avec Qwen3.6, Gemma 4 26B et Nemotron Lightning) : https://huggingface.co/LiquidAI/LFM2.5-24B-A2B et https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF
- Qwen, Qwen3.8-Flash-Next (125 milliards, 6 actifs, qwen-community-1.0) : https://huggingface.co/Qwen/Qwen3.8-Flash-Next ; Unsloth (fichiers de 72,5 Go et plus) : https://unsloth.ai/docs/models/qwen3.8-next
- Strata (README, version 0.2.2 du 21/10, besoins en RAM) : https://github.com/Niko1221/Strata et https://github.com/Niko1221/Strata/releases
- FreeToken : https://github.com/FlashML-org/FreeToken
- Artificial Analysis, modèles ouverts « small » (indice d'intelligence, estimations) : https://artificialanalysis.ai/models/open-source/small
- Qwen 4 27B non sorti, d'après des sources secondaires : https://www.yottalabs.ai/post/qwen-4-27b-release-date-specs-hardware-what-is-known-2026 et https://llmlearner.com/models/qwen4-27b
- NVIDIA, Nemotron 3.5 Lightning (Terminal-Bench 2.1 de 24,58) : https://docs.api.nvidia.com/nim/reference/nvidia-nemotron-3-5-lightning-30b-a3b
- Luke's Dev Lab, `model-configs.ini` (configurations llama.cpp sur une carte de 16 Go) : https://github.com/lukesdevlab/youtube

**Moteurs et matériel**
- llama.cpp, versions (fichiers Windows CUDA 13.4) : https://github.com/ggml-org/llama.cpp/releases
- llama.cpp, README du serveur (`--api-key-file`, `--n-cpu-moe`, `--fit`, `--moe-cache-mib`, `-ctk`) : https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
- llama.cpp, PR #29887 (cache GPU des experts, 7/10/2026) : https://github.com/ggml-org/llama.cpp/pull/29887 ; issue #29949 (branche expérimentale, lich-77) : https://github.com/ggml-org/llama.cpp/issues/29949
- Hugging Face, « New in llama.cpp: Anthropic Messages API » (19/01/2026) : https://huggingface.co/blog/ggml-org/anthropic-messages-api-in-llamacpp
- NVIDIA, Local AI Inference Recipes (recettes pour Windows, pilote 610.88 et CUDA 13.4, RTX 5090) : https://github.com/NVIDIA/local-ai-inference-recipes
- NVIDIA, RTX 5080 (16 Go GDDR7, 256 bits, 360 W) : https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/
- NVIDIA, notes de version de CUDA 13.4 (pilote 580 ou plus pour 13.x) : https://docs.nvidia.com/cuda/archive/13.4.2/cuda-toolkit-release-notes/index.html
- Bande passante de 960 Go/s (30 Gbit/s) d'après la presse : https://www.notebookcheck.net/RTX-5080-will-boast-34-higher-memory-bandwidth-than-its-predecessor-according-to-recent-leak.933536.0.html. **Confirmé le 25/10** par la fiche d'Inno3D de ta X3 OC (« Memory Clock 30Gbps », « 960 GB/sec ») : https://www.inno3d.com/product/inno3d-geforce-rtx-5080-x3-oc
- Bande passante d'un seul CCD, d'après overclock.net : https://www.overclock.net/threads/amd-ddr5-oc-and-24-7-daily-memory-stability-thread.1800926/post-29086941
- Repli mémoire de NVIDIA, d'après Cognex : https://docs.cognex.com/deep-learning_400/web/EN/deep-learning/Content/Topics/optimization/gpu-disable-shared.htm
- Gigabyte B850M AORUS ELITE WIFI6E ICE (sorties HDMI et DisplayPort) : https://www.gigabyte.com/Motherboard/B850M-AORUS-ELITE-WIFI6E-ICE-rev-1x/sp

**Réseau et agents**
- Claude Code, passerelles et variables : https://code.claude.com/docs/en/llm-gateway, https://code.claude.com/docs/en/llm-gateway-connect.md, https://code.claude.com/docs/en/llm-gateway-protocol.md, https://code.claude.com/docs/en/model-config.md
- LM Studio, Claude Code : https://lmstudio.ai/docs/integrations/claude-code ; authentification : https://lmstudio.ai/docs/developer/core/authentication
- Ollama, FAQ (`OLLAMA_HOST`, `OLLAMA_CONTEXT_LENGTH`) : https://docs.ollama.com/faq ; Claude Code : https://docs.ollama.com/integrations/claude-code ; versions (0.40.8 du 21/10) : https://github.com/ollama/ollama/releases
- Bleeding Llama, CVE-2026-7482 (corrigée en 0.17.1) : https://labs.cloudsecurityalliance.org/research/csa-research-note-ollama-bleeding-llama-cve-2026-7482-ai-inf
- Tailscale Serve : https://tailscale.com/docs/features/tailscale-serve
- pi, documentation de la version 1.4.0 (`models.json`, llama.cpp, RTX) : https://cdn.jsdelivr.net/npm/@earendil-works/pi-coding-agent@1.4.0/docs/models.md, https://cdn.jsdelivr.net/npm/@earendil-works/pi-coding-agent@1.4.0/docs/llama-cpp.md, https://cdn.jsdelivr.net/npm/@earendil-works/pi-coding-agent@1.4.0/docs/nvidia-rtx-llama-cpp.md ; versions sur le registre npm
- OpenCode, fournisseurs : https://opencode.ai/docs/providers
- Hermes Agent, démarrage (contexte de 64 K minimum) : https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- DeepSeek Harness (sources secondaires) : https://cryptobriefing.com/deepseek-harness-open-source-developer-preview/ et https://computingforgeeks.com/deepseek-harness-local-model/
