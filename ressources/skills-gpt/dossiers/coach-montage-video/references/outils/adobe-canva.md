# Mise en œuvre : Premiere Pro, After Effects, Canva (et notes DaVinci Resolve / CapCut)

Réglages tels que décrits par l'auteur de la méthode, qui monte dans Premiere Pro et anime dans After Effects.

## Premiere Pro

**Projet**
- Nouveau projet, puis nouvelle séquence en 1920×1080, 60 i/s (4K si la machine suit).
- Disposition de l'auteur : moniteur principal au centre, timeline en bas, rushes et effets sur un côté, options d'effet et moniteur source de l'autre. Les fenêtres manquantes s'activent dans le menu Fenêtre.

**Montage brut**
- Importer la voix off, la glisser dans la timeline, la découper selon le script, supprimer les pauses gênantes.
- Poser la musique juste après, régler son volume sous la voix.
- Placer les rushes selon le script coloré ; tenter des coupes sur les temps forts.

**Zoom**
- Effet Transform sur le plan. Images clés d'échelle et de position au début, avancer dans la timeline, régler la fin du zoom.
- Déplier l'effet et lisser les courbes de vitesse : sans ça, le mouvement est saccadé.
- Afficher des repères (point central, ligne des yeux, règle des tiers) pour garder le point d'attention au même endroit entre les coupes.

**Texte et animation « pop »**
- Outil Texte, cliquer sur l'image, taper, régler police et couleurs dans les options d'effet selon l'identité de la chaîne.
- Effet Transform sur le texte : image clé d'échelle à ~70 % ; ~7 images plus loin, 110 % ; ~5 images plus loin, 100 %. Lisser légèrement. Ajouter lueur, glitch ou autre.
- Sélectionner texte + effets → clic droit → Enregistrer comme preset. Ensuite, glisser-déposer le preset sur un nouveau texte.

**Personnage**
- Tête ou logo généré par IA, posé sur une image de stock, exporté, importé ; animé avec images clés lissées ; enregistré en preset.

**Overlays et transitions**
- Overlay sur fond noir placé au-dessus du plan, mode de fusion **Écran**.
- Light leaks pour les transitions ; packs de presets (glissements, secousses, zooms, rotations).
- Effets favoris de l'auteur : lueur, 3D, Transform, flou, mosaïque.

**Sound design**
- Couper (mute) les pistes de voix off et de musique, regarder le montage, placer whoosh, risers, impacts et bruitages spécifiques. Combiner. Réactiver les pistes et baisser le volume des bruitages.

**Étalonnage**
- Effet Lumetri Color sur chaque plan : exposition, contraste, saturation.

## After Effects

Pour les animations complexes. Normal d'être perdu au début.
- Construire la base avec les outils Texte, Forme et Plume, d'après l'esquisse papier.
- Caler les éléments sur la voix off (importer l'audio dans la composition).
- Texte : animation machine à écrire (typewriter).
- Formes : Trim Paths pour les faire se tracer.
- Finir avec un effet de lueur.
- Notions à apprendre ensuite : voir la feuille de route dans `../ressources.md` (parenting, null object, caméra, tracking, puppet, wiggle, particules).
- Pour réutiliser une animation AE dans Remotion ou HyperFrames : l'exporter en Lottie.

## Canva

Pour les animations simples, sans logiciel complexe (l'auteur a fait les animations de sa première vidéo uniquement avec Canva).
- Reproduire l'esquisse avec formes, textes et graphiques, puis appliquer les animations intégrées.
- Si l'animation sera zoomée au montage, l'exporter en haute qualité, sinon elle devient floue.

## Notes DaVinci Resolve et CapCut

La méthode s'applique telle quelle ; seuls les noms changent. Indications générales, à vérifier dans la version de l'utilisateur :
- **DaVinci Resolve** : montage sur la page Edit (images clés dans l'Inspecteur, mode de composite « Screen » pour les overlays), animations avancées sur la page Fusion, étalonnage sur la page Color.
- **CapCut** : images clés sur la position, l'échelle et l'opacité ; mode de fusion « Écran » pour les overlays ; bibliothèque intégrée d'effets sonores et de transitions.
