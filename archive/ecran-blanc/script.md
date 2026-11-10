# Écran blanc : script final (v2)

**Titre** : *Le génie caché du pixel : comment ton écran trompe tes yeux*

**Durée** : 1 877 mots de voix off (sortie de `controle.py`), 3,0 liaisons pour 100 mots, 0 « vous », question centrale au 47e mot. À ton débit mesuré sur ArtCraft (145 mots/min, pauses comprises) : environ 13 min ; à 165 mots/min : 11 min 23 ; à 180 (coupes serrées, comme Uber) : 10 min 30, plus une trentaine de secondes de pauses au montage. Tes crochets ajoutent un peu. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Texte et sous-texte** (repris de la [fiche](fiche.md)) :
- **Texte** : à la loupe, ton écran n'a pas un seul point blanc : seulement du rouge, du vert et du bleu, collés si près que ton œil les mélange.
- **Sous-texte** : ce que tu vois n'est pas ce qui est là ; ton œil fait le mélange. Il arrive à la fin comme une image (« Le blanc, c'est toi qui le vois »), plus comme une morale.

**Fil rouge** : une chasse au point blanc. Le hook dit qu'il n'y en a pas, puis annonce que certains écrans en cachent un. On remonte la chaîne : l'écran (trois sous-pixels), l'œil (trois sortes de cônes), la norme qui choisit le blanc, puis la lumière que chaque écran gaspille ou économise, jusqu'au sous-pixel blanc des télés LG. À l'image, un compteur de quête de jeu vidéo (« Trouver un point blanc : 0/1 ») revient à chaque fausse piste (proposition, question 4).

**Changements depuis la V1** (le détail est dans [`grill-v1.md`](grill-v1.md)) :
- **Hook** : une seule question (« il sort d'où ? ») au lieu de deux à la suite ; « il faut ouvrir deux machines » devient « la réponse est à moitié dans ton écran, à moitié dans ton œil ». 75 mots au lieu de 88. Le plan « en un seul plan, sans coupe » devient deux plans raccordés au montage : la mise au point d'un macro ne tient pas quand on recule.
- **Section 5 reconstruite en « mais / donc »** : la V1 enchaînait l'iPhone X, puis « Samsung a poussé la triche encore plus loin » avec le PenTile, puis le QD-OLED, puis « Et puis il y a LG ». Or l'iPhone X a lui-même moins de sous-pixels que de pixels (DisplayMate les a comptés) et son écran vient de Samsung Display. La section suit maintenant un seul problème, la lumière : l'OLED fait sa propre lumière, **mais** le bleu éclaire mal, **donc** il est plus gros, et le rouge et le bleu sont un pour deux pixels ; ça passe **parce que** ton œil a peu de capteurs du bleu (récolte de la section 2) ; **mais** sur les télés, LG repart d'une lumière blanche filtrée, **donc** un sous-pixel blanc.
- **Faits sourcés au grill** (lignes 28 à 34 de [`sources.md`](sources.md)) :
  - « F F F F F F = rouge, vert et bleu à fond » : la norme CSS du W3C le dit (fait 28) ;
  - « le sRGB tourne sur presque tous tes écrans » : non prouvé, retiré. À la place, une récolte sourcée : la norme du web range encore les couleurs en hexa dans le sRGB (fait 29) ;
  - « sur un OLED, chaque sous-pixel produit sa propre lumière » : Samsung l'écrit pour les pixels (fait 30) ; on dit « chaque point de l'écran » ;
  - « le PenTile joue sur le même mélange » : remplacé par la raison donnée dans un brevet de Clairvoyante (2000), dont l'inventrice est **Candice Brown Elliott** : ton œil a très peu de capteurs du bleu, et il voit les détails bien plus finement en luminosité qu'en couleur (fait 32). Son nom se dit, comme inventrice de ce brevet, pas comme « conceptrice du PenTile » (Wikipédia seul) ;
  - les comptes de DisplayMate pour l'iPhone X : 2,7 millions de pixels, autant de verts, 1,4 million de rouges et autant de bleus (fait 31) ;
  - les franges de ClearType : un article de Microsoft Research (2000) dit que le filtre de ClearType est fait pour atténuer les franges colorées (fait 33). Leur présence au macro reste à filmer : la phrase ne se dit que si le plan les montre.
- **Faits reformulés** :
  - « Elle fixe les trois couleurs de base **de ton écran** » devient « trois couleurs de base » (beaucoup de téléphones affichent plus large que le sRGB ; rien dans les sources ne dit lesquels) ;
  - « elle tient pour ton téléphone, LCD comme OLED » devient « elle tient pour les écrans que j'ai filmés » : en 2012, le Sony Xperia P avait un LCD avec un sous-pixel blanc, d'après la presse (fait 34) ;
  - « deux recettes qui n'ont aucun ingrédient en commun » : faux, la lumière du jour contient aussi les trois couleurs de l'écran. Devient un plat à cent ingrédients contre un plat à trois ;
  - « la résolution horizontale augmente de trois cents pour cent » (à l'oreille, ça fait ×4) devient « trois fois plus fine sur la largeur », la formulation du fait 18 ;
  - « Un point blanc sur un écran noir, et tu sais maintenant de quoi il est fait » (vers la vidéo Pong) : retiré. Pong passait sur une télé noir et blanc, où rien ne dit que le point était fait de rouge, de vert et de bleu ;
  - « Ensemble, elles donnent de la lumière blanche » (une diode et un luminophore) : accord corrigé, sur la phrase du brevet.
- **Opinions qu'on te prêtait** : « c'est la partie qui me parle en tant que dev » et « Voilà pourquoi je trouve ça génial » deviennent un crochet pour ta phrase à toi.
- **Tics retirés** : « derrière la loupe, il y a un secret », « la triche change complètement de forme », « Samsung a poussé la triche encore plus loin », « Ce que ça change pour toi ? », la rafale « L'écran triche, ton œil se fait avoir, et des devs… », le « Effectivement » qui ne confirmait rien, et la morale finale.
- **Fin** : elle répond à la question du hook avec les récoltes de la vidéo (les 4,6 millions de cônes, le cosplay de soleil, la quête) au lieu de résumer section par section.
- **QD-OLED** (fait 17) : coupé, pour tenir la durée et garder la section 5 sur un seul fil ; il est en réserve en bas du fichier.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à filmer ou à remplir par toi (les `[DÉMO : …]` sont les plans à tourner toi-même, détaillés dans « Plan de tournage »). Nombres en lettres pour la lecture.

---

## 0. Hook (0:00 – 0:31) · objectif : 75 % à 0:15

[VISUEL : plein écran blanc, une page de notes vide. Pas de titre, pas de logo.]
[DÉMO : PLAN 1, LE MACRO DE LA PAGE BLANCHE (VOIR « PLAN DE TOURNAGE », PLAN A). L'EXPOSITION BAISSÉE JUSQU'À CE QUE LES COULEURS APPARAISSENT.]

Zoome sur ton écran. Regarde bien cette page blanche : pas un seul point blanc.

[VISUEL : le macro révèle les sous-pixels rouges, verts et bleus. Coupe sèche.]
[SON : clic d'objectif, puis une seconde de silence.]

Du rouge, du vert, du bleu, et c'est tout. Et pourtant, recule d'un pas, et ton écran est blanc partout.

[DÉMO : PLAN 2, LE MÊME ÉCRAN EN PLAN LARGE (PLAN B). AU MONTAGE, UN DÉZOOM NUMÉRIQUE RACCORDE LE MACRO AU PLAN LARGE : LE BLANC REVIENT D'UN COUP.]

Donc ce blanc que tu regardes toute la journée, il sort d'où ?

La réponse est à moitié dans ton écran, à moitié dans ton œil. Sauf que certains écrans cachent bien du blanc quelque part. Et celui-là, on va le trouver.

[VISUEL : un compteur de quête de jeu vidéo s'affiche en haut à droite : « Trouver un point blanc : 0/1 ».]
[SON : petit son de quête acceptée, style RPG.]

---

## 1. La loupe (0:31 – 2:18)

[VISUEL : le macro, lent, qui glisse sur les sous-pixels. Si le macro du hook vient d'un téléphone OLED (des points, pas des bandes), ce plan-ci est le macro de ton écran LCD (plan C).]

En fait, ce que tu viens de voir, Microsoft l'écrit noir sur blanc. Sur la page de sa techno ClearType, il y a cette phrase : quand tu vois du blanc sur un écran LCD, tu regardes en réalité des bandes rouges, vertes et bleues.

[VISUEL : la citation en anglais, puis sa traduction : « when we see white on an LCD screen, we are really looking at red, green and blue stripes ». 3 secondes, puis retour au macro.]

Donc un pixel d'écran LCD, c'est trois petites cases collées : un sous-pixel rouge, un vert, un bleu. Et quand les trois sont allumés à fond, le pixel donne du blanc.

[VISUEL : un pixel géant, trois barres qui montent ensemble jusqu'en haut ; le pixel devient blanc.]

Si tu as déjà codé une appli, tu connais ce blanc par cœur : F F F F F F. Et la norme du web le dit en toutes lettres : la première paire, c'est le rouge, la deuxième le vert, la dernière le bleu. Et F F, c'est le maximum. Rouge à fond, vert à fond, bleu à fond. Ton code te le disait depuis le début, en fait.

[VISUEL : un éditeur de code, la ligne « #FFFFFF » ; les trois paires « FF » se colorent en rouge, vert et bleu. Source en bas : W3C, CSS Color 4.]
[TON VÉCU, SI TU EN AS UN : LA PREMIÈRE FOIS QUE TU AS ÉCRIT UNE COULEUR EN HEXA, EN FLUTTER OU EN KOTLIN. UNE PHRASE, OU RIEN.]

Et regarde quand on coupe une couleur.

[DÉMO : PLAN D. EN PLEIN ÉCRAN, « #FFFF00 » (JAUNE) PUIS « #00FFFF » (CYAN), FILMÉS AU MACRO. LE CODE S'AFFICHE EN SURIMPRESSION.]
[VISUEL : capture macro réelle. Le bleu s'éteint, le blanc vire au jaune ; le bleu revient, le rouge s'éteint, il passe au cyan.]

Coupe le bleu, et ton blanc vire au jaune. Coupe le rouge, il passe au cyan.

Mais alors, pourquoi tu ne vois jamais ces bandes ? En deux mille dix, pour l'iPhone 4, Apple donne un chiffre : trois cent vingt-six pixels par pouce. Et d'après Apple, à cette densité, l'œil humain n'arrive plus à distinguer les pixels.

[VISUEL : la phrase du communiqué d'Apple du 7 juin 2010, datée (ou 2 à 3 s d'archive de la keynote).]

Microsoft dit pareil pour les sous-pixels : à cette échelle, ton œil ne fait plus la différence entre les couleurs. Du coup, il les mélange.

Bref, le blanc, c'est ton œil qui le fabrique, avec ce que l'écran lui envoie. Sauf que ça pose une question bizarre. Pourquoi trois couleurs ? Pourquoi pas quatre, ou douze ?

---

## 2. Ton œil n'a que trois capteurs (2:18 – 4:36)

[VISUEL : coupe d'un œil en motion design, zoom jusqu'au fond, sur la rétine.]
[SON : whoosh sur le zoom.]

La réponse est au fond de ton œil. Ta rétine a deux grandes sortes de capteurs de lumière. D'un côté, les bâtonnets : environ quatre-vingt-douze millions. De l'autre, les cônes. Et ceux-là, une équipe les a comptés en mille neuf cent quatre-vingt-dix, sur huit rétines : quatre virgule six millions en moyenne.

[VISUEL : deux compteurs qui défilent : « 92 000 000 bâtonnets », « 4 600 000 cônes ». Source en bas : Curcio et al., 1990.]

Pour les couleurs, ce sont les cônes qui bossent. Et des cônes, il n'y en a que trois sortes. Un modèle réglé vers quatre cent vingt nanomètres, un vers cinq cent trente, un vers cinq cent soixante.

[VISUEL : trois courbes de sensibilité en cloche (S, M, L), avec leurs pics à 420, 530 et 560 nm. Source : Bowmaker et Dartnall, 1980.]

Quatre virgule six millions de capteurs, et trois modèles en tout. Ton œil, c'est une manette à trois boutons. Et voilà pourquoi trois couleurs suffisent : ton écran appuie sur les trois boutons, dans le bon dosage.

[VISUEL : une manette avec trois boutons S, M, L ; un pixel RVB appuie dessus.]

Et figure-toi que ça, quelqu'un l'a deviné il y a plus de deux siècles : Thomas Young, dès mille huit cent deux. Helmholtz reprend l'idée une cinquantaine d'années plus tard. Mais pour mesurer ces trois pics sur une vraie rétine humaine, il faut attendre mille neuf cent quatre-vingt.

**Abonnement (≈ 3:29, environ 27 % de la vidéo, juste après la manette et Thomas Young)**

Si tu aimes voir ce qui se cache derrière les trucs que tu utilises tous les jours, abonne-toi : sur Technovore, j'ouvre le capot, un truc à la fois.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; les trois courbes restent à l'écran.]

Du coup, pour ton œil, une couleur, ça se résume à trois réponses : une par sorte de cône. Tu vois le problème ? Deux lumières complètement différentes peuvent donner exactement les trois mêmes réponses. Et donc la même couleur. Ça a un nom : le métamérisme.

[VISUEL : à gauche, le spectre continu de la lumière du jour, une bande arc-en-ciel ; à droite, trois pics fins de l'écran. Sous chacun, les trois mêmes jauges de cônes, au même niveau.]

Imagine un plat avec cent ingrédients, et un autre avec trois seulement. Et ton palais ne fait pas la différence. La lumière du jour, c'est le plat à cent ingrédients : toutes les couleurs de l'arc-en-ciel. Ton écran, c'est le plat à trois. En fait, son blanc est réglé sur une lumière du jour normée, et trois pics suffisent à l'imiter pour ton œil.

Ouais, ton écran fait du cosplay de soleil. Et ça passe.

[VISUEL : un soleil et un écran côte à côte, l'écran enfile une perruque de soleil.]
[SON : petit jingle de victoire de jeu rétro.]

Mais imiter la lumière du jour, d'accord. Sauf qu'il a bien fallu que quelqu'un décide laquelle.

---

## 3. Le blanc a une date de naissance (4:36 – 6:02)

[VISUEL : une fausse fiche d'identité qui se remplit : « Nom : blanc. Né en : 1996. Parents : ? ».]

Et ce quelqu'un, c'est deux boîtes que tu connais. En mille neuf cent quatre-vingt-seize, Hewlett-Packard et Microsoft proposent une norme : le sRGB. Elle fixe trois couleurs de base, et un blanc de référence : une lumière du jour normée, qui s'appelle D65. Et ça prend, parce que trois ans plus tard, c'est une norme internationale.

[VISUEL : la fiche se complète : « Parents : HP et Microsoft. Référence : D65 ». La page du W3C de 1996 en capture.]

Donc le blanc de ton écran, c'est un réglage, fixé par une norme de mille neuf cent quatre-vingt-seize. Il a une date de naissance et deux parents. Et c'est le genre de patch note que personne n'a lu, mais qui tourne encore : ton F F F F F F de tout à l'heure, la norme du web le range toujours dans le sRGB.

[VISUEL : le « #FFFFFF » de la section 1 revient ; une étiquette « sRGB » se colle dessus. Source : W3C, CSS Color 4.]

Et l'idée des trois couleurs est encore plus vieille que ça. En mille huit cent soixante et un, Maxwell montre une photo en couleurs faite avec trois filtres : rouge, vert et bleu. En gros, trois photos, une par filtre, projetées l'une sur l'autre. Ton écran fait la même chose à l'envers.

[VISUEL : trois projecteurs, trois images teintées qui se superposent ; puis la même scène en marche arrière, qui se sépare en trois sous-pixels.]

Bon. Jusque-là, j'ai été gentil avec ton écran. Tu te rappelles le début ? Pas un seul point blanc. À la loupe, c'est vrai. Sauf que sur certains écrans, le blanc est là depuis le début, juste derrière ce que tu as filmé.

[VISUEL : le compteur de quête clignote : « Trouver un point blanc : 0/1 ».]

---

## 4. Ton LCD cache du blanc (6:02 – 7:26)

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : vue éclatée d'un écran LCD, couche par couche, de l'arrière vers l'avant.]

Si ton téléphone ou ton PC a un écran LCD, la lumière part blanche. Tout au fond, il y a un rétroéclairage. Et des brevets de Philips décrivent comment on le fabrique : une diode bleue, recouverte d'un luminophore. Le bleu de la diode et la lueur du luminophore, ensemble, ça donne de la lumière blanche.

[VISUEL : une LED bleue, une couche par-dessus, et la lumière qui sort blanche.]

Ensuite, cette lumière traverse des filtres colorés : rouges, verts, bleus. Et forcément, un filtre rouge ne garde que le rouge. Du coup, d'après ces mêmes brevets, les filtres jettent au moins les deux tiers de la lumière qui leur arrive.

[VISUEL : un faisceau blanc entre dans le filtre ; un tiers seulement ressort, coloré.]

Et au bout de toute la chaîne, d'après un de ces brevets, il ne ressort de l'écran qu'environ quatre à dix pour cent de la lumière de départ.

[VISUEL : « ≈ 4-10 % » plein écran ; mention « d'après un brevet de Philips ».]

Imagine une lampe qui jette plus de neuf rayons sur dix, juste pour faire des couleurs. Le gaspillage, quoi.

Donc oui, dans un LCD, il y a du blanc. Il est derrière, avant d'être découpé. Et quand il arrive jusqu'à toi, il est déjà en morceaux rouges, verts et bleus. Voilà pourquoi ta loupe ne le croise jamais.

[VISUEL : le compteur de quête : « 0/1 · trouvé… derrière l'écran. Ne compte pas. »]

Sauf que ce gaspillage, il y a des écrans qui s'en passent. Et l'écran de ton téléphone en fait peut-être partie.

---

## 5. Les écrans qui trichent autrement (7:26 – 10:37) · relance forte à 57 %

[SON : la musique repart, plus rythmée.]
[VISUEL : la grille en losange de l'iPhone X, en motion design (d'après la description de DisplayMate), ou le macro de ton téléphone s'il est OLED (plan E).]

Sur un écran OLED, il n'y a plus de lampe au fond : d'après Samsung, chaque point de l'écran fait sa propre lumière. Sauf que les trois couleurs ne sont pas à égalité. Sur l'iPhone X, les sous-pixels n'ont même pas la même taille. Avant que je te le dise : à ton avis, lequel est le plus gros ?

[VISUEL : trois sous-pixels cachés sous des points d'interrogation, deux secondes de silence.]

C'est le bleu, et de loin. En fait, c'est celui qui émet le moins bien la lumière, donc il lui faut plus de surface pour suivre les autres. Le vert, lui, est de loin le plus petit, parce que c'est le plus efficace. C'est l'analyse de DisplayMate, un labo qui teste les écrans.

[VISUEL : les points d'interrogation tombent ; le bleu gonfle, le vert rétrécit.]

En gros, sur ton écran, le bleu, c'est le perso le plus faible de l'équipe, et on lui a filé la plus grosse armure.

Et DisplayMate a aussi fait les comptes. L'iPhone X a environ deux virgule sept millions de pixels, et autant de sous-pixels verts. Mais des rouges, il n'y en a qu'un virgule quatre million. Et des bleus, pareil. Donc en gros, un vert par pixel, mais un rouge et un bleu pour deux pixels.

[VISUEL : une grille de pixels ; chaque case a son point vert ; les points rouges et bleus n'apparaissent qu'une case sur deux, en alternance. Compteurs : « 2,7 M pixels · 2,7 M verts · 1,4 M rouges · 1,4 M bleus ». Source : DisplayMate, 2017.]

Normalement, il en manque, et ça devrait se voir. Sauf que repense à tes cônes. Mettre moins de trois sous-pixels par pixel, c'est une idée qui a un nom : le PenTile. Elle vient d'une boîte qui s'appelle Clairvoyante. Et dans un de ses brevets, déposé en deux mille, l'inventrice, Candice Brown Elliott, explique pourquoi ça passe : ton œil a très peu de capteurs pour le bleu, comparé au rouge et au vert. Et il voit les détails bien plus finement en luminosité qu'en couleur.

[VISUEL : la page de garde du brevet US 7 274 383 (Clairvoyante, 2000), le nom de l'inventrice surligné ; puis la manette à trois boutons de la section 2, avec un bouton bleu tout petit.]

Et en effet, DisplayMate le confirme : sur l'iPhone X, avec le bon logiciel, les rouges et les bleus qui manquent ne se voient généralement pas. Et en deux mille huit, c'est Samsung qui rachète le PenTile. L'écran de l'iPhone X, d'ailleurs, c'est Samsung Display qui le fabrique.

[VISUEL : logo Samsung Display sur la grille ; bandeau « écran de l'iPhone X : Samsung Display (DisplayMate) ».]

Et sur les télés, LG prend un autre chemin : ses OLED partent d'une lumière blanche, avec des filtres par-dessus. Et tu te rappelles ce que jettent les filtres ? Au moins les deux tiers. Donc pour gagner en luminosité, d'après les tests spécialisés, les dalles WRGB de LG ajoutent un quatrième sous-pixel, sans filtre. Un sous-pixel blanc.

[VISUEL : le pixel WRGB, quatre cases ; la case sans filtre s'allume en blanc pur.]
[VISUEL : le compteur de quête passe à « 1/1 ».]
[SON : petit « ding » de trouvaille, style coffre ouvert.]

Et là, à la loupe, tu tomberais enfin sur un point blanc. Enfin, sur les modèles testés ces dernières années : LG fait évoluer ses dalles, donc pour un modèle précis, regarde son test.

[VISUEL : bandeau « Tests RTINGS, TechHive, TFTCentral, jusqu'en 2025 ». À reconfirmer avant la sortie (fait 16).]

Donc ma phrase du début, pas un seul point blanc, elle tient pour les écrans que j'ai filmés : [TON TÉLÉPHONE ET TON ÉCRAN DE PC, AVEC LEUR TYPE : LCD OU OLED]. Sur certaines télés, elle tombe. Et je préférais te le dire.

Bon. Jusqu'ici, ce sont des ingénieurs du matériel qui trichent. Sauf qu'il y a aussi un logiciel qui connaît ce secret, et qui s'en sert.

---

## 6. Le code qui se sert des sous-pixels (10:37 – 11:38)

[VISUEL : un mot noir sur fond blanc, dans un éditeur de texte sous Windows.]

Ce logiciel, c'est ClearType, chez Microsoft. [TA PHRASE DE DEV, SI ELLE EST VRAIE : POURQUOI CETTE PARTIE TE PARLE. SINON, RIEN.] Quand Windows dessine du texte avec ClearType, il pilote séparément le rouge, le vert et le bleu de chaque pixel.

Du coup, sur la largeur, il a trois petites cases par pixel pour placer le bord de chaque lettre. Microsoft écrit qu'en théorie, la résolution sur la largeur devient trois fois plus fine.

[VISUEL : une lettre « A » en gros pixels ; le contour s'affine quand on passe des pixels aux sous-pixels.]
[DÉMO : PLAN F. LES DEUX PHRASES SUIVANTES NE SE DISENT QUE SI TON MACRO MONTRE DES BORDS COLORÉS. SINON, SAUTE-LES ET GARDE L'ANIMATION.]

Normalement, une lettre noire sur fond blanc, c'est du noir et du blanc. Et pourtant, regarde le bord des lettres au macro : des franges de couleur.

Et ces franges, les ingénieurs de Microsoft les connaissent bien. Dans leur article de deux mille sur ClearType, ils expliquent que leur filtre est fait pour les atténuer. C'est pour ça qu'à l'œil nu, tu ne les remarques pas.

[VISUEL : le titre de l'article « Displaced Filtering for Patterned Displays » (Platt et al., 2000), une ligne.]

Voilà comment des devs ont écrit du code qui se sert de la triche de l'écran, pour que ton texte soit plus net.

---

## 7. Fin (11:38 – 12:56)

[VISUEL : le dézoom de la vidéo à l'envers : le blanc, la loupe, les sous-pixels, l'œil, les trois courbes.]

Bref, on revient à la page blanche du début. Ce blanc que tu regardes toute la journée, il sort d'où ? De trois couleurs collées si près que ton œil les mélange, et d'une norme de mille neuf cent quatre-vingt-seize qui a choisi ce blanc-là. Le reste, c'est toi : quatre virgule six millions de capteurs, trois modèles, et un cosplay de soleil qui passe à chaque fois.

[VISUEL : la manette à trois boutons, puis le soleil à perruque, une seconde chacun.]

Et en fait, chaque écran triche à sa façon. Le LCD cache son blanc derrière les filtres. L'iPhone X gonfle ses bleus et fait l'impasse sur la moitié de ses rouges. Et les télés de LG, elles, ont fini par ajouter un vrai point blanc. Quête terminée.

[VISUEL : le compteur de quête : « Quête terminée ». SON : fanfare courte de fin de quête.]

Donc la prochaine fois que tu regardes une page blanche, souviens-toi de la loupe. Ton écran t'envoie du rouge, du vert et du bleu. Le blanc, c'est toi qui le vois.

[OPTIONNEL : CE QUI T'A LE PLUS SURPRIS EN PRÉPARANT LA VIDÉO, ET POURQUOI. UNE OU DEUX PHRASES.]

Quel écran ou quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et si tu veux l'autre histoire du pixel, celle d'un point blanc sur un écran noir qui finit avec des milliards de joueurs, elle est juste là. Un pixel, deux histoires.

[VISUEL : écran de fin, 20 s : la vidéo du 14 déc., « D'un pixel à 3,7 milliards de joueurs », à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:03 | Révélation | Le macro : pas un seul point blanc |
| 0:10 | Contraste | Dézoom, le blanc revient partout |
| 0:14 | Question centrale | « il sort d'où ? » |
| 0:24 | Boucle ouverte | « certains écrans cachent bien du blanc » ; le compteur de quête s'affiche (refermée à 10:01) |
| 0:31 | Citation | Microsoft confirme ce qu'on vient de voir |
| 1:02 | Code | « F F F F F F », les trois paires colorées, et la norme du web |
| 1:30 | Démo | On coupe une couleur : jaune, cyan |
| 1:39 | Chiffre | 326 pixels par pouce, d'après Apple |
| 2:06 | Question | « Pourquoi trois couleurs ? Pourquoi pas douze ? » |
| 2:25 | Chiffres | 92 millions de bâtonnets, 4,6 millions de cônes |
| 2:54 | Humour | La manette à trois boutons |
| 3:09 | Histoire | Thomas Young, 1802 ; « il faut attendre 1980 » |
| 3:29 | Appel à l'action | Abonnement (27 %) |
| 3:40 | Question | « Tu vois le problème ? » : le métamérisme |
| 3:58 | Image | Le plat à cent ingrédients contre le plat à trois |
| 4:24 | Humour | Le cosplay de soleil, jingle rétro |
| 4:36 | Visuel | La fiche d'identité du blanc (1996, HP et Microsoft) |
| 5:09 | Récolte | Le « F F F F F F » de la section 1 rangé dans le sRGB |
| 5:27 | Histoire | Maxwell, 1861, trois filtres |
| 5:45 | Retournement | « le blanc est là depuis le début, juste derrière » ; le compteur clignote |
| 6:02 | Coupure musique | Vue éclatée du LCD |
| 6:42 | Chiffre | 4 à 10 % de la lumière ressort |
| 7:01 | Gag | Le compteur « trouvé… derrière l'écran. Ne compte pas. » |
| 7:17 | Pont | « il y a des écrans qui s'en passent » |
| 7:26 | Devinette (relance forte, 57 %) | Musique qui repart ; « lequel est le plus gros ? » |
| 8:11 | Humour | Le bleu, perso faible à la plus grosse armure |
| 8:21 | Chiffres | Les comptes de DisplayMate : un rouge et un bleu pour deux pixels |
| 8:43 | Récolte | « repense à tes cônes » : le brevet de 2000 |
| 9:29 | Retournement | Samsung rachète le PenTile ; Samsung Display fabrique l'écran de l'iPhone X |
| 9:38 | Récolte | « tu te rappelles ce que jettent les filtres ? » |
| 10:01 | Boucle fermée | Le sous-pixel blanc de LG ; quête 1/1 |
| 10:14 | Honnêteté | « Sur certaines télés, elle tombe » |
| 10:37 | Pont | Un logiciel connaît le secret : ClearType |
| 11:01 | Démo | Les franges au macro (si le plan les montre) |
| 11:12 | Chiffre | L'article de Microsoft de 2000 |
| 11:38 | Réponse | Retour à la question du hook, avec les récoltes |
| 12:05 | Gag | « Quête terminée » |
| 12:44 | Écran de fin | Un pixel, deux histoires |

**Total** : 38 relances en 12 min 56 (à 145 mots/min), une toutes les 20 s ; plus long trou : 36 s (2:18 → 2:54, la rétine).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:31, sortie du hook | Moyen | La citation de Microsoft peut sonner « cours » juste après le macro | Elle confirme ce que le spectateur vient de voir ; 3 s à l'image, puis retour au macro |
| Section 2, les cônes | Élevé | Le bloc le plus scolaire (nanomètres, rétine) | Deux chiffres, la manette à trois boutons, Young, puis l'abonnement ; les courbes restent simples |
| Métamérisme | Moyen | Le mot fait peur | Le plat à trois ingrédients, puis le cosplay de soleil ; le mot n'arrive qu'après l'idée |
| Relance (~57 %) | Élevé | Chute classique, juste après la section technique du LCD | Musique qui repart, devinette avec deux secondes de silence, puis le gag de l'armure dans les 30 s |
| PenTile et comptes de DisplayMate | Moyen | Quatre chiffres d'affilée, une grille qui peut perdre les non-geeks | Une seule animation (chaque case a son vert, le rouge et le bleu une case sur deux) ; la récolte des cônes juste après donne la raison |
| ClearType | Moyen | Paraît hors sujet pour les non-devs | Court (1 min) ; la démo des franges est visuelle ; ta phrase de dev en crochet |

## Notes de montage

- **Composants à construire une fois** : le pixel géant à trois barres (sections 1, 4, 5 et 7), les trois courbes des cônes, la manette à trois boutons (sections 2, 5 et 7), la vue éclatée du LCD, les grilles RVB / losange / WRGB, le compteur de quête (hook, sections 3, 4, 5 et 7).
- **Le compteur de quête** est une proposition (question 4) : il donne un motif qui revient et fait de chaque fausse piste un petit gag. Sans lui, le fil tient quand même.
- **Sources à l'écran** : une ligne discrète à chaque chiffre (Microsoft, W3C, Apple 2010, Curcio 1990, Bowmaker et Dartnall 1980, W3C 1996, brevets Philips, Samsung, DisplayMate, brevet Clairvoyante 2000, tests LG, Platt 2000). La vidéo dit « d'après » ; l'image le montre.
- **Pas d'image de DisplayMate** ni de photo de presse en gros plan : la grille de l'iPhone X se refait en motion design d'après la description.
- **Pas d'extrait de keynote long** : 2 à 3 s maximum pour Apple, sinon la phrase du communiqué.
- **Énergie** : calme et curieuse ; montées sur le macro du hook, la manette, la coupure de musique de la section 4, la devinette et le point blanc de LG.
- **Miniature** : `noir-04` (loupe sur un écran blanc, « il n'y a pas de blanc. ») tient si le macro arrive dans les 5 premières secondes, comme ici, et si la nuance de LG reste dans la vidéo (fait 24).

## Plan de tournage (les macros)

Toute la vidéo repose sur ces plans. Tourne-les **avant** d'enregistrer la voix : deux phrases dépendent de ce qu'ils montrent (les franges de ClearType, et « les écrans que j'ai filmés »).

| Plan | Où | Quoi | Pièges |
|---|---|---|---|
| A | Hook | Macro d'une page blanche, sur ton téléphone ou ton écran de PC | **Baisse l'exposition** jusqu'à voir les couleurs : un macro surexposé rend les sous-pixels blancs et contredit la phrase du hook. Mets la luminosité de l'écran à mi-course. Trépied ou téléphone posé |
| B | Hook | Le même écran en plan large, même cadrage | Le raccord avec A se fait au montage (dézoom numérique), pas en un seul plan : au macro, la mise au point ne tient qu'à quelques centimètres |
| C | Section 1 | Macro d'un écran **LCD** (bandes) | Si ton téléphone est OLED, le plan A montre des points en losange, pas des bandes : la citation de Microsoft parle du LCD, donc ce plan vient de ton écran de PC (s'il est LCD) |
| D | Section 1 | Aplats « #FFFF00 » puis « #00FFFF » en plein écran, au macro | Même réglage d'exposition que A, pour comparer |
| E | Section 5 | Macro de ton téléphone, s'il est OLED | Les tailles et les comptes de la voix off concernent l'iPhone X : si tu filmes un autre modèle, le bandeau le dit (« mon téléphone, pas un iPhone X ») |
| F | Section 6 | Texte noir sur blanc sous Windows, ClearType activé (Paramètres → « Ajuster le texte ClearType »), au macro | Teste plusieurs applis : toutes ne lissent pas le texte de la même façon. Sur un écran OLED de PC, la grille n'est pas en bandes et le résultat change. Pas de franges visibles : saute les deux phrases |
| G (bonus) | Section 5 | Macro d'une télé OLED de LG (chez un ami, en magasin) | La meilleure preuve du point blanc. Sinon, l'animation suffit |

Outils possibles : le mode macro de ton téléphone, un objectif macro à clipser, ou une goutte d'eau posée sur l'écran (elle fait loupe ; à tester chez toi, rien dans les sources). Aucun écran de marque en gros plan sans besoin.

## Faits utilisés

| N° (`sources.md`) | 2e vérif | Phrase du script |
|---|---|---|
| 1 | ✅ | « quand tu vois du blanc sur un écran LCD, tu regardes en réalité des bandes rouges, vertes et bleues » ; « un pixel d'écran LCD, c'est trois petites cases… allumés à fond, le pixel donne du blanc » |
| 2 | ✅ | « des brevets de Philips décrivent… une diode bleue, recouverte d'un luminophore » ; « les filtres jettent au moins les deux tiers » ; « environ quatre à dix pour cent de la lumière de départ » |
| 3 | ✅ | « Elle fixe trois couleurs de base, et un blanc de référence… D65 » ; « trois ans plus tard, c'est une norme internationale » (IEC 61966-2-1, 1999) |
| 4 | ✅ | « En mille neuf cent quatre-vingt-seize, Hewlett-Packard et Microsoft proposent une norme : le sRGB » |
| 5 | ✅ | « vers quatre cent vingt nanomètres, un vers cinq cent trente, un vers cinq cent soixante » ; « mesurer ces trois pics sur une vraie rétine humaine… mille neuf cent quatre-vingt » |
| 6 | ❌ corrigé | « une équipe les a comptés en mille neuf cent quatre-vingt-dix, sur huit rétines : quatre virgule six millions en moyenne » ; « environ quatre-vingt-douze millions [de bâtonnets] » (Curcio 1990) |
| 7 | ✅ | « Deux lumières complètement différentes peuvent donner exactement les trois mêmes réponses… le métamérisme » ; « son blanc est réglé sur une lumière du jour normée, et trois pics suffisent à l'imiter pour ton œil » |
| 8 | ⚠️ | « Maxwell montre une photo en couleurs faite avec trois filtres : rouge, vert et bleu… Ton écran fait la même chose à l'envers » (pas « la première ») |
| 9 | ⚠️ | « Thomas Young, dès mille huit cent deux. Helmholtz reprend l'idée une cinquantaine d'années plus tard » |
| 10 | ⚠️ | « Mettre moins de trois sous-pixels par pixel, c'est une idée qui a un nom : le PenTile » (pas « même résolution ») |
| 11 | ⚠️ | « Elle vient d'une boîte qui s'appelle Clairvoyante » ; « en deux mille huit, c'est Samsung qui rachète le PenTile » (presse) ; le nom de Candice Brown Elliott passe par le fait 32, pas par Wikipédia |
| 13 | ✅ | « Sur l'iPhone X… le bleu, et de loin… le vert, lui, est de loin le plus petit… DisplayMate » |
| 15 | ⚠️ | « d'après les tests spécialisés, les dalles WRGB de LG ajoutent un quatrième sous-pixel, sans filtre » ; « sur les modèles testés ces dernières années » |
| 16 | ⚠️ | « Ses dernières télés partent encore d'une lumière blanche, mais LG fait évoluer ses dalles » ; rien sur le G6 |
| 17 | ✅ | En réserve (bas du fichier) : « Le QD-OLED de Samsung Display part d'une lumière bleue… » |
| 18 | ✅ | « il pilote séparément le rouge, le vert et le bleu de chaque pixel » ; « en théorie, la résolution sur la largeur devient trois fois plus fine » |
| 19, 22 | ⚠️ | « pas un seul point blanc » (jamais « pas de lumière blanche ») ; « elle tient pour les écrans que j'ai filmés… Sur certaines télés, elle tombe » |
| 20 | ✅ | « d'après Apple, à cette densité, l'œil humain n'arrive plus à distinguer les pixels » (326 ppi, 2010) |
| 23 | ✅ | Le bleu le plus grand, le vert le plus petit (via le fait 13) |
| 24 | ⚠️ | Promesse de la miniature tenue : macro à 0:05, nuance LCD (section 4) et LG (section 5) |
| 25 | ⚠️ | « Coupe le bleu, et ton blanc vire au jaune. Coupe le rouge, il passe au cyan » : dit sur la capture macro, sans chiffre |
| 26 | ✅ | « à cette échelle, ton œil ne fait plus la différence entre les couleurs » ; « Le blanc, c'est toi qui le vois » (une image, dite comme telle) |
| 27 | ⚠️ | « le blanc de ton écran, c'est un réglage, fixé par une norme de mille neuf cent quatre-vingt-seize » |
| 28 | ✅ (grill) | « la première paire, c'est le rouge, la deuxième le vert, la dernière le bleu. Et F F, c'est le maximum » |
| 29 | ✅ (grill) | « ton F F F F F F de tout à l'heure, la norme du web le range toujours dans le sRGB » |
| 30 | ✅ (grill) | « d'après Samsung, chaque point de l'écran fait sa propre lumière » |
| 31 | ✅ (grill) | « deux virgule sept millions de pixels, et autant de sous-pixels verts… un virgule quatre million [de rouges]… des bleus, pareil » ; « les rouges et les bleus qui manquent ne se voient généralement pas » ; « L'écran de l'iPhone X, d'ailleurs, c'est Samsung Display qui le fabrique » |
| 32 | ✅ (grill) | « dans un de ses brevets, déposé en deux mille, l'inventrice, Candice Brown Elliott… très peu de capteurs pour le bleu… bien plus finement en luminosité qu'en couleur » |
| 33 | ✅ (grill) | « Dans leur article de deux mille sur ClearType, ils expliquent que leur filtre est fait pour les atténuer » (les franges elles-mêmes : à filmer, plan F) |
| 34 | ⚠️ (grill) | Non dit. C'est la raison de « les écrans que j'ai filmés » au lieu de « ton téléphone, LCD comme OLED » |

Non utilisés : 12 (liste de téléphones PenTile), 14 (iPhone X contre Galaxy : la comparaison reste muette ; seul le fabricant, Samsung Display, est dit, via le fait 31), 21 (AirPods).

## Questions pour l'auteur

1. **Ton matériel** : quel téléphone (LCD ou OLED ?) et quel écran de PC ? Ça décide d'où vient le macro du hook, si la citation de Microsoft passe sur le plan C, et ce que tu dis dans le crochet « les écrans que j'ai filmés ». Et pour le macro : mode macro du téléphone, objectif à clipser, ou goutte d'eau ?
2. **Ton vécu de dev** : une première couleur en hexa, un bug de couleur ? Le crochet de la section 1 attend une phrase vraie, ou rien.
3. **ClearType** : la V1 te faisait dire « c'est la partie qui me parle en tant que dev » et « je trouve ça génial ». Si c'est vrai, dis-le avec ta raison dans le crochet de la section 6 ; sinon, la section tient sans.
4. **Les gags** : la manette à trois boutons, le cosplay de soleil, le perso faible à la grosse armure, et le nouveau **compteur de quête** (« Trouver un point blanc : 0/1 » → « Quête terminée »). C'est ton humour, ou tu as mieux (une référence de jeu à toi) ?
5. **Candice Brown Elliott** : son nom passe maintenant par un brevet de Clairvoyante (déposé en 2000), où elle est l'inventrice. On ne dit pas « elle a inventé le PenTile » (Wikipédia seul). Ça te va ?
6. **LG** : le fait 16 est à reconfirmer avant le 19 avril 2027. Si la nouvelle génération n'a plus de sous-pixel blanc, la phrase « sur les modèles testés ces dernières années » tient toujours.
7. **L'écran de fin** : la vidéo du 14 déc. s'appelle *D'un pixel à 3,7 milliards de joueurs* (tranché le 23/10). La voix off dit « des milliards » : ça reste juste.
8. **Ce qui t'a le plus surpris** (fin, optionnel) : une ou deux phrases, ou rien.

## Bloc en réserve : le QD-OLED (~10 s)

À glisser en section 5, juste avant LG, si la prise est courte :

> Et sur les télés, chacun son chemin. Le QD-OLED de Samsung Display part d'une lumière bleue, et des boîtes quantiques la transforment en rouge et en vert. LG, lui, part d'une lumière blanche…

Fait 17 (✅, page de Samsung Display). La phrase remplace « Et sur les télés, LG prend un autre chemin : ses OLED partent d'une lumière blanche… ».
