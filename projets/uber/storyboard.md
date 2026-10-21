# Storyboard : Uber

> **Voix off montée** : [`voix-off-montee.wav`](voix-off-montee.wav). Elle dure **9 min 40 s** (48 kHz, 24 bits, mono). Elle est masterisée avec la chaîne de la recette Premium noir : **-16 LUFS, crête à -2 dBFS**. Elle est tirée de `uber_voix_off.m4a` (25 min 01 s de prises) et compte 119 morceaux.
> Script d'origine : [`script.md`](script.md). Téléprompteur : [`teleprompteur.md`](teleprompteur.md). Fiche : [`fiche.md`](fiche.md).
>
> Les timecodes (TC) de ce document sont ceux de `voix-off-montee.wav`, posé à 0:00. En HyperFrames, `data-start` = le TC en secondes. Si tu insères un mème avec son propre son, la suite se décale d'autant (recette, brique « pub »).
>
> **Durée finale estimée** : 9:40 de voix, environ 15 s de pauses et de mèmes sonores, puis 20 s d'écran de fin, soit **environ 10 min 15 s**.

## Comment la voix off a été montée

- **Les prises** : 25 min 01 s de rushes deviennent 9 min 40 s de voix. Pour chaque phrase, je garde la dernière prise complète, sauf quand une prise plus ancienne est meilleure.
- **Ce qui est retiré** :
  - les « Yeah », « Okay », « What », « Uh » entre les prises ;
  - les faux départs : « Sur ces trajets… », « C'est comme chercher… », « L'astuce… », « Ta case à quatre carrés voisines… », « Donc la case d'à côté, ça peut vouloir… », « Ajoutez un anneau autour. » ;
  - les doublons :
    - « Non, pas les nouilles, mais excusez-moi… » (trois fois) ;
    - « Officiellement, Uber dé… » ;
    - « Sur les forums » (trois fois) ;
    - « Ce décalage, tu sais maintenant d'où il peut venir » (cinq fois) ;
    - « En 2018, des ingénieurs ont… » ;
    - « en plein, en plein » ;
    - « Le téléphone… le téléphone » ;
    - « avec le temps… avec le temps ».
- **La redite du début** : « Là, on va se mettre dans la peau de quelqu'un » faisait doublon avec « On se met dans la peau d'un chauffeur » quelques secondes plus loin. Je l'ai coupée.
- **Les blancs** :
  - dans une phrase, tout silence de plus de 0,45 s est ramené à 0,3 s ;
  - entre deux phrases d'une même idée, je laisse 0,15 à 0,4 s ;
  - en fin de partie, 0,6 à 1 s ;
  - les respirations sont gardées.
- **Les pauses longues sont à poser au montage**, comme tu l'as demandé. Elles sont listées juste en dessous.

### Tes improvisations, gardées

- « C'est comme chercher **Mewtwo en 2016** dans Pokémon Go » (1:29.0) : elle remplace le stade du script, et je la garde. Voir la note dans les erreurs.
- « Sept cases, ça suffit pour trouver **notre dresseur rare ou notre Pokémon shiny** » (2:38.4) : la suite de la même vanne.
- « Mais **excusez-moi pour mon accent anglais** » (4:36.6).
- « Le serveur RAMEN, **bien sûr pas celui d'Ichiraku** » (5:06.4).
- « C'est quand qu'on arrive ? » ×3 (3:44.5) : la 2e prise. Elle sonne plus naturelle que « On est arrivés ? ».
- « Alors **en vrai**, mon pote, il avait raison » (9:17.5).

### Pauses à poser au montage 🟫

| TC | Où | Proposition |
|---|---|---|
| 0:25.1 | après « existent vraiment ? » | 1 s, musique coupée (0,8 s sont déjà dans la voix) |
| 1:33.0 | après « Pokémon Go » | le temps du mème (2 s) |
| 1:48.4 | après « Tu vois le défaut ? » | **2 s de devinette**, musique coupée |
| 3:31.6 | après « ne passera jamais » | 0,5 s pour la voiture à bouée |
| 3:49.6 | après le 3e « C'est quand qu'on arrive ? » | le temps du mème de l'âne (2 s, avec son son) |
| 4:35.2 | entre « un RAMEN. » et « Non, pas les nouilles » | **0,6 s** pour le slurp et le bol |
| 5:26.6 | après « …elle était juste. » | **1 s de silence total**, c'est la relance (0,9 s sont déjà dans la voix) |
| 5:52.1 | après « 180 à l'heure » | 0,8 s pour le carton « C'est la famille. » |
| 9:33.9 | après « c'est des génies » | 0,8 s avant le mot de fin |

## Erreurs relevées dans l'enregistrement

| TC | Passage enregistré | Problème | Ce que j'ai fait |
|---|---|---|---|
| (hook) | « Une grille qui peut descendre jusqu'à **500 milliards** de cases » | Le niveau le plus fin de H3 compte **569 707 381 193 162** cellules, soit 570 000 milliards : ton chiffre est mille fois trop petit | **Coupé**. Le hook enchaîne sans trou, et le compteur exact s'affiche sur le globe (#2). Ligne à réenregistrer : voir plus bas |
| (3:06) | « Il en faut près de **570 milliards** pour couvrir la Terre » | Même erreur : c'est 570 000 milliards | **Coupé**. Le compteur exact s'affiche sans voix (#25) |
| (5:18) | « En 2020, ça tenait plus d'un million et demi de **requêtes** ouvertes » | La source parle de plus de 1,5 M de **connexions** ouvertes en même temps, pas de requêtes | **Coupé**. Le chiffre juste est affiché à l'écran (#38) |
| (0:59) | « **Toutes les secondes**, son téléphone envoie sa position » | Uber ne publie aucune fréquence, d'où le « toutes les quelques secondes » du script | **Coupé** proprement. La phrase devient « On se met dans la peau d'un chauffeur de Paris : son téléphone envoie sa position… » |
| 1:29.0 | « Chercher Mewtwo **en 2016** dans Pokémon Go » | Mewtwo n'est arrivé dans le jeu qu'en **août 2017** ([Bulbanews](https://bulbanews.bulbagarden.net/wiki/Mewtwo_to_be_available_in_Pok%C3%A9mon_GO_via_Exclusive_Raid_Battles)) | **Gardé** : c'est une blague, et elle marche encore mieux. Le carton « Spoiler : Mewtwo n'est arrivé qu'en août 2017 » en fait une double vanne (#14) |
| 5:39.9 | « Si l'appli faisait glisser les voitures **d'une position à l'autre** » | Il manque « fausse ». Or, à 7:31, glisser d'une position à l'autre, c'est justement **la solution**. Sans « fausse », les deux passages se contredisent | **Gardé**, et **corrigé à l'écran** : les deux points portent l'étiquette « position fausse » (#41). Réenregistrement possible, voir plus bas |
| 5:23.4 | « Je fais comme si **cette méthode**, elle était juste » | Le script disait « comme si **elle** [la position] était juste ». Avec « cette méthode », le « elle » de la phrase suivante (« elle peut être fausse de 50 mètres ») devient flou | Gardé. L'écran lève le doute : « position GPS » sur le point, puis « juste ? » (#39) |
| 8:09.3 | « Un **économisateur** d'écran » | Le mot est « économiseur ». Les deux modèles de transcription entendent « économisateur » | Gardé. La citation affichée en jaune écrit « économiseur d'écran » (#53) |
| 9:34.7 | « Si **vous** avez aimé cette vidéo, n'hésitez pas à **vous** abonner… » | Tout le reste de la vidéo tutoie | Gardé. Réenregistrement possible en « tu » |
| 9:17.5 | « Je l'ai fait moi-même dans mes applications » | « Flutter » est tombé. Ce n'est pas une erreur | L'écran le remet : le logo Flutter sur la maquette du #8, reprise au #59 |

**Pas enregistré** (le storyboard compense) :
- les trois lignes de Python sur H3 : le passage pratique saute, mais tu peux mettre le snippet en commentaire épinglé ;
- « Laquelle tu veux que j'ouvre ensuite ? Dis-le en commentaire » : à **épingler en commentaire** ;
- le renvoi vers la vidéo ArtCraft : c'est l'écran de fin qui le fait (#60) ;
- le prénom **Karim** : tu dis « le chauffeur » et « notre chauffeur ». À l'écran, on écrit donc « chauffeur », pas « Karim ».

### 🎙️ À réenregistrer si tu veux (5 min, même micro, même distance)

1. « Une grille qui peut descendre jusqu'à cinq cent soixante-dix mille milliards de cases. » À insérer à **0:07.1**, après « en hexagones ». C'est la seule qui manque vraiment au hook.
2. « Si l'appli faisait glisser la voiture d'une position fausse à l'autre, » À mettre à la place du début de #41 (5:39.9 – 5:42.6).
3. *(facultatif)* « Mieux vaudrait voir ça comme un économiseur d'écran. »
4. *(facultatif)* « Si t'as aimé cette vidéo, abonne-toi, laisse un like et un commentaire. Allez, salut ! »
5. *(facultatif)* « Laquelle tu veux que j'ouvre ensuite ? Dis-le en commentaire. »

Envoie-les-moi : je les insère et je recale les TC.

### 🟨 Collures à vérifier à l'oreille

Ces collures sont validées par retranscription, pas par écoute :
- 1:03.6 : « …chauffeur de Paris : son téléphone » (« toutes les secondes » est retiré juste avant) ;
- 6:11.3 : « En 2018 » (le premier essai est coupé) ;
- 7:23.4 : « plus loin… en plein dans les pattes » (coupé au milieu d'un bégaiement) ;
- 4:50.5 : « Fireball, c'est le **gérant** » (Whisper entend « géant ») ;
- 8:05.7 : « Le support d'Uber **lui répond que** » (dit très vite).

## Rythme et rétention

| Repère | TC | Part de la vidéo |
|---|---|---|
| Fin du hook | 0:25 | 4 % |
| Bascule des carrés aux hexagones | 2:05 | 22 % |
| Appel à l'abonnement | 2:30 | 26 % |
| Gag du RAMEN | 4:35 | 47 % |
| **Relance (« …elle était juste »)** | 5:26 | 56 % |
| Fast and Furious | 5:40 | 59 % |
| Voitures fantômes | 7:48 | 81 % |
| Verdict sur le pote | 9:17 | 96 % |
| Fin de la voix | 9:40 | 100 % |

Le passage le plus fragile va de **5:52 à 7:06** : une minute de GPS, puis Kalman. La parade, c'est la scène 3D de la rue filmée sous trois angles (ANI-08) et un changement de plan toutes les 4 à 6 s. Si ça traîne encore, coupe la parenthèse Kalman (#47, 16,7 s).


## Fiche d'identité

| Axe | Position |
|---|---|
| Cible | Curieux de tech de 18 à 30 ans, débutants à intermédiaires, avec quelques devs |
| But | Théorique : comprendre ce qui se cache derrière une carte qu'on regarde tous les jours |
| Ambiance | Éducatif d'abord, une keynote calme, ponctuée de mèmes courts qui portent ton humour |
| Complexité | Plutôt élevée (H3, polling contre push, GPS en ville, filtre à particules). Ce sont les schémas qui portent cette complexité : **une idée par plan** |
| Outil | HyperFrames, recette « Premium noir » en 16:9 ([`RECETTE-premium.md`](/Users/innocent/.hyperframes-studio/Short%20premium/assets/recette/RECETTE-premium.md)) |

## Le récit (voyage du héros)

Le héros, c'est **la position du chauffeur** : un petit point blanc qu'on suit d'un bout à l'autre, du téléphone du chauffeur jusqu'au tien. Toi, tu joues le guide.

| Étape | Passage | Statut |
|---|---|---|
| Statu quo | « Ouvre Uber. Tu vois ces petites voitures ? » | ✅ présente |
| Appel | Ton pote et l'article sur le polling ; « est-ce que toutes ces voitures existent vraiment ? » | ✅ présente (deux boucles ouvertes) |
| Mentor | Les ingénieurs d'Uber, à travers leur blog | ✅ présente |
| Épreuves | Trouver (hexagones), envoyer (polling, puis RAMEN), afficher (GPS) | ✅ présente : c'est le cœur de la vidéo |
| Crise | « Je fais comme si elle était juste », puis « 50 mètres » | ✅ présente, à 55 % de la vidéo |
| Trésor | L'ombre des immeubles, le filtre à particules, la voiture qu'on fait glisser | ✅ présente |
| Retour | Les voitures fantômes de 2015, expliquées avec ce qu'on vient d'apprendre | ✅ présente |
| Résolution | Le récap, puis « mon pote avait raison » | ✅ présente |

## Direction artistique : mes propositions au monteur

Il connaît le style, donc ce sont des propositions. Ce qui suit vient de la recette Premium noir, adaptée au sujet.

1. **Le décor raconte l'histoire.**
   - Le fond est noir pur, avec une grille fine de **carrés**. Proposition de réglage : traits de 1 px en `#3a3a3c` à 35 %, pas de 96 px, fondue vers les bords par un masque radial.
   - Sur « lui, il a six voisins », toute la grille du fond se change en **hexagones**, et elle le reste jusqu'à la fin.
   - Le spectateur vit donc dans H3 sans qu'on le lui dise. C'est la proposition la plus forte, et elle ne coûte qu'un composant.
2. **Un seul héros à l'écran : le point.**
   - C'est la position du chauffeur : un point blanc de 20 px avec un anneau fin.
   - Les transitions naissent de lui :
     - il quitte le téléphone ;
     - il tombe dans un hexagone ;
     - il entre dans le tuyau RAMEN ;
     - il ressort sur ton écran.
   - Cela donne très peu de coupes franches.
3. **Trois couleurs qui ont un sens.** Jamais plus de deux accents par plan.
   - Rouge `#ff453a` : **l'erreur et le gâchis** (les calculs inutiles, les 80 % de polling, les 50 m d'erreur, les voitures fantômes).
   - Vert `#30d158` : **la bonne réponse** (les cases voisines, le push, la vraie position).
   - Jaune `#ffd60a` : **les voix extérieures** (l'article du pote, l'e-mail du support, le démenti d'Uber).
4. **La carte du trajet** : une barre de trois étapes, Trouver · Envoyer · Afficher, posée sur la grille.
   - Elle revient au début de chaque acte, et l'étape en cours s'allume.
   - C'est le repère du spectateur, et le chapitrage YouTube suit les mêmes actes.
5. **Cinq passages en 3D, et pas plus.**
   - ① Le dézoom du hook : du téléphone jusqu'à la Terre couverte d'hexagones.
   - ② Le globe et ses 12 pentagones dans l'océan.
   - ③ La rue entre deux tours, quand le signal rebondit.
   - ④ La même rue vue de haut, avec les « ombres radio ».
   - ⑤ La même rue, avec le nuage de particules.
   - Les passages ③ à ⑤ forment **une seule scène 3D** filmée sous trois angles, donc un seul décor à construire.
   - Pour l'outil : Three.js dans HyperFrames, ou à défaut de la 3D en CSS (`perspective`).
6. **La caméra** : une seule caméra virtuelle qui glisse sur la grille.
   - Pendant les explications, poussées lentes `sine.inOut` de 3 à 6 s.
   - D'un état à l'autre, `power3.inOut` en 0,7 s.
   - Le point d'attention reste au **centre** pour le point et sur le **tiers gauche** pour les chiffres. Un chiffre réapparaît donc toujours au même endroit.
7. **Typographie** : SF Pro, et SF Mono pour tout ce que « la machine calcule » : compteurs, 41 %, 80 %, 50 m, 180 km/h, coordonnées GPS.
8. **Les mèmes coupent franchement**, comme la brique `pub-leboeuf.html`.
   - Plein écran pendant 1 à 2 s, avec leur son d'origine.
   - La musique se tait pendant le mème, puis tout reprend.
   - C'est la seule exception au « pas de coupe franche ».

### Les mèmes

| Où | Mème | Pourquoi | Risque |
|---|---|---|---|
| Ton pote, « c'est des génies » | « Galaxy brain » (le cerveau qui s'illumine par paliers) | Il pose la promesse en 1 s | Faible (image libre de droits ou recréée) |
| « chercher Mewtwo en 2016 dans Pokémon Go » | La ruée de joueurs de Pokémon Go à Central Park (été 2016), puis un carton « Mewtwo n'est arrivé qu'en août 2017 » | Ta vanne devient double : en 2016, tu pouvais chercher longtemps | ⚠️ extrait de reportage : 2 s maximum |
| « 41 % plus loin » | « Math lady » (la dame entourée d'équations) | La géométrie fait peur, le mème désamorce | Faible |
| « fois 1,8 un samedi à deux heures du mat » | « Not stonks » (côté passager) | Tout le monde a vécu ce tarif | Faible |
| « où aucun Uber ne passera jamais » | Une voiture Uber avec une bouée, qui flotte au milieu de l'océan (motion design maison) | La chute de l'acte | Aucun |
| « c'est quand qu'on arrive ? » | L'âne de *Shrek 2*, « Are we there yet? » | Le mème parfait du polling | ⚠️ extrait de film : 2 s, son d'origine |
| « Non, pas les nouilles » | **Ton idée : un bol de ramen fumant** qui glisse dans le cadre, puis un trait rouge le barre | Ta blague, littéralement | Aucun (photo libre de droits, ou bol en motion design) |
| « excusez-moi pour mon accent anglais » | Une jauge « Accent anglais » qui plafonne à 2 étoiles sur 5 | L'autodérision | Aucun |
| « pas ceux d'Ichiraku » | Naruto qui dévore un bol chez Ichiraku | Ton clin d'œil, 18-30 ans le reconnaissent tout de suite | ⚠️ extrait d'anime : 1,5 s. Sinon, la lanterne rouge « 一楽 » recréée |
| Fast and Furious | Un dérapage en motion design, puis un carton « C'est la famille. » en blanc sur noir | Le gag sans une seule image du film | Aucun (pas d'extrait, pas de musique, pas de logo) |
| « coéquipier qui lag sur Monster Hunter » | 2 s d'un **trailer officiel** où le Rathalos apparaît (*Monster Hunter Wilds*), avec un **faux lag ajouté au montage** : image figée, saut, chasseur « téléporté », badge rouge « 999 ms » | Ton univers ; le lag rend l'extrait drôle | ⚠️ extrait de trailer : 2 s, **sans le son** |
| « un économiseur d'écran » | Le logo DVD qui rebondit, **remplacé par une voiture Uber** qui rebondit dans les coins de l'écran | Le mème le plus parlant de la vidéo, recréé de zéro | Aucun |
| « c'est des génies » (fin) | Le galaxy brain du début revient, cette fois au dernier palier | La boucle est bouclée | Faible |

Il y a 14 mèmes en 10 min (la silhouette de Pokémon shiny du #23 comprise), soit environ un par minute. Il n'en faut pas plus : la vidéo reste une keynote. Si le monteur doit en retirer, il commence par « Stonks » et la jauge d'accent.

> ⚠️ **Content ID** : les quatre extraits (*Shrek 2*, Naruto, Central Park, Monster Hunter) peuvent être repérés. Garde-les courts (2 s au plus) et commentés par ta voix. Prévois la version recréée de chacun au cas où YouTube bloque.

## Musique

| Acte | TC | Ambiance | Coupes |
|---|---|---|---|
| Hook | 0:00 – 0:25 | Nappe tendue et lente | **Drop sur « hexagones » (0:06.2)** au moment du dézoom ; coupe sèche après « existent vraiment ? » (0:25.1) |
| Mon pote | 0:25 – 1:10 | Morceau « maison », minimal et curieux (type *Future Minimal*, kissan4) | Baisse sous « je te dirai si mon pote avait raison » |
| Trouver | 1:10 – 2:30 | Même morceau, plus présent | Coupée pendant le mème Pokémon (1:33) puis pendant la devinette (1:48.4), le temps que le monteur laisse au spectateur ; elle repart sur le « clac » de la grille hexagonale (2:05.6) |
| Abonnement | 2:30 – 2:38 | Même morceau, baissé | — |
| Prix et grille | 2:38 – 3:40 | Même morceau | Remonte sur le globe aux pentagones (3:06) |
| Envoyer | 3:40 – 5:27 | Plus rythmé, électronique et ludique | Se tait pendant l'âne de *Shrek* (3:49.6) et le slurp (4:35.2) |
| **Relance à 56 %** | 5:26.6 | **Coupure nette** sur « …elle était juste » | 1 s de silence total (pause posée au montage) |
| Afficher | 5:27 – 7:48 | Électronique, plus technique, sur une pulsation | Accent sur « 180 à l'heure » (5:51.0) ; s'arrête après « la question du début » (7:47) |
| Voitures fantômes | 7:48 – 8:58 | Nappe sombre (type *Dark Ambient for Crime and Tension*, megalix) | La pulsation entre sur « Officiellement » (8:15.2) |
| Fin | 8:59 – fin | Retour du morceau maison sur un premier temps, à « on récapitule » | **Garder environ 15 s de musique après la voix** pour l'écran de fin |

Volumes (recette) : musique à -19 dB sous la voix, -17 dB pour la nappe sombre, -15 dB sur un temps fort.

## Bruitages

Ce sont ceux de la recette (`assets/sfx/`), à 0 à 2 par plan, entre -20 et -24 dB :
- `air` pour une entrée ou un mouvement de caméra ;
- `slide` pour une carte qui glisse ;
- `tick` pour un surlignage ou un compteur ;
- `bubble` pour une notification ;
- `dissolve` pour un effacement.

Ce que le sujet ajoute, puisque tu as demandé des mèmes (la recette ne les autorise que sur demande) :
- un crissement de pneus (dérapage) ;
- un « slurp » de nouilles (ramen) ;
- un « clac » quand la grille d'hexagones se met en place ;
- un ping sonar (le polling) ;
- un bip satellite (GPS).

## Légende

🟦 VID vidéo, B-roll · 🟩 IMG image · 🟪 ECR capture d'écran · 🟧 ANI animation · ⬜ TXT texte sur fond noir · 🩷 MEM mème, blague visuelle · 🟫 pause à poser · 🟥 élément à collecter · 🟨 à vérifier à l'oreille · ⚠️ risque Content ID

**Règles fixes** :
- pas de vraie interface Uber : la carte côté passager est toujours recréée en motion design (`strategie.md`, partie juridique) ;
- le blog Uber Engineering, la doc H3 et les articles de presse sont de vraies captures ;
- chaque chiffre affiché porte sa source en micro (24 px, gris).

---

## HOOK (0:00 – 0:25)

| # | TC | Voix off (telle que dite) | Visuel | Texte · Son |
|---|---|---|---|---|
| 1 | 0:00.0 | « Ouvre Uber. Tu vois ces petites voitures autour de toi ? » | 🟧 **ANI-01**, début : téléphone en contre-plongée (brique `abonnement.html` : départ sur le bas du téléphone, montée jusqu'au téléphone entier). Carte sombre, 5 voitures blanches qui glissent autour de ton point. Pas de titre ni de logo | Grille carrée du fond déjà là. Karaoké incrusté permis sur l'accroche (recette § 4). `air` sur la montée |
| 2 | 0:03.5 | « Pour te trouver un chauffeur, Uber a découpé la planète en hexagones. » | 🟧 **ANI-01** en 3D : dézoom de la rue vers Paris, la France, puis la Terre couverte de vrais hexagones H3 | **Drop de la musique sur « hexagones » (0:06.2)**. Un `tick` par palier. ⬜ compteur SF Mono « 569 707 381 193 162 cases » sous le globe, sans voix. 🎙️ ligne à insérer ici si tu la réenregistres |
| 3 | 0:07.4 | « Aujourd'hui, on suit une de ces petites voitures, du téléphone d'un chauffeur jusqu'au tien. » | 🟧 la caméra replonge sur Paris. Une voiture s'allume, et **le point blanc** (le héros) quitte son toit | Libellés intégrés « chauffeur » → « toi » |
| 4 | 0:12.1 | « Sur ce trajet, sa position passe par un serveur bombardé de questions, et par un GPS qui se trompe de 50 mètres. » | 🟧 deux vignettes éclair : un serveur bombardé de bulles « ? » (0:14.4), puis le point qui saute de 50 m (0:16.6). 🩷 **teaser de 0,8 s du dérapage** (ANI-07) sur « 50 mètres » (0:17.7), puis arrêt sur image | Crissement de pneus coupé net |
| 5 | 0:18.9 | « Et en 2015, deux chercheurs ont posé une question gênante. Est-ce que toutes ces voitures existent vraiment ? » | 🟧 retour au téléphone : une voiture devient translucide, clignote, disparaît (ANI-10 en version courte) | ⬜ « 2015 » en SF Mono. Musique coupée sèche après « vraiment ? » 🟫 |

## MON POTE ET SES BLOGS (0:25 – 1:10)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 6 | 0:25.9 | « J'ai un pote qui lit les blogs tech des grosses boîtes, pour voir comment elles construisent des produits utilisés par des millions de personnes. Un jour, il m'envoie un article d'Uber, sur un truc qu'on appelle le polling. » | 🟪 défilement lent du blog Uber Engineering (brique « Preuve par capture »), puis la carte de l'article *Uber's Real-Time Push Platform* (18 déc. 2020). « polling » se surligne **en jaune** quand tu le dis (0:35.9) | Musique « maison » qui entre. `slide` sur la carte, `tick` sur le surlignage |
| 7 | 0:37.1 | « Pour lui, les ingés d'Uber, c'est des génies. » | 🩷 **Galaxy brain**, paliers 1 à 3. On garde le 4e pour la fin (#59) | Petit « ding » par palier |
| 8 | 0:40.1 | « Pour moi, des cartes avec des éléments dessus, j'en ai affiché dans mes applications Flutter, mais jamais avec des millions de personnes en même temps, et en temps réel. Alors j'ai lu son article, puis les autres. » | 🟧 **une maquette générique**, et non ton appli : tes applis Flutter sont du travail, donc rien de réel n'est montré. Elle est faite en motion design : un téléphone, une carte simple avec quelques rues, 3 ou 4 marqueurs, et le logo Flutter dans un coin. Sur « des millions de personnes », les marqueurs se multiplient par milliers (recul). Sur « puis les autres », les autres articles du blog s'empilent en éventail, dates nettes et reste flou | ⬜ micro « Toutes les sources en description » |
| 9 | 0:50.6 | « À la fin, je te dirai si mon pote avait raison ou pas. » | ⬜ texte central « Mon pote avait raison ? », puis fondu | La musique baisse |
| 10 | 0:54.1 | « Donc, Uber, c'est plus de 40 millions de courses et de livraisons par jour. » | ⬜ chiffre héros SF Mono qui compte jusqu'à « 40 000 000 / jour », sur le **tiers gauche** (tous les compteurs reviendront à cet endroit) | Micro « Source : Uber, résultats du T2 2026 (3 867 M au trimestre) ». `tick` |
| 11 | 0:59.0 | « On va prendre une seule course. On se met dans la peau d'un chauffeur de Paris : son téléphone envoie sa position, et elle doit arriver sur ton écran, deux rues plus loin. Suivons cette position. » | 🟧 sur la grille : une voiture près de la gare de Lyon, ton téléphone deux rues plus loin, et le point blanc qui part de chez le chauffeur. Sur « Suivons », **la carte du trajet** se dessine : Trouver · Envoyer · Afficher | 🟨 collure à 1:03.6. `air` |

## ÉTAPE 1 : TROUVER (1:10 – 2:30)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 12 | 1:10.4 | « Uber reçoit les positions de millions de chauffeurs. Toi, tu en veux une poignée : ceux qui sont autour de toi. » | 🟧 la carte du trajet, « Trouver » s'allume. Recul : 300 voitures sur la grille carrée, et toi au centre (un anneau blanc) | Ding de chapitre |
| 13 | 1:16.4 | « La solution naïve, c'est de calculer la distance entre toi et chaque chauffeur. Ce qui fait qu'un million de chauffeurs, ça donne un million de calculs pour une seule personne. Et des gens qui ouvrent l'appli Uber au même moment, il y en a des millions. » | 🟧 **ANI-02** : 300 traits rouges, compteur « 1 000 000 » qui s'emballe et rougit (tiers gauche). Sur « des millions », l'écran se démultiplie en mosaïque de téléphones (×4, ×16, ×64) | `tick` de plus en plus serrés |
| 14 | 1:29.0 | « C'est comme chercher Mewtwo en 2016 dans Pokémon Go. » | 🩷 2 s : la ruée de joueurs de Pokémon Go à Central Park (été 2016) ⚠️. Puis le carton ⬜ « Spoiler : Mewtwo n'est arrivé dans le jeu qu'en août 2017 » | Musique coupée pendant le mème. 🟫 |
| 15 | 1:33.5 | « L'astuce, c'est de ranger. On découpe la carte en cases, et chaque chauffeur va dans la sienne. Quand tu ouvres l'appli, Uber regarde ta case et celles d'à côté. » | 🟧 **ANI-02**, fin : les traits s'effacent, les voitures glissent dans leurs cases carrées. Ta case s'allume, puis ses 8 voisines | `dissolve`, puis `slide` |
| 16 | 1:43.8 | « Le réflexe, c'est de prendre des carrés. Regarde la grille deux secondes. Tu vois le défaut ? » | 🟧 **ANI-03**, état initial : grille carrée, case centrale allumée, **aucune flèche**. Poussée lente (`sine.inOut`) | 🟫 **2 s de devinette** après « défaut ? » (1:48.4) : musique coupée, tic-tac discret |
| 17 | 1:49.0 | « Ta case a quatre voisines collées par un côté, et quatre collées par un coin. Celles du coin sont 41 % plus loin. Donc la case d'à côté, ça peut vouloir dire tout près… ou nettement plus loin. » | 🟧 **ANI-03** : 4 flèches vertes (1:52.3), 4 flèches rouges en diagonale (1:54.3), « 1,41 » en pop (1:56.8). 🩷 **Math lady** 1 s sur « 41 % » | Pop |
| 18 | 2:02.9 | « Par contre, si on prend l'hexagone, lui, il a six voisins. Tous ses voisins sont à la même distance. » | 🟧 **ANI-03, la bascule** : toute la grille du fond devient hexagonale sur « six » (2:05.6), et le restera jusqu'à la fin. 6 flèches vertes identiques | **« Clac »** quand la grille se fige, et la musique repart |
| 19 | 2:08.9 | « En 2018, Uber publie sa grille hexagonale en open source. Elle s'appelle H3. » | 🟪 l'article *H3: Uber's Hexagonal Hierarchical Spatial Index* (juin 2018), puis le dépôt GitHub `uber/h3`. ⬜ « H3 » en héros | `slide` |
| 20 | 2:14.0 | « Tu donnes une position GPS à H3, et il te renvoie ton hexagone. Ajoute un anneau autour : sept cases. Deux anneaux : dix-neuf. Les devs appellent ça un k-ring. » | 🟧 **ANI-04**, anneaux : les coordonnées SF Mono « 48.8443, 2.3744 » tombent dans un hexagone. Anneau 1 (7 cases), puis anneau 2 (19 cases) | Micro pour les devs : « kRing → grid_disk dans H3 v4 » |
| 21 | 2:24.0 | « Du coup, au lieu d'un million de chauffeurs, Uber n'en parcourt plus qu'une centaine : ceux de ces dix-neuf cases. » | 🟧 le compteur du #13 revient **au même endroit** et descend de « 1 000 000 » à « ~100 », puis passe au vert | Impact doux sur « centaine » |

## APPEL À L'ABONNEMENT (2:30 – 2:38)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 22 | 2:29.9 | « Si tu aimes comprendre ce qui se cache derrière les applis que tu as dans la poche, alors abonne-toi sur ma chaîne : on les ouvre une par une. » | 🟧 bouton S'abonner en bas à droite (3 s), les hexagones restent à l'écran | `toggle` au clic. Musique baissée |

## ÉTAPE 1 (SUITE) : LE PRIX ET LA GRILLE (2:38 – 3:40)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 23 | 2:38.4 | « Sept cases, ça suffit pour trouver notre dresseur rare ou notre Pokémon shiny. » | 🩷 une silhouette de Pokémon chromatique (des étincelles, pas d'image officielle) au centre de l'anneau de 7 cases. Rappel du #14 | Son d'étincelle. 🟨 « Sept cases » est dit vite |
| 24 | 2:42.8 | « Mais pour fixer un prix, Uber compare, hexagone par hexagone, les demandes de courses et les chauffeurs libres de toute la ville. Le fameux “fois 1,8” un samedi à deux heures du mat' ? C'est ton hexagone qui a décidé. » | 🟧 **ANI-04**, prix : recul sur Paris, carte de chaleur en hexagones. « ×1,8 » en pop sur ton hexagone (2:50.5). 🩷 **« Not stonks »** 1 s sur « C'est ton hexagone qui a décidé » | Horloge SF Mono « sam. 02:00 ». Micro « Source : Uber Engineering, H3, 2018 » |
| 25 | 2:55.1 | « Donc H3 a 16 niveaux de zoom, et à chaque niveau, les hexagones sont sept fois plus petits. Au plus large, un hexagone fait à peu près huit fois la France. Au plus fin, moins d'un mètre carré. » | 🟧 **ANI-04**, seize niveaux : divisions par 7, niveau 0 → 15 à droite. Au niveau 0, la silhouette de la France posée 8 fois dans l'hexagone ; au niveau 15, un hexagone de la taille d'une table basse | ⬜ « 0,9 m² », puis le compteur « 569 707 381 193 162 cases » (**il remplace la phrase coupée**). Micro « Source : h3geo.org » |
| 26 | 3:06.8 | « Enfin, on dit hexagones, mais c'est presque des hexagones. On ne peut pas recouvrir une boule entièrement avec des hexagones : il faut tricher quelque part. Alors H3 cache douze pentagones à chaque niveau. Et pour qu'ils ne tombent pas au milieu d'une ville, la grille est orientée pour les placer tous dans l'océan. » | 🟧 3D ② : le globe tourne, et les **12 pentagones rouges** clignotent, tous en mer | 12 `tick` très bas |
| 27 | 3:26.8 | « Quelque part au milieu de l'eau, il y a douze cases à cinq côtés où aucun Uber ne passera jamais. » | 🩷 la caméra plonge sur un pentagone en plein océan, où **une petite voiture flotte avec une bouée** | Vagues, une mouette. 🟫 0,5 s |
| 28 | 3:32.1 | « Uber sait maintenant quels chauffeurs sont autour de toi. Reste à te les envoyer, en direct. Et ça, pendant des années, Uber l'a mal fait. » | 🟧 retour à la carte du trajet : « Trouver » passe au vert ✓, « Envoyer » clignote. Le point blanc file vers « Envoyer » (transition née de l'action) | Musique qui retombe |

## ÉTAPE 2 : ENVOYER (3:40 – 5:27)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 29 | 3:40.2 | « Parce qu'au début, l'appli Uber se comportait comme un gamin à l'arrière de la voiture. À chaque fois, il demandait : “C'est quand qu'on arrive ? C'est quand qu'on arrive ? C'est quand qu'on arrive ?” » | 🟧 un téléphone sur la banquette arrière (picto). Puis 🩷 **l'âne de *Shrek 2*, « Are we there yet? »**, 2 s avec son son, juste après la 3e question (3:49.6) ⚠️ | Musique plus rythmée qui entre sur « Parce qu'au début ». Coupée pendant le mème |
| 30 | 3:50.0 | « Toutes les quelques secondes, ton téléphone demandait au serveur : “Il y a du nouveau ?” Et la plupart du temps, il répondait non. Ça s'appelle le polling, et c'est de ça que parlait l'article de mon pote. » | 🟧 **ANI-05**, polling : bulles « Du nouveau ? » / « Non. » en rouge. Sur « l'article de mon pote », la carte du #6 revient, « polling » surligné en jaune | Un ping sonar par bulle |
| 31 | 4:00.7 | « Par contre, chaque non coûte de la batterie et du travail pour le serveur. Dans cet article de 2020, Uber donne les chiffres : à un moment, huit requêtes sur dix reçues par la porte d'entrée, c'est-à-dire l'API gateway, étaient du polling. » | 🟧 la batterie qui baisse. Puis ⬜ **« 80 % »** héros en rouge sur le tiers gauche, et une porte « API gateway » où 8 bulles sur 10 sont rouges | Micro « Source : Uber Engineering, 18 déc. 2020 » |
| 32 | 4:14.0 | « Et sur un réseau 2G ou 3G qui coupe, chaque échec relançait des requêtes. Si tu as déjà fixé une appli qui mouline avec une seule barre de réseau, tu vois déjà le tableau. » | 🟧 le trait se coupe, les bulles se dédoublent. Puis un indicateur de chargement qui tourne, avec 1 barre de réseau sur 4 | `bubble` |
| 33 | 4:24.4 | « La solution ? Retourner la conversation. Le téléphone arrête de demander, et c'est le serveur qui prévient quand il y a du nouveau. Cette fois, ça s'appelle du push. Pour ça, Uber a construit un RAMEN. » | 🟧 **ANI-05**, push : le schéma pivote de 180° (4:25.1), et seul le serveur envoie, en vert. « RAMEN » en héros sur 4:34.8 | 🟫 **0,6 s** après « RAMEN. » (4:35.2) |
| 34 | 4:35.4 | « Non, pas les nouilles. Mais excusez-moi pour mon accent anglais : c'est Realtime Asynchronous Messaging Network. Un réseau de messagerie en temps réel. » | 🩷 **ton bol de ramen** fumant glisse dans le cadre pendant la pause, puis un trait rouge le barre sur « Non, pas les nouilles ». 🩷 jauge « Accent anglais ★★☆☆☆ » sur « accent anglais ». ⬜ « **R**ealtime **A**synchronous **ME**ssaging **N**etwork » : les initiales en blanc, le reste en gris | **Slurp** sur le bol |
| 35 | 4:43.4 | « Franchement, je pense qu'ils ont clairement trouvé le nom avant. RAMEN, c'est trois pièces. Pour les comprendre, prends Uber Eats. » | 🟧 les lettres R-A-M-E-N se rangent en haut, et trois silhouettes grises apparaissent (gérant, cuisine, livreur) | — |
| 36 | 4:50.3 | « Fireball, c'est le gérant. Il voit passer chaque événement : un passager commande, un chauffeur accepte, une voiture bouge. Et pour chacun, il décide qui doit être prévenu, et quand. » | 🟧 **ANI-06** : le gérant se dessine, et les trois événements défilent sur sa tablette | 🟨 « gérant » (Whisper entend « géant ») |
| 37 | 4:59.8 | « L'API gateway, c'est la cuisine. Elle prépare la commande : toutes les données dont l'application a besoin, au bon format. » | 🟧 **ANI-06** : la cuisine, le point se fait emballer | — |
| 38 | 5:06.4 | « Et le serveur RAMEN, bien sûr, pas celui d'Ichiraku, c'est le livreur. Il garde une connexion ouverte avec ton téléphone, et livre les messages avec une promesse : chaque message arrive au moins une fois. » | 🩷 **Naruto chez Ichiraku**, 1,5 s sur « Ichiraku » (5:08.4), sans le son ⚠️ (version sans risque : la lanterne rouge « 一楽 » recréée). Puis 🟧 **ANI-06** : le livreur apporte le point, ✓ vert | ⬜ **« +1,5 M de connexions ouvertes en même temps (2020) »** : il remplace la phrase coupée. Micro source |
| 39 | 5:18.7 | « La position de notre chauffeur arrive donc jusqu'à toi en direct, sans vider ta batterie. Mais depuis le début, je fais comme si cette méthode, elle était juste. » | 🟧 la carte du trajet, « Envoyer » ✓. Le point est arrivé, avec l'étiquette « position GPS ». Sur « juste », **tout s'éteint** (brique « Mot choc sur noir ») et ⬜ « juste ? » | **Relance à 56 %** : musique coupée net à 5:26.6, puis 🟫 1 s de silence total |

## ÉTAPE 3 : AFFICHER (5:27 – 7:48)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 40 | 5:27.5 | « En ville, elle peut être fausse de 50 mètres. Ce sont les ingénieurs d'Uber qui le disent, et parfois c'est pire. 50 mètres, c'est l'autre côté du boulevard. Sur ta carte, le chauffeur t'attend devant la gare. En vrai, il est garé en face de toi. » | 🟧 la voiture saute d'un trottoir à l'autre, avec une règle rouge « 50 m » en travers du boulevard. La gare en libellé | Nouveau morceau (électronique, sur une pulsation) sur « En ville ». ⬜ « 50 m » en SF Mono. Micro « Source : Uber Engineering, *Rethinking GPS*, 2018 » |
| 41 | 5:39.9 | « Si l'appli faisait glisser les voitures d'une position à l'autre, le chauffeur arriverait comme dans Fast and Furious, à fond. En dérapage, à travers les immeubles. Un saut de 50 mètres en une seconde, à l'écran, c'est du 180 à l'heure. » | 🟧 **ANI-07** en entier : départ sur « glisser » (5:40.6), dérapage sur « dérapage » (5:46.2), compteur « 180 km/h » sur « 180 » (5:51.0). Puis le carton ⬜ « C'est la famille. » (0,8 s) | ⬜ **les étiquettes « position fausse ① » et « ② »** sur les deux points : elles rendent le « fausse » qui manque à la voix. Crissement, puis moteur. 🟫 0,8 s |
| 42 | 5:52.7 | « Mais alors, pourquoi le GPS se trompe autant ? Le téléphone du chauffeur calcule sa position avec le temps que mettent les signaux des satellites à lui arriver. » | 🟧 début de la 3D ③ : 4 satellites, un trait jusqu'au téléphone pour chacun, et un chrono SF Mono sur chaque trait | Bip satellite |
| 43 | 6:01.0 | « Mais en ville, il y a des immeubles. Un signal tape contre une façade, rebondit, et arrive en retard. Le téléphone croit que le satellite est plus loin qu'en réalité, et il se place au mauvais endroit. » | 🟧 **ANI-08, angle A** : la rue entre les tours, le rebond en rouge, et le point fantôme sur le mauvais trottoir | `air-long` sur l'orbite |
| 44 | 6:11.3 | « En 2018, des ingénieurs d'Uber ont eu une idée tordue : se servir du problème comme d'un indice. » | 🟪 la carte de l'article *Rethinking GPS* (19 avr. 2018) | `slide`. 🟨 collure « En 2018 » |
| 45 | 6:17.2 | « Sur Android, le téléphone connaît la force du signal de chaque satellite. Signal faible ? Il y a sûrement un immeuble entre lui et le satellite. Signal fort ? La voie est libre. On compare ça à une carte 3D de la ville, et on en déduit de quel côté de la rue se trouve le chauffeur. Ils se repèrent grâce à l'ombre des immeubles. » | 🟧 **ANI-08, angle B** : la caméra monte en plongée. Ombres radio au sol, signaux faibles en rouge et forts en vert, et le point qui se cale **en vert** du bon côté | — |
| 46 | 6:36.1 | « Et pour suivre la voiture, ils éparpillent dans les rues des milliers de voitures possibles. À chaque mesure, celles qui collent avec les signaux restent, les autres disparaissent. C'est un filtre à particules, testé à San Francisco. » | 🟧 **ANI-08, angle C** : 2 000 particules, 4 « tics », et le nuage se resserre | Un `tick` par mesure. Libellé « filtre à particules » |
| 47 | 6:49.8 | « Petite parenthèse pour les devs : on lit souvent qu'Uber utilise un filtre de Kalman. Dans cet article, les ingénieurs expliquent pourquoi ils ne l'ont pas pris pour ce problème-là. Kalman suppose une erreur en forme de cloche, avec un seul pic. En ville, la position possible en a plusieurs. » | 🟧 bandeau « Pour les devs ». Une courbe en cloche barrée, puis une carte de chaleur à plusieurs bosses | ✂️ **Coupable au montage** (16,7 s, de 6:49.8 à 7:06.5) |
| 48 | 7:07.2 | « Même juste, la position arrive par à-coups. Le réseau coupe sous un pont, le message arrive en retard. Si l'appli affichait juste la dernière position reçue, la voiture se téléporterait à n'importe quel moment. » | 🟧 **ANI-09**, avant : un pont en picto, et la voiture qui saute de point en point, en saccades | — |
| 49 | 7:18.1 | « Un peu comme un coéquipier qui lag en plein Monster Hunter, et qui réapparaît trois mètres plus loin… en plein dans les pattes du Rathalos. » | 🩷 **2 s d'un trailer officiel de *Monster Hunter Wilds*** où un chasseur affronte le Rathalos ⚠️. Le lag est ajouté au montage : 3 images figées, puis un saut de 3 m du chasseur, un léger glitch et un badge SF Mono rouge « 999 ms ». Le saut tombe sur « réapparaît » (7:21.9) | 🟨 collure à 7:23.4 |
| 50 | 7:25.8 | « Uber n'a pas détaillé comment l'appli anime ses voitures. Mais les jeux vidéo en ligne utilisent un vieux principe : entre deux positions, on fait glisser la voiture. Et si la suivante tarde, on devine où elle devrait être, avec sa dernière vitesse et sa direction. » | 🟧 **ANI-09**, après : la voiture glisse, continue en pointillés, puis se recale | — |
| 51 | 7:39.0 | « C'est la navigation à l'estime, *dead reckoning* en anglais. Les marins faisaient déjà ça avant le GPS. Et ça nous ramène à la question du début. » | 🟩 une carte marine ancienne avec son compas (gravure du domaine public), puis retour au téléphone du hook | 🟫 1 s, et la musique s'arrête |

## LES VOITURES FANTÔMES (7:48 – 8:58)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 52 | 7:48.1 | « En juillet 2015, deux chercheurs, Alex Rosenblat et Luke Stark, publient une enquête sur les chauffeurs Uber. Ils racontent l'histoire d'une chauffeuse qui ouvre l'application côté passager. Sur la carte, quatre voitures juste à côté de son point de départ… et dix-sept minutes d'attente pour la plus proche. » | 🟪 la carte de l'article de Motherboard, *Uber's Phantom Cabs* (juillet 2015). Puis 🟧 **ANI-10** : 4 voitures, et « 17 min » | **Nappe sombre**. ⬜ « 17 min » en rouge |
| 53 | 8:05.7 | « Le support d'Uber lui répond que la carte, c'est “plutôt un effet visuel”. Et même : “mieux vaudrait voir ça comme un économiseur d'écran”. » | 🟧 la citation **en jaune** (voix extérieure), et les voitures qui deviennent translucides. Puis 🩷 **le logo DVD qui rebondit, remplacé par une voiture Uber** qui touche enfin le coin de l'écran | ⬜ la citation affichée dit « économiseur d'écran ». 🟨 « lui répond que » |
| 54 | 8:15.2 | « Officiellement, Uber dément cette histoire. D'après eux, le but, c'est des voitures aussi précises que possible, et la latence peut les décaler. Et l'appli n'afficherait que les huit plus proches : donc en réalité, il y en aurait plutôt plus que ce que tu vois. » | 🟪 l'article de Fortune (30 juil. 2015), avec le démenti surligné en jaune. Puis 🟧 8 voitures autour du point, et d'autres en dehors du cadre | **La pulsation de la nappe entre sur « Officiellement »** |
| 55 | 8:28.6 | « Sur les forums, certains chauffeurs avaient leur explication : un décalage de 30 à 60 secondes. Ce décalage, tu sais maintenant d'où il peut venir. Il vient des messages en retard, et d'une appli qui fait glisser les voitures en les devinant. » | 🟧 un chrono « 30-60 s ». Deux rappels éclair : la bulle en retard (ANI-05), puis la voiture en pointillés (ANI-09) | — |
| 56 | 8:40.5 | « Mais d'autres chauffeurs voyaient des fantômes partout où le passager posait son épingle. Ça, par contre, aucun décalage ne l'explique. Cette enquête date de 2015, et l'appli a beaucoup changé depuis. Mais la voiture qui glisse sur la carte, maintenant, tu sais ce que c'est. » | 🟧 **ANI-10** : l'épingle se pose 3 fois, et des fantômes apparaissent à chaque fois | ⬜ « 2015 » en SF Mono |
| 57 | 8:54.1 | « Au mieux, c'est la position d'un chauffeur il y a quelques secondes, en partie devinée. » | 🟧 retour au téléphone du hook : la voiture se dédouble, avec sa position réelle en gris derrière et la position affichée devant | 🟫 1 s |

## FIN (8:59 – 9:40, puis écran de fin)

| # | TC | Voix off | Visuel | Texte · Son |
|---|---|---|---|---|
| 58 | 8:59.0 | « Bon, on récapitule le trajet. Le téléphone de notre chauffeur envoie une position qui peut être fausse de 50 mètres. Uber la range dans un hexagone. Fireball décide qu'elle mérite de te déranger. RAMEN te la livre, et ton appli la fait glisser pour que tu ne voies jamais les trous. Tout ça pour un geste que tu fais en deux secondes. » | 🟧 la carte du trajet en entier. Le point la parcourt en accéléré, et chaque étape s'allume sur son mot | La musique « maison » revient sur un premier temps, à « on récapitule » |
| 59 | 9:17.5 | « Alors, en vrai, mon pote, il avait raison. Afficher des éléments sur une carte, je l'ai fait moi-même dans mes applications. Tout ce que tu viens de voir, c'est ce qu'il faut en plus quand des millions de personnes regardent en même temps. Donc oui, les ingés d'Uber, c'est des génies. » | 🟧 écran partagé : la maquette Flutter du #8 à gauche (4 marqueurs), la carte recréée d'Uber à droite (des milliers de voitures qui glissent). 🩷 le **dernier palier du Galaxy brain** sur « génies » (9:33.3) | ⬜ « Flutter » en libellé sous la maquette. 🟫 0,8 s |
| 60 | 9:34.7 | « Si vous avez aimé cette vidéo, n'hésitez pas à vous abonner, et à laisser un like et un commentaire. Allez, salut ! » | **Écran de fin** (20 s) : la vidéo ArtCraft à gauche, le bouton S'abonner à droite. **Environ 15 s de musique après la voix** | 🟨 « vous » (voir les erreurs). Commentaire à épingler : « Laquelle j'ouvre ensuite ? » |

---

## Fiches d'animation (HyperFrames, 1920×1080, 60 i/s)

Les temps « t » sont relatifs au début du plan. Les courbes suivent la recette : entrées `power3.out`, sorties `power2.in`, changements d'état `power3.inOut`, dérives lentes `sine.inOut`. Chaque élément arrive 0,03 s avant son mot.

**ANI-00 · Le décor : la grille (toute la vidéo)**
- **Éléments** :
  - un plan de grille en SVG, 3 fois plus grand que l'écran pour que la caméra puisse s'y promener ;
  - traits de 1 px en `#3a3a3c` à 35 %, pas de 96 px ;
  - un masque radial qui fond la grille vers les bords.
- **Deux états** : carrés, puis hexagones de même surface (la bascule est décrite dans ANI-03).
- **Caméra** : un seul conteneur `#camera` déplacé et zoomé. Les autres scènes se posent « sur » la grille, ce qui donne l'impression d'un seul plateau infini.
- **Variante 3D** : la grille couchée en sol (`rotationX: 62`) pour les plans de rue (ANI-08).

**ANI-01 · Le dézoom du hook (3D)**
- **Éléments** :
  - un téléphone posé (brique `abonnement.html`) avec une carte sombre et 5 petites voitures blanches autour d'un point ;
  - la Terre en Three.js (sphère noire, côtes en traits `#3a3a3c`) ;
  - une couche d'hexagones H3 (résolution 2 ou 3, fil blanc à 25 %).
- **Déroulé** :
  - t = 0 : plan serré sur l'écran du téléphone, les voitures glissent ;
  - sur « découpé la planète », la caméra recule en 2,4 s (`power2.inOut`) : la rue, Paris, la France, puis la Terre ;
  - à chaque palier, les hexagones de la couche suivante apparaissent (fondu de 0,2 s) ;
  - sur « hexagones », la Terre entière est quadrillée et tourne lentement (`sine.inOut`).
- **Son** : `air-long` sur le recul, un `tick` par palier, puis le drop de la musique sur « hexagones ».
- **Données** : les vraies cellules H3, générées en Python (`h3.latlng_to_cell` / `h3.cell_to_boundary`) puis exportées en GeoJSON. Elles sont vraies, comme le veut la recette.

**ANI-02 · La recherche naïve, puis les cases (Trouver)**
- **Éléments** :
  - le point bleu (toi) au centre ;
  - 300 voitures blanches dispersées sur la grille carrée ;
  - un compteur en SF Mono, sur le tiers gauche.
- **Déroulé** :
  - sur « calculer la distance », un trait rouge part du point vers chaque voiture : 300 traits en 1,2 s, avec un léger décalage entre eux ;
  - le compteur s'emballe jusqu'à « 1 000 000 » et passe au rouge ;
  - sur « l'astuce, c'est de ranger », tous les traits s'effacent (`dissolve`), et chaque voiture glisse dans sa case (0,6 s, `power3.inOut`) ;
  - la case du point s'allume en blanc à 12 %, puis ses voisines.
- **Point d'attention** : le centre.

**ANI-03 · Carrés contre hexagones (le cœur visuel de la vidéo)**
- **État initial** : grille carrée, case centrale allumée, **aucune flèche** pendant « Regarde la grille deux secondes ».
- **Déroulé** :
  - sur « collées par un côté », 4 flèches vertes de longueur 1 ;
  - sur « par un coin », 4 flèches rouges en diagonale ;
  - sur « 41 % », l'étiquette « 1,41 » sort en pop (70 → 110 → 100 %, 0,12 + 0,08 s) ;
  - sur « six voisins », **toute la grille du fond se change en hexagones**. Chaque carré se déforme vers son hexagone en 0,9 s (`power3.inOut`), avec un léger décalage depuis le centre vers les bords ;
  - 6 flèches vertes identiques partent du centre.
- **Son** : silence pendant la devinette, puis un « clac » quand la grille hexagonale se fige.
- **Technique** : interpoler les 6 sommets de chaque cellule. Un carré, c'est un hexagone dont 2 sommets sont confondus avec leurs voisins, ce qui donne un morphing propre sans plugin.

**ANI-04 · Les anneaux, le prix, les seize niveaux et les pentagones**
- **Anneaux** :
  - sur « Ajoute un anneau », les 7 cases s'allument (centre, puis anneau, en 0,4 s) ;
  - sur « deux anneaux », les 19 cases ;
  - le compteur d'ANI-02 descend de « 1 000 000 » à « ~100 » (tiers gauche, au même endroit qu'avant).
- **Prix** :
  - recul sur tout Paris ;
  - les hexagones se colorent en carte de chaleur (gris, puis orange, puis rouge `#ff453a`) ;
  - « ×1,8 » sort en pop sur l'hexagone du point.
  - Ici, le rouge, c'est « ce qu'on te prend » : il garde son sens.
- **Seize niveaux** :
  - un hexagone géant se divise en 7, puis 7, puis 7, la caméra plongeant à chaque division (0,5 s par niveau, en accélérant) ;
  - à droite, le numéro du niveau en SF Mono, de 0 à 15 ;
  - en bas, le compteur « 569 707 381 193 162 cases ».
- **Pentagones** :
  - retour au globe d'ANI-01 ;
  - 12 pentagones rouges clignotent, tous en mer ;
  - la caméra finit sur l'un d'eux, au milieu de l'eau, où arrive le mème de la voiture à bouée.

**ANI-05 · Polling contre push (Envoyer)**
- **Polling** :
  - le téléphone à gauche, le serveur à droite ;
  - toutes les 0,6 s, une bulle « Du nouveau ? » part du téléphone et un « Non. » rouge revient ;
  - la cadence accélère, la batterie du téléphone descend ;
  - sur « 80 % », le chiffre héros (280 px, rouge) sur le tiers gauche.
- **2G / 3G** : le trait entre les deux se coupe, et les bulles s'empilent et se dédoublent (les relances).
- **Push** : sur « Retourner la conversation », tout le schéma pivote de 180° en 0,8 s (`power3.inOut`). Le téléphone se tait, et seul le serveur envoie, en vert, quand il y a du nouveau.

**ANI-06 · RAMEN, la brigade Uber Eats**
- **Éléments** : trois personnages en traits (pictos de la recette, traits constants et bouts ronds), alignés de gauche à droite :
  - le gérant **Fireball** (une tablette à la main) ;
  - la cuisine **API gateway** (une casserole) ;
  - le livreur **serveur RAMEN** (un vélo) ;
  - puis le téléphone.
- **Déroulé** :
  - chaque personnage se dessine sur son nom (`stroke-dashoffset`, 0,5 s) ;
  - le point blanc (la position) passe de l'un à l'autre : le gérant le tamponne « à prévenir », la cuisine l'emballe, le livreur l'apporte ;
  - sur « au moins une fois », un petit « ✓ » vert sur le téléphone.
- **Texte** : un nom sous chaque personnage en libellé gris (32 px), et le rôle en blanc (44 px).

**ANI-07 · Le dérapage Fast and Furious**
- **Éléments** :
  - la carte de quartier (grille hexagonale du fond, plus des rues en traits blancs) ;
  - la voiture du chauffeur ;
  - deux positions GPS fausses, à 50 m l'une de l'autre, de part et d'autre d'un pâté d'immeubles.
- **Déroulé** :
  - sur « faisait glisser », la voiture part en ligne droite vers la position suivante, **à travers l'immeuble** ;
  - elle dérape (rotation de 35° puis contre-braquage), avec des traces de pneus en traits noirs sur la carte et un léger flou de bougé ;
  - sur « 180 à l'heure », le compteur SF Mono « 180 km/h » sort en pop sur le tiers gauche.
- **Son** : crissement de pneus, puis moteur qui monte.
- **Chute** : un carton « C'est la famille. » de 0,8 s (texte seul), puis retour au calme.
- **Teaser** : le même dérapage, coupé à 0,8 s, sert dans le hook.

**ANI-08 · La rue en 3D (GPS, ombres, particules)** : une scène, trois angles
- **Décor** :
  - deux rangées de tours en volumes gris `#1c1c1e`, arêtes `#3a3a3c` ;
  - au sol, la grille hexagonale couchée ;
  - 4 satellites en haut, en pictos.
- **Angle A, le rebond** (caméra au niveau de la rue, orbite lente de 15°) :
  - un signal direct (trait blanc) est bloqué par une tour ;
  - un autre rebondit sur la façade d'en face et arrive en retard, en rouge ;
  - un point rouge « fantôme » apparaît sur le mauvais trottoir.
- **Angle B, les ombres radio** (caméra qui monte en plongée) :
  - chaque tour projette au sol une « ombre radio » en gris foncé ;
  - les signaux faibles sont barrés en rouge, les forts en vert ;
  - le point se cale du bon côté de la rue, en vert.
- **Angle C, les particules** (même plongée) :
  - 2 000 points blancs à 40 % éparpillés dans la rue (graine fixe pour rester déterministe) ;
  - à chaque « tic » (toutes les 0,8 s, 4 fois), ceux qui ne collent pas s'éteignent et le nuage se resserre sur la vraie position.
- **Parenthèse Kalman** : en surimpression 2D, une courbe en cloche barrée, et à côté une carte de chaleur à plusieurs bosses. Bandeau « Pour les devs ».

**ANI-09 · Glisser et deviner (interpolation, puis navigation à l'estime)**
- **Avant** : la voiture saute de point en point (4 positions, sans transition), comme le coéquipier qui lag.
- **Après** :
  - la même voiture glisse entre les points (interpolation `sine.inOut`) ;
  - quand le point suivant tarde, elle continue en pointillés selon sa vitesse et sa direction, puis se recale doucement quand la vraie position arrive ;
  - une flèche « vitesse + direction » en SF Mono.

**ANI-10 · Les voitures fantômes**
- **Éléments** : la carte vue côté passager, recréée sans l'interface d'Uber, avec 4 voitures et l'étiquette « 17 min ».
- **Déroulé** :
  - sur « effet visuel », les 4 voitures deviennent translucides ;
  - sur « économiseur d'écran », le mème du logo DVD (une voiture qui rebondit) ;
  - sur « partout où le passager posait son épingle », l'épingle se pose à 3 endroits, et à chaque fois des voitures translucides apparaissent autour.
- **Couleur** : les fantômes en blanc à 25 % avec un contour rouge.

## Éléments à collecter 🟥

1. **Le logo Flutter** (simple-icons, ou le logo officiel sur Wikimedia Commons) pour la maquette des #8 et #59. **Aucune capture de tes applis** : elles relèvent de ton travail.
2. **Les captures du blog Uber Engineering** :
   - la liste des articles ;
   - *Uber's Real-Time Push Platform* (2020) ;
   - *H3: Uber's Hexagonal Hierarchical Spatial Index* (2018) ;
   - *Rethinking GPS* (2018).

   Fais-les avec `capture-blog.mjs` de la recette (§ 9), en refusant les cookies (#6, #19, #30, #44).
3. **Le dépôt GitHub `uber/h3`** (#19).
4. **Les articles de presse** : *Uber's Phantom Cabs* (Motherboard, juillet 2015) et Fortune du 30/07/2015 (#52, #54).
5. **Les vraies cellules H3** en GeoJSON. Pour les générer, je peux écrire le script Python si tu veux :
   - Paris aux niveaux 7 à 9, avec la gare de Lyon (#3, #11, #20) ;
   - le globe au niveau 1 ou 2 (#2) ;
   - les 12 pentagones (`h3.get_pentagons`) (#26).
6. **2 s d'un trailer officiel de *Monster Hunter Wilds*** (#49) : un chasseur face au Rathalos. Le trailer de lancement (février 2025) et le teaser des Game Awards 2023 en montrent un. Prends-le sur la chaîne YouTube officielle de Capcom et utilise-le **sans le son**. Le lag se fabrique au montage.
7. **Les mèmes** :
   - Galaxy brain, Math lady, Not stonks ;
   - ⚠️ *Shrek 2* « Are we there yet? », Naruto chez Ichiraku, la ruée Pokémon Go de Central Park, le trailer de Monster Hunter.
8. **Un bol de ramen** sur fond sombre (photo libre de droits sur Pexels ou Unsplash) (#34).
9. **Une carte marine ancienne** du domaine public, par exemple sur Wikimedia Commons (#51).
10. **Les bruitages hors recette** : crissement de pneus, slurp, « clac », ping sonar, bip satellite, vagues.

## Une chose nouvelle à essayer : le décor qui se transforme

La technique de cette vidéo, c'est **la bascule de la grille du fond, des carrés aux hexagones** (#18, 2:05.6, ANI-03). Le décor change sous les yeux du spectateur au moment où l'idée change, et il reste changé.
- **Pourquoi elle sert la vidéo** : tu n'as pas besoin de dire « à partir de maintenant, on est dans H3 ». Le décor le dit pendant 7 min.
- **Le principe** : chaque cellule a toujours 6 sommets. Un carré, c'est un hexagone dont 2 sommets sont doublés. On interpole les 6 sommets de chaque cellule vers leur position hexagonale.
- **En HyperFrames** :
  - les cellules sont des `<polygon>` SVG, et chaque point est stocké dans un objet `{x, y}` ;
  - GSAP anime ces objets ;
  - un `onUpdate` réécrit l'attribut `points` ;
  - le décalage se fait avec `stagger: { from: "center", amount: 0.6 }` et l'easing `power3.inOut` sur 0,9 s ;
  - tout est déterministe : aucune valeur aléatoire évaluée au rendu.
- **Une fois faite**, la grille resservira pour Waze le 7 décembre (`calendrier.md`).
