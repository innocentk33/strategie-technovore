# Sources : « Je teste le meilleur modèle possible avec Strata sur ma 5080 »

> Faits numérotés **T1, T2…**, relus ou relevés le **11/11/2026** sauf mention. Ils reprennent et revérifient les faits S de [`../claude-ou-mon-pc-1/sources.md`](../claude-ou-mon-pc-1/sources.md) (le numéro d'origine est donné). **Les résultats de tes tests n'y sont pas** : ils n'existent pas encore, ils seront dans la fiche de [`plan-tests.md`](plan-tests.md) et remplacent les `⟦…⟧` du [script](script.md).
>
> **Types** : `MESURE` (chiffre publié par un utilisateur ou un tiers, avec sa machine) · `DEV` (affirmation du projet ou de l'auteur du modèle, pas indépendante) · `AVIS` (témoignage ou opinion) · `CALCUL` (déduction de ma part, pas une source).
> **Statut** : ✅ relu le 11/11 · ⚠️ nuancé (dit comment) · ⏳ repris du 05/11, **non revérifié le 11/11**. La relecture du grill (section G) liste ce qui a été revérifié, corrigé ou ajouté (T31 à T38). **Pas rouverts le 11/11** : les chiffres vidéo de T4 (utilisés dans le plan B 9.2 et 9.7), T16, T19, T20, T21, T22, T26, T28, T29 ; aucun n'est dit dans la voix.
> **Règle de la voix** : aucun nom de chaîne ni de créateur ; « un utilisateur », « un testeur », « une chaîne américaine ». Les noms sont ici, pas dans le script.

## A. Strata, la version, l'installation

**T1 ✅ [DEV]** Version **0.2.13**, publiée le **09/11/2026** (12:46 UTC) : « L'appli et le Terminal sont en 0.2.13, Control et tous les paquets de moteur en 0.1.59 ». Mais pour **Windows et Mac**, une note dit que « `strata update` met le moteur en 0.1.59 et laisse le Terminal en 0.2.12 : le Terminal avance à la prochaine version ». Versions précédentes : 0.2.12 (07/11), 0.2.11 (05/11), 0.2.10 (02/11, celle de `claude-ou-mon-pc-1`), 0.2.9 (31/10) : **une version tous les 2 à 3 jours**, donc la « dernière » du 11/11 ne sera pas celle du 16/11. Dépôt : **43 155 étoiles**, **1 328** tickets ouverts (dépôt créé le 24/09/2026).
→ https://github.com/Niko1221/Strata/releases/tag/v0.2.13 ; API https://api.github.com/repos/Niko1221/Strata (11/11/2026). *Reprend S1 (40,3 k étoiles le 05/11).*

**T2 ✅ [DEV]** Windows 10/11 ou Linux x86-64 avec une RTX NVIDIA : « le moteur de ta carte est téléchargé pour toi ». **Les paquets CUDA 13 demandent le pilote NVIDIA 580 ou plus** ; les cartes plus anciennes utilisent CUDA 12. Installation du Terminal : `irm -TimeoutSec 120 https://github.com/Niko1221/Strata/releases/latest/download/install.ps1 | iex` (sans droits d'administrateur) ; `strata launch` guide ensuite.
→ https://github.com/Niko1221/Strata/blob/main/docs/INSTALL.md

**T3 ✅ [DEV, MESURE du projet]** Problème connu de la 0.2.13 : « le premier lancement d'une installation neuve peut prendre **environ 5,5 minutes** à l'étape “Preparing your model” » ; sur un PC avec une RTX 5070, **398 à 406 s** ; sur un Strix Halo, **337 à 411 s** ; la même installation avait pris 398 et 595 s en 0.2.12 le même jour et 107 à 118 s le 07/11 : « nous n'avons pas trouvé la cause ».
→ notes de la 0.2.13 (T1).

**T4 ✅ [MESURE] Le Coder sur 32 Go de RAM, une carte de 12 Go.** NoCodeAbode, *How Good Is Strata's Qwen Coder on 32GB RAM?*, **02/10/2026** (40 536 vues au 11/11) : téléchargement de **58 Go**, **87 Go** occupés sur le disque ; « le mode rapide ne tient pas » (demande 19 Go + 4 de marge, il en restait moins de 14 avec tout fermé) donc **mode lent, lecture sur le SSD** : **8,7 tok/s** en chat, **41 à 46 tok/s sur du code** (contre 55 à 59 sur la machine de 64 Go du projet) ; la RAM libre tombe de 19 Go à **49 Mo** pendant la génération ; un prompt de 20 000 tokens lu en **32 s** (≈ 3 fois plus lent que sur 64 Go) ; **6 tâches de code, 5 réussies, 1 partielle, 0 ratée**, contre 3 / 1 / 2 pour le 27B, **une seule exécution par tâche, réflexion coupée**. Prêt « en une demi-minute » au lancement, sans gel.
→ https://www.youtube.com/watch?v=xze2CeR2Zu0 (sous-titres automatiques en anglais, 11/11). ⚠️ Carte de **12 Go** (la tienne a 16 Go : plus d'experts sur la carte, donc plus de chances d'être en mode rapide) ; chiffres des sous-titres automatiques, à revérifier à l'image avant de les citer.

## B. Le Coder et la RAM

**T5 ✅ [DEV]** Texte exact de la doc : « **Big graphics card, little RAM.** […] A 32 GB PC with a 24 GB GPU runs Q2_0, IQ2_XS and the Coder this way, and **a 32 GB PC with a 12 to 16 GB GPU runs the Coder**. With a small card most experts come from the SSD and it is much slower ; setup says so. » **« `strata launch` has no `--low-ram` flag »** : le mode est choisi par l'installation. Le Coder « is weaker outside code and in languages other than English » (CJK compris). Les images tournent sur le **processeur** sous 24 Go de VRAM ; Strata garde **1 536 Mio** de VRAM libres pour le bureau sur une carte de 16 Go ou moins qui affiche l'écran, **512 Mio** si l'écran est branché ailleurs (DETAILS.md, relu).
→ https://github.com/Niko1221/Strata/blob/main/docs/MODELS.md#coder ; …/TERMINAL_LAUNCH.md. *Reprend S3, S5, S15.*

**T6 ✅ [DEV]** Fiche Hugging Face du Coder (ISTA-DASLab) : **256 experts gardés sur 512** par couche, choisis sur du code, de l'agentique et de l'image ; **un seul quant, IQ1_M** (≈ 3,5 bits par poids selon la fiche pour l'ensemble, 1,89 bit d'après d'autres sources, S6) ; deux fichiers de **29,61 Go** et **28,8 Go** (la table, restée sur le SSD) ; image : 0,91 Go. **« This is an experimental release »**. Mise à jour du **17/10/2026** : SWE-bench Verified **79,2** (base 82,8, soit **95,7 %**), LiveCodeBench v6 **87,43** (= la base). « Degradation outside this set is an accepted cost of the method. » La fiche n'a pas changé depuis le **19/10** (dernière modification du dépôt). *MODELS.md de Strata affiche encore 91 % et 99 % (anciens chiffres).* À citer : **« 95 % du score de code du modèle complet, d'après ses auteurs »**.
→ https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF (API et README, 11/11). *Reprend S6, S7.*

**T15 ✅ [DEV, CALCUL]** Règle de Strata : « le modèle tient quand la **RAM est au moins égale aux experts plus environ 10 Go** » (DETAILS.md compte parfois « ~6 Go ») ; experts du Coder : **23 Go** (**29,6 Go** pour le premier fichier chargé). Ta RAM : 32 Go de DDR5 ≈ 34,4 Go décimaux ; Windows en laisse voir environ 33,5 Go (relevé sur une machine de 31,2 Gio). **Donc 33,5 − 23 = 10,5 Go de marge : à ras.** Le mode « RAM réduite » existe pour ça (T5, T8).
→ MODELS.md « Will it fit? », DETAILS.md. *Reprend S2, S8.*

**T8 ✅ [DEV]** Deux modes quand la RAM ne peut pas tenir les experts : **résident** (`--resident-experts` : les experts que la carte ne garde pas sont copiés en RAM au démarrage, « rien n'est lu sur le SSD pendant les réponses ») ou **mappé** (`--mmap-experts` : le cache de fichiers de Windows garde ce que la carte ne garde pas, beaucoup plus lent). L'écran Advanced de `strata launch` affiche la commande exacte.
→ https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md#low-ram-modes-chosen-by-setup

**T9 ✅ [DEV]** TROUBLESHOOTING.md : au premier lancement, Strata « charge 35 à 55 Go dans ta RAM » et **la souris peut se figer quelques minutes** (si plus de 10 minutes : redémarrer) ; sur un PC d'environ 32 Go, `--resident-budget-gib N` peut bloquer le PC (#649) ; avec 0 Mio de VRAM libre, le décodage tombe de **100 à 14 tok/s** sous Windows (#781, #831) ; certains exécutables ne sont pas signés (Smart App Control, #735).
→ https://github.com/Niko1221/Strata/blob/main/docs/TROUBLESHOOTING.md. *Reprend S15.*

## C. Les réglages, le harnais, les limites de réponse

**T10 ⚠️ [DEV]** La réflexion du modèle : par défaut, niveau **« high »** (le gabarit de Flash-Next met `xhigh`, `high` en est l'alias) ; réglable **par requête** (`reasoning_effort`, ou `"chat_template_kwargs": {"enable_thinking": false}`) ou dans la **configuration du modèle** (`reasoning_effort`, `reasoning_budget_tokens` ; la doc dit qu'un `--reasoning-effort` dans les arguments du moteur y est déplacé). **Les « Chat settings » de la page web de Strata ne règlent que la page** : « Chats, settings and the API key stay in the browser » (DETAILS.md, section de la page web, relue le 11/11). `reasoning_loop_recovery` : désactivé par défaut, « peut confondre du code répété avec une boucle ».
→ https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md#thinking-levels-none-low-medium-high ; AI_SETUP.md. ⚠️ **Pas vérifié** : que `strata launch --set reasoning-effort=medium` soit accepté, et qu'OpenCode permette de choisir un niveau. **Corrigé à la relecture du 11/11** : la même doc dit deux fois que « the web page's shared Chat settings win » sur la config (`reasoning_effort` et l'échantillonnage) ; AI_SETUP.md le répète. Affirmer que la page web « ne sert pas ici » n'est donc pas tenu. Le plan V2 ne règle plus la réflexion.

**T13 ✅ [DEV]** `strata connect` : la longueur maximale d'une réponse est **max(4 096, contexte ÷ 8)**, donc **8 192 tokens à 64K**, **12 288 à 96K**, **16 384 à 128K** ; la réflexion compte dans cette limite ; un fichier écrit en un seul appel d'outil « a été coupé de la même façon » (PR #4230) ; et le serveur termine la réflexion quand il ne reste qu'un quart de la limite (`answer_room`, DETAILS.md).
→ https://github.com/Niko1221/Strata/blob/main/strata_cli/launch/harness.py ; DETAILS.md « Config keys ». *CALCUL pour 8 192 : 65 536 ÷ 8.*

**T14 ✅ [DEV]** `strata connect` gère OpenCode, Codex CLI, Claude Code, oh-my-pi, pi, Hermes Agent, OpenClaw. OpenCode : `strata connect opencode --write` fusionne dans `~/.config/opencode/opencode.json` ; son prompt système et ses outils pèsent **≈ 7,4 K tokens** ; « son premier lancement télécharge un plug-in depuis npm » ; testé avec OpenCode 1.19.3. Claude Code : `--write` fusionne dans **`~/.claude/settings.json`** (`ANTHROPIC_BASE_URL`, nom du modèle…) ; son prompt complet pèse **15,6 K tokens** (20 outils) ; testé avec Claude Code 2.1.302 ; il faut `CLAUDE_CODE_MAX_CONTEXT_TOKENS`.
→ harness.py (T13) ; https://github.com/Niko1221/Strata/blob/main/docs/TERMINAL_LAUNCH.md#connect-your-apps-strata-connect

**T21 ✅ [DEV]** « Kv-streaming » : la mémoire de conversation passe en RAM, **≈ 13,7 Ko de RAM par token de contexte (1,7 Go à 128K)** ; l'installation l'active à partir de 64K quand la RAM le permet.
→ DETAILS.md, tableau des options de mémoire. *CALCUL : 128K → 1,7 Go ; 64K → environ 0,9 Go.*

**T22 ✅ [DEV]** La reprise des appels d'outil mal formés (`tool_call_recovery`) est active par défaut depuis la 0.2.8 ; sur 1 462 tours d'agent, 98,3 % sont lus comme prévu avec, 92,9 % sans (mesure du projet). La 0.2.12 a corrigé plusieurs cas d'appels d'outil (#5409, #5276, #5281, #4622).
→ DETAILS.md « Config keys » ; notes de la 0.2.12.

## D. Mesures publiées sur des machines proches

**T7 ✅ [MESURE] La plus proche de la tienne.** « guilleortas », ticket **#4997**, **02/11/2026** : **RTX 5070 Ti 16 Gio, Ryzen 7 9700X, 31,2 Gio de RAM**, SSD 990 PRO, Windows 11, pilote 621.01, Strata 0.1.55 (moteur 0.1.54), **Coder IQ1_M**, contexte 65 536, **`--resident-experts`**, **réflexion coupée et température 0**. Médianes de 3 essais : chat court **70,4 tok/s** (60,5 à 95,7), premier mot en 0,39 s ; lecture d'un prompt de 4 000 mots : 2 534 tok/s ; de 16 000 : 3 134 ; session d'agent à 5 tours : **78,7 tok/s** (59,0 à 88,5), 69 % de cache. L'auteur : « vitesse seulement, **aucun contrôle de justesse** » ; processus en arrière-plan non relevés. **Une 5070 Ti (672 Go/s), pas une 5080 (960 Go/s)**.
→ https://github.com/Niko1221/Strata/issues/4997 (relu 11/11 ; ticket fermé le 05/11). *Reprend S9.*

**T19 ⏳ [MESURE]** Luke's Dev Lab, *Qwen 3.8 27B vs Strata Coder*, 23/10/2026, 88 460 vues : « les deux tournent à vitesse raisonnable sur un GPU de 16 Go avec 32 Go de RAM » ; le Coder à ≈ **40 tok/s** contre ≈ 17 pour le 27B Q3 (carte bridée à 70 W) ; le 27B est plus soigné et plus autonome (`modeles-5080.md`). **Chiffres non relus dans la vidéo** (sous-titres bloqués le 05/11 ; je n'ai pas retenté celle-ci).
→ https://www.youtube.com/watch?v=xiMAxAQAfC4

**T20 ⏳ [MESURE]** « baiqvesse », 03/11/2026 : RTX 5080 16 Go, Ryzen 9 9950X, 2 × 32 Go DDR5-6400, Windows 11, **Flash-Next complet IQ3_S** : moteur 0.1.54 → **114,1 tok/s** ; moteur 0.1.56 → **85,5 tok/s** (**−25 %**). C'est **une autre machine (64 Go) et un autre fichier**. Une autre issue rapporte « 31 tok/s en 0.1.56, 88 en 0.1.54 » (RTX 5080, 64 Go). Le moteur est maintenant en 0.1.59 : on ne sait pas si c'est corrigé.
→ https://github.com/Niko1221/Strata/issues/5115 ; …/5121. *Reprend S11.*

**T16 ⏳ [MESURE]** Hardware IA (ES), 01/09/2026 : **RTX 5080** seule, Qwen3.8-27B en Q4 qui déborde dans LM Studio : **13 tok/s** ; le même modèle en Q3_K_M avec MTP sur une 5080 : 53,4 → 101,3 tok/s (dépôt communautaire, une mesure, S18). *Autre modèle, autre moteur : pas de comparaison directe.*
→ S18, S21 de `claude-ou-mon-pc-1`.

**T29 ✅ [MESURE]** Zero to MVP, *A 125B Local Model on a 16GB GPU: Fast, But Is It Smart?* (05/10/2026, 74 500 vues) : RTX 4060 Ti 16 Go, **128 Go de RAM**, agent Pi, vitesse ≈ **65 tok/s** (script maison) ; horloge réussie, éditeur de pixels réussi en **5 min 20**, pyramide 3D en caractères ratée. → https://www.youtube.com/watch?v=B77LasklmZU (sous-titres, 11/11). ⚠️ Pas ta RAM.

## E. Ce qui casse (rapports d'autres utilisateurs)

**T23 ✅ [MESURE d'un bug, non résolu] (corrigé le 11/11, voir la fin)** Ticket **#5104** (ouvert, mis à jour le 11/11) : avec le **Coder IQ1_M**, une lecture de prompt de **≈ 3 400 tokens** fait planter le moteur (« the expert source could not copy experts 260.. of layer 24 », code de sortie **−6**), avec un message qui parle à tort de manque de RAM. Contournement du rapporteur : `--set STRATA_PREFILL_LAYER_MAJOR=0` (la lecture devient lente sur sa carte de 8 Go : 4,8 à 11,2 tok/s). Un correctif candidat existe (branche d'un contributeur, testé par un autre sur RTX 3060 12 Go) mais **n'est pas dans la 0.2.13**. Sur une carte de 12 Go avec les réglages par défaut, un autre testeur a vu que ça ne plantait pas, car « la marche couche par couche ne démarre pas ».
→ https://github.com/Niko1221/Strata/issues/5104 (relu 11/11).

**T11 ✅ [AVIS / MESURE d'un bug]** Tickets **#5043, #5046, #5055** (03/11) : sur **RTX 5080 (sm_120), Windows 11, pilote 617.42, 95 Go de RAM, Strata 0.2.9 + moteur 0.1.55**, les fichiers **IQ3_S et IQ3_XXS** (pas le Coder) donnent des **« non-finite logits »** « quel que soit le moteur » essayé. #5046 : **fermé le 08/11 par le robot du projet pour mise en forme**, pas pour correction. Le ticket général #879 (dégénérescence « un seul mot répété ») est fermé depuis le 13/10 ; un commentaire du 09/11 sur Mac dit que la protection du moteur existe pour CUDA et HIP (corrigée pour Metal par la PR #3287). **Non confirmé par le développeur.** À dire : « **un utilisateur de 5080 rapporte** ».
→ https://github.com/Niko1221/Strata/issues/5046 ; …/879 (relus 11/11). *Reprend S14.*

**T27 ✅ [AVIS / MESURE] (description revérifiée le 11/11)** Stef de Samayas, *Strata Tested on RTX 5090 Desktop & Laptop* (06/10/2026, 13 317 vues le 05/11) : Claude Code branché sur Strata, un projet C#/.NET ; d'après la **description**, **le Coder a échoué à la tâche** ; le Q2 standard a mis environ 56 min ; IQ3_S 4 min 05, application qui marche. « Mes tests, pas un benchmark universel. » RTX 5090.
→ https://www.youtube.com/watch?v=PJmC9w47_sg (description relue le 11/11 avec yt-dlp, 13 623 vues : « The Coder variant failed to complete the task successfully » ; Swift 1.5 environ 5 min, appli qui marche ; IQ3_S 4 min 05, appli qui marche ; IQ2_XS sur portable 6 min 26). *Reprend S35.*

**T28 ⏳ [AVIS]** Hacker News, fil du 04/10/2026 (940 points) : « imnotr0b0t : Est-ce que le Coder à 32 Go est utilisable pour du vrai code ? » Réponse de nacs : « Le Coder n'est pas aussi bon et a **une perte notable**. Utilise le normal. » Autre avis : « un quant Q1 avec la moitié des experts arrachés… tu ne peux pas compter dessus pour du code long ».
→ https://news.ycombinator.com/item?id=49953495 (non rouvert le 11/11). *Reprend S17.*

## F. Le contexte (modèle, projet)

**T24 ✅ [DEV]** Strata : moteur d'inférence **gratuit et open source (licence MIT)**, pour Windows, Linux et Mac, avec une appli de bureau et un terminal (`strata launch`) ; il sert des API compatibles OpenAI et Anthropic en local, utilisables avec Claude Code, Codex CLI et OpenCode. Dépôt créé le 24/09/2026.
→ https://github.com/Niko1221/Strata (T1). *Reprend S1.*

**T25 ✅ [DEV]** Comment Strata fait tenir un gros modèle : le GPU garde les experts les plus utilisés, **la RAM garde le reste des experts**, **une table de 29 Go reste sur le SSD**. Flash-Next : **125 milliards de paramètres dont 6 milliards actifs par mot** (180 milliards avec la table de mots).
→ MODELS.md ; https://huggingface.co/Qwen/Qwen3.8-Flash-Next. *Reprend S2, S4. « Dis 125 milliards (180 avec la table de mots). »*

**T26 ⏳ [DEV / MESURE]** Qwen, sur ses propres tableaux, compare ses modèles à **Opus 4.6** (pas la version actuelle) ; Artificial Analysis (indice v5.0.1) donne **Terminal-Bench 4.0 à 6 % pour Qwen3.8-27B contre 46 % pour Claude Opus 5 (High)** (S31). Ce sont des mesures du modèle complet ou de l'API, **pas d'un fichier de 1,89 bit**. **Ne pas mélanger** avec l'ancien indice (52 contre 20).
→ https://huggingface.co/Qwen/Qwen3.8-Flash-Next ; https://artificialanalysis.ai/models/comparisons/qwen3-8-27b-vs-claude-opus-5-high. Non revérifié le 11/11. *Reprend S29 à S31.*

**T30 ✅ [DEV, ancien]** Vitesses d'écriture du **Coder** publiées par le projet (« Speed (measured) », moteur **0.1.26**, RTX 5070 12 Go, Ryzen 5 7600, **64 Go de DDR5-5200**, Windows, 256 tokens générés, MTP activé) : **58,9 tok/s à 1K de contexte**, 55,1 à 4K, 54,9 à 32K, 53,2 à 64K, **43,0 à 128K**, 42,8 à 262K ; lecture du prompt 656 à 2 236 tok/s. Moteur ancien : sert à montrer que **la vitesse baisse avec le contexte**, pas à prédire la tienne.
→ https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md#speed-measured (relu 11/11).

**T17 ✅ [CALCUL]** L'adresse `https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js` répond « 200 » (vérifiée le 11/11) ; C'est la version que le prompt impose, pour que le modèle n'invente pas une adresse. → vérification `curl -I`.

## G. Relecture du 11/11 (grill V1) : revérifié, corrigé, ajouté

Relu le 11/11/2026 dans les fichiers du dépôt (`raw.githubusercontent.com`, branche `main`), l'API GitHub (release v0.2.13, tickets #4997, #5046, #5104 et leurs commentaires), l'API et le README Hugging Face, la doc de Pi.

**Revérifié, sans changement** : T1 (0.2.13 publiée le 09/11 à 12:46 UTC ; 0.2.8 le 29/10, 0.2.9 le 31/10, 0.2.10 le 02/11, 0.2.11 le 05/11, 0.2.12 le 07/11 ; dépôt créé le 24/09 ; **43 159 étoiles**, 1 328 tickets ouverts ; licence MIT) · T2 (pilote 580 pour CUDA 13 ; ligne `install.ps1`) · T3 (≈ 5,5 min, 398 à 406 s) · T5 (« a 32 GB PC with a 12 to 16 GB GPU runs the Coder » ; « `strata launch` has no `--low-ram` flag » ; 1 536 / 512 Mio) · T6 (fichiers de 29 608 446 496 et 28 800 138 432 octets ; SWE-bench 79,20 contre 82,80, 95,7 % ; « This is an experimental release » ; dernière modification du dépôt le 19/10) · T7 (#4997 : 70,4 tok/s, « thinking off for the suite; temperature 0 », « Speed only: no correctness check was run », `--resident-experts`) · T8 · T13 (`output_cap = max(4096, context // 8)`) · T14 · T15 (« RAM is at least the experts plus about 10 GB » ; Coder 23 Go) · T17 (`curl -I` : HTTP 200 le 11/11 à 17:23 UTC) · T25 (fiche Qwen : « 125B with 6B activated, plus 51B n-gram embedding and 4B MTP ») · T30 (tableau « Output (tokens/s) » : Coder 58,9 → 43,0).

**Corrigé** :
- **T9** : la chute « de 100 à 14 tok/s » vient d'une `--expert-cache N` choisie à la main qui remplit la VRAM (#781, #831), pas de n'importe quelle VRAM pleine. Avec `auto` (le défaut), le cas ne se pose pas.
- **T10** : voir plus haut (« shared Chat settings win »).
- **T11** : #5046 (relu) ajoute une contrainte : d'après le rapporteur, « native IQ pack 不允许去掉 --spec/--mtp » (un fichier IQ natif refuse de démarrer sans `--spec`/`--mtp`, le moteur s'arrête). Le Coder est un fichier IQ natif (`--native` dans #4997 et #5104) : **`--mtp off` est retiré du plan B**. Non confirmé par le développeur. La doc dit aussi que les experts du Coder sont « stored like IQ3_S » (MODELS.md) : le format des fichiers où l'erreur a été vue.
- **T23** : le bug est **plus large** que « une carte de 8 Go ». Commentaires du ticket : même plantage sur RTX 4060 8 Go (Linux), RTX 3080 Ti 12 Go (Windows, 0.2.11), RTX 3060 12 Go (≥ 16K tokens, à chaque fois), **RTX 5070 12 Go (sm_120, la famille de la 5080, 20 plantages)**, RTX 2000 Ada 8 Go. **Cause trouvée** (05/11) : la lecture « couche par couche » compte 512 experts en dur alors que le Coder en a 256. Correctif candidat (branche d'un contributeur, 10/11), testé avant / après sur la **source de la 0.2.13** le 11/11 : la 0.2.13 plante encore, le correctif l'empêche. Le plantage ne survient que si la lecture « couche par couche » démarre (ligne de démarrage « layer-major walk ») ; sur une carte de 12 Go par défaut, un testeur ne l'a pas vue démarrer. **Personne ne rapporte de carte de 16 Go.** Les plantages vus commencent à des demandes de 3 349 tokens.
- **T4** : le téléchargement réel dépasse 58 Go : la couche de prédiction s'y ajoute (T33).

**Ajouté** :

**T31 ✅ [CALCUL d'après le code]** `strata_cli/launch/harness.py` : (1) `_keep_output_cap` garde, quand `strata connect --write` réécrit le fichier d'OpenCode, une valeur `limit.output` différente de 4 096 : refaire `--write` à 98 304 de contexte **laisserait 8 192**, et une valeur montée à la main (32 000) est gardée. (2) Pour Pi, `models.json` est fusionné, mais la liste `models` est **remplacée** (`_merge` ne fusionne que les objets) : un `maxTokens` changé à la main revient à 8 192 à chaque `--write`. (3) La docstring de `output_cap` : « the server fits each request's cap to the room its prompt leaves ». (4) `answer_room` (DETAILS.md) : la réflexion est arrêtée quand il reste un quart de la limite, au moins 512 tokens. **Déduction** : à 8 192, il reste ≈ 2 000 tokens pour le fichier si la réflexion va jusqu'au bout. Non testé : à vérifier au calibrage.

**T32 ✅ [DEV]** Notes de la 0.2.13 : « One fit label in the app and the Terminal: "fits" when the model files without the lookup table fit graphics memory plus RAM, otherwise "may run slower" ». Le libellé « fits / tight / does not fit » de TERMINAL_LAUNCH.md est plus ancien.

**T33 ✅ [DEV]** MODELS.md : « The first start also fetches the MTP draft layer (about 6 GB, 1 GB more with pictures) » ; TERMINAL_LAUNCH.md : « the draft layer, about 5.2 GB ». Téléchargement total ≈ 58,4 + 5 à 6 Go : **« une soixantaine de gigas »**.

**T34 ✅ [DEV]** Le moniteur du Terminal a 7 vues : 1 Overview (vitesse, VRAM, RAM, requêtes récentes), 2 Serving, 3 Requests, 4 Engine, 5 Hardware, 6 Logs, 7 Connect. `q` demande s'il faut continuer à servir ou arrêter (TERMINAL_LAUNCH.md).

**T35 ✅ [DEV]** Toutes les options du plan V2 existent dans TERMINAL_LAUNCH.md : `--plan`, `--family coder --model IQ1_M` (MODELS.md), `--context 64k`, `--vision off`, `--parallel 1`, `--tune skip`, `--access local`, `--data-dir`, `--save-preset`, `--preset`, `--set KEY=VALUE`, `--restart`, `--status`, `--stop` ; `strata connect <app>` avec `--write` et `--check` ; `strata monitor --url` (TERMINAL_QUICKSTART.md). `STRATA_PREFILL_LAYER_MAJOR` est listé dans SETTINGS.md (on / off). **Non confirmé** : `--set reasoning-effort=medium` (retiré), le mot « serving » de `--status`.

**T36 ✅ [DEV]** MODELS.md : « A token is about three quarters of a word ».

**T37 ✅ [DEV] Pi** (https://github.com/earendil-works/pi, README et `packages/coding-agent/docs/`, relus le 11/11) : installation Windows `powershell -c "irm https://pi.dev/install.ps1 | iex"` ou `npm install -g --ignore-scripts @earendil-works/pi-coding-agent` ; **Node.js 22.19 ou plus** ; sous Windows natif, **Git Bash** pour l'outil `bash` (Git for Windows suffit), ou un outil `powershell` en option ; **Windows Terminal recommandé** (l'ancienne console a des bugs connus) ; un serveur compatible OpenAI se déclare dans `~/.pi/agent/models.json` (`baseUrl`, `api: "openai-completions"`, `apiKey`, `models[].id`, `maxTokens`, défaut 16 384) ; une clé factice suffit pour un serveur local ; `pi --continue` (`-c`) reprend la dernière session ; `/model` choisit le modèle. Côté Strata (T14, harness.py) : `strata connect pi --write` écrit `~/.pi/agent/models.json` et `settings.json`, testé avec **pi 0.74.2** ; « pi has the smallest prompt of the eight (**1.5K tokens**) », contre ≈ 7,4 K pour OpenCode, 7,5 K pour oh-my-pi, 12,9 K pour Hermes, 15,6 K pour Claude Code. **CALCUL** : 7 400 − 1 500 ≈ **5 900 tokens de moins par requête**, 9 % d'un contexte de 65 536.

**T38 ✅ [DEV] L'appli de bureau** (INSTALL.md, README, notes de la 0.2.13) : `Strata-0.2.13-windows-x64-setup.exe` (113 296 921 octets, avec sa signature `.sig`) s'installe pour l'utilisateur, sans droits d'administrateur ; **le moteur n'est pas dedans** : au premier démarrage, l'appli propose celui de la carte avec un bouton Download (reprise possible) ; on choisit ensuite le modèle et son dossier ; la page Models dit si chaque modèle tient ; « Closing the desktop app stops its managed engine » ; le Terminal partage le dossier d'installation de l'appli (`%LOCALAPPDATA%\Strata\install`) et reprend un modèle qu'elle a installé (« including one the desktop app installed »). Le harnais intégré à l'appli est le « DeepSeek Harness », présenté seulement avec DeepSeek. **Non trouvé dans la doc** : que l'installeur ajoute la commande `strata` (la doc présente le Terminal comme une installation à part), où l'appli affiche l'adresse de son serveur et sa vitesse.

## Ce que la vidéo peut dire sans tes résultats

- Strata est **gratuit et open source** (T24) ; **le Coder est la seule version de Flash-Next annoncée pour 32 Go de RAM** (T5) ; c'est **une version coupée de moitié, faite pour le code, expérimentale** (T6) ; ses auteurs annoncent **95 % du score de code du modèle complet** (T6) ; la carte garde les experts les plus utilisés, **la RAM le reste, une table de 29 Go reste sur le SSD** (T25) ; **ta marge de RAM est à ras** (T15, calcul) ; **un utilisateur d'une 5070 Ti avec le même processeur mesure ≈ 70 tok/s, réflexion coupée, sans test de justesse** (T7) ; **un testeur sur 12 Go de VRAM et 32 Go de RAM a eu 5 réussites sur 6 tâches** (T4) ; **un autre testeur a vu le Coder échouer à une tâche Claude Code** (T27) ; **un utilisateur de 5080 rapporte des erreurs « non-finite logits »** avec d'autres fichiers (T11) ; **le moteur peut planter sur un long prompt avec le Coder** (T23).

## Ce que la vidéo ne doit pas dire

- « Flash-Next tourne sur 32 Go » : c'est **le Coder** seulement (T5). Le Flash-Next complet veut ≥ 44 Go (Q2_0) à 60 Go (IQ3_S), S8.
- « 125 milliards de paramètres sur ma carte » pour le Coder : c'est une version à **256 experts sur 512**, ne dis pas le chiffre pour elle.
- Un tok/s ou une durée avant d'avoir la mesure : tout est dans la fiche.
- « Strata ne marche pas sur 5080 » ou « marche sur 5080 » comme vérité générale : seulement **ce qui s'est passé chez toi** et **ce que rapportent d'autres utilisateurs** (T11, T20).
- Un classement général « local contre Claude » : trois demandes, une tentative chacune.
- Des chiffres de 64 Go ou de 128 Go de RAM comme s'ils étaient les tiens (T4, T29).

## À vérifier toi-même pendant le tournage

1. La **version** installée (`strata --version`, moteur) et le **mode** (`--resident-experts` ou `--mmap-experts`) : T1, T8.
2. Que `"maxTokens": 32000` dans `~/.pi/agent/models.json` suffit pour que le fichier du calibrage soit complet (T31, déduit du code) ; si tu as dû passer à OpenCode, `"output": 32000` dans `opencode.json`.
3. Si la ligne de démarrage « layer-major walk » apparaît (T23), et si tu as dû mettre `STRATA_PREFILL_LAYER_MAJOR=0`.
4. Si l'installeur de l'appli a mis la commande `strata` (T38), et si le Terminal a repris le modèle de l'appli sans le retélécharger (`--plan`).
5. Le nom du faux produit du test 2 : **« Tikaya »**, aucune société de paiement trouvée sous ce nom le 11/11 (recherche web). « Kora » a été écarté : société de paiement réelle, active en Afrique y compris francophone.
6. Tous les chiffres de T4, T19 et T29 qui viennent de sous-titres automatiques, **à l'écran** avant de les citer.

## H. Angle 16 Go (ajouté le 11/11, repris de `claude-ou-mon-pc-1/sources.md`)

**T39 ✅ [MESURE] Une carte de 16 Go abordable.** Ticket Strata **#2250** (13/10/2026) : **AMD Radeon 9600 XT 16 Go**, Ryzen 7 5700X, **30,3 Gio de RAM**, Linux, Strata 0.1.43, **Coder** : **37,6 tok/s** en chat court, 41,7 en session d'agent (https://github.com/Niko1221/Strata/issues/2250 ; S10 de `claude-ou-mon-pc-1/sources.md`, relu le 05/11). Ticket fermé lors de la remise à zéro du suivi ; version ancienne de Strata : à dire « environ ».

**T40 ✅ [DEV + CALCUL] Bande passante mémoire** : RTX 5080 **960 Go/s**, RTX 5060 Ti **448 Go/s** (page de comparaison NVIDIA ; S39 de `claude-ou-mon-pc-1/sources.md`). 960 ÷ 448 ≈ 2,1 : « deux fois plus rapide ». Avec Strata, une partie des experts vient de la RAM : la carte n'est pas le seul facteur, d'où « plutôt le haut de la fourchette », sans chiffre pour la 5060 Ti.
