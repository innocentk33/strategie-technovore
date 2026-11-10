---
name: upload
description: Kit d'upload d'une vidéo Technovore (projets/<nom>/upload.md) : mots-clés vidIQ, chapitres, description, sous-titres .fr.srt / .en.srt, puis la section « Suggestions » (vidéos hôtes françaises du mois, planche de miniatures, comparaison à 168 px, écran de fin). À utiliser dès qu'on prépare la publication d'une vidéo ou qu'on écrit ou relit un upload.md.
---

# Kit d'upload (`projets/<nom>/upload.md`)

Le kit contient les mots-clés vidIQ, les chapitres et la description ; `*.fr.srt` / `*.en.srt` pour les sous-titres.

Une fois le kit écrit, ajoute-lui une section « Suggestions » (le pourquoi est dans `etudes/suggestions-2026-10-23.md`) :

- **les vidéos hôtes** : 4 ou 5 grosses vidéos françaises du même sujet, sorties ce mois-ci (`vidiq_outliers` en `language: fr`, ou `vidiq_youtube_search`) ; note leurs titres et les mots qu'on peut partager dans le nôtre, sans copier leur angle ni leur miniature ;
- **la planche** : leurs miniatures dans `projets/<nom>/miniature/hotes/` (`curl -o <id>.jpg https://i.ytimg.com/vi/<id>/maxresdefault.jpg`), puis `python3 -I ressources/miniatures/planches.py --suggestions <notre miniature> projets/<nom>/miniature/hotes` ;
- **la comparaison** : à 168 px, la nôtre se repère-t-elle, et promet-elle autre chose que les leurs ? Sinon, retouche avant de publier ;
- **l'enchaînement** : l'écran de fin pointe la vidéo suivante de la playlist du pilier, et une fiche tombe pendant le plateau de rétention.
