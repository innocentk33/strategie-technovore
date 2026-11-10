# Grill du script Waze v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Version finale : [`script.md`](script.md).
> Grille : `youtube-script-grill`, mode B (après l'écriture), **variante storytelling** (test des 30 secondes, axe 10 des liaisons, axes S1 à S6).
> Hypothèses : titre *Comment Waze sait qu'il y a un bouchon avant que tu le voies*, miniature `noir-03` (le bouchon en rouge, le détour en bleu, « personne ne l'a signalé, il savait. »), public de 18-30 ans curieux de tech, surtout africain, arrivé par les suggestions à côté de la vidéo de Thibaut Dcode ; objectif : 2e vidéo du pilier « Le génie derrière l'app » après Uber.
> Faits revérifiés à la source le 23/10 : voir « Vérification des faits » en bas, et les lignes 36 à 40 ajoutées à [`sources.md`](sources.md).

## Note globale : 7/10

10 🟢, 7 🟠, 0 🔴. Rien de bloquant : les faits sont presque tous tenus, les liaisons sont déjà au-dessus de la cible et le hook passe le test des 15 secondes. Les trois vrais problèmes sont l'ordre des sections (le sommet tombe à 73 %), un pont du hook qui dit une chose fausse à moitié, et quatre phrases qui vont plus loin que leur source.

## Verdict

C'est le meilleur V1 de la chaîne à ce stade : une vraie question (« comment il savait ? ») posée à 0:14, une machine démontée dans l'ordre où elle travaille, une devinette qui fait réfléchir, une expérience de 2014 qui sert de preuve, et une fin qui retourne la situation (« le Karim, c'est toi »). Personne en français ne détaille ce mécanisme, et le script le fait sans jargon.

Le plus gros problème est structurel : le faux bouchon, le moment le plus fort après le hook, arrive après l'explication du calcul, à 73 % de la vidéo. Entre 5:00 et 8:45, la vidéo n'a plus de sommet à promettre. Et la solution proposée par le rédacteur (sortir le serveur de sessions) ne règle pas le problème, voir « La rétention ». Deuxième problème : le script plante de bonnes graines (« Tu râles », « ton trajet habituel », le détour des chercheurs) et ne les récolte pas.

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** (titre + miniature) : Waze sait qu'il y a un bouchon que tu ne vois pas encore, sans que personne ne l'ait signalé. Le spectateur veut savoir *comment*. La V1 y répond (vitesse des téléphones + comparaison avec l'habitude), mais ne dit jamais en clair le « avant que tu le voies » : les téléphones des voitures devant toi ont ralenti pendant que toi, tu voyais encore une route dégagée. Et la fin de la section 3 se trompe de promesse : « Reste la question qui t'a fait cliquer : pourquoi il t'a fait tourner à droite » (la question du clic, c'est *comment il savait*, déjà résolue en section 2).
- **Le problème de surface** : comment une appli détecte un bouchon.
- **Le problème profond** : la confiance dans la machine, et le fait d'en faire partie sans le savoir. Il est semé dans le hook (« Tu râles »), monte en section 1 (« tu bosses déjà pour lui »), revient avec l'inconnu qui signale (section 3) et se résout dans la fin (« j'aide ceux qui vont prendre Waze après moi »). C'est le bon problème profond, et c'est exactement ce dont parle l'article de Petreanu : son anecdote des cinq secondes est l'histoire du jour où il a su qu'il pouvait faire confiance à l'appli (fait 36, ajouté au grill). La V1 ne s'en sert pas. Il manque aussi ton enjeu à toi : il reste un crochet.
- **La chaîne** (V1) : Waze te fait tourner, **mais** tu râles ; **sauf que** la route est bloquée et personne ne l'a signalé, **donc** comment ? → les téléphones envoient leur position, **donc** une vitesse ; **sauf qu'**une vitesse seule ne dit rien, **donc** comparaison avec l'habitude ; **et** la vitesse fluide, **et** la note de 0 à 5, **et** les extrêmes (un passage en « et aussi ») → **mais** les signalements, ils servent à quoi ? → le bouchon sort des vitesses, **donc** Waze ne sait pas pourquoi ça bloque → **et** l'équation, **et** le serveur de sessions → **et si** quelqu'un fabriquait des faux téléphones ? → le faux bouchon.
  Le défaut est visible ici : après la section 3, le calcul et le serveur s'enchaînent en « et ensuite ». Dans `script.md`, la chaîne devient : combien de téléphones ? **Waze ne le dit pas** ; **mais** des chercheurs en ont fabriqué → immobiles, rien ; ralentis, rien ; **donc** départ à 70 puis freinage → bouchon, **et du coup** un détour → **comme ton virage à droite**, **donc** comment il décide ? → le calcul → voilà ton virage.

## Le test des 15 premières secondes

Relues seules, à 145 mots/min (environ 37 mots) :

> « Waze te fait tourner à droite. Tu râles, ton trajet habituel, c'est tout droit. Sauf que sur la route que tu viens d'éviter, tout le monde est à l'arrêt. Et personne ne l'avait signalé. »

🟢 **Oui, c'est le moment le plus fort de la vidéo qui puisse tenir sans préparation** : c'est l'image de la miniature (le détour bleu, la route rouge, « personne ne l'a signalé »), sans contexte, sans présentation, sans accident inventé ni délai chiffré (2e vérif, lignes 29 et 31). Le faux bouchon de 2014 est plus fou, mais il a besoin du mécanisme pour être compris : son teaser à 0:22 suffit.

**« Tu râles » ou la route rouge directe ?** (question du rédacteur). Garde « Tu râles ». Il coûte deux secondes, mais c'est le contraste croyance → réalité que la variante storytelling demande avant 30 s (tu doutes de Waze, Waze avait raison), et il plante le mot « habitude », qui est le cœur de la section 2. La V1 ne récoltait pas cette graine ; `script.md` la récolte (« Et « d'habitude », tu te rappelles ? C'est ce que tu disais au début »). Version resserrée : « Waze te fait tourner à droite. Toi, tu râles : d'habitude, c'est tout droit. »

## Le test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Waze te fait tourner à droite. Tu râles, ton trajet habituel, c'est tout droit. » | 🟢 Le sujet et une tension, raccord avec le détour bleu de la miniature. |
| 5-15 s | > « Sauf que sur la route que tu viens d'éviter, tout le monde est à l'arrêt. Et personne ne l'avait signalé. » | 🟢 Le contraste et l'image promise, avec sa preuve à l'écran (aucune icône de signalement). |
| 15-30 s | > « Alors comment il savait ? » | 🟢 La question centrale, une seule, en mots simples, au 35e mot (la règle : avant le 90e). |
| Pont | > « En fait, la réponse est dans ta poche : ton téléphone fait partie de la machine. Et en deux mille quatorze, des chercheurs s'en sont servis pour fabriquer un bouchon qui n'existait pas. Waze l'a affiché. » | 🟠 Deux soucis. « La réponse est dans ta poche » est à moitié faux : le bouchon que tu as évité, ce sont les téléphones des conducteurs *devant toi* qui l'ont vu, pas le tien. Et « s'en sont servis » ne se comprend pas à l'oral : servis de quoi, de ton téléphone ? |

**Budget :** 73 mots ≈ 30 s à 145 mots/min, 24 s à 180. 🟢
**À couper :** rien. Chaque phrase confirme le clic, ouvre une question ou fait monter l'enjeu.
**Réécriture du pont** (74 mots au total) :

> En fait, la réponse est dans la poche des conducteurs devant toi. Et dans la tienne.
> La preuve : en deux mille quatorze, des chercheurs ont inventé des conducteurs qui n'existaient pas. Et Waze a affiché leur bouchon.

« Et dans la tienne » plante la fin (« le Karim, c'est toi ») ; « La preuve » relie le teaser à la question au lieu de l'empiler.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Le mécanisme est livré dès 3:00, mais « avant que tu le voies » n'est jamais dit en clair, et la section 3 annonce « la question qui t'a fait cliquer » au mauvais endroit. |
| 2. Alignement | 🟢 | Aucune vente ; un appel à l'abonnement court et bien placé ; l'angle « données et gratuité » reste à Thibaut Dcode. |
| 3. Problème profond | 🟠 | La confiance dans la machine est semée et résolue, mais l'anecdote de Petreanu, qui parle justement de confiance, n'est pas branchée dessus, et ton enjeu reste un crochet. |
| 4. Public & complexité | 🟢 | Position → vitesse → comparaison → signalements → calcul : chaque marche s'appuie sur la précédente, avec un exemple chiffré. |
| 5. Valeur & originalité | 🟢 | Les 48 demi-heures, la comparaison relative, le faux bouchon de 2014, l'heure d'arrivée prudente : personne ne le dit en français. |
| 6. Structure & transformation | 🟠 | Le faux bouchon arrive après le calcul (73 %), et le serveur de sessions est hors promesse. |
| 7. Histoire (enquête) | 🟢 | Une enquête claire, avec une escalade réelle dans la partie 2014 (immobiles, ralentis, puis 70 km/h). |
| 8. Mais / donc | 🟠 | Très bon jusqu'à la section 3 ; « Et pour noter… Et chaque bouchon… Et avant de faire sa moyenne » (section 2), puis le calcul et le serveur, s'enchaînent en « et ensuite ». |
| 9. Engagement actif | 🟢 | La devinette des 20 km/h, « tu dois te demander », le retour à la route rouge du hook. |
| 10. Rythme, oralité & liaisons | 🟢 | 2,1 liaisons pour 100 mots, mais quatre rafales de faits (détail plus bas). |
| 11. Tics d'IA | 🟢 | Peu de tics ; trois « exactement » et une phrase de flourish qui ment un peu (« Un million de fois par seconde »). |
| S1. Les 30 premières secondes | 🟠 | Les 6 questions passent, sauf le pont (« dans ta poche », « s'en sont servis »). |
| S2. Le pont | 🟢 | Le teaser des chercheurs ouvre une deuxième question avant que la première soit résolue. |
| S3. Les retournements | 🟢 | 24 relances en 12 min, aucun trou de plus de 60 s. |
| S4. Planté / récolté et motif | 🟠 | Le « tic » sonore et la route rouge reviennent ; mais « Tu râles » et « ton trajet habituel » ne sont jamais récoltés, et le détour des chercheurs n'est pas relié au tien. |
| S5. Personnages et enjeu | 🟠 | Les chercheurs veulent quelque chose et échouent deux fois, Petreanu a une scène ; le narrateur n'a pas d'envie à lui (crochet). |
| S6. La fin | 🟢 | Elle retourne la situation (« le Karim, c'est toi ») ; mais elle commence par un récap et répète l'appel à l'abonnement. |

## Le grill

### 1. Le sommet arrive trop tard, et sortir le serveur ne suffit pas

> « Bon. Si je reprends : chez Waze, ce sont les téléphones qui fabriquent le bouchon. Et si quelqu'un fabriquait des faux téléphones ? » (8:40, 73 %)

**Pourquoi ça coince :** la relance forte doit tomber vers 60 %. Le rédacteur propose de sortir le serveur de sessions (environ 70 mots). Fais le calcul : ces 70 mots sont *avant* la coupure, donc la vidéo raccourcit d'autant. La coupure passe de 1 269 mots sur 1 738 (73 %) à 1 199 sur 1 668 : 72 %. Ça ne bouge presque pas. Pour atteindre 60 %, il faut déplacer du contenu d'avant la coupure à après.
**Correction :** échanger les sections 4 et 5. Le faux bouchon passe juste après les signalements, et il y a deux bonnes raisons de le faire, en plus du chronomètre :
- la question « combien de téléphones il faut ? », que la V1 pose et laisse sans suite, a un seul repère public : les quinze bots de 2014 (fait 28). Elle devient le pont parfait vers l'expérience ;
- le faux bouchon finit sur un détour (« 1,5 km · 3 min » devient « 1,6 km · 4 min »). C'est le pont naturel vers « comment il décide de te dérouter ? », et donc vers le calcul.

Résultat dans `script.md` : coupure musicale à 7:17, soit **58 %**, et le calcul ferme la boucle du hook à 88 %, juste avant la fin. Le serveur de sessions part quand même en réserve, pour une autre raison : il ne sert pas la promesse (voir n° 4).

### 2. Le titre n'est jamais payé en clair

> « Voilà ton virage à droite. Les téléphones devant toi ont ralenti, la comparaison avec l'habitude a dit « bouchon », et le calcul a jugé que ça valait le coup de te dérouter. »

**Pourquoi ça coince :** le titre promet « avant que tu le voies ». La phrase qui le paie, c'est le décalage entre toi et les conducteurs devant : eux sont déjà à l'arrêt, toi tu vois encore une route dégagée. La V1 le laisse deviner.
**Correction :**
> Voilà ton virage à droite. Toi, tu voyais encore une route dégagée. Les conducteurs devant toi, eux, étaient déjà à l'arrêt, et leurs téléphones l'avaient dit à Waze.

Et à la fin de la section 3, remplacer « Reste la question qui t'a fait cliquer » (fausse, la question du clic est déjà résolue) par le pont vers le faux bouchon.

### 3. Les graines plantées ne sont pas récoltées

> « Tu râles, ton trajet habituel, c'est tout droit. »
> « Yigal Petreanu […] raconte qu'au début, il recevait le signalement d'une voiture sur le bas-côté, et cinq secondes plus tard, il voyait la voiture. »

**Pourquoi ça coince :** « ton trajet habituel » annonce le mot clé de la vidéo (l'habitude), et « Tu râles » pose le doute. Aucun des deux ne revient. Or l'article de Petreanu raconte justement comment il a appris à faire confiance à l'appli (« I knew I could trust the app because it had proven to me that Waze knows what's going on »).
**Correction :** deux récoltes.
> (section 2) Et « d'habitude », tu te rappelles ? C'est ce que tu disais au début : d'habitude, c'est tout droit. Sauf que l'habitude de ta route, Waze la connaît mieux que toi.
> (section 3) Et c'est comme ça, dit-il, qu'il a su qu'il pouvait faire confiance à l'appli. Toi, au début de la vidéo, tu râlais encore.

Et une troisième, gratuite : « Un détour. Comme ton virage à droite. » à la fin du faux bouchon.

### 4. Quatre phrases vont plus loin que leur source

> « Un million de fois par seconde, un serveur se demande : « il en est où, lui ? » »

Le million vient d'un **test de charge** (fait 20 ⚠️), en pointes, et ce sont des lectures (MGET), pas forcément des positions. La phrase transforme un test en trafic réel. Retirée avec le bloc (réserve).

> « Du coup, quand tu arrives deux minutes avant l'heure annoncée, c'est voulu. »

Waze dit qu'il penche du côté prudent (fait 13). Ça ne veut pas dire que chaque avance de deux minutes est voulue. → « si tu arrives souvent un peu avant l'heure annoncée, désolé, c'est peut-être pas toi le Vin Diesel : Waze prévoit large exprès. »

> « Et pour noter la gravité, il garde une deuxième référence : la vitesse fluide du tronçon »

La doc donne un niveau de 0 à 5 et un retard *par rapport à la vitesse fluide* (faits 2, 5). Elle ne dit pas que la vitesse fluide « note la gravité ». → « Ensuite, pour chaque bouchon, il note deux choses. Un niveau, de zéro, fluide, à cinq, bloqué. Et le retard en secondes, par rapport à la vitesse fluide du tronçon, la plus haute qu'on y ait mesurée. »

> « Waze garde exprès des trajets stables, parce qu'un GPS qui change d'avis tous les cent mètres, tu le désinstalles. »

Le « parce que » prête à Waze une raison qu'il ne donne pas. C'est ta réaction, dis-la comme telle : « Waze garde exprès des trajets stables. Et heureusement, parce qu'un GPS qui change d'avis tous les cent mètres, tu le désinstalles. »

### 5. Les deux minutes collées à la question du délai

> « Alors forcément, tu dois te demander combien de temps il faut à Waze pour repérer un bouchon. Pour ses villes partenaires, il envoie toutes ces infos dans un flux mis à jour toutes les deux minutes. »

**Pourquoi ça coince :** la phrase d'après rattrape (« le délai de détection […] Waze ne le dit nulle part »), mais à l'oral, le spectateur retient la question et le premier chiffre qui suit : « deux minutes ». C'est exactement ce que la 2e vérif interdit (fait 6 : « ne pas dire « Waze sait en 2 minutes » »).
**Correction :** d'abord « Waze ne le dit nulle part. On a cherché. », puis le flux, présenté pour ce qu'il est : « Attention, ça, c'est le rythme auquel il livre les infos aux villes. Le temps qu'il met à voir le bouchon, lui, reste secret. » Et « J'ai cherché » devient « On a cherché » : c'est la recherche de la chaîne, pas un geste que tu as fait.

### 6. Le pont du hook dit une chose à moitié fausse

Voir le test des 30 secondes. « La réponse est dans ta poche » : non, elle est dans celle des conducteurs devant toi, et dans la tienne pour ceux qui sont derrière. La correction garde ta formule et la rend juste.

### 7. Les rafales de faits (axe 10)

**Le compte** : V1, 37 liaisons pour 1 738 mots de voix off, soit **2,1 pour 100 mots** (`controle.py`), au-dessus de la cible de 1,5 et très au-dessus des téléprompteurs précédents (0,7 à 0,9). Par section : hook 2,7 · capteur 2,4 · bouchon 1,9 · signalements 2,6 · calcul **1,5** · faux bouchon 1,7 · fin 2,8. Le compteur prend tous les « mais », même ceux de simple addition : sans aucun « mais », la V1 reste à 1,7. Les plus utilisées : « mais » (7), « donc » (5), « en fait » (4) ; aucune ne revient deux fois de suite. Le chiffre est bon ; le problème, ce sont quatre endroits où les faits s'empilent quand même :

> « Waze est né d'une carte communautaire israélienne, FreeMap Israel, lancée en deux mille six. Dès le départ, ce sont les conducteurs qui font la carte. Fin deux mille vingt-deux, ils étaient environ cent cinquante millions par mois. »

Trois faits, aucune liaison, et l'histoire de Waze, c'est le terrain de Thibaut Dcode. → coupé ; seul le chiffre reste, avec une réaction : « Et des capteurs, il en a : fin deux mille vingt-deux, Waze comptait environ cent cinquante millions d'utilisateurs par mois. Ça en fait, des téléphones qui roulent. » (« ils étaient » parlait des conducteurs ; le chiffre compte des utilisateurs, fait 21.)

> « Pour chaque tronçon de route, il garde la vitesse moyenne de chaque demi-heure de chaque jour de la semaine. Quarante-huit mesures par jour, et par tronçon. Un jour normal, il s'appuie sur les huit dernières semaines environ. »

→ « En gros, pour chaque bout de route, il garde […]. Ça fait quarante-huit mesures par jour, rien que pour ce tronçon. Et un jour normal, il s'appuie sur les huit dernières semaines environ. Donc pour ton mardi à huit heures et demie, il a à peu près les huit derniers mardis à huit heures et demie. » La dernière phrase traduit les deux chiffres pour le spectateur (une case par demi-heure et par jour, sur huit semaines).

> « Et pour noter la gravité […]. Et chaque bouchon reçoit une note […]. » puis « Et avant de faire sa moyenne […] »

Trois « Et » d'addition : le passage en « et aussi » de l'axe 8. Corrigé par « Ensuite, pour chaque bouchon, il note deux choses », puis la blague, qui sert de respiration.

> « En effet, l'itinéraire que Waze proposait aux chercheurs a changé : […]. Le faux bouchon est même resté affiché une vingtaine de minutes après l'arrêt des bots. / Et d'après l'étude, en deux mille quatorze, Waze ne faisait aucun effort visible […] »

« En effet » ne confirme ici rien que le spectateur soupçonnait : il sert de colle. → « Et derrière, Waze change l'itinéraire […]. Un détour, pour des conducteurs qui n'existent pas. Le faux bouchon est même resté affiché […]. » La réaction entre les deux chiffres casse la rafale.

**Après correction** (`script.md`) : 39 liaisons pour 1 809 mots, **2,2 pour 100** (1,8 sans aucun « mais »). La section la plus faible, le calcul, passe de 1,5 à 1,9 : un « Donc » et une réaction (« Et heureusement ») en plus.

### 8. Les tics d'IA

| Passage | Tic | Correction |
|---|---|---|
| « Mais la doc actuelle va exactement dans ce sens. » | intensif, et la doc ne décrit pas le calcul position → vitesse | « va dans le même sens » |
| « se posent exactement cette question » | intensif, et ça prête une intention aux chercheurs | « En gros, leur idée : si ce sont les téléphones qui font le bouchon, des faux téléphones devraient pouvoir en faire un aussi. » |
| « Exactement ce que dit la doc. » | intensif en fragment | « C'est ce que dit la doc. » |
| « Un million de fois par seconde, un serveur se demande : « il en est où, lui ? » » | flourish qui gonfle un chiffre (n° 4) | retiré |
| « Sans rien faire. Tu n'as touché à rien, et tu bosses déjà pour lui. » | écho en fragment de la phrase d'avant | garder la seule réaction : « Tu n'as touché à rien, et tu bosses déjà pour lui. » |
| « Et cette fois, sur la carte, un bouchon apparaît. À huit kilomètres-heure. Il a suffi de quinze bots. / Un bouchon de PNJ. » | cascade de fragments | gardée : c'est la seule du script, et elle tombe sur le sommet |
| « Chez Waze, le bouchon, ce sont les téléphones qui le font. Même quand ces téléphones sont faux. » | petite morale de fin de section | gardée (c'est la thèse, dite une fois), mais suivie tout de suite du pont vers le calcul pour qu'elle ne ferme pas la vidéo |
| « Bref, si je reprends depuis le début : […] » | récap annoncé = signal de sortie | « Bref, » seul, une phrase |
| « Sur Technovore, j'ouvre comme ça les applis que tu as dans la poche, une par une. » | doublon presque mot pour mot de l'appel de 3:25 | retiré ; reste « Quelle appli je décortique ensuite ? Dis-le en commentaire, et abonne-toi pour la voir. » |

Pas de fausse opposition grave : « ça décrit ce que le système peut faire, pas forcément ce que Waze fait aujourd'hui » est une vraie réserve, nécessaire (fait 14), garde-la. Aucun « Le pire ? ». La question « Cent mètres en dix secondes ? » suivie de sa réponse frôle le faux suspens : elle devient « Genre, cent mètres en dix secondes : tu roules à trente-six kilomètres-heure. »

### 9. Le narrateur

> « Je suis dev, et quand une appli me fait un coup pareil, j'ai besoin de savoir comment elle a fait. »

« Quand une appli me fait un coup pareil » laisse entendre que Waze t'a fait le coup du virage à droite. Tu ne l'as dit nulle part (le crochet de ton vécu est juste en dessous). → « Moi, je suis dev. Alors j'ai voulu voir la machine de l'intérieur, avec ce que Waze publie lui-même. » Si tu as une vraie raison, elle remplace la phrase (question 2).

### 10. Les blagues (signalées par le rédacteur)

- **Monster Hunter** (« Zéro étoile, tu passes. Cinq étoiles, prépare tes potions ») : l'image ne colle pas. Les quêtes de Monster Hunter commencent à une étoile et montent au-delà de cinq selon les jeux ; un joueur le dira en commentaire. Le **niveau de recherche de GTA 5** va pile de zéro à cinq étoiles (fait 40) et parle de route et de police : « C'est le niveau de recherche de GTA cinq. Zéro étoile, tu roules tranquille. Cinq étoiles, t'as tout Los Santos aux fesses. » Mis dans `script.md`, à valider (question 3).
- **Vin Diesel** : garde. C'est le rappel de ton gag Fast and Furious d'Uber. `script.md` le fait revenir une fois, dans l'heure d'arrivée prudente (« c'est peut-être pas toi le Vin Diesel ») : un running gag, à toi de dire si c'est trop.
- **« Un bouchon de PNJ »** : garde. Les bots sont littéralement des personnages non joueurs, et la phrase tombe sur le sommet.
- **« Le Karim, c'est toi »** : garde. Il était un peu en l'air en V1 ; l'article de Petreanu le tient désormais : « The people behind me might get a route that goes around the traffic » (fait 37). Ajouté juste avant : « Les gens derrière lui, dit-il, auront peut-être un itinéraire qui contourne le bouchon. »

## La rétention

- **Hook** : question centrale à 0:14, teaser à 0:22, budget de 30 s tenu. 🟢
- **0:30-1:00** : la V1 passe 20 s sur les sources (« j'ai lu ce que Waze publie lui-même ») juste après le hook, au moment où ArtCraft perdait le plus. Ça reste dans `script.md`, plus court, avec un défilement rapide à l'écran, parce que la crédibilité sert le spectateur ; le rappel d'Uber arrive à 0:45.
- **Relances** : 24 en V1, 32 dans `script.md`, une toutes les 25 s environ ; le plus long trou est 0:45-1:25 (40 s), tenu par l'animation de Karim qui se multiplie.
- **Ponts entre sections** : bons en V1 (« Sauf qu'une vitesse, toute seule… », « les gens qui appuient sur « signaler », ils servent à quoi ? »), sauf la fin de la section 3 (mauvaise promesse) et l'entrée du faux bouchon (« Bon. Si je reprends »), remplacée par la question du nombre de téléphones.
- **Appel à l'abonnement** : V1 à 3:25 (28 %), `script.md` à 3:00 (**24 %**), au même endroit, juste après la première révélation. 🟢
- **Relance forte** : V1 à 8:45 (**73 %**), `script.md` à 7:17 (**58 %**), voir n° 1.
- **Durée** : V1 1 738 mots (12:00 à 145 mots/min) ; `script.md` 1 809 mots (12:28 à 145, 10:03 à 180). Le serveur de sessions sorti (−70 mots) a laissé la place aux récoltes, au pont du nombre de téléphones et à la chronologie juste de l'étude.

## Ce que le rédacteur a signalé

| Signalement | Décision |
|---|---|
| La relance forte tombe à 73 % ; sortir le serveur de sessions (~25 s) | Sortir le serveur ne suffit pas (72 %). Faux bouchon déplacé avant le calcul : 58 %. Le serveur part quand même en réserve, corrigé. |
| Blagues à valider : Monster Hunter, Vin Diesel, « bouchon de PNJ », « le Karim, c'est toi » | Monster Hunter → GTA 5 (à valider) ; les trois autres gardés, le Karim désormais sourcé. Questions 3 et 4 de `script.md`. |
| « Tu râles… » ou ouverture directe sur la route rouge | « Tu râles » gardé et raccourci : il crée le contraste et plante l'« habitude », récoltée en section 2. |

## Vérification des faits du script

Chaque phrase de la V1 qui affirme quelque chose, contre `sources.md` (colonne « 2e vérif ») ou, à défaut, la source primaire relue aujourd'hui.

| Phrase de la V1 | Fait | Verdict | Dans `script.md` |
|---|---|---|---|
| « tout le monde est à l'arrêt. Et personne ne l'avait signalé » (sans accident ni délai) | 19, 29, 31 | ✅ formulation de la 2e vérif | gardé |
| « la réponse est dans ta poche : ton téléphone fait partie de la machine » | 1, 9, 35 | ⚠️ c'est le téléphone des conducteurs devant toi qui a vu le bouchon | « dans la poche des conducteurs devant toi. Et dans la tienne. » |
| « des chercheurs s'en sont servis pour fabriquer un bouchon qui n'existait pas. Waze l'a affiché. » | 15 | ✅ sur le fond, ❓ « s'en sont servis » flou | « des chercheurs ont inventé des conducteurs qui n'existaient pas. Et Waze a affiché leur bouchon. » |
| « quand une appli me fait un coup pareil » | aucun | ❌ vécu non donné par l'auteur | retiré |
| « la doc qu'il donne aux villes partenaires, un article d'un de ses ingénieurs, et même son brevet » | 1, 3, 7, 14 | ✅ | gardé |
| Karim envoyait sa position pour que tu le voies arriver | vidéo Uber | ✅ (notre script Uber) | gardé |
| « ses infos de bouchon sont fabriquées à partir des points GPS envoyés par les téléphones » | 1 | ✅ | gardé |
| « quand tu gardes l'appli ouverte, tu lui donnes, sans rien faire, la vitesse » | 9 | ✅ | gardé |
| Brevet déposé en 2008 ; position à intervalles réguliers avec l'heure ; vitesse par la différence de position ; moyenne des membres | 14 | ✅ ; « un brevet décrit ce que le système peut faire » dit | gardé |
| « Cent mètres en dix secondes : trente-six kilomètres-heure » | calcul | ✅ (10 m/s = 36 km/h), exemple | « exemple » à l'écran |
| « la doc actuelle va exactement dans ce sens » | 1, 3 | ⚠️ la doc parle de points GPS et de vitesse, pas du calcul lui-même | « va dans le même sens » |
| FreeMap Israel, 2006 ; « ce sont les conducteurs qui font la carte » | 22 ⚠️ | ⚠️ Wikipédia seule ; « par les conducteurs » n'est pas dans la formulation de la 2e vérif | coupé |
| « Fin deux mille vingt-deux, ils étaient environ cent cinquante millions par mois » | 21 ⚠️ | ⚠️ ce sont des utilisateurs, pas des conducteurs | « Waze comptait environ cent cinquante millions d'utilisateurs par mois » |
| « un bouchon, c'est une comparaison : on roule nettement moins vite que d'habitude » | 3, 16 | ✅ | gardé |
| 48 mesures par jour et par tronçon ; huit dernières semaines environ | 7, 8 | ✅ | gardé, plus la traduction « à peu près les huit derniers mardis » (déduction des deux faits, dite avec « à peu près ») |
| « Quand un tronçon roule sous sa vitesse moyenne habituelle […] Puis il recoupe avec les signaux GPS et les signalements » | 3 | ✅ | gardé |
| « pour noter la gravité, il garde une deuxième référence : la vitesse fluide » | 2 ⚠️, 5 | ⚠️ le lien gravité / vitesse fluide n'est pas dans la doc | « il note deux choses. Un niveau […]. Et le retard en secondes, par rapport à la vitesse fluide » |
| Niveau de 0 (fluide) à 5 (bloqué), retard en secondes | 5 | ✅ | gardé |
| Monster Hunter, zéro à cinq étoiles | culture pop | ❌ les quêtes commencent à une étoile | GTA 5, zéro à cinq étoiles (fait 40, ajouté) |
| Les extrêmes écartés ; moto et bus | 11 | ✅ | gardé |
| « signaler un accident, la police ou un objet sur la route » | absent | ⚠️ vérifié dans l'aide Waze : « Trafic », « Police », « Accident », « Dangers » ; « objet » n'est pas un nom du menu | « un danger » (fait 39, ajouté) |
| « tes signalements s'affichent comme des alertes, et ils pèsent aussi sur la façon dont Waze repère les bouchons » | 4 ⚠️ | ✅ formulation de la 2e vérif | gardé |
| « le bouchon sort d'abord des vitesses. Les signalements viennent ensuite le confirmer et le préciser » | 18 ⚠️ | ✅ formulation de la 2e vérif | gardé |
| « Waze savait que ça bloquait. Par contre, il ne savait pas pourquoi » | 19, 31 | ✅ | gardé |
| Petreanu, « ingénieur chez Waze », « au début », la voiture « cinq secondes plus tard » | 32 ⚠️ | ✅ relu au grill : « In my early days at Waze » | « à ses débuts dans la boîte », plus la confiance (fait 36, ajouté) |
| « Quelqu'un, un peu plus loin devant, avait pris le temps d'appuyer sur un bouton » | 32 | ✅ (le signalement venait d'un autre conducteur, passé avant lui) | gardé |
| Flux partenaires mis à jour toutes les deux minutes | 6 | ✅ mais placé juste après la question du délai | déplacé après « Waze ne le dit nulle part », avec la réserve |
| « le délai de détection, ou le nombre de téléphones […] Waze ne le dit nulle part. J'ai cherché. » | 28 | ✅ ; « J'ai cherché » prête un geste à l'auteur | « On a cherché. » |
| Le mélange temps réel / historique, l'équation non publiée | 10 | ✅ | gardé |
| « il penche volontairement du côté prudent » | 13 | ✅ | gardé |
| « quand tu arrives deux minutes avant l'heure annoncée, c'est voulu » | 13 | ⚠️ généralise un biais à chaque trajet | « si tu arrives souvent un peu avant […] Waze prévoit large exprès » |
| « toutes les quelques minutes » ; « pour une minute de retard, aucun intérêt » ; trajets stables | 12 | ✅ | gardé |
| « parce qu'un GPS qui change d'avis tous les cent mètres, tu le désinstalles » (prêté à Waze) | aucun | ⚠️ c'est ton avis | dit comme ton avis (« Et heureusement, parce que… ») |
| « Les téléphones devant toi ont ralenti » | 1, 3, 35 | ✅ | renforcé (« Toi, tu voyais encore une route dégagée ») |
| Serveur de sessions, un million de lectures par seconde en test de charge, moins d'une milliseconde | 20 ⚠️ | ✅ avec « test de charge » | en réserve |
| « Un million de fois par seconde, un serveur se demande : « il en est où, lui ? » » | 20 | ❌ un test de charge présenté comme le trafic réel | retiré |
| Quatre chercheurs du Technion, Haïfa, 2014 | 15 | ✅ | gardé |
| « des faux téléphones, qui envoient à Waze des positions GPS truquées » | 15 | ✅ ; précisé au grill : émulateurs Android avec le vrai client Waze | « des téléphones Android simulés, avec la vraie appli Waze dedans » (fait 38, ajouté) |
| « se posent exactement cette question » | 15 | ⚠️ prête une intention | « En gros, leur idée : […] » |
| « Premier essai : […] immobiles. […] Waze voyait sans doute des gens qui venaient d'ouvrir l'appli » | 16, 38 | ✅ relu : « Our initial attempts » | gardé |
| « Ils essaient aussi de les faire ralentir dans une zone déjà lente. Toujours rien. » | 16, 38 | ⚠️ ordre approximatif : ils ont fait ralentir les bots (15, 8, 2 km/h), échec, puis compris que le campus est une zone lente | « Deuxième essai : ils les font ralentir petit à petit. Toujours rien. Et là, ils comprennent : sur le campus, tout le monde roule doucement. » |
| « le calcul de Waze est relatif […] Exactement ce que dit la doc. » | 3, 16 | ✅ déduction des chercheurs, dite comme telle | « C'est ce que dit la doc. » |
| Départ à 70 km/h puis ralentissement ; bouchon à 8 km/h ; quinze bots | 15, 16, 34 | ✅ | gardé, plus « Quinze, c'est ce qui a suffi sur leur campus ; Waze, lui, n'a jamais donné de seuil » (fait 28) |
| 1,5 km et 3 min avant, 1,6 km et 4 min après ; une vingtaine de minutes | 15, 34 | ✅ | gardé |
| « Waze ne faisait aucun effort visible pour distinguer un humain d'une machine » (2014) | 17 | ✅ daté | gardé |
| « ils écrivent qu'ils pourraient, en théorie, envoyer d'autres conducteurs ailleurs » ; plus de dix ans | 15 | ✅ (« potentially » ; 2014 → 2026) | gardé |
| « J'attends ici, mais j'aide ceux qui vont prendre Waze après moi », « la phrase que se répète l'ingénieur » | 33 ⚠️ | ✅ relu au grill : « I have a mantra for myself when I run into traffic » | gardé, plus « Les gens derrière lui, dit-il, auront peut-être un itinéraire qui contourne le bouchon » (fait 37, ajouté) |
| « c'est lui qui fait tourner à droite quelqu'un derrière toi » | 37 | ⚠️ Petreanu dit « might » | « c'est peut-être lui qui fait tourner à droite quelqu'un, derrière toi » |
| Uber : « des voitures qui n'existaient peut-être pas » | vidéo Uber | ✅ (notre script Uber, voitures fantômes) | gardé |

**Retiré** : « quand une appli me fait un coup pareil », FreeMap Israel et « ce sont les conducteurs qui font la carte », Monster Hunter de zéro à cinq étoiles, « un million de fois par seconde, un serveur se demande », « c'est voulu » (pour chaque avance), la vitesse fluide qui « note la gravité », « J'ai cherché », « exactement » (×3), « un objet sur la route ».
**Ajouté à `sources.md`** (lignes 36 à 40, « ajouté au grill, vérifié le 23/10/2026 ») : 36, les débuts de Petreanu et la confiance ; 37, la suite de son mantra (« the people behind me might get a route that goes around the traffic ») ; 38, les émulateurs Android et l'ordre des essais de 2014 ; 39, les noms du menu de signalement ; 40, les cinq étoiles de GTA 5.
**Reste non publié, et le script le dit** : le délai de détection, le nombre de téléphones, la formule du mélange temps réel / historique.

## Ce qu'il faut garder

- « Chez Waze, c'est le même principe, sauf que tout le monde fait le Karim. » Le pont avec Uber en une phrase, et la graine de la fin.
- « Tu n'as touché à rien, et tu bosses déjà pour lui. » La réaction qui transforme un fait de doc en enjeu pour le spectateur.
- La devinette des 20 km/h et « Bah ça dépend où. » : le spectateur trouve la règle avant qu'on la lui dise.
- « Tant que personne ne le signale, pour lui, ce sont juste des téléphones qui n'avancent plus. » Elle referme le hook sans tricher sur l'accident.
- « Quelqu'un, un peu plus loin devant, avait pris le temps d'appuyer sur un bouton pour un inconnu. » Le problème profond, dit par une scène.
- « Waze ne le dit nulle part. » Dire ce qu'on ne sait pas rend crédible tout le reste.
- Les deux essais ratés des chercheurs : une vraie escalade, qui prouve la section 2 au lieu de la répéter.
- « Un bouchon de PNJ. » et « Tout ça pour une flèche bleue qui tourne à droite. »
- « Attention à ce qu'on en fait, quand même. » : la réserve sur l'étude de 2014, dite franchement.

## Plan d'action (appliqué dans `script.md`)

1. Déplacer le faux bouchon avant le calcul, avec le pont « combien de téléphones ? » à l'entrée et « Comme ton virage à droite » à la sortie (n° 1).
2. Corriger les phrases qui dépassent leur source (n° 4, n° 5, tableau des faits) et sortir le serveur de sessions en réserve.
3. Réécrire le pont du hook (n° 6) et payer le titre en clair (n° 2).
4. Récolter « d'habitude » et la confiance de Petreanu, et sourcer « le Karim, c'est toi » (n° 3, n° 10).
5. Casser les quatre rafales et retirer les tics (n° 7, n° 8), puis contrôle : 1 809 mots, 2,2 liaisons pour 100 mots, question centrale au 35e mot, 0 « vous ».

## Les questions pour toi

Elles sont dans `script.md`, section « Questions pour l'auteur » : ton vécu avec Waze, ta raison de t'y intéresser, GTA ou Monster Hunter (et Vin Diesel deux fois), « le Karim, c'est toi », ton enjeu de dev.
