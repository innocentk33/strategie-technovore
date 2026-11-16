# Sources : choisir un moteur local

Recherche du 16/11/2026, publication provisoire du 25/01/2027. ✅ Source primaire ouverte puis rouverte ; ⚠️ mesure unique ou réemploi ; ❌ point non établi. Aucun test personnel ni classement universel de vitesse.

| ID | Résultat et limite | Source exacte / double contrôle |
|---|---|---|
| F1 ✅ | LM Studio : conversation, recherche sur Hugging Face, gestion des modèles et paramètres, serveur local, CLI et mode sans interface. GGUF via llama.cpp ; MLX sur Apple Silicon. | https://lmstudio.ai/docs/app · ouverte puis rouverte le 16/11 |
| F2 ✅ | Ollama : modèles locaux et cloud, intégrations, API compatibles OpenAI et Anthropic, bibliothèques Python et JavaScript. Les fonctions recouvrent plusieurs usages de LM Studio. | https://docs.ollama.com/ · ouverte puis rouverte le 16/11 |
| F3 ✅ | llama.cpp : outils en ligne de commande, serveur compatible OpenAI avec interface web, plusieurs moteurs matériels et versions déjà compilées. | https://github.com/ggml-org/llama.cpp · ouverte puis rouverte le 16/11 |
| F4 ⚠️ | Étude Mozilla du 17/09/2026 : Mac M4 Max 64 Go sous macOS 26.6.2, Linux avec L40S 48 Go, Steam Deck 16 Go sous SteamOS 3.8.16. Mêmes GGUF, versions précisées, contexte 16 384, tailles de lots laissées par défaut. Jusqu’à +63 % en lecture de prompt pour le 9B sur Steam Deck grâce à une autre préparation des shaders Vulkan. Ce gain ne mesure ni la génération ni Windows. | https://blog.mozilla.ai/benchmarking-local-llm-servers-llama-cpp-llamafile-lm-studio-and-ollama/ · ouverte puis rouverte le 16/11. Une campagne : 15 passages par point, échauffement et extrêmes retirés, moyenne sur 10. Aucune hiérarchie générale. |
| F5 ⚠️ | Laboratoire Windows : meilleure cellule Ollama native à 7,62 tokens/s avec 6 threads ; llama.cpp CPU à 6,12 avec 8 threads. Réglages et conditions différents : aucun duel contrôlé des trois outils. | https://github.com/manishklach/windows-local-llm-lab · ouverte puis rouverte le 16/11 ; chiffres exclus du classement dans la voix. |
| F6 ✅ | Versions observées : Ollama v0.40.16 du 9/11, LM Studio 0.4.28 du 31/10, llama.cpp v1.0.0 depuis la redirection de l’adresse « latest ». Elles ne prédisent pas les versions de janvier. | https://github.com/ollama/ollama/releases/tag/v0.40.16 ; https://lmstudio.ai/changelog/lmstudio ; https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0 · toutes ouvertes puis rouvertes le 16/11. |
| F7 ⚠️ | Connexion de Claude Code aux deux applications documentée ; Anthropic ne prend pas en charge le routage vers des modèles autres que Claude par ces passerelles. | https://docs.ollama.com/integrations/claude-code ; https://lmstudio.ai/docs/integrations/claude-code ; https://code.claude.com/docs/en/llm-gateway · réemploi des faits F1–F3 de claude-code-gratuit, double lecture le 16/11, sans nouvelle ouverture dans ce projet. |
| F8 ✅ | Strata : Windows et Linux, API locales compatibles OpenAI et Anthropic, modèles compatibles dont des mélanges d’experts ; licence MIT. Aucun fonctionnement promis sur tout PC, aucune mémoire ou vitesse supérieure déduite. | https://github.com/Niko1221/Strata · ouverte puis rouverte le 16/11. |
| F9 ⚠️ | LM Studio documente des fonctions hors ligne avec les fichiers et moteurs nécessaires déjà présents ; recherche et téléchargements demandent une connexion. | https://lmstudio.ai/docs/app/offline · réemploi de cadeau-ia-locale F10, double lecture le 16/11. |
| F10 ❌ | Aucun comparatif contrôlé contemporain des trois outils sous Windows, à fichier, cache et contexte identiques, n’est établi dans cette recherche. Aucun vainqueur universel n’en découle. | Recherche primaire bornée. L’étude Mozilla porte sur Linux, Mac et Steam Deck. |

## Journal de double vérification

Les documentations des trois outils ont été rouvertes : leurs fonctions se recouvrent, le choix par usage et par contrôle reste pertinent. L’étude Mozilla a été relue : les 63 % concernent la lecture du prompt, des shaders et le Steam Deck ; les versions du protocole sont distinctes des versions actuelles. Le dépôt Windows a été rouvert : ses meilleures cellules utilisent des réglages différents et ne forment pas un classement causal.

La version Ollama 0.40.16 et sa date du 9/11 ont été relues. Le journal LM Studio affichait d’abord Bionic : l’onglet LM Studio et l’adresse /changelog/lmstudio ont permis de confirmer 0.4.28 au 31/10. La redirection « latest » de llama.cpp vers v1.0.0 a été rouverte. Strata a été rouvert. Les faits F7 et F9 sont réutilisés avec une traçabilité explicite, sans feindre une nouvelle consultation.

Aucune installation n’a été exécutée. Aucun prix ni test personnel n’est demandé pour cette vidéo.
