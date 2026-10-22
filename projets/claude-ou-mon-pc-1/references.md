# Vidéos de référence pour les essais sur la 5080

> Relevé vidIQ du 22/10/2026 (recherche YouTube, vidéos publiées depuis juin 2026). Les vues et le multiple (« ×N » = score d'anomalie vidIQ, par rapport à la moyenne de la chaîne) datent de ce jour. Le plan d'installation et de test est dans [`modeles-5080.md`](modeles-5080.md).

**À retenir avant de regarder** :
- Personne en français n'a publié un test mesuré d'un modèle de 16 Go face à Claude : l'angle de « Claude ou mon PC ? » reste libre.
- On reprend la **méthode** de ces vidéos (protocole, mesures, prompts reproductibles). On ne reprend **ni leur angle ni leurs miniatures** (règle du radar, `CLAUDE.md`).
- Les chiffres qu'elles donnent sont des mesures de tiers : à citer « d'après X », jamais comme les tiens.

## 1. La méthode de test : à regarder en premier

| Vidéo | Chaîne | Vues | Ce que tu en tires |
|---|---|---|---|
| [Qwen 3.8 27B en dos GPUs de 16 GB: de 13 a 66 tokens](https://www.youtube.com/watch?v=rH993Bf1sK8) (ES, 01/09) | Hardware IA (1,7 K abonnés) | 18 K | **La seule mesure trouvée sur une RTX 5080** : d'après lui, Qwen 3.8 27B en Q4 dans LM Studio donne **13 tokens/s** sur sa 5080 seule, parce que le fichier déborde en RAM. Son protocole est simple à copier : le même prompt (un Arkanoid en un seul fichier HTML), **température 0 et seed 42**, puis on compare les jeux obtenus. Le prompt exact est dans sa description. Outil de mesure : [nvitop](https://github.com/XuehaiPan/nvitop). |
| [Qwen 3.8 27B first tests - 16GB Local LLM setup](https://www.youtube.com/watch?v=1EzVVj7DFPc) (15/08) | Luke's Dev Lab (17,6 K) | 181 K (×7,9) | La grille de test la plus complète sur 16 Go, en 9 épreuves : vitesse, mémoire, agent, HumanEval, Kanban, sable, donjon, Blender, Godot. **Ses fichiers de configuration et ses prompts sont publics** : [github.com/lukesdevlab/youtube](https://github.com/lukesdevlab/youtube). Reprends 2 ou 3 de ses épreuves, pas les 9. |
| [Qwen 3.8 27B: 16GB VRAM Local Test](https://www.youtube.com/watch?v=bTaN5VYCN58) (15/08) | kintu (3,3 K) | 49 K (**×42,9**) | Une petite chaîne qui explose avec ton sujet exact sur une carte de 16 Go (RTX 5060 Ti, 64 Go de RAM). Le chapitre « llama.cpp Config » (0:25) montre les réglages. Il termine sur une comparaison avec Claude Opus. |

## 2. Choisir le bon fichier et les bons réglages

| Vidéo | Chaîne | Vues | Ce que tu en tires |
|---|---|---|---|
| [I Tested Every Qwen3.8-27B Quant: Here's the Best One For Your GPU](https://www.youtube.com/watch?v=hg26j0erUSo) (01/09) | Kai | 73 K | Pourquoi le plus gros fichier qui rentre n'est pas le meilleur ; « l'erreur du cache KV » (9:00) ; Ridge, Unsloth et Bartowski comparés ; le décodage spéculatif avec la tête MTP intégrée (14:00). Le benchmark indépendant cité : [Quesma](https://quesma.com/blog/qwen38-27b-quantizations-benchmarked/). |
| [Qwen 3.8 27B GSQ RCO tested - 16GB](https://www.youtube.com/watch?v=jFHu6wx_TMQ) et [Qwen 3.8 27B Ridge tested - 16GB](https://www.youtube.com/watch?v=4NVT6iTvsfs) | Luke's Dev Lab | 75 K et 178 K (×5,4) | Les deux fichiers « spécial 16 Go » testés avec la même grille : de quoi choisir entre ISTA GSQ-RCO et Ridge avant de tout télécharger. |
| [I Tested Every Best Local AI For GPU (8GB TO 24GB VRAM)](https://www.youtube.com/watch?v=ugKAkCVBcz0) (21/10) | Kai | 53 K | Le piège du Q4_K_M par défaut sur 16 Go sous Windows (10:05) et la différence entre tokens par seconde et minutes par tâche (13:27). Déjà analysée dans [`etudes/outliers-2026-10-22.md`](../../etudes/outliers-2026-10-22.md). |
| [Was ich über lokale KI gelernt habe](https://www.youtube.com/watch?v=M1j_uRqKMKI) (DE, 28/08) | c't 3003 (262 K) | 539 K (×13,2) | Un média sérieux qui conseille, **pour 16 Go : Qwen 3.6 35B A3B (Q4_K_M) avec OpenCode**. C'est le candidat « modèle à experts » à mettre face au 27B. |

## 3. L'agent qui pilote le modèle (le « harnais »)

| Vidéo | Chaîne | Vues | Ce que tu en tires |
|---|---|---|---|
| [Qwen3.8 27B: Same Model, Three Harnesses, One Clear Winner](https://www.youtube.com/watch?v=sSySOPGNdjw) (28/08) | James Layne (5,2 K) | 181 K (×41) | Le même modèle dans pi, Hermes Agent et DeepSeek Harness donne des résultats très différents. Montre les réglages de pi (2:38). Ça justifie de dire dans ta vidéo quel harnais tu utilises, et pourquoi. |
| [I ran Qwen3.8 27B on single 8GB Card! (Better than expected)](https://www.youtube.com/watch?v=ye50BbXEczo) (24/08) | Red Stapler (180 K) | 645 K (×14,8) | L'inspiration d'origine de la fiche. En 5 minutes : la configuration du modèle, le harnais pi, les ratés (« pourquoi les fichiers en 3 bits n'ont pas marché », 4:27), puis la comparaison avec Opus. Le chapitre des ratés est ce qui le rend crédible. |
| [I Don't Need Frontier Models Anymore (Qwen 3.8 27B + DeepSeek Harness)](https://www.youtube.com/watch?v=OIUBhUcx8cA) (17/08) | Manolo Remiddi (30,6 K) | 180 K (×20) | Un test honnête : les benchmarks promettent beaucoup, son propre test de chasse aux bugs donne « environ 30 % de mieux que Qwen 3.6 ». Un bon modèle de ton pour ton verdict. |

## 4. Le récit « IA locale contre Claude » : pour la structure de ta vidéo

| Vidéo | Chaîne | Vues | Ce que tu en tires |
|---|---|---|---|
| [Qwen 3.8 27B локально! Отменяю подписку на Claude?](https://www.youtube.com/watch?v=2s6LBHqEz-E) (RU, 27/08) | Студия Игор (17,4 K) | 288 K (×10,8) | **Le concept le plus proche du tien** (« j'annule mon abonnement Claude ? »), sur Mac. Regarde-le pour ne pas faire la même vidéo : lui fabrique un jeu Godot sur 3 jours, toi tu fais un duel A/B et un conseil d'achat. |
| [IA nivel OPUS en tu PC: Gratis e ILIMITADA](https://www.youtube.com/watch?v=ZqkljdI1HT0) (ES, 23/08) | Xavier Mitjana (385 K) | 229 K | Deux défis réels face à Claude Opus et Gemini, plus les réglages de LM Studio pour les cartes grand public (16:53). |
| [Qwen 3.6 vs Qwen 3.8](https://www.youtube.com/watch?v=B8ILtQ4q9S8) (Short, 15/08) | Dan Ackerman (8 K) | 848 K (×178) | Deux modèles, une page web chacun, côte à côte : c'est le même ressort que ton hook « A ou B ? ». Ça confirme que le duel visuel accroche. |

## 5. En français : la concurrence directe

| Vidéo | Chaîne | Vues | Ce que tu en tires |
|---|---|---|---|
| [J'avais tort... Gemma 4 en LLM local, c'est incroyable. Test COMPLET.](https://www.youtube.com/watch?v=kKbDCrvO7Rg) (14/06) | DevArt (18,4 K) | 58 K (×5,5) | Ollama et OpenCode, avec de vraies tâches de dev (landing page, bugs, mini-jeu). Accroche par un aveu (« j'avais tort »), comme Kai. |
| [IA locale : est-ce que ça vaut le coup ? J'ai installé et comparé 5 modèles](https://www.youtube.com/watch?v=rxzxx5Zy3sw) (24/09) | Digitiz (11,6 K) | 55 K (×9) | Sur un Mac mini de 16 Go, des tâches de bureau. **Aucun des deux ne teste une carte graphique de 16 Go face à Claude**, et c'est ta place. |

## 6. Si ton PC a 64 Go de RAM ou plus : les modèles à experts plus gros que la carte

| Vidéo | Chaîne | Vues | Ce que tu en tires |
|---|---|---|---|
| [Qwen 3.8 Flash Next Tested - 16GB Local LLM setup](https://www.youtube.com/watch?v=s4cTVRH2ReA) (14/09) | Luke's Dev Lab | 157 K | Le modèle à experts récent de Qwen (177 milliards de paramètres, 6 actifs) sur une carte de 16 Go, avec la même grille que ses autres tests. |
| [FreeToken vs llama.cpp — An 8GB Laptop Ran a 35B Model at Nearly 40 TPS](https://www.youtube.com/watch?v=MggRcCnFYRo) (23/08) | Morgans Code | 27 K | Un chapitre sur un **test communautaire avec une RTX 5080** (7:21) et le rôle de la RAM (9:12). FreeToken semble réservé à Linux : vérifié dans `modeles-5080.md`. |
| [llama.cpp Just Made Huge MoE Models 4× Faster](https://www.youtube.com/watch?v=ohp15NcKDhA) (21/10) | Code Unpacked | 11 K | Le cache d'experts de llama.cpp, fusionné le 7 octobre. C'est le réglage qui change tout pour les modèles à experts sur une carte de 16 Go. |

## Ordre de visionnage conseillé (environ 1 h 30, à 1,5×)

1. **Hardware IA** : la seule mesure sur ta carte, et son protocole.
2. **Luke's Dev Lab, Qwen 3.8 27B 16GB** : récupère ses configurations sur GitHub.
3. **Kai, les quantifications** (de 2:15 à 11:00) : pour choisir le fichier.
4. **James Layne** (de 0:00 à 5:30) : pour choisir le harnais.
5. **Red Stapler** en entier (5 min) : la structure d'une vidéo courte et le chapitre des ratés.
6. **Студия Игор** en survol : ce qu'il ne faut pas refaire.
