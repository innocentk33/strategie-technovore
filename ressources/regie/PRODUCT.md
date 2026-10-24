# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Node sans dépendance (`regie.mjs`, modules `node:*`) et une page HTML ; choix de l'auteur du 24/10/2026. Rendu Markdown dans la page (marked + DOMPurify, versions figées sur jsDelivr).

## Users

L'auteur de Technovore, seul, sur son Mac. Il passe ses soirées entre le terminal (Claude Code), YouTube Studio et ses documents : il relit des scripts de 30 000 signes, des fiches, la stratégie, et suit une vidéo par lundi.

## Product Purpose

La régie : lire confortablement les fichiers Markdown du dépôt, et piloter la production des vidéos sans ouvrir un éditeur. Réussi quand il sait en un coup d'œil où en est chaque vidéo et ce qu'il reste à faire, et qu'il change un statut ou coche une étape en un clic.

## Operating Context

- Le dépôt est la source de vérité : `README.md` (tableau de suivi, statuts Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié), `calendrier.md` (grille du lundi 18 h, colonne Pilier), un dossier `projets/<nom>/` par vidéo.
- Claude modifie les fichiers en continu : la page suit les changements en direct.
- Les écritures passent par git : l'historique sert d'annulation.

## Capabilities and Constraints

- Lecture de tous les `.md` (hors `.git`, `node_modules`, `claude-youtube/`), liens relatifs et images suivis.
- Changement de statut : réécrit la ligne du projet dans `README.md` et dans la grille de `calendrier.md`, avec la date du jour. La ligne « Mis à jour le … » du calendrier reste à la main.
- Cases à cocher : réécrit le `- [ ]` correspondant du fichier ; refuse si le fichier a changé entre-temps.
- N'écoute que localhost ; refuse les requêtes d'une autre origine.
- Pas d'outils lancés depuis la page (rendre.sh, psd.py, sm7b.sh) : écarté le 24/10.

## Brand Commitments

Technovore : charte noir premium (fond noir, `#1c1c1e`, encre `#f5f5f7`, gris `#8e8e93`, rouge `#ff453a`), menthe `#07c095` et ardoise `#34495e` ; polices locales de `ressources/miniatures/fonts/` (Archivo Black, Inter, JetBrains Mono), jamais SF Pro. Tout en français, tutoiement.

## Product Principles

1. Le fichier reste la vérité : la page ne garde aucun état à elle.
2. Une écriture touche une ligne, jamais plus, et s'arrête si le fichier a bougé.
3. Lire d'abord : le confort de lecture passe avant le tableau de bord.
