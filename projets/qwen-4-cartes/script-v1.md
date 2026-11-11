# Qwen 4 arrive : quelle carte graphique acheter (ou pas) ? : script V1

> **11/11/2026, écrit le jour de l'enregistrement.** Sortie : **jeu. 12 nov. 2026, 18 h**. Vidéo **calculée** : aucun banc d'essai, des mesures publiées (faits `Qx` de [`sources.md`](sources.md), tous relevés le 11/11) et des prix du jour en euros. Construit d'après l'[audit du 11/11](../../etudes/audit-2026-11-11.md) (sections 2, 2 bis, 3 et 5) : la réponse d'abord, pas de cours avant 1:00, un plan en livrables vers 0:30, au plus 5 nombres dits dans la première minute.

**Titre recommandé** : *Qwen 4 arrive : quelle carte graphique acheter avant que ça monte ?* (titre 2 de la fiche, remanié : « avant que ça monte » est **déjà vrai**, +22 % en 30 jours, et il affirme sans mentir sur Qwen 4). **Je déconseille le titre 3 de la fiche** (« ce qu'il te faudra pour le faire tourner chez toi ») : aucun fichier Qwen 4 n'existe, la vidéo ne pourrait pas tenir cette promesse. Pas de « LLM » dans le titre.

## Ce qui change par rapport à la fiche (à lire avant la voix)

1. **Qwen 4 n'est pas sorti, mais une préversion cloud est ouverte depuis le 11/11** : *Qwen4-Max-Preview*, uniquement par l'abonnement d'Alibaba, jusqu'au 25/11 (Q3). Aucun fichier à télécharger, aucun Qwen 4 sur Hugging Face (Q4).
2. **Le nom « Qwen 4 27B » n'est PAS confirmé.** Le radar du 10/11 et la fiche le disaient « confirmé » : le communiqué d'Alibaba du 22/09 ne dit que « Qwen 4 est en entraînement » (Q1). Les noms Max, Plus, Flash et 27B viennent d'un post sur X (Q6). Le script met donc le 27B du côté de « ce qu'on raconte ». **À corriger dans `fiche.md` et `radar.md`** (je n'y ai pas touché).
3. **La hausse des prix ne vient pas de Qwen 4** : +21,8 % en 30 jours pour la 5060 Ti, +20,2 % pour la 5080 (Q20), avant toute sortie. La fiche pariait sur « Qwen 4 fera monter les cartes » : on dit l'inverse, c'est déjà monté, sans lui.
4. **Toutes les vitesses sont celles de Qwen3.8-27B**, jamais de Qwen 4. La voix le dit chaque fois que le modèle change de nom.
5. **Prix d'occasion : aucun relevé du 11/11** (leboncoin, eBay.fr, Back Market refusent la lecture). Un `⟦à écrire⟧` t'attend en section 2, avec le repli daté du 24/10.
6. La miniature de la fiche (« charte verte ») est périmée : elle passe au style OpenCode (`.claude/rules/miniatures.md`, 11/11).

**Texte et sous-texte** :
- **Texte** : Qwen 4 n'est pas sorti et son 27B n'est même pas annoncé ; on prend Qwen3.8-27B comme étalon, et la règle d'achat tient en une phrase : on achète pour la taille d'un fichier, plus de la place pour la conversation, pas pour un nom.
- **Sous-texte** : le marché ne t'attend pas. La 5060 Ti et la 5080 ont pris plus de 20 % en un mois sans Qwen 4 : attendre a un coût, et payer une rumeur aussi. Montré par la 5090 à 7 900 € contre deux 5060 Ti, jamais dit avant la section 4.
- **À ne pas recadrer** : ce n'est pas une vidéo « achète vite ». C'est « voilà ce qui est sûr, voilà ce qui est calculé ».

**Boucles ouvertes** :
1. « Tu achètes maintenant, ou tu attends ? » (0:29) → section 4.
2. « Deux réglages gratuits qui font presque tripler la vitesse de deux cartes » (0:48) → section 2, palier 32 Go.
3. « La règle d'achat en une phrase » (0:52) → section 4.
4. Le résultat montré à 0:33 (le classement) → déroulé carte par carte en section 2.

**Conventions** : texte normal = voix off ; `[VISUEL]`, `[SON]` = montage (fond noir, grammaire de la vidéo d'installation) ; `(Qx)` = fait de `sources.md`, ne se lit pas ; `⟦à écrire⟧` = tes mots, avec un repli entre parenthèses ; `⟦à vérifier⟧` = une question pour toi ; `[À REVÉRIFIER]` = à relever le jour de la voix. Nombres en lettres pour la lecture. Durée et mesures en bas de page.

---

## 0. Hook et plan (0:00 – 1:00) · objectif : 75 % à 0:15, 50 % à 1:00

[0:00-0:02 VISUEL : fond noir. Plein écran, la vraie page du banc d'essai publié (Q12), ligne « RTX 5090 » surlignée en jaune ; « 75 tok/s » grossit. SON : un coup de basse.]

Soixante-quinze tokens par seconde.

[0:02-0:04 VISUEL : fiche Amazon.fr de la RTX 5090, zoom sur « 7 900 € », qui s'écrit en gros avec la voix (Q21) [À REVÉRIFIER].]
[0:04-0:07 VISUEL : meme « Stonks », la flèche qui monte, posé sur le prix.]

C'est la vitesse de Qwen sur une RTX 5090, affichée à sept mille neuf cents euros.

[0:07-0:09 VISUEL : coupe nette, fiche d'une RTX 5060 Ti, « 28 tok/s » en orange (Q14).]

Sur une 5060 Ti, vingt-huit.

[0:09-0:12 VISUEL : les deux fiches côte à côte ; « MÊME MODÈLE : Qwen3.8-27B » s'écrit entre elles, avec en petit la légende « 5090 : fichier Q4_K_M · 5060 Ti : fichier IQ4_XS, plus petit ».]
[0:12-0:15 VISUEL : le logo « Qwen 4 » en gris, un tampon rouge « PAS ENCORE » se plaque dessus. SON : tampon.]

Même modèle. Et c'est le Qwen d'aujourd'hui, pas Qwen quatre.

[0:15-0:18 VISUEL : la doc d'Alibaba, « available through Token Plan only » surligné en jaune (Q3).]
[0:18-0:21 VISUEL : la courbe de prix du comparateur, ligne « RTX 5060 Ti » : « +21,8 % en 30 jours » en rouge (Q20).]
[0:21-0:24 VISUEL : coupe, ligne « RTX 5080 » : « +20,2 % en 30 jours ».]

Sauf que Qwen quatre arrive, en préversion, dans le cloud d'Alibaba : rien à télécharger. Et la 5060 Ti et la 5080, elles, ont déjà pris plus de vingt pour cent en un mois. Sans lui.

[0:29-0:32 VISUEL : écran noir, une phrase qui s'écrit : « J'ACHÈTE OU J'ATTENDS ? ».]

Du coup, tu achètes ta carte maintenant, ou tu attends ?

[0:33-0:36 VISUEL : LE RÉSULTAT. Le classement s'écrit ligne par ligne sur fond noir : 5 cartes, leur vitesse, leur prix du jour. Une ligne par seconde, sans commentaire.]

Voilà le classement, avec les prix d'aujourd'hui.

[0:36-1:00 VISUEL : quatre cases qui s'allument chacune avec son mot : « SÛR / ON RACONTE », « TA CARTE SELON TON BUDGET », « LA TIENNE, DÉJÀ », « ACHETER OU PAS ? ». À 0:48, un compteur « 22 → 37 → 66 tok/s » clignote, deux réglages cochés.]

Au programme : ce qui est sûr sur Qwen quatre, et ce qu'on raconte. La carte selon ton budget, en euros. Ce que fait la carte que tu as. Et si tu dois acheter maintenant. Plus deux réglages gratuits qui font presque tripler la vitesse de deux cartes. Et à la fin, la règle d'achat, en une phrase.

---

## 1. Qwen 4 : ce qui est sûr, ce qu'on raconte (1:00 – 3:15)

[VISUEL : la page Hugging Face de l'organisation Qwen, modèles triés par date. Le plus récent : un modèle d'image. Aucun « Qwen4 ». Capture du 11/11 (Q4), à refaire le 12/11.]

Réponse courte : Qwen quatre n'est pas sorti. Pas pour toi, en tout cas. À la date où j'enregistre, mercredi onze novembre, la liste des modèles de Qwen n'en contient aucun. Rien à télécharger, point. (Q4)

⟦à écrire 1 : en une phrase, pourquoi toi tu guettes Qwen 4 (repli : « Moi, ce que j'attends, c'est de voir si un modèle de cette taille tient sur une carte de seize gigas. »)⟧

[VISUEL : trois cartes vertes « SÛR » s'empilent, chacune avec la vraie capture, la phrase surlignée en jaune : le communiqué du 22/09 (« currently in training »), la fiche Flash-Next (« will underpin Qwen4 »), la doc Qwen4-Max-Preview.]

Alors voilà ce qui est sûr, parce qu'Alibaba l'a écrit lui-même. Le vingt-deux septembre, le communiqué dit que Qwen quatre est « en entraînement ». Pas de date, pas de taille. (Q1) Fin août, Qwen avait publié un modèle d'essai, Flash-Next, et sa fiche dit que c'est l'aperçu de l'architecture de Qwen quatre. (Q2) Et en effet, mercredi, la préversion de Qwen quatre Max, jusqu'au vingt-cinq novembre. Mais la documentation est claire : uniquement avec l'abonnement d'Alibaba. Donc pas de fichier, et pas de prix à l'usage. (Q3)

[VISUEL : l'écran se coupe en deux, une colonne orange « ON RACONTE ». Tampons « RUMEUR » qui claquent un par un. ⟦à vérifier : sur le communiqué, cherche « 27B » toi-même avant de montrer un « 0 résultat » : le texte peut citer Qwen3.8-27B ; ne le montre que s'il est vrai pour « Qwen 4 »⟧]

Maintenant, ce qu'on raconte. Et là, je sépare bien, parce que ça se mélange partout. Tu as sûrement vu passer « Qwen quatre de vingt-sept milliards », la version qu'on pourrait faire tourner chez soi. Sauf que ce nom n'est pas dans le communiqué. Il vient d'un post partagé après la conférence. Donc ce modèle-là, pour l'instant, c'est une rumeur. Et Alibaba n'a même pas promis que les fichiers seraient publics. (Q6)

[VISUEL : un code de logiciel, la ligne qui nomme un « 27B dense », floutée, tampon « estimation ». Puis une capture floue d'un post « la semaine prochaine », tampon « seconde main ».]

Pareil pour la taille : certains parlent d'une quinzaine de gigas, tirés du code d'un logiciel. C'est une estimation, pas un fichier. (Q7) Et la sortie « la semaine prochaine » ? Un participant à une conférence, de seconde main. (Q8)

[VISUEL : un SSD qui se remplit ; une case « ??? Go » à côté d'un jeu sans nom. Puis l'icône Qwen3.8-27B, étiquette « étalon ».]

Bref, comment on achète une carte pour un modèle qui n'existe pas encore ? On prend le plus proche : Qwen trois point huit, vingt-sept milliards, celui que tu peux télécharger aujourd'hui. C'est comme libérer de la place sur ton SSD pour un jeu dont personne ne connaît le poids : tu prends le précédent comme étalon. Si Qwen quatre garde cette taille, ces chiffres tiendront. Sinon, on refera les comptes. (Q10)

---

## 2. La carte pour chaque budget (3:15 – 7:15)

[VISUEL : le fichier Q4_K_M de Qwen3.8-27B sur la vraie page Hugging Face, « 16,56 GB » entouré (Q9). Puis une jauge vide « ta carte ».]

Le fichier de référence, c'est le Q quatre K M, le quatre bits le plus courant : seize gigas et demi. Et la règle est simple : le fichier, plus de la place pour la conversation, doit rentrer dans ta carte. Sinon, ça déborde dans la RAM, et en fait, ça rame. (Q9)

### Seize gigas : la RTX 5060 Ti

[VISUEL : fiche de la 5060 Ti, étiquette « 16 Go ». La jauge : le fichier Q4_K_M (16,56) dépasse en rouge ; un fichier IQ4_XS (14,35) se glisse en vert (Q9, Q11).]

On commence par seize gigas, avec la RTX 5060 Ti. Mauvaise nouvelle d'abord : le Q quatre K M, seize gigas et demi, ne rentre pas. Du coup, on prend un fichier plus serré, de quatorze gigas : un utilisateur mesure vingt-huit tokens par seconde. C'est très correct pour discuter. Par contre, il te reste presque rien pour la conversation, donc pour un agent de code, c'est juste. (Q11, Q14)

[VISUEL : carte YouTube, « 16 Go de VRAM suffisent » (sortie lundi 9 nov.), 3 secondes.]

J'ai détaillé tout ça lundi, dans la vidéo sur les seize gigas.

[VISUEL : trois fiches qui s'enchaînent : Amazon.fr « 694 € », LDLC « 1 029,95 € » (en rupture), LDLC « 1 099,95 € », chacune avec sa vraie capture et la date du jour (Q21, Q22) [À REVÉRIFIER].]

Et le prix ? En France, de sept cents à mille cent euros, selon le marchand. Oui, l'écart est énorme, et il bouge d'une semaine à l'autre. Donc pour essayer, oui. Pour travailler, c'est serré.

### Vingt-quatre gigas : la RTX 3090, ou la RX 7900 XTX

[VISUEL : fiche de la 3090, « 24 Go ». La jauge : Q4_K_M en vert, une marge verte de « ~8 Go » (Q11). Le compteur « 40 tok/s » puis « 34 » quand une barre « conversation longue » s'allonge (Q13).]

Palier suivant : vingt-quatre gigas, avec la RTX 3090. Du coup, cette fois, le Q quatre K M rentre, avec environ huit gigas de marge pour la conversation. Elle tourne autour de quarante tokens par seconde, puis trente-quatre quand la conversation s'allonge. (Q13)

[VISUEL : un meme « ça monte » ; ligne « 40 → 72 » en vert, légende « avec MTP, sur du code, une mesure » (Q13).]

Et avec le MTP, un réglage qui devine plusieurs mots d'avance, un utilisateur monte à plus de soixante-dix sur du code. En gros, c'est le palier où un modèle de cette taille respire. Par contre, le gain du MTP baisse quand la conversation devient très longue. (Q13)

[VISUEL : fiche Amazon.fr de la 3090, « 2 990 € » (Q21) ; puis une fiche d'annonce d'occasion, prix zoomé.]

Et le prix ? La neuve, deux mille neuf cent quatre-vingt-dix euros chez Amazon. Personne ne l'achète neuve, d'accord. Le vrai prix, c'est celui de l'occasion.

⟦à écrire 2 : les prix d'occasion que tu vois aujourd'hui pour une 3090 en France (capture de tes annonces) (repli : « Fin octobre, les annonces tournaient autour de huit cents à mille euros. Regarde les tiennes : ça a sûrement monté depuis. » : relevé du 24/10, Q23, à ne JAMAIS présenter comme un prix du jour)⟧

[VISUEL : fiche de la RX 7900 XTX, « 1 417 € » ; barre « 29 → 41 tok/s » selon le logiciel (Q16, Q21).]

Côté AMD, la RX 7900 XTX, vingt-quatre gigas aussi, mille quatre cent dix-sept euros neuve. Les mesures vont de vingt-neuf à quarante et un tokens par seconde, selon le logiciel. Donc là, ça dépend vraiment de ta config. (Q16)

### Trente-deux gigas : deux 5060 Ti, ou une 5090

[VISUEL : deux 5060 Ti côte à côte, étiquette « 2 × 16 = 32 Go ». La table GitHub, trois lignes surlignées qui s'écrivent : « couches : 22,1 », « -sm tensor : 37,1 », « + MTP : 65,9 » (Q15).]

Dernier palier : trente-deux gigas. Première option, deux 5060 Ti. Et du coup, c'est là que se cachent deux réglages gratuits. Par défaut, le logiciel se contente de couper le modèle en deux, couche par couche : vingt-deux tokens par seconde. Active le tensor split, et tu passes à trente-sept. Ajoute le MTP : soixante-six, et même soixante-seize chez un autre utilisateur. Presque le triple, sans dépenser un euro. (Q15)

[VISUEL : petit tampon « utilisateurs différents, réglages différents », 2 secondes.]

Attention, ce sont des mesures d'utilisateurs différents. L'ordre de grandeur est solide, la virgule beaucoup moins.

[VISUEL : le calcul s'écrit : « 2 × 694 € = 1 388 € » puis « 2 × 1 099,95 € = 2 200 € » (Q21, Q22) [À REVÉRIFIER].]

Le prix des deux cartes : de mille quatre cents à deux mille deux cents euros.

[VISUEL : fiche de la RTX 5090, « 7 900 € », puis le graphique du comparateur : « médiane 9 300 € », « +89,8 % en 3 mois » en rouge (Q20, Q21). Le meme Stonks revient, démesuré.]

Deuxième option : une seule RTX 5090. Soixante-quinze tokens par seconde. Chez Amazon, en stock, sept mille neuf cents euros. Et la médiane des marchands est à neuf mille trois cents : presque quatre-vingt-dix pour cent de plus en trois mois. (Q12, Q20)

[VISUEL : deux colonnes « 5090 : sans MTP » / « 2 × 5060 Ti : avec MTP » ; le tampon « pas à armes égales ».]

Pour être honnête, elle est testée sans MTP, donc à réglages égaux, elle reste devant. Sauf qu'à ce prix, tu peux t'offrir la paire plusieurs fois. Et je détaille tout ça dans la vidéo sur les trente-deux gigas de VRAM, le lundi vingt-trois novembre.

[VISUEL : carte YouTube, vidéo « 32 Go de VRAM » (lun. 23 nov.), 3 secondes.]

⟦à écrire 3 : encart Afrique, 60 à 80 mots : ce qu'on trouve vraiment chez toi (neuf, occasion, import), à quel prix (en francs CFA ou en euros), les frais de dédouanement, la garantie (repli : « Si t'es en Afrique francophone, ces prix français ne sont qu'un repère : l'occasion est souvent le seul chemin, et le prix dépend de l'import. Dis-moi en commentaire ce que tu trouves chez toi, avec le prix, et je compile. », sans aucun chiffre ni aucune anecdote que tu n'as pas vécue)⟧

---

## 3. Et si t'as déjà une carte ? (7:15 – 8:40)

[VISUEL : retour sur la jauge vide. Trois cartes de taille différente se glissent dedans, l'une après l'autre.]

Et si t'as déjà une carte ? Alors là, bonne nouvelle : en fait, tu n'as peut-être rien à acheter. Il suffit de regarder si le fichier rentre.

[VISUEL : la 5080 « 16 Go », la ligne de la table GitHub « 53,4 → 101,3 », légende « une seule mesure, fichier trois bits » (Q17).]

Avec seize gigas, ça passe avec le fichier serré, comme on l'a vu. Une 5080 comme la mienne est dans ce cas : une personne a mesuré cent un tokens par seconde, mais avec un fichier trois bits, donc moins précis, et c'est une seule mesure. Lundi seize novembre, je teste Strata dessus, en vrai. (Q17)

[VISUEL : « 12 Go » : une jauge où le fichier déborde, une flèche vers « RAM » ; « 5 à 7 tok/s » en rouge (Q18). Puis l'histogramme Steam d'octobre : 8 Go 26,9 %, 12 Go 12,9 % (Q19).]

Avec douze gigas, en revanche, le vingt-sept milliards ne rentre pas en quatre bits. Une partie part dans la RAM, et sur une 3060, ça tombe entre cinq et sept tokens par seconde. Huit gigas : même histoire, en pire. Et c'est le cas de beaucoup de monde : sur Steam, en octobre, plus d'un joueur sur quatre a huit gigas, et un sur huit en a douze. (Q18, Q19)

Donc pour eux, la réponse, ce n'est pas de courir acheter : un modèle de cette taille ne tournera pas bien chez toi, et rien ne dit que Qwen quatre sera plus petit.

⟦à écrire 4 : ta carte à toi, en une phrase (repli : « Ma 5080 me suffit pour essayer, je ne l'ai pas changée. » ; ne rien ajouter sur un test que tu n'as pas fait)⟧

---

## 4. Faut-il acheter maintenant ? (8:40 – 10:00)

[VISUEL : un fond noir, trois cases « FAIT 1 », « FAIT 2 », « FAIT 3 » qui se remplissent.]

Alors, on achète maintenant ? Voilà trois faits.

[VISUEL : la ligne « RTX 5080 : +20,2 % en 30 jours » du comparateur (Q20), puis la phrase « pénurie de mémoire » surlignée dans la capture de la vidéo américaine, source en description (Q24).]

Premier fait : les prix montent déjà. La cause avancée, d'après une chaîne américaine, c'est la pénurie de mémoire, pas Qwen quatre. Donc attendre n'est pas gratuit : ces vingt pour cent, d'autres les ont déjà payés en trop. (Q20, Q24)

[VISUEL : le logo Qwen 4, une case « fichier : ??? Go », tampon « RUMEUR » sur « 27B ».]

Deuxième fait : acheter pour Qwen quatre, aujourd'hui, c'est acheter pour un fichier que personne n'a vu. On ne sait même pas si le vingt-sept milliards existe, ni s'il sera public. (Q6)

[VISUEL : un petit calcul qui s'écrit : « 27 milliards × ~4 bits ≈ 15 à 17 Go » ; la jauge 16 Go déborde, la jauge 24 Go garde de la marge (Q9, Q11).]

Troisième fait : un modèle de cette taille, en quatre bits, pèse entre quinze et dix-sept gigas. Même si Qwen quatre fait un peu plus, vingt-quatre gigas gardent de la marge. Seize gigas, non. (Q9, Q11)

[VISUEL : fond noir, une seule phrase qui s'écrit mot par mot, en grand : « N'ACHÈTE PAS POUR UN NOM. ACHÈTE POUR LA TAILLE D'UN FICHIER. »]

Donc voilà la règle, en une phrase : n'achète pas pour un nom, achète pour la taille d'un fichier, plus de la place pour la conversation. Aujourd'hui, ça veut dire vingt-quatre gigas, ou deux fois seize avec le bon réglage.

Et si t'as déjà seize gigas ou plus, ne change rien : tu auras la vraie réponse quand Alibaba publiera les vrais fichiers. Et là, je refais ce classement avec les vrais chiffres.

⟦à écrire 5 : le choix de l'auteur, la carte que toi tu prendrais et pourquoi (repli : « Moi, je ne change rien avant d'avoir vu le vrai fichier de Qwen quatre. »)⟧

---

## 5. Fin (10:00 – 10:30)

[VISUEL : la jauge et la règle en bas. Puis la carte YouTube « 16 Go de VRAM suffisent ».]

Dis-moi en commentaire ta carte, ton budget, et ce que tu trouves vraiment chez toi, avec le prix : je compile, surtout pour ceux qui n'ont pas accès aux prix français. Et du coup, si t'as seize gigas, la vidéo de lundi te dit quel fichier prendre.

[VISUEL : écran de fin, 20 s : à gauche *16 Go de VRAM suffisent* (lun. 9 nov.), à droite la prochaine vidéo IA ; bouton « S'abonner ».]

Lundi seize novembre, je teste Strata sur ma 5080, en vrai. Et le vingt-trois, les trente-deux gigas de VRAM, en détail.

---

## Relances d'attention (timecodes estimés à 145 mots/min, avec tes `⟦à écrire⟧` comptés ; à recaler sur la vraie voix)

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Résultat | 75 tok/s, la page du banc d'essai |
| 0:04 | Meme + prix | Stonks sur les 7 900 € |
| 0:08 | Contraste | 28 tok/s sur une 5060 Ti |
| 0:14 | Retournement | Qwen 4 : cloud seulement |
| 0:29 | Question centrale | « Tu achètes ou tu attends ? » |
| 0:33 | Résultat | le classement s'écrit |
| 0:48 | Boucle ouverte | deux réglages qui triplent presque la vitesse |
| 0:55 | Boucle ouverte | la règle d'achat en une phrase |
| 1:26 | Preuve | les trois cartes « SÛR » |
| 2:01 | Retournement | « ON RACONTE » : le 27B n'est pas annoncé |
| 2:46 | Image gamer | le jeu dont personne ne connaît le poids |
| 3:37 | Résultat | le Q4_K_M ne rentre pas dans 16 Go |
| 4:10 | Surprise | l'écart de prix, 700 à 1 100 € |
| 4:42 | Chiffre | 40 tok/s, puis 72 avec le MTP |
| 5:41 | Révélation | les deux réglages gratuits, 22 → 37 → 66 |
| 6:23 | Contraste | la 5090 contre deux 5060 Ti |
| 7:18 | Appel | Afrique : ton prix en commentaire |
| 7:29 | Promesse tenue | ta carte actuelle |
| 8:43 | Retournement | la hausse ne vient pas de Qwen 4 |
| 9:26 | Récolte | la règle en une phrase |

Au plus 60 s environ entre deux relances (le plus long : 6:40 → 7:18, 5090 puis encart Afrique, ou 3:37 → 4:10). Si la voix dépasse 11 min, coupe d'abord le paragraphe AMD (environ 20 s), puis les 12 et 8 Go.

## Notes de montage (grammaire de la vidéo d'installation)

- **Fond noir, jamais le bleu ardoise de 16 Go.** Vraies images partout : la table GitHub, les fiches Amazon.fr et LDLC avec leur prix et la date visibles, le communiqué d'Alibaba et la doc avec la phrase surlignée en jaune, la page Hugging Face. Pas de schéma redessiné, sauf la jauge « ta carte » (un seul schéma, en plans courts).
- **0 à 30 s : un plan nouveau toutes les 1 à 3 s.** Un meme (Stonks) avant 0:15 ; les mots qui comptent s'écrivent avec la voix (« 75 tok/s », « 7 900 € », « PAS ENCORE », « J'ACHÈTE OU J'ATTENDS ? »).
- **« SÛR » en vert, « ON RACONTE » en orange**, avec un tampon « RUMEUR », à l'écran à chaque fois : c'est la promesse du plan.
- **Une image réelle au moins toutes les 15 s** entre les schémas.
- **Chaque prix à l'écran porte sa date (« 11/11/2026 »).** Refais les captures le jour de la voix et la veille de la sortie.
- **Avant la mise en ligne (jeu. 12/11, matin)** : rouvre la page des modèles de Qwen sur Hugging Face et la doc de `qwen4-max-preview`. Si Qwen 4 est sorti entre-temps, la section 1 change (vraies tailles de fichier) : préviens-moi.

## Faits utilisés

| Dit dans le script | Faits |
|---|---|
| Qwen 4 « en entraînement », 22/09, sans date ni taille | Q1 |
| Flash-Next, aperçu de l'architecture de Qwen 4 | Q2 |
| Préversion de Qwen4-Max jusqu'au 25/11, abonnement seulement | Q3 |
| Aucun Qwen 4 dans la liste des modèles de Qwen au 11/11 | Q4 |
| Le nom « Qwen 4 de 27 milliards » absent du communiqué : rumeur | Q6 |
| Une quinzaine de gigas, tirés du code d'un logiciel : estimation | Q7 |
| Sortie « la semaine prochaine » : seconde main | Q8 |
| Qwen3.8-27B : étalon, fichiers 16,56 et 14,35 Go | Q9, Q10, Q11 |
| 5090 : 75 tok/s, 7 900 € (Amazon), médiane 9 300 €, +89,8 % en 3 mois | Q12, Q20, Q21 |
| 5060 Ti : 28 tok/s ; 700 à 1 100 € | Q14, Q21, Q22 |
| 3090 : 40 puis 34 tok/s ; 72 avec MTP sur du code ; neuve 2 990 € | Q13, Q21 |
| 7900 XTX : 29 à 41 tok/s, 1 417 € | Q16, Q21 |
| Deux 5060 Ti : 22, 37, 66 et 76 tok/s | Q15 |
| Hausses de 20 % en 30 jours, cause avancée : la mémoire | Q20, Q24 |
| 5080 : 101 tok/s avec un fichier trois bits, une mesure | Q17 |
| 3060 12 Go : 5 à 7 tok/s ; Steam 8 et 12 Go | Q18, Q19 |

**Interdits respectés** : aucun nom de chaîne, de site de mesures ni de créateur dans la voix (« un utilisateur », « une chaîne américaine », « un participant à une conférence ») ; aucun « vous » ; aucune anecdote ni aucun test attribués à l'auteur ; aucune vitesse de Qwen 4 ; les prix d'occasion ne sont jamais présentés comme prix du jour ; « Qwen quatre de vingt-sept milliards » est toujours dit comme une rumeur.

## Contrôles (11/11/2026, comptés sur la voix seule, sans `[…]`, sans `(Qx)` ni `⟦…⟧`)

| Mesure | Résultat | Cible |
|---|---|---|
| Mots dits (script, nombres en chiffres) | **1 410** (téléprompteur : nombres en lettres, noms de cartes en chiffres) | 1 300 à 1 600 |
| Réponses des `⟦à écrire⟧` (replis inclus) | environ 130 mots de plus | |
| **Durée à 145 mots/min** | **environ 10 min 30** avec tes cinq passages (9 min 40 sans) | 9 à 11 min |
| Liaisons orales pour 100 mots, **liste étroite** (donc, du coup, en fait, sauf que, en effet, voilà) | **1,8** (25) | ≥ 1,5 |
| Même comptage, **liste large** (+ par contre, bref, en gros, et là, alors, en revanche) | 2,5 (35) | ≥ 1,5 |
| Nombres dits dans la première minute (quantités) | **4** : 75, 7 900 €, 28, 20 % (les noms « Qwen quatre » et « 5090 » ne sont pas des quantités) | ≤ 5 |
| Plus de 2 nombres dans une phrase ? | Non (la phrase de la 5090 a été coupée en trois) | ≤ 2 |
| Question centrale | 0:29 (« tu achètes ou tu attends ? ») | avant 0:30 |
| Résultat montré / plan en livrables | 0:33 / 0:36 à 1:00 : sûr et rumeur, carte par budget, ta carte, acheter ou pas, + les deux réglages gratuits et la règle d'achat | vers 0:30 |
| Première réponse (début de la partie 1) | 1:00, « Qwen quatre n'est pas sorti » ; ta phrase (`⟦à écrire 1⟧`) vers 1:26, avant 2:00 | avant 1:00 / 2:00 |
| Relance toutes les 60 à 90 s | oui (tableau ci-dessus) | 60 à 90 s |
| « vous » dans la voix | 0 | 0 |
| Noms de chaîne, de créateur, de site de mesures dans la voix | aucun (Alibaba, Amazon, Steam, Strata, Qwen sont des entreprises ou des produits) | aucun |
| Chiffres dans `teleprompteur.txt` | seulement les noms de cartes et de fichiers (RTX 5090, Q4 K M, comme dans les téléprompteurs précédents) ; toutes les quantités sont en lettres | quantités en lettres |
| `(Qx)` du script absents de `sources.md` | 0 (Q5 est dans `sources.md` mais non cité) | 0 |

## À faire avant l'enregistrement

1. **Remplir cinq `⟦à écrire⟧`** (ou garder le repli) : pourquoi tu guettes Qwen 4 (section 1), tes annonces de 3090 d'occasion du jour (section 2, avec captures), l'encart Afrique (section 2), ta carte (section 3), ton choix (section 4).
2. **Refaire les captures de prix** sur les fiches Amazon.fr, LDLC, Materiel.net, avec la date visible, surtout la 5060 Ti 16 Go (694 € contre 1 029,95 à 1 099,95 € : écart non expliqué, `sources.md` Q21 et Q22) et la 5090.
3. **Re-vérifier le 12/11, avant la mise en ligne** : la page des modèles de Qwen sur Hugging Face, la doc `qwen4-max-preview` et le post officiel.
4. **Corriger `fiche.md` et `radar.md`** : « Qwen 4 27B » n'est pas confirmé (Q6). Je n'y ai pas touché.
