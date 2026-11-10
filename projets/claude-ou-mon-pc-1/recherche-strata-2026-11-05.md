# Recherche Strata et 16 Go : mesures publiées (consultées le 05/11/2026)

> Pour [« Abonnement ou IA locale ? #1 : 16 Go suffisent »](fiche.md), vidéo **calculée** (aucun essai). Complète [`modeles-5080.md`](modeles-5080.md) (section 0.2) et [`references.md`](references.md). Tout ce qui est ici a été relu le **05/11/2026** sauf mention contraire.
>
> **Types** : `MESURE` = chiffre publié par un utilisateur ou un tiers, avec sa machine ; `DEV` = affirmation de l'auteur du projet ou du modèle (pas indépendante) ; `AVIS` = témoignage ou opinion ; `CALCUL` = déduction de ma part, pas une source. `non trouvé` = je n'ai rien trouvé.
>
> **Limites de cette recherche** : Reddit refuse l'accès direct (les posts r/LocalLLaMA cités viennent de miroirs « reddit.sentinel-team.org », donc des instantanés) ; la transcription des vidéos YouTube a été bloquée (erreur 429), donc je n'ai lu que titres, descriptions, chapitres et vues ; X/Twitter : rien de retrouvable. Pas de chiffre inventé : ce qui manque est dit.

## 0. En bref

**Ce qui tient « 16 Go suffisent »**
- Une carte de 16 Go fait tourner **Qwen3.8-27B en Q3 à 45-101 tok/s** avec MTP (S18, S20), et un modèle à experts type **Qwen3.6-35B-A3B à 79-98 tok/s avec 32 Go de DDR5** en llama.cpp sans Strata (S25).
- **Strata + le Coder tourne sur ta config presque exacte** : une RTX 5070 Ti 16 Go, un Ryzen 7 9700X, 31,2 Gio de RAM, Windows 11 : **70 tok/s** en chat court, 79 tok/s en session d'agent, 2 500 à 3 100 tok/s de lecture de prompt (S9, 02/11, une seule mesure).
- Sur le papier, le 27B et Flash-Next sont proches d'Opus 4.6 sur les tableaux de Qwen (S29, S30) ; Kai résume : 11,8 Go de fichier, mais le vrai sujet est la mémoire du contexte (S20).

**Ce qui fragilise la thèse**
- **La RAM est le vrai verrou, pas la VRAM.** Les 5080 mesurées sur Strata ont **64 à 96 Go de RAM** (S11 à S14) ; avec **32 Go**, seul le **Coder** passe (S5, S6), un Flash-Next élagué de moitié, « plus faible hors du code » (S6), jugé « pas aussi bon, perte notable » par un utilisateur (S17) et qui a **échoué** dans le test Claude Code de Samayas (S35).
- **Aucune mesure Strata sur 5080 + 32 Go de RAM** (non trouvé) ; la mesure la plus proche est celle d'une 5070 Ti (S9), sans test de qualité.
- **Strata sur 5080 est instable en ce moment** : régression de vitesse de 25 % entre deux versions (S11), 88 → 31 tok/s (S11), erreur « non-finite logits » (S14).
- **Le 27B n'est pas Claude** : Artificial Analysis donne Terminal-Bench 4.0 à **6 % contre 46 %** pour Opus 5 (S31). Et le Q4 par défaut déborde sur 16 Go et s'effondre (S21, S22).

---

## A. Strata : ce que c'est

**S1 [DEV]** Strata est un moteur d'inférence gratuit et open source (licence MIT) pour Windows, Linux et Mac, avec une appli de bureau et un terminal (`strata launch`). Il sert des API compatibles OpenAI et Anthropic en local (utilisables avec Claude Code, Codex CLI, OpenCode). Modèles : **Qwen3.8-Flash-Next** (le modèle phare), Qwen3.6-35B-A3B, DeepSeek V4.1-Flash. Dépôt créé le 24/09/2026, **40,3 k étoiles**, version **0.2.10 publiée le 02/11/2026**, **1 349** tickets et demandes de fusion ouverts (731 + 618) le 05/11.
→ https://github.com/Niko1221/Strata et https://api.github.com/repos/Niko1221/Strata (relevé 05/11/2026). Mon relevé : `modeles-5080.md` notait 32 k étoiles et 840 tickets le 24/10, le projet continue de gonfler.

**S2 [DEV]** Comment il fait tenir un gros modèle : le GPU garde les experts les plus utilisés, **la RAM garde le reste des experts**, et la table de mots (« n-gram », 29 Go) reste sur le SSD. Règle donnée : « le modèle tient quand la RAM est au moins égale aux experts plus environ 10 Go ». Mémoire annoncée pour Flash-Next (RAM + VRAM) : Q2_0 37,6 Go ; IQ2_XS 39,2 Go ; IQ3_XXS 47,0 Go ; IQ3_S 54,8 Go. Experts en RAM : 34 / 35,5 / 43 / 50 Go ; **Coder : 23 Go**.
→ https://github.com/Niko1221/Strata/blob/main/docs/MODELS.md (relu 05/11/2026).

**S3 [DEV]** La doc dit : « 64 Go de RAM : toutes les tailles passent ; 48 Go : Q2_0 et IQ2_XS ; **32 Go : utilise le Coder** » (DETAILS.md). Une carte plus grosse « rend plus rapide mais ne baisse pas la RAM nécessaire, sauf en mode RAM réduite ».
→ https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md (lignes 95-109, relu 05/11/2026).

**S4 [DEV]** Les tailles de Flash-Next : **125 milliards de paramètres de langage + 51 milliards de table n-gram + 4 milliards de MTP, 180 milliards au total** pour la fiche Hugging Face ; **6 milliards actifs** ; 512 experts, 10 routés + 1 partagé par mot ; contexte 262 144.
→ https://huggingface.co/Qwen/Qwen3.8-Flash-Next (05/11/2026). *Chiffres contradictoires* : références.md dit « 177 milliards » (titre de Luke's Dev Lab) et modeles-5080.md « 125 milliards » : **les deux sont justes selon qu'on compte la table n-gram ou non**. Dis « 125 milliards (180 avec la table de mots) ».

## B. Strata avec 32 Go de RAM : ce qui rentre vraiment

**S5 [DEV]** « Mode RAM réduite » : Strata ne garde en RAM que ce que le GPU ne tient pas. Texte exact de la doc : « A 32 GB PC with a 24 GB GPU runs Q2_0, IQ2_XS and the Coder this way. A 32 GB PC with a **12 to 16 GB GPU runs the Coder**. With a small GPU, most experts come from the SSD and it is much slower. »
→ https://github.com/Niko1221/Strata/blob/main/docs/MODELS.md#coder (05/11/2026). Donc, même avec le mode RAM réduite, **le Flash-Next complet n'est annoncé qu'avec une carte de 24 Go sur 32 Go de RAM**, pas avec 16 Go.

**S6 [DEV]** Le Coder (ISTA-DASLab, `Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF`) : il **garde 256 des 512 experts** de chaque couche (choisis sur du code, de l'agentique et de l'image), un seul fichier IQ1_M (1,89 bit par poids d'après un blog tiers, S28), **58,4 Go au total dont 29,6 Go qui doivent être en mémoire** (23 Go d'experts) et 28,8 Go de table sur le SSD. Il est « plus faible hors du code et dans les langues autres que l'anglais et le chinois/japonais/coréen ». La fiche le qualifie de « **release expérimentale** ».
→ https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF (05/11/2026).

**S7 [DEV, chiffres changés]** Qualité du Coder annoncée par ses auteurs, **mise à jour le 17/10/2026** : SWE-bench Verified **79,2 contre 82,8** pour le modèle complet (**95,7 %**) ; LiveCodeBench v6 **87,43 contre 87,43** (100 %). La version d'avant : 75,6 et 86,28.
→ même fiche Hugging Face. *Contradiction* : le README de Strata et `modeles-5080.md` disent encore **91 % et 99 %** (ce sont les anciens chiffres : 75,6 ÷ 82,8 = 91 %). À citer : « 95 % du score de code du modèle complet, d'après ses auteurs ».

**S8 [CALCUL] Ce que ça donne pour tes 32 Go de DDR5.** Règle de Strata : experts + 10 Go de RAM. Coder : 23 + 10 = **33 Go**, soit un peu plus que tes 32 Go (32 Go de DDR5 = 32 Gio = environ 34,4 Go décimaux, et Windows en réserve une partie ; Strata mélange Go et Gio dans sa doc, donc la limite est à ras). Le mode RAM réduite sert précisément à ce cas (S5) : la carte de 16 Go garde une partie des experts, il en reste moins en RAM. Flash-Next complet : Q2_0 = 34 + 10 = 44 Go, IQ3_S = 50 + 10 = 60 Go, donc **exclus sur 32 Go** (même verdict que `modeles-5080.md`).

**S9 [MESURE] La mesure la plus proche de ta machine.** Utilisateur « guilleortas », issue #4997, **02/11/2026** : **RTX 5070 Ti 16 Gio, Ryzen 7 9700X, 31,2 Gio de RAM, SSD 990 PRO 2 To, Windows 11**, pilote 621.01, Strata 0.1.55 (moteur 0.1.54), **Coder IQ1_M**, contexte 65 536, option `--resident-experts`. Résultats médians (suite `strata_bench.py`, 3 essais) :
- chat court : **70,4 tok/s** (de 60,5 à 95,7) ; premier mot en 0,39 s ;
- lecture d'un prompt de 4 000 mots : 2 534 tok/s (1,6 s) ; de 16 000 : 3 134 tok/s (5,1 s) ;
- session d'agent à 5 tours, 12 900 tokens de contexte au dernier tour : **78,7 tok/s** (de 59,0 à 88,5), 69 % de cache.
- *Limites dites par l'auteur du rapport* : « vitesse seulement, **aucun contrôle de justesse** » ; processus en arrière-plan non relevés.
→ https://github.com/Niko1221/Strata/issues/4997 (05/11/2026). C'est **une 5070 Ti (672 Go/s), pas une 5080 (960 Go/s)**, mais les deux ont 16 Go et le même processeur que toi.

**S10 [MESURE]** Autre machine à ~32 Go : **AMD Radeon 9600 XT 16 Go, Ryzen 7 5700X, 30,3 Gio de RAM, Linux, Coder** (Strata 0.1.43, 13/10/2026) : **37,6 tok/s** en chat court, 41,7 en session d'agent, lecture de prompt 906-967 tok/s.
→ https://github.com/Niko1221/Strata/issues/2250 (fermée lors de la remise à zéro du suivi, « closed ne veut pas dire rejeté »).

**S11 [MESURE] Les 5080 mesurées ont toutes 64 Go de RAM ou plus.**
- **« baiqvesse », 03/11/2026** : RTX 5080 16 Go, Ryzen 9 9950X, **2 × 32 Go DDR5-6400**, Windows 11, **Flash-Next complet IQ3_S** : moteur 0.1.54 → **114,1 tok/s** (moyenne de deux mesures croisées) ; moteur 0.1.56 → **85,5 tok/s**, soit **-25 %** en décodage et -13,5 % en lecture de prompt. Plus un deuxième bug probable (contexte de lecture de 16 384 qui prend la place des experts dans la VRAM, #5199).
→ https://github.com/Niko1221/Strata/issues/5115
- **Autre rapport, même jour** : « 31 tok/s en 0.1.56, 88 en 0.1.54 » sur RTX 5080 16 Go IQ3_S, 64 Go de RAM, Windows 11 → https://github.com/Niko1221/Strata/issues/5121 (ticket sans détails, signalé incomplet par le robot du projet).

**S12 [MESURE]** « Retarel », 04/11/2026 : **RTX 5080 16 Go** (écran branché dessus), Ryzen 9 9950X3D, **96 Go DDR5**, Windows 11, Strata 0.2.10, Flash-Next *Uncensored* IQ3_XXS (paquet tiers) : décodage anglais **106 / 99 / 97 tok/s** (court / 4K / 16K), lecture de prompt 2 162 tok/s (4K) et 3 899 (16K) ; la zone d'experts en RAM fait **49,8 Gio** (« environ 25 Go de RAM restent libres »). Sans réserve de VRAM, des alertes « moins de 279-531 Mio de VRAM libres » ; `--vram-reserve-mib 1472` les supprime à -0 à -4 %.
→ https://github.com/Niko1221/Strata/issues/5237

**S13 [MESURE]** Sur le même 5080, une autre source : fidélité de trois fichiers 4 bits de Flash-Next (« ShaggyDragon », 05/11/2026, moteur 0.1.56) : IQ3_S de référence 83,6 Go, UD-IQ4_XS 93,7 Go, UD-Q4_K_XL 111,3 Go, mesurée en perplexité, **hors des 32 Go de RAM** (ces fichiers veulent 72 à 88 Go de RAM selon MODELS.md). Rapport sur la précision, pas sur la vitesse.
→ https://github.com/Niko1221/Strata/issues/5291

**S14 [AVIS / MESURE d'un bug]** Plusieurs tickets ouverts le 03/11 (#5043, #5046, #5055, même rapporteur apparent, dont deux en chinois) : sur **RTX 5080 (sm_120), Windows 11, pilote 617.42, 95 Go de RAM, Strata 0.2.9 + moteur 0.1.55**, les fichiers **IQ3_S et IQ3_XXS produisent des « non-finite logits »** (valeurs invalides) quel que soit le moteur essayé ; réponse du projet : pas encore (le robot demande de corriger le titre). **Non confirmé par le développeur**, mais il touche exactement ta carte.
→ https://github.com/Niko1221/Strata/issues/5055 (05/11/2026). Ne pas l'affirmer comme un fait général : « un utilisateur de 5080 rapporte ».

**S15 [DEV]** Ce que le projet dit lui-même des limites (TROUBLESHOOTING.md, 05/11) :
- au premier lancement, Strata « charge 35 à 55 Go dans ta RAM, en verrouille une partie pour la carte graphique » : **la souris peut se figer quelques minutes** (si plus de 10 minutes : redémarrer) ;
- sans réglage de ta part, Strata garde **1 536 Mio de VRAM libres pour le bureau** sur une carte de 16 Go ou moins qui affiche l'écran ;
- sur un PC à ~32 Go de RAM, `--resident-budget-gib` peut le bloquer (#649) et la version 0.1.40 a ralenti le décodage tout en lisant le disque intensément (#1194) ;
- avec 0 Mio de VRAM libre, le décodage tombe de 100 à 14 tok/s sous Windows (#781, #831) ;
- sous 24 Go de VRAM, le lecteur d'images tourne sur le **processeur** (quelques secondes par image).
→ https://github.com/Niko1221/Strata/blob/main/docs/TROUBLESHOOTING.md et MODELS.md (05/11/2026).

**S16 [DEV, ancien]** Vitesses publiées par le projet (« speed history », moteurs anciens 0.1.26-0.1.40) :
- RTX 5070 12 Go, Ryzen 5 7600, 64 Go : Q2_0 94 tok/s, IQ2_XS 79, IQ3_XXS 62, IQ3_S 53, **Coder 55** (chat court) ; à 128K de contexte : 76 / 63 / 49 / 46 / 43.
- **AMD RX 9070 XT 16 Go**, Ryzen 9 3900X, 47 Go, Linux : Q2_0 60, IQ2_XS 52, **Coder 44**.
- Tableau « RTX 5060 Ti 16 GB » du projet : « **Non mesuré**, estimé à ±20 % » (Q2_0 ~80 tok/s, IQ3_XXS ~66).
→ https://github.com/Niko1221/Strata/blob/main/docs/MODELS.md et DETAILS.md (05/11/2026). *Aucun chiffre de RTX 5080 dans la doc officielle* ; ils sont dans les tickets (S11, S12).

**S17 [AVIS]** Hacker News, fil « Run Qwen 3.8 Flash Next (125B) on consumer hardware (RTX 4090) at 100T/s », 04/10/2026, **940 points, 417 commentaires** : https://news.ycombinator.com/item?id=49953495 (via l'API publique de HN, 05/11/2026).
- *Le plus utile pour toi* : « imnotr0b0t : Est-ce que le **Coder à 32 Go** est utilisable pour du vrai code ? » Réponse de **nacs** : « Le Coder n'est pas aussi bon et a **une perte notable**. Utilise le normal : je l'ai utilisé pour de longues sessions de code. »
- **0xbadcafebee** : « Un quant Q1 avec la moitié des experts arrachés… tu ne peux pas compter dessus pour du code long : pas de repas gratuit. » (opinion)
- **roscas** : RTX 3080 10 Go, Ryzen 3600X, 48 Go, **Coder : ~30 tok/s**, thinking réglé sur « low ».
- **bitexploder** : RTX 4080 « autour de **40 tok/s** » avec le « MoE caching build », sans la quantité de RAM ; il estime aussi que le quant IQ3_XXS est « à un point du modèle non quantifié » sur les bancs de code (opinion).
- **theodorton** : RTX 3090 + 64 Go DDR4, « Strata réserve ~28 Go de RAM système ».
- **Jackson__** (mesure) : sur 50 images, l'erreur médiane de localisation est de 154,8 px avec Strata contre 46,5 px avec **les mêmes poids dans llama.cpp**.
- **XCSme** : RTX 3090 + 128 Go ; en réflexion « high » le 27B est meilleur, mais les deux sont trop lents ; en « low », Flash-Next est meilleur et plus rapide.
- Doutes sur la qualité à 2-3 bits : « hallucine plus » (amitp85), « nettement dégradé » (ricardobeat, IQ3_XXS), « bracingly wrong » (spockz).

## C. Autres modèles Qwen sur cartes de 16 Go

**S18 [MESURE] Qwen3.8-27B sur RTX 5080 16 Go.** Dépôt communautaire `sudoingX/qwen38-mtp` : **53,4 tok/s sans MTP → 101,3 avec MTP (n-max 2)**, `Q3_K_M`, contexte 64K, cache KV q4_0, llama.cpp b10488, Windows 11 / CUDA 13.3, 14 445 → 15 359 Mio de VRAM (acceptation 0,53-0,95). *Mise en garde* : le tableau de la page ne donne pas le fichier pour cette ligne ; le rapprochement entre « 53,4 → 101,3 » et « Q3_K_M / b10488 » vient d'une note de bas de page, donc d'une inférence (déjà signalé dans `modeles-5080.md`). Une seule mesure sur 5080.
→ https://github.com/sudoingX/qwen38-mtp (relu 05/11/2026).

**S19 [MESURE]** Même dépôt, autres cartes de 16 Go, Qwen3.8-27B, **baseline → avec MTP** :
- **RTX 5060 Ti 16 Go**, fichier « Q4-XYZ-v2 » (15,06 Go), 32K : 26,3 → 59,5 (n4) ; un autre utilisateur : 50,0 (n2) → 59,3 (n4), 14,5-15,7 Go de VRAM, n-max 6 « OOM au chargement » ;
- **RTX 4060 Ti 16 Go**, même fichier, 32K : **17,6 → 40,0** (n3), 14,8-15,8 Go de VRAM (n4 : OOM) ;
- RX 9060 XT 16 Go (Vulkan/ROCm) : 15,2 → 28,7 ; RTX 3080 Ti laptop 16 Go : 14,8 → 28,6.
→ même page. *Fichier « Q4-XYZ-v2 » : non identifié* (variante communautaire).

**S20 [MESURE]** **Kai**, vidéo « Is 16GB All You Need for Serious Local LLM? » (07/10/2026), description : « 16 Go font tourner Qwen3.8-27B à **45 tok/s sur une RTX 5060 Ti** » ; le fichier ISTA GSQ-RCO fait **11,8 Go** ; le cache KV coûte **64 Ko par token** (128K tokens = 8 Go de plus) ; deux réglages (fichier de vision désactivé, cache 8 bits) font passer la même carte de **~47 000 à ~110 000 tokens de contexte** ; la même carte est rapportée « de 3 à 70 tok/s » selon que le fichier tient ou déborde ; Claude Code dépense ~30 000 tokens avant ta première phrase ; seuil de rentabilité face à du Qwen loué : **~97 jours d'usage non-stop** ; prix du 07/10 (une 5060 Ti à 789 $, +84 % sur le prix de lancement). « Les vitesses sont **auto-déclarées par les propriétaires** ».
→ https://www.youtube.com/watch?v=i9mRnbdDYxk (description lue 05/11/2026 ; **511 821 vues** au 05/11).

**S21 [MESURE]** Qwen3.8-27B **Q4 qui déborde** : Hardware IA (ES, 01/09), RTX 5080 seule, Q4 dans LM Studio : **13 tok/s** (déjà dans `references.md`, vidéo non revérifiée aujourd'hui). Deuxième mesure du même effet, indirecte : un « benchmark communautaire sur une carte AMD de 16 Go » que je n'ai pas retrouvé à sa source. **Source secondaire seulement** : llmrun.dev annoncerait 7,3 tok/s en Q4_K_M qui déborde (https://llmrun.dev/compare/qwen-qwen3-8-27b-vs-qwen-qwen3-8b, non relu en détail). Donc **une seule mesure vérifiée** pour « le Q4 déborde et s'effondre ».

**S22 [MESURE]** Blog **Autodidacts** (23/08/2026), carte « RTX 3080 16 Go » (probablement la version portable, non précisé) : `UD-IQ3_XXS` du 27B, tout en VRAM : **20 à 30 tok/s** ; le `UD-Q4_K_M` « trop lent, peu de place pour le contexte » ; le `UD-Q5_K_M` à 24 couches sur le GPU : **~1,5 tok/s**, une tâche de code a pris « 36 heures, surtout à réfléchir » ; avec un cache KV q4_0 on atteint 128K+. Conclusion : « 16 Go suffisent » mais avec des compromis (quantification forte des poids et du cache).
→ https://www.autodidacts.io/how-to-fit-qwen3-8-27b-into-16gb-vram-run-with-llama-cpp-rtx-3080-flags-quantizations/

**S23 [MESURE, autre version]** dev.to (Rost, « 24 mai », année non indiquée mais Qwen3.6 sorti au printemps 2026), **RTX 4080 16 Go**, RAM non précisée : **Qwen3.6-27B IQ3_XXS** : 45 tok/s standard → **75 avec MTP** (cache q8, contexte moyen 40K) ; **Qwen3.6-35B-A3B IQ3_S** : 146 → 189 tok/s mais contexte moyen 10K « impraticable sur 16 Go ». Attention : **Qwen3.6, pas 3.8**.
→ https://dev.to/rosgluk/qwen-36-27b-and-35b-mtp-vs-standard-on-16gb-gpu-42jd

**S24 [MESURE]** Reddit r/LocalLLaMA (miroir), « RTX 5080 16GB : Qwen3.6 35B MoE à 128k de contexte — 56 tok/s, et pourquoi le MTP n'aide pas » (u/gaztrab, ~mai 2026) : **Ryzen 9 9950X, 128 Go de RAM**, llama.cpp b9204, UD-Q4_K_XL (~22 Go), cache q8_0 : **56 tok/s à 128K, ~73 à 8K** ; le **27B IQ3_XXS + MTP (12,45 Go) : 73 tok/s en moyenne**, 56K de contexte (110K en q4_0), tout dans la VRAM. Les commentaires doutent (« post généré par un LLM », « les chiffres ne sont pas fiables » ; l'auteur renvoie à ses scripts sur GitHub). Qwen3.6, pas 3.8 ; **128 Go de RAM**, pas 32.
→ https://reddit.sentinel-team.org/posts/1tiixql/snapshots/2026-05-21T05%3A05%3A58.868571Z

**S25 [MESURE] La mesure « 16 Go + 32 Go de DDR5 » la plus propre (sans Strata).** Reddit r/LocalLLaMA (miroir), u/marlang, ~avril 2026, 576 points : **RTX 5070 Ti 16 Go + Ryzen 9800X3D + 32 Go DDR5 (-6000 d'après un commentaire)**, llama.cpp b8829, CUDA 13.1, Windows : **Qwen3.6-35B-A3B UD-Q4_K_M (22,1 Go)**, `--n-cpu-moe 20` : **78,7 tok/s** en génération (51,2 avec `--cpu-moe` seul), 12,7 Go de VRAM ; après corrections avec `llama-bench` : **~98 tok/s en tg128**, contexte 128K. Un commentateur sur Linux : ~76 tok/s ; un autre sur 265K + 64 Go DDR5-4800 : ~70 avec Q3_K_M. Les chiffres de prompt de l'auteur ont été corrigés ensuite. **Qwen3.6 (pas 3.8)**.
→ https://reddit.sentinel-team.org/posts/1sor55y/snapshots/2026-04-25T00%3A46%3A56.728262Z

**S26 [AVIS]** HN, ohyes : « j'utilise des quants de **Qwen3.8 en Q3 efficacement sur une 5070 Ti** ; beaucoup dépend des garde-fous » ; latentsea : « je fais mon travail avec un **IQ3_S du 27B sur une 5060 Ti** » ; Moon_Y : « installé en moins de 20 minutes, RTX 5070, vitesse impressionnante ». → fil HN (S17). Un utilisateur de RTX 3080 + 16 Go de RAM (4ggr0) se plaint de ne pas être satisfait ; réponse de jonatron : « avec ce matériel, je ne perdrais pas mon temps ».

**S27 [DEV, non vérifié]** Pistes « 16 Go + 32 Go » trouvées mais non confirmées : un fil Hugging Face (résumé d'un moteur de recherche) prétendrait que « UD-Q4_K_XL tourne sur 16 Go de VRAM et 32 Go de RAM à plus de 15 tok/s » ; la page que j'ai ouverte (`TakiTakiTa/Qwen3.8-Flash-Low-RAM`) **ne dit pas ça** : elle vise une RTX 3050 de 4 Go et annonce 5 à 10 tok/s avec 32 Go de RAM, « expérimental ». → https://huggingface.co/TakiTakiTa/Qwen3.8-Flash-Low-RAM. UD-Q4_K_XL fait 111 Go (Unsloth) : sur 16 + 32 Go, ce serait du SSD. **Ne pas citer.**

**S28 [DEV, secondaire]** Guide launchboosts.com (05/10/2026) : sur 32 Go de RAM, « le Coder est la seule version recommandée », 1,89 bit par poids ; **50,6 tok/s à 4K, 44,0 à 128K de contexte** : *non mesuré par l'auteur du guide*, ces chiffres viennent de VRAM Calculator qui cite la doc de Strata, sur une **RTX 5070 12 Go avec 64 Go de RAM**. À ne pas présenter comme une mesure à 32 Go. → https://launchboosts.com/blog/run-qwen-3-8-flash-next-locally-strata

## D. Qualité face à Claude / ChatGPT

**S29 [DEV, hors quantification]** Fiche Qwen3.8-27B (août 2026) : Terminal-Bench 2.1 **73,0** (Opus 4.6 Max : 78,2) ; SWE-bench Pro **61,7** (53,4) ; GPQA Diamond 89,2 (91,3) ; HLE 30,8 (40,0) ; LiveCodeBench v6 **90,3** (88,8) ; IFBench 79,5 (62,5). Aucun modèle GPT dans la table. Seul Claude comparé : **Opus 4.6 (Max)**, pas la version actuelle.
→ https://huggingface.co/Qwen/Qwen3.8-27B (05/11/2026). Ce sont des mesures du modèle complet (BF16), pas du fichier de 12 Go, avec des harnais maison (Claude Code pour certains).

**S30 [DEV, hors quantification]** Fiche Flash-Next : SWE-bench Pro **62,5** (Opus 4.6 Max : 53,4) ; DeepSWE 58,7 ; GPQA 91,7 (91,3) ; HLE 35,9 (40,0) ; LiveCodeBench v6 91,9 (88,8). Même remarque.
→ https://huggingface.co/Qwen/Qwen3.8-Flash-Next (05/11/2026).

**S31 [MESURE indépendante, **chiffres contradictoires**]** Artificial Analysis :
- Version actuelle de l'indice (**v5.0.1**), Qwen3.8-27B (xhigh) contre **Claude Opus 5 (High)** : **Terminal-Bench 4.0 : 6 % contre 46 %** ; AutomationBench-AA 48 % contre 54 % ; AA-Briefcase 1 391 contre 1 557 ; vitesse de l'API 46 contre 76 tok/s ; prix de sortie 3 $ contre 25 $ le million de tokens. Indice d'intelligence du Qwen : **20** (la valeur d'Opus 5 n'apparaît pas dans ma lecture).
→ https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-claude-opus-5-high (05/11/2026).
- **Contradiction** : en août, des articles (Qubrid, LetsDataScience, 20/08/2026) citent un indice de **52** (xhigh), 44 (medium), 35 (sans réflexion), à rapprocher de GPT-5.6 Luna ; l'indice a changé de version depuis. **Ne pas mélanger 52 et 20.** Ces mesures sont celles de l'API, pas d'un fichier 3 bits sur 16 Go. Qubrid (qui vend le modèle) dit aussi que sur l'indice « agentique » le Qwen est devant Opus 4.8 d'un demi-point, c'est-à-dire à égalité.
→ https://www.qubrid.com/blog/qwen38-27b-benchmarks-official-and-independent-results (05/11/2026).

**S32 [MESURE]** Quantification du 27B, **Quesma** (26/08/2026), sur GPU de location (L40S, H100, H200), fichiers Unsloth : **Q4_K_M (17 Go) sans différence notable** avec le BF16 sur GPQA, IFBench et Terminal-Bench 2.1 ; **UD-Q2_K_XL (10,7 Go)** : baisse nette sur Terminal-Bench (« niveau Opus 4.7 / Gemini 3.1 Pro » selon eux) et ~25 % de tokens de sortie en plus ; **1 bit : effondrement**. Pas de tok/s. *Aucun fichier ISTA dans ce test.*
→ https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/

**S33 [DEV]** ISTA-DASLab (déjà dans `modeles-5080.md`) : leur `IQ3_XXS` du 27B perd peu (LiveCodeBench v6 à 84,6 contre 85,7 en BF16, mesure d'ISTA). Kai répète que le GSQ-RCO « ties the full model on AIME, coding and GPQA » (S20) : chiffre d'ISTA, pas indépendant. Les vrais comparatifs indépendants GSQ-RCO contre Unsloth : *non trouvé*.

**S34 [MESURE d'un tiers]** MindStudio (06/09/2026), sur **4 × RTX 3090** : Qwen3.8-27B en **FP16** a terminé une session de code de deux jours que **Flash-Next en INT4** n'a pas terminée ; Flash-Next préféré pour la conversation créative. C'est une anecdote, sur du matériel sans rapport avec 16 Go. → https://www.mindstudio.ai/blog/qwen-3-8-27b-vs-flash-next-local-agents

## E. Vidéos (EN) récentes sur le sujet, vues au 05/11/2026

**S35 [vidéos]**
| Vidéo | Chaîne | Vues | Date | Angle |
|---|---|---|---|---|
| [A 125B Local Model on a 16GB GPU: Fast, But Is It Smart?](https://www.youtube.com/watch?v=B77LasklmZU) | Zero to MVP | 72 993 | 05/10 | **Strata sur RTX 4060 Ti 16 Go**, Ryzen 7, **128 Go de RAM** (donc pas ta config), 3 tâches de code avec l'agent Pi (horloge, éditeur de pixels, pyramide 3D) ; chapitre « générer la vitesse » à 2:17, conclusion à 6:41. Chiffres non lus (pas de transcription). |
| [Qwen 3.8 27B vs Strata Coder - Local LLM battle](https://www.youtube.com/watch?v=xiMAxAQAfC4) | Luke's Dev Lab | 85 103 | 23/10 | **Le plus proche de ta machine** : « les deux tournent à vitesse raisonnable sur un GPU de **16 Go avec 32 Go de RAM** » ; Qwen 3.8 27B en Q3 contre le Coder, 6 tests (performance, plan de salle, vagues, Prism Relay, diorama, éolienne Blender). Les chiffres « 40 contre 17 tok/s, carte bridée à 70 W » viennent de `modeles-5080.md`, **non revérifiés aujourd'hui**. |
| [125B AI on a Gaming PC? Strata Tested on RTX 5090 Desktop & Laptop](https://www.youtube.com/watch?v=PJmC9w47_sg) | Stef from Samayas | 13 317 | 06/10 | Installation sous Windows puis **Claude Code branché sur Strata** (projet C#/.NET) : d'après la description, **le Coder a échoué à la tâche** ; le Q2 standard a mis ~**56 min** ; Swift 1.5 ~5 min (pas la structure demandée) ; **IQ3_S : 4 min 05**, application qui marche. Précise : « mes tests, pas un benchmark universel ». RTX 5090, pas 16 Go. |
| [Is 16GB All You Need for Serious Local LLM?](https://www.youtube.com/watch?v=i9mRnbdDYxk) | Kai | 511 821 | 07/10 | Le calcul de la mémoire en tokens (S20) ; **pas de Strata**. Le plus gros sur « 16 Go ». |
| [Qwen 3.8 Flash Next Tested - 16GB Local LLM setup](https://www.youtube.com/watch?v=s4cTVRH2ReA) | Luke's Dev Lab | 163 557 | 14/09 | Flash-Next (« 177B A6B ») sur 16 Go, 9 épreuves (même grille que le 27B). Avant Strata (llama.cpp / Unsloth). |
| [Strata GitHub Explained…](https://www.youtube.com/watch?v=hJ_Iw2E7cnc) | Alex Hitt | 4 326 | 01/10 | Explication du routage des experts, « 95 tokens par seconde », goulots Windows (tâche planifiée de 14 minutes), compromis multilingue. Petite chaîne. |
*Vidéo française sur Strata ou sur Flash-Next : **non trouvée*** (recherche large, aucune).

## F. Contradictions à ne pas oublier

1. **« 75 Go » ou « 32 Go » pour Flash-Next chez Unsloth** : la page dit à la fois « fonctionne avec 32 Go de RAM » (tableau, 1 bit) et « il te faut au moins 75 Go » (texte) ; le plus petit fichier fait 72,5 Go. → https://unsloth.ai/docs/models/qwen3.8-next . À retenir : 75 Go sans Strata, 32 Go **seulement avec le Coder et Strata**.
2. **Qualité du Coder : 91 % (README/MODELS) ou 95,7 % (fiche du 17/10)** : S7.
3. **Taille de Flash-Next : 125, 177 ou 180 milliards** : S4.
4. **Indice d'Artificial Analysis : 52 ou 20** (versions différentes de l'indice) : S31.
5. **Vitesse du même modèle sur « 16 Go » : de 3 à 100 tok/s** (Kai le dit lui-même) : tout dépend du fichier qui tient ou déborde, du contexte, du MTP et de la RAM. Les deux mesures sur une 5080 (13 tok/s Hardware IA, 101 tok/s sudoingX) n'ont pas les mêmes réglages.
6. **RTX 5080 Strata : 114 / 85 / 88 / 31 tok/s** selon la version du moteur (S11) : la vitesse bouge d'une mise à jour à l'autre.

## G. Pour le script : formulations qui tiennent (sans « j'ai testé »)

- « Sur une carte de 16 Go, un utilisateur de **RTX 5070 Ti avec le même processeur que moi et 32 Go de RAM** mesure **70 tok/s** avec le Coder de Strata, le 2 novembre. Une seule mesure, et sans test de qualité. » (S9)
- « Le Flash-Next complet, celui qui est vraiment performant, **veut 64 Go de RAM** : sur 32 Go, il faut la version réduite pour le code, et ceux qui l'ont utilisée disent qu'elle perd en qualité. » (S3, S17, S35)
- « Pour 32 Go, la mesure la plus solide n'est pas Strata : c'est **Qwen3.6-35B-A3B en llama.cpp, ~80 à 98 tok/s sur une 5070 Ti avec 32 Go de DDR5** (avril, version 3.6). » (S25)
- « Sur une 5080, le 27B en Q3 avec MTP : **53 → 101 tok/s** d'après un dépôt communautaire, une seule mesure. » (S18) ; « le Q4 qui déborde tombe à **13** » (S21).
- « Sur les tests indépendants d'Artificial Analysis, le 27B est loin d'Opus 5 en agent de terminal (6 % contre 46 %). » (S31) ; « sur les tableaux de Qwen, il bat Opus 4.6 en code, mais c'est Qwen qui compare, et avec l'ancien Opus. » (S29)
- Strata est **jeune** (créé le 24/09, version 0.2.10 le 2/11, 1 349 tickets ouverts) et **la vitesse sur 5080 a bougé de -25 % entre deux versions** (S1, S11).

## H. Non trouvé

- Mesure de **Strata sur RTX 5080 avec 32 Go de RAM** (ni Coder ni autre).
- Mesure de Strata sur **RTX 4080 / 4060 Ti 16 Go avec 32 Go** : la vidéo de Zero to MVP (4060 Ti) a 128 Go de RAM et je n'ai pas pu lire ses chiffres.
- Test de **qualité** indépendant du Coder à 1,89 bit en usage réel (le seul : S35 Samayas, échec, sur RTX 5090).
- Comparaison indépendante **GSQ-RCO contre Unsloth** sur le 27B.
- Posts Reddit lus directement : accès refusé ; X/Twitter : rien de retrouvable.
- Vidéo **française** sur Strata ou Flash-Next.
- Les tok/s de la vidéo de Luke's Dev Lab « 27B vs Strata Coder » (transcription bloquée) : on garde les chiffres de `modeles-5080.md`, à revérifier à l'œil avant la voix.
