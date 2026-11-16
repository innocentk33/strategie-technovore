# Recherche A : Nathan Inline, « Mon IA locale va 11 fois plus vite (même PC) »

> Source : [vidéo](https://www.youtube.com/watch?v=VFC16Tb3lwU), 7 min 27 s, publiée le 14/11/2026. Transcription : `etudes/transcriptions/nathaninline-VFC16Tb3lwU.md` (sous-titres auto, mots parfois mal reconnus : « Innight », « Antoine InLine » = Nathan Inline). Analyse faite le 15/11/2026, sans vidIQ. Tous les chiffres viennent de ses paroles ; aucune mesure n'est vérifiée de notre côté. Les recherches web (section 2) sont rapides et en partie secondaires.

Machine annoncée (0:30-0:47) : RTX 5060 Ti 16 Go (fait « presque tout le travail »), RTX 3070 8 Go, Ryzen 9 3900X, 46 Go de DDR4 (« c'est lui qui va tout décider »). Modèle : « Qwen 3.8 Flash Next », MoE de 512 experts par couche sur plus de 48 couches, 10 experts actifs par token, experts = 40 à 55 Go selon le quant (0:00-1:10). En fin de vidéo (6:59-7:16) : 2 barrettes de 16 Go + 2 de 8 Go de DDR4 et la 5060 Ti.

## 1. Tableau chronologique

D = decode (génération, tok/s). P = prefill (lecture du prompt, tok/s). Les deux ne sont jamais mélangés.

| # | Date (dite) | Étape / levier | Vitesse avant → après | Moteur | Fichier / quant | Conditions | Timecode |
|---|---|---|---|---|---|---|---|
| 1 | fin août | Départ avec llama.cpp | D : — → **7,9** | llama.cpp | non précisé | 5060 Ti (+ 3070 non utilisée à ce stade, non précisé) ; RAM : tout en RAM, non précisé | 1:15-1:24 |
| 2 | fin août | Quelques couches sur la 2e carte | D : 7,9 → **9,5** | llama.cpp | non précisé | 5060 Ti + 3070 ; le CPU est « à fond », les GPU font presque rien : « le problème c'est la RAM » | 1:26-1:38 |
| 3 | 10 sept. | Moteur avec cache d'experts chauds en VRAM (nom non donné) | D : 9,5 → **24,5** (« plus de 3 fois ») | non nommé (autre que llama.cpp) | non précisé | « sans changer de matériel » ; la 3070 « ne sert plus à rien » | 1:40-2:00 |
| 4 | sept. | Quant plus gros Q4_K_M : le piège | P : non précisé ; « une minute » avant le 1er mot | même moteur | Q4_K_M | experts qui dépassent la RAM | 2:02-2:12 |
| 5 | sept. | RAM verrouillée + 9 couches en VRAM | P : **31 → 206** | même moteur | Q4_K_M | tout doit tenir en RAM ; D non précisé | 2:12-2:25 |
| 6 | fin sept. | Abandon de llama.cpp, moteur dédié MoE + MTP (devine plusieurs tokens, vérifie d'un coup) | D : → **58** (« la vitesse double »), puis 64, puis 70 ; P : → **1 000** | moteur dédié (nom non donné ; la fiche A-nathan ne peut pas affirmer lequel) | non précisé | « sans changer de matériel » implicite ; 3070 : 10 à 15 % de gain (bilan 4:59-5:06) | 2:26-2:50 |
| 7 | oct. | Incident : RAM pleine, serveur bloqué (test de trop) | — | — | — | garde-fous ajoutés : limite de RAM, coupure auto, redémarrage auto | 2:53-3:12 |
| 8 | oct. | Son propre moteur, en une journée | D : **29 → 63** | maison | non précisé | plus lent que le moteur déjà utilisé (70) ; mis de côté | 3:14-3:26 |
| 9 | fin oct. | Basalt, 1er essai | D : **57** (moins bien qu'avant) | Basalt | non précisé | 10 Go de RAM occupés par d'anciens tests | 3:28-3:47 |
| 10 | fin oct. | Basalt après nettoyage de la RAM | D : 57 → **94** ; P : → **2 200** | Basalt | non précisé | RAM libérée ; la 3070 ralentit tout, version officielle de Basalt refuse la carte (« uniquement les cartes qui commencent par 50 ») | 3:47-3:55, 5:04-5:12 |
| 11 | début nov. | Autres quants : tous à 63 | D : → **63** pour chacun | Basalt (sous-entendu) | plusieurs quants, non nommés | cause : 1 couche sur 48 dans un format inconnu du mode rapide | 3:56-4:12 |
| 12 | début nov. | Conversion de cette couche | D : 63 → **83** | Basalt (sous-entendu) | non précisé | — | 4:14-4:16 |
| 13 | début nov. | Choix du quant : 9 essayés, UD-IQ2_XS d'Unsloth gardé | D : non précisé ; qualité : perplexité **3,285** vs **3,273** (modèle d'origine), « 99,4 % de la qualité » | Basalt (sous-entendu) | UD-IQ2_XS (Unsloth) | les plus gros quants : experts ne tiennent pas en RAM | 4:18-4:44 |
| 14 | nov. | 2e carte (3070) : bilan | D : +20 % (début) → plus rien (cache d'experts) → +10 à 15 % (moteur dédié) → ralentit (Basalt) | — | — | décision : ne plus l'utiliser | 4:56-5:17 |
| 15 | nov. | Duel Tinfield-1 vs Flash Next | D : Tinfield **80** vs Flash Next **68** | non précisé | non précisé | incohérent avec le 83 de la ligne 12 (autre moteur, autre quant ou autre conditions ? non précisé) | 5:59-6:03 |
| 16 | nov. | Test agent, 10 tâches corrigées auto | qualité : **9,5/10** Flash Next vs **8,95/10** Tinfield-1 | non précisé | — | 6 faciles : égalité ; 4 difficiles : Flash Next réussit tout | 6:12-6:35 |
| 17 | 14 nov. (bilan) | Résultat final annoncé | D : **83** ; P : **2 200** | Basalt (par déduction) | UD-IQ2_XS (par déduction) | 5060 Ti seule (par déduction), 46 Go DDR4 | 6:57-7:02 |

Le « 11 fois plus vite » (7:18-7:20) vient de 83 / 7,9 = 10,5. Il le dit aussi « 10 fois » (4:44) et « plus de 80 vs 7 » (0:15-0:23). Le 94 tok/s (ligne 10) est plus haut que le 83 final : il ne le commente pas (le changement de quant a coûté de la vitesse, non précisé).

Autres cas non précisés : version de llama.cpp, options exactes (`-ngl`, `--n-cpu-moe`, etc.), taille de contexte, cache KV, longueur du prompt pour le prefill, nombre de mesures, moyenne ou pic. Aucun de ces réglages (contexte, cache KV quantisé) n'est mesuré dans sa vidéo.

## 2. Outils et moteurs cités

Recherche web rapide du 15/11, résultats secondaires non vérifiés à la source.

| Nom | Ce que c'est d'après lui | Existence publique |
|---|---|---|
| llama.cpp | « le moteur que tout le monde utilise » (1:17) | Existe (connu). |
| Moteur à cache d'experts chauds | Garde les experts les plus utilisés en VRAM (1:43-1:51) ; nom non donné | Non identifié. Lien probable avec Strata (voir plus bas) : non affirmé. |
| MTP | Deviner plusieurs tokens d'avance et les vérifier d'un coup (2:33-2:40) | Technique réelle (décodage spéculatif par couche multi-token) ; selon un résumé secondaire, Strata l'utilise (jusqu'à 3 tokens proposés). |
| Moteur dédié MoE (sept.) | Moteur « écrit exprès pour ce type de modèle » (2:28) | Nom non donné ; probablement Strata, à confirmer. |
| Basalt | « moteur encore plus récent », promet beaucoup, version officielle compatible seulement avec les cartes « qui commencent par 50 » (3:31, 5:08-5:12) | **Introuvable** (aucun dépôt GitHub trouvé). Un article secondaire ([remio.ai](https://www.remio.ai/de/post/qwen3-8-basalt-benchmark-reports-153-tokens-per-second-on-16gb-vram-de)) le décrit comme un fork de Strata pour Blackwell, 153 tok/s sur RTX 5080 16 Go et 54,1 Go de RAM : affirmation non vérifiée, à ne pas citer sans la source primaire. |
| Swift | Version qui « réfléchit moins longtemps », abandonnée un mois plus tard (5:21-5:25) | **Introuvable**. |
| Edge0 (« Edge Zero ») | Version aux « experts d'un nouveau genre » ; en format classique sa qualité baisse ; avec le moteur modifié : 57 tok/s max, supprimé (5:25-5:40) | **Introuvable**. |
| Tinfield-1 | Fine-tune pour le code, repéré parmi ~1 600 versions du modèle sur Hugging Face (5:41-5:55) | **Introuvable** (la recherche ne renvoie que des dérivés code découpés de Jab1718, dont [qwen3.8-flash-coder-26gb](https://huggingface.co/Jab1718/qwen3.8-flash-coder-26gb) : rien ne dit que ce soit lui). |
| Unsloth UD-IQ2_XS | Quant d'Unsloth qui garde la précision là où c'est important (4:24-4:33) | Dépôt Unsloth existant : [unsloth/Qwen3.8-Flash-Next-GGUF](https://huggingface.co/unsloth/Qwen3.8-Flash-Next-GGUF). Le quant précis UD-IQ2_XS n'a pas été ouvert. |
| Qwen 3.8 Flash Next | Le modèle (0:12) | Existe : [Qwen/Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next). |
| Strata (non cité par lui) | — | Moteur existant d'après des sources secondaires : dépôt Niko1221/Strata (MIT), cache d'experts + MTP, 12 Go de VRAM minimum, 32 à 64 Go de RAM selon les sources ([guide](https://glukhov.org/llm-hosting/strata/strata-qwen3-8-flash-next-quickstart/)). Lien avec « le moteur dédié » de Nathan : déduction, non confirmée. |

## 3. Nombre de paramètres : à vérifier

- Nathan annonce « plus de 177 milliards » (0:06-0:10).
- Notre autre document (Qwen 3.8 Flash Next) dit 125 milliards. La recherche web de ce jour montre la même divergence : la carte du modèle donnerait 125 B au total avec 6 B actifs, et une autre source 176 B en comptant une table d'embeddings n-gram, une troisième environ 180 B en BF16. Je ne tranche pas : il faut ouvrir la carte Hugging Face officielle et noter ce qu'elle dit, avec la date, avant de citer l'un ou l'autre.
- Autre détail à vérifier : 512 experts par couche sur plus de 48 couches, 10 actifs (0:56-1:04), et « experts entre 40 et 55 Go » (1:07).

## 4. Structure, et ce qu'il ne faut pas reprendre

**Hook (0:00-0:30)** : promesse chiffrée immédiate (« plus de 177 milliards de paramètres à plus de 80 tokens/s sur ma petite carte de 16 Go »), avant/après (7 → 80), puis « 3 mois de galère » : tension, puis la config et le chiffre qui décidera (46 Go de RAM).

**Plan** : machine (0:30) → problème MoE (0:51) → llama.cpp (1:15) → moteur à cache (1:40) → piège Q4_K_M (2:02) → moteur MTP (2:26) → incident RAM (2:53) → moteur maison (3:14) → Basalt (3:28) → mystère des 63 (3:56) → bon quant (4:18) → bilan et RTX 3070 (4:44) → Swift, Edge0, Tinfield-1, duel (5:19-6:35) → 5 leçons (6:37) → clôture (7:22).

**Rythme** : 7 min 27 s, un chiffre toutes les 10 à 15 s, échec puis rebond à chaque étape, aucune visualisation décrite dans la transcription, peu d'explication de pourquoi un levier marche.

**À ne pas reprendre** :
- Le récit de 3 mois, avec dates, essais de moteurs, incident serveur et sa propre fabrication de moteur : c'est son histoire, et elle repose sur des outils introuvables (Basalt, Swift, Edge0, Tinfield-1).
- Le duel de modèles et le test agent (hors sujet pour « mêmes réglages, même carte »).
- Sa conclusion « le moteur compte plus que le matériel » comme thèse : la reprendre ferait un doublon, il faut le décomposer en réglages.

**3 angles de différenciation** :
1. **Checklist de réglages vérifiables, chacun avec sa mesure** (avant → après, decode et prefill séparés, même machine) : fichier/quant, déchargement des couches/experts, taille du contexte, cache KV, MTP, moteur. Lui ne mesure aucun contexte ni cache KV.
2. **La règle de la RAM d'abord, comme test à faire en 2 minutes** : « tout doit tenir en RAM » (2:23), et son piège Q4_K_M (31 → 206 en prefill) devient un diagnostic : comment savoir si tes experts débordent. Sa surprise « un seul format de couche fait tout tomber à 63 » (4:07) est un autre piège à vérifier chez soi.
3. **Le test du quant par la qualité** : mesurer perplexité ou tâche réelle avant de choisir un petit quant (son 3,285 vs 3,273 est le seul chiffre de qualité, une mesure unique à croiser avec une seconde source).

## 5. Comparabilité avec une autre machine

Ses tok/s ne sont pas transposables à : RTX 5080 16 Go, 32 Go de DDR5, modèle « Coder » de Strata (la moitié des experts, donc pas le modèle complet).

| Paramètre | Nathan | Autre machine | Effet |
|---|---|---|---|
| Carte | 5060 Ti 16 Go | 5080 16 Go | même VRAM, autre bande passante et autre puissance : decode qui dépend surtout de la RAM, pas comparable à l'avance |
| RAM | 46 Go DDR4 (limite décisive pour lui) | 32 Go DDR5 | moins de capacité (le modèle plein de 40-55 Go d'experts ne tient pas), mais bande passante plus haute |
| Modèle | complet (0:12) | Coder de Strata, moitié des experts | autre modèle, autre taille de fichier, autres qualités : à ne pas comparer en tok/s ni en qualité |
| Quant | UD-IQ2_XS | non précisé | taille du fichier différente, donc besoin de RAM différent |
| Moteur | Basalt (introuvable) | Strata | non reproductible |
| 2e carte | 3070 (a ralenti) | aucune | non applicable |
| Mesure | decode 83, prefill 2 200 | à mesurer | contexte, prompt et nombre de tests non précisés |

À citer seulement comme ordres de grandeur de gains relatifs (x3 avec cache d'experts, x2 avec MTP, +30 % avec un format de couche corrigé), jamais comme des promesses de vitesse absolue : aucune des vitesses n'est « à toi » (règle du calculé).

## Résumé

1. Nathan : 7,9 → 83 tok/s en decode (≈ 10,5 fois) et prefill 2 200, sur 5060 Ti 16 Go + 46 Go DDR4, avec un moteur introuvable (Basalt) et un quant UD-IQ2_XS (4:18-4:44, 6:57-7:02).
2. Ses trois sauts viennent du moteur (24,5 en cache d'experts à 1:51 ; 58 avec MTP à 2:42 ; 94 avec Basalt à 3:49), pas du matériel.
3. Basalt, Swift, Edge0 et Tinfield-1 sont introuvables ; Strata existe, mais le lien avec ses moteurs est une déduction.
4. 177 milliards (lui) contre 125 milliards (notre document, et la carte du modèle d'après la recherche) : à vérifier, non tranché.
5. À ne pas reprendre : son récit de 3 mois ; à faire : checklist de réglages mesurés, decode et prefill séparés, chiffres de Nathan seulement en ordre de grandeur.
