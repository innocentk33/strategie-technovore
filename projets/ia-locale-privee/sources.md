# Sources : ton IA locale est-elle privée ?

Recherche et **deuxième ouverture réelle le 16/11/2026**. Format documentaire, aucune recherche de serveurs ni tentative d'accès ; uniquement rapports publiés et documentation défensive. Les chiffres d'exposition ne sont pas des nombres de victimes.

| Fait | Information | Source exacte, date | Statut et seconde lecture |
|---|---|---|---|
| F1 | Rapport commun SentinelLABS/Censys : **175 108 hôtes uniques**, observés sur **293 jours**, 130 pays ; noyau persistant d'environ 23 000. Cumul distinct d'un parc simultanément exposé ou compromis. | https://www.sentinelone.com/labs/silent-brothers-ollama-hosts-form-anonymous-ai-network-beyond-platform-guardrails/ (publication du 29/01/2026 selon index ; page mise à jour le 06/03/2026) | ⚠️ Mesure primaire unique, ouverte puis rouverte : Executive Summary et Scale. Une capacité d'appel d'outil du modèle ne prouve pas des outils exécutables connectés sur chaque hôte. |
| F2 | Censys identifie 10 600 instances exposées et 1 500 répondant à au moins un prompt dans son étude de 2025. Période et méthode différentes ; aucun taux de croissance F1/F2. | https://censys.com/blog/ollama-drama-investigating-the-prevalence-of-ollama-open-instances-with-censys (24/09/2025) | ⚠️ Rapport primaire ouvert puis rouvert. Censys participe aux deux études : ne pas présenter deux auditeurs indépendants du même parc. |
| F3 | Ollama écoute par défaut sur 127.0.0.1:11434 ; l'API locale n'exige pas d'authentification. L'installation normale n'ouvre pas le service sur internet. | https://docs.ollama.com/faq et https://docs.ollama.com/api/authentication (état du 16/11/2026) | ✅ Deux pages ouvertes puis rouvertes. Aucune commande d'exposition dans le script. |
| F4 | Ollama déclare ne pas voir les prompts et données d'inférence locale. Fonctions cloud facultatives distinctes, désactivables. | https://docs.ollama.com/faq (état du 16/11/2026) | ✅ Documentation d'éditeur ouverte puis rouverte ; déclaration du fournisseur, pas audit de trafic. |
| F5 | LM Studio déclare chats et documents locaux sur l'appareil. Recherche/téléchargement de modèles et mises à jour impliquent des requêtes réseau. Services cloud facultatifs : traitement externe si choisis, absence de conservation annoncée. | https://lmstudio.ai/app-privacy (mise à jour du 19/10/2026, effective en juin 2026) | ✅ Politique primaire ouverte puis rouverte. Distinguer absence de rétention et absence de transmission. |
| F6 | Chat, RAG et serveur local LM Studio peuvent fonctionner hors ligne après téléchargement du modèle. | https://lmstudio.ai/docs/app/offline (état du 16/11/2026) | ✅ Documentation ouverte puis rouverte ; ne prouve pas qu'un outil tiers reste hors ligne. |
| F7 | Des serveurs MCP peuvent lire des fichiers, exécuter du code et utiliser le réseau. LM Studio accepte des MCP locaux et distants. | https://lmstudio.ai/docs/app/mcp (état du 16/11/2026) | ✅ Documentation ouverte puis rouverte. Possibilité et permissions réelles restent distinctes. |
| F8 | Désérialiser un fichier Pickle non fiable peut exécuter du code. Safetensors est conçu pour stocker les tenseurs sans les mécanismes de Pickle. | https://huggingface.co/docs/hub/security-pickle et https://huggingface.co/docs/safetensors/index (état du 16/11/2026) | ✅ Deux documentations ouvertes puis rouvertes. Format plus restrictif ≠ garantie du logiciel complet. Aucun exemple d'exploitation reproduit. |
| F9 | CNIL : le déploiement sur site peut limiter l'exposition de données personnelles à un tiers ; l'organisme conserve ses responsabilités de conformité au RGPD et de sécurité. | https://www.cnil.fr/fr/les-questions-reponses-de-la-cnil-sur-lutilisation-dun-systeme-dia-generative (18/07/2024, lu le 16/11/2026) | ✅ Autorité primaire ouverte puis rouverte, sections 5–6. Aucune certification de la situation du spectateur. |
| F10 | Synthèse défensive : modèle local identifié, fonctions externes connues, accès serveur maîtrisé, dépôts fiables, permissions adaptées, mises à jour et maîtrise des copies. | Déductions de F3–F9. | ⚠️ Proposition documentaire, pas audit personnel ni certification de configuration. |

## Corrections après seconde lecture

- Le total de 175 108 hôtes est un cumul sur 293 jours, conservé dès le hook. Aucune intrusion ni fuite personnelle n'en est déduite.
- L'API Ollama sans authentification accompagne une écoute locale par défaut. Le programme n'est pas annoncé exposé à internet par son installation normale.
- Les services cloud facultatifs et les requêtes de mise à jour sont des trajets distincts. Une connexion réseau ne prouve pas l'envoi des chats locaux.
- Le support d'appels d'outils par un modèle ne prouve pas un agent ayant accès à un terminal.
- Safetensors réduit un risque de sérialisation ; aucun format n'est déclaré invulnérable ni suffisant pour certifier tout un logiciel.
- Le RGPD reste applicable aux traitements concernés, y compris sur site. Aucun conseil juridique personnalisé.

Toutes les URL F1–F9 ont été ouvertes puis rouvertes dans des appels distincts. Requêtes : `site:sentinelone.com Ollama exposed 2026` ; `site:cnil.fr IA générative local données confidentialité` ; `site:lmstudio.ai docs offline privacy telemetry`. Aucun résultat secondaire n'a fourni un chiffre en voix.
