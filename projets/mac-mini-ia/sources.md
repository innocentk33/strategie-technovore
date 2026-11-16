# Sources : Mac mini ou PC gamer

Recherche du 16/11/2026. Date du calendrier : 10/12/2026 ; la fiche mentionnait aussi une date provisoire de février, désormais obsolète. Aucun test personnel.

| ID | Fait et limite | Source exacte et contrôle |
|---|---|---|
| F1 | Apple : M6 de base à 153 Go/s ; options 24 ou 32 Go à 170 Go/s ; M5 Pro à 307 Go/s et jusqu’à 64 Go. La mémoire unifiée est partagée. | https://www.apple.com/fr/mac-mini/specs/ · ✅ Page ouverte puis rouverte : tableaux puce et mémoire. |
| F2 | INNO3D RTX 5080 X3 OC : 16 Go GDDR7, 960 Go/s de bande passante. | https://www.inno3d.com/product/inno3d-geforce-rtx-5080-x3-oc · ✅ Page ouverte puis rouverte : mémoire. |
| F3 | Mac mini M6, 32 Go / SSD 512 Go, référence MHQM4ZD/A-32GB : 1 709 € TTC affichés chez LDLC, délai supérieur à 15 jours. | https://www.ldlc.com/fiche/PB00751971.html · ✅ Fiche ouverte puis rouverte : prix et disponibilité. |
| F4 | Mac M6 32 Go, LM Studio, octobre 2026 : médiane de trois passages, raisonnement désactivé. Qwen 3.6-35B-A3B en MLX 4 bits : 63,2–68,8 tokens/s selon cinq prompts. Contexte demandé de 32 768, pas systématiquement respecté par MLX. | https://github.com/HDZucht/Mac-Mini-M6-LLM-benchmarks · ⚠️ Dépôt ouvert puis rouvert : matériel, protocole et résultats ; une campagne. |
| F5 | Même campagne : Qwen 3.8-27B Splash à 15,3–67,7 tokens/s selon prose, code et JSON ; texte général dense 27B/31B à 7–20. Aucun facteur cinq face à un PC mesuré. | Source F4 · ⚠️ Deux lectures de la source F4. |
| F6 | Autre auteur, Mac M6 32 Go, Qwen 27B en 4 bits, JSON, médiane de trois passages : 8,5 tokens/s avec llama.cpp sans spéculation, 69,3 avec Splash. Les fichiers diffèrent ; l’effet du moteur n’est pas isolé. Vidéo du 17/10, billet du 5/11/2026. | https://gitseonjeap.com/en/blog/engine-compare-splash-rapid-mlx-sushi · ⚠️ Billet ouvert puis rouvert. |
| F7 | Qwen 27B Q4_K_M : fichier d’environ 16,6 Go. Calculs distincts : 960 / 170 ≈ 5,65 pour la bande passante ; 170 / 16,6 ≈ 10,24 tokens/s pour un modèle naïf supposant une lecture complète des poids denses par token, sans autres coûts. Aucun plafond universel de génération. | https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main · ⚠️ Taille héritée de recherche-modele.md, sans nouvelle ouverture ici ; calculs explicites. |
| F8 | Le prix Apple Store d’une configuration 32 Go n’a pas été obtenu : page accessible mais prix dynamiques absents. Le prix de base de 1 049 € n’est pas comparé à une configuration 32 Go. | https://www.apple.com/fr/shop/buy-mac/mac-mini · ❌ Page ouverte puis rouverte, prix non extrait. |
| F9 | Page Claude avec pays FR : Pro à 20 $/mois et Max à 100 $/mois ; aucun prix TTC en euros validé. | https://claude.com/pricing?country=FR · ⚠️ Une ouverture le 16/11, sans réouverture avant rédaction ; tarif exclu des comparaisons en euros. |
| F10 | Scénarios hypothétiques d’économies : 1 709 / 20 € par mois = 85,45 mois ; 1 709 / 100 € par mois = 17,09 mois. Ce sont des économies supposées, pas des prix d’abonnement ni une équivalence fonctionnelle démontrée. | Calcul F3 · ⚠️ Calcul à partir de F3. |
| F11 | Historique fourni par la fiche : PC à 2 000 € et RTX 5080 à 1 100 € en 2025. Aucun prix actuel du PC complet établi. | fiche.md fournie · ⚠️ Fiche fournie, aucun relevé du jour. |
| F12 | Non établis : le modèle « refuse » la RTX 5080, ou le Mac est cinq fois plus lent. Aucun duel à fichier, prompt, cache et moteur identiques ; limite exacte de mémoire GPU sous macOS non validée. | Limites de la recherche · ❌ Promesse de fiche corrigée. |

## Journal de double vérification

Apple attache les 170 Go/s aux configurations de mémoire : les 153 et 170 ne sont pas deux sources contradictoires. Le prix de 1 709 € concerne bien 32 Go / 512 Go, avec le délai indiqué. Les 32 Go partagés ne sont pas 32 Go de mémoire dédiée au GPU.

Un fichier décimal de 16,6 Go ne dépasse pas mathématiquement 16 GiB de puces : il faut compter bureau et cache avant de conclure. Le rapport de bande passante 5,65 ne représente jamais un duel de vitesse applicative. Les campagnes Mac emploient des tâches et fichiers différents ; aucun score de qualité n’est transféré. Le renvoi final suit le calendrier : calcul du coût d’un modèle cloud chez soi le 14 décembre. Aucun filmage d’application ni test demandé.
