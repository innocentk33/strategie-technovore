# IA en local : comment lire le nom d'un modèle (et tout ce qu'il y a autour)

> Phase 1 (recherche) du 23/10/2026. Analyse (piliers, grille) : [`strategie.md`](../../strategie.md), pilier 2. Planning : [`calendrier.md`](../../calendrier.md). Créneau : **lun. 2 nov. 2026, 18 h**, avant Claude #1 (ta décision du 23/10, nuit : c'est elle qui pose les bases ; d'abord placée au 30 nov.) ; reporté dans le README, le calendrier et `strategie.md` (idée 22). 2e vérification des faits faite le 23/10 (corrections en bas).
> Faits et chiffres : [`sources.md`](sources.md). Les vidéos que celle-ci prépare : [`claude-ou-mon-pc-1`](../claude-ou-mon-pc-1/fiche.md), [`cout-claude-local`](../cout-claude-local/fiche.md), [`llama-cpp`](../llama-cpp/fiche.md), [`louer-acheter-ia`](../louer-acheter-ia/fiche.md), [`opencode`](../opencode/).

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (Help : vulgarisation, porte d'entrée de la série) |
| **Format** | Longue, 12-14 min. **Mi-testée, mi-vulgarisation** (voir « Format » plus bas) |
| **Trafic visé** | Recherche (« ia en local », 21 403 recherches/mois, +91 % sur 30 jours) + suggestions à côté des vidéos « IA locale pour débutants » |
| **Mot-clé** | ia en local |
| **Type de hook** | Énigme : un nom de fichier qu'on déchiffre |
| **Production estimée** | ~20 h (5 schémas animés réutilisables : le nom décodé, la balance taille/qualité, le cube « modèle → toi », la porte ouverte/fermée des licences, le routeur) |

**Titres** :
1. Recherche : *IA en local : le guide pour tout comprendre (modèles, quantification, harnais)*
2. Curiosité : *Ce nom de fichier cache toute l'IA locale*
3. Mixte (recommandé) : *IA en local : comment lire le nom d'un modèle (35B, A3B, Q4_K_M…)*

Pourquoi le 3 : il porte le mot-clé qui monte (« ia en local »), et les caractères bizarres (« A3B », « Q4_K_M ») sont ce que ton public a vraiment sous les yeux sur Hugging Face, donc ils servent de mots-clés de sa propre recherche. Le 1 est un titre de guide, il met en concurrence avec les vidéos de 40 min à 6 h. Le 2 ne dit pas le sujet.

**Miniature** (à faire, charte verte « IA chez moi ») : le nom `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf` en grand, découpé par des barres en 5 morceaux, un point d'interrogation sous « A3B ». Pas de visage de concurrent, pas de logo de moteur. À 168 px, il faut lire au moins « A3B » et « .gguf ».

## Les 15 premières secondes (règle du 22/10, `strategie.md`, section 5)

Le meilleur moment, tout de suite : le fichier que tu télécharges vraiment, à l'écran, avec sa taille. Ni « bienvenue », ni « dans cette vidéo ».

> `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf`. Dix-huit gigas. Ma carte graphique en a seize. [CROCHET : ce qui s'est passé quand tu l'as lancé, après ton essai]. Sauf que ce nom, personne ne te l'explique. Et pourtant, chaque morceau te dit combien de place il prend, à quelle vitesse il tourne, et à quel point il est bête. [CROCHETS : ta réaction en voyant ce nom la première fois, à écrire par toi]

À vérifier : « dix-huit gigas » = 18,2 Go sur Hugging Face, environ 17 Go dans l'explorateur de Windows (`sources.md`, ligne 46). ~~« ça tient dans ma carte »~~ : **faux** (2e vérif, ligne 45) : 18,2 Go ne tiennent pas dans 16 Go ; le modèle tourne en laissant une partie des experts en RAM, d'après le plan de `modeles-5080.md`. Ce que tu as vu à l'essai va dans le crochet ; tant qu'il n'est pas fait : « je te montre ce qui se passe quand je le lance ». Le pont pour le reste (question centrale avant 30 s) : « Aujourd'hui, pas d'installation. On apprend à lire. Et à la fin, tu sauras si un modèle rentre dans TON PC avant de le télécharger. » (c'est une phrase de promesse, à faire arriver vers 0:25, pas avant 0:15).

## Texte et sous-texte

- **Texte** : un nom de fichier se lit comme une étiquette de vêtement. Chaque morceau a un sens, et avec une règle de trois (paramètres × bits ÷ 8) tu sais si ça rentre dans ton PC sans le télécharger.
- **Sous-texte** : l'IA locale n'est pas réservée aux riches. Ce vocabulaire a l'air d'un code d'initiés, c'est juste un code. Celui qui le sait ne paie ni abonnement ni clé d'API pour rien. (Pour le public africain et les petites machines : « tu n'as pas besoin de 16 Go de VRAM pour comprendre, ni même pour commencer, voici ce qui tient sur 8 Go ».)
- **À ne pas recadrer** : ne fais pas une vidéo « glossaire ». Garde le fil rouge du nom de fichier jusqu'à la fin, et garde le sous-texte « personne ne te l'explique, alors c'est moi ».

## Contenu (le fil : la carte mentale, d'abord le fichier, puis ce qui l'entoure)

La carte mentale en une phrase, à poser vers 0:25 et à refaire à la fin : **modèle → fichier (quantifié) → moteur → API → (routeur) → harnais → toi.**

1. **Hook (0:00-0:30)** : le nom du fichier, sa taille, la promesse (voir plus haut).
2. **Partie 1, lire le nom (≈ 5 min)** : on décode `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf` puis `gemma-4-12b-it-Q6_K.gguf` morceau par morceau. Les noms viennent de `modeles-5080.md`.
   - Famille + version : *Qwen3.6*, *gemma-4*.
   - **35B** = 35 milliards de paramètres, c'est le nombre de nombres dans le fichier. **A3B** = *activated 3 billion* : un modèle « à experts » (MoE) en a 35 milliards mais n'en utilise que 3 milliards par mot ; un modèle **dense** (Gemma 12B) les utilise tous. Piège : A3B accélère le calcul, pas la place prise (il faut quand même charger les 35 milliards).
   - **it** / Instruct = réglé pour suivre des consignes ; **base** = brut ; **thinking** = il réfléchit avant de répondre (Qwen3.6 le fait par défaut) ; **distill** = un petit modèle entraîné sur les réponses d'un gros.
   - **128K / 256K** = la longueur du contexte (la mémoire de travail), en tokens.
   - **.gguf** vs **safetensors** : GGUF = tenseurs + métadonnées dans un seul fichier, fait pour llama.cpp & co ; safetensors = que les tenseurs.
   - **La quantification, le « JPEG » du modèle** : Q8_0, Q6_K, Q4_K_M, IQ4_XS, IQ3_S, IQ2_XXS = moins de bits par nombre, donc un fichier plus petit et un peu moins fidèle. Le nombre = les bits ; `K` = la famille « K-quants » ; `I` / `IQ` = quantification qui s'appuie sur une matrice d'importance ; `_M`, `_S`, `_XS`, `_XXS` = moyen, petit, très petit ; **UD** = *Unsloth Dynamic* (tous les calques ne sont pas au même nombre de bits) ; BF16/FP16 = pleine précision ; MXFP4 = 4 bits en « virgule flottante par blocs » ; QAT = le modèle a été entraîné **en sachant** qu'il serait quantifié.
   - **La règle de calcul** : paramètres × bits par poids ÷ 8 ≈ Go. Exemple sourcé : Gemma 12B en Q6_K : 11,95 × 6,56 ÷ 8 = 9,8 Go, le fichier fait 9,79 Go. Puis : « plus le contexte ». (La règle donne un ordre de grandeur : sur les mélanges UD de Qwen, l'écart va jusqu'à 7 %, voir `sources.md`.)
3. **Partie 2, local ou open source (≈ 2 min 30)** : trois portes.
   - **Local** = tu as le fichier, il tourne chez toi. **Open weights** = les poids sont publics. **Open source** (au sens de l'OSI, définition 1.0 du 28/10/2024) = tu as aussi le code et assez d'information sur les données d'entraînement pour refaire.
   - Les licences en une image chacune : Apache 2.0 et MIT (tu fais presque tout), licence Llama (limite à 700 millions d'utilisateurs, mention « Built with Llama », nom commençant par « Llama »), Gemma (conditions d'utilisation jusqu'à Gemma 3 ; **Gemma 4 est passé en Apache 2.0**).
   - Un modèle ouvert peut tourner dans le cloud (chez un fournisseur) : « open » ne veut pas dire « local ». À l'inverse, **local exige des poids téléchargeables**.
4. **Partie 3, le moteur (≈ 1 min 30)** : un fichier ne se lance pas tout seul. Le moteur (llama.cpp, Ollama, LM Studio, vLLM) charge les nombres et calcule. Ollama et LM Studio s'appuient sur llama.cpp (LM Studio aussi sur MLX sur Mac). Il expose une **API** (l'adresse à laquelle on parle au modèle).
5. **Partie 4, le routeur (≈ 2 min)** : OpenRouter = une seule API pour des centaines de modèles (cloud). Ce qu'il facture : le prix du fournisseur sans majoration, plus 5,5 % à l'achat de crédits ; BYOK = tu apportes ta propre clé, 5 % au-delà de 25 000 $/mois d'usage gratuit. Confidentialité : il ne journalise pas tes textes par défaut, mais le fournisseur du modèle peut les garder, d'où les réglages `data_collection` et `zdr`. LiteLLM en une ligne : la même idée, à héberger chez toi. **Pas de démo avec une clé** (voir les contraintes).
6. **Partie 5, le harnais (≈ 2 min)** : ce qui donne des mains au modèle. Même définition que `brouillon-v1-grill.md` : « il peut ouvrir tes fichiers et les modifier tout seul ». La boucle (chercher du contexte → agir → vérifier), les outils, l'accès aux fichiers. Exemples : Claude Code, OpenCode, Cline, Aider, Codex CLI. À ne pas confondre avec le moteur : le moteur fait *tourner* le modèle, le harnais le *fait agir*.
7. **Fin (≈ 1 min)** : la carte complète, ton cas à toi [CROCHETS : ce que tu utilises toi, un modèle, un moteur, un harnais, à écrire par toi]. Écran de fin : la vidéo suivante de la playlist « IA chez moi », « 16 Go de VRAM suffisent-ils pour remplacer Claude ? », dès sa sortie le 16 nov. ; d'ici là, la vidéo IA la plus récente.

**Comment rester tenable pour des gens qui n'ont jamais lancé un modèle** : une seule idée par minute, un schéma par idée, jamais deux sigles dans la même phrase.

## Format : testé ou calculé ?

- **Testé (léger, avec ta RTX 5080 de 16 Go)** : ce que tu peux **montrer** sans benchmark : `ls -lh` sur tes vrais fichiers (les tailles de `modeles-5080.md`) ; le journal de chargement de llama-server (combien de couches sur la carte, combien en RAM) ; `nvidia-smi` avant / après chargement ; « celui-ci tient, celui-là déborde » (le Q4 de Qwen3.8-27B à 16,46 Go d'après `modeles-5080.md`, contre l'IQ3_S à 11,8 Go). **Ne dis « testé » que pour ce que tu as vraiment lancé** ; les essais des 23-24/10 ne sont pas encore faits au moment où j'écris.
- **Calculé / vulgarisation** : tout le reste. Dis-le dans les 30 premières secondes (règle 1 du calculé) : « aujourd'hui je ne mesure pas de vitesse, je t'apprends à lire ; les mesures, ce sera dans ma vidéo sur les 16 Go de VRAM » (elle sort le 16 nov., deux semaines après celle-ci). Les vitesses (tokens/s) : **hors sujet ici**, ne les cite pas.
- Les tailles de fichier sont celles des **pages Hugging Face** (faits 13-15), pas des mesures de ton disque : vérifie avec `ls -l` quand tu as téléchargé.

## Ce qui parle aux PC de 8 Go (63 % de ton public est en Afrique, beaucoup de petites machines)

- Dis tout de suite que la **règle de calcul marche pour n'importe quelle machine** : 4 milliards × 4,9 bits ÷ 8 ≈ 2,4 Go (Q4_K_M), donc un petit modèle en Q4 passe dans 8 Go de RAM, même sans carte graphique (plus lent). C'est un calcul, pas un test : marque-le.
- Exemple chiffré à l'écran pour un PC de 8 Go : le **Gemma 4 12B** descend à 4,21 Go en `UD-IQ2_M` et 7,12 Go en `Q4_K_M` (page Unsloth, fait 14). Le premier tient, mais à 2 bits, la qualité baisse (fait 3) ; le deuxième ne tient pas dans 8 Go avec le système et le contexte. C'est exactement la leçon « IQ2 contre Q4 » en une scène.
- Les modèles « effectifs » Gemma 4 E2B / E4B existent pour les petites machines (source secondaire seulement : à relire sur la page officielle en phase 2).
- Pas de démo qui suppose une connexion rapide ni un téléchargement de 20 Go : le public en Afrique paie la data. Dis combien pèse le fichier **avant** de l'installer, c'est tout le sujet.

## Contraintes pour la suite (de l'auteur)

- **Jamais de clé d'API collée dans un outil tiers.** Pas de démo « OpenRouter branché sur un harnais » avec une clé. À la place : (1) le site openrouter.ai (liste des modèles, filtre par prix, la page « Pricing » avec les 5,5 % et les 5 %) filmé en écran ; (2) un **schéma** de la requête : toi → routeur → fournisseur → réponse, avec une clé dessinée floue.
- **Aucun contournement ni jailbreak à l'écran.** Les modèles « abliterated » ou « uncensored » : au plus un mot dans la liste des suffixes (« ça existe, on n'en parle pas ici »), jamais de démo ni de nom de dépôt.
- **Ne montre jamais tes applis Flutter de travail** (arrière-plan du harnais, de l'éditeur, du terminal : floute ou ouvre un dossier vide).
- **Aucune anecdote personnelle inventée.** Ce que tu as vécu va entre `[CROCHETS]` : ta première fois devant un nom de fichier, ton premier modèle qui n'entrait pas, ton premier harnais. Rien n'est écrit à ta place.
- Si tu montres Claude Code branché sur un modèle local : la documentation d'Anthropic ne prend pas ce cas en charge (`modeles-5080.md`, §0.5). Dis-le, ou ne le montre pas ici (c'est le sujet de Claude #1, le 16 nov.).

## Ce qui existe déjà, pour ne pas copier (détail : `sources.md`)

- **En français, rien ne déchiffre un nom de modèle.** Les plus proches : « Chaque IA Expliquée en 19 Minutes » (Yassine Sdiri, 625 K vues, général, pas local), « FORMATION IA COMPLÈTE pour Débutants » (Michel Kartner, 76 K vues, 6 h 46, un chapitre de 6 minutes sur l'IA locale), « Faire tourner une IA en local » (Double Slash, 26 K vues, ×21, 35 min), « Cline 20/20, OpenCode 5/20 : le grand écart des harnais IA locale » (Nicefox, 7,8 K vues).
- **En anglais** : « Local AI Explained » (Tech With Tim, 821 K vues, 24 min) et « How to Run AI Locally in 2026 » (Mark Kashef, 44 min). Leur angle : « comment l'installer ». Le nôtre : « comment lire ». Ne reprends ni l'angle « 4 façons de lancer un modèle » ni les images « JPEG pour cerveaux ». La comparaison du JPEG est dans les deux : trouve la tienne (l'étiquette de vêtement ci-dessus, ou autre).
- Pas de copie de miniature : une miniature « nom de fichier découpé » n'existe chez aucun d'eux dans nos résultats (à revérifier avec une planche, voir `CLAUDE.md`, section 8).

## Points à vérifier

- **Chiffres de taille** : relis chaque fichier avec `ls -l` après téléchargement (le journal de `modeles-5080.md` les tient des pages HF, pas du disque).
- **« Qwen/Qwen3.8-27B » et ses versions ISTA** : les pages ISTA et Unsloth étaient lisibles le 23/10 ; revérifie avant le tournage si un nom ou une taille a bougé (c'est une scène à ne pas rater).
- **OpenRouter** : deux pages se contredisent presque sur le défaut de `data_collection` (« allow » dans la doc de routage, mais « pas de routage vers les fournisseurs qui journalisent, sauf réglage » dans la FAQ). Ne dis pas « c'est privé » ; dis ce que fait chaque réglage, et teste sur un compte jetable sans clé collée.
- **Llama** : Meta appelle ses modèles « open weights » ; l'OSI dit que la licence n'est pas « open source ». Cite l'OSI, ne tranche pas à sa place.
- **« Qwen est open source »** : au sens de l'OSI, il faudrait vérifier si Qwen publie l'information sur ses données. En l'état : « poids ouverts, licence Apache 2.0 » (fait 20), et on ne dit pas « pas open source » sans l'avoir vérifié (fait 21, ❓).
- **128K** : combien de tokens exactement ? (131 072 par convention, mais aucune source lue ; les cartes citent « 128K » ou 262 144.)
- **Contexte et mémoire** : le coût du contexte (cache KV) n'a pas de source primaire dans cette recherche ; les estimations de `modeles-5080.md` sont marquées « estimation ». Ne chiffre pas « 64 K = N Go » sans la phase 2.
- **Titre** : « lire le nom d'un modèle » ne répond à aucune requête mesurée (« gguf », « c'est quoi un llm » : moins de 750/mois). Le clic viendra de « ia en local » et des suggestions, pas de la recherche exacte du titre.

## Corrections de la 2e vérification (23/10)

Détail et sources : `sources.md`, colonne « 2e vérif » (lignes 1-44) et lignes 45-54 ajoutées.

- **Hook et 15 premières secondes** : « ça tient dans ma carte graphique » est **faux** : le fichier pèse 18,2 Go, ta 5080 en a 16. Il tourne parce qu'une partie des experts reste en RAM (plan de `modeles-5080.md`, pas un essai). Corrigé plus haut en « Dix-huit gigas. Ma carte graphique en a seize. [CROCHET] » : c'est plus fort, et ça pose tout de suite la question de la vidéo. Le « dix-huit gigas » est celui de Hugging Face ; Windows et `ls -lh` afficheront environ 17 Go (lignes 45, 46).
- **Règle des 30 s** : le pont disait « Dans cette vidéo-là » vers 0:25. Corrigé en « Aujourd'hui, pas d'installation » (`CLAUDE.md`).
- **Partie 1, la règle de calcul** : elle est juste, c'est le nom qui ne dit pas tout. L'en-tête du fichier `UD-IQ4_XS` de Qwen3.6 montre 59 % de nombres en IQ3_S et seulement 29,5 % en IQ4_XS : 4,10 bits en moyenne, et 35,5 × 4,10 ÷ 8 = 18,2 Go pile. Remplace « l'écart va jusqu'à 7 % » par ce moment-là : « le nom dit IQ4, mais quand on ouvre le fichier, plus de la moitié est en 3 bits » (lignes 2, 47). Dis « environ » pour les bits d'un type (Q4_K_M ≈ 4,8 à 4,9).
- **Les lettres `_M`, `_S`, `_XS`** : aucune doc ne les définit ; `_XL` n'existe que chez Unsloth. Dis « la variante, plus ou moins légère » (ligne 50).
- **128K** = 131 072 tokens, **256K** = 262 144 (`config.json` des modèles, ligne 18).
- **Partie 2, open source** : Qwen3.6 et Gemma 4 ne sont **pas** open source au sens de l'OSI (ni données ni code d'entraînement publiés), malgré leur licence Apache 2.0 : dis « poids ouverts, licence libre » (ligne 21). **Meta, elle, dit « open source »** pour Llama, pas « open weights » : la phrase des « Points à vérifier » est fausse (ligne 48). Le seuil de 700 millions d'utilisateurs se juge à la sortie de Llama 3.1 (ligne 22). L'exclusion de l'UE : l'OSI ne dit pas de quelle version, ne dis pas « Llama 4 » (ligne 23).
- **Gemma 4** : sorti le **31/03/2026** (notes de version officielles, pas le 2 avril de la presse), le 12B le 03/06/2026 ; Apache 2.0 confirmé. Les E2B/E4B « effectifs » sont confirmés par la carte de Google (ligne 49).
- **Partie 3, le moteur** : Ollama est né sur llama.cpp mais a son propre moteur depuis mai 2025 (sur la même bibliothèque GGML) ; LM Studio n'est pas open source, seul son outil `lms` l'est (lignes 40, 41).
- **Partie 4, OpenRouter** : la « contradiction » entre les deux pages n'en est pas une. `data_collection: allow` est le défaut **de la requête** (aucun filtre en plus) ; ce sont les **réglages du compte** qui décident si un fournisseur qui entraîne peut recevoir tes textes. Reste à voir sur un compte jetable comment ces interrupteurs sont réglés au départ (ligne 31). « Des centaines de modèles » : l'API en liste 469, pas 500 (ligne 27). Le même Qwen3.6-35B-A3B y est proposé : c'est ta preuve que « open » ne veut pas dire « local » (ligne 26).
- **Partie 5, harnais** : licences et modèles locaux vérifiés : OpenCode (MIT, Ollama/LM Studio/llama.cpp), Cline (Apache 2.0), Aider (Apache 2.0), Codex CLI (Apache 2.0, LM Studio et Ollama dans son code). Claude Code : Anthropic « doesn't support routing Claude Code to non-Claude models » ; que ça « marche » est un essai de tiers (ligne 43).
- **Cache KV** : il grandit en ligne droite avec le contexte, mais seulement sur les couches à attention complète (10 sur 40 chez Qwen3.6, 8 sur 48 chez Gemma 4 12B). Calcul pour Qwen3.6 en f16 : ≈ 1,3 Go à 64K. Montre le chiffre du journal de llama-server plutôt que le calcul (ligne 51).
- **Place dans la série** (mis à jour le 23/10, nuit) : la vidéo sort le 2 nov., **avant** Claude #1 (16 nov.) et Coût Claude (23 nov.), comme le conseillait déjà la recherche (`sources.md`, « Place dans la série »). C'est la porte d'entrée : elle pose le vocabulaire, et Claude #1 le met à l'épreuve sur ta carte. L'écran de fin pointe Claude #1 dès sa sortie.
- **Titres** : le 3 (recommandé) tient : 35B, A3B et Q4_K_M sont de vrais morceaux de noms, et la vidéo les explique tous. Le 2 (« Ce nom de fichier cache toute l'IA locale ») est une promesse large, mais tenable avec la carte mentale.
