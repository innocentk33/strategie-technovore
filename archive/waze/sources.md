# Comment Waze sait qu'il y a un bouchon avant que tu le voies : sources

> Phase 1 (recherche) du 23/10/2026. 2e vérification : à faire (phase 2).
>
> 2e vérification (Opus) du 23/10/2026 : 20 ✅ · 12 ⚠️ · 1 ❌ · 2 ❓.

## vidIQ (23/10/2026)

### Mots-clés (France)

| Mot-clé | Volume/mois | Concurrence | Remarque |
|---|---|---|---|
| comment fonctionne waze | < 750 (« très faible ») | inconnue | Aucune demande mesurée sur la phrase exacte. Le titre ne doit pas compter sur elle. |
| waze | 45 476 (monde) ; 9 745 en France ; +32 % sur 30 j | 54,2 / 100 | La demande est sur la marque, en hausse. Waze est suggéré avec « gps » (71 510) et « android auto » (19 652). |
| waze vs google maps | 4 352 | 21,1 | Basse concurrence. Variante utile pour un chapitre ou la description. |
| google maps vs waze | 8 230 | 29,7 | Idem. |
| waze carplay | 4 816 | 28,5 | Hors sujet. |
| google maps | 119 593 (monde) ; 11 125 en France | 71,5 | Mot-clé voisin, pas le nôtre. |

### Vidéos de référence (EN)

Aucune vidéo anglaise ne fait l'ingénierie de Waze en profondeur (« how waze detects traffic », outliers, 12 mois). Les plus proches :

| Titre | Chaîne (abonnés) | Vues | × moyenne | URL | Ce qu'on retient |
|---|---|---|---|---|---|
| Why Do Traffic Jams Happen for No Reason? | The Universe Disagrees (3,9 K) | 859 K (12/10/2026) | ×824 | https://youtu.be/fcyXWJlRKw4 | 6:41. Le bouchon « fantôme » (onde de freinage) : un angle physique que Waze permet de relier à la détection. Le sujet marche en ce moment. |
| Google Maps Won't Find the Fastest Route | decomplex (4,2 K) | 125,9 K (16/05/2026) | ×50 | https://youtu.be/bnKdS4csSoI | 6:44. Le calcul d'itinéraire comme problème, pas comme produit. |
| Google Maps vs Apple Maps vs Waze: Which One Knows the Road Best? | Secrets Of Simple Things (34 K) | 73,7 K (05/05/2026) | ×29 | https://youtu.be/xGkb6mjuloc | 10:39. Comparatif ; montre que Waze + « qui sait mieux » fonctionne. |
| How Does Google Maps Know There's Traffic? | Dan Limb (4,3 K) | 3,5 K (21/08/2026) | ×15 | https://youtu.be/R2yIK5hm79A | 3:43. Même question, pour Google Maps ; peu de vues : le sujet est libre en anglais aussi. |

Transcription : une seule, celle de la vidéo française de Thibaut Dcode (voir plus bas), pour savoir ce qu'il couvre déjà. Pas de transcription EN : aucune référence EN ne traite le sujet.

### Ce qui existe en français (recherche « comment fonctionne waze », FR, 23/10/2026)

| Titre | Chaîne | Vues | Date | Angle (à ne pas copier) |
|---|---|---|---|---|
| LA FACE SOMBRE DERRIÈRE LA GRATUITÉ DE WAZE | Thibaut Dcode (85,2 K) | 1 163 955 | 13/09/2026 (20:50) | Business : rachat à 966 M$, modèle gratuit, maires contre l'algorithme, loi sur les contrôles. Le mécanisme technique tient en ~1 min (« deux informations en continu : où vous êtes, à quelle vitesse », puis le pouce levé). |
| Le SECRET que Waze te CACHE (et qui change tes trajets) | Zenko (5,2 K) | 147 146 | 20/11/2025 (23:12) | Histoire + impact sur les villes, « tu deviens une donnée ». Pas d'ingénierie. |
| CONFIGURATION WAZE : 92 % DES AUTOMOBILISTES FONT CETTE ERREUR | Astuces Privées (228 K) | 522 959 | 12/11/2025 | Tuto de réglages. |
| J'ai désinstallé Waze pour cette appli Française | Formation informatique (109 K) | 405 313 | 15/07/2026 | Alternative (RouleMap). |
| Utilisez WAZE comme un PRO | Formation informatique (109 K) | 393 953 | 30/04/2025 | Astuces. |
| Waze : l'application de navigation innovante et communautaire | Geeko (5,2 K) | 26 231 | 14/09/2021 (4:04) | Histoire courte, d'après un article. |
| Waze vs Google : la battle du GPS le plus rapide | RTBF (339 K) | 11 905 | 05/03/2026 | Test à Bruxelles. |

Outliers FR (6 mois, « waze comment ça marche bouchon ») : rien de pertinent sur le mécanisme. Le seul résultat Waze est une alternative (« Marre de Waze ? Roole Map », 29,4 K vues, ×86).

### Ce que ça dit pour nous

- Demande réelle sur « waze » (9,7 K/mois en France, +32 %), nulle sur « comment fonctionne waze » (< 750). Le clic viendra des suggestions (à côté de Thibaut Dcode, 1,16 M vues) plus que de la recherche.
- Angle libre : **personne en français, ni en anglais, ne détaille la machine** (détection par la vitesse des téléphones, historique par demi-heure, mélange temps réel / historique, reroutage). Thibaut Dcode y consacre environ une minute sur 20.
- Mots du titre : « Waze », « bouchon », « comment » ; « avant que tu le voies » porte l'enjeu. Éviter « gratuit », « face sombre », « données », qui sont son territoire.
- Ajouter en description et chapitres « waze vs google maps » (4 352 + 8 230 recherches/mois, concurrence 21 à 30).
- Tendance voisine : la vidéo « bouchons sans raison » fait ×824 sur 7 jours : un sas d'entrée possible (le bouchon fantôme).

## Faits

| # | Affirmation (telle qu'on la dirait) | Source (URL ; auteur, date) | 1re vérif | 2e vérif |
|---|---|---|---|---|
| 1 | Waze fabrique ses infos de bouchon à partir des points GPS envoyés par les téléphones des conducteurs qui utilisent l'appli. | Waze Partners Help, « Waze Data Feed specifications », https://support.google.com/waze/partners/answer/13458165 (v3.0, avril 2023 ; page non datée) : « GPS location-points sent from user phones (users who drive while using the app) ». | ✅ source primaire lue | ✅ relu : « GPS location-points sent from user phones (users who drive while using the app) ». |
| 2 | Il compare la vitesse moyenne actuelle d'un tronçon à sa vitesse « fluide » (free-flow). | Même page. | ✅ | ⚠️ la page définit le free-flow comme la « maximum speed measured on the road-segment ». Dire : « il compare la vitesse de maintenant à la vitesse fluide du tronçon, la plus haute qu'on y ait mesurée ». |
| 3 | Waze signale un ralentissement quand un tronçon roule sous la vitesse moyenne habituelle pour cette heure du jour et ce jour de la semaine, puis recoupe avec les signaux GPS et les signalements. | Waze Partners Help, « Get traffic data with the Waze Data Feed », https://support.google.com/waze/partners/answer/10618035 (page non datée) : « traffic on a segment is below average speed for that time of day or week ». | ✅ | ✅ relu mot à mot : « When traffic on a segment is below average speed for that time of day or week, we identify it as a slowdown or jam. These are then compared with user GPS signals and user reports. » |
| 4 | Les signalements des conducteurs « affectent la manière dont on identifie et présente les bouchons » : ils complètent la vitesse, ils ne la remplacent pas. | https://support.google.com/waze/partners/answer/13458165 | ✅ | ⚠️ la citation est exacte (« These appear as regular alerts, and also affect the way we identify and present traffic jams »). « Ils ne la remplacent pas » est notre lecture, pas une phrase de Waze. Dire : « tes signalements s'affichent comme des alertes et pèsent aussi sur la façon dont Waze repère les bouchons ». |
| 5 | Chaque bouchon a un niveau de congestion de 0 (fluide) à 5 (bloqué) et un retard en secondes par rapport au fluide. | Même page (champs `level` et `delay`). | ✅ | ✅ relu : « 0 = free flow 5 = blocked » ; delay en secondes, −1 si la route est bloquée. |
| 6 | Le flux de données de Waze pour les partenaires est mis à jour toutes les 2 minutes. | https://support.google.com/waze/partners/answer/10618035 : « updated every 2 minutes » | ⚠️ ✅ pour le flux partenaires ; la latence interne du moteur de routage n'est pas publiée. À ne pas présenter comme « Waze sait en 2 minutes ». | ✅ relu (« updated every 2 minutes ») pour le flux des partenaires seulement. La page 13458165 ne donne pas de fréquence. Ne pas dire « Waze sait en 2 minutes ». |
| 7 | Waze garde l'historique des vitesses moyennes de chaque tronçon pour chaque demi-heure de chaque jour de la semaine : 48 échantillons par jour et par tronçon. | Yigal Petreanu (ingénieur logiciel senior), « Under the Hood: Real-time ETA and How Waze Knows You're on the Fastest Route », blog Waze sur Medium, 27/08/2020, https://medium.com/waze/under-the-hood-real-time-eta-and-how-waze-knows-youre-on-the-fastest-route-78d63c158b90 (lu via archive.org, Medium bloque les robots). | ✅ | ✅ relu (archive du 02/12/2020) : « every half hour of every day of the week. That means we take 48 samples ». Article publié par le compte Waze, signé « Senior Software Engineer Yigal Petreanu », 27/08/2020. |
| 8 | Un jour normal, Waze s'appuie sur l'historique des huit dernières semaines environ pour cette plage horaire : c'est ce qu'il suppose quand il ne sait rien d'autre. | Même article : « On a regular day, we rely on historical information from the past eight weeks or so ». | ✅ | ✅ relu : « the past eight weeks or so for a particular time. That is what we assume the traffic is if we don't know anything else ». |
| 9 | Quand tu gardes l'appli ouverte, tu dis à Waze, sans rien faire, la vitesse actuelle de la portion de route. | Même article : « When Wazers keep the app open, they implicitly tell us the current speed ». | ✅ | ✅ relu : « When Wazers keep the app open, they implicitly tell us the current speed on a specific stretch of the road. » |
| 10 | Waze mélange le temps réel et l'historique dans une équation qui donne la vitesse la plus probable, puis en tire l'ETA. | Même article (l'équation n'est pas publiée). | ✅ pour le principe ; ❓ la formule | ✅ relu (« blend them together in a mathematical equation designed to calculate your most likely speed ») ; la formule n'est pas publiée. |
| 11 | Waze écarte les valeurs extrêmes (conducteurs très lents ou très rapides) avant de calculer la moyenne ; il tient compte du type de véhicule (moto, bus). | Même article. | ✅ | ✅ relu : « We filter out the outliers — the very slow or extremely fast drivers » ; exemples moto et bus. |
| 12 | Une fois sur la route, Waze réévalue la situation toutes les quelques minutes : si ça change peu, il te prévient du retard ; si ça change fort, il te trouve un meilleur itinéraire. Il garde volontairement les itinéraires stables. | Même article : « we assess what is going on every few minutes ». | ✅ | ✅ relu : « we assess what is going on every few minutes » ; « If you're one minute late, there's no point in sending you on a completely new route. » |
| 13 | L'ETA de Waze est volontairement prudent : mieux vaut arriver à l'heure ou en avance. | Même article : « we err on the safe side ». | ✅ | ✅ relu : « we err on the safe side […] better to arrive right on time or a few minutes early ». |
| 14 | Brevet Waze (déposé le 19/05/2008, accordé le 24/06/2014, inventeurs Uri Levine, Amir Shinar, Ehud Shabtai) : les membres envoient leur position à intervalles réguliers avec un horodatage ; le serveur calcule leur vitesse à partir de la variation de position, puis en déduit la vitesse du trafic sur la route ; une zone de bouchon se repère à la vitesse moyenne des membres qui y sont ou qui la précèdent. | US 8 762 035 B2, « System and method for realtime community information exchange », https://patents.google.com/patent/US8762035B2/en (titulaire d'origine Waze Mobile Ltd, ex-LINQMAP) | ✅ source primaire lue (80 % du texte, la fin n'a pas été lue) | ✅ relu (Google Patents) : dépôt 19/05/2008, accordé 24/06/2014, Levine, Shinar, Shabtai, LinqMap devenu Waze Mobile. Citations : « calculate the velocities of the members, for example, based on the changes in the locations » ; « identify traffic jam zone 119 based, for example, on the average velocity of the members ». C'est un brevet : il décrit ce que le système peut faire, pas ce que Waze fait aujourd'hui. |
| 15 | En 2014, des chercheurs du Technion ont créé de faux bouchons sur Waze avec des « bots conducteurs » (des positions GPS truquées) et ont détourné des itinéraires. Sur la carte, le faux bouchon s'affichait à 8 km/h. | M. Ben Sinai, N. Partush, S. Yadid, E. Yahav, « Exploiting Social Navigation », arXiv:1410.0151, 01/10/2014, https://arxiv.org/abs/1410.0151 | ✅ lu (texte extrait du PDF) ; ⚠️ 2014, l'algorithme a pu changer | ⚠️ relu (PDF arXiv) : 15 bots, campus du Technion (Haïfa), bouchon affiché « 8kph » ✅. Mais « ont détourné des itinéraires » en rajoute : ils montrent que l'itinéraire que Waze leur proposait a changé (1,5 km et 3 min avant, 1,6 km et 4 min après) et écrivent qu'ils pourraient « potentially » envoyer d'autres conducteurs ailleurs. Dire : « ils ont fabriqué un faux bouchon, et Waze a changé l'itinéraire qu'il proposait ». Toujours dater : 2014. |
| 16 | Dans cette étude, le calcul de congestion de Waze est « relatif » : une route est congestionnée si sa vitesse moyenne actuelle est nettement plus basse que ses vitesses habituelles. Des bots à l'arrêt ou qui ralentissent dans une zone déjà lente (campus) ne créaient aucun bouchon. | Même article, section 2.2 (« the WAZE congestion reporting algorithm is a relative one »). | ✅ (déduction expérimentale des auteurs, l'algorithme n'est pas public) | ✅ relu, section 2.2 (« it seems that the WAZE congestion reporting algorithm is a relative one ») : c'est une déduction des auteurs. Bots immobiles : pas de bouchon, Waze y voyait sans doute des gens qui viennent de lancer l'appli sans avoir démarré. Il a fallu faire rouler les bots à 70 km/h, puis ralentir. |
| 17 | Dans la même étude, Waze ne faisait aucun effort observable pour distinguer l'humain de la machine. | Même article. | ✅ ⚠️ en 2014 | ✅ relu : « WAZE makes no observable effort to differentiate human from machine behavior ». Dire « en 2014 ». |
| 18 | Un signalement d'un conducteur ou le « pouce levé » est un 2e étage : les gens qui signalent un accident ajoutent une info, mais les bouchons sortent d'abord de la vitesse. | Recoupement des faits 1, 3 et 4 (documentation Waze Partners). | ✅ (déduction de la documentation, pas une phrase Waze) | ⚠️ déduction juste des faits 1, 3, 4, pas une phrase de Waze. Dire : « le bouchon sort d'abord des vitesses ; les signalements viennent le confirmer et le préciser ». |
| 19 | **Hook** : Waze peut détecter un ralentissement avant qu'un conducteur ne le signale, parce que la détection vient de la vitesse des téléphones, pas des signalements. | Faits 1 à 4, 9, 14. | ✅ pour le mécanisme. ⚠️ Les mots « un accident que personne n'avait signalé » : Waze détecte un ralentissement, pas un accident ; le délai de détection et le nombre minimal de conducteurs ne sont pas publiés. Dire « un ralentissement que personne n'avait signalé ». | ⚠️ confirmé : Waze détecte un ralentissement, il ne sait pas que c'est un accident tant que personne ne le signale. Délai et nombre de conducteurs non publiés. Voir ligne 29. |
| 20 | Les sessions actives de Waze (itinéraire en cours, position de l'utilisateur, signalements des conducteurs) vivent dans un serveur de sessions adossé à Memorystore for Redis Cluster ; les tests de charge montent à 1 million de commandes MGET par seconde avec une latence inférieure à la milliseconde. | Eden Levin (infra backend Waze) et Yuval Kamran (SRE Waze), Google Cloud Blog, 15/11/2025, https://cloud.google.com/blog/products/databases/how-waze-keeps-traffic-flowing-with-memorystore | ✅ ; ⚠️ « 1 million » est un résultat de test de charge, pas forcément le trafic réel | ✅ relu (Levin et Kamran, 15/11/2025) ; la phrase exacte : « Load testing proved the new architecture can sustain full production traffic, comfortably handling bursts of up to 1 million MGET commands per second with a stable sub-millisecond service latency ». Dire « en test de charge, des pointes jusqu'à un million de lectures par seconde ». |
| 21 | Waze compte environ 151 millions d'utilisateurs actifs par mois (décembre 2022). | Juby Babu, Reuters, 08/12/2022, https://tech.yahoo.com/general/articles/google-merge-mapping-waze-maps-073236632.html | ⚠️ agence de presse, chiffre vieux de près de 4 ans | ⚠️ 151 M repris par plusieurs titres à partir de la dépêche Reuters du 08/12/2022 (Engadget, MobileSyrup…) ; dépêche d'origine non rouverte, pas de chiffre officiel plus récent trouvé. Dire « environ 150 millions d'utilisateurs par mois fin 2022 ». |
| 22 | Waze est né en 2006 à Tel Aviv sous le nom FreeMap Israel, un projet communautaire d'Ehud Shabtai : une carte gratuite faite par les conducteurs. | Wikipédia EN « Waze » (notes 9, 10, archives de FreeMap) ; Thibaut Dcode raconte la même chose. | ⚠️ seconde main (Wikipédia), à remonter aux archives de FreeMap | ⚠️ toujours Wikipédia seule : FreeMap Israel lancé en 2006 par Ehud Shabtai, société Waze en 2008, renommée Waze Mobile en 2009. « Tel Aviv » non confirmé. Dire : « Waze est né d'une carte communautaire israélienne, FreeMap Israel, lancée en 2006 ». |
| 23 | Google a racheté Waze en juin 2013 pour 966 millions de dollars en numéraire (847 M$ de survaleur, 188 M$ d'actifs incorporels, 69 M$ de passifs nets). | Alphabet/Google, formulaire 10-Q du 2e trimestre 2013, SEC, https://www.sec.gov/Archives/edgar/data/0001288776/000128877613000055/goog10-qq22013.htm | ✅ source primaire lue. Wikipédia EN dit 1,3 Md$ : c'est faux par rapport au dépôt SEC. | ✅ relu dans le 10-Q (note 6) : « total cash consideration of $966 million », 847 M$ de survaleur, 188 M$ d'incorporels, 69 M$ de passifs nets, sur une évaluation « préliminaire ». La presse de 2013 parlait de 1,1 à 1,3 Md$ : ne pas dire que Wikipédia a tort, dire « 966 millions de dollars en numéraire, d'après les comptes de Google ». |
| 24 | La routine de routage de Waze préfère le temps réel à l'historique et découpe l'historique en tranches de 10-15 minutes. | Wazeopedia (wiki communautaire), page « Routing server », https://www.waze.com/discuss/t/routing-server/379517 | ⚠️ wiki de bénévoles, « observation et spéculation » de leur propre aveu. Conflit avec le fait 7 (demi-heure, source Waze). Utiliser le fait 7. | ⚠️ relu : le wiki prévient lui-même (« based on observation, speculation ») et se contredit (tranches de « 10-15 minute » puis « as small as 30 minutes »). Ne pas utiliser. |
| 25 | Un téléphone immobile (station-service, drive) peut créer de faux ralentissements. | Forum Waze, https://www.waze.com/discuss/t/show-streets-speeds-all-the-time/98470 | ⚠️ message d'utilisateur | ⚠️ relu : deux messages de l'utilisateur « gettingthere », 15/03/2012, pas de Waze. Et l'étude du Technion (2014) montre que des téléphones immobiles ne créaient pas de bouchon. Ne pas l'affirmer. |
| 26 | Le brevet US 8 433 505 « faster detection of traffic jams » (fermer le tronçon tôt si on avance trop lentement) n'est **pas** un brevet Waze : titulaire d'origine Research in Motion, inventeur Seth Olds Rogers, déposé le 01/07/2010. | https://patents.google.com/patent/US8433505B2/en | ❌ piège : ne pas l'attribuer à Waze. Peut servir d'illustration de l'idée générale (sondes), en le disant. | ✅ relu : titulaire Research in Motion, inventeur Seth Olds Rogers, dépôt 01/07/2010 (priorité 29/12/2009) ; exemple « average speed is less than 15 mph ». Ce n'est pas un brevet Waze. |
| 27 | « Si votre vitesse tombe à 15 km/h sur une voie limitée à 130, l'appli apprend que ça bouche » (exemple de Thibaut Dcode). | Transcription de sa vidéo (13/09/2026). | ❓ le seuil de 15 km/h n'est dans aucune source Waze lue ; le brevet RIM (fait 26) cite 15 mph (≈ 24 km/h) comme exemple. Ne pas reprendre. | ❓ confirmé : aucun seuil de 15 km/h dans les sources Waze relues (transcription vidIQ non relue, pas de crédit dépensé). Ne pas reprendre. |
| 28 | La documentation Waze n'indique pas combien de téléphones il faut pour déclencher un bouchon, ni le délai de détection. | Absence dans les pages 13458165 et 10618035, l'article Medium de 2020 et le brevet. | ❓ introuvable | ❓ confirmé absent des pages Waze, de l'article de 2020 et du brevet. Seul repère : en 2014, 15 bots ont suffi sur le campus (fait 15) ; ce n'est pas un seuil de Waze. |
| 29 | (ajouté en 2e vérif) Hook de l'idée 6 : « Waze t'a fait tourner à droite. Trois minutes plus tard, tu passes devant un accident que personne n'avait encore signalé. » | `strategie.md`, idée 6 | | ❌ tel quel. Waze ne peut pas savoir qu'il y a un accident si personne ne l'a signalé : il voit seulement que les voitures ralentissent (faits 3, 9). « Trois minutes » est inventé (délai non publié, fait 28). Dire : « Waze t'a fait tourner à droite. Sur la route que tu as évitée, tout le monde est à l'arrêt. Personne ne l'avait signalé. » |
| 30 | (ajouté en 2e vérif) Miniature : « personne ne l'a signalé, il savait. » | `fiche.md` | | ✅ si « il » parle du bouchon : un ralentissement se détecte sans aucun signalement (faits 1, 3, 9). La vidéo doit dire qu'il savait que ça ralentit, pas pourquoi. |
| 31 | (ajouté en 2e vérif) Les 15 premières secondes : « le détour bleu, puis l'accident ». | `fiche.md` | | ⚠️ montrer la route rouge et les voitures arrêtées, pas un accident. Si un accident apparaît, il doit avoir été signalé (icône de signalement) : c'est l'autre étage du système. |
| 32 | (ajouté en 2e vérif) Anecdote : un signalement de voiture sur le bas-côté, et « cinq secondes plus tard » la voiture. | Petreanu, 27/08/2020 (relu) : « I would get a report about a car on the side of the road, and then five seconds later see the exact car. » | | ⚠️ exacte, mais elle parle d'un **signalement** fait par d'autres conducteurs, pas de la détection par la vitesse. À placer dans la partie signalements, pas comme preuve du hook. |
| 33 | (ajouté en 2e vérif) Le mantra de l'ingénieur. | Petreanu, 27/08/2020 (relu) : « I'm waiting here, but I'm helping other people who are about to use Waze. » | | ⚠️ la phase 1 traduit « je suis coincé » : dire « j'attends ici, mais j'aide ceux qui vont prendre Waze après moi ». |
| 34 | (ajouté en 2e vérif) En 2014, 15 bots ont suffi pour le faux bouchon, qui restait sur la carte environ 20 minutes après l'arrêt des bots. | arXiv:1410.0151, section 2.2 (relu) : « only 15 bots » ; « persists for roughly 20 minutes past the point where the bots stop driving » | | ✅ (2014, campus). |
| 35 | (ajouté en 2e vérif) Titre : Waze sait qu'il y a un bouchon avant que tu le voies. | Faits 1, 3, 9 | | ✅ pour le mécanisme : les téléphones des voitures devant toi ralentissent avant que tu arrives. Ne pas chiffrer l'avance (fait 28). |
| 36 | (ajouté au grill, vérifié le 23/10/2026) L'anecdote de la voiture sur le bas-côté date des débuts de Petreanu chez Waze, et c'est comme ça qu'il a su qu'il pouvait faire confiance à l'appli. | Petreanu, 27/08/2020 (archive web.archive.org de l'article Medium, relue au grill) : « In my early days at Waze, I was on the road a lot […] I knew I could trust the app because it had proven to me that Waze knows what's going on. » | | ✅ Dire « à ses débuts chez Waze ». |
| 37 | (ajouté au grill, vérifié le 23/10/2026) Le mantra est bien le sien, quand il est dans un bouchon, et il ajoute que les gens derrière lui auront peut-être un itinéraire qui contourne le bouchon. | Même article : « I have a mantra for myself when I run into traffic: I'm waiting here, but I'm helping other people who are about to use Waze. The people behind me might get a route that goes around the traffic ». | | ✅ « might » : dire « peut-être ». Tient la fin (« le Karim, c'est toi »). |
| 38 | (ajouté au grill, vérifié le 23/10/2026) Les bots du Technion étaient des téléphones Android simulés (émulateurs) qui faisaient tourner la vraie appli Waze avec des positions GPS fabriquées. Ordre des essais : bots immobiles (échec), ralentissements progressifs à 15, 8 puis 2 km/h (échec : le campus est une zone lente), puis un départ à 70 km/h suivi du ralentissement (bouchon). | arXiv:1410.0151, version HTML https://arxiv.org/html/1410.0151v1 (relue au grill) : « Android Developer Tools software emulator » ; client Waze Android 3.5.1.4 ; « a small Android application which generates mock GPS locations » ; « Our initial attempts at simulating congestion consisted of spawning botnets » ; « This scenario still failed to yield congestion » ; « we added another phase […] where driving was initiated at 70kph ». | | ✅ (2014). La « zone déjà lente » est l'explication des chercheurs, pas un essai à part. |
| 39 | (ajouté au grill, vérifié le 23/10/2026) Dans Waze, on peut signaler notamment le trafic, la police, un accident et des dangers. | Aide Waze, « Personnaliser les alertes », https://support.google.com/waze/answer/13786535?hl=fr (page non datée) : « Trafic », « Police », « Accident », « Dangers » ; les alertes disponibles varient selon la région. | | ✅ Dire « un danger », pas « un objet sur la route » (ce n'est pas un nom du menu). |
| 40 | (ajouté au grill, vérifié le 23/10/2026) Dans GTA 5, le niveau de recherche va de zéro à cinq étoiles. | Guides de jeu (Prima Games, « Grand Theft Auto V: Evasion Tips » ; WhatCulture, « 10 Tips For Surviving A 5 Star Wanted Level ») : cinq étoiles au maximum. | | ✅ fait de culture pop, pour la blague de la section 2. |

## Matière pour le script

**Chiffres forts**
- 48 échantillons de vitesse par tronçon et par jour, sur environ 8 semaines (faits 7, 8) : Waze sait ce qui est « normal » pour le mardi à 8 h 30 sur ce bout de route.
- Le bouchon vient d'une **comparaison** : vitesse maintenant contre vitesse habituelle (faits 3, 16). Une route lente depuis toujours n'est pas un bouchon (campus de 2014, fait 16).
- Toi, qui n'as rien signalé, tu es déjà un capteur : « chaque Wazer contribue rien qu'en ayant l'appli ouverte » (fait 9).
- Mise à jour du flux partenaires toutes les 2 minutes (fait 6, avec la réserve).

**Démonstrations en motion design**
1. Une route découpée en tronçons ; des points de téléphones qui avancent ; la vitesse de chaque point se calcule par la différence de position entre deux envois (fait 14). Le tronçon devient rouge quand la moyenne chute sous la ligne « normal pour mardi 8 h 30 » (faits 3, 7).
2. La frise de 48 demi-heures de la journée avec une courbe de vitesse habituelle ; la courbe réelle qui plonge sous elle.
3. Le détour : la voiture bleue reroutée « si ce n'est qu'une minute de retard, on ne change rien ; si c'est dramatique, on change » (fait 12).
4. La séquence « le faux bouchon » (fait 15) : une dizaine de points fantômes qui ralentissent et le tronçon devient rouge à 8 km/h. Elle montre à l'écran que ce sont bien les téléphones qui font le bouchon, et pose la limite du système.
5. Réseau de sessions (fait 20) : un point = une session avec position + itinéraire ; en option, pour une courte séquence « 1 million de lectures par seconde ».

**Anecdotes sourcées**
- L'ingénieur Yigal Petreanu dit qu'au début, il recevait le signalement d'une voiture sur le bas-côté, puis « cinq secondes plus tard » voyait la voiture (blog Waze, fait 7 pour la source). Anecdote de l'ingénieur de Waze, pas de l'auteur.
- Le mantra du même ingénieur : « je suis coincé, mais j'aide ceux qui vont utiliser Waze » (même article).
- Les chercheurs du Technion fabriquent un bouchon avec des bots (fait 15).
- Anecdote de l'auteur sur Waze : [à demander à l'auteur].

**Questions que se pose le public** (déduites des vidéos et titres, pas de commentaires lus) : comment Waze sait que ça bouche si personne ne signale ? Pourquoi Waze me fait-il passer par des petites rues ? Pourquoi Waze et Google Maps ne donnent pas le même temps ? Est-ce que Waze utilise mes données ? (angle de Thibaut Dcode : à ne pas traiter).

## Points ouverts

- **Le hook doit changer d'un mot** : « un ralentissement que personne n'avait signalé », pas « un accident » (fait 19).
- Latence réelle de détection et nombre minimal de téléphones : non publiés (fait 28). Ne pas inventer de chiffre ; dire « Waze ne le dit pas ».
- La page d'aide **utilisateur** de Waze (support.google.com/waze/) n'a pas été retrouvée (URL testée : 404). Les deux pages « Partners » sont des sources primaires Waze mais destinées aux villes partenaires.
- Pas de talk d'ingénierie Waze (Google Cloud Next, etc.) retrouvé sur l'algorithme de bouchon. Piste : chercher « Waze » sur le canal Google Cloud Tech.
- Le fait 16 vient d'une étude externe de 2014 : à relire par la phase 2 avant de l'écrire au présent.
- Le fait 21 (151 M) est de décembre 2022 : vérifier s'il y a un chiffre 2025-2026.
- Chiffres vidIQ à 23/10/2026 ; 7 appels vidIQ pour ce sujet (35 crédits) : 2 recherches de mots-clés, 2 recherches YouTube, 2 outliers, 1 transcription.

## Pour le script : ce qu'on peut dire, ce qu'on ne dit pas

**Formulations sûres**
- « Chaque téléphone qui roule avec Waze ouvert envoie sa position GPS ; c'est avec ça que Waze fabrique ses bouchons. » (faits 1, 9)
- « Waze connaît la vitesse normale de chaque bout de route, pour chaque demi-heure de chaque jour de la semaine : 48 mesures par jour, sur environ huit semaines. » (faits 7, 8)
- « Un bouchon, pour Waze, c'est une comparaison : on roule nettement moins vite que d'habitude à cette heure-là. » (faits 3, 16)
- « Tes signalements s'affichent comme des alertes, et ils pèsent aussi sur la façon dont Waze repère les bouchons. » (fait 4)
- « Waze écarte les conducteurs trop lents et trop rapides, et mélange le temps réel et l'historique dans une équation qu'il ne publie pas. » (faits 10, 11)
- « Toutes les quelques minutes, il refait le calcul : pour une minute de retard, il ne change rien ; si ça change beaucoup, il te trouve une autre route. » (fait 12)
- « En 2014, des chercheurs du Technion ont fabriqué un faux bouchon avec 15 faux conducteurs ; Waze l'affichait à 8 km/h et a changé l'itinéraire qu'il proposait. » (faits 15, 34)
- « Google a payé Waze 966 millions de dollars en 2013, d'après ses propres comptes. » (fait 23)
- « En test de charge, ses serveurs de sessions encaissent des pointes d'un million de lectures par seconde. » (fait 20)

**Interdit ou à dire autrement**
- « Un accident que personne n'avait signalé » → « un ralentissement que personne n'avait signalé » (lignes 19, 29).
- « Trois minutes plus tard », « Waze sait en 2 minutes », un nombre de voitures nécessaire : rien de publié (faits 6, 28).
- « 15 km/h sur une voie à 130 » (fait 27) et le brevet « faster detection of traffic jams » présenté comme celui de Waze (fait 26).
- « Un téléphone à la station-service crée un faux bouchon » : message de forum, contredit par l'étude de 2014 (fait 25).
- Les tranches de 10-15 minutes de Wazeopedia (fait 24) : dire « par demi-heure » (fait 7).
- « Des chercheurs ont détourné des milliers de conducteurs » : ils ont montré l'itinéraire changé sur leur test (fait 15).
- « Waze a 151 millions d'utilisateurs » au présent : dire « fin 2022 » (fait 21).
- Le rachat à « 1,3 milliard » : dire 966 millions en numéraire (fait 23).
