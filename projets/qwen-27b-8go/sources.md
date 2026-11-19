# Sources : Qwen 27B sur 8 Go

Relevé du **16/11/2026**, pour la vidéo du **23/11/2026**. Vidéo calculée, aucun essai de l'auteur. Recherches : deux agents GPT-6.1 Sol ; revue indépendante : GPT Astra effort élevé. Les notes détaillées sont dans `recherche-mesures.md`, `recherche-modele.md` et `recherche-interface.md`.

**Légende :** ✅ lu à la source primaire ; ⚠️ source secondaire, mesure unique ou portée limitée ; ❌ introuvable ou contredit. Une source primaire qui publie une seule expérience reste ⚠️ pour la généralisation. Les calculs et propositions éditoriales sont explicitement séparés des mesures.

## Conclusion avant rédaction

- Le fichier existe et sa taille affichée est 7,63 GB. Dynamic V3.1 est annoncé le 11 novembre 2026.
- L'auteur du benchmark publie bien 3,2 → 18,0 tok/s sur GTX 1080 Ti bridée ; aucune seconde reproduction correspondante sur vraie carte 8 Go trouvée dans notre recherche.
- Pas de promesse ×5 dans le titre. « Une mesure publiée », pas « ta carte ira à 18 ».
- Les plafonds de contexte et le débit proviennent de llama.cpp, pas d'un essai LM Studio.
- Les scores Unsloth ne valident pas les performances avec réflexion coupée et contexte court.
- L'article CompressionBench n'est pas une seconde mesure sur une carte grand public de 8 Go.

## Faits utilisables

### F1 ✅ — Fichier et identité

- URL : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
- Fichiers : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main
- Page individuelle : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/blob/main/Qwen3.8-27B-UD-IQ2_XS.gguf (recoupée avec l’arborescence rouverte ; pas deux ouvertures de cette page individuelle).
- Modèle officiel : https://huggingface.co/Qwen/Qwen3.8-27B
- Date : consultation et deuxième lecture 16/11/2026 ; mise à jour Dynamic V3.1 annoncée **11/11/2026** sur https://unsloth.ai/docs/models/qwen3.8.
- Exact : **Qwen3.8-27B-UD-IQ2_XS.gguf**, taille affichée **7,63 GB**. Dense **27B** ; le tag architectural `qwen3_5` ne change pas son identité.
- Limite : taille du fichier sur disque, pas consommation totale de VRAM. « 2 bits » est une famille de quantification, pas exactement deux bits pour chaque nombre du fichier.

### F2 ⚠️ — Avant/après unique, source de l'auteur

- URL : https://www.youtube.com/watch?v=u_DYZhTZ2IM
- Date de publication : **13/11/2026** ; description publique lue deux fois le **16/11**, via deux extractions `yt-dlp` indépendantes après échec du lecteur web. Section **Our measurement**, donc source directe du testeur, pas reprise d'un autre créateur.
- Carte : **GTX 1080 Ti**, mémoire réservée **3 Go**, disponible annoncé **7955 MiB** ; moteur llama.cpp **0943ca5**, **3 passes**.
- Écriture : nouveau UD-IQ2_XS tout GPU **18,0 tok/s** vide, **16,9** à 4K, **15,3** à 13,8K. Ancien UD-IQ4_XS partiellement CPU, i9-9900K : **3,2** vide, **3,0** à 13,8K.
- Lecture du prompt : environ **210–280 tok/s**, annoncée similaire ; jamais la confondre avec l'écriture.
- Limites : pas de logs bruts liés, de dispersion des passes ni de prompt reproductible. Quantification, qualité et placement changent. Ce n'est pas une RTX 4060, ni LM Studio. Attribution obligatoire.

### F3 ⚠️ — Contexte et incident publiés

- Même URL et dates que F2 : https://www.youtube.com/watch?v=u_DYZhTZ2IM
- Cache 8 bits : environ **14K** remplissables ; cache 4 bits : environ **22,5K**, écriture **11,6 tok/s** plein. Commandes : contexte **14336** ou **22528**.
- Fenêtre 4 bits configurée **25,6K**, plantage au-delà d'environ **24K** remplis, selon l'auteur.
- Ne pas transformer ces résultats en limite de toute carte 8 Go ; ne pas garantir ces plafonds dans LM Studio. Le script n'utilise que l'ordre de grandeur 14000 et l'existence du plantage.

### F4 ⚠️ — Qualité : mesures du fournisseur

- URL : https://unsloth.ai/docs/models/qwen3.8
- Date de la mise à jour : **11/11/2026** ; ouverte puis rouverte le **16/11**.
- Benchmarks : **LiveCodeBench v6**, **DeepSWE v1.1**, **Terminal Bench 2.1** notamment.
- Conditions annoncées : **256K** de contexte pour les tests d'agents, **128K** pour les autres. Réflexion **xhigh** et **preserve_thinking**, température **1,0**, top_p **0,95**, top_k **20**. Les relevés des graphiques sont consignés dans `recherche-modele.md`.
- Conclusion autorisée : les évaluations du fournisseur montrent une résistance inégale à la compression selon la tâche. Pas « 95 % de toute la qualité », pas validation du mode sans réflexion à contexte court. Une seule campagne du fournisseur, pas deux mesures indépendantes.
- **Graphique primaire effectivement inspecté deux fois par l'agent principal** : deux téléchargements indépendants puis lecture visuelle le 16/11. URL exacte : https://3215535692-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FxhOjnexMCB3dmuQFQ2Zq%2Fuploads%2FWf4zRxz4iskzXZcBUQYq%2Ffour(1).png?alt=media&token=0e7bc8b1-6a96-4978-bcbe-227d69705eb2
- **DeepSWE v1.1** : annotation BF16 **40,40** exacte ; point vert UD-IQ2_XS vers **12,8**, sans étiquette numérique, donc lecture graphique approximative. Voix : **environ 40 % contre environ 13 %**. Le point UD-IQ4_XS est vers **36**, approximation graphique ; il soutient la préférence conditionnelle pour moins de compression.
- **LiveCodeBench v6** : annotation BF16 **88,62** exacte ; point vert UD-IQ2_XS vers **84,5**, approximation graphique. Pas de décimale prétendue exacte pour le point, pas de ratio « qualité conservée ». Non chiffré en voix pour éviter une rafale.
- Les **94–97 %** MMLU/math de la transcription ne sont pas validés par ce graphique et restent hors script. L'agent Sol n'a pas pu lire les PNG ; cette vérification complémentaire a été réalisée ensuite par l'agent principal, puis confirmée visuellement par le reviewer indépendant Astra.

### F5 ✅ — Réglages LM Studio documentés

- URL : https://lmstudio.ai/docs/app/advanced/per-model
- Page sans date de publication affichée ; ouverte et rouverte **16/11/2026**.
- Chemin documenté : **My Models → roue dentée**. Paramètres cités : GPU offload, context size, Flash Attention.
- Prouve la présence des réglages, pas le débit ni la compatibilité de tous les runtimes avec ce fichier précis.

### F6 ✅ — K/V et Flash Attention

- URL : https://github.com/lmstudio-ai/localization/blob/main/en/config.json
- Date : branche mobile main, date de commit non relevée ; deux ouvertures **16/11/2026**.
- Champs : **K Cache Quantization Type**, **V Cache Quantization Type**. Le texte d'interface dit que réduire leur précision économise la mémoire et peut dégrader la qualité. La quantification V exige **Flash Attention**.
- Ne prouve pas à elle seule que tous les choix de cache sont disponibles sur chaque moteur/matériel.

### F7 ✅ / ⚠️ — Contrôle de réflexion conditionnel

- Primaire : https://lmstudio.ai/docs/app/modelyaml ; page non datée, deux ouvertures **16/11/2026**.
- La section `customFields` montre **Enable Thinking**, lié à `enable_thinking`. Le template doit effectivement prendre en charge cette variable.
- Témoin communautaire, ouvert et rouvert : https://lmstudio.ai/ufnd01/qwen3.8-27b, mise à jour affichée **11 septembre**, année non affichée. Expose réflexion et effort, mais fichiers **MLX** : ne valide pas le GGUF Unsloth.
- Dans la voix : seulement « si disponible et relié au modèle ». Ne pas recommander `/no_think` par analogie avec un autre modèle.

### F8 ✅ — Steam

- URL : https://store.steampowered.com/hwsurvey/
- Période affichée : **octobre 2026**, ouverte et rouverte **16/11/2026**.
- Rubrique **VRAM**, **8 GB : 26,92 %**, variation **+0,21 point**. Ne pas confondre avec System RAM.
- Enquête volontaire anonyme. Le script dit « plus d'un quart des configurations participantes », pas un recensement mondial ni une statistique propre à l'Afrique.

### F9 ⚠️ — Le budget mémoire dépasse les poids

- Sources : protocole F2/F3, https://www.youtube.com/watch?v=u_DYZhTZ2IM ; contrôles mémoire F5/F6.
- Date : **13/11/2026**, deux lectures **16/11**.
- Observation qualitative : les poids, le cache, les buffers et les autres usages doivent cohabiter. Déduction éditoriale : un fichier affiché 7,63 GB ne garantit pas un chargement complet sur toute carte commercialisée « 8 Go ».
- Aucun calcul « 8 − 7,63 = place restante » : unités décimales/binaires et surcoûts distincts.

### F10 — INTERPRÉTATION PAR USAGE, pas nouveaux essais

- Origine : rédaction du **16/11/2026**, à partir de F2/F3/F4. Pas d'URL de benchmark supplémentaire.
- Conversation courte / aide sur un fichier / agent sur dépôt : lecture éditoriale des limites publiées. Les deux premiers usages ne sont pas présentés comme validés par un test de l'auteur. LiveCodeBench soutient un résultat sur exercices de programmation ; ne certifie pas toute aide sur un fichier réel.
- Les anciens conseils d'essai personnel, de comparaison et de contexte **4096 tokens** sont **retirés du script actif** après clarification du format calculé. Ils subsistent uniquement dans l'archive historique.
- L'avis personnel reste un crochet facultatif. Aucun avis de l'auteur inventé.

### F11 ❌ — Seconde reproduction du nouveau fichier non trouvée

- Recherche datée du **16/11/2026**, requêtes et exclusions dans `recherche-mesures.md`.
- URLs examinées : https://www.reddit.com/r/Qwen_AI/comments/1x28tms/qwen3827b_q4_on_rtx_4060_8gb_32gb_ram_6_toks_with/ ; https://github.com/recycie/qwen-local-coder ; https://github.com/jacoprudot/local-llm-benchmark ; https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/discussions/143.
- Les trois rapports de matériel 8 Go portent sur **Q4**, **IQ1_M**, ou ancien **GSQ-RCO IQ2_XS**. Aucun ne reproduit le nouveau **UD-IQ2_XS Dynamic 3.1**. Les mesures examinées ont été relues ; aucune n'est utilisée comme confirmation du ×5.
- « Non trouvée par notre recherche » ne signifie pas « n'existe nulle part ».

### F12 ⚠️ — CompressionBench, comparaison écartée de la voix

- URL : https://arxiv.org/abs/2611.06858 ; texte : https://arxiv.org/html/2611.06858v2
- Publication : **4/11/2026**, révision **9/11/2026**, lectures du **16/11**.
- Contrainte de poids **8 GiB**, exécution sur **H200 NVL**. Pas une preuve sur carte grand public de 8 Go.
- Le ratio approximatif de trois oppose des méthodes de l'article ; ne compare pas directement notre fichier Unsloth dans le PC du spectateur. Voir relevés de l'agent modèle. Exclu du script pour ne pas brouiller le choix.

### F13 ✅ / ❌ — Autres tailles et superlatif à retirer

- URL : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/tree/main ; lecture et deuxième contrôle **16/11/2026**.
- **UD-Q2_K_XL : 9,95 GB** ; un **IQ2_XXS à 7,21 GB** est aussi listé.
- ❌ « Le premier 2 bits qui tient » n'est pas établi par cette liste. Retiré. Le script recommande d'examiner un fichier précis, pas un record historique.

### F14 — CALCULS reproductibles

- Entrées : F2, publication **13/11**, relue **16/11/2026**.
- Contexte vide : **18 / 3,2 = 5,625**. À 13,8K : **15,3 / 3,0 = 5,1**.
- Ce ne sont pas deux mesures indépendantes. **18 / 3 = 6**, donc « de 3 à 18 = exactement cinq fois » est faux.

### F15 — Programmation fournie par l'auteur

- Source locale : `prompt-reprise-gpt.md`, daté **16/11/2026** ; `projets/carte-par-budget/fiche.md`.
- Cette vidéo : **lundi 23 novembre**. Suivante : choix de carte par budget, **jeudi 26 novembre**. Vidéo 32 Go : **lundi 30 novembre**.
- Source fournie, pas fait tiré du web. Aucun prix marchand utilisé dans la vidéo 1.

### F16 — CALCUL de temps d'écriture, pas chronométrage

- Entrées : **3,2** et **18,0 tokens/s**, source F2 du **13/11/2026**, déjà lue et relue le **16/11** : https://www.youtube.com/watch?v=u_DYZhTZ2IM.
- Hypothèse pédagogique du **16/11/2026** : même quantité arbitraire de **500 tokens générés**, débit constant. Ce volume n'est pas une longueur de réponse relevée chez le testeur.
- **500 / 3,2 = 156,25 secondes**, arrondi **156 s = 2 min 36 s**.
- **500 / 18 = 27,777… secondes**, arrondi **28 s**.
- Exclus : chargement, lecture du prompt, autres latences. Si des tokens de réflexion sont générés en plus de ces 500 tokens, le calcul ne les compte pas.
- Deuxième contrôle arithmétique : **156,25 × 3,2 = 500** ; **(250 / 9) × 18 = 500**. Ce contrôle ne crée aucune seconde mesure indépendante.
- Voix et visuel portent « division » / « exemple théorique », et aucune animation n'imite un chat filmé chez l'auteur.

### F17 ⚠️ — MTP laissé de côté dans la mesure F2

- Ajout du **18/11/2026**. Sources : `recherche-mesures.md`, M2 l. 38 (description de https://www.youtube.com/watch?v=u_DYZhTZ2IM : laisser de côté le projecteur vision et le fichier MTP) ; transcription `etudes/transcriptions/simplyexplain-u_DYZhTZ2IM.md`, **06:52** : le fichier vision et le fichier de décodage spéculatif, ensemble, demandent plus de 2 Go qu'une carte de 8 Go n'a pas.
- Voix autorisée : dans cette mesure, le fichier MTP est laissé de côté, faute de place. Rien de plus : on ne sait pas si l'ancien essai à 3,2 tournait avec ou sans MTP ; ne pas dire « tout vient du fichier » ni que le MTP est impossible sur 8 Go.

## Deuxième vérification : journal et corrections

| Groupe | Deuxième lecture du 16/11 | Correction retenue |
|---|---|---|
| F1/F13 | HF rouvert par agent modèle ; contrôle indépendant Astra | Taille fichier ≠ VRAM totale ; aucun « premier fichier » |
| F2/F3 | Deuxième extraction publique YouTube par agent mesures | 3,2 précis ; une expérience malgré trois passes ; plafond llama.cpp non universel |
| F4 | Texte Unsloth rouvert ; PNG téléchargé à nouveau et réinspecté par agent principal | BF16 40,40 annoté ; petit fichier ≈13 lu graphiquement. Pas de décimale inventée ; grands contextes ≠ recette 8 Go |
| F5/F6 | Doc et dépôt d'interface rouverts par agent principal ; contrôles Astra | Paramètres documentés, pas essai LM Studio |
| F7 | Doc model.yaml ouverte puis rouverte par agent principal ; lecture Astra | Bouton conditionnel au template, exemple MLX non probant pour GGUF |
| F8 | Page Steam rouverte à la rubrique VRAM | 26,92 % d'une enquête, pas population mondiale |
| F11 | Rapports Reddit/GitHub rouverts par agent mesures | Exclusion des autres quants et de Flash-Next |
| F12 | arXiv relu par agent modèle et indépendant Astra | H200, pas vraie 8 Go ; comparaison retirée |
| F14 | Divisions recalculées à partir de F2 | 5,625 et 5,1 ; pas 5 exact à partir de 3→18 |

Les détails ou dates non lisibles restent signalés comme tels. Aucune case ✅ n'atteste une reproduction expérimentale par nous.


## Recentrage demandé par l'auteur

Le 16/11/2026, l'auteur confirme un format calculé comme la référence SimplyExplain, sans ouvrir LM Studio ni effectuer d'essai. Les sources factuelles et leur double lecture restent celles du travail documenté ci-dessus ; aucune nouvelle campagne de recherche n'est revendiquée pour cette réécriture. Ajouts : calcul F16 et arrondis de F4 (88,62 → environ89 ; point environ84,5 → environ85). Retraits : recette de départ4096, protocole d'essai à effectuer chez soi, capture de contrôles avant tournage. Les livrables antérieurs sont dans `archive-avant-recentrage/`.
