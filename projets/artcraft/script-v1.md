# Script : ArtCraft (v1)

> Fiche : [`fiche.md`](fiche.md). Sources et vérifications : [`sources.md`](sources.md). Écrit le 16/10/2026 avec `/youtube script`, à partir de [`brouillon-v1.md`](brouillon-v1.md). Ta question du brouillon (« coquille vide ? ») sert de fil rouge.

## Métadonnées

- **Sujet** : ArtCraft, les clones open source d'Adobe codés avec Claude, racontés puis testés sur un vrai travail de créateur
- **Durée visée** : 12 min (~1 800 mots à ~150 mots/min, tolérance 1 620-1 980)
- **Type de chaîne** : récit + test (commentaire / essai)
- **Public** : 18-30 ans, francophones, curieux de tech. Une partie utilise Photoshop ou Premiere, beaucoup ont déjà entendu parler de Claude. Ils ont cliqué pour savoir si c'est « vraiment gratuit et vraiment utilisable ».
- **Ton** : conversationnel, vouvoiement, humour (comme tes brouillons)
- **Mots** : 1 706 mots de voix off écrits (comptés). Avec ~120 mots de résultats de tests (environ 50 s au total), on arrive à ~1 825 mots, soit **environ 12 min**. Au-delà de 250 mots de résultats, la relance glisse après 65 % : coupe plutôt dans les tests.

**Légende** : les lignes `>` sont lues en voix off. Les crochets sont des indications de montage. Les blocs **[À REMPLIR]** attendent tes résultats de tests. Pour chacun, il y a une phrase type si ça marche (✅) et si ça casse (❌).

---

## HOOK (0:00 — 0:30) | Objectif : plus de 70 % de rétention à 0:30

### Accroche (0:00 — 0:05)

[B-ROLL CUE: écran noir, puis une facture Adobe avec la ligne « frais de résiliation » surlignée en rouge]

> Adobe lui a fait payer pour partir. Alors il a recréé Adobe.

[SOUND EFFECT: tampon sec sur la facture]
[PACING: aucune intro, aucun logo. La première phrase tombe sur la première image.]

### Promesse (0:05 — 0:15)

[B-ROLL CUE: les 7 icônes s'enchaînent en rafale : PhotoCraft, FilmCraft, VectorCraft, LightCraft, PdfCraft, EffectCraft, DesignCraft]

> Sept logiciels : Photoshop, Premiere, Lightroom… Gratuits, open source, codés avec une IA et sortis en trois jours. Je les ai testés sur un vrai travail : la miniature et le montage de cette vidéo.

### Enjeu (0:15 — 0:30)

> Si ça marche, adieu l'abonnement Adobe. Sinon, c'est le buzz vide de l'année. Et la vérité est plus tordue : dans cette histoire, le Robin des Bois a lui aussi… un abonnement à vous vendre.

[PACING: petite pause avant « un abonnement à vous vendre ». Cette boucle ouverte se referme au bloc 4.]

⚠️ RISQUE DE DÉCROCHAGE : la promesse « je les ai testés » doit se voir tout de suite. Glisse 1 ou 2 secondes de PhotoCraft ouvert sur ta miniature pendant la promesse.

---

## INTRO (0:30 — 1:32) | Contexte

[GRAPHIC: « 30 septembre 2026 », un terminal GitHub avec le commit « init repo »]

> Le 30 septembre, un développeur d'Atlanta, Brandon Thomas, ouvre un nouveau projet sur GitHub. Il s'appelle PhotoCraft. Le lendemain soir, il poste ça sur Hacker News, le forum préféré des développeurs :

[GRAPHIC: la citation en anglais, traduite en sous-titre]

> « Le logiciel, c'est fini. Mais pour de vrai. Je viens de faire Photoshop d'un seul coup. En entier. » Et il ajoute : « Notre métier ne vaudra bientôt plus rien. »

[SOUND EFFECT: une seconde de silence]

> Ambiance.

> Au moment où j'écris ces lignes, PhotoCraft a près de 67 000 étoiles sur GitHub. Les sept applis réunies, environ 132 000. Et la famille s'est agrandie : treize applis, parce qu'entre-temps, ils ont aussi cloné Word, Excel, PowerPoint… et même Figma.

[UNEXPECTED STAT: compteur qui monte jusqu'à « 2 876 028 lignes »]

> Au total, presque 2,9 millions de lignes de code. En moins de trois semaines.

> Alors aujourd'hui, une seule question : est-ce qu'on peut vraiment s'en servir, ou est-ce que c'est une coquille vide ? Mais pour comprendre ce projet, il faut d'abord comprendre pourquoi un développeur en veut autant à Adobe.

[PACING: rythme soutenu. Les chiffres défilent à l'écran pendant que la voix avance.]

---

## BLOC 1 : La vengeance (1:32 — 3:00)

[GRAPHIC: titre de chapitre « 1. La vengeance »]

> Si vous avez déjà eu un abonnement Adobe, vous connaissez peut-être le piège. Vous prenez l'offre annuelle, payée tous les mois. Ça a l'air souple. Sauf que si vous partez pendant la première année, Adobe vous facture des frais de résiliation : la moitié de tout ce qu'il vous reste à payer.

[B-ROLL CUE: une barre de 12 mois. Clic sur « Résilier » au 4e mois : la moitié des 8 mois restants glisse dans une caisse « Adobe ».]

> Et ça vient de la FTC, le gendarme américain de la consommation. En juin 2024, le ministère américain de la Justice attaque Adobe pour ces pratiques. Et en mars 2026, Adobe accepte un accord à 150 millions de dollars. 75 millions d'amende, 75 millions de services gratuits pour les clients. Adobe, de son côté, conteste toute faute.

[UNEXPECTED STAT: « 150 000 000 $ » en plein écran]

> Brandon Thomas fait partie de ceux qui ont payé. Il l'a écrit noir sur blanc sur Reddit : « Ils m'ont fait payer les frais de résiliation à plusieurs reprises, et je les déteste depuis. »

[CAMERA CHANGE: zoom lent sur « à plusieurs reprises »]

> À plusieurs reprises. Le même piège, plusieurs fois. Et sa vengeance, c'est de reconstruire toute la boîte.

> On a tous voulu se venger d'un abonnement un jour. Moi, j'ai résilié Netflix en râlant. Lui, il a cloné Photoshop.

> Donc : un développeur rancunier, un piège à abonnement, et 150 millions de dollars en toile de fond. Mais comment on fabrique sept logiciels de cette taille en trois jours ? La réponse fait un peu peur.

---

## MID-CTA (~3:00, 25 % de la vidéo)

[GRAPHIC: bouton « S'abonner » animé, en bas à droite]

> Petite pause. Sur Technovore, on décortique le génie caché derrière les applis que vous utilisez tous les jours. Si c'est votre truc, abonnez-vous. C'est gratuit, et contrairement à Adobe, vous pouvez partir quand vous voulez.

[PACING: 10 secondes maximum. La blague sur Adobe fait passer l'appel.]

---

## BLOC 2 : L'usine à code (3:15 — 5:09)

[GRAPHIC: titre de chapitre « 2. L'usine »]
[SOUND EFFECT: transition]

> Brandon n'est pas un débutant : quinze ans de métier, dont une dizaine sur Rust. Mais en février, il a fait un choix radical. Je le cite : « J'ai complètement arrêté d'écrire du code en février. »

[B-ROLL CUE: un terminal Claude Code qui défile en accéléré]

> Depuis, c'est l'IA qui écrit. Son outil ? Claude Code, tel quel, avec le modèle Claude Opus 5.5. Rien de plus. Et ça se voit dans l'historique : plus de la moitié des modifications de PhotoCraft sont cosignées par Claude.

[UNEXPECTED STAT: « 56 % des commits cosignés par Claude »]

> Lui, il joue le chef de chantier. Il découpe le travail, il lance des agents en parallèle, il relit, il redresse la barre. Et dans chaque projet, il y a un fichier d'instructions pour l'IA, avec une règle qui revient partout : on ne regarde jamais le code d'Adobe.

[GRAPHIC: extrait du fichier AGENTS.md, « behaviour and look only » surligné]

> C'est ce qu'on appelle une réimplémentation en « salle blanche ». Imaginez un chef qui goûte un plat au restaurant, puis qui essaie de le refaire chez lui. Il a le droit de goûter. Il n'a pas le droit de voler le cahier de recettes. Ici, le plat, c'est Photoshop tel qu'on l'utilise. Le cahier de recettes, ce serait le code d'Adobe. Le projet interdit même les outils de décompilation, et s'appuie sur des documentations publiques, comme celle du format PSD, qu'Adobe publie lui-même.

[SOUND EFFECT: « ding » de validation]

> Dernier détail : chaque action de ces logiciels est une commande. Du coup, une IA peut les piloter. Vous dites à Claude « détoure ce personnage », et c'est lui qui clique dans PhotoCraft.

[B-ROLL CUE: ta démo MCP si tu l'as tournée (voir test bonus), sinon la capture du README]

> Et il n'est pas seul : un cofondateur, une petite équipe, et plus de 300 contributeurs sur PhotoCraft.

> Un chef de chantier, des agents IA, et une règle d'or : ne jamais copier. Sur le papier, c'est impressionnant. Mais le papier, ça ne fait pas des miniatures. Alors j'ai fait le test.

⚠️ RISQUE DE DÉCROCHAGE : bloc explicatif sans démo. Garde la métaphore du chef en animation (Remotion) et n'ajoute rien : le bloc fait déjà 1 min 54.

---

## BLOC 3 : Le test (5:09 — 7:43)

[GRAPHIC: titre de chapitre « 3. Le test »]
[CAMERA CHANGE: passage en capture d'écran plein cadre]

> Le défi est simple : faire la miniature de cette vidéo avec PhotoCraft, et monter un extrait avec FilmCraft. Pas une démo de dix secondes. Mon vrai travail, celui que je fais pour chaque vidéo.

> L'installation, déjà : Windows, Mac, Linux, et même une version qui tourne dans le navigateur. Pas de compte, pas de carte bancaire.

**[À REMPLIR] Installation** : temps de téléchargement, poids, premier lancement.
- ✅ « Deux minutes plus tard, c'est ouvert. »
- ❌ « Premier lancement… et premier plantage. »

> Premier test : PhotoCraft. Si vous connaissez Photoshop, vous êtes chez vous : mêmes menus, mêmes raccourcis, Cmd+J pour dupliquer un calque, tout est là.

**[À REMPLIR] La miniature** (chronomètre à l'écran) : calques, détourage, texte, ombre portée.
- ✅ « Détourage, texte, ombre : en [X] minutes, j'ai ma miniature. »
- ❌ « Le détourage, ça va. Le texte, par contre… [ce qui a cassé]. »

[UNEXPECTED STAT: « 133 fichiers sur 256 »]

> Maintenant, le vrai juge de paix : j'ouvre une ancienne miniature de la chaîne, un fichier PSD fait sur Photoshop. Et là, le projet le reconnaît lui-même : sur les fichiers créés par Photoshop, il n'en affiche correctement qu'environ la moitié. Alors, le mien ?

**[À REMPLIR] Le PSD** : est-ce qu'il s'ouvre ? Mêmes polices, mêmes effets ?

> Pendant ce temps, je surveille la mémoire. Un testeur du site OMG Ubuntu a vu PhotoCraft grimper à environ 5 Go de RAM après avoir ouvert un seul PSD.

**[À REMPLIR] La RAM mesurée** : une blague possible si c'est beaucoup : « À ce prix-là, je préfère la garder pour Monster Hunter. »

[CAMERA CHANGE: passage à FilmCraft]
[SOUND EFFECT: claquement de clap]

> Deuxième test : FilmCraft, le clone de Premiere. Je prends les rushs de mon dernier Short, et je monte.

**[À REMPLIR] Le montage** : la timeline est-elle fluide ? Le son ? L'export ?

> Pour être honnête, le site XDA a signalé une timeline qui rame et un son cassé. FilmCraft est d'ailleurs la seule appli du lot sans version navigateur.

[B-ROLL CUE: tour express, une appli toutes les 3 secondes, avec un tampon ✅ ou ❌]

> Et le tour express des autres : LightCraft pour retoucher une photo, VectorCraft pour un logo, PdfCraft pour signer un PDF. Ce qui, entre nous, est déjà plus utile que la moitié des logiciels qu'on installe.

**[À REMPLIR] Tour express** : une phrase par appli (LightCraft, VectorCraft, PdfCraft, EffectCraft, DesignCraft).

**[À REMPLIR] Test bonus (si tu as le temps)** : brancher Claude sur PhotoCraft en MCP et lui demander un détourage. C'est le plan le plus fort de la vidéo s'il marche.

> Bilan des tests : [ton verdict en une phrase]. Mais en préparant cette vidéo, je suis tombé sur un détail qui change la façon de regarder toute l'histoire. Et il ne se trouve pas dans le logiciel.

⚠️ RISQUE DE DÉCROCHAGE : un test qui s'étire tue le rythme. Chaque test tient en 30 à 40 secondes, chronomètre à l'écran, et on garde seulement le moment où ça marche et le moment où ça casse.

---

## RELANCE (~7:43, 63 % de la vidéo)

[CAMERA CHANGE: coupure nette, musique coupée, écran noir d'une demi-seconde]

> Parce qu'il y a une question que tout le monde oublie de poser : qui paie tout ça ? Des agents IA qui tournent jour et nuit, ça coûte. Et la réponse est un peu ironique.

⚠️ RISQUE DE DÉCROCHAGE : à 60 %, c'est la falaise classique. Cette relance doit sonner comme un second hook, avec une nouvelle question et une nouvelle musique.

---

## BLOC 4 : Qui paie ? (7:57 — 9:46)

[GRAPHIC: titre de chapitre « 4. Qui paie ? »]

> Les applis sont gratuites, pour de vrai : pas de pub, pas de compte, pas de pistage. Mais elles sont publiées par une entreprise qui s'appelle… ArtCraft. Et ArtCraft, à la base, c'est un studio de création d'images et de vidéos par IA. Payant. Avec des crédits. Et des formules entre 8 et 60 dollars par mois.


> Oui. L'homme qui a cloné Adobe par haine des abonnements finance ses logiciels gratuits… avec un abonnement.

> Bon, pour être juste : son abonnement à lui est « résiliable à tout moment ». Pas de frais de sortie. Le piège, au moins, il l'a évité.

[B-ROLL CUE: la page de tarifs d'ArtCraft, « Cancel anytime » entouré]

> Et Brandon connaît bien les zones grises. En 2020, il lance Vocodes, un site qui fait parler des voix de célébrités grâce à l'IA. Ça devient FakeYou. À l'époque, il disait lui-même : « Je ne suis pas avocat, mais je pense qu'on entre dans une zone grise juridique. » Et en 2022, le gendarme italien de la vie privée ouvre une enquête sur FakeYou.

[UNEXPECTED STAT: « 2020 : voix de célébrités. 2026 : Photoshop. »]

> Pourquoi je vous raconte ça ? Parce que ça pose la vraie question : cloner Photoshop avec une IA, c'est légal ?

> Le code, il ne l'a pas copié : c'est tout le principe de la salle blanche. Mais l'apparence, les menus, les raccourcis sont volontairement les mêmes. Et au moment où j'enregistre, Adobe n'a fait aucune déclaration publique. Pas de plainte connue, rien.

[B-ROLL CUE: la vignette de la vidéo « Adobe Reacts », floutée, avec un tampon « PARODIE »]

> D'ailleurs, si vous avez vu passer une vidéo « Adobe réagit », méfiez-vous : c'est une parodie, jouée par un acteur.

> Donc : des applis gratuites, payées par un abonnement, et un géant qui ne dit rien. Pour l'instant. Il reste la question la plus importante : est-ce qu'on peut résilier Adobe demain matin ?

---

## BLOC 5 : La promesse (9:46 — 11:38)

[GRAPHIC: titre de chapitre « 5. La promesse »]

> Le 3 octobre, Brandon promettait sur Reddit : « On atteindra 100 % de parité d'ici un mois. » Traduction : tout ce que fait Photoshop, dans un mois.

[GRAPHIC: les deux citations côte à côte, avec leur date]

> Deux jours plus tard, sur Hacker News, la promesse a déjà rétréci : « Ça se comptera en mois, pas en années. »

> Et le plus intéressant, c'est que le projet publie sa propre évaluation. Plutôt honnête, d'ailleurs. Environ 76 % des fonctions de Photoshop existent dans PhotoCraft. Mais prêt pour un vrai travail de pro ? Environ 45 %. Et pour aller au bout, ils estiment qu'il faut encore entre 2 300 et 4 100 heures de travail d'agents IA.

[UNEXPECTED STAT: deux jauges, 76 % et 45 %]

> Et c'est là que tout se joue. La première moitié, l'IA l'a écrite en quelques jours. La seconde, ce sont les détails : un fichier qui s'ouvre exactement pareil, une couleur qui ne bouge pas à l'impression, un pinceau qui réagit comme votre main l'attend. Le genre de détails pour lesquels les pros paient Adobe depuis plus de trente ans.

[PACING: ralentir ici. Pause avant la réponse à la question du début.]

> Alors, coquille vide ? Non. Pour une miniature YouTube, un PDF à signer ou une photo à retoucher, [ton verdict d'après les tests]. Pour un graphiste qui vit de Photoshop, pas encore.

> Mais regardez ce que ça raconte de l'avenir. Un développeur et ses agents IA ont posé, en moins de trois semaines, les fondations de ce qu'Adobe a construit en plus de trente ans. Ils n'ont pas fini. Mais ils ont prouvé qu'on pouvait commencer. Et quand écrire du code ne coûte presque plus rien, ce qui compte, c'est la confiance : que votre fichier s'ouvre encore demain, que l'appli existe toujours dans deux ans, que quelqu'un réponde quand ça casse.

> Ça, aucune IA ne l'a encore écrit en trois jours.

⚠️ RISQUE DE DÉCROCHAGE : la conclusion « réflexion » peut sembler molle. Garde-la sous 2 min et finis sur la phrase courte.

---

## OUTRO (11:38 — 12:13)

### Appel à l'action (15 s)

> Et vous, vous résilieriez Adobe pour ça ? Dites-le en commentaire : oui, non, ou « j'utilise déjà GIMP ». On ne juge personne. Et si vous voulez la suite, parce qu'à ce rythme-là il y en aura une, abonnez-vous.

### Écran de fin (15 s)

[GRAPHIC: écran de fin, avec ta meilleure vidéo actuelle à gauche et le bouton d'abonnement à droite]

> Si vous aimez comprendre comment les applis marchent sous le capot, cette vidéo-là devrait vous plaire.

### Teaser de la prochaine vidéo (15 s)

> Et lundi 9 novembre, on part chez Uber : comment votre téléphone affiche des voitures qui bougent en direct, sans ramer. Petit indice : ils ont découpé la planète entière en hexagones.

[PACING: on garde l'énergie jusqu'à la dernière image. Pas de « merci d'avoir regardé ».]

---

## Journal des relances d'attention

| Moment | Type | Description |
|---|---|---|
| 0:00 | [B-ROLL CUE] | La facture et les frais de résiliation |
| 0:04 | [SOUND EFFECT] | Le tampon |
| 0:04 | [B-ROLL CUE] | Rafale des 7 icônes |
| 0:32 | [GRAPHIC] | « 30 septembre 2026 », le commit |
| 0:44 | [GRAPHIC] | La citation de Hacker News |
| 0:56 | [SOUND EFFECT] | Silence, puis « Ambiance. » |
| 1:11 | [UNEXPECTED STAT] | Le compteur à 2 876 028 lignes |
| 1:32 | [GRAPHIC] | Chapitre 1 |
| 1:53 | [B-ROLL CUE] | La barre de 12 mois et la caisse Adobe |
| 2:18 | [UNEXPECTED STAT] | 150 millions de dollars |
| 2:31 | [CAMERA CHANGE] | Zoom sur « à plusieurs reprises » |
| 3:00 | [GRAPHIC] | Bouton d'abonnement (mid-CTA) |
| 3:15 | [GRAPHIC] + [SOUND EFFECT] | Chapitre 2, transition |
| 3:28 | [B-ROLL CUE] | Le terminal de Claude Code |
| 3:44 | [UNEXPECTED STAT] | 56 % des commits cosignés par Claude |
| 4:03 | [GRAPHIC] | AGENTS.md, « behaviour and look only » |
| 4:36 | [SOUND EFFECT] | « Ding » à la fin de la métaphore du chef |
| 4:49 | [B-ROLL CUE] | La démo MCP |
| 5:09 | [GRAPHIC] + [CAMERA CHANGE] | Chapitre 3, capture plein cadre |
| 5:54 | [UNEXPECTED STAT] | 133 fichiers sur 256 |
| 6:37 | [CAMERA CHANGE] + [SOUND EFFECT] | Passage à FilmCraft, avec un clap |
| 7:01 | [B-ROLL CUE] | Le tour express avec les tampons ✅ / ❌ |
| 7:43 | [CAMERA CHANGE] | Coupure nette, musique coupée (relance) |
| 7:57 | [GRAPHIC] | Chapitre 4 |
| 8:36 | [B-ROLL CUE] | La page de tarifs d'ArtCraft |
| 9:01 | [UNEXPECTED STAT] | « 2020 : voix de célébrités. 2026 : Photoshop. » |
| 9:25 | [B-ROLL CUE] | La vidéo parodie, floutée |
| 9:46 | [GRAPHIC] | Chapitre 5 |
| 9:56 | [GRAPHIC] | Les deux promesses, avec leur date |
| 10:27 | [UNEXPECTED STAT] | Les jauges 76 % et 45 % |
| 11:54 | [GRAPHIC] | Écran de fin |

**Total** : 35 relances. Ces horaires sont calculés à 150 mots/min, avec ~120 mots de résultats de tests répartis dans le bloc 3. **Intervalle moyen** : environ 21 secondes. Tests mis à part (le chronomètre et les captures relancent l'attention), le plus long trou est la conclusion du bloc 5 (10:27-11:54, 87 s), sous le maximum de 90 s : on y ralentit exprès.

## Carte des risques de décrochage

| Moment | Niveau | Problème | Solution |
|---|---|---|---|
| 0:04-0:15 | ⚠️ Élevé | La promesse « je les ai testés » n'est pas encore visible | 1 ou 2 s de PhotoCraft ouvert sur ta miniature pendant la promesse |
| 3:15-5:09 | ⚠️ Élevé | Bloc explicatif, sans démo | Métaphore du chef animée, démo MCP. Le bloc fait déjà 1 min 54, n'ajoute rien |
| 5:09-7:43 | ⚠️ Moyen | Des tests qui s'étirent | 30-40 s par test, chronomètre, seulement « ça marche » et « ça casse » |
| 7:43 | ⚠️ Élevé | La falaise des 60 % | Relance traitée comme un second hook (coupure, nouvelle musique, nouvelle question) |
| 8:40-9:15 | ⚠️ Moyen | Le passage sur FakeYou peut sembler hors sujet | Il sert la question « c'est légal ? ». Garde-le factuel, avec les sources à l'écran, sans jugement |
| Toute la vidéo | ⚠️ Moyen | Voix off IA : la référence du skill indique une rétention 70 % plus basse qu'avec un humain | C'est ta propre voix clonée, mais annote le script (pauses, emphases) avec `voix-off-ia` ou `voix-off-voicestudio` avant la génération |

## Notes pour le montage

- **Chaîne sans visage** : [CAMERA CHANGE] veut dire un changement de cadre (zoom, coupe, passage capture ↔ animation).
- **Rythme** : rapide jusqu'à 1:32, posé dans le bloc 1 (c'est le récit), nerveux dans les tests, ralenti dans la conclusion du bloc 5.
- **Musique** : tendue et légère pour le récit, plus rythmée pendant les tests, coupée net à la relance (7:43), puis plus grave pour « Qui paie ? ».
- **Citations** : toujours la version originale en anglais à l'écran, traduite en sous-titre, avec la source et la date en petit (Hacker News, Reddit, TNW). C'est ta protection contre les commentaires « source ? ».
- **Logos** : pas de logo Adobe à l'écran. Les noms (Photoshop, Premiere) sont cités seulement pour comparer.
- **Moments pour la miniature** :
  - 0:00, la facture « frais de résiliation » ;
  - ~5:55, ton PSD ouvert dans PhotoCraft (avant/après) ;
  - ~8:20, « abonnement » barré.

## Chiffres revérifiés le 18/10 (veille de l'enregistrement)

| Chiffre | 16/10 | 18/10 | Dans le script |
|---|---|---|---|
| Étoiles de PhotoCraft | 64 903 | **66 940** | « près de 67 000 » |
| Étoiles des 7 applis | ~128 000 | **132 272** | « environ 132 000 » |
| Lignes de Rust (7 dépôts, tests compris) | ~2,81 M | **2 876 028** | « presque 2,9 millions » |
| Commits de PhotoCraft mentionnant Claude Opus 5.5 | 1 373 / 2 429 (57 %) | **1 428 / 2 564 (56 %)** | « plus de la moitié », 56 % à l'écran |
| Contributeurs de PhotoCraft | 312 | 323 | « plus de 300 » (inchangé) |
| Nombre d'applis | 13 | 13 | inchangé |
| Tarifs d'ArtCraft | 8 à 60 $/mois | idem | inchangé |
| Évaluation du projet (76 % / 45 % / 2 300-4 100 h) | MAJ du 13/10 | idem | inchangé |
| Réaction d'Adobe | aucune | aucune | inchangé |

- « En moins de trois semaines » reste vrai à l'enregistrement du lundi 19 (19 jours). Si tu enregistres après le 20, dis « en moins d'un mois ».
- La voix dit « au moment où j'écris ces lignes » : la vidéo sort le 26, et les chiffres auront encore bougé d'ici là.
