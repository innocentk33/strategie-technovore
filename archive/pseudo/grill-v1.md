# Grill du script pseudo v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Grille : `youtube-script-grill`, mode B (après l'écriture), **variante storytelling** (test des 30 secondes, axe 10 des liaisons, axes S1 à S6).
> Hypothèses : titre *Comment un site sait instantanément que ton pseudo est déjà pris*, miniature `noir-07.png` (formulaire, « technovore » en erreur, « il triche. », sans le « G »), public de 18-30 ans, curieux de tech, avec une part de devs ; pilier « Le génie derrière l'app », joker du calendrier, sortie le lun. 23 nov.
> Mesures faites avec `controle.py` et un comptage par section ; débit de référence : 145 mots/min (ArtCraft), 165 à 180 en coupes serrées.
> Version corrigée : [`script.md`](script.md).

## Verdict

C'est le script le plus propre de la série à ce stade : 2,3 liaisons pour 100 mots (nos téléprompteurs : 0,7 à 0,9), zéro « vous », zéro fausse opposition, et une honnêteté qui le distingue de ByteMonk (« Honnêtement, je ne sais pas », les géants tamponnés « aucune source »). La fin retourne quelque chose (le pseudo libéré que seule la base voit libre), et les abandons de Chrome et de Medium donnent un vrai second acte.

Le plus gros problème est un trou dans l'explication, qui touche la promesse : le filtre de Bloom ne sait jamais dire « pris ». Son seul « non » sûr, c'est « pas pris ». Ton « déjà pris » en rouge, celui du titre et de la miniature, vient donc toujours de la base. Le V1 ne le dit jamais, alors que la miniature dit « il triche. » : le spectateur repart en croyant que le videur a décidé du rouge. C'est aussi le meilleur retournement possible de la vidéo, et il ne coûte que quatre phrases.

Deuxième problème : le hook répond à sa propre question dès 0:17 (« En fait, il a un index »), avec la réponse la moins excitante. Troisième : le clin d'œil Claude, sourcé mais mal placé et à contre-emploi. Rien de bloquant : **🟠, 7/10**, une passe ciblée suffit.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Le titre et la miniature parlent de « déjà pris », mais le script ne dit jamais que le filtre ne sait pas dire « pris » ; le hook répond « un index » à 0:17. |
| 2. Alignement | 🟢 | Aucune vente ; un appel à l'abonnement court, un appel au commentaire utile. |
| 3. Problème profond | 🟠 | Surface : comment le site sait. Profond : peut-on croire une réponse qui a le droit de mentir ? Il est là en filigrane (« la base a le dernier mot »), jamais posé au spectateur ; la frustration du pseudo pris (section 1) attend ton anecdote. |
| 4. Public & complexité | 🟢 | Dictionnaire avant l'arbre B, moulinette avant le hachage, deux exemples seulement ; « arbre B » en bandeau pour les devs. |
| 5. Valeur & originalité | 🟢 | Ce que ByteMonk n'a pas : la preuve que personne ne documente le filtre pour les pseudos, Akamai, la serviette, et deux abandons datés. |
| 6. Structure & transformation | 🟢 | Méthode bête → index → astuce → vrais clients → abandons → croix rouge. Début : « le site a triché ? » ; fin : « la base décide toujours ». |
| 7. Histoire | 🟠 | Enquête plutôt que voyage du héros, c'est le bon choix. Mais les personnes n'arrivent qu'à 7:05 (Talbot) ; avant, ce sont des entités (« le site », « la base »). |
| 8. Mais / donc | 🟠 | Très bon dans les sections 2, 3 et 5 ; la section 4 est une liste (« Cassandra fait pareil », « Akamai », « Et puis Medium ») sans obstacle entre les exemples. |
| 9. Engagement actif | 🟠 | Le spectateur n'est jamais invité à deviner. La question « et quand c'est vraiment pris, il répond quoi ? » est faite pour ça. |
| 10. Rythme, oralité & liaisons | 🟢 | 2,3 liaisons pour 100 mots, mais une rafale de dix phrases dans la section 5, la section 4 à 1,7, et zéro « en effet » (ton mot). |
| 11. Tics d'IA | 🟠 | Peu, mais visibles : une phrase copiée de l'exemple du skill, quatre fragments, l'honnêteté annoncée trois fois, un faux suspens. |
| S1. Les 30 premières secondes | 🟠 | Question centrale à 0:15, pont à 0:28, 76 mots ; mais la phrase 15-20 s répond déjà (« il a un index »). |
| S2. Le pont | 🟢 | « Medium s'en est servi pendant dix ans… avant de la jeter » ouvre une deuxième question. Le « dix ans » est à recaler (voir les faits). |
| S3. Les retournements | 🟠 | Un toutes les 30 s dans la section 3 ; un trou d'environ 1 min 40 dans la section 4 (Bigtable → Medium) sans « sauf que ». |
| S4. Planté / récolté et motif | 🟢 | La croix rouge (début et fin), les cases (sections 3, 5 et 6), le videur en motif. Une récolte manque : la suppression devrait faire mentir le « non » sûr. |
| S5. Personnages et enjeu | 🟠 | Talbot, Sarah, Hess, Montaud ont une envie, mais tard ; le seul « quelqu'un qui veut quelque chose » de la première moitié, c'est toi et ton pseudo, sans ta matière. |
| S6. La fin | 🟢 | Elle retourne : le filtre dirait « peut-être pris », la base répond « libre ». Le clin d'œil Claude, juste avant, la retarde. |

Bilan : 8 🟢, 9 🟠, 0 🔴.

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** (titre + miniature) : « Le site sait tout de suite que ton pseudo est pris. Il triche. Comment ? » La vidéo doit montrer la triche, et dire honnêtement qui la pratique. Le V1 tient la deuxième moitié (l'aveu, les tampons), pas tout à fait la première : il ne dit pas sur quelle réponse le videur triche.
- **Le problème profond** : la confiance dans une réponse instantanée. Le filtre échange de la vérité contre de la vitesse, la base garde la vérité. Le V1 le résout à la fin (« c'est la base qui a le dernier mot ») sans l'avoir posé. Le retournement de la section 3 le pose : « ton rouge, c'est toujours la base ».
- **La chaîne du V1** :
  1. Tu tapes, c'est pris, **mais** il y a un milliard de comptes, **donc** comment ?
  2. La méthode bête ne tient pas, **donc** un index.
  3. L'index marche, **sauf que** chaque question va jusqu'à la base, **donc** Bloom.
  4. Le « non » est sûr, **mais** le « peut-être » ment, **donc** la base vérifie.
  5. [manque : **mais** alors, qui décide du « pris » ?]
  6. Personne ne dit s'en servir pour les pseudos, **mais** des grands s'en servent ailleurs.
  7. Google, Cassandra, Akamai, Medium : **et**, **et**, **et puis** (la liste).
  8. Medium l'aimait, **et pourtant** il l'a jeté, **parce qu'**on ne peut rien effacer.
  9. Retour à la croix rouge, **donc** la base rattrape le videur.

## Test des 15 premières secondes

Relues seules, à 145 mots/min (36 mots) :

> « Tu tapes ton pseudo, et avant même d'avoir fini : « Déjà pris. » Instantanément. Sauf que derrière ce formulaire, imagine un milliard de comptes. Le site n'a pas eu le temps de les regarder un par un. Alors comment il sait ? »

- **Le moment le plus fort ?** L'image de la miniature (le champ rouge avant la dernière lettre) est là dès la première seconde, et le contraste « un milliard de comptes / pas le temps » monte l'enjeu. Pas de contexte, pas de présentation, pas de « dans cette vidéo ». 🟢
- **Ce qui manque** : la promesse « il triche » tombe juste après 15 s, et la phrase suivante (« En fait, il a un index ») la désamorce. La règle des 15 s tient ; c'est la tranche 15-30 s qui flanche.

## Test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Tu tapes ton pseudo, et avant même d'avoir fini : « Déjà pris. » Instantanément. » | 🟢 Le sujet et la tension, raccord avec la miniature et le mot du titre. |
| 5-15 s | > « Sauf que derrière ce formulaire, imagine un milliard de comptes. Le site n'a pas eu le temps de les regarder un par un. » | 🟢 Le contraste, chiffre présenté comme une hypothèse (« imagine »). |
| 15-30 s | > « Alors comment il sait ? En fait, il a un index. Et il existe même une astuce plus rapide, inventée en mille neuf cent soixante-dix, qui accepte de se tromper. Exprès. » | 🟠 La question centrale est bien là (0:15), une seule, en mots simples. Mais « En fait, il a un index » y répond aussitôt, avec la réponse la plus banale : le spectateur qui voulait la triche entend « un index ». |
| Pont | > « Medium s'en est servi pendant dix ans… avant de la jeter. » | 🟢 Deuxième question ouverte avant la première résolue (pourquoi la jeter ?). « Dix ans » est une déduction (voir les faits). |

**Budget** : 76 mots ≈ 31 s à 145 mots/min, 25 s à 180. Dans la cible (75 à 90).
**À couper** : rien ne saute entièrement ; « En fait, il a un index » doit rétrécir et passer derrière un « mais ».
**Réécriture des 30 s** (88 mots, reprise dans `script.md`) :

> Tu tapes ton pseudo, et avant même la dernière lettre : « Déjà pris. » Instantanément.
> Sauf que derrière ce formulaire, imagine un milliard de comptes. Le site n'a pas eu le temps de les regarder un par un. Alors comment il sait ?
> Normalement, avec un index. Mais il existe une astuce plus rapide, inventée en mille neuf cent soixante-dix, qui peut te répondre sans ouvrir un seul compte. Et qui a le droit de se tromper. Exprès.
> Et Medium s'en est servi pendant une dizaine d'années… avant de la jeter.

Les 6 questions : première phrase 🟢 · meilleur moment avant 15 s 🟢 · question centrale avant 30 s 🟢 (0:14) · pont 🟢 · chaque phrase utile 🟢 (l'index reste, en une demi-phrase, parce que c'est la vraie réponse et que la ligne 22 de `sources.md` l'exige) · budget 🟢 (88 mots, 36 s à 145, 29 s à 180).

## L'axe 10 : les liaisons

Comptage sur la voix off du V1 (sans les indications), avec la liste du skill : **34 liaisons pour 1 498 mots, soit 2,3 pour 100** (2,1 sans les « mais »). C'est dans la fourchette de Cam et V2F (1,5 à 2,7).

| Section | Mots | Liaisons | Pour 100 mots |
|---|---|---|---|
| 0. Hook | 76 | 3 | 3,9 |
| 1. Le pseudo | 118 | 2 | 1,7 |
| 2. L'index | 252 | 5 | 2,0 |
| 3. Le videur | 396 | 11 | 2,8 |
| 4. Qui l'a embauché | 294 | 5 | 1,7 |
| 5. La porte | 226 | 5 | 2,2 |
| 6. Fin | 136 | 3 | 2,2 |

Répartition : donc 5, du coup 4, en fait 3, tu vois 3, mais 3, sauf que 2, imagine 2, tu te rappelles 2, et pourtant 2, forcément 2, puis une fois chacun : résultat, pour faire simple, et là, parce que, effectivement, bref. **Aucun « en effet »**, alors que c'est ton mot.

**Les rafales** (trois phrases de faits ou plus sans liaison, sans réaction, sans « tu ») :

> « Et Medium n'est pas le premier à se poser la question. En deux mille onze, un développeur de Chrome, Scott Hess, propose de remplacer le filtre de Bloom qui gardait la liste des sites dangereux. Son argument : le filtre ne fait gagner que vingt-deux pour cent de place. Son remplaçant prend un tiers de mémoire en moins… et lui ne se trompe jamais. Le remplacement commence cette année-là. Pour Medium, c'est en deux mille vingt-cinq. Un de leurs ingénieurs, Raphael Montaud, raconte pourquoi ils ont retiré leurs filtres. Ils avaient grossi jusqu'à des milliards d'éléments. »

La plus longue du script : dix phrases, deux histoires, aucune liaison. **Correction** : « Parce que face à une simple liste… », « Et en effet, le remplacement commence… », « En gros, le videur prenait presque autant de place qu'une liste, et en plus, il mentait. », « Pour Medium, donc, c'est en deux mille vingt-cinq. Raphael Montaud, l'ingénieur du videur… ».

> « C'est notre « sûrement pas pris », version Google. Cassandra, une base de données open source, fait pareil : un filtre par fichier, réglé par défaut sur un pour cent d'erreur. Akamai, un des grands réseaux qui livrent les pages web, a mesuré un truc fou. Sur quarante-cinq serveurs… »

Une liste : chaque client arrive sans raison d'arriver là. **Correction** : couper Cassandra (un « fait pareil » de plus, la seule ligne sans image), et lier Akamai par son problème (les objets d'un seul tube) puis par « Et en effet » sur le résultat.

> « Et puis Medium, la plateforme de blogs. L'histoire commence à un dîner d'anniversaire : une collègue de Jamie Talbot, Sarah, lui demande comment Medium sait si quelqu'un a déjà lu un article. Il lui dessine un filtre de Bloom sur des serviettes. »

**Correction** : « Et là, en plein repas, il lui dessine… ».

## Les tics d'IA

| Passage | Tic | Correction |
|---|---|---|
| « Ouais, t'as bien entendu. » | phrase copiée telle quelle de l'exemple du skill (Cam) : le skill demande de reprendre le mécanisme, jamais la phrase | une réaction à toi, qui traduit le chiffre : « Quinze millions par seconde, juste pour savoir si tu as déjà lu un article. » |
| « Petit détail pour finir : cette image du videur… » | faux suspens d'annonce, juste avant la fin | supprimé avec le clin d'œil (voir le grill, n° 3) |
| « Instantanément. » / « Exprès. » / « Quelques-unes. Sur un milliard. » / « Ailleurs. » | fragments dramatiques en cascade (quatre) | on garde « Instantanément » (le mot du titre) et « Exprès » (la promesse) ; « Quelques-unes, sur un milliard » en une phrase ; « Ailleurs » devient « pour d'autres portes » |
| « Voilà la réponse honnête… » / « Honnêtement, je ne sais pas. » / « je ne vais pas te l'inventer » | l'honnêteté annoncée trois fois en trois minutes : à force, ça sonne « je ne vais pas te mentir » | « Voilà la première réponse » ; on garde « Honnêtement, je ne sais pas », qui est le moment fort |
| « Moi, j'ai cherché. » / « Et j'ai retrouvé leurs chiffres. » | une action personnelle que tu n'as pas faite (la recherche est celle de `sources.md`) | « on a cherché » ; « Et eux, ils ont publié leurs chiffres. » |
| « Par contre, ce videur, les grands l'ont bien embauché. Ailleurs. » | fragment + formule d'annonce | « des grands l'ont bien embauché, pour d'autres portes » |

Passe de vérification : aucune fausse opposition (« ce n'est pas A, c'est B ») dans le V1 ni dans la version finale. Le « Le « non » est sûr. Le « peut-être » peut mentir. » est un parallèle voulu, qui résume la règle : à garder.

## La rétention

| Repère | V1 | Verdict |
|---|---|---|
| Relances | 24 en 10 min 20, une toutes les 26 s ; la plus longue plage ≈ 40 s | 🟢 |
| Appel à l'abonnement (~25 %) | 2:40 (26 %), juste après « Voilà la réponse honnête… : un index » | 🟠 il tombe sur une boucle fermée, au moment où le spectateur a sa réponse. Le mettre après le pont vers Burton Bloom, boucle ouverte (2:58 dans la version finale) |
| Relance forte (~60 %) | 5:48 (56 %) : changement de musique, « 3. Les vrais clients du videur » | 🟢 ; mais derrière, 1 min 40 de liste sans retournement (S3) |
| Ponts entre sections | « un dictionnaire », Burton Bloom, « j'ai retrouvé leurs chiffres », « Medium l'a mis à la porte », « revenons à ta croix rouge » | 🟢 sauf le troisième, à reformuler (tic) |
| Fin | clin d'œil Claude à 9:10, puis la croix rouge | 🟠 un détour de 15 s juste avant la boucle finale |
| Écran de fin | « Waze… (ou Uber) » | à trancher : Waze (voir n° 6) |

## Le grill

### 1. Le videur ne sait jamais dire « pris », et le script ne le dit pas

> « Peut-être un index qui a trouvé ton pseudo en quelques lectures. Peut-être un videur qui a regardé trois cases. Mais dans les deux cas, c'est la base qui a le dernier mot. »

**Pourquoi ça coince** : avec un pseudo vraiment pris, les trois cases sont allumées, le filtre répond « peut-être », et c'est la base qui dit « pris » (`sources.md`, faits 3 et 29). Le filtre accélère les pseudos **libres**, pas les pseudos pris. Le titre (« déjà pris ») et la miniature (« il triche. ») laissent croire l'inverse, et le V1 ne corrige jamais l'idée. Un dev en commentaire le relèvera tout de suite.
**Correction** : un retournement à la fin de la section 3, sous forme de devinette (axe 9) :

> Maintenant, prends deux secondes. Ton pseudo est vraiment pris. Qu'est-ce que le videur te répond ?
> Peut-être. Son seul « non » sûr, c'est « pas pris ». Donc ton « déjà pris » en rouge, c'est toujours la base qui l'a décidé, derrière lui. En fait, le videur ne triche que quand ton pseudo est libre : là, il te répond sans aller voir.

Et la fin s'y raccorde : « Peut-être un videur qui a regardé trois cases, haussé les épaules, et passé la question à la base. Mais dans les deux cas, ton rouge, c'est la base qui l'a mis. »

### 2. Le hook répond à sa question au bout de deux secondes

> « Alors comment il sait ? En fait, il a un index. »

**Pourquoi ça coince** : la question centrale tombe à 0:15 et sa réponse à 0:17. Le spectateur a cliqué pour « il triche » ; il entend la réponse la plus banale, et le « Et il existe même une astuce » arrive en rattrapage. Le V1 l'avait vu (« Points de décrochage ») sans le corriger.
**Correction** : l'index en une demi-phrase, puis un « mais » qui porte la promesse : « Normalement, avec un index. Mais il existe une astuce plus rapide, inventée en mille neuf cent soixante-dix, qui peut te répondre sans ouvrir un seul compte. Et qui a le droit de se tromper. Exprès. » (« peut te répondre » : honnête, puisqu'elle ne répond seule que pour les pseudos libres.)

### 3. Le clin d'œil Claude

> « Petit détail pour finir : cette image du videur, Montaud dit l'avoir obtenue en demandant à Claude, une IA, de lui résumer le filtre simplement. Même l'analogie a été générée. »

**Sourcé ?** Oui : Montaud écrit « I asked Claude to summarize Bloom filters in a really simple way and it went with a funny analogy » (`sources.md`, fait 27, relu le 23/10).
**Utile ?** Non, à cet endroit :
- il tombe à 9:10, entre la chute et la boucle finale, et retarde la fin de 15 s ;
- il ne dit rien des pseudos ni du filtre ;
- « Même l'analogie a été générée » dit au spectateur que l'image centrale de ta vidéo vient d'une IA. Sur une chaîne qui veut des scripts humains, c'est se tirer une balle dans le pied, et la pique tombe à plat dans le pilier génie.
**Dans ton ton ?** La chute « Même l'analogie a été générée » sonne comme une morale, pas comme ta blague.
**Correction** : retiré de la voix off. À la place, le crédit honnête là où l'image arrive : « Un ingénieur de Medium a une image pour ça, et je te la pique : un videur de boîte de nuit, avec une très bonne mémoire, mais pas parfait. » (`sources.md`, ligne 31). Ça plante Medium dès 4:45, et la section 5 le récolte : « Raphael Montaud, l'ingénieur du videur ». Si tu tiens au détail Claude : description ou commentaire épinglé (question 5 de `script.md`).

### 4. La suppression ne récolte pas la règle du « non » sûr

> « Une case peut servir à plusieurs pseudos à la fois. Si tu l'éteins pour en retirer un, tu abîmes aussi les autres. »

**Pourquoi ça coince** : « tu abîmes » reste abstrait, alors que la section 3 a posé la seule règle du filtre : le « non » est sûr. C'est elle qui casse.
**Correction** : « Du coup, « zorro », qui existe bien, sortirait « jamais ajouté ». Et le seul « non » sûr du videur deviendrait faux. » Puis « Voilà pourquoi, chez Medium, un auteur que tu avais masqué… restait masqué pour toujours. »

### 5. La section 4 est une liste

> « Cassandra, une base de données open source, fait pareil… Akamai, un des grands réseaux… Et puis Medium… »

**Pourquoi ça coince** : quatre clients d'affilée, reliés par « et » ; 1 min 40 sans « sauf que » (S3). C'est l'endroit de la vidéo où la rétention chute d'habitude (la relance des 60 %).
**Correction** : couper Cassandra (20 mots, aucune image, un deuxième « fait pareil » après Bigtable) ; donner un problème à Akamai avant le chiffre (les objets d'un seul tube, « forcément, les garder en cache, c'est gâcher de la place ») ; « Et en effet » sur le résultat ; remplacer « Ouais, t'as bien entendu » par une traduction du chiffre.

Au passage, **deux « soixante-quatorze pour cent » d'affilée** pour deux choses différentes (74 % d'objets vus une fois, puis un cache qui part de 74 %) : à l'oral, on les confond. Le premier devient « presque trois objets sur quatre », et les deux s'affichent dans deux couleurs.

### 6. L'écran de fin : Waze

> « Et la vidéo juste là, c'est Waze… » / « [VISUEL : … vidéo Waze à gauche (ou Uber)…] »

**Décision** : **Waze**. Il sera en ligne depuis deux semaines (9/11), c'est la vidéo génie la plus récente, et son propre écran de fin pointe vers Uber : la chaîne pseudo → Waze → Uber suit la playlist du pilier (`CLAUDE.md`, « l'enchaînement »). Le pont s'écrit tout seul : le filtre se trompe tout seul dans un sens, Waze, des chercheurs l'ont fait se tromper exprès (le faux bouchon de 2014, `sources.md`, ligne 32). **Exception** : si le pseudo sort plus tôt comme joker (avant le 9/11, cas prévu pour le 2 nov. dans `calendrier.md`), Waze n'existe pas encore : écran de fin vers Uber, avec la phrase de rechange notée dans le script.

### 7. Petits points

- « Moi, ce qui m'intéresse, c'est ce qui se passe entre ta dernière lettre et le rouge » : une envie qu'on te prête, mais elle est raisonnable et elle ouvre le chapitre. Garde-la si elle est vraie.
- « kirito » libre dans l'exemple : dans la vraie vie, aucun gamer n'y croira. Autant en faire une blague (« Dans la vraie vie, « kirito » libre, tu peux toujours rêver ») plutôt que de laisser un commentaire le faire.
- La section 1 reste ta seule matière personnelle, et elle est encore entre crochets. Sans elle, le problème profond (le pseudo qu'on n'a jamais eu) reste générique.

## La vérification des faits du script, phrase par phrase

| Phrase du V1 | Source | Verdict | Dans `script.md` |
|---|---|---|---|
| « Instantanément » (et le titre) | fait 14, 23 | ⚠️ aucune mesure ; qualitatif, accepté | gardé ; mesure proposée (question 3) |
| « imagine un milliard de comptes » | faits 5, 22 | ✅ présenté comme une hypothèse | gardé |
| « En fait, il a un index » | faits 13, 22 | ✅ | « Normalement, avec un index » |
| « une astuce plus rapide, inventée en mille neuf cent soixante-dix, qui accepte de se tromper » | faits 1, 3 | ✅ | gardé, avec « qui peut te répondre sans ouvrir un seul compte » (vrai pour les pseudos libres, faits 2 et 29) |
| « Medium s'en est servi pendant dix ans » | absent : déduction 2015 → 2025 | ⚠️ vérifié au grill : usage attesté en juin 2015 (dîner de juin, « how we use it at Medium »), retrait en 2025 sans date exacte ; « dix ans » pile n'est pas démontré | « une dizaine d'années » ; ligne 30 ajoutée |
| « Ce que les sites font vraiment… un dictionnaire » ; l'arbre B, « quelques lectures » | faits 13, 18 | ✅ (« quelques », pas « 3 à 4 ») | gardé |
| « Sur PostgreSQL… la base crée toute seule un index unique. C'est lui qui fait respecter la règle. » | fait 13 | ✅ | gardé |
| « deux personnes valident « technovore » à la même seconde ? La base refuse le doublon » | fait 21 | ⚠️ formulation juste (conséquence de la contrainte) | gardé |
| « Et souvent pour rien : le pseudo n'existe pas » | absent | ❌ « souvent » : aucune fréquence sourcée pour les pseudos | « Et quand le pseudo est libre, elle a fouillé… pour ne rien trouver. » |
| « Burton Bloom, publie une idée au titre qui dit tout : gagner de la place et du temps… en autorisant des erreurs » | fait 1 (« Space/time trade-offs in hash coding with allowable errors ») | ✅ | gardé, titre à l'écran |
| Cases, moulinettes, « toujours le même numéro pour le même mot », « on ne garde même pas le pseudo » | fait 2 (tableau de bits, k fonctions) | ✅ | gardé |
| « Le « non » est sûr. Le « peut-être » peut mentir. » ; « la vérification… qu'on aurait faite de toute façon » | faits 3, 20, 29 | ✅ | gardé |
| Le videur (l'image) | fait 27 ; Montaud | ✅ mais présenté comme notre image | crédité à « un ingénieur de Medium » ; ligne 31 ajoutée (citation relue) |
| « moins de dix cases par pseudo… sept moulinettes… cinq lettres ou trente… un virgule deux gigaoctet… un virgule huit » | fait 5 | ✅ | gardé, sauf le 1,8 Go (coupé pour la durée) |
| « C'est la technique qu'on enseigne… dans les tutos et les entretiens d'embauche » | faits 15, 16 ; vidéos de référence | ⚠️ déduction honnête (KodeKloud « Interview », exemple du pseudo ; OneUptime) | gardé, dans « Phrases à valider » |
| « des vidéos qui te disent que Google, Amazon ou Meta font exactement ça » | fait 15 (ByteMonk) | ⚠️ ByteMonk dit « Google, Facebook, and Amazon », et « exactement ça » en rajoute | « des vidéos te citent Google, Facebook ou Amazon » |
| « Moi, j'ai cherché. Aucun blog d'ingénierie, aucune conférence d'un grand site ne dit s'en servir pour les pseudos. » | fait 15 (❓) | ⚠️ c'est une absence dans ce qui a été lu, pas une preuve universelle ; et la recherche n'est pas la tienne | « Sauf qu'on a cherché, et on n'a trouvé aucun blog d'ingénierie ni aucune conférence… » |
| « Et j'ai retrouvé leurs chiffres. » | — | ❌ action prêtée | « Et eux, ils ont publié leurs chiffres. » |
| Bigtable 2006, « la plupart des recherches de lignes qui n'existent pas ne touchent même pas le disque » | fait 6 | ✅ | gardé |
| Cassandra, un filtre par fichier, 1 % par défaut | fait 7 | ✅ (0,1 avec LeveledCompactionStrategy, non dit) | coupé (structure, pas fait) |
| Akamai : 45 serveurs, deux jours, 74 % de 400 millions, « one-hit wonders », deuxième demande, 47 serveurs, 74 → 83 % | faits 8, 9 | ✅ | « presque trois objets sur quatre » pour le premier 74 % |
| Sarah, « une collègue de Jamie Talbot », les serviettes, 2015 | fait 26 | ✅ ; plus précis au grill : « Medium's legal counsel » | « Sarah, la juriste de Medium » ; ligne 30 |
| Les trois filtres de Medium (lu, masqué, proposé trois fois), 15 000 et 15 millions par seconde | faits 11, 28 | ✅ | « servaient » (c'est fini) |
| « dix ans après la serviette, Medium l'a mis à la porte » | faits 12, 26 ; ligne 30 | ✅ juin 2015 → 2025 | gardé |
| Chrome 2011, Scott Hess, sites dangereux, 22 %, un tiers de mémoire en moins, zéro erreur, « le remplacement commence cette année-là » | fait 10 | ⚠️ formulation juste ; mais 22 % s'entend « face à rien » | « face à une simple liste, le filtre ne fait gagner que vingt-deux pour cent » (c'est la comparaison de Hess) |
| Montaud 2025, des milliards d'éléments, rien d'effaçable, masqué pour toujours, dix fois moins cher, « pas forcément équitable », « leur vraie base » | faits 4, 12 | ✅ | gardé |
| La clé « Montaud dit l'avoir obtenue en demandant à Claude » | fait 27 | ✅ sourcé | retiré de la voix off (n° 3) |
| Le pseudo libéré : le filtre dit « peut-être », la base dit « libre » | faits 3, 4, 20 | ✅ déduction, au conditionnel | gardé |
| (nouveau) « ton « déjà pris » en rouge, c'est toujours la base qui l'a décidé » | faits 3, 29 | ✅ déduction directe | ajouté (n° 1) |
| (nouveau) « en deux mille quatorze, des chercheurs ont fait croire à Waze à un bouchon qui n'existait pas, avec de faux conducteurs » | absent ; vérifié au grill dans le résumé arXiv:1410.0151 (« fake traffic jams », « bot drivers ») | ✅ | ajouté (écran de fin) ; ligne 32 |

**Lignes ajoutées à `sources.md`** (fin du tableau des faits, « ajouté au grill, vérifié le 23/10/2026 ») : 30 (Medium, une dizaine d'années ; Sarah juriste), 31 (la citation du videur), 32 (le faux bouchon de Waze, 2014).

**Corrigé dans la voix off** : « dix ans » → « une dizaine d'années » ; « souvent pour rien » retiré ; « Google, Amazon ou Meta font exactement ça » → « des vidéos te citent Google, Facebook ou Amazon » ; « aucun blog… ne dit » → « on n'a trouvé aucun blog… » ; « j'ai cherché » et « j'ai retrouvé » → « on a cherché », « ils ont publié » ; Sarah « une collègue » → « la juriste de Medium » ; Chrome « face à une simple liste » ; « servent » → « servaient » ; le premier 74 % → « presque trois sur quatre » ; le clin d'œil Claude retiré ; le videur crédité.

**Rien d'inventé ajouté** : la devinette, la case de « zorro » et la fin sont des déductions des faits 2, 3, 4, 20 et 29. La blague « kirito » est une blague, signalée comme telle.

**Restent hors du script** : « une milliseconde » et « 0,001 s » (faits 14, 23, 25). Note : la fiche, le README et `strategie.md` gardent « en une milliseconde » dans le titre ; je n'y ai pas touché (fichiers pilotes).

## Ce qu'il faut garder

- « xX_Technovore_2007_Xx, comme tout le monde » : ton registre, et tout le monde s'y reconnaît.
- Le dictionnaire papier pour l'arbre B : on comprend « quelques lectures » sans un mot de jargon.
- « Le « non » est sûr. Le « peut-être » peut mentir. » : la règle du filtre en une phrase qu'on répète à un pote.
- « Honnêtement, je ne sais pas » et les tampons « aucune source » : c'est ce qui te distingue de ByteMonk, et ça rend crédible tout le reste.
- Les « one-hit wonders », les chanteurs d'un seul tube.
- Les serviettes du dîner d'anniversaire : la seule scène humaine de la vidéo, sourcée mot à mot.
- « Un auteur que tu avais masqué, puis démasqué, restait masqué pour toujours » : le défaut technique devient un gag.
- La fin sur le pseudo libéré : elle retourne la vidéo au lieu de la résumer.

## Plan d'action

1. **Le retournement du videur** (n° 1) : quatre phrases à la fin de la section 3, et la fin raccordée. C'est la correction de fond.
2. **Le hook** (n° 2) : l'index en une demi-phrase, l'astuce comme promesse, « une dizaine d'années ».
3. **Le clin d'œil Claude** (n° 3) : retiré ; le videur crédité en section 3 et récolté en section 5.
4. **Les sections 4 et 5** (n° 4, n° 5, axe 10) : Cassandra coupée, Akamai liée, la rafale Chrome-Medium cassée, « zorro » qui fait mentir le « non » sûr.
5. **Passe de détail** : les tics, les formulations recalées sur les sources, l'appel à l'abonnement après le pont, l'écran de fin vers Waze.

Tout est appliqué dans [`script.md`](script.md) : 1 625 mots, 47 liaisons (2,9 pour 100 mots), question centrale au 38e mot, zéro « vous ».

## La question

Le pseudo que tu n'as jamais pu avoir : quel jeu, quel pseudo, et ce que tu as pris à la place ? C'est la seule matière à toi de la vidéo, et c'est ce qui donne un visage au problème profond. Si c'est « kirito », dis-le : la blague de la section 3 devient ton anecdote.
