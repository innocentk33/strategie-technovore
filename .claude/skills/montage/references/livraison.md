# Livraison

## Ce que tu livres
1. La vidéo : `renders/<court>-montage-final-4k.mp4` (3840 × 2160, 30 i/s), après accord ou carte blanche (`verifications.md`).
2. Le kit d'upload et les sous-titres, dans le dépôt : `projets/<nom>/upload.md`, `projets/<nom>/<nom>.fr.srt`, `<nom>.en.srt`. Un sous-agent Sonnet les écrit en suivant le skill `upload` (brief : `briefs/modele-upload.md`), pendant le rendu 4K : la dernière 1080p a les mêmes temps.
3. La sauvegarde du projet sur GitHub, quand l'auteur valide la livraison : `git add -A && git commit` dans le dossier du projet, puis, au premier envoi, `gh repo create innocentk33/premium-noir--<dossier> --private --source=. --remote=origin --push` (ensuite `git push`). Les dépôts existants portent ce nom (`premium-noir--2026-11-qwen-27b-32go`…). Retouches suivantes : un commit par lot.
4. Ton message final (voir plus bas).

## Chapitres
`chapitres.txt` est généré par `montage.py` (un chapitre par `chap=`). Dans la description, ils peuvent être plus parlants, mais chaque temps tombe sur le début d'une phrase de la voix (`voix.words.json`). Règles YouTube : premier à 00:00, au moins 3, chacun d'au moins 10 s.

## Sous-titres
Ce qui est **dit** (`voix.words.json`), avec l'orthographe du téléprompteur ; ≤ 2 lignes d'environ 42 caractères (jamais plus de 46), blocs de 0,8 à 7 s, sans chevauchement ; l'anglais a les mêmes numéros et les mêmes temps que le français ; ≥ 98 % des mots couverts, contrôlé par script.

## Description
- Prix datés (« relevés le 20/11/2026 ») avec le marchand, et la mention qu'ils ont pu changer ; ce qui a changé depuis le relevé dans « PRÉCISIONS ».
- Crédits : musiques (kissan4, megalix, Pixabay), carte (« svg-maps, CC BY 4.0 ») si elle apparaît, bruitages CC BY si utilisés.
- La phrase d'abonnement des vidéos d'achat : « Si cette vidéo t'a évité un mauvais achat, abonne-toi. »
- Aucun nom de chaîne, de créateur ou de personne ; pas de lien d'affiliation ; liens des sources principales.
- Écran de fin : les deux vidéos montrées dans les ~11 dernières secondes ; leurs URL viennent du `README.md` (laisse un emplacement à remplir si elles n'y sont pas).

## Après la mise en ligne (à rappeler à l'auteur, pas à faire sans lui)
- Statut dans `README.md` et `calendrier.md` : « Montage » → « Programmé » quand il a programmé la vidéo, puis « Publié » avec le lien. Mets à jour **les deux** fichiers ; si tu changes le format de leurs tableaux, relance `node ressources/regie/verif.mjs`.
- À la sortie de la vidéo : le skill `radar` avant tout le reste (règle de l'`AGENTS.md` du dépôt).
- Relire les prix le jour de l'upload s'ils peuvent bouger (Black Friday…).

## Message final à l'auteur
Court, en français, en le tutoyant :
- le chemin de la vidéo, sa durée, sa définition, son niveau (LUFS, crête) ; si la 4K a été lancée sans sa relecture, dis-le ;
- les notes des critiques et ce qui a été corrigé ; ce qui n'a pas été corrigé et pourquoi ;
- ce que deviennent les éléments demandés (soupir, rire, pauses…) ;
- la liste courte et datée des passages **à écouter au casque** ;
- les chemins du kit d'upload et des sous-titres, ce qui est à coller ou à remplir (liens, écran de fin) ;
- les prix qui ont bougé depuis le relevé ;
- rien n'est committé.
