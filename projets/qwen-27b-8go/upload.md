# Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? : kit d'upload YouTube

> **Vidéo** : `/Users/innocent/HyperStudio/premium-noir/2026-11-qwen-27b-8go/renders/q8-montage-final-4k.mp4` (en cours de finition ; temps contrôlés sur la v2 1080p `renders/q8-montage-v2.mp4`, mêmes temps) : 3840×2160, 30 i/s, 352,1 s (5:52). Les temps viennent de la voix finale (`sources/voix.words.json`, la voix démarre à 0 : temps de la voix = temps de la vidéo ; elle finit à 343,1 s, la vidéo 9 s plus tard).
> **Sortie** : **lun. 23 nov. 2026, 18 h** ([`calendrier.md`](../../calendrier.md), ligne 3). Faits : [`sources.md`](sources.md) (F1 à F17).
> **vidIQ, 19/11 : 0 crédit dépensé.** Les outils de mots-clés, d'outliers et de recherche YouTube ne sont pas chargés dans cette session (ToolSearch ne trouve que des outils de comptes, de miniatures, de vidéos de chaîne et de réseaux sociaux). Les volumes ci-dessous sont repris des kits voisins, datés ; les vidéos hôtes viennent de la page de résultats de YouTube (curl, 19/11), pas de vidIQ.

## Mots-clés (relevés vidIQ des 23, 24 et 26/10 : aucun n'est refait)

| Mot-clé | Recherches/mois | Concurrence | Usage |
|---|---|---|---|
| qwen | 179 672 (8 045 en France), vidIQ 23/10 | 48,3 | Première ligne, hashtag, tags |
| vram | 15 336, vidIQ 24/10 | 69 | Hashtag, tags : « 8 Go de VRAM » est la forme que le public tape |
| ia en local | 15 204, vidIQ 26/10 | 42 | Hashtag, tags : le mot-clé du pilier |
| ia local | 111 094 (8 546 en France), vidIQ 26/10 | 58 | Tags |
| local llm | 87 763, vidIQ 24/10 | 52 | Tags |
| lm studio | 247 028 (5 146 en France), vidIQ 26/10 | 59 | Chapitre 4:21, description, tags |
| llama.cpp | 21 080 (−46 % sur 30 jours), vidIQ 23/10 | 53,3 | Description (les vitesses viennent de lui), tags |
| **qwen 27b**, **qwen 8 go**, **8 go vram**, **unsloth**, **gguf**, **quantification**, **cache kv** | **non mesurés** (outil absent le 19/11) | — | Titre, première ligne, tags : à mesurer au radar du 23/11 |

**Lecture** : le titre garde « Qwen 27B » et « 8 Go », les mots qu'on voit déjà sur cinq vidéos de ce mois (section Suggestions) ; « plus rapide, mais à quel prix ? » est ce qui nous sépare d'elles. « UD-IQ2_XS » et « MTP » restent hors titre : personne ne les tape encore, ils sont dans la description et les tags.

## Titres

| | Titre | Car. | Ce que la vidéo tient |
|---|---|---|---|
| **A · Calendrier (recommandé)** | Qwen 27B sur 8 Go : plus rapide, mais à quel prix ? | 51 | Oui : le gain (0:05 à 0:35), puis les deux prix, la place (1:57) et la qualité (3:15) ; « sur 8 Go » : la mesure est celle d'une GTX 1080 Ti limitée à 8 Go, dite à 0:10 |
| B · Chiffre | Qwen 27B sur 8 Go de VRAM : 18 tokens par seconde, mais à quel prix ? | 69 | Oui pour le chiffre (0:05), mais il promet « 18 » comme si c'était ta vitesse alors que c'est une seule mesure (0:10) : A est plus sûr |

- **Publie avec A seul**, pour les trois miniatures : le test A/B décidé le 15/11 (h, i, j) ne doit tester que l'image.
- A et la miniature ne se répètent pas : l'image demande si le fichier tient (« 8 GO ÇA RENTRE ? », fichier de 7,63 Go), le titre promet la vitesse et son prix.
- Écarté : « 5 fois plus vite » (une seule mesure, 5,6 fois : `sources.md` F14), « le premier 2 bits qui tient » (non établi, F13).

## Description

```
Qwen 3.8 27B passe de 3,2 à 18 tokens par seconde sur une carte de 8 Go, en changeant un seul fichier : le UD-IQ2_XS d'Unsloth, 7,63 Go. Mais ce fichier a un prix : la place pour la conversation, et la qualité.

C'est une seule mesure publiée, sur une GTX 1080 Ti limitée à 8 Go : pas la vitesse que tu auras. Au programme : la quantification, le cache KV, le test d'agent (environ 13 % contre 40 %), LM Studio, et quel fichier pour quel usage.

CHAPITRES
0:00 Introduction : Qwen 27B sur 8 Go
0:29 Ce que ça change en vrai : 28 secondes au lieu de 2 min 36
1:07 D'où vient le gain : un fichier qui tient dans la carte
1:34 La quantification : le modèle a dû maigrir (et le MTP)
1:57 Le premier prix : la place sur 8 Go
2:18 La mémoire de la conversation : le cache KV
3:15 Le deuxième prix : la qualité (LiveCodeBench)
3:45 Le test d'agent : 40 % contre 13 %
4:21 Et dans LM Studio ?
4:37 Verdict : discuter et expliquer
4:49 Verdict : un bout de code
4:59 Verdict : un agent, garde l'ancien fichier
5:13 Ce que ce fichier te fait perdre
5:28 Ton avis en commentaire

PRÉCISIONS
« Publié le 11 novembre » : c'est la mise à jour (Dynamic V3.1) annoncée ce jour-là par Unsloth. Les 18 tokens par seconde sont mesurés dans llama.cpp, pas dans LM Studio.
Les scores de qualité sont ceux d'Unsloth : 40 % est une valeur annoncée ; 13 % et 36 % sont lus sur leur graphique, donc approximatifs.

LIENS
Le fichier UD-IQ2_XS (Unsloth) : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
Qwen3.8-27B : https://huggingface.co/Qwen/Qwen3.8-27B
Les scores d'Unsloth : https://unsloth.ai/docs/models/qwen3.8
Les réglages de LM Studio : https://lmstudio.ai/docs/app/advanced/per-model
llama.cpp : https://github.com/ggml-org/llama.cpp
La mesure publiée le 13/11 : https://www.youtube.com/watch?v=u_DYZhTZ2IM
Même carte, 2 fois plus rapide (le MTP) : [LIEN À COLLER]
16 Go de VRAM, le bon fichier : https://www.youtube.com/watch?v=jMZFDNbwRNI

MUSIQUES : « Future Minimal » par kissan4 et « Dark Ambient for Crime and Tension » par megalix (Pixabay).

Dis-moi en commentaire : tu utiliserais un fichier différent selon ce que tu fais (discuter, coder, agent) ?
Sur Technovore, j'ouvre le capot de l'IA que tu utilises. Si cette vidéo t'a aidé à faire le bon choix pour ta carte, abonne-toi : c'est le seul abonnement qui ne te prélèvera jamais rien.

#IAenLocal #Qwen #VRAM
```

- **Taille : 2,356 caractères sur 5 000** (compté par script le 19/11). Corps hors chapitres et liens (première ligne, précisions, musiques, appel à commenter) : 1 196 caractères.
- **Chiffres** : 3,2 → 18 tokens/s (voix 0:05 ; F2), 7,63 Go (1:28 ; F1), GTX 1080 Ti et 8 Go (0:10 ; F2), « environ 13 % contre 40 % » (3:50 à 3:52 ; F4), 36 % de l'ancien fichier (3:57 ; F4), 28 s contre 2 min 36 (0:32 ; F16).
- **PRÉCISIONS** : la voix dit « publié par Unsloth le 11 novembre » (1:30) alors que `sources.md` (F1) ne date que la mise à jour Dynamic V3.1 ; les 18 tokens/s viennent de llama.cpp, pas de LM Studio (la voix le dit à 4:31) ; seul le 40 % est annoncé exactement (40,40), le 13 % et le 36 % sont lus sur le graphique d'Unsloth (F4).
- **Aucune chaîne ni créateur nommé.** La mesure est liée par l'URL de sa vidéo, qui ne contient aucun nom (`u_DYZhTZ2IM`), et décrite comme « la mesure publiée le 13/11 ». Pas de chemin de dossier ni de clé. Deux pseudos de musiciens (kissan4, megalix) : c'est le crédit Pixabay, comme dans les kits précédents.
- **Liens** vérifiés ouverts (code 200) le 19/11 : le dépôt GGUF d'Unsloth, Qwen3.8-27B, la doc d'Unsloth, la doc LM Studio (réglages par modèle), llama.cpp, la vidéo de la mesure, ta vidéo « 16 Go de VRAM ». **À coller** : le lien de « Même carte, 2 fois plus rapide » (sortie jeu. 19/11, pas encore dans `README.md` ni sur la chaîne à 1 h du matin le 19/11), à la place de `[LIEN À COLLER]`.
- **Musiques** : `index.html` du montage utilise `music-minimal-long` et `music-tension-long` ; `style/media.json` les crédite à kissan4 (« future minimal ») et megalix (« dark ambient for crime and tension »), Pixabay. Même liaison que dans les kits de Strata et du MTP.
- **Appel à s'abonner** : la voix le dit à 3:11 (« si cette vidéo t'a aidé à faire le bon choix pour ta carte, n'oublie pas de t'abonner ») et à 5:37 ; la description reprend la phrase (règle `.claude/rules/script.md`).
- **Hashtags** : #IAenLocal (le mot-clé du pilier), #Qwen, #VRAM.

### Chapitres : vérification

14 chapitres, premier à 0:00, le plus court fait 10 s (4:49 → 4:59) : les trois règles de YouTube sont tenues. Ceux du montage (`chapitres.txt`) sont remplacés : ils tombaient parfois dans une phrase (4:20 dans « marche », 1:56 dans « maintenant ») et 5:35 tombait dans « selon vos besoins ».

| Début | Titre | Ce qui l'ouvre dans la voix | Vérification (`voix.words.json`) |
|---|---|---|---|
| 0:00 | Introduction | « Est-ce qu'un modèle de 27 milliards… » | 0,03 s |
| 0:29 | Ce que ça change en vrai | « D'abord, ce que ça change en vrai » | 29,40 s (« fabriqué » finit à 28,79) |
| 1:07 | D'où vient le gain | « Mais alors, d'où vient ce gain ? » | 67,18 s (« penses » finit à 66,73) |
| 1:34 | La quantification | « Sauf que pour rentrer dans une carte de 8 gigas » | 94,18 s (« simple » finit à 93,65) ; **ajouté** |
| 1:57 | Le premier prix : la place | « Et le premier prix, c'est de la place » | 117,09 s (« coûte » finit à 116,81) ; le montage dit 1:56 : dans « maintenant » |
| 2:18 | La mémoire de la conversation : le cache KV | « Et la mémoire de la conversation » | 138,22 s (« reste » finit à 137,79) ; **ajouté** |
| 3:15 | Le deuxième prix : la qualité | « Bon, le deuxième prix, c'est la qualité » | 195,43 s (« t'abonner » finit à 195,00) |
| 3:45 | Le test d'agent | « Sur leur test d'agent » | 224,92 s ; à 3:45 (225,0), « sur » est déjà dit (0,1 s) ; **ajouté** |
| 4:21 | Et dans LM Studio ? | « Et si t'es sur LM Studio » | 261,14 s (« coup » finit à 260,73) ; le montage dit 4:20 : dans « marche » |
| 4:37 | Verdict : discuter et expliquer | « Alors, qu'est-ce qu'on peut conclure » | 276,83 s (« alors ») ; à 4:37 (277,0), « alors » est déjà dit |
| 4:49 | Verdict : un bout de code | « Pour te faire aider sur un bout de code » | 288,95 s (« suffit » finit à 288,79) ; **ajouté** |
| 4:59 | Verdict : un agent | « Pour un agent qui travaille » | 298,92 s ; à 4:59 (299,0), « pour » est déjà dit (0,04 s) ; **ajouté** |
| 5:13 | Ce que ce fichier te fait perdre | « Alors, ce que ce petit fichier te fait gagner ou te fait perdre » | 313,42 s (« pas » finit à 312,99) ; **ajouté** |
| 5:28 | Ton avis en commentaire | « Dites-moi en commentaire » | 327,94 s ; à 5:28 (328,0), « dites-moi » démarre déjà, seul « alors » (327,66 à 327,88) est sauté ; 5:27 ferait entendre 0,3 s de « donnes » |

« À la prochaine » (5:35 dans le montage) n'est plus un chapitre : il tombait dans « selon vos besoins » (la voix dit « à la prochaine » à 5:42).

## Tags

```
qwen 27b, qwen 3.8 27b, qwen3.8, qwen 8 go, qwen 8gb vram, 8 go vram, 8gb vram, vram, ia en local, ia locale, ia local, llm local, local llm, unsloth, gguf, quantification, quantization llm, ud-iq2_xs, kv cache, cache kv, lm studio, llama.cpp, carte graphique ia, gtx 1080 ti, technovore
```

**287 caractères sur 500.** « kv cache » et « cache kv » : la voix dit « KV cache », le public français cherche les deux ; « qwen3.8 » corrige l'écriture.

## Commentaire épinglé

```
Tu utiliserais un fichier différent selon l'usage : discuter, coder, agent ? Dis-moi ta carte, ton moteur (LM Studio, llama.cpp…) et si tu as essayé ce fichier de 7,63 Go. Si cette vidéo t'a aidé à faire le bon choix pour ta carte, abonne-toi.
```

La voix dit « dites-moi en commentaire : est-ce que vous êtes prêts à utiliser un fichier différent » à 5:28 ; le commentaire épinglé reprend cette promesse, en tutoyant (le tutoiement de la description et du titre).

## Sous-titres

- Français : [`qwen-27b-8go.fr.srt`](qwen-27b-8go.fr.srt) (167 sous-titres, 0:00-5:43).
- Anglais : [`qwen-27b-8go.en.srt`](qwen-27b-8go.en.srt), mêmes numéros et mêmes temps.
- Dans Studio : « Avec synchronisation », langue de la vidéo en français.
- Le texte est ce que la voix dit, pas le script (`teleprompteur.txt`) : question d'accroche (« Est-ce qu'un modèle de 27 milliards… »), « Moi, c'est du charabia », « une diète incroyable », « c'est top qualité », fin au « vous » avec un second appel à s'abonner ; la voix n'annonce pas la vidéo de jeudi. « 2 fois sur 3 » est écrit en toutes lettres (à 5:09 la voix le prononce de façon peu claire).
- Contrôle par script : 167 blocs dans chaque fichier, mêmes numéros et mêmes temps ; temps croissants, aucun chevauchement, tout dans [0 ; 352,1 s] (dernier bloc : 5:42,9) ; durées de 0,8 à 7 s ; 2 lignes au plus, ligne la plus longue 42 caractères en français et 40 en anglais (aucune au-dessus de 46) ; **1 424 mots de la voix sur 1 424 couverts** (100 %).

## Suggestions

Le pourquoi est dans [`etudes/suggestions-2026-10-23.md`](../../etudes/suggestions-2026-10-23.md). **vidIQ indisponible** (outils de recherche absents) : recherches YouTube « qwen 27b 8 go vram », « ia locale 8 go vram plus rapide » et « qwen 3.8 27b 8gb vram », filtre « ce mois-ci », par curl le **19/11/2026** ; dates, vues et pistes audio lues sur la page de chaque vidéo. Pas un recensement complet. YouTube traduit les titres en français : les vidéos sont toutes en anglais à l'origine, avec une piste française doublée automatiquement.

### Les vidéos hôtes

| # | Vidéo (titre affiché en français) | Chaîne | Vues (19/11) | Sortie |
|---|---|---|---|---|
| 1 | *Votre GPU 8 Go fait tourner Qwen 3.8 27B 5x plus vite maintenant (un nouveau fichier)* (`u_DYZhTZ2IM`) | SimplyExplain | 9 747 | 13/11 |
| 2 | *Votre GPU de 8 Go fait désormais tourner l'IA locale plus vite que Strata (avec une seule option)* (`JU69jDWeGnA`) | SimplyExplain | 11 538 | 17/11 |
| 3 | *La plus grosse IA locale qu'une carte graphique bon marché peut faire tourner* (`QIHoX8aKP4A`) | Locally | 8 597 | 15/11 |
| 4 | *8 Go de VRAM contre un LLM de 180 Md : comment Strata permet de le faire tourner* (`0ksT9HkoWk8`) | Tech-Practice | 4 533 | 17/11 |
| 5 | *J'ai fait tourner qwen3.8 (27B) sur un GPU de 8 Go* (`YeTXbS9KO4o`) | Zilox | 876 | 10/11 |

**Les mots qu'on partage, et ce qu'on ne prend pas** :
1. SimplyExplain (n° 1) : « Qwen 27B », « 8 Go », « plus vite ». **C'est la source de ta mesure** : même fichier, même carte, 7:45 contre ton 5:52. Ne prends ni son « 5x » (une seule mesure, 5,6 fois) ni « un nouveau fichier ». Ce qui te sépare : le prix (la place et la qualité), absent de son titre.
2. SimplyExplain (n° 2) : « 8 Go », « plus vite ». Pas « Strata » ni « une seule option ».
3. Locally : « IA locale », « carte graphique ». Pas « la plus grosse », qui promet un modèle, pas une vitesse.
4. Tech-Practice : « 8 Go de VRAM ». Pas « 180 Md » ni Strata.
5. Zilox : « qwen3.8 (27B) », « 8 Go ». Petite vidéo, mais le même sujet mot pour mot.

À surveiller hors planche : *Qwen 3.8 sur 8 Go de VRAM ? Vérification de la réalité du Dynamic V3.1 d'Unsloth (RTX 4060 vs 4090)* (Prompt Engineer 48, 1 008 vues, 15/11), le même fichier avec une vraie RTX 4060 ; à regarder avant la sortie, c'est peut-être la seconde mesure que `sources.md` (F11) n'a pas trouvée. Et la vidéo de Red Stapler (788 K vues, 24/08), la source de la fiche, hors mois.

### La planche

Les cinq miniatures sont dans [`miniature/hotes/`](miniature/hotes/). `planches.py` a tourné sur des copies renommées (`qwen-8go-h.png`, `-i`, `-j`) : [`suggestions-qwen-8go-h.png`](../../ressources/miniatures/planches/suggestions-qwen-8go-h.png), [`-i`](../../ressources/miniatures/planches/suggestions-qwen-8go-i.png), [`-j`](../../ressources/miniatures/planches/suggestions-qwen-8go-j.png). Ordre : Tech-Practice (n° 4), SimplyExplain (n° 2), **la nôtre**, Locally, Zilox, SimplyExplain (n° 1).

### La comparaison à 168 px

- **Elle se repère** : « 8 GO ÇA RENTRE ? » est le seul texte en français et la seule miniature qui pose une question ; les cinq autres sont en anglais et annoncent un résultat (« 180B on 8GB », « BEATS STRATA », « 5X FASTER »). La barre de 8 Go presque pleine et le fichier de 7,63 Go se lisent même petits. **h** et **j** : le visage perplexe est le seul de la colonne et regarde le texte. **i** (sans visage) est la plus discrète : le texte et la barre tiennent, mais rien ne cible l'œil.
- **Elle promet autre chose** : « ça rentre ? » (la place) là où les autres promettent un multiplicateur ; le titre apporte la vitesse. Les deux ne se répètent pas, mais la miniature ne dit pas « Qwen » : à 168 px, seul le logo violet du fichier le porte. Le titre le dit.
- **Attention** : « ÇA RENTRE ? » est le texte de la miniature de « 16 Go de VRAM suffisent » (09/11, 1,5 % de CTR à J+2). Ici, « 8 GO » est dit et le visage ajoute l'émotion qui manquait ; si h ou j fait à peine mieux, c'est le texte qu'il faut changer, pas le style.
- **Retouche avant de publier** : aucune. Le test h, i, j tranchera ; mon pari est j (visage + palette de Technovore, le menthe n'existe nulle part ailleurs dans la colonne).

### L'enchaînement

- **Écran de fin, de 5:35 à 5:52** (17 s ; la voix dit « à partager la vidéo » à 5:38 et finit à 5:43) : à gauche, « Même carte, 2 fois plus rapide » (sortie jeu. 19/11 : **URL à remplir**, elle n'est pas encore dans `README.md`) ; à droite, « 16 Go de VRAM suffisent » ([`jMZFDNbwRNI`](https://www.youtube.com/watch?v=jMZFDNbwRNI)). YouTube demande au moins 5 s et au plus 20 s : 17 s, c'est bon.
- **Vidéo suivante** : *Carte graphique pour l'IA locale : combien coûte la mémoire dont tu as besoin ?* (jeu. 26/11, [`calendrier.md`](../../calendrier.md) ligne 4). La voix ne l'annonce pas : elle n'est que dans l'enchaînement de la playlist « IA chez moi » et, au besoin, dans le commentaire épinglé de la semaine suivante.
- **Fiche pendant le plateau de rétention** : vers **1:45 à 1:55**, vers « Même carte, 2 fois plus rapide » (la voix dit « le MTP, le module qui doublait la vitesse dans la vidéo précédente », 1:45 à 1:48) ; une seconde à 4:21, vers la vidéo LM Studio de la chaîne (« Pourquoi avoir ta propre IA, et comment l'installer »), dont l'URL n'est pas dans `README.md` : à retrouver dans Studio. Plateau inconnu : recale-les sur la courbe au radar du 23/11.

## À vérifier avant l'upload

- **Écoute les sous-titres une fois sur la vidéo** : je n'ai pas écouté l'audio ; les temps sont ceux de `voix.words.json`. Doutes de transcription (le texte dit est tenu pour la transcription, sauf :) :
  - **« Il s'agit d'une division »** (0:36,8) : la transcription donne « s'agit d'une division » ; j'ai ajouté « Il » ; le téléprompteur dit « Juste une division » : réécoute ;
  - **« tenir sur une simple carte »** (0:02) : la transcription donne « tenir une simple carte » ; j'ai ajouté « sur » ;
  - **« environ 13 % »** (3:52) : la transcription s'arrête à « environ 13 » ; j'ai ajouté « % » (téléprompteur) ;
  - **« KV cache »** (2:18) : la voix dit « kv cache » et le téléprompteur « cache KV » ; gardé tel que dit ;
  - **« ne te dit pas donc »** (2:17) : l'ordre des mots est celui de la voix ; **« il y a pas de problème »** (5:18), **« ça pourrait marcher »** (4:58) et **« c'est top qualité »** (5:19) gardés tels que dits ;
  - **vouvoiement** de la fin (« dites-moi », « vous êtes prêts », « vous a plu », 5:28 à 5:40) : gardé tel que dit ;
- **Chiffres relus contre `sources.md`** : 18/3,2 = 5,625 et 15,3/3,0 = 5,1 (F14), donc « plus de 5 fois plus vite » (4:45) tient ; 500/3,2 = 156 s = 2 min 36 et 500/18 = 28 s (F16) ; 3 fois moins souvent = 40,40/12,8 = 3,2 (F4, lecture graphique) ; « presque 9 fois sur 10 » = 87 % ; « 2 fois sur 3 » pour l'ancien fichier : 64 % si 36 % de réussite (F4, lecture graphique).
- **Faible** : « le petit fichier réussit 3 fois moins souvent » et « presque 9 fois sur 10 » reposent sur un point lu sans étiquette numérique sur le graphique d'Unsloth (vers 12,8) : c'est pour cela que la description dit « environ 13 % ».
- **Pas vérifié** : la voix dit « le moteur… ton bureau… si tu branches ton moniteur directement sur ta carte » (2:07) : un usage, pas un fait de `sources.md` (F9 dit seulement que les poids, le cache et les autres usages cohabitent).
- Après chargement : `calendrier.md` et `README.md` disent encore « Voix » : passe-les à « Programmé ».
- Après la sortie : skill `radar` (règle du dépôt).
