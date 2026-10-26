# La carte d'Uber est une illusion (et c'est génial)

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
3. Mixte (recommandé jusqu'au 26/10) : *Le génie caché derrière la carte en temps réel d'Uber*
4. **Retenu le 26/10 (ton choix)** : *La carte d'Uber est une illusion (et c'est génial)* (vidIQ 88, contre 84 pour le 3). La vidéo tient « illusion » : le support d'Uber parle d'un « effet visuel » (8:13), la position est « en partie devinée » (9:00), et le verdict est « des génies » (9:35).

**Miniature** : 3 propositions à tester (A « 570 000 milliards d'hexagones. », B « elle existe ? » recommandée, C « zéro lag. ») dans [`miniature/propositions.md`](miniature/propositions.md). **Retenue le 21/10** (pilier « génie » = charte noire) : B refaite en Inter au lieu de SF Pro, dont la licence pose question, [`noir-01.png`](../../ressources/miniatures/rendus/noir-01.png), corrigée le 21/10 (voiture fantôme agrandie, vrai logo, halo qui détache la tuile du mode sombre ; détail dans [`upload.md`](upload.md)). **Le 26/10**, le test contre [`noir-01b.png`](../../ressources/miniatures/rendus/noir-01b.png) (« sa position est devinée. », même décor) est remplacé par un test à trois : `noir-01`, puis deux miniatures hors niche, [« HORS-JEU ? »](miniature/propositions/hors-niche-1.png) et [« 17 min »](miniature/propositions/hors-niche-2.png) (voir [`miniature/propositions.md`](miniature/propositions.md)). L'idée « COMMENT ?! » est abandonnée.
**Contenu** : comment Uber affiche en direct des voitures qui bougent sans faire ramer ton téléphone : positions GPS, grille hexagonale H3, mises à jour en continu, animation entre deux positions. Ce que le spectateur retient : le travail invisible derrière un geste banal.

**Publication** : lun. 26/10 à 18 h (avancée du 9/11 le 21/10). La vidéo (10:00) est en ligne en **privé** depuis le 21/10. Avant de la programmer :
- remplace le titre « L'hisoire du temps réel derriere uber » par le titre 3 ci-dessus (fait le 22/10), puis par le titre 4 le 26/10, avant 18 h ;
- remplace les tags (ce sont ceux des tutos Flutter) ;
- suis le kit d'upload [`upload.md`](upload.md) (21/10) : titre, description, tags, fiches, écran de fin, réglages ; les sous-titres [`uber.fr.srt`](uber.fr.srt) et [`uber.en.srt`](uber.en.srt) sont prêts.
