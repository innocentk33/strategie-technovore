# Étude : Morgans Code (@MorgansCode)

> Données vidIQ du 21 oct. 2026 (statistiques de la chaîne, 50 dernières vidéos longues, 2 transcriptions). Lien : https://www.youtube.com/@MorgansCode

## En bref

Chaîne anglophone sur l'**IA en local**, partie de zéro fin juillet 2026 (5 abonnés le 29/07). En 12 semaines : **81 vidéos, 481 K vues, 2 020 abonnés**. Elle publie presque une vidéo par jour, de 8 à 12 minutes, et elle accélère : +240 abonnés du 14 au 21 octobre.

Ton intuition est juste : **Morgans ne teste presque rien.** Ses chiffres viennent des notes de version, des tickets GitHub et des posts de gens qui ont la machine. Il le dit lui-même : « ceux qui postent leurs machines et leurs vitesses, c'est de là que viennent la plupart de mes chiffres ». Ce qui le rend crédible, c'est qu'il **montre son calcul**, puis le confronte aux mesures des autres.

La leçon pour Technovore : **une vidéo « calculée » marche, à condition d'être une enquête honnête.** Tu peux traiter les modèles qui ne tiennent pas dans ta 5080, comme Kai et Morgans, et garder les vrais tests pour ce qui tient dans 16 Go. Personne ne fait ni l'un ni l'autre en français.

---

## 1. Fiche d'identité

| | |
|---|---|
| Abonnés | 2 020 (1 780 le 14/10, 5 le 29/07) |
| Vues totales | 481 K, toutes depuis fin juillet |
| Vidéos | 81 longues, aucun Short repéré |
| Rythme | ~1 vidéo par jour, souvent vers 22 h UTC (minuit à Paris) |
| Durée | 8 à 12 min |
| Pays (vidIQ) | États-Unis |
| Vues médianes (50 dernières vidéos) | ~6 200 |

**Point faible : beaucoup de vues, peu d'abonnés.** Morgans gagne 4,2 abonnés pour 1 000 vues, contre 7,7 pour Kai (49 400 abonnés pour 6,41 M de vues au 21/10). Hypothèse, non vérifiée : sans persona ni série forte, le spectateur vient pour un chiffre et repart. Kai, lui, a une série reconnaissable (« What Would It Cost… »).

## 2. Ce qui marche et ce qui ne marche pas

Vues médianes par thème, sur ses 50 dernières vidéos longues (classement fait à la main d'après les titres) :

| Thème | Vidéos | Vues médianes | Exemple |
|---|---|---|---|
| **Même matériel, plus rapide** (moteur, compression) | 7 | **26 800** | [6× Faster Than llama.cpp — The New Way to Run 125B Models](https://www.youtube.com/watch?v=i7nSjm5tTRw) : 62,9 K, ×16,4 |
| **Coût et matériel** (calculé) | 7 | 9 800 (dont 2 vidéos de 1 et 2 jours) | [Is $1,500 All You Need to Run DeepSeek V4.1 Flash?](https://www.youtube.com/watch?v=mat0oOXVCcU) : 17,7 K **en un jour** |
| Quel modèle faire tourner | 14 | 5 000 | [Qwen 3.8 27B: How to Run a Claude-Level Model Locally](https://www.youtube.com/watch?v=r-b88S-lS2w) : 25,8 K, ×20,5 |
| Actu, benchmarks, API | 22 | **1 900** | « GLM-5.3 Just Beat Anthropic's Hacker Model? » : 805 vues |

**Les plus grosses anomalies** (score vidIQ) :

| Vidéo | Vues | Multiple |
|---|---|---|
| Qwen 3.8 27B: How to Run a Claude-Level Model Locally | 25,8 K | ×20,5 |
| 6× Faster Than llama.cpp — The New Way to Run 125B Models | 62,9 K | ×16,4 |
| Qwen 3.8 27B Is Coming — Sonnet 5 on Your Laptop? | 3,6 K | ×13,2 (au tout début de la chaîne) |
| Qwen 3.8 35B Never Came. Run This Instead | 30,1 K | ×7,8 |
| FreeToken vs llama.cpp — An 8GB Laptop Ran a 35B Model at Nearly 40 TPS | 26,8 K | ×5,6 |
| Qwen 3.8 27B Compressed to 5.9 GB — 98% of the Performance | 38,5 K | ×4,7 |
| Qwen 4 27B: What to Expect From the Next Local AI King | 22,2 K | ×3,5 |

**À retenir** : comme chez Kai, le spectateur vient pour **sa machine**. Le sujet qui marche le mieux chez Morgans est encore plus précis : « ta carte peut faire mieux, sans rien acheter ». L'actu des modèles et des API ne marche pas, même chez lui.

## 3. Comment il fabrique une vidéo « calculée »

Analyse de deux transcriptions : « What Does It Really Cost to Run? » (DeepSeek, 19/10) et « Is $1,500 All You Need… » (20/10).

1. **Une question d'argent dès la 1re phrase.** « Pourrais-tu le faire tourner chez toi et résilier ton abonnement Claude ? »
2. **Il se corrige lui-même, et c'est le hook.** « Dans ma dernière vidéo, j'ai dit qu'il fallait 14 000 dollars. Est-ce que j'avais tort ? » Chaque vidéo prolonge la précédente : ça fabrique une série sans le dire.
3. **Une enquête racontée.** « Je suis allé dans les pages du projet en m'attendant à trouver le piège ici, et il était ailleurs. » Chaque partie finit sur une question qui ouvre la suivante.
4. **Le calcul à l'écran.** Exemple : bande passante de la RAM (68 Go/s) ÷ poids actifs par token (5 Go) = plafond de 13 tokens/s. Puis la mesure d'un inconnu : 10 tokens/s. « Juste sous notre plafond. » Le calcul est vérifié par une mesure, même si ce n'est pas la sienne.
5. **L'honnêteté sur les comparaisons.** « Les nouveaux moteurs comparent souvent leur meilleure version à la pire, alors j'ai cherché la comparaison la plus proche. » Et : « disons presque 3 fois plutôt qu'un chiffre exact ».
6. **Des images simples.** La carte graphique est le bureau, la RAM l'étagère derrière toi, le SSD la cave. Plusieurs agents sur une machine : un seul cuisinier pour plusieurs commandes.
7. **Un verdict selon le profil**, puis l'appel à s'abonner lié à la suite : « abonne-toi si tu veux les chiffres quand quelqu'un testera la version corrigée ».

## 4. Pour Technovore

### Ce qu'on reprend

- **Le format « calculé »** pour les modèles trop gros pour ta 5080 (DeepSeek, Kimi, Claude). C'est le cœur de l'idée 11 (« Combien coûte Claude en local ? »).
- **Le thème « même carte, plus rapide »**, que tu peux **tester pour de vrai** sur ta 5080 : moteurs, compression, réglages. Morgans le calcule, toi tu le mesures.
- **Le fil entre les vidéos** : chaque épisode cite le précédent et annonce le suivant (« dans l'épisode #1, j'avais dit… »).
- **Le calcul vérifié par une mesure** : le tien quand ça tient dans 16 Go, celle d'un autre (citée et datée) sinon.

### Comment te démarquer

1. **Tester ce qui tient dans 16 Go.** Ni Kai ni Morgans ne mesurent eux-mêmes.
2. **Les euros et l'électricité française**, comme pour Kai.
3. **Une persona et une série** (« Claude ou mon PC ? ») pour transformer les vues en abonnés, là où Morgans plafonne à 4,2 abonnés pour 1 000 vues.

### À ne pas copier

- **Le rythme quotidien.**
- **Les vidéos d'actu sur les modèles et les benchmarks** : 1 900 vues médianes.
- **Ses chiffres tels quels** : ce sont des relevés de tiers. Remonte toujours à la source (note de version, ticket GitHub, post) et date-la dans `sources.md`.
