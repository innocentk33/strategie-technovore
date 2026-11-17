# Connexion publique YouTube

La régie fonctionne sans connexion YouTube. Elle lit désormais `YOUTUBE_API_KEY` dans `.env.local` à la racine du dépôt au démarrage. Ce fichier privé est exclu de Git et ne peut pas être servi par la régie. Il est en texte brut sur ton Mac : l'exclusion Git n'est pas un chiffrement. Une variable `YOUTUBE_API_KEY` déjà définie dans l'environnement du processus reste prioritaire, même vide. Aucun autre fichier `.env` n'est chargé et les autres variables de `.env.local` sont ignorées. Node 22 ou plus récent est requis (le Mac utilise Node 24).

## Créer et enregistrer la clé

1. Dans [Google Cloud Console](https://console.cloud.google.com/), crée ou sélectionne un projet, par exemple « Régie Technovore ».
2. Dans **API et services → Bibliothèque**, cherche **YouTube Data API v3** et active-la.
3. Dans **API et services → Identifiants**, crée une **clé API standard**, nommée « Régie locale ». Ne choisis pas un client OAuth ni une clé liée à un compte de service.
4. Dans les restrictions d'API, autorise uniquement **YouTube Data API v3**, puis enregistre. Les appels viennent du serveur Node : une restriction « Sites Web » basée sur localhost ne convient pas. Une restriction par IP utilise ton IP publique sortante, jamais 127.0.0.1 ; elle demande une mise à jour si cette IP change.
5. Copie la clé directement dans le fichier `.env.local` déjà préparé, après `YOUTUBE_API_KEY=`. Ne la colle pas dans le chat. Le modèle `.env.local.example` peut être suivi dans Git ; la vraie clé reste uniquement dans `.env.local`.
6. Redémarre la régie avec `node ressources/regie/regie.mjs`, puis ouvre **Publiées → Actualiser**. Les statistiques apparaîtront pour les vidéos associées.

Forme du fichier local (remplace uniquement la valeur d'exemple) :

```dotenv
YOUTUBE_API_KEY=ta_cle_reelle
```

Sur ce Mac, le fichier a été créé avec les permissions `600` (lecture/écriture pour ton compte). Il reste sauvegardé entre les redémarrages ; tu n'as pas à ressaisir la clé. Garde éventuellement une copie dans ton gestionnaire de mots de passe. Pour changer de clé, modifie ce fichier et redémarre le serveur.

Ne colle jamais la clé dans l'interface, dans une URL de la régie ni dans Git. Le serveur n'envoie au navigateur que les données publiques. Cette V1 ne demande aucun OAuth et ne modifie rien sur YouTube.

L'association est explicite : pour une vidéo au statut **Publié**, le début de la cellule Statut du README doit contenir le lien de publication, par exemple `**Publié** : [Voir sur YouTube](https://www.youtube.com/watch?v=abcdefghijk)`. Les identifiants sont validés. Aucun parcours des scripts, des sources ou des liens d'inspiration n'est effectué. Une vidéo publiée sans lien reste visible localement avec ses statistiques indisponibles.

Pour associer une vidéo sans changer les notes du README, tu peux créer à la racine du dépôt un fichier local caché `.regie-youtube.json` contenant un objet JSON dont les clés sont les noms exacts des dossiers projet et les valeurs les identifiants YouTube de 11 caractères. Par exemple, la forme attendue est `{"nom-du-projet":"abcdefghijk"}` : remplace cet exemple par l'identifiant réel de ta propre publication. Ces associations explicites sont prioritaires sur les liens du README. Les noms ou identifiants invalides sont ignorés ; un JSON mal formé est ignoré entièrement. Aucun identifiant n'est recherché automatiquement. Ce fichier est relu à chaque lecture des projets ; actualise l'interface après modification. Il ne contient aucun secret. Garde-le hors de Git si tu souhaites conserver ces associations locales.

`GET /api/youtube` renvoie `{configured, fetchedAt, videos, error?}`. `videos` est indexé par identifiant YouTube ; chaque entrée contient `title`, `thumbnail`, `duration` (ISO 8601), `publishedAt`, `views`, `likes`, `comments`. Une valeur absente vaut `null`, un compteur réel nul vaut `0`. Une vidéo non renvoyée par YouTube est absente du dictionnaire. `POST /api/youtube/refresh` avec le corps JSON `{}` force une nouvelle lecture. Sans clé, ces deux routes répondent explicitement sans accès réseau.

Les lectures sont groupées par lots de 50 et limitées à 8 secondes par appel. Le cache est en mémoire pendant 24 heures ; il disparaît au redémarrage et ne crée aucun fichier dans le dépôt. Une erreur conserve les dernières données avec leur horodatage et ajoute `error`. Les erreurs sont mises en cache 60 secondes pour éviter les nouvelles tentatives répétées ; Actualiser permet de réessayer immédiatement. Les dernières données sont retirées après 30 jours sans lecture réussie. Le bouton Actualiser consomme du quota à chaque actualisation effective. La limite du projet se consulte dans Google Cloud.

La miniature locale provient en priorité des images de `projets/<nom>/miniature/rendus/` (ou `miniatures/rendus/`), puis d'un fichier explicite `miniature.png`, `miniature.jpg`, `miniature.jpeg` ou `miniature.webp` à la racine du projet. Le tri par nom rend le choix stable. Les références, sources, aperçus, planches et autres éléments de préparation sont exclus ; sans rendu admissible, aucune miniature locale n'est proposée. Ce repli local reste une proposition de travail : il ne prouve pas quelle variante est actuellement publiée sur YouTube.

Les dates locales restent celles des sources, au fuseau Europe/Paris. L'année de départ est l'année explicite du titre du calendrier, puis les passages décembre–janvier avancent d'une année. Pour un nouveau calendrier, garde cette année explicite. Les dates YouTube `publishedAt` restent distinctes et ne changent aucun statut ni aucune planification locale.

Les écritures de statut exigent la `version` obtenue sur les projets : hash du README et du calendrier. Une version absente ou périmée donne HTTP 409 avant toute écriture. Les deux contenus sont préparés avant remplacement et une erreur de remplacement restaure le contenu précédent. Le serveur traite cette opération sans attente asynchrone ; une panne du processus ou un autre outil écrivant exactement entre les remplacements n'offre toutefois pas la garantie transactionnelle d'une base de données. L'historique Git reste le moyen de relire et annuler les changements.

Vérification sans toucher aux projets réels :

```sh
node ressources/regie/verif.mjs
node --test ressources/regie/youtube.test.mjs
```

Références : [clé API](https://developers.google.com/youtube/v3/getting-started), [videos.list](https://developers.google.com/youtube/v3/docs/videos/list), [quota](https://developers.google.com/youtube/v3/determine_quota_cost).
