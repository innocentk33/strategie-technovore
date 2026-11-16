# Sources : avant d'acheter une deuxième carte

Recherche et seconde ouverture réelle : **16 novembre 2026**. Aucune mesure locale. Les références `master` sont un état de documentation mutable, pas une garantie pour toutes les versions. Les vitesses sont la génération sauf mention « lecture du prompt ».

| Fait | Affirmation vérifiée | Source et date | Statut et deuxième lecture |
|---|---|---|---|
| F1 | Sur deux RX 7900 XTX, Qwen3.8-27B UD-Q4_K_XL, llama-bench b10794/ROCm : une carte 36,05±0,04 tok/s ; deux layer 34,03±0,09 ; deux tensor 47,06±0,24. 5 répétitions, pp 2048 / tg 512, b 4096, ub 512, FA ; PCIe 4 x8/x8. | https://github.com/ggml-org/llama.cpp/issues/28863 (LithiumDevourer, 13/09/2026) | ⚠️ mesure primaire unique, rouverte ; la page donne les journaux. Génération layer légèrement plus lente ; tensor ≈ 1,31×. Prefill layer instable exclu. |
| F2 | Deuxième machine : 4070 SUPER 12 Go + 5060 Ti 16 Go ; Q4_K_XL ; à 147 456 de contexte, layer 17,1/17,4/17,4 contre tensor 28,7/28,7/28,6 tok/s. | https://github.com/xenodeve/Qwen-3.8-27B-Tuning/issues/52 (26/08/2026) | ⚠️ expérience indépendante mais autre PC/build ; ouverte puis rouverte. Confirme qu'un mode change le résultat ; ne reproduit pas 1,31× universel. |
| F3 | Même auteur : à 16 384 tokens, 11,7/11,3/11,8 sur une carte partiellement en RAM contre 21,1/20,7/20,9 sur deux cartes en layer ; Q4 désormais entièrement en VRAM. | https://github.com/xenodeve/Qwen-3.8-27B-Tuning/issues/51 (26/08/2026) | ⚠️ ouverte puis rouverte ; gain lié à sortie de RAM, donc « layer n'accélère jamais» serait faux. |
| F4 | `layer` répartit couches et leur KV ; `tensor` partage les opérations et requiert davantage de communications ; expérimental. `row` désormais déconseillé. | https://github.com/ggml-org/llama.cpp/blob/master/docs/multi-gpu.md (lu le 16/11) | ✅ doc ouverte puis rouverte. Selon cette doc, tensor exige FA et cache KV non quantifié ; auto-fit indisponible. Les résultats F2 de build antérieur ne sont pas une recette actuelle. |
| F5 | Aide serveur : layer par défaut ; none, row, tensor ; proportions `--tensor-split` ; auto-fit actif par défaut hors restrictions de mode. | https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md (lu le 16/11) | ✅ ouverte puis rouverte aux lignes 306–320. |
| F6 | Ollama privilégie une seule carte si le modèle y tient ; sinon répartition sur cartes disponibles. | https://docs.ollama.com/faq (lu le 16/11) | ✅ ouverte puis rouverte, section multi-GPU. Le bénéfice dépend des transferts. |
| F7 | LM Studio permet activation des GPU et priorité d'allocation ; billet 0.3.14 du 27/03/2025 marque priorité et limite mémoire dédiée «CUDA only». | https://lmstudio.ai/blog/lmstudio-v0.3.14 | ✅ ouvert puis rouvert. Daté de 2025, ne pas présenter les restrictions comme inventaire exhaustif en 2026. |
| F8 | Vulkan multi-GPU introduit par PR 5321 ; cartes de marques différentes possibles dans ce cadre expérimental. | https://github.com/ggml-org/llama.cpp/pull/5321 (07/02/2024) | ✅ PR ouverte puis rouverte ; ancien support ne garantit pas tous modèles/pilotes actuels. Aucune vitesse mixte extrapolée. |
| F9 | Exemple matériel : second slot Gigabyte B850M AORUS ELITE WIFI6E ICE en PCIe 3 x4 via le chipset ; dimensions et câblage de référence, dossier prévalidé F60–F65. | ../deux-cartes-occasion/sources.md ; manuel constructeur cité dans F60 (audit du 24/10 fourni) | ✅ fourni prévalidé ; pas de fausse affirmation de nouvelle ouverture. Déduction : forme x16 ≠ 16 lignes actives. Aucun pourcentage de pénalité universel. |
| F10 | 2 cartes de 16 Go = 32 Go physiques ; poids + cache + tampons + affichage empêchent de promettre 32 Go libres. | Calcul de capacité + F4/F5 ; voir ../deux-cartes-occasion/sources.md F80–F81 (16/11) | ⚠️ calcul de budget mémoire, pas mesure générale des pertes. |

## Double vérification et corrections

Les URL F1–F8 ont été ouvertes puis **rouvertes séparément**. F9 est explicitement le dossier fourni prévalidé ; aucune nouvelle lecture de manuel prétendue.

- Les 36/34 de la vidéo d'inspiration sont retrouvés à la source dans F1 : 36,05/34,03. La description vidéo seule n'est plus la preuve.
- F1 et F2 viennent de testeurs différents, mais ne permettent pas une promesse de facteur fixe. F3 contredit « la seconde carte n'accélère jamais en layer » lorsque l'ancienne configuration débordait en RAM.
- F1 : le prefill layer très variable n'est pas repris. Le chiffre47,06 est du decode, tandis que 1547,96 appartient au prefill ; laV1ne les mélange pas.
- La doc actuelle F4 limite le cache KV quantifié en mode tensor, alors que F2 utilise une autre version. Aucune commande copiée comme tutoriel universel.
- Les affirmations « -40 % avec x4 », « la plus lente fixe toute la vitesse », « tensor est toujours meilleur » sont exclues faute démonstration générale.
- Jeff Geerling : 403 ; infermeld : résultats secondaires trouvés, non utilisés comme mesure primaire. Le hook n'emprunte aucun de leurs chiffres.

Requêtes : `"LithiumDevourer" llama GPU benchmark` ; `"xenodeve" "7900" "tensor"` ; `"jeffbolznv" "tensor" llama` ; `site:jeffgeerling.com "two GPUs" llama` ; `"infermeld" "benchmark"`. Description de https://www.youtube.com/watch?v=sF_P1OICoEw lue via yt-dlp pour identifier les auteurs, pas comme preuve indépendante.
