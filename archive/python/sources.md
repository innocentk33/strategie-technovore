# Python, ou l'ennui d'un dev à Noël : sources

> Phase 1 (recherche) du 23/10/2026.
> 2e vérification (Opus) du 23/10/2026 : 21 ✅ · 2 ⚠️ · 1 ❌ · 2 ❓.

## vidIQ (23/10/2026)

### Mots-clés (France)
| Mot-clé | Volume/mois | Concurrence | Remarque |
|---|---|---|---|
| histoire de python | < 750 | 9 | Aucune demande mesurable, mais presque aucune concurrence |
| python | 1 096 429 (−21 %) ; France : 12 603 | 60,6 | Mot-clé de la fiche ; 30 % du volume vient d'Inde |
| apprendre python | 16 296 (−37 %) | 39,4 | La demande française est pour apprendre, pas pour l'histoire |
| programmation | 17 551 (+323 %) | 44,9 | Pic récent |
| machine learning | 272 419 (−25 %) | 59,5 | Lien avec l'IA |

### Vidéos de référence (EN)
| Titre | Chaîne (abonnés) | Vues | × moyenne | URL | Ce qu'on retient |
|---|---|---|---|---|---|
| The Story of Python and how it took over the world, *Python: The Documentary* | CultRepo (424 K) | 1,29 M | n/d (vph 58) | youtu.be/GfH4QL4VqJ0 | Documentaire de 84 min avec Guido, Lambert Meertens, Steven Pemberton, Barry Warsaw. Hook : « Did you think Python was going to get popular from the beginning? » puis l'impact (Mars, IA). Structure : ABC et CWI (1:10), l'Amoeba (3:50), Guido crée Python (5:26), version publique (8:38), BDFL (18:21), Python 2→3 (42:59), départ de Guido (1:14:14) |
| The Story of Python, by Its Creator, Guido van Rossum | Oracle Developers (119 K) | 322 K | n/d | youtu.be/J0Aq44Pze-w | Entretien de 4 min (2019), format court |
| Guido van Rossum: The TRUE History Behind The Python Programming Language | Behind The Code (14,3 K) | 31 K | 77× | youtu.be/ucD_1ryKKm0 | Récit de 5 min : prouve qu'un récit court peut sur-performer |
| L'entretien de Guido sur la chaîne GitHub (253 K vues, cité par l'auteur) | GitHub | | | | ❓ introuvable par `vidiq_youtube_search` : demander l'URL à l'auteur |
Les outliers EN de la passe (`vidiq_outliers`, six mois) ne contiennent aucune histoire de Python : ils remontent des cours (« Python Full Course ») et des récits d'autres langages (*The Rise and Fall of Visual Basic*, 90 K vues, 17 K ab.; *Why Is A 1957 Programming Language Still Running The World?*, COBOL, 163 K vues en 2 jours, 9,7 K ab., 24 min). Le format « histoire d'un langage » marche donc ailleurs.

### Ce qui existe en français
| Titre | Chaîne | Vues | Date | Angle (à ne pas copier) |
|---|---|---|---|---|
| **Il s'ennuyait à Noël: Il a créé Python** | Matthieu, Codabee (1,45 K ab.) | 263 | 18/09/2026 | Presque notre titre « curiosité » : décembre 1989, ABC, Monty Python, puis l'IA. Sources : PSF, Guido, CWI. 10 min |
| La grande histoire du langage Python ! | Émerick et le numérique | 1,7 K | 21/09/2024 | Récit court (3:53) |
| La naissance de Python : l'histoire de la création visionnaire de Guido van Rossum | Raskel Tech | 488 | 01/08/2023 | Court (2:18) |
| Langages de programmation : quel avenir face à l'IA ? | AXOPEN (6,7 K ab.) | 5 K | 03/09/2026 | Podcast, pas un récit |
Aucune grosse vidéo française (aucune au-dessus de 5 K vues).

### Ce que ça dit pour nous
- **Titre pris** : Codabee a sorti *Il s'ennuyait à Noël: Il a créé Python* le 18/09/2026, soit sept semaines avant. Avec 263 vues, il ne bloque pas la recherche, mais notre titre curiosité serait quasi identique et vidIQ les rapprochera. Verdict : **à revoir le titre et le hook**, pas le sujet.
- Demande : très faible sur « histoire de python » (< 750), et la demande française est pour apprendre (16 K). La vidéo doit marcher à l'accueil. Le ratio 77× de Behind The Code (14 K ab., 31 K vues, 5 min) montre qu'un récit court sur Guido peut dépasser sa chaîne.
- Angle libre : ce que personne n'a dit en français, c'est le contrepied d'aujourd'hui : Python n'est plus n° 1 sur GitHub (faits 15 et 16), alors que c'est le langage de l'IA. Un angle « du passe-temps d'une semaine à un langage qui ne gagne plus tout » reste à ton sous-texte (ce qui commence par un ennui). Décision à prendre.
- Mots à mettre dans le titre : « Python », « Guido van Rossum », « Noël 1989 ». À éviter : « il s'ennuyait » (déjà pris et Guido ne dit pas qu'il s'ennuyait : fait 5).

## Faits
| # | Affirmation (telle qu'on la dirait) | Source (URL ; auteur, date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| 1 | En décembre 1989, Guido van Rossum cherchait « un projet de programmation “de loisir” qui l'occuperait pendant la semaine de Noël » (« I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas ») | https://www.python.org/doc/essays/foreword/ ; G. van Rossum, préface de *Programming Python* (1re éd.), signée Reston VA, mai 1996 | ✅ source primaire lue | ✅ préface relue mot à mot (python.org, signée « Reston, VA, May 1996 ») : « Over six years ago, in December 1989, I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas. » Traduction fidèle : « un projet de programmation “pour le loisir” qui m'occuperait pendant la semaine autour de Noël » |
| 2 | « Mon bureau (un laboratoire de recherche d'État à Amsterdam) allait être fermé, mais j'avais un ordinateur à la maison, et pas grand-chose d'autre à faire » | Même préface | ✅ | ✅ texte exact : « My office (a government-run research lab in Amsterdam) would be closed, but I had a home computer, and not much else on my hands. » Traduction juste : « …et pas grand-chose d'autre sur les bras » (« à faire » est acceptable) |
| 3 | Il décide d'écrire un interpréteur pour « le nouveau langage de script auquel il pensait », « un descendant d'ABC qui plairait aux hackers Unix/C » | Même préface | ✅ | ✅ texte exact : « I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. » |
| 4 | Le nom : « Python » comme titre de travail, « dans une humeur un peu irrévérencieuse » et fan des Monty Python's Flying Circus | Même préface | ✅ | ✅ texte exact : « I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus). » |
| 5 | (brouillon) « Il se faisait tellement chier qu'il a décidé de créer un langage » / « À quel moment tu t'ennuies assez pour… » | Préface (faits 1-2) : Guido dit qu'il cherche un projet de loisir et n'avait « pas grand-chose d'autre » sous la main. Il ne dit jamais qu'il s'ennuyait | ⚠️ L'ennui est une interprétation, pas sa phrase. À assumer comme « on dirait de l'ennui », sans lui prêter une citation | ⚠️ confirmé : le mot « ennui » (ou « bored ») n'apparaît pas dans la préface. Formulation juste : « Il voulait un projet pour s'occuper pendant la semaine de Noël : son bureau était fermé, et il n'avait pas grand-chose d'autre sur les bras. » « Il s'ennuyait » se dit comme ta lecture (« moi, j'appelle ça s'ennuyer »), jamais comme ses mots |
| 6 | La FAQ officielle donne le nom : Guido lisait les scripts publiés de *Monty Python's Flying Circus* (série de la BBC des années 1970) et voulait un nom « court, unique et un peu mystérieux » | https://docs.python.org/3/faq/general.html (« Why is it called Python? ») | ✅ | ✅ FAQ relue mot à mot : « reading the published scripts from "Monty Python's Flying Circus", a BBC comedy series from the 1970s » ; « short, unique, and slightly mysterious » |
| 7 | Le CWI (Centrum Wiskunde & Informatica) est un institut de recherche d'Amsterdam ; Guido l'a rejoint fin 1982 comme programmeur dans le groupe ABC de Lambert Meertens et Steven Pemberton | https://python-history.blogspot.com/2009/01/personal-history-part-1-cwi.html ; G. van Rossum, 20/01/2009 | ✅ | ✅ billet du 20/01/2009 relu : fin 1982, « as a programmer in the ABC group », groupe de Lambert Meertens et Steven Pemberton |
| 8 | Le projet ABC a été arrêté « après 4 ou 5 ans, faute de succès évident » ; Guido le cite comme « l'inspiration clé » de Python | Même billet | ✅ | ✅ relu : arrêté après « 4 or 5 years » faute de succès évident ; « ABC gave me the key inspiration for Python » |
| 9 | « J'ai commencé à travailler sur Python fin décembre 1989 et j'avais une version qui marchait dans les premiers mois de 1990 » | Même billet | ✅ | ✅ relu : « working on Python in late December 1989 », version qui marche début 1990 |
| 10 | Python 0.9.0 est publié sur alt.sources le 20/02/1991 | https://python-history.blogspot.com/2009/01/brief-timeline-of-python.html (Guido, 2009) : « February 20, 1991: 0.9.0 (released to alt.sources) » | ✅ source primaire (ligne lue via résumé de page : relire le tableau) | ✅ tableau relu : « February 20, 1991 » / « 0.9.0 (released to alt.sources) » |
| 11 | Python 1.0 le 26/01/1994 ; 2.0 le 16/10/2000 ; 3.0 le 03/12/2008 | Même chronologie | ✅ | ✅ relu : 1.0.0 le 26/01/1994 (la chronologie écrit « 1.0.0 »), 2.0 le 16/10/2000, 3.0 le 03/12/2008 |
| 12 | Python 3.0 est « incompatible avec la branche 2.x », beaucoup de fonctions dépréciées retirées | https://www.python.org/download/releases/3.0/ | ✅ | ✅ page relue : « incompatible with the 2.x line of releases » |
| 13 | Python 2 a atteint sa fin de vie le 01/01/2020 ; dernière version : 2.7.18 (avril 2020) | https://www.python.org/doc/sunset-python-2/ | ✅ | ✅ page relue : fin le 01/01/2020 ; 2.7.18 publiée en avril 2020 (la page précise que cette date n'est pas la fin du support) |
| 14 | « BDFL » (benevolent dictator for life) : le terme date de 1995, peu après l'arrivée de Guido au CNRI (Reston), via un courriel de Ken Manheimer, « for life » ajouté par Barry Warsaw ; Guido dit lui-même que c'est probablement Manheimer ou Warsaw | https://en.wikipedia.org/wiki/Benevolent_dictator_for_life ; Guido est arrivé au CNRI en avril 1995 (python-history.blogspot.com/2009/01/personal-history-part-2-cnri-and-beyond.html) | ⚠️ secondaire pour l'origine du mot : lire le courriel de Manheimer | ✅ remonté à la source primaire : billet de Guido « Origin of BDFL » (artima.com, 31/07/2008) : le titre vient d'une réunion du 18/04/1995, « most likely invented by Ken Manheimer or Barry Warsaw, though it may well have been a joint invention by all present », et il ajoute « I doubt that anyone remembers ». Dire « le surnom naît en 1995, en réunion, et même Guido ne sait plus qui l'a inventé » |
| 15 | Le 12/07/2018, Guido écrit à python-committers (« Transfer of power ») qu'il ne veut plus « se battre si fort pour un PEP », se donne « des vacances permanentes » de BDFL et ne nommera pas de successeur | https://mail.python.org/pipermail/python-committers/2018-July/005664.html (jeudi 12/07/2018, 10:57 EDT) | ✅ source primaire. Le PEP en cause est le PEP 572 (opérateur morse `:=`) | ✅ courriel relu : jeudi 12/07/2018 10:57:35 EDT, « Transfer of power » ; « I don't ever want to have to fight so hard for a PEP » ; « giving myself a permanent vacation from being BDFL » ; « I am not going to appoint a successor ». Il reste développeur du cœur |
| 16 | Octoverse 2025 : TypeScript a dépassé Python et JavaScript en août 2025 et devient le langage le plus utilisé sur GitHub, avec 2 636 006 contributeurs mensuels, devant Python d'environ 42 000 ; Python progresse de 48 % sur un an et reste « la colonne vertébrale » de l'IA et de la data | https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/ ; GitHub, 28/10/2025 (mis à jour le 28/02/2026) | ✅ source primaire. ❌ pour toute phrase « Python est le langage n° 1 de GitHub » : c'est faux depuis août 2025 (mesuré en contributeurs) | ✅ billet relu (28/10/2025, mis à jour 28/02/2026) : TypeScript « overtook both Python and JavaScript in August 2025 », 2 636 006 contributeurs mensuels, « surpassing Python by ~42k contributors » ; Python +48,78 % (arrondi +48 %), « the backbone of applied AI work ». Nuance du même billet : « other industry indices… may still rank JavaScript and Python higher ». Dire « n° 2 sur GitHub en nombre de contributeurs » |
| 17 | TIOBE, octobre 2026 : Python n° 1 avec 19,23 % (−5,23 points sur un an) | https://www.tiobe.com/tiobe-index/ (lecture par résumé de page, 23/10/2026) | ⚠️ une autre source donne 17,76 % pour septembre 2026 : relire la page TIOBE à la main avant de citer | ✅ page TIOBE relue le 23/10/2026 : octobre 2026, Python n° 1, 19,23 %, −5,23 points sur un an. Toujours dater (« en octobre 2026 ») |
| 18 | Stack Overflow Developer Survey 2025 : 57,9 % des répondants utilisent Python, +7 points en un an ; JavaScript 66 % | https://survey.stackoverflow.co/2025/technology | ✅ (le sondage 2026 n'était pas trouvable le 23/10/2026) | ✅ page relue : Python 57,9 %, JavaScript 66 %, « a 7 percentage point increase from 2024 to 2025 » |
| 19 | La PSF (Python Software Foundation) est une association à but non lucratif qui détient le copyright de Python depuis la 2.1 | https://docs.python.org/3/faq/general.html | ✅ | ✅ FAQ relue : « independent non-profit organization that holds the copyright on Python versions 2.1 and newer » |
| 20 | « Python est littéralement sur Mars » (phrase du documentaire CultRepo) | Transcription vidIQ de GfH4QL4VqJ0 (début) | ❓ citation du documentaire, aucune source technique lue : ne pas l'utiliser comme fait | ❓ confirmé : ne pas l'utiliser. (Piste non vérifiée ici : l'hélicoptère Ingenuity de la NASA ; il faudrait une source de la NASA) |
| 21 | Le documentaire *Python: The Documentary* (CultRepo, 28/08/2025) : 1,29 M vues, 84 min, parrainé par Anaconda, Dropbox, Meta | vidIQ, 23/10/2026 | ✅ | ✅ chiffres vidIQ du 23/10/2026 (non refaits, règle de la phase 2) ; ne citer que « plus d'un million de vues », daté |
| 22 | La vidéo française *Il s'ennuyait à Noël: Il a créé Python* existe (Codabee, 18/09/2026, 263 vues) | vidIQ, 23/10/2026 | ✅ | ✅ vidIQ du 23/10/2026 (non refait). La recherche web ne la trouve pas : la vidéo est confidentielle par sa taille, mais elle existe d'après vidIQ |
| 23 | (ajouté en 2e vérif) `strategie.md`, idée 13 : « l'entretien de Guido van Rossum sur la chaîne GitHub fait 253 K vues (×40) » | Brief de l'auteur ; vidIQ ne la trouve pas | — | ❓ URL introuvable : chiffre à ne pas citer dans la vidéo (il ne sert qu'à la stratégie) |
| 24 | (ajouté en 2e vérif) Fiche : « comment un passe-temps est devenu le langage de l'IA » | Fait 16 (« backbone of applied AI work ») ; fait 18 | — | ✅ formulation tenue par GitHub (« la colonne vertébrale de l'IA appliquée »), à condition de ne pas ajouter « le n° 1 » |
| 25 | (ajouté en 2e vérif) Fiche, titres 2 et 3 : « Il s'ennuyait (à Noël / pendant les fêtes), alors il a créé Python » | Fait 5 | — | ⚠️ Guido ne dit pas qu'il s'ennuyait (fait 5), et le titre 2 est presque celui de Codabee (fait 22). Voir les corrections de la fiche |
| 26 | (ajouté en 2e vérif) « En une semaine il a créé Python » (lecture possible du titre) | Faits 1, 9, 10 | — | ❌ il a *commencé* pendant la semaine de Noël ; une version marche début 1990, la première publique sort le 20/02/1991, quatorze mois plus tard. Dire « il a commencé à Noël » |
| 27 | La légende de l'ennui circule en anglais : « In 1989, during a week when his office was closed for Christmas and he found himself bored… » | https://interestingengineering.com/engineers-directory/guido-van-rossum (fiche biographique, sans date lue) | — | ✅ (ajouté au grill, vérifié le 23/10/2026) : la phrase est bien sur la page. Elle prouve que la légende existe, pas qu'elle est vraie (fait 5). Aucune source trouvée, en revanche, qui dise « créé en une semaine » : ne pas dire « on lit souvent » pour celle-là |
| 28 | Le mail du 12/07/2018 commence par : « Now that PEP 572 is done, I don't ever want to have to fight so hard for a PEP and find that so many people despise my decisions. » Plus loin : « I'll still be there for a while as an ordinary core dev » | https://mail.python.org/pipermail/python-committers/2018-July/005664.html | — | ✅ (ajouté au grill, vérifié le 23/10/2026). Traduction : « Maintenant que le PEP 572 est fait, je ne veux plus jamais avoir à me battre autant pour un PEP, et découvrir que tant de gens méprisent mes décisions. » |
| 29 | `:=` est « affectueusement surnommé l'opérateur morse », parce qu'il ressemble aux yeux et aux défenses d'un morse (« It is affectionately known as "the walrus operator" due to its resemblance to the eyes and tusks of a walrus ») | https://docs.python.org/3/whatsnew/3.8.html (What's New in Python 3.8) | — | ✅ (ajouté au grill, vérifié le 23/10/2026) |
| 30 | La réunion du 18/04/1995 où naît le titre de BDFL : « a group of folks interested in setting this up met », pour monter une organisation autour de Python ; huit présents : Guido, Ken Manheimer, Mike McLay, Barry Warsaw, Roger Masse, Ted Strollo, Jim Fulton, Paul Everitt | https://www.artima.com/weblogs/viewpost.jsp?thread=235725 ; G. van Rossum, « Origin of BDFL », 31/07/2008 | — | ✅ (ajouté au grill, vérifié le 23/10/2026). Dire « huit personnes se réunissent pour monter une organisation autour de Python » |
| 31 | Après le départ de Guido, les développeurs du cœur votent en décembre 2018 un nouveau modèle (PEP 8016) : un conseil de direction de cinq personnes (« The steering council is a 5-person committee »), réélu après chaque nouvelle version majeure (« A new council is elected after each feature release ») | https://peps.python.org/pep-0013/ (PEP 13, créé le 16/12/2018, statut Active) | — | ✅ (ajouté au grill, vérifié le 23/10/2026) |
| 32 | Le premier conseil, élu du 21/01 au 04/02/2019 : Barry Warsaw, Brett Cannon, Carol Willing, Guido van Rossum, Alyssa (Nick) Coghlan | https://peps.python.org/pep-8100/ (PEP 8100) | — | ✅ (ajouté au grill, vérifié le 23/10/2026). Barry Warsaw est aussi l'un des deux « suspects » du surnom BDFL (fait 14) |
| 33 | Le 29/10/2019, Dropbox annonce que Guido la quitte « and heading into retirement », après six ans et demi ; « He has already put into motion the conversion of the Dropbox server code from Python 2 to Python 3 » | https://blog.dropbox.com/topics/company/thank-you--guido (Dropbox, 29/10/2019) | — | ✅ (ajouté au grill, vérifié le 23/10/2026). Dire « il prend sa retraite en octobre 2019 » ; « chez Dropbox, c'est lui qui a lancé le passage du code serveur de Python 2 à Python 3 » |
| 34 | Le 12/11/2020, Guido tweete : « I decided that retirement was boring and have joined the Developer Division at Microsoft. » Microsoft confirme son arrivée | https://techcrunch.com/2020/11/12/python-creator-guido-van-rossum-joins-microsoft/ (TechCrunch, 12/11/2020) ; même citation chez InfoWorld (infoworld.com/article/3596436) | — | ✅ (ajouté au grill, vérifié le 23/10/2026) par deux médias qui citent le tweet, et Microsoft confirme. Le tweet lui-même (compte @gvanrossum) n'a pas pu être ouvert : fais une capture de l'original avant le montage. C'est la seule fois de l'histoire, dans nos sources, où Guido parle d'ennui |

## Matière pour le script
- **Phrase d'ouverture sourcée** : la citation du fait 1 (« la semaine autour de Noël ») avec la précision du fait 2 (bureau fermé, ordinateur à la maison).
- **Chiffres forts** : 1989 → 2026 ; Python 0.9.0 sur un forum Usenet le 20/02/1991 (fait 10) ; 1,29 M de vues pour le documentaire, 57,9 % des devs en 2025 (fait 18) ; Python 2→3 : onze ans entre 3.0 (2008) et la fin de Python 2 (2020), faits 11 et 13.
- **Anecdotes sourcées** : le nom tiré des scripts de Monty Python que Guido lisait (fait 6) ; le courriel de 2018 « vacances permanentes » (fait 15) ; ABC, qu'il juge un échec mais qui l'inspire (fait 8).
- **Contrepied d'aujourd'hui** : Python n'est plus n° 1 sur GitHub (fait 16), reste la colonne vertébrale de l'IA.
- **Démonstrations en motion design** : une ligne de temps 1989-2026 ; un calendrier de décembre 1989 avec la semaine de Noël ; le même programme en ABC et en Python (à écrire, hors recherche) ; la courbe Octoverse TypeScript/Python/JavaScript.
- **Questions du public** : pas de commentaires FR lus. Dans la transcription de CultRepo, la question centrale est « le langage a-t-il survécu sans Guido ? » (gouvernance après 2018).

## Points ouverts
- Titre : « Il s'ennuyait pendant les fêtes » est trop proche de Codabee (fait 22) ; garder le sujet, changer l'accroche (par exemple sur la citation exacte du fait 1).
- URL de l'entretien GitHub (253 K vues) à demander à l'auteur.
- Origine du mot BDFL (fait 14) et chiffre TIOBE (fait 17) à confirmer en phase 2.
- Brouillon de l'auteur : « se faisait chier » (fait 5) à garder comme ton, mais sans le mettre dans la bouche de Guido.

## Pour le script : ce qu'on peut dire, ce qu'on ne dit pas

### Formulations sûres
1. « Décembre 1989. Guido van Rossum cherche un projet “pour le loisir” qui l'occuperait pendant la semaine de Noël. » (fait 1)
2. « Son bureau, un labo de recherche public à Amsterdam, est fermé. Il a un ordinateur à la maison, et pas grand-chose d'autre sur les bras. » (fait 2)
3. « Il appelle ça Python, parce qu'il est fan des Monty Python. » (faits 4, 6)
4. « Le 20 février 1991, il publie la version 0.9.0 sur un forum Usenet, alt.sources. » (fait 10)
5. « On le surnomme “dictateur bienveillant à vie” dès 1995, et même lui ne sait plus qui a trouvé le nom. » (fait 14)
6. « Le 12 juillet 2018, il écrit : “je ne veux plus jamais avoir à me battre autant pour un PEP”, et se donne des “vacances permanentes”. » (fait 15)
7. « En 2025, 57,9 % des développeurs interrogés par Stack Overflow utilisent Python, sept points de plus qu'en 2024. » (fait 18)
8. « En août 2025, sur GitHub, TypeScript passe devant Python, de 42 000 contributeurs. Python reste “la colonne vertébrale” de l'IA. » (fait 16)
9. « Python 2 meurt le 1er janvier 2020, onze ans après Python 3. » (faits 11, 13)

### Interdit ou à dire autrement
- « Python est le langage n° 1 sur GitHub » (❌ depuis août 2025, fait 16). TIOBE le met n° 1 : préciser le classement et le mois (fait 17).
- « Il a créé Python en une semaine » (❌, fait 26) → « il a commencé pendant la semaine de Noël ».
- « Guido dit qu'il s'ennuyait » (fait 5).
- « Python est sur Mars » (fait 20, ❓).
- Les 253 K vues de l'entretien GitHub (fait 23, ❓).

### Les phrases de l'auteur à corriger (brouillon)
- « Il se faisait tellement chier qu'il a décidé de créer un langage de programmation » → garder le ton, corriger le fait : « Son bureau était fermé pour Noël, il n'avait pas grand-chose d'autre sur les bras… alors il s'est lancé dans un langage. Moi, j'appelle ça s'ennuyer. » La légende à l'écran peut afficher sa vraie phrase (fait 2).
- « À quel moment tu t'ennuies assez pour avoir envie de créer un langage ? » : question posée au spectateur, elle tient telle quelle (ce n'est pas une citation).
