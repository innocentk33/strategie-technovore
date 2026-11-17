# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Node sans dépendance serveur (`regie.mjs`, modules `node:*`) et une page HTML ; choix de l'auteur du 24/10/2026. Rendu Markdown dans la page (Marked 15.0.12 et DOMPurify 3.2.6, versions figées embarquées dans `vendor/`, empreintes SHA384 vérifiées).

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

Technovore : refonte validée le 16/11/2026, inspirée de YouTube Studio, avec modes clair, sombre et système. Conserver les polices locales de `ressources/miniatures/fonts/` (Inter principale, Archivo Black, JetBrains Mono), jamais SF Pro. Tout en français, tutoiement. La charte des miniatures reste indépendante de celle de l'interface.

## Refonte validée le 16 novembre 2026

- Production en Kanban et liste ; une vue Publiées donne accès aux vidéos terminées. « Terminée » signifie exclusivement publiée, pas programmée.
- Déplacement Kanban par poignée à la souris, avec choix explicite Fiche/Brouillon/Recherche dans Préparation ; le menu Statut reste disponible au clavier et sur écran tactile. Écritures versionnées et conflits signalés.
- Choix global des miniatures locales : Auto, une lettre disponible ou Variées avec mélange mémorisé. Une variante absente utilise le repli Auto et le signale. Préférence locale au navigateur, sans modification sur YouTube.
- Vrai calendrier mensuel, vue semaine et agenda mobile, dates et heures Europe/Paris ; ouverture du projet depuis une publication.
- Conserver le lecteur de documents, la mise à jour en direct et les fichiers Markdown comme source de vérité métier. Les préférences visuelles peuvent être mémorisées localement.
- Intégration YouTube publique en lecture seule, facultative : métadonnées et compteurs horodatés. La régie reste utilisable sans clé ni réseau ; les données absentes ne valent pas zéro. Analytics/OAuth et Reporting sont des extensions ultérieures.

## Product Principles

1. Le fichier reste la vérité : la page ne garde aucun état à elle.
2. Une écriture touche une ligne, jamais plus, et s'arrête si le fichier a bougé.
3. Lire d'abord : le confort de lecture passe avant le tableau de bord.
