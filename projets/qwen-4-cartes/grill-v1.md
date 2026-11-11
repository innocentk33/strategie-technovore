# Grill de la V1 : « Qwen 4 arrive » (11/11/2026)

> Script critiqué : la V1 du 11/11, copiée à l'identique dans [`script-v1.md`](script-v1.md). Les passages cités viennent de ce fichier. La V2 corrigée est dans [`script.md`](script.md).
> Faits : [`sources.md`](sources.md), Q1 à Q25. Ceux qui portent le script ont été rouverts à la source le 11/11 (« revérifié le 11/11 par la relecture ») : Q1 à Q4, Q6, Q9, Q12 à Q17, Q20 à Q22, et Q25 (nouveau). **Pas rouverts** : Q7, Q8 (rumeurs, dites comme telles), Q10, Q19 (vérifié le 07/11), Q23 (relevé daté du 24/10), Q24 (un avis) ; Q18 seulement par l'article de seconde main.
> Méthode : skill `youtube-script-grill`, mode B, variante storytelling. Grilles appliquées : les règles de `.claude/rules/script.md` et l'[audit du 11/11](../../etudes/audit-2026-11-11.md), sections 2, 2 bis, 3 et 5.
> Débits : 145 mots/min, la référence des scripts, et **180 mots/min**, ton débit réel, mesuré sur les sous-titres de *16 Go* (2 105 mots en 11:38).

## Verdict

**V1 : 6,5/10. V2 : 8/10 (estimation).**

**Ce qui marche.** La V1 a la bonne charpente : la réponse d'abord, « sûr / on raconte », trois paliers de VRAM avec des prix du jour, une règle d'achat en une phrase. Le rédacteur a aussi eu le bon réflexe de corriger le radar, et il signale lui-même ses points faibles.

**Le plus gros problème : les faits qui portent la vidéo.**
- Le hook dit « même modèle » entre deux fichiers différents.
- Le statut du 27B est faux, dans l'autre sens que le radar.
- La prudence sur les deux 5060 Ti est fausse (c'est le même utilisateur).
- Le calcul « 27 milliards × 4 bits ≈ 15 à 17 Go » est faux.

**Le potentiel.** Une fois ces faits remis d'aplomb, le hook devient plus fort : « son fichier ne rentre même pas » est le sujet de la vidéo.

## Test des 30 secondes (V1)

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-2 s | > « Soixante-quinze tokens par seconde. » | 🟠 Un chiffre fort, mais en unité d'initié et sans sujet. Le titre parle d'acheter une carte : le prix accroche mieux en premier. |
| 2-7 s | > « C'est la vitesse de Qwen sur une RTX 5090, affichée à sept mille neuf cents euros. » | 🟢 Confirme le clic : une carte, un prix. Deux nombres en 5 s, c'est la limite. |
| 7-9 s | > « Sur une 5060 Ti, vingt-huit. » | 🟢 Le contraste, sec, bien placé. |
| 9-11 s | > « Même modèle. » | 🔴 **Inexact.** Même modèle (Qwen3.8-27B), mais pas le même fichier : Q4_K_M sur la 5090, IQ4_XS sur la 5060 Ti (Q12, Q14). Un commentaire averti le relève, et tout le reste perd du crédit. |
| 11-15 s | > « Et c'est le Qwen d'aujourd'hui, pas Qwen quatre. » | 🟠 Honnête et nécessaire. Mais la tournure « X, pas Y » arrive dans les 15 s, et elle désamorce les chiffres qu'on vient de donner. |
| 15-20 s | > « Sauf que Qwen quatre arrive, en préversion, dans le cloud d'Alibaba : rien à télécharger. » | 🟢 Confirme le clic (« Qwen 4 arrive »). Le « sauf que » ne retourne pourtant rien : la phrase d'avant disait déjà « pas Qwen quatre ». |
| 20-27 s | > « Et la 5060 Ti et la 5080, elles, ont déjà pris plus de vingt pour cent en un mois. Sans lui. » | 🟢 Monte l'enjeu, avec la preuve à l'écran. « Sans lui. » est un fragment dramatique : l'information est déjà dans « déjà ». |
| 27-32 s | > « Du coup, tu achètes ta carte maintenant, ou tu attends ? » | 🟢 Une seule question centrale, en mots simples. Elle tombe à 0:32 à 145 mots/min (0:26 à ton débit). |
| Pont | > « Voilà le classement, avec les prix d'aujourd'hui. Au programme : […] Plus deux réglages gratuits […] Et à la fin, la règle d'achat, en une phrase. » | 🟠 Le résultat est montré avant le plan, c'est bien. Mais le plan a **six éléments**, et « Au programme » est une étiquette. |

**Budget V1** : 77 mots jusqu'à la question, soit 32 s à 145 mots/min et 26 s à 180. Jusqu'à la fin du plan, 144 mots, soit 60 s à 145.

**À couper** :
- « Même modèle. » : faux ;
- « Sans lui. » ;
- « Au programme » ;
- deux éléments du plan.

**Réécriture appliquée (76 mots, 31 s à 145, 25 s à ton débit)** :

> Sept mille neuf cents euros : c'est le prix d'une RTX 5090, aujourd'hui. Avec elle, Qwen tourne jusqu'à soixante-quinze tokens par seconde. Sur une 5060 Ti, son fichier ne rentre même pas. Avec un plus petit : vingt-huit. Qwen quatre, lui, n'est qu'en préversion, dans le cloud d'Alibaba : rien à télécharger. Sauf que la 5060 Ti et la 5080 ont déjà pris plus de vingt pour cent en un mois. Du coup, tu achètes maintenant, ou tu attends ?

Ce que fait cette réécriture :
- **Elle ouvre sur le prix, avec le GIF Stonks.** C'est raccord avec un titre qui parle d'achat.
- **Le « même modèle » devient l'argument.** La 5060 Ti doit prendre un fichier plus petit, et elle va quand même moins vite. Le spectateur apprend la règle de la vidéo avant 0:12.
- **« Jusqu'à soixante-quinze ».** Les mêmes bancs donnent aussi 65, et 43 avec la version la plus récente du logiciel (Q12).
- **Toujours 4 nombres** : 7 900, 75, 28, 20 %.

## Tableau de bord

| Axe | V1 | V2 | En une phrase |
|---|---|---|---|
| 1. Promesse | 🟠 | 🟢 | V1 : le titre recommandé (« avant que ça monte ») pousse à acheter, la fin dit « n'achète pas pour un nom ». |
| 2. Alignement | 🟢 | 🟢 | Aucune vente, des prix datés, l'Afrique invitée à donner ses prix. |
| 3. Problème profond | 🟠 | 🟠 | La peur de payer trop cher, ou trop tôt, est là, mais jamais incarnée : seul ton vécu (`⟦à écrire 1⟧` et `⟦4⟧`) peut le faire. |
| 4. Public & complexité | 🟠 | 🟢 | V1 : Q4_K_M, IQ4_XS, tensor split, MTP, trois bits, sans échelle. V2 : le « fichier qui ne rentre pas » est planté dès 0:08, et le MTP expliqué en une phrase. |
| 5. Valeur & originalité | 🟢 | 🟢 | Prix en euros, même carte à 400 € d'écart, deux réglages gratuits ×3, pages Qwen4-27B vides : personne en français. |
| 6. Structure & transformation | 🟢 | 🟢 | Sûr → paliers → ta carte → verdict : chaque section répond à la question du hook. |
| 7. Histoire | 🟠 | 🟠 | C'est une enquête d'achat sans personnage. Normal pour une vidéo calculée ; tes `⟦à écrire⟧` donnent le seul « je ». |
| 8. Mais / donc | 🟠 | 🟢 | V1 : la section 4 aligne « Premier fait, Deuxième fait, Troisième fait ». V2 : une chaîne « d'abord / mais / sauf que / donc ». |
| 9. Engagement actif | 🟠 | 🟢 | V1 : tout est dit. V2 : « Ouvre-les : elles sont vides », « regarde bien », « le 75 et le 28 du début, c'est quoi ? ». |
| 10. Oralité & liaisons | 🟠 | 🟢 | V1 : 1,8 pour 100 mots sur le papier, environ 1,4 une fois retirées les liaisons qui ne relient rien. V2 : 1,65 (liste étroite), 2,8 (liste du skill), sans liaison creuse relevée. |
| 11. Tics d'IA | 🟠 | 🟢 | Voir « Tics à supprimer ». |
| S1. 30 premières secondes | 🟠 | 🟢 | V1 : un fait faux à 0:10, la question à 0:32. V2 : la question à 0:28 à 145 mots/min, 0:23 à ton débit. |
| S2. Le pont | 🟠 | 🟢 | V1 : six éléments. V2 : trois livrables, plus la révélation des deux réglages et la réponse finale. |
| S3. Retournements | 🟠 | 🟠 | V1 : la section 1 tient 2 min 15 sans retour au hook. V2 : les pages vides (1:12), « montré, pas écrit » (2:02), « le 75 du début » (2:43) ; mais en section 2, les relances tombent toutes les 45 à 62 s, pas toutes les 30. |
| S4. Planté / récolté | 🟠 | 🟢 | V1 : le 75 / 28 du hook n'est jamais récolté. V2 : récolté à 2:43 ; « son fichier ne rentre même pas » est récolté en section 2. |
| S5. Personnages | 🔴 | 🟠 | Des « utilisateurs » sans visage, comme le veut ta règle. V2 : « une même personne, avec le même fichier » donne au moins un témoin. |
| S6. La fin | 🟠 | 🟢 | La règle en une phrase, puis « le jour où il sort, je refais ce classement » ouvre la vidéo suivante. |

## Les 5 problèmes les plus graves

### 1. Le hook compare deux fichiers et dit « même modèle »
> « Sur une 5060 Ti, vingt-huit. […] Même modèle. »

**Pourquoi ça coince :**
- Le 75 est mesuré avec le Q4_K_M (16,56 Go), contexte 4 K. Le 28, avec l'UD-IQ4_XS (14,35 Go), contexte 8 K (Q12, Q14).
- La légende à l'écran le dit, mais la voix dit le contraire.
- Le hook est le seul passage que tout le monde entend.

**Correction (faite) :**
- Tourner l'écart en argument : « Sur une 5060 Ti, son fichier ne rentre même pas. Avec un plus petit : vingt-huit. »
- Le 28 est maintenant de première main : le billet de l'utilisateur, daté du 06/10, dit « Plain generation: 28.0 tok/s » (Q14).

### 2. Le statut du « Qwen 4 27B » est faux, dans l'autre sens que le radar
> « Sauf que ce nom n'est pas dans le communiqué. Il vient d'un post partagé après la conférence. Donc ce modèle-là, pour l'instant, c'est une rumeur. Et Alibaba n'a même pas promis que les fichiers seraient publics. »
> (section 4) « On ne sait même pas si le vingt-sept milliards existe, ni s'il sera public. »

**Pourquoi ça coince :** le radar (« confirmé ») et la V1 (« rumeur d'un post X ») se trompent tous les deux.
- **Rien d'écrit par Alibaba.** Le communiqué ne contient ni « 27B », ni « Plus », ni « Flash » (relu le 11/11). La doc de `qwen4-max-preview` n'en parle pas.
- **Mais la presse dit qu'il a été montré à la conférence.** 36Kr (23/09), en résumant la feuille de route du Yunqi : « 开源侧优先安排Qwen4-27B » (côté open source, priorité à Qwen4-27B). Deux autres sites disent que Liu Dayiheng l'a montré sur scène.
- **Une seule source parle d'un post sur X** (RITS).
- Donc « Alibaba n'a même pas promis » et « on ne sait même pas s'il existe » vont trop loin.
- « Max » est devenu officiel le 11/11, par `qwen4-max-preview`.

**Correction (faite) :**
> « D'après la presse chinoise, il a été montré à la conférence, comme la version ouverte de Qwen quatre. Sauf qu'Alibaba ne l'a écrit nulle part : ni dans son communiqué, ni dans sa documentation. Aucune taille, aucune date. Donc pour l'instant, c'est un nom annoncé, et personne n'a vu son fichier. »

À l'écran, une troisième couleur : « MONTRÉ, PAS ÉCRIT », en orange, entre « SÛR » et « RUMEUR ».

La note `⟦à vérifier⟧` de la V1 sur le communiqué reste valable : la relecture a cherché « 27B » dans la page avec un outil de résumé, refais-le toi-même avant de montrer la recherche à l'écran. Sur Hugging Face, ne montre aucun « 0 résultat » : des pages « Qwen4-27B » d'inconnus existent (Q25).

### 3. Le titre recommandé promet le contraire de la conclusion
> **Titre recommandé** : *Qwen 4 arrive : quelle carte graphique acheter avant que ça monte ?*
> (sous-texte) « ce n'est pas une vidéo « achète vite » »
> (section 4) « n'achète pas pour un nom »

**Pourquoi ça coince :**
- « Avant que ça monte » dit au spectateur d'acheter maintenant. La vidéo lui dit d'attendre le vrai fichier s'il a déjà seize gigas.
- C'est l'écart que l'axe 1 sanctionne : le spectateur venu chercher « quoi acheter vite » repart avec « rien, pour l'instant ».
- Et la vidéo ne peut pas savoir si les prix vont continuer de monter (« personne ne sait quand ça redescendra »).

**Correction :**
- La V2 garde le titre du calendrier en en-tête, car tu décides.
- Je recommande *Qwen 4 arrive : quelle carte graphique acheter (ou pas) ?* : il affirme, il dit le sujet, et le « (ou pas) » est tenu par la section 4.
- Reporte ton choix dans `README.md` et `calendrier.md`.

### 4. La section 1 refait le trou de *16 Go* : 2 min 15 de sources avant la première carte
> « Alors voilà ce qui est sûr, parce qu'Alibaba l'a écrit lui-même. Le vingt-deux septembre, […] Fin août, Qwen avait publié un modèle d'essai, Flash-Next, […] Et en effet, mercredi, la préversion de Qwen quatre Max, jusqu'au vingt-cinq novembre. »

**Pourquoi ça coince :**
- L'audit montre que *16 Go* a perdu un tiers des spectateurs entre 0:30 et 1:15, en laissant le mystère du hook de côté.
- Ici, le hook pose 75 contre 28, puis la vidéo parle de communiqués, de Flash-Next et de trois rumeurs. La première carte arrive à 3:15, et le 75 / 28 n'est jamais récolté.
- Flash-Next ne sert pas l'achat.

**Correction (faite) :**
- La section 1 démarre sur du vrai à montrer et un geste : les pages « Qwen4-27B » vides (« Ouvre-les : elles sont vides »). Puis un conseil utile : « méfie-toi ».
- Flash-Next saute. Les deux rumeurs tiennent en une phrase.
- La section finit sur une relance qui récolte le hook : « Mais alors, le soixante-quinze et le vingt-huit du début, c'est quoi ? »
- La longueur reste à peu près la même (2 min à 145 mots/min, 1 min 40 à ton débit), mais il se passe quelque chose toutes les 30 à 40 s.

### 5. Le plan a six éléments, sous une étiquette
> « Au programme : ce qui est sûr sur Qwen quatre, et ce qu'on raconte. La carte selon ton budget, en euros. Ce que fait la carte que tu as. Et si tu dois acheter maintenant. Plus deux réglages gratuits qui font presque tripler la vitesse de deux cartes. Et à la fin, la règle d'achat, en une phrase. »

**Pourquoi ça coince :**
- La règle du 11/11 demande 3 ou 4 livrables, plus la révélation. Ici il y en a six.
- « Si tu dois acheter maintenant » et « la règle d'achat » sont la même chose, dite deux fois.
- « Au programme » sonne comme le « dans cette vidéo » que la règle des 15 s interdit.

**Correction (faite) :**
> « Je te montre ce qui est sûr sur Qwen quatre, et ce qui ne l'est pas. La carte pour ton budget, en euros. Et ce que fait déjà celle que t'as. En route, il y a deux réglages gratuits qui font presque tripler la vitesse d'une paire de cartes. Et à la fin, je réponds à ta question en une phrase : acheter, ou attendre. »

« Ta question » récolte la question centrale de 0:28.

## Les erreurs de faits (revérifiées le 11/11, détail et URL dans `sources.md`)

| V1 | Ce qui est vrai | Source |
|---|---|---|
| « Même modèle » (75 contre 28) | Même modèle, deux fichiers : Q4_K_M (5090), IQ4_XS (5060 Ti) | Q12, Q14 |
| Le 28 de la 5060 Ti, « de seconde main » | De première main : billet de l'utilisateur, 06/10, 8 K, sans MTP ; **51,4** avec MTP | Q14 |
| « Soixante-quinze » sans nuance | 75,19 à 4 K sur une version du logiciel ; 65 sur d'autres, 43 sur la plus récente | Q12 |
| Le 27B « vient d'un post », « Alibaba n'a même pas promis » | Montré à la conférence d'après la presse, comme version ouverte ; écrit nulle part par Alibaba | Q6 |
| « On ne sait même pas si le vingt-sept milliards existe » | Le nom existe, annoncé à l'oral ; c'est son fichier que personne n'a vu | Q6 |
| Deux 5060 Ti : « mesures d'utilisateurs différents » | 22,1 → 37,1 → 65,9 : **même utilisateur, même fichier, même contexte** ; seul le 76 vient d'un autre | Q15 |
| « 27 milliards × ~4 bits ≈ 15 à 17 Go » | 27,78 × 4 / 8 = 13,9 Go ; les vrais fichiers quatre bits font 14,35 à 17,66 Go | Q9 |
| « entre quinze et dix-sept gigas » (section 4) | Entre quatorze et dix-huit, selon le fichier | Q9 |
| « Seize gigas, non » (section 4) | Seize gigas, c'est serré : l'IQ4_XS y tourne à 28 tok/s (section 2 de la même V1) | Q11, Q14 |
| Écart de la 5060 Ti : « pas le même modèle » (Q22) | C'est **le même modèle** (ASUS Prime OC 16 Go) : 694 € chez Amazon.fr, 1 099,95 € chez LDLC, les deux en stock | Q21, Q22 |
| 3090 d'occasion : « huit cents à mille euros » (repli) | 800 à 1 190 € fin octobre (moyenne 834 €) | Q23 |
| « Quand Alibaba publiera les vrais fichiers » | Rien n'est promis par écrit : « si » | Q1, Q3, Q6 |
| La fiche : « Confirmé : Max, Flash, Plus, 27B » ; Flash-Next le 26/08 ; Q4_K_M 16,46 Go | Voir Q6 ; 24/08 ; 16,56 Go au 11/11 | Q2, Q6, Q9 (corrigé dans `fiche.md`) |

**Confirmé tel quel** :
- les dates et les conditions de Qwen4-Max-Preview (Q3) ;
- aucun Qwen 4 sur la page officielle (Q4) ;
- les tailles 14,35 et 16,56 Go (Q9) ;
- la 3090 à 40,31 puis 33,95 (Q13) ;
- la 7900 XTX de 28,8 à 41,0 (Q16) ;
- la 5080 à 101,3 (Q17 ; le « trois bits » vient d'une note de bas de tableau mal reliée) ;
- les hausses du comparateur (Q20) ;
- la 5090 à 7 900 € en stock (Q21) ;
- la 3090 neuve à 2 990 €, la 7900 XTX à 1 417 € (Q21).

## Les tics à supprimer

| V1 | Problème | V2 |
|---|---|---|
| « Et en effet, mercredi, la préversion de Qwen quatre Max, jusqu'au vingt-cinq novembre. » | « En effet » ne confirme rien, et la phrase n'a pas de verbe | « Et depuis aujourd'hui, une préversion, Qwen quatre Max, est ouverte jusqu'au vingt-cinq novembre. » |
| « Du coup, cette fois, le Q quatre K M rentre » ; « Et du coup, c'est là que se cachent » ; « Et du coup, si t'as seize gigas » | « Du coup » sans conséquence, mis pour gonfler le compte | supprimés ; les « du coup » restants suivent une cause |
| « Sinon, ça déborde dans la RAM, et en fait, ça rame. » | « En fait » n'explique rien | « et là, ça rame » |
| « Bref, comment on achète une carte… » | « Bref » ouvre un paragraphe sans rien résumer | « Mais alors, le soixante-quinze et le vingt-huit du début, c'est quoi ? » |
| « Rien à télécharger, point. » ; « Sans lui. » | fragments dramatiques | supprimés |
| « Et le prix ? » ×2 (5060 Ti, 3090) | faux suspens en série, à une minute d'écart | « Côté prix, regarde bien », « Neuve, la 3090… », « Les deux cartes, chez Amazon » |
| « Pas de date, pas de taille. » ; « ta carte, ton budget, et ce que tu trouves vraiment chez toi » | une paire en fragments, un triplet | « sans date ni taille », « on n'en connaît ni la taille ni la date » ; « quelle carte t'as, et combien elle coûte vraiment chez toi » |
| « Premier fait […] Deuxième fait […] Troisième fait » | rafale de trois, liste au lieu de « mais / donc » | « D'abord… Mais… Sauf que… Donc… » |
| « C'est une estimation, pas un fichier. » ; « Et c'est le Qwen d'aujourd'hui, pas Qwen quatre. » | « X, pas Y » à répétition (quatre dans la V1) | réécrits ; il en reste une, la règle (« n'achète pas pour un nom »), qui corrige une idée que le spectateur a vraiment |

Aucun « plongeons », aucun « et ça, c'est… », aucun « vous » dans la V1 : bravo au rédacteur.

## Autres corrections (moins graves)

- **Section 3, la logique se contredit.** La V1 dit : « Donc pour eux, la réponse, ce n'est pas de courir acheter : un modèle de cette taille ne tournera pas bien chez toi ». Si le modèle ne tourne pas, ne pas acheter n'est pas une réponse. Et « pour eux » devient « chez toi » dans la même phrase. V2 : « Qwen quatre ne va sans doute rien changer : rien ne dit qu'il sera plus petit, et pour un modèle de cette taille, il te faudra une carte des paliers d'avant. »
- **Le repli du `⟦à écrire 4⟧` affirmait un vécu.** « Ma 5080 me suffit pour essayer, je ne l'ai pas changée » contredit ton Qwen lent de *16 Go*. Fusionné avec le `⟦5⟧` : il reste quatre `⟦à écrire⟧`.
- **L'encart Afrique et la fin demandaient deux fois la même chose en commentaire.** Le repli Afrique renvoie maintenant à la fin.
- **« Je teste Strata » était dit deux fois** (section 3 et fin). Il ne reste qu'à la fin.
- **Téléprompteur** : les replis étaient entre parenthèses, et la règle dit que les parenthèses ne se lisent pas. Ils sont maintenant écrits en lignes, sous leur marqueur.
- **Montage** :
  - un trou de visuel entre 0:24 et 0:29 ;
  - un classement « 5 cartes » jamais décrit ;
  - la recherche Hugging Face : des pages « Qwen4-27B » d'inconnus existent, à flouter.

Tout est recalé dans la V2.

## Ce qui marche, à garder

- > « C'est comme libérer de la place sur ton SSD pour un jeu dont personne ne connaît le poids : tu prends le précédent comme étalon. » Ta voix gamer, et la meilleure traduction du script. Gardée telle quelle.
- > « n'achète pas pour un nom, achète pour la taille d'un fichier, plus de la place pour la conversation » : une règle qu'on retient et qu'on peut refaire seul. C'est la seule opposition du script, et elle est légitime : le spectateur pense vraiment acheter « pour Qwen 4 ».
- **La séparation « sûr / on raconte » à l'écran**, avec des captures surlignées : c'est ce qu'aucune vidéo concurrente ne fait. La V2 l'étend à trois couleurs.
- **Les deux réglages gratuits sur deux 5060 Ti** (22 → 37 → 66) : la vraie révélation de la vidéo, bien annoncée dans le plan. Elle est encore plus forte maintenant qu'on sait que c'est la même personne et le même fichier.
- **« Pour être honnête, elle est testée sans MTP, donc à réglages égaux, elle reste devant. »** Une honnêteté qui rend crédible tout le reste. Gardée, en plus court.
- **La rigueur des sources du rédacteur** : prix datés, « aucun prix d'occasion relevé » assumé, faits incertains listés. C'est ce qui a permis cette relecture.
- **Aucun nom de chaîne ni de créateur dans la voix**, aucun « vous ».

## Contrôles de la V2

Comptés par script sur la voix seule, sans `[…]`, `(Qx)` ni `⟦…⟧` :

| Mesure | V1 | V2 |
|---|---|---|
| Mots dits (sans les `⟦à écrire⟧`) | 1 347 | 1 390 |
| Replis des `⟦à écrire⟧` | ~130 | 104 |
| Durée à 145 mots/min (replis compris) | ~10 min 10 | ~10 min 20 |
| Durée à ton débit (180 mots/min) | ~8 min 15 | ~8 min 20 |
| Mots jusqu'à la question centrale | 77 | 76 |
| Liaisons, liste étroite (donc, du coup, en fait, sauf que, en effet, voilà) | 1,78 pour 100 (24), dont 5 ou 6 creuses | 1,65 pour 100 (23), sans liaison creuse relevée |
| Liaisons, liste du skill (+ mais, et là, en gros, résultat, par contre…) | 2,75 | 2,8 |
| Nombres dits dans la 1re minute | 4 | 5 (7 900, 75, 28, 20 %, deux réglages) |
| Éléments du plan | 6 | 3 livrables + 1 révélation + la réponse |
| Première carte du budget | 3:15 (145) | 3:09 (145), 2:32 à ton débit |
| `⟦à écrire⟧` | 5 | 4, chacun avec un repli prêt à lire |

## Plan d'action (aujourd'hui, avant la voix)

1. **Lis le hook à voix haute et chronomètre.** Vise 25 à 30 s jusqu'à « ou tu attends ? ». Si tu dépasses, coupe « aujourd'hui » et « dans le cloud d'Alibaba ».
2. **Refais les captures de prix**, avec la date visible :
   - l'ASUS Prime OC 5060 Ti 16 Go, sur Amazon.fr **et** sur LDLC (si l'écart a disparu, le script donne la phrase de repli) ;
   - la 5090, la 3090 et la 7900 XTX sur Amazon.fr.
3. **Remplis les quatre `⟦à écrire⟧`**, ou lis les replis. La priorité est le `⟦2⟧` : tes annonces de 3090 du jour valent mieux que le relevé d'octobre.
4. **Choisis le titre** (problème 3) et reporte-le dans `README.md` et `calendrier.md`.
5. **Le 12/11 au matin** : rouvre la page des modèles de Qwen sur Hugging Face et la doc `qwen4-max-preview`. Si Qwen 4 est sorti, les sections 1 et 4 changent.
