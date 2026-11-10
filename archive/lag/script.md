# Lag : script final (v2)

**Titre** : *Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne*

**Durée** : environ 1 899 mots de voix off, soit 13 min 06 à ton débit mesuré sur ArtCraft (145 mots/min, pauses comprises) et 11 min 31 à 165 mots/min. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

> Critique de la V1 : [`grill-v1.md`](grill-v1.md). La V1 reste dans [`script-v1.md`](script-v1.md). Faits : [`sources.md`](sources.md), colonne « 2e vérif » et lignes 43 à 48 ajoutées au grill.

## Changements depuis la V1

- **Hook** : le « gros ping » du tireur entre dans la scène (« En face, le mec a un gros ping »), comme le demandait la 2e vérification. La question centrale devient « pourquoi le serveur donne raison au tireur ? », et non plus « un mec qui tire dans un mur » : sur son écran, il ne tirait pas dans un mur. Elle se termine au 67e mot (0:28 à 145 mots/min) au lieu du 71e, et le hook passe de 87 à 84 mots.
- **Abonnement** déplacé à la fin de la section 2 (22 %, 2:52), juste après une boucle ouverte (« les touches des autres, ton jeu ne peut pas les deviner »). En V1, il coupait l'explication de l'interpolation entre deux phrases liées.
- **Les deux déductions du rédacteur** :
  - le téléport en arrière s'appuie maintenant sur la doc de Valve (« may cause the client's view to jump erratically ») et se dit au conditionnel (« ça peut venir de là ») ;
  - « camper un angle avec un gros ping » s'appuie sur l'étude de 2024 **et** sur le calcul de Riot, où le ping de celui qui tient l'angle se retranche de son temps de réaction.
- **Attribution corrigée** : « quelques millisecondes » est de Gambetta, pas de Bernier. Bernier dit « beaucoup moins marqué dans un combat normal ».
- **Lien faux retiré** : en V1, « ce choix [donner raison au tireur] a un gagnant : celui qui surgit ». L'avantage de celui qui surgit vient du deuxième mensonge (on voit les autres dans le passé) : l'étude de 2024 le trouve même dans un jeu sans rembobinage. La transition le dit maintenant.
- **Un fait coupé revient** : la lumière « vraiment, vraiment lente » de Gambetta (section 1). Elle donne enfin une source au visuel de l'escargot, et c'est une phrase qu'on répète à un pote. La seconde d'historique de Valve reste coupée (elle aurait allongé le bloc le plus long), comme les 150 ms de Valve (Carmack et ses 300 ms font le même travail).
- **La rétention vers 60 %** : en V1, la relance (coupure musicale) était à 49 % et les 60 % tombaient au début des ticks, la section la plus technique. La relance reste juste après la question refermée (49 %), mais les 55 à 60 % portent maintenant les deux chiffres les plus forts (les dix millisecondes, puis l'étude), les ticks sont réduits à 96 mots, et le brouillard de guerre devient le « mensonge n° 4 » à 68 %.
- **Coupés pour tenir sous 1 900 mots** : le sub-tick de Counter-Strike 2 (une promesse de Valve, pas un fait mesuré), le chrono de VALORANT (50 ms → moins de 2 ms), le coût du brouillard de guerre (50 % → moins de 2 %), l'extrapolation d'un quart de seconde, le « vingt à trente fois par seconde » de la section 1 (redite de la section 3). Tous restent sourcés dans `sources.md` si tu veux en remettre un.
- **L'Afrique** : la section dit maintenant ce que le gros ping change pour toi (« le gros ping de la partie, ça risque d'être toi »), avec l'objectif de 35 ms de Riot comme repère. « Le Cap n'est pas plus près que Paris » devient « un peu plus loin » (calcul ajouté à `sources.md`).
- **Fin** : elle ne résume plus. Elle retourne la scène du début avec la phrase de Respawn (« transféré ») et récolte le « crier au cheat » du hook. La phrase « le jour où c'est toi qui sors de ton abri » quitte la section 4 pour la fin, où elle sert de chute. Le conseil du câble vise « PC ou console » : sur mobile, il ne veut rien dire.
- **Petites corrections** : « jeux Source » au lieu de « jeux de Valve » ; le Spike au lieu de « la bombe » (c'est le mot de Riot et celui des joueurs de VALORANT) ; la vidéo Uber est rappelée « si t'as vu ma vidéo » (elle aura quatre mois et demi) ; « en début de partie » pour les 60 ko/s d'Apex.

**Texte** : comment un jeu en ligne fait croire à des millions de joueurs qu'ils sont dans le même monde, au même instant, alors que chacun le voit avec un retard différent (prédiction, interpolation, compensation du lag, tick rate, brouillard de guerre).
**Sous-texte** : le jeu ment à tout le monde, en permanence, et c'est ce mensonge qui le rend jouable. Chaque joueur vit dans un passé légèrement différent, et le serveur est l'arbitre qui décide quelle version devient la vérité. Ce que tu appelles « le lag » est souvent un choix d'ingénieur : qui on favorise, le tireur ou celui qui se cache.

**Fil rouge** : trois personnages qui reviennent dans chaque animation : toi (bleu), l'autre joueur (rouge) et le serveur (une boîte avec une horloge), chacun avec sa ligne du temps. La vidéo compte les « mensonges » du jeu : le premier (il devine tes mouvements), le deuxième (il te montre les autres dans le passé), le troisième (le serveur remonte le temps), le quatrième (il cache les ennemis aux tricheurs).

**Boucles ouvertes** :
1. « Pourquoi le serveur donne raison au tireur ? » (hook, refermée dans la section 4).
2. « Tu ne vois jamais les autres là où ils sont vraiment » (pont du hook, refermée dans la section 3).
3. « Le minimum théorique depuis Abidjan » (section 1, récoltée dans la section 8 : « le gros ping de la partie, ça risque d'être toi »).
4. « Crier au cheat » et « personne n'a triché » (hook, récoltés dans la fin, avec les rôles inversés).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (HyperFrames ou Remotion). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Aucune vraie capture de jeu n'est indispensable : tout se fait en motion design, vue de dessus.

---

## 0. Hook (0:00 – 0:35)

[VISUEL : vue de dessus en motion design. Ton perso (bleu) sprinte vers un mur, un ennemi (rouge) au loin. Pas de titre, pas de logo.]

Tu sprintes, tu passes derrière le mur, t'es à l'abri. Et là, tu meurs.

[SON : un tir sec, puis le son de la mort. L'écran vire au gris.]
[VISUEL : rembobinage rapide (bande VHS). La même scène, vue de l'écran du rouge : une étiquette « ping : élevé » au-dessus de sa tête, le bleu est encore à découvert. Le rouge tire.]

En face, le mec a un gros ping : sur son écran à lui, t'étais pas encore caché. Il t'a tiré dans ton passé, et le serveur lui a donné raison.

Ton premier réflexe : crier au cheat. Sauf que personne n'a triché : c'est un choix d'ingénieur.

[VISUEL : les deux écrans côte à côte, un point d'interrogation entre les deux.]

Alors pourquoi le serveur donne raison au tireur ?

Pour le comprendre, accepte un truc : tu ne vois jamais les autres là où ils sont vraiment.

---

## 1. Le problème impossible (0:35 – 1:46)

[VISUEL : les trois personnages posés une fois pour toutes : toi (bleu), l'autre (rouge), le serveur au milieu, chacun avec une ligne du temps sous lui.]

Dans un jeu en ligne, t'as toi, l'autre, et au milieu, le serveur : l'arbitre. Ton jeu lui envoie tes touches, et lui te renvoie des nouvelles du monde. Le temps de l'aller-retour, c'est ton ping.

[VISUEL : un petit paquet part du bleu, touche le serveur, revient. Compteur « ping » qui tourne.]

Sauf que ce message, il voyage. Dans la fibre, la lumière va à peu près à deux cent mille kilomètres par seconde. Mais imagine que t'es à Abidjan et que le serveur est à Paris : même en ligne droite, l'aller-retour prend au moins une cinquantaine de millisecondes. Et c'est un minimum théorique : ton vrai ping est forcément plus haut.

[VISUEL : carte, un trait Abidjan–Paris, un point lumineux fait l'aller-retour. Texte : « ≥ 50 ms, minimum théorique ».]

[TON JEU EN LIGNE ET TON PING, MESURÉ CHEZ TOI : JEU, VILLE, OPÉRATEUR, DATE]

Gabriel Gambetta, l'auteur d'un guide sur le sujet, a une image pour ça : c'est comme jouer dans un univers où la lumière est vraiment, vraiment lente.

[VISUEL : un rayon de lumière qui avance comme un escargot entre le bleu et le rouge. Citation en petit : « the speed of light is really, really slow », Gabriel Gambetta.]

Donc chaque joueur reçoit le monde en retard, et chacun avec son retard à lui. Et pourtant, ton jeu doit réagir dès que t'appuies sur une touche, et le serveur doit décider qui a touché qui. Pour s'en sortir, les jeux mentent. Et le premier mensonge, c'est à toi qu'il est fait.

---

## 2. Premier mensonge : ton jeu devine tes mouvements (1:46 – 3:01)

[VISUEL : « Mensonge n° 1 » s'inscrit en haut de l'écran, façon tampon.]
[SON : bruit de modem 56K, deux secondes.]

En 1996, John Carmack prépare QuakeWorld, la version de Quake pour jouer sur internet. À l'époque, presque tout le monde se connecte par modem, et Carmack l'écrit : ça fait plus de trois cents millisecondes de retard, au minimum.

[VISUEL : extrait du « .plan » de Carmack du 2 août 1996, la phrase « 300+ ms latencies, minimum » surlignée.]

Imagine : t'appuies pour avancer, et ton perso part un tiers de seconde plus tard. C'est injouable.

Du coup, Carmack laisse le jeu deviner. Ton jeu n'attend pas la réponse du serveur : il te fait avancer tout de suite, avec les mêmes règles que lui. C'est la prédiction côté client.

[VISUEL : deux bleus côte à côte. Celui de gauche (sans prédiction) démarre en retard, celui de droite (avec prédiction) part au moment de l'appui.]

Mais le serveur garde le dernier mot. Si ton jeu a mal deviné, il corrige ta position, et la doc de Valve prévient : ta vue peut alors sauter d'un coup. Donc si t'as déjà vu ton perso reculer tout seul, ça peut venir de là.

[VISUEL : le bleu avance, un « ✗ » du serveur, il se fait aspirer quelques pas en arrière.]
[SON : un « boing » d'élastique.]

Bon, toi, t'es réglé. Mais les touches des autres, ton jeu ne peut pas les deviner : pour ça, il faudrait lire l'avenir. Il va falloir un deuxième mensonge.

**Abonnement (22 % de la vidéo, 2:52)**

Si t'aimes voir ce qui se cache derrière tes applis et tes jeux, abonne-toi. Sur Technovore, on en ouvre un chaque lundi.

[VISUEL : bouton « S'abonner » en bas à droite, 3 secondes ; le rouge, au loin, avance par à-coups pour préparer la section suivante.]

---

## 3. Deuxième mensonge : tu vois les autres dans le passé (3:01 – 4:22)

[VISUEL : « Mensonge n° 2 ».]

Par défaut, dans les jeux Source de Valve, ton jeu reçoit à peu près vingt nouvelles du serveur par seconde, d'après leur doc. Affichées telles quelles, les ennemis avanceraient par saccades, comme un diaporama.

[VISUEL : le rouge qui se téléporte de point en point, saccadé.]

Si t'as vu ma vidéo sur Uber, tu te rappelles la petite voiture qui glisse sur la carte. Les jeux font pareil, et voilà comment.

[VISUEL : vignette de la vidéo Uber, la petite voiture qui glisse, puis elle se transforme en perso rouge.]

Le jeu attend d'avoir deux positions, et il fait glisser l'ennemi de l'une à l'autre. Pour ça, il te montre les autres joueurs cent millisecondes dans le passé. Exprès.

[VISUEL : ligne du temps du rouge. Deux positions reçues, le perso glisse entre elles, une étiquette « −100 ms » le suit.]

Riot, le studio de VALORANT, le résume en une phrase : tu te vois toujours un peu en avance sur ce que pense le serveur, et les autres, tu les vois un peu en retard.

Donc fais le compte : toi, t'es en avance, les autres sont dans le passé, et chez eux, c'est l'inverse. Personne ne voit le même monde au même moment. Le seul qui sait où tout le monde est, c'est le serveur.

[VISUEL : les trois lignes du temps décalées, trois horloges qui ne disent pas la même heure.]

Sauf que ça crée un sacré problème. Si l'ennemi que tu vises est cent millisecondes dans le passé, quand tu tires pile sur sa tête… en vrai, il n'y est déjà plus.

---

## 4. Troisième mensonge : le serveur remonte le temps (4:22 – 6:24)

[VISUEL : « Mensonge n° 3 ».]

En 2001, Yahn Bernier, un ingénieur de Valve, explique leur solution pour Half-Life et Counter-Strike. Quand tu tires, le serveur fait un pas en arrière dans le temps. Il recule les autres joueurs là où tu les voyais au moment du clic, vérifie si ta balle touche, puis remet tout le monde au présent.

[VISUEL : la ligne du temps du serveur se rembobine, le rouge recule à sa position « vue par le tireur », la balle touche, tout revient au présent.]
[SON : bruit de rembobinage, puis un « clac ».]

En fait, le serveur fait de la VAR : il rembobine, il regarde ce que voyait le tireur, et il siffle.

[VISUEL : un écran de VAR stylisé, sans logo de compétition.]

Pour Bernier, le choix était facile : chaque joueur doit pouvoir viser droit sur ce qu'il voit. Et ça nous ramène au mur du début.

[VISUEL : retour sur la scène du hook, ralentie, avec les deux lignes du temps dessous.]

Un joueur avec un gros ping te tire dessus. Sur son écran, t'es encore à découvert. Le serveur rembobine, et il valide. Sauf que toi, entre-temps, t'étais déjà derrière ton mur. Bernier décrit exactement ça : le joueur planqué derrière une caisse est ramené en arrière dans le temps, et touché.

[VISUEL : citation de Bernier à l'écran : « the hiding player is transported backward in time and is hit ».]

Et Bernier est honnête : pour lui, c'est le cas extrême, un tireur vers cinq cents millisecondes de ping. Dans un combat normal, c'est beaucoup moins marqué.

Chez Apex, Respawn en a même fait un titre de son billet de 2021 : « Je me fais tuer alors que je suis derrière une porte ou un mur ». Et leur réponse : ce non-sens ne peut pas être supprimé, seulement transféré d'un joueur à l'autre.

[VISUEL : citation Respawn à l'écran : « This nonsense can't be eliminated, only transferred ». Une balance qui penche d'un joueur à l'autre.]

Voilà pourquoi personne n'a triché. Half-Life, Counter-Strike, Apex, VALORANT : ces jeux donnent raison au tireur. Avec une limite, quand même : Riot borne jusqu'où le serveur remonte, pour qu'un joueur à cinq cents millisecondes ne te tue pas une demi-seconde après que t'es à couvert.

En gros, ce que t'appelles « le lag », c'est souvent un choix d'ingénieur. Mais le deuxième mensonge, celui qui te montre les autres dans le passé, fait une autre victime : celui qui tient un angle.

---

## 5. Celui qui surgit gagne (6:24 – 8:14) · relance à 49 %, temps forts de 55 à 60 %

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : vue de dessus, le bleu tient un angle, immobile.]

Tu tiens un angle. Le mec sort, et il te tue avant que t'aies vu quoi que ce soit. C'est le peeker's advantage : l'avantage de celui qui surgit.

Et maintenant, tu sais d'où il vient : lui se voit en avance, toi tu le vois dans le passé. Donc quand il apparaît sur ton écran, ça fait déjà un moment qu'il te voit.

[VISUEL : les deux lignes du temps ; une zone rouge « il te voit, tu ne le vois pas » s'étire entre les deux.]

Riot a fait le calcul pour VALORANT, avec un modèle simplifié : avec les réglages de départ, celui qui surgit a environ cent quarante millisecondes d'avance. Et d'après Riot, un humain réagit souvent en trois cents millisecondes environ. Donc il part avec presque la moitié d'un temps de réaction d'avance sur toi.

[VISUEL : deux barres. « Avance du peeker : ~140 ms » à côté de « Réaction humaine : ~300 ms ».]

Et ça pèse lourd. Riot a fait des tests à l'aveugle avec des joueurs de très haut niveau, de force égale : dix millisecondes d'avantage en plus suffisaient à faire passer un duel de quatre-vingt-dix pour cent de victoires pour celui qui tient l'angle au sniper à quatre-vingt-dix pour cent pour celui qui surgit au fusil. Dix millisecondes.

[VISUEL : un camembert 90/10 qui bascule en 10/90.]
[SON : un « tic » d'horloge, très court.]

Résultat, Riot sort l'artillerie lourde : son propre réseau internet et des serveurs à cent vingt-huit ticks. Environ quarante millisecondes de gagnées. Mais Riot l'écrit : ils voudraient zéro avantage pour celui qui surgit, et c'est impossible.

Une étude de 2024, avec vingt-quatre joueurs sur un jeu de test, va plus loin : sans lag, c'est même celui qui attend qui gagne un peu plus. C'est surtout le ping de celui qui attend qui donne l'avantage à celui qui surgit, et le calcul de Riot dit pareil. Donc avec un gros ping, camper un angle, c'est pas ton meilleur plan.

[VISUEL : un perso qui campe dans un coin, une étiquette « gros ping » au-dessus de sa tête, il se fait surprendre.]

---

## 6. Les ticks : combien de fois par seconde le monde existe (8:14 – 8:54)

T'as entendu « cent vingt-huit ticks ». Un tick, c'est un tour de calcul du serveur : il lit les touches de tout le monde et fait avancer la partie. Selon les jeux, ça va de vingt fois par seconde, sur Apex, à cent vingt-huit, sur VALORANT.

[VISUEL : un métronome. À 20, il bat lentement ; à 128, il vibre.]

Du coup, plus c'est haut, plus ça coûte. Respawn a fait le calcul pour Apex : passer à soixante coûterait trois fois plus cher en bande passante et en processeur, pour gagner deux images. Donc il assume ses vingt. Riot, lui, a aussi payé pour un quatrième mensonge. Celui-là, il vise les tricheurs.

---

## 7. Quatrième mensonge : le serveur cache les ennemis (8:54 – 10:12)

[VISUEL : « Mensonge n° 4 ».]

Un wallhack te montre les ennemis à travers les murs, parce que ton jeu connaît leur position. Donc en 2020, Riot fait un truc radical pour VALORANT : le serveur ne t'envoie pas la position d'un ennemi que tu ne peux pas voir. La triche n'a plus rien à lire.

[VISUEL : la liste des positions envoyées par le serveur. Le rouge caché derrière un mur disparaît de la liste.]

Sauf que si le serveur attend que tu le voies, l'ennemi apparaît en retard, d'un coup. Alors le serveur regarde un peu dans le futur : il t'envoie l'ennemi juste avant qu'il tourne le coin, avec une avance plus grande que ton ping. Et pour savoir qui voit qui, il découpe la carte en cellules, comme des cubes de Minecraft : c'est l'image de Riot.

[VISUEL : la carte se découpe en cubes façon Minecraft ; deux cubes qui se voient s'allument.]

Et il y a eu des bugs drôles. Un ennemi caché commence à désamorcer le Spike, et toi, tu ne reçois rien. Du coup, quand il réapparaît, il est dans sa pose par défaut, planté comme un mannequin, en plein désamorçage.

[VISUEL : le rouge accroupi sur le Spike apparaît en pose de mannequin, immobile. Un « ??? » au-dessus.]
[SON : un « bloop » de bug.]

Ça réduit beaucoup les wallhacks, mais tant que l'ennemi arrive un peu en avance, une triche peut encore le voir. Et tout ça suppose un serveur pas trop loin. Depuis Abidjan, c'est une autre histoire.

---

## 8. Et depuis l'Afrique ? (10:12 – 11:58)

[VISUEL : la carte de l'Afrique et de l'Europe, sombre. Abidjan, Dakar, Kinshasa s'allument.]

Tu te rappelles le minimum théorique ? Une cinquantaine de millisecondes entre Abidjan et Paris, juste à cause de la physique. Depuis Kinshasa, autour de soixante. Et en 2020, Riot visait trente-cinq millisecondes de ping pour soixante-dix pour cent de ses joueurs. Donc le gros ping de la partie, ça risque d'être toi : quand tu tires, le serveur te donne raison, mais quand tu tiens un angle, c'est toi qui paies.

[VISUEL : le bleu, posé sur Abidjan, avec l'étiquette « gros ping » ; à côté, un joueur à Paris, « 35 ms ».]

Normalement, tu te dis : il faut un serveur en Afrique. Le seul serveur VALORANT d'Afrique est au Cap, depuis le 31 août 2023. Et le réseau de relais de Valve pour Counter-Strike n'a qu'un point africain : Johannesburg. Un relais, attention, pas forcément un serveur de partie.

[VISUEL : Le Cap et Johannesburg s'allument tout en bas de la carte.]

Mais regarde la carte. Abidjan–Johannesburg, c'est à peu près la même distance qu'Abidjan–Paris : environ quatre mille neuf cents kilomètres dans les deux cas. Et Le Cap est même un peu plus loin d'Abidjan que Paris.

[VISUEL : un compas part d'Abidjan. Le même cercle touche Paris et Johannesburg.]
[SON : un « ding » quand le cercle touche les deux villes.]

Du coup, pour l'Afrique de l'Ouest, l'Afrique du Sud ne rapproche rien. Pour Kinshasa, par contre, ça change tout : l'Afrique du Sud est à moins de trois mille cinq cents kilomètres. Un plancher autour de trente millisecondes, contre une soixantaine pour Paris. Un serveur en Afrique, ça ne veut pas dire un serveur près de chez toi.

[TON PING VERS PARIS ET VERS LE CAP OU JOHANNESBURG, MESURÉ DEPUIS CHEZ TOI, SI TU PEUX]

Et Free Fire, PUBG Mobile, Call of Duty Mobile ? Leurs studios n'ont rien publié sur leur netcode, en tout cas rien qu'on ait trouvé. Les mêmes principes s'y appliquent sans doute, mais c'est une supposition.

Bref, la distance, tu ne la changeras pas. Mais deux trucs, si.

---

## 9. Fin (11:58 – 13:05)

Le premier : arrête de regarder seulement le débit. Un jeu envoie de tout petits paquets : d'après Respawn, Apex consomme environ soixante kilo-octets par seconde en début de partie. À peu près un demi-mégabit par seconde : une broutille. En fait, ce qui compte, c'est le temps de l'aller-retour. Ton ping.

[VISUEL : deux tuyaux. Un énorme (débit) presque vide, un fin (ping) avec un chrono.]

Le deuxième, si tu joues sur PC ou sur console : le câble, parce que le Wi-Fi rend ton ping instable. Respawn l'écrit même dans son billet : si tu joues en Wi-Fi, on ne peut pas faire grand-chose pour toi.

[VISUEL : citation Respawn : « If you play on WiFi, we can't do much for you! ». Un câble Ethernet qui se branche.]

Et la prochaine fois que tu meurs derrière un mur, repense à Respawn : ce non-sens passe d'un joueur à l'autre. Le jour où c'est toi qui surgis d'un angle et qui gagnes un duel que l'autre n'a même pas vu venir, c'est lui qui crie au cheat. Et pourtant, personne n'a triché.

[VISUEL : la scène du hook rejouée à l'envers : cette fois, le bleu surgit, le rouge meurt derrière son mur, un « CHEAT ?! » au-dessus du rouge.]

[OPTIONNEL : TA PIRE MORT DERRIÈRE UN MUR, OU CE QUI T'A LE PLUS SURPRIS DANS CES BILLETS. UNE OU DEUX PHRASES.]

Quelle appli ou quel jeu je décortique ensuite ? Dis-le en commentaire.

Et la petite voiture d'Uber, elle est dans la vidéo juste là.

[VISUEL : écran de fin, 20 s : vidéo Uber à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Choc | Tu meurs derrière le mur |
| 0:05 | Retournement visuel | Rembobinage : la scène vue de l'écran de l'autre, et son gros ping |
| 0:15 | Contraste | « Crier au cheat », puis « personne n'a triché » (récolté à 12:33) |
| 0:24 | Question centrale | « Pourquoi le serveur donne raison au tireur ? » (refermée à 5:51 – 6:09) |
| 0:27 | Pont | « Tu ne vois jamais les autres là où ils sont vraiment » (refermé à 3:51) |
| 0:58 | Lien au vécu | Abidjan–Paris, au moins une cinquantaine de millisecondes (récolté à 10:12) |
| 1:13 | Image | Gambetta : la lumière « vraiment, vraiment lente » |
| 1:38 | Motif | « Les jeux mentent » : le compteur de mensonges démarre |
| 1:46 | Son + archive | Modem 56K, le « .plan » de Carmack |
| 2:01 | Adresse | « Imagine : t'appuies pour avancer… » |
| 2:21 | Humour + son | Le perso qui recule tout seul, « boing » d'élastique |
| 2:40 | Boucle ouverte | « Il faudrait lire l'avenir » : il faut un deuxième mensonge |
| 2:52 | Appel à l'action | Abonnement (22 %) |
| 3:15 | Rappel | La voiture d'Uber qui glisse |
| 3:51 | Révélation | Trois horloges qui ne disent pas la même heure |
| 4:08 | Pont | « Il n'y est déjà plus » |
| 4:43 | Humour | Le serveur fait de la VAR |
| 5:02 | Boucle fermée | Retour sur la scène du hook, ralentie |
| 5:33 | Citation | Respawn : « derrière une porte ou un mur », « only transferred » |
| 6:09 | Réponse + pont | « Un choix d'ingénieur », puis « une autre victime : celui qui tient un angle » |
| 6:24 | Coupure musique | Relance : « Tu tiens un angle » (49 %) |
| 6:49 | Chiffre | 140 ms d'avance contre 300 ms de réaction |
| 7:10 – 7:33 | Temps fort | 10 ms : 90/10 devient 10/90 (55 à 58 %) |
| 7:48 | Surprise | Sans lag, c'est celui qui attend qui gagne (60 %) |
| 8:09 | Humour | « Camper un angle, c'est pas ton meilleur plan » |
| 8:14 | Question | « Un tick, c'est quoi ? » |
| 8:36 | Choix d'ingénieur | Respawn assume ses vingt ticks |
| 8:50 | Annonce | Un quatrième mensonge, contre les tricheurs |
| 8:54 | Changement de sujet | Les wallhacks (68 %) |
| 9:36 | Référence | Les cubes de Minecraft (image de Riot) |
| 9:40 | Anecdote drôle | L'ennemi en pose de mannequin sur le Spike |
| 10:05 | Pont | « Depuis Abidjan, c'est une autre histoire » |
| 10:28 | Récolte + enjeu | « Le gros ping de la partie, ça risque d'être toi » (80 %) |
| 10:59 | Moment fort | Le compas : Abidjan–Johannesburg = Abidjan–Paris |
| 11:19 | Nuance | Kinshasa, elle, est près de l'Afrique du Sud |
| 11:57 | Utile | Le ping plutôt que le débit |
| 12:17 | Utile + citation | Le câble ; « If you play on WiFi… » |
| 12:33 | Retournement final | La scène du hook à l'envers : c'est l'autre qui crie au cheat |
| 12:55 | Engagement | « Quelle appli ou quel jeu je décortique ensuite ? » |
| 13:00 | Écran de fin | Uber |

**Total** : 40 relances en 13 min 05, environ une toutes les 20 secondes ; le plus long trou fait 22 s (0:27 – 0:49, comblé par le visuel du paquet qui fait l'aller-retour).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:35 – 1:46, le problème impossible | Moyen | Le premier bloc d'explication arrive juste après le hook | Abidjan dès 0:58 (le vécu de 63 % du public), ton ping en crochets, l'image de Gambetta, et le motif « les jeux mentent » qui donne une raison de rester |
| 2:52 – 3:01, l'abonnement | Faible | Un appel à l'action au milieu du récit | Il arrive juste après une boucle ouverte (« il va falloir un deuxième mensonge ») : le spectateur attend la suite, et le rouge saccadé à l'écran l'annonce |
| 4:22 – 6:24, la compensation | Élevé | Le bloc le plus long (296 mots) | La VAR, le retour à la scène du hook, la citation Respawn ; il referme la question centrale, donc la relance arrive juste derrière |
| 6:24, après la question refermée | Élevé | Risque de « j'ai ma réponse, je pars » | Coupure musicale, nouvelle scène vécue (l'angle), puis trois chiffres forts en 85 s, avec les dix millisecondes à 58 % et l'étude à 60 % |
| 8:14 – 8:54, les ticks | Moyen | Le passage le plus technique | Réduit à 96 mots, métronome ; il finit sur un choix d'ingénieur (Respawn) et l'annonce du quatrième mensonge |
| 11:58, la fin | Moyen | « Ce que ça change pour toi » peut sonner conseil générique | Deux conseils sourcés, puis la scène du hook rejouée à l'envers : c'est le dernier retournement de la vidéo |

## Notes de montage

- **Composants à construire une fois** (HyperFrames ou Remotion), réutilisés dans toute la vidéo :
  - les trois personnages vus de dessus (bleu, rouge, serveur) avec leur ligne du temps ;
  - le rembobinage (bande VHS) du hook, repris dans la section 4 et rejoué à l'envers dans la fin ;
  - le tampon « Mensonge n° 1, 2, 3, 4 » ;
  - la carte Afrique-Europe avec le compas (section 1, puis section 8).
- **Pas de vraie capture de jeu indispensable.** Si tu veux une vraie mort derrière un mur, un court extrait de bande-annonce officielle passe (même règle que Monster Hunter pour Uber), avec le gag monté par-dessus. Pas de logo de jeu en gros plan.
- **Les citations à l'écran** sont des extraits courts des sources primaires : Carmack (« 300+ ms latencies, minimum »), Gambetta (« the speed of light is really, really slow »), Bernier (« transported backward in time »), Respawn (« only transferred », « If you play on WiFi »). Date et auteur en petit sous chaque citation.
- **La VAR** : un écran de VAR stylisé, sans logo de compétition.
- **Énergie** : forte sur le hook, calme sur les explications, montées sur la VAR, le retour au mur, les 10 ms (≈ 7:30, 58 %), le bug du Spike et le compas.
- **Miniature** : charte noire, à faire. La scène du hook (le bleu derrière le mur, la balle qui le touche quand même) est le candidat évident ; vérifie qu'elle ne copie pas Frame Lab ni NPC Ned (`sources.md`, « Ce qui existe »).
- **Écran de fin** : la vidéo Uber, rappelée dans la section 3. Au kit d'upload, vérifie la règle de `CLAUDE.md` (« la vidéo suivante de la playlist du pilier ») : si une autre vidéo « génie » colle mieux en mars, change la phrase de fin.
- **Coupable au montage** si la prise dépasse 13 min 30 : le calcul de Respawn dans la section 6 (garde « de vingt à cent vingt-huit »), puis les cubes de Minecraft dans la section 7.

## Faits utilisés

Numéros de `sources.md`. Seuls des faits ✅ ou ⚠️ (dans la formulation donnée) à la 2e vérification, plus les lignes 43 à 48 ajoutées au grill du 23/10/2026.

| Fait | Phrase du script |
|---|---|
| 8 ✅, 33 ✅, 48 ✅ | « En face, le mec a un gros ping : sur son écran à lui, t'étais pas encore caché. Il t'a tiré dans ton passé, et le serveur lui a donné raison. » ; « le joueur planqué derrière une caisse est ramené en arrière dans le temps » ; « le cas extrême, un tireur vers cinq cents millisecondes (…) Dans un combat normal, c'est beaucoup moins marqué » (Bernier : « much less pronounced in normal combat situations ») |
| 3 ✅ | « Ton jeu lui envoie tes touches, et lui te renvoie des nouvelles du monde » ; « Le temps de l'aller-retour, c'est ton ping. » |
| 1 ⚠️ | « la lumière va à peu près à deux cent mille kilomètres par seconde » |
| 2 ⚠️ | « au moins une cinquantaine de millisecondes. Et c'est un minimum théorique » ; « Depuis Kinshasa, autour de soixante » |
| 11 ✅ | « jouer dans un univers où la lumière est vraiment, vraiment lente » (Gambetta) |
| 28 ⚠️ | « En 1996, John Carmack prépare QuakeWorld (…) presque tout le monde se connecte par modem (…) plus de trois cents millisecondes de retard, au minimum » ; « Carmack laisse le jeu deviner » |
| 6 ✅, 43 ✅ | « avec les mêmes règles que lui » ; « le serveur garde le dernier mot » ; « ta vue peut alors sauter d'un coup » ; « si t'as déjà vu ton perso reculer tout seul, ça peut venir de là » ; « il faudrait lire l'avenir » |
| 5 ✅ | « à peu près vingt nouvelles du serveur par seconde » ; « cent millisecondes dans le passé. Exprès. » (jeux Source par défaut, « d'après leur doc ») |
| 12 ✅ | « Riot (…) le résume en une phrase : tu te vois toujours un peu en avance sur ce que pense le serveur, et les autres, tu les vois un peu en retard » |
| 7 ✅ | « le serveur fait un pas en arrière dans le temps. Il recule les autres joueurs (…) puis remet tout le monde au présent » |
| 9 ✅ | « chaque joueur doit pouvoir viser droit sur ce qu'il voit » |
| 33 ✅ | « Respawn en a même fait un titre de son billet de 2021 » ; « ce non-sens ne peut pas être supprimé, seulement transféré d'un joueur à l'autre » ; fin : « ce non-sens passe d'un joueur à l'autre. Le jour où c'est toi qui surgis d'un angle (…) c'est lui qui crie au cheat » |
| 8, 9, 10, 33 | « Half-Life, Counter-Strike, Apex, VALORANT : ces jeux donnent raison au tireur » (seuls les jeux sourcés ; pas d'Overwatch, pas de « tous les jeux ») |
| 10 ✅ | « Riot borne jusqu'où le serveur remonte, pour qu'un joueur à cinq cents millisecondes ne te tue pas une demi-seconde après » (pas de chiffre de limite chez Riot) |
| 13 ⚠️ | « avec un modèle simplifié : avec les réglages de départ, celui qui surgit a environ cent quarante millisecondes d'avance » ; « un humain réagit souvent en trois cents millisecondes environ » ; « presque la moitié d'un temps de réaction » (141 / 300 ≈ 47 %, notre calcul) |
| 15 ✅, 45 ✅ | « joueurs de très haut niveau, de force égale : dix millisecondes (…) celui qui tient l'angle au sniper (…) celui qui surgit au fusil » (Riot : « For evenly matched players », sans « dans certains cas ») |
| 14 ✅, 38 ⚠️ | « son propre réseau internet et des serveurs à cent vingt-huit ticks. Environ quarante millisecondes de gagnées » ; « ils voudraient zéro avantage (…) et c'est impossible » |
| 16 ✅, 44 ✅ | « Une étude de 2024, avec vingt-quatre joueurs sur un jeu de test (…) c'est surtout le ping de celui qui attend » ; « C'est surtout le ping de celui qui attend qui donne l'avantage à celui qui surgit, et le calcul de Riot dit pareil » ; « avec un gros ping, camper un angle, c'est pas ton meilleur plan » (conséquence des deux) |
| 36 ✅ (correction) | « de vingt fois par seconde, sur Apex, à cent vingt-huit, sur VALORANT » |
| 18 ✅, 25 ⚠️, 34 ✅ | « plus c'est haut, plus ça coûte » ; « Respawn a fait le calcul pour Apex : passer à soixante coûterait trois fois plus cher en bande passante et en processeur, pour gagner deux images. Donc il assume ses vingt » |
| 19 ✅ | « en 2020, Riot (…) le serveur ne t'envoie pas la position d'un ennemi que tu ne peux pas voir » |
| 20 ✅ | « une avance plus grande que ton ping » ; « comme des cubes de Minecraft : c'est l'image de Riot » |
| 21 ✅, 46 ✅ | « désamorcer le Spike (…) dans sa pose par défaut » |
| 22 ⚠️ | « Ça réduit beaucoup les wallhacks, mais tant que l'ennemi arrive un peu en avance, une triche peut encore le voir. » (rien sur le son) |
| 14 ✅ | « en 2020, Riot visait trente-cinq millisecondes de ping pour soixante-dix pour cent de ses joueurs » (un objectif, pas un résultat) |
| 8, 10, 16, 44 | « quand tu tires, le serveur te donne raison, mais quand tu tiens un angle, c'est toi qui paies » |
| 29 ✅ | « Le seul serveur VALORANT d'Afrique est au Cap, depuis le 31 août 2023. » (à revérifier avant la voix) |
| 30 ✅ | « le réseau de relais de Valve pour Counter-Strike n'a qu'un point africain : Johannesburg. Un relais, attention, pas forcément un serveur de partie. » (lu le 23/10/2026, à revérifier avant la voix) |
| 35 ✅, 47 ✅ | « Abidjan–Johannesburg (…) environ quatre mille neuf cents kilomètres dans les deux cas » ; « Le Cap est même un peu plus loin d'Abidjan que Paris » ; « Pour Kinshasa (…) l'Afrique du Sud est à moins de trois mille cinq cents kilomètres. Un plancher autour de trente millisecondes » |
| 41 ❓ (généralisation) | « Leurs studios n'ont rien publié sur leur netcode (…) Les mêmes principes s'y appliquent sans doute, mais c'est une supposition. » |
| 32 ⚠️, 34 ✅ | « d'après Respawn, Apex consomme environ soixante kilo-octets par seconde en début de partie » ; « à peu près un demi-mégabit par seconde » (60 × 8 = 480 kbit/s, notre calcul) ; « ce qui compte, c'est le temps de l'aller-retour » |
| 32 ⚠️, 37 ⚠️ | « le Wi-Fi rend ton ping instable » ; « si tu joues en Wi-Fi, on ne peut pas faire grand-chose pour toi » (pas de chiffre) |

**Interprétations du script, à assumer ou à couper** :
- « si t'as déjà vu ton perso reculer tout seul, ça peut venir de là » : la doc de Valve dit que la correction d'une erreur de prédiction « peut faire sauter ta vue » (fait 43). Elle ne dit pas que c'est *la* cause des téléports que voient les joueurs, d'où « ça peut ». Respawn cite la même plainte (« sometimes I roll back to my previous position »), mais l'explique par la compensation du lag : le script ne s'en sert pas.
- « avec un gros ping, camper un angle, c'est pas ton meilleur plan » : conséquence de l'étude (fait 16, jeu sans rembobinage côté serveur) et du calcul de Riot (fait 44). Aucune des deux sources ne le formule comme un conseil.
- « le gros ping de la partie, ça risque d'être toi » : déduit du plancher physique (fait 2) comparé à l'objectif de Riot (fait 14). Aucun ping réel mesuré.
- La VAR et le mannequin sont des images, pas des faits.

**Écartés exprès** : Overwatch (fait 24), Fortnite (31), League of Legends (40), Street Fighter 6 (39), Guilty Gear (27), le sub-tick de CS2 (23), le chrono de VALORANT (18), le coût du brouillard (21), l'extrapolation d'un quart de seconde (5), la seconde d'historique de Valve (10), Dakar (47), tous coupés à la V2 pour la durée ; les 150 ms de Valve (6, redondants avec Carmack), Duke Nukem 3D et Tony Cannon (26, 28), le « +30 % » de Tariq10x, la date de sortie de VALORANT (non sourcée).

## Questions pour l'auteur

1. **Ton ping** : à quel jeu en ligne tu joues, et quel ping tu as vers Paris (et, si le jeu le permet, vers Le Cap ou Johannesburg) ? Il me faut le jeu, la ville, l'opérateur et la date de la mesure. Ça remplit les crochets des sections 1 et 8. Sans mesure, le script garde seulement le minimum théorique, et la phrase « le gros ping de la partie, ça risque d'être toi » reste au conditionnel.
2. **Ta pire mort derrière un mur** : tu en as une en tête (jeu, situation) ? Elle irait dans le crochet optionnel de la fin, ou à la place de la scène générique du hook si tu as la capture.
3. **PC ou mobile** : le public joue surtout sur mobile (Free Fire, PUBG Mobile, CoD Mobile), et aucune source primaire ne décrit leur netcode. Je garde VALORANT, Counter-Strike et Apex comme preuves, avec une phrase prudente sur le mobile (section 8), et le conseil du câble vise « PC ou console ». Tu veux mesurer un ping sur un jeu mobile, en 4G puis en Wi-Fi, pour donner un conseil aux joueurs sur téléphone ?
4. **Ton humour** : la VAR (section 4), « camper un angle, c'est pas ton meilleur plan » (section 5) et le mannequin du Spike (section 7), c'est ton registre ? Sinon, dis-moi quelle blague de joueur tu mettrais à la place (un jeu, un meme, un pote qui crie au cheat).
5. **La fin à l'envers** : la dernière scène fait de toi le joueur qui surgit et de l'autre celui qui crie au cheat. Ça te va, ou tu préfères finir sur ton conseil du câble ?
