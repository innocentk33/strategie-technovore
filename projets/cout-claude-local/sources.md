# Combien coûte Claude en local ? : sources

> Tout a été relevé le **22/10/2026** (date de consultation de chaque source, sauf mention contraire). Les numéros `[S…]` sont ceux du [`brouillon-v1.md`](brouillon-v1.md).
> **Aucun chiffre de Kai ni de Morgans Code n'est repris.** Les études `etudes/kai.md` et `etudes/morganscode.md` n'ont servi qu'à la structure du script ; tous les chiffres viennent de fiches de modèles, de pages d'éditeurs, de boutiques ou d'API publiques.
> Légende : **Confirmé** = lu à la source primaire ; **Presse** = source secondaire ; **Calcul** = fait par nous à partir de sources ; **⚠️** = à vérifier avant le tournage.

---

## 1. Claude (Anthropic)

### [S1] Vue d'ensemble des modèles
- URL : https://platform.claude.com/docs/en/models/overview
- Confirmé le 22/10/2026 :
  - lignée actuelle : Claude **Fable 5.1** (10 $ / 50 $ par million de tokens, entrée / sortie), **Opus 5.5** (4 $ / 20 $), Sonnet 5.5 (2 $ / 10 $), Haiku 5.5 (dès 0,10 $ / 0,50 $) ;
  - la page recommande de commencer par Opus 5.5 et de réserver Fable 5.1 aux raisonnements les plus exigeants ;
  - la page ne donne **aucun nombre de paramètres** pour aucun modèle.
- Fable 5.1 est donc le modèle le plus puissant de la gamme, Opus 5.5 le modèle recommandé par défaut. Le titre de la vidéo (« Opus 5.5 ») suit la fiche et la recommandation d'Anthropic.

### [S2] Fiche d'Opus 5.5
- URL : https://platform.claude.com/docs/en/models/opus-5-5/overview
- Confirmé le 22/10/2026 : « Latest. Released September 22, 2026. » ; contexte 1 M tokens ; sortie max 128 K ; **entrée 4 $ / sortie 20 $ par million de tokens** ; aucune mention de nombre de paramètres ni de poids.
- ⚠️ à vérifier : la *system card* d'Opus 5.5 (https://www.anthropic.com/claude-opus-5-5-system-card) n'a pas été lue. Le constat « Anthropic ne publie pas la taille » repose sur les deux pages ci-dessus et sur l'absence de poids publics.

---

## 2. Le modèle ouvert de référence : DeepSeek V4.1 Flash

### Choix et raison
- **DeepSeek V4.1 Flash** (candidat de la fiche, confirmé).
- Raison : sa fiche officielle le compare à **Claude Opus 5**, la génération juste avant Opus 5.5, avec des résultats mêlés (voir le tableau). C'est la comparaison la plus récente qu'un éditeur de modèle ouvert publie contre Opus.
- **Kimi K3 n'est pas retenu comme référence**, malgré son score : sa fiche compare à Claude Fable 5 et Opus 4.8, pas à Opus 5 ou 5.5, et ses fichiers pèsent 1,56 To, hors de portée de tout palier sauf le dernier. Il sert de dernier palier de la vidéo (voir S13). Ce n'est pas le choix de Kai : on garde un modèle dont la taille rend le calcul discutable pour un particulier.

### [S3] Fiche Hugging Face de DeepSeek-V4.1-Flash
- URL : https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash
- Confirmé le 22/10/2026 :
  - **552 milliards de paramètres « backbone »** ; modèle à experts, multimodal ; licence **MIT** ; contexte 1 M tokens ;
  - **8 milliards de paramètres actifs par token à la lecture (prefill), 16 milliards à l'écriture (decode)** ;
  - 384 experts routés + 1 partagé, 6 experts routés actifs par token (fichier `config.json` du dépôt) ;
  - mémoire « Engram » : « Engram conditional memory (196B parameters, sparsely accessed via token-based lookup) » ;
  - cache KV global : « about 890 bytes per token », environ un quart de DeepSeek-V4-Flash ;
  - métadonnées Hugging Face : 763 milliards de paramètres au total ;
  - somme des fichiers `.safetensors` du dépôt (API Hugging Face, 48 fichiers) : **510,3 Go** ; dépôt créé le 10/09/2026, modifié le 16/10/2026.
- Tableau de la fiche (« Opus-5.0, max reasoning effort » contre « DS-V4.1-Flash », **chiffres du constructeur**) :

| Test | Opus 5.0 | DeepSeek V4.1 Flash |
|---|---|---|
| Terminal-Bench 2.1 | 89,1 | **90,6** |
| DeepSWE v1.1 | 74,0 | **74,2** |
| Terminal-Bench 4.0 | **51,8** | 31,2 |
| HLE (Humanity's Last Exam) | **56,3** | 36,8 |
| NL2Repo-Bench | **75,3** | 64,0 |
| GPQA Diamond | **93,4** | 90,9 |

- ⚠️ à vérifier :
  - la fiche étiquette la colonne « Opus-5.0 » sans écrire « Claude » ; je l'interprète comme Claude Opus 5 (la fiche du modèle « 1017 » écrit « Opus 5 ») ;
  - la fiche précise que les résultats agentiques dépendent de réglages et d'échafaudages propres à chaque test ;
  - **aucun test indépendant** n'a été trouvé ; Opus 5.5 (sorti le 22/09) n'est pas dans le tableau ;
  - **552 + 196 = 748, pas 763** : l'écart d'une quinzaine de milliards (vision ?) n'est pas expliqué sur la fiche ;
  - le cache KV de 890 octets par token concerne le « cache global » ; le cache de fenêtre glissante s'ajoute (la fiche le dit proportionnellement, sans chiffre).

### [S4] DeepSeek-V4.1-Flash-1017 (mise à jour du 17/10/2026)
- URL : https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017
- Confirmé le 22/10/2026 : « minor update » de V4.1 Flash ; 763 milliards de paramètres dans les métadonnées (même total) ; fichiers `.safetensors` : **510,3 Go** (API Hugging Face) ; scores annoncés plus hauts, par exemple Terminal-Bench 4.0 : 42,3 contre 51,8 pour Opus 5 ; DeepSWE v1.1 : 77,0 contre 74,0.
- ⚠️ à vérifier : la fiche ne redonne pas le nombre de paramètres actifs ni le cache. Nous supposons ceux de V4.1 Flash (même architecture, « minor update »). La date de publication du 17/10 vient de la date de création du dépôt (2026-10-17).

---

## 3. Calcul de mémoire

### [S5] Fichiers de la communauté : projet « ds4 » (antirez)
- URLs :
  - https://huggingface.co/antirez/deepseek-v4.1-flash-gguf
  - https://github.com/antirez/ds4 et son fichier `docs/MODELS.md`
- Confirmé le 22/10/2026 (table V4.1 Flash de `docs/MODELS.md`) :

| Cible | Fichier total | Poids principaux (en mémoire) | Tables Engram (sur le disque) |
|---|---|---|---|
| `ds41f-q2` | 341 Gio | 152 Gio | 189 Gio |
| `ds41f-q4` | 483 Gio | 294 Gio | 189 Gio |

  - « Engram rows are read directly from the file as needed in every mode, never loaded as a resident table » ;
  - « Q4 needs SSD streaming or a 512 GB Mac » ; une 128 Go de Mac fait tourner Q2 avec le streaming SSD ; la pleine résidence a été testée sur un M3 Ultra 512 Go.
- Calcul (Gio × 1,0737 = Go) :
  - Q2 : 152 Gio = **163 Go** ; 163 × 8 ÷ 552 = **2,4 bits** par paramètre ;
  - Q4 : 294,15 Gio = **316 Go** ; 316 × 8 ÷ 552 = **4,6 bits** par paramètre ;
  - Engram : 189 Gio = **203 Go**.
  - Formule de base (paramètres × bits ÷ 8) : 552 × 2 = 1 104 Go (16 bits) ; 552 Go (8 bits) ; 276 Go (4 bits).
- Autres tailles relevées sur Hugging Face (somme des fichiers, API, 22/10/2026), pour le contexte seulement : NVIDIA `DeepSeek-V4.1-Flash-NVFP4` 429 Go ; `mlx-community/…-oQ4e-mtp` 432 Go ; Unsloth `UD-Q4_K_XL` 501 Go, `UD-IQ1_S` 233 Go, `UD-Q2_K_XL` 335 Go. Ces fichiers incluent les tables Engram.
- ⚠️ à vérifier : l'explication « les 510 Go du fichier officiel contiennent le dictionnaire Engram » est une déduction de ma part (la fiche ne la donne pas ; elle découle de S3 et S5).

### Octets lus par token (vitesse maximale)
- **Calcul** : 16 milliards de paramètres actifs (S3) × bits ÷ 8 :
  - Q2 : 16 × 2,4 ÷ 8 ≈ **4,7 Go** par token ;
  - Q4 : 16 × 4,6 ÷ 8 ≈ **9,2 Go** par token.
- Simplification : tous les paramètres actifs sont comptés en quantification moyenne ; les lectures dans Engram et la partie traitée en FP8 ne sont pas comptées. C'est un **plafond**, pas une prévision.

### [S9] Mesures publiées par le projet ds4
- URL : https://github.com/antirez/ds4/blob/main/docs/PERFORMANCE.md (lu via `raw.githubusercontent.com`)
- Confirmé le 22/10/2026, **Flash Q2** (le document ne nomme pas « V4.1 » et ne donne pas de date : « recorded baselines ») :

| Machine | Contexte | Écriture (tokens/s) |
|---|---|---|
| M5 Max, 128 Go | 2 048 | **39,35** |
| M5 Max, 128 Go | 65 536 | 27,64 |
| DGX Spark, 128 Go | 2 048 | **18,05** |
| DGX Spark, 128 Go | 65 536 | 13,84 |

- **Calcul de la « règle des 30 % »** (contexte 2 048) :
  - M5 Max : 614 ÷ 4,7 = 130 ; 39,35 ÷ 130 = **30 %** ;
  - DGX Spark : 273 ÷ 4,7 = 58 ; 18,05 ÷ 58 = **31 %**.
- Estimations appuyées sur la règle :
  - M5 Ultra, Q4 : 1 200 ÷ 9,2 = 130 ; × 0,3 ≈ **40 tokens/s** ;
  - PC avec RAM : 90 ÷ 4,7 = 19 ; × 0,3 ≈ **6 tokens/s**.
- ⚠️ à vérifier :
  - la règle repose sur **deux mesures**, en Q2, faites par un tiers à date inconnue ; elle n'est pas une loi ;
  - l'article de presse donne deux bandes passantes pour le M5 Max (460 ou 614 Go/s) ; je prends 614 en supposant la version haut de gamme, la configuration testée n'étant pas précisée ;
  - **la qualité des versions à 2 bits n'est mesurée nulle part** dans les sources trouvées ;
  - aucune mesure sur une RTX 5080 : le projet ne donne aucun chiffre CUDA hors DGX Spark. **Le 90 Go/s de la mémoire de bureau est une hypothèse** (deux canaux DDR5 à ~5 600 MT/s ; quatre barrettes peuvent obliger à descendre en fréquence) ;
  - la partie GPU (5080) accélérerait un peu l'attention : l'estimation de 6 tokens/s est probablement basse, mais je n'ai aucune mesure pour le dire.

### [S11] Bande passante du DGX Spark
- URL : https://www.nvidia.com/en-us/products/workstations/dgx-spark/
- Confirmé le 22/10/2026 : « Memory Bandwidth: 273 GB/s » ; 128 Go de mémoire unifiée.

---

## 4. Matériel et prix en euros

### [S6] RTX 5080 : fiche NVIDIA France
- URL : https://www.nvidia.com/fr-fr/geforce/graphics-cards/50-series/rtx-5080/
- Confirmé le 22/10/2026 : **16 Go de GDDR7**, interface 256 bits, puissance graphique totale (TGP) **360 W**, alimentation système requise 850 W.

### [S7] Prix de la RTX 5080 en France
- URL : https://www.comparateur-gamer.fr/prix/pny-rtx-5080-16gb-overclocked-triple-fan-751492794266
- Relevé : « prix mis à jour le 22/10/2026 à 20 h » ; PNY RTX 5080 16 Go Overclocked Triple Fan : **CDiscount 2 039,98 € (livraison comprise)**, InMac 2 236,02 €, Cybertek et Grosbill 2 249,90 €, en stock.
- Contexte : prix de lancement français 1 169-1 179 € en 2025 (presse). L'écart vient de la pénurie de mémoire, selon la presse d'août 2026 (Tech Insider) : non vérifiée à la source.
- ⚠️ à vérifier : un seul modèle relevé, sur un comparateur et non sur LDLC, Materiel.net ou Topachat (pages illisibles par mon outil). À reprendre à la main le jour du tournage.

### [S8] Prix de la RAM DDR5
- URL : https://www.achatmoinscher.com/comparateur-de-prix-Memoire-vive/ddr5-corsair-vengeance-rgb-192-go-4-x-48-go-5200-mhz-cas-38.html
- Relevé : DDR5-6000 **Corsair Vengeance RGB 64 Go (2 × 32 Go) : 839,00 €** (« 9 e-boutiques ») ; Crucial Pro 64 Go : 881,91 €. Le kit Corsair 192 Go (4 × 48 Go) n'est plus vendu chez Topachat (fiche « épuisé »).
- **Calcul** : 839 × 3 = 2 517 €, arrondi à « environ 2 500 € » pour 192 Go.
- ⚠️ à vérifier : date du relevé inconnue ; le triplement est une estimation (pas de kit 192 Go à un prix actuel trouvé) ; des offres de 192 Go citées par la presse allaient de 1 800 € (juin 2026) à plus de 3 000 € ; **la carte mère doit accepter quatre barrettes de 48 Go** (non vérifié).

- Complément du 22/10 (grill) :
  - LDLC, Corsair Vengeance DDR5 192 Go (4 × 48 Go, 5200 MHz) : plus vendu, **dernier prix 2 859 €** (https://www.ldlc.com/en/product/PB00545878.html) ;
  - Hardware Cooking, octobre 2026 : un kit de 32 Go de DDR5 dépasse 410 € (https://www.hardwarecooking.fr/prix-ddr5-nouvelle-hausse-kit-32-go-octobre-2026/) ;
  - overclocking.com : la DDR5 coûte 5,6 fois plus cher qu'en juillet 2025, d'après 3DCenter (https://overclocking.com/crise-memoires-ram-coute-5-6-fois-plus-cher-2026/).
  - Dans le script v2 : « au moins deux mille cinq cents euros ». Aucun kit de 192 Go à un prix actuel trouvé.

### [S5 bis] L'auteur de ds4
- https://github.com/antirez/ds4, consulté le 22/10/2026 : le README est signé « Salvatore », alias antirez, le créateur de Redis (Salvatore Sanfilippo). Le projet s'appelle **DwarfStar** : un petit moteur d'inférence pour quelques modèles ouverts sur du matériel grand public (Metal, CUDA, ROCm).

### [S10] Mac Studio M5 Ultra
- URLs :
  - https://www.apple.com/fr/mac-studio/specs/ (Apple)
  - https://lokan.fr/2026/08/26/mac-studio-m5-max-m5-ultra/ (presse, 26/08/2026)
  - https://www.blog-nouvelles-technologies.fr/379044/mac-studio-m5-max-ultra-apple/ (presse, 25/08/2026)
- Confirmé chez Apple le 22/10/2026 : M5 Ultra, jusqu'à **512 Go de mémoire unifiée**, **1,2 To/s** de bande passante ; la page d'achat propose 96 Go (M5 Ultra) en configuration visible.
- Presse : M5 Max à partir de **2 999 €** ; M5 Ultra à partir de **6 599 €** (96 Go, 1 To) ; une configuration M5 Ultra 256 Go + 16 To à **20 679 €** (lokan.fr) ; **prix du 512 Go « pas encore communiqué »**, disponibilité « fin octobre » ; premières livraisons du 22/09.
- ⚠️ à vérifier : **prix du M5 Ultra 512 Go**, à relever sur apple.com/fr à sa sortie ; les deux repères de prix viennent de la presse et non d'Apple ; une estimation de « 20 000 € » vue sur un site (quelllm.fr) n'a aucune source et n'est pas reprise.

### [S16] Consommation du Mac Studio
- URL : https://www.apple.com/fr/mac-studio/specs/
- Confirmé le 22/10/2026 : « Consommation maximale en continu : 480 W ».

### [S12] Location : OVHcloud, serveur à 8 H200
- URL de la page : https://www.ovhcloud.com/fr/public-cloud/prices/ (page dynamique : prix lu dans le catalogue public de l'API)
- Source lue : https://eu.api.ovh.com/1.0/order/catalog/public/cloud?ovhSubsidiary=FR (22/10/2026, taux de TVA 20 %).
- Confirmé : instance **`h200-1920`** : 8 GPU **H200 de 141 Go (HBM3e)**, 224 vCPU, 1 920 Go de RAM ; prix à la consommation **42,00 € de l'heure HT**. Autres références du catalogue : `h100-1520` (4 × H100 80 Go) à 11,20 €/h ; `h100-760` (2 × H100) à 5,60 €/h.
- **Calcul** :
  - 8 × 141 = **1 128 Go** de mémoire GPU, pour des fichiers de 510 Go (S3) ;
  - 42 € × 730 h (8 760 h ÷ 12) = **30 660 € HT par mois** ; × 1,2 = **36 792 € TTC** ;
  - 2 heures de test : 84 €.
- ⚠️ à vérifier : prix HT ; disponibilité réelle (stocks, région) non vérifiée ; l'instance 8 × H200 est la seule configuration OVHcloud où les 510 Go tiennent (4 × H100 = 320 Go ; pas de 8 × H100 chez eux), mais un 8 × H100 de 640 Go ailleurs (Scaleway le liste sans prix actuel) pourrait aussi convenir ; la phrase du hook dit « le serveur qu'il faut » : à nuancer en « le plus petit serveur de ce type que j'ai trouvé chez un hébergeur européen » si tu veux être strict ; **aucune mesure de vitesse** trouvée sur ce serveur.

### [S17] H200 : consommation
- URL : https://www.nvidia.com/en-us/data-center/h200/
- Confirmé le 22/10/2026 (« preliminary specifications ») : TDP jusqu'à **700 W** (configurable), 141 Go, 4,8 To/s.
- **Calcul** : 8 × 0,7 kW × 730 h = 4 088 kWh ; × 0,2001 = **818 €** par mois pour les cartes seules.

### [S13] Kimi K3
- URL : https://huggingface.co/moonshotai/Kimi-K3
- Confirmé le 22/10/2026 : **2,8 T de paramètres**, 104 milliards actifs par token, poids en MXFP4, licence « Kimi K3 License », contexte 1 M tokens ; somme des fichiers (API Hugging Face) : **1 561 Go**. Comparaisons de la fiche : Claude Fable 5 et Claude Opus 4.8 (pas Opus 5).

### [S14] Location : Scaleway, serveur à 8 B300
- URLs :
  - https://www.scaleway.com/en/pricing/gpu/ (page)
  - https://api.scaleway.com/instance/v1/zones/fr-par-2/products/servers (API publique, lue le 22/10/2026) et `/availability`
- Confirmé : **`B300-SXM-8-288G`** : 8 GPU B300 de 288 Gio chacun (2 304 Gio au total), 224 vCPU, 4 To de RAM ; **60,00 € de l'heure**, **43 800 € par mois** (730 h) ; disponibilité : « shortage ».
- Autres lignes lues : `H100-SXM-4-80G` 12,771 €/h ; `H100-SXM-2-80G` 6,62 €/h ; `H100-1-80G` 2,87 €/h.
- ⚠️ à vérifier : la devise n'est pas écrite dans l'API (j'ai pris l'euro, la page publique disant « Prices before tax » ; donc HT) ; pénurie constatée le 22/10.

---

## 5. Électricité en France

### [S15] Tarif réglementé de vente d'électricité (Tarif Bleu, option Base)
- URL : https://particulier.edf.fr/fr/accueil/electricite-gaz/tarif-bleu.html (EDF)
- Confirmé le 22/10/2026 : option **Base : 0,2001 € TTC le kWh** ; abonnement 6 kVA **15,86 € TTC par mois** ; mention « Prix applicable à compter du 1er août 2026 ».
- Recoupement (presse) : https://selectra.info/energie/actualites/marche/nouveaux-prix-electricite-tarif-bleu-1er-aout-2026 : 0,2001 € contre 0,1940 € avant (+ 3,1 %), qui cite la délibération de la CRE du 15 juillet 2026 ; prochaine hausse en février 2027.
- ⚠️ à vérifier : la mention de date de la page EDF suit le tableau « Tempo » ; la délibération de la CRE n'a pas été lue (le site renvoyait une erreur) ; la hausse de février 2027 vient de Selectra seul.
- **Calculs** (à 0,2001 €/kWh) :
  - Mac Studio, 480 W : 4 h/jour × 30 j = 57,6 kWh → **11,5 €** ; 24 h/24 : 345,6 kWh → **69 €** ;
  - PC avec la 5080, 600 W : 4 h/jour = 72 kWh → **14,4 €** ; 24 h/24 : 432 kWh → **86 €** ;
  - serveur 8 × H200 chez toi : voir S17.
- ⚠️ à vérifier : les **600 W du PC complet sont mon estimation** (5080 : 360 W de TGP, S6, plus le reste) ; les 480 W du Mac sont un maximum, pas une conso moyenne.
- Côte d'Ivoire / Cameroun (facultatif) : **non retenu, aucune source officielle trouvée**. Seuls des agrégateurs donnent des prix (≈ 80 à 95 FCFA/kWh) et la presse un ajustement de 10 % en 2024 ; pas de grille de la CIE ni de l'ANARE-CI. À ajouter si tu en trouves une.

---

## 6. Abonnement Claude et conversion

### [S18] Prix des abonnements Claude
- URL : https://claude.com/fr-fr/pricing
- Confirmé le 22/10/2026 : **Pro 17 $ par mois en facturation annuelle (200 $), 20 $ en mensuel** ; **Max à partir de 100 $ par mois** ; prix en dollars, hors taxes applicables.

### [S19] Taux de change
- URL : https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.en.html
- Confirmé : **1 € = 1,1205 $** (taux de référence de la BCE, 22/10/2026).
- **Calculs** :
  - Max : 100 ÷ 1,1205 = **89,2 €** ; Pro : 20 ÷ 1,1205 = **17,85 €** ;
  - 30 660 ÷ 89,2 ≈ **344** abonnements Max ; 30 660 ÷ 17,85 ≈ **1 718** abonnements Pro ;
  - seuil de rentabilité face à l'API : 30 660 € × 1,1205 = 34 355 $ ; ÷ 20 $ par million de tokens de sortie (S2) = **1 718 millions** de tokens ; ÷ (730 h × 3 600 s) = **654 tokens/s** en continu.
- ⚠️ à vérifier : le seuil ne compte que les tokens de sortie au tarif de base : il ignore les tokens d'entrée, le cache et la remise batch de 50 %. Il compare aussi le serveur à Opus 5.5 alors que le modèle ouvert ne le vaut pas partout (S3). Les prix des abonnements sont en dollars : le prix payé en France peut différer (TVA, conversion).

---

## 7. Récapitulatif des chiffres du script

| Chiffre dit dans la vidéo | Valeur | Source / type |
|---|---|---|
| Prix du hook | 30 660 € HT par mois (36 792 € TTC) | S12, calcul |
| Mémoire de la 5080 | 16 Go | S6 |
| Taille du modèle en mémoire | 163 Go (Q2) à 316 Go (Q4) ; fichiers officiels 510 Go | S3, S5, calcul |
| Paramètres | 552 milliards, 16 milliards actifs | S3 |
| Engram (sur le SSD) | 196 milliards de paramètres, environ 203 Go | S3, S5 |
| Cache KV | 890 octets par token, soit 0,89 Go pour un million de tokens | S3 (constructeur) |
| RTX 5080 | ≈ 2 040 € | S7 |
| RAM 192 Go | ≈ 2 500 € | S8, estimation |
| Vitesse 5080 + RAM | ≈ 6 tokens/s | estimation (règle des 30 %), non mesurée |
| Mac Studio | 512 Go, 1,2 To/s ; 96 Go : 6 599 € ; 256 Go + 16 To : 20 679 € ; 512 Go : prix non publié | S10 |
| Vitesse M5 Ultra Q4 | ≈ 40 tokens/s | estimation |
| Mesures citées | 39,35 tokens/s (M5 Max, Q2), 18,05 (DGX Spark, Q2) | S9 |
| OVHcloud 8 × H200 | 42 €/h HT ; 1 128 Go | S12 |
| Kimi K3 | 2,8 T de paramètres ; 1 561 Go ; Scaleway 8 × B300 : 60 €/h, 43 800 €/mois | S13, S14 |
| Électricité | 0,2001 €/kWh TTC (Base) | S15 |
| Abonnements | Pro 20 $ (≈ 17,85 € HT, ≈ 21 € TTC), Max 100 $ (≈ 89 € HT ; **107 € TTC**, ce que tu paies en France, 23/10) | S18, S19, toi |
| Seuil API | 1,7 milliard de tokens de sortie par mois, 654 tokens/s | S2, S19, calcul |

## 8. Liste des `⚠️ à vérifier` (à trancher avant le tournage)

1. **Prix du Mac Studio M5 Ultra 512 Go** : non publié par Apple ; à relever fin octobre.
2. **RAM 192 Go** : prix estimé par triplement d'un kit de 64 Go (date du relevé inconnue) ; compatibilité carte mère à 4 barrettes de 48 Go.
3. **Prix de la 5080** : un seul modèle, sur comparateur ; à refaire sur LDLC, Materiel.net ou Topachat.
4. **Écart 552 / 763 milliards de paramètres** : Engram = 196 milliards ; ~15 milliards restent inexpliqués (vision ?).
5. **Benchmarks DeepSeek** : chiffres du constructeur, contre Opus 5 et non Opus 5.5 ; colonne « Opus-5.0 » non étiquetée « Claude ».
6. **Paramètres actifs et cache de la version « 1017 »** : supposés identiques à V4.1 Flash.
7. **Règle des 30 %** : deux mesures, en Q2, par un tiers, date inconnue ; bande passante du M5 Max testé (614 Go/s) non confirmée.
8. **Qualité des quantifications à 2 bits** : aucune mesure trouvée.
9. **Vitesses estimées** (5080 + RAM ≈ 6 tokens/s ; M5 Ultra Q4 ≈ 40 tokens/s) : estimations, jamais mesurées sur ces machines ; 90 Go/s pour la RAM de bureau est une hypothèse.
10. **Serveur 8 × H200 OVHcloud** : prix HT lu dans le catalogue ; disponibilité non vérifiée ; aucune mesure de vitesse ; la formule « le serveur qu'il faut » du hook est à nuancer.
11. **Scaleway 8 × B300** : devise supposée en euros HT ; pénurie du jour.
12. **Cache KV** : 890 octets par token (chiffre de la fiche, cache global seulement).
13. **Électricité** : 600 W du PC complet estimés ; 480 W du Mac = maximum ; délibération de la CRE non lue ; hausse de février 2027 d'après Selectra seul.
14. **Seuil de rentabilité face à l'API** : tokens de sortie seulement, tarif de base.
15. **Taille d'Anthropic** : *system card* d'Opus 5.5 non lue ; l'absence de chiffre est constatée sur les pages de documentation.
16. **Question Reddit ou X** et les trois réponses : à relever à la main (aucune n'est inventée dans le script).
