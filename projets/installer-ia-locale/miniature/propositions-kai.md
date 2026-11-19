# Miniatures Kai — installer-ia-locale

Nouvelle série du 19/11/2026, ajoutée aux variantes anciennes conservées. Aucune modification du script, du titre publié ou de YouTube.

**Titre associé :** Pourquoi avoir ta propre IA, et comment l’installer (LM Studio)

**Accroche :** TON IA / HORS LIGNE

**Scène :** L’icône LM Studio officielle dans un écran où la réponse continue, à côté d’un câble réseau débranché.

**Réaction :** Roll Safe : geste malin, le plan B que tu contrôles.

## Promesse tenue

Le script V 3 du 25/10 suit la capture réelle du 24/10. Hook et test 2 montrent internet coupé, Google inaccessible puis Gemma qui répond. La miniature illustre ce bénéfice après téléchargement de l’application et du modèle. Elle ne promet ni installation sans internet, ni supériorité sur Claude, ni confidentialité de toutes les fonctions connectées.

## Trois variantes

| Variante | Direction |
|---|---|
| h | Noir calme, blanc et jaune #ffcc 33, copies rouge/bleue, portrait illustré à droite regardant vers le texte. |
| i | Fond uni #141 e 27, menthe #07 c 095, copie blanche ; sans visage, texte en haut et scène agrandie. |
| j | Même composition que h, Technovore, peau naturelle, contour clair, menthe et copie blanche. |

Archivo Black locale. Copie décalée seulement sur la ligne accentuée. Espace net entre lettres/copie et objets. Le coin inférieur droit ne porte aucun élément indispensable.

## Sources et références

Base de prompts explicite : `ressources/miniatures/prompts-chatgpt-31-12.md` ; skill `.claude/skills/miniature-kai/SKILL.md`, règles `.claude/rules/miniatures.md` et coach-miniature-youtube. Maquette de référence `ressources/miniatures/propositions/kai-31-12.html` et planche `images/test-168 px-31-12.png`. Les anciennes références hors niche du projet sont conservées et relues : pas de nouvelle scène copiée d’une autre chaîne.

Portrait réemployé de la bibliothèque utilisateur, projet `ram-vram-unifiee`, avec accord explicite dans la session. Les tentatives Jack Sparrow et Doc Brown ont été refusées automatiquement par image_gen ; aucun portrait nouveau ni placeholder n’est prétendu. Prompt et provenance d’origine conservés dans `sources/`. Réemploi documenté dans `sources/provenance-kai.md`.

Le véritable logo provient de `ressources/miniatures/logos/lm-studio.svg` : fichier copié exactement sous `sources/lm-studio-officiel.svg`, proportions et couleurs conservées. Logos nominativement utilisés, sans affiliation suggérée.

## Sources modifiables et reproduction

- `propositions/miniature-kai.html?v=h|i|j` : maquette 1280 × 720, SVG modifiable et textes HTML.
- `rendre-kai.sh` : PNG 3840 × 2160 avec profil Chrome temporaire unique.
- `rendre-kai.sh --psd` / `export-kai-psd.py` : PSD via l’outil commun `psd.py`, sans toucher aux anciens scripts.
- `photocraft/{h,i,j}-kai.psd` : décor raster et 3 calques de texte modifiables. Les objets restent éditables dans le SVG source et les portraits PNG séparés.
- `apercu/kai/` : comparaison 640 px, planche 168 px et moitié basse masquée ; vérification des PSD rouverts et JSON technique.

## Relecture et test proposé

Contrôle visuel des 6 PNG par le producteur, puis critique indépendante par un autre agent dans `critique-kai.md`. Aucune prédiction de CTR. Test h/i/j sous le même titre, sans publication automatique. h/j teste surtout la palette ; i change aussi la mise en page et l’échelle, donc i/j compare une proposition sans visage plutôt que le seul effet du visage isolé.
