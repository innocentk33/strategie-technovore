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

**Mots-clés français** (`vidiq_outliers`, `language: fr`, `threeMonths`) : « IA en local », « comment ça marche », et le nom de l'appli ou du modèle des prochains créneaux.

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
