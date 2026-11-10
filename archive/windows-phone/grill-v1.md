# Grill du script Windows Phone v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Version finale : [`script.md`](script.md).
> Grille : `youtube-script-grill`, mode B (après l'écriture), **variante storytelling** (test des 30 secondes, axe 10 des liaisons, axes S1 à S6).
> Hypothèses : titre *Ton téléphone est une brique. Microsoft l'a appris à ses dépens.* (titre 3 de la fiche), miniature dans la charte noire (`noir.html`), public de 18-30 ans, surtout africain, qui n'a souvent jamais tenu un Windows Phone ; arrivée par l'accueil. Objectif : la 3e « grande histoire » du pilier, après le pixel (14 déc.) et Python (28 déc.).
> Faits revérifiés à la source le 23/10 : voir « Vérification des faits » en bas, et les lignes 33 à 38 ajoutées à [`sources.md`](sources.md).

## Note globale : 7/10

9 🟢, 8 🟠, 0 🔴. La V1 est propre sur les faits de `sources.md` (aucune affirmation ❌ dite comme vraie), elle garde ton sous-texte et presque toutes tes phrases, et elle a déjà 2,5 liaisons pour 100 mots. Ce qui coince : un hook qui garde son chiffre le plus fou pour la 23e seconde et pose deux questions, trois « mon premier jet » qui font de la vidéo le corrigé de ton brouillon, trois ajouts du rédacteur sans source (dont une définition de l'effet de réseau qui ne colle pas au cercle qu'elle explique), et une fin qui résume trois fois.

## Verdict

Le squelette marche : ta phrase-brique ouvre et ferme la vidéo, Windows Phone sert de preuve et non de sujet, et la vidéo apporte ce que les vidéos anglaises sur le sujet n'ont pas (6snap, le message de Belfiore, Google qui bloque l'appli YouTube de Microsoft, le Store plein mais sans les bonnes applis). Le jeu multi sans joueurs est la meilleure image du script, et elle est à toi (humour gamer).

Le plus gros problème est la manière dont la V1 corrige ton brouillon : elle le fait à voix haute, trois fois, en parlant de « mon premier jet ». Le spectateur ne sait pas qu'il existe un brouillon ; il entend un narrateur qui s'est trompé trois fois sur son propre sujet. Une seule correction, celle de WhatsApp, fait un vrai retournement (WhatsApp → Instagram) : elle reste, dite comme ce que tu croyais. Deuxième problème : la définition de l'effet de réseau (« une appli vaut quelque chose parce que les autres y sont déjà ») décrit l'effet direct, celui de WhatsApp, alors que le cercle de la vidéo (applis ↔ utilisateurs) est l'effet indirect.

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** : sans tes applis, ton téléphone est une brique, et Microsoft l'a payé 7,6 milliards. Le hook la confirme dès la première phrase ; la vidéo la tient avec Belfiore (« on les a payés… trop peu d'utilisateurs »), qui est la preuve par la bouche de Microsoft.
- **Le problème de surface** : pourquoi Windows Phone a échoué.
- **Le problème profond** (ton sous-texte) : ce qu'on aime dans notre téléphone, ce sont nos applis. Il est posé (hook, section 1 et tes « bonbons pour ton cerveau »), développé (le Store à 340 000 applis sans les dix qu'on utilise), et résolu à la fin. La V1 le résout trois fois de suite (« Bref. Windows Phone avait… », « Donc la prochaine fois… », « Au début, tu me disais… ») : il perd de sa force à chaque redite.
- **La chaîne** (V1) : la brique → **mais** tes applis, **donc** ton téléphone = tes applis → un téléphone qui avait tout → Nokia, **donc** Microsoft a gagné → **mais** trois pour cent, **donc** il manquait quoi ? → WhatsApp, **sauf que** c'est faux → Instagram → Snapchat jamais → YouTube bloqué → **donc** le Store était vide ? **même pas** → **donc** un dev code Snapchat → **sauf que** tout disparaît → « signal fort ? » **sauf que** Microsoft savait → **parce que** le cercle → **et en plus** ils ont tout changé → **et** le rachat, **et** 7,6 Md$, **et** fin 2019 → ta liste d'applis.
  Le « et ensuite » ne se voit qu'en fin de section 6 (rachat, dépréciation, Belfiore, fin du support, quatre dates d'affilée). `script.md` y met un « sauf que » qui récolte la phrase de la section 5 : « Sauf que, on l'a vu, des utilisateurs, ça s'achète pas. Et en effet, en juillet 2015… ».

## La fidélité au brouillon et au sous-texte

**Gardées** (13 phrases sur 21, mot pour mot ou dans le sens) : la brique, « Si je te demande… Mais en fait c'est faux », « ces bonbons pour ton cerveau. Tes applications », « Sans elles ton téléphone ne t'intéressera pas », Metro « révolutionnaire » et les photos « extraordinaires » dites comme ton avis, la pub, « des apps que tout le monde utilise », Snapchat jamais sorti, le « signal fort », « ils ont tout changé ». Ton « tu » est partout (0 « vous », vérifié par `controle.py`), même dans la partie données où ton brouillon passait au « vous ».

**Corrigées** :

| Ta phrase | Dans la V1 | Verdict |
|---|---|---|
| « Microsoft a fait sortir son téléphone » | Dite puis corrigée : « Dans mon premier jet, j'avais écrit que Microsoft sortait “son téléphone”. En fait, c'est son système. », phrase barrée à l'écran | 🟠 Juste sur le fond (fait 1), mais 25 mots et un bandeau barré pour un détail que personne n'avait en tête. `script.md` le dit juste, sans le barrer : « Microsoft ne fabrique pas de téléphones : lui, il fait le système » |
| « WhatsApp a mis des années » | « Et là, je dois corriger mon propre brouillon. J'avais écrit que… », barrée en rouge | 🟢 sur le fond (faits 12, 31) : c'est un vrai retournement, il amène le bon exemple (Instagram), et « c'est WhatsApp qui le dit » le rend solide. 🟠 sur la forme : « mon propre brouillon ». `script.md` : « Moi, j'étais persuadé que WhatsApp avait mis des années… Sauf que c'est faux » ; à l'écran, l'étiquette « ce que je croyais » au lieu de « brouillon » |
| « Je ne comprends pas pourquoi ça n'a pas été un signal fort » | « Quand j'ai écrit mon premier jet, je ne comprenais pas pourquoi… Sauf que Microsoft avait très bien compris. » | 🟢 C'est la meilleure relance de la vidéo (ta vraie question, et Belfiore y répond). « Quand j'ai écrit mon premier jet » est de trop : ta question tient seule, au passé (« Moi, je comprenais pas pourquoi… ») |
| « Un informaticien passionné… pour que sa meuf puisse l'utiliser » | Rudy Huyn et 6snap (fait 16) ; le motif en crochet, **deux fois** (un crochet court et un long, sur la même phrase) | 🟢 pour le crochet (fait 19 : aucune source), 🟠 pour le doublon. Ton mot « passionné » disparaît (« un fan », « un passionné » une fois) : `script.md` le garde comme ton regard, « pour moi, c'est un passionné » |
| « Ils se sont embêtés à le rendre fermé » | Le crochet propose (a) la licence ou (b) les versions incompatibles, et « le script dit (b) en attendant » | 🟠 (b) est déjà ta phrase suivante (« ils ont tout changé ») : la V1 fond deux idées de ton brouillon en une. `script.md` ne dit rien sur « fermé » tant que tu n'as pas répondu, et la phrase sur la licence (fait 20) est prête dans le crochet |

**Ce qui a été perdu** : rien de ton sous-texte. Le recadrage vers « l'échec de Microsoft » est évité (le rachat et la fin tiennent en une minute, section 6). Le risque est ailleurs : avec trois « premier jet » et deux phrases barrées, la vidéo devient la tienne contre ton brouillon, au lieu de la tienne contre une idée reçue.

**Les légendes barrées : est-ce que ça marche ?** Une fois, oui : c'est l'« échec honnête » du skill (V2F, `storytelling.md` section 4), et il rend crédible tout le reste. Trois fois, non : le spectateur ne connaît pas ton brouillon, et chaque « mon premier jet » lui rappelle que tu n'étais pas sûr de ton sujet, dans une vidéo dont la valeur est la recherche. Et la troisième (le Store « vide ») n'est même pas à toi : elle venait de la fiche. Dans `script.md` : WhatsApp à voix haute, comme ce que tu croyais (question 7) ; « son téléphone » dit juste ; le Store vide prêté au spectateur (« tu dois te dire »), ce qui est légitime puisque c'est la déduction naturelle de « il manquait des applis ».

## Le test des 15 premières secondes

Relues seules, à 145 mots/min (environ 36 mots) :

> « Ton téléphone, quand tu le sors de la boîte, c'est une brique qui ne sert à rien. Je sais, il appelle et il prend des photos. Mais enlève-lui WhatsApp, TikTok et Snap : tu le gardes combien de temps en main ? »

🟠 **La première phrase est la bonne, la suite recule.** Ta phrase-brique est raccord avec le titre et la miniature, et elle provoque. Mais :
- « Je sais, il appelle et il prend des photos » arrive à 0:07 et désamorce la provocation avant qu'elle ait fait son effet. Ta section 1 fait déjà cette concession (« Bon, pas complètement. Il appelle, il envoie des SMS… ») à 0:50 : on la garde là ;
- « tu le gardes combien de temps en main ? » est une question dont le spectateur connaît la réponse, et la section 1 refait la même scène (« Imagine : tu achètes le téléphone le plus puissant du monde. Tu l'allumes, et pas de WhatsApp ») ;
- le chiffre le plus fou de la vidéo, « sept virgule six milliards de dollars », arrive au 56e mot, à 0:23.

Dans `script.md`, les 15 s deviennent ta phrase-brique, puis « Et Microsoft l'a appris à ses dépens : sept virgule six milliards de dollars, effacés de ses comptes. » (34 mots, 0:14 à 145). Le titre, dit à voix haute, avec sa preuve chiffrée.

## Le test des 30 secondes

| Tranche | Ce que dit la V1 | Verdict |
|---|---|---|
| 0-5 s | > « Ton téléphone, quand tu le sors de la boîte, c'est une brique qui ne sert à rien. » | 🟢 Le sujet et une tension, raccord avec la miniature. |
| 5-15 s | > « Je sais, il appelle et il prend des photos. Mais enlève-lui WhatsApp, TikTok et Snap : tu le gardes combien de temps en main ? » | 🟠 Une concession et une question déjà répondue ; pas de preuve. |
| 15-30 s | > « Microsoft et Nokia ont fait l'expérience en vrai. Un téléphone superbe, quarante et un mégapixels… et sept virgule six milliards de dollars effacés. Alors, qu'est-ce que tu aimes vraiment dans ton téléphone ? » | 🟠 Le bon contraste (41 Mpx → 7,6 Md$), mais dit de travers (la perte est celle de Microsoft, pas « de Microsoft et Nokia », voir les faits), et la question centrale est la deuxième question du hook, au 63e mot. Elle est aussi déjà répondue : après « enlève-lui WhatsApp », le spectateur sait ce qu'il aime dans son téléphone. |
| Pont | > « La réponse est cachée dans un téléphone que tu n'as sûrement jamais tenu : le Windows Phone. » | 🟠 Il présente le sujet sans ouvrir de deuxième question. |

**Budget :** 88 mots ≈ 36 s à 145 mots/min, 30 s à 178. 🟢
**À couper :** « Je sais, il appelle et il prend des photos » (déplacée en section 1), « tu le gardes combien de temps en main ? » (doublon de la section 1), « superbe » (un avis sans preuve à cet endroit).
**Réécriture des 30 s** (dans `script.md`, 91 mots ≈ 38 s à 145, 31 s à 178 ; question centrale au 66e mot) :

> Ton téléphone, quand tu le sors de la boîte, c'est une brique qui ne sert à rien.
> Et Microsoft l'a appris à ses dépens : sept virgule six milliards de dollars, effacés de ses comptes.
> Et pourtant, son système tournait sur un Nokia au capteur de quarante et un mégapixels, avec tout l'argent de Microsoft derrière. Alors comment le téléphone qui avait tout a fini en brique ?
> En fait, la réponse est sur ton écran d'accueil. Et pour la trouver, on va suivre un dev qui a fini par coder Snapchat lui-même.

Une seule question, celle que le titre pose (« appris à ses dépens » : comment ?). Le pont ouvre une deuxième boucle (qui ? pourquoi ?), refermée à 6:51 par Rudy Huyn. « La réponse est sur ton écran d'accueil » garde ton sous-texte dès le hook, sans le livrer.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | La brique en première phrase, Windows Phone comme preuve, Belfiore comme aveu : le titre est tenu. |
| 2. Alignement | 🟢 | Aucune vente ; un appel à l'abonnement, mais mal branché (voir la rétention). |
| 3. Problème profond | 🟢 | Ton sous-texte est posé, développé et résolu ; il est seulement résolu trois fois de suite. |
| 4. Public & complexité | 🟠 | Metro, client non officiel et « app gap » sont expliqués ; l'effet de réseau est mal défini, et à contresens du cercle qu'il explique. |
| 5. Valeur & originalité | 🟢 | Aucune vidéo du sujet (Apple Explained, Owen Cook, amx) ne fait des applis le sujet ; 6snap, Belfiore et l'appli YouTube sont absents des vidéos françaises. |
| 6. Structure & transformation | 🟢 | Du « j'aime mon téléphone pour ses photos » à « j'aime mon téléphone pour mes applis », par une preuve en quatre temps. |
| 7. Histoire | 🟠 | Une ascension et chute claire, mais racontée avec des entités (« Microsoft », « Google », « Snapchat ») ; seul Rudy Huyn veut quelque chose. |
| 8. Mais / donc | 🟢 | Très bon jusqu'à la section 5 ; la fin de la section 6 empile quatre dates. |
| 9. Engagement actif | 🟢 | « Tu vas me dire : donc le Store était vide », « mets-toi à la place de Snapchat », la question finale en commentaire. |
| 10. Rythme, oralité & liaisons | 🟠 | 2,5 pour 100 au total, mais 1,1 dans le hook, 1,2 à la fin, zéro « en effet » (ton mot), et trois rafales. |
| 11. Tics d'IA | 🟠 | Une fausse opposition, deux annonces, et l'inventaire « système, Nokia, argent » répété quatre fois. |
| S1. Les 30 premières secondes | 🟠 | Deux questions, la seconde déjà répondue, et le meilleur chiffre à 0:23. |
| S2. Le pont | 🟠 | Il nomme le sujet sans ouvrir de deuxième question. |
| S3. Les retournements | 🟢 | 33 relances, une toutes les 25 s ; plus long trou 10:35 → 11:25 (50 s). |
| S4. Planté / récolté et motif | 🟢 | La brique, les 41 Mpx, les 7,6 Md$, le « signal fort » → Belfiore, l'écran d'accueil qui se vide puis se remplit. |
| S5. Personnages et enjeu | 🟠 | Rudy Huyn a une envie et un obstacle ; Microsoft reste une entreprise sans visage jusqu'à Belfiore (8:28). |
| S6. La fin | 🟠 | Elle revient à la brique et ouvre une question (les données) et la vidéo suivante, mais après trois résumés. |

## L'axe 10 : les liaisons

Compte de `controle.py` sur la V1 : **50 liaisons pour 1 982 mots, soit 2,5 pour 100** (cible : 1,5). Par fonction : « donc » 9, « mais » 8, « sauf que » 5, « imagine » 5, « en fait » 4, « et là » 4, puis « forcément », « tu te rappelles », « du coup », « parce que » (2 chacun), « normalement », « résultat », « tu vois », « en gros », « pour faire simple », « voilà pourquoi », « bref » (1 chacun). **« En effet » : 0**, alors que c'est ta liaison à toi.

| Section | Mots | Liaisons / 100 (V1) | `script.md` |
|---|---|---|---|
| 0. Hook | 88 | **1,1** | 2,2 |
| 1. Les bonbons pour ton cerveau | 215 | 3,3 | 2,8 |
| 2. Le téléphone qui avait tout | 381 | 2,1 | 1,9 |
| 3. Les icônes qui manquaient | 313 | 3,5 | 3,7 |
| 4. Le dev qui a codé son Snapchat | 233 | 1,7 | 2,1 |
| 5. Microsoft savait | 305 | 4,3 | 3,5 |
| 6. Ils ont tout changé | 207 | **1,4** | 2,3 |
| 7. Ta liste d'applis | 240 | **1,2** | 3,1 |

**Les problèmes, au-delà du chiffre :**
- **La section 5 est à 4,3, mais par des « donc » mécaniques** : « Pas d'applis, donc pas d'utilisateurs. Et pas d'utilisateurs, donc pas d'applis » puis « Le serveur est vide, donc personne ne vient, donc le serveur reste vide ». Quatre « donc » en deux phrases-slogans. `script.md` en garde deux.
- **Les rafales de faits** (trois phrases et plus sans liaison ni réaction) :
  - section 4 : « Il s'appelle Rudy Huyn. Il avait déjà fait 6tag […]. Et le vingt et un novembre 2013, il sort 6snap […]. Fait par un développeur qui ne bosse même pas chez Snapchat. » `script.md` : la date au mois, « la même semaine que la bêta d'Instagram » en incise, et ton regard (« pour moi, c'est un passionné ») ;
  - section 6 : « En 2012, Windows Phone 8 arrive. Et aucun téléphone Windows Phone 7 ne peut passer à Windows Phone 8. Aucun. Même pas le Lumia 900, vendu cette année-là. Microsoft leur donne un lot de consolation » : `script.md` ajoute « À la place » ;
  - section 6 : « En avril 2014, Microsoft rachète… Et en juillet 2015, il supprime… En 2017, Belfiore écrit aussi… Et fin 2019, Microsoft arrête le support. C'est fini. » : quatre dates en « et ». `script.md` : « Sauf que, on l'a vu, des utilisateurs, ça s'achète pas. Et en effet, en juillet 2015… », puis « Et après, ça s'éteint doucement : en 2017… ».
- **Le hook à 1,1** : une seule liaison (« Alors »), normal pour 30 s qui doivent frapper ; `script.md` en met deux (« Et pourtant », « En fait »).
- **La fin à 1,2** : trois paragraphes de bilan sans liaison. `script.md` n'en garde qu'un, relié (« Tu vois, au début, tu me disais… Sauf que le Lumia 1020… Et pourtant, ça l'a pas sauvé »).

`script.md` : **2,7 pour 100** sur 1 977 mots, aucune section sous 1,9, et trois « en effet » qui confirment ce que le spectateur soupçonne (« Et en Europe, en effet, ça prend », « Et en effet, pour la plupart des boîtes, le calcul dit non », « Et en effet, en juillet 2015 »). Attention à « sauf que » (8) : c'est la liaison la plus utilisée ; à la prise, remplace-en une ou deux par « mais » si elles s'entendent.

## Les tics d'IA

| Citation de la V1 | Tic | Dans `script.md` |
|---|---|---|
| « Tu vois le truc ? Ton téléphone ne te sert pas à avoir trois cent quarante mille applis. Il te sert à avoir les dix que tes potes utilisent. » | Annonce (« Tu vois le truc ? ») puis fausse opposition « ne te sert pas à A, il te sert à B » | « Toi, sur ton téléphone, t'en utilises combien, des applis ? Dix, quinze ? Et la plupart, ce sont celles où sont tes potes. » (une vraie question au spectateur) |
| « Imagine le tableau. Un passionné code l'appli à la place de la boîte, la boîte ne vient toujours pas, et ceux qui s'en servaient se retrouvent sans rien. » | Annonce, rafale de trois, résumé de ce qu'on vient d'entendre | « Résultat : ceux qui avaient enfin Snap sur Windows Phone se retrouvent sans rien. Et l'appli officielle ne viendra jamais. » |
| « Et ça, c'est Microsoft qui le dit. Quand le chef lui-même te dit « on a payé, et ça n'a pas marché », tu sais que l'argent n'était pas le seul problème. » | Redite de la phrase précédente, petite morale, et inexact (Belfiore est un des patrons de Windows, pas « le chef », fait 9) | retiré : « Ouais, t'as bien entendu » suffit, et le « Alors pourquoi ? » enchaîne |
| « un système magnifique, des appareils photo de fou, le plus gros fabricant de téléphones de la planète, et l'argent de Microsoft » (section 1) ; « avec un système pareil, Nokia et l'argent de Microsoft » (section 2) ; « Windows Phone avait une interface que personne n'avait, Nokia, des photos de fou et l'argent de Microsoft » (section 7) ; « Le verre, l'aluminium, les mégapixels » (section 7) | Le même inventaire quatre fois | gardé une fois en section 1 (c'est l'annonce de la preuve) ; ailleurs, réduit à « avec Nokia et l'argent de Microsoft », ou retiré |
| « Et fin 2019, Microsoft arrête le support. C'est fini. » | Fragment de clôture | « Et fin 2019, Microsoft arrête le support de Windows 10 Mobile, le dernier Windows pour téléphone. » (l'image et le son disent « c'est fini ») |
| « Et si tu veux savoir comment ça finit, et ce que ça dit du téléphone que tu as dans la poche, abonne-toi » | Appel illogique : pour savoir comment ça finit, il suffit de rester | « Et sur le papier, toi aussi, t'es déjà abonné à Technovore. » (une blague dans le récit, comme Cam) |
| « Un téléphone superbe » (hook) | Adjectif vide à l'endroit où il faut une preuve | « un Nokia au capteur de quarante et un mégapixels » |
| « Il lui manquait juste quelques icônes. Et tu vas voir que ça suffit pour tout perdre. » | Annonce, mais qui tient sa promesse | gardé : c'est le pont de la section 1 |
| « Snapchat, lui, n'a jamais sorti d'appli officielle pour Windows Phone. Jamais. » ; « Aucun. Même pas le Lumia 900 » | Fragments d'insistance | gardés : un chacun, sur deux faits forts |

Aucune fausse opposition « ce n'est pas A, c'est B » au sens strict, ni dans la V1 ni dans `script.md` (recherche faite sur « n'est pas », « c'est pas », « pas juste », « ne te sert pas »).

## La rétention

- **Relances** : 33 dans la V1, une toutes les 25 s ; plus long trou 10:35 → 11:25 (50 s), le rachat de Nokia. Dans `script.md` : 40, une toutes les 20 s ; plus long trou 9:59 → 10:39 (40 s).
- **Abonnement vers 25 %** : à 3:15 dans la V1 (24 %), au bon endroit (juste après « Microsoft vient de gagner »), mais avec une logique bancale (voir les tics) et suivi d'un « Du coup, en octobre 2011 » qui ne relie rien à l'appel. `script.md` : 3:11 (24 %), une blague « sur le papier » qui prolonge la phrase d'avant, puis « Bon. Huit mois plus tard… ».
- **Relance forte vers 60 %** : 8:28 (62 %) dans la V1, et elle est bonne : ta question « signal fort » posée, coupure musicale, Belfiore qui répond. `script.md` la garde (8:15-8:30, 61-63 %), avec ta question au passé et sans « mon premier jet ».
- **Points fragiles qui restent** : la section 2 (trois dates, 2010-2013) et le raisonnement de Snapchat (9:59-10:39). Le premier est tenu par la ligne de temps, Metro, le 3310 et la loupe ; le second par le jeu multi juste avant.

## Le grill

### 1. Trois « premier jet » qui font de ta vidéo un corrigé

> « Dans mon premier jet, j'avais écrit que Microsoft sortait « son téléphone ». En fait, c'est son système. »
> « Et là, je dois corriger mon propre brouillon. »
> « Quand j'ai écrit mon premier jet, je ne comprenais pas pourquoi… »

**Pourquoi ça coince :** voir « Les légendes barrées » plus haut. Le spectateur ne connaît pas ton brouillon ; il entend trois fois que tu t'es trompé.
**Correction :** une seule correction à voix haute, celle qui fait un retournement, dite comme une croyance : « Et là, je vais être honnête. Moi, j'étais persuadé que WhatsApp avait mis des années à arriver sur Windows Phone. Sauf que c'est faux, et c'est WhatsApp qui le dit… » ; « son téléphone » dit juste ; le « signal fort » comme ta question (« Moi, je comprenais pas pourquoi ça n'avait pas été un signal fort pour Microsoft »).

### 2. Le hook garde son meilleur chiffre pour la 23e seconde

Voir les tests des 15 et 30 secondes. Correction : la brique, puis le titre dit avec sa preuve (7,6 Md$), puis le contraste (41 Mpx, l'argent), une seule question, et un pont vers Rudy Huyn.

### 3. Trois ajouts du rédacteur sans source

> « Tu te rappelles le 3310 de ton oncle, celui qui survivait à tout ? »

Un mème présenté comme un fait. Sourcé au grill (fait 33, NPR, 15/02/2017 ; origine Reddit, décembre 2011) et dit comme un mème : « celui que les mèmes disent indestructible ».

> « En gros, c'est l'effet de réseau : une appli vaut quelque chose parce que les autres y sont déjà. »

Juste pour WhatsApp ou Snapchat (l'effet direct), faux pour le cercle de la vidéo, qui est indirect : les développeurs suivent les utilisateurs, et l'inverse (fait 34, Niskanen Center, 2018). Réécrit : « Les économistes, eux, parlent d'effet de réseau : les développeurs choisissent un système selon le nombre d'utilisateurs, et les utilisateurs le choisissent selon le nombre d'applis. »

> « Un client non officiel, c'est une appli qui parle aux serveurs de Snapchat sans que Snapchat l'ait faite. »

Juste, et sourcé au grill par ce que Snapchat écrit lui-même en octobre 2014 (fait 35) : pas d'API publique, et toute appli qui n'est pas la sienne « viole ses conditions d'utilisation ». `script.md` l'ajoute : c'est ce qui rend la chute de décembre 2014 logique (« Et forcément, l'histoire finit mal »).

### 4. Google claque la porte sans raison

> « Microsoft a fini par coder sa propre appli YouTube, à la place de Google. Résultat : en 2013, Google la bloque. En mai, puis encore en août. Microsoft fait le boulot de Google à sa place, et Google lui claque la porte au nez. »

**Pourquoi ça coince :** en mai 2013, Google envoie une mise en demeure (une demande de retrait), il ne bloque pas encore ; et il donne une raison, l'appli bloque les pubs (fait 36). Taire la raison rend le récit injuste, et un commentaire te le dira.
**Correction :** « Sauf que d'après Google, elle bloque les pubs, et en mai 2013, Google lui demande de la retirer. Microsoft la refait, et en août, Google la bloque : pour lui, elle ne respecte toujours pas ses règles. » La chute (« Google lui ferme la porte au nez ») reste, elle est méritée.

### 5. La fin résume trois fois

> « Bref. Windows Phone avait une interface que personne n'avait, Nokia, des photos de fou et l'argent de Microsoft. Il lui manquait Instagram à temps, Snapchat, et un YouTube sans bataille. Et ça a suffi. » / « Donc la prochaine fois que tu sors ton téléphone… Le verre, l'aluminium, les mégapixels, Windows Phone les avait aussi… » / « Au début, tu me disais… »

**Correction :** garder la seule qui retourne quelque chose, ta question du début : « Tu vois, au début, tu me disais : pour les photos, et pour parler aux autres. Sauf que le Lumia 1020 avait quarante et un mégapixels, et il appelait, comme tous les téléphones. Et pourtant, ça l'a pas sauvé. » Puis ta brique, une fois.

### 6. Le « fermé » fondu dans « tout changé »

Le crochet de la section 6 de la V1 propose (b) « des téléphones qui ne passent pas à la version suivante », puis le script le dit. Or c'est ta phrase suivante. `script.md` ne dit rien sur « fermé » et garde la phrase prête sur la licence (question 3).

### 7. Petits points

- **« Presque jamais l'appli Téléphone »** : une affirmation sur le spectateur, sans source. Devenue une question : « L'appli Téléphone, tu l'as ouverte quand, la dernière fois ? »
- **« trois pour cent des téléphones du monde »** (section 5) : ce sont les smartphones vendus (fait 2).
- **« Début 2014 »** pour Kantar : les trois mois finissent en janvier 2014 ; « fin 2013 » est plus juste (fait 3).
- **« Des applis, il y en a des millions »** : pas de chiffre sourcé à cette date ; « des tonnes ».
- **« grandes tuiles carrées »** : il y avait aussi des tuiles larges ; « grandes tuiles ».
- **Le crochet de la copine en double** (section 4) : fusionné.
- **« Quarante et un, dans un téléphone, en 2013 »** : une réaction juste, mais ne dis pas « le premier » : le Nokia 808 PureView (Symbian) l'avait en 2012.
- **Thibaut Dcode** : la partie données reste une phrase, dite comme ton avis (« Moi, j'ai mon idée »), et renvoie à une autre vidéo. 🟢
- **Fiche (carte) YouTube** : quand WhatsApp passe à l'écran (4:41), une fiche vers *WhatsApp et ses 50 ingénieurs* (11 janv.).

## Vérification des faits du script

Phrase par phrase, chaque affirmation de la voix off de la V1 contre [`sources.md`](sources.md). Les faits absents de `sources.md` ont été vérifiés à la source le 23/10/2026 et ajoutés en fin de tableau (lignes 33 à 38).

| Phrase de la V1 | Source | Verdict | Dans `script.md` |
|---|---|---|---|
| « Ton téléphone, quand tu le sors de la boîte, c'est une brique » | Fait 29 | ⚠️ provocation, à concéder vite | Gardée ; la concession arrive à 0:50 |
| « Microsoft et Nokia ont fait l'expérience en vrai. Un téléphone superbe, quarante et un mégapixels… et sept virgule six milliards de dollars effacés. » | Faits 5, 23 ; **fait 38** (news.microsoft.com, 08/07/2015, relu ; blogs.windows.com, 11/07/2013) | ⚠️ les deux chiffres sont justes, la phrase les relie mal : 41 Mpx, c'est le capteur du Lumia 1020 de Nokia (2013) ; 7,6 Md$, c'est une **dépréciation** passée par Microsoft en 2015 sur les actifs achetés à Nokia. La perte est celle de Microsoft, pas « de Microsoft et Nokia », et c'est une perte comptable, pas de l'argent dépensé | « Microsoft l'a appris à ses dépens : sept virgule six milliards de dollars, effacés de ses comptes » ; « son système tournait sur un Nokia au capteur de quarante et un mégapixels » |
| « un téléphone que tu n'as sûrement jamais tenu » | Public (sources, « Ce que ça dit pour nous ») | ⚠️ hypothèse, adoucie par « sûrement » | Retirée (le pont change) |
| « Presque jamais l'appli Téléphone. » | Aucune | ❓ | Devient une question |
| « Octobre 2010. Microsoft lance Windows Phone 7 […] HTC, Samsung, LG ou Dell » | Fait 1 | ✅ | Gardée |
| « Chez Microsoft, ce style avait un nom de code : Metro » ; « révolutionnaire » | Fait 4 | ⚠️ presse ; avis dit comme le tien | Gardée |
| « Le onze février 2011, à Londres, Nokia […] annonce avec Microsoft que Windows Phone devient le système principal » | Fait 6 | ✅ | Gardée (« En février 2011 ») |
| « Nokia, à l'époque le premier vendeur de téléphones au monde » | Fait 8 | ⚠️ Strategy Analytics via Bloomberg | Gardée |
| « le 3310 de ton oncle, celui qui survivait à tout » | **Fait 33** (NPR, 15/02/2017 ; Know Your Meme) | ⚠️ un mème, pas un fait | « celui que les mèmes disent indestructible » |
| « en octobre 2011, à Londres, le patron de Nokia, Stephen Elop, présente le premier Lumia : le Lumia 800 » | Fait 5 | ✅ | Gardée, avec « Huit mois plus tard » (11/02 → 26/10/2011) |
| « Nokia met le paquet sur la pub » | Fait 7 | ⚠️ aucun montant | Gardée |
| « Début 2012, Samsung lui passe devant, après quatorze ans de Nokia à la première place » | Fait 8 | ⚠️ | Gardée |
| « En juillet 2013, le Lumia 1020 sort avec un capteur de quarante et un mégapixels » | Faits 5, 38 | ⚠️ « capteur » est le bon mot (photos en 38 et 5 Mpx) | Gardée |
| « Début 2014, dans les cinq grands pays d'Europe, dont la France, […] un smartphone vendu sur dix » | Fait 3 (Kantar, trois mois à janvier 2014) | ✅ | « Fin 2013 » |
| « dans le monde entier, c'est environ trois pour cent des smartphones vendus. Au mieux. » | Fait 2 ; formulation sûre 8 | ⚠️ | Gardée |
| « [WhatsApp] arrive fin septembre 2011. Onze mois après Windows Phone 7, et un mois avant le premier Lumia. » | Fait 12 | ✅ (billet de WhatsApp) | Gardée |
| « Instagram arrive en novembre 2013. Trois ans après […] une bêta : pas de vidéo, et tu ne peux même pas prendre ta photo dans l'appli » | Fait 13 | ✅ | Gardée |
| « Snapchat, lui, n'a jamais sorti d'appli officielle pour Windows Phone. » | Fait 14 | ⚠️ formulation juste | Gardée |
| « Microsoft a fini par coder sa propre appli YouTube […] en 2013, Google la bloque. En mai, puis encore en août. » | Fait 25 ; **fait 36** (Engadget, BetaNews, 15/08/2013 ; silicon.co.uk) | ⚠️ en mai, c'est une demande de retrait ; la raison de Google (les pubs) manque | Réécrite (grill n° 4) |
| « Fin septembre 2014, d'après Microsoft, il y a environ trois cent quarante mille applis » | Fait 24 | ⚠️ formulation juste | Gardée |
| « Il s'appelle Rudy Huyn. Il avait déjà fait 6tag […] le vingt et un novembre 2013, il sort 6snap : un client Snapchat gratuit pour Windows Phone 8 » | Fait 16 | ✅ | Gardée (« en novembre 2013 ») |
| « c'est la même semaine que la bêta d'Instagram » | Faits 13 et 16 (20 et 21/11/2013) | ✅ rapprochement | Gardée |
| « Un client non officiel, c'est une appli qui parle aux serveurs de Snapchat sans que Snapchat l'ait faite » | **Fait 35** (BuzzFeed News, 14/10/2014, citant Snapchat) | ✅ | Gardée, avec la phrase de Snapchat |
| « En décembre 2014, tous les clients Snapchat non officiels disparaissent du Store, et des comptes sont bloqués. […] la demande ne venait pas de Snapchat » | Fait 17 | ⚠️ sans accuser | Gardée |
| « Et il a même proposé son code à Snapchat. » | Fait 18 | ⚠️ une source | Gardée (onmsft à l'écran) |
| « En octobre 2017, Joe Belfiore, un des chefs de Windows […] : « On a essayé TRÈS FORT… » » | Fait 9 | ⚠️ tweet relayé par la presse, dit comme tel | Gardée (« un des patrons de Windows ») |
| « Quand le chef lui-même te dit… » | Fait 9 | ❌ Belfiore n'est pas « le chef » | Retirée |
| « La presse de l'époque avait un nom pour ça : l'« app gap » » | Fait 26 | ⚠️ terme de presse | Gardée |
| « l'effet de réseau : une appli vaut quelque chose parce que les autres y sont déjà » | **Fait 34** (Niskanen Center, 13/09/2018) | ⚠️ définition de l'effet direct, pas du cercle | Réécrite (grill n° 3) |
| « Pour environ trois pour cent des téléphones du monde » | Fait 2 | ⚠️ des smartphones vendus | Corrigée |
| « En 2012, Windows Phone 8 arrive. Et aucun téléphone Windows Phone 7 ne peut passer à Windows Phone 8 […] le Lumia 900 […] Windows Phone 7.8 » | Fait 21 ; **fait 37** (Engadget, 20/06/2012) | ✅ | « En juin 2012, Microsoft présente Windows Phone 8 » |
| « pour un développeur, c'est la double peine : déjà peu d'utilisateurs, et en plus coupés en deux » | **Fait 37** (phonescoop ; Dice, 21/06/2012) | ✅ dans ce sens : les applis WP7 tournent sur WP8, pas l'inverse | Précisée |
| « En avril 2014, Microsoft rachète la partie téléphones de Nokia, pour environ cinq virgule quatre milliards d'euros » | Fait 22 | ✅ | Gardée |
| « en juillet 2015, il supprime jusqu'à sept mille huit cents postes et efface sept virgule six milliards de dollars sur Nokia » | Faits 23, 38 | ✅ | « sur ce qu'il a acheté à Nokia » |
| « Belfiore écrit aussi qu'ils continuent les correctifs, mais que les nouvelles fonctions et le nouveau matériel ne sont plus la priorité » | Fait 10 | ⚠️ | Gardée |
| « Et fin 2019, Microsoft arrête le support. » | Fait 11 | ✅ | « le support de Windows 10 Mobile, le dernier Windows pour téléphone » |
| « Des applis, il y en a des millions » | Aucune à cette date | ❓ | « des tonnes » |
| « elles étudient ce que tu aimes, et elles vivent de tes données » | Fait 27 | ❓ dit comme ton avis | Gardée comme avis (question 6) |
| « en décembre 1989, il cherchait de quoi s'occuper pendant la semaine de Noël. Il a commencé Python » | `projets/python/sources.md` | ✅ | Gardée |

**Ce que j'ai corrigé** : le hook (Microsoft seul, « effacés de ses comptes », « capteur ») ; le 3310 (mème) ; l'effet de réseau (indirect) ; le client non officiel (sourcé) ; YouTube (mai = demande de retrait, raison de Google dite) ; Windows Phone 8 (« présente » en juin 2012) et la double peine (sens de la compatibilité) ; « le chef » retiré ; « trois pour cent des téléphones » → des smartphones vendus ; « début 2014 » → fin 2013 ; « presque jamais l'appli Téléphone » et « des millions » retirés.
**Lignes ajoutées à `sources.md`** : 33 (3310), 34 (effet de réseau), 35 (client non officiel), 36 (YouTube), 37 (Windows Phone 7 → 8), 38 (les deux chiffres du hook, relus). Rien n'a été effacé.

## Ce qu'il faut garder

- **« Ces bonbons pour ton cerveau. Tes applications. »** Ta phrase, et la plus jolie du script.
- **Le jeu multi sans joueurs** (« Recherche de joueurs : une minute, trois minutes, sept minutes… personne ») : l'effet de réseau compris en dix secondes, dans ton registre.
- **« Tu peux payer une appli, mais tu ne peux pas payer des millions de gens pour qu'ils viennent dessus. »** La seule morale du script qui mérite sa place ; `script.md` la récolte en section 6.
- **« Donc le Store était vide. Même pas. »** : le retournement le plus utile de la vidéo, parce qu'il dit ton sous-texte avec un chiffre.
- **« Un téléphone sans Insta, pour un lycéen de 2013, c'est un téléphone de daron. »** Ton humour, et ton public.
- **« Imagine : t'as un téléphone à quarante et un mégapixels, et pour poster sur Insta, tu fais ta photo à côté »** : la récolte des 41 Mpx qui fait rire.
- **Le « signal fort » suivi de la coupure et de Belfiore** : la meilleure relance à 60 % des scripts du dépôt.
- **L'icône Téléphone avec sa toile d'araignée**, et l'écran d'accueil qui se vide puis se remplit.

## Plan d'action (appliqué dans `script.md`)

1. **Hook** : la brique, le 7,6 Md$ dit juste avant 15 s, une seule question, un pont vers Rudy Huyn.
2. **Les corrections** : une seule à voix haute (WhatsApp, comme ce que tu croyais), les autres dites juste.
3. **Les faits** : les trois ajouts sourcés ou réécrits, YouTube complété, la double peine précisée (lignes 33 à 38 de `sources.md`).
4. **La fin** : un seul retour à la brique, avec ta question du début.
5. **Passe de détail** : l'abonnement dans le récit, les « donc » de la section 5, les rafales de la section 6, tes « en effet ».

## Les questions pour toi

Elles sont aussi en bas de `script.md`.

1. **« Pour que sa meuf puisse l'utiliser »** : d'où tiens-tu ce motif ? Sans lien (interview, vidéo de Rudy Huyn), on le coupe.
2. **« Nokia c'était quand même pas goat »** : (a) « c'était le GOAT des téléphones » ou (b) « pas le meilleur en smartphones » ?
3. **« Le rendre fermé »** : la licence payante jusqu'en avril 2014 (phrase prête), ou autre chose ?
4. **La pub Nokia Lumia** : laquelle, et avec quels droits ?
5. **Ton vécu** : un Lumia autour de toi ? Et ton appli sans laquelle ton téléphone est une brique ?
6. **La phrase sur les données** : on la garde comme ton avis, ou seulement la question ?
7. **L'aveu WhatsApp** (« j'étais persuadé que… ») : ça te va de le dire ?
8. **« Passionné »** pour Rudy Huyn, dit comme ton regard : ça te va ?
