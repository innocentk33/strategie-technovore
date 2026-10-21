# Storyboard : OpenCode piraté (YouTube 16:9, recette « Premium noir »)

> **Voix off montée** : `assets/audio/voix-off-montee.wav` (8:20,9 ; 48 kHz ; −15,9 LUFS ; crête −2 dBTP), tirée de `openCode.m4a` (21 min 41 de prises). Horodatage mot à mot : `assets/audio/voix-off-montee.transcript.json`.
> **Durée de la vidéo** : 8:35,9 = voix (avec les blancs des 7 écrans de chapitre et des 5 mèmes) + 15 s de musique pour l'écran de fin.
> **Planche avec les images** : `boards/storyboard.html` (104 plans posés dans le vrai projet). Les timecodes (TC) ci-dessous sont ceux de la vidéo finale.
> Script : `/Users/innocent/Dev/youtubeSkill/projets/opencode/script.md` · sources : `sources.md` (même dossier).

## Fiche d'identité

| Axe | Position |
|---|---|
| Cible | Devs et curieux de tech, intermédiaires (public Claude et code de la chaîne) |
| But | Théorique (comprendre la faille) avec une vraie part pratique (la checklist) |
| Ambiance | Enquête posée, ton complice ; l'humour passe par le geste et des mèmes très courts |
| Complexité | Moyenne : hash contre chiffrement, base « référencée » |
| Outil | HyperFrames (HTML + GSAP), recette Premium noir en 16:9 |
| Technique nouvelle | **La caméra continue qui suit le protagoniste** : un monde noir par chapitre, la caméra glisse d'un élément au suivant au lieu de couper |

## L'idée de mise en scène : suivre la clé

- **Le protagoniste, c'est la clé API.** Un seul picto (trait blanc, bouts ronds) traverse toute la vidéo : blanche quand elle est neutre, **rouge** quand elle est volée, **verte** quand elle est à toi, gris foncé quand elle est morte. La caméra la suit : de Max à OpenCode (accroche), du PC à la Console (ch. 1), dans la cellule `credentials` (ch. 3), de main en main chez les revendeurs (ch. 5), jusqu'à la checklist (ch. 7). À la fin elle disparaît : « la seule clé qu'on ne peut pas te voler, c'est celle que tu ne possèdes pas ».
- **Le motif, c'est la bulle « ok »** : posée dans l'accroche (plans 8-11), elle revient à la relance (plan 65), puis en grand recul parmi 8 966 requêtes (plan 77). C'est aussi la miniature.
- **Un monde par chapitre, une caméra continue.** Chaque chapitre est un plan-séquence sur fond noir : la caméra glisse (power3.inOut 0,7-0,9 s), recule pour révéler, pousse sur une preuve (×1,05 à ×1,55), et dérive lentement pendant les tenues. Les coupes franches sont réservées aux mèmes et aux mots chocs. Ch. 2 est un **travelling le long d'une frise horaire**, ch. 3 une **descente le long de l'historique Git**, ch. 6 une **montée de l'escalier des paliers**, ch. 7 un **défilement de la checklist**.
- **Les écrans de chapitre sont des stations sur un rail.** Le même rail de 7 stations revient à chaque chapitre ; la clé avance d'une station, la caméra la suit puis plonge dans la clé, qui devient le premier objet du chapitre (transition née de l'action). Le rail apparaît dès la fin de l'accroche, avec la checklist qui attend à la station 7.
- **Récit (voyage du héros)** : statu quo = « deux OpenCode » ; appel = la nuit du 17 octobre ; épreuves = le code (colonne en clair, pas de hash, pas de coffre, base référencée) ; crise = la relance « pourquoi payer pour un ok ? » sans réponse ferme ; trésor = « une clé API, c'est une carte bancaire déjà branchée sur une IA » ; retour = ta clé à toi, le plafond, la checklist ; nouvelle vie = la clé que tu ne possèdes pas (RTX 5080).

## Comment la voix off a été montée

- **117 morceaux** gardés sur 197 prises de phrase. Règle : la dernière prise complète, sauf quand une plus ancienne colle mieux au script.
- **Reprises supprimées** (exemples) : « Avec les clés de Max. » ×2 ; « Près de 9 000 requêtes, son crédit… » ; « Le code d'OpenCode est public, alors on va voir… » ×3 ; « Un peu comme Claude Code ou Codex. » ×2 ; « La console qui est un tableau de bourse » ; « Ça s'appelle du bring… » ×2 ; « Donc c'est la Console qui a été touchée… » ×3 ; « Ces clés-là ne nous arrivent jamais » ×1 ; « 17 h 30, Matt Johansen… » ×8 ; « 20 h, OpenCode confirme… » ×5 ; « Anthropic et Google bloquent… » ×2 ; « Dax trouvait un peu frustrant que les API… » ; « Mais comment des clés… » ×2 et la reprise « On ouvre le code, le code de, le code de la Console » ; « …les 8 derniers caractères » (1re prise, fausse) ; « Pour t'afficher la fin de la clé » ×2 ; « Alors, toi qui codes… » (remplacée par ta 2e version) ; « Une clé API, il faut l'envoyer en entier… » ×1 ; « Pour avoir une empreinte… » ; « Il n'a qu'à vérifier… » ×1 ; « Rien ne relie ce système » ; « Le pirate est entré » ; « Il me reste ma question… poux » ; « Le mot de la distillation… » ×2 ; « Là, c'est une hypothèse… » ×1 ; « Dax raconte avoir banni une personne » ; « Alors, c'est OK » ×1 ; « Mais on n'entraîne pas un modèle avec… » ×1 ; « Est-ce que… » ; « Et une requête en chinois. » ; « À ce jour, OpenCode n'a… » ×3 ; « Maintenant, pour toi, ta clé… » ×5 ; « Et même appliqué » ; « Chez Anthropic, ça a du prépayé » ; « Là, ton compte se recharge… » et deux reprises de la recharge ; « 500 $ pour un mois au premier / au prix » ; « Donc ce soir, si tu as reçu… » ×2 ; « Deux, sans e-mail mais avec une clé » ; « Trois… et tu ne coupes pas » ; « Quatre, une attaque limite » ; « Cinq, supprime les clés oubliées » ×1 ; « je n'ai pas encore collé ou » ; « Pourtant, j'utilise ».
- **Corrections après ta relecture (21/10)** : le mème de Gandalf est retiré ; coupés en plus : le faux départ « Une clé API, il faut l'envoyer en entier à… » et « Une empreinte… » (3:08-3:12), « En février 2026, Anthropic » dit deux fois (4:58), « Il faut… » dit deux fois (6:45) et un « et même » de trop (6:47) ; rendus en entier : « …à ce système » (4:01), « Donc ce soir » (7:19) et le « où » de « tu sais où » (7:36).
- **Vitesse 1,1 et respirations (21/10)** : toute la voix passe à 1,1 (hauteur conservée) ; les silences de 0,2 à 0,6 s entre les phrases sont réduits d'un tiers, les respirations de plus de 0,3 s à l'intérieur d'une phrase ramenées à 0,22 s. Les écrans de chapitre, les mèmes et la pause de la devinette gardent leur durée réelle. Ton « ok » de l'IA est remplacé par le mème « Okay ». Résultat : 9 min 28 → 8 min 21 de voix.
- **Corrections du 21/10, après ta 2e relecture** : le silence entre « Dax » et « Raad » est retiré (0,36 s, à 1:20,6) ; le mème « Okay » ne garde que la fin où il dit « ok » et passe en carte à gauche ; un navigateur ouvre la vraie page GitHub d'OpenCode sur « Le code d'OpenCode est public » ; la forgeronne de Monster Hunter Wilds joue le perso resté à la taverne ; toutes les musiques sont 10 dB plus bas (sauf la fin qui remonte) et six morceaux du dossier PERSO remplacent les répétitions ; mèmes normalisés à −16 LUFS comme la voix.
- **Ce qui est gardé tel quel, parce que c'est ta voix** : « Reste jusqu'à la fin car c'est ta checklist », « Bon, OpenCode, c'est quoi ? », « Perso… j'ai tendance à faire très attention », « il est légitime de se dire », « Mais en vrai », « Faut pas abuser, en vrai », « C'est le pire abonnement de ta vie, en vrai », « Pourtant, je compte utiliser OpenCode », « remplacer un abonnement Claude », « celle que tu ne possèdes pas ».
- **Les blancs** : tout silence de plus de 0,6 s à l'intérieur d'une phrase est ramené à 0,4 s ; entre deux phrases 0,1 à 0,35 s, 0,5 à 0,6 s quand l'idée change, 0,8 à 1 s en fin de partie ; coupes dans les silences, fondus de 6 ms.
- **Les blancs posés exprès** : 3 s par écran de chapitre (1,4 s quand ta voix dit le titre : ch. 2 « La nuit du 17 octobre », ch. 7 « Donc ce soir ») ; la durée exacte de chaque mème ; 2 s pour la devinette (« Prends deux secondes ») ; le mème muet de Cyprien sur « Mais pourquoi ? » (1,85 s en tout) ; ≈ 0,9 s après « Pas de coffre ».

### À vérifier à l'oreille, ou à corriger à l'écran

| Passage enregistré | Problème | Ce que j'ai fait |
|---|---|---|
| « 2 h du matin » (1:35) | L'exposition commence à 00:30 UTC, soit **2 h 30** à Paris | Gardé à l'oral ; **l'écran affiche 02:30** avec la conversion en micro. Pour corriger l'oral, enregistre « Deux heures trente du matin » |
| « Matt Johnson » (1:46) | Il s'appelle **Johansen** | Gardé à l'oral ; **le nom écrit est juste** sur la capture et le libellé |
| « 264 $ partis sur la clé d'Anthropic » (0:19) | Raccord entre deux prises juste après « et » | 🟨 Écoute ce raccord |
| « Est-ce que ça peut vraiment remplacer un abonnement Claude ? » (8:05) | La phrase du script sur la série « Claude ou mon PC ? » n'a pas été enregistrée | Remplacée par une petite carte à l'écran « Bientôt sur la chaîne : Claude ou mon PC ? » |
| « Un mot de passe, si le site n'a jamais besoin… » | Le « si » s'écarte du script | Gardé : c'est ta formulation |

## Chapitres YouTube (à coller dans la description)

```
0:00 Introduction
0:45 Deux OpenCode
1:33 La nuit du 17 octobre
2:22 Comment tes clés étaient rangées
3:53 L'ancien système
4:38 Pourquoi tes clés valent de l'or
6:25 Le réglage qui décide de ta facture
7:19 Ta checklist pour ce soir
```

## Rythme et rétention

| Repère | TC | Part de la vidéo |
|---|---|---|
| Fin de l'accroche | 0:45,4 | 9 % |
| Révélation « Pas de coffre » | 3:31,5 | 41 % |
| Appel à l'abonnement | 3:42,8 | 43 % |
| Relance : la musique coupe, le « ok » revient | 4:38,2 | 54 % |
| Thèse : « une carte bancaire déjà branchée sur une IA » | 5:53,9 | 69 % |
| La checklist | 7:19,4 | 85 % |
| Écran de fin | 8:09,9 | 95 % |

Passages fragiles : **3:01 à 3:41** (hash, coffre, disque : 52 s d'explication) et **4:47 à 5:40** (distillation, chiffres d'Anthropic). Une action visible toutes les 4 à 5 s dans le plan-séquence : la clé bouge, une preuve arrive, un chiffre tombe.

## Musique par partie

Chaque morceau normalisé à −16 LUFS puis limité à −3 dB, puis posé **10 dB plus bas qu'avant** sous la voix (volumes 0,035 et 0,045), sauf la musique de fin qui remonte jusqu'à 0,141 puis 0,178 sur l'écran de fin. **Coupée pendant chaque mème.**

| Partie | TC | Morceau | Ruptures |
|---|---|---|---|
| Accroche | 0:00 – 0:45,4 | « Dark Ambient for Crime and Tension » (megalix, Pixabay) | Coupée par le mème « Okay », **coupée net sur « pourquoi »**, la pulsation reprend sur « public » |
| Ch. 1 | 0:45,4 – 1:31,0 | « Future Minimal » (kissan4, Pixabay) | Entre sur l'écran de chapitre |
| Ch. 2 | 1:33,1 – 2:22,3 | « Singularity » (MokkaMusic) | La nuit |
| Ch. 3 | 2:22,3 – 3:42,9 | « Intrigue » (Savfk, CC BY 4.0) | **Silence total sur « Pas de coffre »**, puis reprise douce |
| Abonnement | 3:42,9 – 3:53,2 | « A Complicated Profession » (Fuzzeke) | — |
| Ch. 4 | 3:53,2 – 4:30,3 | « Breath of Freedom » (Infraction) | Très basse sur « La base reste » |
| Taverne | 4:30,3 – 4:38,2 | « The Fantasy » (Fuzzeke) | Le clin d'œil RPG |
| Ch. 5 | 4:45,4 – 6:25,8 | **Silence** à la relance, « Dark Ambient » sur « Pour y répondre », puis « Neverland » (orchestral sombre) sur « Et les clés volées, ça se revend » | La pulsation monte sur « Anthropic a accusé » |
| Ch. 6 | 6:25,8 – 7:03,1 | « Blue Shirt Guy » (Fuzzeke) | Coupée par le mème |
| Ch. 6 (fin) et 7 | 7:04,8 – 7:47,1 | « Energetic Drum Background » (Epic Music Waves) | Les coches de la checklist tombent sur les temps |
| Fin | 7:46,8 – 8:35,9 | « Future Minimal » | **Part 10 dB plus bas et remonte jusqu'au niveau d'origine sur l'écran de fin**, se creuse sous la dernière phrase |

Crédits à mettre en description : *Intrigue* par Savfk (CC BY 4.0, free-stock-music.com) ; *Singularity* par MokkaMusic (inaudio.org) ; *A Complicated Profession*, *The Fantasy* et *Blue Shirt Guy* par Fuzzeke ; *Breath of Freedom* par Infraction (inaudio.org) ; *Neverland* (Emotional Dark Orchestral Music) ; *Energetic Drum Background* par Epic Music Waves ; *Future Minimal* (kissan4) et *Dark Ambient for Crime and Tension* (megalix) sur Pixabay.

## Bruitages

Banque de la recette, copiée dans `assets/sfx/` : `air`, `air-long` (caméra, entrées), `slide` (carte qui glisse), `tick` (surlignage, contour), `bubble` (bulle, cloche), `toggle` (tampon, interrupteur, coche), `dissolve` (effacement), `powerdown` (avant un mot choc), `absorb`, `poweron` (voyant vert). Crête −3 dB puis −20 à −24 dB ; **0 à 2 par plan** ; une piste audio par famille. Pas d'impact, d'alarme ni de basse, **sauf l'impact basse demandé sur « 35 millions de tokens »** (`sfx/bass-1.wav`, à 0:00,7, volume 0,35).

## Mèmes (coupe franche, voix et musique coupées)

| # | TC | Mème | Fichier (déjà coupé et mis à −18 LUFS) | Source |
|---|---|---|---|---|
| 9 | 0:26,4 | Okay (à la place de ton « ok »), **en carte à gauche** sans couper l'image | `assets/memes/okay.mp4` | PACK › MEMES › NORMAL › « Okay.mp4 », 5 s → fin |
| 11 | 0:31,4 | Pourquoi (Cyprien), **muet, sans couper la voix** | `assets/memes/cyprien-pourquoi-muet.mp4` | « Cyprien_Pourquoi_Meme.mp4 », son retiré |
| 24 | 1:30,9 | ça va bien se passer | `assets/memes/ca-va-bien-se-passer.mp4` | PACK › MEMES › NORMAL › « Ne t'inquiète pas ça va bien se passer », 0 → 1,85 s |
| 43 | 2:53,8 | C'est logique | `assets/memes/c-est-logique.mp4` | « Steelorse - C'est logique », 0 → 1,2 s |
| 58 | 4:14,2 | You're deleting all my data | `assets/memes/deleting-all-my-data.mp4` | ton extrait de Silicon Valley, 5,15 → 6,25 s, sous-titre FR à ajouter |
| 90 | 7:03,1 | Merci aux clients fidèles | `assets/memes/merci-clients-fideles.mp4` | « Merci aux clients fidèles », 0 → 1,7 s |

En plus, posés dans le décor sans couper : le chien « This is fine » dans la Console (plan 23) le post de Dax avec sa photo de policiers (plan 75) et ton mème de la distillation (plan 67). YouTube peut repérer les extraits de films et de séries (Silicon Valley) : ils sont très courts, mais garde-le en tête.

## Légende

🟦 VID vidéo · 🟩 IMG image · 🟪 ECR capture d'écran ou code · 🟧 ANI animation · ⬜ TXT texte sur noir · 🩷 MEM mème · 🟫 CHAP écran de chapitre · 🟨 à vérifier

## Fiches d'animation

**ANI-CHAP · Écran de chapitre (3 s, 7 fois)**
- État initial : noir, le rail de 7 stations (trait `#3a3a3c`, 1 200 px, y = 780) ; stations passées blanches, la clé sur la station précédente.
- t = 0,00 : `air-long`. La clé glisse jusqu'à la station suivante (0,9 s, power3.inOut) ; le trait blanc la suit ; la caméra recadre pour garder la station au centre.
- t = 0,35 : « CHAPITRE n » (SF Mono 32, gris) puis le titre (128 px) mot à mot : flou 6 px → 0 et opacité 0 → 1 en 0,13 s, 0,067 s d'écart.
- t = 0,95 : `tick` à l'arrivée. Tenue jusqu'à 2,4 s.
- t = 2,40 : titre qui s'efface (0,2 s) ; la caméra pousse dans la clé (×6, 0,6 s, power3.in) ; la clé devient le premier objet du chapitre.

**ANI-CAM · La caméra continue**
- Chaque scène = un « monde » (div de 6 000 à 8 000 px) dans un cadre caméra ; on anime `x`, `y` et `scale` du monde, jamais des éléments un par un.
- Déplacement : 0,7-0,9 s, power3.inOut, flou de mouvement horizontal 6-12 px au plus vite. Dérive pendant une tenue : ×1,00 → ×1,04 en sine.inOut. Arrivée lente, départ net. Le sujet garde la même place à l'écran d'un plan à l'autre (tiers gauche ou centre).
- Blocs du catalogue à reprendre : `pan-stations` (ch. 2, ch. 5 farming), `scroll-camera-story` (ch. 3 historique, ch. 7 checklist), `pull-back-reveal` (plans 2, 17, 77), `ui-focus-zoom` (captures).

**ANI-OK · La bulle « ok »**
- Bulle `#2c2c2e`, coins 44 px, « ok » 96 px. Entrée : ×0,7 → ×1,1 → ×1 (0,12 + 0,08 s) avec `bubble`. Même cadrage aux plans 10, 65 et 78 ; au plan 77, recul de 2 s jusqu'à n'être qu'un point d'une grille de 8 966.

**ANI-PHONE · Le téléphone de Max (plans 6 à 8)**
- Brique « téléphone » de la recette (`abonnement.html` du projet Short premium) : arrivée par le bas en contre-plongée (rotationX −14), la capture défile à l'intérieur, contours tracés (`stroke-dashoffset`) sur 8,966 puis −$2.15 ; glissement vers la capture Claude ; poussée ×1,55 dans la ligne des logs qui se détache en deux bulles.

**ANI-FRISE · La nuit du 17 octobre (ch. 2)**
- Une seule ligne horaire de 00:00 à 00:00 (graduations SF Mono 24 gris) ; la caméra la longe en continu ; lune → soleil → lune ; marqueurs rouges 02:30, 17:30, 20:08 ; chaque preuve est une carte accrochée au-dessus de son heure.

## État du montage (21/10)

Montage complet dans le projet : les 10 scènes sont animées (caméra continue `.cam` par plan, écrans de chapitre animés, entrées calées sur les mots), avec 114 bruitages de la banque posés dans les scènes, l'impact basse sur « 35 millions de tokens », 17 morceaux de musique, dont six du dossier PERSO (coupés pendant les mèmes et sur « Pas de coffre », silence à la relance du ch. 5), le karaoké de l'accroche (`compositions/captions.html`), SF Mono via `local("SF Mono")`, et la RTX 5080 détourée (`assets/cutouts/rtx-5080-nvidia-rtx-5080.png`).
Mixage simulé (21/10, après la baisse des musiques) : −15,9 LUFS intégrés, crête −2,4 dBFS (cible de la recette : −16 à −14 LUFS, crête < −1 dBFS). Voix, musiques et mèmes sont tous normalisés à −16 LUFS avant d'être posés.

Reste à faire hors du projet :
1. Écouter les raccords signalés plus haut (« …et 264 $ »).
2. Sur YouTube : poser l'écran de fin (vidéo ArtCraft et bouton d'abonnement) dans les zones réservées, à partir de 8:15 environ (20 s maximum) ; coller les chapitres et les crédits musicaux dans la description.
3. Les images de cette planche montrent les poses du storyboard, pas l'animation finale : regarde la vidéo dans l'aperçu.

---

## Plans

### Accroche

## Frame 1: Le compteur (0.2-2.5s)
- act: Accroche
- status: posé (image `boards/stills/at-0.73s.png`)
- TC : 0:00,2 → 0:02,5 (2.3 s) · 🟧 ANI
- Voix : « 35 millions de tokens. »
- Image : Noir pur. Un compteur géant en SF Mono s'emballe de 0 à **35 026 055** et se fige ; « tokens » en gris à droite. Bandeau micro en bas : « OpenCode piraté · 17 octobre 2026 ».
- Caméra : Fixe, poussée lente ×1 → ×1,04 (sine) sur toute la phrase.
- Texte : Chiffre héros 240 px. Karaoké incrusté sur toute l'accroche (56 px, une ligne, y ≈ 960).
- Son : **Impact basse** `sfx/bass-1.wav` (PACK › SFX › Impact › 00-BASS › Bass_1) sur « 35 » (0:00,7), puis la rafale de `tick` du compteur, coupée net sur le dernier chiffre. Musique « Dark Ambient » en douceur.

## Frame 2: Vingt fois Harry Potter (2.5-7.6s)
- act: Accroche
- status: posé (image `boards/stills/at-3.47s.png`)
- TC : 0:02,5 → 0:07,6 (5.1 s) · 🟧 ANI
- Voix : « En gros, de quoi écrire plus de 20 fois toute la saga Harry Potter. »
- Image : Le compteur monte en haut du cadre. Dessous, 7 tranches de livres dessinées en traits (pas d'image de la saga) se dupliquent en un mur de 140 tranches. « ×20 » en héros.
- Caméra : **Recul** de 0,9 s (power3.inOut) : le compteur devient le titre de la scène.
- Texte : « ×20 » 240 px. Micro gris : « Estimation : 35 M tokens ≈ 26 M de mots ; la saga ≈ 1,08 M de mots ».
- Son : `air` sur le recul.

## Frame 3: Cramés (7.6-9.1s)
- act: Accroche
- status: posé (image `boards/stills/at-8.33s.png`)
- TC : 0:07,6 → 0:09,1 (1.5 s) · 🟧 ANI
- Voix : « Cramés en moins d'une journée, »
- Image : Le mur de livres se dissout de bas en haut (flou + fondu, braises rouges). Un arc d'horloge se dessine autour du vide : « < 24 h » en rouge.
- Caméra : Fixe.
- Texte : « < 24 h » SF Mono rouge `#ff453a`.
- Son : `dissolve`.

## Frame 4: Les clés de Max (9.1-12.8s)
- act: Accroche
- status: posé (image `boards/stills/at-9.98s.png`)
- TC : 0:09,1 → 0:12,8 (3.7 s) · 🟩 IMG
- Voix : « avec les clés de Max Weinbach, volées chez OpenCode. »
- Image : **Le protagoniste entre** : avatar rond de Max (photo de profil X) et son nom. À côté de lui, ses 3 clés (picto clé en trait) étiquetées OpenAI, Anthropic, Google. Sur « volées », le logo OpenCode apparaît à droite ; les 3 clés y glissent, passent au rouge et sortent du cadre.
- Caméra : **La caméra suit les clés** : panoramique vers la droite (0,8 s, power3.inOut), puis revient.
- Texte : « Max Weinbach » blanc / « @mweinbach » gris.
- Son : `slide` quand les clés partent.
- Médias : `images/avatar-mweinbach.jpg`, `logos/openai.svg`, `logos/anthropic.svg`, `logos/google.svg`, `images/opencode-logo.png`

## Frame 5: Rien lancé (12.8-15.2s)
- act: Accroche
- status: posé (image `boards/stills/at-13.5s.png`)
- TC : 0:12,8 → 0:15,2 (2.4 s) · 🟧 ANI
- Voix : « Pourtant, lui, il n'a rien lancé. »
- Image : Retour sur Max : à côté de lui, un terminal vide, curseur immobile.
- Caméra : Retour panoramique sur Max, puis fixe.
- Texte : « 0 requête lancée » gris 44 px.
- Son : —

## Frame 6: Le tableau de bord OpenAI (15.2-19.4s)
- act: Accroche
- status: posé (image `boards/stills/at-16.14s.png`)
- TC : 0:15,2 → 0:19,4 (4.2 s) · 🟪 ECR
- Voix : « Près de 9 000 requêtes. Son crédit OpenAI à moins 2,15 $ »
- Image : Brique **téléphone** de la recette (coque CSS, écran arrondi) avec la vraie capture du tableau de bord OpenAI de Max. Contour qui se dessine sur « Total requests 8,966 », puis sur « Credit balance −$2.15 » (contour rouge).
- Caméra : Le téléphone arrive par le bas en contre-plongée (rotationX −14) ; la capture **défile dans l'écran** de « Total tokens » à « Credit balance ».
- Texte : Colonne droite (x ≈ 1240) : « 8 966 requêtes » blanc, puis « −2,15 $ » rouge 240 px.
- Son : `air-long` à l'arrivée du téléphone, `tick` à chaque contour.
- Médias : `captures/max-openai-usage.jpg` (35 026 055 tokens et 8 966 requêtes sont bien côté OpenAI)

## Frame 7: La facture Anthropic (19.4-22.6s)
- act: Accroche
- status: posé (image `boards/stills/at-20.31s.png`)
- TC : 0:19,4 → 0:22,6 (3.2 s) · 🟪 ECR
- Voix : « et 264 $ partis sur sa clé Anthropic. »
- Image : Dans le même téléphone, l'écran glisse vers la capture du tableau de bord Claude : « Total cost $264.09 » entouré en orange Claude.
- Caméra : Glissement horizontal de l'écran du téléphone (0,6 s).
- Texte : « 264 $ » blanc 240 px.
- Son : `slide`.
- Médias : `captures/max-claude-cost.jpg`

## Frame 8: Réponds ok (22.6-26.4s)
- act: Accroche
- status: posé (image `boards/stills/at-23.54s.png`)
- TC : 0:22,6 → 0:26,4 (3.8 s) · 🟪 ECR
- Voix : « Et dans ses logs, une requête, en chinois : “Réponds ok.” L'IA répond… » *(ton « ok » est remplacé par le mème)*
- Image : Le téléphone affiche la page Logs de Max. La ligne « 请回复ok → ok » se détache de l'écran et devient deux bulles de chat au centre : bulle grise « 请回复ok » (traduction micro « Réponds ok »), puis bulle « ok ».
- Caméra : **Poussée** ×1,55 dans l'écran jusqu'à la ligne, puis le téléphone tombe hors champ et seules les bulles restent.
- Texte : Bulles 64 px ; « ok » 96 px.
- Son : `bubble` pour chaque bulle. La musique baisse à −24 dB sous le « ok ».
- Médias : `captures/max-openai-log-ok.jpg`

## Frame 9: Mème : Okay (26.4-28.0s)
- act: Accroche
- status: posé (image `boards/stills/at-27.3s.png`)
- TC : 0:26,4 → 0:28,0 (1.6 s) · 🩷 MEM
- Voix : *(mème, 1,35 s, à la place de ton « ok »)*
- Image : Le mème « Okay » dans une carte arrondie **à gauche** (600 × 600, pop à l'entrée) ; l'animation reste visible à droite : la bulle « 请回复ok » et la bulle « ok » de l'IA, qui apparaît pile sur le « Okay » du mème.
- Caméra : —
- Texte : —
- Son : Le son du mème (mis au niveau de la voix) ; voix et musique se taisent.
- Médias : `assets/memes/okay.mp4` (PACK › MEMES › NORMAL › « Okay.mp4 », de 5 s jusqu'à la fin : la dernière seconde et demie, où il dit « ok »), posé dans la scène de l'accroche

## Frame 10: Payé pour un ok (28.0-31.4s)
- act: Accroche
- status: posé (image `boards/stills/at-28.93s.png`)
- TC : 0:28,0 → 0:31,4 (3.4 s) · 🟧 ANI
- Voix : « Quelqu'un a payé, avec l'argent d'un autre, pour faire dire “ok” à une IA. »
- Image : La bulle « ok » seule au centre. Une étiquette de prix rouge s'y accroche : « payé par Max ». C'est le motif de la vidéo (et de la miniature).
- Caméra : Dérive lente ×1,00 → ×1,03.
- Texte : Étiquette rouge 32 px.
- Son : —

## Frame 11: Mème : Pourquoi (Cyprien, muet) (31.4-33.3s)
- act: Accroche
- status: posé (image `boards/stills/at-32.29s.png`)
- TC : 0:31,4 → 0:33,3 (1.9 s) · 🩷 MEM
- Voix : « Mais pourquoi ? »
- Image : Le mème « Pourquoi » de Cyprien plein écran, **sans son**, par-dessus ta voix : les lettres POUR… QUOI s'écrivent pendant que tu le dis.
- Caméra : —
- Texte : —
- Son : Muet : on n'entend que ta voix. **Musique coupée net** sur « pourquoi » pendant le mème.
- Médias : `assets/memes/cyprien-pourquoi-muet.mp4` (PACK › MEMES › NORMAL › « Cyprien_Pourquoi_Meme.mp4 », son retiré)

## Frame 12: Bande-annonce : le code (33.3-40.0s)
- act: Accroche
- status: posé (image `boards/stills/at-34.18s.png`)
- TC : 0:33,3 → 0:40,0 (6.7 s) · 🟪 ECR
- Voix : « Le code d'OpenCode est public : alors on va voir où ces clés étaient rangées, et pourquoi on ne pouvait pas les hasher comme un mot de passe. »
- Image : **Un navigateur** s'ouvre : l'adresse `github.com/anomalyco/opencode` se tape, la vraie page du dépôt se charge sur « public », défile jusqu'au README (logo OpenCode). Sur « où ces clés étaient rangées », la caméra plonge dans le navigateur et arrive sur le code : `credentials: text("credentials")` s'allume. Puis le « # » (le hash) rebondit sur une serrure.
- Caméra : **Plongée** dans le code (traversée en diagonale, 2 s, sine), puis arrêt sur la serrure.
- Texte : Aucun texte en plus (le karaoké suffit).
- Son : `air-long` ; la pulsation de la musique reprend sur « public ».
- Médias : `assets/captures/web-github-repo.jpg` (capture de github.com/anomalyco/opencode, thème sombre), `code/provider.sql.ts.txt`

## Frame 13: Ta checklist (40.0-45.4s)
- act: Accroche
- status: posé (image `boards/stills/at-40.65s.png`)
- TC : 0:40,0 → 0:45,4 (5.4 s) · 🟧 ANI
- Voix : « Et si t'as déjà collé une clé API quelque part, reste jusqu'à la fin : c'est ta checklist pour ce soir. »
- Image : Une carte « Ta checklist pour ce soir » (panneau `#1c1c1e`) avec 5 lignes floutées et 5 cases vides.
- Caméra : La carte recule et se pose au bout d'un rail horizontal : **le rail des chapitres**, qui sert d'enchaînement vers l'écran 1.
- Texte : Titre de carte 56 px.
- Son : `slide`.

### Chapitre 1 · Deux OpenCode

## Frame 14: Écran de chapitre 1 (45.4-48.4s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-46.38s.png`)
- TC : 0:45,4 → 0:48,4 (3.0 s) · 🟫 CHAP
- Voix : *(3 s sans voix)*
- Image : **Écran de chapitre** (voir la fiche ANI-CHAP) : rail de 7 stations, la clé avance jusqu'à la station 1. « CHAPITRE 1 » / « Deux OpenCode ».
- Caméra : La caméra suit la clé sur le rail, puis **plonge dans la clé**, qui devient le curseur du terminal du plan suivant.
- Texte : « CHAPITRE 1 » SF Mono 32 px gris, titre 128 px blanc.
- Son : `air-long` + `tick` à l'arrivée. Changement de musique : « Future Minimal ».

## Frame 15: Le terminal (48.4-53.1s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-49.29s.png`)
- TC : 0:48,4 → 0:53,1 (4.7 s) · 🟪 ECR
- Voix : « Bon, OpenCode, c'est quoi ? OpenCode, c'est un agent de code open source qui tourne dans ton terminal, »
- Image : Fenêtre de terminal macOS (`#1c1c1e`) : logo-mot OpenCode en pixels, invite qui clignote, une ligne de conversation.
- Caméra : Recul depuis le curseur jusqu'à la fenêtre entière.
- Texte : Libellé intégré « agent de code · open source » gris 32 px.
- Son : —
- Médias : `images/opencode-wordmark.png`, `captures/web-opencode-home.png` (référence)

## Frame 16: Tu branches le modèle (53.1-57.3s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-54.02s.png`)
- TC : 0:53,1 → 0:57,3 (4.2 s) · 🟧 ANI
- Voix : « un peu comme Claude Code ou Codex, mais tu le branches sur le modèle que tu veux. »
- Image : « Claude Code » et « Codex » en gris à gauche. Puis 5 cartouches de modèles (OpenAI, Claude, Gemini, DeepSeek, Kimi) glissent et se branchent dans le terminal.
- Caméra : Fixe ; les cartouches entrent par la droite en décalé.
- Texte : —
- Son : `slide` sur 3 cartouches seulement (0 à 2 sons par plan).
- Médias : `logos/openai.svg`, `logos/claude.svg`, `logos/googlegemini.svg`, `logos/deepseek.svg`, `logos/kimi.svg`

## Frame 17: Deux OpenCode (57.3-63.0s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-58.13s.png`)
- TC : 0:57,3 → 1:03,0 (5.7 s) · 🟧 ANI
- Voix : « Sauf qu'en réalité, il y a deux OpenCode : l'application PC et la Console. »
- Image : Écran partagé. À gauche, une tour de PC sur le plateau avec le terminal, et la clé dedans (voyant vert « local »). À droite, une fenêtre de navigateur « Console » qui flotte (opencode.ai).
- Caméra : **Recul** du terminal vers le plan large (1 s) : le terminal devient l'écran du PC.
- Texte : Titres intégrés : « L'appli » / « La Console » (96 px), fantômes `#3a3a3c` puis blancs quand ils sont dits.
- Son : `air`.

## Frame 18: La Console (63.0-68.9s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-63.88s.png`)
- TC : 1:03,0 → 1:08,9 (5.9 s) · 🟧 ANI
- Voix : « La Console, c'est un tableau de bord sur le web, où tu peux enregistrer tes propres clés OpenAI, Anthropic ou Google. »
- Image : Dans la fenêtre Console : le vrai tableau « Providers » recréé d'après le code (lignes OpenAI, Anthropic, Google Gemini, avec un champ de clé). **La clé quitte le PC** et vole vers le champ OpenAI.
- Caméra : **La caméra suit la clé** de gauche à droite et pousse sur la Console (×1,4).
- Texte : —
- Son : `air` pendant le vol de la clé, `toggle` quand elle se pose.
- Médias : `code/provider-section.tsx.txt` (libellés réels)

## Frame 19: Bring your own key (68.9-71.3s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-69.75s.png`)
- TC : 1:08,9 → 1:11,3 (2.4 s) · ⬜ TXT
- Voix : « Ça s'appelle du bring your own key. »
- Image : Le nom s'inscrit au-dessus de la Console.
- Caméra : Fixe.
- Texte : « Bring your own key » 96 px blanc, « BYOK » gris au-dessus.
- Son : —

## Frame 20: Moi, jamais (71.3-76.8s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-72.24s.png`)
- TC : 1:11,3 → 1:16,8 (5.5 s) · 🟧 ANI
- Voix : « Perso, j'ai jamais collé de clé API dans un outil comme ça. J'ai tendance à faire très attention. »
- Image : Ta clé à toi, **verte**, reste devant le PC ; elle fait un petit « non » latéral devant la Console.
- Caméra : Retour vers la gauche (0,7 s).
- Texte : « Moi : 0 clé collée » vert 44 px.
- Son : —

## Frame 21: La Console touchée (76.8-84.5s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-77.72s.png`)
- TC : 1:16,8 → 1:24,5 (7.7 s) · 🟪 ECR
- Voix : « Donc c'est la Console qui a été touchée. Le soir même, Dax Raad, d'OpenCode, a précisé : “C'est la Console, pas OpenCode lui-même.” »
- Image : Le contour de la fenêtre Console se dessine en rouge. La vraie capture du post de Dax glisse à droite, surlignage jaune sur « not OpenCode itself ».
- Caméra : Panoramique vers la Console, puis poussée lente sur le post (×1,05).
- Texte : Traduction grise sous la capture : « C'est la Console, pas OpenCode lui-même ». Micro : « 17/10, 23 h 38 ».
- Son : `slide` (carte), `tick` (surlignage).
- Médias : `captures/tw-dax-console-seul.png`

## Frame 22: Ces clés ne nous arrivent jamais (84.5-89.1s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-85.76s.png`)
- TC : 1:24,5 → 1:29,1 (4.6 s) · 🟪 ECR
- Voix : « Ces clés-là ne nous arrivent jamais. Donc, en gros, si tu utilises l'appli seulement, »
- Image : Surlignage de « those keys never come to us ». Puis retour sur l'écran partagé : le PC (l'appli) passe au vert.
- Caméra : Recul vers l'écran partagé.
- Texte : « L'appli : pas touchée » vert.
- Son : `poweron` doux sur le voyant vert.

## Frame 23: This is fine (89.1-90.9s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-90.41s.png`)
- TC : 1:29,1 → 1:30,9 (1.8 s) · 🩷 MEM
- Voix : « tu peux souffler. Les autres… on ne sait pas trop. »
- Image : Dans la fenêtre Console rouge, le chien « This is fine » détouré s'assoit, tasse à la main.
- Caméra : Poussée lente sur la Console.
- Texte : —
- Son : —
- Médias : `images/this-is-fine.png`

## Frame 24: Mème : ça va bien se passer (90.9-93.1s)
- act: Chapitre 1 · Deux OpenCode
- status: posé (image `boards/stills/at-92.25s.png`)
- TC : 1:30,9 → 1:33,1 (2.2 s) · 🩷 MEM
- Voix : *(mème, 1,85 s)*
- Image : **Coupe franche** plein écran : « Ne t'inquiète pas, ça va bien se passer » (vidéo verticale centrée sur le noir), avec son son.
- Caméra : —
- Texte : —
- Son : Voix et musique coupées pendant le mème.
- Médias : PACK MONTAGE › MEMES › NORMAL › « Ne tinquiète pas ça va bien se passer.mp4 », 0,00 → 1,85 s

### Chapitre 2 · La nuit du 17 octobre

## Frame 25: Écran de chapitre 2 (93.1-95.8s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-94.47s.png`)
- TC : 1:33,1 → 1:35,8 (2.7 s) · 🟫 CHAP
- Voix : « La nuit du 17 octobre, »
- Image : Écran de chapitre : la clé avance à la station 2. « CHAPITRE 2 » / « La nuit du 17 octobre ». **Ton titre est dit par ta voix** : chaque mot passe en blanc quand il est dit.
- Caméra : La caméra suit la clé sur le rail ; le rail se change en **frise horaire** (même trait), qui porte tout le chapitre.
- Texte : Titre 128 px.
- Son : `air-long`. Musique : « Dark Synthwave · Singularity », nappe de nuit.

## Frame 26: 2 h 30 du matin (95.8-100.1s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-97.07s.png`)
- TC : 1:35,8 → 1:40,1 (4.3 s) · 🟪 ECR
- Voix : « 2 h du matin : d'après OpenCode, les clés ont pu être exposées dès cette heure-là. »
- Image : La frise horaire (graduations SF Mono, une lune en trait). Marqueur rouge **02:30**. Carte : l'e-mail de suivi d'OpenCode, recadré sur « The earliest possible exposure… 00:30 UTC ». **Les fins de clés de cet e-mail sont floutées.**
- Caméra : **Travelling latéral continu** le long de la frise pendant tout le chapitre (la caméra suit le temps qui passe).
- Texte : Micro gris : « 00:30 UTC = 2 h 30 à Paris ».
- Son : Pas d'horloge qui tic-taque : la nappe suffit.
- Médias : `captures/max-email-suivi.jpg` (flouter les 3 lignes « key ending… »)

## Frame 27: Les factures grimpent (100.1-102.0s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-101.21s.png`)
- TC : 1:40,1 → 1:42,0 (1.9 s) · 🟧 ANI
- Voix : « Dans la journée, les factures grimpent. »
- Image : Le soleil se lève sur la frise ; une courbe rouge de coûts monte le long de la frise.
- Caméra : Le travelling continue, légère montée.
- Texte : —
- Son : —

## Frame 28: Nerf (102.0-107.6s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-103.3s.png`)
- TC : 1:42,0 → 1:47,6 (5.6 s) · 🟪 ECR
- Voix : « Max reçoit un e-mail de Google : ses limites ont été “temporairement abaissées”. Google a nerfé son compte. »
- Image : Carte : l'e-mail de Google recadré ; surlignage jaune de « temporarily lowered the allowed usage limits ». Sur « nerfé », **tampon rouge « NERF »** qui claque sur la carte.
- Caméra : Arrêt du travelling sur la carte, poussée ×1,1.
- Texte : Tampon : contour rouge arrondi, 96 px, légèrement penché (pop 0,7 → 1,1 → 1).
- Son : `tick` (surlignage), `toggle` (tampon).
- Médias : `captures/max-email-google.jpg`

## Frame 29: Confirmé. OpenCode piraté. (107.6-113.9s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-108.77s.png`)
- TC : 1:47,6 → 1:53,9 (6.3 s) · 🟪 ECR
- Voix : « 17 h 30, Matt Johansen poste l'e-mail reçu par des clients : “Confirmé. OpenCode piraté. Clés volées.” »
- Image : Marqueur **17:30** sur la frise. La vraie capture du post de Matt (avec l'e-mail en image) ; surlignage de « Confirmed. OpenCode hacked. Keys stolen. »
- Caméra : Le travelling reprend jusqu'au marqueur, puis s'arrête sur la carte.
- Texte : Traduction grise. Micro : « 783 600 vues ». Le nom affiché est bien **Johansen**.
- Son : `slide`, `tick`.
- Médias : `captures/tw-mattjay.png`

## Frame 30: 1,4 % de la Console (113.9-121.4s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-115.22s.png`)
- TC : 1:53,9 → 2:01,4 (7.5 s) · 🟪 ECR
- Voix : « 20 h, OpenCode confirme une attaque “de distillation à grande échelle” sur 1,4 % des utilisateurs de la Console touchés. »
- Image : Marqueur **20:08**. La capture du post d'OpenCode : surlignage de « large scale distillation attack », puis de « 1.4% of OpenCode Console users ».
- Caméra : Travelling jusqu'au marqueur, poussée lente ×1,05.
- Texte : « 1,4 % » héros blanc dans la colonne droite.
- Son : `tick` ×2.
- Médias : `captures/tw-opencode-annonce.png`

## Frame 31: Retiens ce mot (121.4-123.6s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-122.66s.png`)
- TC : 2:01,4 → 2:03,6 (2.2 s) · ⬜ TXT
- Voix : « Retiens bien ce mot : distillation. »
- Image : Le mot « distillation » se détache du post et vient se poser au centre ; puis il se range en haut à gauche (il reviendra au chapitre 5).
- Caméra : Fixe.
- Texte : « distillation » 128 px blanc ; « retiens ce mot » gris.
- Son : `air`.

## Frame 32: Bloquées, remboursé (123.6-128.1s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-124.95s.png`)
- TC : 2:03,6 → 2:08,1 (4.5 s) · 🟧 ANI
- Voix : « Anthropic et Google bloquent les clés ; OpenAI rembourse, d'après TechCrunch. »
- Image : Trois logos en rang avec une pastille d'état : Anthropic « clés bloquées », Google « clés bloquées », OpenAI « rembourse » (vert).
- Caméra : Travelling qui longe les trois logos.
- Texte : Micro : « Source : TechCrunch, 19/10/2026 ».
- Son : —
- Médias : `logos/anthropic.svg`, `logos/google.svg`, `logos/openai.svg`

## Frame 33: Un peu frustrant (128.1-132.7s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-129.42s.png`)
- TC : 2:08,1 → 2:12,7 (4.6 s) · 🟪 ECR
- Voix : « Toujours d'après TechCrunch, en analysant l'attaque, Dax trouvait “un peu frustrant” que les IA refusent de l'aider. »
- Image : La capture de l'article TechCrunch : le titre, puis le passage « a bit frustrating » surligné en jaune.
- Caméra : Poussée ×1,3 du titre vers le passage.
- Texte : Traduction grise du passage.
- Son : `tick`.
- Médias : `captures/web-techcrunch.png` (passage à y ≈ 2730 px css)

## Frame 34: Les garde-fous (132.7-137.9s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-133.95s.png`)
- TC : 2:12,7 → 2:17,9 (5.2 s) · 🟧 ANI
- Voix : « Les garde-fous censés bloquer les pirates… bloquaient en réalité la victime. »
- Image : Avatar de Dax arrêté devant un bouclier « Refusé » ; derrière lui, une clé rouge passe sans être arrêtée.
- Caméra : Fixe, la clé rouge traverse le cadre.
- Texte : « Refusé » rouge.
- Son : —
- Médias : `images/avatar-thdxr.jpg`

## Frame 35: On ouvre le code (137.9-142.2s)
- act: Chapitre 2 · La nuit du 17 octobre
- status: posé (image `boards/stills/at-139.25s.png`)
- TC : 2:17,9 → 2:22,2 (4.3 s) · 🟧 ANI
- Voix : « Mais comment des clés se retrouvent dans la nature ? On ouvre le code. »
- Image : La frise arrive dans la nuit. Au bout, le logo GitHub en trait ; il s'ouvre comme une porte.
- Caméra : Fin du travelling, **poussée dans la porte** : enchaînement sur l'écran du chapitre 3.
- Texte : —
- Son : `air-long`.
- Médias : `logos/github.svg`

### Chapitre 3 · Comment tes clés étaient rangées

## Frame 36: Écran de chapitre 3 (142.2-145.2s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-143.66s.png`)
- TC : 2:22,2 → 2:25,2 (3.0 s) · 🟫 CHAP
- Voix : *(3 s sans voix)*
- Image : Écran de chapitre : station 3, « Comment tes clés étaient rangées ».
- Caméra : La caméra suit la clé, puis plonge vers le bas : le rail devient la **ligne de l'historique Git**.
- Texte : —
- Son : `air-long` + `tick`. Musique : « Intrigue », enquête.

## Frame 37: L'historique (145.2-149.1s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-146.57s.png`)
- TC : 2:25,2 → 2:29,1 (3.9 s) · 🟪 ECR
- Voix : « Le code de la Console est sur GitHub, avec tout son historique. »
- Image : Une liste de commits (la ligne Git et ses points) défile ; on s'arrête sur le **12 oct.**
- Caméra : **Descente verticale continue** le long de la ligne Git.
- Texte : Dates en SF Mono gris.
- Son : —

## Frame 38: La colonne credentials (149.1-154.9s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-150.44s.png`)
- TC : 2:29,1 → 2:34,9 (5.8 s) · 🟪 ECR
- Voix : « Jusqu'au 12 octobre, on y trouve une table “provider”, avec une colonne “credentials”… de type texte. »
- Image : Carte de code (vrai fichier `provider.sql.ts`, version d'avant le 12/10). La ligne 11 `credentials: text("credentials").notNull()` s'allume ; le mot `text` est entouré.
- Caméra : Poussée sur la ligne 11 (×1,3).
- Texte : Micro : « anomalyco/opencode · provider.sql.ts · commit 773d862 ».
- Son : `tick` (entourage).
- Médias : `code/provider.sql.ts.txt`

## Frame 39: Telle que tu l'as collée (154.9-160.0s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-156.23s.png`)
- TC : 2:34,9 → 2:40,0 (5.1 s) · 🟧 ANI
- Voix : « Quand tu enregistres ta clé, elle atterrit dans cette colonne telle que tu l'as collée. »
- Image : Le code devient une table « provider » (id · workspace · provider · **credentials**). **La clé arrive** et sa valeur s'écrit lettre par lettre dans la cellule : `sk-proj-Ab12Cd34…Wx98Yz76` (clé inventée).
- Caméra : La caméra suit la clé jusqu'à la cellule.
- Texte : Étiquette rouge « en clair ».
- Son : `tick` doux pendant la frappe.

## Frame 40: La page de réglages (160.0-165.0s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-161.25s.png`)
- TC : 2:40,0 → 2:45,0 (5.0 s) · 🟧 ANI
- Voix : « La preuve, c'est la page de réglages. Elle t'affiche ta clé masquée : les 8 premiers caractères, »
- Image : La ligne de réglages recréée d'après le vrai composant : « OpenAI · sk-proj-…Wx98Yz76 ». Une accolade se dessine sous les 8 premiers caractères.
- Caméra : Glissement de la table vers la page de réglages.
- Texte : « 8 » sous l'accolade.
- Son : —

## Frame 41: slice(-8) (165.0-170.5s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-166.25s.png`)
- TC : 2:45,0 → 2:50,5 (5.5 s) · 🟪 ECR
- Voix : « 3 points et les 8 derniers caractères. Et ce masque est calculé à partir de la valeur stockée. »
- Image : Accolades sur « … » et sur les 8 derniers. Puis la vraie fonction `maskCredentials` : `slice(0, 8)` et `slice(-8)` surlignés (2 s maximum). Une flèche relie la cellule complète au masque.
- Caméra : Recul pour voir la cellule et le masque ensemble.
- Texte : —
- Son : —
- Médias : `code/provider-section.tsx.txt` (l. 18-19)

## Frame 42: Il faut avoir ta clé (170.5-173.8s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-171.82s.png`)
- TC : 2:50,5 → 2:53,8 (3.3 s) · ⬜ TXT
- Voix : « Pour t'afficher la fin de ta clé, il faut avoir ta clé. »
- Image : Texte seul sur noir.
- Caméra : Fixe.
- Texte : « Pour afficher la fin de ta clé… » gris 56 px / « il faut avoir ta clé. » blanc 96 px.
- Son : —

## Frame 43: Mème : C'est logique (173.8-175.3s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-174.72s.png`)
- TC : 2:53,8 → 2:55,3 (1.5 s) · 🩷 MEM
- Voix : *(mème, 1,2 s)*
- Image : **Coupe franche** : « C'est logique ! » (Steelorse).
- Caméra : —
- Texte : —
- Son : Voix et musique coupées.
- Médias : PACK › MEMES › NORMAL › « Steelorse - C_est logique.mp4 » (1,25 s)

## Frame 44: La devinette (175.3-180.7s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-176.58s.png`)
- TC : 2:55,3 → 3:00,7 (5.4 s) · 🟧 ANI
- Voix : « Alors, il est légitime de se dire : pourquoi est-ce qu'ils ne l'ont pas hashée comme un mot de passe ? Prends deux secondes pour y réfléchir. »
- Image : Deux colonnes : « Mot de passe » | « Clé API ».
- Caméra : Fixe.
- Texte : Titres 96 px.
- Son : —

## Frame 45: Deux secondes (180.7-182.7s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-182.07s.png`)
- TC : 3:00,7 → 3:02,7 (2.0 s) · 🟧 ANI
- Voix : *(2 s sans voix)*
- Image : Un chrono circulaire se dessine en 2 s entre les deux colonnes.
- Caméra : Fixe.
- Texte : « 2 s » SF Mono.
- Son : `tick` sur chaque seconde. Musique en retrait.

## Frame 46: Le hash du mot de passe (182.7-189.7s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-183.98s.png`)
- TC : 3:02,7 → 3:09,7 (7.0 s) · 🟧 ANI
- Voix : « Un mot de passe, le site n'a jamais besoin de le relire : il hashe ce que tu tapes et compare les deux empreintes. »
- Image : Colonne gauche : « •••••••• » entre dans une boîte « hash » et ressort en empreinte `9f2c…e1` ; elle se pose sur l'empreinte stockée identique : coche verte.
- Caméra : La caméra suit l'empreinte vers le bas de la colonne.
- Texte : —
- Son : `absorb` (boîte hash), `poweron` court (coche).

## Frame 47: OpenAI n'en fait rien (189.7-194.6s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-190.45s.png`)
- TC : 3:09,7 → 3:14,6 (4.9 s) · 🟧 ANI
- Voix : « Une clé API, il faut l'envoyer en entier au fournisseur, à chaque requête. Une empreinte, OpenAI n'en fait rien. »
- Image : Colonne droite : la clé entière part vers le logo OpenAI à chaque requête (3 allers rapides). Puis une empreinte part à sa place et revient avec un tampon rouge « 401 · invalide ».
- Caméra : Panoramique vers la droite avec la clé.
- Texte : Tampon rouge.
- Son : `air` ×1, `toggle` (tampon).
- Médias : `logos/openai.svg`

## Frame 48: Celui qui fabrique la clé (194.6-203.9s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-195.99s.png`)
- TC : 3:14,6 → 3:23,9 (9.3 s) · 🟧 ANI
- Voix : « Le seul qui peut se contenter d'une empreinte, c'est celui qui fabrique la clé : il n'a qu'à vérifier celle que tu lui montres. Un outil qui s'en sert à ta place doit pouvoir la relire. »
- Image : Chaîne « Toi → OpenCode → OpenAI ». Chez OpenAI (le fabricant) : un registre d'empreintes, coche verte. Chez OpenCode, au milieu : la clé entière, qu'il doit relire pour la renvoyer.
- Caméra : **Recul** pour voir toute la chaîne.
- Texte : Libellés 32 px : « fabrique la clé » / « s'en sert à ta place ».
- Son : —

## Frame 49: Le coffre (203.9-211.5s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-205.23s.png`)
- TC : 3:23,9 → 3:31,5 (7.6 s) · 🟧 ANI
- Voix : « Donc une clé API, on la chiffre, avec une deuxième clé rangée ailleurs, dans un coffre. Pour la lire, le pirate doit voler deux choses au lieu d'une. »
- Image : Retour sur la cellule : la clé devient du charabia chiffré. Un coffre (picto) apparaît à droite avec une 2e clé dedans. Deux contours rouges « 1 » et « 2 » : ce que le pirate doit voler.
- Caméra : Panoramique de la base vers le coffre.
- Texte : « 1 » et « 2 » en rouge.
- Son : `absorb` (la clé entre dans le coffre).

## Frame 50: Pas de coffre (211.5-214.4s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-212.84s.png`)
- TC : 3:31,5 → 3:34,4 (2.9 s) · ⬜ TXT
- Voix : « Dans ce code-là, il n'y a pas de coffre. »
- Image : Le coffre se dissout ; la cellule redevient lisible, seule. Puis tout s'éteint et il ne reste que le mot choc.
- Caméra : Fixe.
- Texte : « Pas de coffre. » blanc 240 px, tenu 1,2 s.
- Son : `powerdown`, **musique coupée**, silence total pendant le mot choc.

## Frame 51: Le disque chiffré (214.4-222.8s)
- act: Chapitre 3 · Comment tes clés étaient rangées
- status: posé (image `boards/stills/at-215.72s.png`)
- TC : 3:34,4 → 3:42,8 (8.4 s) · 🟧 ANI
- Voix : « Pour être honnête, l'hébergeur chiffre peut-être ses disques. Ça protège si quelqu'un repart avec le disque, pas face à quelqu'un qui peut interroger directement la base. »
- Image : Un disque (picto) avec un cadenas gris « peut-être ». Un voleur repart avec le disque : illisible (vert). Puis une requête tapée `SELECT credentials FROM provider;` : la réponse affiche la clé en clair (rouge).
- Caméra : Fixe, puis poussée sur la requête.
- Texte : Étiquette « peut-être » grise.
- Son : Musique de l'enquête reprend doucement.

### Appel à l'abonnement

## Frame 52: Abonne-toi (222.8-233.2s)
- act: Appel à l'abonnement
- status: posé (image `boards/stills/at-224.15s.png`)
- TC : 3:42,8 → 3:53,2 (10.4 s) · 🟧 ANI
- Voix : « Si t'aimes voir ce genre de soucis sous le capot des outils que tu utilises tous les jours, alors abonne-toi sur ma chaîne Technovore. On les ouvre un par un, et c'est le seul abonnement qui ne te prélèvera jamais rien. »
- Image : Feuille iOS (`#1c1c1e`) « Technovore » avec un bouton « S'abonner » qui passe à « Abonné ». Ligne de prix « 0,00 € / mois · pour toujours » en vert. Derrière, la table « provider » floutée.
- Caméra : La feuille monte par le bas (expo.out).
- Texte : Prix en SF Mono vert.
- Son : `toggle` sur le bouton.

### Chapitre 4 · L'ancien système

## Frame 53: Écran de chapitre 4 (233.2-236.2s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-234.54s.png`)
- TC : 3:53,2 → 3:56,2 (3.0 s) · 🟫 CHAP
- Voix : *(3 s sans voix)*
- Image : Écran de chapitre : station 4, « L'ancien système ».
- Caméra : La caméra suit la clé, puis glisse vers une enveloppe (l'e-mail).
- Texte : —
- Son : `air-long` + `tick`. Musique « Intrigue » (suite).

## Frame 54: Ancien système (236.2-242.4s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-237.45s.png`)
- TC : 3:56,2 → 4:02,4 (6.2 s) · 🟪 ECR
- Voix : « Dans l'e-mail envoyé aux victimes, OpenCode parle d'un accès à un “ancien système qu'on était en train de démanteler”. »
- Image : La capture de l'e-mail aux victimes ; surlignage de « legacy system that we were in the process of decommissioning ».
- Caméra : Poussée lente ×1,05.
- Texte : Traduction grise.
- Son : `tick`.
- Médias : `captures/email-victimes-reddit.jpg`

## Frame 55: Rien ne relie (242.4-247.0s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-243.88s.png`)
- TC : 4:02,4 → 4:07,0 (4.6 s) · 🟧 ANI
- Voix : « Rien ne relie ce qui suit à ce système : OpenCode n'a pas dit où le pirate est entré. »
- Image : Un fil pointillé part de l'e-mail vers la droite… et se coupe net.
- Caméra : La caméra suit le fil puis s'arrête sur la coupure.
- Texte : « Point d'entrée : non communiqué » gris.
- Son : —

## Frame 56: Le piège (247.0-249.5s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-248.3s.png`)
- TC : 4:07,0 → 4:09,5 (2.5 s) · ⬜ TXT
- Voix : « Mais en vrai, c'est un piège que tout dev devrait connaître. »
- Image : Texte seul.
- Caméra : Fixe.
- Texte : « Le piège que tout dev devrait connaître » 96 px.
- Son : —

## Frame 57: Le commit du 12 octobre (249.5-254.2s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-250.64s.png`)
- TC : 4:09,5 → 4:14,2 (4.7 s) · 🟪 ECR
- Voix : « Le 12 octobre, un commit retire l'ancienne base de données du code de la Console. »
- Image : La page GitHub du commit b9ca4d2 (thème sombre) : titre « remove legacy database from Console » surligné ; le compteur « −183 758 » défile en rouge, « +123 » en vert.
- Caméra : Poussée sur le titre, puis sur le compteur.
- Texte : « −183 758 lignes » rouge 240 px.
- Son : `tick`.
- Médias : `captures/web-github-commit.png`

## Frame 58: Mème : You're deleting all my data (254.2-255.6s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-255.12s.png`)
- TC : 4:14,2 → 4:15,6 (1.4 s) · 🩷 MEM
- Voix : *(mème, 1,1 s)*
- Image : **Coupe franche** : Silicon Valley, « You're deleting all my data! ».
- Caméra : —
- Texte : Sous-titre FR : « Tu supprimes toutes mes données ! »
- Son : Voix et musique coupées.
- Médias : `memes/silicon-valley-delete-all.mp4`, 5,15 → 6,25 s

## Frame 59: Seulement référencée (255.6-262.0s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-256.87s.png`)
- TC : 4:15,6 → 4:22,0 (6.4 s) · 🟪 ECR
- Voix : « Dans leur code d'infrastructure, cette base de production n'a jamais été créée par le code. Elle est seulement référencée. »
- Image : Carte de code `infra/console.ts` (vraies lignes 14 à 26) : `planetscale.getBranchOutput(...)` surligné avec l'étiquette « référencée (get) » ; en gris, `new planetscale.Branch(...)` « créée (new) : hors production seulement ».
- Caméra : Poussée sur la ligne `getBranchOutput`.
- Texte : Étiquettes 32 px.
- Son : `tick`.
- Médias : `code/console.ts.txt`

## Frame 60: Elle existe, elle est là (262.0-264.8s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-263.3s.png`)
- TC : 4:22,0 → 4:24,8 (2.8 s) · 🟧 ANI
- Voix : « En gros : elle existe, elle est là. »
- Image : Un cylindre « base de production » (picto) ; une flèche le désigne.
- Caméra : Recul du code vers le cylindre.
- Texte : « elle existe, elle est là » gris 44 px.
- Son : —

## Frame 61: Le mot de passe saute (264.8-268.4s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-266.07s.png`)
- TC : 4:24,8 → 4:28,4 (3.6 s) · 🟪 ECR
- Voix : « Son mot de passe, créé par le code, saute au déploiement suivant. »
- Image : La ligne `new planetscale.Password(...)` surlignée ; le picto mot de passe à côté du cylindre se dissout.
- Caméra : Fixe.
- Texte : —
- Son : `dissolve`.

## Frame 62: La base reste (268.4-270.3s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-269.66s.png`)
- TC : 4:28,4 → 4:30,3 (1.9 s) · ⬜ TXT
- Voix : « La base reste. »
- Image : Le cylindre seul, plein de clés rouges.
- Caméra : Fixe, tenu 0,7 s.
- Texte : « La base reste. » 128 px.
- Son : Musique très basse.

## Frame 63: La taverne (270.3-278.2s)
- act: Chapitre 4 · L'ancien système
- status: posé (image `boards/stills/at-271.56s.png`)
- TC : 4:30,3 → 4:38,2 (7.9 s) · 🟧 ANI
- Voix : « En gros, c'est comme si tu retirais un personnage de ton équipe dans un jeu : il disparaît de ton écran, mais il attend toujours à la taverne avec tout son inventaire. »
- Image : Barre d'équipe de RPG : Appli, Console, Proxy et **la forgeronne de Monster Hunter Wilds** (la « Base »). Elle quitte l'équipe ; la caméra la suit jusqu'à l'enseigne « Taverne », où elle attend avec son inventaire (grille 4 × 4) plein de clés rouges.
- Caméra : **La caméra suit le perso** qui quitte l'équipe et entre dans la taverne (travelling 1,2 s).
- Texte : « Inventaire : 16 clés » SF Mono.
- Son : `slide`, puis `bubble` à l'ouverture de l'inventaire ; musique « The Fantasy » (Fuzzeke) pendant la taverne.

### Chapitre 5 · Pourquoi tes clés valent de l'or
- Médias : `assets/forgerone_mhwilds.png`

## Frame 64: Écran de chapitre 5 (278.2-281.2s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-279.58s.png`)
- TC : 4:38,2 → 4:41,2 (3.0 s) · 🟫 CHAP
- Voix : *(3 s sans voix)*
- Image : Écran de chapitre : station 5, « Pourquoi tes clés valent de l'or ».
- Caméra : La caméra suit la clé, puis la clé se change en bulle « ok ».
- Texte : —
- Son : **Musique coupée net** (relance à 55 %) ; seul le `air-long`.

## Frame 65: La question du début (281.2-285.4s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-282.29s.png`)
- TC : 4:41,2 → 4:45,4 (4.2 s) · 🟧 ANI
- Voix : « Il me reste la question du début : pourquoi payer, avec l'argent d'un autre, pour un “ok” ? »
- Image : **Retour de la bulle « ok »**, seule au centre, au même cadrage qu'au plan 10.
- Caméra : Fixe.
- Texte : —
- Son : Silence musical ; la musique (« Dark Ambient ») revient sur « Pour y répondre ».

## Frame 66: Ce que vaut une clé (285.4-289.2s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-286.7s.png`)
- TC : 4:45,4 → 4:49,2 (3.8 s) · 🟧 ANI
- Voix : « Pour y répondre, il faut savoir ce que vaut une clé API en 2026. »
- Image : La bulle redevient la clé ; une étiquette de prix « ? $ » s'y accroche.
- Caméra : Fixe.
- Texte : —
- Son : —

## Frame 67: Mème : la distillation (289.2-292.8s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-291.2s.png`)
- TC : 4:49,2 → 4:52,8 (3.6 s) · 🩷 MEM
- Voix : « Le mot de l'annonce, distillation, c'est copier sur le premier de la classe : »
- Image : « distillation » revient du coin où on l'avait rangé (plan 31). Ton mème dans une carte arrondie : Anthropic boit « l'Internet public » à la noix de coco… et les labos boivent dans Anthropic.
- Caméra : Fixe, poussée lente ×1,00 → ×1,04.
- Texte : « distillation » 96 px au-dessus de la carte.
- Son : —
- Médias : `assets/distillation_meme.jpeg`. Il écrit « Chinese AI companies » : c'est raccord avec l'accusation d'Anthropic qui suit (DeepSeek, Moonshot, MiniMax), mais on ne le relie jamais au pirate d'OpenCode.

## Frame 68: Distillation (292.8-299.4s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-294.5s.png`)
- TC : 4:52,8 → 4:59,4 (6.6 s) · 🟧 ANI
- Voix : « tu poses des millions de questions à un gros modèle, et tu entraînes un petit modèle à partir des réponses, pour beaucoup moins cher. »
- Image : Deux disques : un gros « gros modèle », un petit qui « copie ». Un flux de points (les questions) va du petit au gros ; les réponses reviennent.
- Caméra : La carte du mème s'efface, poussée sur le petit modèle.
- Texte : « ×1 000 000 » SF Mono ; « pour beaucoup moins cher » gris.
- Son : —

## Frame 69: 24 000 faux comptes (299.4-306.5s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-300.32s.png`)
- TC : 4:59,4 → 5:06,5 (7.1 s) · 🟪 ECR
- Voix : « En février 2026, Anthropic a accusé DeepSeek, Moonshot et MiniMax d'avoir fait ça avec environ 24 000 faux comptes. »
- Image : Capture de l'article d'Anthropic ; puis 3 logos (DeepSeek, Moonshot, MiniMax) et une grille de points gris (les faux comptes).
- Caméra : Recul de l'article vers la grille.
- Texte : « 24 000 faux comptes » héros.
- Son : —
- Médias : `captures/web-anthropic-distillation.png`, `logos/deepseek.svg`, `logos/moonshotai.svg`, `logos/minimax.svg`

## Frame 70: Bannis en moins de 2 h (306.5-312.4s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-307.8s.png`)
- TC : 5:06,5 → 5:12,4 (5.9 s) · 🟪 ECR
- Voix : « Le 12 octobre, il annonce de nouvelles défenses, avec des faux comptes souvent bannis en moins de deux heures. »
- Image : Capture « Strengthening our defenses against distillation attacks » ; les points de la grille s'éteignent par paquets.
- Caméra : Fixe.
- Texte : « < 2 h » SF Mono.
- Son : `dissolve` léger.
- Médias : `captures/web-anthropic-defenses.png`

## Frame 71: Le 31 août (312.4-316.7s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-313.61s.png`)
- TC : 5:12,4 → 5:16,7 (4.3 s) · 🟧 ANI
- Voix : « Et une de ces protections ne couvre que les comptes créés à partir du 31 août. »
- Image : Une frise de dates : à partir du **31 août**, la zone est couverte par un bouclier ; avant, non.
- Caméra : Panoramique le long de la frise.
- Texte : « 31 août » SF Mono.
- Son : —

## Frame 72: L'hypothèse (316.7-326.2s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-317.99s.png`)
- TC : 5:16,7 → 5:26,2 (9.5 s) · 🟧 ANI
- Voix : « Là, c'est une hypothèse, personne ne l'a confirmé : pour un pirate, le compte d'un vrai développeur, ouvert avant cette date, vaut sans doute bien plus qu'un faux compte tout neuf. »
- Image : Étiquette « Hypothèse » (contour gris) en haut à gauche pendant tout le plan. Une porte blindée se ferme sur une file de faux comptes neufs ; un vieux compte « dev · 2024 » s'approche de la porte de service, un « ? » au-dessus.
- Caméra : Travelling le long de la file jusqu'à la porte de service.
- Texte : « Hypothèse : personne ne l'a confirmé » gris.
- Son : —

## Frame 73: Le seul objectif (326.2-334.7s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-327.49s.png`)
- TC : 5:26,2 → 5:34,7 (8.5 s) · 🟪 ECR
- Voix : « Et les clés volées, ça se revend. Dans son rapport de septembre, Anthropic écrit que voler des clés API est devenu le seul objectif de plusieurs groupes criminels. »
- Image : Capture du rapport de menace d'Anthropic : « the sole objective » surligné.
- Caméra : Poussée ×1,3 vers le passage.
- Texte : Traduction grise.
- Son : `tick`.
- Médias : `captures/web-anthropic-threat.png` (passage à y ≈ 27 340 px css : recadrer)

## Frame 74: Le farming (334.7-342.0s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-335.93s.png`)
- TC : 5:34,7 → 5:42,0 (7.3 s) · 🟧 ANI
- Voix : « Des réseaux de revente font tourner les clés volées jusqu'à les vider. C'est un peu comme du farming, mais avec ta carte bancaire. »
- Image : **La caméra suit la clé rouge** qui passe de main en main le long d'une chaîne de 5 nœuds ; son solde baisse à chaque passage : 1 000 $ → 640 $ → 210 $ → 0 $ → −2,15 $.
- Caméra : Travelling latéral continu calé sur la clé.
- Texte : Soldes en SF Mono ; le dernier en rouge.
- Son : `slide` sur 2 passages.

## Frame 75: 480 000 $ par mois (342.0-353.9s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-343.22s.png`)
- TC : 5:42,0 → 5:53,9 (11.9 s) · 🟪 ECR
- Voix : « En juillet, sans aucun lien avec la fuite, Dax racontait avoir banni une seule personne qui possédait 8 000 faux comptes OpenCode : 480 000 $ de tokens revendus par mois. Faut pas abuser, en vrai. »
- Image : Capture du post de Dax avec son image (les policiers et les tas de jetons) ; surlignage de « 8,000 fraudulent » et « $480,000 ».
- Caméra : Poussée sur les tas de jetons sur « faut pas abuser ».
- Texte : Étiquette grise « sans lien avec la fuite ». « 480 000 $ / mois » héros.
- Son : `tick`.
- Médias : `captures/tw-dax-ban.png`

## Frame 76: Une carte bancaire (353.9-358.3s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-355.2s.png`)
- TC : 5:53,9 → 5:58,3 (4.4 s) · 🟧 ANI
- Voix : « En fait, une clé API, c'est une carte bancaire déjà branchée sur une IA. »
- Image : La clé se transforme en carte bancaire (puce, `sk-proj-…Yz76` gravé), branchée dans un connecteur. **La phrase-thèse**.
- Caméra : Fixe, tenu 1,5 s.
- Texte : « Une clé API, c'est une carte bancaire » blanc / « déjà branchée sur une IA » gris.
- Son : `toggle` au branchement.

## Frame 77: 1 sur 8 966 (358.3-364.8s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-359.59s.png`)
- TC : 5:58,3 → 6:04,8 (6.5 s) · 🟧 ANI
- Voix : « Alors, ce “ok” ? Max l'a publié comme un exemple : une requête sur près de 9 000, pas forcément la première. »
- Image : Retour de la bulle « ok ». Elle rétrécit et n'est plus qu'un point parmi une grille de 8 966 points.
- Caméra : **Grand recul** (2 s, power3.inOut).
- Texte : « 1 / 8 966 » SF Mono.
- Son : `air-long`.

## Frame 78: Test de clé ? (364.8-372.1s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-366.07s.png`)
- TC : 6:04,8 → 6:12,1 (7.3 s) · 🟧 ANI
- Voix : « Seule, elle ne prouve rien. Mais on n'entraîne pas un modèle avec “réponds ok”. Ça ressemble plutôt à un test : est-ce que cette clé marche ? »
- Image : La bulle reprend sa place ; une étiquette s'y accroche : « test de clé ? ». Une clé envoie « ping », reçoit « ok » : coche.
- Caméra : Poussée inverse jusqu'à la bulle.
- Texte : Étiquette contour gris.
- Son : `bubble`.

## Frame 79: Très bizarre (372.1-377.5s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-373.29s.png`)
- TC : 6:12,1 → 6:17,5 (5.4 s) · 🟪 ECR
- Voix : « Donc, ranger un vol de clé sous le mot distillation, Nathan Lambert trouve ça très bizarre. »
- Image : Capture du post de Nathan Lambert : « something very odd » et « looped under the same term » surlignés.
- Caméra : Poussée lente.
- Texte : Traduction grise.
- Son : `tick`.
- Médias : `captures/tw-lambert.png`

## Frame 80: Qui l'a envoyée ? (377.5-379.9s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-378.81s.png`)
- TC : 6:17,5 → 6:19,9 (2.4 s) · 🟧 ANI
- Voix : « Et une requête en chinois ne dit pas qui l'a envoyée. »
- Image : La bulle « 请回复ok » ; l'avatar de l'expéditeur est un cercle vide avec un « ? ».
- Caméra : Fixe.
- Texte : —
- Son : —

## Frame 81: On ne sait pas (379.9-385.8s)
- act: Chapitre 5 · Pourquoi tes clés valent de l'or
- status: posé (image `boards/stills/at-380.95s.png`)
- TC : 6:19,9 → 6:25,8 (5.9 s) · ⬜ TXT
- Voix : « À ce jour, OpenCode n'a publié ni le point d'entrée, ni le nombre de clés. On ne sait pas qui, ni pourquoi. »
- Image : Fiche : « Point d'entrée : — » / « Clés touchées : — », datée du 20/10/2026.
- Caméra : Fixe.
- Texte : « On ne sait pas. » gris 96 px.
- Son : Musique qui retombe, 1 s de pause.

### Chapitre 6 · Le réglage qui décide de ta facture

## Frame 82: Écran de chapitre 6 (385.8-388.8s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-387.14s.png`)
- TC : 6:25,8 → 6:28,8 (3.0 s) · 🟫 CHAP
- Voix : *(3 s sans voix)*
- Image : Écran de chapitre : station 6, « Le réglage qui décide de ta facture ».
- Caméra : La caméra suit la clé ; la clé redevient blanche (c'est la tienne).
- Texte : —
- Son : `air-long` + `tick`. **La musique « maison » revient** (« Future Minimal ») sur un premier temps.

## Frame 83: Ton plafond (388.8-394.7s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-390.05s.png`)
- TC : 6:28,8 → 6:34,7 (5.9 s) · 🟧 ANI
- Voix : « Maintenant, ta clé à toi. Le jour où elle fuit, combien tu perds dépend surtout d'un réglage : ton plafond. »
- Image : Ta clé blanche au centre ; au-dessus, une ligne « plafond » se dessine.
- Caméra : Fixe.
- Texte : « ton plafond » 96 px.
- Son : —

## Frame 84: Sous zéro (394.7-401.7s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-395.79s.png`)
- TC : 6:34,7 → 6:41,7 (7.0 s) · 🟧 ANI
- Voix : « Regarde le −2,15 $ de Max : son crédit est passé sous zéro. Le compteur ne coupe pas pile à zéro. »
- Image : Une jauge de crédit se vide, dépasse 0 et glisse dans le rouge jusqu'à « −2,15 $ » (rappel du plan 6).
- Caméra : Fixe.
- Texte : « −2,15 $ » rouge.
- Son : —

## Frame 85: Une alerte ne bloque rien (401.7-406.2s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-403.05s.png`)
- TC : 6:41,7 → 6:46,2 (4.5 s) · 🟪 ECR
- Voix : « Chez OpenAI, une alerte de dépense ne bloque rien, c'est dans leur doc. »
- Image : Capture de la doc OpenAI : « Spend alerts do not enforce a cap » surligné. Une cloche sonne, le compteur continue de tourner.
- Caméra : Poussée ×1,2 sur la phrase.
- Texte : Traduction grise.
- Son : `bubble` (la cloche, pas d'alarme).
- Médias : `captures/web-openai-spend.png`

## Frame 86: Pas instantané (406.2-410.9s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-407.06s.png`)
- TC : 6:46,2 → 6:50,9 (4.7 s) · 🟪 ECR
- Voix : « Il faut donc une vraie limite, à part. Et même cette limite, elle n'est pas appliquée instantanément. »
- Image : « Hard spend limit » ; « Enforcement is not instantaneous » surligné. Le compteur dépasse un peu la ligne avant de s'arrêter.
- Caméra : Fixe.
- Texte : —
- Son : `tick`.

## Frame 87: Prépayé (410.9-414.5s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-412.21s.png`)
- TC : 6:50,9 → 6:54,5 (3.6 s) · 🟧 ANI
- Voix : « Chez Anthropic, c'est du prépayé : quand c'est vide, ça s'arrête. »
- Image : Une jauge prépayée se vide et s'arrête net à 0 (vert « stop »).
- Caméra : Fixe.
- Texte : —
- Son : `powerdown` court.

## Frame 88: Le rechargement automatique (414.5-420.9s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-415.78s.png`)
- TC : 6:54,5 → 7:00,9 (6.4 s) · 🟧 ANI
- Voix : « Sauf si t'as activé le rechargement automatique : là, ton solde se recharge avec ta carte, pour le pirate. »
- Image : Interrupteur iOS « Rechargement automatique » qui passe à ON ; la jauge se remplit avec une carte bancaire… et se vide aussitôt vers une clé rouge.
- Caméra : Glissement de la jauge vers la clé rouge.
- Texte : —
- Son : `toggle`.

## Frame 89: Le pire abonnement (420.9-423.1s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-422.18s.png`)
- TC : 7:00,9 → 7:03,1 (2.2 s) · ⬜ TXT
- Voix : « C'est le pire abonnement de ta vie, en vrai. »
- Image : Texte seul.
- Caméra : Fixe.
- Texte : « Le **pire abonnement** de ta vie. » (rouge sur « pire abonnement »).
- Son : —

## Frame 90: Mème : Merci aux clients fidèles (423.1-425.0s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-424.26s.png`)
- TC : 7:03,1 → 7:05,0 (1.9 s) · 🩷 MEM
- Voix : *(mème, 1,7 s)*
- Image : **Coupe franche** : « Merci aux clients fidèles ».
- Caméra : —
- Texte : —
- Son : Voix et musique coupées.
- Médias : PACK › MEMES › NORMAL › « Merci aux clients fidèles.mp4 », 0,00 → 1,70 s

## Frame 91: Les paliers (425.0-432.2s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-426.33s.png`)
- TC : 7:05,0 → 7:12,2 (7.2 s) · 🟪 ECR
- Voix : « Sans réglage, ton plafond, c'est celui de ton palier : 500 $ par mois au premier, 200 000 $ tout en haut. »
- Image : L'escalier des paliers (d'après la doc platform.claude.com) : chaque marche porte son plafond ; la dernière, « 200 000 $ », en rouge.
- Caméra : **La caméra monte l'escalier** (tilt continu, 2,5 s).
- Texte : Montants en SF Mono. Micro : « Source : platform.claude.com ».
- Son : `air-long` pendant la montée.
- Médias : `captures/web-claude-ratelimits.png`

## Frame 92: Dix minutes de retard (432.2-439.4s)
- act: Chapitre 6 · Le réglage qui décide de ta facture
- status: posé (image `boards/stills/at-433.5s.png`)
- TC : 7:12,2 → 7:19,4 (7.2 s) · 🟧 ANI
- Voix : « Chez Google, la facture de Gemini peut avoir jusqu'à une dizaine de minutes de retard. Pour un script qui tourne à fond, c'est long. »
- Image : Logo Gemini. Deux compteurs : « consommation réelle » qui file, « facture » qui suit avec un retard visible.
- Caméra : Fixe.
- Texte : « ≈ 10 min de retard » SF Mono. Micro : « Source : ai.google.dev ».
- Son : —
- Médias : `logos/googlegemini.svg`, `captures/web-gemini-billing.png` (référence)

### Chapitre 7 · Ta checklist pour ce soir

## Frame 93: Écran de chapitre 7 (439.4-442.3s)
- act: Chapitre 7 · Ta checklist pour ce soir
- status: posé (image `boards/stills/at-440.84s.png`)
- TC : 7:19,4 → 7:22,3 (2.9 s) · 🟫 CHAP
- Voix : « Donc ce soir : »
- Image : Écran de chapitre : la clé arrive à la station 7, où attend la carte checklist de l'accroche. « Ta checklist pour ce soir » (dit par ta voix).
- Caméra : La caméra suit la clé jusqu'à la carte, puis pousse dans la carte.
- Texte : —
- Son : `air-long`. Musique « Future Minimal » : chaque coche tombe sur un temps.

## Frame 94: 1. Révoque (442.3-448.5s)
- act: Chapitre 7 · Ta checklist pour ce soir
- status: posé (image `boards/stills/at-443.56s.png`)
- TC : 7:22,3 → 7:28,5 (6.2 s) · 🟧 ANI
- Voix : « Un, si t'as reçu l'e-mail, révoque ta clé chez le fournisseur, immédiatement. La supprimer de la Console ne la désactive pas. »
- Image : La carte checklist, nette cette fois. Ligne 1 se coche (vert). Sous-ligne rouge : « La supprimer de la Console ≠ la désactiver ».
- Caméra : **Défilement vertical continu** de la carte, ligne par ligne, pendant tout le chapitre.
- Texte : Lignes 44 px.
- Son : `toggle` (coche).

## Frame 95: 2. Une nouvelle clé Claude (448.5-454.5s)
- act: Chapitre 7 · Ta checklist pour ce soir
- status: posé (image `boards/stills/at-449.82s.png`)
- TC : 7:28,5 → 7:34,5 (6.0 s) · 🟪 ECR
- Voix : « Deux, sans e-mail mais avec une clé Claude dans OpenCode, Anthropic conseille d'en créer une nouvelle, par prudence. »
- Image : Ligne 2 se coche. À droite, la capture du post de Lydia Hallie (Anthropic) : « please create a new one! » surligné.
- Caméra : Défilement + la capture entre par la droite.
- Texte : —
- Son : `toggle`.
- Médias : `captures/tw-lydia.png`

## Frame 96: 3. Une clé par outil (454.5-458.8s)
- act: Chapitre 7 · Ta checklist pour ce soir
- status: posé (image `boards/stills/at-455.86s.png`)
- TC : 7:34,5 → 7:38,8 (4.3 s) · 🟧 ANI
- Voix : « Trois, une clé par outil : si elle fuit, tu sais d'où, et tu ne coupes qu'elle. »
- Image : Ligne 3 : trois petites clés, chacune avec son étiquette d'outil ; l'une passe au rouge et se coupe seule.
- Caméra : Défilement.
- Texte : —
- Son : `toggle`.

## Frame 97: 4. Une vraie limite (458.8-462.1s)
- act: Chapitre 7 · Ta checklist pour ce soir
- status: posé (image `boards/stills/at-460.14s.png`)
- TC : 7:38,8 → 7:42,1 (3.3 s) · 🟧 ANI
- Voix : « Quatre, une vraie limite, et pas de rechargement automatique. »
- Image : Ligne 4 : l'interrupteur « Rechargement automatique » repasse à OFF (rappel du plan 88) ; une ligne « limite » se pose.
- Caméra : Défilement.
- Texte : —
- Son : `toggle`.

## Frame 98: 5. Les clés oubliées (462.1-467.0s)
- act: Chapitre 7 · Ta checklist pour ce soir
- status: posé (image `boards/stills/at-463.16s.png`)
- TC : 7:42,1 → 7:47,0 (4.9 s) · 🟧 ANI
- Voix : « Cinq, supprime les clés oubliées. On en a tous une qui traîne quelque part d'un vieux tuto. »
- Image : Ligne 5 : une clé grise poussiéreuse dans un fichier « tuto-2023.md » se dissout. La checklist complète est tenue 1 s.
- Caméra : Recul pour voir la checklist entière.
- Texte : —
- Son : `dissolve`.

### Fin et écran de fin

## Frame 99: Moi, jamais (467.0-471.5s)
- act: Fin et écran de fin
- status: posé (image `boards/stills/at-468.36s.png`)
- TC : 7:47,0 → 7:51,5 (4.5 s) · 🟧 ANI
- Voix : « Pour moi, je te l'ai dit dès le début : j'ai jamais collé de clé dans ce genre d'outil. »
- Image : Retour au plateau : ta tour de PC posée au sol, aucune clé à l'écran.
- Caméra : La checklist s'efface vers le haut, la caméra descend sur le plateau.
- Texte : —
- Son : —

## Frame 100: L'appli oui, la Console non (471.5-478.8s)
- act: Fin et écran de fin
- status: posé (image `boards/stills/at-472.81s.png`)
- TC : 7:51,5 → 7:58,8 (7.3 s) · 🟧 ANI
- Voix : « Pourtant, je compte utiliser OpenCode, et après avoir lu ce code, c'est pas demain que je vais commencer à coller des clés API partout. »
- Image : Le terminal OpenCode s'allume sur le PC (l'appli) ; la Console reste éteinte, grise, à côté.
- Caméra : Fixe.
- Texte : —
- Son : `poweron` (terminal).

## Frame 101: La RTX 5080 (478.8-486.1s)
- act: Fin et écran de fin
- status: posé (image `boards/stills/at-480.08s.png`)
- TC : 7:58,8 → 8:06,1 (7.3 s) · 🟩 IMG
- Voix : « Sur ma RTX 5080, je peux faire tourner des modèles locaux sans clé API. La seule facture, c'est l'électricité. »
- Image : Brique **produit sur le plateau** : la RTX 5080 (photo NVIDIA détourée) monte de 420 px, reflet qui balaie la carte, voyant vert.
- Caméra : Entrée par le bas, `expo.out` 1,1 s.
- Texte : Colonne droite : « NVIDIA » gris / « RTX 5080 » blanc ; « 0 clé API » vert ; « La seule facture : l'électricité » gris.
- Son : `air`, `poweron`.
- Médias : `images/rtx-5080-nvidia.jpg` (à détourer avec l'outil « Cut out » de l'app)

## Frame 102: Remplacer Claude ? (486.1-489.9s)
- act: Fin et écran de fin
- status: posé (image `boards/stills/at-487.46s.png`)
- TC : 8:06,1 → 8:09,9 (3.8 s) · ⬜ TXT
- Voix : « Est-ce que ça peut vraiment remplacer un abonnement Claude ? »
- Image : La question en héros ; une petite carte « Bientôt sur la chaîne : Claude ou mon PC ? ».
- Caméra : Fixe.
- Texte : Question 96 px ; carte 32 px grise.
- Son : —

## Frame 103: Écran de fin (489.9-496.7s)
- act: Fin et écran de fin
- status: posé (image `boards/stills/at-491.16s.png`)
- TC : 8:09,9 → 8:16,7 (6.8 s) · 🟧 ANI
- Voix : « En attendant, si vous voulez voir Claude entre de bonnes mains, c'est juste ici : un seul développeur a recréé les 7 logiciels d'Adobe. »
- Image : **Écran de fin** : zone réservée à droite pour la carte vidéo YouTube (ArtCraft), zone ronde pour le bouton d'abonnement ; une flèche fine pointe vers la carte.
- Caméra : Fixe (YouTube pose ses éléments par-dessus).
- Texte : —
- Son : Musique de fin qui monte légèrement.

## Frame 104: La seule clé (496.7-515.9s)
- act: Fin et écran de fin
- status: posé (image `boards/stills/at-497.99s.png`)
- TC : 8:16,7 → 8:35,9 (19.2 s) · ⬜ TXT
- Voix : « Et la seule clé qu'on ne peut pas te voler, c'est celle que tu ne possèdes pas. »
- Image : La dernière clé se dissout ; il reste son emplacement vide (contour pointillé). La phrase s'écrit sous les zones de l'écran de fin. Puis environ 15 s de musique pour l'écran de fin.
- Caméra : Fixe.
- Texte : 56 px blanc, hors des zones YouTube.
- Son : `dissolve` ; silence de 0,6 s avant la phrase.
