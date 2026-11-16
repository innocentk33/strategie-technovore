# Correspondances : concept de montage → mise en œuvre par outil

La méthode décrit des concepts. Ce tableau dit comment les réaliser dans chaque famille d'outils. Les détails et exemples de code sont dans les fichiers dédiés : `adobe-canva.md`, `remotion.md`, `hyperframes.md`.

Si un skill officiel de l'outil (Remotion, HyperFrames) est disponible dans l'environnement, il fait foi pour la syntaxe : les API évoluent, ce tableau donne la direction.

## Différences fondamentales à garder en tête

| | Logiciels classiques (Premiere, After Effects, DaVinci, CapCut, Canva) | Remotion | HyperFrames |
|---|---|---|---|
| Langage | Interface graphique | React (TSX) | HTML + CSS + bibliothèque d'animation « seekable » (GSAP, CSS, Lottie, Three.js, Anime.js, WAAPI) |
| Unité de temps | Images et timecode | **Images (frames)** via `useCurrentFrame()` | **Secondes** (`data-start`, `data-duration`, durées GSAP) |
| Placement dans le temps | Timeline | `<Sequence from durationInFrames>` | Attributs `data-start` / `data-duration` / `data-track-index` sur les éléments `class="clip"` |
| Animation | Images clés + courbes | `interpolate()` / `spring()` avec easing | Timeline GSAP en pause, enregistrée pour être pilotée image par image |
| Piège principal | Rendu lourd | Les transitions/animations CSS et les classes d'animation Tailwind ne se rendent pas correctement : tout doit dépendre de l'image courante | Tout doit être « seekable » et déterministe : pas d'animation basée sur l'horloge réelle ni d'aléatoire non seedé |
| Force | Finesse manuelle, effets prêts à l'emploi | Animations pilotées par des données, composants réutilisables, génération par agent IA | HTML pur sans build, idéal pour agents IA, catalogue de blocs prêts à l'emploi |

Conversion utile à 60 i/s : 1 image ≈ 0,0167 s ; 7 images ≈ 0,12 s ; 30 images = 0,5 s ; 60 images = 1 s.

## Tableau des concepts

| Concept (méthode) | Logiciels classiques | Remotion | HyperFrames |
|---|---|---|---|
| Projet 1920×1080, 60 i/s | Paramètres de séquence | `<Composition width={1920} height={1080} fps={60} …>` | `data-width="1920" data-height="1080"` sur la composition ; cadence réglée au rendu |
| Poser la voix off et la musique | Pistes audio | Composant audio dans une `<Sequence>`, `volume` | `<audio data-start data-duration data-track-index data-volume>` |
| Mouvement fluide (keyframes + lissage) | Images clés + courbes de vitesse lissées | `interpolate(frame, [a, b], [x, y], { easing, extrapolate… 'clamp' })` ou `spring()` | Tween GSAP avec `ease` (`power2.out`, etc.) |
| Zoom avec point d'attention constant | Transform (échelle + position), repères règle des tiers | Échelle animée + `transformOrigin` placé sur le point d'attention (ex. `'33% 33%'`) | Idem en CSS : `transform-origin` + tween GSAP sur `scale` |
| Tracé qui se dessine (trim paths) | Trim Paths (AE) | `evolvePath()` de `@remotion/paths` sur un `<path>` SVG | Tween GSAP sur `strokeDashoffset` (ou plugin DrawSVG) |
| Texte machine à écrire | Animateur de texte « typewriter » | `texte.slice(0, n)` avec `n` calculé depuis l'image courante | Découpage par caractère (SplitText ou spans) + apparition échelonnée |
| Pop de texte 70 → 110 → 100 % | Effet Transform, 3 images clés | `interpolate(frame, [0, 7, 12], [0.7, 1.1, 1])` | Deux tweens GSAP : 0,12 s puis 0,08 s |
| Lueur (glow) | Effet Lueur | `filter: drop-shadow(…)` / `textShadow`, ou effet `glow()` de `@remotion/effects` sur un composant canvas | `filter: drop-shadow(…)` / `text-shadow` |
| Parenting / null object | Liens de parenté, objet nul | Imbriquer les éléments, animer le parent | Imbriquer les éléments, animer le parent (ou une sous-composition) |
| Caméra | Calque caméra (AE), zooms | Conteneur « caméra » transformé ; 3D via `@remotion/three` | Conteneur « caméra » transformé ; 3D via l'adaptateur Three.js |
| Wiggle (tremblement) | Expression `wiggle()` | Bruit seedé (`@remotion/noise`) ou `random(seed)` | Valeurs pseudo-aléatoires seedées précalculées (pas de `Math.random` à chaque image) |
| Particules | Effets de particules | Positions générées avec `random(seed)`, ou Three.js | Positions seedées, Three.js, ou bloc du catalogue |
| Déformation (puppet) | Outil Marionnette | Importer une animation Lottie (`@remotion/lottie`) | Adaptateur Lottie |
| Overlay sur fond noir | Mode de fusion Écran | `style={{ mixBlendMode: 'screen' }}` sur la vidéo d'overlay | `mix-blend-mode: screen` en CSS |
| Transitions, light leaks | Presets de transition, overlays light leak | `@remotion/transitions` (`TransitionSeries`) ; `lightLeak()` de `@remotion/effects` | Transitions shader (`@hyperframes/shader-transitions`, blocs du catalogue) ou overlay en mode Écran |
| Bruitage (whoosh, riser, impact) | Piste audio dédiée | Audio dans une `<Sequence from={…}>` calée sur l'image de l'événement ; banque `@remotion/sfx` | `<audio>` avec `data-start` égal à l'instant de l'événement |
| Coupe sur le rythme | Repères sur les temps forts | Calculer les images des temps forts et y caler les `<Sequence>` | Caler les `data-start` sur les temps forts ; skill `/music-to-video` pour un montage piloté par la musique |
| Sous-titres | Outil de sous-titres | `@remotion/captions` | Sous-titres gérés par les skills HyperFrames |
| Étalonnage | Lumetri (Premiere), page Color (DaVinci) | `filter: brightness() contrast() saturate()` ou effets de `@remotion/effects` | `filter: brightness() contrast() saturate()` |
| Réutilisation (preset) | Preset d'effet | Composant React avec props | Sous-composition ou bloc réutilisable |
| Pont depuis After Effects | — | Exporter l'animation AE en Lottie puis l'importer | Exporter en Lottie puis utiliser l'adaptateur Lottie |

## Pipelines hybrides

- **Montage classique + animations en code** : créer les animations dans Remotion ou HyperFrames, les rendre en vidéo, les importer dans le logiciel de montage. Pour superposer une animation, il faut soit un rendu avec transparence (Remotion sait le faire : ProRes 4444 ou WebM avec canal alpha ; pour HyperFrames, vérifier la documentation), soit un rendu sur fond noir utilisé en mode Écran.
- **Montage 100 % code** : la voix off devient une piste audio, le script coloré devient la liste des scènes, et chaque passage devient une séquence avec début et durée. Voir la section « Montage 100 % code » de `remotion.md` ou `hyperframes.md`.

## Quel outil conseiller pour une animation ?

- Animation simple, unique, sans données : Canva ou l'outil déjà utilisé.
- Animation complexe et artisanale (personnage, tracking, effets organiques) : After Effects ou équivalent.
- Animation pilotée par des données (graphiques, chiffres, listes), répétée d'une vidéo à l'autre, déclinée en plusieurs langues ou formats, ou générée par un agent IA : Remotion (si l'utilisateur est à l'aise avec React) ou HyperFrames (si HTML/CSS lui suffit, sans étape de build).
