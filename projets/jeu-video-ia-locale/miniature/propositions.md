# Miniatures — jeu-video-ia-locale

Créées le 16/11/2026. Sources prioritaires : fiche et script corrigé du 16/11 ; charte `.claude/skills/miniature-kai/SKILL.md`, base `ressources/miniatures/prompts-chatgpt-31-12.md`, maquette `ressources/miniatures/propositions/kai-31-12.html`.

Titre associé (script corrigé) : **Créer un petit jeu avec une IA locale : ce que montrent 16 Go**.

Texte : **UN JEU / COMPLET ?**. Portrait de réaction : **Nicolas Cage**, allusion à un meme connu, pas présence de l’acteur dans la vidéo.

Les archives documentent du code et des prototypes ; le script ne certifie pas un workflow complet ni un jeu commercial terminé.

- h : palette Kai, jaune, ombre rouge/bleue ; portrait illustré.
- i : fond #141e27 uni, menthe et copie blanche ; aucun visage, scène SVG agrandie sous le texte.
- j : même composition que h, palette Technovore, peau naturelle et copie blanche.

Les trois variantes testent la palette puis la présence du visage. Aucun résultat de CTR prédit. Importer les trois dans « Tester et comparer ».

## Sources modifiables et reproduction

`propositions/miniature-kai.html?v=h|i|j` : textes HTML et objets SVG modifiables. `sources/` : original généré sur vert et déclinaisons détourées par `portrait.py`. `rendre.sh` : PNG 3840×2160, profil Chrome temporaire isolé. `photocraft/*-kai.psd` : décor et trois calques de texte modifiables, générés avec `psd.py` et PhotoCraft. Les objets restent modifiables dans le SVG source de la maquette.

## Génération et provenance

Outil intégré `image_gen.imagegen` (pas API/CLI). Prompt dérivé de la base utilisateur, reproduit intégralement dans `sources/prompt-portrait.md`. Le nom du meme change ; conservation des aplats, facettes, contours noirs, peau naturelle, regard vers la gauche et fond #00FF00. Image originale générée à 1254×1254 ; export final composé en 4K. Portraits utilisés comme illustrations de réaction éditoriales autorisées par la demande ; aucune licence d’acteur ni d’œuvre n’est acquise par la génération.

## Vérification

Voir `apercu/test-50-et-168px-kai.png` : trois variantes à 168 px et moitié basse masquée. Le texte principal reste dans la moitié haute ; aucun élément essentiel sous la durée en bas à droite. Critique indépendante dans `critique-independante.md` lorsqu’elle est réalisée.

Correction après critique indépendante : scène remontée de 95 px dans h/j et de 55 px dans i pour montrer davantage le sujet dans la moitié haute. Label CLAUDE CODE agrandi ; accroche moteurs précisée « TON IA / 3 OUTILS ».

Validation finale : critique indépendante du lot matériel approuvée après corrections. Les 3 PSD ont été rouverts avec PhotoCraft et comparés visuellement au PNG : `apercu/verification-psd.png`. Contrôle binaire : format PSD 3840×2160 et 3 blocs de texte éditables TySh par fichier. Mesures et SHA256 : `apercu/validation-technique.json`. Export PSD reproductible : `./rendre.sh --psd`.
