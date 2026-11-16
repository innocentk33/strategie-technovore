# Recherche des mesures : Qwen3.8-27B sur 8 Go

Recherche et deuxième lecture effectuées le **16 novembre 2026**. Périmètre : identité du modèle, origine du 3,2 → 18 tok/s, deuxième mesure indépendante sur une vraie carte de 8 Go. Aucun essai local et aucun script rédigé.

## Verdict

Le **3,2 → 18,0 tok/s est bien publié par l'auteur de la mesure dans la description publique de sa vidéo**, retrouvée directement avec `yt-dlp`, puis relue par une seconde extraction indépendante. Ce n'est donc plus un chiffre uniquement recopié de la transcription fournie. En revanche, cela reste **une seule expérience**, sur GTX 1080 Ti 11 Go bridée en mémoire. Aucun second avant/après du **nouveau UD-IQ2_XS Unsloth du 11 novembre** sur une vraie carte de 8 Go n'a été trouvé dans les pages examinées.

Le gain calculé au contexte vide vaut 18 / 3,2 = **5,625 fois** ; à 13,8 K, 15,3 / 3,0 = **5,1 fois**. Ce sont des divisions des mesures publiées, pas des mesures supplémentaires. Le titre ne doit donc pas promettre « ta carte 5× plus vite » comme une généralité.

## M1 — Identité exacte du modèle

**✅ Source primaire ouverte et rouverte :** [Qwen/Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B), consultée le 16/11/2026. Carte officielle : **Qwen3.8-27B**, modèle dense 27B, vision et texte, 64 couches. La page explique sa filiation architecturale avec Qwen3.5 ; le tag `qwen3_5` ne renomme donc pas le modèle Qwen3.5. Ne pas confondre avec **Qwen3.8-Flash-Next**, rencontré très souvent dans les recherches de vitesse sur 8 Go.

Le [dépôt quantifié Unsloth](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) renvoie au même modèle de base.

## M2 — Source du 3,2 → 18,0 tok/s

**⚠️ Source primaire lue deux fois, mais mesure unique non reproduite indépendamment :** [SimplyExplain, description publique YouTube](https://www.youtube.com/watch?v=u_DYZhTZ2IM), publiée le **13/11/2026** (`upload_date=20261113` extrait des métadonnées). La page web a échoué dans l'outil de navigation avec « Cache miss ». La lecture publique via `yt-dlp --skip-download --no-warnings --print description URL` a réussi, puis une deuxième commande a relu date, titre et description. Aucun téléchargement vidéo ni cookies de compte.

La section **Our measurement** de la description donne :

| Condition publiée | Valeur |
|---|---|
| Carte | GTX 1080 Ti, 3 Go de VRAM réservés, **7 955 MiB libres** |
| Moteur et répétitions | llama.cpp build **0943ca5**, **3 exécutions par condition** |
| Nouveau fichier | `Qwen3.8-27B-UD-IQ2_XS.gguf`, toutes les **64 couches** sur GPU, cache KV 8 bits |
| Génération, contexte vide | **18,0 tok/s** |
| Génération, 4 K tokens | **16,9 tok/s** |
| Génération, 13,8 K tokens | **15,3 tok/s** |
| Ancien fichier | UD-IQ4_XS, **33 couches sur 65** sur GPU, reste sur **i9-9900K** |
| Ancien fichier, contexte vide | **3,2 tok/s** |
| Ancien fichier, 13,8 K tokens | **3,0 tok/s** |
| Lecture du prompt, les deux fichiers | Environ **210–280 tok/s**, annoncée similaire |

Autres observations publiées dans cette même section : environ **14 K tokens** remplissables en KV 8 bits ; environ **22,5 K** en KV 4 bits, avec **11,6 tok/s** une fois plein. Réduire `-ub` et `-b` à 256 apporte selon l'auteur **1,5–2,5 K** de contexte. Une fenêtre 4 bits de **25,6 K** se charge mais échoue en se remplissant au-delà d'environ **24 K**.

Les commandes affichées utilisent `-ngl 99 -fa on -c 14336 -ctk q8_0 -ctv q8_0`, ou `-c 22528 -ctk q4_0 -ctv q4_0`. L'auteur demande de laisser de côté le projecteur vision et le fichier MTP, et de couper la réflexion ou choisir `low`.

**Limites :** aucun journal brut ni fichier de résultats lié dans la description ; pas de dispersion des trois passes ; prompt et longueur de génération non précisés. Même carte physique mais quantification, répartition RAM/GPU et qualité changent. Une 1080 Ti bridée ne reproduit pas l'architecture, la bande passante ou les pilotes d'une RTX 4060. « Un seul fichier » résume donc un changement qui modifie également le placement des poids. Les 64/65 couches sont les décomptes publiés : ne pas présenter cet écart comme un changement de modèle sans examiner les journaux.

## M3 — Mesure indépendante sur RTX 4060 8 Go : ancien Q4

**⚠️ Témoignage expérimental primaire ouvert et rouvert :** [sammysamm77 sur r/Qwen_AI](https://www.reddit.com/r/Qwen_AI/comments/1x28tms/qwen3827b_q4_on_rtx_4060_8gb_32gb_ram_6_toks_with/), consulté le 16/11/2026. Le moteur de recherche indique octobre 2026 ; la page ouverte affiche une date relative (« 18d ago »). **Date calendaire exacte non certifiée.**

RTX 4060 8 Go, i5-14400F, 32 Go DDR5, Windows 11, llama.cpp CUDA, contexte 32 K. UD-Q4_K_XL : **environ 3,82 tok/s sans MTP**, **5,99 avec MTP**. UD-IQ4_XS : **environ 4,17 tok/s avec MTP**. Cela corrobore la lenteur d'un Q4 partiellement déchargé en RAM, **pas le nouveau fichier ni le ×5**.

Un commentaire ultérieur du même auteur annonce 28,7 tok/s en chat et 18,1 en agent, mais il a changé pour **Flash-Next et Strata**. Ces nombres sont exclus de la comparaison du dense 27B.

## M4 — Mesure GitHub 8 Go : autre quantification

**⚠️ Rapport primaire ouvert et rouvert :** [recycie/qwen-local-coder](https://github.com/recycie/qwen-local-coder), consulté le 16/11/2026 ; date exacte des mesures non indiquée dans le tableau lu.

RTX 5060 8 Go, i7-12700F, 32 Go RAM, llama.cpp b11576 : environ **5 tok/s** avec GSQ-RCO IQ2_XS + MTP et des FFN en RAM, contre environ **32 tok/s en nouveau code** avec **UD-IQ1_M**, ngram et contexte limité à 4 K. L'auteur rapporte une forte dégradation quand la mémoire est dépassée. **Ce n'est pas UD-IQ2_XS Dynamic 3.1 ; cela ne reproduit pas le gain de M2.**

## M5 — Autre résultat Q4 sur laptop 8 Go, à manier prudemment

**⚠️ Dépôt ouvert et rouvert :** [jacoprudot/local-llm-benchmark](https://github.com/jacoprudot/local-llm-benchmark), consulté le 16/11/2026. Déclare RTX 5060 Laptop 8 Go, Ryzen AI 9, 32 Go DDR5, IQ4_XS + MTP, contexte configuré 64 K : **4,7 tok/s en génération**, **90 tok/s de prefill** pour un prompt de **3 807 tokens**. Pas une mesure à 64 K réellement remplis. L'indication de threads est reprise d'un « original report » Intel selon sa propre note, ce qui rend l'indépendance/provenance moins nette. Ne pas en faire une seconde validation forte ; ce dépôt ne teste de toute façon pas le nouveau 2 bits.

## Pages communautaires Unsloth examinées

- [Liste des discussions](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/discussions), ouverte le 16/11 : pas de reproduction 8 Go identifiable dans les titres examinés.
- [Discussion #143, annonce Dynamic v3.1](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/discussions/143), ouverte et relue : échanges sur les quantifications et leurs mises à jour, **pas de benchmark utilisateur 8 Go du nouveau fichier** dans le contenu visible.
- [Discussion #141, UD v3.1](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF/discussions/141), ouverte : pas de mesure 1080 Ti identifiée.

## Requêtes effectuées

Requêtes exactes ou variantes proches lancées le 16/11/2026 :

- `"u_DYZhTZ2IM" benchmark 1080` ; `"u_DYZhTZ2IM"`
- `"Your 8GB GPU Runs" "Qwen"`
- `"SimplyExplain" "1080" Qwen` ; `"SimplyExplain" "Qwen 3.8"` ; `"SimplyExplain" "Qwen" "7.63"`
- `"Qwen3.8-27B" "1080 Ti"` ; `"Qwen3.8" "GTX 1080" "18"`
- `"Qwen3.8" "18.0" "3.2"` ; `"Qwen3.8-27B" "7955"` ; `"Qwen3.8" "7,955"`
- `"Qwen3.8" "IQ2_XS" "8GB"`
- `"Qwen3.8" "UD-IQ2_XS" -Flash -strata`
- `"Qwen3.8-27B" "IQ2_XS" "4060"` ; `"Qwen3.8-27B" "IQ2_XS" "3070"`
- `"Qwen3.8-27B" "IQ2_XS" benchmark`
- `site:reddit.com/r/LocalLLaMA "Qwen3.8" "27B" "8"`
- `site:reddit.com/r/LocalLLaMA "Qwen3.8" "7.63"`
- `site:reddit.com "Qwen3.8" "Dynamic 3.1" "8GB"`
- `site:github.com "Qwen3.8-27B" "UD-IQ2_XS"`
- `site:github.com "Qwen3.8-27B" "8GB" benchmark`
- `site:huggingface.co/unsloth/Qwen3.8-27B-GGUF/discussions "8" "IQ2_XS"`
- `"Qwen3.8" "IQ2_XS" "8 GB" -Flash -Next`
- `"Qwen3.8" "IQ2_XS" "8GB" -Flash -Next -strata`

La recherche infructueuse n'établit pas qu'aucune deuxième mesure n'existe : elle établit qu'aucune n'a été trouvée et vérifiée ici. Plusieurs résultats « 8 Go + IQ2_XS » concernent **Flash-Next**, d'autres le vieux **GSQ-RCO IQ2_XS**, et ne répondent pas à la question.

## Deuxième vérification et corrections

- Nouvelle extraction YouTube réussie : même date, même protocole et mêmes nombres. Le préfixe 3,2 n'est pas une précision inventée à partir du « trois » oral : il figure dans la description de l'auteur.
- Page officielle Qwen rouverte : identité Qwen3.8 confirmée malgré le tag architectural hérité.
- Reddit rouvert : les 5,99 concernent **Q4_K_XL avec MTP**, les 4,17 **IQ4_XS avec MTP**. Aucun de ces résultats n'est le nouveau 2 bits. Le commentaire rapide porte sur Flash-Next.
- Deux dépôts GitHub rouverts : l'un compare IQ2_XS GSQ et **IQ1_M**, l'autre uniquement **IQ4_XS**. Aucun ne valide le ×5 du nouveau fichier.
- **Correction éditoriale à conserver :** le résultat est attribuable (« une mesure publiée sur une 1080 Ti bridée »), et non généralisable à toutes les cartes 8 Go. Le modèle reste le même, sa copie quantifiée et ses conditions mémoire changent.
