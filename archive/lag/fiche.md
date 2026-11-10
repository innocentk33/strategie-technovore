# Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne

> Choisie le 23/10 au radar des idées, à la place de Mobile Money (abandonnée). Signaux : [`etudes/radar.md`](../../etudes/radar.md), entrée du 23/10. Planning : [`calendrier.md`](../../calendrier.md). **Publication provisoire : lun. 8 mars à 18 h**, à confirmer au radar du 22/02.

| Champ | Détail |
|---|---|
| **Pilier** | Le génie derrière l'app (Hub) : l'« appli », ici, c'est ton jeu en ligne |
| **Format** | Longue, 10-12 min |
| **Trafic visé** | Accueil + suggestions (à côté des vidéos de jeu, pas des vidéos tech) |
| **Mot-clé** | lag / ping (« lag jeux en ligne » : moins de 750 recherches par mois en France, vidIQ 23/10 ; « lag » : 23 K par mois dans le monde). Sujet porté par l'accueil, pas par la recherche |
| **Type de hook** | Situation vécue (le joueur est mort derrière un mur) |
| **Production estimée** | ~20-25 h (deux joueurs, un serveur, une ligne du temps : animations simples et réutilisables ; estimation) |

**Titres** :
1. Recherche : *Comment les jeux en ligne gèrent le lag ?*
2. Curiosité : *Tu étais caché. Le jeu t'a tué quand même.*
3. Mixte (recommandé) : *Pourquoi tu meurs derrière un mur : le génie caché des jeux en ligne*

**Miniature** : à faire (charte noire).

**Les 15 premières secondes** (règle du 22/10, `strategie.md`, section 5) : la scène que tout joueur a vécue, montrée tout de suite. Tu te mets à l'abri derrière un mur, tu es en sécurité… et tu meurs. Puis on rejoue la scène vue de l'écran de l'autre joueur : chez lui, tu n'étais pas encore caché. Pas de contexte avant.

**Texte** : comment un jeu en ligne fait croire à des millions de joueurs qu'ils sont dans le même monde, au même instant, alors que chacun le voit avec un retard différent (prédiction côté client, interpolation, compensation du lag, tick rate).
**Sous-texte** : le jeu ment à tout le monde, en permanence, et c'est ce mensonge qui le rend jouable. Chaque joueur vit dans un passé légèrement différent, et le serveur est l'arbitre qui décide quelle version devient la vérité. Ce que tu appelles « le lag » est souvent un choix d'ingénieur : qui on favorise, le tireur ou celui qui se cache.

**Contenu** :
- **Le problème impossible** : la lumière met du temps, le réseau encore plus. Entre ton clic et le serveur, des dizaines de millisecondes, et l'autre joueur a les siennes.
- **Les astuces** :
  - ton jeu prédit tes propres mouvements sans attendre le serveur ;
  - il affiche les autres légèrement dans le passé (interpolation) ;
  - quand quelqu'un tire, le serveur remonte le temps pour vérifier ce que le tireur voyait (compensation du lag) ;
  - l'avantage de celui qui surgit d'un angle (« peeker's advantage ») ;
  - le tick rate (64 ou 128 fois par seconde) ;
  - et le brouillard de guerre côté serveur contre les wallhacks.
- **Fin** : ce que ça change pour toi (pourquoi le ping compte plus que le débit, pourquoi le Wi-Fi te coûte), puis la question du pilier : « Quelle appli, ou quel jeu, je décortique ensuite ? »

**À vérifier** (sources primaires) :
- la doc « Source Multiplayer Networking » de Valve et l'article de Yahn Bernier (2001) sur la compensation de la latence ;
- les billets de Riot Games sur les serveurs à 128 ticks et sur le brouillard de guerre de Valorant contre les wallhacks (2020) ;
- le « sub-tick » de Counter-Strike 2 (Valve, 2023) ;
- la conférence GDC 2017 d'Overwatch sur le netcode (Tim Ford) ;
- le rollback des jeux de combat (GGPO).

Ne pas dire « tous les jeux font ça » : chaque jeu choisit ses compromis.

**Références** (vidIQ, 23/10) : DeadInSperanza, *Hidden Players: Why Don't Servers Just Hide Enemies?* (52 K, ×108, 13/10/2026) ; Outscal, *The Secret to LAG FREE Online Gaming Explained* (38 K, ×35) ; Tariq10x, *The +30% Advantage Devs Have No Control Over* (297 K). Aucune vidéo française repérée sur le sujet. On ne reprend ni leurs angles ni leurs miniatures.

## Corrections de la 2e vérification (23/10)

Le détail est dans [`sources.md`](sources.md), section « Pour le script ».

- **Titres** : les trois tiennent. « Tu meurs derrière un mur » est même l'intitulé d'une section du billet de Respawn sur Apex (« I am being killed while behind a door/wall », 28/04/2021, fait 33).
- **Le hook** : confirmé (Bernier 2001, Gambetta, Riot, Respawn). Ajoute la nuance : « sur l'écran de l'autre, tu n'étais pas encore caché : il t'a tiré dans ton passé, et le serveur lui a donné raison ». Et dis que c'est surtout vrai quand il a un gros ping : Bernier situe le cas extrême vers 500 ms, et dans un combat normal l'écart n'est que de quelques millisecondes (faits 8, 33). Ne dis pas que tous les jeux le font : seuls Half-Life et Counter-Strike, VALORANT (avec une limite) et Apex sont sourcés.
- **Contenu, tick rate** : « 64 ou 128 fois par seconde » est faux pour Apex (20 Hz) et pour Left 4 Dead (30). Remplace par « de 20 à 128 fois par seconde selon les jeux » (fait 36).
- **Fin, Wi-Fi** : une seule source, une phrase de Respawn sans chiffre. Dis « le Wi-Fi rend ton ping instable », pas « le Wi-Fi te coûte » avec un chiffre (faits 32, 37).
- **À vérifier, Overwatch** : la conférence GDC 2017 reste inaccessible. Ne cite ni le « 60 Hz » (le mode High Bandwidth, c'est 63 mises à jour par seconde côté client, en seconde main) ni le « 16 ms » (fait 24).
- **Public mobile** : aucune source primaire sur le netcode de Free Fire, PUBG Mobile ou Call of Duty Mobile (fait 41). Point ouvert : n'en parle que comme d'une généralisation.
