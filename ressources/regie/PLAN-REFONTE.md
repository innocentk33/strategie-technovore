# Plan de refonte de la régie

16 novembre 2026 — plan validé et réalisé. La connexion réelle à YouTube attend une clé API ; OAuth et Reporting restent des extensions ultérieures.

## Brief confirmé

- Application locale Technovore, destinée à piloter les vidéos et lire les documents du dépôt.
- Référence demandée : YouTube Studio. Modes clair et sombre.
- « Terminées » signifie exclusivement « Publiées » ; Programmé reste distinct.
- Ajouter un Kanban et rendre les vidéos publiées immédiatement accessibles.
- La vue Calendrier doit être un véritable calendrier visuel pour se repérer dans les dates.
- Conserver les fichiers Markdown comme source de vérité et le serveur Node existant.

## Direction proposée

Interface de travail sobre inspirée de YouTube Studio : navigation latérale resserrée, titres lisibles, vraies miniatures, tableaux compacts et accents rouges mesurés. Inter reste la police principale. Le vert indique la réussite ; le rouge de marque ne doit pas servir seul à signaler une erreur.

Clair : fond gris très clair, surfaces blanches, texte anthracite. Sombre : fond presque noir, surfaces gris charbon, texte blanc cassé. Tokens sémantiques distincts pour texte, surfaces, bordures, focus, actions et états. Choix clair/sombre/système mémorisé, sans flash au chargement.

Navigation : Production · Publiées · Calendrier · Documents. Production offre Kanban et liste. Les colonnes regroupent les premières étapes lorsque cela facilite la lecture, avec le statut exact sur chaque carte. Les statuts vides restent accessibles mais compacts. Publiées propose miniatures, titre, date, durée, vues, likes, commentaires et liens vers la vidéo et le dossier local.

Le lecteur conserve sommaire, repères, liens et cases interactives. Sur petit écran, listes et sélection d'étape remplacent le tableau trop large. Le glisser-déposer éventuel conserve une alternative clavier par menu.

### Calendrier de publication

Vue mensuelle par défaut, en grille lundi–dimanche, avec navigation mois précédent/suivant, choix du mois et bouton Aujourd'hui. Le jour courant est clairement repéré. Une vue semaine permet de lire les périodes chargées ; sur mobile, un agenda chronologique reste disponible.

Chaque vidéo affiche sa miniature si disponible, son titre, son heure et son statut textuel. Les publications passées et les sorties prévues sont distinguées sans dépendre uniquement de la couleur. Un clic ouvre le détail du projet et ses documents. Filtres par statut et pilier ; les journées chargées offrent un accès à tous leurs éléments. Les projets sans date restent accessibles dans une section À planifier.

Le calendrier reprend les dates locales existantes, avec année explicite et fuseau Europe/Paris, et se synchronise avec les autres vues. Les dates prévues et les dates réelles fournies par YouTube sont identifiées séparément si elles divergent. La première version sert au repérage : une reprogrammation interactive éventuelle devra modifier les sources locales de façon cohérente et ne sera jamais présentée comme une reprogrammation sur YouTube.

## Lots de réalisation

1. **Fondations et fiabilité** : protéger les changements de statut contre les modifications concurrentes ; préserver notes et cohérence README/calendrier ; ne jamais réordonner le Markdown pour déplacer une carte. Couvrir les conflits avec des tests sur dépôt temporaire.
2. **Design et thèmes** : appliquer les tokens aux contrôles, lecteur et messages ; construire navigation et modes clair/sombre/système. Documenter le système retenu après validation.
3. **Kanban et bibliothèque publiée** : filtres, recherche de vidéos, compteurs, cartes avec miniatures disponibles, actions de statut et états vides. Garder visibles les statuts inconnus sous « À classer ». Une checklist incomplète ne rétrograde pas une vidéo publiée.
4. **Calendrier visuel** : grille mensuelle, vue semaine et agenda mobile, navigation temporelle, repère Aujourd'hui, cartes de publication et accès aux projets. Vérifier changements de mois et d'année, journées chargées, dates absentes et heures Europe/Paris.
5. **YouTube public** : module serveur en lecture seule, association explicite projet/videoId, clé hors Git, récupération groupée, cache horodaté et bouton Actualiser. Afficher les données indisponibles comme telles, jamais comme zéro. Le statut local n'est pas écrasé automatiquement par YouTube.
6. **Qualité** : vérifications existantes, tests ciblés des nouvelles écritures et de l'adaptateur API, inspection visuelle desktop/mobile dans les deux thèmes, parcours clavier, réduction des animations, réseau indisponible, quota épuisé et actualisation externe sans perte de focus.
7. **Option ultérieure** : OAuth lecture seule pour Analytics ; Reporting API pour impressions/CTR. Ne pas coupler ces fonctions à la livraison du Kanban.

## Coordination GPT-6.1 Sol

Audit initial réalisé par deux agents : architecture/risques et faisabilité YouTube. Pour la réalisation : un agent interface, un agent serveur/YouTube, puis un agent de revue indépendante. Le coordinateur fixe les contrats de données, intègre les changements et vérifie le rendu. Les agents ne modifient pas simultanément le même fichier.

## API YouTube

La Data API expose les métadonnées et compteurs publics avec une clé API. Les données privées et Analytics requièrent OAuth. Le quota standard documenté pour les endpoints usuels est de 10 000 unités/jour ; videos.list coûte 1 unité par appel. Pour cette régie, commencer par une actualisation quotidienne et manuelle, puis ajuster aux vidéos récentes. Le quota réel du projet reste visible dans Google Cloud ; ne pas promettre un service illimité.

Sources officielles :

- https://developers.google.com/youtube/data/getting-started
- https://developers.google.com/youtube/data/determine_quota_cost
- https://developers.google.com/youtube/data/reference/rest/v3/videos/list
- https://developers.google.com/youtube/data/guides/authentication
- https://developers.google.com/youtube/analytics/channel_reports
- https://developers.google.com/youtube/reporting/v1/reports/channel_reports

## Critères de réception

- Les 7 vidéos actuellement publiées sont accessibles en un clic, séparément des 20 projets à venir.
- Changer de vue, filtre ou thème ne recharge pas toute la page et ne perd pas la sélection.
- Le calendrier permet de situer les sorties dans une vraie grille mensuelle, de revenir à aujourd'hui et d'ouvrir une vidéo en un clic ; toutes les vidéos restent accessibles même sans date ou sur une journée chargée.
- Les données locales restent utilisables sans clé API ni réseau.
- Chaque statistique indique sa fraîcheur ; aucune statistique fictive.
- Les écritures préservent les notes existantes et refusent les versions périmées.
- Les deux thèmes et les interactions sont vérifiés sur le rendu réel.

## Livraison et vérifications

Interface réalisée : Production Kanban/liste, Publiées, calendrier mois/semaine/agenda, créneaux Radar et Documents ; thèmes clair/sombre/système. API publique YouTube facultative, cache mémoire horodaté et association explicite des vidéos. Voir CONNEXION-YOUTUBE.md pour l'activation.

Tests de la régie réussis sur dépôt temporaire ; 6 tests YouTube réussis avec réponses simulées. Parcours visuels vérifiés sur ordinateur et mobile, dans les deux thèmes : filtres, recherche, calendrier, navigation et lecteur. Revue Impeccable : correction du focus de recherche évaluée comme résolue, verdict `ship`. Aucune statistique réelle récupérée, faute de clé API configurée.

Reste à configurer Google Cloud pour activer les statistiques réelles. Aucun secret à inclure dans le chat ou dans Git.
