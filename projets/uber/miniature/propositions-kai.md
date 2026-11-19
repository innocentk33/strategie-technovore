# Miniatures Kai — uber

Nouvelle série du 19/11/2026, ajoutée aux variantes anciennes conservées. Aucune modification du script, du titre publié ou de YouTube.

**Titre associé :** La carte d’Uber est une illusion (et c’est génial)

**Accroche :** VRAIMENT / LÀ ?

**Scène :** Une voiture pleine et son contour fantôme sur un plan dessiné : la question porte sur la position affichée, pas sur le prix de la course.

**Réaction :** Travolta perplexe : il cherche où se trouve la voiture.

## Promesse tenue

Le script suit trouver/envoyer/afficher ; §4 traite les erreurs GPS, les messages retardés et la position en partie devinée. La scène est une illustration conceptuelle, pas une capture ni une preuve de voitures fictives en 2026. La question reste ouverte ; aucun 17 min historique présenté comme actuel, aucun tarif et aucune vitesse inventés.

## Trois variantes

| Variante | Direction |
|---|---|
| h | Noir calme, blanc et jaune #ffcc 33, copies rouge/bleue, portrait illustré à droite regardant vers le texte. |
| i | Fond uni #141 e 27, menthe #07 c 095, copie blanche ; sans visage, texte en haut et scène agrandie. |
| j | Même composition que h, Technovore, peau naturelle, contour clair, menthe et copie blanche. |

Archivo Black locale. Copie décalée seulement sur la ligne accentuée. Espace net entre lettres/copie et objets. Le coin inférieur droit ne porte aucun élément indispensable.

## Sources et références

Base de prompts explicite : `ressources/miniatures/prompts-chatgpt-31-12.md` ; skill `.claude/skills/miniature-kai/SKILL.md`, règles `.claude/rules/miniatures.md` et coach-miniature-youtube. Maquette de référence `ressources/miniatures/propositions/kai-31-12.html` et planche `images/test-168 px-31-12.png`. Les anciennes références hors niche du projet sont conservées et relues : pas de nouvelle scène copiée d’une autre chaîne.

Portrait réemployé de la bibliothèque utilisateur, projet `choisir-moteur`, avec accord explicite dans la session. Les tentatives Jack Sparrow et Doc Brown ont été refusées automatiquement par image_gen ; aucun portrait nouveau ni placeholder n’est prétendu. Prompt et provenance d’origine conservés dans `sources/`. Réemploi documenté dans `sources/provenance-kai.md`.

Le véritable logo provient de `ressources/miniatures/logos/uber.svg` : fichier copié exactement sous `sources/uber-wordmark.svg`, proportions et couleurs conservées. Logos nominativement utilisés, sans affiliation suggérée.

## Sources modifiables et reproduction

- `propositions/miniature-kai.html?v=h|i|j` : maquette 1280 × 720, SVG modifiable et textes HTML.
- `rendre-kai.sh` : PNG 3840 × 2160 avec profil Chrome temporaire unique.
- `rendre-kai.sh --psd` / `export-kai-psd.py` : PSD via l’outil commun `psd.py`, sans toucher aux anciens scripts.
- `photocraft/{h,i,j}-kai.psd` : décor raster et 3 calques de texte modifiables. Les objets restent éditables dans le SVG source et les portraits PNG séparés.
- `apercu/kai/` : comparaison 640 px, planche 168 px et moitié basse masquée ; vérification des PSD rouverts et JSON technique.

## Relecture et test proposé

Contrôle visuel des 6 PNG par le producteur, puis critique indépendante par un autre agent dans `critique-kai.md`. Aucune prédiction de CTR. Test h/i/j sous le même titre, sans publication automatique. h/j teste surtout la palette ; i change aussi la mise en page et l’échelle, donc i/j compare une proposition sans visage plutôt que le seul effet du visage isolé.
