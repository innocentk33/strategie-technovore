<!-- Modèle (origine de chaque variable : ../sous-agents.md, « D’où viennent les variables »). Remplace : {{TITRE}}, {{NOM}} (dossier projets/<nom>), {{PROJET}}, {{RENDU}}, {{SORTIE}} (date et heure de publication du calendrier), {{PRECISIONS}} (dates des prix, ce qui a changé, crédits obligatoires), {{NOMS_JUSTES}} (orthographe des noms et références), {{ECRAN_FIN}} (les deux vidéos de l'écran de fin), {{SCRATCH}}. Exemples réels : exemples/brief-upload-32go.md, brief-upload-8go.md. Modèle : Sonnet. -->
Tu prépares le kit d'upload YouTube **et** les sous-titres FR / EN de la vidéo Technovore « {{TITRE}} ». Réponds et écris en français, en tutoyant l'auteur. Ne commite rien. N'écris que les trois fichiers demandés (plus tes fichiers de travail dans `{{SCRATCH}}`).

## Où et quoi
- Dépôt : `/Users/innocent/Dev/youtubeSkill` (lis son `CLAUDE.md`, puis `.claude/skills/upload/SKILL.md` : tu le suis).
- Projet : `projets/{{NOM}}/` (`script.md`, `sources.md`, `fiche.md`, `teleprompteur.txt`, `miniature/`, `recherche/`).
- Modèles de forme les plus récents : les `upload.md` et `.srt` des derniers projets publiés (l'auteur a validé : **description courte et précise**).
- Vidéo finale : `{{RENDU}}` (la dernière 1080p de `renders/` a les mêmes temps). Sortie : {{SORTIE}}.
- La voix mot à mot avec les temps (la voix démarre à 0 s ; la vidéo finit environ 11 s après) : `{{PROJET}}/sources/voix.words.json` et `voix.phrases.json`. Plan par plan : `STORYBOARD.md`. Chapitres du montage : `chapitres.txt` ; tu peux les rendre plus parlants, mais chaque temps tombe sur le début d'une phrase (vérifie dans voix.words.json) ; premier à 0:00, au moins 3, chacun ≥ 10 s. Durée exacte : `ffprobe`.
- {{PRECISIONS}}

## 1. `projets/{{NOM}}/upload.md`
Mots-clés (vidIQ si les outils sont chargés : forfait gratuit, dépense peu, note les crédits ; sinon relevés datés des kits voisins, et dis-le) ; titres (celui du calendrier + 1 ou 2 variantes que la vidéo tient) ; description prête à coller (< 5 000 caractères comptés par script : 2 premières lignes fortes, CHAPITRES, faits ou prix datés, sources en liens, musiques d'après `/Users/innocent/HyperStudio/premium-noir/style/media.json`, crédits, appel à commenter et abonnement, 3 hashtags, « PRÉCISIONS » en 3 lignes au plus) ; tags (≤ 500 caractères) ; section « Suggestions » du skill (vidéos hôtes, planche, comparaison à 168 px, enchaînement). Écran de fin : {{ECRAN_FIN}} ; URL depuis `README.md`, sinon un emplacement à remplir.

## 2. Sous-titres
`projets/{{NOM}}/{{NOM}}.fr.srt` et `.en.srt` (anglais naturel et oral, **mêmes numéros et mêmes temps**). Ce qui est **dit**, avec l'orthographe du téléprompteur ; SRT valide UTF-8 ; ≤ 2 lignes d'environ 42 caractères (jamais > 46) ; blocs de 0,8 à 7 s ; pas de chevauchement. Noms justes : {{NOMS_JUSTES}}. Contrôle par script : mêmes blocs et temps dans les deux fichiers, temps croissants, aucun bloc hors de la vidéo, ≥ 98 % des mots couverts. voix.words.json peut contenir des erreurs de transcription : corrige-les avec le téléprompteur et liste tes doutes.

## Règles de l'auteur
Aucun nom de chaîne, pseudo ou nom de personne dans la description ni les sous-titres ; pas de chemin de dossier ni de clé ; rien d'inventé (chaque chiffre tenu par la voix finale et sources.md).

## Ta réponse finale (courte)
Les trois chemins, le titre recommandé, les caractères de la description, les blocs des sous-titres et les contrôles, les crédits vidIQ dépensés, ce que tu n'as pas pu vérifier.
