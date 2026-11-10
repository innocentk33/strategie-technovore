# Radar Technovore

> À chaque sortie d'une vidéo, on refait le radar : la procédure est dans [`CLAUDE.md`](../CLAUDE.md), section « Radar ». L'entrée la plus récente est en haut. Tous les chiffres viennent de vidIQ et sont datés.

## Liste de surveillance

À passer en un seul appel `vidiq_outliers` par langue (`channelIds`, `publishedWithin: thisMonth`).

| Chaîne | Langue | Pourquoi | ID |
|---|---|---|---|
| Kai | EN | IA locale : coût et matériel ([étude](kai.md)) | `UCgUfJoPtkt7-RiiuYh4vmGA` |
| Morgans Code | EN | IA locale : calculs sans tests ([étude](morganscode.md)) | `UCetGP9xk9LYIxzYO9Id3o6g` |
| Code Unpacked | EN | IA locale : « même carte, plus rapide » ([étude](outliers-2026-10-22.md)) | `UCuXX9B1kSwRTQE2BIhK7Khw` |
| ByteMonk | EN | Le génie derrière l'app | `UCzCsyvyrq38R6TnztEzOmgg` |
| Thibaut Dcode | FR | Applis et marques, angle business | `UCNew6vrycRR0QnlYmLoMRZg` |
| Makertronic Tech | FR | Matériel, IA, histoire de la tech | `UCjBWE9WaXEtkqad7F68W5OQ` |
| Le Lab IA (Jerome Fortias) | FR (BE) | IA en local | `UC4PY6oWBZjLg32a3z2zrUKw` |
| Baptiste Simard | FR | Claude Code, vibe coding | `UCzabGLybo9x307MkDtqTyFQ` |
| Machine Learning Lab | FR | « Comment ça marche » sur l'IA | `UCu34JW8lOyx_1vElmxqyUew` |
| Bricolo2.0 | FR | IA gratuite à la maison | `UCPC2ZL10br9fuhvhvuKh13g` |
| FEU | FR | IA en local, agents | `UCvgcGOW3UQskqWboU1VDX9A` |
| RepoChad | EN | IA locale : matériel et VRAM (« Every Way to Get X GB of VRAM… ») | `UCtyEhOTxGx45sljlfryc6jw` |
| Weights & Wonders | EN | IA locale : GPU et prix, voix IA, actu Qwen | `UC6dYyJvl6mj6Xu1vCFsl-6A` |

**Mots-clés français** (`vidiq_outliers`, `language: fr`, `threeMonths`) : « IA en local », « comment ça marche », « Qwen 4 », « VRAM », « carte graphique IA », et le nom de l'appli ou du modèle des prochains créneaux.

---

## 10/11/2026 : passage à 2 vidéos IA/semaine (lun. + jeu.), « 16 Go » à J+1, l'installation à J+8, Qwen 4 et deux nouvelles chaînes EN

**Décision du jour (ta demande) :** la chaîne passe à **2 vidéos par semaine, lundi et jeudi, 18 h, uniquement IA / IA locale**, du jeu. 12/11 au lun. 4/01/2027, puis retour à 1 vidéo/semaine (lundi). Les piliers « génie » et « histoires » sont **archivés** pour cette période : plus de règle 3 pour 1. Chaque vidéo se fait en 1-2 jours, reste calculée (sources, mesures publiées, études, calculs) sauf exceptions filmées déjà décidées (installation du 2/11, test Strata du 16/11).

### Notre chaîne

| | 16 Go de VRAM (09/11, **J+1**) | Installation IA locale (02/11, **J+8**) |
|---|---|---|
| Vues (Studio) | 79 | 297 |
| Likes / commentaires | 5 / 3 | 3 / 7 |
| `vidiq_channel_analytics` (totaux) | **Vide : retard de l'API**, comme au 21/10. Rien de plus fiable que le compteur Studio à J+1. | Traffic sources et rétention ci-dessous |
| Sources de trafic (02-10/11, ~273 vues) | — | **Abonnés 46 %**, externe (EXT_URL) 24 %, recherche YouTube 16 %, suggestions (RELATED_VIDEO) seulement 6 %, notifications 3 % |
| Rétention (courbe) | — | **0:15 ≈ 74 %** (cible 75 %, presque atteinte), **1:00 ≈ 59 %** (cible 50 %, dépassée) ; creux à ~40 % vers le milieu puis remontée à ~65 % (55-65 % de la vidéo), puis descente classique en fin de vidéo |
| Suggestions détaillées | — | 5 vidéos sources, 1-2 vues chacune : **rien d'exploitable**, échantillon trop petit |

- **L'installation reste le meilleur format retenu de la chaîne** après celui du 05/11 : la rétention à 1:00 dépasse largement la cible, et les abonnés (46 % du trafic) regardent encore. Les suggestions ne nous portent presque pas (6 %) : le classement Flutter pèse toujours.
- **16 Go** n'a qu'un jour de recul : pas de verdict avant le prochain radar (J+7, vers le 16/11).

### Concurrents EN (liste de surveillance, `thisMonth`, 13 chaînes dont les 2 nouvelles)

- **Kai** reste la référence du format « X Go de VRAM » : *Don't Buy a GPU Instead Build This 32GB Free AI Server* (419,7 K, ×5,8, 12/10), *Your Local AI Is Not as Private as You Think* (573,1 K, ×5,3, 21/10), *512GB VRAM* (193,1 K, ×2,3), *How I Got Frontier Performance on 16GB VRAM (Qwen 3.8 27B)* (112,6 K, ×1,1, 18/10) — très proche de notre « 16 Go ».
- **RepoChad** (14 200 abonnés, 2,53 M vues, 55 vidéos, Inde) : *Every Way to Get 256 GB of VRAM for Local AI* (162,4 K, **×7,4**, 19/10) — le format visé par l'idée (a) ; *Run FULL DeepSeek v4.1 Flash on a 12GB GPU* (53,7 K, ×2,6, 02/11) ; *China's AI Bubble Just Burst! Will GPU Prices Finally Drop?* (40 K, ×1,9, 28/10).
- **Weights & Wonders** (1 220 abonnés, 172,7 K vues, 22 vidéos, Inde) : ***Don't Miss Out on These GPUs Before Qwen 4's Release!*** (25,6 K, **×4,2**, 272,7 vues/h, publiée le 08/11, il y a 2 jours) — l'idée (b) ; *I asked Qwen 3.8 27B to Optimise Itself* (33,3 K, ×16) ; *I Forced Qwen to Use All Its Experts* (19,2 K, ×4,1).
- **Morgans Code** : *Qwen 4 27B: What to Expect From the Next Local AI King* (28 K, ×3,8, 16/10, rumeur/attente) ; *Uncensored Qwen 3.8 27B Isn't the Hacker You Think* (6,2 K, **×20**, 08/11) ; *DeepSeek V4.1 1017 Flash Is Opus-Level: What Does It Really Cost to Run?* (15,3 K, ×1,6, 19/10).

### Public français

- **« Qwen 4 » en français (`vidiq_outliers`, fr, thisMonth)** : **aucun résultat pertinent** — les 15 vidéos qui sortent sont des faux positifs sur le chiffre « 4 » (MW4, saisons 4, épisodes 4…). **Personne n'en parle encore en français.**
- **« VRAM carte graphique IA » (fr, threeMonths)** : signal direct — **Makertronic Tech**, *TAXE VRAM, la Chine dit NON : elle double la VRAM de tes RTX !* (20,1 K, ×2,1, **05/11**, 115,5 vues/h) : la chaîne de notre liste de surveillance couvre déjà l'angle « VRAM + Chine », pas encore « deux cartes d'occasion » ni l'actu Qwen 4. Sinon, rien de spécifique IA locale (bruit gaming/matériel général).

### Qwen 4 : confirmé ou rumeur ? (recherche web, sources datées)

**Confirmé (annonces officielles Alibaba/Qwen)** :
- **22/09/2026, conférence Apsara (Hangzhou)** : Alibaba a dévoilé les noms **Qwen 4 Max, Qwen 4 Flash, Qwen 4 Plus, Qwen 4 27B**, et confirmé que Qwen 4 est en entraînement. Aucune date de sortie, aucun prix, aucun poids téléchargeable à cette date.
- **26/08/2026** : Qwen a publié **Qwen3.8-Flash-Next** sur Hugging Face, explicitement présenté comme un aperçu de l'architecture de Qwen 4 (Gated DeltaNet + Qwen Sparse Attention).
- **06/11/2026** : le compte officiel Qwen a posté un teaser (« The becoming begins ») qui a relancé les spéculations, sans date précise.
- Alibaba a aussi annoncé une feuille de route **Qwen 4.5 et Qwen 5** (5 à 10 000 milliards de paramètres).

**Rumeur / non confirmé** :
- Une sortie en **novembre 2026** « semble de plus en plus probable » selon un participant à une conférence Alibaba du 29/10 qui rapporte des propos du CTO — information de seconde main, non officielle.
- Des identifiants de code (« qwen4-max », « qwen4-plus », « qwen4-coder-plus ») trouvés dans des mises à jour de code du 28/10 (fuite non confirmée par Alibaba).
- **Aucun checkpoint Qwen 4 n'est disponible sur Hugging Face** à la date du radar.

**Verdict pour nos vidéos** : on peut dire « Qwen 4 Max/Flash/Plus/27B existent déjà comme noms officiels, en entraînement depuis le 22/09, mais sans date, prix ni poids confirmés » — c'est vérifiable et sourcé. Tout le reste (date de sortie, tailles exactes en Go) doit être présenté comme rumeur.

### Proposition de grille (jeu. 12/11 → lun. 4/01/2027, lundis ET jeudis, uniquement IA)

**Créneaux déjà pourvus en IA, inchangés** : lun. 16/11 (Strata, filmée, exception déjà décidée), lun. 30/11 (Combien coûte Claude en local), lun. 7/12 (Strata petits budgets — angle à revoir sans Strata si Strata recule), lun. 14/12 (IA en local : lire le nom d'un modèle), lun. 28/12 (Louer, acheter), lun. 4/01 (Abonnement ou IA locale #2).

**Créneaux à sortir de la règle 2×/semaine IA (non-IA, pilier archivé) :** lun. 23/11 (Waze, génie) et lun. 21/12 (Python) ne sont plus « IA / IA locale » strictes. Python garde un lien ténu (« le langage de l'IA ») : à trancher avec toi. Waze n'a aucun lien IA : à décaler vers un créneau post-04/01, quand les piliers reviennent.

| Créneau | Vidéo proposée | /40 | Justification (une ligne) |
|---|---|---|---|
| **Jeu. 12/11** | **Qwen 4 : les cartes graphiques à acheter avant sa sortie** (inspirée de Weights & Wonders, angle Technovore : prix FR/Afrique, confirmé vs rumeur) | **32/40** (demande 8 · clic 8 · production 7 · niche 9) | W&W fait ×4,2 en 2 jours (272 vues/h) sur cet angle précis ; fenêtre courte avant que Qwen 4 sorte vraiment (teaser du 06/11) — à produire vite (1-2 j) |
| **Lun. 23/11** (remplace Waze) | **32 Go de VRAM avec deux cartes d'occasion** (inspirée de RepoChad, reprend `deux-cartes-occasion`) | **35/40** (demande 9 · clic 8 · production 8 · niche 10) | RepoChad fait 162 K vues ×7,4 sur « Every Way to Get X GB VRAM » ; sources déjà vérifiées deux fois (24/10), aucun achat réel, rien d'équivalent en français |
| **Jeu. 19/11** | **Même carte, 2 fois plus rapide** (idée 16, réserve `idees.md`) | **34/40** (demande 8 · clic 9 · production 8 · niche 9) | Déjà scorée en réserve ; Code Unpacked avait fait 11,2 K en un jour sur l'angle « plus rapide, pas plus grosse » (22/10), rien en français |
| **Jeu. 26/11** | **Ton IA locale est-elle vraiment privée ?** (idée réserve, sécurité : Ollama exposé, modèles piégés) | **34/40** (demande 9 · clic 9 · production 7 · niche 9) | Kai fait 573 K vues ×5,3 sur l'angle proche ; aucun équivalent français trouvé dans ce radar ni le précédent |
| **Jeu. 3/12** | **Combien coûte DeepSeek V4.1 Flash chez toi ?** (série « combien coûte [modèle] », idées réserve) | **30/40** (demande 7 · clic 7 · production 7 · niche 9) | Morgans Code fait 15,3 K ×1,6 sur ce calcul ; angle Technovore en euros/FCFA, calculée, réutilise la méthode de Coût Claude |
| **Jeu. 10/12** | **Mac mini ou PC gamer pour l'IA en local ?** (avancée du 11/01, `mac-mini-ia`) | **33/40** (demande 8 · clic 8 · production 7 · niche 10) | Fiche déjà posée (24/10), inspirée de Locally (40 K, ×21,9) ; recherche et double vérification restent à faire — avancer la date densifie le bloc IA sans nouvelle idée |
| **Jeu. 17/12** | **Le dev qui a mis un ChatGPT dans ton PC** (llama.cpp, avancée du 18/01) | **31/40** (demande 7 · clic 8 · production 7 · niche 8) | Script déjà écrit (23/10) ; limite avec la nouvelle règle (plus « histoire d'outil » que calcul pur) — à confirmer avec toi avant de le déplacer ici |
| **Jeu. 24/12** (veille de Noël) | **Pause recommandée**, ou rediffusion/compilation plutôt qu'une nouvelle vidéo | — | Faible trafic habituel la veille de Noël ; mieux vaut garder la vidéo du 21/12 (ou son remplaçant) en avant plutôt qu'un nouveau sujet qui se perdra |
| **Jeu. 31/12** (veille du Nouvel An) | **Pause recommandée**, même raison | — | Idem : veille de jour férié, faible audience attendue |

**Stock restant si tu veux garder le rythme sans pause le 24 et le 31/12** : les deux idées réserve non encore datées (« Combien coûte [modèle] » peut se refaire modèle par modèle, p. ex. DeepSeek V4.1 ou Qwen 3.8 27B) ou une 2e vidéo Qwen 4 dès qu'il sort réellement (si la sortie confirmée tombe avant le 04/01, elle mérite un créneau dédié, probablement en remplaçant un des candidats ci-dessus plutôt qu'en ajout).

**Crédits vidIQ utilisés dans ce radar : 45** (~~balance 0~~ **corrigé le 10/11, 2e passe : la balance affichée ce jour-là n'était pas 0, voir ci-dessous** · `vidiq_user_videos` 5 · 4× `vidiq_channel_analytics` 20 · `vidiq_get_channels_by_ids` 5 · `vidiq_outliers` ×3 15).

---

## 10/11/2026 (2e passe) : DeepSeek Super-Agent (verdict), Qwen 4 (toujours rumeur) et les 4 créneaux de fin décembre

**Correction des crédits** : le « balance 0 » noté dans l'entrée du 10/11 ci-dessus était faux. Le solde réel, vérifié ce jour (`vidiq_balance`, 0 crédit) : **4 454 crédits** (3 829 renouvelables sur 6 000, renouvellement le 12/11 ; 625 crédits bonus sur 700). Il restait donc largement de quoi faire ce 2e passage. Budget utilisé ici : **10 crédits** (`vidiq_balance` 0 · 2× `vidiq_outliers` 10), sur un budget de ~60.

### DeepSeek Super-Agent : les faits (sources datées)

- **Ce que c'est** : `dsh-superagent`, publié le **31/10/2026** par DeepSeek sur `deepseek-ai/dsh-superagent-prototype` (GitHub), **licence MIT**, écrit en TypeScript. C'est un agent de codage qui vit dans un dépôt GitHub (et optionnellement les discussions Feishu de l'équipe), pas un nouveau modèle : il s'ajoute à **DeepSeek Harness (`dsh`)**, le framework d'agents sorti en août 2026. DeepSeek le présente lui-même comme « un prototype de recherche, pas un produit fini ». Sources : [MarkTechPost, 01/11](https://marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent), [datastudios.org](https://www.datastudios.org/post/deepseek-dsh-superagent-mit-proactive-coding-agent-github-feishu).
- **Peut-il tourner en local ?** Oui, mais pas avec « DeepSeek » comme modèle local : `dsh` accepte n'importe quel serveur compatible OpenAI (protocole `openai-completions`), donc un modèle **local, pas DeepSeek** — le guide d'installation documente un test concluant avec **Qwen3.5-4B** (2,74 Go en GGUF Q4_K_M) via **llama.cpp ou Ollama** (Ollama 0.32.11 a l'intégration directe `ollama launch dsh`). Sans cette config, `dsh` utilise par défaut l'API cloud `deepseek-flash`. Source : [jacar.es](https://jacar.es/?p=7252).
- **Quelle machine ?** Node.js, 5 Go de RAM libres minimum pour le serveur local, Docker ou llama.cpp. Sur CPU sans GPU, une fonction simple a pris **entre 171 secondes et 45 minutes** selon la charge — un modèle 4B, lent, avec une fidélité faible sur les accents et les caractères non-latins. Pour `dsh-superagent` lui-même, DeepSeek recommande en plus une **machine dédiée ou un compte système isolé**, parce que les sessions « worker » exécutent des commandes sans validation préalable (risque de sécurité).
- **Tendance mesurée** (`vidiq_outliers`, ce mois) :
  - **EN** : très couvert — Sam Witteveen (140 K abonnés) à 195,7 K vues (×4, 03/11) ; AI LABS (180 K) à 72,6 K vues (×2,1, 05/11) ; Julian Goldie SEO (439 K) a sorti **5 vidéos** sur le sujet en une semaine.
  - **FR** : déjà traité par au moins **3 chaînes** avec un angle proche du nôtre si on le ferait : Julien Massey (39,1 K abonnés, FR), *« DeepSeek vient de TUER Claude Code »*, 41,2 K vues, ×5,9, **07/11** ; Pentiminax (30,1 K, FR), **2 vidéos** (*« il travaille à ta place »*, 20,4 K vues, 02/11, et une mise à jour le 20/10) ; IA Technologie (8 K), *« l'IA qui bosse dans ton équipe »*, 26,7 K vues, ×18, 03/11. Confirme et précise le « trois grosses chaînes françaises » du 05/11.
  - Recherche FR directe sur « DeepSeek Super Agent » : les résultats sont dominés par ces mêmes vidéos de créateurs IA/dev — pas de vide à combler.

**Verdict : (c) on ne le fait pas**, pour trois raisons qui se cumulent :
1. ce n'est pas vraiment de l'IA **locale** : l'angle « je le fais tourner sans cloud » obligerait à montrer un petit modèle Qwen 4B, lent (jusqu'à 45 min pour une fonction) et pas fiable, sous le nom « DeepSeek », ce qui induirait le public en erreur (« les faits comptent », `CLAUDE.md`) ;
2. l'angle (b), IA non locale, est déjà traité par au moins 3 chaînes françaises avec le même cadrage (« ça tue Claude Code », « il bosse à ta place ») et des dizaines de vidéos anglaises : aucune place pour ne pas copier l'angle ;
3. c'est un agent de codage pour des équipes de dev, pas un sujet qui parle à notre audience grand public (63 % Afrique francophone, 94 % moins de 35 ans), contrairement aux séries « combien ça coûte » ou « combien de VRAM ».

Score, si on le forçait quand même en angle (a) « je le fais tourner sans cloud » : **22/40** (demande 6 · clic 7 · production 4 : contredit la règle « calculé, sans essai » puisqu'il faudrait démontrer la lenteur réelle · niche 5 : agent de code, pas IA locale grand public). Sous le seuil des créneaux retenus (29-35/40) : confirme qu'on laisse tomber, comme le 05/11.

### Qwen 4 : toujours une rumeur au 10/11

Rien de neuf depuis l'entrée du 10/11 ci-dessus : le teaser du **06/11** (« The becoming begins ») n'a ni nommé Qwen 4 ni donné de date, d'accès API ou de poids téléchargeable. Un participant à la conférence Alibaba du 29/10 rapporte qu'une sortie « la semaine suivante » aurait été évoquée par le CTO — toujours de seconde main, non officiel. Aucun checkpoint Qwen 4 sur Hugging Face à ce jour. **La vidéo du jeudi 12/11 parle bien de l'attente (cartes graphiques à acheter avant la sortie), pas d'une sortie confirmée** : le script reste correct en l'état. Sources : [emergent.sh](https://emergent.sh/news/alibaba-teases-qwen4-lineup-apsara-due-next), [af.net](https://af.net/realtime/alibaba-teaser-sparks-qwen-4-speculation-as-release-date-and-checkpoints-remain-unverified/).

### Les 4 créneaux à remplir (jeu. 17/12, lun. 21/12, jeu. 24/12, jeu. 31/12)

Aucun doublon avec la grille déjà posée. Toutes calculées (sources, prix relevés, pas d'essai), dans la règle 2×/semaine IA jusqu'au 4/01.

| Créneau | Vidéo proposée | /40 | Justification |
|---|---|---|---|
| **Jeu. 17/12** | **Le Black Friday a-t-il vraiment fait baisser les prix de l'IA en local ?** (bilan prix, GPU et RAM) | **33/40** (demande 8 · clic 8 · production 8 · niche 9) | Contre-pied vérifiable : en 2026 les prix de la DRAM/GDDR/NAND montent d'environ 20 %/trimestre, donc le Black Friday (27/11) n'a pas vraiment baissé le prix des cartes et de la RAM pour l'IA locale (sources : [runaihome.com](https://runaihome.com/blog/black-friday-2026-local-ai-hardware-buy-now-or-wait/), [tomsguide.com](https://www.tomsguide.com/computing/gpus/gpu-price-hikes-are-coming-in-2026-so-now-is-the-best-time-to-buy-ive-found-the-best-deals-for-you-to-get-ahead-of-it)) ; sert les acheteurs avant Noël, aucun équivalent français trouvé, et relie Claude #1, 32 Go de VRAM et Louer/acheter |
| **Lun. 21/12** | **Combien coûte Kimi K3.1 Pro chez toi ?** (série « combien coûte [modèle] ») | **31/40** (demande 7 · clic 7 · production 8 · niche 9) | Kimi K3.1 Pro est sorti sur Hugging Face vers le **05/11/2026** et grimperait en tête des classements selon les premiers retours ; la série a déjà marché 2 fois (Coût Claude, DeepSeek V4.1 Flash), méthode éprouvée, pas de nouvel essai |
| **Jeu. 24/12** (veille de Noël) | **Le cadeau IA locale : quel budget pour s'offrir une machine qui tourne sans le cloud** | **34/40** (demande 8 · clic 8 · production 9 · niche 9) | Intemporel et cadeau, comme demandé : synthétise les calculs déjà faits (Mac mini, 32 Go de VRAM, Louer/acheter) en guide d'achat de fin d'année ; aucune actu à vérifier, production très légère (montage de sources existantes) |
| **Jeu. 31/12** (veille du Nouvel An) | **Résolution 2027 : ce que coûte vraiment de quitter le cloud pour de bon** | **32/40** (demande 7 · clic 8 · production 9 · niche 8) | Thème « résolution de janvier » (quitter les abonnements), intemporel ; referme la série « Abonnement ou IA locale ? » avant l'épisode #2 du 4/01, recycle les chiffres déjà vérifiés de Coût Claude et DeepSeek V4.1 Flash |

**2 remplaçants** (si un sujet ci-dessus doit bouger, ou en réserve pour un futur créneau radar) :

| Remplaçant | /40 | Justification |
|---|---|---|
| **L'IA cachée dans ta carte graphique** (NPU, Tensor Cores : ce qu'ils changent vraiment pour toi) — reprend l'idée mise de côté dans `strategie.md` | **30/40** (demande 6 · clic 7 · production 8 · niche 9) | Intemporel, calculé (specs publiées), complète la série matériel sans répéter VRAM/Mac mini |
| **Combien coûte GLM-5.3 chez toi ?** (2e itération de la série « combien coûte », si Kimi K3.1 Pro est pris pour un autre créneau) | **29/40** (demande 6 · clic 7 · production 8 · niche 8) | GLM-5.3 (Z.ai) est cité en tête des classements open source de novembre 2026 ; méthode déjà rodée, risque de production le plus faible de tous les candidats |

**DeepSeek Super-Agent dans ces créneaux ?** Non : voir le verdict ci-dessus (22/40, sous le seuil). Il ne mérite aucun des 4 créneaux ni les remplaçants.

---

## 05/11/2026 : bilan d'Uber, de l'IA locale et d'OpenCode (captures de Studio)

| | IA locale (2/11) | Uber (26/10) | OpenCode (21/10) | ArtCraft (19/10) |
|---|---|---|---|---|
| Vues | 195-209 | 221 | 479 | 608 |
| Impressions | 1,3 K | 4,4 K | 2,3 K | 10,5 K (21/10) |
| CTR | 2,0 % | 1,3 % | **4,2 %** | 0,9 % |
| % regardé | **41,2 %** (3:53) | 26,8 % (2:41) | 21,3 % (1:50) | 28 % |
| Rétention 0:15 / 1:00 (courbe) | ~70 % / **~50 %** | ~65 % / ~45 % | ~65 % / ~35 % | 66 % / 47 % |
| Commentaires | **7** | 0 | 1 | 1 |
| Part des suggestions | 8,6 % | 24 % | 4,2 % (Accueil 79 %) | 98 % |

- **IA locale** : le meilleur contenu de la chaîne (1:00 à 50 %, remontée entre 1:00 et 2:00, plateau à 50 % jusqu'à 3:30). Elle pèche par le clic.
- **Uber** : YouTube l'a beaucoup montrée, mais personne n'a cliqué. Le titre est trop abstrait. **On la laisse tomber** (décision du 05/11) et on optimise les vidéos suivantes.
- **OpenCode** : le drame fait cliquer, mais le contenu ne tient pas la promesse (plateau à 15 %).
- **Suggestions** : les vidéos qui nous suggèrent n'ont rien à voir avec nous (JDG, trading, foot, Edenred…). YouTube n'a pas encore classé le nouveau format.

**Décision (05/11)** : 3 vidéos « IA chez moi » pour 1 vidéo « histoire / génie ». La règle « pas deux fois le même pilier de suite » tombe. La prochaine vidéo est une vidéo IA locale : elle garde le fond de la vidéo d'installation et l'emballage d'OpenCode (enjeu, question, verdict), et vise 75 % à 0:15.

**Ajout du 05/11 (recherche sur le web ; `vidiq_outliers` indisponible dans cette session)** :
- **DeepSeek Super-Agent** (`dsh-superagent`, MIT, 31/10) : un prototype de recherche, un agent de code pour les équipes qui lit les discussions Feishu, sans benchmark publié. Trois grosses chaînes françaises l'ont déjà traité (selon l'auteur), et ce n'est pas de l'IA locale pour notre public. **On ne le fait pas.**
- **Higgsfield contre ComfyUI** (fin octobre) : un concours à environ 25 K$ pour recréer Higgsfield en open source, suivi d'une mise en demeure sous 48 h. La vidéo envoyée par l'auteur (`znrYe8yVQ_Q`, en anglais, 85 K vues, 3/11) en parle. C'est un bon récit « open source contre géant », mais sur la vidéo IA, pas les LLM locaux. **Candidat pour un créneau histoire** (15 févr.), pas pour un créneau proche.
- Calendrier : Claude #1 (« 16 Go suffisent », avec Strata) passe au 9 nov., « nom d'un modèle » au 16 nov.

## 23/10/2026 : radar des idées (le 8 mars, à la place de Mobile Money)

Pas une sortie de vidéo : l'auteur a abandonné Mobile Money (« je n'aime pas l'idée ») et llama.cpp a pris son créneau du 8 févr. Il fallait une vidéo pour le 8 mars, entre deux créneaux IA, donc **génie ou histoire**. Environ 15 appels vidIQ.

### Signaux
- **Génie, en anglais** (chaînes de la liste et voisines, 6 mois) :
  - Enrico Tartarotti : *The Insane Design Of Messaging* (1,7 M, ×17), *The LIES That Make Hardware ACTUALLY Work* (793 K, ×7,1), *The Ridiculous Engineering Of Animations* (288 K en 5 jours, pour l'iPhone du 7 déc.) et *…Of Text* (302 K) ;
  - ByteMonk : SQLite (221 K, ×12) ;
  - Hussein Nasser : Postgres (235 K, ×14) ;
  - Low Level : *I Tested The Viral Reverse Engineering Repo* (3,1 M, ×9,1).
- **Objets du quotidien** :
  - PawelCodeStuff, *The Most Overengineered Part of Your iPhone* (Face ID, 713 K, ×32, 15/10) ;
  - History of Simple Things, *How Do QR Codes Work?* (1,35 M, ×113) ;
  - Factron Process, câbles sous-marins (509 K, ×162).
- **Jeux en ligne** :
  - DeadInSperanza, *Hidden Players: Why Don't Servers Just Hide Enemies?* (52 K, ×108, 13/10) ;
  - Outscal, lag (38 K, ×35) ;
  - Tariq10x (297 K) ;
  - Surnex, *Once you see this, You'll see Competitive Games Differently* (2,5 M, ×356).
  - **Aucune vidéo française** sur le netcode.
- **En français** :
  - V2F (overfl0w), *Ce que tes yeux ne voient pas dans un QR Code* (214 K, sept. 2026) : l'angle du QR code est pris ;
  - Face ID : seulement Micode (2017, 428 K) et des tutos de dépannage.
- **Mots-clés** :
  - « how qr codes work » : 19,6 K par mois, +129 % ;
  - « lag jeux en ligne » et « câble sous-marin internet » : moins de 750 par mois en France ;
  - « shazam » est pollué par le film.

### Décision
- **Lun. 8/03 : *Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne*** ([fiche](../archive/lag/fiche.md)), choisie par l'auteur. 32/40 (demande 7 · clic 9 · production 7 · niche 9). C'est un sujet d'accueil, pour un public de 18-24 ans joueurs, et il n'existe pas en français.
- **En réserve** (`idees.md`) :
  - Face ID (32/40), à garder loin de l'iPhone du 7 déc. ;
  - le QR code (30/40), seulement quand la vidéo de V2F ne circulera plus ;
  - le jour où l'Afrique de l'Ouest a perdu internet (29/40), à envisager pour le 14 mars 2027 (3 ans).

---

## 21/10/2026 : sortie d'OpenCode (radar n° 1)

### Notre chaîne
- **2 610 abonnés**, +20 en 30 jours ; ~3 200 vues en 30 jours (169 312 au total).
- **ArtCraft** (19/10) : 285 vues à J+2. CTR de 0,9 % pour 10,5 K impressions, dont 98 % viennent des suggestions (relevé Studio du 21/10). Sous les 3 %, le guide de l'algorithme dit qu'il faut corriger : tes 3 miniatures memes (Toy Story, Clawd, Solo Leveling) sont là pour ça.
- **OpenCode** (21/10, 13 h) : 3 vues à H+2.
- **Uber** est en ligne en privé, avec un titre à corriger (« L'hisoire du temps réel derriere uber ») et les **tags Flutter par défaut**. Il faut les remplacer avant le 26/10 ; le kit d'upload n'existe pas encore.
- Les statistiques par vidéo (`vidiq_channel_analytics`) sont vides pour ces trois jours : l'API a du retard. À reprendre au prochain radar.

### Concurrents
- **Kai** : 49 400 abonnés, **+11 400 en 7 jours**, 8 vidéos. Ses meilleures vidéos du mois parlent toutes de matériel : « Every Ways to Get 128GB VRAM… » (821 K), « Don't Buy a Mac Mini For Local AI » (409 K), « Is 16GB All You Need… » (386 K), « Can a Mac Mini Replace your $200 AI Subscription? » (316 K), « Don't Buy a GPU Instead Build This 32GB Free AI Server » (258 K).
- **Morgans Code** : 2 020 abonnés (+240 en 7 jours). « Is $1,500 All You Need to Run DeepSeek V4.1 Flash? » : 17,7 K en un jour. « Qwen 4 27B: What to Expect » : 22,2 K. Étude complète : [`morganscode.md`](morganscode.md).
- **Thibaut Dcode** : « L'effrayante vérité sur l'empire WhatsApp » a 204 K vues (×0,6). Sur sa chaîne, c'est sous la moyenne.
- **Makertronic Tech** (5 900 abonnés, chaîne en pleine montée) : « NVIDIA sous le CHOC : la RX 10700 XT détruit la RTX 5080 ! » (35 K, ×2,6) ; « 512 Go pour l'IA : la Chine veut casser les prix ! » (17,9 K en 2 jours).
- **Baptiste Simard** : « J'ai cloné une application payante avec Claude Code (Fin du SAAS ?) » (36,5 K, ×6,7) ; « 11 repos GitHub indispensables à brancher sur Claude Code » (29,3 K en 4 jours).

### Public français
- **IA en local** : « Adieu le cloud pour les LLM ! Vive le local » (Le Lab IA, 47,8 K, ×24) ; « Gérer HomeAssistant avec une IA 100 % gratuite » (Bricolo2.0, 25,9 K, ×31) ; « L'IA sur CPU et sans GPU, avec Openvino » (Le Lab IA, 26,6 K, ×9,1).
- **« Comment ça marche » sur l'IA** : « L'IA laisse une trace invisible dans vos textes. Voici comment ça marche » (Machine Learning Lab, 2 200 abonnés, **177,8 K, ×539**) ; « 10 termes IA que tout le monde utilise sans vraiment les comprendre » (même chaîne, ×59).
- **Smartphones** : « J'ai tenté d'utiliser le plus vieil iPhone encore à jour » (Nightech, 166,9 K en 3 jours).
- Aucune vidéo française en format « combien ça coûte en local » ni « même carte, plus rapide ».

### Décision
- **Lun. 2/11 : « Combien coûte Claude en local ? »** (avancée du 4 janvier). C'est le format qui marche le mieux chez Kai (4 de ses plus gros succès) et que Morgans vient de refaire avec DeepSeek V4.1 Flash. Il n'existe pas en français, et il se produit sans gros essais. Le calcul part de DeepSeek V4.1 Flash, le modèle ouvert au niveau d'Opus 5 en code d'après le tableau de DeepSeek (à revérifier à la source).
- **Lun. 16/11 : Claude ou mon PC ? #1 (16 Go)**, avancée d'une semaine : 11 jours avant le Black Friday au lieu de 4. Kai « Is 16GB All You Need… » en est à 386 K.
- **À surveiller** :
  - la sortie de **Qwen 4 27B** : si elle tient dans 16 Go, c'est un épisode testé pour un créneau IA ;
  - le thème **« même carte, plus rapide »** (idée 16), le meilleur de Morgans, testable sur ta 5080 ;
  - le CTR d'ArtCraft après le changement de miniature.
- **Modifié le 22/10 au soir, par l'auteur** : les deux vidéos IA sont inversées. Claude #1 sort le 2/11 (essais sur la 5080 les 23-24/10) et Coût Claude le 16/11, pour réutiliser ces mesures.
