# Correction du bord inférieur — 20/11/2026

Défaut confirmé visuellement sur h/j : un trait horizontal rouge (h) ou menthe (j) passait au bord inférieur, sous toute la coupe droite du buste. Il provenait du contour et de l’ombre de l’asset détouré ; il ne faisait pas partie du vêtement.

Correction reproductible : dans `propositions/miniature-kai.html`, le portrait passe de `top:10px` à `top:30px`, à taille identique de 730 px. La coupe droite et ses ombres passent entièrement sous le cadre ; la silhouette du vêtement continue naturellement jusqu’au bord. Texte, logos, décor et variante i restent inchangés.

Les quatre rendus h/j du lot ont été réexportés en PNG et PSD 4K. Ce projet conserve trois calques Type Archivo Black par PSD ; les PSD ont été réouverts et comparés aux PNG. Contrôles complets dans [verification.json](verification.json) et [../validation-technique.json](../validation-technique.json). Variante i : hashes PNG/PSD inchangés, vérifiés.

| Variante | Plus long trait de couleur bas 12 px avant | Après | SHA-256 PNG final |
|---|---:|---:|---|
| h | 1922 px | 0 px | `6b3e0c9ad13fe91d527d2f0ea2565c0ebecf29e768bebef8c8d23cdae084c79a` |
| j | 1916 px | 0 px | `60890b751fe1c3da94ed32f3ca2ed233c6e9fcf28b2752af0a125c0e631fce22` |

La mesure est un témoin ciblé sur la couleur d’accent, pas un détecteur universel de bordure. Comparaison visuelle : [avant-apres-bord.png](avant-apres-bord.png). Sources précédentes des PNG dans `avant/`. Comparaisons 168 px / 50 %, 640 px, reconversions PSD et planches coach locales actualisées.

Reproduire : `./rendre.sh h j`, puis `python3 -I export-psd.py h j`. La revue indépendante des nouvelles images est réalisée et approuvée par lot_modeles : h/j validées après observation de la composition et du bord inférieur, empreintes complètes dans critique-independante.md et critique-logos.md. Les critiques du 16/11 restent des traces de leur ancienne version.
