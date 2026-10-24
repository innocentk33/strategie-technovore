# Grill du script iPhone fluide v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Grille : `youtube-script-grill`, mode B (après l'écriture), variante storytelling (test des 30 secondes, axe 10).
> Hypothèses : titre *Pourquoi tout paraît plus fluide sur un iPhone* ; miniature pas encore faite (piste de la fiche : l'iPhone net, l'Android flou) ; public de 18-30 ans, surtout africain et **surtout sur Android** ; objectif : la 2e ou 3e vidéo du pilier « Le génie derrière l'app », après Uber et Waze.
> Faits revérifiés le 23/10 : voir « Vérification des faits » en bas. Version corrigée : [`script.md`](script.md).

## Verdict

Le script est solide. Le fil rouge du battement tient de la première à la dernière seconde, la légende du « temps réel » est racontée comme une légende et corrigée, et la fin rend justice à Android avec des dates sourcées. Aucune vidéo française n'explique ce mécanisme (`sources.md`) : la valeur est là.

Le plus gros problème est factuel. Il y a une date fausse (l'iPad Air 2 « cette année-là »), deux affirmations trop fortes (« Android a ouvert le bal » du 120 Hz, alors que l'iPad Pro y est en juin 2017 ; le DJ qui fait tourner l'animation « pendant un gros calcul ») et une image qui mélange Flutter et le RenderThread d'Android. Deuxième problème : le titre dit « paraît », au présent, et la vidéo répond au passé. La section 6 ne dit jamais pourquoi un Android peut encore saccader aujourd'hui.

Rien de bloquant. La version finale corrige les faits, raccourcit de 59 mots et fait revenir Guitar Hero.

**Note globale : 7 🟢 · 11 🟠 · 0 🔴, soit environ 14/20.** La V2 remonte à environ 17/20 : il ne reste en 🟠 que ce qui dépend de toi (ton vécu, ton avis, l'enjeu du narrateur).

## Promesse, problème profond, « mais / donc »

- **La promesse** : « je vais t'expliquer pourquoi la page colle à ton doigt sur un iPhone ». Le spectateur clique en pensant à son téléphone à lui : soit il a un Android et se demande s'il est moins bien, soit il a un iPhone et veut savoir pourquoi il est meilleur.
- **Le problème de surface** : comment un téléphone sort une image toutes les 16 ms.
- **Le problème profond** : « Mon Android est-il un cran en dessous d'un iPhone, par nature ? » Le script y répond (non : même battement depuis 2012, même fil de rendu depuis 2014, et 120 Hz en premier sur les téléphones), mais ne pose jamais la question tout haut. La V2 la pose au présent : « Alors pourquoi un Android peut encore saccader en 2026 ? »
- **La chaîne « mais / donc »** :
  - une image toutes les 16 ms, **donc** un jeu de rythme ;
  - l'iPhone fait glisser des calques, **sauf que** le dessin final se fait ailleurs ;
  - Android traîne, **donc** quelqu'un propose le temps réel, **mais** c'est faux ;
  - **donc** il manquait quoi ? Le battement commun (2012), **sauf qu'**il reste un trou, **donc** le fil de rendu (2014) ;
  - **et** ton téléphone aujourd'hui ?
  
  Elle tient jusqu'à 9:19. Deux passages tournent à l'« et aussi » : 7:48-8:41 (Choreographer, puis le troisième tampon, puis le toucher, puis le coup de boost) et 11:09-12:00 (Razer, puis Google, puis Android 11, puis Perfetto).

## Test des 15 premières secondes

À 145 mots/min, 15 s font environ 36 mots. Le V1 dit, seul :

> « Pose ton doigt sur l'écran et fais défiler. Tu vois ? La page colle à ton doigt. Sauf que pour ça, ton téléphone doit fabriquer une nouvelle image toutes les seize millisecondes, sans jamais rater le temps. L'iPhone sort en 2007. »

Le geste est raccord avec le titre, et le chiffre de 16 ms crée l'enjeu. Le moment le plus fort, le contraste 2007 → 2012, commence à 14,9 s et finit vers 18 s : il déborde. Le meilleur moment de la vidéo reste la légende démontée (4:49) ; c'est bien de ne pas la griller dans les 15 s, puisque le pont la teaser.
**Verdict** : 🟠 de peu. Couper « Tu vois ? » et serrer « sans jamais rater le temps » en « sans en rater une » fait tomber « L'iPhone sort en 2007 » à 13,7 s (V2).

## Test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Pose ton doigt sur l'écran et fais défiler. Tu vois ? La page colle à ton doigt. » | 🟢 Le spectateur fait le geste en regardant. Raccord avec le titre ; la tension arrive dès la phrase suivante (« Sauf que… »). |
| 5-15 s | > « Sauf que pour ça, ton téléphone doit fabriquer une nouvelle image toutes les seize millisecondes, sans jamais rater le temps. L'iPhone sort en 2007. » | 🟠 Le chiffre est fort ; le contraste 2007 → 2012 arrive à 15-18 s, un peu tard. |
| 15-30 s | > « Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran. Alors qu'est-ce que l'iPhone avait compris, et qu'Android a mis des années à rattraper ? » | 🟢 Une seule question, en mots simples, posée à 22 s (54e mot). |
| Pont | > « Fin 2011, un ancien stagiaire d'Android publie sa réponse. La presse tech la reprend. Et des ingénieurs la démontent. » | 🟢 Il ouvre une deuxième question (quelle réponse, et pourquoi fausse ?) avant la première. Trois phrases de même forme, mais c'est la seule cascade du script : elle passe. |

**Budget** : 87 mots, soit 36 s à 145 mots/min et 29 s à 180 (tes coupes serrées d'Uber). Ça tient.
**À couper** : « Tu vois ? » (la question est déjà dans le geste) ; « sans jamais rater le temps » se dit plus court.
**Réécriture des 30 s** (V2, 86 mots) :

> Pose ton doigt sur l'écran et fais défiler. La page colle à ton doigt.
> Sauf que pour ça, ton téléphone doit sortir une nouvelle image toutes les seize millisecondes, sans en rater une.
> L'iPhone sort en 2007. Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran.
> Alors qu'est-ce que l'iPhone avait compris, et qu'Android a mis des années à rattraper ?
> Fin 2011, un ancien stagiaire d'Android croit avoir trouvé. La presse tech reprend sa réponse. Et pourtant, des ingénieurs la démontent.

Le « et pourtant » remplace le « et » du pont : la cascade garde son rythme, gagne un retournement, et ne répète pas le « sauf que » de la deuxième phrase.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Le titre dit « paraît », au présent ; la vidéo explique le passé (2007-2014) et laisse le présent à un crochet. |
| 2. Alignement | 🟢 | Aucune vente ; un appel à l'abonnement court et bien placé. |
| 3. Problème profond | 🟠 | « Mon Android est-il moins bien ? » est la vraie question du public, jamais dite tout haut. |
| 4. Public & complexité | 🟢 | Chaque terme arrive avec son image (feuille, partition, orchestre, DJ) ; la boucle en cinq temps ne nomme pas les cinq temps. |
| 5. Valeur & originalité | 🟢 | Rien en français, rien en anglais sur le mécanisme ; la légende de 2011 et la modif du 3 mai 2012 sont introuvables ailleurs. Rien de Tartarotti (pas d'easing, pas de ressorts). |
| 6. Structure & transformation | 🟢 | iPhone → légende → 2012 → 2014 → ton téléphone : la progression est claire et chaque section répond à la précédente. |
| 7. Histoire | 🟠 | Des personnages (l'étudiant, Hackborn, Haase et Guy), mais personne ne *veut* rien ; le narrateur n'a pas d'enjeu tant que ton vécu de dev est vide. |
| 8. Mais / donc | 🟠 | Très bon jusqu'à 7:48 ; deux listes en « et aussi » (7:48-8:41, 11:09-12:00). |
| 9. Engagement actif | 🟢 | Le spectateur fait le geste, on lui prête une croyance (« Normalement, tu te dis… »), on le rappelle (« Tu te rappelles le stagiaire ? »). |
| 10. Rythme, oralité & liaisons | 🟠 | 1,9 liaison pour 100 mots, au-dessus du repère ; mais 27 phrases commencent par « Et », et les sections 4 et 6 tombent à 1,5 et 1,3. |
| 11. Tics d'IA | 🟠 | Sept tics légers, aucun grave (liste plus bas). |
| Faits (« Les faits comptent ») | 🟠 | Une date fausse, deux affirmations trop fortes, une image trompeuse ; le reste est propre. |
| S1. 30 premières secondes | 🟠 | Question à 22 s, pont à 28 s ; le contraste déborde des 15 s de 3 s. |
| S2. Le pont | 🟢 | Le stagiaire ouvre une deuxième boucle, refermée à 5:40. |
| S3. Retournements | 🟠 | Un toutes les 25-40 s, sauf deux trous de 50-55 s (7:48-8:41, 10:29-11:09). |
| S4. Planté / récolté et motif | 🟢 | Le métronome à chaque chapitre ; le FPS de 4:10 récolté à 8:30 ; le stagiaire du hook récolté à 4:49. Guitar Hero reste à moitié planté (voir plus bas). |
| S5. Personnages et enjeu | 🟠 | Des noms, pas d'envie : il manque la phrase où Google *cherche* à rattraper. |
| S6. La fin | 🟠 | Le rappel « Seize millisecondes. Toc. » est bon ; la fin résume, puis s'en remet à ton avis sans répondre au « paraît ». |

## Axe 10 : les liaisons

Compte de `controle.py` sur la voix off du V1 : **34 liaisons pour 1 819 mots, soit 1,9 pour 100 mots** (repère : 1,5 ; tes téléprompteurs : 0,7 à 0,9). Par section :

| Section | Mots | Liaisons | Pour 100 mots | Phrases en « Et » |
|---|---|---|---|---|
| 0. Hook | 87 | 2 | 2,3 | 2 |
| 1. Le cœur de ton écran | 225 | 5 | 2,2 | 2 |
| 2. Ce que l'iPhone fait de ton doigt | 388 | 8 | 2,1 | 3 |
| 3. La légende du temps réel | 261 | 6 | 2,3 | 4 |
| 4. 2012 | 390 | 6 | **1,5** | 6 |
| 5. 2014 | 170 | 3 | 1,8 | 4 |
| 6. Ton Android aujourd'hui | 298 | 4 | **1,3** | 6 |

Le chiffre global est bon. Le vrai tic, c'est le « Et » en tête de phrase : **27 fois**. Il sert de liaison passe-partout et ne dit jamais pourquoi le fait arrive là.

**Les rafales de faits sans liaison** :

> « D'après Nick Lockwood, l'auteur d'un livre sur Core Animation, dès le premier iPhone, l'interface est faite de calques assemblés par la puce graphique. Et aujourd'hui encore, la doc d'Apple le dit : sur iOS, chaque élément de l'écran repose sur un calque. »

Deux attributions de suite, et la phrase commence par la source au lieu du fait. V2 : « En fait, dès le premier iPhone, l'interface est faite de calques… C'est Nick Lockwood qui le raconte… »

> « Et cette année-là, Apple présente l'iPad Air 2 : son écran tourne à soixante hertz, mais il lit le tactile à cent vingt. Deux fois plus vite que tous les autres iPhone et iPad de l'époque. »

Un iPad dans une vidéo sur l'iPhone, trois chiffres, et une date fausse (voir les faits). Coupé.

> « Ce qui lui manquait, c'était le contenu des fenêtres : les boutons et les listes. Ça, la puce graphique ne s'en charge qu'à partir d'Android 3.0. Et par défaut, seulement pour les applis qui visent Android 4.0 ou plus. »

Trois numéros de version en trois phrases (1.0, 3.0, 4.0). V2 : on coupe la 4.0, comme le proposait le rédacteur, et on récolte la feuille de la section 2 : « Tu te rappelles la feuille qui glisse sur l'iPhone ? Côté Android, ce contenu-là, la puce graphique ne s'en charge qu'à partir d'Android 3.0. »

> « Android 4.1 ajoute aussi un troisième tampon d'image. Pour faire simple, une feuille de plus pour préparer les images suivantes. / Et il s'occupe de ton doigt. D'abord… Ensuite… Et quand tu touches l'écran après une pause… »

La liste en « et aussi » de 7:48-8:41. Le troisième tampon ne sert pas l'histoire du battement (et sa nuance est ⚠️) : coupé. Le FPS devient le retournement du passage (voir la rétention).

> « D'après StatCounter, en septembre 2026, environ huit téléphones sur dix… Et d'après Canalys et Omdia, environ la moitié des smartphones… »

Deux « d'après » en tête de phrase. V2 : « …il y a de bonnes chances que ce soit un Android : d'après StatCounter… Et parmi les smartphones vendus en Afrique en 2025, environ la moitié sont des Tecno… » ; puis « Forcément… Donc il a hérité… » donne la conséquence pour le spectateur.

**V2** : 38 liaisons pour 1 760 mots, soit **2,2 pour 100 mots** ; 14 phrases en « Et » au lieu de 27 ; plus aucune section sous 1,6.

## Tics d'IA

1. > « Et elle ajoute une phrase qui dit tout : la puce graphique n'est pas une solution miracle… »
   Faux suspens : la formule annonce que la phrase est forte. V2 : « Elle prévient quand même : la puce graphique n'est pas une solution miracle pour une interface fluide. »
2. > « L'explication est simple, elle fait plaisir, et la presse tech la relaie. »
   Rafale de trois, et redite du hook (« La presse tech la reprend »). Coupée.
3. > « Et aucune priorité magique là-dedans. Juste des systèmes qui ont appris à se caler sur le battement de l'écran. »
   Le « Pas A. Juste B. », plus une petite morale en fin de paragraphe. Le « A » est réel (la légende), donc on le garde comme récolte, sans le fragment : « Et la priorité temps réel du stagiaire ? Elle n'apparaît nulle part dans cette histoire. Aujourd'hui, les deux systèmes se calent sur le battement de l'écran. »
4. > « Voilà pour l'iPhone. Du coup, retour fin 2011, côté Android. »
   « Du coup » sans conséquence : rien de ce qui précède n'amène 2011. V2 : « Maintenant, retour fin 2011… »
5. > « Google crée une nouvelle pièce, avec un nom qui ne laisse aucun doute : Choreographer. »
   Formule creuse ; « Le chorégraphe » et « Cinq, six, sept, huit » font déjà la blague. Coupée.
6. > « Voilà comment Android a rattrapé son retard. Et ça répond à la question du début. »
   Annonce méta : le spectateur entend la réponse, pas besoin de lui dire que c'en est une. Coupée.
7. > « Ce moment d'hésitation, tu ne l'as jamais remarqué. »
   Petite morale de fin de paragraphe. Coupée.

Tolérés :
- « Sur iPhone, c'est plus malin que ça » : la croyance est prêtée au spectateur (« Normalement, tu te dis… ») puis contredite par un fait ;
- la cascade du pont : c'est la seule du script.

Aucune fausse opposition « ce n'est pas A, c'est B ». Aucun « vous ».

## Rétention

- **Relances** : 30 en 12 min 30, une toutes les 25 s. Deux trous dépassent 45 s :
  - **7:48-8:41**, la liste Choreographer → tampon → toucher → boost. Le V1 avait déjà la bonne graine : « la visée en avance du FPS, trois ans avant qu'Apple l'ouvre aux développeurs de l'iPhone ». V2 : on la plante explicitement en section 2 (« Garde ce FPS en tête, on va le recroiser côté Android ») et on la récolte comme un retournement (« Oui, la visée en avance du FPS ! Sauf que là, on est en 2012 »). C'est aussi un point pour le spectateur Android.
  - **10:29-11:09**, les chiffres de marché. V2 : la conséquence (« Donc il a hérité du battement de 2012… ») arrive juste après.
- **Ponts** : « Sur iPhone, c'est plus malin que ça », « il manquait quoi ? … avec un jeu de mots », « Sauf qu'il reste un trou » : les trois sont bons, garde-les.
- **Abonnement** : à 3:31, soit 28 %, juste après la partition. V2 : avancé à 2:50 (23 %), après la feuille qui glisse, pour que le « sauf que » du serveur de rendu serve de relance juste derrière l'appel. Le passage le plus technique (la boucle en cinq temps) suit au lieu de précéder l'appel.
- **Relance forte vers 60 %** : à 7:30 (60 %), la cacophonie qui s'arrête net et un seul « toc ». C'est le meilleur moment de montage du script. V2 : 7:08 (59 %).
- **Guitar Hero, fil ou gadget ?** Dans le V1, à moitié l'un et l'autre :
  - il est planté à 1:02 avec le « MISS » ;
  - il revient une seule fois, en passant (« dans notre jeu de rythme ») ;
  - ensuite, la partition, l'orchestre, le chorégraphe et le DJ prennent le relais. Ces images restent de la même famille (le rythme), donc le fil tient.
  
  V2 : le « MISS » revient deux fois avec un sens nouveau. Dans l'orchestre d'avant 2012, « Bonjour les "MISS" », sur la même piste. Dans Perfetto, « c'est ton "MISS" de Guitar Hero, en vrai ». Ça en fait un vrai planté-récolté, sans un mot de plus sur le jeu.

## Le grill

### 1. Trois faits faux ou trop forts, et une image trompeuse

> « Et cette année-là, Apple présente l'iPad Air 2 »

« Cette année-là », c'est 2015, l'année d'iOS 9. Sauf que l'iPad Air 2 a été présenté le **16 octobre 2014** (Apple Newsroom, fait 37). La session WWDC de 2015 le *cite*, elle ne le présente pas.
**Correction** : coupé. Le détail parle d'un iPad, pas de l'iPhone, et coûte 40 mots.

> « Et pour les écrans, Android a même ouvert le bal. »

Apple met du 120 Hz sur l'**iPad Pro dès le 5 juin 2017** (Apple Newsroom, fait 36), cinq mois avant le Razer Phone. Le fait 22 le notait déjà (« les tablettes ne sont pas comptées ici »), mais la phrase du script parle « des écrans » en général. Un spectateur iPad le relèvera en commentaire.
**Correction** : « Pour les écrans, sur les téléphones, c'est même Android qui ouvre le bal. » Le Razer Phone n'est plus présenté « comme le premier » : un autre Android, le Sharp Aquos R Compact, était en vente quelques semaines avant (Lowyat, fait 36). Comme les deux sont des Android, « Android ouvre le bal » reste vrai.

> « ton appli peut aller chercher ses données ou faire un gros calcul, l'animation continue de tourner sur le battement. »

Google dit : le RenderThread « garde les animations fluides même quand le fil principal de l'UI a du retard » (fait 10). « Faire un gros calcul » sur le fil principal, c'est justement le cas où l'appli saccade : la doc actuelle de Google le dit (« Sometimes, jank occurs because your app's UI Thread is blocked », fait 35). Le DJ promet plus que le RenderThread.
**Correction** : « Là, c'est pareil : l'appli prend du retard, et le fil de rendu continue de faire tourner l'animation sur le battement. » Et la limite revient dans la section 6 : « Le DJ peut faire durer le morceau, mais à un moment, il faut bien changer de disque. »

> « [VISUEL : maquette générique d'une appli avec le logo Flutter (jamais tes applis de travail) ; un chargement qui tourne pendant qu'une barre « calcul » se remplit.] »

Le RenderThread est une pièce d'Android. Flutter dessine avec son propre moteur et ses propres fils. Un logo Flutter sur le RenderThread mélange les deux, et tes abonnés devs Flutter le verront.
**Correction** : maquette sans logo pour le RenderThread. Le logo Flutter n'apparaît que si ton vécu (le crochet) parle de Flutter. La question du crochet est recentrée sur ce que tout dev a vécu : une interface qui gèle parce qu'un calcul tourne sur le fil principal. Ce vécu devient la nuance honnête du DJ.

### 2. Le titre dit « paraît », la vidéo répond au passé

> « [TON AVIS DE DEV : SI UN ANDROID RAME ENCORE EN 2026, D'OÙ ÇA VIENT SELON TOI ? …] »

Le titre promet une raison *actuelle*. La vidéo explique très bien 2007-2014, puis dit au spectateur qu'il a tout hérité, et laisse le présent à un crochet. Si le crochet reste vide, la promesse n'est tenue qu'au passé.
**Correction** : une question au présent, une piste sourcée, puis ton avis.

> Alors pourquoi un Android peut encore saccader en 2026 ? Google donne une piste dans sa propre doc : souvent, l'image saute parce que le fil principal de l'appli est bloqué. Le DJ peut faire durer le morceau, mais à un moment, il faut bien changer de disque.
>
> [TON AVIS DE DEV : AU-DELÀ DU FIL PRINCIPAL BLOQUÉ, D'OÙ ÇA VIENT SELON TOI ? …]

### 3. Le « Et » passe-partout et les deux listes

Voir l'axe 10 : 27 « Et » en tête de phrase, et les passages 7:48-8:41 et 11:09-12:00. La V2 en garde 14, coupe le troisième tampon et la phrase sur Android 11 (`setFrameRate()`, un détail de dev qui allongeait la liste), et transforme le FPS en retournement.

### 4. La légende : bien racontée, deux réglages

> « Bob Lee, ancien responsable des bibliothèques d'Android, parle d'erreurs de raisonnement. Un autre, Jay Freeman, dit que c'est tout simplement faux. Et l'étudiant finit par corriger son post. »

- **Bob Lee et Jay Freeman sont-ils sourcés ?** Oui, en seconde main (fait 32). PhoneArena (décembre 2011) cite Jay Freeman, « qui a fait Cydia », pour « simply wrong », et Bob Lee, « CTO de Square et ancien responsable des bibliothèques d'Android », pour « fallacies ». Le roundup d'Ole Begemann (décembre 2011) confirme que Bob Lee a publié sa réponse. Les posts Google+ ont disparu : on n'a lu aucun des deux à la source, d'où le ⚠️.
- **« Un autre, Jay Freeman »** : sans son titre, le nom ne dit rien au spectateur. Or Freeman est le créateur de Cydia, l'appli des iPhone jailbreakés : c'est quelqu'un qui connaît l'intérieur d'iOS qui dit « faux ». V2 : « Jay Freeman, le créateur de Cydia, l'appli des iPhone jailbreakés, dit que c'est tout simplement faux. »
- **« corriger son post »** : les sources disent « updated post », sans dire ce qui a changé. V2 : « mettre son post à jour ».
- **L'ordre des posts** : Hackborn a publié *avant* l'étudiant, puis l'a contredit (fait 33). Le V1 la présente comme si elle arrivait après coup (« On pourrait croire… En fait, d'après Dianne Hackborn »). V2 : « Côté Google, une ingénieure d'Android, Dianne Hackborn, rejette elle aussi cette idée. Et elle avait déjà remis les pendules à l'heure sur un autre point. »
- **Le mythe** n'apparaît que comme une légende, au conditionnel (« serait dessinée », « passerait devant »), avec le tampon « LÉGENDE ». C'est exactement ce que demandait le fait 13. Garde-le.

### 5. La miniature « Android flou »

D'accord avec le rédacteur : un Android flou à côté d'un iPhone net promet « ton Android rame aujourd'hui ». La vidéo dit le contraire, et ton public est sur Android. Le spectateur qui clique pour se faire confirmer que son téléphone est nul repart frustré ; celui qui a un Android ne clique pas, ou clique fâché.
**Pistes** : le doigt sur une liste avec la ligne du temps de 16 ms et une seule image « MISS » (la mécanique de la vidéo, sans marque perdante) ; ou « 2007 → 2012 » sur le doigt (le contraste du hook). Avant de choisir, fais la planche des vidéos hôtes françaises (`CLAUDE.md`, kit d'upload) : les vidéos françaises qui marchent sur ce sujet sont des comparatifs de marques (`sources.md`), donc vérifie leurs miniatures et évite de mettre deux téléphones face à face.

### 6. La durée

Le rédacteur propose de couper la phrase sur Android 4.0 et le troisième tampon. **D'accord pour les deux** : la 4.0 empile une troisième version en trois phrases, et le troisième tampon est ⚠️ et hors du fil. On coupe aussi l'iPad Air 2 (date fausse), la phrase sur Android 11, et les redites relevées plus haut.
Résultat : 1 760 mots, contre 1 819, en ajoutant les faits qui manquaient (Cydia, Hackborn, la doc actuelle de Google). Ça fait environ 12 min 10 à 145 mots/min, et environ 10 min avec tes coupes serrées d'Uber.

## Ce qu'il faut garder

- > « Pose ton doigt sur l'écran et fais défiler. »
  Le spectateur fait le geste pendant qu'il regarde. C'est le meilleur engagement actif possible, et c'est l'image de la miniature.
- > « Chez Apple, ce raté a un nom : un hitch… Cinq millisecondes sur toute une seconde. Ouais, ils sont exigeants. »
  Un chiffre sourcé, puis ta réaction. C'est le ton « on discute » que tu veux.
- > « En gros, ton appli écrit la partition, et c'est un autre musicien qui la joue en rythme. »
  Toute la boucle en cinq temps en une phrase.
- > « Leur conférence s'appelle « For Butter or Worse ». Pour le beurre ou pour le pire. Oui, chez Google aussi, on aime les jeux de mots. »
  Humour et fait sourcé, et le « jeu de mots » est annoncé une minute avant : une boucle courte et tenue.
- **La relance de 7:30** : la cacophonie, une seconde de silence, puis un seul « toc ».
- > « Comme toi au fond de la classe quand le prof dit ton prénom. »
  Ta blague, à garder telle quelle.
- > « Pour une fois, c'est l'iPhone qui arrive après. »
  Le moment où le spectateur Android relève la tête.
- > « Seize millisecondes. Toc. »
  Le rappel du hook, en quatre mots.

## Plan d'action (fait dans `script.md`)

1. Corriger les faits : iPad Air 2 coupé, « sur les téléphones », Razer sans « premier », DJ recalé sur la phrase de Google, logo Flutter retiré du RenderThread.
2. Répondre au « paraît » dans la section 6 : la piste de Google (le fil principal bloqué), puis ton avis.
3. Faire revenir Guitar Hero (orchestre, Perfetto) et transformer le FPS en retournement côté Android.
4. Couper Android 4.0, le troisième tampon, Android 11 et les sept tics ; réduire les « Et ».
5. Resserrer le hook (contraste à 13,7 s) et avancer l'abonnement à 23 %.

## Vérification des faits du script V1

Chaque affirmation de la voix off, dans l'ordre. ✅ = fait ✅ de `sources.md` ; ⚠️ = fait ⚠️ dit avec sa bonne formulation ; ✏️ = corrigé dans `script.md` ; ✂️ = coupé.

| Temps | Phrase du V1 | Fait | Verdict |
|---|---|---|---|
| 0:08 | « une nouvelle image toutes les seize millisecondes » | 16 | ✅ |
| 0:20 | « L'iPhone sort en 2007. Et il faut attendre 2012 pour que tout Android batte au rythme de l'écran. » | 12, 30, 1 | ⚠️ formulation exacte de la 2e vérif. Le sous-entendu « l'iPhone de 2007 battait déjà » n'est jamais dit ; la section 5 parle de calques, pas de VSync en 2007 (fait 27) |
| 0:30 | « un ancien stagiaire d'Android publie sa réponse. La presse tech la reprend. Et des ingénieurs la démontent. » | 13, 32 | ⚠️ seconde main (AppleInsider, Cult of Mac, PhoneArena) |
| 0:40 | « soixante fois par seconde… seize virgule six sept… huit virgule trois trois » | 16 | ✅ |
| 1:10 | « si elle arrive en retard, l'écran garde l'ancienne image, et la page saute » | 15 | ✅ (définition du hitch, Apple) |
| 1:26 | Le barème de 5 et 10 ms par seconde | 15 | ✅ |
| 2:09 | « D'après Nick Lockwood… dès le premier iPhone, l'interface est faite de calques assemblés par la puce graphique » | 27 | ⚠️ attribué à Lockwood, comme demandé |
| 2:20 | « sur iOS, chaque élément de l'écran repose sur un calque » | 17 | ✅ |
| 2:35 | « Core Animation… garde le contenu de ces calques en mémoire sous forme d'images… le matériel graphique les manipule directement » | 17 | ✅ |
| 2:45 | « l'iPhone peut se contenter de faire glisser la feuille, sans redessiner ta liste à chaque image » | 34 (ajouté) | ✅ absent de `sources.md` : vérifié dans le guide Core Animation (un changement de propriété ne change que l'état du calque ; le matériel rend l'image déjà en mémoire) |
| 2:55 | « une conférence pour développeurs de 2020 : … une boucle en cinq temps… le serveur de rendu » | 14 | ✅ |
| 3:43 | Le minuteur de UIScrollView et l'annulation du toucher | 18 | ✅ |
| 4:10 | « Depuis iOS 9, en 2015, l'iPhone… prédit où sera ton doigt » | 19 | ✅ |
| 4:20 | « Et cette année-là, Apple présente l'iPad Air 2 » | 37 (ajouté) | ❌ présenté le 16/10/2014. ✂️ |
| 4:25 | « son écran tourne à soixante hertz, mais il lit le tactile à cent vingt. Deux fois plus vite que tous les autres » | 19 | ✅, mais ✂️ avec la phrase précédente |
| 4:40 | « la presse tech se pose une question : pourquoi les animations d'Android traînent derrière celles de l'iPhone ? » | 9 | ⚠️ (titre de 9to5Google, 5/12/2011) |
| 4:55 | « c'est un étudiant, ancien stagiaire dans l'équipe Android… sur iOS, l'interface serait dessinée dans un fil à part, avec une priorité temps réel » | 13 | ⚠️ légende au conditionnel, étudiant non nommé ✅ |
| 5:20 | « Bob Lee, ancien responsable des bibliothèques d'Android, parle d'erreurs de raisonnement » | 13, 32 | ⚠️ seconde main (PhoneArena) |
| 5:25 | « Un autre, Jay Freeman, dit que c'est tout simplement faux » | 13, 32 | ⚠️ ✏️ « le créateur de Cydia » ajouté |
| 5:30 | « Et l'étudiant finit par corriger son post » | 13, 32 | ⚠️ ✏️ « mettre son post à jour » |
| 5:35 | « dans les pages qu'on a lues, aucune ne parle d'une priorité temps réel » | 13 | ✅ (dit honnêtement : « les pages qu'on a lues ») |
| 5:47 | « d'après Dianne Hackborn… en 2011, Android assemble les fenêtres… depuis avant la version 1.0 » | 9, 33 | ⚠️ ✏️ l'ordre des posts est rétabli (« elle avait déjà… ») |
| 6:05 | « la puce graphique ne s'en charge qu'à partir d'Android 3.0 » | 8 | ✅ |
| 6:10 | « Et par défaut, seulement pour les applis qui visent Android 4.0 ou plus » | 8 | ✅, mais ✂️ (durée) |
| 6:20 | « la puce graphique n'est pas une solution miracle pour une interface fluide » | 9 | ⚠️ (seconde main, formulation fidèle) |
| 6:37 | « Avant Android 4.1, les animations et les dessins d'Android n'étaient pas calés sur le battement » | 2 | ✅ |
| 7:03 | « Fin juin 2012, à la conférence Google I/O, … Chet Haase et Romain Guy… « For Butter or Worse » » | 5, 7 | ✅ (sans jour de sortie) |
| 7:15 | « ce chantier, la presse l'appelle Project Butter » | 5 | ⚠️ formulation exacte |
| 7:30 | « tout le système avance au même pas, sur un battement de seize millisecondes… c'est Google qui l'emploie » | 1 | ✅ |
| 7:48 | Choreographer | 6 | ✅ |
| 8:11 | « Android 4.1 ajoute aussi un troisième tampon d'image » | 3 | ⚠️ formulation exacte, mais ✂️ (durée, hors du fil) |
| 8:20 | Le toucher calé sur le battement, le doigt deviné, le coup d'accélérateur | 4 | ✅ |
| 8:30 | « trois ans avant qu'Apple l'ouvre aux développeurs de l'iPhone, avec iOS 9 » | 19 | ✅ sur le fond (`predictedTouches` depuis iOS 9.0) ; ✏️ « côté iPhone, cette prédiction n'arrive dans la doc des développeurs qu'avec iOS 9 », pour ne pas sous-entendre qu'Android l'« ouvrait » aux développeurs |
| 8:41 | « Une modif du 3 mai 2012, pour le Galaxy Nexus… « Boost pulse CPU speeds » » | 25 | ✅ |
| 9:10 | « Quand l'appli elle-même prend du retard sur son fil principal, les animations trinquent avec elle » | 10 | ✅ (déduit de la phrase de Google sur Lollipop) |
| 9:19 | « Fin 2014, Android 5.0… le RenderThread… garde les animations fluides même quand le fil principal de l'appli a du retard » | 10, 11 | ✅ |
| 9:34 | « ton appli peut aller chercher ses données ou faire un gros calcul, l'animation continue de tourner » | 10, 35 | ❌ trop fort. ✏️ (voir grill, point 1) |
| 10:00 | Le récap des trois marches, « d'après Lockwood » | 27, 8, 1, 10 | ⚠️ ✅ |
| 10:29 | « environ huit téléphones sur dix qui vont sur le web en Afrique sont des Android » | 23 | ✅ |
| 10:40 | « environ la moitié des smartphones vendus en Afrique en 2025 sont des Tecno, des Infinix ou des itel » | 24 | ⚠️ formulation exacte |
| 10:50 | « un Tecno de 2025 tourne sur un Android bien plus récent que la version 5.0. Donc le battement de 2012 et le fil de rendu de 2014, il les a. » | déduction, 35 | Déduction logique ; la 2e moitié est maintenant tenue par la doc actuelle d'Android (fait 35) |
| 11:09 | « Android a même ouvert le bal. En novembre 2017, Razer présente son Razer Phone… comme le premier écran à cent vingt hertz » | 22, 36 | ❌ trop fort (iPad Pro, juin 2017 ; Sharp avant Razer). ✏️ « sur les téléphones », sans « premier » |
| 11:20 | « L'iPhone, lui, passe à cent vingt hertz en septembre 2021, avec l'iPhone 13 Pro. Quatre ans plus tard. » | 20 | ✅ |
| 11:30 | « beaucoup de téléphones Android ont des écrans à quatre-vingt-dix ou cent vingt hertz » | 21 | ✅ |
| 11:40 | « depuis Android 11, une appli peut dire au système à quel rythme elle veut être affichée » | 21 | ✅, mais ✂️ (durée, liste) |
| 11:50 | « Perfetto, un outil de traçage, intégré depuis Android 10 » | 29 | ✅ |

**Ajouté à `sources.md`** (faits 32 à 37, « ajouté au grill, vérifié le 23/10/2026 ») :
- 32 : Cydia, Bob Lee et le post mis à jour (PhoneArena, Ole Begemann) ;
- 33 : l'ordre des posts Hackborn → étudiant → Hackborn ;
- 34 : Core Animation ne redessine pas un calque qui bouge ;
- 35 : la doc actuelle d'Android (Choreographer, RenderThread, le fil principal bloqué) ;
- 36 : le 120 Hz de l'iPad Pro (juin 2017) et du Sharp Aquos R Compact ;
- 37 : la date de l'iPad Air 2.

**Ce que j'ai corrigé dans `script.md`** :
- **Retiré** :
  - l'iPad Air 2 « cette année-là » (faux) ;
  - « Android a ouvert le bal » au sens large ;
  - Razer « premier » ;
  - « faire un gros calcul, l'animation continue » ;
  - le logo Flutter sur le RenderThread ;
  - Android 4.0, le troisième tampon et Android 11 (coupes de durée, faits justes).
- **Reformulé** :
  - « corriger son post » devient « mettre son post à jour » ;
  - « trois ans avant qu'Apple l'ouvre aux développeurs » devient « n'arrive dans la doc des développeurs qu'avec iOS 9 » ;
  - Hackborn arrive « déjà » avant l'étudiant ;
  - « sur les téléphones, c'est même Android qui ouvre le bal ».
- **Ajouté (sourcé)** :
  - Jay Freeman, « le créateur de Cydia » ;
  - Hackborn qui rejette la priorité temps réel ;
  - « la doc d'Android parle encore aujourd'hui du chorégraphe et du RenderThread » ;
  - « souvent, l'image saute parce que le fil principal de l'appli est bloqué ».

**Points non résolus** :
- Le nom « Project Butter » : Google l'a peut-être prononcé au keynote d'I/O 2012, mais aucune page Google lue ne le dit, d'où « la presse l'appelle », qui reste vrai.
- Les posts de Munn, Hackborn et Bob Lee n'ont pas été lus à la source (Google+ a fermé) : tout le chapitre 3 repose sur la presse de 2011, et le script le dit (« D'après la presse de l'époque »).

## Questions pour l'auteur

1. **Ton vécu de dev** (9:21 dans la V2) : as-tu déjà vu une interface geler parce qu'un calcul tournait sur le fil principal (en Flutter ou en Kotlin), et qu'as-tu fait ? C'est ce qui donnerait un enjeu au narrateur (axes 7 et S5). Sinon, la phrase saute.
2. **Ton avis** (11:12) : au-delà du fil principal bloqué, si un Android rame encore en 2026, d'où ça vient selon toi ? L'appli, la puce, la surcouche du fabricant ? C'est ce qui tient le « paraît » du titre.
3. **Les noms** : on garde Bob Lee et Jay Freeman (cités par la presse de 2011), sans nommer l'étudiant ? Pour info, Bob Lee est mort en avril 2023 ; la phrase parle de 2011 et n'a pas à changer, mais des commentaires pourraient le rappeler.
4. **La miniature** : on abandonne l'« Android flou » pour le doigt et le « MISS », ou pour « 2007 → 2012 » ?
5. **Ton téléphone** : si c'est un Android à 120 Hz, une phrase sur lui au moment du Razer Phone rendrait la fin plus personnelle.
