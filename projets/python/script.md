# Python : script final (v2)

**Titre** (ton idée du 23/10) : *Python, le langage de l'IA, est un cadeau de Noël*. Variante B pour « Tester et comparer » : *Noël nous a apporté le langage de l'IA*. On ne dit pas « Noël nous a apporté l'IA » : l'IA est bien plus ancienne (le mot date du milieu des années 1950), c'est son langage qui est né à Noël 1989. Le hook tient le titre : Noël 89, puis « c'est le langage de l'IA », avant 0:15

**Durée** : environ 1 870 mots de voix off (compte de `controle.py`). À ton débit mesuré sur ArtCraft (145 mots/min, pauses et improvisations comprises) : environ 12 min 55. Avec des coupes serrées comme sur Uber (~180 mots/min) : 10 min 25, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Texte et sous-texte** :
- **Texte** : l'histoire de Python, du bureau fermé de Noël 1989 au langage de l'IA en 2026.
- **Sous-texte** (ta phrase du [brouillon](brouillon.md) : « À quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation ? ») : ce qu'un dev fait d'une semaine où personne ne lui demande rien. Ta question ouvre la vidéo, comme dans ton brouillon, et ton « il se faisait tellement chier » devient la légende que la vraie phrase de Guido corrige (« pas grand-chose d'autre sur les bras », faits 1, 2 et 5 de [`sources.md`](sources.md)).

**Fil rouge** : le mot « ennui ». La légende le met à Noël 1989 ; Guido ne l'écrit pas (préface de 1996). Il finit par l'écrire en novembre 2020, « la retraite, c'était ennuyeux », et il retourne coder (fait 34). Le motif des vacances court tout du long : la semaine de Noël 1989, les « vacances permanentes » de 2018, la retraite de 2019, puis la semaine de Noël du spectateur.

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **hook** : ta question passe en première phrase, comme dans ton brouillon (la V1 la mettait au 50e mot, derrière « Du coup, j'ai une question », une liaison qui ne reliait rien) ; « la colonne vertébrale de l'IA », abstrait à l'oral, devient un chiffre (presque six devs sur dix, Stack Overflow 2025) plus « le langage de l'IA » ; le pont ouvre une vraie deuxième boucle : le mot « ennui », Guido l'écrira, mais trente ans plus tard ;
- **nouvelle fin** : le tweet du 12/11/2020 (« J'ai décidé que la retraite, c'était ennuyeux », fait 34) répond enfin à ta question avec un fait, au lieu d'un crochet ; ta place pour le verdict reste ;
- **section 8** : la question « Python peut-il tenir sans lui ? » reçoit sa vraie réponse, le conseil de cinq élu en 2019 (faits 31 et 32), au lieu du copyright de la PSF, qui ne répondait pas ; Barry Warsaw, planté en section 5, y est récolté ; le contrepied « Python n'est plus premier » est réduit à une phrase honnête (2e sur GitHub, 1er chez TIOBE) et on finit sur un Python qui tient ;
- **relance forte** : la coupure musicale passe de 66 % à 62 % (7:53) (sections 1 à 6 resserrées, fin rallongée) ; elle porte maintenant la phrase la plus dure du mail (« tant de gens méprisent mes décisions », fait 28) ;
- **faits** : « On lit souvent qu'il a créé Python en une semaine » (aucune source ne le dit) devient la question que le hook fait naître chez le spectateur ; « un truc que peu de langages ont vécu » et « Il lui fallait du temps devant lui » retirés (non sourcés) ; « un langage qui a raté » devient « qui n'a pas percé » (« faute de succès évident ») ; la légende de l'ennui est attribuée à une vraie page (fait 27) ; le surnom « morse » vient de la doc officielle (fait 29) ; la réunion de 1995 est décrite (fait 30) ; Dropbox et Python 3 (fait 33) remplacent la boîte imaginaire de la section 6 ;
- **tics** : « Normalement, c'est le moment où je te dis qu'ABC a changé le monde », « Et c'est là que la légende en rajoute une couche », « Et regarde la boucle », « Normalement, avec un hook comme le mien » et « Bref, le projet de vacances ne gagne plus tout » retirés ; « en gros » passe de 5 à 2 ;
- **rafales** : les dates de Python 2 et 3 sans les jours, le 2.7.18 retiré, les chiffres de la section 8 un par un avec leur liaison.

**Boucles ouvertes** :
1. « Le mot, il finira par l'écrire, plus de trente ans plus tard » (hook, 0:30) : refermée dans la section 9 par le tweet de 2020.
2. « C'est quoi, ABC ? Et pourquoi il a déjà un langage en tête ? » (section 1) : refermée dans la section 2.
3. « Titre de travail » : un nom provisoire (section 3), récolté en section 8 (« pas mal, pour un nom provisoire ») et à la fin.
4. « Retiens Barry Warsaw, et retiens “à vie” » (section 5) : « à vie » refermé en section 7, Barry Warsaw en section 8.
5. « Est-ce que Python peut tenir sans le mec qui l'a inventé ? » (fin de la section 7) : refermée dans la section 8.
6. Ta question du début, ennui ou pas (hook) : refermée dans la section 9.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Les faits viennent uniquement des lignes ✅ de [`sources.md`](sources.md), et des ⚠️ avec la formulation qu'il donne.

---

## 0. Hook (0:00 – 0:34) · objectif : 75 % à 0:15

[VISUEL : écran noir de la charte. Ta question s'écrit en blanc, mot par mot. Pas de titre, pas de logo.]

À quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation ?

[VISUEL : un appartement d'Amsterdam la nuit, une guirlande à la fenêtre, un vieil écran cathodique allumé. Texte en bas : « Décembre 1989 ».]

Noël quatre-vingt-neuf. Un dev a son bureau fermé, et pas grand-chose d'autre sur les bras. Du coup, il commence un projet pour s'occuper.

[VISUEL : dès « un projet », l'écran zoome sur le curseur, une ligne de temps file de 1989 à 2026, le logo Python se forme. « 57,9 % » s'affiche en grand, source en bas : « Stack Overflow, sondage 2025 ».]
[SON : un « bip » de vieil ordi, puis un whoosh.]

Aujourd'hui, presque six devs sur dix disent s'en servir. Et c'est le langage de l'IA. Ça s'appelle Python.

Sauf que lui, ce Noël-là, il ne parle jamais d'ennui. Le mot, il finira par l'écrire, mais plus de trente ans plus tard. Et pas à Noël.

[VISUEL : le mot « ennui » s'écrit en rouge ; dessous, une date floutée, « ??/??/20?? ».]

---

## 1. La légende (0:34 – 2:08)

Parce que la version qu'on raconte, c'est celle-là. Tu la trouves même noir sur blanc sur un site de biographies d'ingénieurs. Et je te cache pas que c'était la mienne au début : il se faisait tellement chier qu'il a décidé de créer un langage de programmation.

[VISUEL : ta phrase s'affiche comme une citation ; à côté, la capture d'Interesting Engineering, « he found himself bored » surligné. Un tampon « LÉGENDE » vient écraser les deux.]
[SON : coup de tampon.]

Sauf que le dev en question, Guido van Rossum, a raconté lui-même ce Noël-là. En mille neuf cent quatre-vingt-seize, dans la préface d'un livre, *Programming Python*. Et sa phrase, la voilà.

[VISUEL : la préface en anglais sur python.org, les deux phrases surlignées l'une après l'autre ; la traduction s'écrit en dessous. Lien en description.]

« En décembre mille neuf cent quatre-vingt-neuf, je cherchais un projet de programmation “pour le loisir” qui m'occuperait pendant la semaine autour de Noël. Mon bureau, un labo de recherche public à Amsterdam, allait être fermé, mais j'avais un ordinateur à la maison, et pas grand-chose d'autre sur les bras. »

Tu vois ? Il cherche un truc pour s'occuper. Le mot « ennui », il n'est nulle part.

Moi, une semaine sans rien sur les bras, j'appelle ça s'ennuyer. Lui, il appelle ça un projet de loisir. Et son loisir à lui, c'est d'écrire un interpréteur, pour faire simple le programme qui lit ton code et l'exécute, pour un nouveau langage auquel il pensait depuis quelque temps. Je cite encore : « un descendant d'ABC qui plairait aux hackers Unix et C ».

[VISUEL : « descendant d'ABC » reste à l'écran, les lettres ABC grossissent.]

Donc, deux questions. C'est quoi, ABC ? Et pourquoi un mec qui veut juste s'occuper pendant les fêtes a déjà un langage dans la tête ?

---

## 2. Le langage qui n'a pas percé (2:08 – 3:31)

Pour le comprendre, il faut reculer de sept ans. Fin quatre-vingt-deux, Guido sort de la fac et entre au CWI, l'institut de recherche en maths et en informatique d'Amsterdam. Il y est programmeur, dans l'équipe d'un langage qui s'appelle justement ABC, celle de Lambert Meertens et Steven Pemberton.

[VISUEL : une carte d'Amsterdam, un point sur le CWI ; trois silhouettes en 2D avec leurs noms. Ligne de temps en bas : 1982.]

ABC, t'en as sûrement jamais entendu parler. Et c'est normal : le projet est arrêté au bout de quatre ou cinq ans, faute de succès évident. C'est Guido lui-même qui l'écrit, sur son blog, en deux mille neuf.

[VISUEL : le logo ABC (reconstitué) tombe dans un tiroir qui se referme.]
[SON : tiroir qui claque.]

Imagine : tu sors de la fac, tu bosses des années dans l'équipe d'un langage, et un jour on range tout dans un tiroir.

Et pourtant, dans le même billet, il dit qu'ABC lui a donné « l'inspiration clé » de Python. En gros, Python, c'est le fils d'un langage qui n'a pas percé.

[TON AVIS DE DEV, SI TU EN AS UN : UN PROJET QUI A FOIRÉ ET QUI T'A SERVI PLUS TARD. UNE PHRASE.]

Voilà pourquoi, quand son bureau ferme pour Noël, il a déjà une idée qui lui trotte dans la tête. Et là, il a une semaine devant lui.

Il lui manque juste un nom.

**Abonnement (≈ 3:18, 26 % de la vidéo, juste avant la révélation du nom)**

Et avant de te le donner : si t'aimes savoir d'où viennent les outils que tu utilises tous les jours, abonne-toi. Sur Technovore, on raconte leur histoire, et on ouvre le capot.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; le tiroir d'ABC reste à l'écran.]

---

## 3. Pas de serpent (3:31 – 4:22)

Python. Forcément, tu penses au serpent. Sauf que le nom vient d'une bande de comiques britanniques.

[VISUEL : un serpent en pixel art glisse vers le centre de l'écran… et se fait écraser par un pied géant façon collage (création maison, aucun extrait de la série).]
[SON : « splotch » cartoon.]

Guido l'écrit dans la même préface : il choisit « Python » comme titre de travail, « dans une humeur un peu irrévérencieuse », et parce qu'il est grand fan du *Monty Python's Flying Circus*.

Et la FAQ officielle de Python complète. Quand il commence à coder, il lit les scripts publiés de la série, une émission comique de la BBC des années soixante-dix. Et il veut un nom court, unique, et un peu mystérieux.

[VISUEL : la FAQ de docs.python.org, « short, unique, and slightly mysterious » surligné.]

[TA RÉACTION OU TA RÉFÉRENCE MONTY PYTHON, SI TU EN AS UNE. UNE PHRASE.]

Note bien les mots « titre de travail ». C'est un nom provisoire, en attendant de trouver mieux. Trente-sept ans plus tard, personne n'a trouvé mieux.

[VISUEL : une étiquette « provisoire » scotchée sur le logo Python, qui jaunit et se décolle à mesure que les années défilent.]

Bon. Il a un nom provisoire, un ordi et une semaine de libre.

---

## 4. En une semaine ? (4:22 – 5:34)

Là, tu dois te demander : en une semaine, il a fait un langage entier ?

[VISUEL : « Python, créé en une semaine ? » s'affiche, le point d'interrogation clignote.]

Eh ben non, et c'est encore lui qui le dit, sur son blog : il commence à travailler sur Python fin décembre quatre-vingt-neuf, et il a une version qui marche dans les premiers mois de quatre-vingt-dix.

Donc la semaine de Noël, c'est le départ. Le reste, c'est des mois de boulot.

[VISUEL : un calendrier de décembre 1989, la semaine de Noël entourée ; les pages tournent, mois après mois, jusqu'à février 1991.]

Et pour que d'autres gens puissent s'en servir, il faut même attendre le vingt février quatre-vingt-onze. Ce jour-là, il publie la version zéro point neuf point zéro sur alt.sources, un forum Usenet où les devs postaient du code. Pas de GitHub, pas de bouton « télécharger » : le code arrive dans des messages, et c'est à toi de le récupérer.

[VISUEL : une fenêtre de terminal verte sur noir, un message Usenet reconstitué, « 0.9.0 ». En petit : « reconstitution ».]

Quatorze mois. En fait, son projet de vacances, il l'a fait tenir bien après les vacances.

Python un point zéro arrive en janvier quatre-vingt-quatorze, et là, Python commence à avoir du monde autour. Sauf que plus il y a de monde, plus il y a d'avis. Il faut bien quelqu'un pour trancher.

---

## 5. Dictateur à vie (5:34 – 6:41)

En avril quatre-vingt-quinze, Guido quitte Amsterdam pour les États-Unis. Il rejoint le CNRI, un centre de recherche à Reston, en Virginie. D'ailleurs, la préface du projet de Noël, il la signera là-bas, un an plus tard.

[VISUEL : un avion en papier traverse l'Atlantique d'Amsterdam à Reston ; la signature « Reston, VA, May 1996 » de la préface apparaît.]

Et le dix-huit avril, le mois de son arrivée, huit personnes se réunissent pour monter une organisation autour de Python. C'est là que Guido récupère un titre. BDFL : Benevolent Dictator For Life. Le dictateur bienveillant à vie.

[VISUEL : huit silhouettes autour d'une table ; une couronne en carton se pose sur la tête de Guido en 2D, « BDFL » en lettres dorées.]
[SON : fanfare ridicule, trois notes.]

Pour faire simple : sur Python, le dernier mot, c'est lui. Bienveillant, d'accord, mais dictateur quand même.

Et qui a trouvé le surnom ? Même Guido ne sait plus. D'après lui, c'est sans doute Ken Manheimer ou Barry Warsaw, peut-être toute la salle. Et il ajoute qu'à son avis, plus personne ne s'en souvient.

[VISUEL : deux silhouettes floues avec un point d'interrogation, « Ken Manheimer ? Barry Warsaw ? ».]

Du coup, retiens Barry Warsaw. Et retiens surtout les deux derniers mots, « à vie ». On y reviendra.

Parce que sous son règne, Python va vivre un truc bien pénible : deux versions incompatibles, côte à côte, pendant onze ans.

---

## 6. Deux Python pour le prix d'un (6:41 – 7:53)

Python deux sort en deux mille. Huit ans plus tard, en décembre deux mille huit, arrive Python trois. Sauf que Python trois, sa propre page de téléchargement le dit : il est incompatible avec la branche deux.

[VISUEL : deux routes qui partent du même point, « 2.x » et « 3.0 », qui s'écartent.]

Imagine la mise à jour de ton jeu préféré qui casse tes sauvegardes. T'as cent heures de jeu, et tu repars de zéro. Là, c'est pareil, mais avec du code : ton programme écrit pour Python deux peut ne plus tourner sur Python trois.

[VISUEL : un écran de jeu « Sauvegarde corrompue », qui devient un terminal rouge plein d'erreurs.]
[SON : le « buzz » d'erreur d'un vieux jeu.]

Résultat, les deux vivent ensemble pendant des années. Même chez Dropbox, la boîte où Guido bosse à la fin des années deux mille dix, c'est lui qui lance le passage du code serveur de Python deux à Python trois.

[VISUEL : le billet de blog de Dropbox (29/10/2019), « conversion of the Dropbox server code from Python 2 to Python 3 » surligné.]

Et Python deux ne s'arrête officiellement que le premier janvier deux mille vingt, onze ans après Python trois. Un premier janvier, en plus. Pour le Nouvel An, les devs Python ont eu droit à un enterrement.

[VISUEL : un gâteau du Nouvel An avec une bougie « 2 » qui s'éteint ; confettis en noir et blanc.]

[TON VÉCU, SI TU EN AS UN : TU AS CONNU PYTHON 2, OU TU ES ARRIVÉ DIRECTEMENT SUR PYTHON 3 ?]

Bref, onze ans de transition. Et pendant tout ce temps, le dictateur tient. Mais en deux mille dix-huit, il y a une proposition qui passe mal.

---

## 7. Vacances permanentes (7:53 – 9:29) · relance forte à 62 %

[SON : la musique coupe net, une seconde de silence.]

Un PEP, c'est une proposition pour faire évoluer Python. Et en deux mille dix-huit, il y en a une qui coince : le PEP cinq cent soixante-douze. Il ajoute un opérateur, deux points égal. Et la doc officielle le surnomme elle-même « l'opérateur morse », parce que ça ressemble aux yeux et aux défenses d'un morse.

[VISUEL : « := » à l'écran ; il pivote d'un quart de tour et devient les yeux et les défenses d'un morse en pixel art.]

Le PEP finit par passer. Sauf que le douze juillet deux mille dix-huit, Guido envoie un mail aux développeurs du cœur de Python. Titre : « Transfer of power ». Le transfert du pouvoir.

[VISUEL : le mail réel de la liste python-committers, daté « Thu Jul 12 10:57:35 EDT 2018 », les phrases surlignées une à une. Lien en description.]

Il écrit : « Maintenant que le PEP cinq cent soixante-douze est fait, je ne veux plus jamais avoir à me battre autant pour un PEP, et découvrir que tant de gens méprisent mes décisions. » Et il se donne, je cite, « des vacances permanentes » de son rôle de BDFL.

Imagine. T'as inventé le langage, t'en es le chef depuis plus de vingt ans, et des gens méprisent tes décisions pour deux caractères. Deux points, égal.

Tu te rappelles ? Dictateur bienveillant à vie. Eh ben la vie, elle aura duré vingt-trois ans.

[VISUEL : la couronne en carton tombe de la tête de Guido ; compteur « 1995 → 2018 : 23 ans ».]

Python est né d'une semaine de vacances. Et le règne de son créateur finit sur des vacances. Permanentes, cette fois.

[VISUEL : écran coupé en deux : à gauche le calendrier de décembre 1989, à droite le mail de juillet 2018, le mot « vacances » surligné des deux côtés.]

Il ne nomme même pas de successeur. Par contre, il ne part pas : il reste simple développeur du cœur.

Donc la vraie question, à ce moment-là, c'est : est-ce que Python peut tenir sans le mec qui l'a inventé ?

---

## 8. Sans dictateur (9:29 – 11:09)

Et la réponse arrive vite. En décembre deux mille dix-huit, les développeurs du cœur votent. À la place du dictateur, un conseil de cinq personnes, réélu après chaque grande version de Python.

[VISUEL : la couronne en carton posée sur une table ; cinq chaises apparaissent autour, une par une.]

Début deux mille dix-neuf, ils élisent le premier. Et dans les cinq, il y a Guido lui-même. Et Barry Warsaw, tu te rappelles ? Un des deux suspects du surnom « à vie ». En gros, le mec qui a peut-être inventé le dictateur à vie s'assoit à la table qui le remplace.

[VISUEL : les cinq noms du premier conseil (PEP 8100) s'affichent sur les chaises ; « Barry Warsaw » s'allume, le point d'interrogation de la section 5 revient au-dessus de lui.]

Et pour le reste, les chiffres répondent. Sur GitHub, Python progresse de quarante-huit pour cent en un an, d'après le rapport Octoverse de deux mille vingt-cinq. Et le même rapport l'appelle « la colonne vertébrale » de l'IA appliquée.

[VISUEL : « +48 % » plein écran, puis la phrase « the backbone of applied AI work » surlignée. Source en bas : GitHub Octoverse 2025.]

Chez Stack Overflow, c'est cinquante-sept virgule neuf pour cent des développeurs interrogés en deux mille vingt-cinq. Tu vois, les presque six sur dix du début. Et c'est sept points de plus qu'un an avant.

[VISUEL : « 57,9 % » plein écran, une flèche « +7 points ». Source en bas : Stack Overflow Developer Survey 2025.]

Alors oui, si t'as vu passer que TypeScript l'a doublé sur GitHub : c'est vrai. En août deux mille vingt-cinq, d'environ quarante-deux mille contributeurs par mois. Du coup, sur GitHub, Python est deuxième.

[VISUEL : la courbe Octoverse, TypeScript qui croise Python en août 2025 ; « ~42 000 contributeurs d'écart ».]

Et en octobre deux mille vingt-six, l'indice TIOBE le met encore numéro un. Le projet de vacances a même eu droit à son propre documentaire en deux mille vingt-cinq, qui dépasse le million de vues sur YouTube. Pas mal, pour un nom provisoire.

[VISUEL : le classement TIOBE d'octobre 2026, Python en tête, daté ; puis l'étiquette « provisoire » de la section 3 se recolle une seconde sur le logo.]

[TON PREMIER SCRIPT PYTHON : QUAND, ET CE QU'IL FAISAIT. UNE OU DEUX PHRASES.]

Bref, Python tient très bien sans son dictateur. Mais Guido, lui, il devient quoi ?

---

## 9. Alors, il s'ennuyait ? (11:09 – 12:50)

En octobre deux mille dix-neuf, il quitte Dropbox et prend sa retraite. Les vacances permanentes, pour de vrai.

[VISUEL : le billet de Dropbox, « heading into retirement » surligné ; un transat et un parasol en 2D.]

Sauf qu'un an plus tard, le douze novembre deux mille vingt, il tweete, je cite : « J'ai décidé que la retraite, c'était ennuyeux, et j'ai rejoint la division développeurs de Microsoft. »

[VISUEL : la capture du tweet original ; « retirement was boring » surligné du même rouge que le mot « ennui » du hook. La date floutée du hook se révèle : « 12/11/2020 ».]
[SON : le « bip » de vieil ordi du hook.]

Le voilà, le mot. Plus de trente ans après Noël quatre-vingt-neuf. Et pas pendant les fêtes : à la retraite.

Donc on revient à ma question. À quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation ? Guido, à Noël quatre-vingt-neuf, avait un bureau fermé, une idée tirée d'un langage qui n'a pas percé, et pas grand-chose d'autre sur les bras. En fait, lui, il appelait ça un projet de loisir.

[VISUEL : la préface revient, la phrase « not much else on my hands » surlignée, à côté du tweet.]

Moi, j'appelle toujours ça s'ennuyer. [TON VERDICT, AVEC TES MOTS : ENNUI OU PAS ? PISTE SI ELLE TE VA : « SAUF QUE CHEZ UN DEV, L'ENNUI, ÇA RESSEMBLE À ÇA : PERSONNE NE TE DEMANDE RIEN, ALORS TU CODES POUR TOI. »] Et en effet, le jour où il dit enfin qu'il s'ennuie, il retourne bosser sur Python.

Et ça tombe bien. Cette semaine, entre Noël et le Nouvel An, il y a des chances que ton bureau, ta fac ou ton école soit fermé. T'as peut-être un ordi à la maison, et pas grand-chose d'autre sur les bras.

[VISUEL : le même appartement que dans le hook, mais en 2026 : un laptop à la place de l'écran cathodique, la guirlande à la fenêtre. Le curseur clignote.]

Tu vois où je veux en venir.

Donc dis-moi en commentaire ce que tu coderais, toi, avec une semaine de libre. Et si tu le commences, garde un titre de travail. Ça porte chance.

Et si t'as encore du temps devant toi, l'histoire du jeu vidéo, d'un seul pixel à des milliards de joueurs, c'est la vidéo juste là. Bonnes fêtes.

[VISUEL : écran de fin, 20 s : la vidéo du pixel (14 déc.) à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Question | Ta question, en première phrase |
| 0:10 | Visuel | La ligne de temps 1989 → 2026 et le « 57,9 % » |
| 0:16 | Chiffre | « Presque six devs sur dix », « le langage de l'IA » |
| 0:23 | Boucle ouverte | « Le mot, il finira par l'écrire, trente ans plus tard » (refermée à 11:30) |
| 0:40 | Son + visuel | Le tampon « LÉGENDE » sur ta phrase et sur la page anglaise |
| 1:26 | Retournement | « Le mot ennui, il n'est nulle part » |
| 1:58 | Boucle ouverte | « C'est quoi, ABC ? » (refermée à 2:28) |
| 2:28 | Son | Le tiroir qui claque : ABC arrêté |
| 2:59 | Formule | « Le fils d'un langage qui n'a pas percé » |
| 3:18 | Appel à l'action | Abonnement (26 %), glissé avant la révélation du nom |
| 3:31 | Gag visuel | Le serpent écrasé par le pied géant |
| 4:13 | Humour | « Titre de travail » : trente-sept ans de provisoire |
| 4:22 | Question | « Tu dois te demander : en une semaine ? » |
| 5:12 | Chiffre | Quatorze mois jusqu'à la première version publique |
| 6:00 | Son + visuel | Huit personnes, la couronne en carton, « BDFL » |
| 6:26 | Planté | « Retiens Barry Warsaw, et retiens “à vie” » (récoltés à 9:01 et 9:55) |
| 6:56 | Référence gamer | La sauvegarde corrompue |
| 7:37 | Humour | L'enterrement de Python 2 au Nouvel An |
| 7:53 | Coupure musique | Relance forte (62 %) : le PEP qui coince, le morse |
| 8:28 | Choc | « Tant de gens méprisent mes décisions » |
| 9:01 | Récolte | « La vie, elle aura duré vingt-trois ans » |
| 9:05 | Motif | Une semaine de vacances / des vacances permanentes |
| 9:21 | Boucle ouverte | « Python peut-il tenir sans lui ? » (refermée à 9:29 – 11:07) |
| 9:55 | Récolte | Barry Warsaw à la table qui remplace le dictateur |
| 10:32 | Retournement | TypeScript devant sur GitHub, Python deuxième |
| 11:01 | Récolte | « Pas mal, pour un nom provisoire » |
| 11:07 | Boucle ouverte | « Mais Guido, lui, il devient quoi ? » |
| 11:17 | Retournement | Le tweet : « la retraite, c'était ennuyeux » |
| 11:38 | Boucle fermée | Retour à ta question |
| 12:08 | Récolte | La semaine de Noël du spectateur : même décor que le hook |
| 12:28 | Engagement | « Ce que tu coderais avec une semaine de libre » |

**Total** : 31 relances en 12 min 50, environ une toutes les 25 secondes. Le plus long trou : 3:31 → 4:13 (42 s), couvert par le gag du serpent et la FAQ à l'écran.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15 | Moyen | Le chiffre (presque six devs sur dix) tombe vers 0:16 à 145 mots/min, vers 0:13 en coupes serrées | La ligne de temps 1989 → 2026 et le « 57,9 % » s'affichent dès « un projet » (≈ 0:10), avant que la voix le dise |
| La citation de la préface (section 1) | Moyen | Quarante mots lus d'un bloc | Surlignée phrase par phrase à l'écran, et « Tu vois ? » juste après pour réagir |
| CWI et ABC (section 2) | Élevé | Le seul passage biographique, avec trois noms propres | Le tiroir qui claque, « le fils d'un langage qui n'a pas percé », et la réponse à la question ouverte juste avant |
| Python 2 / 3 (section 6) | Moyen | Des dates | Deux dates seulement, sur une ligne de temps ; la sauvegarde corrompue, Dropbox, l'enterrement du Nouvel An |
| Relance (section 7) | Élevé | Chute classique vers 60 % | Coupure musicale, le morse, la phrase « tant de gens méprisent mes décisions », puis la récolte « à vie » dans la minute |
| Les chiffres de la section 8 | Moyen | Quatre chiffres en une minute | Un seul chiffre plein écran à la fois, chacun avec sa liaison ; Barry Warsaw juste avant pour relancer le récit |

## Notes de montage

- **Pilier « grandes histoires »** : charte noire (`noir.html`). Animations simples : une ligne de temps 1982-2026 qui revient à chaque section, le tampon « LÉGENDE » (section 1), le calendrier de décembre 1989 (sections 4, 7 et la fin).
- **Le mot « ennui » en rouge** : il apparaît dans le hook avec une date floutée, et la date se révèle sur le tweet de la section 9. C'est la récolte visuelle principale.
- **Guido en 2D** : un personnage stylisé, sans chercher la ressemblance photo. Les captures autorisées : la préface sur python.org, la FAQ, la chronologie du blog *The History of Python*, le mail de python-committers, la doc de Python 3.8, le PEP 8100, le billet de Dropbox, le tweet du 12/11/2020, les pages Octoverse, Stack Overflow et TIOBE, la page d'Interesting Engineering.
- **Monty Python** : aucun extrait de la série, aucune musique, aucun visuel officiel. Le collage « pied géant » est une création maison dans l'esprit, rien de plus.
- **Le morse** : `:=` qui pivote, en pixel art. C'est le gag visuel de la relance.
- **Énergie** : calme dans les sections 1-2 (citations), montée sur le nom (3), sur Python 2 / 3 (6), coupure puis montée sur la section 7, un sourire sur Barry Warsaw (8), ton chaleureux à la fin.
- **La fin** reprend le décor du hook (même appartement, 2026).

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1 | « je cherchais un projet de programmation “pour le loisir” qui m'occuperait pendant la semaine autour de Noël » (section 1) ; « il commence un projet pour s'occuper » (hook) ; la préface signée à Reston en mai 1996 (section 5) |
| 2 | « son bureau fermé, et pas grand-chose d'autre sur les bras » (hook, section 1, fin) |
| 3 | « un nouveau langage auquel il pensait depuis quelque temps… un descendant d'ABC qui plairait aux hackers Unix et C » (section 1) |
| 4 | « titre de travail », « dans une humeur un peu irrévérencieuse », fan du *Monty Python's Flying Circus* (section 3) |
| 5 (⚠️) | « ce Noël-là, il ne parle jamais d'ennui » ; « Moi, j'appelle ça s'ennuyer » : l'ennui de 1989 reste ta lecture, jamais ses mots (hook, sections 1 et 9) |
| 6 | les scripts publiés, série comique de la BBC des années soixante-dix, « court, unique, et un peu mystérieux » (section 3) |
| 7 | fin 1982, sorti de la fac, programmeur au CWI, équipe ABC de Lambert Meertens et Steven Pemberton (section 2) |
| 8 | arrêté « au bout de quatre ou cinq ans, faute de succès évident » ; « l'inspiration clé » (section 2) |
| 9 | « fin décembre 1989… une version qui marche dans les premiers mois de 1990 » (section 4) |
| 10 | 0.9.0 sur alt.sources le 20/02/1991 (section 4) |
| 11 | 1.0 en janvier 1994 (section 4) ; 2.0 en 2000, 3.0 en décembre 2008 (section 6) |
| 12 | « incompatible avec la branche deux » (section 6) |
| 13 | fin de Python 2 le 01/01/2020 (section 6) |
| 14 | arrivée au CNRI en avril 1995 ; réunion du 18/04/1995 ; « sans doute Ken Manheimer ou Barry Warsaw, peut-être toute la salle… plus personne ne s'en souvient » (section 5) ; « un des deux suspects » (section 8) ; 1995 → 2018, vingt-trois ans (section 7) |
| 15 | mail du 12/07/2018 « Transfer of power », la phrase sur le PEP, « vacances permanentes », pas de successeur, reste développeur du cœur ; PEP 572 et `:=` (section 7) |
| 16 | Python +48 %, « la colonne vertébrale » de l'IA appliquée, TypeScript devant en août 2025 de ~42 000 contributeurs, « deuxième sur GitHub » (section 8) |
| 17 | TIOBE octobre 2026 : numéro un (section 8, daté) |
| 18 | Stack Overflow 2025 : 57,9 %, « presque six devs sur dix », +7 points (hook, section 8) |
| 21 | le documentaire de 2025, « dépasse le million de vues » (section 8 ; chiffre vidIQ du 23/10/2026, à redater avant la voix) |
| 24 | « c'est le langage de l'IA » (hook ; tenu par le fait 16, sans « numéro un ») |
| 26 (❌) | « créé en une semaine » : posé comme la question du spectateur, corrigé par les faits 9 et 10 (section 4) |
| 27 | la légende de l'ennui « noir sur blanc sur un site de biographies d'ingénieurs » (section 1) |
| 28 | « et découvrir que tant de gens méprisent mes décisions » ; « Le PEP finit par passer » (« Now that PEP 572 is done ») ; « simple développeur du cœur » (section 7) |
| 29 | « la doc officielle le surnomme elle-même l'opérateur morse » (section 7) |
| 30 | « huit personnes se réunissent pour monter une organisation autour de Python » (section 5) ; « Python commence à avoir du monde autour » (section 4) |
| 31 | vote de décembre 2018, conseil de cinq, réélu après chaque grande version (section 8) |
| 32 | premier conseil début 2019, avec Guido et Barry Warsaw (section 8) |
| 33 | Dropbox et le passage du code serveur à Python 3 (section 6) ; retraite en octobre 2019 (section 9) |
| 34 | le tweet du 12/11/2020, « la retraite, c'était ennuyeux », Microsoft (hook : « plus de trente ans plus tard » ; section 9) |

Non utilisés : 19 (PSF, retirée : le copyright ne répondait pas à la question de la gouvernance), 20 (Mars, ❓), 22 (Codabee, sert au titre), 23 (253 K vues, ❓). Le −5,23 points de TIOBE (fait 17) et la 2.7.18 (fait 13) sont retirés pour alléger les rafales de chiffres.

## Phrases du brouillon

| Ta phrase | Dans le script | Pourquoi |
|---|---|---|
| « A quel moment tu t'ennuies assez pour avoir envie de créer un langage de programmation » | **Gardée** telle quelle (avec l'accent sur « À »), en **première phrase** de la vidéo comme dans ton brouillon, et reprise dans la fin | C'est ta question au spectateur, pas une citation de Guido (fait 5). La V1 la plaçait au 50e mot |
| « Lui c'est... » | **Complétée** : « le dev en question, Guido van Rossum » (section 1) | Le nom arrive après la question et le contraste ; dans le hook, c'est « un dev » |
| « Et il se fesait tellement chier qu'il a décidé de créer un langage de programmation » | **Gardée, devenue la légende** (section 1), attribuée à une vraie page (fait 27), puis corrigée par sa vraie phrase ; ton « moi, j'appelle ça s'ennuyer » reste ta lecture, et le tweet de 2020 te donne raison à moitié | Guido ne dit jamais qu'il s'ennuyait à Noël 1989 (faits 2 et 5) ; il le dit de sa retraite (fait 34). Orthographe : « se faisait » |

## Questions pour l'auteur

1. **Le titre** : tranché le 23/10 (voir en tête). Il t'oblige à garder « c'est le langage de l'IA » dans le hook et la phrase d'Octoverse en section 8 : les deux y sont.
2. **La fin avec le tweet de 2020** (« la retraite, c'était ennuyeux ») : elle te va ? Elle change ta fin : ton verdict n'a plus à tout porter, le fait répond à moitié à ta question. Fais une capture du tweet original (compte @gvanrossum) : on n'a pu le lire que cité par TechCrunch et InfoWorld (fait 34).
3. **Ton verdict de la fin** (section 9) : ennui ou pas ? La piste entre crochets est une proposition, pas ta phrase. Dis-la avec tes mots, ou change-la.
4. **Ton vécu** : ton premier script Python (section 8), Python 2 ou 3 (section 6), un projet raté qui t'a servi (section 2). Si tu n'as rien de vrai, on coupe les crochets.
5. **Le contrepied** : je l'ai gardé en une phrase (« Alors oui, si t'as vu passer que TypeScript l'a doublé… ») et la section 8 finit sur un Python qui tient. Si tu veux un vrai « Python ne gagne plus tout », dis-le, mais il casse la montée vers la fin.
6. **L'écran de fin** pointe le pixel (14 déc.), la vidéo précédente du pilier. D'accord ?
7. **L'entretien de Guido sur la chaîne GitHub** (253 K vues, `strategie.md`) : si tu as l'URL, il peut servir de vidéo hôte dans `upload.md`.
