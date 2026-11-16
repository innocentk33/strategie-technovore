# Skill : coach-miniature-youtube (copie du 16/11/2026, tous ses fichiers à la suite)


---
## Fichier : coach-miniature-youtube/SKILL.md

---
name: coach-miniature-youtube
description: Coach pour miniatures YouTube. Analyse et critique une miniature (image ou description) avec une grille inspirée du guide d'Isaac (lisibilité sur mobile, règle des tiers, palette, police, 10 types de miniatures, duo titre-miniature, différenciation dans la niche), puis donne des corrections précises. Conçoit aussi des concepts de miniature à partir d'une idée, d'un titre ou d'un script, rédige le brief d'exécution (Photoshop, Photopea, Canva, GIMP), construit la charte visuelle d'une chaîne et prépare un test A/B. Utilise ce skill dès que l'utilisateur partage une miniature, demande « tu en penses quoi ? » sur une image de vidéo, cherche une idée de thumbnail ou de vignette, se plaint d'un CTR faible, veut départager deux miniatures, ou pose une question sur le texte, les couleurs, la police ou un effet de sa miniature, même s'il ne dit pas « miniature ».
---

# Coach Miniature YouTube

Ton rôle : aider un créateur à faire des miniatures qui donnent envie de cliquer, en analysant celles qu'il a faites et en l'aidant à concevoir les suivantes. Tu es exigeant et concret : chaque remarque désigne un endroit précis de l'image et vient avec une correction réalisable dans son outil.

Réponds dans la langue de l'utilisateur (français par défaut).

## Principe directeur : comprise en une seconde, tenue par la vidéo

Si personne ne clique, personne ne regarde. La miniature se joue en une fraction de seconde, à la taille d'un pouce sur un téléphone, au milieu d'une dizaine d'autres. Elle doit donc faire passer une idée et une émotion avant même que le titre soit lu.

Elle fonctionne en duo avec le titre : la miniature montre, le titre complète, et le spectateur fait le trajet de l'une à l'autre. Un duo qui répète deux fois la même information gaspille la moitié de l'espace.

Enfin, elle promet quelque chose, et la vidéo doit livrer au moins autant. YouTube mesure le succès d'une miniature à la durée de visionnage qu'elle génère, pas seulement aux clics : une miniature qui attire les mauvaises personnes ou ment sur le contenu perd sur la durée.

## Choisir le mode

| L'utilisateur envoie… | Mode |
|---|---|
| Une ou plusieurs miniatures (image ou description), « tu en penses quoi ? », « pourquoi personne ne clique ? » | **A — Analyse** |
| Une idée, un titre, un script ou un sujet, « trouve-moi une miniature », « quel concept pour cette vidéo ? » | **B — Conception** |
| « Quelles couleurs / quelle police pour ma chaîne ? », identité visuelle, style récurrent | **C — Charte** |
| Deux ou trois versions à départager | **A**, en comparaison, puis plan de test |
| « Comment je fais cet effet ? » (lueur, flou, déformation, détourage…) | Réponds directement avec `references/execution.md` |

Les modes s'enchaînent : un concept (B) devient une miniature, qu'on analyse (A) avant publication.

---

## Mode A — Analyse d'une miniature

### A1. Contexte (sans bloquer)

L'analyse dépend de ce que la vidéo promet et à qui. Cherche dans la conversation :
- **Le titre** prévu ou publié.
- **Le sujet et la niche**, le public visé.
- **Ce que la vidéo livre vraiment** (pour vérifier que la promesse est tenue).
- **La charte de la chaîne** si elle existe (couleurs, police, style habituel).

S'il manque des éléments, avance avec des hypothèses explicites (« Je suppose que le titre est… ») et pose au plus une question, à la fin.

### A2. Regarder comme le spectateur

Tu vois l'image en grand ; le spectateur la voit sur un téléphone, souvent à 160-360 pixels de large. Ce qui se lit en plein écran peut disparaître à cette taille. Quand tu as le fichier image et un outil pour exécuter du code, lance le script du skill (chemin à adapter au dossier où le skill est installé) :

```bash
python3 <dossier-du-skill>/scripts/apercu_miniature.py miniature.jpg --titre "Titre de la vidéo" --sortie apercu/
```

Le script produit une planche (grille des tiers, rendus aux tailles réelles, niveaux de gris, version floutée, palette dominante, zone de la durée) et des simulations de page d'accueil en mode clair et sombre. Ouvre les PNG produits et regarde-les vraiment avant d'écrire : c'est là qu'apparaissent les textes illisibles et les sujets qui se fondent dans le fond. Les métriques (contraste, couleurs, zones chargées, poids, résolution) sont des indices pour orienter ton regard, pas des verdicts. Détails et options : `references/test.md`.

Envoie ensuite à l'utilisateur la planche et la simulation de page d'accueil la plus parlante, avec l'outil d'envoi de fichiers dont tu disposes : voir sa miniature se fondre dans la page convainc plus qu'une phrase. Ne cite pas de chemins de fichiers qu'il ne peut pas ouvrir.

Commence ta réponse par le **test de la seconde** : en une phrase, ce que tu comprends en regardant la version miniature pendant une seconde. Si cette phrase ne correspond pas à la promesse de la vidéo, c'est le problème principal, avant tout le reste.

Sans fichier (simple description), raisonne à partir de la description et dis ce que tu ne peux pas vérifier.

### A3. Diagnostiquer

Lis `references/grille.md` (questions de contrôle, signaux d'alerte, corrections typiques) et `references/types.md` pour identifier les types de miniature employés. Évalue sur ces 10 axes :

1. **Lisibilité en une seconde** : un seul point focal, peu d'éléments, compréhensible à la taille d'un téléphone ?
2. **Composition** : éléments clés sur les lignes des tiers, hiérarchie claire, rien d'important sous la durée en bas à droite ?
3. **Contraste et couleurs** : sujet détaché du fond, palette maîtrisée, ressort sur l'interface claire et sombre ?
4. **Texte** : court, lisible en petit, complète le titre au lieu de le répéter (ou absent, si c'est mieux) ?
5. **Émotion et curiosité** : une émotion nette, une question que le spectateur se pose ?
6. **Types de miniature** : lesquels sont combinés, la combinaison sert-elle le sujet ?
7. **Duo titre-miniature** : complémentaires, un vrai trajet de l'un à l'autre ?
8. **Différenciation** : se démarque-t-elle des miniatures de la niche sur le même sujet, ou ressemble-t-elle au cliché du moment ?
9. **Identité de chaîne** : reconnaissable sans voir le nom de la chaîne, cohérente avec la charte ?
10. **Promesse et technique** : la vidéo tient-elle la promesse ; format 16:9, résolution, netteté ?

Distingue toujours **problème de concept** et **problème d'exécution**. Si l'idée même ne crée ni émotion ni curiosité, aucun effet ne la sauvera : dis-le en premier et propose d'autres concepts (mode B). Si l'idée est bonne, concentre-toi sur la réalisation.

### A4. Rendre le verdict

```
## Le test de la seconde
[Ce qu'on comprend en une seconde, à taille téléphone.]

## Verdict
[2-3 phrases franches : ce qui marche, le plus gros problème, concept ou exécution.]
[Une ligne d'hypothèses si tu en as pris, et les images que tu lui envoies.]

## Tableau de bord
| Axe | Note | En une phrase |
|---|---|---|
| Lisibilité | 🟢/🟠/🔴 | ... |
... (les 10 axes)

## Les corrections
[Du plus impactant au moins impactant. Pour chacune :]
### [Titre court]
**Où :** zone précise (« tiers supérieur gauche », « le texte "500 €" », « le visage à droite »)
**Pourquoi ça coince :** ...
**Correction :** action concrète (quoi déplacer, agrandir, supprimer, quelle couleur en hex, quel texte), et comment la faire dans son outil si ce n'est pas évident.

## Ce qu'il faut garder
[Les éléments forts et pourquoi, pour qu'ils survivent aux corrections.]

## Version retravaillée
[Croquis de la miniature corrigée en 4 à 6 lignes : quoi, où sur la grille, quel texte, quelles couleurs. Il résume l'image finale ; le détail des réglages est déjà dans les corrections, ne le répète pas.]
```

Adapte le volume : 3 à 5 corrections, les plus impactantes. Une miniature presque bonne mérite 3 corrections ciblées, pas 10 remarques mineures. Une analyse complète tient en général en 800 à 1 200 mots ; au-delà, l'utilisateur ne lit plus et ne corrige rien.

Si tu peux générer des images, une maquette rapide de la version retravaillée (formes simples, vrai texte, vraies couleurs, avec une étiquette « ta photo ici » à la place des éléments à photographier) passée dans le script à côté de l'originale montre l'effet des corrections en un coup d'œil. Optionnel, mais très convaincant quand l'écart est grand.

### A5. Comparer plusieurs versions

Quand il y a 2 ou 3 versions, passe-les ensemble dans le script (il produit une comparaison côte à côte) et classe-les en justifiant par les axes de la grille. Rappelle que ton classement est une hypothèse : le vrai juge est le public. Si la chaîne y a accès, propose le test A/B intégré à YouTube Studio (détails à jour dans `references/test.md`) et explique quoi garder constant pour que le test soit lisible.

---

## Mode B — Conception d'une miniature

### B1. Trouver la matière

Une miniature forte part de ce que la vidéo a de plus frappant. Cherche dans ce qu'il t'a envoyé, et demande seulement ce qui manque vraiment (2 ou 3 questions au plus, chacune avec 2 ou 3 pistes concrètes pour éviter la page blanche) :
- **La promesse** : ce que le spectateur gagne ou découvre en regardant.
- **Le moment ou l'image la plus forte** de la vidéo : un résultat, un chiffre, un objet, une réaction, un avant/après. Ce qui choquerait, surprendrait ou intriguerait.
- **Le titre** (ou ses candidats).
- **La niche** et ce que font déjà les miniatures sur ce sujet.
- **La charte** et l'outil de montage (Photoshop, Photopea, Canva, GIMP…).

S'il est pressé, prends des hypothèses visibles et avance.

### B2. Proposer trois concepts

Lis `references/types.md`. Propose 3 concepts qui jouent sur des leviers différents (par exemple un choc, une comparaison, une simplicité intrigante), chacun combinant 2 ou 3 types :

```
### Concept [N] — [nom court] ([types combinés])
**Croquis :** ce qu'on voit et où, sur la grille des tiers (premier plan, fond, texte)
**Texte sur l'image :** [2-4 mots] ou aucun
**Titre associé :** [le titre qui complète l'image]
**Ce que le spectateur se demande :** la question qui le fait cliquer
**À préparer :** photo ou objet à shooter, capture de la vidéo, expression à jouer (si la chaîne est face caméra), élément graphique
**Risque :** ce qui peut rater (illisible, cliché de la niche, promesse trop forte)
```

**Montre les concepts.** Quand tu peux exécuter du code, dessine une maquette de chaque concept en 1280 × 720 (avec Pillow par exemple : formes simples, vrai texte dans une police grasse, vraies couleurs, étiquette « ta photo ici » à la place des éléments à photographier) et passe les trois maquettes ensemble dans le script d'aperçu. La comparaison aux tailles réelles aide le créateur à choisir et révèle tout de suite le concept qui ne se lit pas en petit. Ce sont des plans de composition, pas des visuels à publier : dis-le. Reste rapide : des formes simples suffisent, un passage dans le script, et une retouche seulement si une alerte ou un rendu en petit le justifie. Envoie-lui la comparaison et la page d'accueil simulée (celle du mode où se joue un éventuel problème, sinon le mode clair).

Recommande ensuite un concept en 2 ou 3 phrases et dis pourquoi, en t'appuyant sur ce que montrent les maquettes ; propose éventuellement le deuxième comme challenger pour un test A/B.

### B3. Brief d'exécution

Pour le concept recommandé seulement, donne la recette dans son outil : calques dans l'ordre, détourage, style du texte, effets, ajustements de couleur, export. Lis `references/execution.md`. Reste au niveau des actions (« double-clique sur le calque texte, ajoute un contour extérieur noir de 8 px ») plutôt que des généralités. Les autres concepts n'ont pas de recette tant que l'utilisateur ne les a pas choisis : propose-la en une phrase.

Termine par le test à faire avant publication, centré sur le risque principal du concept (souvent la lisibilité d'un petit élément à 168 pixels), et propose de repasser sa version finale dans l'aperçu.

Vise 800 à 1 200 mots pour l'ensemble (hypothèses, trois concepts, recommandation, brief, test) : le créateur doit pouvoir lire et passer à l'action.

---

## Mode C — Charte de chaîne

Lis la section « Charte » de `references/fondamentaux.md`. Livre une fiche :

```
## Charte miniatures — [chaîne]
- **Couleur principale :** #...
- **Noir / blanc / ton intermédiaire :** #... / #... / #... (légèrement teintés vers la principale)
- **Couleurs d'accent (à faire tourner d'une vidéo à l'autre) :** #..., #..., #...
- **Police :** [nom] — [style : graisse, contour, ombre], alternative gratuite si besoin, licence à vérifier
- **Combinaison de types :** [2-3 types] pour les ~5 prochaines vidéos
- **Règles de mise en page :** où se placent le visage, l'objet, le texte
- **Ce qui ne change jamais / ce qui varie :** ...
```

Justifie chaque choix par la niche et le public (contraste avec les chaînes concurrentes, lisibilité, cohérence avec le montage).

---

## Principes communs

- **Ancre chaque remarque dans l'image.** « Le texte manque de contraste » ne sert à rien ; « le texte jaune en haut à droite se fond dans le ciel clair : passe-le en blanc avec un contour noir » se corrige en deux minutes.
- **Le concept avant les effets.** Les styles de calque et les retouches améliorent une bonne idée ; ils ne rattrapent pas une idée faible.
- **Pense téléphone d'abord.** Juge à la taille réelle, pas à la taille de travail.
- **Inspiration hors de la niche.** Regarder sa niche sert à repérer le cliché à éviter. Pour les idées, va chercher dans d'autres niches : la miniature se démarquera de ses voisines, qui se ressemblent entre elles. Si un outil de recherche de miniatures similaires est disponible (par exemple vidIQ), un appel suffit pour voir ce que fait la niche ; ces outils peuvent consommer des crédits. S'il est absent, refusé ou hors sujet, décris les clichés courants du sujet en précisant que c'est de mémoire, et demande à l'utilisateur de vérifier en cherchant le sujet sur YouTube (ou de t'envoyer des captures des miniatures concurrentes, que le script peut placer autour de la sienne).
- **Cohérence sans répétition.** Couleurs, police et style stables pour être reconnu ; concept et couleur d'accent qui changent pour rester frais.
- **Curiosité, pas mensonge.** Ne recommande jamais une miniature trompeuse : objet absent de la vidéo, résultat inventé, visage d'une célébrité dont la vidéo ne parle pas. Le clickbait mensonger fait fuir le spectateur après 10 secondes, et c'est la durée de visionnage que YouTube récompense.
- **Pas de dogme.** Ces règles sont des points de départ issus de ce qui marche souvent. Les données de la chaîne (CTR, résultats de tests) ont le dernier mot.
- **Adapte-toi à son outil et à son niveau.** Un débutant sur Canva n'a pas besoin des modes de fusion de Photoshop.


---
## Fichier : coach-miniature-youtube/references/execution.md

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


---
## Fichier : coach-miniature-youtube/references/fondamentaux.md

# Fondamentaux du design de miniature

## Sommaire
1. Composition : la règle des tiers
2. Couleurs : la palette en 5 couleurs
3. Police
4. Le texte sur la miniature
5. Lisibilité à petite taille
6. Charte de chaîne (mode C)
7. Inspiration et différenciation

---

## 1. Composition : la règle des tiers

Trace deux lignes verticales et deux horizontales qui découpent l'image en 9 cases égales. Place les éléments clés (visage, objet, texte) sur ces lignes, idéalement sur leurs intersections. Selon Isaac, presque toutes les miniatures de grandes chaînes suivent ce principe à la base, et c'est ce qui fait passer une composition « fouillis » à une composition équilibrée.

Conseils de mise en page :
- **Un point focal principal**, éventuellement un second plus petit. Au-delà de 3 éléments, l'œil ne sait plus où aller.
- **Hiérarchie** : l'élément le plus important est le plus grand et le plus contrasté.
- **Profondeur** : premier plan net et contrasté, arrière-plan plus sombre, plus flou ou moins saturé.
- **Le regard guide** : un visage qui regarde vers l'objet ou le texte y emmène l'œil du spectateur.
- **Zone morte en bas à droite** : YouTube y affiche la durée de la vidéo (et la barre de progression rouge en bas pour les vidéos déjà vues). N'y mets rien d'essentiel.
- **Marges** : garde l'essentiel un peu à l'intérieur des bords, certaines interfaces recadrent légèrement ou arrondissent les coins.

Commence par un croquis sur papier avant d'ouvrir le logiciel : la composition se décide là, pas en déplaçant des calques au hasard.

---

## 2. Couleurs : la palette en 5 couleurs

Le principe classique est le contraste : prendre deux couleurs opposées sur le cercle chromatique (complémentaires). Isaac utilise une méthode plus simple, qui sert aussi pour toute la chaîne :

1. **Une couleur principale** que tu aimes et qui te représente (lui : le jaune).
2. **Un noir, un blanc et un ton intermédiaire** (gris), qu'on peut légèrement teinter vers la couleur principale pour l'harmonie.
3. **Une couleur d'accent** pour faire ressortir un élément précis (un mot, une flèche, un chiffre).

Pour éviter que toutes les miniatures se ressemblent, change seulement la couleur d'accent d'une vidéo à l'autre : la chaîne reste reconnaissable et chaque miniature garde une fraîcheur.

Points à vérifier :
- **Contraste de valeur** (clair/sombre), pas seulement de teinte. Un rouge et un vert de même luminosité se confondent en niveaux de gris et pour les personnes daltoniennes. Le test : passer l'image en noir et blanc, le sujet doit encore ressortir.
- **L'interface** : YouTube s'affiche sur fond blanc (mode clair) ou presque noir (mode sombre). Une miniature à fond blanc se fond dans le mode clair, une miniature très sombre dans le mode sombre. Un fond moyen ou saturé ressort dans les deux.
- **Le rouge YouTube** : une miniature dominée par le rouge du logo et des boutons peut se noyer dans l'interface.
- **Saturation** : des couleurs vives attirent l'œil, mais une image entièrement saturée n'a plus de point focal. Garder un fond plus calme que le sujet.

---

## 3. Police

Choisis une police simple, lisible, et qui n'est pas déjà utilisée par tous les youtubers. Exemples cités par Isaac : Eastman Roman (celle qu'il utilise), Nexa, Kallisto, Berlin Rounded, HammerBro101. On trouve des polices gratuites sur dafont.

À vérifier :
- **Licence** : beaucoup de polices gratuites sur dafont sont réservées à un usage personnel. Une chaîne monétisée est un usage commercial : vérifier la licence, ou choisir une police sous licence libre (par exemple sur Google Fonts).
- **Graisse** : en petit, une police fine disparaît. Préférer les graisses grasses (Bold, Black, Heavy).
- **Lisibilité** : éviter les scripts, les polices très condensées ou décoratives pour le texte principal.
- **Constance** : une seule famille de police sur toutes les miniatures, c'est un élément de reconnaissance.

---

## 4. Le texte sur la miniature

Options selon Isaac, à choisir selon la vidéo :
- **Un gros chiffre**, si la vidéo s'y prête.
- **Une affirmation forte**, ou le contre-pied d'une idée reçue.
- **Une formule qui représente la vidéo.**
- **Rien du tout**, si aucune option ne colle vraiment. Une image forte sans texte vaut mieux qu'un texte forcé.

Règles pratiques :
- **2 à 4 mots** en général. Au-delà, c'est illisible en petit et ça fait doublon avec le titre.
- **Complémentaire du titre** : si le titre dit « J'ai testé le PC le moins cher d'Amazon », le texte « 89 € » ou « ça marche ?! » ajoute quelque chose ; « PC pas cher » répète.
- **Lisible** : contour, ombre portée ou bandeau derrière le texte pour le détacher du fond.
- **Langue** : le texte doit être dans la langue du public visé.

---

## 5. Lisibilité à petite taille

Tailles d'affichage approximatives :
- Fil d'accueil sur téléphone : la largeur de l'écran, environ 360-400 pixels.
- Suggestions à côté d'une vidéo sur ordinateur : environ 168 pixels de large.
- Résultats de recherche et accueil sur ordinateur : environ 300-400 pixels de large.

Tests rapides :
- **Le test de la seconde** : regarde la miniature à 168 pixels de large pendant une seconde. Peux-tu dire de quoi parle la vidéo ?
- **Le test du plissement d'yeux** : floute l'image (ou plisse les yeux). On doit encore distinguer les grandes formes et le point focal.
- **Le test du noir et blanc** : le sujet doit se détacher en niveaux de gris.

---

## 6. Charte de chaîne (mode C)

Les éléments qui doivent rester constants pour qu'un abonné reconnaisse la vidéo sur sa page d'accueil sans lire le nom de la chaîne :
- La palette (couleur principale + noir/blanc/intermédiaire).
- La police et son style (contour, ombre).
- La combinaison de types du moment.
- Éventuellement un élément signature : position récurrente du visage, cadre, logo discret.

Ce qui doit varier : le concept de chaque vidéo et la couleur d'accent. Avec le temps, cette reconnaissance fait monter le CTR auprès des abonnés.

Pour construire une charte :
1. Regarde les miniatures des 5 à 10 chaînes concurrentes : quelles couleurs dominent ? La couleur principale doit s'en distinguer.
2. Choisis la couleur principale (qui se voit sur fond clair et sombre), puis les tons neutres.
3. Prépare 3 ou 4 couleurs d'accent qui contrastent avec la principale.
4. Choisis la police (licence vérifiée) et un style de texte unique (par exemple : blanc, contour noir 8 px, ombre portée).
5. Fixe la combinaison de types pour les 5 prochaines vidéos.
6. Teste la charte sur une maquette avant de l'appliquer.

---

## 7. Inspiration et différenciation

Le conseil courant « regarde ce que fait ta niche et reproduis ce qui marche » est, selon Isaac, la pire chose à faire quand on débute :
- Si beaucoup de chaînes utilisent déjà le même style sur le même sujet, c'est devenu le cliché. Le public est le même : il n'a aucune raison de cliquer sur la vidéo à 0 vue plutôt que sur celle à 100 000.
- Les gens remarquent la ressemblance, et la chaîne passe pour une copie.

Ce qu'il propose :
- **Regarder sa niche pour savoir quoi éviter**, pas quoi copier.
- **S'inspirer de chaînes d'autres niches** : leurs codes visuels sont inconnus du public de la niche, donc la miniature se démarque au milieu de ses voisines qui se ressemblent toutes.
- **Garder les éléments de base constants** (couleurs, police, style) en expérimentant sur le concept.

Pour trouver de l'inspiration : parcourir les chaînes qu'on suit dans des domaines sans rapport, noter les mises en page et les idées, et se demander comment les transposer à son sujet.


---
## Fichier : coach-miniature-youtube/references/grille.md

# Grille d'analyse d'une miniature

Pour chaque axe : les questions à se poser, les signaux d'alerte, et les corrections qui reviennent le plus souvent. Les principes détaillés sont dans `fondamentaux.md`.

Notation dans le tableau de bord :
- 🟢 l'axe fonctionne, rien d'important à changer ;
- 🟠 fonctionne en partie, une correction améliorerait nettement ;
- 🔴 bloque le clic ou trahit la vidéo, à corriger avant publication.

---

## 1. Lisibilité en une seconde

**Questions :** À 168 pixels de large, comprend-on le sujet en une seconde ? Combien d'éléments distincts ? Où va l'œil en premier ?

**Signaux d'alerte :**
- Plus de 3 éléments qui se disputent l'attention.
- Sujet principal qui occupe moins d'un tiers de l'image.
- Détails essentiels (texte fin, petit objet, capture d'écran) qui deviennent une bouillie en petit.
- Sur la version floutée, aucune forme ne ressort.

**Corrections typiques :** supprimer les éléments secondaires ; agrandir le sujet (recadrer plus serré) ; remplacer une capture d'écran entière par un détail zoomé ; simplifier le fond.

## 2. Composition

**Questions :** Les éléments clés sont-ils sur les lignes ou intersections des tiers ? La hiérarchie est-elle claire ? Le regard est-il guidé ? Quelque chose d'important se trouve-t-il en bas à droite, sous la durée ?

**Signaux d'alerte :**
- Tout est centré et plat, ou tout est collé aux bords.
- Deux éléments de même taille et même contraste se font concurrence.
- Texte ou objet clé dans le coin inférieur droit.
- Visage qui regarde hors de l'image, à l'opposé du sujet.

**Corrections typiques :** décaler le sujet sur un tiers vertical et le texte sur l'autre ; agrandir l'élément principal et réduire le secondaire ; remonter ce qui est en bas à droite ; retourner l'image du visage pour qu'il regarde vers l'objet.

## 3. Contraste et couleurs

**Questions :** Le sujet se détache-t-il du fond, y compris en noir et blanc ? Combien de couleurs dominantes ? La miniature ressort-elle sur l'interface claire et sur l'interface sombre ? La palette correspond-elle à la charte ?

**Signaux d'alerte :**
- En niveaux de gris, sujet et fond ont la même valeur.
- Fond blanc ou très clair (disparaît en mode clair), ou fond très sombre sans élément lumineux (disparaît en mode sombre).
- Plus de 4 couleurs saturées qui se battent.
- Arrière-plan plus saturé ou plus lumineux que le sujet.

**Corrections typiques :** assombrir ou flouter l'arrière-plan derrière le sujet et le texte ; contour clair autour du sujet détouré ; désaturer le fond ; ramener la palette à principale + neutres + un accent ; changer la teinte du fond (teinte/saturation) pour qu'elle contraste avec le sujet.

## 4. Texte

**Questions :** Combien de mots ? Lisible à 168 pixels ? Le texte ajoute-t-il une information que le titre n'a pas ? La police est-elle grasse, lisible, cohérente avec la chaîne ? Faut-il vraiment du texte ?

**Signaux d'alerte :**
- Plus de 4-5 mots.
- Le texte répète le titre mot pour mot.
- Police fine, script ou décorative ; pas de contour ni d'ombre sur un fond chargé.
- Texte dans une langue différente de celle du public.

**Corrections typiques :** réduire à 2-4 mots qui complètent le titre ; passer en graisse Black/Heavy ; ajouter un contour ou un bandeau ; supprimer le texte si l'image se suffit.

## 5. Émotion et curiosité

**Questions :** Quelle émotion domine (surprise, curiosité, envie, amusement, inquiétude) ? Quelle question le spectateur se pose-t-il en voyant l'image ? S'il y a un visage, l'expression est-elle lisible en petit et cohérente avec le sujet ?

**Signaux d'alerte :**
- Aucune question ne naît de l'image : on comprend tout, rien ne donne envie d'en savoir plus.
- Ou au contraire, on ne comprend rien : la curiosité demande un minimum de contexte.
- Expression neutre, ou grimace exagérée sans rapport avec le sujet.
- Visage trop petit pour lire l'expression.

**Corrections typiques :** cacher le résultat (flouté) ou montrer l'instant juste avant ; ajouter un enjeu (chiffre, comparaison) ; resserrer sur le visage ; choisir une expression qui correspond à la vraie réaction dans la vidéo.

## 6. Types de miniature

**Questions :** Quels types de `types.md` sont combinés ? Lequel porte l'émotion principale ? La combinaison convient-elle au format de la vidéo ? Est-elle cohérente avec les dernières miniatures de la chaîne ?

**Signaux d'alerte :**
- Aucun type identifiable : une photo sans angle.
- 4 types ou plus empilés : surcharge.
- Le même schéma depuis plus de 10 vidéos sans variation.

**Corrections typiques :** choisir le type qui sert le mieux le moment fort de la vidéo et en ajouter un ou deux en soutien ; retirer un type qui n'apporte rien.

## 7. Duo titre-miniature

**Questions :** Que dit le titre, que montre l'image ? Le spectateur fait-il un trajet de l'un à l'autre ? Le duo crée-t-il une seule promesse claire ?

**Signaux d'alerte :**
- Image et titre disent exactement la même chose.
- Image et titre semblent parler de deux vidéos différentes.
- Le texte de la miniature et le titre se contredisent ou se coupent mutuellement l'effet (par exemple, le titre révèle ce que l'image floute).

**Corrections typiques :** faire porter l'émotion à l'image et le contexte au titre (ou l'inverse) ; reformuler le texte de l'image pour qu'il complète le titre ; proposer 2 titres alternatifs adaptés à la miniature.

## 8. Différenciation

**Questions :** À quoi ressemblent les miniatures des vidéos concurrentes sur le même sujet ? Celle-ci se démarque-t-elle dans une page de résultats de recherche ou de suggestions ? Y a-t-il un cliché de niche (même pose, même flèche rouge, même cercle, même visage choqué) ?

**Signaux d'alerte :**
- On pourrait l'échanger avec celle d'un concurrent sans que personne ne le remarque.
- Elle reprend le format qu'une chaîne plus grosse utilise déjà sur le même sujet.

**Corrections typiques :** prendre le contre-pied visuel de la niche (simple si tout est chargé, lumineux si tout est sombre) ; transposer une mise en page vue dans une autre niche ; changer d'angle (montrer le résultat au lieu du processus, l'objet au lieu du visage).

Si tu n'as pas accès aux miniatures concurrentes, dis-le et demande à l'utilisateur ce qu'il voit en cherchant son sujet sur YouTube, ou utilise un outil de recherche de miniatures similaires s'il est disponible.

## 9. Identité de chaîne

**Questions :** Un abonné reconnaîtrait-il la chaîne sans lire son nom ? Couleurs, police et style sont-ils cohérents avec les miniatures précédentes ?

**Signaux d'alerte :**
- Chaque miniature a une police et une palette différentes.
- Ou inversement, toutes les miniatures sont identiques au point qu'on ne distingue plus les vidéos entre elles.

**Corrections typiques :** proposer une charte (mode C) ; changer seulement la couleur d'accent et le concept, garder le reste.

## 10. Promesse et technique

**Questions :** La vidéo montre-t-elle ce que la miniature promet, et assez tôt ? Le format est-il en 16:9 ? La résolution suffit-elle ? L'image est-elle nette, sans artefacts de compression ?

**Signaux d'alerte :**
- Élément de la miniature absent de la vidéo, résultat exagéré, visage d'une personne dont la vidéo ne parle pas.
- Ratio différent de 16:9 (bandes noires ou recadrage).
- Moins de 1280 × 720 (une image floue, et un test A/B dégradé en 480p) ; moins de 640 pixels de large (refusé).
- Fichier de plus de 2 Mo si l'upload se fait depuis un téléphone.
- Image pixellisée, flou de compression, détourage baveux.

**Corrections typiques :** ajuster la promesse à ce que la vidéo livre vraiment, ou montrer le moment promis dans les 30 premières secondes ; réexporter en 16:9, au moins 1920 × 1080 ; compresser en JPG qualité 85-90 si le poids dépasse ; refaire le détourage.

---

## Erreurs fréquentes chez les petites chaînes

- Un visage choqué générique qui n'a rien à voir avec le contenu.
- Une phrase entière en guise de texte.
- Une capture d'écran de la vidéo prise au hasard, sans retouche.
- Un fond chargé sans assombrissement derrière le texte.
- Copier la miniature du concurrent qui a fait le plus de vues sur le sujet.
- Changer de style à chaque vidéo.
- Juger la miniature uniquement en plein écran.


---
## Fichier : coach-miniature-youtube/references/test.md

# Tester une miniature

Trois niveaux, du plus rapide au plus fiable.

## 1. Planche d'aperçu (script local)

`scripts/apercu_miniature.py` (dépendance : Pillow ; chemins relatifs au dossier du skill).

```bash
# Une miniature, avec son titre
python3 scripts/apercu_miniature.py mini.jpg --titre "Titre de la vidéo" --sortie apercu/

# Deux ou trois versions à comparer (titres dans le même ordre)
python3 scripts/apercu_miniature.py v1.png v2.png --titre "Titre A" "Titre B" --sortie apercu/

# Avec les miniatures concurrentes autour, et le nom de la chaîne
python3 scripts/apercu_miniature.py mini.jpg --contexte concu1.jpg concu2.jpg --chaine "Ma chaîne"
```

Fichiers produits :
- `planche_<nom>.png` : grille des tiers et zone de la durée sur l'image, rendus aux tailles réelles (360, 300 et 168 pixels de large, avec le badge de durée), niveaux de gris, version floutée, palette dominante, mesures et alertes.
- `accueil_clair.png` et `accueil_sombre.png` : la miniature au milieu d'une page d'accueil simulée. Les voisines sont les images passées avec `--contexte`, sinon des blocs neutres. Avec de vraies miniatures concurrentes, le test est bien plus parlant.
- `comparaison.png` : les versions côte à côte aux petites tailles (si plusieurs images).
- `metriques.json` : toutes les mesures.

Comment lire les mesures :
- **Contraste de valeurs** (écart-type de la luminosité, 0 à 0,5) : en dessous de 0,17 environ, l'image paraît terne. Une image très contrastée n'est pas forcément lisible pour autant : regarder la version en niveaux de gris.
- **Pourtour quasi blanc / quasi noir** : au-delà de 50 %, la miniature se fond dans l'interface du mode correspondant.
- **Familles de couleurs vives** : 4 ou plus suggère une palette dispersée.
- **Détails sous la durée** : densité de contours dans la zone du badge ; élevée = quelque chose y est peut-être caché.
- **Zones les plus chargées** : densité de contours par case de la grille. Utile pour voir où se concentre le détail ; les photos texturées donnent des valeurs plus élevées partout, donc comparer les cases entre elles plutôt qu'à un seuil.

Ces mesures orientent le regard. Le jugement se fait en regardant les rendus en petit et la page d'accueil simulée.

Si le script ne peut pas tourner (pas de Python, pas de fichier), décris à l'utilisateur comment faire le test lui-même : réduire l'image à 168 pixels de large, la regarder une seconde, puis la passer en noir et blanc.

## 2. Simulateur de page d'accueil en ligne

Des outils comme thumbsup.tv (cité par Isaac) placent la miniature et le titre dans une fausse page YouTube, avec de vraies vidéos autour. Pratique pour voir le duo titre-miniature en situation, sur ordinateur et mobile. Si la miniature ne ressort pas, retour au croquis.

## 3. Test A/B dans YouTube Studio (« Tester et comparer »)

Le seul test qui mesure le comportement réel du public. Fonctionnement relevé dans l'aide YouTube en octobre 2026 (à revérifier, la fonction évolue) :
- Jusqu'à **3 variantes** : titres seuls, miniatures seules, ou combinaisons titre + miniature.
- Le gagnant est choisi sur la **part de durée de visionnage**, pas sur le taux de clic. Une miniature qui attire des clics de gens qui repartent aussitôt peut perdre.
- Durée : de quelques jours à **2 semaines** selon les impressions.
- **Uniquement sur ordinateur**, dans YouTube Studio, avec les fonctionnalités avancées activées.
- Non éligibles : Shorts, lives programmés, premières (éligibles une fois converties), vidéos pour enfants, réservées aux adultes ou privées.
- Modifier le titre ou la miniature pendant le test l'arrête.
- Une miniature en dessous de 1280 × 720 fait passer toutes les variantes en 480p.
- Résultats possibles : gagnant, performances équivalentes, ou non concluant (la première variante est alors conservée).

Conseils pour un test lisible :
- **Changer une seule chose importante** entre les variantes (le concept, ou le texte, ou le visage), sinon on ne sait pas ce qui a fait la différence.
- **Mettre en première position** la variante préférée : c'est elle qui reste si le test n'est pas concluant.
- **Noter le résultat** et ce qu'il apprend sur le public, pour orienter les miniatures suivantes. Un « équivalent » est aussi une information : la variable testée compte peu.


---
## Fichier : coach-miniature-youtube/references/types.md

# Les 10 types de miniatures

Source : le guide d'Isaac (isaacverse), qui reprend lui-même la classification de Tyler Fleischman (21 catégories au total ; Isaac en retient les 10 qui couvrent l'essentiel des cas). Selon Isaac, la quasi-totalité des miniatures virales combinent plusieurs de ces types.

## Sommaire
1. Les 10 types (principe, émotion, quand l'utiliser, pièges)
2. Combiner les types
3. Pistes par format de vidéo
4. Lire une miniature existante

---

## 1. Les 10 types

### Choquant
- **Principe :** une image qui provoque une réaction immédiate pendant le défilement (« mais qu'est-ce qu'il fait ? »).
- **Émotion :** surprise, incrédulité.
- **Quand l'utiliser :** la vidéo contient un moment, un fait ou une image vraiment surprenante. Marche aussi hors divertissement : l'exemple d'Isaac est une vidéo technique sur les tests de moteurs d'avion, dont la miniature montre une volaille projetée vers un réacteur.
- **Question à poser au créateur :** « Qu'est-ce qui, dans ta vidéo, ferait dire "attends, quoi ?" à quelqu'un qui ne connaît pas le sujet ? »
- **Pièges :** choquer avec quelque chose qui n'est pas dans la vidéo ; surenchère qui ressemble à toutes les miniatures criardes.

### Gros chiffres
- **Principe :** un montant, une quantité ou une échelle impressionnante, en très grand (« 20 000 $ », « 100 jours », « 1 million »).
- **Émotion :** curiosité, envie, vertige.
- **Quand l'utiliser :** la vidéo tourne autour d'une grandeur mesurable (prix, durée, nombre, distance). Les gens veulent voir à quoi ressemble une maison à 50 millions.
- **Pièges :** chiffre exagéré ou trompeur ; chiffre qui répète exactement le titre ; trop de chiffres.
- **Vérification :** un chiffre affiché en énorme sera contesté en commentaire s'il est faux. Si c'est toi qui le proposes, vérifie-le (recherche rapide) ou signale-le clairement comme à vérifier avant publication.

### Simple
- **Principe :** un seul objet ou une seule capture sur fond épuré, sans texte ou presque. Exemple du guide : une simple chaise blanche sur fond noir.
- **Émotion :** intrigue (« pourquoi une chaise ? »).
- **Quand l'utiliser :** la niche est saturée de miniatures chargées et criardes ; le sujet est un objet ou un concept iconique. Se démarque par contraste avec ses voisines.
- **Pièges :** simple et banal à la fois (l'objet doit poser une question) ; trop petit pour être lu.

### Question
- **Principe :** une capture d'écran de la vidéo (une conversation, un écran, une interface) accompagnée d'une question courte qui crée la curiosité.
- **Émotion :** curiosité, besoin de comprendre.
- **Quand l'utiliser :** sujets d'explication, d'enquête, de tech, de société. Exemple du guide : un logo dégoulinant avec « pourquoi tu ne trouves plus rien » pour une vidéo sur la dégradation d'un moteur de recherche.
- **Pièges :** question trop longue ; question dont la réponse est évidente ; capture illisible en petit.

### Différence de taille
- **Principe :** le créateur (ou le sujet) face à quelque chose de beaucoup plus grand ou plus petit. Exemple du guide : une personne minuscule à l'entrée d'un labyrinthe géant, avec une flèche « moi ».
- **Émotion :** démesure, défi.
- **Quand l'utiliser :** défis, constructions, voyages, objets hors norme. C'est le style qu'on voit partout sur YouTube.
- **Pièges :** l'échelle ne se lit pas en petit (le personnage devient un point) ; perspective qui écrase l'effet.

### Header (bandeau de texte)
- **Principe :** un texte en haut de l'image qui donne le contexte, au-dessus d'une image forte. Exemple du guide : « 500ft DEEP » au-dessus d'une personne dans un tunnel.
- **Émotion :** dépend du texte ; donne la clé de lecture.
- **Quand l'utiliser :** l'image seule est ambiguë et 2-4 mots la rendent claire. Isaac l'utilise lui-même.
- **Pièges :** texte qui répète le titre ; texte trop long ; bandeau qui mange l'image.

### Comparaison
- **Principe :** deux choses côte à côte : avant/après, pas cher contre cher, iPhone contre Android, humain contre IA.
- **Émotion :** curiosité du verdict (« lequel gagne ? »).
- **Quand l'utiliser :** tests, duels, transformations, choix d'achat. Très efficace en tech.
- **Pièges :** les deux côtés se ressemblent trop en petit ; le « VS » prend trop de place ; aucun indice d'enjeu.

### Flouté
- **Principe :** cacher le résultat final ou le personnage (flou, pixellisation, cache) pour qu'on clique afin de découvrir. Exemple du guide : « Day 1 » net à gauche, « Day 7 » flouté à droite pour une vidéo d'apprentissage.
- **Émotion :** frustration curieuse, besoin de voir.
- **Quand l'utiliser :** transformations, résultats, révélations, apprentissages sur une durée.
- **Pièges :** le flou cache tout, même ce qui fait comprendre le sujet ; la révélation déçoit dans la vidéo.

### Social hacking (visage connu)
- **Principe :** utiliser le visage d'une personnalité connue de la niche. Selon Isaac, c'est souvent la meilleure façon pour une petite chaîne d'une niche populaire d'obtenir ses premières vues.
- **Émotion :** reconnaissance, intérêt préexistant.
- **Condition absolue :** la vidéo doit parler de cette personne. Sinon c'est du clickbait, et le public le sanctionne.
- **Pièges :** droit à l'image et droits d'auteur sur la photo (préférer ses propres captures ou des images libres, citer la source) ; laisser croire à une collaboration ou un soutien qui n'existe pas.
- **Variante :** un objet, un logo ou un lieu que tout le monde reconnaît joue le même rôle sans visage. Montrer un produit ou un logo dans une vidéo qui en parle est courant ; la miniature ne doit simplement pas laisser croire à un contenu officiel ou sponsorisé par la marque.

### Objet bizarre
- **Principe :** un objet étrange, inconnu ou détourné qui intrigue. Exemple du guide : un créateur tech qui porte un casque audio avec un masque intégré.
- **Émotion :** « c'est quoi, ce truc ? ».
- **Quand l'utiliser :** tests de produits insolites, inventions, objets rares, gadgets.
- **Pièges :** l'objet n'est pas identifiable en petit ; il est bizarre mais pas intéressant.

---

## 2. Combiner les types

Les miniatures qui marchent combinent généralement 2 ou 3 types. Exemples analysés par Isaac :
- **Une série « j'ai acheté toutes les versions de [console] »** : gros chiffres (le prix total), header, comparaison (les générations côte à côte) et social hacking (des produits que tout le monde reconnaît), tout en même temps.
- **La chaise blanche** : simple (rien d'autre qu'une chaise), branding (logo de la chaîne), social hacking (une chaise que tout le monde a déjà vue), voire objet bizarre.
- **La première vidéo d'Isaac** : gros chiffres + header. Peu original selon lui, mais efficace.

Règle de rythme : choisir 2 ou 3 types, les garder pendant environ 5 vidéos pour que le public associe ce style à la chaîne, puis faire évoluer. Répéter la même formule indéfiniment donne l'impression que la chaîne se répète et fait baisser les clics (exception : les chaînes de réaction, où la constance est attendue).

Quand tu proposes une combinaison, vérifie :
- que chaque type ajoute quelque chose (un gros chiffre + une comparaison + un flou + un header = surcharge) ;
- qu'un type porte l'émotion principale et que les autres le servent ;
- que la combinaison reste lisible en petit.

---

## 3. Pistes par format de vidéo

Points de départ, à adapter à la matière réelle de la vidéo :

| Format | Combinaisons qui marchent souvent |
|---|---|
| Tutoriel / « comment faire » | Comparaison (avant/après) + header ; flouté (résultat caché) + différence de taille |
| Test de produit | Objet bizarre + header ; comparaison + gros chiffres (prix) |
| Duel, « X contre Y » | Comparaison + social hacking (produits ou marques connus) |
| Storytelling, histoire d'une entreprise ou d'un jeu | Simple + question ; social hacking (logo, personnage, fondateur) + header |
| Explication, enquête, actu tech | Question + simple ; choquant + header |
| Défi, expérience sur une durée | Flouté + gros chiffres (« jour 1 / jour 30 ») ; différence de taille |
| Budget, argent, prix | Gros chiffres + comparaison (pas cher / cher) |

---

## 4. Lire une miniature existante

Pour identifier les types d'une miniature, pose-toi ces questions dans l'ordre :
1. Qu'est-ce qui attire l'œil en premier ? (ça indique le type dominant)
2. Y a-t-il un chiffre, une question, un texte de contexte ? (gros chiffres, question, header)
3. Deux éléments sont-ils mis en opposition ? (comparaison, différence de taille)
4. Quelque chose est-il caché ? (flouté)
5. Reconnaît-on une personne, une marque ou un objet célèbre ? (social hacking)
6. Est-ce que l'image est presque vide ? (simple)

Nomme ensuite les types repérés dans l'analyse et dis si la combinaison sert le sujet.


---
## Fichier : coach-miniature-youtube/scripts/apercu_miniature.py

#!/usr/bin/env python3
"""Aperçu d'une ou plusieurs miniatures YouTube telles que le spectateur les voit.

Produit, dans le dossier de sortie :
  - planche_<nom>.png   : grille des tiers + zone de la durée, rendus aux tailles
                          réelles (fil mobile, suggestions), niveaux de gris,
                          version floutée (test du plissement d'yeux), palette dominante
  - accueil_clair.png / accueil_sombre.png : simulation de page d'accueil, la ou les
                          miniatures au milieu de miniatures voisines (--contexte)
  - comparaison.png     : versions côte à côte aux petites tailles (si plusieurs images)
  - metriques.json      : mesures brutes (résolution, poids, contraste, couleurs...)
et affiche un résumé avec des alertes.

Les métriques sont des indices pour orienter le regard, pas un verdict.

Usage :
  python apercu_miniature.py mini.jpg --titre "Mon titre" --sortie apercu/
  python apercu_miniature.py v1.png v2.png --titre "Titre A" "Titre B"
  python apercu_miniature.py mini.jpg --contexte concurrent1.jpg concurrent2.jpg
  python apercu_miniature.py mini.jpg --chaine "Ma chaîne"

Dépendance : Pillow (pip install pillow).
"""

import argparse
import json
import math
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat
except ImportError:
    sys.exit("Pillow est requis : pip install pillow")

RATIO_CIBLE = 16 / 9
TAILLE_TRAVAIL = (1280, 720)
TAILLES_REELLES = [
    ("Fil mobile (~360 px)", 360),
    ("Accueil ordinateur (~300 px)", 300),
    ("Suggestions (~168 px)", 168),
]
# Zone approximative du badge de durée (bas droite), en fraction de l'image
ZONE_DUREE = (0.86, 0.86, 0.985, 0.975)

FOND_CLAIR = (255, 255, 255)
FOND_SOMBRE = (15, 15, 15)
TEXTE_CLAIR = (15, 15, 15)
TEXTE_SOMBRE = (241, 241, 241)
TEXTE_SECONDAIRE_CLAIR = (96, 96, 96)
TEXTE_SECONDAIRE_SOMBRE = (170, 170, 170)


# ---------------------------------------------------------------- utilitaires

def police(taille, gras=False):
    candidats = (
        ["DejaVuSans-Bold.ttf", "Arial Bold.ttf", "arialbd.ttf", "LiberationSans-Bold.ttf"]
        if gras
        else ["DejaVuSans.ttf", "Arial.ttf", "arial.ttf", "LiberationSans-Regular.ttf"]
    )
    dossiers = [
        "",
        "/usr/share/fonts/truetype/dejavu/",
        "/usr/share/fonts/truetype/liberation/",
        "/Library/Fonts/",
        "/System/Library/Fonts/Supplemental/",
        "C:/Windows/Fonts/",
    ]
    for nom in candidats:
        for dossier in dossiers:
            try:
                return ImageFont.truetype(dossier + nom, taille)
            except OSError:
                continue
    try:
        return ImageFont.load_default(size=taille)
    except TypeError:
        return ImageFont.load_default()


def charger(chemin):
    img = Image.open(chemin)
    img = ImageOps.exif_transpose(img)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        fond = Image.new("RGB", img.size, (128, 128, 128))
        fond.paste(img, mask=img.split()[-1])
        return fond
    return img.convert("RGB")


def en_16_9(img, taille):
    """Recadre au centre en 16:9 (comme le ferait l'affichage) puis redimensionne."""
    return ImageOps.fit(img, taille, Image.LANCZOS, centering=(0.5, 0.5))


def couper_texte(draw, texte, fnt, largeur_max, lignes_max=2):
    mots = texte.split()
    lignes, courante = [], ""
    for mot in mots:
        essai = (courante + " " + mot).strip()
        if draw.textlength(essai, font=fnt) <= largeur_max:
            courante = essai
        else:
            if courante:
                lignes.append(courante)
            courante = mot
        if len(lignes) == lignes_max:
            break
    if courante and len(lignes) < lignes_max:
        lignes.append(courante)
    utilises = " ".join(lignes).split()
    if len(utilises) < len(mots) and lignes:
        dernier = lignes[-1]
        while dernier and draw.textlength(dernier + "…", font=fnt) > largeur_max:
            dernier = dernier[:-1]
        lignes[-1] = dernier.rstrip() + "…"
    return lignes


def pixels(img):
    if hasattr(img, "get_flattened_data"):
        return list(img.get_flattened_data())
    return list(img.getdata())


# ---------------------------------------------------------------- mesures

def palette_dominante(img, n=6):
    petite = img.copy()
    petite.thumbnail((240, 240))
    quant = petite.quantize(colors=10, method=Image.Quantize.FASTOCTREE)
    pal = quant.getpalette()
    comptes = sorted(quant.getcolors(), reverse=True)
    total = sum(c for c, _ in comptes)
    fusion = []  # fusionne les teintes quasi identiques
    for compte, idx in comptes:
        rgb = tuple(pal[idx * 3: idx * 3 + 3])
        for f in fusion:
            if sum((a - b) ** 2 for a, b in zip(f["rgb"], rgb)) ** 0.5 < 32:
                f["compte"] += compte
                break
        else:
            fusion.append({"rgb": rgb, "compte": compte})
    fusion.sort(key=lambda f: -f["compte"])
    return [
        {
            "hex": "#{:02X}{:02X}{:02X}".format(*f["rgb"]),
            "rgb": f["rgb"],
            "part": round(f["compte"] / total, 3),
        }
        for f in fusion[:n]
    ]


def familles_saturees(palette, part_min=0.03):
    """Nombre de familles de teintes vives (hors noirs, blancs, gris) dans la palette."""
    familles = set()
    for c in palette:
        r, g, b = [v / 255 for v in c["rgb"]]
        mx, mn = max(r, g, b), min(r, g, b)
        if c["part"] < part_min or mx < 0.35 or (mx - mn) / mx < 0.45:
            continue
        if mx == r:
            h = ((g - b) / (mx - mn)) % 6
        elif mx == g:
            h = (b - r) / (mx - mn) + 2
        else:
            h = (r - g) / (mx - mn) + 4
        familles.add(int(h * 60 // 40))  # tranches de 40° sur le cercle chromatique
    return len(familles)


def carte_contours(img):
    gris = en_16_9(img, (384, 216)).convert("L")
    return gris.filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v > 40 else 0)


def densite_zone_duree(bords):
    w, h = bords.size
    x0, y0, x1, y1 = ZONE_DUREE
    zone = bords.crop((int(x0 * w), int(y0 * h), int(x1 * w) - 1, int(y1 * h) - 1))
    return round(ImageStat.Stat(zone).mean[0] / 255, 3)


def densite_details(img):
    """Densité de contours par case de la grille 3x3 (indice de zones chargées)."""
    bords = carte_contours(img)
    w, h = bords.size
    cases = []
    noms = [
        ["haut-gauche", "haut-centre", "haut-droite"],
        ["milieu-gauche", "centre", "milieu-droite"],
        ["bas-gauche", "bas-centre", "bas-droite"],
    ]
    for ligne in range(3):
        for col in range(3):
            boite = (col * w // 3 + 2, ligne * h // 3 + 2, (col + 1) * w // 3 - 2, (ligne + 1) * h // 3 - 2)
            moyenne = ImageStat.Stat(bords.crop(boite)).mean[0] / 255
            cases.append({"case": noms[ligne][col], "densite": round(moyenne, 3)})
    valeurs = [c["densite"] for c in cases]
    moyenne = sum(valeurs) / len(valeurs)
    ecart = math.sqrt(sum((v - moyenne) ** 2 for v in valeurs) / len(valeurs))
    return cases, round(moyenne, 3), round(ecart, 3)


def mesurer(chemin, img):
    w, h = img.size
    gris = img.convert("L")
    stat = ImageStat.Stat(gris)
    hsv = img.convert("HSV")
    sat = ImageStat.Stat(hsv.split()[1]).mean[0] / 255

    # Bande de 4 % sur le pourtour : c'est elle qui touche l'interface de YouTube
    bord = 0.04
    bandes = [
        img.crop((0, 0, w, int(h * bord))),
        img.crop((0, int(h * (1 - bord)), w, h)),
        img.crop((0, 0, int(w * bord), h)),
        img.crop((int(w * (1 - bord)), 0, w, h)),
    ]
    moyennes_bords = [ImageStat.Stat(b).mean for b in bandes]
    couleur_bords = tuple(int(sum(m[i] for m in moyennes_bords) / 4) for i in range(3))
    pix_bords = [p for b in bandes for p in pixels(b.resize((max(1, b.width // 4), max(1, b.height // 4))))]
    bords_blancs = sum(1 for p in pix_bords if min(p) > 225) / len(pix_bords)
    bords_noirs = sum(1 for p in pix_bords if max(p) < 35) / len(pix_bords)

    hist = gris.histogram()
    total = w * h
    tres_clair = sum(hist[235:]) / total
    tres_sombre = sum(hist[:25]) / total

    cases, densite_moy, densite_ecart = densite_details(img)
    palette = palette_dominante(img)
    poids = os.path.getsize(chemin)

    return {
        "fichier": os.path.basename(chemin),
        "largeur": w,
        "hauteur": h,
        "ratio": round(w / h, 3),
        "poids_octets": poids,
        "poids_mo": round(poids / 1_000_000, 2),
        "format": (Image.open(chemin).format or "?"),
        "luminosite_moyenne": round(stat.mean[0] / 255, 3),
        "contraste_valeurs": round(stat.stddev[0] / 255, 3),
        "saturation_moyenne": round(sat, 3),
        "part_tres_claire": round(tres_clair, 3),
        "part_tres_sombre": round(tres_sombre, 3),
        "couleur_moyenne_bords": "#{:02X}{:02X}{:02X}".format(*couleur_bords),
        "part_bords_quasi_blancs": round(bords_blancs, 3),
        "part_bords_quasi_noirs": round(bords_noirs, 3),
        "palette": palette,
        "familles_couleurs_vives": familles_saturees(palette_dominante(img, n=10), part_min=0.015),
        "densite_details_par_case": cases,
        "densite_details_moyenne": densite_moy,
        "densite_details_ecart": densite_ecart,
        "densite_zone_duree": densite_zone_duree(carte_contours(img)),
    }


def alertes(m):
    a = []
    if abs(m["ratio"] - RATIO_CIBLE) > 0.02:
        a.append(f"Ratio {m['ratio']} au lieu de 1,778 (16:9) : l'image sera recadrée ou bordée.")
    if m["largeur"] < 640:
        a.append("Largeur inférieure à 640 px : YouTube refuse la miniature.")
    elif m["largeur"] < 1280:
        a.append("Moins de 1280 × 720 : image moins nette, et un test A/B serait dégradé en 480p.")
    if m["poids_mo"] > 2:
        a.append(f"{m['poids_mo']} Mo : au-dessus de 2 Mo, l'upload depuis un téléphone échoue "
                 "(l'ordinateur accepte jusqu'à 50 Mo).")
    if m["contraste_valeurs"] < 0.17:
        a.append("Contraste de valeurs faible : l'image risque de paraître terne et plate en petit.")
    if m["part_bords_quasi_blancs"] > 0.5:
        a.append(f"{round(m['part_bords_quasi_blancs'] * 100)} % du pourtour est quasi blanc : "
                 "la miniature se fond dans le mode clair.")
    if m["part_bords_quasi_noirs"] > 0.5:
        a.append(f"{round(m['part_bords_quasi_noirs'] * 100)} % du pourtour est quasi noir : "
                 "la miniature se fond dans le mode sombre.")
    if m["densite_zone_duree"] > max(0.08, 1.5 * m["densite_details_moyenne"]):
        a.append("Beaucoup de détails sous la zone de la durée (bas droite) : "
                 "vérifier que rien d'important n'y est caché.")
    if m["familles_couleurs_vives"] >= 4:
        a.append(f"{m['familles_couleurs_vives']} familles de couleurs vives : la palette se disperse, "
                 "aucune couleur ne domine.")
    return a


# ---------------------------------------------------------------- rendus

def avec_grille(img):
    base = en_16_9(img, TAILLE_TRAVAIL).copy()
    calque = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(calque)
    w, h = base.size
    for i in (1, 2):
        x, y = w * i // 3, h * i // 3
        for dx in range(-1, 2):
            d.line([(x + dx, 0), (x + dx, h)], fill=(0, 0, 0, 120))
            d.line([(0, y + dx), (w, y + dx)], fill=(0, 0, 0, 120))
        d.line([(x, 0), (x, h)], fill=(255, 255, 255, 220), width=1)
        d.line([(0, y), (w, y)], fill=(255, 255, 255, 220), width=1)
    for i in (1, 2):
        for j in (1, 2):
            cx, cy = w * i // 3, h * j // 3
            d.ellipse([cx - 7, cy - 7, cx + 7, cy + 7], outline=(255, 214, 0, 255), width=3)
    # Zone de sécurité de la durée : semi-transparente pour voir ce qu'elle recouvre
    x0, y0, x1, y1 = ZONE_DUREE
    boite = [int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)]
    d.rounded_rectangle(boite, radius=6, fill=(0, 0, 0, 90), outline=(255, 60, 60, 255), width=3)
    d.text(((boite[0] + boite[2]) / 2, (boite[1] + boite[3]) / 2), "durée",
           fill=(255, 255, 255, 230), font=police(22, gras=True), anchor="mm")
    return Image.alpha_composite(base.convert("RGBA"), calque).convert("RGB")


def avec_badge(img_petite):
    """Ajoute le badge de durée à peu près à la taille où YouTube l'affiche."""
    img = img_petite.copy()
    d = ImageDraw.Draw(img)
    w, h = img.size
    fnt = police(max(8, round(h * 0.062)), gras=True)
    texte = "12:34"
    tw = d.textlength(texte, font=fnt)
    marge = max(3, round(w * 0.012))
    pad = max(2, round(w * 0.009))
    bh = max(10, round(h * 0.095))
    boite = [w - marge - tw - 2 * pad, h - marge - bh, w - marge, h - marge]
    d.rounded_rectangle(boite, radius=max(2, round(h * 0.02)), fill=(0, 0, 0))
    d.text(((boite[0] + boite[2]) / 2, (boite[1] + boite[3]) / 2), texte,
           fill=(255, 255, 255), font=fnt, anchor="mm")
    return img


def arrondir(img, rayon):
    masque = Image.new("L", img.size, 0)
    ImageDraw.Draw(masque).rounded_rectangle([0, 0, img.size[0] - 1, img.size[1] - 1], radius=rayon, fill=255)
    fond = Image.new("RGBA", img.size, (0, 0, 0, 0))
    fond.paste(img, mask=masque)
    return fond


def taille_reelle(img, largeur):
    h = round(largeur * 9 / 16)
    return avec_badge(en_16_9(img, (largeur, h)))


def planche(img, m, titre=None):
    marge = 30
    col_g = 1280
    largeur = marge * 3 + col_g + 400
    hauteur = 1450
    p = Image.new("RGB", (largeur, hauteur), (236, 236, 236))
    d = ImageDraw.Draw(p)
    f_titre = police(30, gras=True)
    f_label = police(18, gras=True)
    f_petit = police(16)

    d.text((marge, 18), f"Aperçu — {m['fichier']}", fill=(20, 20, 20), font=f_titre)
    if titre:
        d.text((marge, 56), f"Titre : {titre}", fill=(70, 70, 70), font=f_petit)

    y = 90
    d.text((marge, y), "Grille des tiers (intersections en jaune) et zone de la durée (cadre rouge)",
           fill=(40, 40, 40), font=f_label)
    p.paste(avec_grille(img), (marge, y + 28))

    y2 = y + 28 + 720 + 30
    x = marge
    for label, w in TAILLES_REELLES:
        petite = taille_reelle(img, w)
        d.text((x, y2), label, fill=(40, 40, 40), font=f_label)
        p.paste(petite, (x, y2 + 28))
        x += w + 40

    y3 = y2 + 28 + 203 + 40
    x = marge
    gris = ImageOps.grayscale(en_16_9(img, (360, 203))).convert("RGB")
    d.text((x, y3), "Niveaux de gris (contraste de valeurs)", fill=(40, 40, 40), font=f_label)
    p.paste(gris, (x, y3 + 28))
    x += 360 + 40
    floue = en_16_9(img, (360, 203)).filter(ImageFilter.GaussianBlur(6))
    d.text((x, y3), "Floutée (test du plissement d'yeux)", fill=(40, 40, 40), font=f_label)
    p.paste(floue, (x, y3 + 28))

    # colonne de droite : palette et mesures
    xd = marge * 2 + col_g
    yd = 90
    d.text((xd, yd), "Palette dominante", fill=(40, 40, 40), font=f_label)
    yd += 32
    for c in m["palette"]:
        d.rectangle([xd, yd, xd + 70, yd + 44], fill=tuple(c["rgb"]), outline=(120, 120, 120))
        d.text((xd + 85, yd + 4), c["hex"], fill=(30, 30, 30), font=f_label)
        d.text((xd + 85, yd + 25), f"{round(c['part'] * 100)} % de l'image", fill=(90, 90, 90), font=f_petit)
        yd += 56

    yd += 16
    d.text((xd, yd), "Mesures (indices, pas verdicts)", fill=(40, 40, 40), font=f_label)
    yd += 30
    lignes = [
        f"{m['largeur']} × {m['hauteur']} px, ratio {m['ratio']}",
        f"{m['format']}, {m['poids_mo']} Mo",
        f"Luminosité moyenne : {m['luminosite_moyenne']}",
        f"Contraste de valeurs : {m['contraste_valeurs']}",
        f"Saturation moyenne : {m['saturation_moyenne']}",
        f"Familles de couleurs vives : {m['familles_couleurs_vives']}",
        f"Pourtour quasi blanc : {round(m['part_bords_quasi_blancs'] * 100)} %",
        f"Pourtour quasi noir : {round(m['part_bords_quasi_noirs'] * 100)} %",
        f"Détails sous la durée : {m['densite_zone_duree']}",
        "Zones les plus chargées :",
    ]
    top = sorted(m["densite_details_par_case"], key=lambda c: -c["densite"])[:3]
    lignes += [f"  {c['case']} ({c['densite']})" for c in top]
    for ligne in lignes:
        d.text((xd, yd), ligne, fill=(30, 30, 30), font=f_petit)
        yd += 24

    al = alertes(m)
    if al:
        yd += 14
        d.text((xd, yd), "Alertes", fill=(170, 30, 30), font=f_label)
        yd += 28
        for a in al:
            for ligne in couper_texte(d, "• " + a, f_petit, 360, lignes_max=4):
                d.text((xd, yd), ligne, fill=(120, 30, 30), font=f_petit)
                yd += 22
            yd += 6
    return p


def carte(img, titre, chaine, sombre, largeur=360):
    h = round(largeur * 9 / 16)
    mini = arrondir(avec_badge(en_16_9(img, (largeur, h))), 12)
    hauteur = h + 110
    fond = FOND_SOMBRE if sombre else FOND_CLAIR
    c = Image.new("RGBA", (largeur, hauteur), fond + (255,))
    c.alpha_composite(mini, (0, 0))
    d = ImageDraw.Draw(c)
    d.ellipse([0, h + 12, 36, h + 48], fill=(120, 120, 120) if sombre else (200, 200, 200))
    f_t = police(16, gras=True)
    f_s = police(13)
    lignes = couper_texte(d, titre, f_t, largeur - 50, lignes_max=2)
    y = h + 12
    for ligne in lignes:
        d.text((48, y), ligne, fill=TEXTE_SOMBRE if sombre else TEXTE_CLAIR, font=f_t)
        y += 21
    d.text((48, y + 4), chaine, fill=TEXTE_SECONDAIRE_SOMBRE if sombre else TEXTE_SECONDAIRE_CLAIR, font=f_s)
    d.text((48, y + 22), "12 k vues · il y a 2 jours",
           fill=TEXTE_SECONDAIRE_SOMBRE if sombre else TEXTE_SECONDAIRE_CLAIR, font=f_s)
    return c


def placeholder(index, sombre):
    teintes = [(84, 110, 122), (121, 85, 72), (69, 90, 100), (96, 125, 139), (93, 64, 55), (55, 71, 79)]
    base = teintes[index % len(teintes)]
    img = Image.new("RGB", (640, 360), base)
    d = ImageDraw.Draw(img)
    d.ellipse([60, 60, 300, 300], fill=tuple(min(255, v + 50) for v in base))
    d.rectangle([340, 110, 600, 170], fill=tuple(min(255, v + 90) for v in base))
    d.rectangle([340, 190, 540, 240], fill=tuple(max(0, v - 30) for v in base))
    return img


def page_accueil(images, titres, contexte, chaine, sombre):
    colonnes, lignes = 3, 2
    largeur_carte, gout = 360, 16
    cartes = []
    voisins = list(contexte)
    i_voisin = 0
    positions_cible = [1, 3, 5, 0, 2, 4][: len(images)]
    for pos in range(colonnes * lignes):
        if pos in positions_cible:
            k = positions_cible.index(pos)
            cartes.append(carte(images[k], titres[k], chaine, sombre, largeur_carte))
        else:
            if i_voisin < len(voisins):
                img_v = voisins[i_voisin]
                titre_v = "Vidéo voisine (contexte)"
            else:
                img_v = placeholder(pos, sombre)
                titre_v = "Autre vidéo de la page d'accueil"
            i_voisin += 1
            cartes.append(carte(img_v, titre_v, "Autre chaîne", sombre, largeur_carte))
    h_carte = cartes[0].size[1]
    W = colonnes * largeur_carte + (colonnes + 1) * gout
    H = lignes * h_carte + (lignes + 1) * gout + 40
    fond = FOND_SOMBRE if sombre else FOND_CLAIR
    page = Image.new("RGBA", (W, H), fond + (255,))
    d = ImageDraw.Draw(page)
    d.text((gout, 10), "Simulation page d'accueil — mode " + ("sombre" if sombre else "clair"),
           fill=TEXTE_SECONDAIRE_SOMBRE if sombre else TEXTE_SECONDAIRE_CLAIR, font=police(15, gras=True))
    for idx, c in enumerate(cartes):
        r, col = divmod(idx, colonnes)
        page.alpha_composite(c, (gout + col * (largeur_carte + gout), 40 + gout + r * (h_carte + gout)))
    return page.convert("RGB")


def comparaison(images, noms):
    largeurs = [360, 168]
    marge = 24
    hauteur_ligne = 203 + 40
    W = marge + len(images) * (360 + 168 + 3 * marge)
    H = marge + hauteur_ligne + 50
    p = Image.new("RGB", (W, H), (236, 236, 236))
    d = ImageDraw.Draw(p)
    x = marge
    for img, nom in zip(images, noms):
        d.text((x, marge - 4), nom, fill=(30, 30, 30), font=police(16, gras=True))
        xx = x
        for w in largeurs:
            p.paste(taille_reelle(img, w), (xx, marge + 24))
            xx += w + marge
        x += 360 + 168 + 3 * marge
    return p


# ---------------------------------------------------------------- principal

def main():
    ap = argparse.ArgumentParser(description="Aperçu de miniatures YouTube aux tailles réelles.")
    ap.add_argument("images", nargs="+", help="miniature(s) à analyser (jusqu'à 3 pour une comparaison)")
    ap.add_argument("--titre", nargs="*", default=[], help="titre(s) des vidéos, dans le même ordre")
    ap.add_argument("--contexte", nargs="*", default=[], help="miniatures voisines (concurrents, autres vidéos)")
    ap.add_argument("--chaine", default="Ta chaîne", help="nom de la chaîne affiché sous le titre")
    ap.add_argument("--sortie", default="apercu_miniature", help="dossier de sortie")
    args = ap.parse_args()

    if len(args.images) > 3:
        sys.exit("Trois miniatures au maximum à la fois.")
    os.makedirs(args.sortie, exist_ok=True)

    images, mesures, noms = [], [], []
    for i, chemin in enumerate(args.images):
        img = charger(chemin)
        images.append(img)
        m = mesurer(chemin, img)
        m["alertes"] = alertes(m)
        mesures.append(m)
        nom = os.path.splitext(os.path.basename(chemin))[0]
        noms.append(nom)
        titre = args.titre[i] if i < len(args.titre) else None
        planche(img, m, titre).save(os.path.join(args.sortie, f"planche_{nom}.png"))

    titres = [args.titre[i] if i < len(args.titre) else "Titre de la vidéo (non fourni)" for i in range(len(images))]
    contexte = [charger(c) for c in args.contexte]
    page_accueil(images, titres, contexte, args.chaine, sombre=False).save(os.path.join(args.sortie, "accueil_clair.png"))
    page_accueil(images, titres, contexte, args.chaine, sombre=True).save(os.path.join(args.sortie, "accueil_sombre.png"))
    if len(images) > 1:
        comparaison(images, noms).save(os.path.join(args.sortie, "comparaison.png"))

    with open(os.path.join(args.sortie, "metriques.json"), "w", encoding="utf-8") as f:
        json.dump(mesures, f, ensure_ascii=False, indent=2)

    for m in mesures:
        print(f"\n== {m['fichier']} ==")
        print(f"{m['largeur']}×{m['hauteur']} px, ratio {m['ratio']}, {m['format']}, {m['poids_mo']} Mo")
        print(f"Contraste de valeurs {m['contraste_valeurs']}, saturation {m['saturation_moyenne']}, "
              f"luminosité {m['luminosite_moyenne']}")
        print("Palette : " + ", ".join(f"{c['hex']} ({round(c['part'] * 100)} %)" for c in m["palette"]))
        top = sorted(m["densite_details_par_case"], key=lambda c: -c["densite"])[:3]
        print("Zones les plus chargées : " + ", ".join(f"{c['case']} ({c['densite']})" for c in top))
        if m["alertes"]:
            print("Alertes :")
            for a in m["alertes"]:
                print("  - " + a)
        else:
            print("Aucune alerte automatique.")
    print(f"\nFichiers écrits dans {os.path.abspath(args.sortie)} :")
    for f in sorted(os.listdir(args.sortie)):
        print("  " + f)


if __name__ == "__main__":
    main()

