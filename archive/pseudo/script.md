# Pseudo déjà pris : script final

**Titre** : *Comment un site sait en une milliseconde que ton pseudo est déjà pris* (ton choix du 23/10). Le hook le tient **côté serveur** : une vérification de ce genre prend moins d'une milliseconde d'après la doc de Redis (fait 33, vérifié deux fois). On ne dit jamais que le site te répond en une milliseconde : ce que tu attends, c'est surtout le réseau.

**Durée** : environ 1 625 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft) : environ 11 min 12 ; à 165 mots/min : environ 9 min 50 ; en coupes serrées comme sur Uber (~180 mots/min) : environ 9 min, plus les pauses du montage. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : la petite croix rouge « déjà pris ». On part de la méthode bête (comparer à tout le monde), on passe par ce que font vraiment les sites (un index unique, la base qui tranche), puis par l'astuce qu'on enseigne (le filtre de Bloom, le videur qui ne se trompe que dans un sens). Le retournement : le videur ne sait jamais dire « pris » tout seul, donc ton rouge vient toujours de la base. Ensuite, ceux qui l'ont vraiment embauché, et ceux qui l'ont mis à la porte. Retour à la croix rouge à la fin.

**Changements depuis la V1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- **Hook** : « En fait, il a un index » répondait à la question centrale dès 0:17. L'index passe en une demi-phrase (« Normalement, avec un index. Mais… ») et l'astuce devient la promesse : elle peut répondre sans ouvrir un seul compte, et elle a le droit de se tromper. « Medium s'en est servi pendant dix ans » devient « une dizaine d'années » (usage attesté en juin 2015, retrait en 2025 : `sources.md`, ligne 30).
- **Le retournement du videur** (section 3, nouveau) : on demande au spectateur ce que répond le videur quand le pseudo est vraiment pris. Réponse : « peut-être ». Son seul « non » sûr, c'est « pas pris » : ton « déjà pris » vient toujours de la base. Ça rend la miniature « il triche. » honnête (il triche sur les pseudos libres) et ça prépare la fin.
- **Le clin d'œil Claude est retiré** de la voix off. À la place, l'image du videur est créditée à l'ingénieur de Medium dès qu'elle arrive (section 3), puis récoltée dans la section 5 (« Raphael Montaud, l'ingénieur du videur »).
- **Suppression dans un filtre** : la case éteinte fait maintenant mentir le seul « non » sûr (« zorro » sortirait « jamais ajouté ») : on récolte la règle de la section 3.
- **Formulations recalées sur les sources** : « des vidéos te citent Google, Facebook ou Amazon » (ByteMonk dit Facebook, pas Meta) ; « on n'a trouvé aucun blog… » au lieu de « aucun blog ne dit » ; « on a cherché » et « ils ont publié leurs chiffres » au lieu de « j'ai cherché » et « j'ai retrouvé » ; « souvent pour rien » retiré (fréquence non sourcée) ; Chrome « face à une simple liste » ; Sarah, « la juriste de Medium » ; Medium « servait » (c'est fini).
- **Akamai** : « soixante-quatorze pour cent » deux fois de suite pour deux chiffres différents ; le premier devient « presque trois objets sur quatre ».
- **Appel à l'abonnement** déplacé juste après le pont vers Burton Bloom : il tombe pendant une boucle ouverte, plus sur une réponse.
- **Tics retirés** : « Ouais, t'as bien entendu » (phrase d'exemple du skill, tirée de Cam), « Petit détail pour finir », « Ailleurs. », un des trois « honnête ».
- **Liaisons** : rafale de dix phrases sans liaison de la section 5 cassée (« parce que », « du coup », « en gros », « voilà pourquoi ») ; deux « en effet » (ton mot).
- **Fin** : le videur « hausse les épaules et passe la question à la base », raccord avec le retournement. **Écran de fin vers Waze** (sorti le 9/11), avec une phrase-pont sur le faux bouchon de 2014 ; Uber si le pseudo sort plus tôt comme joker.
- Gag pop sur « kirito » libre (section 3).
- **Coupes pour la durée** (environ 60 mots) : Cassandra, le 0,1 % → 1,8 Go, la phrase « Sur Technovore, j'ouvre comme ça… » de la fin.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = motion design (Remotion ou HyperFrames). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Aucun grand site n'est nommé pour les pseudos (`sources.md`, fait 15).

---

## 0. Hook (0:00 – 0:36) · objectif : 75 % à 0:15

[VISUEL : un formulaire d'inscription sombre, plein écran. On tape « technovore ». Le champ vire au rouge avant même la dernière lettre : « Ce nom est déjà pris. » Pas de titre, pas de logo.]
[SON : le « bonk » d'erreur, sec.]

Tu tapes ton pseudo, et avant même la dernière lettre : « Déjà pris. » Instantanément. En fait, côté serveur, ce genre de vérification prend moins d'une milliseconde.

[VISUEL : un chrono « < 1 ms » s'affiche au-dessus du champ rouge. En petit : « côté serveur · exemple : doc de Redis ».]

Sauf que derrière ce formulaire, imagine un milliard de comptes. Le site n'a pas eu le temps de les regarder un par un. Alors comment il sait ?

[VISUEL : dézoom : derrière le champ, un mur de comptes à perte de vue ; une loupe qui n'a même pas le temps de bouger.]

Normalement, avec un index. Mais il existe une astuce plus rapide, inventée en mille neuf cent soixante-dix, qui peut te répondre sans ouvrir un seul compte. Et qui a le droit de se tromper. Exprès.

[VISUEL : une rangée de cases grises ; trois s'allument d'un coup. Arrêt sur image.]

Et Medium s'en est servi pendant une dizaine d'années… avant de la jeter.

---

## 1. Le pseudo que tu n'as jamais pu avoir (0:36 – 1:25)

Si tu as déjà joué en ligne, tu connais. Tu trouves LE pseudo, celui qui claque. Le jeu te répond : déjà pris. Du coup tu ajoutes un tiret du bas. Pris. Ton année de naissance. Pris aussi. Et tu finis en « xX_Technovore_2007_Xx », comme tout le monde.

[VISUEL : le champ qui se remplit de tirets, de chiffres et de « Xx » ; la croix rouge à chaque essai, de plus en plus vite.]
[SON : un « bonk » par essai, qui accélère.]

[LE PSEUDO QUE TU N'AS JAMAIS PU AVOIR, ET CE QUE TU AS PRIS À LA PLACE. UNE OU DEUX PHRASES.]

Moi, ce qui m'intéresse, c'est ce qui se passe entre ta dernière lettre et le rouge. Donc on ouvre le capot.

La méthode bête, c'est de prendre ton pseudo et de le comparer à chaque compte. Le premier, le deuxième, le troisième… jusqu'au milliardième. Et ça, pour une seule personne qui s'inscrit.

[VISUEL : un compteur « comparaisons » qui défile et s'emballe ; une barre de chargement qui n'avance pas.]

Forcément, personne ne fait ça. Ce que les sites font vraiment, tu l'as déjà eu entre les mains : un dictionnaire.

---

## 2. Ce que fait vraiment le site : l'index (1:25 – 3:09)

[VISUEL : titre de chapitre « 1. L'index ».]

Tu te rappelles les dictionnaires papier ? Pour trouver « pseudo », tu ne lisais pas tout depuis la lettre A. Tu ouvrais au milieu, tu tombais sur « M », donc tu allais plus loin. Puis « R », tu revenais un peu. Et en quelques gestes, tu y étais.

[VISUEL : un dictionnaire qui s'ouvre, se referme, se rouvre ; un compteur « gestes : 1, 2, 3 ».]

Une base de données fait pareil, avec ce qu'on appelle un arbre B. Les pseudos sont rangés dans l'ordre, par paquets, et chaque paquet dit où chercher la suite. Résultat : même parmi un milliard de pseudos, la base retrouve le tien en quelques lectures. Quelques-unes, sur un milliard.

[VISUEL : un arbre à trois étages ; un chemin s'allume de la racine jusqu'à « technovore ». Bandeau « Pour les devs : B-tree ».]

Et cet index a un deuxième boulot, le plus important. Sur PostgreSQL, par exemple, quand le dev écrit « ce pseudo doit être unique », la base crée toute seule un index unique. Et c'est lui qui fait respecter la règle.

Du coup, tu vois le cas où deux personnes valident « technovore » à la même seconde ? La base refuse le doublon. Une seule inscription passe, l'autre se prend le rouge.

[VISUEL : deux mains qui cliquent sur « S'inscrire » en même temps ; un seul ✓, un ✗.]
[SON : un « ding » et un « bonk », collés.]

Voilà la première réponse à « comment il sait » : un index, et la base qui tranche.

Sauf que chaque question, même rapide, va jusqu'à la base. Et quand le pseudo est libre, elle a fouillé… pour ne rien trouver. En mille neuf cent soixante-dix, un chercheur, Burton Bloom, publie une idée au titre qui dit tout : gagner de la place et du temps… en autorisant des erreurs.

[VISUEL : la couverture de l'article de 1970, le titre surligné : « Space/time trade-offs in hash coding with allowable errors ».]

Si tu aimes voir ce qu'il y a derrière les petits trucs de tous les jours, abonne-toi. Sur Technovore, on ouvre les applis une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; le titre de Bloom reste à l'écran.]

---

## 3. Le videur qui ne se trompe que dans un sens (3:09 – 6:31)

[VISUEL : titre de chapitre « 2. L'astuce ». Trente-deux cases grises en rangée.]
[SON : ding de chapitre.]

Le filtre de Bloom, pour faire simple, c'est une rangée de cases, toutes éteintes, et quelques fonctions de hachage. Une fonction de hachage, c'est une moulinette : tu lui donnes un mot, elle te sort un numéro. Toujours le même numéro pour le même mot.

[VISUEL : « technovore » entre dans trois moulinettes ; elles crachent 4, 19 et 27.]

Quand quelqu'un prend « technovore », on le passe donc dans trois moulinettes. Elles donnent quatre, dix-neuf et vingt-sept. Du coup, on allume ces trois cases. Et on ne garde même pas le pseudo : juste les cases.

[VISUEL : les cases 4, 19 et 27 s'allument.]
[SON : trois « tic » lumineux.]

Maintenant, tu tapes « kirito ». Les moulinettes donnent deux, dix-neuf et trente. Et là, la case deux est éteinte. Le filtre sait une chose à cent pour cent : « kirito » n'a jamais été ajouté. Parce que s'il l'avait été, la case deux serait allumée. Donc réponse : sûrement pas pris. Et la base n'est même pas dérangée.

[VISUEL : la case 2 clignote, éteinte ; tampon vert « SÛREMENT PAS PRIS ».]

Bon, dans notre base à un seul compte, hein. Dans la vraie vie, « kirito » libre, tu peux toujours rêver.

[VISUEL : gag d'une seconde : « kirito » libre ? un emoji qui pleure de rire.]

Mais avec le temps, d'autres pseudos allument d'autres cases. Un jour, tu tapes un pseudo tout neuf. Personne ne l'a jamais pris, et pourtant ses trois cases sont déjà allumées par d'autres. Le filtre ne peut pas faire la différence. Il répond : peut-être pris.

[VISUEL : trois cases allumées, chacune reliée par un fil de couleur à un autre pseudo (« zorro », « lea_92 », « ninja »). Tampon orange « PEUT-ÊTRE ».]

Voilà l'erreur autorisée de Burton Bloom. Le « non » est sûr. Le « peut-être » peut mentir.

En fait, ce mensonge ne coûte presque rien. Le « peut-être » déclenche juste la vérification dans la base qu'on aurait faite de toute façon.

Un ingénieur de Medium a une image pour ça, et je te la pique : un videur de boîte de nuit, avec une très bonne mémoire, mais pas parfait. Imagine-le devant la base. Les « non », il les règle lui-même, à la porte, sans déranger personne. Les « peut-être », il les envoie à l'accueil, qui vérifie la vraie liste.

[VISUEL : une file de pseudos devant un videur ; voie rapide verte pour les « non », couloir orange vers la base pour les « peut-être ». Petite mention en bas : « image : Raphael Montaud, Medium, 2025 ».]

Et le videur ne prend presque pas de place. Avec un pour cent d'erreur, il faut moins de dix cases par pseudo, et à peu près sept moulinettes. Que ton pseudo fasse cinq lettres ou trente, c'est pareil. Du coup, un milliard de pseudos tiennent dans environ un virgule deux gigaoctet.

[VISUEL : un curseur « erreurs » ; on le baisse, la rangée de cases s'allonge. Calcul à l'écran : « 1 % → 1,2 Go ».]

Maintenant, prends deux secondes. Ton pseudo est vraiment pris. Qu'est-ce que le videur te répond ?

[VISUEL : « technovore » face au videur ; un compte à rebours de deux secondes.]
[SON : tic-tac, deux coups.]

Peut-être. Son seul « non » sûr, c'est « pas pris ». Donc ton « déjà pris » en rouge, c'est toujours la base qui l'a décidé, derrière lui. En fait, le videur ne triche que quand ton pseudo est libre : là, il te répond sans aller voir.

[VISUEL : tampon orange « PEUT-ÊTRE » sur « technovore » ; flèche vers la base, qui tamponne « PRIS » en rouge. Puis « kirito » : tampon vert direct, la base reste éteinte.]

Alors, c'est comme ça que ton site vérifie ton pseudo ? Honnêtement, je ne sais pas. C'est la technique qu'on enseigne pour ce problème, dans les tutos et les entretiens d'embauche de dev. Sur YouTube, des vidéos te citent Google, Facebook ou Amazon. Sauf qu'on a cherché, et on n'a trouvé aucun blog d'ingénierie ni aucune conférence d'un grand site qui dise s'en servir pour les pseudos. Donc je ne vais pas te l'inventer.

[VISUEL : « Google ? Facebook ? Amazon ? » ; chaque nom reçoit un tampon gris « AUCUNE SOURCE ».]

Par contre, ce videur, des grands l'ont bien embauché, pour d'autres portes. Et eux, ils ont publié leurs chiffres.

---

## 4. Qui l'a vraiment embauché (6:31 – 8:34) · relance à 60 %

[SON : la musique change, plus rythmée.]
[VISUEL : titre de chapitre « 3. Les vrais clients du videur ».]

En deux mille six, Google publie le papier de Bigtable, une de ses bases de données géantes. Dedans, une phrase : grâce aux filtres de Bloom, la plupart des recherches de lignes qui n'existent pas ne touchent même pas le disque. Tu vois le lien ? C'est notre « sûrement pas pris », version Google.

[VISUEL : capture du papier Bigtable, la phrase surlignée.]

Akamai, un des grands réseaux qui livrent les pages web, a mesuré un truc fou. Sur quarante-cinq serveurs, en deux jours, presque trois objets sur quatre, parmi quatre cents millions, n'ont été demandés qu'une seule fois. Les ingés les appellent les « one-hit wonders », les chanteurs d'un seul tube. Forcément, les garder en cache, c'est gâcher de la place. Donc le filtre retient ce qui est déjà passé une fois, et le serveur ne garde un fichier qu'à sa deuxième demande. Et en effet, sur environ quarante-sept serveurs, le cache passe d'à peu près soixante-quatorze à quatre-vingt-trois pour cent de réussite.

[VISUEL : un tas de fichiers ; les trois quarts s'effacent en gris (« vus une fois ») ; puis, dans une autre couleur, une jauge de cache qui monte de 74 à 83 %.]

Et puis il y a Medium, la plateforme de blogs. Chez eux, tout commence à un dîner d'anniversaire : Sarah, la juriste de Medium, demande à Jamie Talbot comment le site sait si quelqu'un a déjà lu un article. Et là, en plein repas, il lui dessine un filtre de Bloom sur des serviettes. C'est lui qui le raconte, en deux mille quinze.

[VISUEL : une serviette en papier, des cases dessinées au stylo qui s'allument une à une.]

Chez Medium, ces filtres servaient à ne pas te remontrer un article déjà lu, un auteur que tu as masqué, ou une histoire qu'on t'a déjà proposée trois fois. Jusqu'à quinze mille questions au filtre pour un seul fil d'actualité. Plus de quinze millions par seconde au total.

[VISUEL : « 15 000 » pour un fil, puis un compteur « 15 000 000 / s » qui tourne.]

Quinze millions par seconde, juste pour savoir si tu as déjà lu un article. Là, tu comprends pourquoi on veut un videur rapide.

Et pourtant, dix ans après la serviette, Medium l'a mis à la porte.

---

## 5. Ceux qui l'ont mis à la porte (8:34 – 10:13)

[SON : la musique coupe net, une seconde de silence.]

Et Medium n'est pas le premier à le mettre dehors. En deux mille onze déjà, un développeur de Chrome, Scott Hess, propose de remplacer le filtre de Bloom qui gardait la liste des sites dangereux. Parce que face à une simple liste, le filtre ne fait gagner que vingt-deux pour cent de place. Et son remplaçant prend un tiers de mémoire en moins… sans jamais se tromper. Et en effet, le remplacement commence cette année-là. En gros, le videur prenait presque autant de place qu'une liste, et en plus, il mentait.

[VISUEL : deux barres côte à côte, « Bloom » et « PrefixSet » ; la seconde est un tiers plus courte, avec « 0 erreur ».]

Pour Medium, donc, c'est en deux mille vingt-cinq. Raphael Montaud, l'ingénieur du videur, raconte pourquoi ils ont retiré leurs filtres. Ils avaient grossi jusqu'à des milliards d'éléments. Et surtout, on ne peut rien effacer d'un filtre de Bloom.

Tu te rappelles les cases allumées ? Une case peut servir à plusieurs pseudos à la fois. Si tu l'éteins pour en retirer un, tu abîmes aussi les autres. Du coup, « zorro », qui existe bien, sortirait « jamais ajouté ». Et le seul « non » sûr du videur deviendrait faux.

[VISUEL : on éteint la case 19 pour retirer « technovore » ; « zorro » perd aussi sa case, tampon vert « JAMAIS AJOUTÉ » barré ; alarme rouge.]

Voilà pourquoi, chez Medium, un auteur que tu avais masqué, puis démasqué, restait masqué pour toujours. Le videur avait une super mémoire, mais impossible de lui faire oublier quelqu'un. Et sans les filtres, en interrogeant directement leur vraie base, ils disent payer dix fois moins cher. Bon, l'auteur précise lui-même que la comparaison n'est pas forcément équitable.

[VISUEL : « ×10 moins cher » qui tombe, puis un astérisque géant : « comparaison pas forcément équitable » (Medium, 2025).]

Bref, revenons à ta croix rouge.

---

## 6. Fin (10:13 – 11:12)

[VISUEL : retour au formulaire du début, « technovore », la croix rouge.]

La prochaine fois que tu vois « déjà pris » avant même d'avoir fini de taper, tu sauras ce qui a pu se passer. Peut-être un index qui a trouvé ton pseudo en quelques lectures. Peut-être un videur qui a regardé trois cases, haussé les épaules, et passé la question à la base. Mais dans les deux cas, ton rouge, c'est la base qui l'a mis.

Et c'est justement elle qui rattrape les défauts du videur. Si un site utilisait un filtre et qu'un pseudo se libérait, le filtre dirait encore « peut-être pris ». La base, elle, répondrait : en fait, il est libre.

[OPTIONNEL : TON AVIS EN UNE PHRASE. TU METTRAIS UN FILTRE DE BLOOM DEVANT TA BASE, TOI ?]

Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et en parlant d'erreurs : en deux mille quatorze, des chercheurs ont fait croire à Waze à un bouchon qui n'existait pas, avec de faux conducteurs. C'est la vidéo juste là.

[VISUEL : écran de fin, 20 s : vidéo Waze à gauche, bouton « S'abonner » à droite. Si le pseudo sort plus tôt comme joker (avant le 9/11, Waze pas encore en ligne) : vidéo Uber, et la phrase devient « Et si tu veux voir comment Uber fait glisser ses petites voitures sur ta carte, c'est la vidéo juste là. »]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel | La croix rouge avant la dernière lettre (l'image de la miniature) |
| 0:14 | Question centrale | « Alors comment il sait ? » sur le mur d'un milliard de comptes |
| 0:18 | Promesse | Une astuce qui répond sans ouvrir un seul compte, et se trompe exprès |
| 0:31 | Pont | Medium s'en est servi une dizaine d'années, puis l'a jetée (refermée à 8:29) |
| 0:40 | Humour gamer | « xX_Technovore_2007_Xx », un « bonk » par essai |
| 1:04 | Visuel | Le compteur de comparaisons qui s'emballe |
| 1:25 | Lien au vécu | Le dictionnaire papier |
| 2:19 | Mini-scène | Deux inscriptions à la même seconde, un ✓ et un ✗ |
| 2:37 | Retournement | « Sauf que chaque question va jusqu'à la base », puis Burton Bloom, « en autorisant des erreurs » |
| 2:58 | Appel à l'action | Abonnement (≈ 26 %), boucle ouverte |
| 3:27 | Visuel | Les moulinettes, trois cases qui s'allument |
| 3:42 | Révélation | « kirito » : la case éteinte, le « non » sûr |
| 4:04 | Gag | « kirito » libre, tu peux toujours rêver |
| 4:12 | Retournement | Le pseudo neuf qui sort « peut-être pris » |
| 4:45 | Personnage | Le videur et ses deux files, crédité à un ingénieur de Medium (récolté à 9:15) |
| 5:09 | Chiffre | Un milliard de pseudos dans 1,2 Go |
| 5:30 | Devinette | « Ton pseudo est vraiment pris : que répond le videur ? » Deux secondes de silence |
| 5:36 | Retournement | « Peut-être » : ton « déjà pris » vient toujours de la base |
| 5:53 | Aveu | « Honnêtement, je ne sais pas » : les géants tamponnés « aucune source » |
| 6:31 | Changement de musique | Relance (≈ 58 %) : qui l'utilise vraiment |
| 6:52 | Chiffre | Akamai, presque trois objets sur quatre vus une seule fois |
| 7:34 | Anecdote | Le filtre dessiné sur des serviettes |
| 8:16 | Chiffre | 15 millions de questions par seconde, et la réaction |
| 8:29 | Coupure musique | « Et pourtant… Medium l'a mis à la porte », puis Chrome |
| 9:28 | Récolte | La case éteinte fait mentir le seul « non » sûr |
| 9:47 | Gag | L'auteur masqué pour toujours |
| 10:10 | Boucle fermée | Retour à la croix rouge |
| 10:39 | Retournement final | Le pseudo libéré : le filtre dit « peut-être », la base dit « libre » |
| 10:54 | Appel à l'action | « Quelle appli je décortique ensuite ? » puis le faux bouchon de Waze |

**Total** : 29 relances en 11 min 12 (à 145 mots/min), environ une toutes les 23 secondes ; la plus longue plage sans relance fait environ 40 s (6:52 – 7:34, Akamai).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15-0:30 | Faible | « Normalement, avec un index » pourrait sembler répondre trop tôt | Une demi-phrase seulement, aussitôt suivie du « Mais » et de l'astuce qui a le droit de se tromper, puis de Medium qui l'a jetée |
| Section 2, l'arbre B | Moyen | Le mot « arbre B » peut perdre les non-devs | Le dictionnaire porte l'explication ; « arbre B » reste un bandeau pour les devs |
| Fin de la section 2 | Moyen | « Voilà la première réponse » ferme une boucle | Le « Sauf que » et Burton Bloom ouvrent la suivante avant l'appel à l'abonnement |
| Section 3, les hachages | Élevé | Le bloc le plus abstrait de la vidéo | Deux exemples seulement (« technovore », « kirito »), le gag « kirito », des cases qui s'allument, puis le videur |
| Section 3, « je ne sais pas » | Moyen | L'aveu peut sembler casser la promesse | Il arrive juste après le retournement (le videur ne dit jamais « pris ») et ouvre « qui l'utilise vraiment ? », à quoi la section 4 répond tout de suite avec des chiffres |
| Relance (~60 %) | Élevé | Chute classique, et quatre exemples d'affilée | Changement de musique, un chiffre ou une image par exemple, la serviette, puis la coupure musicale de la section 5 |

## Notes de montage

- **Composants à construire une fois** : la rangée de 32 cases (elle sert aux sections 3, 5 et 6), les trois moulinettes, le videur avec ses deux files, le formulaire du hook. Animations simples : c'est une vidéo légère.
- **Le formulaire** : générique, en motion design, sans logo de site réel. Pas de « G » de Google, ni sur la miniature ni à l'écran (`sources.md`, ligne 24).
- **Le retournement** (section 3) : laisse vraiment deux secondes de silence après « Qu'est-ce que le videur te répond ? ». Le spectateur doit avoir le temps de se tromper.
- **Le crédit du videur** : petite mention à l'écran (« image : Raphael Montaud, Medium, 2025 ») la première fois qu'il apparaît ; elle revient en section 5 sur « l'ingénieur du videur ».
- **La section « je ne sais pas »** : les noms Google, Facebook, Amazon n'apparaissent qu'avec le tampon « aucune source ». Ne pas montrer la miniature ni le titre de la vidéo de ByteMonk.
- **Akamai** : les « trois quarts » et la jauge 74 → 83 % dans deux couleurs différentes, pour qu'on ne confonde pas les deux chiffres.
- **Captures autorisées** : le papier Bigtable (USENIX), la revue de code Chromium, les deux billets de Medium (2015 et 2025), la doc PostgreSQL.
- **Énergie** : calme et joueuse jusqu'à la fin de la section 2, montée sur les cases qui s'allument, rythme plus vif dans la section 4, coupure nette au début de la section 5.
- **Le gag des pseudos** (section 1) : il peut piocher dans ta vraie liste de pseudos refusés, à l'écran.
- **Miniature** : `noir-07.png`, « il triche. », sans le « G ». La vidéo tient la promesse : le filtre répond sans regarder la base quand le pseudo est libre, et le script dit qu'on ne sait pas quel site le fait.

## Faits utilisés

| Fait (`sources.md`) | Phrase du script |
|---|---|
| 1 | « inventée en mille neuf cent soixante-dix » ; « un chercheur, Burton Bloom, publie une idée au titre qui dit tout : gagner de la place et du temps… en autorisant des erreurs » |
| 2 | « une rangée de cases, toutes éteintes, et quelques fonctions de hachage » ; « on allume ces trois cases » ; « La case deux est éteinte… n'a jamais été ajouté » |
| 3, 29 | « Le "non" est sûr. Le "peut-être" peut mentir. » ; « Les "peut-être", il les envoie à l'accueil, qui vérifie la vraie liste. » ; le retournement : « son seul "non" sûr, c'est "pas pris". Donc ton "déjà pris" en rouge, c'est toujours la base qui l'a décidé » (déduction directe de la ligne 29) |
| 4 | « on ne peut rien effacer d'un filtre de Bloom » ; « "zorro", qui existe bien, sortirait "jamais ajouté" » (conséquence de la raison donnée au fait 4) |
| 5 | « moins de dix cases par pseudo, et à peu près sept moulinettes » ; « Que ton pseudo fasse cinq lettres ou trente, c'est pareil » ; « un virgule deux gigaoctet » |
| 6 | « la plupart des recherches de lignes qui n'existent pas ne touchent même pas le disque » |
| 8 | « Sur quarante-cinq serveurs, en deux jours, presque trois objets sur quatre, parmi quatre cents millions, n'ont été demandés qu'une seule fois » (74 %) ; « one-hit wonders » ; « ne garde un fichier qu'à sa deuxième demande » |
| 9 | « sur environ quarante-sept serveurs, le cache passe d'à peu près soixante-quatorze à quatre-vingt-trois pour cent de réussite » |
| 10 (⚠️) | « En deux mille onze déjà, un développeur de Chrome, Scott Hess, propose de remplacer… face à une simple liste… vingt-deux pour cent… un tiers de mémoire en moins… sans jamais se tromper. Et en effet, le remplacement commence cette année-là. » (1,27 / 1,93 ≈ 0,66 ; pas d'unité dite, pas d'« abandonné ») |
| 11 | « ces filtres servaient à ne pas te remontrer un article déjà lu, un auteur que tu as masqué, ou une histoire qu'on t'a déjà proposée trois fois » |
| 12 | « des milliards d'éléments » ; « restait masqué pour toujours » ; « dix fois moins cher… pas forcément équitable » ; « leur vraie base » (sans nommer DynamoDB) |
| 13 | « la base crée toute seule un index unique. Et c'est lui qui fait respecter la règle. » |
| 15, 16 (❓, ⚠️) | « C'est la technique qu'on enseigne pour ce problème… Sur YouTube, des vidéos te citent Google, Facebook ou Amazon. Sauf qu'on a cherché, et on n'a trouvé aucun blog d'ingénierie ni aucune conférence d'un grand site qui dise s'en servir pour les pseudos. » |
| 18 (⚠️) | « la base retrouve le tien en quelques lectures » (pas « 3 à 4 ») |
| 20 | « Le "peut-être" déclenche juste la vérification dans la base qu'on aurait faite de toute façon. » |
| 21 (⚠️) | « La base refuse le doublon. Une seule inscription passe » |
| 22 (⚠️) | « Le site n'a pas eu le temps de les regarder un par un… Normalement, avec un index. Mais il existe une astuce encore plus rapide, qui peut te répondre sans ouvrir un seul compte… qui a le droit de se tromper. » (« un milliard » présenté comme hypothèse, « imagine », comme dans le calcul du fait 5) |
| 26 | « Sarah, la juriste de Medium, demande à Jamie Talbot comment le site sait si quelqu'un a déjà lu un article… il lui dessine un filtre de Bloom sur des serviettes » |
| 28 | « Jusqu'à quinze mille questions au filtre pour un seul fil d'actualité. Plus de quinze millions par seconde au total. » |
| 30 (ajouté au grill) | « Medium s'en est servi pendant une dizaine d'années… avant de la jeter » ; « dix ans après la serviette » |
| 31 (ajouté au grill) | « Un ingénieur de Medium a une image pour ça… un videur de boîte de nuit, avec une très bonne mémoire, mais pas parfait » ; « Raphael Montaud, l'ingénieur du videur » |
| 32 (ajouté au grill) | « en deux mille quatorze, des chercheurs ont fait croire à Waze à un bouchon qui n'existait pas, avec de faux conducteurs » |

**Non utilisés, exprès** : 7 (Cassandra, coupée au grill : un deuxième « fait pareil » après Bigtable, dans la liste de la section 4) ; le 0,1 % → 1,8 Go du fait 5 (coupé pour la durée) ; 14, 23, 25 (« le site répond en une milliseconde », « 0,001 s » : sans mesure ; le hook dit « côté serveur, moins d'une milliseconde », fait 33) ; 17 (la chaîne filtre → cache → base, modèle pédagogique) ; 19 (Instagram, Spanner) ; le filtre à compteurs (fait 4, Wikipédia seulement) ; 27 (l'analogie demandée à Claude : retirée de la voix off au grill, voir la question 5).

**Phrases à toi de valider** (déductions ou blagues, pas des citations) :
- La fin (« si un pseudo se libérait… la base répondrait : il est libre ») est un raisonnement tiré des faits 3, 4 et 20, au conditionnel.
- « dans les tutos et les entretiens d'embauche de dev » : déduit des vidéos de référence de `sources.md` (le Short « Interview » de KodeKloud, avec l'exemple du pseudo ; Engineering Digest) et du tutoriel OneUptime.
- « Dans la vraie vie, "kirito" libre, tu peux toujours rêver » : une blague, pas une mesure. Change le pseudo si tu en veux un autre.
- « le videur prenait presque autant de place qu'une liste, et en plus, il mentait » : 22 % gagnés seulement face à la liste, et des faux positifs que le PrefixSet n'a pas (fait 10). C'est un résumé, au ton de la blague.

## Questions pour l'auteur

1. **Ton pseudo** (section 1) : quel pseudo tu n'as jamais pu avoir, sur quel jeu, et ce que tu as pris à la place ? C'est ta seule matière perso de la vidéo ; sans elle, le gag « xX_Technovore_2007_Xx » reste générique. Si « kirito » (l'exemple de la section 3) est un de tes vrais pseudos, dis-le : la blague devient ton anecdote.
2. **Tu as déjà codé une vérification de pseudo** (un formulaire, un index unique dans une de tes bases) ? Si oui, une phrase dans la section 2 te mettrait dans le récit, sans montrer d'appli de travail.
3. **« En une milliseconde »** : réglé le 23/10. Tu gardes le titre, et le hook dit « côté serveur, moins d'une milliseconde » (fait 33). Si tu veux montrer ce que voit le visiteur, mesure-le toi-même dans les outils réseau du navigateur : ce sera plus long, à cause du réseau.
4. **L'écran de fin** : tranché pour Waze (sorti le 9/11, la vidéo génie la plus récente, et elle pointe déjà vers Uber : pseudo → Waze → Uber). Uber seulement si le pseudo sort plus tôt comme joker. D'accord ?
5. **Le clin d'œil Claude** (retiré) : Montaud dit avoir demandé l'analogie du videur à Claude. C'est sourcé, mais placé à 9:10 il retardait la fin, et dire « même l'analogie a été générée » dans un script qu'on veut le plus humain possible jouait contre toi. Si tu y tiens, mets-le dans la description ou en commentaire épinglé, ou dis-le avec ton mot à toi dans la section 5.
