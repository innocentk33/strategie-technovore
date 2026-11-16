# Ressources et feuille de route d'apprentissage

## Sommaire
1. Outils utilisés par l'auteur
2. Sources d'assets
3. Feuille de route d'apprentissage des animations (tous outils)
4. Chaînes et tutoriels recommandés
5. Documentation Remotion et HyperFrames

---

## 1. Outils utilisés par l'auteur
| Outil | Usage |
|---|---|
| ElevenLabs | Voix off IA |
| Pikzels | Inspiration pour les miniatures |
| Epidemic Sound | Musique et bruitages libres de droits |
| Spunkram Library | Plugin de montage pour Premiere Pro |
| Notion | Planification (script coloré, suivi) |
| VidIQ | SEO et recherche de mots-clés |

Il propose aussi des presets Premiere Pro gratuits et expérimentaux (« Screen Presets ») pour animer les captures d'écran.

## 2. Sources d'assets
- **Musique** : playlists YouTube sans droits ; Epidemic Sound (coller un lien Spotify permet d'y trouver des morceaux similaires).
- **Bruitages** : playlists YouTube ; Epidemic Sound, classés en whoosh, riser, impact et autres.
- **Overlays** : playlists YouTube de transitions et de lueurs sur fond noir.
- **Scènes de films** : chaînes YouTube @movieclips et @joblomovieclips ; playphrase.me pour retrouver une réplique précise.
- **Images et vidéos** : recherche Google ; banques gratuites Freepik, Pexels, Unsplash ; génération IA (Midjourney, Leonardo, ChatGPT, Gemini, Minimax).

Rappel : vérifier les droits d'utilisation de tout extrait de film ou image trouvée.

## 3. Feuille de route d'apprentissage des animations

Les mots-clés viennent de la liste After Effects de l'auteur. Ils désignent des **concepts** qui existent dans les autres outils ; la colonne « équivalent » renvoie à `outils/correspondances.md` pour la mise en œuvre. Suggère une seule notion à la fois, la suivante dans l'ordre que l'utilisateur ne maîtrise pas encore et qui servirait sa vidéo actuelle.

| Niveau | Concept (terme After Effects) | Ce que ça permet | Équivalent hors AE |
|---|---|---|---|
| 1 | Keyframes + lissage | Tout mouvement fluide | Interpolation avec easing (`interpolate()`, tween GSAP) |
| 1 | Pen tool | Dessiner des formes libres | Tracés SVG |
| 1 | Trim paths | Tracé qui se dessine | Animation de `stroke-dashoffset` |
| 1 | Raccourcis clavier | Aller vite | Snippets, composants réutilisables |
| 2 | Text animation | Machine à écrire, apparition par lettre | Découpage du texte par caractère |
| 2 | Parenting | Un élément entraîne les autres | Imbrication d'éléments, transformation du parent |
| 2 | Null object | Piloter un groupe par un contrôleur invisible | Conteneur vide animé, variables partagées |
| 2 | Camera | Zooms, panoramiques, 3D | Conteneur « caméra » transformé ; Three.js |
| 3 | Tracking | Coller un élément sur un objet qui bouge | Coordonnées animées (souvent préparées dans un logiciel classique) |
| 3 | Puppet tool | Déformer une illustration | Lottie, animation de tracés SVG |
| 3 | Wiggle expression | Tremblement, mouvement organique | Bruit déterministe (seedé) |
| 3 | Particle effect | Poussière, étincelles, confettis | Particules générées avec un aléatoire seedé, Three.js, blocs prêts à l'emploi |

## 4. Chaînes et tutoriels recommandés
- **Chaînes After Effects** : Mapal, TomsProject, After Effects Basics, Ben Marriott, Bricks, Adobe in a Minute.
- **Tutoriels cités par l'auteur** (titres en anglais) :
  - How To Animate Infographics Like VOX (Mapal)
  - How to edit SO good your viewers get addicted to your videos (Learn By Leo)
  - 3 Editing Secrets I Wish I Knew Earlier (HillierSmith)
  - How To Animate Like Dan Koe – Minimalistic Animations (Mapal)
  - 6 Easy Ways to Film Yourself AND Still Look Cinematic (TristanNich)
  - How To Edit Like Iman Gadzhi – Crazy Graph Animation (TomsProject)

Ces tutoriels sont faits pour After Effects, mais leurs **idées de mouvement** se transposent : regarder le tutoriel pour le design et le timing, puis reproduire les concepts dans son outil avec `outils/correspondances.md`.

## 5. Documentation Remotion et HyperFrames
- **Remotion** : documentation officielle sur remotion.dev. Skills officiels pour agents IA disponibles ; s'ils sont installés dans l'environnement (`remotion-best-practices`, `remotion-markup`, etc.), les consulter pour la syntaxe à jour.
- **HyperFrames** : documentation sur hyperframes.heygen.com, terrain de jeu sur hyperframes.dev, catalogue de blocs (transitions, overlays, sous-titres, graphiques, cartes). Skills pour agents installables avec `npx skills add heygen-com/hyperframes`.
