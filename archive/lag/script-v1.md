# Lag : script v1

**Titre** : *Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne*

**Durée** : environ 1 877 mots de voix off, soit 12 min 57 à ton débit mesuré sur ArtCraft (145 mots/min, pauses comprises) et 11 min 23 à 165 mots/min. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Texte** : comment un jeu en ligne fait croire à des millions de joueurs qu'ils sont dans le même monde, au même instant, alors que chacun le voit avec un retard différent (prédiction, interpolation, compensation du lag, tick rate, brouillard de guerre).
**Sous-texte** : le jeu ment à tout le monde, en permanence, et c'est ce mensonge qui le rend jouable. Chaque joueur vit dans un passé légèrement différent, et le serveur est l'arbitre qui décide quelle version devient la vérité. Ce que tu appelles « le lag » est souvent un choix d'ingénieur : qui on favorise, le tireur ou celui qui se cache.

**Fil rouge** : trois personnages qui reviennent dans chaque animation : toi (bleu), l'autre joueur (rouge) et le serveur (une boîte avec une horloge), chacun avec sa ligne du temps. La vidéo compte les « mensonges » du jeu : le premier (il devine tes mouvements), le deuxième (il te montre les autres dans le passé), le troisième (le serveur remonte le temps). Le motif revient avec le brouillard de guerre (« un autre endroit où le serveur ment exprès »).

**Boucles ouvertes** :
1. « Pourquoi un jeu donne raison à quelqu'un qui tire dans un mur ? » (hook, refermée dans la section 4).
2. « Tu ne vois jamais les autres là où ils sont vraiment » (pont du hook, refermée dans la section 3).
3. « Le minimum théorique depuis Abidjan » (section 1, récoltée dans la section 8 avec la carte de l'Afrique).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation (HyperFrames ou Remotion). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Aucune vraie capture de jeu n'est indispensable : tout se fait en motion design, vue de dessus.

---

## 0. Hook (0:00 – 0:36)

[VISUEL : vue de dessus en motion design. Ton perso (bleu) sprinte vers un mur, un ennemi (rouge) au loin. Pas de titre, pas de logo.]

Tu sprintes, tu passes derrière le mur, t'es à l'abri. Et là, tu meurs.

[SON : un tir sec, puis le son de la mort. L'écran vire au gris.]
[VISUEL : rembobinage rapide (bande VHS). La même scène, vue de l'écran du rouge : le bleu est encore à découvert. Le rouge tire.]

Vue de son écran à lui, t'étais pas encore caché. Il t'a tiré dans ton passé, et le serveur lui a donné raison.

Tu vas crier au cheat. Sauf que personne n'a triché : le jeu a fait ce que ses ingénieurs ont choisi.

[VISUEL : les deux écrans côte à côte, un point d'interrogation entre les deux.]

Alors pourquoi un jeu donne raison à un mec qui tire dans un mur ?

Pour le comprendre, accepte un truc : tu ne vois jamais les autres là où ils sont.

---

## 1. Le problème impossible (0:36 – 1:41)

[VISUEL : les trois personnages posés une fois pour toutes : toi (bleu), l'autre (rouge), le serveur au milieu, chacun avec une ligne du temps sous lui.]

Dans un jeu en ligne, t'as toi, l'autre, et au milieu, le serveur : l'arbitre. Ton jeu lui envoie tes touches, et lui te renvoie des nouvelles du monde, vingt à trente fois par seconde d'après la doc de Valve. Le temps de l'aller-retour, c'est ton ping.

[VISUEL : un petit paquet part du bleu, touche le serveur, revient. Compteur « ping » qui tourne.]

Mais ce message, il voyage. Dans la fibre, la lumière va à peu près à deux cent mille kilomètres par seconde. Imagine que t'es à Abidjan et que le serveur est à Paris : même en ligne droite, l'aller-retour prend au moins une cinquantaine de millisecondes. Et ça, c'est un minimum théorique. Ton vrai ping est forcément plus haut.

[VISUEL : carte, un trait Abidjan–Paris, un point lumineux fait l'aller-retour. Texte : « ≥ 50 ms, minimum théorique ».]

[TON JEU EN LIGNE ET TON PING, MESURÉ CHEZ TOI : JEU, VILLE, OPÉRATEUR, DATE]

Donc chaque joueur reçoit le monde en retard, et chacun avec son retard à lui.

[VISUEL : un rayon de lumière qui avance comme un escargot entre le bleu et le rouge.]

Et pourtant, ton jeu doit réagir dès que t'appuies sur une touche, et le serveur doit décider qui a touché qui. Pour s'en sortir, les jeux mentent. Et le premier mensonge, c'est à toi qu'il est fait.

---

## 2. Premier mensonge : ton jeu devine tes mouvements (1:41 – 2:40)

[VISUEL : « Mensonge n° 1 » s'inscrit en haut de l'écran, façon tampon.]
[SON : bruit de modem 56K, deux secondes.]

En 1996, John Carmack prépare QuakeWorld, une version de Quake pensée pour jouer en ligne. Presque tout le monde a un modem, et Carmack l'écrit : ça fait plus de trois cents millisecondes de retard, au minimum.

[VISUEL : extrait du « .plan » de Carmack du 2 août 1996, la phrase « 300+ ms latencies, minimum » surlignée.]

Imagine : t'appuies pour avancer, et ton perso part un tiers de seconde plus tard. Injouable.

Du coup, il laisse le jeu deviner. Ton jeu n'attend pas la réponse du serveur : il te fait avancer tout de suite, avec les mêmes règles que lui. C'est la prédiction côté client.

[VISUEL : deux bleus côte à côte. Celui de gauche (sans prédiction) démarre en retard, celui de droite (avec prédiction) part au moment de l'appui.]

Mais le serveur garde le dernier mot. Si ton jeu a mal deviné, le serveur corrige, et ton perso se fait recaler. Le petit téléport en arrière quand ta co rame, en gros, c'est souvent ça.

[VISUEL : le bleu avance, un « ✗ » du serveur, il se fait aspirer quelques pas en arrière.]
[SON : un « boing » d'élastique.]

Bon, toi, t'es réglé. Mais les touches des autres, ton jeu ne peut pas les deviner. Voilà pourquoi il faut un deuxième mensonge.

---

## 3. Deuxième mensonge : tu vois les autres dans le passé (2:40 – 4:14)

[VISUEL : « Mensonge n° 2 ».]

Par défaut, dans les jeux de Valve, ton jeu reçoit à peu près vingt nouvelles du serveur par seconde. Affichées telles quelles, les ennemis avanceraient par saccades, comme un diaporama.

[VISUEL : le rouge qui se téléporte de point en point, saccadé.]

Tu te rappelles la voiture d'Uber qui glisse sur la carte ? Je te disais que les jeux en ligne font pareil. Eh ben voilà comment.

[VISUEL : vignette de la vidéo Uber, la petite voiture qui glisse, puis elle se transforme en perso rouge.]

Le jeu attend d'avoir deux positions, et il fait glisser l'ennemi de l'une à l'autre. Pour ça, il te montre les autres joueurs cent millisecondes dans le passé. Exprès. Et si des nouvelles se perdent, il devine la suite, mais un quart de seconde maximum.

[VISUEL : ligne du temps du rouge. Deux positions reçues, le perso glisse entre elles, une étiquette « −100 ms » le suit.]

**Abonnement (≈ 25 % de la vidéo)**

Si t'aimes voir ce qui se cache derrière les applis et les jeux de tous les jours, abonne-toi : sur Technovore, on les ouvre un par un.

[VISUEL : bouton « S'abonner » en bas à droite, 3 secondes ; le rouge continue de glisser à l'écran.]

Riot, le studio de VALORANT, résume ce décalage en une phrase : tu te vois toujours un peu en avance sur ce que pense le serveur, et tu vois les autres un peu en retard.

Donc fais le compte : toi, t'es dans le futur, les autres dans le passé, et chez eux c'est l'inverse. Personne ne voit le même monde au même moment. Le seul qui sait où tout le monde est, c'est le serveur.

[VISUEL : les trois lignes du temps décalées, trois horloges qui ne disent pas la même heure.]

Sauf que ça crée un sacré problème. Si l'ennemi que tu vises est cent millisecondes dans le passé, quand tu tires pile sur sa tête… il n'y est déjà plus.

---

## 4. Troisième mensonge : le serveur remonte le temps (4:14 – 6:23)

[VISUEL : « Mensonge n° 3 ».]

En 2001, Yahn Bernier, ingénieur chez Valve, explique leur solution pour Half-Life et Counter-Strike. Quand tu tires, le serveur fait un pas en arrière dans le temps. Il recule les autres joueurs là où tu les voyais au moment du clic, vérifie si ta balle touche, puis remet tout le monde au présent.

[VISUEL : la ligne du temps du serveur se rembobine, le rouge recule à sa position « vue par le tireur », la balle touche, tout revient au présent.]
[SON : bruit de rembobinage, puis un « clac ».]

En fait, le serveur fait de la VAR : il rembobine, regarde ce que voyait le tireur, et il siffle.

Pour Bernier, le choix était facile : chaque joueur doit pouvoir viser droit sur ce qu'il voit. Et ça nous ramène au mur du début.

[VISUEL : retour sur la scène du hook, ralentie, avec les deux lignes du temps dessous.]

Un joueur avec un gros ping te tire dessus. Sur son écran, t'es encore à découvert. Le serveur rembobine, et valide. Mais toi, entre-temps, t'étais déjà derrière ton mur. Bernier décrit exactement ça : le joueur planqué derrière une caisse est ramené en arrière dans le temps, et touché.

[VISUEL : citation de Bernier à l'écran : « the hiding player is transported backward in time and is hit ».]

Et il est honnête : pour lui, c'est le cas extrême, un tireur vers cinq cents millisecondes de ping. Dans un combat normal, l'écart n'est que de quelques millisecondes. Du coup, ça t'arrive surtout face à un gros ping.

Chez Apex, Respawn en a même fait un titre de son billet de 2021 : « Je me fais tuer alors que je suis derrière une porte ou un mur ». Et leur réponse : ce non-sens ne peut pas être supprimé, seulement transféré. Parce que le jour où c'est toi qui sors de ton abri, c'est l'autre qui meurt face à quelqu'un qu'il ne voyait pas encore.

[VISUEL : citation Respawn à l'écran : « This nonsense can't be eliminated, only transferred ». Une balance qui penche d'un joueur à l'autre.]

Voilà pourquoi personne n'a triché. Half-Life, Counter-Strike, Apex, VALORANT : ces jeux donnent raison au tireur. Riot limite quand même jusqu'où le serveur remonte, pour qu'un joueur à cinq cents millisecondes ne te tue pas une demi-seconde après que t'es à couvert.

En gros, ce que t'appelles « le lag », c'est souvent un choix d'ingénieur. Et ce choix a un gagnant : celui qui surgit d'un angle.

---

## 5. Celui qui surgit gagne (6:23 – 8:06) · relance vers 55 %

[SON : la musique coupe net, une seconde de silence.]
[VISUEL : vue de dessus, le bleu tient un angle, immobile.]

Tu tiens un angle. Le mec sort, et il te tue avant que t'aies vu quoi que ce soit. C'est le peeker's advantage : l'avantage de celui qui surgit.

Et maintenant, tu sais pourquoi : lui se voit en avance, toi tu le vois dans le passé. Donc quand il apparaît sur ton écran, ça fait déjà un moment qu'il te voit.

[VISUEL : les deux lignes du temps ; une zone rouge « il te voit, tu ne le vois pas » s'étire entre les deux.]

Riot a fait le calcul pour VALORANT, avec un modèle simplifié : avec les réglages de départ, celui qui surgit a environ cent quarante millisecondes d'avance. Et d'après Riot, un humain réagit souvent en trois cents millisecondes environ.

[VISUEL : deux barres. « Avance du peeker : ~140 ms » à côté de « Réaction humaine : ~300 ms ».]

Et ça pèse lourd. Riot a fait des tests à l'aveugle avec des joueurs de très haut niveau, à niveau égal : dix millisecondes d'avantage faisaient passer un duel de quatre-vingt-dix pour cent de victoires pour l'un à quatre-vingt-dix pour cent pour l'autre. Dix millisecondes.

[VISUEL : un camembert 90/10 qui bascule en 10/90.]
[SON : un « tic » d'horloge, très court.]

Résultat, Riot sort l'artillerie lourde : son propre réseau internet et des serveurs à cent vingt-huit ticks. Environ quarante millisecondes de gagnées. Mais Riot l'écrit : ils voudraient zéro avantage pour celui qui surgit, et c'est impossible.

Une étude de 2024, avec vingt-quatre joueurs, va plus loin : sans lag, c'est même celui qui attend qui gagne un peu plus. Ce qui donne l'avantage à celui qui surgit, c'est surtout le ping de celui qui attend. Donc, d'après cette étude, avec un gros ping, camper un angle, c'est pas ton meilleur plan.

[VISUEL : un perso qui campe dans un coin, une étiquette « 120 ms » au-dessus de sa tête, il se fait surprendre.]

T'as entendu « cent vingt-huit ticks ». Mais un tick, c'est quoi, et pourquoi tout le monde n'en met pas cent vingt-huit ?

---

## 6. Les ticks : combien de fois par seconde le monde existe (8:06 – 9:07)

Un tick, c'est un tour de calcul du serveur : il lit les touches de tout le monde et fait avancer la partie. Selon les jeux, ça va de vingt fois par seconde, sur Apex, à cent vingt-huit, sur VALORANT.

[VISUEL : un métronome. À 20, il bat lentement ; à 128, il vibre.]

Du coup, à cent vingt-huit, chaque tour doit tenir en moins de huit millisecondes. Le serveur de VALORANT, au début, en mettait cinquante. Les ingés de Riot l'ont fait descendre sous les deux.

[VISUEL : un chrono « 50 ms » qui fond jusqu'à « < 2 ms ».]

Respawn, lui, assume ses vingt ticks sur Apex. Leur calcul : passer à soixante coûterait trois fois plus cher en bande passante et en processeur, pour gagner deux images.

Et Counter-Strike 2 ? Valve promet qu'avec son « sub-tick », le serveur connaît l'instant exact de ton tir, même entre deux ticks.

[VISUEL : la ligne du temps découpée en ticks ; un tir tombe entre deux traits, une petite étiquette indique l'instant exact.]

Bref, chaque studio choisit où il met son argent. Et il y a un autre endroit où le serveur ment exprès. Celui-là, il vise les tricheurs.

---

## 7. Le serveur qui cache les ennemis (9:07 – 10:24)

Un wallhack te montre les ennemis à travers les murs, parce que ton jeu connaît leur position. Donc en 2020, Riot fait un truc radical pour VALORANT : le serveur ne t'envoie plus la position d'un ennemi que tu ne peux pas voir. Rien à lire pour la triche.

[VISUEL : la liste des positions envoyées par le serveur. Le rouge caché derrière un mur disparaît de la liste.]

Sauf que si le serveur attend que tu le voies, l'ennemi apparaît en retard, d'un coup. Alors le serveur regarde un peu dans le futur : il t'envoie l'ennemi juste avant qu'il tourne le coin, avec une avance plus grande que ton ping. Et pour savoir qui voit qui, il découpe la carte en cellules, comme des cubes de Minecraft : c'est l'image de Riot.

[VISUEL : la carte se découpe en cubes façon Minecraft ; deux cubes qui se voient s'allument.]

Et il y a eu des bugs drôles. Un ennemi caché commence à désamorcer la bombe, et toi, tu ne reçois rien. Du coup, quand il réapparaît, il est dans sa pose par défaut, comme s'il ne faisait rien, en plein désamorçage.

[VISUEL : le rouge accroupi sur la bombe apparaît en pose de mannequin, immobile. Un « ??? » au-dessus.]
[SON : un « bloop » de bug.]

Ça réduit beaucoup les wallhacks, mais tant que l'ennemi arrive un peu en avance, une triche peut encore le voir. Ça, c'est le côté génial. Maintenant, le côté qui fâche : jouer depuis l'Afrique.

---

## 8. Et depuis l'Afrique ? (10:24 – 11:52)

[VISUEL : la carte de l'Afrique et de l'Europe, sombre. Abidjan, Dakar, Kinshasa s'allument.]

Tu te rappelles le minimum théorique ? Une cinquantaine de millisecondes entre Abidjan et Paris, juste à cause de la physique. Depuis Kinshasa, autour de soixante.

Normalement, tu te dis : il faut un serveur en Afrique. Le seul serveur VALORANT d'Afrique est au Cap, depuis le 31 août 2023. Et le réseau de relais de Valve pour Counter-Strike n'a qu'un point africain : Johannesburg. Un relais, attention, pas forcément un serveur de partie.

[VISUEL : Le Cap et Johannesburg s'allument tout en bas de la carte.]

Mais regarde la carte. Abidjan–Johannesburg, c'est à peu près la même distance qu'Abidjan–Paris : environ quatre mille neuf cents kilomètres dans les deux cas. Et Le Cap n'est pas plus près d'Abidjan que Paris.

[VISUEL : un compas part d'Abidjan. Le même cercle touche Paris et Johannesburg.]
[SON : un « ding » quand le cercle touche les deux villes.]

Du coup, pour l'Afrique de l'Ouest, l'Afrique du Sud ne rapproche rien. Pour Kinshasa, par contre, Johannesburg est à moins de trois mille kilomètres : un plancher autour de trente millisecondes, contre une soixantaine pour Paris. Un serveur en Afrique, ça ne veut pas dire un serveur près de chez toi.

[TON PING VERS PARIS ET VERS LE CAP OU JOHANNESBURG, MESURÉ DEPUIS CHEZ TOI, SI TU PEUX]

Et Free Fire, PUBG Mobile, Call of Duty Mobile ? Leurs studios n'ont rien publié sur leur netcode, en tout cas rien que j'aie trouvé. Les mêmes principes s'y appliquent sans doute, mais c'est une supposition.

Bref, la distance, tu ne la changeras pas. Par contre, il y a deux trucs que tu peux changer chez toi.

---

## 9. Fin (11:52 – 12:57)

Le premier : arrête de regarder seulement le débit. Un jeu envoie de tout petits paquets : Apex consomme environ soixante kilo-octets par seconde. En fait, ce qui compte, c'est le temps de l'aller-retour. Ton ping.

[VISUEL : deux tuyaux. Un énorme (débit) presque vide, un fin (ping) avec un chrono.]

Le deuxième : le câble, parce que le Wi-Fi rend ton ping instable. Respawn l'écrit même dans son billet : si tu joues en Wi-Fi, on ne peut pas faire grand-chose pour toi.

[VISUEL : citation Respawn : « If you play on WiFi, we can't do much for you! ». Un câble Ethernet qui se branche.]

Et la prochaine fois que tu meurs derrière un mur, tu sauras ce qui s'est passé. Ton jeu t'a menti, il a menti à l'autre aussi, et c'est ce mensonge qui rend la partie jouable. Le serveur a tranché, et cette fois, il a donné raison au tireur.

[OPTIONNEL : TA PIRE MORT DERRIÈRE UN MUR, OU CE QUI T'A LE PLUS SURPRIS EN LISANT CES BILLETS. UNE OU DEUX PHRASES.]

Sur Technovore, j'ouvre comme ça les applis et les jeux que t'as dans la poche. Quelle appli ou quel jeu je décortique ensuite ? Dis-le en commentaire.

Et la petite voiture qui glisse sur la carte d'Uber, tu la retrouves dans la vidéo juste là.

[VISUEL : écran de fin, 20 s : vidéo Uber à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:04 | Choc | Tu meurs derrière le mur |
| 0:06 | Retournement visuel | Rembobinage, la scène vue de l'écran de l'autre |
| 0:24 | Question centrale | « Pourquoi un jeu donne raison à un mec qui tire dans un mur ? » (refermée à 5:57) |
| 0:29 | Pont | « Tu ne vois jamais les autres là où ils sont » (refermé à 3:46) |
| 1:04 | Lien au vécu | Abidjan–Paris, au moins une cinquantaine de millisecondes (récolté à 10:24) |
| 1:34 | Motif | « Les jeux mentent » : le compteur de mensonges démarre |
| 1:41 | Son + archive | Modem 56K, le « .plan » de Carmack |
| 2:24 | Humour + son | Le téléport en arrière, « boing » d'élastique |
| 2:52 | Rappel | La voiture d'Uber qui glisse (vidéo précédente du pilier) |
| 3:21 | Appel à l'action | Abonnement (26 %) |
| 3:46 | Révélation | Trois horloges qui ne disent pas la même heure |
| 4:02 | Pont | « Il n'y est déjà plus » |
| 4:37 | Humour | Le serveur fait de la VAR |
| 4:55 | Boucle fermée | Retour sur la scène du hook, ralentie |
| 5:30 | Citation | Respawn : « derrière une porte ou un mur », « only transferred » |
| 6:23 | Coupure musique | Relance : « Tu tiens un angle » (49 %) |
| 6:48 | Chiffre | 140 ms d'avance contre 300 ms de réaction |
| 7:03 | Chiffre fort | 10 ms : 90/10 devient 10/90 (54 %) |
| 7:36 | Surprise | Sans lag, c'est celui qui attend qui gagne (59 %) |
| 7:58 | Question | « Un tick, c'est quoi ? » |
| 8:23 | Visuel | Le chrono de 50 ms qui fond sous 2 ms |
| 8:48 | Rupture | Counter-Strike 2 et le sub-tick |
| 9:07 | Changement de sujet | Les wallhacks |
| 9:35 | Référence | Les cubes de Minecraft (image de Riot) |
| 9:53 | Anecdote drôle | L'ennemi en pose par défaut pendant le désamorçage |
| 10:24 | Changement de ton | « Le côté qui fâche » : l'Afrique |
| 10:54 | Moment fort | Le compas : Abidjan–Johannesburg = Abidjan–Paris |
| 11:13 | Nuance | Kinshasa, elle, est près de Johannesburg |
| 11:52 | Utile | Le ping plutôt que le débit |
| 12:06 | Utile + citation | Le câble ; « If you play on WiFi… » |
| 12:45 | Engagement | « Quelle appli ou quel jeu je décortique ensuite ? » |
| 12:50 | Écran de fin | Uber |

**Total** : 32 relances en 12 min 57, environ une toutes les 24 secondes ; le plus long trou fait 35 s (0:29 – 1:04).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:36 – 1:41, le problème impossible | Moyen | Le premier bloc d'explication arrive juste après le hook | Abidjan dès 1:04 (le vécu de 63 % du public), ton ping en crochets, et le motif « les jeux mentent » qui donne une raison de rester |
| 2:40 – 4:14, l'interpolation | Moyen | Notion abstraite (« cent millisecondes dans le passé ») | Le diaporama saccadé puis fluide, le rappel Uber, les trois horloges |
| 4:14 – 6:23, la compensation | Élevé | Le bloc le plus long (310 mots) | La VAR, le retour à la scène du hook à 4:55, la citation Respawn ; il referme la question centrale, donc il faut la relance juste derrière |
| 6:23, après la question refermée | Élevé | La question du hook est résolue : risque de « j'ai ma réponse, je pars » | Coupure musicale, nouvelle scène vécue (l'angle), puis trois chiffres forts en 75 s |
| 8:06 – 9:07, les ticks | Moyen | Le passage le plus technique, deux liaisons seulement | Section courte (146 mots), métronome, chrono qui fond ; coupable au montage si la prise est trop longue (garde alors la phrase « de vingt à cent vingt-huit ») |
| 11:52, la fin | Moyen | « Ce que ça change pour toi » peut sonner conseil générique | Deux conseils seulement, chacun tenu par une source (Valve, Respawn), puis le retour au mur du début |

## Notes de montage

- **Composants à construire une fois** (HyperFrames ou Remotion), réutilisés dans toute la vidéo :
  - les trois personnages vus de dessus (bleu, rouge, serveur) avec leur ligne du temps ;
  - le rembobinage (bande VHS) du hook, repris à 4:14 et à 4:55 ;
  - le tampon « Mensonge n° 1, 2, 3 » ;
  - la carte Afrique-Europe avec le compas (1:04, puis 10:24).
- **Pas de vraie capture de jeu indispensable.** Si tu veux une vraie mort derrière un mur, un court extrait de bande-annonce officielle passe (même règle que Monster Hunter pour Uber), avec le gag monté par-dessus. Pas de logo de jeu en gros plan.
- **Les citations à l'écran** sont des extraits courts des sources primaires : Carmack (« 300+ ms latencies, minimum »), Bernier (« transported backward in time »), Respawn (« only transferred », « If you play on WiFi »). Date et auteur en petit sous chaque citation.
- **La VAR** : un écran de VAR stylisé, sans logo de compétition.
- **Énergie** : forte sur le hook, calme sur les explications, montées sur la VAR, le retour au mur (4:55), les 10 ms (7:03), le bug de la bombe (9:53) et le compas (10:54).
- **Miniature** : charte noire, à faire. La scène du hook (le bleu derrière le mur, la balle qui le touche quand même) est le candidat évident ; vérifie qu'elle ne copie pas Frame Lab ni NPC Ned (`sources.md`, « Ce qui existe »).
- **Écran de fin** : la vidéo Uber, qui est la vidéo précédente du pilier et que la section 3 rappelle.
- **Section 6 coupable** si la prise dépasse 13 min : garde « de vingt à cent vingt-huit selon les jeux » et le calcul de Respawn, coupe le chrono de VALORANT et le sub-tick.

## Faits utilisés

Numéros de `sources.md`. Seuls des faits ✅ ou ⚠️ (dans la formulation donnée) à la 2e vérification.

| Fait | Phrase du script |
|---|---|
| 8 ✅, 33 ✅ | « Il t'a tiré dans ton passé, et le serveur lui a donné raison. » ; « le joueur planqué derrière une caisse est ramené en arrière dans le temps » ; « le cas extrême, un tireur vers cinq cents millisecondes (…) quelques millisecondes » |
| 3 ✅ | « vingt à trente fois par seconde d'après la doc de Valve » ; « Le temps de l'aller-retour, c'est ton ping. » |
| 1 ⚠️ | « la lumière va à peu près à deux cent mille kilomètres par seconde » |
| 2 ⚠️ | « au moins une cinquantaine de millisecondes. Et ça, c'est un minimum théorique » ; « Depuis Kinshasa, autour de soixante » |
| 28 ⚠️ | « En 1996, John Carmack prépare QuakeWorld (…) plus de trois cents millisecondes de retard, au minimum » ; « il laisse le jeu deviner » |
| 6 ✅ | « avec les mêmes règles que lui » ; « le serveur garde le dernier mot (…) le serveur corrige » |
| 5 ✅ | « à peu près vingt nouvelles du serveur par seconde » ; « cent millisecondes dans le passé. Exprès. » ; « un quart de seconde maximum » (jeux Source par défaut : le script dit « dans les jeux de Valve ») |
| 12 ✅ | « tu te vois toujours un peu en avance sur ce que pense le serveur, et tu vois les autres un peu en retard » |
| 7 ✅ | « le serveur fait un pas en arrière dans le temps. Il recule les autres joueurs (…) puis remet tout le monde au présent » |
| 9 ✅ | « Pour Bernier, le choix était facile : chaque joueur doit pouvoir viser droit sur ce qu'il voit. » |
| 33 ✅ | « Respawn en a même fait un titre de son billet de 2021 » ; « ce non-sens ne peut pas être supprimé, seulement transféré » ; « c'est l'autre qui meurt face à quelqu'un qu'il ne voyait pas encore » |
| 8, 9, 10, 33 | « Half-Life, Counter-Strike, Apex, VALORANT : ces jeux donnent raison au tireur » (seuls les jeux sourcés ; pas d'Overwatch, pas de « tous les jeux ») |
| 8 ✅, 10 ✅ | « Riot limite quand même jusqu'où le serveur remonte, pour qu'un joueur à cinq cents millisecondes ne te tue pas une demi-seconde après » (pas de chiffre de limite) |
| 13 ⚠️ | « Riot a fait le calcul (…) avec un modèle simplifié : avec les réglages de départ, celui qui surgit a environ cent quarante millisecondes d'avance » ; « un humain réagit souvent en trois cents millisecondes environ » |
| 15 ✅ | « joueurs de très haut niveau, à niveau égal : dix millisecondes (…) de quatre-vingt-dix pour cent (…) à quatre-vingt-dix pour cent pour l'autre » |
| 14 ✅, 38 ⚠️ | « son propre réseau internet et des serveurs à cent vingt-huit ticks. Environ quarante millisecondes de gagnées » ; « ils voudraient zéro avantage (…) et c'est impossible » |
| 16 ✅ | « Une étude de 2024, avec vingt-quatre joueurs (…) c'est surtout le ping de celui qui attend » (le conseil « camper un angle » est présenté comme une conséquence de l'étude) |
| 36 ✅ (correction) | « de vingt fois par seconde, sur Apex, à cent vingt-huit, sur VALORANT » |
| 18 ✅ | « moins de huit millisecondes » ; « au début, en mettait cinquante (…) sous les deux » |
| 25 ⚠️, 34 ✅ | « Respawn, lui, assume ses vingt ticks (…) trois fois plus cher en bande passante et en processeur, pour gagner deux images » |
| 23 ✅ | « Valve promet qu'avec son « sub-tick », le serveur connaît l'instant exact de ton tir » |
| 19 ✅ | « en 2020, Riot (…) le serveur ne t'envoie plus la position d'un ennemi que tu ne peux pas voir » |
| 20 ✅ | « une avance plus grande que ton ping » ; « comme des cubes de Minecraft : c'est l'image de Riot » |
| 21 ✅ | « il est dans sa pose par défaut, comme s'il ne faisait rien, en plein désamorçage » |
| 22 ⚠️ | « Ça réduit beaucoup les wallhacks, mais tant que l'ennemi arrive un peu en avance, une triche peut encore le voir. » (rien sur le son) |
| 29 ✅ | « Le seul serveur VALORANT d'Afrique est au Cap, depuis le 31 août 2023. » |
| 30 ✅ | « le réseau de relais de Valve pour Counter-Strike n'a qu'un point africain : Johannesburg. Un relais, attention, pas forcément un serveur de partie. » |
| 35 ✅ | « Abidjan–Johannesburg, c'est à peu près la même distance qu'Abidjan–Paris : environ quatre mille neuf cents kilomètres » ; « Johannesburg est à moins de trois mille kilomètres : un plancher autour de trente millisecondes » |
| `sources.md`, formulation 10 | « Le Cap n'est pas plus près d'Abidjan que Paris. » |
| 41 ❓ (généralisation) | « Leurs studios n'ont rien publié sur leur netcode (…) Les mêmes principes s'y appliquent sans doute, mais c'est une supposition. » |
| 32 ⚠️, 34 ✅ | « Apex consomme environ soixante kilo-octets par seconde » ; « ce qui compte, c'est le temps de l'aller-retour » |
| 32 ⚠️, 37 ⚠️ | « le Wi-Fi rend ton ping instable » ; « si tu joues en Wi-Fi, on ne peut pas faire grand-chose pour toi » (pas de chiffre) |

**Interprétations du script, à assumer ou à couper** :
- « Le petit téléport en arrière quand ta co rame, en gros, c'est souvent ça » : la doc de Valve décrit la correction d'une erreur de prédiction ; le lien avec ce que les joueurs appellent un téléport est une explication, dite avec « en gros » et « souvent ».
- « avec un gros ping, camper un angle, c'est pas ton meilleur plan » : conséquence tirée de l'étude du fait 16, dite avec « d'après cette étude ». L'étude n'avait pas de compensation côté serveur.
- La VAR est une image, pas un fait.

**Écartés exprès** : Overwatch (fait 24), Fortnite (31), League of Legends (40), Street Fighter 6 (39), Guilty Gear (27), Valve « une seconde d'historique » (10, coupé pour la durée), Duke Nukem 3D et Tony Cannon (26, 28), le « +30 % » de Tariq10x.

## Questions pour l'auteur

1. **Ton ping** : à quel jeu en ligne tu joues, et quel ping tu as vers Paris (et, si le jeu le permet, vers Le Cap ou Johannesburg) ? Il me faut le jeu, la ville, l'opérateur et la date de la mesure. Ça remplit les crochets des sections 1 et 8 ; sans mesure, le script garde seulement le minimum théorique.
2. **Ta pire mort derrière un mur** : tu en as une en tête (jeu, situation) ? Elle irait dans le crochet optionnel de la fin, ou à la place de la scène générique du hook si tu as la capture.
3. **PC ou mobile** : le public joue surtout sur mobile (Free Fire, PUBG Mobile, CoD Mobile), et aucune source primaire ne décrit leur netcode. Je garde VALORANT, Counter-Strike et Apex comme preuves, avec une phrase prudente sur le mobile (section 8). Ça te va, ou tu préfères que tu mesures toi-même un ping sur un jeu mobile pour l'ancrer ?
4. **Ton humour** : la VAR (4:37) et « camper un angle, c'est pas ton meilleur plan » (7:36), c'est ton registre ? Sinon, dis-moi quelle blague de joueur tu mettrais à la place (un jeu, un meme, un pote qui crie au cheat).
