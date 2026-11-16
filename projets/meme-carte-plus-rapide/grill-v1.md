# Grill de la V1 : « Même carte, 2 fois plus rapide » (15/11/2026)

> Critiqué : [`script-v1.md`](script-v1.md) (intact). Corrigé dans la V2 : [`script.md`](script.md), [`teleprompteur.md`](teleprompteur.md) / [`.txt`](teleprompteur.txt). Seule source de chiffres : [`sources.md`](sources.md) (M1…M38, F, tableau G). Méthode : skill `youtube-script-grill`, mode B, **variante storytelling** (test des 30 secondes, axe 10) ; règles de `.claude/rules/script.md`. Débit de référence : 145 mots/min. Voix de l'auteur relue dans `../strata-test/strata-test.fr.srt` ; vidéo du 09/11 relue dans `../claude-ou-mon-pc-1/script.md` ; concurrent : [`recherche/A-nathan.md`](recherche/A-nathan.md).

## Verdict

**V1 : 6,5/10. V2 estimée : 8/10** (8,5 avec tes crochets remplis et le défaut de LM Studio vérifié).

La V1 est **honnête et bien sourcée** : chaque chiffre a son identifiant, le « ×2 » est donné avec ses conditions, la vidéo Strata n'est jamais un avant, aucun nom de chaîne. Le hook est court et raccord avec la miniature. Mais elle a quatre défauts sérieux :
- **la section 6, celle du titre, se contredit** : un « tout le monde conseille » sans source, puis un réglage qui « ne sert à rien pour la vitesse » et qui « t'évite le piège » ;
- **trois chiffres sont collés à côté de choses qu'ils ne disent pas** : le « 10 à 30 % » qui mêle une perte et un gain, le « près de 70 » de lundi posé à côté de gains de llama.cpp, et le −35 % sans « en 4 bits » ;
- **le 53 → 101 de la 5080 était déjà le hook de ta vidéo du 09/11** : redit comme une découverte, il sonne réchauffé pour tes abonnés ;
- **la vidéo française est placée dans la mauvaise section**, celle où « tout tient », alors que son cas est un modèle qui déborde.

## Test des 15 et des 30 premières secondes (V1)

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Une 5060 Ti de 16 gigas. Même modèle, même fichier : 26 tokens par seconde. » | 🟠 Raccord avec la miniature, mais c'est une fiche technique : aucune tension avant « On allume un seul réglage » (≈ 6 s). Et rien ne dit que la mesure est celle d'un autre. |
| 5-15 s | > « On allume un seul réglage… 59. Plus du double, sur la même carte, sans rien acheter. » | 🟠 Le meilleur moment est bien là, avec sa preuve (le bandeau). Mais **« On allume »** laisse croire que c'est toi qui mesures ; l'attribution n'arrive qu'à 0:30 (« je n'ai rien mesuré chez moi »). Pour une vidéo calculée, § H demande « mesures d'autres testeurs » dans la première minute : c'est tenu, mais le spectateur a cru 25 s que c'était ton test. |
| 15-30 s | > « Et 6 testeurs, sur 5 cartes de 16 gigas, trouvent entre 1,9 et 2,3 fois plus vite. Du coup : est-ce que ta carte est bridée, sans que tu le saches ? » | 🟢 Une seule question, en mots simples, raccord avec « TA CARTE BRIDÉE ? », vers 0:25. ⚠️ « 5 cartes » : ce sont 5 **modèles** de cartes (6 cartes). |
| Pont | > « Par contre, cette fois, je n'ai rien mesuré chez moi : ce sont leurs chiffres, et ils ont des conditions. C'est la vitesse d'écriture, sur Qwen 3.8 27B, un modèle qui tient en entier dans la carte, et ça gagne surtout sur du code. La lecture de ton prompt, elle, ralentissait dans les premiers tests de mai. » | 🟠 Honnête, mais c'est une **rafale de quatre conditions** (écriture, modèle, code, prompt) qui retarde le plan jusqu'à ≈ 0:50-1:05, alors que la règle du 11/11 le veut vers la fin des 30 s. La lecture du prompt n'a rien à faire là : elle sert dans l'explication du MTP. |

**Budget V1** : 60 mots ≈ 25 s ; question vers 0:25 ; plan de 0:50 à 1:05.
**À couper ou déplacer** : « On allume » (→ « un testeur allume ») ; la lecture du prompt (→ section 1) ; les conditions passent **après** le plan.

**Réécriture appliquée (V2, 67 mots ≈ 28 s)** :

> Sur une carte de 16 gigas, un testeur allume un seul réglage, et son IA écrit 2 fois plus vite : de 29 à 64 tokens par seconde. Même fichier, et rien acheté. Et ils sont 6 testeurs, sur 5 modèles de cartes de 16 gigas, à trouver entre 1,9 et 2,3 fois plus vite. Du coup, ta carte, elle serait pas bridée, sans que tu le saches ?

- **« un testeur » et « écrit » dès 0:03** : la miniature est tenue sans ambiguïté, et la différence avec la vidéo française s'entend tout de suite (un réglage, six testeurs).
- **M5 au lieu de M2** : c'est la seule mesure indépendante (médiane de 5). Elle devient le personnage qui revient : section 1 (« la plus solide, c'est celle du début »), section 5 (29 → 20, 64 → 39), section 6 (il avait déjà le cache compressé).
- Juste après : le plan (≈ 0:28-0:48), puis les conditions (≈ 0:48-1:00), puis « Ce réglage, c'est le MTP » : la première partie commence par la réponse.

## Tableau de bord

| Axe | V1 | V2 | En une phrase |
|---|---|---|---|
| 1. Promesse | 🟠 | 🟢 | Le « 2× » et « bridée ? » sont tenus dès 0:25 ; mais la moitié « celui qui ne sert à rien » du titre se contredit en V1 (voir problème 1). |
| 2. Alignement | 🟢 | 🟢 | « Avant d'en racheter une plus grosse, essaie ça » : le spectateur garde son argent, et toi sa confiance. |
| 3. Problème profond | 🟠 | 🟠 | « Ma carte est-elle déjà trop petite ? » : semé par « sans rien acheter », résolu par l'abonne-toi ; la V2 le referme à la fin (« ça se répare ce soir, sans rien acheter »). Reste à ta phrase de verdict de le porter. |
| 4. Public & complexité | 🟠 | 🟢 | V1 : « têtes MTP », « lecture du prompt » dans la première minute, et la RAM des machines à experts jamais dite à un public de 8-16 Go. V2 : le clavier du téléphone, le prompt dans la section 1, « leurs PC avaient 32 et 64 gigas de RAM ». |
| 5. Valeur & originalité | 🟠 | 🟢 | La checklist mesurée est un vrai angle. Mais le 53 → 101 et l'explication du MTP répètent presque mot pour mot ta vidéo du 09/11 ; la V2 en fait un renvoi (« je te disais alors : une seule mesure ; depuis, j'en ai trouvé 5 autres »). |
| 6. Structure & transformation | 🟢 | 🟢 | Du plus rentable au moins utile, puis la liste. Début : « ma carte est peut-être trop lente » ; fin : « je sais quoi régler ce soir ». |
| 7. Histoire | 🟠 | 🟠 | Une enquête sur des réglages, sans narrateur qui change (normal pour une vidéo calculée). La V2 donne un personnage récurrent : le testeur du début. |
| 8. Mais / donc | 🟠 | 🟢 | V1 : « Ensuite, le moteur » et « Maintenant, le piège » (le second passe). V2 : « Mais tout ça dépend aussi du moteur », « il reste un dernier réglage ». |
| 9. Engagement actif | 🟠 | 🟢 | V1 : aucune question au spectateur après 0:25. V2 : « À ton avis, est-ce que ça fait écrire plus vite ? Garde ta réponse. », et la question de la miniature refermée à la fin. |
| 10. Rythme, oralité & liaisons | 🟠 | 🟢 | Assez de liaisons (1,65 sur la liste courte), mais quatre « par contre », trois « attention », et trois rafales de trois chiffres (sections 1, 4, 6). |
| 11. Tics d'IA | 🟠 | 🟢 | Un homme de paille répété trois fois, deux faux suspens, une fausse opposition, deux « Alors pourquoi… ? Parce que… » de même forme. |
| S1. 30 premières secondes | 🟠 | 🟢 | Question à 0:25 ; V1 sans attribution avant 0:30 et plan à 0:50. |
| S2. Le pont | 🟠 | 🟢 | V1 : un bloc de conditions. V2 : le plan, dont la dernière ligne ouvre une deuxième boucle (« pourquoi le connaître quand même »). |
| S3. Retournements | 🟠 | 🟢 | V1 : la section 4 (50 s) n'a qu'un « Par contre » de précaution ; la section 3 finit sur une liste de versions. V2 : un « sauf que » ou une récolte toutes les 30 à 40 s. |
| S4. Planté / récolté | 🟠 | 🟢 | V1 : une seule récolte (« la falaise de tout à l'heure »). V2 : le testeur du début (×4), la falaise (×3), la 4080 (×2), « bridée ? » (×3), le 101 du 09/11. |
| S5. Personnages | 🟠 | 🟠 | Des testeurs sans nom (ta règle) ; la V2 en fait revenir un. |
| S6. La fin | 🟠 | 🟢 | V1 : elle résume puis s'arrête. V2 : elle répond à la question de la miniature (« Si le MTP est éteint, ou si ton fichier déborde, oui »). |

## La promesse du titre et de la miniature

- **Miniature « TA CARTE BRIDÉE ? » + compteur « 2× » : tenue, en V1 comme en V2.** Le « 2× » arrive avant 10 s, avec six mesures de ×1,9 à ×2,3 (M1-M6, seul gain que § H autorise). « Bridée » reste une question et reçoit une réponse vérifiable : dans llama.cpp, le MTP ne s'allume pas tout seul (M8). **Point faible restant** : pour ton public, qui a installé LM Studio avec ta vidéo du 2 nov., la réponse dépend du réglage par défaut de LM Studio, **non vérifié** (M30b). C'est ton crochet de la section 1 : voir la question 1.
- **Titre « 16 Go de VRAM : le réglage qui fait écrire 2 fois plus vite, et celui qui ne sert à rien » : tenu à moitié en V1.** La V1 dit « ne sert à rien pour la vitesse », puis « c'est ça qui t'évite le piège de tout à l'heure », c'est-à-dire un effet sur la vitesse. La V2 tient les deux bouts : pour la vitesse, rien (M26, M27) ; pour la place, beaucoup (M28), ce qui **peut** éviter la falaise (CALCUL), sans éviter le tiers en moins (M5 l'avait déjà). Le titre seul laisse croire que le réglage ne sert à rien du tout : question 2.
- **Ne prends pas le titre de repli** (« Ton IA locale peut écrire 2 fois plus vite, sans changer de carte ») ni le nom de travail en titre public : à côté de « Mon IA locale va 11 fois plus vite (même PC) », ce sont la même formule et le même découpage, avec un chiffre cinq fois plus petit. Dans les suggestions, tu aurais l'air d'en être la version faible.

## En quoi la vidéo se distingue de celle du 14/11 (M38)

| | Vidéo française du 14/11 | Ta V1 | Ta V2 |
|---|---|---|---|
| Forme | Récit de 3 mois sur une machine, un chiffre toutes les 10-15 s | Checklist mesurée | Checklist mesurée, avec un testeur qui revient |
| Modèle | Flash Next en entier, qui déborde en RAM | Qwen 3.8 27B qui tient dans la carte | Pareil, et le cas qui déborde en section 4 |
| Preuve | Ses propres chiffres, sans versions ni réglages exacts | 6 mesures publiées, datées, versions du 15/11 | Pareil, et l'indépendance des mesures dite (5 sur 6 du même tableau) |
| Lecture / écriture | Il donne les deux (83 et 2 200), sans longueur de prompt, ni contexte, ni nombre d'essais (A-nathan § 1) | Séparées, avec les conditions | Séparées, dès 0:03 (« écrit ») |
| Contexte, cache KV | Non mesurés | Mesurés (M22-M28) | Pareil |

**Ce qui la distingue** : un modèle qui tient au lieu d'un modèle qui déborde, six testeurs au lieu d'une machine, et la section 6, qu'il n'a pas.
**Ce qui lui ressemble encore** :
- **la même carte (5060 Ti) et la même forme avant/après chiffrée dans le hook**. C'est inévitable : c'est la carte de 16 Go la plus courante, et le compteur est ta miniature. La V2 compense en disant « un testeur » et « 6 testeurs » avant 15 s ;
- **la même explication du MTP** (son explication de 2:33-2:40, résumée dans A-nathan : « deviner plusieurs tokens d'avance et les vérifier d'un coup » ; et la tienne du 09/11). La V2 ajoute l'image du clavier du téléphone ;
- **son « la vitesse double » avec le MTP (2:42) n'est pas un ×2 du MTP seul** : il change de moteur au même moment (correction de `sources.md` § E). Ne le cite pas comme une confirmation.

**Sa place dans la V1 est fausse** :
> « Et justement, un créateur français vient de passer de 8 à 83 tokens par seconde sur une 5060 Ti, surtout en changeant de moteur. »

Cette phrase vient juste après « Quand tout tient dans la carte, Ollama a été mesuré 10 % plus lent ». Le spectateur comprend que changer de moteur, sur un modèle qui tient, peut faire ×10. Or son modèle est Flash Next **en entier, qui déborde** (A-nathan § 1). La V2 la déplace en section 4, « Et si ton modèle est trop gros pour la carte, comme celui de lundi ? », où elle illustre le bon cas.

## Le grill, du plus grave au moins grave

### 1. La section 6 promet un réglage inutile, puis lui trouve une utilité, avec un « tout le monde » sans source
> « Et à la fin, le réglage que tout le monde conseille, alors qu'il ne sert à rien pour la vitesse. »
> « Et c'est là qu'arrive le réglage que tout le monde conseille »
> « Alors pourquoi tout le monde le conseille ? Parce qu'en fait, il donne de la place. »
> « Et voilà le retournement : il ne va pas plus vite, mais il fait tenir la conversation dans la carte, et c'est ça qui t'évite le piège de tout à l'heure. »

**Pourquoi ça coince** :
- **« Tout le monde conseille »** : rien dans `sources.md` ne montre qui le conseille, ni pour quoi. C'est un homme de paille (`anti-ia.md` § 1), répété trois fois.
- **« Le piège de tout à l'heure »**, c'est le tiers de vitesse en moins de la section 5 (M22). Or ce testeur **avait déjà le cache en 4 bits** (M5 : « KV q4_0 »). Le cache compressé n'évite donc pas ce piège-là. Il peut éviter **la falaise** de la 4080 (M23), et seulement par déduction (G : « c'est ça qui évite de ralentir »).
- **« Et c'est là qu'arrive »** et **« Et voilà le retournement »** sont des faux suspens : ils annoncent le moment fort au lieu de le rendre fort.
- La tension avec la fin de la section n'est pas dite : **au moins 3 des 6 testeurs du « ×2 » étaient en 4 bits** (M1, M4, M5), et la V1 conclut « reste en 8 bits ».

**Correction (faite)** : la section s'ouvre sur une vraie question (« À ton avis, est-ce que ça fait écrire plus vite ? Garde ta réponse. »). Puis la mesure, « Donc pour la vitesse, il ne sert à rien », « Sauf qu'il fait de la place », « il peut t'éviter la falaise » (CALCUL, sans l'attribuer à la 4080 : M23 ne dit pas si son banc avait déjà le cache compressé), le tiers qui reste, les 3 testeurs en 4 bits, et « si tout tient en 8 bits chez toi, reste en 8 bits ».

### 2. Le « près de 70 » de lundi, juste avant les gains de llama.cpp : un avant/après déguisé
> « Lundi, avec Strata, j'ai mesuré près de 70 tokens par seconde, et tu as vu ma RAM se remplir et le disque se mettre à lire. […] Dans llama.cpp, sur une 3060 de 12 gigas, bien régler les experts a fait gagner 12 %. »

**Pourquoi ça coince** : la décision est claire, tes chiffres Strata ne sont jamais un avant. Ici, le spectateur entend « 70 », puis « +12 %, +29 %, +34 % », et fait le calcul tout seul. Pire, s'il va voir les sources, la même famille de modèle tourne à 15-19 tok/s dans llama.cpp sur une 5060 Ti (M19). Il en conclura « Strata est 4 fois plus rapide que llama.cpp ». Or c'est une paire que personne n'a mesurée : autre carte, autre moteur, et ton Coder IQ1_M n'a que la moitié des experts. Le visuel « la capture du moniteur de Strata de lundi » montrait en plus le compteur.

**Correction (faite)** : la V2 ne garde de lundi que ce qui pose le problème (« ma RAM pleine, et le disque qui se met à lire », F, srt 4:36-4:51). Le visuel est recadré sur la RAM et le disque, **sans le compteur**.

### 3. « Deux réglages qui rapportent de 10 à 30 % » : une perte et un gain dans le même sac
> « deux réglages qui rapportent de 10 à 30 % [M17, M19, M29, M30] »

**Pourquoi ça coince** : M29 et M30 disent qu'**Ollama est 10 à 30 % plus lent** ; passer à llama.cpp rapporte en fait de +11 % à +41 % (M30 : ×1,41). Et les experts montent à **+34 %** dans la section 4 (3090, M17), au-dessus de la fourchette annoncée. `sources.md` § C réserve d'ailleurs le « 10 à 30 % » aux cartes de **12 à 16 Go**.
**Correction (faite)** : dans le plan, « le moteur qui peut te coûter jusqu'à 30 % » (M30). Les experts restent dans la vidéo, avec deux mesures (12 et 16 Go) ; la 3090 de 24 Go sort.

### 4. Le 53 → 101 de la 5080, redit comme une nouveauté
> « Et ça se voit sur les cinq modèles de cartes. Chez un testeur, sur une 5080, on passe de 53 à 101 tokens par seconde. »
> « En fait, le modèle devine plusieurs tokens d'avance, puis il les vérifie tous d'un coup. »

**Pourquoi ça coince** : c'était le hook de ta vidéo publiée du 09/11 (« Un vrai modèle de 27 milliards de paramètres, à 101 tokens par seconde », `../claude-ou-mon-pc-1/16-go-de-vram.fr.srt`, 0:04-0:08), avec la même explication et la même réserve (« Le modèle devine plusieurs mots à l'avance, et la carte les vérifie d'un seul coup. Résultat : 101. Par contre, c'est une seule mesure », 3:56-4:11). Vérifié dans le .srt de la vidéo publiée, pas seulement dans son script. Tes abonnés l'ont déjà entendu. C'est aussi une occasion ratée : cette vidéo est **la suite** de celle-là.
**Correction (faite)** :
> « Et le 101 tokens par seconde de cette vidéo-là, c'était déjà lui : sur une 5080, 53 sans le MTP, 101 avec. Je te disais alors : une seule mesure. Depuis, j'en ai trouvé 5 autres. »

L'explication garde son principe, avec une image neuve : les suggestions du clavier du téléphone. Cette image est de moi : garde-la seulement si elle te ressemble.

### 5. Le hook ne dit pas que la mesure est celle d'un autre
> « On allume un seul réglage… 59. »

**Pourquoi ça coince** : « On » te met au centre d'un test que tu n'as pas fait. Pendant 25 s, le spectateur croit à ton test ; à 0:30, « je n'ai rien mesuré chez moi » sonne comme une marche arrière. Pour une vidéo calculée, c'est la confiance du reste de la vidéo qui se joue là.
**Correction (faite)** : « un testeur allume un seul réglage, et son IA écrit 2 fois plus vite ».

### 6. La vidéo française dans la mauvaise section, et un « ni ses réglages » trop fort
> « Sauf que son moteur ne marche que sur les cartes RTX 50, sous Linux, et il ne donne ni ses versions ni ses réglages. En gros, c'est le résultat d'une machine, pas une promesse pour la tienne. »

**Pourquoi ça coince** :
- La place : voir plus haut, son cas est un modèle qui déborde.
- **« ni ses réglages »** : il en donne quelques-uns (RAM verrouillée, 9 couches en VRAM, le fichier UD-IQ2_XS : A-nathan, lignes 5 et 13). Ce qui manque, ce sont les options exactes, les versions et le nombre d'essais (M38).
- **« c'est le résultat d'une machine, pas une promesse pour la tienne »** : un « c'est A, pas B ».

**Correction (faite)** : section 4, « ni ses versions ni ses réglages exacts », puis « Donc ça a marché sur sa machine, et je ne peux pas te le promettre sur la tienne. »

### 7. La section 4 parle à des PC que ton public n'a pas
> « Dans llama.cpp, sur une 3060 de 12 gigas, bien régler les experts a fait gagner 12 %. Sur une 5060 Ti de 16, avec le nouveau cache d'experts de llama.cpp, 29 %. Et sur une 3090 de 24, 34 %. »

**Pourquoi ça coince** :
- C'est une rafale de trois chiffres sans réaction.
- Elle tait que ces machines avaient **31 et 62 Go de RAM** pour un fichier de 78 Go (M17, M19), alors que ton public a souvent 16 Go.
- Elle ne dit pas quel réglage toucher.
- Le 29 % vient d'un **commit de fork** qui porte la PR (M19), pas de llama.cpp officiel.

**Correction (faite)** : le réglage est nommé à l'écran (`--n-cpu-moe`, `--moe-cache-mib`), avec la règle « en garder sur la carte autant que possible, juste avant que ça plante » (M17 : 29 le meilleur, 26 = OOM ; CALCUL). Il reste deux chiffres ; « le cache d'experts arrivé dans llama.cpp en octobre » (M18, M19) ; « leurs PC avaient 32 et 64 gigas de RAM ».

### 8. Les rafales de chiffres et les tics de liaison
> « Chez un testeur, sur une 5080, on passe de 53 à 101 tokens par seconde. Sur une 4060 Ti, de 17,6 à 40. Même sur une Radeon, la RX 9060 XT, de 15 à presque 29. »
> « Sur une 5060 Ti, en 8 bits, l'écriture est 6,6 % plus lente. En 4 bits, 1,8 % plus lente. Et sur une machine de Nvidia faite pour l'IA, à 64 000 tokens, l'écriture perd même 35 %. »

**Pourquoi ça coince** : trois chiffres d'affilée sans réaction (`storytelling.md` § 3), trois fois dans la vidéo (sections 1, 4, 6).
- **« Par contre »** revient 4 fois et **« attention »** 3 fois : le script s'excuse en permanence.
- **« En effet, la mémoire de la conversation prend de la place »** : « en effet » ne confirme ici aucun soupçon du spectateur.
- **« Pour info, au 15 novembre, on en est à… »** remplit sans rien apporter : les versions sont mieux à l'écran.

**Correction (faite)** :
- une réaction après chaque série (« Donc même la Radeon double presque. ») ;
- section 4 à deux chiffres ;
- « par contre » 3, « attention » 1 ;
- « En fait, la mémoire de la conversation se range aussi dans la carte » ;
- « Celles du 15 novembre sont à l'écran ».

### 9. La section 5 donne un remède qui ne soigne qu'à moitié
> « Bref, la solution est toute bête : une nouvelle conversation dès que tu changes de sujet. »

**Pourquoi ça coince** : c'est un conseil sans identifiant (donc CALCUL), et il ne règle que la baisse progressive (M22). La falaise de la 4080 (M23) vient du cache du contexte qui « pousse le modèle hors de la carte » : la taille de conversation **réglée** compte autant que la conversation réellement tapée. `sources.md` ne dit pas si Glukhov mesure à contexte rempli ou à contexte réglé : à garder prudent.
**Correction (faite)** : « deux gestes tout bêtes : une nouvelle conversation dès que tu changes de sujet, et une taille de conversation réglée au plus juste dans ton moteur [CALCUL] ». S'y ajoutent deux récoltes : « Tu te rappelles le testeur du début, à 29 tokens par seconde ? » (29 → 20, puis 64 → 39 avec le MTP, ×1,98 à 64K : « Le MTP double toujours, mais tout descend ») et « Tu te rappelles la 4080 qui montait à 45 avec le petit fichier ? ».

### 10. La fin résume et s'arrête
> « Donc, dans l'ordre : […] Et note ta version. […] Et si 16 gigas ne te suffisent plus, lundi prochain, on cherche 32 gigas de VRAM au moins cher. Allez, salut ! »

**Pourquoi ça coince** : la question de la miniature (« bridée ? ») n'est jamais refermée en toutes lettres. Et la checklist met deux « ×2 » l'un sous l'autre : le spectateur va les multiplier, ce que G interdit.
**Correction (faite)** : « Alors, ta carte, bridée ? Si le MTP est éteint, ou si ton fichier déborde, oui. Et ça se répare ce soir, sans rien acheter. » ; « ×2 ET ×2 ≠ ×4 » affiché sous la checklist et à la fin de la section 2.

## Chaque chiffre de la V1, revérifié contre `sources.md`

✅ = la source le dit ainsi · ⚠️ = juste, mais il manque une condition, ou la mesure est unique · ❌ = la source ne le permet pas.

| Section | Ce que dit la V1 | Source | Statut | Ce qu'en fait la V2 |
|---|---|---|---|---|
| 0 | 26 → 59 tok/s, 5060 Ti | M2 : 26,3 → 59,5 | ✅ ⚠️ dit « On », sans attribution | Remplacé par M5 (29 → 64), « un testeur » |
| 0 | « Plus du double » | M2 ×2,26 | ✅ | « 2 fois » (M5 ×2,19) |
| 0 | 6 testeurs, « 5 cartes », 1,9 à 2,3 | M1-M6 : 6 auteurs, **5 modèles** de cartes | ⚠️ | « 5 modèles de cartes » |
| 0 bis | Écriture, modèle qui tient, surtout du code | M1-M6, M3, § H | ✅ | Gardé, après le plan |
| 0 bis | Lecture du prompt qui ralentissait en mai | M7 (deux machines à deux cartes, Qwen3.6) | ✅ ⚠️ bien sans chiffre | Déplacé en section 1 |
| 0 bis | « deux réglages qui rapportent de 10 à 30 % » | M29/M30 = Ollama **plus lent** de 10-30 % ; M17 +34 % sur 24 Go | ❌ (mélange une perte et un gain ; la fourchette exclut le 34 %) | « le moteur qui peut te coûter jusqu'à 30 % » |
| 0 bis, 5 | Un tiers de ta vitesse | M22 −32 % | ✅ | Gardé |
| 0 bis, 6 | « le réglage que tout le monde conseille » | aucune | ❌ | Retiré |
| 1 | 53 → 101, 5080 | M1 : 53,4 → 101,3 | ✅ ⚠️ déjà dit le 09/11 | Renvoi à la vidéo du 09/11 |
| 1 | 17,6 → 40, 4060 Ti | M3 | ✅ | Gardé |
| 1 | 15 → presque 29, RX 9060 XT | M4 : 15,2 → 28,7 | ✅ | Gardé, + réaction |
| 1 | 5 des 6 mesures du même tableau, même script | § A, conclusion | ✅ | Gardé |
| 1 | 29 → 64, testeur à part | M5 : 29,18 → 63,89 | ✅ | Devient le hook ; « 5 fois » (médiane de 5) |
| 1 | Moyenne code + texte + commandes, réflexion coupée | § A, conditions | ✅ ⚠️ vaut pour le tableau, M5 est un banc de code | Gardé |
| 1 | ×1,8 sur du texte | M3 : 17,6 → 32,3 | ✅ | Gardé |
| 1 | « surtout sur du code », sans chiffre | M3 : 17,6 → 49 (×2,78) | ✅ (bien de ne pas dire « presque 3 fois » : § H) | Gardé |
| 1 | ×1,5 « sur les gros modèles à experts » | M10/M11 : ×1,47, 35B-A3B, Qwen3.6, avril | ⚠️ « gros » : c'est un 35B | « sur un modèle à experts » |
| 1 | MTP non automatique, fichier avec les têtes MTP | M8 | ✅ | « le module, un petit bout de modèle en plus » |
| 1 | LM Studio 0.4.22 | M30b | ✅ ; défaut **non vérifié** | Crochet gardé |
| 2 | 1 à 2,5 Go de VRAM en plus | M9 : +1,16 ; +1,58 ; +2,49 | ✅ | Gardé |
| 2 | 4080 : 15 Go, 20 → 11,5 Go, 45 | M12 : 20,5 → 45,3, **Qwen3.5**-27B | ✅ ⚠️ ce n'est pas le Qwen 3.8 du hook | « un Qwen de 27 milliards plus ancien » |
| 2 | 8 couches sur 48 dehors, 43 → 12,5 | M13 (débordement forcé) | ✅ | Gardé |
| 2 | « ce qui sort de la carte est calculé beaucoup plus lentement, et tout le reste attend » | aucune (M16 : « spilling … collapses throughput ») | ⚠️ explication sans id | [M16, CALCUL] |
| 2 | Qualité perdue non mesurée | § B, conclusion | ✅ ⚠️ « aucune de ces pages » | « aucun de ces testeurs » |
| 2 | Les gains ne s'additionnent pas | M9, CALCUL | ✅ | Gardé, + « ×2 ET ×2 ≠ ×4 » à l'écran |
| 2 | « jusqu'à 2 fois plus vite », ta carte actuelle | M1-M6 | ✅ (conditions dites avant) | « ton modèle peut écrire jusqu'à 2 fois plus vite » |
| 3 | Ollama 10 % plus lent, 5060 Ti | M29 (un testeur ; petit modèle et mélange D/P **non relus**) | ⚠️ | « un testeur » ; le modèle, non relu, n'est pas dit |
| 3 | Ollama jusqu'à 30 % plus lent, 3090 | M30 (×1,41 → −29 %) | ✅ | Gardé |
| 3 | LM Studio 76,8 contre 77 | M29 | ⚠️ une mesure | Gardé, « était presque à égalité » |
| 3 | 8 → 83 tok/s, 5060 Ti, moteur | M38 (7,9 → 83) | ✅ ⚠️ mauvaise section | Section 4 |
| 3 | RTX 50, Linux, « ni ses versions ni ses réglages » | M38 | ⚠️ il donne quelques réglages | « ni ses réglages exacts » |
| 3 | −25 % après une mise à jour, 5080, Strata | M31 : 117 → 86,1 ; 111,2 → 84,9 ; 0.1.54 → 0.1.56 | ✅ ⚠️ « d'une version à l'autre » | « à une version plus récente » |
| 3 | 0.2.14 du 15/11, écriture −10 % sur 5070 Ti, projet | M32 : 17,5 contre 19,4 ; 21,8 contre 23,8 | ✅ | Gardé, + « celle d'après la mienne » (M36) |
| 3 | llama.cpp 1.0, LM Studio 0.4.28, Ollama 0.40.16 | M33, M35, M34 | ✅ | À l'écran ; la voix dit seulement qu'elles y sont |
| 4 | Près de 70 tok/s, RAM, disque (lundi) | F | ✅ mais ⚠️ mis à côté de gains de llama.cpp | RAM et disque seulement |
| 4 | +12 % sur 3060 12 Go | M17 (8,66 → 9,64 ; 10,92 → 12,22) | ✅ ⚠️ une mesure | Gardé |
| 4 | +29 % sur 5060 Ti, « nouveau cache d'experts de llama.cpp » | M19 : 14,95 → 19,26, commit d'un fork | ⚠️ | « le cache d'experts arrivé dans llama.cpp en octobre » (M18, M19) |
| 4 | +34 % sur 3090 24 Go | M17 | ✅ mais hors fourchette annoncée et hors public | Retiré |
| 5 | 4 000 → 64 000 tokens, 29 → 20 | M22 : 29,18 → 19,77 | ✅ | Gardé, + 64 → 39 avec MTP (M22) |
| 5 | 4080 : 45 → moins de 10 à 128 000 | M23 : 45,3 → 9,6 | ✅ | Gardé, présenté comme la 4080 de la section 2 (même fichier de 11,5 Go) |
| 5 | « une nouvelle conversation dès que tu changes de sujet » | aucune | ⚠️ conseil sans id | [CALCUL], + taille de conversation réglée |
| 6 | 8 bits −6,6 %, 4 bits −1,8 %, 5060 Ti | M26 : 81,8 · 76,4 · 80,3 (**Qwen2.5-Coder-7B**, 8K) | ✅ ⚠️ petit modèle non dit | « avec un petit modèle de 7 milliards » |
| 6 | « l'écriture perd même 35 % » à 64 000 tokens, machine Nvidia | M27 : **f16 → q4_0**, DGX Spark | ⚠️ « en 4 bits » manquant : on croit à du 8 bits | « en 4 bits » |
| 6 | 32 000 → plus de 128 000 tokens | M28 | ✅ | Gardé |
| 6 | « c'est ça qui t'évite le piège de tout à l'heure » | M5 avait déjà KV q4_0 ; G : « évite de ralentir » | ❌ pour le tiers ; ⚠️ pour la falaise (CALCUL) | « il fait tenir beaucoup plus de conversation dans la carte » ; « il peut t'éviter la falaise », pas le tiers |
| 6 | Ressemblance 82 % / 8 % | M26 : 81,6 % / 8,3 % | ✅ | Gardé, « dans le même test » |
| 7 | Checklist (« FICHIER QUI TIENT · ≥ ×2 », « EXPERTS · +10 à 30 % ») | M12 ; M17, M19 | ✅ ⚠️ deux « ×2 » empilés | « +12 à +29 % » ; « ×2 ET ×2 ≠ ×4 » |
| 7 | 32 Go de VRAM, lundi 23/11 | `calendrier.md` | ✅ | « lundi » |

**Ajouts de la V2, vérifiés de la même façon** :
- 64 → 39 à 64K avec le MTP, et « le MTP double toujours » : M22, M5 (×1,98) ✅.
- Le testeur du début avait déjà le cache compressé : M5 (KV q4_0) ✅.
- Au moins 3 des 6 testeurs en 4 bits : M1, M4, M5 ✅ (non précisé pour M2, M3, M6, d'où « au moins »).
- Leurs PC avaient 32 et 64 gigas de RAM : M17 (31 Go), M19 (62 Go) ✅ (arrondi).
- « juste avant que ça plante » : M17 (-ncmoe 29 contre 26 = OOM) + CALCUL ⚠️.
- Le 101 de la vidéo du 09/11 et « une seule mesure » : `../claude-ou-mon-pc-1/16-go-de-vram.fr.srt` (la vidéo publiée), 0:04-0:08 et 3:56-4:11 ✅. Elle ne dit pas « 5080 » dans le hook : la V2 place « sur une 5080 » dans la phrase de M1, pas dans le rappel.
- 0.2.13 dans ta vidéo, donc 0.2.14 « celle d'après la mienne » : M36 ✅.

## Liaisons, tics, rythme (même script de comptage pour V1 et V2)

Voix seule (sections 0 à 7, sans `[VISUEL]`, `[CROCHET]` ni identifiants). Liste courte de la règle : donc, du coup, en fait, sauf que, en effet, voilà, bref. Ajoutées ensuite : par contre, alors, justement. Sens large : + mais, parce que, maintenant, attention, en gros, « bon, ». (« Bon » est compté à part, car il se confond avec « bon réglage ».)

| | Mots | Durée à 145 mots/min | Hook | Liste courte | + par contre, alors, justement | Large |
|---|---|---|---|---|---|---|
| V1 | 1 390 | 9 min 35 | 60 mots ≈ 25 s | **1,65** (23) | 2,30 (32) | 3,02 (42) |
| **V2** | **1 533** | **10 min 34** | **67 mots ≈ 28 s** | **1,63** (25) | **2,09** (32) | **2,67** (41) |

Le rédacteur de la V1 annonçait 1 383 mots et 1,59 : même ordre de grandeur, découpage différent.

- **Liaisons** : la V1 n'en manquait pas, elle en avait de mauvaises. Elle comptait 4 « par contre » et 3 « attention », un « en effet » sans soupçon à confirmer, et presque aucune réaction après un chiffre. La V2 passe à « donc » 9, « du coup » 6, « sauf que » 5, « en fait » 3, « par contre » 3, « attention » 1, et ajoute des réactions (« Donc même la Radeon double presque. », « La falaise, encore. », « Le MTP double toujours, mais tout descend. »).
- **Tics d'IA de la V1** :
  - l'homme de paille « tout le monde conseille » (×3) ;
  - les faux suspens « Et c'est là qu'arrive… » et « Et voilà le retournement : » ;
  - la fausse opposition « c'est le résultat d'une machine, pas une promesse pour la tienne » ;
  - deux questions de même forme suivies de leur réponse (« Alors, pourquoi je dis « bridée » ? Parce que… », « Alors pourquoi tout le monde le conseille ? Parce qu'en fait… »). La V2 garde la première (elle referme la boucle de la miniature) et remplace la seconde par une vraie question au spectateur.

  Passe anti-IA faite sur la V2 : il reste « il ne t'évite pas le tiers de vitesse en moins, puisque… Par contre, il peut t'éviter la falaise ». C'est une vraie distinction, tenue par M5 et M23, et elle est isolée.
- **Rythme** :
  - la V2 dure une minute de plus. Ce temps va aux récoltes (sections 5 et 6), au renvoi du 09/11 et à la réponse finale ;
  - la fiche vise 10 à 12 min ;
  - la section 1 (≈ 2 min) est la plus longue : elle tient grâce à trois retournements (« Par contre, ça ne joue que sur l'écriture », « Sauf que 5 de ces 6 », « Alors, pourquoi je dis bridée ? ») ;
  - si tu dois couper, coupe d'abord la phrase sur LM Studio en section 3 (« Du coup, si tu l'as installé… ») et la deuxième phrase sur la Radeon.

## Ce qu'il faut garder

- > « Sauf que 5 de ces 6 mesures viennent du même tableau, avec le même script de test. » : personne ne fait ça en français. C'est ce qui rend le « ×2 » crédible.
- > « Et attention, ces gains ne s'additionnent pas. » : le garde-fou contre le « ×4 » que le spectateur ferait tout seul.
- > « Bon, voilà déjà de quoi faire écrire ta carte actuelle jusqu'à 2 fois plus vite. Donc avant d'en racheter une plus grosse, essaie ça. Si cette vidéo t'a évité un mauvais achat, abonne-toi. » : l'abonne-toi est juste après le service rendu, comme le veut la règle du 12/11.
- La falaise (M13), qui fait comprendre le débordement sans un mot de jargon.
- L'absence de « 3× » sur le code (M3 donne ×2,78) : la discipline de § H.
- « C'est ce que je te disais lundi : la vitesse baisse quand la conversation grandit » et « note bien ta version » : de vrais renvois, mot pour mot dans le srt, et pas de « comme promis ».
- Les crochets : aucun avis ni aucune expérience inventés à ta place.

## Plan d'action

1. **Avant la voix** : ouvre LM Studio 0.4.28 et regarde où s'allume le MTP et s'il est allumé par défaut (question 1). C'est ce qui décide si « bridée » vaut pour ton public.
2. Tranche le titre (question 2) et la mention de la vidéo française (question 3).
3. Remplis les quatre crochets dans [`teleprompteur.txt`](teleprompteur.txt) (question 5), avec tes mots.
4. Relis le hook à voix haute au chrono : 28 s à 145 mots/min. Si tu dépasses 30 s, coupe « Même fichier, et rien acheté », le bandeau le dit.
5. Après le montage : vérifie que le visuel de la section 4 ne montre **aucun compteur de vitesse** de Strata, et que « ×2 ET ×2 ≠ ×4 » est lisible sous la checklist. Puis mets à jour `README.md` et `calendrier.md`, qui disent encore « Fiche ».

## Questions pour toi

1. **Le MTP dans LM Studio 0.4.28 : allumé par défaut ou pas, et où ?** (crochet de la section 1). S'il est éteint par défaut, dis-le : c'est la meilleure preuve de « bridée » pour ceux qui ont suivi ta vidéo du 2 nov. S'il est allumé, dis-le aussi, et « bridée » ne vaut plus que pour llama.cpp et les fichiers qui débordent. Si tu ne vérifies pas, garde la phrase de repli (« Donc va vérifier qu'il est bien allumé chez toi »).
2. **Le titre : tu gardes « … et celui qui ne sert à rien » ?** La V2 le tient pour la vitesse, mais la section 6 montre que le réglage sert à autre chose (la place). Variante plus exacte : « 16 Go de VRAM : le réglage qui fait écrire 2 fois plus vite, et celui qui ne fait rien gagner ». Dans les deux cas, évite le repli « Ton IA locale peut écrire 2 fois plus vite » (trop proche de « Mon IA locale va 11 fois plus vite »).
3. **La vidéo française du 14/11 : tu la cites (section 4, 2 phrases, sans nom) ou tu la coupes ?** La citer montre que tu connais le « ×10 » et pourquoi tu ne le promets pas ; mais elle envoie aussi des curieux vers lui. Si tu coupes, enchaîne « le disque qui se met à lire » directement sur « Là, dans llama.cpp, il y a un réglage à toi ».
4. **Le cache en 4 bits des testeurs : tu gardes la phrase « au moins 3 des 6 testeurs du début étaient en 4 bits » ?** C'est honnête et ça récolte le hook, mais ça jette une petite ombre sur le « ×2 » (leur vitesse tient, leur qualité n'est pas mesurée). Et toi, dans LM Studio, tu règles le cache comment ? Si tu le sais, une phrase à toi le dirait mieux que moi.
5. **Les trois autres crochets** : ton avis après les deux premiers réglages (section 2), ta réaction au retournement du cache (section 6) et ton verdict (section 7). Remplis-les avec tes mots, ou coupe-les : le texte tient sans eux. Aucun ne doit raconter un test que tu n'as pas fait.
