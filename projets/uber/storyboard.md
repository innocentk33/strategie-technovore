# Storyboard : Le génie caché derrière la carte en temps réel d'Uber

> Montage HyperFrames, recette « Premium noir » 16:9. **Durée : 9:59,6** (599,58 s), 1920 × 1080. Les temps de ce document sont ceux de la vidéo finale.
> La page visuelle (une image par plan) est `boards/storyboard.html`, dans l'onglet Storyboard.

## 1. La vidéo

| Champ | Détail |
|---|---|
| Pilier | Le génie derrière l'app |
| Format | Vidéo longue YouTube, 9:59 |
| Mot-clé principal | comment fonctionne uber |
| Type d'accroche | Curiosité : « Est-ce que toutes ces voitures existent vraiment ? » |
| Promesse | Suivre une seule position GPS, du téléphone d'un chauffeur parisien jusqu'au tien |
| Héros | Le point blanc : la position du chauffeur |
| Structure | Accroche → un pote, un article → Trouver → Envoyer → Afficher → les voitures fantômes → le verdict |

### Titres possibles

1. **Le génie caché derrière la carte en temps réel d'Uber** (recommandé : recherche + curiosité)
2. Uber a dû découper la planète en hexagones
3. Comment fonctionne la carte en temps réel d'Uber ?

### Miniature

Retenue le 21/10 : [`noir-01.png`](../../ressources/miniatures/rendus/noir-01.png) (« elle existe ? »), en test A/B contre [`noir-01b.png`](../../ressources/miniatures/rendus/noir-01b.png). L'idée « COMMENT ?! » est abandonnée (voir la [fiche](fiche.md)).

## 2. Description YouTube (à copier)

> **Version finale : [`upload.md`](upload.md)** (21/10), avec le mot-clé en 1re phrase, le lien des résultats d'Uber et les hashtags. Ce bloc reste le premier jet.

```text
Ouvre Uber : tu vois ces petites voitures qui glissent autour de toi ? Pour qu'elles arrivent sur ta carte, il a fallu découper la planète en hexagones, réinventer la façon dont ton téléphone parle au serveur, et corriger un GPS qui se trompe de 50 mètres en ville.

Dans cette vidéo, on suit une seule position GPS, du téléphone d'un chauffeur parisien jusqu'au tien : la grille hexagonale H3, le passage du polling au push (RAMEN), l'ombre des immeubles, le filtre à particules… et l'enquête de 2015 sur les « voitures fantômes ».

Quelle appli j'ouvre ensuite ? Dis-le en commentaire.

⏱️ Chapitres
0:00 Intro
0:25 Un pote, un article
1:11 Trouver les chauffeurs autour de toi
1:48 Carrés contre hexagones
2:14 H3, la grille d'Uber
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

📚 Sources
• Uber Engineering, « Uber's Real-Time Push Platform » (18 déc. 2020) : https://www.uber.com/blog/real-time-push-platform/
• Uber Engineering, « H3: Uber's Hexagonal Hierarchical Spatial Index » (27 juin 2018) : https://www.uber.com/blog/h3/
• Uber Engineering, « Rethinking GPS: Engineering Next-Gen Location at Uber » (19 avr. 2018) : https://www.uber.com/blog/rethinking-gps/
• H3, dépôt open source : https://github.com/uber/h3 · documentation et table des résolutions : https://h3geo.org/docs/core-library/restable/
• A. Rosenblat et L. Stark, « Uber's Phantom Cabs », Motherboard / VICE (27 juil. 2015) : https://www.vice.com/en/article/ubers-phantom-cabs/
• B. Snyder, « Uber denies there are 'phantom' cars in its app », Fortune (30 juil. 2015) : https://fortune.com/2015/07/30/uber-phantom-cars/
• Uber, résultats du 2e trimestre 2026 (3 867 M de courses et livraisons) : [lien à ajouter]
• Mewtwo dans Pokémon GO (2017), Bulbanews : https://bulbanews.bulbagarden.net/wiki/Mewtwo_to_be_available_in_Pok%C3%A9mon_GO_via_Exclusive_Raid_Battles

🗺️ Cartes
Données cartographiques © les contributeurs d'OpenStreetMap (licence ODbL) · Natural Earth (domaine public) · cellules H3 générées avec la bibliothèque H3 (Apache 2.0). La carte d'Uber est recréée : aucune vraie interface de l'application n'est montrée.

🎵 Musiques
• « Future Minimal », kissan4 (Pixabay)
• « Dark Ambient for Crime and Tension », megalix (Pixabay)
• Track: MokkaMusic - Singularity https://youtu.be/FRACg2wCY9M · Music provided by MokkaMusic Youtube channel and https://inaudio.org
• « INTRIGUE », Savfk (CC BY 4.0) · https://www.youtube.com/c/SavfkMusic · promoted by Epic Music Waves

🔊 Bruitages
• « Sonar ping (sine wave) » par marb7e, CC BY 4.0 : https://freesound.org/people/marb7e/sounds/620321
• « E-type Jaguar, car engine, rev-twice » par Dan_AudioFile, CC BY 4.0 : https://freesound.org/people/Dan_AudioFile/sounds/614695
• Autres bruitages : CC0 (Openverse) et banque personnelle

🖼️ Images et extraits
• Carte portulan de l'Atlantique, Library of Congress (domaine public)
• Bol de ramen : « Shoyu ramen - Goemon Ramen Bar », Wikimedia Commons (CC0)
• Extraits courts cités et commentés : Pokémon GO à Central Park (2016), Shrek 2 (DreamWorks), Senhora do Destino (« Math Lady », Globo), Boruto (Crunchyroll), Monster Hunter Wilds (Capcom), le sorcier de Clash Royale (Supercell), le mème « Galaxy brain »
```

### Chapitres courts (si tu préfères n'en garder que 7)

```text
0:00 Intro
0:25 Un pote, un article
1:11 Trouver les chauffeurs autour de toi
3:44 Envoyer la position en direct
5:36 Afficher la voiture au bon endroit
7:53 Les voitures fantômes
9:02 Le verdict
```

Chaque chapitre principal a son écran dédié dans la vidéo, aux mêmes temps.

## 3. Commentaire épinglé

```text
Quelle appli tu veux que j'ouvre ensuite ? Dis-le en commentaire 👇

Pour les devs, la recherche de la vidéo en 3 lignes (H3 v4, Python) :
import h3
cell = h3.latlng_to_cell(48.8443, 2.3744, 9)  # la gare de Lyon
voisins = h3.grid_disk(cell, 2)                # 19 cases (kRing → grid_disk dans H3 v4)
```

## 4. Mots-clés (tags)

comment fonctionne uber, carte uber temps réel, uber H3, grille hexagonale, hexagones uber, polling vs push, RAMEN uber, uber fireball, GPS en ville, urban canyon, filtre à particules, dead reckoning, voitures fantômes uber, uber engineering, system design, architecture temps réel, géospatial

## 5. Shorts à extraire

> Plus de Shorts depuis le 21/10 (stratégie v4). Ces passages restent une liste des moments forts.

| Short | Passage de la vidéo | Idée |
|---|---|---|
| « Uber a découpé la planète en hexagones » | 0:00 à 0:07 puis 2:08 à 2:14 | Le dézoom jusqu'au globe, puis la bascule de la grille |
| « Pourquoi des hexagones et pas des carrés ? » | 1:48 à 2:14 | La devinette, 1,41, Math Lady, les 6 voisins |
| « La voiture sur ta carte n'est pas là où tu crois » | 5:36 à 6:03 | 50 m d'erreur, Fast and Furious, « C'est la famille. » |
| (bonus) « Le serveur qui pète un câble » | 3:46 à 4:09 | L'âne de Shrek, puis la dispute du polling jusqu'au « NON ! » |

## 6. Écran de fin YouTube

- De **9:39,5 à 9:59,6** (20 s) : cadre « Vidéo suivante » à gauche (y placer l'élément vidéo, la vidéo ArtCraft), bouton « S'abonner » à droite.
- Rien d'important sous les éléments YouTube ; la musique « maison » continue environ 15 s après la voix.

## 7. Musique

| Passage | Morceau | Ruptures |
|---|---|---|
| Accroche | Future Minimal (kissan4) | Drop sur « hexagones » (0:06), coupe sèche après « vraiment ? » |
| Un pote → Trouver | Future Minimal, boucle « maison » | 0:25–1:35, coupée pour le mème Pokémon GO ; 1:38–1:53 ; silence pendant la devinette et les carrés ; repart sur le « clac » des hexagones (2:11–3:45) |
| Envoyer | Singularity (MokkaMusic) | 3:46–3:55, coupée pour l'âne de Shrek ; 3:58–4:43, coupée pour le slurp ; 4:44–5:35, coupée net sur « juste » |
| Afficher | Intrigue (Savfk) | 5:38–6:02, accent sur « 180 », coupée pour « C'est la famille. » ; 6:04–7:53 |
| Les voitures fantômes | Dark Ambient (megalix) | 7:57–9:02 ; la pulsation entre sur « Officiellement » |
| Le verdict, fin | Future Minimal, « maison » | 9:04–9:59, revient sur « on récapitule » |

Mixage complet mesuré à la dernière vérification : -16 LUFS intégrés, crête -4 dBFS (cible de la recette : -16 à -14 LUFS, crête < -1 dBFS).

## 8. La voix

- Voix montée d'origine gardée : `assets/audio/voix-off-montee.flac`. La vidéo joue `assets/audio/voix-off-montee-v2.flac`, d'où ces reprises sont coupées :
  - 1:55 : le faux départ « Ta carte, euh… » ;
  - 3:00 : le premier des deux « donc » ;
  - 6:51 : la reprise « À chaque mesure, celles qui co… » ;
  - 6:55 : le premier des deux « C'est » ;
  - 7:08 : la reprise « Kalman suppose… Kal… » ;
  - 7:25 : un murmure et un « en » isolé avant « Un peu comme un coéquipier » ;
  - 8:16 : les reprises « Et même mieux vaudrait voir. Et même mieux. » ;
  - 9:29 : la reprise « Tout ce qu'on vient, » ;
- Liste des coupes dans `assets/lib/kit.js` (EDITS) : toutes les animations suivent la voix.

### À réenregistrer si tu veux (je les insère et je recale tout)

- 5:00 : « Fireball, c'est le **géant** » (le gérant)
- 6:52 : « celles qui **cognent** avec les signaux » (collent)
- 8:12 : « Le support d'Uber lui répond que… », dit trop vite
- 8:18 : « un **économisateur** d'écran » (économiseur ; l'écran affiche le bon mot)
- 9:39 : « Si **vous** avez aimé… » : tout le reste tutoie

## 9. Avant de publier

- **Content ID** : les extraits de Pokémon GO, Shrek 2, Math Lady, Boruto et Monster Hunter Wilds durent 1 à 2,6 s et sont commentés. YouTube peut quand même les repérer : en cas de blocage, remplace l'extrait par un écran recréé.
- **Singularity (MokkaMusic)** : avec l'offre gratuite d'inaudio, la réclamation se retire depuis https://inaudio.org (rubrique « Remove Claim ») en collant le lien de la vidéo ; le crédit en description est obligatoire.
- **Chiffre de 40 millions par jour** : ajouter le lien des résultats Uber du 2e trimestre 2026 dans les sources.
- **Le sorcier de Clash Royale** : image de Supercell ; vérifie que ton usage respecte leur politique de contenu de fans (Fan Content Policy).

## 10. Le plan, image par image

Une entrée par plan, dans l'ordre du film (temps en secondes). Les images sont dans `boards/stills/`.

## Frame 1: Le téléphone en contre-plongée (0-3.45s)
- act: Accroche
- still: boards/stills/at-2.6s.png
- status: animated
- 0:00,0 : La caméra monte du bas du téléphone : carte sombre de la gare de Lyon, 5 voitures qui glissent sur de vraies rues autour de toi. Sous-titres karaoké.

## Frame 2: Dézoom : Paris puis la France (3.45-5.9s)
- act: Accroche
- still: boards/stills/at-5.5s.png
- status: animated
- 0:03,5 : On plonge dans l'écran, puis on recule sans coupe : la rue, Paris, la France sous de vraies cellules H3.

## Frame 3: La Terre en hexagones (5.9-7.5s)
- act: Accroche
- still: boards/stills/at-6.9s.png
- status: animated
- 0:05,9 : Le globe couvert d'hexagones H3 tombe sur « hexagones » (drop de la musique) ; compteur « 569 707 381 193 162 cases ».

## Frame 4: Du chauffeur jusqu'à toi (7.5-12.15s)
- act: Accroche
- still: boards/stills/at-11.9s.png
- status: animated
- 0:07,5 : Retour sur la gare de Lyon : la voiture s'allume, le point blanc quitte son toit, « chauffeur » → « toi ».

## Frame 5: Un serveur bombardé (12.15-15.9s)
- act: Accroche
- still: boards/stills/at-15.4s.png
- status: animated
- 0:12,2 : Un serveur en traits sous une pluie de bulles « ? » ; ses voyants passent au rouge.

## Frame 6: Le GPS se trompe de 50 m (15.9-17.66s)
- act: Accroche
- still: boards/stills/at-17.3s.png
- status: animated
- 0:15,9 : Le point saute de travers ; règle rouge « 50 m ».

## Frame 7: Teaser du dérapage (17.66-18.9s)
- act: Accroche
- still: boards/stills/at-18.2s.png
- status: animated
- 0:17,7 : 0,8 s de dérapage avec traces de pneus, arrêt sur image, crissement coupé net.

## Frame 8: La voiture qui n'existe pas (18.9-25.45s)
- act: Accroche
- still: boards/stills/at-24.7s.png
- status: animated
- 0:18,9 : Le téléphone revient ; « 2015 » ; sur « vraiment », une voiture devient translucide et disparaît. Musique coupée sèche.

## Frame 9: Écran de chapitre 1 (25.55-27.5s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-26.6s.png
- status: animated
- 0:25,6 : « Un pote, un article » ; la musique « maison » entre sur l'écran.

## Frame 10: Le blog Uber (27.25-34.6s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-29.5s.png
- status: animated
- 0:27,2 : La vraie page Ingénierie du blog Uber défile dans une carte arrondie.

## Frame 11: L'article du pote (34.6-37.4s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-35s.png
- status: animated
- 0:34,6 : « Uber's Real-Time Push Platform » (18 déc. 2020) passe devant la page.

## Frame 12: « polling » surligné (37-38.5s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-38.4s.png
- status: animated
- 0:37,0 : Poussée sur l'intro de l'article, « polling » se surligne en jaune quand il est dit.

## Frame 13: Galaxy brain, paliers 1 à 3 (38.55-41.45s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-41.1s.png
- status: animated
- 0:38,5 : Coupe franche : trois cerveaux de plus en plus lumineux, avec nos légendes.

## Frame 14: Maquette Flutter générique (41.45-46.4s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-43s.png
- status: animated
- 0:41,5 : Un téléphone avec une carte simple, le logo Flutter et quatre marqueurs (pas ton appli).

## Frame 15: Des millions de positions (46.4-50.1s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-48.2s.png
- status: animated
- 0:46,4 : Recul : des milliers de points autour du téléphone devenu minuscule.

## Frame 16: Les autres articles (50.15-52.15s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-51.4s.png
- status: animated
- 0:50,1 : Trois vrais articles en éventail (Push Platform, H3, Rethinking GPS), « Toutes les sources en description ».

## Frame 17: Mon pote avait raison ? (53.1-54.9s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-54.1s.png
- status: animated
- 0:53,1 : La question au centre, mot à mot ; la musique baisse.

## Frame 18: 40 millions par jour (55.6-61.4s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-59.5s.png
- status: animated
- 0:55,6 : Compteur SF Mono jusqu'à « 40 000 000 / jour » sur le tiers gauche, source en petit.

## Frame 19: Une seule course (61.3-63s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-62.2s.png
- status: animated
- 1:01,3 : Il reste un point blanc qui file vers le chauffeur ; la vraie carte apparaît.

## Frame 20: Le chauffeur, gare de Lyon (63-67.2s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-66.9s.png
- status: animated
- 1:03,0 : La voiture du chauffeur porte le point, qui quitte son toit sur « position ».

## Frame 21: Deux rues plus loin (66.75-69.8s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-69.4s.png
- status: animated
- 1:06,8 : Recul : l'anneau « toi » et le trajet en pointillés.

## Frame 22: La carte du trajet (69.8-71s)
- act: Chapitre 1 · Un pote, un article
- still: boards/stills/at-70.9s.png
- status: animated
- 1:09,8 : Trouver · Envoyer · Afficher se dessine, à la place exacte de l'écran de chapitre suivant.

## Frame 23: Écran de chapitre 2 (71-73.35s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-72.4s.png
- status: animated
- 1:11,0 : « Trouver », étape 1 allumée.

## Frame 24: 300 voitures (73.05-79.6s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-78.6s.png
- status: animated
- 1:13,0 : Recul sur 300 voitures posées sur la grille carrée, toi au centre.

## Frame 25: Un million de calculs (79.6-88.5s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-87.3s.png
- status: animated
- 1:19,6 : 300 traits rouges, compteur « 1 000 000 » qui s'emballe sur le tiers gauche.

## Frame 26: La mosaïque de téléphones (88.5-95.9s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-92.6s.png
- status: animated
- 1:28,5 : L'écran se démultiplie (×4, ×16, ×64).

## Frame 27: Mème : Pokémon GO (95.9-98.1s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-97.6s.png
- status: animated
- 1:35,9 : Coupe franche sur la ruée de Central Park avec son son, puis « Spoiler : Mewtwo n'est arrivé qu'en 2017 ».

## Frame 28: Chaque chauffeur dans sa case (98.1-108.75s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-107.9s.png
- status: animated
- 1:38,1 : Les traits s'effacent, les voitures glissent dans leur case ; ta case puis ses 8 voisines.

## Frame 29: La devinette (108.75-115.4s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-114.5s.png
- status: animated
- 1:48,8 : Deux secondes de silence sur la grille, tic-tac discret, musique coupée.

## Frame 30: Côté contre coin (115.4-122.77s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-120.37s.png
- status: animated
- 1:55,4 : 4 flèches vertes, 4 flèches rouges en diagonale.

## Frame 31: « 1,41 » et Math Lady (121.77-128.17s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-122.37s.png
- status: animated
- 2:01,8 : « 1,41 » en pop ; Math Lady 1 s en carte (le texte incrusté est rogné).

## Frame 32: La bascule en hexagones (128.17-131.77s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-130.57s.png
- status: animated
- 2:08,2 : Toute la grille se déforme du centre vers les bords et se fige en hexagones (« clac », la musique repart).

## Frame 33: Six voisins à égale distance (131.77-134.27s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-132.97s.png
- status: animated
- 2:11,8 : 6 flèches vertes identiques. Le décor reste hexagonal jusqu'à la fin.

## Frame 34: L'article H3 (2018) (134.27-136.97s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-135.97s.png
- status: animated
- 2:14,3 : La vraie capture de l'article du 27 juin 2018.

## Frame 35: GitHub et « H3 » (136.97-139.27s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-138.47s.png
- status: animated
- 2:17,0 : Le dépôt uber/h3 et « H3 » en héros.

## Frame 36: Position GPS → hexagone (139.27-142.87s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-140.77s.png
- status: animated
- 2:19,3 : « 48.8443, 2.3744 » tombe dans ta case.

## Frame 37: 7 puis 19 cases (142.87-149.17s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-147.57s.png
- status: animated
- 2:22,9 : Anneau 1, anneau 2 ; « un k-ring » ; mention pour les devs « kRing → grid_disk ».

## Frame 38: 1 000 000 → ~100 (149.17-154.67s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-152.77s.png
- status: animated
- 2:29,2 : Le compteur revient au même endroit et descend à « ~100 », en vert.

## Frame 39: Abonne-toi (154.67-162.37s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-158.97s.png
- status: animated
- 2:34,7 : Bouton « S'abonner » cliqué en bas à droite, la musique baisse.

## Frame 40: Le Pokémon shiny (162.37-168.27s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-166.67s.png
- status: animated
- 2:42,4 : Une silhouette d'étincelles au centre des 7 cases (aucune image officielle).

## Frame 41: Chaque hexagone comparé (167.97-174.37s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-171.17s.png
- status: animated
- 2:48,0 : Recul sur tout Paris (données OSM), carte de chaleur H3, l'article H3 surligné.

## Frame 42: ×1,8 : ton hexagone décide (174.37-180.27s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-178.67s.png
- status: animated
- 2:54,4 : « ×1,8 » rouge sur le tiers gauche, « sam. 02:00 », relié à ton hexagone.

## Frame 43: Niveau 0 : huit France (180.27-188.93s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-188.63s.png
- status: animated
- 3:00,3 : L'hexagone du niveau 0 se divise en 7 ; 8 silhouettes de France à l'échelle.

## Frame 44: Niveau 15 : 0,9 m² (188.93-192.63s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-191.33s.png
- status: animated
- 3:08,9 : Plongée jusqu'au niveau 15, « 0,9 m² » et « 569 707 381 193 162 cases ».

## Frame 45: Douze pentagones en mer (192.63-211.33s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-210.13s.png
- status: animated
- 3:12,6 : Le globe tourne, 12 pentagones rouges clignotent, tous en mer ; la musique remonte.

## Frame 46: La voiture à bouée (211.33-217.23s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-215.03s.png
- status: animated
- 3:31,3 : Plongée sur le pentagone du Pacifique : une voiture flotte dans une bouée. Vagues, mouette.

## Frame 47: Trouver ✓, Envoyer clignote (217.23-224.53s)
- act: Chapitre 2 · Trouver
- still: boards/stills/at-221.63s.png
- status: animated
- 3:37,2 : « Trouver » passe au vert, le point file vers « Envoyer ».

## Frame 48: Écran de chapitre 3 (224.53-226.53s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-225.63s.png
- status: animated
- 3:44,5 : « Envoyer », étape 2.

## Frame 49: Le gamin à l'arrière (226.23-235.53s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-234.73s.png
- status: animated
- 3:46,2 : Le téléphone sur la banquette demande trois fois « C'est quand qu'on arrive ? ».

## Frame 50: Mème : l'âne de Shrek 2 (235.53-238.13s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-236.73s.png
- status: animated
- 3:55,5 : Coupe franche sur l'extrait VF « On est presque arrivés ? », avec son son, musique coupée.

## Frame 51: Le polling (238.13-249.03s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-243.6s.png
- status: animated
- 3:58,1 : La dispute en trois temps : le téléphone crie « Du nouveau ? », le serveur répond « non… » tout bas ; « Encore du nouveau ? », « Non. », le serveur grossit ; puis « NON ! » hurlé, le serveur enfle et le téléphone rapetisse pour se cacher.

## Frame 52: L'article du pote, encore (246.53-249.13s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-248.03s.png
- status: animated
- 4:06,5 : La carte de l'article revient, « polling » surligné.

## Frame 53: 80 % des requêtes (249.13-262.13s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-259.63s.png
- status: animated
- 4:09,1 : La batterie se vide ; « 80 % » rouge, la phrase de l'article surlignée, 8 pastilles sur 10 à la porte d'entrée.

## Frame 54: Le réseau qui coupe (262.13-266.73s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-265.73s.png
- status: animated
- 4:22,1 : Le fil se rompt (2G · 3G), les requêtes s'empilent et se dédoublent.

## Frame 55: L'appli qui mouline (266.73-272.43s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-269.93s.png
- status: animated
- 4:26,7 : Dans le téléphone : roue de chargement, une barre de réseau sur quatre.

## Frame 56: Le push (272.43-283.13s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-281.13s.png
- status: animated
- 4:32,4 : Le schéma pivote de 180°, seul le serveur envoie, en vert.

## Frame 57: RAMEN (283.13-283.93s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-283.53s.png
- status: animated
- 4:43,1 : « RAMEN » en héros.

## Frame 58: Non, pas les nouilles (283.73-286.43s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-285.13s.png
- status: animated
- 4:43,7 : Le vrai bol glisse pendant la pause, slurp, puis un trait rouge le barre.

## Frame 59: Accent anglais ★★☆☆☆ (286.43-287.33s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-286.83s.png
- status: animated
- 4:46,4 : La jauge d'autodérision, 2 étoiles sur 5.

## Frame 60: L'acronyme (287.13-292.23s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-290.13s.png
- status: animated
- 4:47,1 : « Realtime Asynchronous MEssaging Network », initiales en blanc.

## Frame 61: Trois pièces (292.23-299.23s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-298.13s.png
- status: animated
- 4:52,2 : La brigade Uber Eats en retrait : le sorcier Fireball, la cuisine, le livreur, le téléphone.

## Frame 62: Fireball, le gérant (299.23-308.53s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-304.93s.png
- status: animated
- 4:59,2 : Le sorcier à la boule de feu (Fireball) s'allume, trois événements défilent, le point est tamponné « À PRÉVENIR ».

## Frame 63: L'API gateway, la cuisine (308.53-315.33s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-312.73s.png
- status: animated
- 5:08,5 : Le point est emballé dans une boîte.

## Frame 64: Mème : Ichiraku (317.38-318.83s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-317.93s.png
- status: animated
- 5:17,4 : Coupe franche muette : Naruto qui mange chez Ichiraku (extrait Boruto, Crunchyroll).

## Frame 65: Le livreur, 1,5 M (315.33-324.93s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-321.13s.png
- status: animated
- 5:15,3 : Le livreur porte le colis sur un fil toujours ouvert ; « 1,5 M connexions ouvertes en même temps » (chiffre de l'article).

## Frame 66: Au moins une fois (324.93-327.43s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-326.53s.png
- status: animated
- 5:24,9 : ✓ vert sur le téléphone.

## Frame 67: Envoyer ✓ (327.43-334.93s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-331.13s.png
- status: animated
- 5:27,4 : Vue d'ensemble, « Envoyer » au vert, le point arrivé « position GPS ».

## Frame 68: juste ? (334.93-336.23s)
- act: Chapitre 3 · Envoyer
- still: boards/stills/at-335.93s.png
- status: animated
- 5:34,9 : Tout s'éteint, la musique se coupe net : « juste ? » seul dans le silence (relance à 56 %).

## Frame 69: Écran de chapitre 4 (336.23-338.18s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-337.33s.png
- status: animated
- 5:36,2 : « Afficher », étape 3.

## Frame 70: Le GPS se trompe de 50 m (337.73-350.53s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-348.93s.png
- status: animated
- 5:37,7 : Vraie carte du boulevard Diderot : la voiture saute d'un trottoir à l'autre, règle rouge « 50 m ».

## Frame 71: Fast and Furious (350.53-361.53s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-357.53s.png
- status: animated
- 5:50,5 : « position fausse ① » et « ② » ; la voiture traverse la gare et dérape, traces de pneus.

## Frame 72: 180 km/h (361.53-362.98s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-362.03s.png
- status: animated
- 6:01,5 : « 180 km/h » en héros sur le tiers gauche, accent de la musique.

## Frame 73: C'est la famille. (362.98-363.78s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-363.33s.png
- status: animated
- 6:03,0 : Carton blanc sur noir, coupe franche.

## Frame 74: Quatre satellites (363.78-372.53s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-371.73s.png
- status: animated
- 6:03,8 : Rue en 3D : 4 satellites, une ligne et un chrono vers le téléphone du chauffeur.

## Frame 75: Le signal rebondit (372.53-382.68s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-378.73s.png
- status: animated
- 6:12,5 : Au niveau de la rue : signal direct bloqué, rebond rouge en retard, point fantôme sur le mauvais trottoir.

## Frame 76: L'article Rethinking GPS (382.68-388.38s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-384.93s.png
- status: animated
- 6:22,7 : La vraie capture de l'article (19 avril 2018).

## Frame 77: L'ombre des immeubles (388.63-407.53s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-403.73s.png
- status: animated
- 6:28,6 : Plongée : ombres radio au sol, signaux faibles rouges, forts verts, le point se cale en vert.

## Frame 78: Le filtre à particules (407.53-419.11s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-416.91s.png
- status: animated
- 6:47,5 : 2 000 particules, 4 mesures, le nuage se resserre sur la vraie position.

## Frame 79: Pour les devs : Kalman (419.11-434.41s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-433.11s.png
- status: animated
- 6:59,1 : Cloche barrée, carte de chaleur à plusieurs bosses. Bloc autonome, coupable si besoin.

## Frame 80: Les à-coups (434.41-446.87s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-438.11s.png
- status: animated
- 7:14,4 : Sous un pont, la voiture saute de point en point.

## Frame 81: Le coéquipier qui lag (446.87-451.27s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-448.27s.png
- status: animated
- 7:26,9 : Trailer officiel de Monster Hunter Wilds sans le son, faux lag ajouté, badge « 999 ms ».

## Frame 82: Glisser, puis deviner (451.27-464.62s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-462.97s.png
- status: animated
- 7:31,3 : La voiture glisse, continue en pointillés « vitesse + direction », puis se recale.

## Frame 83: Navigation à l'estime (464.62-471.57s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-468.17s.png
- status: animated
- 7:44,6 : Une carte portulan du domaine public, « dead reckoning ».

## Frame 84: Retour à la question du début (471.57-473.57s)
- act: Chapitre 4 · Afficher
- still: boards/stills/at-473.27s.png
- status: animated
- 7:51,6 : Le téléphone de l'accroche revient ; la musique s'arrête.

## Frame 85: Écran de chapitre 5 (473.57-475.47s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-474.57s.png
- status: animated
- 7:53,6 : « Les voitures fantômes ».

## Frame 86: L'enquête de Motherboard (475.22-487.67s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-479.72s.png
- status: animated
- 7:55,2 : La vraie page VICE « Uber's Phantom Cabs » (27 juillet 2015), surlignée.

## Frame 87: Quatre voitures, 17 minutes (487.17-492.97s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-491.72s.png
- status: animated
- 8:07,2 : Carte passager recréée : 4 voitures autour de l'épingle, « 17 min » en rouge.

## Frame 88: « Plutôt un effet visuel » (492.97-496.77s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-496.22s.png
- status: animated
- 8:13,0 : La citation du support en jaune ; les voitures deviennent des fantômes.

## Frame 89: L'économiseur d'écran (496.77-499.88s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-499.08s.png
- status: animated
- 8:16,8 : Façon DVD : la voiture Uber rebondit et touche enfin le coin ; citation corrigée « économiseur d'écran ».

## Frame 90: Fortune : le démenti (499.58-508.78s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-501.68s.png
- status: animated
- 8:19,6 : La vraie page de Fortune (30 juillet 2015), sans les pubs, le démenti surligné ; la pulsation entre sur « Officiellement ».

## Frame 91: Les 8 plus proches (508.78-513.18s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-511.83s.png
- status: animated
- 8:28,8 : 8 voitures autour de l'épingle, d'autres hors du cadre.

## Frame 92: Un décalage de 30 à 60 s (513.08-525.38s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-518.33s.png
- status: animated
- 8:33,1 : Chrono « 30–60 s », rappels du message en retard et de la voiture en pointillés.

## Frame 93: Des fantômes à chaque épingle (525.18-534.68s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-530.18s.png
- status: animated
- 8:45,2 : Trois épingles, des fantômes autour de chacune ; « Cette enquête date de 2015 ».

## Frame 94: Une position d'il y a quelques secondes (534.68-542.28s)
- act: Chapitre 5 · Les voitures fantômes
- still: boards/stills/at-541.53s.png
- status: animated
- 8:54,7 : Dans le téléphone, la voiture affichée devant sa position réelle en gris.

## Frame 95: Écran de chapitre 6 (542.28-544.73s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-543.48s.png
- status: animated
- 9:02,3 : « Le verdict », les trois étapes au vert.

## Frame 96: Récap : 50 m (544.13-552.18s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-550.38s.png
- status: animated
- 9:04,1 : Le trajet récapitulé ; le point sort du téléphone du chauffeur, « ± 50 m » ; le morceau « maison » revient.

## Frame 97: Récap : Fireball et RAMEN (552.18-556.18s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-554.43s.png
- status: animated
- 9:12,2 : « Trouver » au vert, l'hexagone, le sorcier Fireball puis RAMEN.

## Frame 98: Récap : l'appli fait glisser (556.18-560.08s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-558.13s.png
- status: animated
- 9:16,2 : « Afficher » s'allume, la voiture glisse jusqu'à « toi ».

## Frame 99: Un geste de deux secondes (560.08-564.38s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-562.88s.png
- status: animated
- 9:20,1 : Ton téléphone grandit, sa carte s'allume, chrono 0 → 2 s.

## Frame 100: Flutter contre Uber (564.38-572.98s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-569.18s.png
- status: animated
- 9:24,4 : La maquette Flutter générique à gauche, la carte recréée d'Uber à droite.

## Frame 101: Des millions en même temps (572.98-577.78s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-574.43s.png
- status: animated
- 9:33,0 : La carte d'Uber se remplit de milliers de points.

## Frame 102: C'est des génies (577.78-579.48s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-578.53s.png
- status: animated
- 9:37,8 : Le dernier palier du galaxy brain, tenu dans la pause.

## Frame 103: Écran de fin (579.48-588.98s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-584.43s.png
- status: animated
- 9:39,5 : Cadre « Vidéo suivante » (élément YouTube ArtCraft) et « S'abonner » qui s'allume sur le mot.

## Frame 104: Écran de fin tenu (588.98-599.58s)
- act: Chapitre 6 · Le verdict
- still: boards/stills/at-594.93s.png
- status: animated
- 9:49,0 : Le même écran, presque immobile, environ 14 s de musique après la voix.
