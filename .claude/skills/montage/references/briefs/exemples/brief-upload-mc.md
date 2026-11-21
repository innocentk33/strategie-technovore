Tu prépares le kit d'upload YouTube **et** les sous-titres FR / EN de la vidéo Technovore « Même carte, 2 fois plus rapide ». Réponds et écris en français, en tutoyant l'auteur (comme les autres documents du dépôt). Ne commite rien. N'écris que les trois fichiers demandés (plus tes fichiers de travail dans `/private/tmp/claude-501/-Users-innocent-Dev-youtubeSkill/faba7d5d-1ace-458b-9af0-6094e0041d17/scratchpad/upload-mc/`).

## Où et quoi
- Dépôt : `/Users/innocent/Dev/youtubeSkill` (lis son `CLAUDE.md`, puis le skill `.claude/skills/upload/SKILL.md` : tu le suis).
- Projet : `projets/meme-carte-plus-rapide/` (`script.md`, `sources.md`, `fiche.md`, `teleprompteur.txt`, `miniature/`).
- Modèle de forme le plus récent : `projets/strata-test/upload.md` et ses `strata-test.fr.srt` / `.en.srt` (l'auteur a validé ce format : **description courte et précise**, pas 5 000 caractères).
- Vidéo finale : `/Users/innocent/HyperStudio/premium-noir/2026-11-meme-carte-plus-rapide/renders/mc-montage-v5-4k.mp4` : 3840×2160, 30 i/s, 463,5 s (7:43). Sortie prévue : **jeu. 19 nov. 2026, 18 h** (`calendrier.md`).
- Ce que dit la voix finale, mot à mot avec les temps (voix = vidéo, la voix démarre à 0 s ; la vidéo finit 9 s après la voix) : `/Users/innocent/HyperStudio/premium-noir/2026-11-meme-carte-plus-rapide/sources/voix.words.json` et `voix.phrases.json`. Plan par plan : `.../STORYBOARD.md`. Chapitres du montage : `.../chapitres.txt` (00:00 Introduction, 00:42 Le MTP, le réglage qui double, 02:16 Le fichier qui tient dans la carte, 03:24 Le moteur, et sa version, 04:17 Quand le modèle déborde : les experts, 04:50 Le piège : la conversation longue, 05:33 Le cache KV compressé, 06:42 La liste, dans l'ordre, 07:26 À la prochaine). Tu peux les rendre plus parlants et mieux référencés, mais chaque temps doit tomber sur le début d'une phrase de la voix (vérifie dans voix.words.json). Règles YouTube : premier à 0:00, au moins 3, chacun ≥ 10 s.
- La voix finale s'écarte un peu du script : l'auteur n'a pas dit « Moi, j'ai rien testé » ; il dit « ma vidéo précédente » (Strata) ; la fin parle de la vidéo 8 Go « plus tard » ; il vouvoie à la toute fin. Fie-toi à la voix, pas au script.

## 1. `projets/meme-carte-plus-rapide/upload.md`
Comme `strata-test/upload.md` :
1. **Mots-clés** (tableau) : vidIQ si possible (forfait gratuit, 150 crédits par mois : dépense peu, note les crédits). Les outils vidIQ peuvent ne pas être chargés : cherche-les avec ToolSearch (« vidiq keyword », « vidiq outliers », « vidiq youtube search ») ; sinon réutilise les relevés datés des kits voisins et dis-le. Date chaque chiffre vidIQ.
2. **Titres** : le titre du calendrier, plus 1 ou 2 variantes au plus, en vérifiant que la vidéo tient chaque promesse. (Le test A/B des miniatures se fait avec un seul titre.)
3. **Description courte** (bloc de code prêt à coller) : 2 premières lignes fortes ; CHAPITRES ; les sources principales en liens (seulement des projets, sites et dépôts : llama.cpp, LM Studio, Ollama, Unsloth / Hugging Face…, d'après `sources.md`) ; les musiques (vérifie dans `/Users/innocent/HyperStudio/premium-noir/style/media.json` : music-minimal et music-tension) ; l'appel à commenter et l'abonnement à la manière des kits précédents ; 3 hashtags. Corps court (≈ 600 à 1 200 caractères hors chapitres et liens), total < 5 000 caractères : compte par script. Une courte section « PRÉCISIONS » (3 lignes au plus) si la voix dit quelque chose d'approximatif par rapport à `sources.md`.
4. **Tags** (bloc de code, ≤ 500 caractères).
5. **Section « Suggestions »** du skill : vidéos hôtes françaises du mois (vidIQ si disponible), planche (`ressources/miniatures/planches.py --suggestions`, miniatures dans `miniature/rendus/`), comparaison à 168 px, enchaînement. **Écran de fin** : le montage montre la vidéo Strata à gauche (« Je l'ai testé chez moi ») et la vidéo « 16 Go de VRAM suffisent » à droite, pendant les ~11 dernières secondes (≈ 7:32 à 7:43) ; trouve leurs URL dans `README.md`.

## 2. Sous-titres
- `projets/meme-carte-plus-rapide/meme-carte-plus-rapide.fr.srt` et `.en.srt` (traduction naturelle et orale, au « you », **mêmes numéros et mêmes temps** que le français).
- Sous-titre ce qui est **dit** (voix.words.json), avec l'orthographe et la ponctuation du téléprompteur quand le texte est le même. Les nombres peuvent être en chiffres.
- SRT valide (UTF-8, `HH:MM:SS,mmm --> HH:MM:SS,mmm`, ligne vide entre blocs) ; ≤ 2 lignes d'environ 42 caractères (jamais > 46) ; bloc de 0,8 à 7 s ; pas de chevauchement ; un bloc commence à son premier mot et finit à son dernier (+0,1 à 0,2 s si ça ne chevauche pas).
- Noms justes : Qwen 3.8 27B, llama.cpp, LM Studio, Ollama, Unsloth, MTP, KV, VRAM, tokens/s, RTX 5060 Ti, 4060 Ti, 5080, RX 9060 XT, NVIDIA ; Go (fr) → GB (en) ; nombres anglais au format anglais.
- Contrôle par script : mêmes blocs et temps dans les deux fichiers, temps croissants, aucun bloc hors de [0 ; 463,5 s], durées dans les bornes, aucune ligne > 46 caractères, ≥ 98 % des mots de voix.words.json couverts. Relis tout le français : voix.words.json peut contenir des erreurs de transcription ; corrige-les avec le téléprompteur et liste celles dont tu doutes.

## Règles de l'auteur
- Aucun nom de chaîne YouTube, pseudo de créateur ou nom de personne dans la description ni les sous-titres. Pas de chemin de dossier ni de clé.
- Rien d'inventé : chaque chiffre est tenu par la voix finale et `sources.md`.
- Sous la description, quelques puces de justification seulement.

## Ta réponse finale (courte)
Les trois chemins, le titre recommandé, le nombre de caractères de la description, le nombre de blocs des sous-titres et les résultats des contrôles, les crédits vidIQ dépensés, et ce que tu n'as pas pu vérifier ou dont tu doutes.
