# Skill : coach-montage-video (copie du 16/11/2026, tous ses fichiers à la suite)


---
## Fichier : coach-montage-video/SKILL.md

---
name: "coach-montage-video"
description: Coach de montage vidéo YouTube (style « fancy editing », avec animations, textes animés, overlays et sound design) qui critique des scripts de montage et guide le montage étape par étape, quel que soit l'outil (Premiere Pro, After Effects, Canva, DaVinci Resolve, CapCut, ou montage en code avec Remotion ou HyperFrames). Utilise ce skill dès que l'utilisateur partage un script, un storyboard, une voix off annotée ou un plan de montage et demande un avis, une critique, une relecture ou des améliorations, quand il veut structurer l'histoire d'une vidéo (voyage du héros), et aussi quand il demande comment monter une vidéo, la rendre plus dynamique, où placer effets, textes, musique, bruitages ou animations, ou comment traduire une animation d'After Effects vers Remotion ou HyperFrames, même s'il ne dit pas explicitement « critique » ou « montage ».
---

# Coach montage vidéo

Ce skill applique la méthode de montage d'un créateur YouTube spécialisé dans le montage « fancy » (animations, textes animés, overlays, sound design soigné), tirée de son tutoriel et de son guide de référence (« The Editing Guide »). Il a deux usages :

- **Mode A – Critiquer un script de montage** : l'utilisateur fournit un script (voix off seule ou annotée) et veut savoir ce qui cloche et comment l'améliorer.
- **Mode B – Accompagner un montage** : l'utilisateur veut suivre la méthode pour monter une vidéo, ou bloque sur une étape.

Un texte collé + « qu'en penses-tu » = mode A ; « comment je fais pour… » = mode B.

Réponds dans la langue de l'utilisateur (le français par défaut).

## Fichiers de référence

Lis-les au moment où ils servent, pas tous d'un coup :

| Fichier | Quand le lire |
|---|---|
| `references/principes-montage.md` | Toujours, avant de critiquer ou de guider : la méthode complète, indépendante de l'outil. |
| `references/voyage-du-heros.md` | Pour évaluer ou construire le récit d'une vidéo (axe 4, étape script). |
| `references/outils/correspondances.md` | Dès qu'il faut dire *comment* réaliser une technique : table concept → outil. |
| `references/outils/adobe-canva.md` | Si l'utilisateur monte avec Premiere Pro, After Effects ou Canva. |
| `references/outils/remotion.md` | Si l'utilisateur monte ou anime avec Remotion (React). |
| `references/outils/hyperframes.md` | Si l'utilisateur monte ou anime avec HyperFrames (HTML). |
| `references/ressources.md` | Pour recommander des sources d'assets, des outils ou la prochaine technique à apprendre. |
| `assets/modele-script-montage.txt` | À proposer quand l'utilisateur n'a pas de format de script de montage. |

## Étape 0 – Identifier l'outil (les deux modes)

La méthode est la même quel que soit le logiciel ; seule la mise en œuvre change. Repère l'outil de l'utilisateur dans son message ou son script (mentions de keyframes, de composition, de JSX, de `data-start`, etc.).

- **Outil connu** : donne les instructions concrètes pour cet outil, en t'appuyant sur le fichier `references/outils/` correspondant.
- **Outil inconnu** : formule les conseils en concepts (« un tracé qui se dessine progressivement », « un zoom lissé ») et donne l'exemple dans un seul outil, sans bloquer pour demander.
- **Remotion ou HyperFrames** : si des skills dédiés à ces outils sont disponibles dans l'environnement (par exemple `remotion-best-practices`, `remotion-markup`, ou les skills `hyperframes`), consulte-les pour la syntaxe exacte avant d'écrire du code. Ce skill-ci dit *quoi* faire et *pourquoi* ; eux disent *comment* l'écrire correctement dans la version actuelle de l'outil.
- **Pipeline hybride** fréquent : montage dans un logiciel classique, animations générées en code puis importées en vidéo. Tiens-en compte dans tes conseils.

---

## Mode A – Critique d'un script de montage

### Ce qu'est un « script de montage »

Le plus souvent : le texte de la voix off découpé en passages, avec pour chacun ce qu'on voit et entend (vidéo, image, capture d'écran, animation, texte à l'écran, musique, bruitage). Si le script ne contient que la voix off, critique quand même le fond (idée, récit, rythme) et propose toi-même la catégorisation visuelle. Le but est de faire avancer la vidéo, pas de remplir un formulaire.

### Étapes

1. **Lis le script en entier** avant de commenter.
2. **Établis la fiche d'identité** de la vidéo sur quatre axes : cible (débutant ↔ avancé), but (théorique ↔ pratique), ambiance (éducatif ↔ divertissant), complexité (simple ↔ complexe). Si l'utilisateur ne l'a pas donnée, déduis-la et dis-le. Elle sert d'étalon : un montage n'est bon ou mauvais que par rapport à elle.
3. **Cartographie le récit** avec le voyage du héros (`references/voyage-du-heros.md`) : quelles étapes existent, lesquelles manquent.
4. **Passe la grille d'évaluation**. Chaque remarque pointe un passage précis du script.
5. **Rédige le rapport** au format imposé.

### Grille d'évaluation

Note chaque axe sur 5 (5 = rien d'important à changer ; 3 = fonctionne mais un problème visible ; 1 = bloque la vidéo). Axe impossible à juger : « – » et une phrase sur ce qui manque.

| # | Axe | Question clé |
|---|-----|--------------|
| 1 | Identité & cohérence | Le style de montage prévu colle-t-il à la cible, au but, à l'ambiance et à la complexité ? |
| 2 | Idée & miniature | Un inconnu de la cible cliquerait-il ? Le concept et la miniature s'appuient-ils sur quelque chose d'éprouvé ? |
| 3 | Structure & progression | Le fil avance-t-il du début à la fin ? Le problème profond est-il posé ? Les parties inutiles sont-elles coupées ? |
| 4 | Récit (voyage du héros) | Y a-t-il une histoire secondaire qui suit les étapes clés : appel, mentor, épreuves, crise, retour ? |
| 5 | Préparation visuelle | Chaque passage a-t-il un visuel identifié et catégorisé (code couleur) ? Des trous ? |
| 6 | Rythme & espace | Des longueurs vides ? Des moments forts étouffés faute de respiration ? |
| 7 | Pertinence des effets | Chaque effet sert-il ce qui est dit, ou est-ce de la décoration ? |
| 8 | Texte à l'écran | Parcimonieux, sur les moments importants, dans l'un des 3 usages (sous-titre, texte central, texte intégré) ? |
| 9 | Animations | Chaque animation est-elle esquissée, utile, assez précise pour être réalisée, et faisable dans l'outil choisi ? |
| 10 | Musique | Ambiance définie par partie ? Coupes calées sur le rythme ? |
| 11 | Sound design | Whoosh, risers, impacts et bruitages spécifiques prévus aux bons endroits ? |
| 12 | Point d'attention | Zooms et enchaînements gardent-ils le regard au même endroit (règle des tiers) ? |
| 13 | Nouveauté | La vidéo tente-t-elle au moins une technique nouvelle ? |

### Principes qui guident la critique

- **Le fond d'abord.** Un montage brillant ne sauve ni une idée faible ni un récit absent. Si les axes 1 à 4 sont faibles, dis-le en premier, même si l'utilisateur ne demandait que des conseils d'effets.
- **Couper n'est pas forcément mieux.** Le public n'a pas moins d'attention, il est plus exigeant : une pause est bonne si ce qui suit la récompense. Signale les longueurs vides ET les moments qui mériteraient de respirer.
- **Moins d'effets, mieux placés.** Si le script accumule effets, textes et bruitages, recommande d'en retirer.
- **Concret et actionnable dans l'outil de l'utilisateur.** « Rendre plus dynamique » ne sert à rien. « Passage 12 : zoom lent sur le graphique centré sur le tiers gauche, riser jusqu'au chiffre, impact sur le chiffre » est utile, suivi de la façon de le faire dans son outil (réglage Premiere, `interpolate()` Remotion, tween GSAP HyperFrames…).
- **Des animations spécifiées.** Une ligne « animation stylée ici » n'est pas réalisable, surtout en code ou par un agent IA. Quand une animation est floue, réécris-la sous forme de fiche d'animation (voir le modèle).
- **Honnêteté bienveillante.** Ne gonfle pas les notes.
- **Contre le perfectionnisme.** Trois priorités maximum ; le reste va dans « Détails optionnels ».

### Format du rapport

```
## Verdict en une phrase
[Ce qui marche le mieux + le principal frein.]

## Fiche d'identité
Cible : … | But : … | Ambiance : … | Complexité : … (déduite / fournie)
Outil de montage : … (déduit / fourni / inconnu)

## Carte du voyage du héros
| Étape | Passage du script | Statut (présente / faible / absente) |
(uniquement les étapes clés ; voir references/voyage-du-heros.md)

## Notes par axe
| Axe | Note | Commentaire court |
(les 13 axes)

## Les 3 priorités
1. [Problème] → [passage concerné] → [correction concrète, avec la mise en œuvre dans l'outil]
2. …
3. …

## Annotations passage par passage
| Passage | Constat | Suggestion de montage |
(uniquement les passages qui méritent un commentaire)

## Détails optionnels
[Améliorations mineures, en quelques lignes.]

## Une chose nouvelle à essayer dans cette vidéo
[Une seule technique, adaptée à la vidéo et à l'outil, tirée de la feuille de route de references/ressources.md, avec comment s'y prendre.]
```

Si l'utilisateur demande une version réécrite ou annotée du script, fournis-la après le rapport en suivant `assets/modele-script-montage.txt`.

---

## Mode B – Accompagner un montage

Repère où en est l'utilisateur et guide-le à partir de là, une étape à la fois.

1. **Identité** – fixer cible, but, ambiance, complexité.
2. **Fondations** – idée intéressante pour la cible ; miniature basée sur un concept éprouvé ; script : plan, recherche, problème profond, voyage du héros, affinage.
3. **Voix off** – micro ou voix IA, complète avant de monter.
4. **Inspiration** – regarder un bon film avec un œil de monteur.
5. **Ressources** – musique, bruitages, overlays, presets ou composants réutilisables.
6. **Script coloré** – une catégorie (et une couleur) par passage, puis collecte de tous les éléments.
7. **Montage brut** – projet en 1920×1080, 60 i/s ; voix off découpée ; musique posée tout de suite ; visuels placés selon les couleurs ; coupes sur le rythme.
8. **Animations** – esquisse papier → fiche d'animation → réalisation dans l'outil adapté (Canva, After Effects, Remotion, HyperFrames…) → calage sur la voix off.
9. **Deuxième passe** – revoir, ajouter, couper ce qui ne sert pas l'objectif, gérer l'espace.
10. **Finitions** – zooms lissés et point d'attention constant, textes, personnage éventuel, overlays et transitions, effets avec parcimonie.
11. **Sound design** – autres pistes coupées, bruitages placés, combinés, puis volume baissé.
12. **Étalonnage** – exposition, contraste, saturation plan par plan.
13. **Publier** – « suffisant » vaut mieux que « parfait ».

Pour chaque étape, la méthode est dans `references/principes-montage.md` et la mise en œuvre par outil dans `references/outils/`. Si l'utilisateur monte entièrement en code, chaque fichier d'outil décrit comment ces étapes se traduisent (voix off comme piste audio, timings issus du script, scènes en séquences).

Rappels à transmettre quand c'est pertinent, sans sermon :
- Une seule nouvelle technique par vidéo, jusqu'à la maîtriser.
- Un effet qu'on sait faire n'est pas un effet qu'on doit mettre.
- Si l'utilisateur tourne en rond sur les mêmes retouches, dis-le franchement et encourage-le à publier.


---
## Fichier : coach-montage-video/assets/modele-script-montage.txt

MODÈLE DE SCRIPT DE MONTAGE
===========================

FICHE D'IDENTITÉ
  Titre de la vidéo        :
  Cible                    : débutant  <->  avancé
  But                      : théorique <->  pratique
  Ambiance                 : éducatif  <->  divertissant
  Complexité               : simple    <->  complexe
  Concept de miniature     : (sur quoi s'appuie-t-il de déjà éprouvé ?)
  Problème profond         :
  Outil de montage         : (Premiere / After Effects / Canva / DaVinci / CapCut / Remotion / HyperFrames / hybride)
  Technique nouvelle tentée:

HISTOIRE SECONDAIRE (voyage du héros, une ligne par étape, laisser vide si absente)
  Héros                    :
  01 Statu quo             :
  02 Appel à l'aventure    :
  03 Aide / mentor         :
  04 Départ                :
  05 Épreuves              : = le contenu principal
  06 Approche              :
  07 Crise                 :
  08 Trésor                :
  09 Résultat              :
  10 Retour                :
  11 Nouvelle vie          :
  12 Résolution            :

CODE COULEUR (surlignage Notion)
  [VID] Vidéo / B-roll ......... Bleu    fond #E7F3F8  texte #337EA9
  [IMG] Image .................. Vert    fond #EDF3EC  texte #448361
  [ECR] Capture d'écran ........ Violet  fond #F6F3F9  texte #9065B0
  [ANI] Animation .............. Orange  fond #FBECDD  texte #D9730D
  [TXT] Texte sur fond noir .... Gris    fond #F1F1EF  texte #787774
  [MEM] Mème / blague visuelle . Rose    fond #FAF1F5  texte #C14C8A
  Suivi : Jaune = à retravailler (#FBF3DB / #CB912F)
          Rouge = élément manquant (#FDEBEC / #D44C47)
          Marron = pause voulue (#F4EEEE / #9F6B53)

---------------------------------------------------------------
PARTIE 1 – [Nom]   Étape du héros : [..]   Musique : [ambiance / morceau]
---------------------------------------------------------------

#01   [début ≈ 0:00]
VO      : "Texte exact de la voix off."
VISUEL  : [CATÉGORIE] description de ce qu'on voit
TEXTE   : (aucun | sous-titre | texte central | texte intégré) + contenu
EFFETS  : zoom (point d'attention : centre / tiers gauche / tiers droit), overlay, transition… ou rien
SON     : whoosh / riser / impact / bruitage spécifique, et à quel instant ; ou rien
NOTE    : pause voulue, coupe sur le rythme, etc.

#02   [début ≈ 0:00]
VO      :
VISUEL  :
TEXTE   :
EFFETS  :
SON     :
NOTE    :

---------------------------------------------------------------
PARTIE 2 – [Nom]   Étape du héros : [..]   Musique : [ambiance / morceau]
---------------------------------------------------------------

#03   [début ≈ 0:00]
VO      :
VISUEL  :
TEXTE   :
EFFETS  :
SON     :
NOTE    :

===============================================================
FICHE D'ANIMATION (une par élément [ANI])
Assez précise pour être réalisée à la main ou codée par un agent IA.
===============================================================

ANI-01   lié au passage #..
  Esquisse     : (description ou lien vers le croquis)
  Éléments     : formes, textes, icônes, couleurs
  État initial : ce qu'on voit à la première image
  Déroulé      :
    t = 0,00 s  ...
    t = 0,50 s  ...
    t = 1,20 s  ...
  Easing       : (lissé en sortie / en entrée et sortie / rebond…)
  Point d'attention : (où le regard doit être à la fin)
  Son associé  : (whoosh à t = .., impact à t = ..)
  Outil prévu  : (Canva / After Effects / Remotion / HyperFrames)
  Export       : (vidéo normale / fond noir + mode Écran / transparence)


---
## Fichier : coach-montage-video/references/outils/adobe-canva.md

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


---
## Fichier : coach-montage-video/references/outils/correspondances.md

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


---
## Fichier : coach-montage-video/references/outils/hyperframes.md

# Mise en œuvre : HyperFrames (HTML)

HyperFrames (open source, par HeyGen) décrit une vidéo en HTML : des éléments placés dans le temps avec des attributs `data-*`, animés par une bibliothèque « seekable » (GSAP le plus souvent, mais aussi CSS, Lottie, Three.js, Anime.js, WAAPI), puis rendus en MP4 par un navigateur sans interface et FFmpeg. Pas d'étape de build : le fichier `index.html` se prévisualise tel quel.

Le framework est jeune et évolue vite. Si les skills HyperFrames sont disponibles dans l'environnement (`/hyperframes`, `/hyperframes-core`, `/music-to-video`…), ils font foi. Sinon, ils s'installent avec `npx skills add heygen-com/hyperframes`, et la documentation est sur hyperframes.heygen.com.

## Règles d'or
- Le temps se compte en **secondes**. Les valeurs « en images » de la méthode se convertissent à 60 i/s (7 images ≈ 0,12 s).
- Chaque élément temporel porte `class="clip"`, `data-start`, `data-duration` et `data-track-index`.
- Les animations vivent dans une timeline GSAP **en pause**, enregistrée dans `window.__timelines[<id de composition>]` : c'est le moteur qui la positionne à chaque image. Les positions dans la timeline sont des instants de la composition.
- Déterminisme : pas d'animation liée à l'horloge réelle, pas de `Math.random()` évalué au rendu. Précalculer les valeurs aléatoires avec un générateur seedé.
- Les vidéos sont muettes (`muted playsinline`) ; le son passe par des éléments `<audio>`.
- Une animation réutilisable = une sous-composition ou un bloc du catalogue (l'équivalent d'un preset).

## Squelette de composition
```html
<div id="stage" data-composition-id="video" data-start="0" data-width="1920" data-height="1080">
  <!-- éléments .clip ici -->
  <script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({ paused: true });
    // tweens ici
    window.__timelines = window.__timelines || {};
    window.__timelines.video = tl;
  </script>
</div>
```

## Recettes

### Pop de texte (70 → 110 → 100 %)
```html
<h1 id="titre" class="clip" data-start="2" data-duration="3" data-track-index="1"
    style="filter: drop-shadow(0 0 12px #D9730D)">Texte</h1>
```
```js
tl.fromTo("#titre", { scale: 0.7 }, { scale: 1.1, duration: 0.12, ease: "power2.out" }, 2)
  .to("#titre", { scale: 1, duration: 0.08, ease: "power1.inOut" });
```

### Zoom lissé avec point d'attention sur la règle des tiers
```html
<div id="camera" class="clip" data-start="10" data-duration="4" data-track-index="0"
     style="transform-origin: 33.3% 33.3%"> <!-- plan --> </div>
```
```js
tl.fromTo("#camera", { scale: 1 }, { scale: 1.3, duration: 0.75, ease: "power2.inOut" }, 10);
```
Garder le même `transform-origin` d'un plan à l'autre maintient le regard au même endroit entre les coupes.

### Tracé qui se dessine (équivalent Trim Paths)
```js
const path = document.querySelector("#fleche");
const len = path.getTotalLength();
gsap.set(path, { strokeDasharray: len, strokeDashoffset: len });
tl.to(path, { strokeDashoffset: 0, duration: 0.5, ease: "power2.out" }, 4);
```

### Texte machine à écrire
```js
const el = document.querySelector("#machine");
el.innerHTML = [...el.textContent].map(c => `<span style="opacity:0">${c}</span>`).join("");
tl.to("#machine span", { opacity: 1, duration: 0.01, stagger: 0.035 }, 5);
```

### Overlay sur fond noir (mode Écran)
```html
<video class="clip" src="overlays/light-leak.mp4" data-start="8" data-duration="1.5"
       data-track-index="3" muted playsinline style="mix-blend-mode: screen"></video>
```
Le catalogue propose aussi des transitions prêtes à l'emploi (par exemple `npx hyperframes add flash-through-white`) et le paquet `@hyperframes/shader-transitions`.

### Bruitage calé sur un événement
```html
<audio src="sfx/impact.wav" data-start="12.4" data-duration="1" data-track-index="5" data-volume="0.4"></audio>
```
Un riser se place pour **finir** sur l'événement : `data-start = événement − durée du riser`.

### Étalonnage
`filter: brightness(1.05) contrast(1.1) saturate(1.15);` sur le plan.

## Montage 100 % code : traduction des étapes de la méthode

| Étape de la méthode | En HyperFrames |
|---|---|
| Projet 1920×1080, 60 i/s | `data-width` / `data-height` sur la composition ; cadence choisie au rendu (voir l'aide de `npx hyperframes render`) |
| Voix off découpée | Un `<audio>` pour la voix off ; les débuts de passages viennent du script (minutage ou transcription horodatée) |
| Musique posée tout de suite | `<audio>` sur toute la durée, `data-volume` réduit |
| Script coloré | Chaque passage devient un `.clip` ; la couleur indique le type d'élément (VID, IMG, ECR, ANI, TXT, MEM) |
| Coupes sur le rythme | `data-start` calés sur les temps forts ; skill `/music-to-video` quand la musique doit piloter le montage |
| Sous-titres, voix IA, animation réactive au son | Gérés par les skills HyperFrames |
| Prévisualiser / exporter | `npx hyperframes preview` puis `npx hyperframes render` (Node.js 22+ et FFmpeg requis) |

Migration : le skill `/remotion-to-hyperframes` porte une composition Remotion existante vers HyperFrames.


---
## Fichier : coach-montage-video/references/outils/remotion.md

# Mise en œuvre : Remotion (React)

Remotion décrit une vidéo avec des composants React rendus image par image. Ce fichier traduit la méthode en recettes Remotion. Si les skills Remotion officiels sont disponibles dans l'environnement (`remotion-best-practices`, `remotion-markup`, `remotion-captions`…), ils font foi pour la syntaxe et les imports selon la version installée.

## Règles d'or
- Tout mouvement dépend de `useCurrentFrame()`. Les transitions et animations CSS, ou les classes d'animation Tailwind, ne se rendent pas correctement.
- Le temps se compte en **images**. À 60 i/s, une durée en secondes × 60 = images. Garder une petite fonction `const s = (sec: number) => Math.round(sec * fps)` évite les erreurs.
- Dans une `<Sequence from={…}>`, `useCurrentFrame()` repart de 0 : chaque animation peut être écrite comme si elle commençait au début.
- Aléatoire : uniquement `random('graine')` de `remotion` ou le bruit de `@remotion/noise`, jamais `Math.random()` (chaque image serait différente au rendu).
- Une animation réutilisable = un composant avec des props (l'équivalent d'un preset).

## Recettes

### Pop de texte (70 → 110 → 100 %)
```tsx
import { Easing, interpolate, useCurrentFrame } from "remotion";

export const PopText: React.FC<{ text: string; color?: string }> = ({ text, color = "#D9730D" }) => {
  const frame = useCurrentFrame();
  const scale = interpolate(frame, [0, 7, 12], [0.7, 1.1, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.quad),
  });
  return (
    <div style={{ transform: `scale(${scale})`, filter: `drop-shadow(0 0 12px ${color})` }}>
      {text}
    </div>
  );
};
```

### Zoom lissé avec point d'attention sur la règle des tiers
```tsx
const frame = useCurrentFrame();
const scale = interpolate(frame, [0, 45], [1, 1.3], {
  extrapolateRight: "clamp",
  easing: Easing.inOut(Easing.cubic),
});
// transformOrigin = le point qui reste fixe : le sujet, placé sur un tiers
<AbsoluteFill style={{ transform: `scale(${scale})`, transformOrigin: "33.3% 33.3%" }}>
  {/* plan */}
</AbsoluteFill>
```
Garder le même `transformOrigin` d'un plan à l'autre maintient le regard au même endroit entre les coupes.

### Tracé qui se dessine (équivalent Trim Paths)
```tsx
import { evolvePath } from "@remotion/paths";

const progress = interpolate(frame, [0, 30], [0, 1], {
  extrapolateRight: "clamp",
  easing: Easing.out(Easing.cubic),
});
const { strokeDasharray, strokeDashoffset } = evolvePath(progress, d);
<path d={d} fill="none" stroke="#fff" strokeWidth={6}
      strokeDasharray={strokeDasharray} strokeDashoffset={strokeDashoffset} />
```

### Texte machine à écrire
```tsx
const visible = Math.floor(
  interpolate(frame, [0, text.length * 2], [0, text.length], { extrapolateRight: "clamp" })
);
<span>{text.slice(0, visible)}</span>
```

### Overlay sur fond noir (mode Écran)
```tsx
import { Video } from "@remotion/media";
import { staticFile } from "remotion";

<Video src={staticFile("overlays/light-leak.mp4")} style={{ mixBlendMode: "screen" }} />
```
Pour les light leaks de transition, Remotion propose aussi `lightLeak()` (`@remotion/effects`) et les transitions `@remotion/transitions` (`TransitionSeries`).

### Bruitage calé sur un événement
```tsx
import { Audio } from "@remotion/media";

<Sequence from={s(12.4)}>          {/* instant de l'impact */}
  <Audio src={staticFile("sfx/impact.wav")} volume={0.4} />
</Sequence>
```
Un riser se place pour **finir** sur l'événement : `from = événement − durée du riser`.

### Étalonnage
`filter: "brightness(1.05) contrast(1.1) saturate(1.15)"` sur le plan, ou les effets `brightness()`, `contrast()`, `saturation()` de `@remotion/effects` pour les composants canvas.

## Montage 100 % code : traduction des étapes de la méthode

| Étape de la méthode | En Remotion |
|---|---|
| Projet 1920×1080, 60 i/s | `<Composition width={1920} height={1080} fps={60} durationInFrames={…}>` |
| Voix off découpée | Fichier audio de la voix off ; les débuts de passages viennent du script (minutage ou transcription horodatée) |
| Musique posée tout de suite | Piste audio sur toute la durée, volume réduit sous la voix |
| Script coloré | Un tableau de scènes `{ debut, duree, categorie, contenu }` qui génère les `<Sequence>` : la couleur devient le type de composant (VID, IMG, ECR, ANI, TXT, MEM) |
| Coupes sur le rythme | Liste des images des temps forts, utilisée pour caler les débuts de scènes |
| Sous-titres | `@remotion/captions` |
| Sound design | Une liste de bruitages `{ instant, fichier, volume }` rendue en `<Sequence>` |
| Prévisualiser / exporter | Remotion Studio pour prévisualiser, rendu en MP4 ; rendu avec transparence possible (ProRes 4444 ou WebM) pour importer une animation dans un autre logiciel |

Avantage pour la critique : comme tout est décrit en données, une remarque du rapport peut souvent se traduire par une modification précise d'une ligne du tableau de scènes.


---
## Fichier : coach-montage-video/references/principes-montage.md

# Principes de montage – méthode indépendante de l'outil

Synthèse de la méthode du tutoriel et de son guide de référence. Ce fichier décrit *quoi* faire et *pourquoi*. La mise en œuvre dans chaque logiciel est dans `outils/`. Les chiffres sont ceux de l'auteur : des points de départ, pas des règles absolues.

## Sommaire
1. Identité de la vidéo
2. Fondations : idée, miniature, script
3. Voix off
4. Inspiration
5. Ressources
6. Script coloré et collecte
7. Configuration du projet
8. Montage brut
9. Animations
10. Deuxième passe et gestion de l'espace
11. Zooms et point d'attention
12. Texte à l'écran
13. Personnage / mascotte
14. Overlays, transitions, effets
15. Sound design
16. Étalonnage
17. Progresser et publier

---

## 1. Identité de la vidéo
Avant tout, situer la vidéo sur quatre axes :

| Question | Spectre |
|---|---|
| Qui est la cible ? | débutant ↔ avancé |
| Quel est le but principal ? | théorique ↔ pratique |
| Quelle ambiance ? | éducatif ↔ divertissant |
| Quelle complexité ? | simple ↔ complexe |

Ces réponses décident du style de montage. Un montage ultra-rapide façon MrBeast ne convient pas à une vidéo calme et posée. Cette méthode enseigne un style précis : le montage « fancy » (animations, textes animés, overlays, effets lumineux, sound design dense).

## 2. Fondations : idée, miniature, script
Un excellent montage ne sauve ni une idée faible ni un script ennuyeux.

- **Idée** : intéressante pour la cible ? Un inconnu cliquerait-il ?
- **Miniature** : partir d'un concept éprouvé (ce qui marche déjà dans la niche), pas d'une idée sortie de nulle part.
- **Script** :
  1. **Plan** : lister tous les points à couvrir, écrire tout ce qui vient en tête.
  2. **Recherche** : s'appuyer sur des faits, exemples et sources solides.
  3. **Problème profond** : identifier la vraie difficulté ou la vraie question sous le sujet apparent.
  4. **Voyage du héros** : construire une histoire secondaire qui porte la vidéo (voir `voyage-du-heros.md`). Le contenu principal se loge dans l'étape « épreuves ».
  5. **Affiner** : couper l'inutile, simplifier (une IA peut aider), construire une progression du début à la fin.
  6. **Code couleur** : voir section 6.

## 3. Voix off
- Micro, ou voix IA (ex. ElevenLabs) ; les voix IA rendent désormais des émotions.
- Générer par petits morceaux plutôt qu'en un seul bloc.
- Terminer la voix off avant de monter : elle sert de colonne vertébrale au montage.

## 4. Inspiration
- Regarder d'autres vidéastes, mais surtout **un bon film** avec un regard de monteur : transitions, narration, montages, angles de caméra. Beaucoup de ces techniques n'ont presque jamais été utilisées sur YouTube : c'est la meilleure source d'originalité.
- Ne pas en faire une excuse pour procrastiner.

## 5. Ressources
- Quatre familles : musique, effets sonores, overlays, presets (ou, en montage par code, composants et blocs réutilisables).
- Se constituer une bibliothèque réutilisable. Sources dans `ressources.md`.

## 6. Script coloré et collecte
- Attribuer à chaque passage du script une catégorie selon ce qu'on voit à l'écran. L'auteur utilise 6 catégories, à adapter. Code couleur proposé (couleurs de surlignage Notion) :

| Catégorie | Étiquette | Couleur | Fond | Texte |
|---|---|---|---|---|
| Vidéo / B-roll | [VID] | Bleu | `#E7F3F8` | `#337EA9` |
| Image | [IMG] | Vert | `#EDF3EC` | `#448361` |
| Capture d'écran | [ECR] | Violet | `#F6F3F9` | `#9065B0` |
| Animation | [ANI] | Orange | `#FBECDD` | `#D9730D` |
| Texte sur fond noir | [TXT] | Gris | `#F1F1EF` | `#787774` |
| Mème / blague visuelle | [MEM] | Rose | `#FAF1F5` | `#C14C8A` |

  Couleurs libres pour le suivi : jaune (`#FBF3DB` / `#CB912F`) = à retravailler ; rouge (`#FDEBEC` / `#D44C47`) = élément manquant ; marron (`#F4EEEE` / `#9F6B53`) = pause ou respiration voulue. L'orange est réservé aux animations parce que ce sont les éléments les plus longs à produire : ils doivent sauter aux yeux.
- Une fois tout le script coloré, rassembler **tous** les éléments de chaque catégorie avant de monter. Les animations sont seulement repérées (et esquissées) à ce stade.

## 7. Configuration du projet
- 1920×1080 (4K seulement si la machine suit), 60 images/s.
- Espace de travail organisé à sa main.

## 8. Montage brut
1. Poser la voix off, la découper selon le script, supprimer les pauses gênantes.
2. **Poser la musique juste après la voix off** (et non à la fin) : elle fixe l'ambiance, permet de couper sur le rythme, rend le travail plus agréable. Régler son volume sous la voix.
3. Placer vidéos, images et captures selon les couleurs du script.
4. Expérimenter des coupes sur les temps forts de la musique (facultatif pour un débutant).
5. Un simple texte sur fond noir est une option visuelle valable.

## 9. Animations
- **Esquisser sur papier d'abord.** Exemple : des cases reliées par des flèches comme un organigramme, titres floutés, zoom sur la première case qui révèle son texte.
- **Rédiger une fiche d'animation** (voir le modèle de script) : éléments, état de départ, mouvements, durées, easing, son associé. Indispensable si l'animation est réalisée en code ou par un agent IA, utile dans tous les cas.
- **Choisir l'outil selon la complexité et le pipeline** :
  - *Simple, sans code* : Canva.
  - *Complexe, à la main, avec un rendu très fin* : After Effects (ou équivalent).
  - *Basée sur des données, répétée, à modifier souvent, ou générée par un agent IA* : Remotion (React) ou HyperFrames (HTML).
- **Briques de base**, quel que soit l'outil : formes, textes, tracés ; texte qui s'écrit (machine à écrire) ; tracé qui se dessine progressivement ; lueur (glow) pour faire ressortir.
- Méthode : esquisser, spécifier, créer, animer, caler sur la voix off. Si l'animation sera zoomée au montage, l'exporter en haute résolution.

## 10. Deuxième passe et gestion de l'espace
- Le premier montage brut n'est jamais parfait : le revoir en entier.
- **Ajouter** : animations, captures, mèmes ; réécrire des passages si une meilleure idée apparaît.
- **Couper** : lignes ennuyeuses, images inutiles, mauvaises blagues.
- **L'espace** : couper chaque milliseconde vide peut détruire l'histoire. Le public n'a pas une attention plus courte, il a des exigences plus hautes. Une pause est permise si ce qui suit la vaut.

## 11. Zooms et point d'attention
- Règle générale : un effet doit compléter ce qui est dit.
- Zoom = animation d'échelle et de position entre deux instants, **avec une courbe lissée** (ease) ; un mouvement linéaire paraît saccadé.
- Niveau supérieur : **garder le point d'attention au même endroit d'une coupe à l'autre**. Repères : point central, ligne des yeux, et surtout **règle des tiers**. Le sujet de chaque zoom et de chaque plan reste au même endroit de l'écran.

## 12. Texte à l'écran
Trois usages :
1. **Sous-titre** – seulement quand on dit quelque chose d'important.
2. **Texte central** – quand un sous-titre ne suffit pas : couleur propre, lueur, tout ce qui le fait ressortir.
3. **Texte intégré à la scène** – attaché à un écran, un mur, un élément du décor.

Animation « pop » de référence (à 60 i/s) :
- échelle 70 % au départ ;
- 110 % environ 7 images plus tard (≈ 0,12 s) ;
- 100 % environ 5 images après (≈ 0,08 s) ;
- lissage léger ; lueur, glitch ou autre selon le style.

Rendre l'animation réutilisable : preset, composant ou fonction selon l'outil.

## 13. Personnage / mascotte (facultatif)
- Générer une tête ou un logo avec un générateur d'images IA, la poser sur une image de stock, intégrer à la vidéo.
- Animer avec des mouvements lissés ; rendre réutilisable.

## 14. Overlays, transitions, effets
- **Overlays** : vidéos sur fond noir (électricité, poussière, light leaks, textures). Mode de fusion **Écran** (screen) pour rendre le noir transparent. Usages : surligner, faire une transition, habiller.
- **Transitions** : light leaks principalement ; glissements, secousses, zooms, rotations.
- **Effets favoris** (avec parcimonie) : lueur, 3D, transformation, flou, mosaïque.
- Pouvoir utiliser un effet ne veut pas dire devoir l'utiliser.

## 15. Sound design
- Sans bruitages, même un beau montage paraît plat : le son représente la moitié de la vidéo.
- Trois bases : **whoosh** (mouvements, transitions), **riser** (montée de tension), **impact** (moment fort). Puis tout ce qui colle au sujet : clavier, engrenages, mèmes, clics, explosion, horloge…
- Méthode : **couper la voix off et la musique**, regarder la vidéo et placer les bruitages. Oser combiner plusieurs sons. Enfin, **baisser le volume** des bruitages pour qu'ils ne deviennent pas agaçants.

## 16. Étalonnage
- Plan par plan : exposition, contraste, saturation.

## 17. Progresser et publier
- Une seule technique nouvelle par vidéo, pratiquée jusqu'à l'aisance, puis la suivante (feuille de route dans `ressources.md`).
- Les chaînes qui stagnent sont celles où chaque vidéo copie les dix précédentes.
- Investir 3 h pour 5 secondes de vidéo est rentable : la fois suivante ça prend 1 h, puis quelques minutes.
- **Perfectionnisme** : un travail créatif n'est jamais « fini ». Décider que c'est suffisant et publier.
- Pas de technique secrète : continuer d'apprendre, mélanger les styles, s'inspirer, casser les règles, et mettre de soi dans ses montages.


---
## Fichier : coach-montage-video/references/ressources.md

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


---
## Fichier : coach-montage-video/references/voyage-du-heros.md

# Le voyage du héros appliqué aux vidéos YouTube

L'auteur de la méthode construit l'histoire de toutes ses vidéos sur le voyage du héros. Selon lui, c'est un récit solide qui distingue une bonne vidéo d'une vidéo inoubliable. Le contenu principal (le tutoriel, l'explication, l'analyse) se loge dans l'étape « épreuves » ; les autres étapes forment l'histoire secondaire qui l'enveloppe.

## Les 12 étapes et leur application au tutoriel de montage

| # | Étape | Rôle | Dans le tutoriel de référence |
|---|---|---|---|
| 1 | Statu quo | Situation de départ | Le créateur a une chaîne qui marche |
| 2 | Appel à l'aventure | Un défi apparaît, souvent avec un doute | On lui réclame un tuto ; il ne se sent pas légitime |
| 3 | Aide | Un mentor intervient | Un ami entre en scène comme mentor |
| 4 | Départ | Le héros s'engage | Il commence à planifier le tutoriel |
| 5 | Épreuves | Le cœur du contenu | Tout le contenu pédagogique |
| 6 | Approche | Les difficultés montent, le héros refuse de les voir | Il bloque mais ne l'accepte pas |
| 7 | Crise | Le point le plus bas | Les mois passent, il n'arrive pas à finir |
| 8 | Trésor | La révélation ou le gain | Le mentor lui dit « c'est suffisant » |
| 9 | Résultat | La conséquence immédiate | Il termine… presque |
| 10 | Retour | Le héros revient transformé | Il publie |
| 11 | Nouvelle vie | La leçon intégrée | Il a appris sa leçon (perfectionnisme) |
| 12 | Résolution | Retour à un nouveau statu quo | Le public apprécie ; il repart sur le prochain tuto avec ce qu'il a appris |

## Comment l'utiliser en critique

1. Pour chaque étape, cherche le passage du script qui la remplit. Marque-la « présente », « faible » ou « absente ».
2. Les étapes **indispensables** pour qu'il y ait une histoire : appel à l'aventure, épreuves, crise, retour. Sans crise, pas de tension ; sans retour, pas de résolution.
3. Les étapes peuvent être très courtes (une phrase, un plan, un gag) : l'histoire secondaire ne doit pas voler la place du contenu.
4. Le héros n'est pas forcément le créateur : ce peut être le spectateur, une entreprise, un jeu, un personnage animé, une mascotte.
5. Vérifie que la leçon de l'histoire secondaire fait écho au contenu principal. Dans la référence, le tutoriel parle de progresser et l'histoire parle de lâcher le perfectionnisme : les deux se répondent.

## Comment l'utiliser pour construire un script

1. Écrire d'abord le contenu principal (les « épreuves »).
2. Se demander : quel problème profond vit le héros autour de ce contenu ? Le doute, l'échec, l'obsession, la peur…
3. Remplir les 12 étapes en une ligne chacune, puis ne garder que ce qui sert.
4. Placer chaque étape dans le script et lui donner un traitement visuel distinctif (scènes en dialogue, personnage, ambiance musicale différente) pour que le spectateur sente le récit sans qu'on le lui explique.

