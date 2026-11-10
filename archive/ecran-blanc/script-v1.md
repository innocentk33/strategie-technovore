# Écran blanc : script v1

**Titre** : *Le génie caché du pixel : comment ton écran trompe tes yeux*

**Durée** : environ 1 760 mots de voix off (chiffre exact : sortie de `controle.py`). À ton débit mesuré sur ArtCraft (145 mots/min, pauses et improvisations comprises) : environ 12 min 10. À 165 mots/min : 10 min 40. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : on part de la loupe posée sur une page blanche, et on remonte la chaîne : l'écran (trois sous-pixels), l'œil (trois sortes de cônes), la norme qui décide du blanc, puis les écrans qui trichent chacun à leur façon. Le sous-texte de la fiche tient la vidéo : ce que tu vois n'est pas ce qui est là, ton œil fait le mélange.

**Boucles ouvertes** :
1. « Comment ton écran te fait voir une couleur qu'on ne trouve nulle part à la loupe ? » (hook, refermée dans la section 2 puis dans la fin).
2. « Certains écrans cachent bien du blanc quelque part. On va le trouver. » (hook, refermée deux fois : le rétroéclairage du LCD en section 4, le sous-pixel blanc de LG en section 5).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à filmer ou à remplir par toi (les `[DÉMO : …]` sont les démonstrations à faire toi-même). Nombres en lettres pour la lecture.

---

## 0. Hook (0:00 – 0:36)

[VISUEL : plein écran blanc, une page de notes vide sur un téléphone. Pas de titre, pas de logo.]
[DÉMO : TU POSES L'OBJECTIF MACRO (OU UNE LOUPE) SUR TON ÉCRAN, EN UN SEUL PLAN, SANS COUPE.]

Zoome sur ton écran. Regarde bien cette page blanche : pas un seul point blanc.

[VISUEL : le macro révèle les bandes rouges, vertes et bleues. Coupe sèche.]
[SON : clic d'objectif, puis une seconde de silence.]

Du rouge, du vert, du bleu, et c'est tout. Et pourtant, recule d'un pas, et ton écran est blanc partout.

[VISUEL : dézoom rapide, le blanc revient d'un coup.]

Donc ce blanc que tu regardes toute la journée, il sort d'où ? Comment ton écran te fait voir une couleur qu'on ne trouve nulle part à la loupe ?

Pour répondre, il faut ouvrir deux machines : ton écran et ton œil. Sauf que certains écrans cachent bien du blanc quelque part. On va le trouver.

---

## 1. La loupe (0:36 – 2:15)

[VISUEL : le macro, lent, qui glisse sur les bandes rouges, vertes et bleues.]

En fait, ce que tu viens de voir, Microsoft l'écrit noir sur blanc. Sur la page de sa techno ClearType, il y a cette phrase : quand tu vois du blanc sur un écran LCD, tu regardes en réalité des bandes rouges, vertes et bleues.

[VISUEL : la citation en anglais, puis sa traduction : « when we see white on an LCD screen, we are really looking at red, green and blue stripes ».]

Donc un pixel, c'est trois petites cases collées : un sous-pixel rouge, un vert, un bleu. Et quand les trois sont allumés à fond, le pixel donne du blanc.

[VISUEL : un pixel géant, trois barres qui montent ensemble jusqu'en haut ; le pixel devient blanc.]

Si tu as déjà codé une appli, tu connais ce blanc par cœur : F F F F F F. Rouge à fond, vert à fond, bleu à fond. Ton code te le disait depuis le début, en fait.

[VISUEL : un éditeur de code, la ligne « #FFFFFF » ; les trois paires « FF » se colorent en rouge, vert et bleu.]
[TON VÉCU, SI TU EN AS UN : LA PREMIÈRE FOIS QUE TU AS ÉCRIT UNE COULEUR EN HEXA, EN FLUTTER OU EN KOTLIN.]

Et là, regarde ce qui se passe quand on coupe une couleur.

[DÉMO : AFFICHE EN PLEIN ÉCRAN DU JAUNE, PUIS DU CYAN, ET FILME-LES AU MACRO.]
[VISUEL : capture macro réelle. Le bleu s'éteint, le blanc vire au jaune ; le bleu revient, le rouge s'éteint, il passe au cyan.]

Coupe le bleu, et ton blanc vire au jaune. Coupe le rouge, il passe au cyan. Ton blanc, c'est un mélange, et on peut le démonter.

Mais alors, pourquoi tu ne vois jamais ces bandes ? Parce qu'elles sont minuscules. En deux mille dix, pour l'iPhone 4, Apple annonce trois cent vingt-six pixels par pouce. Et d'après Apple, c'est tellement dense que l'œil humain n'arrive plus à distinguer les pixels.

[VISUEL : archive de la keynote de 2010 (extrait court) ou la phrase du communiqué d'Apple, datée.]

Microsoft dit pareil pour les sous-pixels : à cette échelle, ton œil ne fait plus la différence entre les couleurs. Du coup, il les mélange.

Bref, le blanc, c'est ton œil qui le fabrique, avec ce que l'écran lui envoie. Sauf que ça pose une question bizarre. Pourquoi trois couleurs ? Pourquoi pas quatre, ou douze ?

---

## 2. Ton œil n'a que trois capteurs (2:15 – 4:35)

[VISUEL : coupe d'un œil en motion design, zoom jusqu'au fond, sur la rétine.]
[SON : whoosh sur le zoom.]

La réponse est au fond de ton œil. Ta rétine est tapissée de capteurs de lumière, et il y en a deux sortes. Les bâtonnets, environ quatre-vingt-douze millions. Et les cônes : à peu près quatre virgule six millions, d'après une étude de mille neuf cent quatre-vingt-dix qui les a comptés sur huit rétines.

[VISUEL : deux compteurs qui défilent : « 92 000 000 bâtonnets », « 4 600 000 cônes ». Source en bas : Curcio et al., 1990.]

Pour les couleurs, ce sont les cônes qui comptent. Et des cônes, il n'y en a que trois sortes. Un modèle réglé vers quatre cent vingt nanomètres, un vers cinq cent trente, un vers cinq cent soixante.

[VISUEL : trois courbes de sensibilité en cloche (S, M, L), avec leurs pics à 420, 530 et 560 nm. Source : Bowmaker et Dartnall, 1980.]

Quatre virgule six millions de capteurs, et trois modèles en tout. Ton œil, c'est une manette à trois boutons. Et voilà pourquoi trois couleurs suffisent : ton écran appuie sur les trois boutons, dans le bon dosage.

[VISUEL : une manette avec trois boutons S, M, L ; un pixel RVB appuie dessus.]

Et figure-toi que ça, quelqu'un l'a deviné il y a plus de deux siècles : Thomas Young, dès mille huit cent deux. Helmholtz reprend l'idée une cinquantaine d'années plus tard. Et les pics que je viens de te donner, eux, ont été mesurés sur une vraie rétine humaine, en mille neuf cent quatre-vingt.

**Abonnement (≈ 3:15, environ 25 % de la vidéo, juste après la manette à trois boutons)**

Si tu aimes voir ce qui se cache derrière les trucs que tu utilises tous les jours, abonne-toi : sur Technovore, j'ouvre le capot, un truc à la fois.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; les trois courbes restent à l'écran.]

Du coup, pour ton œil, une couleur, ça se résume à trois réponses : une par sorte de cône. Tu vois le problème ? Deux lumières complètement différentes peuvent donner exactement les trois mêmes réponses. Et donc la même couleur. Ça a un nom : le métamérisme.

[VISUEL : à gauche, le spectre continu de la lumière du jour, une bande arc-en-ciel ; à droite, trois pics fins de l'écran. Sous chacun, les trois mêmes jauges de cônes, au même niveau.]

Imagine deux recettes qui n'ont aucun ingrédient en commun, et qui ont exactement le même goût. Ton écran, c'est la recette avec trois ingrédients. Le blanc de ton écran est réglé sur une lumière du jour normée, et trois pics suffisent à l'imiter pour ton œil.

Ouais, ton écran fait du cosplay de soleil. Et ça passe.

[VISUEL : un soleil et un écran côte à côte, l'écran enfile une perruque de soleil.]
[SON : petit jingle de victoire de jeu rétro.]

Mais imiter la lumière du jour, d'accord. Sauf qu'il a bien fallu que quelqu'un décide laquelle.

---

## 3. Le blanc a une date de naissance (4:35 – 5:45)

[VISUEL : une fausse fiche d'identité qui se remplit : « Nom : blanc. Né en : 1996. Parents : ? ».]

Et ce quelqu'un, c'est deux boîtes que tu connais. En mille neuf cent quatre-vingt-seize, Hewlett-Packard et Microsoft proposent une norme : le sRGB. Elle fixe les trois couleurs de base de ton écran, et un blanc de référence : une lumière du jour normée, qui s'appelle D65. Trois ans plus tard, elle devient une norme internationale.

[VISUEL : la fiche se complète : « Parents : HP et Microsoft. Référence : D65 ». La page du W3C de 1996 en capture.]

Donc le blanc de ton écran, c'est un réglage, fixé par une norme de mille neuf cent quatre-vingt-seize. Il a une date de naissance et deux parents. C'est le genre de patch note que personne n'a lu, et qui tourne sur presque tous tes écrans.

[POINT À SOURCER AVANT DE GARDER « PRESQUE TOUS TES ÉCRANS » : VOIR LES QUESTIONS. SINON, DIS « QUI TOURNE SUR TON ÉCRAN ».]

Et l'idée des trois couleurs est encore plus vieille que ça. En mille huit cent soixante et un, Maxwell montre une photo en couleurs faite avec trois filtres : rouge, vert et bleu. Trois photos, une par filtre, projetées l'une sur l'autre. Ton écran fait la même chose à l'envers.

[VISUEL : trois projecteurs, trois images teintées qui se superposent ; puis la même scène en marche arrière, qui se sépare en trois sous-pixels.]

Bon. Jusque-là, j'ai été gentil avec ton écran. Tu te rappelles le début ? Pas un seul point blanc. À la loupe, c'est vrai. Sauf que derrière la loupe, il y a un secret.

---

## 4. Ton LCD cache du blanc (5:45 – 7:05)

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : vue éclatée d'un écran LCD, couche par couche, de l'arrière vers l'avant.]

Si ton téléphone ou ton PC a un écran LCD, la lumière part blanche. Effectivement : tout au fond, il y a un rétroéclairage. D'après des brevets de Philips, c'est une diode bleue recouverte d'un luminophore, et ensemble, elles donnent de la lumière blanche.

[VISUEL : une LED bleue, une couche jaune par-dessus, et la lumière qui sort blanche.]

Ensuite, cette lumière traverse des filtres colorés : rouges, verts, bleus. Et forcément, un filtre rouge ne garde que le rouge. D'après ces mêmes brevets, les filtres jettent au moins les deux tiers de la lumière qui leur arrive.

[VISUEL : un faisceau blanc entre dans le filtre ; un tiers seulement ressort, coloré.]

Et au bout de toute la chaîne, il ne ressort de l'écran qu'environ quatre à dix pour cent de la lumière de départ. C'est ce que décrit un de ces brevets.

[VISUEL : « ≈ 4-10 % » plein écran ; mention « d'après un brevet de Philips ».]

Imagine une lampe qui jette plus de neuf rayons sur dix, juste pour faire des couleurs. Le gaspillage, quoi.

Donc oui, dans un LCD, il y a du blanc. Il est derrière, avant d'être découpé. À la loupe, tu ne le croises jamais : quand il arrive jusqu'à toi, il est déjà en morceaux rouges, verts et bleus.

Voilà ce qui se passe dans un LCD. Mais l'écran de ton téléphone est peut-être un OLED. Et là, la triche change complètement de forme.

---

## 5. Les écrans qui trichent autrement (7:05 – 9:20) · relance à 60 %

[SON : la musique repart, plus rythmée.]
[VISUEL : la grille en losange de l'iPhone X, en macro.]

Sur un écran OLED, chaque sous-pixel produit sa propre lumière. Et sur l'iPhone X, les sous-pixels n'ont même pas la même taille. Avant que je te le dise : à ton avis, lequel est le plus gros ?

[VISUEL : trois sous-pixels cachés sous des points d'interrogation, deux secondes de silence.]

C'est le bleu, et de loin. Parce que c'est celui qui émet le moins bien la lumière : il lui faut plus de surface pour suivre les autres. Le vert, lui, est de loin le plus petit, parce que c'est le plus efficace. C'est l'analyse de DisplayMate, un labo qui teste les écrans.

[VISUEL : les points d'interrogation tombent ; le bleu gonfle, le vert rétrécit.]

En gros, sur ton écran, le bleu, c'est le perso le plus faible de l'équipe, et on lui a filé la plus grosse armure.

Et Samsung a poussé la triche encore plus loin. En deux mille huit, Samsung rachète une grille qui s'appelle le PenTile. L'idée : au lieu de trois sous-pixels par pixel, un pixel sur deux a un rouge et un vert, et l'autre un bleu et un vert.

[VISUEL : une grille RVB classique, puis la grille PenTile qui s'y substitue, pixel par pixel : rouge-vert, bleu-vert, rouge-vert…]

Donc deux sous-pixels par pixel au lieu de trois. Ça fait un tiers de sous-pixels en moins. Tu dois te demander comment ça passe. Tu te rappelles la phrase de Microsoft ? À cette échelle, ton œil ne sépare plus les couleurs. Le PenTile joue sur le même mélange.

Chez Samsung Display, il y a même des écrans qui partent d'une seule couleur. Le QD-OLED part d'une lumière bleue, et des boîtes quantiques la transforment en rouge et en vert. Tout un écran construit à partir du bleu.

[VISUEL : une nappe de lumière bleue ; certains points passent par une boîte quantique et ressortent rouges ou verts.]

Et puis il y a LG, qui fait presque l'inverse. Tu te rappelles les filtres qui jettent au moins les deux tiers de la lumière ? Les télés OLED de LG partent d'une lumière blanche. Et d'après les tests spécialisés, les dalles WRGB de LG ajoutent un quatrième sous-pixel, sans filtre, pour gagner en luminosité. Un sous-pixel blanc.

[VISUEL : le pixel WRGB, quatre cases ; la case sans filtre s'allume en blanc pur.]
[SON : petit « ding » de trouvaille.]

Et là, à la loupe, tu tomberais bien sur un point blanc. C'est ce que disent les tests des modèles de ces dernières années. Leurs dernières télés partent encore d'une lumière blanche, mais LG fait évoluer ses dalles : pour un modèle précis, regarde son test.

[VISUEL : bandeau « Tests RTINGS, TechHive, TFTCentral, jusqu'en 2025 ». À dater sur la version finale.]

Donc ma phrase du début, pas un seul point blanc, elle tient pour ton téléphone, LCD comme OLED. Sur certaines télés, elle tombe. Et je préférais te le dire.

Bon. Jusqu'ici, ce sont des ingénieurs du matériel qui trichent. Sauf qu'il y a aussi un logiciel qui connaît ce secret, et qui s'en sert.

---

## 6. Le code qui se sert des sous-pixels (9:20 – 10:25)

[VISUEL : un mot noir sur fond blanc, dans un éditeur de texte sous Windows.]

Et ça, c'est la partie qui me parle en tant que dev. Le logiciel, c'est ClearType, chez Microsoft. Quand Windows dessine du texte avec ClearType, il pilote séparément le rouge, le vert et le bleu de chaque pixel.

Du coup, sur la largeur, il a trois petites cases par pixel pour placer le bord de chaque lettre. Microsoft écrit qu'en théorie, la résolution horizontale augmente de trois cents pour cent.

[VISUEL : une lettre « A » en gros pixels ; le contour s'affine quand on passe des pixels aux sous-pixels.]
[DÉMO : FILME AU MACRO UN TEXTE NOIR SUR BLANC SOUS WINDOWS, CLEARTYPE ACTIVÉ. SI LES FRANGES COLORÉES NE SE VOIENT PAS, GARDE SEULEMENT L'ANIMATION.]

Normalement, une lettre noire sur fond blanc, c'est noir et blanc. Et pourtant, regarde le bord des lettres au macro : des franges rouges et bleues. À l'œil nu, tu ne les as jamais vues.

Voilà pourquoi je trouve ça génial. L'écran triche, ton œil se fait avoir, et des devs ont écrit du code qui exploite la triche pour que ton texte soit plus net.

---

## 7. Fin (10:25 – 12:10)

[VISUEL : le dézoom de la vidéo à l'envers : le blanc, la loupe, les sous-pixels, l'œil, les trois courbes.]

Bref, on récapitule. À la loupe, ton écran n'a que du rouge, du vert et du bleu. Ton œil n'a que trois sortes de cônes, donc trois couleurs suffisent à le tromper. Le blanc qu'il voit est un réglage de mille neuf cent quatre-vingt-seize. Et chaque écran triche à sa façon : le LCD part d'un blanc qu'il découpe, l'iPhone X gonfle ses bleus, et les dalles de LG ajoutent un point blanc.

Ce que ça change pour toi ? La prochaine fois que tu regardes une page blanche, tu sauras ce qui se passe. Ton écran t'envoie trois couleurs, et c'est ton œil qui fait le mélange. C'est une image, hein : ton cerveau complète. Ce que tu vois n'est pas toujours ce qui est là.

[OPTIONNEL : CE QUI T'A LE PLUS SURPRIS EN PRÉPARANT LA VIDÉO, ET POURQUOI. UNE OU DEUX PHRASES.]

Sur Technovore, j'ouvre comme ça les trucs que tu as dans la poche, un par un. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et si tu veux l'autre histoire du pixel, elle est juste là. Un point blanc sur un écran noir, et tu sais maintenant de quoi il est fait, qui finit avec trois virgule six milliards de joueurs. Un pixel, deux histoires.

[VISUEL : écran de fin, 20 s : la vidéo « D'un pixel à 3,6 milliards de joueurs » (14 déc.) à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:05 | Révélation | Le macro : pas un seul point blanc |
| 0:15 | Contraste | Dézoom, le blanc revient partout |
| 0:30 | Boucle ouverte | « Certains écrans cachent bien du blanc » (refermée à 6:30 et 8:40) |
| 1:00 | Code | « F F F F F F », les trois paires colorées |
| 1:20 | Démo | On coupe une couleur : jaune, cyan |
| 1:45 | Chiffre | 326 pixels par pouce, d'après Apple |
| 2:10 | Question | « Pourquoi trois couleurs ? Pourquoi pas douze ? » |
| 2:30 | Chiffres | 92 millions de bâtonnets, 4,6 millions de cônes |
| 3:00 | Humour | La manette à trois boutons |
| 3:15 | Appel à l'action | Abonnement (≈ 25 %) |
| 3:45 | Visuel | Soleil contre trois pics : le métamérisme |
| 4:20 | Humour | Le cosplay de soleil, jingle rétro |
| 4:35 | Visuel | La fiche d'identité du blanc (1996, HP et Microsoft) |
| 5:20 | Histoire | Maxwell, 1861, trois filtres |
| 5:45 | Coupure musique | Retournement : « derrière la loupe, il y a un secret » |
| 6:30 | Chiffre | 4 à 10 % de la lumière ressort |
| 7:05 | Devinette (relance 60 %) | « Lequel est le plus gros ? » |
| 7:40 | Humour | Le bleu, perso faible à la plus grosse armure |
| 8:00 | Visuel | La grille PenTile qui remplace la grille RVB |
| 8:40 | Boucle fermée | Le sous-pixel blanc de LG |
| 9:05 | Honnêteté | « Ma phrase du début tombe sur certaines télés » |
| 9:40 | Démo | Les franges ClearType au macro |
| 10:25 | Récap | Le dézoom à l'envers |
| 11:35 | Écran de fin | Un pixel, deux histoires |

**Total** : 24 relances en 12 min 10, environ une toutes les 30 secondes ; aucun trou de plus de 45 s.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:36, sortie du hook | Moyen | La citation de Microsoft peut sonner « cours » juste après le macro | Elle confirme ce que le spectateur vient de voir ; à l'image, la citation tient 3 s maximum, puis on revient au macro |
| Section 2, les cônes | Élevé | Le bloc le plus scolaire (nanomètres, rétine) | Deux chiffres seulement, la manette à trois boutons, puis l'abonnement ; les courbes restent simples |
| Métamérisme | Moyen | Le mot fait peur | La recette, puis le cosplay de soleil ; le mot n'arrive qu'après l'idée |
| Relance (~60 %) | Élevé | Chute classique, juste après la section technique du LCD | Musique qui repart, devinette avec deux secondes de silence, puis le gag de l'armure dans les 30 s |
| PenTile | Moyen | La grille peut perdre les non-geeks | Une seule animation (RVB → PenTile), l'arithmétique dite simplement (« deux au lieu de trois ») |
| ClearType | Moyen | Paraît hors sujet pour les non-devs | Annoncé comme « la partie qui me parle en tant que dev », court (1 min), et la démo des franges est visuelle |

## Notes de montage

- **Macros d'écran** : c'est le cœur de la vidéo (~30 h de production prévues dans la fiche). À filmer : la page blanche du hook, les aplats jaune et cyan, le texte ClearType. Toutes les macros sur ton téléphone ou ton PC ; aucun écran de marque en gros plan sans besoin.
- **Composants à construire une fois** : le pixel géant à trois barres (sert aux sections 1, 4, 5 et 7), les trois courbes des cônes, la vue éclatée du LCD, les grilles RVB / PenTile / losange / WRGB. Le pixel géant peut resservir à l'écran de fin vers la vidéo du 14 déc.
- **Sources à l'écran** : une ligne discrète à chaque chiffre (Microsoft, Apple 2010, Curcio 1990, Bowmaker et Dartnall 1980, W3C 1996, brevets Philips, DisplayMate, Samsung Display, tests LG). La vidéo dit « d'après » ; l'image le montre.
- **Pas d'extrait de keynote long** : 2 à 3 s maximum pour Apple, sinon la phrase du communiqué.
- **Énergie** : calme et curieuse ; montées sur le macro du hook, la manette, la coupure de musique de la section 4, la devinette et le point blanc de LG.
- **Miniature** : `noir-04` (loupe sur un écran blanc, « il n'y a pas de blanc. ») tient si le macro arrive dans les 5 premières secondes, comme ici, et si la nuance de LG reste dans la vidéo (fait 24).

## Faits utilisés

| N° (`sources.md`) | 2e vérif | Phrase du script |
|---|---|---|
| 1 | ✅ | « quand tu vois du blanc sur un écran LCD, tu regardes en réalité des bandes rouges, vertes et bleues » ; « trois petites cases… quand les trois sont allumés à fond, le pixel donne du blanc » |
| 2 | ✅ | « D'après des brevets de Philips, c'est une diode bleue recouverte d'un luminophore » ; « les filtres jettent au moins les deux tiers » ; « environ quatre à dix pour cent de la lumière de départ » |
| 3 | ✅ | « Elle fixe les trois couleurs de base de ton écran, et un blanc de référence… D65 » ; « Trois ans plus tard, elle devient une norme internationale » (IEC 61966-2-1, 1999) |
| 4 | ✅ | « En mille neuf cent quatre-vingt-seize, Hewlett-Packard et Microsoft proposent une norme : le sRGB » |
| 5 | ✅ | « Un modèle réglé vers quatre cent vingt nanomètres, un vers cinq cent trente, un vers cinq cent soixante » ; « mesurés sur une vraie rétine humaine, en mille neuf cent quatre-vingt » |
| 6 | ❌ corrigé | « à peu près quatre virgule six millions [de cônes]… comptés sur huit rétines » ; « environ quatre-vingt-douze millions [de bâtonnets] » (Curcio 1990) |
| 7 | ✅ | « Deux lumières complètement différentes peuvent donner exactement les trois mêmes réponses… le métamérisme » ; « réglé sur une lumière du jour normée, et trois pics suffisent à l'imiter pour ton œil » |
| 8 | ⚠️ | « Maxwell montre une photo en couleurs faite avec trois filtres : rouge, vert et bleu… Ton écran fait la même chose à l'envers » (pas « la première ») |
| 9 | ⚠️ | « Thomas Young le devine dès mille huit cent deux. Helmholtz reprend l'idée une cinquantaine d'années plus tard » |
| 10 | ⚠️ | « un pixel sur deux a un rouge et un vert, et l'autre un bleu et un vert… un tiers de sous-pixels en moins » (pas « même résolution ») |
| 11 | ⚠️ | « En deux mille huit, Samsung rachète une grille qui s'appelle le PenTile » |
| 13 | ✅ | « sur l'iPhone X, les sous-pixels n'ont même pas la même taille… le bleu, et de loin… le vert, lui, est de loin le plus petit » |
| 15 | ⚠️ | « d'après les tests spécialisés, les dalles WRGB de LG ajoutent un quatrième sous-pixel, sans filtre, pour gagner en luminosité » ; phrase datée (« les tests des modèles de ces dernières années ») |
| 16 | ⚠️ | « Leurs dernières télés partent encore d'une lumière blanche » ; rien sur le G6 |
| 17 | ✅ | « Le QD-OLED part d'une lumière bleue, et des boîtes quantiques la transforment en rouge et en vert » |
| 18 | ✅ | « il pilote séparément le rouge, le vert et le bleu de chaque pixel » ; « en théorie, la résolution horizontale augmente de trois cents pour cent » |
| 19, 22 | ⚠️ | « pas un seul point blanc » (jamais « pas de lumière blanche ») ; « elle tient pour ton téléphone, LCD comme OLED. Sur certaines télés, elle tombe » |
| 20 | ✅ | « d'après Apple, c'est tellement dense que l'œil humain n'arrive plus à distinguer les pixels » (326 ppi, 2010) |
| 23 | ✅ | Le bleu le plus grand, le vert le plus petit (via le fait 13) |
| 24 | ⚠️ | Promesse de la miniature tenue : macro à 0:05, nuance LCD (section 4) et LG (section 5) |
| 25 | ⚠️ | « Coupe le bleu, et ton blanc vire au jaune. Coupe le rouge, il passe au cyan » : dit sur la capture macro, sans chiffre |
| 26 | ✅ | « à cette échelle, ton œil ne fait plus la différence entre les couleurs » ; « C'est une image, hein : ton cerveau complète » |
| 27 | ⚠️ | « le blanc de ton écran, c'est un réglage, fixé par une norme de mille neuf cent quatre-vingt-seize » (pas « le blanc n'est pas une couleur ») |

Non utilisés : 12 (liste de téléphones PenTile), 14 (iPhone X contre Galaxy), 21 (AirPods).

## Questions pour l'auteur

1. **Le macro** : as-tu un objectif macro ou une loupe pour filmer les sous-pixels de ton téléphone et de ton écran de PC ? Toute la vidéo repose sur ces plans. La goutte d'eau sur l'écran est une piste à tester chez toi, je ne l'ai pas mise dans la voix off (rien dans `sources.md`).
2. **Ton vécu de dev** : une première couleur en hexa, un bug de couleur, un écran qui t'a surpris ? Le crochet de la section 1 attend une phrase vraie, ou rien.
3. **À sourcer avant la v2** (absents de `sources.md`) :
   - « F F F F F F = rouge, vert et bleu à fond » (trivial, mais une ligne de la spec CSS ou sRGB suffit) ;
   - « le sRGB tourne sur presque tous tes écrans » (section 3) : sinon, garde « qui tourne sur ton écran » ;
   - « sur un écran OLED, chaque sous-pixel produit sa propre lumière » : déduit de DisplayMate (« light emission efficiency »), à confirmer par une source sur l'OLED ;
   - « le PenTile joue sur le même mélange » : c'est mon interprétation, pas une source ;
   - les franges colorées de ClearType au macro : à vérifier en filmant.
4. **Le nom de Candice Brown Elliott** (conceptrice du PenTile) : Wikipédia seul, donc je ne l'ai pas dit. Tu veux qu'on le remonte au *Journal of the SID* pour le garder ?
5. **LG** : le fait 16 est à reconfirmer avant le 19 avril 2027. Si la nouvelle génération n'a plus de sous-pixel blanc, la section 5 garde « d'après les tests des modèles de ces dernières années ».
6. **Les gags** : la manette à trois boutons, le cosplay de soleil, le perso faible à la grosse armure. C'est ton humour, ou tu as mieux (une référence de jeu à toi) ?
