# Louer, acheter ou s'abonner : script final (v2)

**Titre** : *Louer, acheter ou s'abonner : j'ai fait le calcul pour l'IA* (titre mixte recommandé par la [fiche](fiche.md)).

**Sortie** : lun. 4 janv. 2027 à 18 h (bonnes résolutions : « je coupe mes abonnements »). Pilier « IA chez moi », format **calculé**. V2 du 23/10/2026 : corrections du [grill](grill-v1.md) appliquées sur le [script v1](script-v1.md), qui reste tel quel.

**Mis à jour le 23/10 (soir), à ta demande : plus d'électricité, le seul coût de l'achat est le prix de la carte.** La section « Acheter : l'électricité » sort, et les seuils sont recalculés : Pro 89 mois (plus de 7 ans au lieu de 12), Max 100 $ 18 mois (au lieu de 19), Max 200 $ 9 mois, PC complet 38 mois (au lieu de 41), location médiane 38 mois (au lieu de 45), la moins chère 59 mois (au lieu de 79). Les timecodes après 2:59 reculent d'environ 1:30, à recaler sur la vraie prise.

**Durée** : environ 1 530 mots de voix off après le retrait de l'électricité, le 23/10 (avant : 1 760, compte de `controle.py` : 2,0 liaisons pour 100 mots, 0 « vous », question centrale au 57e mot). Avec tes crochets et ⟦à écrire⟧ (~100 à 150 mots) : environ 11 min 15 à 11 min 35 à 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises) ; environ 9 min en coupes serrées comme sur Uber (~180 mots/min). Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : un seul chiffre posé dès la première seconde, le nombre de mois avant qu'une RTX 5080 coûte moins cher qu'un abonnement. L'astérisque tombe dès le hook (la carte ne fait pas tourner Claude, donc c'est pour un modèle de 16 Go), et le taximètre de la location est planté juste après. On construit le chiffre route par route (s'abonner, acheter), puis la troisième route le bat : à 4 h par jour, louer reste moins cher qu'acheter pendant plus de trois ans (relance forte à ≈ 60 % avec tes ajouts). Le verdict répond enfin au titre, profil par profil.

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **hook** : « d'après mon calcul » dans la première phrase (règle 4 du calculé) ; le Max 200 $ reste à l'écran mais sort de la voix ; **l'astérisque « 16 Go » tombe dans les 30 s**, comme le demande la fiche (2e vérification) ; le « piège » flou devient un pont concret : la même carte se loue dès 30 centimes de dollar de l'heure ;
- **ordre** : la location passe **avant** le « piège ». C'est elle qui porte la relance forte (≈ 63 % avec tes ajouts, 66 % sans) : sur trois ans, la location reste sous l'achat. L'ex-section « Le piège » devient « Ce que sait faire un modèle de 16 Go », plus courte, juste avant le verdict ;
- **verdict** : le profil Max dit enfin la route la moins chère (louer d'abord : 30 à 50 € par mois au lieu de 107 €) ; « comme moi » devient un crochet à confirmer ; la « bonne question c'est plutôt… » (reformulation en fausse opposition) est remplacée par un conseil direct ;
- **coupes (~200 mots)** : les 13 $ par développeur en entreprise et « presque un cadeau. Presque. » ; la 3e conversion dite à voix haute (214 €) ; « Bon. On a tout. » ; le doublon du commentaire épinglé ; la phrase des 360 W de NVIDIA, qui contredisait l'hypothèse de 350 W pour tout le PC ; « au moment où j'écris ce script » ; la liste des trois routes en section 1 (déjà dans la question du hook) ; la redite « quand je dis dix-neuf mois » (déjà dans le hook) ;
- **ajouts (~80 mots)** : la facturation de Vast.ai (on paie tant que la machine est allumée, et le stockage même arrêtée : fait 28, ajouté au grill) ; Scaleway comparé au Max ; le seuil de location face à Pro (environ 2 h par jour) ;
- **faits corrigés** : « un an et demi au plus » (faux à 240 h et avec un PC) devient « environ » ; « rationné à la journée » devient « toutes les cinq heures » ; « les prix n'incluent pas les taxes » cité mot pour mot ; « sous toutes les vidéos anglaises » ramené au commentaire réellement relevé ; « cet été » devient « l'été dernier » (la vidéo sort en janvier) ; « plus que ma 5080 » devient « plus de mémoire que ma 5080 » ; les 350 W sont ceux de **tout le PC** (fait 19), pas de la carte ; les 30 000 € de Coût Claude sont dits « pour louer le serveur » ;
- **relevés** : les dix lignes `[PRIX À RELEVER LE 2/01/2027 …]` deviennent des renvois courts `[RELEVÉ Rn]` vers une seule liste, « Relevé avant la voix », en annexe ; la date dite à voix haute est un crochet ; un contrôle CRE est ajouté (le montant du 1er février peut être publié avant ta voix).

**Boucles ouvertes** :
1. Le taximètre « dès 0,30 $/h » (hook, 0:35) → refermé en section 5 (≈ 6:29) : la location bat l'achat à 4 h par jour.
2. « Je t'avais promis cette vidéo » (section 1, rappel de Coût Claude) → refermée par le verdict.
3. Le pari sur le prix de la carte (section 3) → récolté en section 4 (11 mois à 1 200 €).
4. Les compteurs du hook et leurs astérisques → remplis en section 4, battus par le taximètre en section 5, repris dans le verdict.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = à l'écran (motion design). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi, ou à vérifier. `[RELEVÉ Rn]` = prix à relever avant la voix (liste en annexe). `⟦…⟧` = mesure à faire ou texte à écrire par toi. `(#n)` dans les annexes = fait n° n de `sources.md`. Rien de tout ça ne se lit. Nombres en lettres pour la lecture ; la voix arrondit, l'écran donne le chiffre exact.

**Hypothèses du calcul** (à l'écran vers 1:00, et en tête du commentaire épinglé) :
1. **Prix relevés le 23/10/2026**, TTC sauf mention HT. Ils seront relevés de nouveau avant la voix et le 2/01/2027 (annexe « Relevé avant la voix »).
2. **Carte** : RTX 5080 la moins chère, 1 899,95 € (Gainward Python III, LDLC et Materiel.net). **PC fixe complet** : 4 049,95 € (LDLC PC11 BOOSTER).
3. **Abonnements en euros** : Anthropic n'affiche pas de prix en euros. Prix en dollars ÷ 1,1205 (BCE, 22/10/2026) × 1,2 (TVA 20 %) : Pro ≈ 21,42 €, Max 5x ≈ 107,10 €, Max 20x ≈ 214,19 €. Ce sont des calculs, à vérifier à la caisse (claude.ai/upgrade).
4. **Électricité non comptée** (décidé le 23/10) : le seul coût de l'achat est le prix de la carte. Ça avantage un peu l'achat, et c'est dit dans la vidéo.
5. **Usage (pour la location)** : 120 h par mois (≈ 4 h par jour) ; variante à 240 h. Ce sont des cas types, pas des mesures. Sans électricité, les heures ne changent plus le seuil achat contre abonnement.
6. **Location** : prix HT × 1,2 pour les hébergeurs français ; prix en dollars (Vast.ai) ÷ 1,1205, sans TVA ajoutée (non précisée). Les heures louées sont comptées égales aux heures d'écriture : en vrai, il y en a un peu plus (la machine allumée qui attend, le stockage).
7. Pas de revente de la carte, pas d'autre usage (jeu) compté.
8. **On compare des prix, pas des services** : une carte de 16 Go fait tourner un modèle ouvert de 16 Go, pas Claude.

**Chapitres (YouTube, estimés)** :

| Minutage | Chapitre |
|---|---|
| 0:00 | Plus de sept ans |
| 0:40 | D'où viennent les chiffres |
| 1:21 | S'abonner |
| 2:59 | Acheter : la carte |
| 3:53 | Le calcul |
| 5:41 | Louer à l'heure |
| 7:56 | Ce que sait faire un modèle de 16 Go |
| 8:49 | Le verdict selon ton profil |

---

## 0. Plus de sept ans (0:00 – 0:40)

[VISUEL : la RTX 5080 seule sur fond vert sombre (charte « IA chez moi »). Au-dessus, un compteur de mois qui défile et s'arrête sur « 89 mois ». Bandeau en bas dès la première image : « Calcul · prix relevés le [DATE DU RELEVÉ] · sources en description ». Pas de titre, pas de logo.]
[SON : un « tic » par mois qui défile, de plus en plus vite, coupé net à l'arrêt.]

Plus de sept ans. D'après mon calcul, c'est le temps qu'il faut à une RTX 5080 pour coûter moins cher qu'un abonnement Claude à vingt dollars.

[VISUEL : trois compteurs côte à côte : « Pro : + de 7 ans », « Max 100 $ : ≈ 18 mois », « Max 200 $ : ≈ 9 mois ». Mention en petit : « calcul, prix d'achat seul ».]

Contre celui à cent dollars, environ dix-huit mois.

Du coup, quand tu fais le ménage dans tes abonnements en janvier : louer, acheter ou rester abonné, qu'est-ce qui coûte le moins cher ?

[VISUEL : un astérisque rouge tombe sur chaque compteur : « * pour ce qu'un modèle de 16 Go sait faire ».]

Sauf que ma carte ne fait pas tourner Claude. Donc ces dix-huit mois, c'est pour un modèle de seize gigas. Et chaque prix est à l'écran, avec sa source.

[VISUEL : un taximètre s'allume à côté de la carte : « dès 0,30 $/h ».]
[SON : le « ding » du taximètre.]

Et cette même carte se loue dès trente centimes de dollar de l'heure.

---

## 1. D'où viennent les chiffres (0:40 – 1:21)

[VISUEL : carte YouTube vers « Combien coûte Claude en local ? ». Extrait de 2 s de sa fin : « Louer, acheter ou rester abonné, j'en fais une vidéo complète le quatre janvier ».]

Tu te rappelles ? Dans « Combien coûte Claude en local », je t'avais promis cette vidéo pour le quatre janvier. Et en effet, on y est.

⟦à écrire : ton enjeu, en une ou deux phrases. Ton brouillon de Claude #1 dit : « on paie déjà 60 abonnements par mois, c'est trop », et que tu paies Claude Max. Une chose vraie, avec tes mots.⟧

[VISUEL : trois chemins sur une frise de 36 mois : « S'abonner », « Acheter », « Louer ». Les trois partent du même point, sans courbe encore.]

Pour les trois routes, les prix viennent de boutiques et d'hébergeurs français, ou de la page officielle du service. Je les ai relevés le [DATE DU RELEVÉ, EN LETTRES]. Et comme une carte graphique change de prix plus vite qu'un patch de jeu, la date reste en bas de l'écran toute la vidéo.

[VISUEL : la liste des hypothèses, une ligne à la fois, 1 s chacune : « 1 899,95 € », « 1 € = 1,1205 $ », « électricité non comptée », « 120 h par mois (location) ».]

Les dollars, je les convertis au taux de la Banque centrale européenne. Et je ne compte que le prix d'achat : l'électricité dépend trop de ton contrat et de tes heures, donc elle n'est pas dans le calcul. Bref, si un chiffre te paraît bizarre, sa source est en description.

---

## 2. S'abonner (1:21 – 2:59)

On commence par la route que tu connais. Claude Pro, c'est vingt dollars par mois. Et Claude Max existe en deux paliers : cinq fois l'usage de Pro à cent dollars, et vingt fois à deux cents dollars, d'après le centre d'aide d'Anthropic.

[VISUEL : capture de la page de prix d'Anthropic (claude.com/fr-fr/pricing), surlignage sur « 20 $ » puis sur « À partir de 100 $ ».]
[RELEVÉ R1 et R2]

Sauf que tu remarques un détail : il n'y a pas un seul euro sur cette page. Que des dollars, et en petit : « Les prix affichés n'incluent pas les taxes applicables ».

[VISUEL : zoom sur la mention.]

Donc j'ai fait la conversion moi-même. Vingt dollars au taux du jour, plus vingt pour cent de TVA : environ vingt et un euros par mois, d'après mon calcul. Et le Max à cent dollars, environ cent sept euros.

[VISUEL : le calcul posé ligne par ligne.
20 $ ÷ 1,1205 × 1,2 ≈ 21,42 €
100 $ ÷ 1,1205 × 1,2 ≈ 107,10 €
200 $ ÷ 1,1205 × 1,2 ≈ 214,19 €
En dessous : « calcul, pas prix affiché : à vérifier à la caisse ».]

Le vrai prix, tu ne le vois qu'à la caisse.

[RELEVÉ R3 : SI CLAUDE.AI/UPGRADE AFFICHE UN PRIX EN EUROS TTC, DIS-LE À LA PLACE DU CALCUL.]

En face, ChatGPT Plus est à environ vingt-trois euros, d'après la presse.

[RELEVÉ R4]

Et même en payant, Claude te limite sur une fenêtre glissante de cinq heures, et les formules payantes ajoutent une limite à la semaine. Tu vois le problème : tu paies au mois, et tu es rationné toutes les cinq heures.

[VISUEL : une jauge qui se vide en 5 heures, puis un cadenas « limite hebdomadaire » qui se pose dessus.]

Et puisqu'on parle de couper des abonnements : le seul que je te demande de garder, c'est celui-là. Il est gratuit, et lui, il ne te rationne pas.

[VISUEL : bouton « S'abonner » animé, 3 s, sur la jauge des cinq heures.]

---

## 3. Acheter : la carte (2:59 – 3:53)

Deuxième route : tu achètes la carte une fois, et après, elle est à toi. Sur le papier, c'est le rêve.

[VISUEL : la RTX 5080 qui tombe sur un comptoir de boutique, étiquette « 1 899,95 € ».]

Le [DATE DU RELEVÉ], la RTX 5080 la moins chère est à presque mille neuf cents euros, chez LDLC et chez Materiel.net.

[RELEVÉ R5]

Sauf qu'elle a été annoncée à mille cent soixante-dix-neuf euros à sa sortie, en janvier deux mille vingt-cinq, d'après la presse. Et l'été dernier, elle est même descendue à mille deux cents euros. La mienne, je l'ai eue en deux mille vingt-cinq à mille cent euros. Aujourd'hui, on la trouve à mille neuf cents. La preuve que la crise du matériel a vraiment tout cassé.

[VISUEL : une courbe en trois points : « annoncée à 1 179 € (janv. 2025, presse) », « 1 200 € (plus bas de l'été 2026, comparateur) », « 1 899,95 € ([DATE DU RELEVÉ]) ».]

Donc acheter une carte, c'est aussi parier sur le prix du marché. Et ce pari-là pèse plus lourd que tout le reste du calcul, tu vas voir.

Et si tu n'as pas de PC pour la mettre dedans, le premier PC fixe avec une 5080 chez LDLC est à quatre mille cinquante euros, en gros. Le mien, je l'avais monté pour jouer, en deux mille vingt-cinq : deux mille euros. Rien que la RAM m'avait coûté quatre-vingt-treize euros ; aujourd'hui, la même est à cinq cent soixante sur Amazon.

[VISUEL : l'étiquette « 4 049,95 € » sur un PC fixe. Mention : « les portables "RTX 5080" n'ont pas la même puce, on ne les compare pas ».]
[RELEVÉ R6]

Et d'occasion ? Pour la 5080, oublie : en ce moment, elle coûte quasiment le même prix d'occasion qu'en neuf. Par contre, sur des modèles en dessous, une RTX 3060 se trouve à partir de deux cent quarante euros, selon le vendeur. Prends bien la douze gigas : moins de mémoire que ma 5080, mais pour un modèle de douze gigas, ça suffit. Sauf que là, regarde qui vend. Chez un pro, même d'occasion, t'as deux ans de garantie. Entre particuliers, il ne te reste que les vices cachés, et c'est à toi de les prouver. Donc achète chez un pro, et si c'est en ligne, teste-la dans les quatorze jours.

[RELEVÉ : tes prix du 24/10/2026 (5080 d'occasion ≈ neuf ; RTX 3060 dès 240 €) : à revérifier le 2/01.]

[VISUEL : deux étiquettes : « pro : garantie 2 ans, même d'occasion » ; « particulier : vices cachés, à prouver ». Source : `deux-cartes-occasion/sources.md`, conseils 6 et 7 (Code de la consommation L217-3, L217-7, L219-1, L221-18 ; Code civil 1641, 1648).]

[SI LA VIDÉO DES DEUX CARTES D'OCCASION EST SORTIE (21/12) : « Et deux cartes d'occasion pour additionner la mémoire, j'ai fait le calcul dans une vidéo complète : si tu veux le détail, elle est là. » + CARTE YOUTUBE.]

[VISUEL : ton PC de 2025 : 2 000 €, dont la 5080 à 1 100 € ; la RAM : 92,95 € en 2025, 560 € sur Amazon. Tes chiffres du 24/10/2026 : revérifie le prix d'Amazon au relevé du 2/01.]

---

## 4. Le calcul (3:53 – 5:41)

[VISUEL : la balance. À gauche, des barres d'abonnement qui s'empilent mois après mois. À droite, la carte à 1 899,95 €.]

Chaque mois, l'abonnement que tu coupes, c'est de l'argent que tu gardes. Donc la carte est rentable quand ce que tu gardes a remboursé son prix.

[VISUEL : la formule, en grand.
mois = prix de la carte ÷ abonnement
En petit : « électricité non comptée ».]

Contre le Max à cent dollars : mille neuf cents divisés par cent sept, environ dix-huit mois. Un an et demi, en gros.

[VISUEL : 1 899,95 ÷ 107,10 ≈ 17,7 mois. Le compteur « Max 100 $ » du hook se remplit.]

Contre le Max à deux cents dollars, ça descend à neuf mois. Forcément : tu économises deux fois plus vite.

[VISUEL : 1 899,95 ÷ 214,19 ≈ 8,9 mois.]

Et contre Pro, à vingt et un euros ? Mille neuf cents divisés par vingt et un, quatre-vingt-neuf mois. Plus de sept ans.

[VISUEL : 1 899,95 ÷ 21,42 ≈ 89 mois. Le compteur affiche « 7 ans » ; une RTX 5080 qui prend la poussière, toile d'araignée comprise.]

Sept ans. Dans sept ans, ta carte sera une pièce de musée. [TA BLAGUE SI TU VEUX : UNE CARTE D'IL Y A SEPT ANS QUE TON PUBLIC CONNAÎT, DATE À VÉRIFIER.] Bref, pour un usage à vingt euros, la carte n'est jamais rentable.

Et si tu pars de zéro, avec le PC complet à quatre mille cinquante euros ? Contre le Max à cent dollars, il faut trente-huit mois. Plus de trois ans.

[VISUEL : 4 049,95 ÷ 107,10 ≈ 37,8 mois. Le chemin « Acheter » de la frise s'allonge jusqu'au bord de l'écran.]

Par contre, tu te rappelles le pari sur le prix de la carte ? Si tu l'avais eue à mille deux cents euros l'été dernier, le seuil contre le Max tombait à environ onze mois. Un tiers de moins, juste en achetant au bon moment.

[VISUEL : 1 200 ÷ 107,10 ≈ 11,2 mois. Le compteur recule de 18 à 11.]

Donc sur le papier, si tu paies un Max à cent dollars, la carte se rembourse en un an et demi environ. Sauf qu'on n'a regardé que deux routes sur trois.

---

## 5. Louer à l'heure (5:41 – 7:56)

[VISUEL : le chemin « Louer » de la frise s'allume. Le taximètre du hook revient à côté de la carte.]

La troisième, c'est le taximètre du début. Tu ne paies ni un abonnement, ni une carte : tu loues la carte de quelqu'un d'autre, à l'heure.

Et là, sur Vast.ai, une RTX 5080, la même carte que la mienne, se loue dès trente centimes de dollar de l'heure. Environ vingt-sept centimes d'euro.

[VISUEL : « Vast.ai, RTX 5080 : dès 0,303 $/h ≈ 0,27 € (médiane 0,468 $/h) ». Mention : « prix de marché, [DATE DU RELEVÉ], taxes non précisées ».]
[RELEVÉ R9]

Attention, c'est un prix de marché : il bouge avec l'offre et la demande, et la TVA n'est pas précisée. Mais en gros, cent vingt heures par mois, ça te fait environ trente-deux euros. À l'offre médiane, environ cinquante.

[VISUEL : 0,270 € × 120 h ≈ 32 € / mois ; 0,418 € × 120 h ≈ 50 € / mois.]

Du coup, à quatre heures par jour, il faudrait louer trente-huit mois à la médiane, et cinquante-neuf au plus bas, avant que l'achat devienne moins cher.

[VISUEL : 1 899,95 ÷ 50,12 ≈ 37,9 mois ; 1 899,95 ÷ 32,45 ≈ 58,6 mois.]
[SON : la musique coupe net. Une seconde de silence.]
[VISUEL : la frise de 36 mois complète, à 120 h par mois. Max 100 $ : droite raide jusqu'à ≈ 3 856 €. Achat : marche de 1 900 € puis plat (électricité non comptée). Location Vast.ai médiane : droite douce, ≈ 1 804 € à 36 mois. Le taximètre reste sous la marche d'un bout à l'autre.]

Regarde la frise : sur trois ans, la location reste sous l'achat du début à la fin.

Sauf qu'il y a un truc que le taximètre ne montre pas. Tu paies à la seconde tant que la machine est allumée, même quand elle n'écrit rien. Et le stockage se paie en continu, même machine arrêtée, d'après la doc de Vast.ai. Donc tu loueras toujours un peu plus d'heures que tu n'en écris.

[VISUEL : capture de la doc de Vast.ai, surlignage sur « Charged per second while your instance is running » et « Storage charges continue even when instances are stopped ».]

Et chez un hébergeur français ? Scaleway loue une carte L4 de vingt-quatre gigas, plus de mémoire que ma 5080, à soixante-dix-neuf centimes de l'heure hors taxes. Avec la TVA, environ cent quatorze euros pour cent vingt heures. Là, tu paies plus qu'un Max.

[VISUEL : « Scaleway L4 24 Go : 0,79 € HT → 0,95 € TTC × 120 h ≈ 114 € / mois », à côté de « Max 100 $ ≈ 107 € ».]
[RELEVÉ R10]

Chez OVHcloud, il y a moins cher, trente-six centimes de l'heure hors taxes. Sauf que c'est une Quadro RTX 5000 de deux mille dix-huit. Une vieille carte pro de seize gigas, qui n'a rien d'une 5080, malgré le nom.

[VISUEL : « OVHcloud rtx5000-28 : Quadro RTX 5000, 16 Go, 2018 · 0,36 € HT/h ». Le « 5000 » clignote à côté de « 5080 », puis un tampon « pas la même carte ».]
[RELEVÉ R10]

Bref, si tu paies un Max, à quatre heures par jour, la location sur Vast.ai est la moins chère des trois routes pendant plus de trois ans. Mais à trente-deux euros, tu as déjà dépassé Pro. Et si tu passes tes journées dessus, à huit heures par jour, l'achat repasse devant en un an et demi à deux ans et demi environ.

[VISUEL : la frise bascule à 240 h : l'achat croise la location médiane à ≈ 19 mois, la location la moins chère à ≈ 29 mois.]

---

## 6. Ce que sait faire un modèle de 16 Go (7:56 – 8:49)

Mais louer ou acheter quoi, au juste ? Ma 5080 ne fait pas tourner Claude. Et tant qu'Anthropic ne publie pas ses poids, aucune carte de particulier ne le fera tourner.

Ce qu'elle fait tourner, c'est un modèle ouvert qui tient dans ses seize gigas. Par exemple, le Qwen de vingt-sept milliards de paramètres. En quatre bits, il pèse environ seize gigas : trop juste, il déborde de la carte. Du coup, on le compresse en trois bits, il tombe à douze gigas, et là, il tient.

[VISUEL : la jauge « 16 Go » de la carte ; la barre « Qwen3.8-27B, 4 bits : ≈ 16,5 Go » qui dépasse en rouge, puis « 3 bits (IQ3_S) : ≈ 12 Go » qui rentre. Source : `claude-ou-mon-pc-1/modeles-5080.md` (UD-Q4_K_M 16,46 Go, IQ3_S d'ISTA 12,12 Go).]

Est-ce que ça te suffit ? Ça, le calcul seul ne le dit pas. Du coup, j'ai rassemblé les mesures et les avis de ceux qui ont une carte comme la mienne, dans une vidéo complète : si tu veux le détail, elle est là.

⟦à écrire : le résultat de Claude #1 en deux ou trois phrases (calculé depuis le 25/10, plus d'essai). Quel modèle, sa vitesse sur une 5080 d'après les mesures publiées (qui, quand), ce qu'il sait faire et ce qu'il rate. Une scène vue à l'écran, pas un tableau. Jamais « j'ai testé ».⟧

[VISUEL : extrait de Claude #1, le compteur de tokens par seconde en grand ; carte YouTube vers la vidéo des 16 Go.]

Et un modèle de la trempe de Claude, chez soi ? J'en ai fait le calcul dans « Combien coûte Claude en local » : plus de trente mille euros par mois, rien que pour louer le serveur.

[VISUEL : rappel de la baie de serveurs de Coût Claude, compteur « 30 660 € HT / mois », 2 s.]

---

## 7. Le verdict selon ton profil (8:49 – 10:34)

Alors, louer, acheter ou s'abonner ? Ça dépend de ce que tu paies aujourd'hui, et de ce que tu demandes à l'IA. Repère ton profil.

[VISUEL : quatre cartes de profil qui apparaissent une par une, chacune avec sa route en couleur.]

Si tu es sur Pro ou sur ChatGPT Plus, à vingt euros, ne touche à rien. La carte ne sera jamais rentable, et la location te coûte plus cher dès deux heures par jour, environ.

Si tu paies un Max à cent dollars, et que ce qui te sert tient dans un modèle de seize gigas, commence par louer. À quatre heures par jour, c'est trente à cinquante euros par mois, plus le stockage, au lieu de cent sept. Et tu sauras vite si le modèle te suffit.

Si tu es sur le Max à deux cents dollars, la carte se rembourse en neuf mois. Sauf que si tu paies ce prix-là pour avoir le meilleur modèle, lui, il ne rentre pas dans seize gigas.

Et si tu as déjà la carte, parce que tu joues dessus, comme moi, tu l'as déjà payée. Donc pour toi, il n'y a rien à rembourser. Franchement, essaie.

Voilà les quatre cas sur un seul écran, avec le pour et le contre de chaque route. Fais une capture.

[VISUEL : la grille des quatre cas (prix du relevé).
Carte déjà là, contre Pro : rien à rembourser, 21 € gardés par mois.
Carte déjà là, contre Max 100 $ : rien à rembourser, 107 € gardés par mois.
Pas de carte, contre Pro : plus de 7 ans (la carte), 16 ans (le PC complet).
Pas de carte, contre Max 100 $ : environ 18 mois (la carte), 38 mois (le PC complet).
Puis deux colonnes « pour / contre ». Local : tes données restent chez toi, pas de limite toutes les cinq heures, ça marche hors ligne, la carte sert aussi à jouer / un modèle de 16 Go n'est pas Claude, tout se paie d'avance, et le prix de la carte est un pari. Abonnement : le meilleur modèle, rien à installer, rien à payer d'avance / rationné toutes les cinq heures et à la semaine, en dollars plus la TVA, et tes textes partent chez Anthropic.]

[À ÉCRIRE : TON VERDICT À TOI, AVEC TES MOTS. CE QUE TU GARDES (TON ABONNEMENT RÉEL), CE QUE TU FAIS DÉSORMAIS SUR TA 5080, ET COMBIEN D'HEURES PAR MOIS ELLE TRAVAILLE VRAIMENT. ÇA RÉPOND À TON ENJEU DE LA SECTION 1.]

[VISUEL : retour aux trois compteurs du hook, avec leurs astérisques, et le taximètre à côté : « Pro : + de 7 ans », « Max 100 $ : ≈ 18 mois* (louer : 32 à 50 €/mois) », « Max 200 $ : ≈ 9 mois* ». En dessous : « * pour ce qu'un modèle de 16 Go sait faire ».]

Alors avant de couper ou d'acheter quoi que ce soit, demande-toi de quel modèle tu as vraiment besoin. Si c'est Claude, aucune carte ne le remplace. Si c'est un modèle de seize gigas, refais le calcul avec tes heures : toutes les formules sont dans le commentaire épinglé.

Et toi, tu paies combien aujourd'hui, et quel modèle je calcule ensuite ? Dis-le en commentaire.

Et ce que ce modèle fait vraiment sur une carte comme la mienne, c'est dans ma vidéo sur les seize gigas, juste là.

[VISUEL : écran de fin, 20 s : « 16 Go de VRAM suffisent-ils pour remplacer Claude ? » à gauche, « Combien coûte Claude en local ? » en second choix, « S'abonner » à droite.]

---

## Relances d'attention

Temps à 145 mots/min sans tes ajouts (ajoute ~15 s après 0:45 pour ton enjeu, ~20 s après 8:20 pour Claude #1). Après 3:53, tout recule d'environ 1:30 depuis le retrait de l'électricité : à recaler sur la vraie prise.

| Temps (estimé) | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Chiffre-surprise | « Plus de sept ans » et le compteur qui défile |
| 0:10 | Contraste | 18 mois contre plus de 7 ans (9 mois à l'écran) |
| 0:14 | Question centrale | Louer, acheter ou rester abonné ? (57e mot) |
| 0:23 | Enjeu honnête | L'astérisque « 16 Go » tombe sur les compteurs |
| 0:35 | Pont | Le taximètre : la même carte dès 0,30 $/h (refermé à ≈ 6:29) |
| 0:40 | Rappel de série | La promesse de Coût Claude |
| 1:00 | Visuel récurrent | La frise des trois chemins, les hypothèses |
| 1:38 | Surprise | Pas un seul euro sur la page d'Anthropic |
| 2:31 | Concret | « Rationné toutes les cinq heures », la jauge |
| 2:48 | Appel à l'action (≈ 26 %, 27 % avec tes ajouts) | Le seul abonnement à garder |
| 3:16 | Retournement | 1 179 € à la sortie, 1 200 € l'été dernier, 1 900 € aujourd'hui |
| 3:30 | Graine | « Ce pari-là pèse plus lourd que tout le reste » (récolté à ≈ 5:10) |
| 4:12 | Boucle fermée | Le compteur « Max 100 $ » se remplit : 18 mois |
| 4:47 | Humour | 7 ans, la carte au musée, toile d'araignée |
| 5:10 | Récolte | Le pari sur le prix : 11 mois à 1 200 € |
| 5:37 | Pont | « On n'a regardé que deux routes sur trois » |
| 5:51 | Surprise | La même 5080 se loue 27 centimes de l'heure |
| 6:29 | Relance forte (≈ 61 %, ≈ 60 % avec tes ajouts) | Coupure musicale, la frise : la location reste sous l'achat sur trois ans |
| 6:36 | Retournement | Le taximètre tourne même quand la carte n'écrit rien |
| 6:59 | Contraste | Scaleway coûte plus qu'un Max |
| 7:17 | Gag | « RTX 5000 » = carte de 2018 |
| 7:56 | Question | « Louer ou acheter quoi, au juste ? » |
| 8:34 | Rappel de série | 30 000 € par mois (Coût Claude) |
| 8:49 | Verdict | Quatre profils |
| 10:21 | Participation | « Tu paies combien, quel modèle je calcule ensuite ? » |

**Total** : 25 relances en 10 min 34 environ (sans tes ajouts), environ une toutes les 25 s ; le plus long trou est 1:38-2:31 (53 s, la conversion en euros, tenue par le calcul ligne par ligne à l'écran), puis 3:30-4:12 (42 s, l'entrée dans le calcul) et 7:56-8:34 (38 s, tenu par ton résultat de Claude #1).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:40 – 1:21 | Moyen | La méthode (dates, sources) juste après le hook | Raccourcie à 40 s ; le rappel de Coût Claude et ton enjeu d'abord ; hypothèses à 1 s par ligne |
| 1:38 – 2:31 | Moyen | Deux conversions de suite | La voix en dit deux, l'écran en montre trois ; la jauge des 5 heures relance juste après |
| 3:53 – 5:41 | Élevé | Le bloc de calcul, le plus dense | La balance et les compteurs du hook qui se remplissent ; la blague des 7 ans au milieu ; il finit sur un pont (« deux routes sur trois ») |
| ≈ 6:29 | Élevé (≈ 60 %) | Chute classique | Coupure musicale et frise : le taximètre bat l'achat |
| 6:36 – 7:50 | Moyen | Trois hébergeurs | La facturation à la seconde, puis « plus qu'un Max », puis le gag « 5000 n'est pas 5080 » ; RunPod reste en réserve dans l'annexe |

## Notes de montage

- **Les 15 premières secondes** : la carte, le compteur qui défile, les trois compteurs. Rien d'autre : ni logo, ni titre, ni présentation.
- **Le bandeau « Calcul · prix relevés le … »** reste en bas de l'écran pendant toute la vidéo, dès la première image (règle 2 du calculé).
- **Chaque calcul s'affiche** ligne par ligne, avec les mots « calcul », « hypothèse », « mesuré » ou « d'après X » écrits à l'écran (règles 3 et 4).
- **Les compteurs et le taximètre** sont la boucle visuelle : posés dans le hook, remplis dans la section 4, le taximètre passe sous la marche de l'achat à ≈ 6:29, et tout revient dans le verdict.
- **Électricité** : non comptée (décidé le 23/10). La mention « électricité non comptée » apparaît avec les hypothèses (section 1) et sous la formule (section 4).
- **Les phrases à chiffres sont isolées** : si un prix bouge entre ta voix et le 2/01, tu ne refais que ces phrases-là (liste « Relevé avant la voix »).
- **Captures autorisées** : la page de prix d'Anthropic, les pages de prix et la doc des hébergeurs. Pas l'appli Claude. Pas de capture de tes projets Flutter de travail.
- **Pas de portable « RTX 5080 »** à l'écran à côté de la carte de bureau : ce n'est pas la même puce (fait 12).
- **Composants réutilisables** : la frise des trois chemins, la balance, le taximètre. La jauge de mémoire vient de Claude #1, le compteur « 30 660 € » de Coût Claude.
- **Miniature** : charte verte (`vert.html`), à concevoir. Si elle affiche un chiffre, c'est celui de la première phrase (« + de 7 ans ») ou des 18 mois, avec l'astérisque.

## Relevé avant la voix

> À faire le jour de la voix, puis le 2/01/2027. Si un prix a bougé, refais les lignes de « Le calcul », les compteurs du hook et la date du bandeau, puis réenregistre seulement les phrases concernées. Prix du 23/10/2026 entre parenthèses.

| N° | Quoi | Où | Ce qui change si ça bouge |
|---|---|---|---|
| R1 | Claude Pro et Max (20 $, « à partir de 100 $ ») | claude.com/fr-fr/pricing | Section 2, hook, sections 4 et 7 |
| R2 | Le 200 $ du Max 20x | Centre d'aide d'Anthropic (404 le 23/10 : réessaie) | Hook (écran), section 4 |
| R3 | Prix en euros TTC de Pro et des deux Max | claude.ai/upgrade, avant paiement | Remplace le calcul s'il est affiché |
| R4 | ChatGPT Plus (≈ 23 €) | À la caisse (page OpenAI illisible le 23/10) | Section 2, verdict |
| R5 | RTX 5080 la moins chère (Gainward Python III, 1 899,95 €, en stock) | LDLC et Materiel.net | Hook, sections 3, 4, 5, 7 : tous les seuils |
| R6 | PC fixe le moins cher avec RTX 5080 (PC11 BOOSTER, 4 049,95 €) | LDLC | Sections 3 et 4 |
| R9 | Vast.ai, RTX 5080 : offre la moins chère et médiane (0,303 et 0,468 $/h, 10 offres) | console.vast.ai/api/v0/bundles | Hook, sections 5 et 7 |
| R10 | Scaleway L4-1-24G (0,79 €/h HT) ; OVHcloud rtx5000-28 et l4-90 (0,36 et 0,75 €/h HT) | Pages de prix, catalogue OVH | Section 5 |

R7 (tarif EDF) et R8 (tarif du 1er février, CRE) sont retirés le 23/10 avec l'électricité.
| — | Taux BCE (1,1205 $ le 22/10) | ecb.europa.eu | Toutes les conversions |

## Le calcul

> Pour l'écran et pour le commentaire épinglé. Prix du 23/10/2026, à refaire avec le relevé. Script de calcul de la recherche : voir `sources.md`, « Seuil de rentabilité » ; recalculé de zéro au grill (identique).

**Commentaire épinglé (brouillon)**

> Le calcul de la vidéo (prix relevés le [DATE DU DERNIER RELEVÉ]) :
> - Carte : RTX 5080 la moins chère, 1 899,95 € (LDLC, Materiel.net). PC complet : 4 049,95 € (LDLC).
> - Abonnements : prix en dollars ÷ 1,1205 (BCE) × 1,2 (TVA) : Pro ≈ 21,42 €, Max 5x ≈ 107,10 €, Max 20x ≈ 214,19 €. Calcul, à vérifier à la caisse.
> - Seul le prix d'achat compte : l'électricité n'est pas dans le calcul.
> - Acheter contre s'abonner : mois = prix de la carte ÷ abonnement.
> - Acheter contre louer : mois = prix de la carte ÷ location par mois.
> - Refais-le avec tes heures : location par mois = prix horaire × heures.

**Abonnements** : 20 $ → 21,42 € ; 100 $ → 107,10 € ; 200 $ → 214,19 € (÷ 1,1205 × 1,2).

**Acheter contre s'abonner** : mois = P ÷ abonnement (sans électricité, les heures ne comptent pas).

| Contre | Carte (1 899,95 €) | PC complet (4 049,95 €) |
|---|---|---|
| Pro (21,42 €) | 1 899,95 ÷ 21,42 ≈ **89 mois** (> 7 ans) | ≈ 189 mois |
| ChatGPT Plus (23 €) | ≈ 83 mois (> 6 ans) | ≈ 176 mois |
| Max 5x (107,10 €) | 1 899,95 ÷ 107,10 ≈ **17,7 mois** | ≈ **37,8 mois** |
| Max 20x (214,19 €) | 1 899,95 ÷ 214,19 ≈ **8,9 mois** | ≈ 18,9 mois |

- Carte à 1 200 € (plus bas de l'été 2026) contre Max 5x : 1 200 ÷ 107,10 ≈ **11,2 mois** (− 37 %).

**Acheter contre louer** : mois = P ÷ location par mois.

| Location | Prix horaire retenu | Coût à 120 h | Carte rentable en | Coût à 240 h | Carte rentable en |
|---|---|---|---|---|---|
| Vast.ai RTX 5080, offre la moins chère (0,303 $/h) | 0,270 € (÷ 1,1205, sans TVA) | 32,45 € | **58,6 mois** | 64,90 € | 29,3 mois |
| Vast.ai RTX 5080, médiane (0,468 $/h) | 0,418 € | 50,12 € | **37,9 mois** | 100,24 € | 19,0 mois |
| Scaleway L4 24 Go (0,79 € HT) | 0,948 € TTC | 113,76 € | 16,7 mois | 227,52 € | 8,4 mois |
| OVHcloud Quadro RTX 5000 de 2018, 16 Go (0,36 € HT) | 0,432 € TTC | 51,84 € | 36,7 mois | 103,68 € | 18,3 mois |
| En réserve : RunPod RTX 4090 Community (0,34 $/h) | 0,303 € | 36,41 € | 52,2 mois | 72,82 € | 26,1 mois |

**La frise sur 36 mois** (120 h) : Max 5x 107,10 × 36 ≈ **3 856 €** ; achat **1 900 €**, plat (électricité non comptée) ; location Vast.ai médiane 50,12 × 36 ≈ **1 804 €** ; la moins chère 32,45 × 36 ≈ 1 168 €. La location médiane reste sous l'achat jusqu'à 37,9 mois, donc sur toute la frise.

**Louer contre Pro** : la location dépasse Pro (21,42 €) à partir de 21,42 ÷ 0,418 ≈ 51 h par mois (≈ 1,7 h par jour) à la médiane, 21,42 ÷ 0,270 ≈ 79 h (≈ 2,6 h par jour) au plus bas : « dès deux heures par jour, environ ».

**Ce que le calcul ne dit pas** : la carte fait tourner un modèle ouvert qui tient dans 16 Go (Qwen3.8-27B en 3 bits, environ 12 Go ; son 4 bits de 16,46 Go déborde), pas Claude ; pas de revente ; pas de jeu ; **pas d'électricité** (décidé le 23/10 : ça avantage un peu l'achat) ; les heures de location comptées égales aux heures d'écriture (en vrai, un peu plus, et le stockage en plus, fait 28).

## Faits utilisés

| Fait (`sources.md`) | Statut | Phrase du script |
|---|---|---|
| #1 (prix Anthropic, taxes non incluses) | ✅ | « Claude Pro, c'est vingt dollars par mois » ; « Les prix affichés n'incluent pas les taxes applicables » (mot pour mot) |
| #2 (paliers 5x et 20x, 200 $ du 20x) | ⚠️ | « cinq fois l'usage de Pro à cent dollars, et vingt fois à deux cents dollars, d'après le centre d'aide d'Anthropic » (R2 : à relire) |
| #3 (fenêtre de 5 h, limites hebdomadaires) | ✅ | « une limite sur une fenêtre glissante de cinq heures, et les formules payantes ajoutent une limite à la semaine » ; « rationné toutes les cinq heures » |
| #4 (prix en euros = calcul) | ⚠️ | « environ vingt et un euros par mois, d'après mon calcul » ; « Le vrai prix, tu ne le vois qu'à la caisse » |
| #5 (taux BCE) | ✅ | « Les dollars, je les convertis au taux de la Banque centrale européenne » |
| #6 (ChatGPT Plus) | ⚠️ | « ChatGPT Plus est à environ vingt-trois euros, d'après la presse » (Pro non cité) |
| #9 (16 Go) | ✅ | « seize gigas » |
| #10 (1 899,95 €) | ✅ | « la RTX 5080 la moins chère est à presque mille neuf cents euros, chez LDLC et chez Materiel.net » |
| #11, #25, #26 (prix de lancement, plus bas de l'été) | ⚠️ / ❌ évité / ⚠️ | « annoncée à mille cent soixante-dix-neuf euros à sa sortie, en janvier deux mille vingt-cinq, d'après la presse » ; « l'été dernier, elle est même descendue à mille deux cents euros » |
| #12 (PC complet LDLC) | ✅ | « le premier PC fixe avec une 5080 chez LDLC est à quatre mille cinquante euros, en gros » |
| #13 (OVHcloud, Quadro RTX 5000 de 2018) | ✅ | « trente-six centimes de l'heure hors taxes. Sauf que c'est une Quadro RTX 5000 de deux mille dix-huit » |
| #14 (Scaleway L4) | ✅ | « une carte L4 de vingt-quatre gigas, plus de mémoire que ma 5080, à soixante-dix-neuf centimes de l'heure hors taxes » |
| #16 (Vast.ai) | ⚠️ | « dès trente centimes de dollar de l'heure » ; « un prix de marché : il bouge avec l'offre et la demande, et la TVA n'est pas précisée » |
| #20 (Claude non public ; Qwen 27B ≈ 16 Go) | ✅ | « Ma carte ne fait pas tourner Claude » (hook) ; « tant qu'Anthropic ne publie pas ses poids » ; « en quatre bits, il pèse environ seize gigas : trop juste, il déborde » ; « en trois bits, douze gigas » (corrigé le 24/10 : « il tient tout juste » contredisait `modeles-5080.md`, où le Q4 de 16,46 Go ne tient pas) |
| #23 (le hook doit dire les deux cas et le 16 Go) | ⚠️ → appliqué | Hook : « Plus de sept ans » (Pro), « environ dix-huit mois » (Max 100 $), « ces dix-huit mois, c'est pour ce qu'un modèle de seize gigas sait faire » |
| #28 (facturation de Vast.ai, ajouté au grill) | ✅ | « Tu paies à la seconde tant que la machine est allumée […] le stockage se paie en continu, même machine arrêtée, d'après la doc de Vast.ai » |
| Calcul (« Seuil de rentabilité ») | ✅ recalculé le 23/10 sans électricité | 18, 9, 89, 38, 11 mois ; 59 et 38 mois ; frise sur 36 mois ; « dès deux heures par jour, environ » |
| Coût Claude (`cout-claude-local/sources.md`, S12) | ✅ (épisode précédent) | « plus de trente mille euros par mois, rien que pour louer le serveur » |

**Non utilisés, exprès** : #17, #18, #19, #22 et #27 (électricité : retirée le 23/10, à ta demande), #7 (Pro d'OpenAI « fermé », ❓), #8 et #24 (13 $ par développeur en entreprise : coupé, hors des trois routes), #9 pour les 360 W (contredisait l'hypothèse « PC complet »), #21 (OpenRouter : gardé pour un autre épisode), ChatGPT Pro à 103 ou 229 € (pas relevé à la caisse), l'App Store à 22 € (tiers), RunPod (en réserve), 2 723,99 € (❌).

## Questions pour l'auteur

1. **Ton enjeu** (section 1) : ton brouillon de Claude #1 parle de « 60 abonnements par mois » et de ton Claude Max. Quel abonnement paies-tu vraiment, et à quel palier (100 ou 200 $) ? C'est ce qui donne son sens au verdict.
2. **Tes heures** : combien d'heures par mois ta 5080 écrirait-elle vraiment ? Si c'est loin de 120 h, on change le cas type de la location (le hook ne bouge plus : sans électricité, les heures ne changent pas le seuil d'achat ; le verdict « louer d'abord » peut basculer).
3. ~~Mesure de Claude #1~~ : **réglé le 23/10**, pas de mesure et pas d'électricité dans la vidéo.
4. **« Comme moi »** (verdict) : tu joues vraiment sur ta 5080 ? Sinon, on retire le crochet et la phrase garde « parce que tu joues dessus ».
5. **La date de ta voix** : avant ou après le 2 janvier ? Si c'est avant, tu fais le relevé le jour de la voix, puis le 2/01, et tu ne réenregistres que les phrases à chiffres qui ont bougé.
6. **Ta carte** (optionnel) : ce que tu as payé ta 5080, et quand ? Pour toi, c'est un coût déjà payé.
7. **La blague des sept ans** (section 4) : une carte d'il y a sept ans que ton public connaît ? Je vérifierai sa date de sortie.
8. **Hors de ce script** : *Combien coûte Claude en local ?* (23 nov.) donne le Max à 89 € et Pro à 18 €, **sans TVA** ; ici, ils sont à 107 € et 21 € **avec**. Un abonné qui voit les deux lira deux prix pour le même abonnement. **Réglé le 23/10** : tu paies 107 € TTC, Coût Claude passe en TTC (107 € et 21 €).
