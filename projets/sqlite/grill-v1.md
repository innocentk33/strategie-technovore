# Grill du script SQLite v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Grille : `youtube-script-grill`, mode B (APRÈS), **variante storytelling** (test des 30 secondes, axe 10, axes S1 à S6).
> Hypothèses : titre provisoire *SQLite : la base de données qui est partout, et qui n'a pas de serveur* ; miniature pas encore faite (la fiche dit « à faire ») ; public de 18-30 ans curieux de tech, 63 % en Afrique, une bonne part de devs ; objectif : une vidéo du pilier « génie derrière l'app » qui vit des suggestions (la recherche « comment fonctionne sqlite » est sous les 750 par mois).
> Faits revérifiés à la source le 23/10 : voir « La vérification des faits » en bas. Six lignes ajoutées à [`sources.md`](sources.md) (faits 35 à 40).
> Version corrigée : [`script.md`](script.md).

## Verdict

Le V1 est propre, bien rythmé et très bien sourcé sur les gros pièges : le « 300 Ko » n'apparaît que comme légende corrigée, « certifié DO-178B » est évité, « deux ingénieurs » et MySQL sont tenus à l'écart. Le fil du téléphone tient du hook à la fin, et les plantés-récoltés marchent (la partie en ligne qui devient la carte mémoire, le téléphone éteint qui revient dans les tests).

Le plus gros problème est dans la section 5, le cœur émotionnel de la vidéo : elle s'ouvre sur « À un moment, des bugs remontent depuis Android », sans date ni scène, puis raconte l'aviation comme un chapitre d'après, alors que c'est le même chantier. Or la vraie histoire est bien meilleure, et elle est sourcée : Hipp se vantait « naïvement » de n'avoir aucun bug, Android lui a « clairement donné tort », et il a passé dix mois (un an d'après lui) à tout tester selon une norme d'avion, du 25/09/2008 au 25/07/2009. C'est la crise qui manque au script. Deuxième problème, bloquant pour la règle des faits : une anecdote inventée (« SQLite, je l'ai rangé dans mes propres applis »).

Le reste se règle en une passe : deux surclassements (« le plus installé »), Skype qui n'existe plus, trois liaisons à contresens, un contraste du hook qui ne parle qu'aux devs, et l'abonnement trop tard.

**Note globale : 🟠, 6,5/10.** Sur les 11 axes : 5 🟢, 6 🟠, 0 🔴 ; variante storytelling : 1 🟢, 5 🟠 ; faits : 🔴 tant que l'anecdote inventée reste. Après correction (`script.md`), j'estime le script à 8/10 : il lui manque surtout tes deux crochets (ton vécu, ton avis de dev).

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | « Partout » est tenu dès 0:05 et prouvé en section 1 ; « pas de serveur » est expliqué en section 3. |
| 2. Alignement | 🟢 | Pas de vente forcée ; deux appels à l'abonnement courts. |
| 3. Problème profond | 🟠 | Le sous-texte (la fiabilité, tenir sa promesse) passe par les tests, mais sans faute ni humilité : Hipp ne se trompe jamais. |
| 4. Public & complexité | 🟢 | Le dictionnaire, la carte mémoire, le brouillon du WAL : chaque notion arrive avec son image. |
| 5. Valeur & originalité | 🟠 | Les corrections (300 Ko, certification) sont une vraie valeur, mais l'ordre des chapitres est exactement celui de ByteMonk. |
| 6. Structure & transformation | 🟢 | Départ : « je ne connais pas ce nom ». Arrivée : « je sais qui remercier quand mon téléphone se rallume ». |
| 7. Histoire | 🟠 | Un vrai désir en section 2 (une appli qui marche même quand le serveur tombe) ; aucune crise ensuite. |
| 8. Mais / donc | 🟠 | Bon dans les sections 2 et 4 ; des « et aussi » en sections 3 et 6. |
| 9. Engagement actif | 🟠 | Le spectateur ne devine jamais rien. |
| 10. Rythme, oralité & liaisons | 🟢 | 2,5 liaisons pour 100 mots, mais 3 à contresens, et 25 phrases sur 130 commencent par « Et ». |
| 11. Tics d'IA | 🟠 | Une dizaine, légers ; deux plus graves : une phrase empruntée à Cam et un avis prêté. |
| S1. Les 30 premières secondes | 🟠 | Le chiffre est là et la question tombe à 0:28, mais le contraste « n'a même pas de serveur » ne dit rien à un non-dev. |
| S2. Le pont | 🟠 | Bon départ (le bateau de guerre), aussitôt garé : « On y vient. D'abord, je veux te montrer où il se cache. » |
| S3. Les retournements | 🟠 | La section 1 tient 1 min 30 sans retournement (une liste) ; la section 6 aussi, ou presque. |
| S4. Planté / récolté et motif | 🟢 | La partie en ligne → la carte mémoire ; le téléphone éteint → les tests ; le téléphone en motif du début à la fin. |
| S5. Personnages et enjeu | 🟠 | Hipp veut quelque chose en section 2, puis devient une machine à tests en section 5. |
| S6. La fin | 🟠 | « Bref, si je reprends » résume, puis la chute « tu sauras qui remercier » retourne bien. |
| Faits (règle du dépôt) | 🔴 | Une anecdote inventée, deux surclassements, une chronologie sans source, Skype. Tout le reste tient. |

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** (titre + hook) : « ce logiciel est dans ton téléphone et à peu près partout, et il n'a pas de serveur ; voilà comment il en est arrivé là ». Le V1 la tient, mais « pas de serveur » est une promesse de dev : pour la majorité de ton public, c'est le téléphone et le « comment un truc pareil ? » qui font cliquer.
- **Texte** : SQLite, une bibliothèque et un fichier, sans serveur, probablement plus déployée que tous les autres moteurs réunis.
- **Sous-texte** (fiche, à valider par toi) : celui qui gagne, c'est celui qui a supprimé le problème et qui tient sa promesse de fiabilité. Le V1 le porte à moitié : la suppression du problème est là (le serveur du destroyer), la promesse de fiabilité arrive sans prix à payer. La vantardise de Hipp et la claque d'Android donnent ce prix : on ne devient fiable qu'après avoir eu tort. C'est le problème profond qui manquait, et il vient des sources, pas d'une invention.
- **La chaîne du V1** :
  - un serveur tombe, **donc** un collègue dit « écris le tien », **et** les contrats sont gelés, **donc** il le fait (🟢) ;
  - **mais** sans serveur, comment ça marche ? **Donc** une bibliothèque, un fichier (🟢) ;
  - **et** ça pèse moins d'un Mo, **et** ça monte à 281 To, **et** c'est 35 % plus rapide (🟠 : trois « et aussi ») ;
  - **mais** qu'est-ce qu'il y a dedans ? Pages, arbre, WAL, **sauf que** le disque peut s'arrêter (🟢) ;
  - « À un moment », des bugs, **donc** des tests ; **et** l'aviation ; **et** l'Airbus (🟠 : l'aviation arrive après coup) ;
  - **et** le domaine public, **et** la licence, **du coup** la Bibliothèque du Congrès, **et** 2050 (🟠).
- **La chaîne corrigée de la section 5** : Hipp se vante de n'avoir aucun bug, **mais** Android plante sans arrêt, **donc** il applique une norme d'avion qu'il vient de découvrir, **et en effet** dix mois plus tard, plus aucun rapport d'Android ; **du coup** aujourd'hui, 590 lignes de tests par ligne de code, **donc** le même logiciel vole dans l'A350.

## Le test des 15 premières secondes

Relues seules, à ton débit (145 à 180 mots/min, 36 à 45 mots) :

> « Dans ton téléphone, là, maintenant, il y a probablement des centaines de petites bases de données. Et toutes viennent du même logiciel : SQLite. Du coup, avec plus de quatre milliards de smartphones sur Terre, sqlite.org estime qu'il y a probablement plus de mille milliards… »

**Verdict : 🟢, avec un manque.** Sans contexte, sans présentation, raccord avec le titre et l'image (le téléphone qui se remplit). Le chiffre le plus fou de la vidéo arrive vers 0:14 à 180 mots/min, 0:17 à 145 : c'est limite, mais c'est le bon moment. Le manque : l'image la plus forte de la vidéo, l'A350, n'est pas plantée. « Le même logiciel est dans ton téléphone et dans le logiciel de vol d'un Airbus » est le contraste qui fait dire « attends, quoi ? » à un non-dev. Le `script.md` le monte à 0:20 (et à l'image dès le dézoom), puis le récolte en section 5.

Les autres candidats ne battent pas le téléphone : le destroyer demande du contexte, et les 92 millions de lignes de tests ne parlent qu'une fois qu'on sait ce qu'est un test.

## Test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Dans ton téléphone, là, maintenant, il y a probablement des centaines de petites bases de données. » | 🟢 Le sujet, le spectateur dedans, et une tension (« des centaines ? dans mon téléphone ? »). Sourcé (fait 32, avec « probablement »). |
| 5-15 s | > « Du coup, avec plus de quatre milliards de smartphones sur Terre, sqlite.org estime qu'il y a probablement plus de mille milliards de bases SQLite en service. » | 🟢 Le chiffre fou, sa preuve à l'écran (« estimation de sqlite.org »), et une liaison qui dit d'où il vient. |
| 15-30 s | > « Sauf que ce logiciel n'a même pas de serveur. Alors comment un truc pareil s'est retrouvé à peu près partout ? » | 🟠 La question centrale est posée, une seule, au 70e mot (≈ 0:28). Mais le contraste ne marche que pour un dev : pour les autres, « pas de serveur » sonne comme un détail, pas comme un handicap. Le « sauf que » n'oppose rien qu'ils perçoivent. |
| Pont | > « En fait, tout commence sur un bateau de guerre, avec un serveur qui tombe en panne. On y vient. D'abord, je veux te montrer où il se cache. » | 🟠 La première phrase est un vrai pont (départ inattendu). Les deux suivantes l'annulent : « On y vient. D'abord… » annonce un plan et gare la boucle derrière une liste de marques. |

**Budget :** 70 mots ≈ 29 s à 145 mots/min, 23 s à 180. Dans la cible.
**À couper :** « On y vient. D'abord, je veux te montrer où il se cache. » ; « sur Terre » (ne fait rien).
**Le contraste à mettre** : l'échelle (mille milliards, un Airbus) contre l'origine (un développeur sans contrat, un serveur qui plantait). Les deux sont sourcés (faits 1, 11, 14, 15).

**Réécriture des 30 s** (celle du `script.md`, 88 mots, question centrale au 88e mot, ≈ 0:29 à 180 mots/min, 0:36 à 145) :

> Dans ton téléphone, là, il y a probablement des centaines de petites bases de données. Et toutes, c'est SQLite.
>
> Du coup, avec plus de quatre milliards de smartphones, sqlite.org estime qu'il y a probablement plus de mille milliards de bases SQLite en service. Et il tourne même dans le logiciel de vol de l'A trois cent cinquante.
>
> Sauf qu'au départ, c'est juste un développeur sans contrat et un serveur qui plantait, pour un destroyer. Alors comment un truc né comme ça s'est retrouvé à peu près partout ?
>
> *(pont)* En fait, ce serveur en panne, c'est la clé de toute l'histoire. Mais avant, regarde à quel point SQLite s'est bien caché.

Les 6 questions : première phrase 🟢 ; le meilleur moment avant 15 s 🟢 (le chiffre, l'Airbus juste après) ; la question centrale 🟢 (0:29 à 180, 0:36 à 145 : à ton débit réel, plutôt la première) ; le pont 🟢 (« la clé de toute l'histoire » ouvre une deuxième question) ; chaque phrase compte 🟢 ; le budget 🟠 : 88 mots, c'est le haut de la fourchette (75 à 90). Si la prise déborde, coupe « là, » et « à peu près ».

## L'axe 10 : les liaisons

**Le compte** (`controle.py`, liste du skill) : **1 677 mots, 2,5 liaisons pour 100 mots** (≈ 42). Par section : hook 2 pour 70 mots, section 1 : 4 pour 225 (1,8), section 2 : 7 pour 267, section 3 : 8 pour 238, section 4 : 7 pour 259, section 5 : 7 pour 291, section 6 : 3 pour 168 (1,8), fin : 4 pour 159. C'est bien au-dessus de tes téléprompteurs (0,7 à 0,9) et dans la fourchette de Cam et V2F.

**Mais trois liaisons mentent sur la logique**, et une liaison qui ne relie rien s'entend autant qu'une absence de liaison :

> « Et WhatsApp, alors ? […] Résultat, sqlite.org pense que SQLite est probablement utilisé plus que tous les autres moteurs de bases de données réunis. »

WhatsApp n'est pas la cause de l'estimation de sqlite.org. Correction : « Voilà pourquoi sqlite.org pense… » (le « voilà pourquoi » renvoie à toute la liste, qui est bien le raisonnement de sqlite.org).

> « Et pour les entreprises qui veulent un papier en règle, Hwaci […] vend aussi des garanties juridiques. Du coup, même la Bibliothèque du Congrès américain range les fichiers SQLite parmi ses formats préférés »

La Bibliothèque du Congrès ne recommande pas SQLite à cause des garanties de Hwaci. Correction : couper Hwaci (fait 17 ⚠️, peu utile), puis « Même la Bibliothèque du Congrès… ».

> « À un moment, des bugs remontent depuis Android. Donc Hipp se lance dans un chantier énorme »

Le « donc » tient, mais il repose sur un « à un moment » sans source. Voir la vérification des faits.

**Les rafales de faits sans liaison** :

> « Si tu ouvres un fichier SQLite, les cent premiers octets, c'est une carte d'identité. Et dedans, il y a écrit en clair : « SQLite format 3 ». Ensuite, le fichier est découpé en pages, toutes de la même taille. Par défaut, quatre mille quatre-vingt-seize octets. »

Quatre faits empilés. Ça passe parce que l'image (la boîte qui s'ouvre) porte le rythme, et le dictionnaire arrive juste après ; je l'ai gardé presque tel quel.

> « Et la bibliothèque entière pèse moins d'un mégaoctet. […] Et un seul fichier, ça tient beaucoup. La taille maximale d'une base SQLite, c'est deux cent quatre-vingt-un téraoctets. […] Et en fait, pour lire et écrire plein de petits morceaux de données, SQLite peut aller plus vite… »

Trois faits reliés par « et », sans raison d'arriver l'un après l'autre (voir le grill n° 6).

**Le tic de la liaison** : 25 phrases sur 130 commencent par « Et ». Ce n'est pas faux à l'oral, mais à ce taux, « Et » devient le nouveau « Du coup ». Le `script.md` en retire une douzaine.

## Le grill

### 1. La section 5 raconte la mauvaise histoire, et la vraie est meilleure

> « À un moment, des bugs remontent depuis Android. Donc Hipp se lance dans un chantier énorme : tester chaque branche du code. »
> « Mais l'histoire ne s'arrête pas aux téléphones. Des constructeurs d'avionique s'intéressent à SQLite. Du coup, les développeurs construisent une deuxième suite de tests, TH3, pensée pour les normes de l'aviation. »

**Pourquoi ça coince :**
- « À un moment » n'est pas sourcé (question 3 du V1). Je l'ai cherché : CoRecursive ne date pas les plantages, mais sqlite.org date le chantier (fait 35) : la première ligne de TH3 le **25 septembre 2008**, 100 % MC/DC le **25 juillet 2009**, après « un effort intense » de dix mois. C'est l'année de soixante heures par semaine dont parle Hipp.
- L'aviation n'est pas une suite : c'est la méthode du même chantier. Hipp raconte qu'il travaillait pour Rockwell Collins, un constructeur d'avionique, « à peu près au même moment, ou un peu avant » ; c'est là qu'il découvre DO-178B, qui exige 100 % MC/DC (fait 36). Et sqlite.org dit que TH3 a été conçue pour cette norme (fait 10). Le V1 fait de TH3 une « deuxième suite » construite après coup : c'est faux.
- Et surtout, le V1 passe à côté de la crise. Hipp le dit lui-même : ils disaient à tout le monde, « naïvement », que SQLite n'avait pas de bugs ; puis SQLite s'est retrouvé « sur des millions d'appareils », ça plantait « sans arrêt », et « Android nous a clairement donné tort » (fait 36). C'est le moment bas du voyage du héros, celui qui manquait aux axes 3, 7 et S5, et il est sourcé.

**Correction** (début de la section 5, dans le `script.md`) :
> Hipp le raconte lui-même sur CoRecursive : à l'époque, ils allaient dire à tout le monde, je cite, « naïvement », que SQLite n'avait pas de bugs.
>
> Et là, d'un coup, SQLite se retrouve sur des millions de téléphones Android. Ça plante sans arrêt. Sa phrase, c'est : « Android nous a clairement donné tort. »
>
> Du coup, il ressort un truc qu'il venait de découvrir en bossant pour Rockwell Collins, un constructeur d'avionique : une norme de l'aviation, la DO-178B. […]
>
> D'après sqlite.org, des constructeurs d'avionique s'intéressaient justement à SQLite, et c'est pour suivre cette norme qu'ils montent une nouvelle suite de tests, TH3. La première ligne est écrite le vingt-cinq septembre deux mille huit.

Le teaser de la relance change avec : « Et tout commence le jour où Android lui donne tort. » Le titre de la section aussi : « Android lui donne tort ».

### 2. Une anecdote inventée

> « Moi, je suis dev, et SQLite, je l'ai rangé dans mes propres applis. [TON VÉCU : …] »

**Pourquoi ça coince :** rien, ni dans la fiche ni dans `sources.md`, ne dit que tu as utilisé SQLite (la fiche le marque même « [à demander à l'auteur] »). C'est le même piège que le « j'ai résilié Netflix » d'ArtCraft : une phrase au « je » que tu n'as pas dite. Le crochet qui suit ne corrige rien, puisque la phrase qui le précède affirme déjà le fait.
**Correction :** tout passer dans le crochet : « [TON VÉCU, SI TU EN AS UN : TU AS DÉJÀ UTILISÉ SQLITE DANS TES APPLIS ? … SINON, ON PASSE DIRECTEMENT À WHATSAPP.] ». La maquette Flutter ne s'affiche que si tu le remplis.

### 3. Le contraste du hook ne parle qu'aux devs

> « Sauf que ce logiciel n'a même pas de serveur. Alors comment un truc pareil s'est retrouvé à peu près partout ? »

**Pourquoi ça coince :** voir le test des 30 secondes. Pour un étudiant qui ne code pas, « pas de serveur » n'est ni un défaut ni un exploit. La question centrale est bonne, c'est son tremplin qui est faible.
**Correction :** l'échelle contre l'origine (réécriture ci-dessus) : mille milliards et un Airbus, contre « un développeur sans contrat et un serveur qui plantait ». Le « pas de serveur » reste la réponse de la section 3, où il devient une récolte : « Voilà comment Hipp a réglé son problème : le serveur qui tombait, il n'existe plus. »

### 4. Deux surclassements

> « Le truc le plus installé de ta vie, et tu n'as jamais vu son nom. »
> « un type s'ennuyait, et il a écrit le logiciel le plus installé de ta poche. »

**Pourquoi ça coince :** dix secondes plus tôt, le script dit lui-même que sqlite.org le classe **deuxième**, après libz (fait 3). Un dev le relèvera en commentaire. Et « s'ennuyait » prête à Hipp une émotion qu'il ne raconte pas : il dit qu'il était « sans travail pendant quelques mois » (fait 15).
**Correction :** « Un des logiciels les plus installés de ta vie, et tu n'avais sans doute jamais vu son nom. » ; « Un gouvernement met ses contrats en pause, un développeur se retrouve sans boulot, et il écrit le moteur qui finira dans mille milliards de bases. » Même chose dans la fin : « un type au chômage technique » devient le récit du bilan (le chômage technique est un statut de salarié ; Hipp était sous-traitant sans contrat).

### 5. L'abonnement arrive à 31 %, hors de toute boucle

> **Abonnement (≈ 3:35, ~30 % de la vidéo…)** « Si tu aimes découvrir ce qui se cache derrière les applis que tu as dans la poche, abonne-toi… »

**Pourquoi ça coince :** mesuré sur le texte, l'appel tombe au 524e mot sur 1 677, soit 31 %, à 3:37 au débit de 145. Et il arrive juste après la chute « trois mois », quand la boucle du destroyer est fermée : c'est le moment où un spectateur peut partir.
**Correction :** le glisser **dans** la boucle, entre la question du collègue et la réponse de Hipp, à 23 % (≈ 2:43) :
> « Richard, pourquoi tu n'en écris pas une toi-même ? »
> Et avant que je te dise ce qu'il a répondu : si tu aimes voir ce qui se cache derrière les applis de ta poche, abonne-toi. Sur Technovore, je les ouvre une par une.
> Bon, Hipp lui répond : « OK, je vais essayer. »

La réponse de Hipp est vraie (« Okay, I'll give it a try », CoRecursive, fait 36), et elle arrive cinq secondes après : la promesse est tenue tout de suite.

### 6. La section 3 empile trois « et aussi »

> « Et la bibliothèque entière pèse moins d'un mégaoctet. » … « Et un seul fichier, ça tient beaucoup. La taille maximale […] deux cent quatre-vingt-un téraoctets. » … « Et en fait, pour lire et écrire plein de petits morceaux de données, SQLite peut aller plus vite… »

**Pourquoi ça coince :** juste après la meilleure animation (le serveur qui rentre dans le téléphone), trois faits arrivent sans que l'un rende l'autre nécessaire. Et « Ça reste minuscule, mais en fait, pas aussi minuscule » annule sa propre phrase.
**Correction :** donner une croyance au spectateur et la contredire, comme le permet le skill quand la croyance est réelle :
> Normalement, là, tu te dis : un simple fichier, c'est petit et c'est lent. Sauf qu'une base SQLite peut monter jusqu'à deux cent quatre-vingt-un téraoctets. J'aimerais bien voir la tête de celui qui atteint la limite.
>
> Et pour lire et écrire plein de petits morceaux de données, SQLite peut même aller plus vite que des fichiers séparés : environ trente-cinq pour cent, dans un essai de sqlite.org en deux mille dix-sept.

### 7. Le spectateur ne devine jamais

> « Et là, regarde la taille de la pile. En deux mille vingt-trois, pour cent cinquante-six mille lignes de code, il y avait quatre-vingt-douze millions de lignes de tests. »

**Pourquoi ça coince :** c'est le chiffre le plus fou de la seconde moitié, et il est livré d'un bloc. Personne ne devinera 92 millions : c'est justement ce qui rend la devinette efficace.
**Correction :**
> Du coup, petite question : à ton avis, pour cent cinquante-six mille lignes de code, il faut combien de lignes de tests ? Garde ton chiffre en tête.
>
> [VISUEL : la petite pile seule, un « ? », compte à rebours de 3 s.]
>
> En deux mille vingt-trois, il y en avait quatre-vingt-douze millions.

### 8. Les tics d'IA

| Passage | Tic | Réécriture |
|---|---|---|
| « Ouais, t'as bien entendu. » | phrase reprise mot pour mot d'un exemple du skill (Cam) : « reprends le mécanisme, jamais la phrase » | « En gros, pour chaque ligne de code, presque six cents lignes rien que pour la surveiller. Chaque ligne a ses six cents gardes du corps. » |
| « Voilà ce que je trouve fou. » | avis prêté à l'auteur (tu ne l'as pas dit) | coupé, avec la version 3.54.1 qui suivait ; la frise de 2050 porte l'émotion |
| « Et le plus étrange, c'est peut-être qu'il n'appartient à personne. » | annonce (« le plus étrange ») | « Ce logiciel, en fait, il n'appartient à personne. » |
| « Attention, je pèse mes mots : rien ne dit que SQLite est certifié pour les avions. Ce qui est sourcé, c'est une suite de tests pensée pour leurs normes. » | annonce + jargon de vérification à voix haute (« ce qui est sourcé ») | « Mais attention : ce qui suit les règles de l'aviation, ce sont ses tests. Rien ne dit que SQLite lui-même est certifié pour voler. » (la seule opposition gardée : elle corrige une idée que le spectateur vient de se faire) |
| « un engagement que presque personne ne prend » | superlatif sans source | « Les développeurs ont même pris un engagement : … » |
| « Ça reste minuscule, mais en fait, pas aussi minuscule. » | phrase qui s'annule | coupée (n° 6) |
| « Imagine la liste des endroits où SQLite tourne. » | « imagine » décoratif : il n'y a rien à imaginer, c'est une liste sourcée | « D'après sqlite.org, il est dans… » |
| « Trois mois. Pendant qu'un gouvernement…, un type s'ennuyait, et il a écrit… » | fragment + morale de fin de paragraphe | réécrit (n° 4) |
| « On y vient. D'abord, je veux te montrer… » | annonce de plan | « Mais avant, regarde à quel point SQLite s'est bien caché. » |

Rien de grave sur les fausses oppositions : aucune « ce n'est pas A, c'est B » dans le V1. Bon point.

### 9. Valeur : le squelette est celui de ByteMonk

`sources.md` résume les chapitres de ByteMonk : « 1 000 milliards de déploiements → origine sur un destroyer → pas de serveur → pages et B-arbres → journal WAL → testé comme un logiciel d'avion → deux ingénieurs ». Le V1 suit cet ordre, chapitre pour chapitre. Les règles de la chaîne disent qu'on ne copie pas l'angle d'un concurrent.

**Ce qui nous distingue déjà :** le fil du téléphone, le français, les corrections (300 Ko, certification, et Oracle si tu le gardes), la partie en ligne et la carte mémoire au lieu du restaurant. **Ce que le `script.md` ajoute :** la vantardise de Hipp et la claque d'Android racontées comme une scène, les dates de TH3, l'Airbus planté puis récolté, la devinette. Je ne pense pas qu'il faille tout réordonner : l'ordre suit la logique (d'où il vient, comment il marche, pourquoi il tient). Mais si tu veux t'éloigner davantage, la piste est d'ouvrir la section 5 plus tôt et de la couper en deux : la vantardise juste après la v1.0 (« et il en était fier »), la claque d'Android à 60 %.

### 10. Petits points

- **Skype** : sqlite.org le cite encore, mais Microsoft l'a fermé le 5 mai 2025 (fait 38). En mars 2027, le citer fait daté. Retiré.
- **« Par défaut, quatre mille quatre-vingt-seize octets »** : c'est le défaut depuis la 3.12.0, mais il dépend de la plateforme (fait 24). « En général » suffit.
- **« Dans vingt-quatre ans »** : la vidéo sort en mars 2027, ce sera vingt-trois. Et « s'ouvrira » transforme une intention (« the intent of the developers ») en certitude : « devra encore s'ouvrir ».
- **« Ça arrive sur des milliards d'appareils »** (la relance) : aucune source ne compte les coupures pendant une écriture. Retiré.
- **« Tes conversations, tes groupes, tout ça finit dans une petite base »** : les sources parlent des messages ; « tes groupes » n'y est pas. Coupé.
- **« C'est exactement ce qui tombait sur le destroyer »** : rien ne dit que le serveur était à bord. « Pour le destroyer ».
- **WhatsApp** : la source du fait 22 date de 2016. Une analyse de juillet 2026 confirme que la base des messages, une fois déchiffrée, est « un simple fichier SQLite » (fait 39). La formule « d'après des analyses forensiques » reste.
- **La fin vers WhatsApp** : « une cinquantaine d'ingénieurs… neuf cents millions » est juste, mais c'était en 2015 (`projets/whatsapp/sources.md`, fait 1). Ajouté : « en deux mille quinze ».

## Les questions de ta liste

### Le titre

| Titre | Verdict |
|---|---|
| *SQLite : la base de données qui est partout, et qui n'a pas de serveur* (fiche, titre 3) | 🟠 Juste et sourcé, avec les mots-clés « SQLite » et « base de données ». Mais 67 caractères, deux promesses, et « pas de serveur » ne parle qu'aux devs. Le mot que `sources.md` recommande, « téléphone », n'y est pas. |
| *Le logiciel le plus installé du monde n'a pas de serveur* | 🔴 Faux tel quel : sqlite.org le classe 2e, après libz (fait 3). « La base de données la plus installée du monde » serait défendable (c'est le titre de la page de sqlite.org, fait 37), mais c'est le projet qui le dit de lui-même, et la moitié « n'a pas de serveur » reste abstraite. |
| *SQLite : le fichier de moins d'1 Mo qui est dans ton téléphone* | 🟠 « Dans ton téléphone » est la bonne promesse. « Moins d'1 Mo » ne fait pas d'effet en 2027 (une photo pèse plus) et « fichier » rapetisse le sujet. |

**Je recommande : *SQLite : la base de données cachée dans ton téléphone*** (52 caractères). C'est un mélange du titre 3 et du troisième :
- il garde « SQLite », « base de données » et « téléphone », les trois mots que `sources.md` recommande ;
- il promet une découverte sur un objet que le spectateur a dans la main ;
- le hook le tient en 5 secondes, avec le téléphone qui se remplit de fichiers, et c'est la même image que la miniature à faire.

Garde le titre 3 de la fiche comme variante B pour un test A/B : une seule variable à la fois, le titre, avec la même miniature.

### Les blagues (à valider par toi)

- **La partie en ligne perdue** (section 2) : je la garde, elle sert. Elle prépare la carte mémoire de la section 3 et fait comprendre le serveur sans le mot « serveur ». J'ai changé « alors que toi, tu n'as rien fait » en « alors que toi, tu jouais bien » : c'est plus drôle et plus gamer.
- **La carte mémoire** : la meilleure image du script pour ton public, garde-la. Seul risque : les plus jeunes n'ont pas connu les cartes mémoire de console. Si tu veux, remplace-la par « la sauvegarde en local ».
- **« La tête de celui qui atteint la limite »** : gardée. C'est une réaction, exactement ce que l'axe 10 demande.
- **Le boss de Dark Souls** : dans ton registre (Monster Hunter, Rathalos). Gardé tel quel.
- **Ajoutées dans le `script.md`, à valider** : les six cents gardes du corps, le badge « 0 BUG » qui se fissure, le téléphone au musée en 2050. Remplace celles qui ne sont pas de toi.

### « Battu Oracle » : une minute entière, non

Une minute « légende à corriger », c'est trop. La vidéo de ByteMonk est en anglais (220 K vues) : la plupart de tes spectateurs n'ont jamais entendu ce « battu Oracle ». Passer une minute à démentir une phrase qu'ils ne connaissent pas, c'est l'homme de paille du skill, en version longue.

Deux phrases accrochées à la correction du « 300 Ko », en revanche, sont utiles :
- elles vaccinent les devs qui ont vu ByteMonk ;
- elles servent l'explication : Oracle est un serveur, SQLite un fichier dans l'appli, ils ne font pas le même boulot. On revient au cœur de la section 3.

Le fait est sourcé (DB-Engines, octobre 2026 : Oracle 1er, SQLite 11e, fait 30). C'est dans le `script.md`, entre crochets « à valider ». Si tu les gardes, relis DB-Engines avant le tournage.

## Ce qu'il faut garder

- « Dans ton téléphone, là, maintenant, il y a probablement des centaines de petites bases de données. » La première phrase idéale : le spectateur est dedans, et c'est sourcé.
- « C'est comme perdre ta partie en ligne parce que le serveur du jeu a lâché » puis « SQLite, c'est la sauvegarde sur la carte mémoire. Personne ne peut la couper à ta place. » Un planté-récolté parfait, et une analogie qui n'est pas celle de ByteMonk.
- Le dictionnaire pour le B-arbre : on comprend en une phrase, sans le mot « logarithme ».
- Le WAL « comme un brouillon » : simple et juste (fait 25).
- La relance à 60 % : la musique qui coupe, la batterie à 1 %, puis « Tu vois le téléphone qui s'éteint de tout à l'heure ? Il est dans les tests. » La boucle la mieux fermée du script.
- « Donc le même logiciel que dans ton téléphone vole au-dessus de ta tête. » La meilleure chute.
- « tu sauras qui remercier » : une fin qui retourne quelque chose au lieu de résumer.
- La discipline des sources : « d'après sqlite.org », « mesures de 2023 », « d'après des analyses forensiques ». Avec un public de devs, c'est ce qui rend crédible tout le reste.

## Plan d'action (fait dans `script.md`)

1. **Section 5** : la vantardise, la claque d'Android, la norme d'avion, les dates de TH3 (n° 1). C'est le plus gros changement, environ 150 mots.
2. **Faits** : l'anecdote inventée passe en crochet (n° 2) ; les surclassements, Skype, les liaisons à contresens et les petits points (n° 4, 10).
3. **Hook** : le contraste échelle contre origine, et l'Airbus planté (n° 3).
4. **Rétention** : l'abonnement dans la boucle à 23 % (n° 5), la section 3 en « mais / donc » (n° 6), la devinette (n° 7).
5. **Passe anti-IA** (n° 8), puis toi : le titre, les blagues, Oracle, tes deux crochets.

## La vérification des faits

Chaque affirmation de la voix off du V1, comparée à `sources.md` (colonne « 2e vérif »). Ce qui n'y était pas a été cherché à la source primaire le 23/10/2026, puis ajouté en fin de tableau de `sources.md` (faits 35 à 40).

| Phrase du V1 | Verdict | Source, et ce qui change dans `script.md` |
|---|---|---|
| « il y a probablement des centaines de petites bases de données » | ✅ | Fait 32 (« each holding hundreds of SQLite database files »), relu le 23/10. Le « probablement » reste. |
| « plus de quatre milliards de smartphones […] plus de mille milliards de bases SQLite en service » | ✅ | Fait 1. « Sur Terre » coupé. |
| « ce logiciel n'a même pas de serveur » | ✅ | Fait 26. Déplacé : il devient la réponse de la section 3. |
| « chaque appareil Android, chaque iPhone, chaque Mac, et chaque Windows dix et onze. Et dans Chrome, Firefox et Safari » | ✅ | Fait 4. |
| « Skype, Dropbox, Python, la plupart des téléviseurs et des box, […] des systèmes multimédias des voitures » | ⚠️ | Fait 4, mais Skype a fermé le 5 mai 2025 (fait 38, ajouté). **Skype retiré.** |
| « Moi, je suis dev, et SQLite, je l'ai rangé dans mes propres applis. » | ❌ | Aucune source : anecdote inventée. **Passée en crochet.** |
| « Google donne aux développeurs une boîte à outils toute prête […] dossier privé de l'appli. Personne d'autre n'y touche. » | ✅ / ⚠️ | Fait 20 ; « personne d'autre n'y touche » force le sens de « private folder ». **Coupé** (peu utile, et il retarde WhatsApp). |
| « D'après des analyses forensiques, sur Android, WhatsApp range tes messages dans un fichier SQLite » | ⚠️ | Fait 22 (2016), complété par le fait 39 (analyse de juillet 2026, ajouté). Formulation gardée. |
| « Tes conversations, tes groupes, tout ça finit dans une petite base » | ⚠️ | « Tes groupes » absent des sources. **Coupé.** |
| « Résultat, sqlite.org pense que SQLite est probablement utilisé plus que tous les autres moteurs […] réunis » | ✅ (fait) / ❌ (liaison) | Fait 2. « Résultat » devient « Voilà pourquoi ». |
| « la deuxième bibliothèque logicielle la plus déployée au monde, juste après libz » | ✅ | Fait 3 ⚠️, avec la bonne formulation. |
| « Le truc le plus installé de ta vie » | ❌ | Contredit le fait 3. **« Un des logiciels les plus installés de ta vie ».** |
| « D. Richard Hipp est sous-traitant pour Bath Iron Works, un chantier naval qui construit des navires pour l'US Navy » | ✅ | Fait 14 ; la description du chantier, absente de `sources.md`, est vérifiée dans la presse spécialisée (fait 40, ajouté). |
| « le USS Oscar Austin » ; « contrôle des avaries […] isoler la partie touchée » | ✅ | Fait 14. « Le USS » devient « l'USS ». |
| « Informix […] ce serveur, de temps en temps, il tombe. Et quand il tombe, l'appli de Hipp ne marche plus. » | ✅ | Fait 14 (« sometimes the server would go down »). Dans le hook : « un serveur qui plantait », sans « sans arrêt ». |
| « « Richard, pourquoi tu n'en écris pas une toi-même ? » » | ✅ | Fait 14. Ajout de sa réponse, « OK, je vais essayer » (« Okay, I'll give it a try », fait 36, ajouté). |
| « les contrats publics sont gelés, et il se retrouve quelques mois sans travail » | ✅ | Fait 15 (« out of work for a few months », relu). |
| « Le projet SQLite démarre le neuf mai deux mille, et la version un point zéro sort le dix-sept août » | ✅ | Faits 12, 13. |
| « un type s'ennuyait, et il a écrit le logiciel le plus installé de ta poche » | ❌ | « S'ennuyait » non sourcé ; « le plus installé » contredit le fait 3. **Réécrit.** |
| « une bibliothèque […] rien à configurer. La base, c'est un fichier » | ✅ | Fait 26. |
| « moins d'un mégaoctet. En deux mille vingt-trois, […] entre cinq cent quatre-vingt-dix et sept cent cinquante kilo-octets » | ✅ | Fait 5. |
| « si tu as vu passer « trois cents kilo-octets » quelque part, c'est faux aujourd'hui » | ✅ | Faits 5, 34 : légende corrigée, le seul endroit où « 300 Ko » apparaît. |
| « Ça reste minuscule, mais en fait, pas aussi minuscule. » | — | Phrase vide. **Coupée.** |
| « La taille maximale d'une base SQLite, c'est deux cent quatre-vingt-un téraoctets » | ✅ | Fait 26. |
| « Dans un essai de deux mille dix-sept, sqlite.org mesurait environ trente-cinq pour cent de gagné » | ✅ | Fait 23, dit comme un essai. |
| « les cent premiers octets […] « SQLite format 3 » » | ✅ | Fait 24. |
| « Par défaut, quatre mille quatre-vingt-seize octets » | ⚠️ | Fait 24 : le défaut dépend de la plateforme (4 096 depuis la 3.12.0). **« En général ».** |
| « ces pages sont rangées en arbre » ; « en quelques sauts » | ✅ | Fait 24 (B-arbres) ; « en quelques sauts » est une illustration. |
| « depuis deux mille dix, SQLite a un mode qui s'appelle le WAL » ; le brouillon, le checkpoint ; « ceux qui lisent ne bloquent plus celui qui écrit » | ✅ | Fait 25. |
| « Et ça arrive sur des milliards d'appareils. » | ❓ | Aucune source ne compte les coupures pendant une écriture. **Retiré.** |
| « un type qui a passé un an, à soixante heures par semaine, à chasser ses propres bugs » | ✅ | Fait 27. |
| « À un moment, des bugs remontent depuis Android. » | ❓ → ✅ | Date absente de CoRecursive ; trouvée sur th3.html (fait 35, ajouté) : chantier du 25/09/2008 au 25/07/2009. La scène vient de CoRecursive (fait 36, ajouté). **Réécrit** (grill n° 1). |
| « tester chaque branche du code. Chaque « si », chaque « sinon ». » | ✅ | Fait 7 et définition de Hipp (fait 36). |
| « « On a arrêté de recevoir des rapports de bugs d'Android. » » | ✅ | Fait 27. |
| « le cœur de SQLite est couvert à cent pour cent : chaque branche testée, et […] le MC/DC » | ✅ | Fait 7. |
| « En deux mille vingt-trois, pour cent cinquante-six mille lignes de code, […] quatre-vingt-douze millions de lignes de tests. Cinq cent quatre-vingt-dix fois plus. » | ✅ | Fait 6. |
| « plus de mémoire, erreurs de disque, et plantages en plein milieu d'une écriture, coupures de courant comprises » | ✅ | Fait 8. |
| « Mais l'histoire ne s'arrête pas aux téléphones. […] Du coup, les développeurs construisent une deuxième suite de tests, TH3 » | ❌ (chronologie) | TH3 *est* le chantier de 2008-2009, pas une suite construite après (faits 10, 35). **Fusionné dans le récit de la section 5.** |
| « rien ne dit que SQLite est certifié pour les avions » | ✅ | Fait 10 : la certification n'apparaît nulle part comme affirmée. |
| « d'après sqlite.org, Airbus confirme que SQLite tourne dans le logiciel de vol de l'A trois cent cinquante » | ✅ | Fait 11. Ajouté aussi dans le hook. |
| « Le code de SQLite est dans le domaine public » ; la déclaration écrite pour contribuer | ✅ | Fait 16. |
| « Hwaci, la société qui emploie les développeurs, vend aussi des garanties juridiques » | ✅ (formulation juste du fait 17 ⚠️) | **Coupé** (peu utile, et il portait la liaison à contresens). |
| « la Bibliothèque du Congrès américain range les fichiers SQLite parmi ses formats préférés […] à côté du CSV et du JSON » | ✅ | Fait 18 (« d'après sqlite.org (2018) » à l'écran). |
| « un engagement que presque personne ne prend : soutenir SQLite jusqu'en deux mille cinquante » | ✅ / ❓ | 2050 : fait 19 ✅ ; « que presque personne ne prend » : aucune source. **Coupé.** |
| « on en est à la version trois point cinquante-quatre point un » | ✅ au 23/10/2026 | Fait 31, mais faux à la sortie en mars 2027. **Coupé.** |
| « un fichier de ta toute première appli s'ouvrira encore dans vingt-quatre ans » | ⚠️ | Fait 19 : une intention ; 23 ans en 2027. **« devra encore s'ouvrir »**, sans compte d'années. |
| « un type au chômage technique pendant trois mois » | ⚠️ | Mauvais terme (fait 15 : sous-traitant sans contrat). **Bilan réécrit.** |
| « le mode WAL ne marche pas sur un système de fichiers en réseau » | ✅ | Fait 25. |
| « une cinquantaine d'ingénieurs le faisaient tourner pour neuf cents millions de personnes » | ✅ | `projets/whatsapp/sources.md`, faits 1 et 2. **Daté : « en deux mille quinze ».** |

**Ajouté dans `script.md`, vérifié au grill** : la vantardise « naïvement », les « millions de téléphones », « ça plante sans arrêt », « Android nous a clairement donné tort », Rockwell Collins, DO-178B, les journées de douze heures et « OK, je vais essayer » (fait 36) ; les dates du 25/09/2008 et du 25/07/2009 (fait 35) ; Oracle 1er et SQLite 11e chez DB-Engines (fait 30, déjà ✅, à relire avant le tournage).

**Les points critiques de la commande** :
- « 300 Ko » : n'apparaît que comme légende corrigée (section 3).
- « Battu Oracle » : seulement comme légende corrigée, entre crochets « à valider ».
- « Certifié DO-178B » : absent ; le script dit « rien ne dit que SQLite lui-même est certifié pour voler ».
- « Des centaines de petites bases de données » : sourcé (fait 32).
- La date des bugs d'Android : trouvée pour le chantier (2008-2009) ; les plantages eux-mêmes ne sont pas datés, et le script ne les date pas.
- « Le logiciel le plus installé du monde » : nulle part. Le script dit « deuxième, juste après libz » et « un des logiciels les plus installés ».

## Les questions qui restent pour toi

1. Ton vécu avec SQLite (crochet de la section 1) : tu l'as déjà utilisé ? Sinon, on coupe.
2. Ton avis de dev pour la fin : quand SQLite, quand un vrai serveur ?
3. Le titre recommandé, et la variante B.
4. Oracle : les deux phrases, oui ou non ?
5. Les blagues, surtout les trois nouvelles.
6. Le sous-texte : « on ne devient fiable qu'après avoir eu tort » (la claque d'Android), c'est ce que tu veux dire, ou tu préfères celui de la fiche ?
