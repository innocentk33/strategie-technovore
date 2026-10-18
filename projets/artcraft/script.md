# Script : ArtCraft (v2)

> Fiche : [`fiche.md`](fiche.md). Sources : [`sources.md`](sources.md). v1 : [`script-v1.md`](script-v1.md), grillée dans [`grill-v1.md`](grill-v1.md).
> **Changements de la v2 (18/10)** :
> - le test passe avant l'usine ;
> - les 15 tics d'IA sont corrigés ;
> - le passage FakeYou part de la citation de Brandon ;
> - **nouveau hook (18/10)** : « Ce mec en avait tellement marre de payer Adobe… qu'il l'a recréé. » (ta formule, avec le mot fort en fin de phrase) ;
> - **ajouts du 18/10** : tes 33 €/mois, le PDF « presque privatisé », ton avis juridique (« je ne suis pas avocat non plus »), ton verdict (suffisant pour tes miniatures, pas encore pour un pro), et ta conclusion « must have » (moins de 100 Mo, 2 s) ;
> - tes ajouts du brouillon sont intégrés (époque de dingue, Thanos, Linux frère, farmer l'aura, l'interface, le gag de l'agent) ;
> - **un seul test, PhotoCraft** (18/10, ta décision : éviter l'effet tutoriel). FilmCraft et le tour express sont retirés ;
> - la famille de 13 applis et la légende du « mec seul » passent dans « Qui paie ? », pour tenir la relance vers 60 % ;
> - ta réponse sur « notre métier » (les petits SaaS face au support et à la compatibilité) devient la fin.

## Métadonnées

- **Sujet** : ArtCraft, les clones open source d'Adobe codés avec Claude, racontés, avec un seul test : PhotoCraft sur un vrai travail de créateur (la miniature)
- **Durée visée** : ~11 min (~1 650 mots à ~150 mots/min, tolérance ±10 %). Plus courte que prévu : un seul test, c'est voulu
- **Type de chaîne** : récit + test (commentaire / essai)
- **Public** : 18-30 ans, francophones, curieux de tech, dont beaucoup apprennent à coder. Ils ont cliqué pour savoir si c'est « vraiment gratuit et vraiment utilisable ».
- **Ton** : conversationnel, vouvoiement, ton humour
- **Mots** : 1 697 mots de voix off écrits (comptés). Avec ~30 mots de résultats de test, on arrive à ~1 727 mots, soit **environ 11 min 30 s**.

**Légende** : les lignes `>` sont lues en voix off. Les crochets sont des indications de montage. Les blocs **[À REMPLIR]** attendent tes résultats de test (~30 mots au total : le PSD et la RAM). Pour chacun, il y a une phrase type si ça marche (✅) et si ça casse (❌).

---

## HOOK (0:00 — 0:30) | Objectif : plus de 70 % de rétention à 0:30

### Accroche (0:00 — 0:05)

[B-ROLL CUE: sa photo de profil GitHub (publique) sur « Ce mec », puis une facture Adobe qui défile, ligne « frais de résiliation » surlignée en rouge]

> Ce mec en avait tellement marre de payer Adobe… qu'il l'a recréé.

[SOUND EFFECT: tampon sec sur la facture, pile sur « recréé »]
[PACING: aucune intro, aucun logo. La première phrase tombe sur la première image. Le mot fort est le dernier : « recréé ».]

### Promesse (0:05 — 0:15)

[B-ROLL CUE: les 7 icônes en rafale, puis 1 seconde de ta miniature en cours dans PhotoCraft]

> Photoshop, Premiere, Lightroom : sept logiciels gratuits, sortis en trois jours, et c'est une IA qui a écrit le code. Moi, j'ai essayé de faire la miniature de cette vidéo avec son Photoshop.

### Enjeu (0:15 — 0:30)

> Si ça marche, adieu l'abonnement Adobe. Sinon, c'est le buzz vide de l'année. Et dans cette histoire, le Robin des Bois a lui aussi… un abonnement à vous vendre.

[PACING: petite pause avant « un abonnement à vous vendre ». Cette boucle se referme dans « Qui paie ? ».]

---

## INTRO (0:29 — 1:38) | Contexte

> On vit une époque de dingue. Depuis Claude Opus 5.5, des gens sortent des trucs de plus en plus fous.

[GRAPHIC: « 30 septembre 2026 », un terminal GitHub avec le commit « init repo »]

> Le 30 septembre, un développeur d'Atlanta, Brandon Thomas, ouvre un nouveau projet sur GitHub : PhotoCraft. Le lendemain soir, il poste ça sur Hacker News, le forum préféré des développeurs :

[GRAPHIC: la citation en anglais, traduite en sous-titre, avec la date]

> « Le logiciel, c'est fini. Mais pour de vrai. Je viens de faire Photoshop d'un seul coup. En entier. » Et il ajoute : « Notre métier ne vaudra bientôt plus rien. »

[SOUND EFFECT: une seconde de silence]

> Ambiance.

> Moi, je suis développeur. Et ma première pensée a été pour les petits SaaS, ces services en ligne qui font une seule chose, comme générer un QR code. Si une IA recrée Photoshop en trois jours, est-ce que tout ça va disparaître ? Adobe compris ? On y revient à la fin.

[B-ROLL CUE: un générateur de QR code en ligne, puis zoom arrière sur l'interface de Photoshop]

[UNEXPECTED STAT: compteur d'étoiles GitHub qui monte jusqu'à « 66 940 »]

> En moins de trois semaines, son projet a récolté près de 67 000 étoiles sur GitHub, les likes des développeurs.

> Alors, est-ce qu'on peut vraiment s'en servir, ou est-ce que c'est une coquille vide ? Pour répondre, il faut remonter à une facture.

---

## BLOC 1 : La vengeance (1:38 — 2:40)

[GRAPHIC: titre de chapitre « 1. La vengeance »]

> Si vous avez déjà eu un abonnement Adobe, vous connaissez peut-être le piège. Vous prenez l'offre annuelle, payée tous les mois. Ça a l'air souple. Sauf que si vous partez pendant la première année, Adobe vous facture des frais de résiliation : la moitié de tout ce qu'il vous reste à payer.

[B-ROLL CUE: une barre de 12 mois. Clic sur « Résilier » au 4e mois : la moitié des 8 mois restants glisse dans une caisse « Adobe ».]

> En 2024, la justice américaine attaque Adobe pour ces pratiques. En mars 2026, Adobe accepte de payer 150 millions de dollars, sans reconnaître de faute.

[UNEXPECTED STAT: « 150 000 000 $ » en plein écran, puis « 75 M$ d'amende + 75 M$ de services gratuits » en petit, sources FTC et justice.gov]

> Brandon Thomas fait partie de ceux qui ont payé. Il l'a écrit sur Reddit : « Ils m'ont fait payer les frais de résiliation à plusieurs reprises, et je les déteste depuis. »

[CAMERA CHANGE: zoom lent sur « à plusieurs reprises »]

> À plusieurs reprises. Alors il a décidé de farmer l'aura sur le dos d'Adobe, en reconstruisant toute la boîte.

> On a tous voulu se venger d'un abonnement un jour. Moi, je paie 33 euros par mois à Adobe, juste pour faire mes miniatures. Lui, il a cloné Photoshop.

---

## MID-CTA (~2:40, 23 % de la vidéo)

[GRAPHIC: bouton « S'abonner » animé, en bas à droite]

> Petite pause. Sur Technovore, on décortique le génie caché derrière les applis que vous utilisez tous les jours. Si c'est votre truc, abonnez-vous. C'est gratuit, et contrairement à Adobe, vous pouvez partir quand vous voulez.

[PACING: 10 secondes maximum.]

---

## BLOC 2 : Le test (2:55 — 5:12)

[GRAPHIC: le post Reddit, compteur de votes (3 445)]

> Sur Reddit, où ses posts s'enflamment, il promet : « On atteindra 100 % de parité d'ici un mois. » Traduction : tout Photoshop, dans un mois.

> Sept logiciels en trois jours, tout Photoshop promis en un mois : sur le papier, c'est impressionnant. Mais le papier, ça ne fait pas des miniatures. Alors j'ai fait le test.

[GRAPHIC: titre de chapitre « 2. Le test »]
[CAMERA CHANGE: passage en capture d'écran plein cadre]

> Un seul : le plus connu. Le défi : faire la miniature de cette vidéo avec PhotoCraft. Mon vrai travail, celui que je fais pour chaque vidéo.

> Même mieux : je décris le style, je donne les images, et je laisse mon agent IA la faire tout seul… Non, je rigole. Faut pas abuser.

[PACING: pause comique d'une seconde avant « Non, je rigole ». Ce gag se referme dans l'usine.]

> L'installation, déjà : Windows, Mac, et Linux. Linux, frère ! Même Adobe n'y est pas. Normal : eux, ce qui les intéresse, c'est l'argent, et avec dix personnes sous Linux, le marché n'est pas rentable.

> Le fichier fait moins de 100 Mo, et le logiciel démarre en deux secondes.

> La force d'Adobe, c'est son interface. Les gens y sont habitués, et changer ses habitudes, c'est terriblement difficile. Sauf que là, le mec débarque avec quasiment la même interface, les mêmes raccourcis, et il ouvre les fichiers Photoshop. Mais que demande le peuple ?

> Pour mes miniatures, je n'utilise pas d'effets artistiques compliqués : des calques, un détourage, du texte. Et là, tout y est.

[UNEXPECTED STAT: « 133 fichiers sur 256 »]

> Maintenant, le vrai juge de paix : j'ouvre une ancienne miniature de la chaîne, un fichier PSD fait sur Photoshop. Le projet le reconnaît lui-même : sur les fichiers créés par Photoshop, il n'en affiche correctement qu'environ la moitié. Alors, le mien ? Faites vos pronostics.

**[À REMPLIR] Le PSD** : est-ce qu'il s'ouvre ? Mêmes polices, mêmes effets ? (Ce résultat sert aussi à la fin de la vidéo.)

> Et comme tout est écrit en Rust, un langage réputé ultra-rapide, je surveille la mémoire : chez OMG Ubuntu, PhotoCraft est monté à environ 5 Go de RAM pour un seul PSD.

**[À REMPLIR] La RAM mesurée** : si c'est beaucoup : « À ce prix-là, je préfère la garder pour Monster Hunter. »

> Bilan : pour mes miniatures, il fait largement le job. Et pour un logiciel sorti il y a trois semaines, c'est bluffant. Mais comment un seul développeur sort sept logiciels de cette taille en trois jours ?

⚠️ RISQUE DE DÉCROCHAGE : 30 à 40 secondes par étape (installation, miniature, PSD, RAM), chronomètre à l'écran. On garde le moment où ça marche et le moment où ça casse.

---

## BLOC 3 : L'usine (5:12 — 6:51)

[GRAPHIC: titre de chapitre « 3. L'usine »]
[SOUND EFFECT: transition]

> Brandon a quinze ans de métier, dont une dizaine sur Rust. Mais en février, il a fait un choix radical. Je le cite : « J'ai complètement arrêté d'écrire du code en février. »

[B-ROLL CUE: un terminal Claude Code qui défile en accéléré]

> Depuis, c'est l'IA qui écrit : Claude Code, tel quel, avec Claude Opus 5.5. Plus de la moitié des modifications de PhotoCraft sont cosignées par Claude. Et sur les sept applis, ça fait presque 2,9 millions de lignes de code.

[UNEXPECTED STAT: « 56 % des commits cosignés par Claude », puis un compteur qui monte jusqu'à « 2 876 028 lignes »]

> Lui, il joue le chef de chantier : il découpe le travail, lance des agents en parallèle, relit, redresse la barre. Avec une règle répétée dans chaque projet : on ne regarde jamais le code d'Adobe.

[GRAPHIC: extrait du fichier AGENTS.md, « behaviour and look only » surligné]

> On appelle ça une réimplémentation en « salle blanche ». Imaginez un chef qui goûte un plat au restaurant, puis qui le refait chez lui. Il a le droit de goûter. Il n'a pas le droit de voler le cahier de recettes, ici le code d'Adobe. Le projet interdit même la décompilation, et s'appuie sur des documentations publiques, comme celles des formats PSD et PDF. Le PDF, d'ailleurs, c'est Adobe qui l'a inventé, et avec Acrobat, il l'a presque privatisé. Pourtant, c'est une norme ouverte depuis 2008 : même votre navigateur sait lire un PDF. ArtCraft en a profité pour sortir son PdfCraft.

[SOUND EFFECT: « ding » de validation]
[B-ROLL CUE: un PDF ouvert dans un navigateur, puis dans PdfCraft]

> Autre détail : chaque action de ces logiciels est une commande. Du coup, une IA peut les piloter. Vous dites à Claude « détoure ce personnage », et c'est lui qui clique dans PhotoCraft.

**[À REMPLIR] Test bonus (facultatif)** : brancher Claude sur PhotoCraft en MCP et lui demander un détourage.
- ✅ « Bon… tout à l'heure, je rigolais. Mais j'ai quand même essayé. [résultat] »
- Sans test : supprime cette ligne, le gag du bloc 2 tient tout seul.

[B-ROLL CUE: ta démo MCP, sinon la capture du README]

---

## RELANCE (~6:51, 60 % de la vidéo)

[CAMERA CHANGE: coupure nette, musique coupée, écran noir d'une demi-seconde]

> Sauf que des agents IA qui codent jour et nuit, ça coûte cher. Alors j'ai cherché qui paie tout ça. Et je suis tombé sur une page de tarifs.

⚠️ RISQUE DE DÉCROCHAGE : c'est la falaise des 60 %. Nouvelle musique, nouvelle question : traite cette relance comme un second hook.

---

## BLOC 4 : Qui paie ? (7:03 — 9:09)

[GRAPHIC: titre de chapitre « 4. Qui paie ? »]

> Les applis sont gratuites pour de vrai : sans pub, et sans compte à créer. Mais elles sont publiées par une entreprise qui s'appelle… ArtCraft. Et ArtCraft, à la base, c'est un studio de création d'images et de vidéos par IA. Payant. Avec des crédits. Et des formules entre 8 et 60 dollars par mois.

[SOUND EFFECT: disque rayé]

> Oui. L'homme qui a cloné Adobe par haine des abonnements finance ses logiciels gratuits… avec un abonnement.

> Bon, pour être juste : son abonnement à lui est « résiliable à tout moment ». Pas de frais de sortie. Le piège, au moins, il l'a évité.

> Et ArtCraft ne s'arrête pas à Adobe : treize applis, avec des clones de Word, Excel, PowerPoint… et même Figma. Comme Thanos avec les pierres d'infinité : il les veut toutes. Derrière, un cofondateur, une petite équipe et plus de 300 contributeurs. On est loin de la légende du mec seul dans sa chambre.

[B-ROLL CUE: la page de tarifs d'ArtCraft, « Cancel anytime » entouré]

> En 2020, Brandon disait déjà : « Je ne suis pas avocat, mais je pense qu'on entre dans une zone grise juridique. » C'était à propos de Vocodes, son site qui faisait parler des voix de célébrités avec l'IA, devenu FakeYou. En 2022, le gendarme italien de la vie privée a ouvert une enquête sur FakeYou. Aujourd'hui, la même question revient avec Photoshop : cloner un logiciel avec une IA, c'est légal ?

[GRAPHIC: la citation de 2020 (TNW), puis le communiqué du Garante, sources et dates en petit]

> Côté code, la salle blanche le protège. Mais les menus et les raccourcis sont volontairement les mêmes, et c'est justement ce qui fait sa force. Au moment où j'enregistre, Adobe n'a fait aucune déclaration publique. Aucune plainte connue.

> Moi non plus, je ne suis pas avocat. Mais à mon avis, ces copies restent open source et gratuites, sans rien à vendre dedans. Et ça les protège à peu près des attaques juridiques.

[B-ROLL CUE: la vignette de la vidéo « Adobe Reacts », floutée, avec un tampon « PARODIE »]

> D'ailleurs, si vous avez vu passer une vidéo « Adobe réagit », méfiez-vous : c'est une parodie, jouée par un acteur. Reste à savoir si la promesse de Brandon tient.

---

## BLOC 5 : La promesse (9:09 — 10:44)

[GRAPHIC: titre de chapitre « 5. La promesse »]

> Cent pour cent de Photoshop en un mois. Deux jours plus tard, sur Hacker News, la promesse avait déjà rétréci : « Ça se comptera en mois, pas en années. »

[GRAPHIC: les deux citations côte à côte, avec leur date]

> Et le projet publie sa propre évaluation, plutôt honnête d'ailleurs. Environ 76 % des fonctions de Photoshop existent dans PhotoCraft. Mais prêt pour un vrai travail de pro ? Environ 45 %. Et pour aller au bout, ils estiment qu'il faut encore entre 2 300 et 4 100 heures de travail d'agents IA.

[UNEXPECTED STAT: deux jauges, 76 % et 45 %]

> La première moitié, l'IA l'a écrite en quelques jours. La seconde, ce sont les détails : un fichier qui s'ouvre exactement pareil, une couleur qui ne bouge pas à l'impression, un pinceau qui réagit comme votre main l'attend.

[PACING: ralentir. Pause avant la réponse à la question du début.]

> Alors, coquille vide ? Non. Pour un usage comme le mien, ça suffit largement. Pour un pro, il manque encore des fonctions : sur Reddit et Hacker News, des utilisateurs les listent une par une. Mais plus de 300 contributeurs en trois semaines, ça montre que le projet intéresse vraiment.

[CAMERA CHANGE: retour sur le générateur de QR code du début]

> Et mon métier, alors ? Je reviens à mes petits SaaS. Un service qui fait une seule chose, comme générer un QR code, je pense qu'il va disparaître : une IA le recrée trop facilement. Mais une grosse boîte comme Adobe vend aussi du support, et la compatibilité avec des années de projets. Mon vieux fichier PSD l'a montré : [ce qui s'est passé à l'ouverture]. Ça, aucune IA ne l'a encore écrit en trois jours.

⚠️ RISQUE DE DÉCROCHAGE : la fin « réflexion » peut sembler molle. Elle tient parce qu'elle répond à TA question de l'intro, avec TON test PSD comme preuve. Garde-la courte.

---

## OUTRO (10:44 — 11:30)

### Appel à l'action (15 s)

> En tout cas, moi, je vais l'utiliser pour mes miniatures. Un logiciel de moins de 100 Mo qui démarre en deux secondes, juste pour gérer mes minias, c'est le must have. Pour vous, tout dépend de ce qu'il vous faut. Alors dites-le en commentaire : il vous manquerait quoi pour lâcher Adobe ? Ou « j'utilise déjà GIMP », on ne juge personne. Et si vous voulez la suite, abonnez-vous.

### Écran de fin (15 s)

[GRAPHIC: écran de fin, avec ta meilleure vidéo actuelle à gauche et le bouton d'abonnement à droite. Il reste 20 s à l'écran.]

> Si vous aimez comprendre comment les applis marchent sous le capot, cette vidéo-là devrait vous plaire.

### Teaser de la prochaine vidéo (15 s)

> Et lundi 9 novembre, on part chez Uber : comment votre téléphone affiche des voitures qui bougent en direct, sans ramer. Petit indice : ils ont découpé la planète entière en hexagones.

[PACING: on garde l'énergie jusqu'à la dernière image. Pas de « merci d'avoir regardé ».]

---

## Journal des relances d'attention

| Moment | Type | Description |
|---|---|---|
| 0:00 | [B-ROLL CUE] | Sa photo de profil GitHub (publique) sur « Ce mec », puis une facture Adobe qui défile, li |
| 0:04 | [SOUND EFFECT] | Tampon sec sur la facture, pile sur « recréé » |
| 0:04 | [B-ROLL CUE] | Les 7 icônes en rafale, puis 1 seconde de ta miniature en cours dans PhotoCraft |
| 0:37 | [GRAPHIC] | « 30 septembre 2026 », un terminal GitHub avec le commit « init repo » |
| 0:49 | [GRAPHIC] | La citation en anglais, traduite en sous-titre, avec la date |
| 1:00 | [SOUND EFFECT] | Une seconde de silence |
| 1:21 | [B-ROLL CUE] | Un générateur de QR code en ligne, puis zoom arrière sur l'interface de Photoshop |
| 1:21 | [UNEXPECTED STAT] | Compteur d'étoiles GitHub qui monte jusqu'à « 66 940 » |
| 1:38 | [GRAPHIC] | Titre de chapitre « 1 |
| 1:59 | [B-ROLL CUE] | Une barre de 12 mois |
| 2:09 | [UNEXPECTED STAT] | « 150 000 000 $ » en plein écran, puis « 75 M$ d'amende + 75 M$ de services gratuits » en  |
| 2:21 | [CAMERA CHANGE] | Zoom lent sur « à plusieurs reprises » |
| 2:40 | [GRAPHIC] | Bouton « S'abonner » animé, en bas à droite |
| 2:55 | [GRAPHIC] | Le post Reddit, compteur de votes (3 445) |
| 3:16 | [GRAPHIC] | Titre de chapitre « 2 |
| 3:16 | [CAMERA CHANGE] | Passage en capture d'écran plein cadre |
| 4:20 | [UNEXPECTED STAT] | « 133 fichiers sur 256 » |
| 5:12 | [GRAPHIC] | Titre de chapitre « 3 |
| 5:12 | [SOUND EFFECT] | Transition |
| 5:25 | [B-ROLL CUE] | Un terminal Claude Code qui défile en accéléré |
| 5:41 | [UNEXPECTED STAT] | « 56 % des commits cosignés par Claude », puis un compteur qui monte jusqu'à « 2 876 028 l |
| 5:55 | [GRAPHIC] | Extrait du fichier AGENTS.md, « behaviour and look only » surligné |
| 6:35 | [SOUND EFFECT] | « ding » de validation |
| 6:35 | [B-ROLL CUE] | Un PDF ouvert dans un navigateur, puis dans PdfCraft |
| 6:51 | [B-ROLL CUE] | Ta démo MCP, sinon la capture du README |
| 6:51 | [CAMERA CHANGE] | Coupure nette, musique coupée, écran noir d'une demi-seconde |
| 7:03 | [GRAPHIC] | Titre de chapitre « 4 |
| 7:24 | [SOUND EFFECT] | Disque rayé |
| 8:02 | [B-ROLL CUE] | La page de tarifs d'ArtCraft, « Cancel anytime » entouré |
| 8:29 | [GRAPHIC] | La citation de 2020 (TNW), puis le communiqué du Garante, sources et dates en petit |
| 8:58 | [B-ROLL CUE] | La vignette de la vidéo « Adobe Reacts », floutée, avec un tampon « PARODIE » |
| 9:09 | [GRAPHIC] | Titre de chapitre « 5 |
| 9:20 | [GRAPHIC] | Les deux citations côte à côte, avec leur date |
| 9:41 | [UNEXPECTED STAT] | Deux jauges, 76 % et 45 % |
| 10:15 | [CAMERA CHANGE] | Retour sur le générateur de QR code du début |
| 11:12 | [GRAPHIC] | Écran de fin, avec ta meilleure vidéo actuelle à gauche et le bouton d'abonnement à droite |

**Total** : 36 relances, une toutes les 19 secondes en moyenne. Horaires calculés à 150 mots/min, avec ~30 mots de résultats de test répartis dans les blocs [À REMPLIR]. Le plus long trou (64 s, de 3:16 à 4:20) tombe dans le test, où le chronomètre et les captures relancent l'attention.

## Carte des risques de décrochage

| Moment | Niveau | Problème | Solution |
|---|---|---|---|
| Promesse (0:05-0:15) | ⚠️ Élevé | Le test doit se voir tout de suite | 1 seconde de ta miniature en cours dans PhotoCraft pendant la promesse |
| Le test | ⚠️ Moyen | Un test qui s'étire en tutoriel | 30-40 s par étape, chronomètre, seulement « ça marche » et « ça casse ». Un seul logiciel testé |
| L'usine | ⚠️ Moyen | Bloc explicatif après le test | Métaphore du chef animée, démo MCP, gag de l'agent qui se referme. Le bloc a été resserré : n'ajoute rien |
| Relance (~60 %) | ⚠️ Élevé | La falaise classique | Coupure nette, nouvelle musique, nouvelle question |
| FakeYou | ⚠️ Moyen | Une personne réelle | Ses propres mots d'abord, sources à l'écran, aucun jugement |
| Toute la vidéo | ⚠️ Moyen | Voix off IA : la référence du skill indique une rétention 70 % plus basse qu'avec un humain | Ta voix clonée, annotée avec `voix-off-voicestudio` ou `voix-off-ia` (pauses, emphases, nombres en lettres) |

## Notes pour le montage

- **Chaîne sans visage** : [CAMERA CHANGE] veut dire un changement de cadre (zoom, coupe, passage capture ↔ animation).
- **Rythme** : rapide dans le hook et l'intro, posé dans la vengeance, nerveux dans le test, plus calme dans la promesse.
- **Musique** : tendue et légère pour le récit, rythmée pour le test, coupée net à la relance, puis plus grave pour « Qui paie ? ».
- **Citations** : version originale en anglais à l'écran, traduite en sous-titre, avec la source et la date en petit (Hacker News, Reddit, TNW, Garante).
- **Logos** : pas de logo Adobe à l'écran. Les noms (Photoshop, Premiere) sont cités seulement pour comparer.
- **Le QR code** : le même plan au début (ta question) et à la fin (ta réponse). Le spectateur doit reconnaître la boucle.
- **Moments pour la miniature** : la facture « frais de résiliation », ton PSD ouvert dans PhotoCraft (avant/après), « abonnement » barré.

## Chiffres (revérifiés le 18/10)

| Chiffre | Valeur | Dans la voix |
|---|---|---|
| Étoiles de PhotoCraft | 66 940 | « près de 67 000 » |
| Lignes de Rust (7 dépôts, tests compris) | 2 876 028 | « presque 2,9 millions » |
| Commits de PhotoCraft mentionnant Claude Opus 5.5 | 1 428 / 2 564 (56 %) | « plus de la moitié » |
| Contributeurs de PhotoCraft | 323 | « plus de 300 » |
| Applis | 13 | « treize » |
| Tarifs d'ArtCraft | 8 à 60 $/mois | « entre 8 et 60 dollars » |
| Évaluation du projet | 76 % / 45 % / 2 300-4 100 h (MAJ du 13/10) | idem |
| Votes Reddit (r/SaaS, 03/10) | 3 445 | (à l'écran seulement) |
| Installeurs de PhotoCraft v0.10.0 (18/10) | 66 à 92 Mo selon la plateforme | « moins de 100 Mo » |
| Démarrage | 2 s (ta mesure) | « deux secondes » |
| PDF | norme ouverte ISO 32000-1 depuis juillet 2008, brevets d'Adobe cédés gratuitement | « une norme ouverte depuis 2008 » |
| Ton abonnement Adobe | 33 €/mois (toi) | « 33 euros par mois » |
| Réaction d'Adobe | aucune | « aucune déclaration publique » |

- « En moins de trois semaines » reste vrai jusqu'au 20/10 (premier commit le 30/09). Si tu enregistres plus tard, dis « en moins d'un mois ».
- La voix dit « au moment où j'écris ces lignes » : la vidéo sort le 26, les chiffres auront encore bougé.
