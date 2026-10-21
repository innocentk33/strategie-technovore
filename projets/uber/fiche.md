# Le génie caché derrière la carte en temps réel d'Uber

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 2. Planning : [`calendrier.md`](../../calendrier.md).

**Origine** : un pote m'a dit qu'Uber, c'étaient des génies : il avait lu leur blog. J'ai vérifié, et j'ai vu tout ce qu'ils ont accompli. Inspiration : [Philipp Lackner, The Genius System Behind the Uber App's Real-Time Map](https://www.youtube.com/watch?v=gHIs0Mdow8M).

| Champ | Détail |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) |
| **Format** | Longue, 10-12 min |
| **Trafic visé** | Accueil + suggestions |
| **Mot-clé** | comment fonctionne uber |
| **Type de hook** | Curiosité |
| **Production estimée** | ~35 h (la bibliothèque Remotion est à créer, voir [`ressources/`](../../ressources/)) |

**Titres** :
1. Recherche : *Comment fonctionne la carte en temps réel d'Uber ?*
2. Curiosité : *Uber a dû découper la planète en hexagones*
3. Mixte (recommandé) : *Le génie caché derrière la carte en temps réel d'Uber*

**Miniature** : 3 propositions à tester (A « 570 000 milliards d'hexagones. », B « elle existe ? » recommandée, C « zéro lag. ») dans [`miniature/propositions.md`](miniature/propositions.md). L'idée « COMMENT ?! » est abandonnée.
**Contenu** : comment Uber affiche en direct des voitures qui bougent sans faire ramer ton téléphone : positions GPS, grille hexagonale H3, mises à jour en continu, animation entre deux positions. Ce que le spectateur retient : le travail invisible derrière un geste banal.

## Shorts

1. 12 nov : « Uber a découpé la planète en hexagones. »
2. Réserve : « Pourquoi des hexagones et pas des carrés ? » (chaque voisin est à la même distance).
3. Réserve : « La voiture sur ta carte n'est pas exactement là où tu crois. »
