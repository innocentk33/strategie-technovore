Tu prépares le kit d'upload YouTube **et** les sous-titres FR / EN de la vidéo Technovore « Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? ». Réponds et écris en français, en tutoyant l'auteur (comme les autres documents du dépôt). Ne commite rien. N'écris que les trois fichiers demandés (plus tes fichiers de travail dans `/private/tmp/claude-501/-Users-innocent-Dev-youtubeSkill/faba7d5d-1ace-458b-9af0-6094e0041d17/scratchpad/upload-8go/`).

## Où et quoi
- Dépôt : `/Users/innocent/Dev/youtubeSkill` (lis son `CLAUDE.md`, puis le skill `.claude/skills/upload/SKILL.md` : tu le suis).
- Projet : `projets/qwen-27b-8go/` (`script.md`, `sources.md`, `fiche.md`, `teleprompteur.txt`, `miniature/`).
- Modèles de forme les plus récents : `projets/meme-carte-plus-rapide/upload.md` (le plus proche) et `projets/strata-test/upload.md`, avec leurs sous-titres (l'auteur a validé ce format : **description courte et précise**, pas 5 000 caractères).
- Vidéo finale : `/Users/innocent/HyperStudio/premium-noir/2026-11-qwen-27b-8go/renders/q8-montage-final-4k.mp4` (en cours de finition ; la v2 1080p `renders/q8-montage-v2.mp4` a les mêmes temps) : 3840×2160, 30 i/s, 352,1 s (5:52). Sortie prévue : **lun. 23 nov. 2026, 18 h** (`calendrier.md`).
- Ce que dit la voix finale, mot à mot avec les temps (voix = vidéo, la voix démarre à 0 s ; la vidéo finit 9 s après la voix (voix : 343,1 s)) : `/Users/innocent/HyperStudio/premium-noir/2026-11-qwen-27b-8go/sources/voix.words.json` et `voix.phrases.json`. Plan par plan : `.../STORYBOARD.md`. Chapitres du montage : `.../chapitres.txt` (00:00 Introduction, 00:29 Ce que ça change en vrai, 01:07 Pourquoi ça va plus vite, 01:56 Le premier prix : la place, 03:15 Le deuxième prix : la qualité, 04:20 Et dans LM Studio ?, 04:36 Le verdict par usage, 05:35 À la prochaine). Tu peux les rendre plus parlants et mieux référencés, mais chaque temps doit tomber sur le début d'une phrase de la voix (vérifie dans voix.words.json). Règles YouTube : premier à 0:00, au moins 3, chacun ≥ 10 s.
- La voix finale s'écarte du script : question d'accroche au début (« Est-ce qu'un modèle de 27 milliards… Eh ben en fait, oui. »), « Moi, c'est du charabia », « une diète incroyable », « publié par Unsloth le 11 novembre » (sources.md : mise à jour annoncée le 11/11), « c'est top qualité » pour discuter, fin au « vous » avec un 2e appel à s'abonner ; **il n'annonce pas la vidéo de jeudi**. « 2 fois sur 3 » est mal articulé à 5:09 (sonne « sur toi ») : écris « 2 fois sur 3 ». Fie-toi à la voix, pas au script.

## 1. `projets/qwen-27b-8go/upload.md`
Comme `strata-test/upload.md` :
1. **Mots-clés** (tableau) : vidIQ si possible (forfait gratuit, 150 crédits par mois : dépense peu, note les crédits). Les outils vidIQ peuvent ne pas être chargés : cherche-les avec ToolSearch (« vidiq keyword », « vidiq outliers », « vidiq youtube search ») ; sinon réutilise les relevés datés des kits voisins et dis-le. Date chaque chiffre vidIQ.
2. **Titres** : le titre du calendrier, plus 1 ou 2 variantes au plus, en vérifiant que la vidéo tient chaque promesse. (Le test A/B des miniatures se fait avec un seul titre.)
3. **Description courte** (bloc de code prêt à coller) : 2 premières lignes fortes ; CHAPITRES ; les sources principales en liens (seulement des projets, sites et dépôts : la page Hugging Face du fichier, la doc Unsloth, la doc LM Studio, llama.cpp, d'après `sources.md`. **La mesure vient d'une vidéo YouTube d'un autre créateur : ne nomme pas sa chaîne ; un lien vers la vidéo source est permis seulement si l'URL ne contient aucun nom, sinon « une mesure publiée le 13/11 »**) ; les musiques (vérifie dans `/Users/innocent/HyperStudio/premium-noir/style/media.json` : music-minimal et music-tension) ; l'appel à commenter et l'abonnement à la manière des kits précédents ; 3 hashtags. Corps court (≈ 600 à 1 200 caractères hors chapitres et liens), total < 5 000 caractères : compte par script. Une courte section « PRÉCISIONS » (3 lignes au plus) si la voix dit quelque chose d'approximatif par rapport à `sources.md`.
4. **Tags** (bloc de code, ≤ 500 caractères).
5. **Section « Suggestions »** du skill : vidéos hôtes françaises du mois (vidIQ si disponible), planche (`ressources/miniatures/planches.py --suggestions`, miniatures dans `miniature/rendus/`), comparaison à 168 px, enchaînement. **Écran de fin** : le montage montre « Même carte, 2 fois plus rapide » à gauche (« Le réglage qui double », sortie jeu. 19/11 : son URL n'est peut-être pas encore dans `README.md`, laisse un emplacement à remplir) et la vidéo « 16 Go de VRAM suffisent » à droite, de 5:35 à 5:52 ; trouve les URL dans `README.md`. La vidéo suivante du calendrier (cartes par budget, jeu. 26/11) n'est pas annoncée dans la voix : mentionne-la seulement dans les suggestions.

## 2. Sous-titres
- `projets/qwen-27b-8go/qwen-27b-8go.fr.srt` et `.en.srt` (traduction naturelle et orale, au « you », **mêmes numéros et mêmes temps** que le français).
- Sous-titre ce qui est **dit** (voix.words.json), avec l'orthographe et la ponctuation du téléprompteur quand le texte est le même. Les nombres peuvent être en chiffres.
- SRT valide (UTF-8, `HH:MM:SS,mmm --> HH:MM:SS,mmm`, ligne vide entre blocs) ; ≤ 2 lignes d'environ 42 caractères (jamais > 46) ; bloc de 0,8 à 7 s ; pas de chevauchement ; un bloc commence à son premier mot et finit à son dernier (+0,1 à 0,2 s si ça ne chevauche pas).
- Noms justes : Qwen 3.8 27B (Qwen 27B à l'oral), UD-IQ2_XS, Unsloth, GTX 1080 Ti, llama.cpp, LM Studio, LiveCodeBench, DeepSWE, MTP, cache KV, VRAM, tokens/s ; Go (fr) → GB (en) ; nombres anglais au format anglais.
- Contrôle par script : mêmes blocs et temps dans les deux fichiers, temps croissants, aucun bloc hors de [0 ; 352,1 s], durées dans les bornes, aucune ligne > 46 caractères, ≥ 98 % des mots de voix.words.json couverts. Relis tout le français : voix.words.json peut contenir des erreurs de transcription ; corrige-les avec le téléprompteur et liste celles dont tu doutes.

## Règles de l'auteur
- Aucun nom de chaîne YouTube, pseudo de créateur ou nom de personne dans la description ni les sous-titres. Pas de chemin de dossier ni de clé.
- Rien d'inventé : chaque chiffre est tenu par la voix finale et `sources.md`.
- Sous la description, quelques puces de justification seulement.

## Ta réponse finale (courte)
Les trois chemins, le titre recommandé, le nombre de caractères de la description, le nombre de blocs des sous-titres et les résultats des contrôles, les crédits vidIQ dépensés, et ce que tu n'as pas pu vérifier ou dont tu doutes.


Rappel de l'appel à l'abonnement (règle `.claude/rules/script.md`) : vidéo d'achat/choix de carte → dans la description, le bloc « abonne-toi » peut reprendre « Si cette vidéo t'a aidé à faire le bon choix pour ta carte, abonne-toi. » (ce que dit la voix).
