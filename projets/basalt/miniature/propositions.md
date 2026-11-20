# Basalt — miniatures h / i / j

Livraison du 20 novembre 2026. Les trois accroches posent une question, **500 TOKENS/S ?** en h et j, **224 TOKENS/S ?** en i. La marque **BASALT**, avec son emblème officiel, est immédiatement accolée à chaque chiffre. Les valeurs viennent des titres des deux références de la fiche, et ne sont pas présentées comme une mesure de Technovore ni comme une vitesse générale du logiciel. Les conditions des essais de génération sur RTX 5090 figurent dans la [fiche de la vidéo](../fiche.md#chiffres-des-miniatures).

- h : fond noir, chiffre blanc, unité jaune et copie rouge ; Jim Halpert sceptique à droite.
- i : fond Technovore uni #141e27, sans visage, texte blanc et menthe à copie blanche, grands logos.
- j : même scène et même texte que h, palette Technovore ; couleurs de peau conservées.

Le couple de logos signifie **Strata → Basalt**, l'origine du fork, sans score attribué à Strata. Les deux noms sont inscrits sur des tuiles blanches ; leurs emblèmes gardent les proportions et couleurs des fichiers officiels. Une signature Basalt supplémentaire au-dessus du débit évite l'ambiguïté entre le chiffre et la tuile Strata.

Le portrait illustré de Jim Halpert est réemployé depuis `prix-apres-black-friday`, pour son regard sceptique dirigé vers le débit. Son buste est placé assez bas pour que sa coupe horizontale et ses ombres sortent sous le cadre, sans fondu ni bandeau de masquage. Aucun nouveau portrait n'a été généré.

Le style suit `.claude/skills/miniature-kai/SKILL.md`, les consignes de `ressources/miniatures/prompts-chatgpt-31-12.md` et `.claude/rules/miniatures.md`. La variante i porte 224 tandis que h et j portent 500 ; i/j modifient donc à la fois le visage et l'angle chiffré. h/j isolent bien la palette.

## Fichiers

- Maquette : `propositions/miniature-kai.html?v=h|i|j`.
- Exports : `rendus/h-kai.png`, `i-kai.png`, `j-kai.png`, 3840 × 2160, RGB.
- PSD : `photocraft/h-kai.psd`, `i-kai.psd`, `j-kai.psd`. Le décor conserve le portrait et les logos, les trois calques de texte sont éditables ; la maquette reste la source complète des objets.
- Galerie : `index.html` ; planches à 168 et 500 px dans `apercu/`.
- Test moitié basse masquée : `apercu/test-50-et-168px-kai.png` (168 px réels) et `apercu/test-50-pourcent-500px.png`.

## Reproduction

`sh projets/basalt/miniature/rendre.sh --psd` depuis la racine du dépôt. Chrome headless demande une autorisation de sortie du bac à sable dans cet environnement. Les polices sont locales, aucun service externe n'est nécessaire au rendu.

[Critique indépendante des trois versions finales](critique-kai.md)

## Contrôle terminé

La V2 PNG a été approuvée après critique indépendante : la signature Basalt a été ajoutée au-dessus de chaque débit, et l'unité ainsi que le point d'interrogation de h/j ont été remontés entièrement dans la moitié haute. Aucun PNG n'a été modifié après cette validation.

Les trois PSD ont été rouverts avec `photocraft-cli`, contrôlés par `info`, puis convertis en PNG et inspectés dans `apercu/verification-psd-500px.png`. Chacun contient **3 calques texte éditables en Archivo Black** : le chiffre, l'unité et sa copie décalée. Dimensions : 3840 × 2160 ; mode RGB 8 bits ; aucun avertissement de lecture. L'écart moyen avec les PNG de Chrome est de 0,086 (h), 0,065 (i) et 0,105 (j) sur 255, dû à la rasterisation des textes. La maquette reste la source éditable des logos, tuiles et placements.

Le bord inférieur des portraits se trouve à y766 (h) et y775 (j), au-delà des 720 px du cadre. Le test réel à 168 px conserve **BASALT, le débit, TOKENS/S et le ?** dans la moitié haute. Le détail mesuré et les empreintes SHA-256 des PNG sont enregistrés dans `apercu/verification-technique.json` ; le contrôle se relance par `python3 -I projets/basalt/miniature/verifier.py`.
