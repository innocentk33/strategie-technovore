# SQLite : la base de données qui est partout, et qui n'a pas de serveur

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 18. Planning : [`calendrier.md`](../../calendrier.md). **Publication provisoire : lun. 22 mars 2027 à 18 h**, à confirmer au radar du 8/03.
> Faits et sources : [`sources.md`](sources.md) (phase 1 du 23/10/2026, à re-vérifier). Le titre de ByteMonk (« The 300KB File That Beat Oracle and Postgres ») n'est pas repris : la taille est fausse (590 à 750 Ko, fait 5) et « battu Oracle » n'est pas dans les sources (fait 30).

| Champ | Détail |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) |
| **Format** | Longue, 8-10 min |
| **Trafic visé** | Suggestions + accueil (à côté de la vidéo ByteMonk et de la vague « bases de données » d'octobre 2026) |
| **Mot-clé** | sqlite / sqlite database (13 389 et 8 990 recherches par mois dans le monde, vidIQ 23/10/2026) ; « comment fonctionne sqlite » : <750 |
| **Type de hook** | Choc (chiffre) |
| **Production estimée** | ~20 h (estimation : peu d'animations, le fichier découpé en pages, l'arbre, le journal WAL) |

**Titres** :
1. Recherche : *Comment fonctionne SQLite ?*
2. Curiosité : *Le logiciel qui est sur ton téléphone, dans ton navigateur et dans un Airbus*
3. Mixte (recommandé) : *SQLite : la base de données qui est partout, et qui n'a pas de serveur*

**Titre choisi le 23/10** : *Sans cette base de données, ton téléphone ne marche pas* (variante B : *SQLite : la base de données cachée dans ton téléphone*). Il est tenu par le fait 41 de `sources.md` (contacts, SMS et appels dans des bases SQLite sur Android).

**Miniature** : à faire.

**Les 15 premières secondes** (règle du 22/10, `strategie.md`, section 5) : le meilleur moment d'abord, sans contexte. Candidat : le chiffre. Sur ton téléphone, il y a probablement des centaines de petits fichiers SQLite, et sqlite.org estime qu'il y en a plus de mille milliards en service (fait 1). Montre-le tout de suite sur l'écran d'un téléphone qui se remplit de fichiers, puis pose la question : pourquoi un logiciel sans serveur s'est-il retrouvé partout ? Ni « dans cette vidéo », ni présentation. Reste prudent : « probablement » est dans la source.

**Texte et sous-texte** (le « problème de surface / problème profond » du skill grill) :
- **Texte** : SQLite est une base de données qui tient dans une bibliothèque et un fichier, sans serveur, et elle est probablement plus déployée que tous les autres moteurs réunis (faits 2, 3, 26).
- **Sous-texte** : le plus utilisé n'est pas le plus grand ni le plus impressionnant, c'est celui qui a supprimé le problème (le serveur qui tombe) et qui tient une promesse de fiabilité à chaque version : tester sans relâche et s'engager sur la durée (faits 7, 19). [À valider avec l'auteur : le sous-texte, qui reste à lui.]

**Contenu** (ordre proposé, à valider) :
1. Le chiffre et ton téléphone : où SQLite se cache (Android, iPhone, navigateurs ; WhatsApp avec la nuance du fait 22).
2. L'origine : Hipp, un destroyer, un serveur Informix qui tombe, un moteur sans serveur (faits 12, 14).
3. Serveur contre bibliothèque : ce que ça change, expliqué sans copier l'analogie de ByteMonk.
4. Dedans : un fichier découpé en pages, un arbre pour retrouver une ligne, un journal (WAL) pour ne pas perdre de données si le courant saute (faits 24, 25).
5. Pourquoi on lui fait confiance : 92 millions de lignes de tests pour 156 000 lignes de code, 100 % MC/DC, le logiciel de vol de l'A350, sans prétendre à la certification (faits 6, 7, 10, 11).
6. Domaine public, Bibliothèque du Congrès, soutien annoncé jusqu'en 2050 (faits 16, 18, 19).
7. Ce que ça change pour toi : quand utiliser SQLite pour un projet, quand prendre un vrai serveur. Retourner à l'image du début.
8. Écran de fin : la vidéo suivante de la playlist « génie ».

**À vérifier** (détail dans `sources.md`) :
- la taille de la bibliothèque : 590 à 750 Ko selon la plateforme, moins de 900 KiB avec toutes les options (fait 5) ;
- « mille milliards » est une estimation de sqlite.org, pas un comptage (fait 1) ;
- « certifié DO-178B » : faux en l'état, les sources parlent d'un test suivant ce standard (fait 10) ;
- « deux ingénieurs » et les chiffres sur MySQL et PostgreSQL de ByteMonk : sans source, à ne pas dire (faits 28, 29) ;
- « battu Oracle » : à reformuler en « plus déployé que tous les autres réunis » (fait 30) ;
- les chiffres de tests datent de la version 3.42.0 (2023) : relever la version actuelle ;
- aucune anecdote personnelle de l'auteur : [à demander à l'auteur] s'il en a une sur SQLite.

## Corrections de la 2e vérification (23/10)

Le titre recommandé de la fiche tient. Ce qui change (détail dans [`sources.md`](sources.md)) :
- **Le titre de `strategie.md`, idée 18** (« le fichier de 300 Ko qui a battu Oracle ») tombe en entier : la bibliothèque fait 590 à 750 Ko (mesures de 2023, fait 5), et en popularité Oracle est 1er et SQLite 11e chez DB-Engines en octobre 2026 (fait 30). Garde les titres de cette fiche, ou :
  - *SQLite : le fichier de moins d'1 Mo qui est dans ton téléphone*
  - *Le logiciel le plus installé du monde n'a pas de serveur*
- **« Battu Oracle »** n'est pas seulement à reformuler : c'est faux en popularité. Dis « probablement plus installé que tous les autres réunis » (fait 2).
- **À vérifier, mis à jour** : les « 60 h par semaine » sont sourcées (Hipp sur CoRecursive, fait 27) ; la version actuelle est la 3.54.1 du 16/10/2026, mais les chiffres de tests restent ceux de 2023 : dis « en 2023 » (faits 6, 31) ; « deux ingénieurs » devient « une petite équipe à plein temps » (fait 29).
