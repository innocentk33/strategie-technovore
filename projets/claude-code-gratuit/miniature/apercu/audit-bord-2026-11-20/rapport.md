# Correction du bord inférieur — 20/11/2026

Défaut confirmé visuellement sur h/j : un trait horizontal rouge (h) ou menthe (j) passait au bord inférieur, sous toute la coupe droite du buste. Il provenait du contour et de l’ombre de l’asset détouré ; il ne faisait pas partie du vêtement.

Correction reproductible : dans `propositions/miniature-kai.html`, le portrait passe de `top:10px` à `top:30px`, à taille identique de 730 px. La coupe droite et ses ombres passent entièrement sous le cadre ; la silhouette du vêtement continue naturellement jusqu’au bord. Texte, logos, décor et variante i restent inchangés.

Les quatre rendus h/j du lot ont été réexportés en PNG et PSD 4K. Ce projet conserve trois calques Type Archivo Black par PSD ; les PSD ont été réouverts et comparés aux PNG. Contrôles complets dans [verification.json](verification.json) et [../validation-technique.json](../validation-technique.json). Variante i : hashes PNG/PSD inchangés, vérifiés.

| Variante | Plus long trait de couleur bas 12 px avant | Après | SHA-256 PNG final |
|---|---:|---:|---|
| h | 1922 px | 0 px | `7de1fe57cca38dc801d48e40e4f2180a9b860047e15d937152ba99baf8fb7b9c` |
| j | 1916 px | 0 px | `1cee9f7434d887ac945140fae3dbc42491a946898a2aa46c1e70816d1d91a8ef` |

La mesure est un témoin ciblé sur la couleur d’accent, pas un détecteur universel de bordure. Comparaison visuelle : [avant-apres-bord.png](avant-apres-bord.png). Sources précédentes des PNG dans `avant/`. Comparaisons 168 px / 50 %, 640 px, reconversions PSD et planches coach locales actualisées.

Reproduire : `./rendre.sh h j`, puis `python3 -I export-psd.py h j`. La revue indépendante des nouvelles images est réalisée et approuvée par lot_modeles : h/j validées après observation de la composition et du bord inférieur, empreintes complètes dans critique-independante.md et critique-logos.md. Les critiques du 16/11 restent des traces de leur ancienne version.
