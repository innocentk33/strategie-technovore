# Sources : RAM, VRAM et mémoire unifiée

Recherche et double lecture réelle le **16/11/2026**. Vidéo documentaire prévue le 31/12. Les chiffres Strata proviennent exclusivement du dossier fourni `../strata-test/sources.md` ; leurs pages primaires ont été rouvertes pour contrôler les lignes utiles. Aucun nouveau test demandé.

| Fait | Information et limite | Source datée | Statut / seconde vérification |
|---|---|---|---|
| F1 | Barrette DDR5-5600, bus de données 64 bits. Hypothèse de deux canaux 64 bits à 5600 MT/s :5600×8×2=89600 Mo/s=89,6 Go/s théoriques. La capacité 64 Go ne fixe pas ce débit. | https://www.kingston.com/datasheets/KF556C40BW-16.pdf (fiche 2023,consultée 16/11) | ✅ fiche ouverte puis rouverte ;⚠️double canal et débit calculés,non mesurés, vitesse XMP non garantie sur tout PC. |
| F2 | RTX5080 :16 GoGDDR7,960 Go/s. Le débit constructeur n'est pas un benchmark LLM. | https://www.nvidia.com/en-us/geforce/graphics-cards/compare/ (16/11) | ✅ page ouverte puis rouverte,série 50,colonnes 5080etbande passante. |
| F3 | Mac miniM5Pro :307 Go/s,configurable 48/64 Go ;M6 :153 ou 170 Go/s selon configuration. | https://www.apple.com/fr/mac-mini/specs/ (16/11) | ✅ ouverte puis rouverte ; ne pas attribuer 307 àtoutMac mini. Mémoire partagée par système et applis. |
| F4 | Exemple pédagogique dense : lire 17 Go de poids par token avec 89,6 Go/s donnerait~5,27 token/s au mieux dans ce modèle simplifié ;960/17≈56,47. Hypothèses :une conversation,lecture complète,aucun autre coût,bande passante pleinement utilisée. | CalculF1/F2 ;17 Go taille arrondie d'exemple, pas artefact commercial précis | ⚠️ plafond de modèle mémoire, pas une prédiction mesurée ni plafond avec spéculation/batching. Les 17 Go ne sont pas censés tenir sur 5080sans marge. |
| F5 | Mesure d'un testeur sur 4070SUPER12 Go+i 5-13500+48 GoDDR5 :Q4_K_XL partiellement en RAM12,58–13,74 tok/s ;IQ2_XXS entièrement GPU42,44–42,47 tok/s. Quantification et spéculation changent aussi ;aucune causalité «RAM seule» isolée. | https://github.com/xenodeve/Qwen-3.8-27B-Tuning/blob/main/docs/reports/MASTER-REPORT-2026-08-19.md (rapport 19/08/2026) | ⚠️ primaire unique,ouverte puis rouverte. Pas de calcul d'une pénalité universelle 71%. |
| F6 | Strata Coder sur 5070Ti 16 Gio+31,2 GioRAM,02/11 :70,4 tok/s médian en chat court,60,5–95,7 ;réflexion coupée, température 0, 3 exécutions. Pas de contrôle de justesse. | DossierStrataT7 ;https://github.com/Niko1221/Strata/issues/4997 | ⚠️ source primaire utilisateur,ouverte puis rouverte ;lecture du prompt distincte :2534,5 tok/s sur 4019 tokens. Ne pas l'assimiler à génération. |
| F7 | Strata place des experts sur GPU et RAM,avec calcul CPU des experts horsGPU ;table n-gram surSSD. Modes résident/mappé distincts. | DossierT8/T25 ;https://github.com/Niko1221/Strata/blob/main/docs/DETAILS.md (état 16/11) | ✅ documentation du projet ouverte puis rouverte,How it works ;affirmation du projet,aucun débit disque extrapolé. |
| F8 | Les archives auteur rapportent 30,8/31 GoRAM et 165–183 Mo/s disque pendantdragon ;ce trafic ne prouvepas à lui seul du swap ou des experts tous sur SSD. | `../strata-test/sources.md` T45 (relevés 13–14/11) | ✅ fichierfourni relu ;⚠️rushes Windows non ouverts ici. Aucune nouvelle demande. Chiffres non utilisés dans la voix pour préserver format strictement documentaire. |
| F9 | Un MoE n’active qu’une partie des poids par token ;nombre total de paramètres etpoids actifs différents. ExempleFlash-Next 125B/6B vient du dossierT25/T47. | `../strata-test/sources.md` T25/T47,12–14/11 ;docF7 | ✅ fourni et explication primaireF7 ; ne pas déduire la VRAM nécessaire du seul 6B. |

## Deuxième lecture et corrections

F1,F2,F3,F5,F6,F7 ont été **ouverts puis rouverts**. F8/F9 sont des faits fournis identifiés, pas de nouvelles mesures. Les calculsF1/F4 ont été refaits séparément :89,6/17=5,2706 ;960/17=56,4706.

- La RAM plus grande ne devient pas automatiquement aussi rapide que laVRAM. La comparaison d'une capacité et d'un débit est retirée.
- L'exemple «bande passante/taille» est une estimation dans un scénario précis ;MTP,batching,cache,calcul etarchitecture en changent la lecture.
- Strata :on ne dit pas «tout le modèle passe par le SSD» à partir du traficdisque. La table n-gram en lit légitimement.
- Le contraste dense/MoE dépend aussi du moteur,du routage etdes experts utiles. Pas de classement universel à partir de deux modèles différents.
- Aucun prix RAM comparatif n'est utilisé faute d’offre TTC exacte vérifiée ;renvoi à la vidéo DeepSeek pour les paliers de coût. Pas de prix inféré d'une ancienne vidéo.

Requêtes :`site:kingston.com DDR5 5600 MT/s 64 bit bandwidth` ;`site:github.com "Qwen 3.8-27B" "CPU" "tok/s" RAM`. PageAMD395 devinée 404,aucun chiffre repris. Périmètre assumé :explication etchoixparprofil, pas classement de performances pour toutes les machines.

### F10 — Identité du Coder du résultat initial

Dossier fourni `../strata-test/sources.md`, T6/T7, relu pour le contrôle final 16/11 : **Coder IQ1_M expérimental**,256 experts conservés sur 512 par couche, choix spécialisé. URL primaire consignée dans le dossier : https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF . Il s’agit de la réutilisation du dossier déjà doublement vérifié, pas d’une nouvelle ouverture revendiquée ici. F6 reprend le même CoderIQ1_M ; conserver logiciel 0.1.55/moteur 0.1.54, Ryzen 7 9700X etabsence de contrôle de justesse avec 70,4t/s. Le processeur calcule les experts horsGPU ; la RAM les stocke. Aucun score de qualité n’est ajouté au script.
