# Miniatures Kai — cout-deepseek-flash

Production du 16 novembre 2026. Fiche, script.md et sources.md lus ; le script corrigé du 16/11 prévaut sur le brief historique. Références : miniature-kai, coach-miniature-youtube, prompts-chatgpt-31-12.md, plan-kai-31-12.md, maquette commune kai-31-12.html et planche test-168px-31-12.png.

**Titre associé :** DeepSeek V4 Flash sans carte graphique : les 64 Go valent-ils leur coût ?

**Accroche :** ET LA / QUALITÉ ?

**Concept :** Une barrette de RAM, une étiquette 64 GO et la baleine officielle DeepSeek dans une tuile claire. Aucun prix ni pourcentage de perte inventé, aucun benchmark montré dans la miniature.

**Promesse :** Keanu « whoa », réaction symbolique. Le titre donne le fonctionnement sans carte graphique et le coût ; la miniature questionne la compression et sa qualité. Le script précise la version V4 Flash 0731 et la machine unique mesurée.

| Variante | Palette | Composition |
|---|---|---|
| h | jaune #ffcc33, noir ; ombres rouge et bleu | Texte à gauche, portrait illustré à droite, scène dans le bas gauche |
| i | fond uni #141e27, menthe #07c095, copie du mot accentué blanche | Sans visage ; texte en haut, scène SVG agrandie dessous |
| j | même palette Technovore que i | Même scène que h, portrait aux couleurs de peau naturelles |

Police : Archivo Black locale, installée et incluse comme référence dans le HTML. Seul le mot accentué a une copie décalée (0,055 em). h/j gardent la scène constante ; h contre j teste la palette. i change aussi le placement et l’échelle pour être une vraie version sans visage.

## Sources modifiables et reproduction

- propositions/miniature-kai.html?v=h|i|j : source HTML/CSS/SVG, scène modifiable.
- sources/ : génération brute, portraits détourés, habillages et prompts exacts avec provenance.
- rendre.sh : rendu Chrome 3840 × 2160 avec profil temporaire ; `./rendre.sh --psd` refait également les PSD.
- export-psd.py : importe l’outil commun psd.py et lui donne un profil Chrome temporaire ; pas de modification du script commun.
- photocraft/{h,i,j}-kai.psd : décor raster + 3 calques de texte modifiables (ligne blanche, copie décalée, mot accentué). Pour modifier les objets ou le portrait séparément, utiliser le HTML/SVG et les PNG sources puis réexporter.

## Contrôles de production

Rendus PNG 4K contrôlés. Comparaison des trois variantes à 168 px : apercu/comparaison-168px.png. Test de la moitié basse masquée : apercu/comparaison-50-pourcent.png ; le texte et le haut du visage restent reconnaissables. Aucun objet essentiel dans le coin inférieur droit destiné à la durée. Fond i/j uniforme. Portraits générés dans le style des prompts de l’auteur, sans reprise d’une photo protégée.

Relecture finale indépendante : critique-independante.md est fournie par un autre agent après observation des trois rendus. Le classement de clic reste une hypothèse ; le test A/B/C réel fait foi.

## Validation finale

Les trois PSD ont été reconvertis par photocraft-cli : résolution 3840 × 2160, écart moyen par canal avec les PNG entre 0,03 et 0,08 sur 255. Preuves : apercu/h-psd-verifie.png, i-psd-verifie.png, j-psd-verifie.png. Les trois textes sont modifiables en Archivo Black ; le décor et les objets restent dans la source HTML/SVG.

Première revue indépendante reçue de l’agent lot_usages avant ajout des logos. Revue ciblée des vrais logos terminée par l’agent lot_materiel : [critique-logos.md](critique-logos.md), avec contrôle des actifs primaires et empreintes finales des trois PNG. Aucun point bloquant. La critique initiale reste dans critique-independante.md et précède cette retouche. Le choix de miniature reste à trancher par le public.

## Reconnaissance du modèle — demande finale

Les trois variantes montrent désormais le vrai logo du modèle. Qwen est intégré au fichier existant pour éviter un élément de plus ; DeepSeek remplace les mots DEEP / SEEK par sa baleine officielle. Les vrais tracés et leurs couleurs sont conservés dans h, i et j : les palettes de chaîne modifient seulement le décor, les objets et leurs ombres. Provenance et empreinte du SVG : sources/logos-provenance.md.

PNG 4K, PSD et planches 168 px / moitié masquée régénérés après la modification. Les repères de fichier, mémoire et qualité ne deviennent pas des gains ou benchmarks supplémentaires. Les contrôles techniques de la version finale avec logos sont consignés ci-dessous.

Contrôle de reconversion de chaque PSD et empreintes finales : [validation-logos.md](validation-logos.md).
