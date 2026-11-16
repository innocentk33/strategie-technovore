# Sources : Claude Code et modèles locaux

Recherche du 16/11/2026 pour une publication provisoire du 7/01/2027. ✅ Primaire ouverte puis rouverte ; ⚠️ calcul, mesure unique ou réemploi indiqué ; ❌ non établi. Aucun essai personnel ni résultat de projet inventé.

| ID | Fait et limite | Source exacte et contrôle |
|---|---|---|
| F1 | Ollama documente `ollama launch claude`, une API compatible Anthropic, des modèles locaux et cloud, ainsi que les outils avec des modèles compatibles. Recommandation : contexte local d’au moins 64K. | https://docs.ollama.com/integrations/claude-code · ✅ Page ouverte puis rouverte le 16/11. |
| F2 | LM Studio documente Claude Code via POST /v1/messages et conseille un contexte supérieur à environ 25K. | https://lmstudio.ai/docs/integrations/claude-code · ✅ Page ouverte puis rouverte le 16/11. |
| F3 | Anthropic ne prend pas en charge le routage de Claude Code vers des modèles autres que Claude via une passerelle ; le fournisseur ne maintient ni n’audite les passerelles tierces. | https://code.claude.com/docs/en/llm-gateway · ✅ Page ouverte puis rouverte le 16/11 ; possibilité technique et support fournisseur distincts. |
| F4 | Licence de Claude Code : tous droits réservés, usage soumis aux conditions commerciales d’Anthropic. Aucune licence MIT déduite, aucun avis juridique sur la conformité globale. | https://github.com/anthropics/claude-code/blob/main/LICENSE.md · ✅ Licence ouverte puis rouverte le 16/11. |
| F5 | Qwen 3.5-4B Q4_K_M : 2,74 Go, petit candidat pour une carte de 8 Go. Le poids du fichier ne prouve pas un agent fiable. | https://huggingface.co/unsloth/Qwen3.5-4B-GGUF/tree/main · ⚠️ Réemploi de cadeau-ia-locale F5, double lecture le 16/11, sans nouvelle ouverture ici. |
| F6 | Qwen 2.5-Coder-14B Q4_K_M : fichier de 8,99 Go, arrondi à 9 Go. Candidat texte et code pour 12 Go de VRAM, cache et bureau à ajouter ; outils de Claude Code non garantis. | https://huggingface.co/lmstudio-community/Qwen2.5-Coder-14B-Instruct-GGUF/tree/main · ✅ Arborescence ouverte puis rouverte le 16/11. |
| F7 | Ollama gpt-oss:20b : fichier de 14 Go, format MXFP4, 20,9 milliards de paramètres. Outils et raisonnement documentés ; format et moteur exacts à conserver. | https://ollama.com/library/gpt-oss:20b · ✅ Bibliothèque ouverte puis rouverte le 16/11. |
| F8 | Pour une carte de 16 Go, gpt-oss 20B reste un candidat, sans garantie de contexte 64K entièrement sur GPU. LM Studio le cite dans son exemple de connexion de Claude Code. | Sources F2 et F7 · ⚠️ F2 et F7 ; capacité théorique, aucun benchmark matériel. |
| F9 | Aucun taux comparatif de réussite sur un même dépôt, avec 8/12/16 Go et contexte identique. Aucune équivalence avec Opus ou Sonnet, aucune utilisation illimitée démontrée. | Limites de la recherche · ❌ Recherche bornée, résultat filmé remplacé par un schéma documentaire. |
| F10 | L’absence de facturation par une API locale ne rend pas le matériel gratuit. Aucun coût total du client validé ; aucune économie chiffrée annoncée. | Raisonnement de coût · ⚠️ Raisonnement sur les coûts. |

## Journal de double vérification

La commande et le contexte Ollama ont été relus ; ses exemples cloud sont exclus du scénario entièrement local. LM Studio conseille environ 25K contre 64K chez Ollama : deux recommandations différentes, aucun minimum universel. Le support non-Claude est explicitement absent côté Anthropic et cette limite figure en voix. Claude Code n’est pas présenté sous licence MIT.

Le fichier de 8,99 Go est arrondi à 9 Go, sans comparaison trompeuse avec 8,37 GiB. Les 14 Go de gpt-oss ne sont pas sa mémoire totale : cache et outils s’ajoutent. Le réemploi F5 est tracé. Versions, candidats recommandés et tarifs de janvier demandent une actualisation ; aucun futur inventé. Aucune installation ni redirection réelle du PC de l’auteur n’a été exécutée.
