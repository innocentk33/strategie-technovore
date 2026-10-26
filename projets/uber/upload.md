# Uber : kit d'upload YouTube

> Vidéo finale : 9:59,6, montage HyperFrames. Les temps viennent du [storyboard](STORYBOARD.md), calé sur la vidéo finale. Sous-titres prêts : [`uber.fr.srt`](uber.fr.srt) et [`uber.en.srt`](uber.en.srt).
> La vidéo est déjà en ligne **en privé** (id `cRv2ouxZZdw`). Son titre actuel, « L'hisoire du temps réel derriere uber », et ses tags, ceux des tutos Flutter, sont à remplacer par ce kit.
> **26/10, ton choix : titre *La carte d'Uber est une illusion (et c'est génial)*** et test à trois miniatures (`noir-01`, « HORS-JEU ? » et « 17 min »). Les sections « Titres », « Le test », « Réglages Studio » et « Avant de publier » sont à jour.
> Recherche vidIQ du 21/10. Le chiffre de 40 millions par jour a été vérifié le 21/10 dans les résultats d'Uber (lien dans la description).

## Mots-clés (vidIQ, 21/10)

| Mot-clé | Recherches/mois | Concurrence | Usage |
|---|---|---|---|
| uber | 237 K dans le monde, **12,9 K en France** | 71 | Titre, miniature (vrai logo) |
| how uber works | 9,1 K | 39 | Tags (public dev anglophone, sous-titres EN) |
| uber system design | 8,7 K, **+155 % en 30 jours** | 38 | Tags, hashtag |
| comment fonctionne uber | < 750 | 31 | Début de la description, tags |
| uber hexagone | < 750 | — | Tags |

En français, la recherche sur ce sujet précis est quasi nulle : la vidéo vivra des suggestions et de l'accueil, comme prévu dans la stratégie (pilier « génie »). Le seul mot qui pèse, c'est « Uber ». Côté devs anglophones, « uber system design » monte vite : tes sous-titres anglais servent ici.

## Titres

| | Titre | Car. | Score vidIQ |
|---|---|---|---|
| **Retenu le 26/10** | La carte d'Uber est une illusion (et c'est génial) | 50 | 88 |
| *Écarté le 26/10* | Pourquoi la carte Uber est un mensonge permanent | 48 | 85 |
| *Écarté le 26/10* | Dans les coulisses d'Uber : la technologie derrière votre course | 64 | 87 |
| *Écarté le 26/10* | Les voitures fantômes d'Uber : la vérité technique | 50 | 84 |
| A · Mixte (recommandé jusqu'au 26/10) | Le génie caché derrière la carte en temps réel d'Uber | 53 | 84 |
| B · Recherche | Comment fonctionne la carte en temps réel d'Uber ? | 50 | 84 |
| C · Curiosité | Uber a dû découper la planète en hexagones | 42 | 80 |
| *Écarté* | Uber : le génie caché derrière sa carte en temps réel | 52 | 78 |

- **Pourquoi « illusion » (26/10)** :
  - il garde le conflit de « mensonge » sans accuser Uber, que la vidéo n'accuse pas : c'est le support d'Uber qui parle d'un « effet visuel » (8:13), et la vidéo dit « la position d'un chauffeur d'il y a quelques secondes, en partie devinée » (9:00) ;
  - « (et c'est génial) » est le verdict de la vidéo (9:35, « les ingés d'Uber, c'est des génies ») ;
  - « Uber » arrive dans les 15 premiers caractères : la coupure mobile (vers 45) tombe dans la parenthèse ;
  - les 6 titres notés par vidIQ le 26/10 vont de 78 à 88 : l'écart ne départage pas, le choix se fait sur le fond.
- **Pourquoi A (21/10)** :
  - c'est la formule de l'inspiration (Philipp Lackner, « The Genius System Behind the Uber App's Real-Time Map », ×35,7) et celle de ton pilier ;
  - la miniature pose la question (« elle existe ? ») et le titre promet le génie, sans répéter la même info.
  - Sur mobile, « d'Uber » peut être coupé, mais le vrai logo Uber est sur la miniature.
- **B** a le même score. Elle est plus « recherche », mais la recherche française est quasi nulle (< 750 par mois).
- **C** reprend le hook de 0:06 (« hexagones »), donc la vidéo tient la promesse. C'est la variante à tester si A déçoit.
- **Honnêteté** : la vidéo explique bien la carte en temps réel (trouver, envoyer, afficher), avec ses sources Uber Engineering. Rien dans A, B ou C n'est exagéré. « Illusion » est tenu par 8:13 et 9:00, alors que « mensonge » ne l'est pas : Uber a démenti, et la vidéo conclut au génie.

**Le test (26/10)** : Studio sur ordinateur > ta vidéo > « Tester et comparer », trois miniatures dans cet ordre : [`noir-01`](../../ressources/miniatures/rendus/noir-01.png) (« elle existe ? », la charte de la série, gardée si le test n'est pas concluant), [`hors-niche-1`](miniature/propositions/hors-niche-1.png) (« HORS-JEU ? ») et [`hors-niche-2`](miniature/propositions/hors-niche-2.png) (« 17 min »). Le titre ne bouge pas pendant le test : le modifier l'arrête. La vidéo est programmée, donc privée jusqu'à 18 h : si Studio ne propose pas encore le test, lance-le dès la sortie. Il remplace le test `noir-01` contre `noir-01b` ; le détail est dans [`miniature/propositions.md`](miniature/propositions.md).

## Description

```
Comment fonctionne la carte en temps réel d'Uber ? Ces petites voitures qui glissent autour de toi, il a fallu découper la planète en hexagones pour les afficher.

Dans cette vidéo, on suit une seule position GPS, du téléphone d'un chauffeur parisien jusqu'au tien. Trois étapes : trouver les chauffeurs autour de toi (la grille hexagonale H3), envoyer leur position en direct (le passage du polling au push, avec RAMEN et Fireball), puis l'afficher au bon endroit malgré un GPS qui se trompe de 50 mètres en ville (l'ombre des immeubles, le filtre à particules). Et à la fin, l'enquête de 2015 sur les « voitures fantômes » d'Uber.

Sous-titres en français et en anglais.

CHAPITRES
0:00 Ces voitures existent-elles vraiment ?
0:25 Un pote, un article
1:11 Trouver les chauffeurs autour de toi
1:48 Carrés contre hexagones
2:14 H3, la grille hexagonale d'Uber
2:47 Le prix fixé hexagone par hexagone
3:00 Les 16 niveaux de H3
3:12 Les 12 pentagones cachés
3:44 Envoyer la position en direct
3:58 Le polling
4:32 Le push
4:43 RAMEN : Fireball, l'API gateway et le livreur
5:36 Afficher la voiture au bon endroit
6:03 Pourquoi le GPS se trompe en ville
6:28 L'ombre des immeubles
6:47 Le filtre à particules
6:59 Pour les devs : pourquoi pas Kalman
7:31 Glisser et deviner
7:53 Les voitures fantômes
9:02 Le verdict

SOURCES
• Uber Engineering, « Uber's Real-Time Push Platform » (18 déc. 2020) : https://www.uber.com/blog/real-time-push-platform/
• Uber Engineering, « H3: Uber's Hexagonal Hierarchical Spatial Index » (27 juin 2018) : https://www.uber.com/blog/h3/
• Uber Engineering, « Rethinking GPS: Engineering Next-Gen Location at Uber » (19 avr. 2018) : https://www.uber.com/blog/rethinking-gps/
• H3, dépôt open source : https://github.com/uber/h3 · table des résolutions : https://h3geo.org/docs/core-library/restable/
• A. Rosenblat et L. Stark, « Uber's Phantom Cabs », Motherboard / VICE (27 juil. 2015) : https://www.vice.com/en/article/ubers-phantom-cabs/
• B. Snyder, « Uber denies there are 'phantom' cars in its app », Fortune (30 juil. 2015) : https://fortune.com/2015/07/30/uber-phantom-cars/
• Uber, résultats du 2e trimestre 2026 : 3 867 millions de courses et livraisons en 3 mois, soit plus de 40 millions par jour : https://www.businesswire.com/news/home/20260805020613/en/
• Mewtwo dans Pokémon GO (2017), Bulbanews : https://bulbanews.bulbagarden.net/wiki/Mewtwo_to_be_available_in_Pok%C3%A9mon_GO_via_Exclusive_Raid_Battles

CARTES
Données cartographiques © les contributeurs d'OpenStreetMap (licence ODbL) · Natural Earth (domaine public) · cellules H3 générées avec la bibliothèque H3 (Apache 2.0). La carte d'Uber est recréée : aucune vraie interface de l'application n'est montrée.

MUSIQUES
• « Future Minimal », kissan4 (Pixabay)
• « Dark Ambient for Crime and Tension », megalix (Pixabay)
• Track: MokkaMusic - Singularity https://youtu.be/FRACg2wCY9M · Music provided by MokkaMusic Youtube channel and https://inaudio.org
• « INTRIGUE », Savfk, licence CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/) · https://www.youtube.com/c/SavfkMusic · promoted by Epic Music Waves

BRUITAGES
• « Sonar ping (sine wave) » par marb7e, CC BY 4.0 : https://freesound.org/people/marb7e/sounds/620321
• « E-type Jaguar, car engine, rev-twice » par Dan_AudioFile, CC BY 4.0 : https://freesound.org/people/Dan_AudioFile/sounds/614695
• Autres bruitages : CC0 (Openverse) et banque personnelle

IMAGES ET EXTRAITS
• Carte portulan de l'Atlantique, Library of Congress (domaine public)
• Bol de ramen : « Shoyu ramen - Goemon Ramen Bar », Wikimedia Commons (CC0)
• Extraits courts cités et commentés : Pokémon GO à Central Park (2016), Shrek 2 (DreamWorks), Senhora do Destino (« Math Lady », Globo), Boruto (Crunchyroll), Monster Hunter Wilds (Capcom), le sorcier de Clash Royale (Supercell), le mème « Galaxy brain »

Quelle appli j'ouvre ensuite ? Dis-le en commentaire.

Sur Technovore, j'ouvre le capot des applis que tu utilises tous les jours. Abonne-toi : c'est le seul abonnement qui ne te prélèvera jamais rien.

#Uber #CommentÇaMarche #SystemDesign
```

- **Les deux premières lignes** (avant « … plus ») : « Comment fonctionne la carte en temps réel d'Uber » dès les premiers mots, puis le hook de la vidéo (les hexagones).
- **Changements par rapport au premier jet du storyboard** :
  - la 1re phrase porte le mot-clé ;
  - les chapitres commencent par la question de l'accroche au lieu d'« Intro » ;
  - le lien des résultats d'Uber est ajouté : 3 867 M de courses et livraisons sur 91 jours, soit 42,5 M par jour, donc « 40 millions » est un arrondi prudent ;
  - le lien de la licence CC BY est ajouté pour Savfk ;
  - les hashtags sont ajoutés.
- **Chapitres** : ils commencent à 0:00, et le plus court (4:32 → 4:43) dure 11 s. YouTube exige au moins 10 s par chapitre. Si tu en veux moins, prends la version courte du storyboard (7 chapitres), en gardant « 0:00 Ces voitures existent-elles vraiment ? ».
- **Crédit MokkaMusic** : la ligne « Track: MokkaMusic… » est recopiée telle quelle, c'est le texte exigé par inaudio.

## Tags

```
comment fonctionne uber, carte uber temps réel, uber, how uber works, uber system design, uber h3, grille hexagonale, hexagones uber, polling vs push, uber ramen, uber fireball, gps en ville, filtre à particules, dead reckoning, voitures fantômes uber, uber engineering, system design, technovore
```

Les tags pèsent très peu (le guide SEO du skill les dit « vestigiaux »). Ils servent surtout aux mots anglais que tapent les devs.

## Commentaire épinglé

```
Quelle appli tu veux que j'ouvre ensuite ? Dis-le en commentaire 👇

Pour les devs, la recherche de la vidéo en 3 lignes (H3 v4, Python) :
import h3
cell = h3.latlng_to_cell(48.8443, 2.3744, 9)  # la gare de Lyon
voisins = h3.grid_disk(cell, 2)                # 19 cases (kRing → grid_disk dans H3 v4)
```

Le code est juste pour H3 v4 : `grid_disk(cell, 2)` renvoie 1 + 6 + 12 = 19 cases, comme les anneaux de la vidéo (2:22).

## Fiches et écran de fin

| Élément | Quand | Vers | Pourquoi |
|---|---|---|---|
| Fiche 1 | **5:08** (« l'API gateway, la cuisine ») | OpenCode a été gravement piraté | Le même public de devs, et un pont naturel : une API, des clés, ce qui se passe quand ça fuit |
| Fiche 2 (à ajouter le 9/11) | **5:37** (le GPS qui se trompe de 50 m) | Waze | La suite logique : un autre téléphone qui sert de capteur de position |
| Écran de fin | **9:39,5 → 9:59,6** (20 s) | À gauche, l'élément vidéo **ArtCraft** ; à droite, « S'abonner » | Les cadres sont déjà dessinés dans la vidéo, aux bonnes places. **Le 9/11, remplace ArtCraft par Waze** : même pilier, mêmes cartes |

Les fiches ne suivent pas la règle « 20 % et 70 % » : elles sont posées sur les deux moments qui donnent envie de cliquer. Le guide SEO du skill rappelle que fiches et écrans de fin ne jouent pas sur le classement ; ils servent à garder le spectateur.

## Réglages Studio

| Réglage | Valeur | Pourquoi |
|---|---|---|
| Visibilité | **Programmée : lun. 26/10 à 18:00** (heure de Paris) | Créneau de la v4. Après le passage à l'heure d'hiver du 25/10, ça fait 17 h à Abidjan, 18 h à Kinshasa et Douala |
| Première | Non | Une première attire peu de monde à cette taille de chaîne, et la vidéo serait visible avant sa sortie |
| Public | Non conçu pour les enfants | |
| Catégorie | Science et technologie | |
| Langue de la vidéo | Français | |
| Sous-titres | Importer `uber.fr.srt` (français) et `uber.en.srt` (anglais) | Le guide SEO : un fichier SRT est mieux indexé que les sous-titres automatiques |
| Contenu modifié ou synthétique | Non | C'est ta vraie voix, et la carte est une animation recréée, pas une scène réaliste |
| Promotion payante | Non | |
| Commentaires | Ouverts, sans tri automatique pour les 2 premières heures | Tu réponds à tout pendant les 2 premières heures (stratégie, section 5) |
| Miniature | `noir-01`, puis « Tester et comparer » avec `hors-niche-1` et `hors-niche-2` (26/10) | Voir « Le test » |

## Avant de publier

- [ ] Titre *La carte d'Uber est une illusion (et c'est génial)* dans Studio, avant 18 h (26/10)
- [ ] Les tags Flutter remplacés par ceux du kit
- [ ] « Uber » et « comment fonctionne » dans les 25 premiers mots de la description
- [ ] Description sous 5 000 caractères (4 084) et tags sous 500 (296)
- [ ] Chapitres à partir de 0:00, 20 chapitres, tous ≥ 10 s
- [ ] Hashtags dans la description, pas dans le titre (3)
- [ ] Miniature personnalisée `noir-01`, puis « Tester et comparer » avec `hors-niche-1` et `hors-niche-2` (les PNG 4K, importés depuis l'ordinateur)
- [ ] Sous-titres FR et EN importés, et un coup d'œil sur un passage de chacun dans le lecteur
- [ ] Fiche 1 à 5:08 vers OpenCode
- [ ] Écran de fin : ArtCraft à gauche, « S'abonner » à droite, de 9:39,5 à 9:59,6, sur les cadres dessinés dans la vidéo
- [ ] Public : non conçu pour les enfants ; catégorie : Science et technologie ; contenu modifié : non
- [ ] Programmation : lun. 26/10, 18:00
- [ ] Commentaire épinglé prêt à coller à 18 h
- [ ] **Après la mise en ligne** (storyboard, section 9) :
  - Content ID : une réclamation sur les extraits de 1 à 2,6 s (Pokémon GO, Shrek 2, Math Lady, Boruto, Monster Hunter Wilds) ? Remplace l'extrait par un écran recréé ;
  - Singularity (MokkaMusic) : retire la réclamation sur https://inaudio.org, rubrique « Remove Claim », avec le lien de la vidéo ;
  - le sorcier de Clash Royale : vérifie la politique de Supercell sur les contenus de fans (Fan Content Policy).
- [ ] Facultatif : à 9:39, la voix dit « Si **vous** avez aimé » alors que tout le reste tutoie (storyboard, section 8). Réenregistrer ou laisser.
