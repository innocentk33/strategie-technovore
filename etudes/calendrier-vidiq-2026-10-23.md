# Recherche vidIQ sur tout le calendrier (23/10/2026)

> Faite le 23/10, avant le passage au forfait gratuit du 12/11. Elle a servi aux 14 scripts écrits d'avance (génie, histoires, « Louer, acheter »).
> - Le détail de chaque sujet est dans `projets/<nom>/sources.md` : mots-clés, références, faits avec double vérification.
> - Le radar des idées du 8 mars est dans [`radar.md`](radar.md) (entrée du 23/10).
> - Tous les chiffres viennent de vidIQ au 23/10. Les volumes sont mondiaux, sauf quand la part de la France est donnée.

## Sujet par sujet

| Lundi | Sujet | Mot-clé principal (volume par mois) | Meilleure référence | En français | Verdict |
|---|---|---|---|---|---|
| 9 nov | [Waze](../projets/waze/sources.md) | « waze » 45,5 K (9,7 K en France, +32 %) ; « comment fonctionne waze » moins de 750 | Aucune vidéo d'ingénierie sur Waze. Voisine : *Why Do Traffic Jams Happen for No Reason?* (859 K, ×824) | Thibaut Dcode, 1,16 M (business, 1 min sur le mécanisme) | **Garder.** Le hook dit « un ralentissement que personne n'avait signalé », pas « un accident » |
| 23 nov | [Pseudo](../projets/pseudo/sources.md) | « bloom filter » 17,1 K (+240 %) ; « pseudo déjà pris » moins de 750 | ByteMonk, 707 K (×21,7) ; Short KodeKloud, 156 K en 2 jours (21/10) | Rien au-dessus de 10 K | **Garder, angle à revoir** : aucun grand site sourcé ne vérifie les pseudos avec un filtre de Bloom, et « en une milliseconde » n'est pas sourcé |
| 7 déc | [iPhone](../projets/iphone-fluide/sources.md) | « iphone fluide » moins de 750 | Aucune vidéo d'ingénierie. Demande : Trevor Nace, 120 Hz caché (354 K, ×43) ; Enrico Tartarotti, *The Ridiculous Engineering Of Animations* (288 K en 5 jours, radar du 23/10) | Short CED « fluidité Android » (978 K) | **Garder.** Le mythe de la « priorité temps réel » d'iOS est faux. Android fait 83 % du mobile en Afrique (StatCounter, sept. 2026) |
| 14 déc | [Pixel](../projets/pixel/sources.md) | « jeux vidéo » 24 K ; « histoire du jeu vidéo » moins de 750 | TierLine, consoles les plus vendues (198 K, ×68) | Tech'Antik, Pong (2,5 K) | **Garder.** Trancher entre 3,6 milliards (Newzoo 2025 : 3,578) et 3,70 (2026, préliminaire) |
| 28 déc | [Python](../projets/python/sources.md) | « python » 1,1 M (12,6 K en France) | CultRepo, *Python: The Documentary* (1,29 M) | Codabee, *Il s'ennuyait à Noël: Il a créé Python* (263 vues, 18/09/2026) | **Titre et hook à revoir** : Codabee a pris le titre, et Guido ne dit jamais qu'il s'ennuyait |
| 4 janv | [Louer, acheter](../projets/louer-acheter-ia/sources.md) | « ia local » 108 K (11,4 K en France) ; « ia en local » 21,4 K (+91 %) | Kai, 326 K (×8,2) | Personne ne compare en euros | **Garder.** Prix relevés le 23/10, **2e relevé avant la sortie** |
| 11 janv | [WhatsApp](../projets/whatsapp/sources.md) | « whatsapp » 388 K (2,4 K en France) | Enrico Tartarotti, *The Insane Design Of Messaging* (1,67 M), qui parle de **design, pas de serveurs** | Thibaut Dcode, 207 K (business, 32 ingénieurs en une phrase) | **Garder.** 32 ou 35 ingénieurs au rachat (2014), 50 en 2015 |
| 25 janv | [Windows Phone](../projets/windows-phone/sources.md) | « windows phone » 21,5 K (−50 %) | Apple Explained, *Why The Windows Phone Failed* (3,22 M, ×8,2) | by amx (18,9 K, 2024) | **Garder** : l'angle des applis n'existe nulle part. WhatsApp arrive onze mois après le lancement, pas « des années » |
| 8 févr | [llama.cpp](../projets/llama-cpp/sources.md) | « ollama » 335 K (9,8 K en France) ; « llama.cpp » 21 K | Codacus, guide llama.cpp (426 K, ×89) ; un seul récit en anglais (109 vues) | Aucun récit | **Garder.** Premier commit le 10/03/2023 (API GitHub) |
| 22 févr | [Jeux possédés](../projets/jeux-possedes/sources.md) | « stop killing games » 92 K (2,9 K en France, +38 %) ; « the crew » 91 K | SuperJoshua06, *I will NEVER Buy a Digital Only PlayStation* (222 K, ×35) | Pico, 494 K (angle disque et jailbreak, inspiration de l'auteur) | **Garder, sujet chaud**, avec un créneau à rediscuter avant GTA 6 (19/11) |
| 8 mars | [Lag des jeux en ligne](../projets/lag/fiche.md) | « lag jeux en ligne » moins de 750 ; « lag » 23 K | DeadInSperanza (×108), Tariq10x (297 K) | Aucune vidéo | **Choisie au radar du 23/10** |
| 22 mars | [SQLite](../projets/sqlite/sources.md) | « sqlite » 13,4 K ; « comment fonctionne sqlite » moins de 750 | ByteMonk, 221 K (×12,6) | Olivier Poncet, un live de 43 min (8,2 K) | **Titre à changer** : « 300 Ko » est faux (590 à 750 Ko d'après sqlite.org), « certifié DO-178B » aussi |
| 5 avr | [Sans contact](../projets/sans-contact/sources.md) | « paiement sans contact » moins de 750 ; « nfc » 116 K | ByteMonk, 195 K (×4,4) | Konbini 2021 (145 K), Frandroid 2019 (199 K) : risques, pas d'ingénierie | **Garder (provisoire).** Le paiement NFC parle-t-il à ton public africain ? [à te demander] |
| 19 avr | [Écran blanc](../projets/ecran-blanc/sources.md) | « comment fonctionne un écran » moins de 750 | Enrico Tartarotti, 761 K (×6,8) ; Andy Geers (×431) | Rien sur les sous-pixels | **Garder (provisoire).** « Pas de blanc » est à nuancer : le rétroéclairage LCD est blanc, et les dalles WRGB de LG ont un sous-pixel blanc |

**Crédits** :
- environ 650 dépensés le 23/10 (3 agents de recherche, le radar des idées et le lag) ;
- solde au 23/10 au soir : voir le dernier `vidiq_balance` ;
- **8 appels ont échoué** sur une erreur du proxy (« Invalid content from server ») et ont peut-être été facturés.

---

## Banque du radar IA (pour les 9 créneaux IA)

À reprendre à chaque radar à partir du 30/11. Après le 12/11, on n'aura plus que 150 crédits par mois.

### Mots-clés

| Mot-clé | Volume par mois | Sur 30 jours | Concurrence | France |
|---|---|---|---|---|
| ia en local | 21 403 | **+91 %** | 41,6 | n/d |
| ia local | 108 220 | −19 % | 47,1 | 11 392 |
| local ai | 278 076 | +30 % | 70 | 10 112 |
| ollama | 334 853 | −7 % | 68 | 9 849 |
| lm studio | 247 760 | +9 % | 59,4 | 2 581 |
| open webui | 61 215 | +4 % | **29,8** | n/d |
| qwen | 179 672 | −19 % | 48,3 | 8 045 |
| gemma 4 | 74 451 | −4 % | 67,5 | 2 978 |
| llama.cpp | 21 080 | −46 % | 53,3 | n/d |
| ollama vs llama.cpp | 4 224 | n/d | **34** | n/d |
| claude code | 2 693 482 | +1 % | 72 | 46 632 |
| carte graphique ia | moins de 750 | n/d | 28 | n/d |

**Ce qu'il faut retenir des mots-clés** :
- le mode `rising` ne renvoie **rien** en français : ne le relance pas, chaque essai coûte 5 crédits. Passe plutôt par `research` sur le nom du modèle ou de l'outil du moment ;
- personne ne cherche « carte graphique ia » : on cherche par modèle (« qwen ») et par outil (« ollama »).

### Vidéos qui dépassent leur chaîne (3 mois)

- **En français**, l'offre est mince : aucune vidéo sur « IA en local » ne dépasse 30 K vues.
  - FEU, podcast « IA en local & Hermes Agent » : 26,2 K, ×10 ;
  - Naier Saidane, « Agents IA en LOCAL de ZÉRO à PRO en 2h00 » : 21,4 K, ×4,2 ;
  - Double Slash, « Faire tourner une IA en local » : 26 K, ×21, en mai.
- **En anglais**, le modèle du moment est Qwen3.8 27B :
  - Red Stapler, « I ran Qwen3.8 27B on single 8GB Card! » : 648 K, ×15 ;
  - RepoChad, « Run Qwen3.8-27B on ANY GPU » : 187 K ;
  - Locally, « The Truth About Running AI On Your Own Hardware » : 139 K, **×725** ;
  - Amir Husain, une carte à 19 $ : 85,5 K, ×158 ;
  - Codacus, un modèle de 35 B sur 6 Go : 426 K, ×89.
- **Trois formes gagnent** :
  - une grosse IA sur une petite carte ;
  - quel modèle pour quelle carte ;
  - le matériel improbable.

### Candidates pour les créneaux IA

| # | Idée | Signal | Format |
|---|---|---|---|
| 1 | Un modèle de 27 B sur 16 Go : jusqu'où ça tient ? | Red Stapler 648 K, RepoChad 187 K | **Testé**, si Q3 ou un déport sur le CPU tient : à mesurer avant de le promettre. 27 B en 4 bits pèsent environ 15-17 Go (estimation de l'agent) |
| 2 | Quel modèle pour quelle carte (4 à 24 Go), en euros | Code Bear, Kai, RepoChad ; rien en français | **Calculé**, avec 1 ou 2 mesures sur la 5080 |
| 3 | Même carte, 2 fois plus rapide : Ollama, llama.cpp ou LM Studio ? (idée 16) | « ollama vs llama.cpp », faible concurrence ; Codacus ×89 | **Testé**, en lien avec llama.cpp du 8 févr. |
| 4 | Ton ChatGPT privé en 10 minutes avec Open WebUI | « open webui » 61 K, la concurrence la plus faible (29,8) | **Testé** (une vidéo qui répond à une recherche précise) |
| 5 | Une IA locale sur un vieux PC ou un portable de 8 Go | Red Stapler (8 Go), Amir Husain (×158), TinyTechGuy (×77) | **Calculé**. C'est le sujet le plus proche du public africain |
| 6 | Des agents IA en local : ce que la 5080 sait faire seule | Naier Saidane (FR), Web Dev Simplified 1,1 M | Testé avec de petits modèles, calculé avec les gros |
| 7 | DeepSeek V4 Flash (284 B) : combien ça coûte vraiment ? | The Stack 209 K | **Calculé** (remonter à antirez.com) |

« Louer ou acheter » est déjà au calendrier (4 janv.). « Ton IA locale est-elle vraiment privée ? » reste en réserve dans `idees.md`.
