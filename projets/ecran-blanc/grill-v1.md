# Grill du script Écran blanc v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Version finale : [`script.md`](script.md).
> Grille : `youtube-script-grill`, mode B (après l'écriture), **variante storytelling** (test des 30 secondes, axe 10 des liaisons, axes S1 à S6).
> Hypothèses : titre *Le génie caché du pixel : comment ton écran trompe tes yeux* (fiche, `strategie.md`, idée 10), miniature `noir-04` (une loupe sur un écran blanc, « il n'y a pas de blanc. »), public de 18-30 ans, surtout africain, curieux de tech, avec une part de devs, arrivé par l'accueil (« comment fonctionne un écran » est sous les 750 recherches par mois). Objectif : une vidéo « astuce cachée » du pilier « Le génie derrière l'app », sur un sujet que personne ne traite en français.
> Faits revérifiés à la source le 23/10 : voir « Vérification des faits » en bas, et les lignes 28 à 34 ajoutées à [`sources.md`](sources.md).

## Note globale : 7/10

8 🟢, 9 🟠, 0 🔴. C'est le meilleur hook de la série : la miniature tient en 5 secondes, la question tombe à 0:14, et la boucle « certains écrans cachent du blanc » tient jusqu'à 8:48. Mais cinq affirmations n'ont pas de source, quatre autres vont plus loin que la leur, la section 5 est un catalogue dans le désordre, et plusieurs plans au macro sont impossibles tels qu'ils sont écrits. Tout se corrige phrase par phrase, et c'est fait dans `script.md`.

## Verdict

Le fil est bon : une chasse au point blanc, annoncée dans le hook (« On va le trouver »), avec deux fausses pistes (le LCD qui cache son blanc derrière les filtres) et une vraie trouvaille (le sous-pixel blanc de LG). La V1 tient sa promesse honnêtement (« Sur certaines télés, elle tombe. Et je préférais te le dire. »), et elle a déjà les bons réflexes : 2,5 liaisons pour 100 mots, une devinette à 58 %, des sources dites à voix haute.

Le plus gros problème, ce sont les faits du milieu de vidéo. Le rédacteur l'a signalé lui-même : cinq points ne sont pas dans `sources.md`. En les vérifiant, j'en ai trouvé un qui retourne la section 5 : d'après DisplayMate, l'iPhone X n'a qu'un rouge et un bleu pour deux pixels. La V1 le présente pourtant avant le PenTile, comme si Samsung avait ensuite « poussé la triche encore plus loin ». Deuxième problème, le tournage : la vidéo repose sur des macros, et le hook demande un plan « sans coupe » du macro jusqu'au plan large, que la mise au point ne permet pas.

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** (titre + miniature) : ton écran te trompe, et à la loupe il n'a pas de blanc. Le macro arrive à 0:03, le dézoom à 0:10. Le spectateur veut savoir d'où vient le blanc qu'il voit. Le script répond (l'œil fait le mélange, section 1 ; trois cônes, section 2) et nuance honnêtement (LCD, LG). 🟢
- **Le problème de surface** : comment un écran fabrique du blanc avec trois couleurs.
- **Le problème profond** (le sous-texte de la fiche) : ce que tu vois n'est pas ce qui est là ; ton œil fait le mélange. Il est semé dans le hook (tu vois du blanc, il n'y en a pas) et dans la section 1 (« le blanc, c'est ton œil qui le fabrique »), puis il revient seulement à la fin, sous forme de morale (« Ce que tu vois n'est pas toujours ce qui est là »). Entre les deux, la section 5 l'oublie, alors que c'est elle qui le prouve le mieux : l'iPhone X retire la moitié de ses rouges et de ses bleus, et ton œil ne voit rien. `script.md` fait de ce passage le sommet du sous-texte (« repense à tes cônes ») et finit sur une image (« Le blanc, c'est toi qui le vois »). Ton enjeu à toi tient dans trois crochets (hexa, ClearType, « ce qui t'a surpris ») : c'est normal pour un sujet d'explication, mais deux phrases te prêtaient des opinions (voir n° 5).
- **La chaîne** (V1) : pas de point blanc, **et pourtant** du blanc partout, **donc** d'où vient-il ? → Microsoft le dit, **donc** trois cases, **et** FFFFFF, **et** le jaune et le cyan → **mais alors** pourquoi tu ne vois rien ? → l'œil mélange, **sauf que** pourquoi trois ? → trois cônes, **donc** trois couleurs suffisent → **du coup**, deux lumières différentes peuvent se confondre → **mais** il a fallu choisir laquelle → sRGB, **et** Maxwell → **sauf que** le LCD cache du blanc → les filtres en jettent les deux tiers, **donc** du blanc derrière → **mais** ton téléphone est peut-être OLED → iPhone X, **et** PenTile, **et** QD-OLED, **et puis** LG → **sauf qu'**il y a aussi un logiciel → ClearType.
  Très bonne jusqu'à 7:05. La section 5 retombe en « et ensuite » : « Et Samsung a poussé la triche encore plus loin », « Chez Samsung Display, il y a même… », « Et puis il y a LG ». `script.md` la refait sur un seul problème, la lumière : l'OLED fait sa propre lumière, **sauf que** le bleu éclaire mal, **donc** il est plus gros, et un rouge et un bleu pour deux pixels, **sauf que** ton œil a peu de capteurs du bleu, **donc** ça ne se voit pas ; **mais** LG repart d'une lumière blanche filtrée, **donc** un sous-pixel blanc.

## Le test des 15 premières secondes

Relues seules, à 145 mots/min (environ 36 mots) :

> « Zoome sur ton écran. Regarde bien cette page blanche : pas un seul point blanc. Du rouge, du vert, du bleu, et c'est tout. Et pourtant, recule d'un pas, et ton écran est blanc partout. »

🟢 **C'est le moment le plus fort de la vidéo, et il est là.** L'image de la miniature (la loupe, les sous-pixels) arrive à 0:03, sa preuve est filmée (le macro), et le contraste tombe à 0:10. Aucun contexte, aucune présentation. Les seuls concurrents pour cette place seraient « 4 à 10 % de la lumière ressort » ou le point blanc de LG, mais le premier demande trois phrases d'explication, et le second casse la promesse de la miniature. On garde l'ordre.

Deux réserves, qui touchent le tournage plus que le texte :
- **Le plan « sans coupe »** : « TU POSES L'OBJECTIF MACRO (OU UNE LOUPE) SUR TON ÉCRAN, EN UN SEUL PLAN, SANS COUPE », puis « dézoom rapide, le blanc revient d'un coup ». Au macro, la mise au point ne tient qu'à quelques centimètres : tu ne peux pas reculer jusqu'au plan large dans la même prise. **Correction** : deux plans (A : macro ; B : plan large, même cadrage) raccordés par un dézoom numérique au montage.
- **L'exposition** : un macro surexposé brûle les sous-pixels en blanc. Ça montrerait exactement le contraire de la phrase. Le plan A de `script.md` le dit en toutes lettres.

## Le test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Zoome sur ton écran. Regarde bien cette page blanche : pas un seul point blanc. » | 🟢 Le sujet, la tension, et l'image de la miniature, dans la même phrase. |
| 5-15 s | > « Du rouge, du vert, du bleu, et c'est tout. Et pourtant, recule d'un pas, et ton écran est blanc partout. » | 🟢 Le contraste, avec sa preuve à l'image (macro, puis dézoom). |
| 15-30 s | > « Donc ce blanc que tu regardes toute la journée, il sort d'où ? Comment ton écran te fait voir une couleur qu'on ne trouve nulle part à la loupe ? » | 🟠 La question centrale arrive au 47e mot (0:14), très bien. Mais elle est posée deux fois de suite : la deuxième phrase dit la même chose en plus long. |
| Pont | > « Pour répondre, il faut ouvrir deux machines : ton écran et ton œil. Sauf que certains écrans cachent bien du blanc quelque part. On va le trouver. » | 🟢 Le « sauf que » ouvre une deuxième question (où est ce blanc ?), fermée à 6:30 et à 8:48. « Il faut ouvrir deux machines » sonne un peu comme un plan de cours. |

**Budget :** 88 mots ≈ 36 s à 145 mots/min, 29 s à 180. 🟠 (`script.md` : 75 mots, 31 s à 145, 25 s à 180 ; question au 47e mot.)
**À couper :** « Comment ton écran te fait voir une couleur qu'on ne trouve nulle part à la loupe ? » (la question en double).
**Réécriture des 30 s** (dans `script.md`) :

> Zoome sur ton écran. Regarde bien cette page blanche : pas un seul point blanc.
> Du rouge, du vert, du bleu, et c'est tout. Et pourtant, recule d'un pas, et ton écran est blanc partout.
> Donc ce blanc que tu regardes toute la journée, il sort d'où ?
> La réponse est à moitié dans ton écran, à moitié dans ton œil. Sauf que certains écrans cachent bien du blanc quelque part. Et celui-là, on va le trouver.
> [compteur de quête : « Trouver un point blanc : 0/1 »]

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | La loupe à 0:03, le blanc qui revient à 0:10, et la nuance (LCD, LG) dite plus loin : la miniature est tenue honnêtement. |
| 2. Alignement | 🟢 | Rien à vendre ; l'abonnement parle du pilier (« j'ouvre le capot ») et tient en une phrase. |
| 3. Problème profond | 🟠 | Le sous-texte est semé (hook, section 1), absent de la section 5 qui le prouve le mieux, puis asséné en morale à la fin. |
| 4. Public & complexité | 🟢 | Les nanomètres, D65 et le métamérisme arrivent après leur image (la manette, la recette, le cosplay de soleil). |
| 5. Valeur & originalité | 🟢 | Rien en français sur les sous-pixels (`sources.md`) ; le bleu « perso faible » de l'iPhone X et les 4 à 10 % de lumière qui ressortent d'un LCD valent le clic. |
| 6. Structure & transformation | 🟠 | Départ et arrivée nets (je vois du blanc → je sais d'où il vient) ; mais la section 5 met l'iPhone X avant le PenTile, et la fin résume section par section. |
| 7. Histoire (enquête) | 🟠 | La chasse au point blanc est une vraie enquête, mais elle disparaît entre 0:36 et 5:45, et personne n'y veut rien en dehors du narrateur. |
| 8. Mais / donc | 🟠 | Excellent jusqu'à 7:05 ; la section 5 enchaîne « Et Samsung… », « Chez Samsung Display, il y a même… », « Et puis il y a LG ». |
| 9. Engagement actif | 🟢 | « À ton avis, lequel est le plus gros ? » avec deux secondes de silence, « Tu vois le problème ? », « Tu te rappelles le début ? ». |
| 10. Rythme, oralité & liaisons | 🟢 | 2,5 liaisons pour 100 mots ; trois rafales de faits et un « Effectivement » qui ne confirme rien (détail au n° 6). |
| 11. Tics d'IA | 🟠 | Aucune fausse opposition, mais des annonces (« il y a un secret », « la triche change complètement de forme »), une rafale de trois et une morale finale. |
| S1. Les 30 premières secondes | 🟠 | Tout passe, sauf la question posée deux fois et 88 mots (36 s à ton débit de prise). |
| S2. Le pont | 🟢 | « Sauf que certains écrans cachent bien du blanc quelque part » ouvre la deuxième boucle. |
| S3. Les retournements | 🟢 | 24 relances en 12 min, aucun trou de plus de 45 s. |
| S4. Planté / récolté et motif | 🟠 | Trois bonnes récoltes (« Tu te rappelles la phrase de Microsoft ? », « Tu te rappelles les filtres ? », « ma phrase du début ») ; mais le FFFFFF et les cônes ne reviennent pas, et la chasse au blanc n'a pas de motif qui revient. |
| S5. Personnages et enjeu | 🟠 | Surtout des entités (Microsoft, Apple, HP, Samsung, LG) et des noms sans envie (Young, Maxwell) ; le seul « personnage » est le bleu, et il marche très bien. |
| S6. La fin | 🟠 | Elle résume (« Bref, on récapitule »), assène une morale, puis rattrape bien avec « Un pixel, deux histoires ». |

## Le grill

### 1. Cinq affirmations sans source, et quatre qui vont plus loin que la leur

Le rédacteur en a listé cinq. Voici ce que chacune devient, après vérification à la source primaire (lignes 28 à 33 de `sources.md`) :

> « F F F F F F. Rouge à fond, vert à fond, bleu à fond. »

✅ La norme CSS du W3C le dit mot pour mot : la première paire de chiffres est le rouge, la deuxième le vert, la dernière le bleu, et « ff » est le maximum (fait 28). Gardé, et la norme est citée dans la voix off : pour ton public de devs, c'est une petite récompense.

> « C'est le genre de patch note que personne n'a lu, et qui tourne sur presque tous tes écrans. »

❓ Aucune source ne dit quelle part des écrans est réglée en sRGB, et beaucoup de téléphones récents affichent plus large. Retiré. En cherchant, j'ai trouvé mieux : la même norme CSS range les couleurs en hexa dans le sRGB (fait 29). D'où une récolte du FFFFFF de la section 1 : « ton F F F F F F de tout à l'heure, la norme du web le range toujours dans le sRGB ». Le gag du patch note reste.

> « Sur un écran OLED, chaque sous-pixel produit sa propre lumière. »

✅ Samsung l'écrit pour les pixels : « OLED displays use self-lit pixels that create their own light » (fait 30). Dit « d'après Samsung, chaque point de l'écran fait sa propre lumière ».

> « Le PenTile joue sur le même mélange. »

C'était une interprétation, et elle était trop vague pour expliquer quoi que ce soit. La vraie raison est écrite dans un brevet de Clairvoyante, déposé en 2000, dont l'inventrice est **Candice Brown Elliott** (fait 32) : l'œil a « very few blue receptors compared to red or green », et sa résolution en luminosité est « several times higher » qu'en couleur. C'est une récolte toute trouvée de la section 2 (« repense à tes cônes »). Et ça règle ta question 4 : son nom peut se dire, comme inventrice de ce brevet. « Elle a inventé le PenTile » reste Wikipédia seul, donc on ne le dit pas.

> « Et pourtant, regarde le bord des lettres au macro : des franges rouges et bleues. À l'œil nu, tu ne les as jamais vues. »

⚠️ La voix off affirme ce que le plan n'a pas encore montré. L'article de Microsoft Research sur ClearType (Platt et al., 2000) dit que son filtre est conçu pour atténuer les franges colorées (fait 33) : les franges existent, mais rien ne dit qu'elles se voient au macro, ni qu'elles sont « rouges et bleues ». **Correction** : « des franges de couleur », dites seulement si le plan F les montre ; puis l'article de 2000, qui explique pourquoi tu ne les remarques pas. Sinon, les deux phrases sautent.

Et quatre phrases sourcées en apparence qui vont plus loin que leur source :

> « Elle fixe les trois couleurs de base de ton écran »

Le sRGB fixe trois primaires ; « de ton écran » suppose que ton écran est réglé en sRGB. Devient « trois couleurs de base ».

> « Donc ma phrase du début, pas un seul point blanc, elle tient pour ton téléphone, LCD comme OLED. »

Trop général : en 2012, le Sony Xperia P avait un LCD « WhiteMagic » avec un sous-pixel blanc, d'après la presse de son lancement (fait 34, ⚠️). Personne ne peut garantir « ton téléphone ». **Correction** : « elle tient pour les écrans que j'ai filmés : [ton téléphone et ton écran de PC] ». C'est vérifiable, puisque tu les montres.

> « Imagine deux recettes qui n'ont aucun ingrédient en commun, et qui ont exactement le même goût. »

L'image est fausse : la lumière du jour contient aussi les longueurs d'onde des trois pics de l'écran. Les deux « recettes » ont des ingrédients en commun. **Correction** : « Imagine un plat avec cent ingrédients, et un autre avec trois seulement. Et ton palais ne fait pas la différence. »

> « Microsoft écrit qu'en théorie, la résolution horizontale augmente de trois cents pour cent. »

C'est la citation exacte (« increases 300 percent »), mais à l'oreille, « augmente de 300 % » veut dire ×4. Microsoft veut dire ×3, comme le fait 18. **Correction** : « en théorie, la résolution sur la largeur devient trois fois plus fine ».

Et une dernière, dans l'écran de fin :

> « Un point blanc sur un écran noir, et tu sais maintenant de quoi il est fait, qui finit avec trois virgule six milliards de joueurs. »

Le point blanc de la vidéo du 14 déc. est celui de *Tennis for Two* et de Pong. Le prototype de Pong tournait sur « a cheap 12" black-and-white TV set » (blog du Computer History Museum, « 50 Years of Fun With Pong », https://computerhistory.org/blog/50-years-of-fun-with-pong/), et rien dans nos sources ne dit que ce point était fait de rouge, de vert et de bleu. « Tu sais maintenant de quoi il est fait » est donc probablement faux, et la phrase est bancale (le « qui » se rattache mal). Le chiffre, lui, n'est pas tranché (3,6 ou 3,7 milliards, voir `projets/pixel/script.md`). **Correction** : « celle d'un point blanc sur un écran noir qui finit avec des milliards de joueurs ».

### 2. La section 5 est un catalogue, et dans le désordre

> « Et Samsung a poussé la triche encore plus loin. En deux mille huit, Samsung rachète une grille qui s'appelle le PenTile. L'idée : au lieu de trois sous-pixels par pixel, un pixel sur deux a un rouge et un vert, et l'autre un bleu et un vert. »

> « Chez Samsung Display, il y a même des écrans qui partent d'une seule couleur. » … « Et puis il y a LG, qui fait presque l'inverse. »

Deux soucis.
- **L'ordre est faux.** DisplayMate a compté les sous-pixels de l'iPhone X : environ 2,7 millions de pixels, 2,7 millions de verts, mais 1,4 million de rouges et 1,4 million de bleus (fait 31). L'iPhone X fait donc déjà ce que la V1 présente comme l'étape suivante, et son écran est fabriqué par Samsung Display (même page). « Samsung a poussé la triche encore plus loin » met à la suite deux choses qui se recouvrent.
- **C'est un « et ensuite ».** Quatre écrans, quatre paragraphes reliés par « Et », « Chez… il y a même », « Et puis il y a ». C'est à 65-72 % de la vidéo, juste après la relance forte : c'est là qu'une liste fait partir les gens.

**Correction** (dans `script.md`) : un seul fil, la lumière, avec deux récoltes.
> Sur un écran OLED, il n'y a plus de lampe au fond : d'après Samsung, chaque point de l'écran fait sa propre lumière. Sauf que les trois couleurs ne sont pas à égalité. […] le bleu, c'est le perso le plus faible de l'équipe, et on lui a filé la plus grosse armure.
> Et DisplayMate a aussi fait les comptes. […] Donc en gros, un vert par pixel, mais un rouge et un bleu pour deux pixels.
> Normalement, il en manque, et ça devrait se voir. Sauf que repense à tes cônes. […] l'inventrice, Candice Brown Elliott, explique pourquoi ça passe : ton œil a très peu de capteurs pour le bleu, comparé au rouge et au vert.
> […] Et sur les télés, LG prend un autre chemin : ses OLED partent d'une lumière blanche, avec des filtres par-dessus. Et tu te rappelles ce que jettent les filtres ? Au moins les deux tiers. Donc pour gagner en luminosité […] un sous-pixel blanc.

Le QD-OLED (fait 17) n'entre pas dans ce fil : il passe en réserve, en bas de `script.md`, pour 10 secondes si la prise est courte.

### 3. Les macros : des plans impossibles ou flous

La vidéo repose sur tes plans au macro ; la fiche compte 30 h de production pour eux. Plusieurs crochets ne sont pas faisables tels quels :

> « [DÉMO : TU POSES L'OBJECTIF MACRO (OU UNE LOUPE) SUR TON ÉCRAN, EN UN SEUL PLAN, SANS COUPE.] » puis « [VISUEL : dézoom rapide, le blanc revient d'un coup.] »

Impossible en une prise (voir le test des 15 s). Deux plans, raccord au montage.

> « [VISUEL : le macro révèle les bandes rouges, vertes et bleues.] » puis « Microsoft l'écrit noir sur blanc… des bandes rouges, vertes et bleues. »

Des **bandes**, c'est un LCD. Si tu filmes un téléphone OLED, le macro montre des points en losange, et la citation de Microsoft ne colle plus à l'image. Il faut savoir quels écrans tu as (question 1) : `script.md` prévoit un plan C, le macro d'un écran LCD, pour la citation.

> « [VISUEL : la grille en losange de l'iPhone X, en macro.] »

Sauf si tu as un iPhone X, ce plan n'existe pas, et les photos de DisplayMate ne sont pas à toi. **Correction** : motion design d'après la description de DisplayMate, ou ton propre téléphone s'il est OLED, avec un bandeau qui dit que ce n'est pas un iPhone X.

> « [DÉMO : FILME AU MACRO UN TEXTE NOIR SUR BLANC SOUS WINDOWS, CLEARTYPE ACTIVÉ. SI LES FRANGES COLORÉES NE SE VOIENT PAS, GARDE SEULEMENT L'ANIMATION.] »

Bonne prudence, mais la voix off juste en dessous affirme les franges sans condition. `script.md` met la condition sur la voix off, et ajoute deux pièges : toutes les applis de Windows ne lissent pas le texte de la même façon, et un écran OLED de PC n'a pas de bandes.

**Ce qui manquait** : un ordre de tournage. Deux phrases de la voix off dépendent de ce que montrent les plans (les franges, « les écrans que j'ai filmés »). `script.md` ajoute un « Plan de tournage » (plans A à G) : à tourner **avant** la voix.

### 4. La chasse au point blanc disparaît pendant cinq minutes

> « Sauf que certains écrans cachent bien du blanc quelque part. On va le trouver. » (0:30) … « Sauf que derrière la loupe, il y a un secret. » (5:40)

C'est la meilleure boucle de la vidéo, et entre 0:36 et 5:45 personne ne la cherche. Le spectateur peut l'oublier avant qu'elle serve. Il manque un motif qui revient.

**Correction** (proposition, question 4) : un compteur de quête de jeu vidéo, « Trouver un point blanc : 0/1 ». Il s'affiche dans le hook, clignote à la fin de la section 3, affiche « trouvé… derrière l'écran. Ne compte pas. » après le LCD, passe à 1/1 avec le sous-pixel de LG, et finit en « Quête terminée ». Ça colle à ton humour gamer, ça ne coûte aucun mot de voix off (sauf « Quête terminée »), et ça donne trois petits gags. Sans lui, le fil tient quand même.

### 5. Deux opinions qu'on te prête

> « Et ça, c'est la partie qui me parle en tant que dev. »
> « Voilà pourquoi je trouve ça génial. »

Même cas que le « c'est la partie que je préfère » du grill d'Uber : tu ne l'as dit nulle part. C'est peut-être vrai, mais c'est à toi de le dire, avec ta raison. **Correction** : un crochet en tête de section 6 (« [TA PHRASE DE DEV, SI ELLE EST VRAIE : POURQUOI CETTE PARTIE TE PARLE. SINON, RIEN.] »), et la fin de section devient « Voilà comment des devs ont écrit du code qui se sert de la triche de l'écran, pour que ton texte soit plus net. »

### 6. Les liaisons (axe 10)

Compte du contrôle sur la V1 : **44 liaisons pour 1 761 mots, soit 2,5 pour 100** (cible : 1,5). Par section : hook 3,4 ; 1 : 3,7 ; **2 : 1,9 ; 3 : 1,7** ; 4 : 3,1 ; 5 : 2,5 ; 6 : 3,0 ; **7 : 1,5**. Le chiffre est bon. Ce qui coince, c'est un contresens et trois rafales.

**Un « effectivement » qui ne confirme rien :**
> « Si ton téléphone ou ton PC a un écran LCD, la lumière part blanche. Effectivement : tout au fond, il y a un rétroéclairage. »

« Effectivement » confirme ce que le spectateur soupçonnait. Là, il ne soupçonnait rien : c'est la révélation. Le contrôle le compte quand même. Retiré ; ton « en effet » passe en section 5, où il confirme vraiment ce que le spectateur vient de se demander (« Normalement, il en manque, et ça devrait se voir. […] Et en effet, DisplayMate le confirme »).

**Les rafales :**
> « En mille neuf cent quatre-vingt-seize, Hewlett-Packard et Microsoft proposent une norme : le sRGB. Elle fixe les trois couleurs de base de ton écran, et un blanc de référence : une lumière du jour normée, qui s'appelle D65. Trois ans plus tard, elle devient une norme internationale. »

> « Et figure-toi que ça, quelqu'un l'a deviné il y a plus de deux siècles : Thomas Young, dès mille huit cent deux. Helmholtz reprend l'idée une cinquantaine d'années plus tard. Et les pics que je viens de te donner, eux, ont été mesurés sur une vraie rétine humaine, en mille neuf cent quatre-vingt. »

> « Chez Samsung Display, il y a même des écrans qui partent d'une seule couleur. Le QD-OLED part d'une lumière bleue, et des boîtes quantiques la transforment en rouge et en vert. Tout un écran construit à partir du bleu. »

**Corrections** (dans `script.md`) :
- sRGB : « Et ça prend, parce que trois ans plus tard, c'est une norme internationale. »
- Young : trois dates deviennent un « mais » : « Mais pour mesurer ces trois pics sur une vraie rétine humaine, il faut attendre mille neuf cent quatre-vingt. »
- QD-OLED : en réserve.

`script.md` : **56 liaisons pour 1 877 mots, 3,0 pour 100** ; plus aucune section sous 1,5 (la plus basse : la fin, à 1,6). Pas deux fois la même liaison de suite ; « donc » revient 11 fois sur 13 minutes, à surveiller dans ta prise.

### 7. Les tics d'IA

Aucune fausse opposition (« ce n'est pas A, c'est B ») : c'est rare et ça mérite d'être dit. Le reste :

| Passage de la V1 | Tic | Dans `script.md` |
|---|---|---|
| « Sauf que derrière la loupe, il y a un secret. » | Faux suspens : annonce un secret au lieu de le dire | « Sauf que sur certains écrans, le blanc est là depuis le début, juste derrière ce que tu as filmé. » |
| « Et là, la triche change complètement de forme. » | Annonce | « Sauf que ce gaspillage, il y a des écrans qui s'en passent. » |
| « Et Samsung a poussé la triche encore plus loin. » | Annonce, et faux dans l'ordre (n° 2) | Retiré |
| « Mais alors, pourquoi tu ne vois jamais ces bandes ? Parce qu'elles sont minuscules. » | Question suivie d'une réponse en trois mots | La question reste ; la réponse passe directement au chiffre d'Apple |
| « Ton blanc, c'est un mélange, et on peut le démonter. » | Petite morale de fin de paragraphe | Retiré : la capture du jaune et du cyan le montre |
| « L'écran triche, ton œil se fait avoir, et des devs ont écrit du code… » | Rafale de trois | « Voilà comment des devs ont écrit du code qui se sert de la triche de l'écran… » |
| « Ce que ça change pour toi ? La prochaine fois… » | Faux suspens | « Donc la prochaine fois que tu regardes une page blanche, souviens-toi de la loupe. » |
| « Ce que tu vois n'est pas toujours ce qui est là. » | Morale assénée | « Ton écran t'envoie du rouge, du vert et du bleu. Le blanc, c'est toi qui le vois. » |
| « Bref, on récapitule. » + quatre phrases de résumé | Fin qui résume | La fin répond à la question du hook avec les récoltes (n° 8) |

### 8. La fin résume au lieu de retourner

> « Bref, on récapitule. À la loupe, ton écran n'a que du rouge, du vert et du bleu. Ton œil n'a que trois sortes de cônes, donc trois couleurs suffisent à le tromper. Le blanc qu'il voit est un réglage de mille neuf cent quatre-vingt-seize. Et chaque écran triche à sa façon… »

Quatre phrases qui redisent les sections dans l'ordre, puis la morale. Le spectateur a déjà tout compris : la fin doit lui rendre quelque chose. **Correction** : on revient à la question du hook, et la réponse se fait avec les récoltes de la vidéo (« Le reste, c'est toi : quatre virgule six millions de capteurs, trois modèles, et un cosplay de soleil qui passe à chaque fois »), puis « Quête terminée », puis la dernière image. Le sous-texte de la fiche est gardé, sous forme d'image.

## La rétention

- **Hook** : V1 88 mots (36 s à 145 mots/min), question au 47e mot ; `script.md` 75 mots (31 s), question au même endroit, 0:14. 🟢
- **Appel à l'abonnement** : V1 à 3:31 (29 %, et pas 25 % comme annoncé dans la V1) ; `script.md` à **3:29 (27 %)**, juste après la manette et Thomas Young, avant le métamérisme. Il coupe une explication, mais à sa jointure : « Du coup » relance juste après.
- **Relance forte** : V1 à 7:07 (58 %) ; `script.md` à **7:26 (57 %)** : musique qui repart, devinette, deux secondes de silence, gag de l'armure dans les 45 s.
- **Relances** : V1 24 en 12 min ; `script.md` 38 en 12 min 56, une toutes les 20 s ; plus long trou : 36 s (la rétine, 2:18 → 2:54).
- **Ponts** : chaque section finit sur ce qui rend la suivante nécessaire (« Pourquoi trois couleurs ? », « il a bien fallu que quelqu'un décide », « le blanc est là depuis le début », « des écrans qui s'en passent », « un logiciel qui connaît ce secret »). 🟢
- **Durée** : V1 1 761 mots ; `script.md` 1 877 mots (12:56 à 145 mots/min, 11:23 à 165, environ 10:30 à 180). Les comptes de DisplayMate et le brevet ajoutent 40 s à la section 5, en partie repris par la réserve du QD-OLED et les coupes ailleurs.

## Ce que le rédacteur a signalé

| Question de la V1 | Décision |
|---|---|
| 1. Le macro : as-tu le matériel ? La goutte d'eau ? | Toujours ouverte (question 1 de `script.md`), avec un plan de tournage A à G. La goutte d'eau est notée comme outil possible, hors voix off. |
| 2. Ton vécu de dev (hexa) | Crochet gardé (« une phrase, ou rien »). |
| 3. Cinq points à sourcer | Quatre sourcés et reformulés, un retiré (« presque tous tes écrans »), voir n° 1. |
| 4. Candice Brown Elliott | Sourcée par un brevet de Clairvoyante (2000) où elle est l'inventrice ; dite comme telle (fait 32). |
| 5. LG, fait 16 à reconfirmer | Inchangé : à reconfirmer avant le 19 avril 2027. La phrase « sur les modèles testés ces dernières années » tient dans tous les cas. |
| 6. Les gags | Gardés, plus le compteur de quête ; à valider par toi (question 4). |

## Vérification des faits du script

Chaque phrase de la V1 qui affirme quelque chose, contre `sources.md` (colonne « 2e vérif ») ou, à défaut, la source primaire relue aujourd'hui.

| Phrase de la V1 | Fait | Verdict | Dans `script.md` |
|---|---|---|---|
| « pas un seul point blanc » (à la loupe) | 19, 22 | ✅ la formulation juste | gardé |
| « Du rouge, du vert, du bleu, et c'est tout » | 1, 13 | ✅ à la loupe d'un téléphone ou d'un PC courant | gardé |
| « quand tu vois du blanc sur un écran LCD, tu regardes en réalité des bandes rouges, vertes et bleues » | 1 | ✅ Microsoft | gardé ; plan C pour que l'image montre bien des bandes |
| « un pixel, c'est trois petites cases collées » | 1, 31 | ⚠️ vrai pour un LCD ; faux pour l'iPhone X (deux sous-pixels par pixel en moyenne) | « un pixel d'écran LCD » |
| « F F F F F F. Rouge à fond, vert à fond, bleu à fond » | 28 (ajouté) | ✅ CSS Color 4, § 5.2 | gardé, la norme citée |
| « Coupe le bleu, et ton blanc vire au jaune. Coupe le rouge, il passe au cyan » | 25 | ⚠️ à montrer | gardé sur la capture (plan D) |
| « En deux mille dix, pour l'iPhone 4, Apple annonce trois cent vingt-six pixels par pouce… l'œil humain n'arrive plus à distinguer les pixels » | 20 | ✅ « d'après Apple » | gardé |
| « Microsoft dit pareil pour les sous-pixels » | 26 | ✅ | gardé |
| « Ta rétine est tapissée de capteurs de lumière, et il y en a deux sortes » | 6 | ⚠️ bâtonnets et cônes, oui ; « deux sortes » tout court est un raccourci | « deux grandes sortes » |
| « environ quatre-vingt-douze millions » ; « quatre virgule six millions… sur huit rétines » ; 1990 | 6 | ✅ Curcio 1990 | gardé |
| 420, 530, 560 nm | 5 | ✅ Bowmaker et Dartnall | gardé |
| « Thomas Young, dès mille huit cent deux. Helmholtz… une cinquantaine d'années plus tard » | 9 | ⚠️ formulation de la 2e vérif | gardé |
| « mesurés sur une vraie rétine humaine, en mille neuf cent quatre-vingt » | 5 | ✅ « a human retina » | gardé, en « mais » |
| « Deux lumières complètement différentes peuvent donner exactement les trois mêmes réponses… le métamérisme » | 7 | ✅ CIE | gardé |
| « deux recettes qui n'ont aucun ingrédient en commun » | 7 | ❌ image fausse : la lumière du jour contient les couleurs des trois pics | plat à cent ingrédients contre plat à trois |
| « réglé sur une lumière du jour normée, et trois pics suffisent à l'imiter » | 3, 7 | ✅ formulation de la 2e vérif | gardé |
| « En mille neuf cent quatre-vingt-seize, Hewlett-Packard et Microsoft proposent une norme : le sRGB » | 4 | ✅ | gardé |
| « Elle fixe les trois couleurs de base de ton écran » | 3 | ⚠️ « de ton écran » suppose un écran réglé en sRGB | « trois couleurs de base » |
| « Trois ans plus tard, elle devient une norme internationale » | 3 | ✅ IEC 61966-2-1, 1999 | gardé |
| « le blanc de ton écran, c'est un réglage, fixé par une norme de mille neuf cent quatre-vingt-seize » | 27 | ✅ formulation de la 2e vérif | gardé |
| « qui tourne sur presque tous tes écrans » | — | ❓ rien ne le prouve | retiré ; remplacé par le fait 29 (« la norme du web le range toujours dans le sRGB ») |
| « En mille huit cent soixante et un, Maxwell montre une photo en couleurs faite avec trois filtres » ; « Trois photos, une par filtre, projetées l'une sur l'autre » | 8 | ⚠️ formulation juste (pas « la première ») ; V&A | gardé |
| « la lumière part blanche… d'après des brevets de Philips, c'est une diode bleue recouverte d'un luminophore, et ensemble, elles donnent de la lumière blanche » | 2 | ✅ ; mais les brevets décrivent une conception, pas tous les LCD, et « elles » ne s'accorde avec rien | « des brevets de Philips décrivent comment on le fabrique » ; « Le bleu de la diode et la lueur du luminophore, ensemble, ça donne de la lumière blanche » |
| « un filtre rouge ne garde que le rouge » | — | ✅ c'est ce que fait un filtre | gardé |
| « les filtres jettent au moins les deux tiers » ; « environ quatre à dix pour cent » | 2 | ✅ « d'après ces brevets » | gardé |
| « une lampe qui jette plus de neuf rayons sur dix » | 2 | ✅ à 4-10 % de sortie, 90 à 96 % se perdent | gardé |
| « Sur un écran OLED, chaque sous-pixel produit sa propre lumière » | 30 (ajouté) | ✅ Samsung, pour les pixels | « d'après Samsung, chaque point de l'écran fait sa propre lumière » |
| « sur l'iPhone X, les sous-pixels n'ont même pas la même taille… le bleu… le vert… le plus efficace » | 13 | ✅ DisplayMate | gardé |
| « il lui faut plus de surface pour suivre les autres » | 13 | ⚠️ déduction directe de « lowest light emission efficiency » | gardé |
| « Samsung a poussé la triche encore plus loin. En deux mille huit, Samsung rachète une grille qui s'appelle le PenTile » | 11, 31 | ⚠️ la date tient (presse) ; « encore plus loin » non : l'iPhone X fait déjà moins de trois sous-pixels par pixel | réordonné (n° 2) |
| « un pixel sur deux a un rouge et un vert, et l'autre un bleu et un vert… un tiers de sous-pixels en moins » | 10, 31 | ⚠️ PenTile par Wikipédia ; les comptes de DisplayMate pour l'iPhone X sont primaires et disent la même chose | « un vert par pixel, mais un rouge et un bleu pour deux pixels » (fait 31) |
| « Le PenTile joue sur le même mélange » | 32 (ajouté), 31 | ✅ reformulé avec la raison du brevet de 2000 et « generally not visible » de DisplayMate | « ton œil a très peu de capteurs pour le bleu… bien plus finement en luminosité qu'en couleur » |
| Candice Brown Elliott (non dite dans la V1) | 32 (ajouté) | ✅ inventrice du brevet US 7 274 383 (Clairvoyante, 2000) | dite comme inventrice de ce brevet |
| « Le QD-OLED part d'une lumière bleue… boîtes quantiques » | 17 | ✅ Samsung Display | en réserve |
| « Les télés OLED de LG partent d'une lumière blanche » | 16 | ⚠️ formulation de la 2e vérif | gardé |
| « d'après les tests spécialisés, les dalles WRGB de LG ajoutent un quatrième sous-pixel, sans filtre, pour gagner en luminosité » | 15 | ⚠️ tests concordants, pas de page de LG Display | gardé, « d'après les tests » |
| « elle tient pour ton téléphone, LCD comme OLED » | 19, 22, 34 (ajouté) | ⚠️ trop général : le Sony Xperia P (2012) avait un sous-pixel blanc, d'après la presse | « elle tient pour les écrans que j'ai filmés » |
| « il pilote séparément le rouge, le vert et le bleu de chaque pixel » | 18 | ✅ | gardé |
| « en théorie, la résolution horizontale augmente de trois cents pour cent » | 18 | ⚠️ à l'oreille, ×4 ; Microsoft veut dire ×3 | « trois fois plus fine sur la largeur » |
| « des franges rouges et bleues. À l'œil nu, tu ne les as jamais vues » | 33 (ajouté) | ⚠️ ClearType est conçu pour atténuer ces franges (Platt, 2000) ; leur visibilité au macro et leurs couleurs, à filmer | « des franges de couleur », seulement si le plan F les montre, puis l'article de 2000 |
| « des devs ont écrit du code qui exploite la triche pour que ton texte soit plus net » | 18 | ✅ (« sharp », « readability ») | gardé |
| « l'iPhone X gonfle ses bleus, et les dalles de LG ajoutent un point blanc » | 13, 15 | ✅ | gardé, plus « fait l'impasse sur la moitié de ses rouges » (fait 31) |
| « Un point blanc sur un écran noir, et tu sais maintenant de quoi il est fait » | — | ❌ le point de Pong passait sur une télé noir et blanc : rien ne dit qu'il était fait de RVB | retiré |
| « trois virgule six milliards de joueurs » | pixel | ⚠️ le titre du 14 déc. n'est pas tranché (3,6 ou 3,7) | « des milliards de joueurs » ; le titre en crochet sur l'écran de fin |

**Ce que j'ai corrigé, en bref** : 1 affirmation retirée (« presque tous tes écrans »), 2 phrases fausses retirées ou réécrites (la recette, le point de Pong), 6 reformulées (« de ton écran », « ton téléphone, LCD comme OLED », « 300 % », les franges, « chaque sous-pixel » de l'OLED, « un pixel, c'est trois cases »), 1 accord corrigé (« ensemble, elles »), 4 faits ajoutés au script (28, 29, 31, 32), 1 en appui de condition (33), 1 en réserve (34, non dit).

## Ce qu'il faut garder

- **Le hook** : « Zoome sur ton écran. Regarde bien cette page blanche : pas un seul point blanc. » Le meilleur premier plan de la série : l'image de la miniature, filmée, à 0:03.
- **« Microsoft l'écrit noir sur blanc »** : le jeu de mots fait sourire et la citation sert de preuve.
- **« Ton code te le disait depuis le début, en fait. »** Une phrase pour tes devs, sans exclure les autres.
- **« Ton œil, c'est une manette à trois boutons. »** L'image qui rend les cônes simples ; `script.md` la fait revenir deux fois (le bouton bleu tout petit, la fin).
- **« Ouais, ton écran fait du cosplay de soleil. Et ça passe. »** Ton humour, et la meilleure façon de faire passer le métamérisme.
- **« C'est le genre de patch note que personne n'a lu »** : gardé, avec la récolte du FFFFFF.
- **« Imagine une lampe qui jette plus de neuf rayons sur dix, juste pour faire des couleurs. Le gaspillage, quoi. »** Le chiffre traduit pour le spectateur, exactement ce que demande l'axe 10.
- **« le bleu, c'est le perso le plus faible de l'équipe, et on lui a filé la plus grosse armure »** : le seul personnage de la vidéo, et il marche.
- **« Sur certaines télés, elle tombe. Et je préférais te le dire. »** L'honnêteté qui bat l'attente, et qui protège la miniature.
- **« Un pixel, deux histoires. »** La bonne chute vers la vidéo du 14 déc.

## Plan d'action (appliqué dans `script.md`)

1. **Les faits** : sourcer ou retirer les cinq points du rédacteur, corriger les quatre phrases qui vont trop loin, retirer la recette et le point de Pong (n° 1).
2. **La section 5** : un seul fil (la lumière), les comptes de DisplayMate, le brevet de 2000 en récolte des cônes, puis LG ; le QD-OLED en réserve (n° 2).
3. **Le tournage** : deux plans pour le hook, un plan de tournage A à G, l'exposition baissée, la voix off des franges conditionnée au plan (n° 3).
4. **Le motif** : le compteur de quête, à valider (n° 4).
5. **La voix** : les deux opinions prêtées passent en crochet ; tics, rafales et fin réécrits (n° 5 à 8).

## Les questions pour toi

Reprises dans `script.md`, section « Questions pour l'auteur » :
1. Ton téléphone et ton écran de PC : LCD ou OLED ? Et avec quoi tu filmes au macro ?
2. Une phrase vraie sur ta première couleur en hexa, ou rien.
3. ClearType : une raison à toi pour laquelle cette partie te parle, ou rien.
4. Les gags (manette, cosplay de soleil, armure) et le nouveau compteur de quête : ça te ressemble ?
5. Candice Brown Elliott, dite comme inventrice d'un brevet de Clairvoyante : ça te va ?
6. LG (fait 16) : à reconfirmer avant le 19 avril 2027.
7. Le titre de la vidéo du 14 déc. (3,6 ou 3,7 milliards) pour l'écran de fin.
