# Louer, acheter ou s'abonner : script v1

**Titre** : *Louer, acheter ou s'abonner : j'ai fait le calcul pour l'IA* (titre mixte recommandé par la [fiche](fiche.md)).

**Sortie** : lun. 4 janv. 2027 à 18 h (bonnes résolutions : « je coupe mes abonnements »). Pilier « IA chez moi », format **calculé**. Script v1 du 23/10/2026, écrit sur [`sources.md`](sources.md) (2e vérification du 23/10) et la section « Corrections de la 2e vérification » de la fiche.

**Durée** : 1 876 mots de voix off (compte de `controle.py`), plus tes crochets et ⟦à écrire⟧ (~100 à 150 mots). À 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises) : environ 12 min 56 ; à 165 mots/min : environ 11 min 22. Avec tes ajouts, prévois de couper ~100 mots au grill pour rester sous 13 min. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : un seul chiffre posé dès la première seconde, le nombre de mois avant qu'une RTX 5080 coûte moins cher qu'un abonnement. On le construit route par route (s'abonner, acheter, louer), puis on le retourne : la carte ne fait pas tourner Claude, donc « rentable » veut dire « rentable pour ce qu'un modèle de 16 Go sait faire ».

**Boucles ouvertes** :
1. « Il y a un piège dedans » (hook, 0:30) → refermée dans la section 6 : la carte ne fait pas tourner Claude.
2. « Je t'avais promis cette vidéo » (section 1, rappel de Coût Claude du 16 nov.) → refermée par le verdict.
3. Le compteur de mois à l'écran (hook) → rempli case par case dans la section 5, puis barré d'un astérisque dans la section 6.
4. « Le prochain mouvement du tarif tombe le 1er février » (section 4) → rappelé dans le verdict.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = à l'écran (motion design). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi, ou à vérifier. `[PRIX À RELEVER LE … : …]` = prix à relever avant la sortie. `⟦…⟧` = mesure à faire ou texte à écrire par toi. `(#n)` dans les annexes = fait n° n de `sources.md`. Rien de tout ça ne se lit. Nombres en lettres pour la lecture.

**Hypothèses du calcul** (à l'écran à 1:25, et en tête du commentaire épinglé) :
1. **Prix relevés le 23/10/2026**, TTC sauf mention HT. Ils seront relevés de nouveau avant la sortie et le jour du tournage.
2. **Carte** : RTX 5080 la moins chère, 1 899,95 € (Gainward Python III, LDLC et Materiel.net). **PC complet** : 4 049,95 € (LDLC PC11 BOOSTER).
3. **Abonnements en euros** : Anthropic n'affiche pas de prix en euros. Prix en dollars ÷ 1,1205 (BCE, 22/10/2026) × 1,2 (TVA 20 %) : Pro ≈ 21,42 €, Max 5x ≈ 107,10 €, Max 20x ≈ 214,19 €. Ce sont des calculs, à vérifier à la caisse (claude.ai/upgrade).
4. **Puissance** : **hypothèse de 350 W** pendant que la carte écrit, à remplacer par ⟦mesure de Claude #1⟧.
5. **Électricité** : EDF Tarif Bleu, option Base, 0,2001 €/kWh TTC (depuis le 1er août 2026). Abonnement EDF non compté. Prochain mouvement : 1er février 2027 (CRE), sens et montant non publiés.
6. **Usage** : 120 h de génération par mois (≈ 4 h par jour) ; variante à 240 h. Ce sont des cas types, pas des mesures.
7. **Location** : prix HT × 1,2 pour les hébergeurs français ; prix en dollars (Vast.ai) ÷ 1,1205, sans TVA ajoutée (non précisée).
8. Pas de revente de la carte, pas d'autre usage (jeu) compté.
9. **On compare des prix, pas des services** : une carte de 16 Go fait tourner un modèle ouvert de 16 Go, pas Claude.

**Chapitres (YouTube, estimés)** :

| Minutage | Chapitre |
|---|---|
| 0:00 | Plus de dix ans |
| 0:37 | D'où viennent les chiffres |
| 1:36 | S'abonner |
| 3:42 | Acheter : la carte |
| 4:39 | Acheter : l'électricité |
| 6:14 | Le calcul |
| 8:13 | Le piège |
| 9:15 | Louer à l'heure |
| 11:00 | Le verdict selon ton profil |

---

## 0. Plus de dix ans (0:00 – 0:37)

[VISUEL : la RTX 5080 seule sur fond vert sombre (charte « IA chez moi »). Au-dessus, un compteur de mois qui défile et s'arrête sur « 146 mois ». Pas de titre, pas de logo.]
[SON : un « tic » par mois qui défile, de plus en plus vite, coupé net à l'arrêt.]

Plus de dix ans. C'est le temps qu'il faut à une RTX 5080 pour devenir moins chère qu'un abonnement Claude à vingt dollars.

[VISUEL : trois compteurs côte à côte : « Pro : + de 10 ans », « Max 100 $ : ≈ 19 mois », « Max 200 $ : ≈ 9 mois ». Mention en petit : « calcul, prix du 23/10/2026, 4 h par jour ».]

Contre l'abonnement à cent dollars, environ dix-neuf mois. Et contre celui à deux cents, neuf mois.

Du coup, en janvier, quand tu fais le ménage dans tes abonnements : louer, acheter ou rester abonné, qu'est-ce qui coûte le moins cher ?

Je n'ai pas fait tourner Claude chez moi, donc j'ai fait le calcul, chaque prix à l'écran avec sa source. Sauf qu'il y a un piège dedans.

---

## 1. D'où viennent les chiffres (0:37 – 1:36)

[VISUEL : carte YouTube vers « Combien coûte Claude en local ? ». Extrait de 2 s de sa fin : « Louer, acheter ou rester abonné, j'en fais une vidéo complète le quatre janvier ».]

Tu te rappelles ? Dans « Combien coûte Claude en local », je t'avais promis cette vidéo pour le quatre janvier. Et en effet, on y est.

⟦à écrire : ton enjeu, en une ou deux phrases. Ton brouillon de Claude #1 dit : « on paie déjà 60 abonnements par mois, c'est trop », et que tu paies Claude Max. Une chose vraie, avec tes mots.⟧

Donc on compare trois routes. S'abonner, comme tout le monde. Acheter une carte graphique et faire tourner une IA chez soi. Ou louer une carte à l'heure, chez quelqu'un d'autre.

[VISUEL : trois chemins sur une frise de 36 mois : « S'abonner », « Acheter », « Louer ». Les trois partent du même point, sans courbe encore.]

Tous les prix viennent de boutiques et d'hébergeurs français, ou de la page officielle quand il n'y a pas d'euros. Je les ai relevés le vingt-trois octobre, au moment où j'écris ce script. Et parce que le prix d'une carte graphique bouge plus vite qu'un patch de jeu, je les relève de nouveau avant de tourner.

[VISUEL : bandeau permanent en bas de l'écran pendant toute la vidéo : « Prix relevés le 23/10/2026 · sources en description ».]
[PRIX À RELEVER LE 2/01/2027 : TOUS LES PRIX DE LA VIDÉO, PUIS CHANGER LA DATE DU BANDEAU ET DE CETTE PHRASE.]

L'électricité, c'est le tarif bleu d'EDF, en France. Les dollars, je les convertis au taux de la Banque centrale européenne. Bref, si un chiffre te paraît bizarre, sa source est en description, avec sa date.

[VISUEL : la liste des hypothèses, une ligne à la fois, 1 s chacune : « 1 899,95 € », « 0,2001 €/kWh », « 1 € = 1,1205 $ », « 350 W (hypothèse) », « 120 h par mois ».]

---

## 2. S'abonner (1:36 – 3:42)

On commence par la route que tu connais déjà. Claude Pro, c'est vingt dollars par mois. Et Claude Max existe en deux paliers : cinq fois l'usage de Pro, à cent dollars, et vingt fois, à deux cents dollars, d'après le centre d'aide d'Anthropic.

[VISUEL : capture de la page de prix d'Anthropic (claude.com/fr-fr/pricing), surlignage sur « 20 $ » puis sur « À partir de 100 $ ».]
[PRIX À RELEVER LE 2/01/2027 : PAGE DE PRIX D'ANTHROPIC ; LE 200 $ DU MAX 20X SUR LE CENTRE D'AIDE.]

Sauf que tu remarques un détail : il n'y a pas un seul euro sur cette page. Anthropic affiche ses prix en dollars, et en petit, « les prix n'incluent pas les taxes ».

[VISUEL : zoom sur la mention « Les prix affichés n'incluent pas les taxes applicables ».]

Donc j'ai fait la conversion moi-même. Vingt dollars au taux du jour, plus vingt pour cent de TVA : environ vingt et un euros par mois, d'après mon calcul. Le Max à cent dollars, environ cent sept euros. Et le Max à deux cents, environ deux cent quatorze euros.

[VISUEL : le calcul posé ligne par ligne.
20 $ ÷ 1,1205 × 1,2 ≈ 21,42 €
100 $ ÷ 1,1205 × 1,2 ≈ 107,10 €
200 $ ÷ 1,1205 × 1,2 ≈ 214,19 €
En dessous : « calcul, pas prix affiché : à vérifier à la caisse ».]

Le vrai prix, tu ne le vois qu'à la caisse.

[À VÉRIFIER SUR CLAUDE.AI/UPGRADE AVANT LA VOIX : LE PRIX EN EUROS TTC DE PRO ET DES DEUX MAX. S'IL EST AFFICHÉ, DIS-LE À LA PLACE DU CALCUL.]

Et en face, ChatGPT Plus est à environ vingt-trois euros, d'après la presse. Bref, l'entrée de gamme, partout, tourne autour de vingt euros.

[PRIX À RELEVER LE 2/01/2027 : CHATGPT PLUS, À LA CAISSE (PAGE OPENAI ILLISIBLE LE 23/10).]

Et attention, même en payant, tu n'as pas un accès illimité. Les abonnements ont des limites sur une fenêtre glissante de cinq heures, et les formules payantes ajoutent des limites à la semaine. Tu vois le problème : tu paies au mois, et tu es rationné à la journée.

[VISUEL : une jauge qui se vide en 5 heures, puis un cadenas « limite hebdomadaire » qui se pose dessus.]

Pour situer, en entreprise, Claude Code coûte en moyenne treize dollars par développeur et par jour actif, d'après Anthropic, facturé au token. Donc à côté, l'abonnement à vingt dollars par mois, c'est presque un cadeau. Presque.

[VISUEL : « Entreprise, au token : ≈ 13 $ / dev / jour actif (Anthropic) » face à « Pro : 20 $ / mois ».]

Et puisqu'on parle de couper des abonnements : le seul que je te demande de garder, c'est celui-là. Il est gratuit, et il ne te rationne pas.

[VISUEL : bouton « S'abonner » animé, 3 s, sur la jauge des cinq heures.]

---

## 3. Acheter : la carte (3:42 – 4:39)

Deuxième route : tu achètes la carte une fois, et tu ne paies plus que l'électricité. Sur le papier, c'est le rêve.

[VISUEL : la RTX 5080 qui tombe sur un comptoir de boutique, étiquette « 1 899,95 € ».]

Au moment où j'écris, la RTX 5080 la moins chère est à mille huit cent quatre-vingt-dix-neuf euros quatre-vingt-quinze, chez LDLC et chez Materiel.net.

[PRIX À RELEVER LE 2/01/2027 : RTX 5080 LA MOINS CHÈRE, LDLC ET MATERIEL.NET (23/10 : GAINWARD PYTHON III, 1 899,95 €, EN STOCK).]

Sauf qu'elle a été annoncée à mille cent soixante-dix-neuf euros à sa sortie, en janvier deux mille vingt-cinq, d'après la presse. Et cet été, elle est même descendue à mille deux cents euros. Aujourd'hui, mille neuf cents minimum.

[VISUEL : une courbe en trois points : « annoncée à 1 179 € (janv. 2025, presse) », « 1 200 € (plus bas de l'été, comparateur) », « 1 899,95 € (23/10/2026) ».]

Donc acheter une carte, c'est aussi parier sur le prix du marché. Et ce pari-là, il pèse plus lourd que tout le reste du calcul. On va le voir.

Et si tu n'as pas de PC pour la mettre dedans, le premier PC complet avec une 5080 chez LDLC est à quatre mille quarante-neuf euros quatre-vingt-quinze.

[VISUEL : l'étiquette « 4 049,95 € » sur un PC fixe. Mention : « les portables "RTX 5080" n'ont pas la même puce, on ne les compare pas ».]
[PRIX À RELEVER LE 2/01/2027 : PC FIXE LE MOINS CHER AVEC RTX 5080 CHEZ LDLC (23/10 : PC11 BOOSTER, 4 049,95 €).]

[À ÉCRIRE SI TU VEUX : CE QUE TU AS PAYÉ TA 5080, ET QUAND. POUR TOI, C'EST UN COÛT DÉJÀ PAYÉ.]

---

## 4. Acheter : l'électricité (4:39 – 6:14)

Et la facture d'électricité, alors ? C'est la question qui revient sous toutes les vidéos anglaises, parce qu'elles calculent avec un kilowattheure américain. Ici, on est en France.

[VISUEL : capture de la grille du Tarif Bleu d'EDF, option Base, surlignage sur « 0,2001 € » et sur « à compter du 1er août 2026 ».]

Le tarif bleu d'EDF, option Base, c'est vingt centimes le kilowattheure, depuis le premier août.

[PRIX À RELEVER LE 2/01/2027 : TARIF BLEU EDF, OPTION BASE, 6 KVA (23/10 : 0,2001 €/KWH TTC).]

Pour la consommation, NVIDIA annonce trois cent soixante watts pour la carte. Moi, je prends trois cent cinquante watts pendant qu'elle écrit. Une hypothèse, pas une mesure.

[VISUEL : un compteur de watts à la prise, aiguille sur « 350 W ». Étiquette : « hypothèse ».]

Du coup, à quatre heures par jour, soit cent vingt heures par mois, ça fait huit euros quarante. Et à huit heures par jour, seize euros quatre-vingts.

[VISUEL : le calcul, ligne par ligne.
0,35 kW × 120 h = 42 kWh × 0,2001 € = 8,40 € / mois
0,35 kW × 240 h = 84 kWh × 0,2001 € = 16,81 € / mois]

Huit euros. Ouais, c'est moins que ton abonnement le moins cher. En fait, l'électricité, c'est le plus petit poste de toute la vidéo : de sept à vingt-deux euros par mois, même si ma carte consomme plus ou moins que prévu. Et une erreur sur les watts change le résultat d'un ou deux mois au plus.

Seul bémol : le prochain mouvement du tarif tombe le premier février deux mille vingt-sept, quatre semaines après cette vidéo, d'après la Commission de régulation de l'énergie. Le sens et le montant ne sont pas encore publiés. Donc garde un œil dessus, je mettrai le nouveau tarif en commentaire épinglé.

[VISUEL : un calendrier, le 1er février 2027 entouré, un « ? » sur le prix.]

---

## 5. Le calcul (6:14 – 8:13)

Bon. On a tout. Maintenant, on pose le calcul.

[VISUEL : la balance. À gauche, des barres d'abonnement qui s'empilent mois après mois. À droite, la carte à 1 899,95 € et une petite jauge d'électricité qui monte doucement.]

Chaque mois, l'abonnement que tu coupes, c'est de l'argent que tu gardes. Sauf que tu en reperds un peu en électricité. Donc la carte est rentable quand ce que tu gardes chaque mois a remboursé son prix.

[VISUEL : la formule, en grand.
mois = prix de la carte ÷ (abonnement − électricité)]

Contre le Max à cent dollars : cent sept euros moins huit euros quarante, ça laisse quatre-vingt-dix-huit euros par mois. Mille neuf cents euros divisés par quatre-vingt-dix-huit, environ dix-neuf mois. Un an et demi, en gros.

[VISUEL : 1 899,95 ÷ (107,10 − 8,40) ≈ 19,3 mois. Le premier compteur du hook se remplit.]

Contre le Max à deux cents dollars, ça descend à neuf mois. Forcément : tu économises deux fois plus vite.

[VISUEL : 1 899,95 ÷ (214,19 − 8,40) ≈ 9,2 mois.]

Et contre Pro, à vingt et un euros ? Il te reste treize euros par mois. Mille neuf cents divisés par treize, ça fait cent quarante-six mois. Plus de douze ans.

[VISUEL : 1 899,95 ÷ (21,42 − 8,40) ≈ 146 mois. Le compteur affiche « 12 ans » ; une RTX 5080 qui prend la poussière, toile d'araignée comprise.]

Douze ans. Dans douze ans, ta carte sera une pièce de musée, et tu auras rentabilisé un abonnement que tu aurais pu couper en un clic. Bref, pour un usage à vingt euros, la carte n'est jamais rentable.

Et si tu pars de zéro, avec le PC complet à quatre mille cinquante euros ? Contre le Max à cent dollars, il faut quarante et un mois. Presque trois ans et demi.

[VISUEL : 4 049,95 ÷ 98,70 ≈ 41 mois. Le chemin « Acheter » de la frise s'allonge jusqu'au bord de l'écran.]

Par contre, tu te rappelles le pari sur le prix de la carte ? Si tu l'avais eue à mille deux cents euros cet été, le seuil contre le Max à cent dollars tombait à environ douze mois. Un tiers de moins, juste en achetant au bon moment.

[VISUEL : 1 200 ÷ 98,70 ≈ 12,2 mois. Le compteur recule de 19 à 12.]

Donc sur le papier, si tu paies un Max, la carte se rembourse en un an et demi au plus. Mais ce calcul repose sur une égalité que je n'ai pas encore vérifiée.

---

## 6. Le piège (8:13 – 9:15)

[SON : la musique coupe net. Une seconde de silence.]
[VISUEL : les trois compteurs du hook. Un astérisque rouge tombe sur chacun.]

Ma 5080 ne fait pas tourner Claude. Et aucune carte de particulier ne le fera, parce que ses poids ne sont pas publics.

Ce qu'elle fait tourner, c'est un modèle ouvert qui tient dans ses seize gigas. Par exemple, le Qwen de vingt-sept milliards de paramètres pèse environ seize gigas en quatre bits. Il tient tout juste dans la carte.

[VISUEL : la jauge « 16 Go » de la carte ; la barre « Qwen3.8-27B, 4 bits : ≈ 16 Go » qui s'y glisse au millimètre.]

Du coup, quand je dis « dix-neuf mois », c'est dix-neuf mois pour remplacer ton abonnement par ce que sait faire un modèle de seize gigas. Est-ce que c'est assez pour toi ? Ça, le calcul ne le dit pas. Je l'ai testé dans l'épisode un de « Claude ou mon PC ? ».

⟦à écrire : le résultat de Claude #1 en deux ou trois phrases. Quel modèle, sa vitesse mesurée sur la 5080, la tâche réelle, et ce qu'il en a fait. Une scène vue à l'écran, pas un tableau.⟧

[VISUEL : extrait de Claude #1, le compteur de tokens par seconde en grand ; carte YouTube vers l'épisode 1.]

Et pour un modèle de la trempe de Claude, j'ai fait le calcul dans « Combien coûte Claude en local ». Pour ceux qui l'ont raté : plus de trente mille euros par mois de serveur. Donc là, aucune carte de particulier ne se rentabilise, jamais.

[VISUEL : rappel de la baie de serveurs de Coût Claude, compteur « 30 660 € / mois », 2 s.]

---

## 7. Louer à l'heure (9:15 – 11:00)

Il reste une troisième route, et c'est celle que presque personne ne calcule. Tu ne paies ni un abonnement, ni une carte : tu loues la carte de quelqu'un d'autre, à l'heure.

[VISUEL : le chemin « Louer » de la frise s'allume. Un taximètre apparaît à côté de la carte.]

Et là, sur Vast.ai, une RTX 5080, la même carte que la mienne, se loue dès trente centimes de dollar de l'heure. Environ vingt-sept centimes d'euro.

[VISUEL : « Vast.ai, RTX 5080 : dès 0,303 $/h ≈ 0,27 € (médiane 0,468 $/h) ». Mention : « prix de marché, 23/10/2026, taxes non précisées ».]
[PRIX À RELEVER LE 2/01/2027 : VAST.AI, RTX 5080, OFFRE LA MOINS CHÈRE ET MÉDIANE (23/10 : 0,303 $/H ET 0,468 $/H, 10 OFFRES).]

Attention, c'est un prix de marché : il change d'une heure à l'autre, et la TVA n'est pas précisée. Mais en gros, cent vingt heures par mois, ça te fait environ trente-deux euros. À l'offre médiane, environ cinquante.

[VISUEL : 0,270 € × 120 h ≈ 32 € / mois ; 0,418 € × 120 h ≈ 50 € / mois.]

Donc pour égaler le prix de la carte, il faudrait louer pendant soixante-dix-neuf mois au tarif le plus bas, ou quarante-cinq à la médiane. Plus de six ans, ou un peu moins de quatre.

[VISUEL : 1 899,95 ÷ (32,45 − 8,40) ≈ 79 mois ; 1 899,95 ÷ (50,12 − 8,40) ≈ 45,5 mois.]

Et chez un hébergeur français ? Scaleway loue une carte L4 de vingt-quatre gigas, plus que ma 5080, à soixante-dix-neuf centimes de l'heure hors taxes. Avec la TVA, environ cent quatorze euros pour cent vingt heures.

[VISUEL : « Scaleway L4 24 Go : 0,79 € HT → 0,95 € TTC × 120 h ≈ 114 € / mois ».]
[PRIX À RELEVER LE 2/01/2027 : SCALEWAY L4-1-24G (23/10 : 0,79 €/H HT).]

Chez OVHcloud, il y a moins cher, trente-six centimes de l'heure hors taxes. Sauf que c'est une Quadro RTX 5000 de deux mille dix-huit. Une vieille carte pro de seize gigas, qui n'a rien d'une 5080, malgré le nom.

[VISUEL : « OVHcloud rtx5000-28 : Quadro RTX 5000, 16 Go, 2018 · 0,36 € HT/h ». Le « 5000 » clignote à côté de « 5080 », puis un tampon « pas la même carte ».]
[PRIX À RELEVER LE 2/01/2027 : OVHCLOUD, RTX5000-28 ET L4-90 (23/10 : 0,36 ET 0,75 €/H HT).]

Bref, louer, c'est la route des petits usages. Tu paies les heures où la carte travaille, et rien les autres jours. Sauf qu'à trente-deux euros, tu as dépassé le prix de Pro, pour un modèle de seize gigas. Et si tu passes tes journées dessus, l'achat finit par gagner.

[VISUEL : la frise de 36 mois complète. Les trois chemins tracés à 120 h par mois : abonnement Max (droite raide), location Vast.ai (droite douce), achat (marche de départ puis presque plat). Le point où l'achat croise le Max clignote à 19 mois.]

---

## 8. Le verdict selon ton profil (11:00 – 12:56)

Alors, louer, acheter ou s'abonner ? Ça dépend de ce que tu paies aujourd'hui, et de ce que tu demandes à l'IA.

[VISUEL : quatre cartes de profil qui apparaissent une par une.]

Si tu es sur Pro ou sur ChatGPT Plus, à vingt euros, ne touche à rien. La carte ne sera jamais rentable, et la location te coûterait plus cher dès quelques heures par jour.

Si tu paies un Max à cent dollars, et que ce qui te sert tient dans un modèle de seize gigas, la carte se rembourse en dix-neuf mois environ. Mais avant de sortir mille neuf cents euros, loue une 5080 quelques heures, pour trois fois rien. Tu sauras vite si le modèle te suffit.

Si tu es sur le Max à deux cents dollars, le calcul devient sérieux : neuf mois. Sauf que c'est souvent parce que tu as besoin du meilleur modèle. Et le meilleur modèle, il ne rentre pas dans seize gigas.

Et si tu as déjà la carte, parce que tu joues dessus, comme moi, tu l'as déjà payée. Donc il ne te reste que l'électricité, huit euros par mois pour quatre heures par jour. Franchement, essaie.

[À ÉCRIRE : TON VERDICT À TOI, AVEC TES MOTS. CE QUE TU GARDES (TON ABONNEMENT RÉEL), CE QUE TU FAIS DÉSORMAIS SUR TA 5080, ET COMBIEN D'HEURES PAR MOIS ELLE TRAVAILLE VRAIMENT. ÇA RÉPOND À TON ENJEU DE LA SECTION 1.]

[VISUEL : retour aux trois compteurs du hook, avec leurs astérisques : « Pro : jamais », « Max 100 $ : ≈ 19 mois* », « Max 200 $ : ≈ 9 mois* ». En dessous : « * pour ce qu'un modèle de 16 Go sait faire ».]

Voilà pourquoi la bonne question, en janvier, c'est plutôt : de quel modèle j'ai vraiment besoin ? Si c'est Claude, aucune carte ne le remplace. Si c'est un modèle de seize gigas, alors fais le calcul avec tes heures. Toutes les formules sont dans le commentaire épinglé, et je mettrai à jour l'électricité après le premier février.

Et toi, quel modèle je calcule ensuite ? Dis-le en commentaire, avec ce que tu paies aujourd'hui.

Ce qu'un modèle de seize gigas fait vraiment sur ma carte, je l'ai mesuré dans l'épisode un de « Claude ou mon PC ? ». Il est juste là.

[VISUEL : écran de fin, 20 s : « Claude ou mon PC ? #1 » à gauche, « Combien coûte Claude en local ? » en second choix, « S'abonner » à droite.]

---

## Relances d'attention

| Temps (estimé) | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Chiffre-surprise | « Plus de dix ans » et le compteur qui défile |
| 0:08 | Contraste | Trois compteurs : plus de 10 ans, 19 mois, 9 mois |
| 0:22 | Question centrale | Louer, acheter ou rester abonné ? |
| 0:34 | Boucle ouverte | « Il y a un piège dedans » (refermée à 8:13) |
| 0:40 | Rappel de série | La promesse de Coût Claude |
| 1:05 | Visuel récurrent | La frise des trois chemins |
| 1:55 | Surprise | Pas un seul euro sur la page d'Anthropic |
| 2:50 | Concret | « Rationné à la journée », la jauge des 5 heures |
| 3:30 | Appel à l'action (≈ 27 %) | Le seul abonnement à garder |
| 4:00 | Retournement | 1 179 € à la sortie, 1 899,95 € aujourd'hui |
| 5:20 | Calcul | 8,40 € d'électricité |
| 5:55 | Boucle ouverte | Le 1er février 2027 |
| 6:50 | Boucle fermée | Le premier compteur se remplit : 19 mois |
| 7:15 | Humour | 12 ans, la carte au musée, toile d'araignée |
| 7:50 | Rappel | Le pari sur le prix : 12 mois à 1 200 € |
| 8:13 | Relance forte (≈ 63 %) | Coupure musicale, astérisques rouges : la carte ne fait pas tourner Claude |
| 8:55 | Rappel de série | 30 660 € par mois (Coût Claude) |
| 9:30 | Surprise | Une 5080 se loue 27 centimes de l'heure |
| 10:25 | Retournement | « RTX 5000 » = carte de 2018 |
| 10:50 | Visuel récapitulatif | La frise complète, les courbes qui se croisent |
| 11:00 | Verdict | Quatre profils |
| 12:25 | Participation | « Quel modèle je calcule ensuite ? » |

**Total** : 22 relances en 12 min 56, environ une toutes les 35 s ; aucun trou de plus de 80 s.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:37 – 1:36 | Moyen | La méthode (dates, sources) peut sonner comme une notice | Elle arrive avec le rappel de Coût Claude et ton enjeu ; la frise des trois chemins tient l'image ; hypothèses à 1 s par ligne |
| 2:00 – 2:40 | Moyen | Trois conversions de suite | Une ligne de calcul à l'écran, la voix arrondit ; la jauge des 5 heures relance juste après |
| 6:14 – 8:13 | Élevé | Le bloc de calcul, le plus dense | La balance et les compteurs du hook qui se remplissent un par un ; la blague des 12 ans au milieu |
| 8:13 | Élevé (≈ 63 %) | Chute classique | Coupure musicale et astérisques : on retourne le chiffre du hook |
| 9:50 – 10:50 | Moyen | Beaucoup d'hébergeurs | Trois seulement, le gag « 5000 n'est pas 5080 » au milieu ; RunPod reste en réserve dans l'annexe |

## Notes de montage

- **Refaire le relevé de prix avant la sortie** : tous les `[PRIX À RELEVER …]`, le 2/01/2027 au plus tard, puis le jour du tournage si les deux diffèrent. Si un prix bouge, refais les lignes du calcul (section « Le calcul » ci-dessous) **et** les compteurs du hook, puis la date du bandeau.
- **Les 15 premières secondes** : la carte, le compteur qui défile, les trois compteurs. Rien d'autre : ni logo, ni titre, ni présentation.
- **Le bandeau « Prix relevés le … »** reste en bas de l'écran pendant toute la vidéo (règle 2 du calculé).
- **Chaque calcul s'affiche** ligne par ligne, avec les mots « calcul », « hypothèse », « mesuré » ou « d'après X » écrits à l'écran (règles 3 et 4).
- **Les compteurs du hook** sont la boucle visuelle : posés à 0:10, remplis dans la section 5, barrés d'un astérisque rouge à 8:13, repris avec leurs astérisques dans le verdict.
- **350 W** : étiquette « hypothèse » tant que ⟦mesure de Claude #1⟧ n'existe pas. Si la mesure arrive, remplace l'étiquette par « mesuré le … » et refais les calculs (l'écart reste d'un à deux mois, fait 27).
- **Captures autorisées** : la page de prix d'Anthropic, la grille d'EDF, les pages de prix des hébergeurs. Pas l'appli Claude. Pas de capture de tes projets Flutter de travail.
- **Pas de portable « RTX 5080 »** à l'écran à côté de la carte de bureau : ce n'est pas la même puce (fait 12).
- **Composants réutilisables** : la frise des trois chemins, la balance, le taximètre, le compteur de watts. La jauge de mémoire vient de Claude #1, le compteur « 30 660 € » de Coût Claude.
- **Miniature** : charte verte (`vert.html`), à concevoir.

## Le calcul

> Pour l'écran et pour le commentaire épinglé. Prix du 23/10/2026, à refaire avec le relevé du 2/01/2027. Script de calcul de la recherche : voir `sources.md`, « Seuil de rentabilité ».

**Commentaire épinglé (brouillon)**

> Le calcul de la vidéo (prix relevés le [DATE DU DERNIER RELEVÉ]) :
> - Carte : RTX 5080 la moins chère, 1 899,95 € (LDLC, Materiel.net). PC complet : 4 049,95 € (LDLC).
> - Abonnements : prix en dollars ÷ 1,1205 (BCE) × 1,2 (TVA) : Pro ≈ 21,42 €, Max 5x ≈ 107,10 €, Max 20x ≈ 214,19 €. Calcul, à vérifier à la caisse.
> - Électricité : 0,2001 €/kWh (EDF, option Base). Puissance : 350 W (hypothèse) [OU LA MESURE].
> - Mois avant rentabilité = prix de la carte ÷ (abonnement − électricité).
> - Refais-le avec tes heures : électricité = watts ÷ 1000 × heures × 0,2001.
> - [APRÈS LE 1/02/2027 : NOUVEAU TARIF EDF ET CALCUL MIS À JOUR.]

**Électricité** (c = 0,2001 €/kWh) : coût mensuel = W ÷ 1000 × h × c.
- 350 W × 120 h = 42 kWh → **8,40 €** ; 350 W × 240 h = 84 kWh → **16,81 €**.
- Fourchette : 300 W × 120 h → 7,20 € ; 450 W × 240 h → 21,61 €.

**Abonnements** : 20 $ → 21,42 € ; 100 $ → 107,10 € ; 200 $ → 214,19 € (÷ 1,1205 × 1,2).

**Acheter contre s'abonner** : mois = P ÷ (abonnement − électricité).

| Contre | 120 h, carte (1 899,95 €) | 120 h, PC complet (4 049,95 €) | 240 h, carte |
|---|---|---|---|
| Pro (21,42 €) | 1 899,95 ÷ 13,02 ≈ **146 mois** (> 12 ans) | ≈ 311 mois | ≈ 412 mois |
| Max 5x (107,10 €) | 1 899,95 ÷ 98,70 ≈ **19,3 mois** | ≈ **41,0 mois** | ≈ 21,0 mois |
| Max 20x (214,19 €) | 1 899,95 ÷ 205,79 ≈ **9,2 mois** | ≈ 19,7 mois | ≈ 9,6 mois |

- Carte à 1 200 € (plus bas de l'été) contre Max 5x, 120 h : 1 200 ÷ 98,70 ≈ **12,2 mois** (− 37 %).
- Sensibilité à la puissance (Max 5x) : 19,0 mois à 300 W, 19,7 mois à 450 W (120 h) ; 21,0 à 22,2 mois (240 h).

**Acheter contre louer** (350 W, 120 h) : mois = P ÷ (location − électricité).

| Location | Prix horaire retenu | Coût à 120 h | Carte rentable en |
|---|---|---|---|
| Vast.ai RTX 5080, offre la moins chère (0,303 $/h) | 0,270 € (÷ 1,1205, sans TVA) | 32,45 € | **79,0 mois** |
| Vast.ai RTX 5080, médiane (0,468 $/h) | 0,418 € | 50,12 € | **45,5 mois** |
| Scaleway L4 24 Go (0,79 € HT) | 0,948 € TTC | 113,76 € | 18,0 mois |
| OVHcloud Quadro RTX 5000 de 2018, 16 Go (0,36 € HT) | 0,432 € TTC | 51,84 € | 43,7 mois |
| En réserve : RunPod RTX 4090 Community (0,34 $/h) | 0,303 € | 36,4 € | 67,8 mois |

**Ce que le calcul ne dit pas** : la carte fait tourner un modèle ouvert d'environ 16 Go (Qwen3.8-27B en 4 bits), pas Claude ; pas de revente ; pas de jeu ; abonnement EDF non compté.

## Faits utilisés

| Fait (`sources.md`) | Statut 2e vérif | Phrase du script |
|---|---|---|
| #1 (prix Anthropic, taxes non incluses) | ✅ | « Claude Pro, c'est vingt dollars par mois » ; « les prix n'incluent pas les taxes » |
| #2 (paliers 5x et 20x, 200 $ du 20x) | ⚠️ | « cinq fois l'usage de Pro, à cent dollars, et vingt fois, à deux cents dollars, d'après le centre d'aide d'Anthropic » |
| #3 (fenêtre de 5 h, limites hebdomadaires) | ✅ | « des limites sur une fenêtre glissante de cinq heures, et les formules payantes ajoutent des limites à la semaine » |
| #4 (prix en euros = calcul) | ⚠️ | « environ vingt et un euros par mois, d'après mon calcul » ; « C'est un calcul, je le redis » |
| #5 (taux BCE) | ✅ | « Les dollars, je les convertis au taux de la Banque centrale européenne » |
| #6 (ChatGPT Plus) | ⚠️ | « ChatGPT Plus est à environ vingt-trois euros, d'après la presse » (Pro non cité) |
| #8, #24 (13 $ par dev, en entreprise) | ✅ / ⚠️ | « en entreprise, Claude Code coûte en moyenne treize dollars par développeur et par jour actif, d'après Anthropic, facturé au token » |
| #9 (360 W, 16 Go) | ✅ | « NVIDIA annonce trois cent soixante watts pour la carte » |
| #10 (1 899,95 €) | ✅ | « la RTX 5080 la moins chère est à mille huit cent quatre-vingt-dix-neuf euros quatre-vingt-quinze, chez LDLC et chez Materiel.net » |
| #11, #25, #26 (prix de lancement, plus bas de l'été) | ⚠️ / ❌ évité / ⚠️ | « annoncée à mille cent soixante-dix-neuf euros à sa sortie, en janvier deux mille vingt-cinq, d'après la presse » ; « cet été, elle est même descendue à mille deux cents euros. Aujourd'hui, mille neuf cents minimum » (pas de 2 723,99 €, pas de « plus que doublé ») |
| #12 (PC complet LDLC) | ✅ | « le premier PC complet avec une 5080 chez LDLC est à quatre mille quarante-neuf euros quatre-vingt-quinze » ; portables écartés à l'écran |
| #13 (OVHcloud, Quadro RTX 5000 de 2018) | ✅ | « trente-six centimes de l'heure hors taxes. Sauf que c'est une Quadro RTX 5000 de deux mille dix-huit » |
| #14 (Scaleway L4) | ✅ | « une carte L4 de vingt-quatre gigas […] à soixante-dix-neuf centimes de l'heure hors taxes » |
| #16 (Vast.ai) | ⚠️ | « se loue dès trente centimes de dollar de l'heure » ; « c'est un prix de marché […] la TVA n'est pas précisée » |
| #17 (EDF 0,2001 €/kWh) | ✅ | « vingt centimes le kilowattheure, depuis le premier août » |
| #18 (prochain mouvement le 1er février 2027, CRE) | ✅ | « le prochain mouvement du tarif tombe le premier février deux mille vingt-sept […] Le sens et le montant ne sont pas encore publiés » |
| #19 (consommation non mesurée) | ❓ → hypothèse | « je prends trois cent cinquante watts […] Une hypothèse, pas une mesure » + ⟦mesure de Claude #1⟧ |
| #20 (Claude non public ; Qwen 27B ≈ 16 Go) | ✅ | « Ma 5080 ne fait pas tourner Claude » ; « le Qwen de vingt-sept milliards de paramètres pèse environ seize gigas en quatre bits » |
| #22 (électricité 7 à 22 €) | ✅ | « huit euros quarante » ; « de sept à vingt-deux euros par mois » |
| #23 (le hook doit dire les deux cas) | ⚠️ → appliqué | Hook : « Plus de dix ans » (Pro), « environ dix-neuf mois » (Max 100 $), « neuf mois » (Max 200 $) ; astérisque « 16 Go » à 8:13 |
| #27 (sensibilité à la puissance) | ✅ | « une erreur sur les watts change le résultat d'un ou deux mois au plus » |
| Calcul (« Seuil de rentabilité ») | ✅ recalculé | 19 mois, 9 mois, 146 mois, 41 mois, 12 mois, 79 et 45 mois |
| Coût Claude (`cout-claude-local/sources.md`, S12) | ✅ (épisode précédent) | « plus de trente mille euros par mois de serveur » |

**Non utilisés, exprès** : #7 (Pro d'OpenAI « fermé », ❓), #21 (OpenRouter : quatrième route non retenue), ChatGPT Pro à 103 ou 229 € (pas relevé à la caisse), l'App Store à 22 € (tiers), RunPod (en réserve), 2 723,99 € (❌).

## Questions pour l'auteur

1. **Ton enjeu** (section 1) : ton brouillon de Claude #1 parle de « 60 abonnements par mois » et de ton Claude Max. Quel abonnement paies-tu vraiment, et à quel palier (100 ou 200 $) ? C'est ce qui donne son sens au verdict.
2. **Tes heures** : combien d'heures par mois ta 5080 écrirait-elle vraiment ? Si c'est loin de 120 h, on change le cas type du hook.
3. **Ta carte** : ce que tu as payé ta 5080, et quand ? (Optionnel ; pour toi c'est un coût déjà payé, ce qui sert le profil « tu as déjà la carte ».)
4. **⟦mesure de Claude #1⟧** : la puissance au wattmètre pendant l'écriture est-elle mesurée ? Sans elle, les 350 W restent une hypothèse à l'écran.
5. **Le profil « comme moi »** (verdict) : tu joues vraiment sur ta 5080 ? Sinon, je retire « parce que tu joues dessus, comme moi ».
6. **La route OpenRouter** (louer le modèle à la requête, fait 21) : on l'ajoute en quatrième route, ou on la garde pour un autre épisode ?
