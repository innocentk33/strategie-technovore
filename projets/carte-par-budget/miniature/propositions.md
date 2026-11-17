# Miniatures h, i, j — carte-par-budget

Production du 16/11/2026. Base : `ressources/miniatures/prompts-chatgpt-31-12.md`, plan Kai du 15/11 et scripts corrigés du 16/11. Skills miniature-kai, coach-miniature-youtube et imagegen appliqués. Critique indépendante réalisée après visualisation des h/i/j par un autre agent : [critique-independante.md](critique-independante.md), verdict livrable.

**Texte : PAYER PLUS / POUR RIEN ?**

Trois cartes illustrées de tailles différentes, en escalier, sous le texte. La variante i remplace l’illustration par trois cartes SVG aux volumes croissants.

## Promesse et fidélité

Le script corrigé du 16/11 ouvre sur une carte 12 Go plus chère de 70 € qu’une 16 Go. Il explique qu’une dépense supplémentaire ne débloque pas toujours la capacité utile. La question interroge ce piège ; elle ne promet ni classement exhaustif, ni offre Black Friday, ni prix africain.

L’illustration est générique : la taille physique ne représente ni la VRAM ni le prix d’un modèle précis. Aucun tarif ni modèle commercial n’est inscrit.

## Variantes

- **h** : noir calme, blanc, jaune Kai ; copie rouge décalée du segment en couleur, ombres rouge et bleue sur le sujet.
- **i** : ardoise unie `#141e27`, menthe `#07c095`, copie blanche décalée ; aucun visage, scène SVG agrandie sous le texte en haut.
- **j** : même scène que h, fond Technovore et ombres adaptées ; couleurs naturelles du sujet conservées.

Archivo Black locale. Texte à gauche ou en haut ; aucune information essentielle dans le coin durée (x > 1130, y > 650). Matériel illustré générique pour les sujets de matériel pur.

## Fichiers et reproduction

- Maquette : [propositions/miniature-kai.html](propositions/miniature-kai.html), `?v=h`, `?v=i`, `?v=j`.
- Reproduire : `./projets/carte-par-budget/miniature/rendre.sh` depuis la racine du dépôt.
- PNG 3840 × 2160 : `rendus/h-kai.png`, `i-kai.png`, `j-kai.png`.
- PSD : `photocraft/h-kai.psd`, `i-kai.psd`, `j-kai.psd` ; décor raster et textes droits en calques de texte modifiables.
- Contrôle : `apercu/test-50-et-168px-kai.png` ; haut de la composition conservé dans le test à 50 %.
- Assets : `sources/`, prompt consigné dans [prompts-generation.md](prompts-generation.md).

Le script utilise le CLI PhotoCraft installé et le moteur commun `ressources/miniatures/psd.py`, avec un profil Chrome temporaire isolé. Le décor SVG et l’image source restent modifiables dans la maquette, les titres et labels droits dans le PSD.

## Contrôle de conception

L’hypothèse du concept : la question et le matériel se reconnaissent à 168 px. Le test de moitié haute conserve toute la question. Les h/j comparent principalement la palette ; i est une scène sans visage, à comparer séparément. Le public tranche via « Tester et comparer » h / i / j, à titre et publication constants. Pas de résultat A/B inventé.

Vérification technique finale : les douze exports du lot ont été inspectés avec `photocraft-cli info` (PNG et PSD 3840 × 2160, calques Type en Archivo Black, aucune alerte). Réouverture du PSD j et comparaison au rendu Chrome dans `apercu/comparaison-psd.png`. Détails : `apercu/verification-export.json`.
