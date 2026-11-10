# Comment un site sait en une milliseconde que ton pseudo est déjà pris

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 4. Planning : [`calendrier.md`](../../calendrier.md), S5-S6. **Publication : lun. 30 nov. à 18 h** (reculée du 23 nov. le 24/10, quand Coût Claude est passé avant le Black Friday). C'est aussi le **joker** du calendrier : si une semaine déraille, il sort à la place de la vidéo en retard.

| Champ | Détail |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) |
| **Format** | Longue, 8-10 min |
| **Trafic visé** | Accueil + recherche |
| **Mot-clé** | pseudo déjà pris / comment ça marche |
| **Type de hook** | Curiosité |
| **Production estimée** | ~15-20 h (une seule astuce, des animations simples ; estimation) |

**Titres** :
1. Recherche : *Comment un site vérifie si ton pseudo est déjà pris ?*
2. Curiosité : *Ton pseudo est déjà pris. Le site a triché.*
3. Mixte (recommandé) : *Comment un site sait en une milliseconde que ton pseudo est déjà pris*

**Miniature** (21/10, charte noire) : [`noir-07.png`](../../ressources/miniatures/rendus/noir-07.png). Formulaire, « technovore » en erreur, « Ce nom est déjà pris. », « il triche. ». Retire le « G » de Google si aucune source ne confirme que Google utilise cette technique.
**Contenu** : le filtre de Bloom, la technique classique. Un tri rapide répond « sûrement pas pris » ou « peut-être pris », et seule la base de données tranche le « peut-être ». On le montre avec des cases qui s'allument.

**À vérifier** : un exemple **sourcé** d'un grand site qui utilise un filtre de Bloom (blog d'ingénierie, conférence). Sans source, on parle de « la technique classique », sans nommer Google (`strategie.md`, idée 4).

## Corrections de la 2e vérification (23/10)

- **Titre 3 (« en une milliseconde »)** : aucune source ni mesure. Soit tu mesures toi-même (outils réseau du navigateur sur un vrai formulaire d'inscription), soit tu écris *Comment un site sait instantanément que ton pseudo est déjà pris*. Même chose pour le chronomètre « 0,001 s » de l'idée 4. **Gardé le 23/10 (ton choix)** : tenu côté serveur par la doc de Redis (fait 33), et le hook le dit comme ça. Le chronomètre de la miniature dit « < 1 ms », pas « 0,001 s » (sans mesure).
- **Hook (« Il a triché »)** et titre 2 (« Le site a triché ») : aucun grand site ne dit vérifier les pseudos avec un filtre de Bloom (recherche refaite le 23/10). Présente-le comme la technique qu'on enseigne et dis qu'on ne sait pas quel site l'emploie. « Le site ne les a pas tous vérifiés » reste vrai : un simple index trouve le pseudo en quelques lectures.
- **Miniature** : retire le « G » de Google (Google utilise le filtre dans Bigtable, pas pour les pseudos).
- **Chrome** : il n'a pas « abandonné » le filtre en 2011 ; il a commencé à le remplacer en 2011. Voir `sources.md`, fait 10 et lignes 22 à 25.
