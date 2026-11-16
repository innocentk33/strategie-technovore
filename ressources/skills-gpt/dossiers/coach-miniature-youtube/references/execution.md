# Exécution : de l'idée au fichier

Les noms de menus sont donnés pour Photoshop en français, avec l'anglais entre parenthèses. Photopea (gratuit, dans le navigateur) reprend la plupart des menus de Photoshop en anglais. Les noms exacts peuvent varier selon la version du logiciel : si un menu n'existe pas, décris le résultat voulu et laisse l'utilisateur chercher l'équivalent.

## Sommaire
1. Le déroulé d'Isaac
2. Techniques, outil par outil
3. Export et spécifications
4. Modèle de brief d'exécution

---

## 1. Le déroulé d'Isaac

1. **Concept** choisi (types combinés, texte, émotion).
2. **Croquis détaillé sur papier.**
3. **Nouveau document** en 16:9, avec des repères sur les lignes des tiers.
4. **Assemblage** : personnage, texte, arrière-plan, autres éléments.
5. **Style du texte** (styles de calque), enregistré pour la prochaine fois.
6. **Effets** sur les éléments : déformation, flou.
7. **Assombrir l'arrière-plan** derrière le texte et le personnage.
8. **Corriger la couleur** de l'arrière-plan (teinte/saturation).
9. **Reflets de lumière** pour intégrer le personnage dans la scène.
10. **Retouche couleur finale** (Isaac l'envoie sur son téléphone et la passe dans Lightroom).
11. **Test** en conditions réelles (voir `test.md`), et retour au croquis si ça ne ressort pas.

Ajouts utiles : prévoir au tournage la photo du visage avec la bonne expression et la bonne lumière (bien plus simple que de la truquer ensuite), et détourer proprement le sujet.

---

## 2. Techniques, outil par outil

### Repères des tiers
- **Photoshop :** Affichage > Nouvelle disposition de repères (View > New Guide Layout), 3 colonnes et 3 lignes, sans gouttière.
- **Photopea :** View > New Guide Layout fonctionne de la même façon, ou glisser des repères depuis les règles.
- **Canva :** Fichier > Paramètres > Afficher les règles et repères, puis placer les repères à 1/3 et 2/3 ; ou importer une image de grille sur un calque temporaire.
- **GIMP :** Image > Repères > Nouveaux repères (en %), à 33,3 % et 66,6 % dans les deux sens.

### Détourer le sujet
- **Photoshop :** Sélection > Sujet (Select > Subject), puis Sélectionner et masquer (Select and Mask) pour affiner les cheveux ; ou « Supprimer l'arrière-plan » dans les actions rapides du panneau Propriétés.
- **Photopea :** Select > Remove BG (détourage en un clic) ; sinon baguette magique sur un fond uni, Select > Inverse, puis masque de fusion.
- **Canva :** Modifier > Suppresseur d'arrière-plan (offre payante).
- **GIMP :** outil Sélection de premier plan, puis masque de calque.
- **Conseil :** un contour (blanc ou couleur d'accent) de quelques pixels autour du sujet détouré le détache du fond et masque un détourage imparfait.

### Styler le texte
- **Photoshop / Photopea :** double-clic sur le calque texte, à côté de son nom, pour ouvrir le style de calque (Layer Style). Effets utiles : Contour (Stroke), Ombre portée (Drop Shadow), Lueur externe (Outer Glow), Lueur interne (Inner Glow), Biseautage et estampage (Bevel & Emboss) avec parcimonie. Une fois satisfait, bouton « Nouveau style » (New Style) pour le réutiliser en un clic. Ça vaut aussi pour les autres éléments (contour du personnage, cadre).
- **Canva :** sélectionner le texte > Effets : Ombre, Contour, Relief, Néon, Arrière-plan (bandeau). Enregistrer les styles dans le kit de marque si disponible, ou dupliquer une ancienne miniature.
- **GIMP :** pas de styles de calque natifs. Contour : Calque > Transparence > Alpha vers sélection, Sélection > Agrandir, remplir sur un calque en dessous. Ombre : Filtres > Lumière et ombre > Ombre portée.
- **Réglages de départ :** texte blanc ou couleur principale, contour noir de 6 à 12 px (sur une image 1920 × 1080), ombre portée douce. Ajuster jusqu'à ce que le texte soit lisible à 168 px de large.

### Déformer un élément (courber un graphique, incliner un objet)
- **Photoshop :** Ctrl+T (transformation manuelle), puis le bouton « Basculer entre transformation et déformation » dans la barre d'options ; ou Édition > Transformation > Déformation (Edit > Transform > Warp). Tirer les poignées ou choisir une forme prédéfinie (arc, drapeau…).
- **Photopea :** Edit > Transform > Warp.
- **Canva :** pas de déformation libre ; seul le texte peut être courbé (Effets > Incurver). Pour un objet, préparer l'image déformée ailleurs.
- **GIMP :** outil Déformation interactive (Warp Transform) ou outil Cage.

### Flouter un élément gênant
- **Flou gaussien :** Filtre > Flou > Flou gaussien (Filter > Blur > Gaussian Blur). Pour calmer un arrière-plan ou des éléments secondaires qui distraient.
- **Mosaïque :** Filtre > Pixellisation > Mosaïque (Filter > Pixelate > Mosaic). Pour le type « flouté » (cacher un résultat) ou un effet stylisé.
- **Canva :** Modifier > Ajuster > Flou ; pour cacher une zone, placer un élément flou ou une forme par-dessus.
- **GIMP :** Filtres > Flou > Flou gaussien ; Filtres > Flou > Pixeliser.
- Isaac le reconnaît : un flou ne convient pas à toutes les miniatures. Essayer, comparer en petit, annuler si ça n'aide pas.

### Assombrir l'arrière-plan derrière le texte et le sujet
- **Photoshop / Photopea :** nouveau calque juste au-dessus de l'arrière-plan ; outil Pinceau, grande taille, dureté 0 %, couleur noire, flux (Flow) vers 5 %, lissage (Smoothing) élevé ; peindre par passages successifs derrière le texte, le personnage et les éléments importants. Baisser l'opacité du calque si c'est trop.
- **Alternatives :** dégradé noir vers transparent sur un calque ; vignettage (Filtre Camera Raw > Effets) ; calque de réglage Courbes avec un masque.
- **Canva :** ajouter un élément « dégradé » noir semi-transparent derrière le texte ; ou Modifier > Ajuster > Vignettage.
- **GIMP :** nouveau calque, Pinceau avec une brosse douce et une opacité faible (5-10 %), peindre en noir.

### Changer la couleur de l'arrière-plan
- **Photoshop / Photopea :** sélectionner le calque, Image > Réglages > Teinte/Saturation (Image > Adjustments > Hue/Saturation, Ctrl+U). Dans le menu déroulant, cibler une couleur précise (Rouges, Jaunes…) ou modifier toute l'image. Pour garder la modification réversible, passer par un calque de réglage.
- **Canva :** Modifier > Ajuster (teinte, saturation, température) ; certaines versions permettent de modifier une couleur précise de la photo.
- **GIMP :** Couleurs > Teinte-Saturation.
- **Objectif :** que la teinte du fond contraste avec le sujet et le texte, et colle à la palette de la chaîne.

### Ajouter des reflets de lumière
Rend un personnage détouré plus naturel dans la scène (par exemple, un texte lumineux au-dessus de sa tête devrait éclairer ses cheveux).
- **Photoshop / Photopea :** sélectionner l'élément (Ctrl+clic sur la vignette du calque), nouveau calque, pinceau doux plus petit, couleur de la source lumineuse ; peindre du côté d'où vient la lumière ; passer le mode de fusion du calque sur Incrustation (Overlay). Si ça ne rend pas bien, essayer Lumière tamisée (Soft Light) ou Densité couleur − (Color Dodge), et d'autres couleurs.
- **GIMP :** même principe, mode de calque Overlay (Superposer).
- **Canva :** possibilités limitées ; un élément « lueur » semi-transparent posé sur le bord du sujet peut suffire.

### Retouche couleur finale
- **Lightroom (mobile ou ordinateur)** comme Isaac, ou **Filtre > Filtre Camera Raw** dans Photoshop : contraste, vibrance, clarté, courbes, étalonnage.
- **Photopea / GIMP :** Courbes et Vibrance/Saturation.
- **Canva :** Modifier > Ajuster, ou un filtre léger.
- Comparer avant/après à petite taille : un léger gain de contraste et de saturation sur le sujet suffit souvent.

---

## 3. Export et spécifications

Spécifications officielles relevées en octobre 2026 (à revérifier sur l'aide YouTube si un doute existe, elles évoluent) :
- **Format :** 16:9 ; JPG ou PNG.
- **Résolution recommandée :** 3840 × 2160 ; **largeur minimale :** 640 px.
- **Poids maximal :** 2 Mo si la miniature est envoyée depuis un téléphone ; 50 Mo depuis un ordinateur.
- **Test A/B :** une miniature en dessous de 1280 × 720 fait descendre toutes les miniatures du test en 480p.

En pratique : travailler en 1920 × 1080 ou 3840 × 2160, exporter en JPG qualité 85-90 (ou PNG si le poids reste raisonnable), et garder le fichier source avec ses calques pour pouvoir corriger après un test.

---

## 4. Modèle de brief d'exécution

```
## Brief — [nom du concept]
**Document :** 1920 × 1080 (ou 3840 × 2160), repères des tiers
**Calques (de bas en haut) :**
1. Arrière-plan : [image], [flou / teinte / assombrissement]
2. Assombrissement : pinceau noir doux derrière [zones]
3. [Élément secondaire] : position [case de la grille], [effet]
4. Sujet détouré : position [intersection], contour [couleur, épaisseur]
5. Reflets : [couleur], mode Incrustation, côté [gauche/droite]
6. Texte : « [texte] », [police, graisse], [couleur], contour [x px], ombre portée, position [zone]
**Couleurs :** principale #..., accent #...
**Export :** JPG qualité 85-90, vérifier le poids
**Test :** planche d'aperçu + simulation page d'accueil (voir `test.md`)
```
