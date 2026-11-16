# C. Les mesures de l'auteur dans la vidéo Strata (15/11/2026)

> Relevé des chiffres de vitesse et de mémoire que **tu as toi-même mesurés** sur ta machine (RTX 5080 16 Go, Ryzen 7 9700X, 32 Go de DDR5-6000, Windows) pendant la vidéo [Strata](../../strata-test/fiche.md) (lun. 16/11). Référence de ce qui a été dit : `projets/strata-test/strata-test.fr.srt` (« srt »). Faits et horodatages de tournage : `projets/strata-test/sources.md` (T41, T45), `plan-tests.md`, `storyboard.md`. Rien n'est inventé : ce qui manque est écrit « non relevé ».

## 1. Les chiffres de l'auteur

Conditions communes à toutes les lignes « Strata » (sauf mention) : appli Strata **0.2.13** (moteur **0.1.59**, `sources.md` T1), modèle **Qwen3.8-Flash-Next Coder, fichier IQ1_M** (`coder-iq1_m`, ≈ 58,4 Go à télécharger), contexte **128K** (131 072), harnais **Pi 1.5.2**, réflexion **« high »** (niveau par défaut du serveur, `plan-tests.md` calibrage ; `upload.md` l. 140), `maxTokens` 32 000, navigateur fermé. Vitesse lue sur la page **Monitor** de l'appli (colonne « Decode »). Pi n'affiche pas les tok/s.

| Chiffre | Conditions précises | Où c'est écrit |
|---|---|---|
| **≈ 70 tok/s** « près de 70 en moyenne » | Moyennes du moniteur : **69,4** (18 requêtes du calibrage, 13/11 19:07), **67,8** (45 requêtes, casse-briques compris, 19:46), **66,1** (63 requêtes de Sillage, 14/11 11:30). Plusieurs requêtes par test (une par appel d'outil) | srt (0:03 et 3:14-3:18) ; `sources.md` T45 l. 183 ; `storyboard.md` MON2, MON3, MON4 |
| **Fourchette 43–84** | Requêtes vues au moniteur : de **42,9** (creux, Sillage) à **83,6** (pointe). Affichage en direct « 81.5 t/s Decode now » pendant le calibrage (13/11 19:01) | srt (3:14-3:18) ; `sources.md` T45 ; `storyboard.md` MON1, MON4 |
| **77,2 tok/s** | Requête finie du calibrage (to-do list, 148 lignes), 13/11 vers 19:03. Non dit dans la vidéo | `plan-tests.md` l. 190 |
| **51 tok/s sur l'histoire du dragon** (50,8) | Prompt « Tell me a short story about a dragon who loves video games. », 13/11 19:45:59, **590 tokens écrits** en 13,7 s, 1 849 tokens lus, **presque pas de réflexion** (161 caractères). Avec la lecture du prompt : 42,9. Plus lent que les tests, **cause non expliquée** | srt (3:06-3:11) ; `sources.md` T41 l. 173 et T45 l. 184 ; `storyboard.md` MON3 |
| **Lecture du prompt (Prefill) 102 à 216 tok/s** | Calibrage 13/11 : 1 884 tokens lus en ≈ 8 s. Très loin des ≈ 2 500 mesurés par un tiers sur une 5070 Ti. **Non dit dans la vidéo** | `plan-tests.md` l. 190 |
| **RAM 30,8 / 31 Go** | Pendant que le dragon s'écrit (13/11), barre rouge ; 30,7 / 31 pendant Sillage ; 29,7 / 31 au calibrage ; **24,0 / 31 au repos** (13/11 18:32, avant de lancer) ; Opera ouvert = 3,8 Go (20 processus) au calibrage | srt (4:36-4:41) ; `sources.md` T45 l. 185 ; `storyboard.md` MON0 à MON3 |
| **Lecture disque ≈ 200 Mo/s** | **0,1 Mo/s au repos** ; **165 à 183 Mo/s** pendant le dragon ; **239 Mo/s** (avec 247 Mo/s d'écriture, donc plutôt le fichier d'échange de Windows : 3,3 Go utilisés) en plein calibrage. L'explication « la RAM est pleine, donc une partie passe par le SSD » est une **interprétation**, pas une mesure | srt (4:44-4:51) ; `sources.md` T45 l. 186 ; `plan-tests.md` l. 190 |
| **VRAM** : 2 973 experts en VRAM (5,7 Go) ; VRAM 15,1 / 16 Go au repos, 14,6 / 16 Go au Gestionnaire des tâches (11/11) | Calibrage 13/11 ; non dit dans la vidéo | `plan-tests.md` l. 190 ; `storyboard.md` MON0 ; `sources.md` T45 |
| **Limite de réponse 32 000 tokens** | Réglage **manuel** de `maxTokens` dans `models.json` de Pi (défaut Pi 16 384, ce que Strata écrirait à 128K). **Une seule** coupure à 32 000 sur toutes les sessions (essai 1 du site : `stopReason: length`, 413 s ≈ 7 min) | srt (5:04-5:29) ; `sources.md` T41, T44 |
| **Prompt système de Pi ≈ 1 500 tokens contre ≈ 7 400 pour OpenCode** | **Chiffres du projet Strata** (harness.py, `strata connect`), pas une mesure de l'auteur : Pi 1,5 K, OpenCode 7,4 K, oh-my-pi 7,5 K, Hermes 12,9 K, Claude Code 15,6 K ; testé par eux avec pi 0.74.2 et OpenCode 1.19.3. Calcul : ≈ 5 900 tokens de moins par requête | srt (4:09-4:17) ; `sources.md` T14, T37 |
| **Taille du contexte vu** | 35k / 128K au dragon ; 54k / 128K pendant Sillage ; **vide à 0,0 %** au lancement du dragon | `plan-tests.md` (OCR `dragon.json` : « 35k / 128K ») ; `storyboard.md` MON4 |
| **Durées des tests** | Île **15 min 32** (0 relance, 472 lignes) ; casse-briques **8 min 12** (0 relance, 493 lignes) ; site essai 1 **31 min 33** (1 282 lignes, anglais) ; site avec plan de Claude **16 min 57** pour Sillage (le srt dit « 17 minutes »), 2 blocages Chrome ; mini-Minecraft **34 min 58** (3 relances, dont 23 min 08 de travail du modèle) ; blocages Chrome **2 h 22** cumulées. **Ce sont des durées de tâche, pas des vitesses de moteur** | srt (0:48-1:42 et 5:20-7:00) ; `sources.md` T41 |
| **Téléchargement / premier lancement** | Clic « Download model » ≈ 19:30 → premier message 20:06 (11/11), un peu plus d'une demi-heure, 58,4 Go compris. Le srt dit « un peu moins d'une demi-heure » | srt (4:26-4:32) ; `sources.md` T45 |
| **Claude, site de voyage** | **< 2 min 30** en français, un prompt d'une phrase, **pas le même prompt** que le modèle local (non comparable). Latitude Sud : 2 min 23 s après la demande | srt (7:03-7:25) ; `sources.md` T42 |
| **Version du moteur** | Appli 0.2.13 (09/11), moteur 0.1.59. Dans la vidéo, la voix dit seulement « la version que j'ai testée » et « note bien ta version » ; **aucun numéro n'est dit** | srt (7:44-8:07) ; `sources.md` T1 ; `upload.md` l. 140 |
| **Réflexion** | « Allumée » (niveau high) ; mesurée **sans** la couper : aucun test de l'auteur avec réflexion coupée | srt (3:28-3:36) ; `plan-tests.md` l. 190 |
| **Machine** | RTX 5080 16 Go (Inno3D X3 OC, 960 Go/s), Ryzen 7 9700X, 32 Go DDR5-6000 EXPO, SSD 990 EVO Plus 2 To + P3 Plus 1 To (le fichier du modèle est sur `D:\Strata`, **disque exact non relevé**) | `claude-ou-mon-pc-1/modeles-5080.md` l. 7 ; `plan-tests.md` |

Chiffres du srt qui **ne sont pas** à l'auteur (à ne pas lui attribuer) : 70 tok/s d'un utilisateur de 5070 Ti (srt), 37 tok/s d'une Radeon 16 Go (srt), « de 59 à 43 tok/s » du projet sur une autre machine avec un ancien moteur (srt), 81 contre 74 et 95 % (Qwen), 125 milliards dont 6 actifs.

## 2. Le point clé : une paire avant/après chez l'auteur ?

**Aucune paire avant/après mesurée chez l'auteur.** Recherche faite dans : le srt, `sources.md`, `plan-tests.md`, `script.md`, `storyboard.md`, `teleprompteur.txt`, `upload.md`, `claude-ou-mon-pc-1/modeles-5080.md`, et les fichiers texte du montage `/Users/innocent/HyperStudio/premium-noir/2026-11-strata-test/` (il n'y a ni CSV, ni log du moniteur : seulement des sorties OCR des plans, `edit-plan/ocr/*.json`, et les captures `MON0`-`MON4`). Cas examinés, tous écartés :

- **Une seule configuration** : Strata 0.2.13 / moteur 0.1.59, un seul fichier (IQ1_M), un seul modèle, contexte 128K fixe, réflexion « high » fixe. Aucun réglage n'a été changé entre deux mesures de vitesse.
- **Deux versions du moteur** : non. Les 114,1 → 85,5 tok/s (0.1.54 → 0.1.56) sont d'un tiers (« baiqvesse », autre machine, 64 Go, autre fichier) ; le « de 59 à 43 » est du projet.
- **Avec / sans réflexion** : non. Le dragon (presque pas de réflexion, 51 tok/s) et les tests (réflexion longue, ≈ 70) sont **deux prompts différents** : différence de tâche, pas de réglage. Le srt le dit lui-même (« bizarrement »), sans cause (`sources.md` T45 : « non expliqué, ne pas inventer de raison »).
- **Pi contre OpenCode** : non. OpenCode n'a jamais tourné (plan B, section 9.10) ; les 1 500 / 7 400 sont des chiffres du projet.
- **Contexte court contre long** : pas de série. On a seulement des points isolés (contexte à 0 % au lancement du dragon, 35k au dragon, 54k pendant Sillage) avec des moyennes sur des **tâches différentes** ; le creux de 42,9 est dans Sillage mais **aucune corrélation avec le contexte n'a été relevée**.
- **Navigateur ouvert / fermé** : l'ordre de calibrage a eu lieu avec Opera ouvert (3,8 Go), puis le plan demandait de refaire la mesure fermé ; **aucun résultat comparatif noté** dans les fichiers lus.
- **Claude contre le modèle local** : prompts différents (« pas de faux match », srt (7:09-7:13)).
- **LM Studio** : aucune mesure de l'auteur. Le plan d'essais du 23-24/10 (`modeles-5080.md`) a été **abandonné le 25/10** (« plus d'essais »). Tous les tok/s de ce fichier sont des estimations ou des mesures de tiers (13 tok/s Q4 qui déborde, 53,4 → 101,3 avec MTP par sudoingX, 17 et 40 par Luke's Dev Lab).
- **MTP / cache KV / quantification** : jamais touchés par l'auteur (le Coder IQ1_M ne démarre sans doute pas sans MTP, `sources.md` T11 ; la voix du projet T30 dit « MTP activé »).

Conséquence pour la vidéo du 19/11 (`fiche.md` : « calculée, aucune vitesse à toi ») : tes chiffres sont des **mesures isolées d'un même état**, jamais un gain.

## 3. Ce que tes données illustrent, et ce qu'on ne peut pas en dire

| Levier | Ce que tes données montrent | Ce qu'on ne peut PAS dire |
|---|---|---|
| **RAM pleine → SSD** | RAM 30,8 / 31 Go (vs 24,0 au repos) et lecture disque de 0 à ≈ 200 Mo/s dès qu'il écrit. Illustre : « quand un modèle dépasse la mémoire, une partie lit sur le SSD » | Que le SSD **ralentit** ton modèle (pas de mesure avec RAM libre) ; combien de tok/s ça coûte ; que ce soit le mode mmap (le 239 Mo/s accompagne 247 Mo/s d'écriture : fichier d'échange de Windows) |
| **Carte + RAM + SSD répartis** | 2 973 experts en VRAM (5,7 Go), RAM presque pleine, table sur SSD : le principe de Strata se voit à l'écran | Quelle part du modèle est dans chaque niveau, et son effet sur la vitesse |
| **Prompt système court** | Le choix de Pi (1,5 K) contre OpenCode (7,4 K) est ton choix de tournage ; chiffres du projet | Que Pi t'ait fait gagner de la vitesse ou du temps (aucune mesure avec OpenCode) |
| **Contexte qui grandit** | Contexte vu : 0 % → 35k → 54k / 128K ; moyennes de 69,4 → 67,8 → 66,1 (dans l'ordre chronologique) | Que la baisse vienne du contexte : tâches différentes, 66-69 est dans le bruit, et ton srt dit lui-même que les tests sont « plus rapides » que le dragon. La baisse du projet (59 → 43) est sur une autre machine |
| **Réflexion** | Réflexion « high » allumée pendant tous les tests ; ≈ 7 min de coupure à 32 000 une fois | Combien de tok/s la réflexion fait gagner ou perdre ; la durée d'un test n'est pas une vitesse |
| **Bande passante de la carte** | Ta 5080 (960 Go/s) « haut de la fourchette » (srt) | Que ta carte te rende 2 fois plus rapide que la 5060 Ti : la comparaison vient des fiches de bande passante et d'utilisateurs tiers, **pas de ta mesure** |
| **Quantification / fichier** | IQ1_M, 58 Go, tient « à ras » dans 32 Go de RAM | Rien sur la vitesse d'un autre fichier |
| **Le moteur** | Aucun plantage chez toi, 0 erreur du moteur dans les sessions | Rien sur les versions plus anciennes ou plus récentes |

## 4. Trois tests rapides avant le 18/11 (propositions, moins d'une heure en tout)

Règle commune (comme dans le plan Strata) : **un seul réglage change**, même appli, même version, même contexte, même prompt tapé tel quel, navigateur fermé (ferme Opera : il prend 3,8 Go de RAM), autre fenêtres fermées, **3 essais par réglage** (note la médiane, pas la meilleure), un « tour de chauffe » jeté avant. Note : version de l'appli et du moteur, fichier, contexte, réflexion, RAM et VRAM affichées, « Disk read ». Filme le moniteur à plein écran, « Decode » lisible. Les protocoles ci-dessous sont **à vérifier** avant de les filmer (ce que l'appli permet de régler n'a pas été relevé ici).

**Test 1, Strata : contexte court contre contexte long (≈ 15 min).** Même Coder, même prompt court (le dragon : « Tell me a short story about a dragon who loves video games. », 590 tokens environ, 51 tok/s en référence). A. Conversation neuve. B. La même demande après avoir collé dans Pi un gros fichier (par exemple le `index.html` de 1 282 lignes de l'essai 1, ou `AGENTS.md` de 51 Ko pour ≈ 35k à 54k de contexte). Note : tokens lus, tok/s Decode, tok/s Prefill, remplissage du contexte (« xk / 128K »). Donne une vraie paire « contexte qui grandit » sur la même machine, même fichier, même prompt de génération.

**Test 2, Strata : réflexion coupée contre réflexion « high » (≈ 15 min).** Même prompt (to-do list du calibrage : « Create a single-file index.html: a to-do list… About 150 lines. »). A. Défaut (« high »). B. Réflexion coupée par requête (`chat_template_kwargs: {"enable_thinking": false}` ou `reasoning_effort`, d'après `sources.md` T10 : à tester, Pi ne l'envoie pas tel quel, il faudra une requête directe sur `http://127.0.0.1:47831/v1`). Note : tok/s Decode, durée totale, tokens écrits, longueur de la réflexion. Attention : la réflexion change la **durée**, pas forcément le tok/s : à dire tel quel.

**Test 3, LM Studio : Qwen3.8-27B avec / sans MTP, ou cache KV f16 contre q8_0 (≈ 20-25 min).** C'est la seule paire possible sur un modèle **qui tient entièrement dans la 5080** (donc proche du « même carte, plus vite » de la fiche). Fichier ISTA `Qwen3.8-27B-GSQ-RCO-IQ3_S-mtp` (11,8 Go) comme prévu dans `modeles-5080.md` 0.1, GPU Offload au maximum, contexte 32K, Flash Attention allumée, **réflexion coupée si LM Studio le permet** (sinon note-la), même prompt de 200 tokens. A. MTP éteint. B. MTP allumé (si l'option apparaît ; sinon met à jour le moteur llama.cpp dans Settings > Runtime, `modeles-5080.md` l. 29). Variante : A. cache KV f16, B. q8_0 (`modeles-5080.md` l. 229-230, issue llama.cpp #27623). Note : version de LM Studio et du moteur, tok/s (le panneau de LM Studio), VRAM utilisée. Ferme Strata avant (elle garde VRAM et RAM).

Piste non retenue (plus de 1 h) : deux versions du moteur de Strata (mise à jour automatique, retour en arrière non vérifié) ; Pi contre OpenCode (réinstallation, prompts différents).

## 5. Ce que la vidéo Strata annonce, et ce qu'on ne doit pas répéter

**Point d'attention : la phrase d'annonce n'est plus dans la voix finale.** Le `.srt` (montage final) **ne contient aucune phrase** sur « jeudi » ni sur « plus vite avec la même carte ». Il se termine par « Et on se dit à la prochaine pour une autre vidéo. Salut ! » (srt, ≈ 9:22-9:25). La phrase « Et jeudi, on cherche comment aller plus vite avec la même carte » est dans `script.md` l. 200 et `teleprompteur.txt` l. 287, mais `upload.md` l. 111 note qu'elle a été « **coupée au montage** » ; l'annonce se fait par l'écran de fin (carte vers la vidéo du jeu. 19/11, sans lien). Le seul « jeudi » du srt est « le modèle dont je te parlais **jeudi dernier** » (srt, ≈ 1:55-1:58) pour la vidéo Qwen 4.

Phrases du srt qui préparent le terrain de la vidéo du 19/11 (à citer ou à renvoyer, pas à recopier) :
- « Lundi dernier, je te disais que 16 Go suffisent si tu prends le bon fichier. » (≈ 2:27)
- « Presque pas de réflexion, une réponse courte, et le moniteur affiche 51 tokens par seconde. » (≈ 3:06)
- « Près de 70 en moyenne, et selon le test, ça va de 43 à 84. » (≈ 3:14)
- « Sur ta carte 16 Go, ça tourne aussi, juste moins vite. Et la vitesse baisse quand la conversation grandit. » (≈ 3:53)
- « Sur une autre machine, avec un ancien moteur, le Coder passe de 59 à 43 tokens par seconde. Donc en gros, plus l'agent lit de code, plus il ralentit. » (≈ 4:01)
- « C'est pour ça que j'ai pris Pi : ses instructions font 1500 tokens, contre 7400 pour OpenCode. » (≈ 4:09)
- « Ma RAM est pleine à 30,8 Go sur 31 » et « La RAM est pleine, donc une partie passe par le SSD. » (≈ 4:36-4:51)
- « Tu montes tes limites de réponse plus haut que mes 32 000 tokens. » (≈ 9:00)
- « Si ta toute première IA en local, commence plutôt par la vidéo sur LM Studio. » (≈ 9:17)

Chiffres que la nouvelle vidéo **ne doit pas répéter tels quels** (déjà donnés, un spectateur qui a vu Strata les reconnaîtrait) mais auxquels elle peut **renvoyer** (« comme dans la vidéo de lundi ») : **≈ 70 tok/s (43-84)**, **51 tok/s au dragon**, **RAM 30,8 / 31 Go et ≈ 200 Mo/s de disque**, **1 500 contre 7 400 tokens** (Pi / OpenCode), **59 → 43 tok/s** du projet, **32 000 tokens** de limite, les 70 tok/s d'une 5070 Ti et 37 d'une Radeon, **81 contre 74** de Qwen. **À éviter** aussi : tout présenter les chiffres Strata comme un « avant » : ce ne sont pas des paires (section 2). Préférer « avec Strata, j'ai mesuré près de 70 ; ici, on cherche à aller plus vite sur le même type de carte, avec des réglages mesurés par d'autres » tant qu'aucune paire n'existe.

## 6. Captures et clips réutilisables (montage `/Users/innocent/HyperStudio/premium-noir/2026-11-strata-test/`)

- `assets/shots/MON0.png` à `MON4.png` : moniteur au repos (RAM 24,0), 81,5 « Decode now » (RAM 29,7, disque 239), 69,4 moyen (18 requêtes), dragon 50,8 + 67,8 moyen + RAM 30,8 (**MON3**, la plus utile), Sillage 66,1 moyen, creux 42,9 (**MON4**). Originaux : `Strata-Monitor-2026-11-13*.png` et `-14.png` dans `D:\_Technovore\Youtube\Strata test` (Windows, pas sur ce Mac).
- Clips : `assets/clips/dragon.mp4` (+ `dragon-last.jpg`), `conf-monitor.mp4` (moniteur seul), `brick-intro.mp4` (réflexion qui défile, moniteur en « Generating »), `conf-maxtokens.mp4`, `conf-json.mp4` (le `models.json` à 32 000), `inst-perf.mp4`, `conf-models.mp4` (page Models, contexte 128K).
- Captures web : `assets/captures/C1-3-vitesse(.png/-surligne)` (70,4 tok/s du ticket #4997), `C4-details-1-vitesses-coder` (vitesses du Coder publiées par le projet, 58,9 → 43,0), `C2-*` (plantage et vraie cause), `C4-models-*` (« Will it fit », 32 / 16 Go).
- Pas de CSV, de log du moniteur ni de relevé brut : seules sources chiffrées = les captures MON0-MON4, le calibrage dans `plan-tests.md`, et les sessions de Pi relues dans `sources.md` T41.
