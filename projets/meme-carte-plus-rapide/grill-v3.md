# Grill de la V3 : « Même carte, 2 fois plus rapide » (18/11/2026)

> Critiqué : [`script.md`](script.md) (V3 du 18/11) et [`teleprompteur.txt`](teleprompteur.txt) (identique à `teleprompteur.md`, et mot pour mot à la voix de `script.md`, vérifié par script). Comparé à [`script-v2.md`](script-v2.md). Seule source de chiffres : [`sources.md`](sources.md) (M1…M38, F). Méthode : skill `youtube-script-grill`, mode B, **variante storytelling** (test des 30 secondes, axe 10) ; règles de `.claude/rules/script.md`. Les numéros « l. N » renvoient aux lignes de `teleprompteur.txt`.
>
> **Débit** : 145 mots/min, comme dans `grill-v1.md`. Mais ta voix de lundi (`../strata-test/strata-test.fr.srt`, 207 sous-titres distincts, 2 195 mots en 9 min 25) tourne à **≈ 233 mots/min** une fois montée. Les deux temps sont donnés. À 233, la V3 (1 529 mots) dure **≈ 6 min 35**, pas les 10 min 50 annoncées en tête de `script.md`.

## Verdict

**V3 : 7,5/10. Avec les 4 corrections bloquantes : 8,5/10.**

Le corps de la V3 est le meilleur des trois. Les chiffres sont justes, à quelques réserves près, et aucun nom n'est dit dans la voix. Il ne reste qu'un seul renvoi à une autre vidéo. Les récoltes marchent bien : la mesure du début, la 4080, la falaise. Le gros problème est **l'ouverture** :
- **l'origine des chiffres arrive à 59 s** (37 s à ton débit réel), alors que tu la veux dans les 30 premières secondes. Pendant une minute, « tu allumes… ton IA écrit 2 fois plus vite » sonne comme une promesse pour la machine du spectateur. Ça va contre ton exigence 4 et contre `sources.md` § H (« dans la première minute : écriture, modèle qui tient, mesures d'autres testeurs ») ;
- **l'annonce de la révélation est fausse et la gâche** : « le réglage qu'on croit fait pour la vitesse, et qui ne la change pas ». Il la change, puisqu'il la ralentit (M26, M27). Et la réponse tombe 8 minutes avant la question « À ton avis, est-ce que ça fait écrire plus vite ? » (l. 109) ;
- **une phrase affirme plus que la source** : « personne n'a vérifié s'il l'allume tout seul » (l. 38) ;
- **le téléprompteur ne respecte pas « une ligne = un souffle »** : la l. 7 fait 49 mots, la l. 78 en fait 34, et 10 autres lignes dépassent 22 mots.

## Test des 30 secondes (V3 telle quelle)

Temps cumulés à 145 mots/min (entre parenthèses : à 233).

| Tranche | Ce que dit le téléprompteur | Verdict |
|---|---|---|
| 0-5 s | > « Sur une carte de 16 gigas, tu allumes un seul paramètre, » | 🟢 Le sujet et la tension (un seul réglage) sont là tout de suite, raccords avec la miniature. |
| 5-11 s | > « et ton IA écrit 2 fois plus vite : de 29 à 64 tokens par seconde. » | 🟢 Le meilleur moment, avec sa preuve à l'écran (bandeau). 🟠 « tu » et « ton IA » sans attribution : c'est la mesure d'un autre (M5). |
| 11-13 s | > « Même fichier, même carte, rien acheté. » | 🟢 Monte l'enjeu en 6 mots. À garder. |
| 13-24 s | > « Et ce n'est pas un coup de chance : sur 5 modèles de cartes de 16 gigas, 6 mesures trouvent entre 1,9 et 2,3 fois plus vite. » | 🟠 Le chiffre fait monter l'enjeu, mais l'ouverture est une fausse opposition (« ce n'est pas A »). Et c'est l'endroit idéal pour dire « publiées » : il manque. |
| 24-29 s | > « Du coup, ta carte, elle serait pas bridée, sans que tu le saches ? » | 🟢 Une seule question centrale, en mots simples, raccord avec « TA CARTE BRIDÉE ? », à 29 s (18 s). |
| Pont, 29-59 s (18-37 s) | > « Donc on va voir le réglage qui peut doubler… un tiers de ta vitesse, rien qu'avec une conversation trop longue. Et reste jusqu'à la fin, parce qu'on va démystifier le réglage qu'on croit fait pour la vitesse, et qui ne la change pas. » | 🟠 Les livrables sont bons : « doubler », le tiers perdu. 🔴 Mais la révélation est donnée, et elle est inexacte (voir B2). 🔴 72 mots sur 2 lignes. |
| 59-73 s (37-46 s) | > « Ces chiffres ne sont pas les miens, ce sont des mesures publiées : je n'ai rien testé chez moi. Et c'est l'écriture, sur Qwen 3.8 27B, un modèle qui tient en entier dans la carte. » | 🔴 L'origine arrive après 30 s à tous les débits, et « modèle qui tient » arrive après la première minute à 145 mots/min. C'est encore une fausse opposition (« ne sont pas les miens, ce sont… »). « Et c'est l'écriture » ne se comprend pas à l'oreille. |

**Budget** : 71 mots jusqu'à la question, soit 29 s (18 s) ✅. Le plan court jusqu'à 59 s (37 s), et la première partie (« Ce réglage, c'est le MTP ») commence à 1:14 (0:46).
**À couper ou déplacer** : « ce n'est pas un coup de chance » ; la l. 10, à fondre dans le hook ; « qu'on croit » et « qui ne la change pas ».

**Réécriture des 30 s** : la correction B1 ci-dessous (76 mots jusqu'à la question, ≈ 31 s à 145 et ≈ 20 s à 233). Ta phrase d'ouverture reste mot pour mot, et l'origine est dite une seule fois, vers 0:17.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Le « 2× » et « bridée ? » sont tenus, mais les conditions qui les rendent vrais arrivent à 1:06-1:13, et l'annonce de la révélation est fausse. |
| 2. Alignement | 🟢 | « Avant d'en racheter une plus grosse, essaie ça » et « sans rien acheter » : l'intérêt du spectateur passe d'abord. |
| 3. Problème profond | 🟢 | « Ta carte est mal réglée, pas trop petite » : semé au début (« bridée ? »), résolu à la fin (« Si le MTP est éteint, ou si ton fichier déborde, oui »). |
| 4. Public & complexité | 🟢 | Le jargon est traduit (« le moteur, le programme qui fait tourner le modèle », « cache KV, la mémoire de la conversation »). La section 4 (experts, 32-64 gigas de RAM) reste la plus pointue. |
| 5. Valeur & originalité | 🟢 | « 5 de ces 6 mesures viennent du même tableau », « ces deux gains ne s'additionnent pas » : personne ne dit ça en français. |
| 6. Structure | 🟢 | De l'indispensable au piège, puis au réglage démystifié, puis la liste et la réponse. Le plan ne cite pas le fichier qui tient, mais la l. 45 en fait un « sauf que », et ça marche. |
| 7. Histoire | 🟠 | Une liste de réglages, portée par la question « bridée ? » et par des personnages qui reviennent (la mesure du début, la 4080). Pour un tuto, c'est suffisant. |
| 8. Mais / donc | 🟢 | Chaque partie s'ouvre sur un « sauf que » ou un « mais » qui la rend nécessaire. |
| 9. Engagement | 🟠 | « À ton avis… Garde ta réponse. » est excellent, mais le plan l'a déjà répondu à 0:55. |
| 10. Rythme & liaisons | 🟠 | **1,70** liaison pour 100 mots sur la liste courte (26 sur 1 529) ✅, et 2,16 avec « par contre », « alors », « justement ». Mais 12 lignes dépassent un souffle, et 5 paragraphes s'ouvrent par « Sauf que ». |
| 11. Tics d'IA | 🟠 | 4 phrases en « pas A, B » (l. 4, 10, 119, 127). Celle de la l. 119 est juste, celle de la l. 127 est une petite morale qui redit la l. 114. |
| S1. 30 premières secondes | 🟠 | La question est posée à 29 s, mais l'origine et les conditions arrivent après. |
| S2. Pont | 🟠 | Le plan fait office de pont, mais il ferme la boucle de la fin au lieu de l'ouvrir. |
| S3. Retournements | 🟢 | Un toutes les 30 à 45 s ; aucun trou d'une minute. |
| S4. Planté / récolté | 🟢 | La mesure du début revient 4 fois, la 4080 et la falaise 2 fois chacune, « bridée » 3 fois. |
| S5. Personnages | 🟠 | « La mesure du début » est une chose, pas une personne : c'est le prix de ton exigence « pas de "un testeur" ». C'est accepté. |
| S6. Fin | 🟢 | Elle répond à la miniature, puis ouvre lundi. On peut encore la renforcer (A9). |

## Tes 7 exigences, une par une

| # | Exigence | Tenue ? | Lignes en cause |
|---|---|---|---|
| 1 | Script complet, rien d'inventé, jamais « j'ai testé » | 🟢 presque | Aucun crochet, aucune anecdote, et seulement « je n'ai rien testé ». ❌ l. 38 : « personne n'a vérifié » affirme un fait que `sources.md` ne tient pas (B3). |
| 2 | Téléprompteur : seulement des lignes à lire, un souffle par ligne, nombres en chiffres | 🟠 | Aucun titre, marqueur, crochet ni parenthèse ✅. ❌ Souffle : l. 7 (49 mots), 78 (34), 46 et 72 (27), 1, 4, 80, 105 et 112 (26), 14 (24), 8 et 51 (23). Chiffres : « deux gestes » (l. 105), « ces deux réglages » (l. 60), « ces deux gains » (l. 56) sont des quantités, à écrire « 2 » (A11). |
| 3 | Un seul renvoi dans le corps + l'annonce finale | 🟢 | Seul renvoi : l. 77 ✅. Annonce : l. 141 ✅. « Tu te rappelles » (l. 93, 101), « celle du début » (l. 26), « la mesure du début » (l. 119, 125) renvoient à **cette** vidéo : ce sont des récoltes, pas des renvois cachés. « Une chaîne française » (l. 78) cite la vidéo d'un autre, qui se comprend sans l'avoir vue : ça ne compte pas comme renvoi. Une réserve : à la l. 77, « tu as vu » suppose que le spectateur l'a vue (A5). |
| 4 | Ton hook, pas de « un testeur… un testeur », l'origine une fois dans les 30 s | 🔴 | Hook mot pour mot ✅, aucun « un testeur » ✅. ❌ L'origine est dite à la l. 10, vers **59-67 s** (37-41 s à 233) (B1). |
| 5 | Plan percutant, « doubler », livrables concrets, révélation de fin | 🟠 | « peut doubler » ✅, « un tiers de ta vitesse » ✅. ❌ l. 8 : « qu'on croit » (une croyance sans source), « qui ne la change pas » (faux, et ça gâche la révélation). 🟠 « le moteur qui te permet d'y arriver » n'est jamais livré en clair (A1). Deux variantes plus fortes en B2. |
| 6 | Ta voix : « tu », « on », ami, phrases courtes, ≥ 1,5 liaison / 100 mots, aucun nom, pas de tics | 🟠 | Liaisons à 1,70 ✅, aucun nom ✅, tutoiement ✅. 🟠 4 « pas A, B » ; peu de réactions et presque pas d'humour (A12). |
| 7 | Le hook promet-il plus que les sources ? | 🔴 tel quel, 🟢 après B1 | Le « 2 fois » est tenu (M5 ×2,19, M1-M6 ×1,9 à 2,3). Mais `sources.md` § G interdit « ta carte ira 2 fois plus vite » sans condition, et la V3 laisse le « tu » sans condition pendant 59 s. Avec B1, « mesures publiées » arrive à 0:17 et « modèle qui tient » vers 0:37. Le « un seul paramètre » reste un peu optimiste : il faut aussi un fichier qui contient le module (l. 36), mais c'est dit honnêtement à 2:55. |

## Corrections

### Bloquant avant l'enregistrement

#### B1. L'origine des chiffres et les conditions entrent dans les 30 secondes (l. 1-11)

> l. 4 : « Et ce n'est pas un coup de chance : sur 5 modèles de cartes de 16 gigas, 6 mesures trouvent entre 1,9 et 2,3 fois plus vite. »
> l. 10-11 : « Ces chiffres ne sont pas les miens, ce sont des mesures publiées : je n'ai rien testé chez moi. Et c'est l'écriture, sur Qwen 3.8 27B, un modèle qui tient en entier dans la carte. »

**Pourquoi ça coince :**
- l'origine tombe à 59 s (exigence 4), et « modèle qui tient » à 1:13 (§ H) ;
- deux fausses oppositions de suite ;
- « Et c'est l'écriture » ne se comprend pas à l'oral.

**Réécriture** (remplace les l. 1 à 5 et 10-11 ; ta phrase d'ouverture est seulement coupée en deux souffles) :

```
Sur une carte de 16 gigas, tu allumes un seul paramètre,
et ton IA écrit 2 fois plus vite : de 29 à 64 tokens par seconde.
Même fichier, même carte, rien acheté.

Et c'est ce que trouvent 6 mesures publiées,
sur 5 modèles de cartes de 16 gigas : entre 1,9 et 2,3 fois plus vite.
Moi, j'ai rien testé : ce sont leurs chiffres.
Du coup, ta carte, elle serait pas bridée, sans que tu le saches ?

Et attention : ça vaut pour l'écriture,
sur Qwen 3.8 27B, un modèle qui tient en entier dans la carte.
```

- 76 mots jusqu'à la question (≈ 31 s à 145, ≈ 20 s à 233) ; les conditions finissent vers 0:37 (0:24), avant le plan.
- « publiées » à 0:17 : l'origine est dite une fois, sans « un testeur » (M1-M6).
- Les conditions passent avant le plan parce qu'elles tiennent maintenant en une seule phrase. La V1 avait une rafale de 4 conditions, et c'est pour ça que la V2 les avait mises après.
- Juste après le plan, la l. 13 doit nommer le réglage, sinon « Ce réglage » renvoie au réglage démystifié du plan. Écris : `Le réglage qui double, c'est le MTP, un petit module en plus dans le modèle.`

#### B2. Le plan : une révélation fausse et dévoilée, et une ligne de 49 mots (l. 7-8)

> l. 8 : « Et reste jusqu'à la fin, parce qu'on va démystifier le réglage qu'on croit fait pour la vitesse, et qui ne la change pas. »

**Pourquoi ça coince :**
- « qui ne la change pas » est faux. En 8 bits l'écriture perd 6,6 % (M26), et en 4 bits à 64 000 tokens elle perd 35 % (M27). La l. 113 le dit elle-même : « elle perd même 35 % ».
- La réponse est donnée à 0:55, alors que la l. 109 la demande à 8:27 (« À ton avis… Garde ta réponse »). La révélation est morte avant d'arriver.
- « qu'on croit » ramène la croyance sans source que la V2 avait retirée (« tout le monde conseille »).
- La l. 7 se lit en un seul souffle de 49 mots.

**Est-ce que ça donne envie de rester ?** À moitié. « Doubler » et « un tiers de ta vitesse » accrochent. « Le moteur qui te permet d'y arriver » est vague, et la fin ne laisse plus rien à découvrir.

**Variante A, recommandée** (ta phrase, resserrée ; la fin devient une boucle ouverte ; 71 mots, ≈ 29 s à 145, ≈ 18 s à 233) :

```
Donc on va voir le réglage qui peut doubler la vitesse de ta carte graphique,
et le moteur qui te permet d'y arriver.
Et surtout, tout ce qu'il faut éviter pour ne pas perdre ce que tu as gagné :
une conversation trop longue, et c'est déjà un tiers de ta vitesse qui part.
Et reste jusqu'à la fin, parce qu'on va démystifier un réglage
que tu as peut-être allumé pour aller plus vite.
```

**Variante B** (plus concrète : les deux pièges sont chiffrés ; 70 mots) :

```
Donc on va voir le réglage qui peut doubler ta vitesse,
et le moteur qui te permet d'y arriver.
Et surtout, les 2 pièges qui te reprennent ce que tu as gagné :
un fichier qui déborde, et ta vitesse est divisée par 3,
une conversation trop longue, et c'est un tiers qui part.
Et reste jusqu'à la fin : on va démystifier un réglage
que tu as peut-être allumé pour aller plus vite.
```

- « divisée par 3 » : 43 → 12,5 (M13) ; « un tiers » : M22.
- « que tu as peut-être allumé » est une hypothèse sur le spectateur, pas une croyance attribuée à « on » ou à « tout le monde » : aucune source n'est nécessaire.
- Dans les deux variantes, la récolte arrive à la l. 127 (voir A4).

#### B3. « Personne n'a vérifié » : plus fort que la source (l. 38)

> « Par contre, personne n'a vérifié s'il l'allume tout seul. »

**Pourquoi ça coince :** M30b dit « Non vérifié » : c'est **nous** qui ne l'avons pas vérifié. « Personne », c'est une affirmation sur le monde entier, sans source. En plus, ça sonne bizarre : tu as LM Studio, le spectateur se demandera pourquoi tu n'as pas regardé.

**Réécriture** :

```
Par contre, je n'ai trouvé écrit nulle part s'il l'allume tout seul.
```

Si tu ouvres LM Studio 0.4.28 avant d'enregistrer, remplace cette ligne par ce que tu vois. Lire un réglage, ce n'est pas un test de vitesse : ça reste compatible avec la vidéo calculée.

#### B4. Une ligne = un souffle (12 lignes trop longues)

Les l. 7 et 8 sont déjà réglées par B2, et les l. 1 et 4 par B1. Pour les autres, voici les coupes exactes, sans changer un mot :

| Ligne | Mots | Coupe proposée |
|---|---|---|
| 14 | 24 | `En gros, c'est comme les suggestions du clavier de ton téléphone :` / `le modèle propose plusieurs tokens d'avance, puis il les vérifie tous d'un coup.` |
| 46 | 27 | `Sur une 4080 de 16 gigas, avec un Qwen de 27 milliards plus ancien :` / `un fichier de 15 gigas qui déborde un peu, 20 tokens par seconde.` |
| 51 | 23 | `Sur une 5060 Ti, quelqu'un a laissé dehors exprès 8 couches sur 48 d'un modèle plus petit :` / `on tombe de 43 à 12,5.` |
| 72 | 27 | `Et sa version 0.2.14, sortie le 15 novembre, lit ton prompt plus vite,` / `mais écrit environ 10 % moins vite sur une 5070 Ti, d'après le projet lui-même.` |
| 78 | 34 | voir A2 (réécrite et coupée) |
| 80 | 26 | `Sauf que son dernier moteur ne marche que sur les cartes RTX 50, sous Linux,` / `et il ne donne ni ses versions ni ses réglages exacts.` |
| 105 | 26 | `Bref, 2 gestes tout bêtes : une nouvelle conversation dès que tu changes de sujet,` / `et une taille de conversation réglée au plus juste dans ton moteur.` |
| 112 | 26 | `Sur une 5060 Ti, avec un petit modèle de 7 milliards, l'écriture est 6,6 % plus lente en 8 bits,` / `et 1,8 % plus lente en 4 bits.` |

### Améliorations (par ordre de priorité)

#### A1. Livrer en clair « le moteur qui te permet d'y arriver » (l. 64)

> « Mais tout ça dépend aussi du moteur, le programme qui fait tourner le modèle. »

**Problème :** le plan promet un moteur, mais la section 3 parle surtout d'Ollama qui ralentit. Le spectateur n'entend jamais « c'est celui-là ». Les identifiants du plan dans `script.md` (M29, M30) ne tiennent pas cette promesse ; ce qui la tient, c'est M8, M30b et l'en-tête de § A (les 6 mesures sont toutes sur llama.cpp).

**Réécriture** :

```
Et le moteur qui te permet d'y arriver, le programme qui fait tourner le modèle, c'est llama.cpp :
les 6 mesures du début ont toutes été faites dessus.
```

Les l. 65 à 68 restent telles quelles (Ollama 10 à 30 % plus lent, LM Studio à égalité, « t'es tranquille »).

#### A2. La vidéo française : « en entier » induit en erreur (l. 78)

> « Sur un gros modèle à experts, Qwen 3.8 Flash Next en entier, une chaîne française vient de passer de 8 à 83 tokens par seconde sur une 5060 Ti, surtout en changeant de moteur. »

**Problème :**
- dans la V2, « en entier » s'opposait au Coder de ta vidéo de lundi. Ce lien a disparu ;
- à l'oreille, après « un modèle qui tient en entier dans la carte » (l. 11), on comprend que Flash Next tient sur une 5060 Ti. C'est le contraire : 125 milliards de paramètres (M37), des fichiers de dizaines de gigas (M19 : 78 Go) ;
- la ligne fait 34 mots.

« Sur une 5060 Ti » est juste : son 7,9 est mesuré avant d'ajouter sa 3070 (M38). Et sa transcription (`etudes/transcriptions/nathaninline-VFC16Tb3lwU.md`, 4:56-5:17) dit que Basalt refuse la 3070 et qu'il ne l'utilise pas.

**Réécriture** :

```
Sur un modèle à experts énorme, Qwen 3.8 Flash Next, beaucoup trop gros pour 16 gigas,
une chaîne française vient de passer de 8 à 83 tokens par seconde sur une 5060 Ti,
surtout en changeant de moteur.
```

#### A3. « Dans le même test » pointe vers le mauvais test (l. 123), et le 4 bits du début (l. 125)

> « Dans le même test, la réponse en 8 bits ressemble à 82 % à celle d'origine. »
> « Et au moins 3 des 6 mesures du début étaient en 4 bits. »

**Problème :**
- entre M26 (l. 112) et cette ligne, on a entendu M27 (machine Nvidia) et M28 (32 000 → 128 000). « Le même test » renvoie donc à M28, alors que les 82 % et 8 % viennent de M26 ;
- la l. 125 laisse croire que les mesures du « ×2 » donnaient des réponses ressemblantes à 8 %. Or M26 porte sur un modèle de 7 milliards à 8 000 tokens, et la qualité des mesures M1-M6 n'est mesurée nulle part.

**Réécriture** :

```
Sur le petit modèle de 7 milliards de tout à l'heure, la réponse en 8 bits ressemble à 82 % à celle d'origine.
En 4 bits, à 8 % seulement.
Et au moins 3 des 6 mesures du début étaient en 4 bits, sur un modèle bien plus gros :
ce que ça leur a coûté en qualité, aucune ne le dit.
```

#### A4. La petite morale de la l. 127 : la changer en récolte du plan

> « En fait, ce réglage ne sert pas à aller plus vite : il sert à tenir plus longtemps. »

**Problème :** c'est une fausse opposition qui redit les l. 114 et 116 (« pour la vitesse, il ne sert à rien. Sauf qu'il fait de la place »), en morale de fin de paragraphe. Elle tombe en plus après « reste en 8 bits ».

**Réécriture** (elle récolte le « démystifier » de B2) :

```
Voilà le réglage démystifié : lui, il sert à tenir plus longtemps.
```

#### A5. Le seul renvoi ne doit pas supposer qu'on a vu la vidéo (l. 77)

> « Dans la vidéo précédente, tu as vu ce que ça donne : la RAM pleine, et le disque qui se met à lire. »

**Problème :** pour un nouveau spectateur, « tu as vu » est faux, et ton exigence 3 veut que tout se comprenne sans l'autre vidéo.

**Réécriture** :

```
Dans la vidéo précédente, je te l'ai montré : la RAM pleine, et le disque qui se met à lire.
```

#### A6. Le « 2 fois » moyen concerne le tableau, pas la mesure du hook (l. 29)

> « En fait, ce « 2 fois », c'est une moyenne sur du code, du texte et des commandes, avec la réflexion coupée. »

**Problème :**
- cette condition de § A vaut pour le tableau partagé (M1-M4, M6) ;
- le 29 → 64 du hook (M5) vient d'un banc sur du code (l'article de M5 porte « mtp-coding » dans son adresse, déjà noté dans `grill-v1.md`), à 4 000 tokens ;
- juste après, la l. 31 dit « C'est sur du code que ça gagne le plus ». Le spectateur attentif comprendra donc que le hook est le meilleur cas, alors que la phrase lui dit l'inverse.

**Réécriture** :

```
En fait, dans le tableau, ce « 2 fois », c'est une moyenne sur du code, du texte et des commandes, avec la réflexion coupée.
```

#### A7. « Sur une même carte » : dire laquelle (l. 117)

> « Sur une même carte, on passe de 32 000 à plus de 128 000 tokens de conversation. »

**Problème :** « une même carte » sonne écrit et vague. M28 cite l'article de M14 : une 3080 de PC portable de 16 Go, avec le modèle du hook. C'est plus parlant.

**Réécriture** :

```
Sur une 3080 de PC portable de 16 gigas, avec Qwen 3.8 27B, on passe de 32 000 à plus de 128 000 tokens de conversation.
```

#### A8. Le modèle à experts : une seule source citée, alors qu'il y en a deux (l. 32)

> « Et sur un modèle à experts, une mesure ne donne que 1,5 fois. »

**Problème :** c'est ×1,47 sur Qwen 3.6 en avril (M10), et M11 donne même ×1,28. « 1,5 » est le haut de la fourchette. C'est mineur, mais facile à rendre exact.

**Réécriture** :

```
Et sur un modèle à experts, les mesures tombent à 1,5 fois au mieux.
```

#### A9. L'annonce de lundi peut ouvrir une vraie boucle (l. 141)

> « Et si ta carte n'a que 8 gigas, lundi, on regarde le nouveau fichier qui fait tenir Qwen 27B en entier dedans. »

**Vérifié :** « en entier » est tenu par `../qwen-27b-8go/sources.md` F1-F2 : un fichier de 7,63 Go, tout sur la carte, 3,2 → 18 tok/s. ⚠️ C'est une seule mesure, sur une 1080 Ti bridée à 8 Go. La question laissée ouverte en fin de `script.md` est donc réglée.

**Amélioration :** le titre de lundi est « plus rapide, mais à quel prix ? ». Ouvre cette boucle (F4 de ce projet : la qualité résiste mal à la compression selon la tâche) :

```
Et si ta carte n'a que 8 gigas, lundi, on regarde le nouveau fichier qui fait tenir Qwen 27B en entier dedans,
et ce qu'il te coûte en qualité.
```

#### A10. Varier les ouvertures de paragraphe

5 paragraphes s'ouvrent par « Sauf que » (l. 25, 41, 56, 80, 116), et deux questions s'ouvrent par « Tu te rappelles » (l. 93, 101). Deux changements suffisent :
- l. 80 : `Le hic, c'est que son dernier moteur ne marche que sur les cartes RTX 50, sous Linux,`
- l. 101 : `Et la 4080 qui montait à 45 avec le petit fichier ?`

#### A11. Nombres en chiffres (règle du téléprompteur)

Ces trois-là sont des quantités, donc en chiffres :
- l. 56 : `Sauf que ces 2 gains ne s'additionnent pas.`
- l. 60 : `Bon, rien qu'avec ces 2 réglages, ton modèle peut écrire jusqu'à 2 fois plus vite, sur la carte que tu as déjà.`
- l. 105 : `2 gestes`

« Un tiers » reste en lettres.

#### A12. Une ou deux réactions de plus, sans anecdote

Le corps aligne bien les faits, mais il réagit peu : « Donc même la Radeon double presque » et « La falaise, encore » sont les seules vraies réactions. Deux endroits où une réaction courte suffit, sans rien inventer :
- après la l. 51 : `Pour 8 couches sur 48.`
- après la l. 71 : `Oui : une mise à jour qui te fait perdre un quart de ta vitesse.` (M31, −25 %)

#### A13. « Paramètre » contre « réglage » (l. 1)

C'est ta phrase, donc garde-la si tu y tiens. Sache seulement que dans ta niche, « paramètre » veut d'abord dire un poids du modèle (« 27 milliards de paramètres »), et que tout le reste du script dit « réglage ». La variante `tu allumes un seul réglage` est cohérente avec le plan et la l. 13.

#### A14. Les versions « du 15 novembre » (l. 74)

La vidéo sort le 19. llama.cpp publie un build nocturne chaque jour (M33). Relis M33-M36 le 19 au matin, ou garde la date sur la carte à l'écran, comme prévu. La voix dit déjà « du 15 novembre » : elle reste juste.

#### A15. Hors voix : l'en-tête de `script.md` est périmé

`script.md` annonce ≈ 1 570 mots, « donc 11 » et 1,9 liaison. Le comptage donne 1 529 mots, « donc » 10, et 1,70 sur la liste courte (2,16 avec « par contre »). Le tableau « Chiffre → source » garde aussi deux lignes retirées de la voix : « Le moteur qui peut coûter jusqu'à 30 % (0 bis) » et « celle d'après la mienne ». À corriger dans la prochaine version (ce grill ne modifie pas `script.md`).

## Liaisons et tics (V3)

Même méthode que `grill-v1.md` : voix seule.

| | Mots | Durée à 145 | Durée à 233 | Hook jusqu'à la question | Liste courte | + par contre, alors, justement | Large |
|---|---|---|---|---|---|---|---|
| V2 | 1 533 | 10 min 34 | ≈ 6 min 35 | 67 mots | 1,63 | 2,09 | 2,67 |
| **V3** | **1 529** | **10 min 33** | **≈ 6 min 34** | **71 mots ≈ 29 s** | **1,70** (26) | **2,16** (33) | **2,75** (42) |

- Détail : « donc » 10, « du coup » 6, « en fait » 4, « sauf que » 4 (plus « sauf qu'il » 1), « voilà » 1, « bref » 1, « par contre » 4, « alors » 2, « justement » 1.
- Dans les 30 premières secondes, il n'y a qu'un « Du coup » sur 71 mots (1,4) : B1 garde ce niveau.
- Les « pas A, B » :
  - l. 4 et l. 10 : fausses oppositions, réglées par B1 ;
  - l. 119 : vraie distinction, tenue par M5 et M23, à garder ;
  - l. 127 : morale, réglée par A4.
- Pas de faux suspens. « Maintenant, le piège. » et « Et ça peut être bien pire. » annoncent bien un fait, qui suit tout de suite : on peut les garder.

## Ce qu'il faut garder

- > « Même fichier, même carte, rien acheté. » : 6 mots qui font tout le travail de la miniature.
- > « Sauf que 5 de ces 6 mesures viennent du même tableau en ligne… la plus solide, c'est celle du début » : c'est ce qui rend le « ×2 » crédible.
- > « Le MTP double toujours, mais tout descend. » et « La falaise, encore. » : des réactions courtes, justes, mémorables.
- > « Il ne t'évite pas le tiers de vitesse en moins, puisque la mesure du début avait déjà le cache compressé. Par contre, il peut t'éviter la falaise. » : une nuance que presque personne ne fait.
- > « Si cette vidéo t'a évité un mauvais achat, abonne-toi. » : elle arrive juste après le service rendu (4:52), comme le veut la règle du 12/11.
- La fin, « Alors, ta carte, bridée ? Si le MTP est éteint, ou si ton fichier déborde, oui. » : la question de la miniature reçoit une réponse nette.

## Plan d'action

1. Colle B1 et la variante A (ou B) de B2 dans les l. 1-13 du téléprompteur, avec `Le réglage qui double, c'est le MTP…` à la l. 13.
2. Remplace la l. 38 (B3) ; ou ouvre LM Studio 0.4.28 et écris ce que tu vois.
3. Fais les coupes de souffle de B4.
4. Si tu as 15 minutes : A1, A2, A3, A4, A5, dans cet ordre.
5. Chronomètre les 30 premières secondes à voix haute : la question doit tomber avant 0:31, et « publiées » avant 0:20.

## Erreurs de faits

Vérifiés ✅, sans remarque : M1 (53 → 101), M3 (17,6 → 40 ; ×1,8 sur du texte), M4 (15 → presque 29), M5 (29 → 64, 5 fois, cache en 4 bits), M1-M6 (5 modèles de cartes, ×1,9 à 2,3, 5 sur 6 du même tableau), M7 (la lecture du prompt, sans chiffre), M8, M30b (0.4.22), M9 (1 à 2,5 Go), M12 (15 Go → 20, 11,5 Go → 45), M13 (8 couches sur 48, 43 → 12,5), M17 (+12 %), M17/M19 (32 et 64 Go de RAM), M22 (29 → 20, 64 → 39, un tiers), M23 (45 → moins de 10 à 128 000), M26 (−6,6 %, −1,8 %, 82 %, 8 %), M27 (−35 % en 4 bits à 64 000), M28 (32 000 → 128 000+), M29 (−10 %, 76,8 contre 77), M30 (jusqu'à −30 %), M31 (−25 %), M32 (0.2.14, environ −10 % sur 5070 Ti), M38 (8 → 83 sur une 5060 Ti, RTX 50, Linux).

| Ligne | Ce que dit la voix | Ce que dit `sources.md` | Id | Gravité | Correction |
|---|---|---|---|---|---|
| 8 | Le réglage démystifié « ne la change pas » (la vitesse) | 8 bits : −6,6 % ; 4 bits : −1,8 % (8K) ; 4 bits à 64K : **−35,3 %** | M26, M27 | ❌ faux, et en contradiction avec la l. 113 | B2 |
| 8 | « qu'on croit fait pour la vitesse » | aucune source pour cette croyance (§ G : pas de « tout le monde conseille ») | — | ❌ sans source | B2 |
| 38 | « personne n'a vérifié s'il l'allume tout seul » | « **Non vérifié** : que le MTP soit éteint ou allumé par défaut » (par nous) | M30b | ❌ plus fort que la source | B3 |
| 7 (plan, via `script.md`) | « le moteur qui te permet d'y arriver », avec [M29, M30] | M29/M30 = Ollama plus lent ; c'est M8, M30b et § A (6 mesures sur llama.cpp) qui tiennent la promesse | M8, M30b | ⚠️ promesse non livrée en clair | A1 |
| 78 | « Qwen 3.8 Flash Next en entier… sur une 5060 Ti » | 125 milliards de paramètres ; fichiers de dizaines de gigas (78 Go) : le modèle déborde | M37, M19, M38 | ⚠️ trompeur à l'oreille | A2 |
| 123 | « Dans le même test », 82 % / 8 % | 81,6 % / 8,3 % viennent de M26 (5060 Ti, 7B, 8K), pas de M28, cité juste avant | M26 | ⚠️ mauvais renvoi | A3 |
| 125 | « au moins 3 des 6 mesures du début étaient en 4 bits », juste après le 8 % | KV q4_0 chez M1, M4, M5 ✅ ; mais le 8 % vaut pour un modèle de 7B, et la qualité des M1-M6 n'est mesurée nulle part | M1, M4, M5, M26 | ⚠️ extrapolation suggérée | A3 |
| 29 | Le « 2 fois » = moyenne de code, texte et commandes | Vrai pour le tableau (M1-M4, M6) ; M5, la mesure du hook, vient d'un banc sur du code à 4K | § A, M5 | ⚠️ condition mal rattachée | A6 |
| 32 | « une mesure ne donne que 1,5 fois » | ×1,47 (Qwen 3.6, avril) et ×1,28 (repris de B, non rouvert) | M10, M11 | ⚠️ mineur | A8 |
| 87 | 29 % « avec le cache d'experts arrivé dans llama.cpp en octobre » | 14,95 → 19,26 (+28,8 %) mesuré sur un commit de fork du 05/10, qui porte la PR fusionnée le 07/10 ; une seule mesure | M18, M19 | ⚠️ acceptable : « une seule mesure » est dit | — |
| 141 | « fait tenir Qwen 27B en entier » dans 8 gigas | 7,63 Go, tout sur la carte, 18 tok/s ; **une** mesure, sur une 1080 Ti bridée à 8 Go | F1, F2 de `../qwen-27b-8go/sources.md` | ⚠️ tenu, une seule mesure | A9 (facultatif) |
| 74 | « Celles du 15 novembre sont à l'écran » | Versions relevées le 15/11 ; la vidéo sort le 19 | M33-M36 | ⚠️ à relire le 19 | A14 |
