# Miniatures — claude-code-gratuit

Créées le 16/11/2026. Sources prioritaires : fiche et script corrigé du 16/11 ; charte `.claude/skills/miniature-kai/SKILL.md`, base `ressources/miniatures/prompts-chatgpt-31-12.md`, maquette `ressources/miniatures/propositions/kai-31-12.html`.

Titre associé (script corrigé) : **Claude Code avec une IA locale : connexion, mémoire et tâches réalistes**.

Texte : **LE MÊME / CERVEAU ?**. Portrait de réaction : **Morpheus**, allusion à un meme connu, pas présence de l’acteur dans la vidéo.

La connexion à Claude Code ne démontre pas une équivalence avec un modèle Claude. Le script distingue interface, moteur et modèle.

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

## Correction logos réels — 16/11/2026

À la demande de l’auteur, les marques sont identifiées par leurs SVG véritables. Provenance et empreintes dans `sources/logos-provenance.md`. Logo Claude original placé dans le terminal CLAUDE CODE, puce distincte marquée LOCAL. PNG, PSD, planches et empreintes sont régénérés après cette modification ; la critique précédente est remplacée par une relecture indépendante des nouvelles versions.

Vérification après correction des logos : les 3 PSD ont été recréés puis rouverts et comparés visuellement aux PNG ; 3 calques texte modifiables conservés. `apercu/validation-technique.json` contient les nouvelles empreintes et mesures. Le logo Claude est orange #D97757, copie de la source Strata existante, et reste associé au terminal Claude Code.


## Correction du bord inférieur — 20/11/2026

Un trait horizontal de contour sous le buste h/j a été supprimé en décalant le portrait de 20 px vers le bas, dans la maquette reproductible. PNG/PSD et aperçus locaux réexportés, variante i identique. [Rapport et hashes finaux](apercu/audit-bord-2026-11-20/rapport.md).
