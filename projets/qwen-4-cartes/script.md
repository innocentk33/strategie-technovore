# Qwen 4 arrive : les cartes graphiques qui le feront tourner : script V2

> **11/11/2026, V2 après relecture, prête à enregistrer aujourd'hui.** Sortie : **jeu. 12 nov. 2026, 18 h**. Vidéo **calculée** : aucun banc d'essai, des mesures publiées (faits `Qx` de [`sources.md`](sources.md) : ceux qui portent le script ont été rouverts à la source le 11/11 par la relecture ; pas rouverts : Q7, Q8, Q10, Q19, Q23, Q24, et Q18 seulement par l'article de seconde main) et des prix du jour en euros. V1 : [`script-v1.md`](script-v1.md). Critique : [`grill-v1.md`](grill-v1.md). Construit d'après l'[audit du 11/11](../../etudes/audit-2026-11-11.md) (sections 2, 2 bis, 3 et 5).

**Titre** : celui du calendrier est gardé ici (*Qwen 4 arrive : les cartes graphiques qui le feront tourner*). Le grill recommande *Qwen 4 arrive : quelle carte graphique acheter (ou pas) ?* : le « avant que ça monte » de la V1 pousse à acheter vite, alors que la vidéo conclut « n'achète pas pour un nom ». Décision à toi, à reporter dans `README.md` et `calendrier.md`.

## Changements depuis la V1

1. **Le hook est exact.** La V1 disait « même modèle » entre la 5090 (fichier Q4_K_M) et la 5060 Ti (fichier IQ4_XS, plus petit). La V2 en fait l'argument : sur une 5060 Ti, le fichier standard **ne rentre même pas**, il en faut un plus petit, et ça donne vingt-huit. Le hook ouvre sur le prix (7 900 €), raccord avec un titre qui parle d'achat. Le 75 devient « jusqu'à soixante-quinze » (d'autres versions du logiciel donnent 65). Le 28 est maintenant **de première main** (billet de l'utilisateur, 06/10, Q14).
2. **Le statut de « Qwen 4 27B » est corrigé, dans les deux sens.** La V1 disait « rumeur, tirée d'un post sur X », et la fiche disait « confirmé ». Les deux sont faux. Le nom a été **montré à la conférence d'après la presse chinoise** (36Kr, 23/09) et plusieurs sites, comme la version ouverte de Qwen 4. Mais il n'est **écrit nulle part par Alibaba** : ni dans le communiqué, ni dans la doc. La phrase « Alibaba n'a même pas promis que les fichiers seraient publics » saute (Q6).
3. **La section 1 garde sa longueur (environ 2 min à 145 mots/min), mais change d'ordre** : elle commence par du vrai à montrer : la page officielle, sans Qwen 4, et les pages « Qwen4-27B » **vides** créées par des inconnus sur Hugging Face (Q25, nouveau). Flash-Next et le détail des rumeurs sont coupés. Elle se termine sur une relance qui récolte le hook (« le soixante-quinze et le vingt-huit du début, c'est quoi ? »).
4. **Le plan passe de 6 éléments à 3 livrables, plus une révélation et la réponse finale.** Le « Au programme » de la V1, une étiquette, devient « Je te montre… ».
5. **Faux dans la V1, corrigé :**
   - les mesures de deux 5060 Ti (22 → 37 → 66) viennent de **la même personne, avec le même fichier** (Q15). La V1 disait « utilisateurs différents » : la comparaison est en fait propre ;
   - le calcul « 27 milliards × ~4 bits ≈ 15 à 17 Go » est faux (4 bits donnent 13,9 Go). On montre la vraie liste des fichiers : **14 à 18 Go** selon le fichier quatre bits (Q9) ;
   - « seize gigas, non » contredisait la section 2 : seize gigas, c'est **serré**, pas impossible ;
   - l'écart de prix de la 5060 Ti vient du **marchand**, pas du modèle : la même ASUS Prime OC coûte 694 € chez Amazon et 1 099,95 € chez LDLC (Q21, Q22 ; prix du 11/11, recalé à 832,99 € le 12/11, Q30) ;
   - le repli d'occasion de la 3090 dit 800 à 1 200 € (Q23), et non 800 à 1 000 ;
   - « tu auras la réponse quand Alibaba publiera les fichiers » devient « *si* » : rien n'est promis par écrit.
6. **Section 4 sans « fait 1, fait 2, fait 3 ».** Elle devient une chaîne « mais / donc » : attendre ne protège pas des prix, mais acheter pour un nom non plus, sauf qu'on connaît déjà la taille d'un 27 milliards.
7. **Ajouts sourcés :**
   - la 5060 Ti seule passe de 28 à 51 tok/s avec le MTP (même utilisateur, Q14) ;
   - le mode tensor est expérimental (Q15) ;
   - « plus de cinq paires de 5060 Ti pour le prix d'une 5090 » (calcul, Q21 ; devenu « presque cinq paires » le 12/11, Q30).
8. **Tics retirés :**
   - les « du coup » qui ne relient rien (« Du coup, cette fois, le Q4_K_M rentre ») ;
   - le « et en effet » qui ne confirmait rien ;
   - « Bref » en ouverture de paragraphe, « Rien à télécharger, point. », « Sans lui. », les deux « Et le prix ? » ;
   - les triplets « pas de date, pas de taille » et « ta carte, ton budget, et ce que tu trouves ».
9. **Les `⟦à écrire⟧` passent de 5 à 4.** « Ta carte à toi » fusionne avec « ton choix » : le repli de la V1 (« Ma 5080 me suffit ») affirmait un vécu et contredisait ton Qwen lent de *16 Go*. Chaque repli est maintenant écrit en lignes lisibles dans le téléprompteur, pas entre parenthèses.
10. **Les notes `[VISUEL]` sont recalées** : plus de trou entre 0:24 et 0:29, le classement est décrit carte par carte, les cases du plan reprennent les livrables. Aucun « 0 résultat » sur Hugging Face (des pages « Qwen4-27B » existent) ; la recherche « 27B » dans le communiqué attend ta vérification.

**Texte et sous-texte** (inchangés) :
- **Texte** : Qwen 4 n'est pas téléchargeable, et son 27B n'est qu'un nom montré sur scène. On prend Qwen3.8-27B comme étalon. La règle d'achat tient en une phrase : on achète pour la taille d'un fichier, plus la place de la conversation, pas pour un nom.
- **Sous-texte** : le marché ne t'attend pas. La 5060 Ti et la 5080 ont pris plus de 20 % en un mois sans Qwen 4, donc attendre a un coût, et payer une rumeur aussi. On le montre par la 5090 à 7 900 € contre deux 5060 Ti, sans le dire avant la section 4.
- **À ne pas recadrer** : ce n'est pas une vidéo « achète vite ». C'est « voilà ce qui est sûr, voilà ce qui est calculé ».

**Boucles ouvertes** :
1. « Tu achètes maintenant, ou tu attends ? » (0:28) → section 4.
2. « Le fichier ne rentre même pas » (0:08) → section 2, seize gigas.
3. « Deux réglages gratuits qui font presque tripler la vitesse » (0:50) → section 2, trente-deux gigas.
4. Le classement montré à 0:31 → déroulé carte par carte en section 2.
5. Le 75 et le 28 du hook → récoltés à la fin de la section 1 (« c'est quoi ? »).

**Conventions** :
- texte normal = voix off ;
- `[VISUEL]`, `[SON]` = montage, sur fond noir, dans la grammaire de la vidéo d'installation ;
- `(Qx)` = fait de `sources.md`, ne se lit pas ;
- `⟦à écrire⟧` = tes mots, avec un repli prêt à lire ;
- `[À REVÉRIFIER]` = prix à relever en capture le jour de la voix ;
- nombres en lettres pour la lecture ; durée et contrôles en bas de page.

---

## 0. Hook et plan (0:00 – 1:02) · objectif : 75 % à 0:15, 55 % à 1:00

[0:00-0:02 VISUEL : fond noir. Plein écran, la vraie fiche Amazon.fr de la RTX 5090 (ASUS TUF), zoom sur « 7 900 € » ; la date « 11/11/2026 » en bas (Q21) [À REVÉRIFIER]. SON : un coup de basse.]
[0:02-0:04 VISUEL : GIF « Stonks », la flèche qui monte, posé sur le prix.]

Sept mille neuf cents euros : c'est le prix d'une RTX 5090, aujourd'hui.

[0:04-0:07 VISUEL : la vraie page du banc d'essai, ligne « RTX 5090 » surlignée en jaune ; « jusqu'à 75 tok/s » s'écrit avec la voix (Q12).]

Avec elle, Qwen tourne jusqu'à soixante-quinze tokens par seconde.

[0:07-0:09 VISUEL : coupe nette. Fiche de la RTX 5060 Ti 16 Go. La jauge « 16 Go » : le fichier Q4_K_M (16,56 Go) tombe dedans et déborde en rouge (Q9). SON : buzzer.]

Sur une 5060 Ti, son fichier ne rentre même pas.

[0:09-0:12 VISUEL : un fichier plus petit, IQ4_XS (14,35 Go), se glisse en vert ; « 28 tok/s » en orange, sur la capture du billet de l'utilisateur (Q14).]

Faut prendre une version plus compressée, et là, tu tombes à vingt-huit.

[0:12-0:15 VISUEL : la vraie doc d'Alibaba, « available through Token Plan only » surligné en jaune (Q3) ; un tampon rouge « PAS DE FICHIER » se plaque sur le logo Qwen 4. SON : tampon.]

Qwen quatre, lui, n'est qu'en préversion, dans le cloud d'Alibaba : rien à télécharger.

[0:15-0:18 VISUEL : le vrai graphique du comparateur de prix, ligne « RTX 5060 Ti » : « +21,8 % en 30 jours » en rouge (Q20).]
[0:18-0:21 VISUEL : coupe, ligne « RTX 5080 » : « +20,2 % en 30 jours ».]
[0:21-0:24 VISUEL : le GIF Stonks revient, plus gros, puis se fige.]

Sauf que la 5060 Ti et la 5080 ont déjà pris plus de vingt pour cent en un mois.

[0:24-0:28 VISUEL : écran noir, une phrase qui s'écrit mot à mot : « J'ACHÈTE OU J'ATTENDS ? ».]

Du coup, tu achètes maintenant, ou tu attends ?

[0:28-0:34 VISUEL : LE RÉSULTAT. Le classement s'écrit sur fond noir, une ligne par seconde, pendant la question et la phrase du classement, chaque ligne avec la photo de la carte :
- RTX 5090, 32 Go : jusqu'à 75 tok/s, dès 7 900 € ;
- 2 × RTX 5060 Ti, 32 Go : 22 → 66 tok/s, dès 1 670 € ;
- RTX 3090, 24 Go : ~40 tok/s, ≈ 850 € d'occasion (Q27) ;
- RX 7900 XTX, 24 Go : 29 à 41 tok/s, 1 417 € ;
- RTX 5060 Ti, 16 Go : 28 tok/s (fichier serré), dès 833 €.
Petite mention : « Qwen3.8-27B · prix du 11/11/2026 ».]

Voilà le classement, carte par carte, avec les prix du jour.

[0:34-1:02 VISUEL : trois cases qui s'allument avec leur mot : « CE QUI EST SÛR », « TA CARTE SELON TON BUDGET », « LA TIENNE, DÉJÀ ». À 0:50, un compteur « 22 → 37 → 66 tok/s » clignote, deux réglages se cochent. À 0:57, une quatrième case : « ACHETER OU ATTENDRE ? », avec un cadenas.]

Je te montre ce qui est sûr sur Qwen quatre, et ce qui ne l'est pas. La carte pour ton budget, en euros. Et ce que fait déjà celle que t'as. En route, il y a deux réglages gratuits qui font presque tripler la vitesse d'une paire de cartes. Et à la fin, je réponds à ta question en une phrase : acheter, ou attendre.

---

## 1. Qwen 4 : ce qui est sûr, ce qui ne l'est pas (1:02 – 3:09)

[VISUEL : la vraie page Hugging Face de l'organisation Qwen, modèles triés par date : le plus récent est un modèle d'image ; aucun « Qwen4 ». Date à l'écran (Q4). À refaire le 12/11 au matin.]

Réponse courte : non, Qwen quatre n'est pas téléchargeable. Sur la page officielle de Qwen, à l'heure où j'enregistre, il n'y en a aucun. (Q4)

[VISUEL : la recherche « Qwen4-27B » sur Hugging Face : trois pages d'inconnus avec ce nom. Zoom sur l'une : « No model weights are available in this repository », et la liste des fichiers : un README, rien d'autre. Noms des comptes floutés (Q25).]

Par contre, si tu tapes « Qwen4-27B » sur Hugging Face, tu vas tomber sur des pages qui portent ce nom. Ouvre-les : elles sont vides. En fait, des gens réservent juste la place pour le jour où il sortira. Donc si quelqu'un te propose un Qwen quatre à télécharger aujourd'hui, méfie-toi. (Q25)

[VISUEL : la fiche Hugging Face de Qwen3.8-Flash-Next, « This experimental preview of the architecture that will underpin Qwen4 » surligné ; puis son tableau de code, deux colonnes seulement : Flash-Next contre Qwen3.8-27B (SWE-bench Pro 62,5 contre 61,7 ; SWE-bench Multilingual 81,0 contre 73,8), avec la mention « chiffres de Qwen » (Q2, Q28).]

Moi, je guette Qwen quatre pour une raison simple. En août, Qwen a sorti un avant-goût, Qwen trois point huit Flash Next, qui montre l'architecture de Qwen quatre. Et en code, d'après les tests de Qwen, il bat déjà le vingt-sept B. Du coup, j'attends beaucoup de Qwen quatre, d'autant que Qwen, c'est une des familles les plus recommandées pour coder en local. (Q2, Q28)

[VISUEL : deux cartes vertes « SÛR » s'empilent, chacune avec la vraie capture et la phrase surlignée en jaune : le communiqué du 22/09 (« Qwen 4, is currently in training »), puis la doc de Qwen4-Max-Preview (« 11/11 – 25/11 », « Token Plan only »), puis le vrai post de @Alibaba_Qwen sur X, la ligne sur l'accès anticipé (QwenWork, Qoder, Qwen APP, QwenStudio) surlignée (Q1, Q3, Q26).]

Ce qu'Alibaba a écrit noir sur blanc, c'est peu. Le vingt-deux septembre, son communiqué dit que Qwen quatre est « en entraînement », sans date ni taille. Et depuis aujourd'hui, une préversion, Qwen quatre Max, est ouverte jusqu'au vingt-cinq novembre. Mais seulement dans le cloud : par l'abonnement d'Alibaba, ou en accès anticipé dans ses applis, comme l'appli Qwen. Tu peux l'essayer, mais pas le télécharger. Donc là non plus, pas de fichier. (Q1, Q3, Q26)

[VISUEL : une troisième carte, orange, « MONTRÉ, PAS ÉCRIT » : le titre de l'article chinois du 23/09, la phrase « 开源侧优先安排Qwen4-27B » surlignée, sa traduction en dessous (« côté open source, priorité à Qwen4-27B »). Puis le communiqué d'Alibaba, la phrase « Qwen 4, is currently in training » (Q1, Q6). ⟦à vérifier : avant de montrer une recherche « 27B » dans le communiqué, fais-la toi-même dans ton navigateur ; la relecture l'a faite par un outil de résumé. Sinon, ne montre que la phrase.⟧]

Et le Qwen quatre de vingt-sept milliards, celui qu'on pourrait faire tourner chez soi ? D'après la presse chinoise, il a été montré à la conférence, comme la version ouverte de Qwen quatre. Sauf qu'Alibaba ne l'a écrit nulle part : ni dans son communiqué, ni dans sa documentation. On n'en connaît ni la taille ni la date. Donc pour l'instant, c'est un nom annoncé, et personne n'a vu son fichier. (Q6)

[VISUEL : tampons « RUMEUR » qui claquent sur deux captures floutées : « ~15 Go » et « la semaine prochaine » (Q7, Q8).]

Pour le reste, voilà ce qu'on raconte : une quinzaine de gigas, estimés à partir du code d'un logiciel, et une sortie « la semaine prochaine », rapportée de seconde main. (Q7, Q8)

[VISUEL : retour au classement du hook ; « 75 » et « 28 » se rallument. Puis l'icône de Qwen3.8-27B sur la vraie page Hugging Face, étiquette « étalon » (Q10).]

Mais alors, le soixante-quinze et le vingt-huit du début, c'est quoi ? C'est Qwen trois point huit, vingt-sept milliards : le Qwen d'aujourd'hui, celui que tu peux télécharger.

[VISUEL : un SSD qui se remplit ; une case « ??? Go » à côté d'une jaquette de jeu sans nom ; à côté, la jaquette du jeu précédent avec son poids.]

C'est comme libérer de la place sur ton SSD pour un jeu dont personne ne connaît le poids : tu prends le précédent comme étalon. Si Qwen quatre garde cette taille, ces chiffres tiendront. Sinon, je refais les comptes. (Q10)

---

## 2. La carte pour chaque budget (3:09 – 7:14)

[VISUEL : la vraie liste des fichiers de Qwen3.8-27B sur Hugging Face, la ligne « Q4_K_M · 16,56 GB » entourée (Q9). Puis la jauge vide « ta carte ».]

Son fichier le plus courant, le Q quatre K M, pèse seize gigas et demi. Et pour que ça tourne vite, il doit rentrer dans ta carte, avec de la place en plus pour la conversation. Sinon, une partie déborde dans la RAM, et là, ça rame. (Q9)

### Seize gigas : la RTX 5060 Ti

[VISUEL : fiche de la 5060 Ti, étiquette « 16 Go ». La jauge : Q4_K_M (16,56) déborde en rouge, IQ4_XS (14,35) se glisse en vert ; il reste une fine bande « conversation : < 2 Go » (Q9, Q11). Capture du billet de l'utilisateur, « 28.0 tok/s » surligné (Q14).]

On commence par seize gigas, avec la RTX 5060 Ti. Comme tu l'as vu, le Q quatre K M ne rentre pas. Du coup, on prend un fichier plus serré, de quatorze gigas, et un utilisateur mesure vingt-huit tokens par seconde. Pour discuter, c'est très correct. Par contre, il te reste moins de deux gigas pour la conversation, donc pour un agent de code, qui lit des fichiers entiers, c'est juste. (Q11, Q14)

[VISUEL : carte YouTube, « 16 Go de VRAM suffisent » (sortie lundi 9 nov.), 3 secondes.]

J'ai tout détaillé lundi, dans la vidéo sur les seize gigas.

[VISUEL : deux fiches côte à côte, la même ASUS Prime OC 16 Go : Amazon.fr « 832,99 € » (ta capture du 12/11, Q30), LDLC « 1 099,95 € », date du jour sur chacune (Q22, Q30) [LDLC À REVÉRIFIER]. Un meme de visage choqué entre les deux.]

Côté prix, regarde bien : la même carte, de la même marque, coûte huit cent trente-trois euros chez Amazon, et mille cent chez LDLC. Plus de deux cent cinquante euros d’écart pour la même boîte. Donc compare avant de payer : pour essayer, elle suffit, pour travailler, c'est serré. (Q21, Q22)

[VISUEL : ta capture Leboncoin de la RX 6800 XT Red Dragon, « 16 Go » et « 280 € » zoomés, date du 11/11 (Q27) ; petit tampon « vitesse : pas de mesure trouvée ».]

Et en occasion, il y a bien moins cher : une Radeon RX 6800 XT, seize gigas elle aussi, autour de deux cent quatre-vingts euros sur Leboncoin. Sauf que je n'ai trouvé aucune mesure de ce modèle sur cette carte, donc je ne te donne pas de vitesse. (Q27)

### Vingt-quatre gigas : la RTX 3090, ou la RX 7900 XTX

[VISUEL : fiche de la 3090, « 24 Go ». La jauge : Q4_K_M en vert, une marge verte « ~8 Go » (Q11). Le compteur « 40 tok/s », puis « 34 » quand une barre « conversation longue » s'allonge (Q13).]

Palier suivant : vingt-quatre gigas, avec la RTX 3090. Cette fois, le Q quatre K M rentre, et il reste environ huit gigas pour la conversation. Résultat, autour de quarante tokens par seconde, et encore trente-quatre quand la conversation devient très longue. (Q11, Q13)

[VISUEL : le mot « MTP » s'écrit ; petite animation : trois mots devinés d'avance, deux validés en vert. Puis « 40 → 72 tok/s », légende « sur du code, une mesure » (Q13). GIF de réaction « ça monte ».]

Et là, il y a un réglage dont tu vas entendre parler : le MTP. En gros, le modèle devine plusieurs mots d'avance, puis il vérifie. Sur une 3090, un utilisateur passe de quarante à plus de soixante-dix, sur du code. Le gain baisse quand la conversation s'allonge, mais il est gratuit. (Q13)

[VISUEL : fiche Amazon.fr de la 3090 neuve, « 2 990 € » (Q21) ; puis tes captures d'annonces d'occasion, prix zoomés, avec la date.]

Neuve, la 3090 est encore affichée à près de trois mille euros chez Amazon. Évidemment, personne ne l'achète neuve : son vrai prix, c'est celui de l'occasion. (Q21)

[VISUEL : ta capture de l'annonce Leboncoin de la 3090, « 850 € » zoomé, date du 11/11 (Q27).]

Aujourd'hui, sur Leboncoin, j'en vois une à huit cent cinquante euros. Moins d'un tiers du prix neuf. Par contre, en occasion, vérifie qu'elle tourne avant de payer. (Q27)

[VISUEL : fiche de la RX 7900 XTX, « 1 417 € » (Q21) [À REVÉRIFIER] ; la barre « 29 → 41 tok/s » qui hésite, avec trois petites étiquettes de logiciels (Q16).]

Côté AMD, la RX 7900 XTX a aussi vingt-quatre gigas, pour un peu plus de mille quatre cents euros neuve. Sauf que ses mesures vont de vingt-neuf à quarante et un tokens par seconde, selon le logiciel et le système. Donc avec elle, c'est moins prévisible. (Q16, Q21)

### Trente-deux gigas : deux 5060 Ti, ou une 5090

[VISUEL : deux 5060 Ti côte à côte, étiquette « 2 × 16 = 32 Go ». La vraie table GitHub, trois lignes du même utilisateur surlignées une par une, avec la voix : « -sm layer : 22,1 », « -sm tensor : 37,1 », « + MTP : 65,9 » (Q15).]

Dernier palier : trente-deux gigas. Première option, deux 5060 Ti. Et c'est là que se cachent les deux réglages gratuits. Par défaut, le logiciel coupe le modèle en deux, couche par couche, et une carte attend l'autre : vingt-deux tokens par seconde. Active le tensor split, et les deux cartes calculent en même temps : trente-sept. Ajoute le MTP : soixante-six. Presque le triple, sans dépenser un euro. (Q15)

[VISUEL : petit tampon « même personne, même fichier » sur la table ; puis « tensor : expérimental » en jaune, 2 secondes (Q15).]

Et ce sont les mesures d'une même personne, avec le même fichier : la comparaison est propre. Attention quand même, le tensor split est encore marqué expérimental dans le logiciel. (Q15)

[VISUEL : le calcul s'écrit : « 2 × 833 € ≈ 1 670 € » (Q30).]

Les deux cartes, chez Amazon : à partir de mille six cent soixante-dix euros environ. (Q30)

[VISUEL : fiche de la RTX 5090, « 7 900 € », puis le graphique du comparateur : « médiane 9 300 € », « +89,8 % en 3 mois » en rouge (Q20, Q21). Le GIF Stonks revient, démesuré.]

Deuxième option : une seule RTX 5090. Jusqu'à soixante-quinze tokens par seconde, sans même le MTP. Donc à réglages égaux, elle reste devant. Sauf qu'en stock, elle démarre à sept mille neuf cents euros, et son prix médian a presque doublé en trois mois. (Q12, Q20, Q21)

[VISUEL : quatre paires de 5060 Ti et presque une cinquième qui s'empilent face à une seule 5090 ; légende « 7 900 € ÷ 1 666 € ≈ 4,7 » (Q30).]

Du coup, pour le prix d'une 5090, tu t'offres presque cinq paires de 5060 Ti. Bon, t'en as pas besoin de cinq. Mais je fais une vidéo entière sur les trente-deux gigas le lundi vingt-trois novembre. (Q21)

[VISUEL : carte YouTube, vidéo « 32 Go de VRAM » (lun. 23 nov.), 3 secondes.]

Et si t'es pas en France, je garde les prix en euros : fais la conversion dans ta monnaie. Et à la fin, je te demande combien ça coûte chez toi.

---

## 3. Et si t'as déjà une carte ? (7:14 – 8:28)

[VISUEL : retour sur la jauge vide. Trois cartes de taille différente (16, 12 et 8 Go) se glissent dedans, l'une après l'autre.]

Et si t'as déjà une carte ? Alors, avant d'acheter quoi que ce soit, regarde juste si le fichier rentre.

[VISUEL : la 5060 Ti seule, « 28 → 51 tok/s », légende « avec MTP, conversation courte (8 K) » ; puis la 5080, « 53 → 101 tok/s », légende « une seule mesure » (Q14, Q17).]

Avec seize gigas, ça passe avec le fichier serré, on l'a vu. Et avec le MTP, l'utilisateur de la 5060 Ti passe de vingt-huit à cinquante et un, sur une conversation courte. Sur une 5080, quelqu'un a même mesuré cent un tokens par seconde, mais avec un fichier trois bits, moins précis, et c'est une seule mesure. (Q14, Q17)

[VISUEL : « 12 Go » : une jauge où le fichier déborde, une flèche vers « RAM » ; « 5 à 7 tok/s » en rouge (Q18). Puis le vrai tableau Steam d'octobre : 8 Go 26,9 %, 12 Go 12,9 % (Q19).]

Avec douze gigas, en revanche, ce modèle ne rentre pas, même en quatre bits. Une partie part dans la RAM, du coup, sur une 3060, on tombe entre cinq et sept tokens par seconde. Avec huit gigas, c'est pire. Et c'est le cas de beaucoup de monde : sur Steam, en octobre, plus d'un joueur sur quatre a huit gigas, et environ un sur huit en a douze. (Q18, Q19)

[VISUEL : tes deux captures Leboncoin de 3060 12 Go, « 280 € » et « 320 € », à côté de celle de la RX 6800 XT 16 Go, « 280 € » (Q27).]

Et le piège, c'est le prix : une 3060 de douze gigas d'occasion, je la vois entre deux cent quatre-vingts et trois cent vingt euros sur Leboncoin. À peu près le prix de la Radeon de seize gigas. Donc pour ce genre de modèle, à prix égal, prends les seize. (Q27)

Donc si c'est ton cas, Qwen quatre ne va sans doute rien changer : rien ne dit qu'il sera plus petit, et pour un modèle de cette taille, il te faudra une carte des paliers d'avant.

---

## 4. Acheter ou attendre ? (8:28 – 9:58)

[VISUEL : fond noir, « J'ACHÈTE OU J'ATTENDS ? » revient, le cadenas du plan s'ouvre.]

Alors, tu achètes maintenant, ou tu attends ?

[VISUEL : la ligne « RTX 5080 : +20,2 % en 30 jours » du comparateur (Q20), puis la phrase « pénurie de mémoire » surlignée dans la capture de la vidéo américaine, source en description (Q24).]

D'abord, attendre Qwen quatre ne te protège pas des prix : ils ont commencé à monter sans lui. La cause avancée, d'après une chaîne américaine, c'est la pénurie de mémoire. Et personne ne sait quand ça redescendra. (Q20, Q24)

[VISUEL : le logo Qwen 4, une case « fichier : ??? Go », la carte orange « MONTRÉ, PAS ÉCRIT » revient (Q6).]

Mais acheter pour Qwen quatre, c'est acheter pour un fichier que personne n'a vu. En fait, le vingt-sept milliards a été montré à une conférence, rien de plus. (Q6)

[VISUEL : la vraie liste des fichiers quatre bits de Qwen3.8-27B : « IQ4_XS 14,35 · Q4_K_S 15,36 · Q4_K_M 16,56 · Q4_K_XL 17,66 » ; à côté, la jauge 16 Go remplie à ras bord, la jauge 24 Go avec de la marge (Q9, Q11).]

Sauf qu'on sait déjà une chose : un modèle de vingt-sept milliards, en quatre bits, pèse entre quatorze et dix-huit gigas selon le fichier. On vient de le voir avec Qwen trois point huit. Donc si Qwen quatre garde cette taille, vingt-quatre gigas gardent de la marge, et seize gigas restent serrés. (Q9, Q11)

[VISUEL : fond noir, une seule phrase qui s'écrit mot par mot, en grand : « N'ACHÈTE PAS POUR UN NOM. ACHÈTE POUR LA TAILLE D'UN FICHIER. »]

Voilà la règle, en une phrase : n'achète pas pour un nom, achète pour la taille d'un fichier, plus la place de la conversation. Aujourd'hui, ça veut dire vingt-quatre gigas, ou deux fois seize avec le bon réglage.

Et si t'as déjà seize gigas ou plus, ne change rien pour l'instant : attends de voir le vrai fichier. Le jour où il sort, je refais ce classement avec les vrais chiffres.

[VISUEL : la fiche du Coder sur Hugging Face, « Qwen3.8-Flash-Next » surligné dans son nom ; puis la ligne de la doc de Strata « a 32 GB PC with a 12 to 16 GB GPU runs the Coder » (Q29).]

Moi, je vais attendre. Parce que des projets comme Strata font déjà tourner une version compressée de Flash Next, l'avant-goût de Qwen quatre, avec seize gigas de VRAM et trente-deux de RAM. Donc si Qwen quatre garde cette architecture, peut-être que mes seize gigas suffiront. (Q29)

---

## 5. Fin (9:58 – 10:20)

[VISUEL : la jauge et la règle en bas. Puis la carte YouTube « 16 Go de VRAM suffisent ».]

Dis-moi en commentaire quelle carte t'as, et combien elle coûte vraiment chez toi : je compile vos réponses, surtout pour ceux qui n'ont pas accès aux prix français. Et si t'as seize gigas, la vidéo de lundi te dit quel fichier prendre.

[VISUEL : écran de fin, 20 s : à gauche *16 Go de VRAM suffisent* (lun. 9 nov.), à droite la prochaine vidéo IA ; bouton « S'abonner ».]

Lundi seize novembre, je teste Strata sur ma 5080, en vrai. Et le vingt-trois, les trente-deux gigas de VRAM, en détail.

---

## Relances d'attention (timecodes à 145 mots/min, replis des `⟦à écrire⟧` compris ; à ton débit réel, environ 180 mots/min d'après les sous-titres de *16 Go*, retire à peu près un cinquième)

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Prix + meme | 7 900 €, Stonks |
| 0:05 | Résultat | jusqu'à 75 tok/s |
| 0:08 | Contraste | sur une 5060 Ti, le fichier ne rentre même pas |
| 0:13 | Retournement | Qwen 4 : pas de fichier |
| 0:20 | Enjeu | +20 % en un mois |
| 0:28 | Question centrale | « Tu achètes ou tu attends ? » |
| 0:31 | Résultat | le classement s'écrit |
| 0:50 | Boucle ouverte | deux réglages qui triplent presque la vitesse |
| 1:12 | Démo du vrai | les pages « Qwen4-27B » vides |
| 2:02 | Retournement | le 27B : montré, pas écrit |
| 2:43 | Récolte | « le 75 et le 28 du début, c'est quoi ? » |
| 3:28 | Récolte | le Q4_K_M ne rentre pas dans 16 Go |
| 4:02 | Surprise | la même carte, 400 € d'écart |
| 4:38 | Révélation | le MTP, 40 → 72 |
| 5:40 | Révélation | les deux réglages, 22 → 37 → 66 |
| 6:41 | Contraste + blague | presque cinq paires pour le prix d'une 5090 |
| 7:14 | Promesse tenue | ta carte actuelle, 28 → 51 |
| 7:45 | Retournement | douze gigas : ça ne rentre pas, cinq à sept tok/s |
| 8:28 | Question récoltée | « acheter ou attendre ? » |
| 9:19 | Récolte | la règle en une phrase |

Les relances tombent toutes les 30 à 62 s : le plus long trou est 4:38 → 5:40 (la 3090, son prix d'occasion, la 7900 XTX), puis 5:40 → 6:41. Ce n'est pas un retournement toutes les 30 s : la section 2 tient par ses chiffres et ses vraies images. Si la voix dépasse 10 min 30, coupe d'abord le paragraphe AMD (environ 20 s), puis la phrase sur la 5080 en section 3.

## Notes de montage (grammaire de la vidéo d'installation)

- **Fond noir, jamais le bleu ardoise de 16 Go.** Vraies images partout :
  - la table GitHub et le billet de l'utilisateur de la 5060 Ti ;
  - les fiches Amazon.fr et LDLC, avec leur prix et la date visibles ;
  - le communiqué d'Alibaba et la doc, la phrase surlignée en jaune ;
  - la page Hugging Face de Qwen, et une page « Qwen4-27B » vide ;
  - la liste des fichiers de Qwen3.8-27B.
- **Un seul schéma, la jauge « ta carte »**, en plans courts entre de vraies images.
- **De 0 à 30 s, un plan nouveau toutes les 1 à 3 s.**
  - Le GIF Stonks à 0:02, avant 0:15.
  - Les mots qui comptent s'écrivent avec la voix : « 7 900 € », « 75 tok/s », « 28 », « PAS DE FICHIER », « J'ACHÈTE OU J'ATTENDS ? ».
- **Les trois couleurs de statut**, à l'écran à chaque fois, c'est la promesse du plan :
  - « SÛR » en vert ;
  - « MONTRÉ, PAS ÉCRIT » en orange ;
  - « RUMEUR » en rouge.
- **Au moins une image réelle toutes les 15 s** entre les schémas.
- **Chaque prix à l'écran porte sa date (« 11/11/2026 »).** Refais les captures le jour de la voix et la veille de la sortie.
- **Pages Hugging Face d'inconnus** : floute les noms des comptes ; la voix ne les nomme pas.
- **Avant la mise en ligne (jeu. 12/11, matin)** : rouvre la page des modèles de Qwen sur Hugging Face et la doc de `qwen4-max-preview`. Si Qwen 4 est sorti entre-temps, la section 1 et la section 4 changent (vraies tailles de fichier) : préviens-moi.

## Faits utilisés

| Dit dans le script | Faits |
|---|---|
| Qwen 4 « en entraînement », 22/09, sans date ni taille | Q1 |
| Préversion de Qwen4-Max du 11/11 au 25/11, abonnement seulement | Q3 |
| Aucun Qwen 4 sur la page officielle de Qwen au 11/11 | Q4 |
| Le 27B : montré à la conférence d'après la presse, écrit nulle part par Alibaba | Q6 |
| Pages « Qwen4-27B » vides, créées par des inconnus | Q25 |
| Une quinzaine de gigas (code d'un logiciel), « la semaine prochaine » (seconde main) | Q7, Q8 |
| Qwen3.8-27B : étalon ; fichiers de 14,35 à 17,66 Go en quatre bits | Q9, Q10, Q11 |
| 5090 : jusqu'à 75 tok/s, sans MTP ; dès 7 900 € en stock, médiane presque doublée en 3 mois | Q12, Q20, Q21 |
| 5060 Ti : 28 tok/s, 51 avec MTP ; 832,99 € (Amazon, 12/11) contre 1 099,95 € (LDLC, 11/11), même carte | Q14, Q22, Q30 |
| 3090 : 40 puis 34 tok/s ; plus de 70 avec MTP sur du code ; neuve 2 990 € ; occasion 800-1 200 € fin octobre | Q13, Q21, Q23 |
| 7900 XTX : 29 à 41 tok/s, 1 417 € | Q16, Q21 |
| Deux 5060 Ti : 22, 37, 66 tok/s, même personne, même fichier ; tensor expérimental | Q15 |
| Hausses de 20 % en 30 jours, cause avancée : la mémoire | Q20, Q24 |
| 5080 : 101 tok/s avec un fichier trois bits, une mesure | Q17 |
| 3060 12 Go : 5 à 7 tok/s ; Steam 8 et 12 Go | Q18, Q19 |

**Interdits respectés** :
- aucun nom de chaîne, de site de mesures, de compte ni de créateur dans la voix (« un utilisateur », « une chaîne américaine », « la presse chinoise ») ;
- aucun « vous » ;
- aucune anecdote ni aucun test attribués à l'auteur ;
- aucune vitesse de Qwen 4 ;
- les prix d'occasion jamais présentés comme prix du jour ;
- « Qwen quatre de vingt-sept milliards » toujours dit comme un nom annoncé, sans fichier.

## Contrôles (11/11/2026, comptés par script sur la voix seule, sans `[…]`, `(Qx)` ni `⟦…⟧`)

Voir [`grill-v1.md`](grill-v1.md), section « Contrôles de la V2 », pour le détail des comptages.

| Mesure | V2 | Cible |
|---|---|---|
| Mots dits (sans les `⟦à écrire⟧`) | **1 390** | 1 300 à 1 600 |
| Tes 3 passages du 12/11 (remplacent les replis de 104 mots) | 139 mots, soit environ 15 s de plus à 145 mots/min | |
| **Durée** | **environ 10 min 20 à 145 mots/min** avec les replis ; **environ 8 min 20 à ton débit de *16 Go*** (180 mots/min, 2 105 mots en 11:38) ; un encart Afrique complet ajoute 15 à 20 s | 9 à 11 min à 145 |
| Mots jusqu'à la question centrale | **76** (31 s à 145, 25 s à ton débit) | ≤ 75 |
| Liaisons orales pour 100 mots, liste étroite (donc, du coup, en fait, sauf que, en effet, voilà) | **1,65** (23) | ≥ 1,5 |
| Liste du skill (+ mais, et là, en gros, résultat, par contre, en revanche, alors) | **2,8** (39) | ≥ 1,5 |
| Nombres dits dans la première minute | **5** : 7 900, 75, 28, 20 %, deux réglages (« Qwen quatre », « 5060 Ti », « 5090 » sont des noms) | ≤ 5 |
| Plus de 2 nombres dans une phrase ? | Non | ≤ 2 |
| Question centrale | 0:28 | avant 0:30 |
| Résultat montré / plan en livrables | 0:31 / 0:34 à 1:02 : sûr ou pas, ta carte par budget, la tienne déjà, + les deux réglages + la réponse finale | vers 0:30 |
| Première réponse | 1:02 à 145 (0:50 à ton débit), « non, Qwen quatre n'est pas téléchargeable » | vers 1:00 |
| Ta phrase perso (pourquoi tu guettes Qwen 4, écrite le 12/11) | vers 1:32 | avant 2:00 |
| « vous » dans la voix | 0 | 0 |

## À faire avant l'enregistrement (aujourd'hui)

1. ~~**Les `⟦à écrire⟧`**~~ : **tous écrits le 12/11** avec tes réponses.
   - Pourquoi tu guettes Qwen 4 (section 1) : Flash-Next, l'avant-goût de Qwen 4, bat déjà le 27B en code (Q28). **Nuancé** : « le modèle le plus apprécié pour coder en local » devient « une des familles les plus recommandées », car aucun classement ne dit « le plus ».
   - L'encart Afrique (section 2) : prix en euros, chacun convertit ; la demande de prix reste à la fin.
   - Ta décision (section 4) : tu attends. **Précisé** : Strata ne compresse pas le modèle lui-même ; il fait tourner le Coder, une version de Flash-Next compressée par ISTA-DASLab (moitié des experts, 1 bit), avec 32 Go de RAM (Q29).
   - ~~Tes annonces de 3090 d'occasion du jour~~ : fait le 11/11 (850 €, Q27), avec la RX 6800 XT et les 3060.
2. **Captures de prix** (12/11 : la 5090 à 7 900,15 € et la 5060 Ti à 832,99 € sur Amazon.fr sont faites, Q30 ; restent LDLC, la 3090 et la 7900 XTX), date visible : la 5090 sur Amazon.fr, l'ASUS Prime OC 5060 Ti 16 Go sur Amazon.fr **et** sur LDLC, la 3090 et la 7900 XTX sur Amazon.fr. Si l'écart Amazon / LDLC a disparu, remplace la phrase par « de sept cents à mille cent euros selon le marchand ».
3. **Le 12/11 au matin**, revérifie la page des modèles de Qwen sur Hugging Face et la doc `qwen4-max-preview`.
4. **Choisis le titre** (voir l'en-tête) et reporte-le dans `README.md` et `calendrier.md`.
