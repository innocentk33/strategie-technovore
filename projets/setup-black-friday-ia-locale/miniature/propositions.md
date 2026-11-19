# Miniatures — PC complet pour IA locale, Black Friday

Série h/i/j du 20/11/2026. Base factuelle : fiche du projet, cinq budgets de **500, 800, 1 000, 1 500 et 2 000 € pour la tour**. La fiche ne comporte pas encore de paniers calculés à chacun de ces montants : l’image représente des budgets, pas des offres disponibles.

**Accroche : BLACK FRIDAY / PC POUR L’IA.**

**Étiquette : 5 BUDGETS — 500 À 2 000 €.** La fourchette résume les cinq paliers sans faire croire qu’ils se limitent à trois. Pas de remise inventée, prix barré, disponibilité promise ni réduction en pourcentage.

Une tour entière est montrée, avec la carte graphique à l’intérieur : la vidéo concerne aussi le processeur, la carte mère, la RAM, le SSD, l’alimentation, le refroidissement et le boîtier. « PC » désigne ici la tour complète, pas un ensemble écran/clavier. La tour illustrée est une représentation générique, pas un modèle ni un panier précis promis à 500 €.

## Les trois variantes

- **h** : palette Kai, fond noir calme, blanc/jaune, copie rouge décalée et ombres rouge/bleue. Tour illustrée entière à droite.
- **i** : fond uni #141e27, menthe #07c095, copie blanche ; tour entière SVG à gauche avec composants visibles et étiquette à droite.
- **j** : même tour illustrée et composition que h, palette Technovore, copie blanche ; les couleurs réelles de l’illustration du matériel restent intactes.

C’est le **cas matériel pur** prévu par le skill miniature-kai : la tour remplace le portrait humain dans h/j. Aucun visage n’est ajouté comme décor. h/j compare la palette ; i compare une autre composition et l’illustration à plat, pas le seul effet d’un visage.

Archivo Black locale. Texte en haut ou à gauche, espace net entre l’étiquette et la tour. Le Black Friday est écrit, la silhouette pointue et perforée de l’étiquette reprend un repère de magasin sans annoncer de réduction. Le coin de durée ne cache aucune information indispensable.

## Sources et références

Charte `.claude/skills/miniature-kai/SKILL.md`, règles `.claude/rules/miniatures.md`, base explicite `ressources/miniatures/prompts-chatgpt-31-12.md` (prompt PC gamer), bibliothèque déjà produite et maquette de référence `ressources/miniatures/propositions/kai-31-12.html`. Pas de nouvelle génération d’image : réemploi autorisé de la tour illustrée du projet mac-mini-ia, copies locales, provenance et empreintes dans `sources/provenance.md` et `sources/manifest.json`. Les contours des pieds du boîtier sont le contour naturel du matériel, pas le bord rectangulaire d’une photo de portrait.

## Reproduction et fichiers modifiables

- `propositions/miniature-kai.html?v=h|i|j` : maquette 1280×720, objet SVG modifiable dans i, image détourée séparée dans h/j.
- `./rendre-kai.sh` : trois PNG 3840×2160 ; variantes ciblables par `h`, `i` ou `j`.
- `./rendre-kai.sh --psd` : PSD via `export-kai-psd.py`, outil commun psd.py et CLI PhotoCraft, avec profil Chrome temporaire. Le cache Python commun est désactivé.
- `photocraft/{h,i,j}-kai.psd` : décor raster + **5 calques de texte modifiables** : événement, ligne accentuée et sa copie, légende et montant du budget.
- `python3 verifier-kai.py --convert` : rouvre les PSD avec PhotoCraft, reconstruit les planches 168 px/50 %/640 px et le JSON de validation.
- `apercu/kai/verification-psd.png` et `verification-technique.json` : comparaison des rendus et empreintes finales.

## Relecture et test

Les trois PNG sont soumis à un autre agent utilisant le coach-miniature-youtube ; rapport dans `critique-kai.md`, avec les SHA-256 des versions vues. Aucun gagnant de CTR prévu. Le test h/i/j reste une comparaison de propositions sous le même titre, pas une publication automatique.
