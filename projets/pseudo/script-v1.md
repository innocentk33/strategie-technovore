# Pseudo déjà pris : script v1

**Titre** : *Comment un site sait instantanément que ton pseudo est déjà pris* (« en une milliseconde » n'a pas de mesure : fiche, corrections du 23/10)

**Durée** : environ 1 500 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft) : environ 10 min 20 ; à 165 mots/min : environ 9 min 05. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Fil rouge** : la petite croix rouge « déjà pris ». On part de la méthode bête (comparer à tout le monde), on passe par ce que font vraiment les sites (un index unique, la base qui tranche), puis par l'astuce qu'on enseigne (le filtre de Bloom, le videur qui ne se trompe que dans un sens), ceux qui l'utilisent vraiment, et ceux qui l'ont mis à la porte. Retour à la croix rouge à la fin.

**Boucles ouvertes** :
1. « Comment il sait, sans regarder tous les comptes ? » (hook, refermée en deux temps : l'index dans la section 2, le filtre dans la section 3).
2. « Une astuce qui accepte de se tromper, exprès » (hook, refermée dans la section 3 : le « peut-être »).
3. « Medium l'a jetée en 2025 » (hook, refermée dans la section 5).
4. « Qui l'utilise vraiment pour les pseudos ? » (section 3, réponse honnête : personne ne le dit publiquement ; les usages sourcés sont dans la section 4).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = motion design (Remotion ou HyperFrames). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Aucun grand site n'est nommé pour les pseudos (`sources.md`, fait 15).

---

## 0. Hook (0:00 – 0:31) · objectif : 75 % à 0:15

[VISUEL : un formulaire d'inscription sombre, plein écran. On tape « technovore ». Le champ vire au rouge avant même la dernière lettre : « Ce nom est déjà pris. » Pas de titre, pas de logo.]
[SON : le « bonk » d'erreur, sec.]

Tu tapes ton pseudo, et avant même d'avoir fini : « Déjà pris. » Instantanément.

Sauf que derrière ce formulaire, imagine un milliard de comptes. Le site n'a pas eu le temps de les regarder un par un. Alors comment il sait ?

[VISUEL : dézoom : derrière le champ, un mur de comptes à perte de vue ; une loupe qui n'a même pas le temps de bouger.]

En fait, il a un index. Et il existe même une astuce plus rapide, inventée en mille neuf cent soixante-dix, qui accepte de se tromper. Exprès. Medium s'en est servi pendant dix ans… avant de la jeter.

[VISUEL : une rangée de cases grises ; trois s'allument d'un coup. Arrêt sur image.]

---

## 1. Le pseudo que tu n'as jamais pu avoir (0:31 – 1:20)

Si tu as déjà joué en ligne, tu connais. Tu trouves LE pseudo, celui qui claque. Le jeu te répond : déjà pris. Du coup tu ajoutes un tiret du bas. Pris. Ton année de naissance. Pris aussi. Et tu finis en « xX_Technovore_2007_Xx », comme tout le monde.

[VISUEL : le champ qui se remplit de tirets, de chiffres et de « Xx » ; la croix rouge à chaque essai, de plus en plus vite.]
[SON : un « bonk » par essai, qui accélère.]

[LE PSEUDO QUE TU N'AS JAMAIS PU AVOIR, ET CE QUE TU AS PRIS À LA PLACE. UNE OU DEUX PHRASES.]

Moi, ce qui m'intéresse, c'est ce qui se passe entre ta dernière lettre et le rouge. Donc on ouvre le capot.

La méthode bête, c'est de prendre ton pseudo et de le comparer à chaque compte. Le premier, le deuxième, le troisième… jusqu'au milliardième. Et ça, pour une seule personne qui s'inscrit.

[VISUEL : un compteur « comparaisons » qui défile et s'emballe ; une barre de chargement qui n'avance pas.]

Personne ne fait ça, évidemment. Ce que les sites font vraiment, tu l'as déjà eu entre les mains : un dictionnaire.

---

## 2. Ce que fait vraiment le site : l'index (1:20 – 3:04)

[VISUEL : titre de chapitre « 1. L'index ».]

Tu te rappelles les dictionnaires papier ? Pour trouver « pseudo », tu ne lisais pas tout depuis la lettre A. Tu ouvrais au milieu, tu tombais sur « M », donc tu allais plus loin. Puis « R », tu revenais un peu. Et en quelques gestes, tu y étais.

[VISUEL : un dictionnaire qui s'ouvre, se referme, se rouvre ; un compteur « gestes : 1, 2, 3 ».]

Une base de données fait pareil, avec ce qu'on appelle un arbre B. Les pseudos sont rangés dans l'ordre, par paquets, et chaque paquet dit où chercher la suite. Résultat : même parmi un milliard de pseudos, la base retrouve le tien en quelques lectures. Quelques-unes. Sur un milliard.

[VISUEL : un arbre à trois étages ; un chemin s'allume de la racine jusqu'à « technovore ». Bandeau « Pour les devs : B-tree ».]

Et cet index a un deuxième boulot, le plus important. Sur PostgreSQL, par exemple, quand le dev écrit « ce pseudo doit être unique », la base crée toute seule un index unique. C'est lui qui fait respecter la règle.

Tu vois le cas où deux personnes valident « technovore » à la même seconde ? La base refuse le doublon. Une seule inscription passe, l'autre se prend le rouge.

[VISUEL : deux mains qui cliquent sur « S'inscrire » en même temps ; un seul ✓, un ✗.]
[SON : un « ding » et un « bonk », collés.]

Voilà la réponse honnête à « comment il sait » : un index, et la base qui tranche.

Si tu aimes voir ce qu'il y a derrière les petits trucs de tous les jours, abonne-toi : sur Technovore, on ouvre les applis une par une.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes ; l'arbre reste à l'écran.]

Sauf que chaque question, même rapide, va jusqu'à la base. Et souvent pour rien : le pseudo n'existe pas, et elle a quand même fait le trajet. En mille neuf cent soixante-dix, un chercheur, Burton Bloom, publie une idée au titre qui dit tout : gagner de la place et du temps… en autorisant des erreurs.

---

## 3. Le videur qui ne se trompe que dans un sens (3:04 – 5:48)

[VISUEL : titre de chapitre « 2. L'astuce ». Trente-deux cases grises en rangée.]
[SON : ding de chapitre.]

Le filtre de Bloom, pour faire simple, c'est une rangée de cases, toutes éteintes, et quelques fonctions de hachage. Une fonction de hachage, c'est une moulinette : tu lui donnes un mot, elle te sort un numéro. Toujours le même numéro pour le même mot.

[VISUEL : « technovore » entre dans trois moulinettes ; elles crachent 4, 19 et 27.]

Quand quelqu'un prend « technovore », on le passe dans trois moulinettes. Elles donnent quatre, dix-neuf et vingt-sept. Du coup, on allume ces trois cases. Et on ne garde même pas le pseudo : juste les cases.

[VISUEL : les cases 4, 19 et 27 s'allument.]
[SON : trois « tic » lumineux.]

Maintenant, tu tapes « kirito ». Les moulinettes donnent deux, dix-neuf et trente. La case deux est éteinte. Et là, le filtre sait une chose à cent pour cent : « kirito » n'a jamais été ajouté. Parce que s'il l'avait été, la case deux serait allumée. Donc réponse : sûrement pas pris. Et la base n'est même pas dérangée.

[VISUEL : la case 2 clignote, éteinte ; tampon vert « SÛREMENT PAS PRIS ».]

Mais avec le temps, d'autres pseudos allument d'autres cases. Un jour, tu tapes un pseudo tout neuf. Personne ne l'a jamais pris, et pourtant ses trois cases sont déjà allumées par d'autres. Le filtre ne peut pas faire la différence. Il répond : peut-être pris.

[VISUEL : trois cases allumées, chacune reliée par un fil de couleur à un autre pseudo (« zorro », « lea_92 », « ninja »). Tampon orange « PEUT-ÊTRE ».]

Voilà l'erreur autorisée de Burton Bloom. Le « non » est sûr. Le « peut-être » peut mentir.

En fait, ce mensonge ne coûte presque rien. Le « peut-être » déclenche juste la vérification dans la base qu'on aurait faite de toute façon.

Imagine un videur devant la base. Les « non », il les règle lui-même, à la porte, sans déranger personne. Les « peut-être », il les envoie à l'accueil, qui vérifie la vraie liste.

[VISUEL : une file de pseudos devant un videur ; voie rapide verte pour les « non », couloir orange vers la base pour les « peut-être ».]

Et le videur ne prend presque pas de place. Avec un pour cent d'erreur, il faut moins de dix cases par pseudo, et à peu près sept moulinettes. Que ton pseudo fasse cinq lettres ou trente, c'est pareil. Du coup, un milliard de pseudos tiennent dans environ un virgule deux gigaoctet. Tu veux dix fois moins d'erreurs ? Tu montes à environ un virgule huit.

[VISUEL : un curseur « erreurs » ; on le baisse, la rangée de cases s'allonge. Calcul à l'écran : « 1 % → 1,2 Go » puis « 0,1 % → 1,8 Go ».]

Alors, c'est comme ça que ton site vérifie ton pseudo ? Honnêtement, je ne sais pas. C'est la technique qu'on enseigne pour ce problème, dans les tutos et les entretiens d'embauche de dev. Sur YouTube, tu trouveras des vidéos qui te disent que Google, Amazon ou Meta font exactement ça. Moi, j'ai cherché. Aucun blog d'ingénierie, aucune conférence d'un grand site ne dit s'en servir pour les pseudos. Donc je ne vais pas te l'inventer.

[VISUEL : « Google ? Amazon ? Meta ? » ; chaque nom reçoit un tampon gris « AUCUNE SOURCE ».]

Par contre, ce videur, les grands l'ont bien embauché. Ailleurs. Et j'ai retrouvé leurs chiffres.

---

## 4. Qui l'a vraiment embauché (5:48 – 7:50) · relance à 60 %

[SON : la musique change, plus rythmée.]
[VISUEL : titre de chapitre « 3. Les vrais clients du videur ».]

En deux mille six, Google publie le papier de Bigtable, une de ses bases de données géantes. Dedans, une phrase : grâce aux filtres de Bloom, la plupart des recherches de lignes qui n'existent pas ne touchent même pas le disque. Tu vois le lien ? C'est notre « sûrement pas pris », version Google.

[VISUEL : capture du papier Bigtable, la phrase surlignée.]

Cassandra, une base de données open source, fait pareil : un filtre par fichier, réglé par défaut sur un pour cent d'erreur.

Akamai, un des grands réseaux qui livrent les pages web, a mesuré un truc fou. Sur quarante-cinq serveurs, en deux jours, soixante-quatorze pour cent de quatre cents millions d'objets n'ont été demandés qu'une seule fois. Les ingés les appellent les « one-hit wonders », les chanteurs d'un seul tube. Forcément, les garder en cache, c'est gâcher de la place. Donc le filtre retient ce qui est déjà passé une fois, et le serveur ne garde un fichier qu'à sa deuxième demande. Et effectivement, sur environ quarante-sept serveurs, le cache passe d'à peu près soixante-quatorze à quatre-vingt-trois pour cent de réussite.

[VISUEL : un tas de fichiers ; les trois quarts s'effacent en gris (« vus une fois ») ; une jauge de cache qui monte de 74 à 83 %.]

Et puis Medium, la plateforme de blogs. L'histoire commence à un dîner d'anniversaire : une collègue de Jamie Talbot, Sarah, lui demande comment Medium sait si quelqu'un a déjà lu un article. Il lui dessine un filtre de Bloom sur des serviettes. C'est lui qui le raconte, en deux mille quinze.

[VISUEL : une serviette en papier, des cases dessinées au stylo qui s'allument une à une.]

Chez Medium, ces filtres servent à ne pas te remontrer un article déjà lu, un auteur que tu as masqué, ou une histoire qu'on t'a déjà proposée trois fois. Jusqu'à quinze mille questions au filtre pour un seul fil d'actualité. Plus de quinze millions par seconde au total.

[VISUEL : « 15 000 » pour un fil, puis un compteur « 15 000 000 / s » qui tourne.]

Ouais, t'as bien entendu. Là, tu comprends pourquoi on veut un videur rapide.

Et pourtant, dix ans après la serviette, Medium l'a mis à la porte.

---

## 5. Ceux qui l'ont mis à la porte (7:50 – 9:23)

[SON : la musique coupe net, une seconde de silence.]

Et Medium n'est pas le premier à se poser la question. En deux mille onze, un développeur de Chrome, Scott Hess, propose de remplacer le filtre de Bloom qui gardait la liste des sites dangereux. Son argument : le filtre ne fait gagner que vingt-deux pour cent de place. Son remplaçant prend un tiers de mémoire en moins… et lui ne se trompe jamais. Le remplacement commence cette année-là.

[VISUEL : deux barres côte à côte, « Bloom » et « PrefixSet » ; la seconde est un tiers plus courte, avec « 0 erreur ».]

Pour Medium, c'est en deux mille vingt-cinq. Un de leurs ingénieurs, Raphael Montaud, raconte pourquoi ils ont retiré leurs filtres. Ils avaient grossi jusqu'à des milliards d'éléments. Et surtout, on ne peut rien effacer d'un filtre de Bloom.

Tu te rappelles les cases allumées ? Une case peut servir à plusieurs pseudos à la fois. Si tu l'éteins pour en retirer un, tu abîmes aussi les autres.

[VISUEL : on tente d'éteindre la case 19 ; « technovore » et « zorro » perdent chacun une case ; alarme rouge.]

Du coup, chez Medium, un auteur que tu avais masqué, puis démasqué, restait masqué pour toujours. Le videur avait une super mémoire, mais impossible de lui faire oublier quelqu'un. Et sans les filtres, en interrogeant directement leur vraie base, ils disent payer dix fois moins cher. Bon, l'auteur précise lui-même que la comparaison n'est pas forcément équitable.

[VISUEL : « ×10 moins cher » qui tombe, puis un astérisque géant : « comparaison pas forcément équitable » (Medium, 2025).]

Petit détail pour finir : cette image du videur, Montaud dit l'avoir obtenue en demandant à Claude, une IA, de lui résumer le filtre simplement. Même l'analogie a été générée.

[VISUEL : une bulle de chat avec « bouncer » ; clin d'œil.]

Bref, revenons à ta croix rouge.

---

## 6. Fin (9:23 – 10:19)

[VISUEL : retour au formulaire du début, « technovore », la croix rouge.]

La prochaine fois que tu vois « déjà pris » avant même d'avoir fini de taper, tu sauras ce qui a pu se passer. Peut-être un index qui a trouvé ton pseudo en quelques lectures. Peut-être un videur qui a regardé trois cases. Mais dans les deux cas, c'est la base qui a le dernier mot.

Et c'est justement elle qui rattrape les défauts du videur. Si un site utilisait un filtre et qu'un pseudo se libérait, le filtre dirait encore « peut-être pris ». La base, elle, répondrait : en fait, il est libre.

[OPTIONNEL : TON AVIS EN UNE PHRASE. TU METTRAIS UN FILTRE DE BLOOM DEVANT TA BASE, TOI ?]

Sur Technovore, j'ouvre comme ça les applis que tu utilises tous les jours. Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir.

Et la vidéo juste là, c'est Waze : comment il sait qu'il y a un bouchon avant que tu le voies.

[VISUEL : écran de fin, 20 s : vidéo Waze à gauche (ou Uber), bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel | La croix rouge avant la dernière lettre |
| 0:15 | Question centrale | « Alors comment il sait ? » sur le mur d'un milliard de comptes |
| 0:25 | Boucle ouverte | Une astuce qui se trompe exprès, que Medium a jetée (refermée à 7:50) |
| 0:40 | Humour gamer | « xX_Technovore_2007_Xx », un « bonk » par essai |
| 1:05 | Visuel | Le compteur de comparaisons qui s'emballe |
| 1:20 | Lien au vécu | Le dictionnaire papier |
| 2:05 | Mini-scène | Deux inscriptions à la même seconde, un ✓ et un ✗ |
| 2:40 | Appel à l'action | Abonnement (≈ 25 %) |
| 2:55 | Pont | Burton Bloom, « en autorisant des erreurs » |
| 3:30 | Visuel | Les moulinettes, trois cases qui s'allument |
| 4:00 | Révélation | « kirito » : la case éteinte, le « non » sûr |
| 4:25 | Retournement | Le pseudo neuf qui sort « peut-être pris » |
| 4:50 | Personnage | Le videur et ses deux files |
| 5:10 | Chiffre | Un milliard de pseudos dans 1,2 Go |
| 5:25 | Aveu | « Honnêtement, je ne sais pas » : les géants tamponnés « aucune source » |
| 5:48 | Changement de musique | Relance (≈ 60 %) : qui l'utilise vraiment |
| 6:30 | Chiffre | Akamai, 74 % d'objets vus une seule fois |
| 7:05 | Anecdote | Le filtre dessiné sur des serviettes |
| 7:30 | Chiffre | 15 millions de questions par seconde |
| 7:50 | Coupure musique | Chrome, puis Medium mettent le videur à la porte |
| 8:45 | Gag | L'auteur masqué pour toujours |
| 9:10 | Clin d'œil | L'analogie du videur vient de Claude |
| 9:23 | Boucle fermée | Retour à la croix rouge |
| 9:55 | Appel à l'action | « Quelle appli je décortique ensuite ? » puis Waze |

**Total** : 24 relances en 10 min 20, environ une toutes les 26 secondes ; la plus longue plage sans relance fait environ 40 s.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15-0:35 | Moyen | « Il a un index » peut sembler répondre trop tôt | La phrase suivante relance aussitôt : une astuce qui se trompe exprès, et Medium qui l'a jetée |
| Section 2, l'arbre B | Moyen | Le mot « arbre B » peut perdre les non-devs | Le dictionnaire porte l'explication ; « arbre B » reste un bandeau pour les devs |
| Section 3, les hachages | Élevé | Le bloc le plus abstrait de la vidéo | Deux exemples seulement (« technovore », « kirito »), des cases qui s'allument, puis le videur |
| Section 3, « je ne sais pas » | Moyen | L'aveu peut sembler casser la promesse | Il ouvre la question « qui l'utilise vraiment ? », et la section 4 y répond tout de suite avec des chiffres |
| Relance (~60 %) | Élevé | Chute classique, et quatre exemples d'affilée | Changement de musique, un chiffre ou une image par exemple, la serviette, puis la coupure musicale de la section 5 |

## Notes de montage

- **Composants à construire une fois** : la rangée de 32 cases (elle sert aux sections 3, 5 et 6), les trois moulinettes, le videur avec ses deux files, le formulaire du hook. Animations simples : c'est une vidéo légère.
- **Le formulaire** : générique, en motion design, sans logo de site réel. Pas de « G » de Google, ni sur la miniature ni à l'écran (`sources.md`, ligne 24).
- **La section « je ne sais pas »** : les noms Google, Amazon, Meta n'apparaissent qu'avec le tampon « aucune source ». Ne pas montrer la miniature ni le titre de la vidéo de ByteMonk.
- **Captures autorisées** : le papier Bigtable (USENIX), la doc Cassandra, la revue de code Chromium, les deux billets de Medium (2015 et 2025), la doc PostgreSQL.
- **Énergie** : calme et joueuse jusqu'à 3:04, montée sur les cases qui s'allument, rythme plus vif dans la section 4, coupure nette au début de la section 5.
- **Le gag des pseudos** (section 1) : il peut piocher dans ta vraie liste de pseudos refusés, à l'écran.
- **Miniature** : `noir-07.png`, « il triche. », sans le « G ». La vidéo tient la promesse : le filtre répond sans regarder la base, et le script dit qu'on ne sait pas quel site le fait.

## Faits utilisés

| Fait (`sources.md`) | Phrase du script |
|---|---|
| 1 | « En mille neuf cent soixante-dix, un chercheur, Burton Bloom, publie une idée au titre qui dit tout » |
| 2 | « une rangée de cases, toutes éteintes, et quelques fonctions de hachage » ; « on allume ces trois cases » ; « La case deux est éteinte… n'a jamais été ajouté » |
| 3, 29 | « Le "non" est sûr. Le "peut-être" peut mentir. » ; « Les "peut-être", il les envoie à l'accueil, qui vérifie la vraie liste. » |
| 4 | « on ne peut rien effacer d'un filtre de Bloom » |
| 5 | « moins de dix cases par pseudo, et à peu près sept moulinettes » ; « un virgule deux gigaoctet » ; « un virgule huit » |
| 6 | « la plupart des recherches de lignes qui n'existent pas ne touchent même pas le disque » |
| 7 | « Cassandra… un filtre par fichier, réglé par défaut sur un pour cent d'erreur » |
| 8 | « Sur quarante-cinq serveurs, en deux jours, soixante-quatorze pour cent de quatre cents millions d'objets n'ont été demandés qu'une seule fois » |
| 9 | « sur environ quarante-sept serveurs, le cache passe d'à peu près soixante-quatorze à quatre-vingt-trois pour cent » |
| 10 (⚠️) | « En deux mille onze, un développeur de Chrome, Scott Hess, propose de remplacer… vingt-deux pour cent… un tiers de mémoire en moins… ne se trompe jamais. Le remplacement commence cette année-là. » (1,27 / 1,93 ≈ 0,66 ; pas d'unité dite, pas d'« abandonné ») |
| 11 | « ne pas te remontrer un article déjà lu, un auteur que tu as masqué, ou une histoire qu'on t'a déjà proposée trois fois » |
| 12 | « des milliards d'éléments » ; « restait masqué pour toujours » ; « dix fois moins cher… pas forcément équitable » ; « leur vraie base » (sans nommer DynamoDB) |
| 13 | « la base crée toute seule un index unique. C'est lui qui fait respecter la règle. » |
| 15, 16 (❓, ⚠️) | « C'est la technique qu'on enseigne pour ce problème… Aucun blog d'ingénierie, aucune conférence d'un grand site ne dit s'en servir pour les pseudos. » (légende corrigée explicitement) |
| 18 (⚠️) | « la base retrouve le tien en quelques lectures » (pas « 3 à 4 ») |
| 20 | « Le "peut-être" déclenche juste la vérification dans la base qu'on aurait faite de toute façon. » |
| 21 (⚠️) | « La base refuse le doublon. Une seule inscription passe » |
| 22 (⚠️) | « Le site n'a pas eu le temps de les regarder un par un… il a un index. Et il existe même une astuce plus rapide… qui accepte de se tromper. » (« un milliard » présenté comme hypothèse, « imagine », comme dans le calcul du fait 5) |
| 26 | « une collègue de Jamie Talbot, Sarah, lui demande comment Medium sait si quelqu'un a déjà lu un article. Il lui dessine un filtre de Bloom sur des serviettes. » |
| 27 | « cette image du videur, Montaud dit l'avoir obtenue en demandant à Claude » |
| 28 | « Jusqu'à quinze mille questions au filtre pour un seul fil d'actualité. Plus de quinze millions par seconde au total. » |

**Non utilisés, exprès** : 14, 23, 25 (« une milliseconde », « 0,001 s » : remplacés par « instantanément ») ; 17 (la chaîne filtre → cache → base, modèle pédagogique) ; 19 (Instagram, Spanner) ; le filtre à compteurs (fait 4, Wikipédia seulement).

**Phrases à toi de valider** (déductions, pas des citations) :
- « Medium s'en est servi pendant dix ans » (hook) : de 2015 (Talbot) à 2025 (Montaud). Si tu préfères la prudence : « Medium s'en est servi… avant de la jeter ».
- La fin (« si un pseudo se libérait… la base répondrait : il est libre ») est un raisonnement tiré des faits 3, 4 et 20, au conditionnel.
- « dans les tutos et les entretiens d'embauche de dev » : déduit des vidéos de référence de `sources.md` (KodeKloud, Engineering Digest, Hello Interview) et du tutoriel OneUptime.

## Questions pour l'auteur

1. **Ton pseudo** (section 1) : quel pseudo tu n'as jamais pu avoir, sur quel jeu, et ce que tu as pris à la place ? C'est ta seule matière perso de la vidéo ; sans elle, le gag « xX_Technovore_2007_Xx » reste générique.
2. **Tu as déjà codé une vérification de pseudo** (un formulaire, un index unique dans une de tes bases) ? Si oui, une phrase dans la section 2 te mettrait dans le récit, sans montrer d'appli de travail.
3. **« Instantanément »** : veux-tu mesurer toi-même (outils réseau du navigateur sur un vrai formulaire d'inscription) ? Avec une vraie mesure, on peut remettre un chiffre dans le hook et le titre.
4. **L'écran de fin** : Waze (sorti le 9/11, plus récent) ou Uber (la vidéo génie publiée) ?
5. **Le clin d'œil Claude** (section 5) : tu le gardes ? C'est sourcé, mais ça parle d'une IA dans une vidéo du pilier génie.
