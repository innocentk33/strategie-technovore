Tu prépares le kit d'upload YouTube **et** les sous-titres FR / EN de la vidéo Technovore « 32 Go pour Qwen 27B : les prix, les routes et leurs pièges ». Réponds et écris en français, en tutoyant l'auteur (comme les autres documents du dépôt). Ne commite rien. N'écris que les trois fichiers demandés (plus tes fichiers de travail dans `<TMP>/upload-32go/`).

## Où et quoi
- Dépôt : `<DEPOT>` (lis son `AGENTS.md`, puis le skill `.claude/skills/upload/SKILL.md` : tu le suis).
- Projet : `projets/deux-cartes-occasion/` (`script.md`, `sources.md`, `recherche/prix-20-11.md`, `fiche.md`, `teleprompteur.txt`, `miniature/`).
- Modèles de forme les plus récents : `projets/qwen-27b-8go/upload.md` (le plus proche) et `projets/meme-carte-plus-rapide/upload.md`, avec leurs sous-titres (l'auteur a validé ce format : **description courte et précise**).
- Vidéo finale : `<PREMIUM>/2026-11-qwen-27b-32go/renders/q32-montage-final-4k.mp4` (en cours de rendu ; la dernière 1080p de `renders/` a les mêmes temps). Sortie prévue : **lun. 30 nov. 2026, 18 h** (`calendrier.md`).
- Ce que dit la voix finale (voix clonée de l'auteur), mot à mot avec les temps (voix = vidéo, la voix démarre à 0 s ; la vidéo finit environ 11 s après la voix) : `<PREMIUM>/2026-11-qwen-27b-32go/sources/voix.words.json` et `voix.phrases.json`. Plan par plan : `.../STORYBOARD.md`. Chapitres du montage : `.../chapitres.txt`. Tu peux les rendre plus parlants et mieux référencés, mais chaque temps doit tomber sur le début d'une phrase de la voix (vérifie dans voix.words.json). Règles YouTube : premier à 0:00, au moins 3, chacun ≥ 10 s. La durée exacte : `ffprobe` sur la vidéo.
- La voix suit le téléprompteur. **Les prix sont ceux relevés le 20/11/2026** (TTC affichés, marchand nommé) : la description doit le dire clairement, et préciser qu'ils ont pu changer (Black Friday le 27/11). Le 21/11, l'offre Amazon de la RX 9060 XT (699,99 €) n'était plus en ligne : une ligne dans « PRÉCISIONS ».
- La carte d'Afrique vient de svg-maps (@svg-maps/world, licence CC BY 4.0) : crédit obligatoire dans la description (« Carte : svg-maps, CC BY 4.0 »).
- Les liens des offres : ceux de `recherche/prix-20-11.md` (marchands : Amazon, LDLC, GMKtec ; pas de lien leboncoin vers une annonce de particulier). Pas de lien d'affiliation. Sources de faits : service-public.fr (garantie légale, vices cachés, rétractation), blog NVIDIA CUDA 13, README llama.cpp, guide AMD, page Hugging Face du modèle.

## 1. `projets/deux-cartes-occasion/upload.md`
Comme `qwen-27b-8go/upload.md` :
1. **Mots-clés** (tableau) : vidIQ si possible (forfait gratuit, 150 crédits par mois : dépense peu, note les crédits). Les outils vidIQ peuvent ne pas être chargés : cherche-les avec ToolSearch ; sinon réutilise les relevés datés des kits voisins et dis-le. Date chaque chiffre vidIQ.
2. **Titres** : le titre du calendrier, plus 1 ou 2 variantes au plus, en vérifiant que la vidéo tient chaque promesse.
3. **Description courte** (bloc de code prêt à coller) : 2 premières lignes fortes ; CHAPITRES ; les prix du 20/11 en liste courte (carte, prix, marchand) ; les sources principales en liens ; les musiques (vérifie dans `<PREMIUM>/style/media.json` : music-minimal et music-tension) ; le crédit de la carte ; l'appel à commenter et l'abonnement (la voix dit : « Si cette vidéo t'a évité un mauvais achat, abonne-toi. ») ; 3 hashtags. Total < 5 000 caractères : compte par script. « PRÉCISIONS » (3 lignes au plus).
4. **Tags** (bloc de code, ≤ 500 caractères).
5. **Section « Suggestions »** du skill : vidéos hôtes françaises du mois (vidIQ si disponible), planche (`ressources/miniatures/planches.py --suggestions`, miniatures dans `miniature/`), comparaison à 168 px, enchaînement. **Écran de fin** : le montage montre « Qwen 27B sur 8 Go » à gauche et « Le setup par budget » (sortie jeu. 26/11) à droite, sur les ~11 dernières secondes ; trouve les URL dans `README.md` (laisse un emplacement à remplir si elles n'y sont pas).

## 2. Sous-titres
- `projets/deux-cartes-occasion/deux-cartes-occasion.fr.srt` et `.en.srt` (traduction naturelle et orale, au « you », **mêmes numéros et mêmes temps** que le français).
- Sous-titre ce qui est **dit** (voix.words.json), avec l'orthographe et la ponctuation du téléprompteur quand le texte est le même. Les nombres peuvent être en chiffres.
- SRT valide (UTF-8, `HH:MM:SS,mmm --> HH:MM:SS,mmm`, ligne vide entre blocs) ; ≤ 2 lignes d'environ 42 caractères (jamais > 46) ; bloc de 0,8 à 7 s ; pas de chevauchement ; un bloc commence à son premier mot et finit à son dernier (+0,1 à 0,2 s si ça ne chevauche pas).
- Noms justes : Qwen 27B, RTX 5060 Ti, RX 9060 XT, Arc A770, Arc Pro B65 / B70, Radeon AI PRO R9700, RTX 5090, Tesla V100, Mac mini M6, Ryzen AI Max+, GMKtec, LDLC, Amazon, leboncoin, llama.cpp, CUDA, 12V-2x6, PCIe ; Go (fr) → GB (en) ; prix en euros, format anglais en anglais (€1,599.98) ; « garantie légale de conformité » → « legal guarantee of conformity (France) ».
- Contrôle par script : mêmes blocs et temps dans les deux fichiers, temps croissants, aucun bloc hors de la durée de la vidéo, durées dans les bornes, aucune ligne > 46 caractères, ≥ 98 % des mots de voix.words.json couverts. Relis tout le français : voix.words.json peut contenir des erreurs de transcription ; corrige-les avec le téléprompteur et liste celles dont tu doutes.

## Règles de l'auteur
- Aucun nom de chaîne YouTube, pseudo de créateur ou nom de personne dans la description ni les sous-titres. Pas de chemin de dossier ni de clé.
- Rien d'inventé : chaque chiffre est tenu par la voix finale et `sources.md`.
- Sous la description, quelques puces de justification seulement.

## Ta réponse finale (courte)
Les trois chemins, le titre recommandé, le nombre de caractères de la description, le nombre de blocs des sous-titres et les résultats des contrôles, les crédits vidIQ dépensés, et ce que tu n'as pas pu vérifier ou dont tu doutes.


