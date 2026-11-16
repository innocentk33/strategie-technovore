# Sources : DeepSeek sans GPU

Recherche du 16/11/2026. ✅ Source primaire ouverte puis rouverte ; ⚠️ mesure unique ou calcul ; ❌ non établi. Aucun essai personnel. Le résultat CPU concerne V4-Flash-0731, pas V4.1.

| ID | Fait et limite | Source exacte et contrôle |
|---|---|---|
| F1 | Checkpoint aligné MaxQ-Fractal : 56,93 GiB, 61 129 364 160 octets, environ 61,13 Go décimaux, 284,33 milliards de paramètres. | https://github.com/synchopate/llama-modchip/blob/main/docs/DEEPSEEK_V4_OPTIMIZATIONS.md ; https://huggingface.co/Synchopate/DeepSeek-V4-Flash-0731-MaxQ-Fractal-64GB-CPU-GGUF · ✅ Les deux sources ont été rouvertes le 16/11. Écart de 192 octets entre notes de version et document, sans incidence sur la taille arrondie. |
| F2 | Ryzen 9 9955HX, 64 Go DDR5, aucun GPU : génération pure à 8,66–9,06 tokens/s ; préremplissage froid à 36,11–43,98 et chaud à 44,36 tokens/s. Mesure du projet, version 2.5.5. | https://github.com/synchopate/llama-modchip/blob/main/README.md · ⚠️ README ouvert puis rouvert le 16/11 ; une équipe, aucune réplication indépendante. |
| F3 | Perplexité MaxQ : 7,2977 ± 0,0504 contre 4,5381 pour la référence sur wiki-alt, 51 blocs. Calcul : +60,8096 %. Cela ne signifie pas 60,8 % de mauvaises réponses. | Document d’optimisation cité en F1 · ⚠️ Document F1 relu ; protocole propre, aucun benchmark universel. |
| F4 | Mélange d’experts : 13,17 milliards de paramètres actifs par token pour environ 284 milliards au total. Les poids inactifs restent stockés. | README cité en F2 · ✅ README F2 relu ; aucune vitesse transférée à tout CPU. |
| F5 | Kit DIMM de bureau G.Skill Aegis 5, 64 Go, 2 × 32, DDR5-6000 CL36 : 1 299,95 € TTC. Délai annoncé de 7 à 15 jours, date affichée du 26/11. | https://www.ldlc.com/fiche/PB00669811.html · ✅ Fiche ouverte puis rouverte le 16/11. |
| F6 | Kit DIMM de bureau Corsair RGB, 96 Go, 2 × 48, DDR5-6000 CL36 : 1 723,95 € TTC. Délai de 7 jours, date affichée du 20/11. | https://www.ldlc.com/fiche/PB00707401.html · ✅ Fiche ouverte puis rouverte le 16/11. |
| F7 | Kit DIMM de bureau Corsair RGB, 128 Go, 2 × 64, DDR5-6000 CL40 : 2 879,95 € TTC, en rupture. Prix affiché, aucune disponibilité garantie. | https://www.ldlc.com/fiche/PB00712975.html · ✅ Fiche ouverte puis rouverte le 16/11. |
| F8 | Parité : 1 € = 655,957 FCFA. Conversions de F5–F7 : environ 852 711, 1 130 837 et 1 889 123 FCFA. Ce sont des conversions, pas des prix locaux livrés. | https://www.bceao.int/fr/content/histoire-du-franc-cfa · ✅ Source ouverte puis rouverte le 16/11 ; conversions calculées. |
| F9 | L’API actuelle deepseek-flash sert V4.1-Flash-1017 ; les anciens noms V4 sont redirigés. Par million de tokens : entrée sans cache 0,15 $ / 0,30 $, sortie 0,60 $ / 1,20 $ en heures creuses / pointe. | https://api-docs.deepseek.com/quick_start/pricing/ · ✅ Page ouverte puis rouverte le 16/11 après un premier délai dépassé sur l’adresse sans barre finale ; TVA et change non établis. |
| F10 | Exemple hypothétique : 1 million de tokens en entrée sans cache et 1 million en sortie coûtent 0,75 $ en heures creuses ou 1,50 $ en pointe, hors outils, taxes et change. Le modèle diffère du fichier CPU. | Calcul à partir de F9 · ⚠️ Calcul de F9 ; aucune facture mesurée. |
| F11 | Non validés précisément : 1,71 bit par poids, deux réplications indépendantes, échelle Atomic de 79–144 Go et valeurs de 21 % / 0,2 %. Ces affirmations sont retirées du script ; aucun score n’est inventé pour 96 ou 128 Go. | fiche.md fournie · ❌ Pistes de la fiche fournie, recherche primaire bornée. |
| F12 | Les kits DIMM de bureau ne sont pas ceux du portable du test et ne décrivent pas son prix complet. Le projet cite un fichier UD-IQ1_S de 76,87 GiB, environ 82,5 Go ; aucune qualité ou vitesse comparable des autres paliers n’est établie. | F2 et fiches F5–F7 · ⚠️ README F2 et fiches F5–F7. |

## Journal de double vérification

Le document d’optimisation et Hugging Face ont été rouverts : unités Go/GiB et version V4/V4.1 corrigées. Les fiches RAM individuelles ont été rouvertes, avec délais et ruptures conservés. Les anciennes pistes Crucial 64 Go et Kingston 128 Go étaient en fin de vente ; le Corsair 96 Go sans RGB à 1 689,95 € était également en rupture et a été exclu des offres disponibles.

L’API a été lue deux fois après le premier échec ; le service actuel reste distinct du fichier local. Le taux BCEAO a été relu. La génération pure est séparée du préremplissage et de PVS ; aucun débit général de 25 tokens/s n’est promis. Les prix du 3 décembre demandent une actualisation : [PRIX À RELEVER]. Aucun prix local africain, tarif d’abonnement TTC ou seuil de rentabilité en euros n’est établi ; le calcul API reste en dollars.
