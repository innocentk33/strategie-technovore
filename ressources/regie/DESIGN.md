---
name: "La régie · Technovore"
description: "Régie vidéo locale inspirée de YouTube Studio, en clair et sombre."
colors:
  clair-fond: "#f7f7f7"
  clair-panneau: "#fff"
  clair-releve: "#f1f1f1"
  clair-releve-2: "#e9e9e9"
  clair-trait: "#e1e1e1"
  clair-trait-fort: "#c5c5c5"
  clair-encre: "#202020"
  clair-encre-2: "#484848"
  clair-encre-3: "#666"
  clair-menthe: "#087f60"
  clair-menthe-doux: "#e5f3ed"
  clair-rouge: "#c5221f"
  clair-ambre: "#956000"
  clair-accent: "#c5221f"
  clair-accent-doux: "#fcebea"
  sombre-fond: "#181818"
  sombre-panneau: "#212121"
  sombre-releve: "#2b2b2b"
  sombre-releve-2: "#363636"
  sombre-trait: "#393939"
  sombre-trait-fort: "#606060"
  sombre-encre: "#f5f5f5"
  sombre-encre-2: "#d0d0d0"
  sombre-encre-3: "#aaa"
  sombre-menthe: "#64d8b2"
  sombre-menthe-doux: "#203c33"
  sombre-rouge: "#ff8a80"
  sombre-ambre: "#e9b961"
  sombre-accent: "#ff8a80"
  sombre-accent-doux: "#442b2a"
  marque-rouge: "#d92323"
  blanc: "#fff"
  miniature-temps: "#111d"
typography:
  headline:
    fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    fontSize: "26px"
    fontWeight: 650
    lineHeight: 1.25
    letterSpacing: "-.025em"
  document-headline:
    fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    fontSize: "2rem"
    fontWeight: 750
    lineHeight: 1.15
    letterSpacing: "-.028em"
  title:
    fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.45
  body:
    fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    fontSize: "14px"
    lineHeight: 1.5
  reading:
    fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    fontSize: "16.5px"
    lineHeight: 1.7
  label:
    fontFamily: 'Inter, "Helvetica Neue", Arial, sans-serif'
    fontSize: "11px"
  technical:
    fontFamily: '"JetBrains Mono", Menlo, monospace'
    fontSize: "12.5px"
    fontWeight: 500
rounded:
  badge: "4px"
  segment: "5px"
  control: "6px"
  navigation: "7px"
  status: "8px"
  mobile-card: "9px"
  container: "10px"
  card: "12px"
spacing:
  compact: "4px"
  small: "8px"
  control-gap: "10px"
  card-gap: "12px"
  grid-gap: "16px"
  toolbar: "20px"
  section: "24px"
  page-inline: "36px"
components:
  button-action:
    backgroundColor: "{colors.clair-panneau}"
    textColor: "{colors.clair-encre}"
    rounded: "{rounded.control}"
    padding: "8px 10px"
  button-segment:
    textColor: "{colors.clair-encre-3}"
    rounded: "{rounded.segment}"
    padding: "7px 11px"
  input-search:
    backgroundColor: "{colors.clair-panneau}"
    rounded: "{rounded.control}"
    height: "36px"
    width: "280px"
    padding: "0 10px"
  navigation-current:
    backgroundColor: "{colors.clair-accent-doux}"
    textColor: "{colors.clair-accent}"
    rounded: "{rounded.navigation}"
    padding: "9px 13px"
  badge-published:
    backgroundColor: "{colors.clair-menthe-doux}"
    textColor: "{colors.clair-menthe}"
    rounded: "{rounded.badge}"
    padding: "3px 7px"
  card-video:
    backgroundColor: "{colors.clair-panneau}"
    rounded: "{rounded.card}"
  calendar-event:
    backgroundColor: "{colors.clair-releve}"
    rounded: "{rounded.segment}"
    padding: "7px"
---

# Design System: La régie · Technovore

## Overview

**Creative North Star: "La régie YouTube Studio"**

Une régie de travail inspirée de YouTube Studio : surfaces neutres, contrôles familiers et miniatures réelles. Le rouge signale la navigation active ; la menthe accompagne les liens, les publications et certains états de lecture. La densité permet de suivre plusieurs vidéos tout en gardant leurs titres lisibles.

Le clair et le sombre partagent la même géométrie. Le mode système choisit l’un de ces deux thèmes selon la préférence du système. La lecture des documents conserve une mesure généreuse et les polices locales de Technovore ; la charte des miniatures reste indépendante de l’interface.

**Key Characteristics:**

- Surfaces neutres et bordures fines.
- Miniatures 16:9 et statuts textuels.
- Navigation rouge mesurée, menthe fonctionnelle.
- Inter locale et lecture longue à 72ch.

## Colors

Les neutres blancs et gris deviennent charbon en sombre, avec des accents rouges et menthe accessibles sur leur surface respective. Les préfixes `clair-` et `sombre-` documentent les valeurs effectives de la cascade, après les anciennes déclarations du début de la feuille. Dans le code, `--fond`, `--encre`, etc. changent de valeur selon `data-theme` ; les composants du frontmatter montrent le clair, les snippets restent liés aux variables des deux thèmes.

### Primary

- **Rouge Studio** : `accent` et `accent-doux`, pour l’entrée active, le jour courant, la sélection de texte et le focus général. `rouge` partage la valeur d’accent et sert aux erreurs.
- **Rouge de marque** : `marque-rouge`, invariant pour le petit symbole vidéo.

### Secondary

- **Menthe fonctionnelle** : `menthe` et `menthe-doux`, pour « Publié », les liens du lecteur, les indicateurs de progression et le focus de recherche vidéo.
- **Ambre de repérage** : `ambre`, pour les passages marqués du lecteur.

### Neutral

- `fond` : toile principale ; `panneau` : navigation et cartes ; `releve` / `releve-2` : contrôles, survols et emplacements de miniatures.
- `trait` / `trait-fort` : séparateurs et limites interactives.
- `encre` / `encre-2` / `encre-3` : texte principal, secondaire et métadonnées.
- `blanc` et `miniature-temps` : triangle du symbole vidéo et cartouche de durée sur les miniatures.

**The Semantic Color Rule.** Le rouge de navigation suit --accent ; les publications et les liens suivent --menthe. Ne pas remplacer les états textuels par la couleur seule.

## Typography

**Body Font:** Inter, "Helvetica Neue", Arial, sans-serif ; Inter variable locale (100–900).
**Label/Mono Font:** "JetBrains Mono", Menlo, monospace ; fichiers locaux 500 et 700.

La hiérarchie de l’interface utilise Inter sans police d’affichage séparée. Archivo Black reste chargé et utilisé pour les grands jours dans l’en-tête de projet hérité ; ce rôle ponctuel ne définit pas les titres Studio.

### Hierarchy

- **Headline** : 26px / 1.25, 650, approche −.025em ; titre de vue, réduit à 24px à 820px.
- **Document headline** : 2rem / 1.15, 750, approche −.028em ; titre Markdown.
- **Calendar title** : 19px, 600, approche −.02em ; réduit à 17px à 820px.
- **Title** : 13px / 1.45, 600 ; titres de vidéos.
- **Body** : 14px / 1.5 ; interface. Le contexte de vue et la recherche sont à 13px ; boutons et tableaux à 12px ; métadonnées à 11px.
- **Reading** : 16.5px / 1.7 ; contenu Markdown, encre secondaire.
- **Technical** : 12.5px, 500 en mono pour chemins et onglets ; autres tailles ponctuelles de 10 à 12px pour compteurs et suivi. Les nombres tabulaires servent aux tables et dates.

**The Reading Measure Rule.** Les paragraphes du lecteur restent à 72ch maximum ; les tableaux et blocs de code peuvent utiliser la largeur disponible.

## Layout

La coque comporte une navigation de 232px et un contenu `minmax(0,1fr)`. La navigation reste à hauteur de fenêtre ; son arbre de fichiers défile séparément. Le Studio est limité à 1800px, centré, avec padding 34px 36px 80px. Les outils se replient avec gap 10px. Le Kanban utilise cinq colonnes `minmax(225px,1fr)` et gap 16px, avec défilement horizontal ; les cartes de chaque colonne défilent verticalement au-dessus de 820px.

À 1200px : padding 30px 24px 70px, colonnes de 235px, tables débordantes dans leur conteneur. À 820px : navigation en tiroir de 288px, Studio en 66px 20px 60px, documents en une colonne. À 600px : Kanban empilé, cartes horizontales avec miniature de 110px et corps à 11px de padding ; recherche pleine largeur, tableau transformé en lignes souples avec libellés, calendrier remplacé par agenda. Les cartes ordinaires ont 13px de padding et 12px d’écart vertical.

Le lecteur utilise un contenu et un sommaire de 224px, gap 56px, largeur maximale 1240px et padding 40px 48px 160px. Le sommaire disparaît à 1180px. Le calendrier est une grille lundi–dimanche de sept colonnes, jours de 118px minimum (350px en semaine), avec adaptation à 112px puis 100px aux seuils 1200px et 820px.

## Elevation & Depth

Les fonds, séparateurs de 1px et bordures créent la profondeur ordinaire. Les cartes ne sont pas soulevées au survol. Les ombres sont limitées aux couches et états existants.

### Shadow Vocabulary

- **Segment sélectionné** : `0 2px 4px #0001`.
- **Annonce** : `0 8px 24px #0002`.
- **Tiroir mobile** : `0 0 40px rgba(0, 0, 0, .6)`.
- Les traits `inset 0 2px var(--menthe)` des événements publiés et `inset 1px 0 var(--menthe)` du sommaire sont des repères, pas une élévation.

**The Flat Surface Rule.** Les cartes restent sans ombre au repos et au survol ; leur bordure change. Réserver les ombres aux états et couches déjà présents.

## Shapes

Bordures de 1px ; arrondis compacts, sans pilules généralisées : 4px pour badges, 5px pour segments et événements, 6px pour contrôles, 7px pour navigation, 8px pour sélecteurs de statut, 10px pour grands conteneurs et 12px pour cartes vidéo. Les cartes mobiles passent à 9px. La miniature occupe un cadre 16:9 avec `object-fit:cover`. Seul le jour courant utilise un disque de 26px ; les états vides ont un contour pointillé.

## Components

### Buttons

Les boutons d’action sont des contrôles sobres : panneau, trait fort, rayon 6px, padding 8px 10px, texte 12px, hauteur minimale 36px. Le survol passe à `releve`. Le bouton désactivé utilise opacity .6 et curseur d’attente. Les boutons de segment ont rayon 5px, padding 7px 11px, texte 12px ; la sélection reçoit panneau, poids 600 et petite ombre. Le conteneur segmenté a rayon 7px et padding 3px.

### Chips

Badges à 11px, padding 3px 7px, rayon 4px, fond relevé et encre secondaire. « Publié » utilise menthe sur menthe douce. Un badge n’est pas un bouton.

### Cards / Containers

Carte vidéo : panneau, trait fin, rayon 12px, débordement masqué, corps 13px. Le survol renforce la bordure. Miniature réelle ou état d’absence explicite ; titres à 13px / 1.45, soulignés au survol. Les cartes contiennent date, statut et suivi. Une carte vide utilise le contour pointillé sans inventer de miniature.

### Inputs / Fields

Recherche vidéo : panneau, trait fort, rayon 6px, hauteur 36px, largeur 280px, padding horizontal 10px, texte 13px ; champ interne sans bordure. `.recherche-videos:focus-within` porte une outline menthe de 2px, décalée de 3px. Les autres contrôles ont le focus général rouge de 2px, décalé de 2px. Les sélecteurs statut conservent leur flèche et rayon 8px ; ils mesurent 30px dans les cartes, 32px dans les tables.

### Navigation

Entrées à hauteur minimale 43px, padding 9px 13px, rayon 7px, texte 14px. Le survol utilise `releve` ; `aria-current` utilise accent sur accent doux. Les compteurs ont rayon 4px, texte 11px et fond relevé. Le tiroir mobile conserve ces états. Les onglets du lecteur sont en mono 12.5px avec soulignement menthe de 2px sur l’actif.

### Calendrier

Conteneur panneau, rayon 10px et trait fin. Événements relevés, rayon 5px, texte 11px / 1.35, padding 7px ; survol relevé-2. Une publication porte un trait menthe supérieur. Le mois compacte les événements et affiche des miniatures de 40×25px ; la semaine et l’agenda montrent davantage de contenu. Les liens ouvrent le projet. Les dates et heures sont présentées en Europe/Paris.

### Motion and feedback

Courbe existante `cubic-bezier(.16, 1, .3, 1)` : entrée .22s, tiroir .25s, annonce transform .25s et opacité .2s ; les bordures ont une transition .15s lorsqu’elle est définie. La préférence `prefers-reduced-motion: reduce` coupe animations et transitions.

## Do's and Don'ts

### Do:

- **Do** utiliser les propriétés CSS du thème actif et garder les mêmes dimensions en clair et sombre.
- **Do** conserver des titres et statuts textuels avec les miniatures réelles.
- **Do** préserver le focus visible et la préférence de réduction du mouvement.
- **Do** garder « Publié » distinct de « Programmé ».

### Don't:

- **Don't** appliquer la charte des miniatures à toutes les surfaces de l’interface.
- **Don't** remplacer Inter locale par SF Pro.
- **Don't** ajouter une ombre aux cartes vidéo ordinaires.
