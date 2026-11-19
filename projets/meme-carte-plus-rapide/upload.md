# Même carte, 2 fois plus rapide : kit d'upload YouTube

> **Vidéo** : `/Users/innocent/HyperStudio/premium-noir/2026-11-meme-carte-plus-rapide/renders/mc-montage-v5-4k.mp4`, rendue le 18/11 : 3840×2160, 30 i/s, 463,5 s (7:43). Les temps viennent de la voix finale (`sources/voix.words.json`, la voix démarre à 0 : temps de la voix = temps de la vidéo ; elle finit à 454,2 s, la vidéo 9 s plus tard).
> **Sortie** : **jeu. 19 nov. 2026, 18 h** ([`calendrier.md`](../../calendrier.md), ligne 2). Faits : [`sources.md`](sources.md) (M1 à M38).
> **vidIQ, 18/11 : 0 crédit dépensé.** Les outils de recherche (mots-clés, outliers, recherche YouTube) ne sont pas chargés dans cette session (ToolSearch ne trouve que des outils de comptes, de miniatures et de réseaux sociaux). Les volumes ci-dessous sont repris des kits voisins, datés ; les vidéos hôtes viennent de la page de résultats de YouTube (curl, 18/11), pas de vidIQ.

## Mots-clés (relevés vidIQ des 23, 24 et 26/10 : aucun n'est refait)

| Mot-clé | Recherches/mois | Concurrence | Usage |
|---|---|---|---|
| **llama.cpp** | 21 080 (−46 % sur 30 jours), vidIQ 23/10 | 53,3 | Description, tags, hashtag : le moteur de la vidéo |
| ollama vs llama.cpp | 4 224, vidIQ 23/10 | **34** | Tags : la seule requête « moteur contre moteur » mesurée |
| ollama | 354 489 (7 334 en France), vidIQ 26/10 | 67 | Chapitre 3:25, tags |
| lm studio | 247 028 (5 146 en France), vidIQ 26/10 | 59 | Chapitres, description, tags |
| qwen | 179 672 (8 045 en France), vidIQ 23/10 | 48,3 | Première ligne, tags |
| ia en local | 15 204, vidIQ 26/10 | 42 | Hashtag, tags : le mot-clé du pilier |
| ia local | 111 094 (8 546 en France), vidIQ 26/10 | 58 | Tags |
| local llm | 87 763, vidIQ 24/10 | 52 | Tags |
| vram | 15 336, vidIQ 24/10 | 69 | Titre B et C (« 16 Go de VRAM »), tags |
| **mtp**, **qwen 3.8 27b**, « ia plus rapide » | **non mesurés** (outil absent le 18/11) | — | Hashtag, première ligne, tags : mots neufs, à mesurer au radar du 19/11 |

**Lecture** : « 2 fois plus rapide » n'a pas de volume mesuré ; ce que les gens tapent, c'est le moteur (« llama.cpp », « ollama », « lm studio ») et la config (« 16 Go de VRAM »). « MTP » reste hors titre : personne ne le cherche encore, le titre vend le résultat et la miniature le doute.

## Titres

| | Titre | Car. | Ce que la vidéo tient |
|---|---|---|---|
| **A · Calendrier (recommandé)** | Même carte, 2 fois plus rapide | 30 | Oui, avec les conditions dites dans les 40 premières secondes : l'écriture, Qwen 3.8 27B, un modèle qui tient en entier dans la carte (0:18 à 0:24) ; 6 mesures de 1,9 à 2,3 fois (0:09 à 0:15) |
| B · Résultat | Ton IA locale écrit 2 fois plus vite sur la même carte (16 Go de VRAM) | 70 | Oui (« écrit » = l'écriture, pas la lecture du prompt, 0:57 à 1:03) ; 16 Go : les cartes de 16 Go des 6 mesures |
| C · Réglage | MTP : le réglage qui double la vitesse de ta carte (16 Go de VRAM) | 66 | La voix dit « le réglage qui te permet de doubler la vitesse de ta carte graphique » (0:24) ; mais « double » sans condition promet plus que 1,8 fois sur du texte seul (1:35) : B est plus sûr |

- **Publie avec A seul**, pour les trois miniatures : le test A/B décidé le 15/11 (h, i, j) ne doit tester que l'image.
- A et la miniature ne se répètent pas : le titre dit le gain (« 2 fois plus rapide »), l'image pose le doute (« TA CARTE BRIDÉE ? », compteur de 1× à 2×).
- **Attention à la ressemblance avec la vidéo française du 14/11** (*Mon IA locale va 11 fois plus vite (même PC)*, 20 796 vues au 18/11) : « même carte » et « même PC » sont presque le même mot, « 2 fois plus rapide » contre « 11 fois plus vite » le même format. Ce qui te distingue : le doute (« bridée ») et les mesures de 6 cartes, pas un récit de 3 mois. Si le titre A se perd à côté du sien dans les suggestions, B ajoute « (16 Go de VRAM) » pour la config.
- Écarté : « 2 fois plus rapide sur 6 cartes » (6 mesures, mais sur 5 modèles de cartes : la voix dit 5), « 3× », « 4× », « 10× » (sources.md, section H).

## Description

```
Sur une carte de 16 Go, un seul réglage, le MTP, fait écrire Qwen 3.8 27B 2 fois plus vite : de 29 à 64 tokens par seconde, sans rien acheter. D'après 6 mesures publiées, de 1,9 à 2,3 fois selon la carte.

Le gain vaut pour l'écriture, sur un modèle qui tient en entier dans la carte. Au programme : le fichier qui tient, le MTP, le moteur (llama.cpp, LM Studio, Ollama), les experts, la conversation longue et le cache KV compressé.

CHAPITRES
0:00 Introduction : 2 fois plus vite, même carte
0:42 Le MTP, le réglage qui double
1:18 Les limites des 6 mesures
1:45 Pourquoi ta carte est peut-être bridée (et le prix du MTP)
2:16 Le fichier qui tient en entier dans la carte
3:08 Avant de racheter une carte plus grosse
3:25 Le moteur : llama.cpp, LM Studio, Ollama
3:53 Une mise à jour peut te ralentir
4:18 Modèle trop gros : où vont les experts
4:50 Le piège : la conversation longue
5:33 Le cache KV compressé : vitesse ou place ?
6:19 Le cache en 4 bits : attention à la qualité
6:43 La liste, dans l'ordre
7:10 Alors, ta carte est-elle bridée ?
7:21 La suite : l'IA sur une carte de 8 Go

PRÉCISIONS
« 2 fois plus vite » : écriture seulement, sur un modèle qui tient dans la carte ; 1,8 fois sur du texte seul, 1,5 fois au mieux avec des experts ; la lecture du prompt ralentit.
Dans llama.cpp, le MTP demande une option et un fichier qui contient le module ; LM Studio le gère depuis la 0.4.22 (je n'ai pas vérifié s'il est éteint par défaut).
Experts : 12 % et 29 %, une mesure chacune.

LIENS
llama.cpp : https://github.com/ggml-org/llama.cpp
Le MTP dans llama.cpp : https://github.com/ggml-org/llama.cpp/pull/22673
Le cache d'experts de llama.cpp : https://github.com/ggml-org/llama.cpp/pull/29887
LM Studio (version 0.4.22 et le MTP) : https://lmstudio.ai/changelog/lmstudio-v0.4.22
Ollama : https://github.com/ollama/ollama
Strata : https://github.com/Niko1221/Strata/releases/tag/v0.2.14
Qwen3.8-27B : https://huggingface.co/Qwen/Qwen3.8-27B
Les fichiers GGUF (Unsloth) : https://huggingface.co/unsloth/Qwen3.8-27B-GGUF
Mon test de Strata : https://www.youtube.com/watch?v=892vB0mRY8U
16 Go de VRAM, le bon fichier : https://www.youtube.com/watch?v=jMZFDNbwRNI

MUSIQUES : « Future Minimal » par kissan4 et « Dark Ambient for Crime and Tension » par megalix (Pixabay).

Ta carte et ta vitesse avec et sans MTP ? Dis-le en commentaire, avec ta réponse sur le cache KV (5:36).
Sur Technovore, j'ouvre le capot de l'IA que tu utilises. Si cette vidéo t'a évité un mauvais achat, abonne-toi : c'est le seul abonnement qui ne te prélèvera jamais rien.

#IAenLocal #LlamaCpp #MTP
```

- **Taille : 2,585 caractères sur 5 000** (compté par script le 18/11). Corps hors chapitres et liens : 1,247 caractères, PRÉCISIONS, musiques et appel à commenter compris.
- **PRÉCISIONS** corrige ce que la voix dit un peu vite : « 2 fois plus vite » (0:00, 3:08 : c'est la moyenne en écriture, `sources.md` section A et G : 1,8 fois sur du texte seul, 1,5 fois au mieux avec des experts, M7 : lecture du prompt plus lente), « quelques clics » (7:16, `llama.cpp` : option `--spec-type draft-mtp` et fichier avec le module, M8 ; LM Studio : réglage par défaut **non vérifié**, M30b, alors que la voix dit « éteint de base » à 7:12) et les gains sur les experts (4:38 à 4:45 : la voix dit « une seule mesure chacune », mais le 29 % vient d'un commit de fork qui porte la PR, M19, pas de llama.cpp officiel).
- **Pas dans les PRÉCISIONS faute de place** : « le plus populaire, c'est llama.cpp » (3:28 : pas dans `sources.md`) ; « 10 % plus lent que llama.cpp » pour Ollama (M29 : un testeur, un modèle de 7 milliards, temps réel qui mêle écriture et lecture, repris sans relecture) ; « jusqu'à 30 % » (M30 : de 18 à 29 % sur une 3090 d'un autre testeur) ; « 3 des 6 mesures en 4 bits » (cache KV en q4_0 : M1, M4, M5).
- **Aucune chaîne ni créateur nommé** (les noms de projets, de dépôts et de fichiers seulement) ; pas de chemin de dossier, pas de clé. Deux pseudos de musiciens (kissan4, megalix) : c'est le crédit Pixabay, comme dans les kits précédents. Le dépôt de Strata porte le nom de son auteur dans l'URL (`Niko1221`), comme dans le kit de Strata ; je n'ai pas lié le tableau de mesures (le dépôt et le blog des mesures portent un pseudo ; leurs chiffres sont dans `sources.md`).
- **Chiffres de la description** : 29 → 64 et 1,9 à 2,3 fois (M1 à M6, M5 pour le 29 → 64), 16 Go, 1,8 et 1,5 fois (M3, M10, M11), 0.4.22 (M30b), 12 % et 29 % (M17, M19). Liens vérifiés ouverts (code 200) le 18/11 : llama.cpp, PR 22673 (MTP) et 29887 (cache d'experts), LM Studio 0.4.22, Ollama, Strata v0.2.14, Qwen3.8-27B, GGUF d'Unsloth, tes deux vidéos.
- **Hashtags** : #IAenLocal (le mot-clé du pilier), #LlamaCpp, #MTP.
- Musiques : `style/media.json` (kissan4, megalix, Pixabay) ; `index.html` du montage utilise `music-minimal` et `music-tension`. La liaison entre ces deux identifiants et les deux titres n'est pas écrite dans `media.json` ; je l'ai reprise du kit de Strata (même DA).
- **La fin** : la voix dit « on va essayer d'explorer plus tard » l'IA sur 8 Go de VRAM (pas « lundi ») : j'ai donc écrit « La suite : l'IA sur une carte de 8 Go » sans date. Le script la place lundi (23/11, `calendrier.md` ligne 3).

### Chapitres : vérification

| Début | Titre | Ce qui l'ouvre dans la voix | Vérification (`voix.words.json`) |
|---|---|---|---|
| 0:00 | Introduction : 2 fois plus vite, même carte | « Sur une carte de 16 gigas » | 0,07 s |
| 0:42 | Le MTP, le réglage qui double | « Le réglage qui double, c'est le MTP » | 42,22 s (« vite » finit à 41,62) |
| 1:18 | Les limites des 6 mesures | « Sauf que 5 de ces 6 mesures » | 78,46 s (« vitesse » finit à 77,90) ; **ajouté** |
| 1:45 | Pourquoi ta carte est peut-être bridée (et le prix du MTP) | « Alors, pourquoi est-ce que je dis que ta carte est bridée » | 105,20 s (« mieux » finit à 104,78) ; le chapitre 2:06 du montage est fondu (10 s pile : trop juste) |
| 2:16 | Le fichier qui tient en entier dans la carte | « Donc le vrai réglage numéro un » | 136,62 s ; à 2:16, on entend encore 0,07 s de la fin de « coince » (finit à 136,07) |
| 3:08 | Avant de racheter une carte plus grosse | « Bon, rien qu'avec ces 2 réglages » | 188,03 s (« MTP » finit à 187,37), **ajouté** |
| 3:25 | Le moteur : llama.cpp, LM Studio, Ollama | « Et le moteur qui te permet d'y arriver » | 204,84 s ; le montage dit 3:24, qui tombe dans « abonne-toi » (finit à 204,24) ; 3:25 démarre sur « moteur » (« et le » finit à 204,98) |
| 3:53 | Une mise à jour peut te ralentir | « Et même avec un moteur optimisé » | 232,81 s ; 3:52 tomberait dans « t'es tranquille » (finit à 232,26) ; 3:53 démarre sur « même » |
| 4:18 | Modèle trop gros : où vont les experts | « Et si ton modèle est trop gros » | 258,02 s ; le montage dit 4:17, qui tombe dans « écran » (finit à 257,58) |
| 4:50 | Le piège : la conversation longue | « Maintenant, qu'est-ce qui coince » | 290,46 s ; à 4:50, on entend encore 0,1 s de « RAM » (finit à 290,10) |
| 5:33 | Le cache KV compressé : vitesse ou place ? | « Ce réglage, c'est compresser le cache KV » | 333,37 s (« faire » finit à 332,94) |
| 6:19 | Le cache en 4 bits : attention à la qualité | « Par contre, il faut aussi faire attention au 4 bits » | 379,54 s ; **ajouté** (« vitesse » finit à 379,08) |
| 6:43 | La liste, dans l'ordre | « Donc maintenant, qu'est-ce qu'il te faut » | 403,06 s ; le montage dit 6:42, qui tombe dans « conversation » (finit à 402,59) |
| 7:10 | Alors, ta carte est-elle bridée ? | « Alors, est-ce que ta carte est bridée ou pas » | 430,37 s (« tienne » finit à 429,97), **ajouté** (le chapitre « À la prochaine » du montage, 7:26, tombe au milieu de « vram ») |
| 7:21 | La suite : l'IA sur une carte de 8 Go | « Et si ta carte n'a que 8 gigas » | 440,81 s ; à 7:21 (441,0), « et si » est déjà dit (0,2 s) |

15 chapitres, premier à 0:00, le plus court fait 11 s (7:10 → 7:21) : les trois règles de YouTube sont tenues.

## Tags

```
ia en local, ia locale, ia local, llm local, local llm, llama.cpp, llama cpp, mtp, multi token prediction, qwen 3.8 27b, qwen3.8, 16 go vram, 16gb vram, vram, lm studio, ollama, ollama vs llama.cpp, carte graphique ia, ia plus rapide, accélérer ia locale, rtx 5080, rtx 5060 ti, strata, technovore
```

**297 caractères sur 500.** « multi token prediction » est le sens de MTP ; « qwen3.8 » corrige l'écriture.

## Commentaire épinglé

```
La question du cache KV (5:36) : ça fait écrire plus vite, oui ou non ? Réponds avant de regarder la suite. Et dis-moi ta carte, ton moteur et ta vitesse avec et sans MTP.
```

La voix dit « dis-le-moi en commentaire » à 5:39 : le commentaire épinglé reprend cette promesse.

## Sous-titres

- Français : [`meme-carte-plus-rapide.fr.srt`](meme-carte-plus-rapide.fr.srt) (174 sous-titres, 0:00-7:34).
- Anglais : [`meme-carte-plus-rapide.en.srt`](meme-carte-plus-rapide.en.srt), mêmes numéros et mêmes temps.
- Dans Studio : « Avec synchronisation », langue de la vidéo en français.
- Les temps viennent des mots de la voix finale (`voix.words.json`, la voix démarre à 0 : temps de la voix = temps de la vidéo). Le texte est ce que la voix dit, pas le script : « ma vidéo précédente », « dans cette vidéo », le vouvoiement de la fin (« vous avez aimé », « boostez la vidéo »), « surtout actuellement avec les prix incroyables… ». La phrase « Moi, j'ai rien testé » n'est plus dite.

## Suggestions

Le pourquoi est dans [`etudes/suggestions-2026-10-23.md`](../../etudes/suggestions-2026-10-23.md). **vidIQ indisponible** (outils de recherche absents) : recherches YouTube « llama.cpp MTP plus rapide », « ia locale plus rapide carte graphique » et « qwen 3.8 27b MTP 16 go », filtre « ce mois-ci », par curl le **18/11/2026** ; dates, vues et pistes audio lues sur la page de chaque vidéo. Pas un recensement complet.

### Les vidéos hôtes

| # | Vidéo | Chaîne | Langue | Vues (18/11) | Sortie |
|---|---|---|---|---|---|
| 1 | *Toutes les astuces pour accélérer votre IA locale. Voici comment faire.* (`RRUhZ1rpovk`) | Alex Grankin | Piste française doublée (original anglais ; miniature « LOCAL AI 3× FASTER ») | 11 459 | 08/11 |
| 2 | *Mon IA locale va 11 fois plus vite (même PC)* (`VFC16Tb3lwU`) | Nathan Inline | Français | 20 796 | 14/11 |
| 3 | *Ollama vs LM Studio vs llama.cpp (Vitesse de l'IA locale)* (`h8BQOBOsp7c`) | Locally | Piste française doublée (original anglais) | 4 910 | 10/11 |
| 4 | *Votre GPU 8 Go fait tourner Qwen 3.8 27B 5x plus vite maintenant (un nouveau fichier)* (`u_DYZhTZ2IM`) | SimplyExplain | Piste française doublée (original anglais) | 9 711 | 12/11 |
| 5 | *Ce fork de llama.cpp vient de battre Strata de 47 % sur AMD* (`wyYTC-rpp0g`) | Code Unpacked | Piste française doublée (original anglais) | 27 590 | 30/10 |

**Les mots qu'on partage, et ce qu'on ne prend pas** :
1. Alex Grankin : « accélérer », « IA locale ». Pas « toutes les astuces » : la vidéo en traite 6, dans l'ordre.
2. Nathan Inline : « IA locale », « plus vite », « même PC / même carte ». **C'est ton concurrent direct** : même format de titre, même carte de 16 Go. Ne prends ni son « 11 fois » ni son récit ; la voix ne le cite pas. À regarder 5 minutes avant la sortie, pour ne pas sortir un titre jumeau.
3. Locally : « llama.cpp », « LM Studio », « Ollama », « vitesse ». Pas « Which One? » (un duel de moteurs : ta vidéo y consacre un chapitre d'environ 50 s).
4. SimplyExplain : « Qwen 3.8 27B », « plus vite », « GPU ». Pas « 5x » ni « 8 Go » : **ta vidéo suivante est sur 8 Go** (le 23/11), garde le mot pour elle.
5. Code Unpacked : « llama.cpp » seulement. Pas « 47 % », pas AMD ni le scandale Strata.

À surveiller hors planche : *llama.cpp vient de créer d'énormes modèles MoE 4 fois plus rapidement* (Code Unpacked, 18 671 vues, 21/10, piste française doublée), la source du « 4× » que la vidéo **n'utilise pas** (`sources.md` M20).

### La planche

Les cinq miniatures sont dans [`miniature/hotes/`](miniature/hotes/). `planches.py` a tourné sur des copies renommées (`meme-carte-h.png`, `-i`, `-j`) pour ne pas écraser d'autres planches : [`suggestions-meme-carte-h.png`](../../ressources/miniatures/planches/suggestions-meme-carte-h.png), [`-i`](../../ressources/miniatures/planches/suggestions-meme-carte-i.png), [`-j`](../../ressources/miniatures/planches/suggestions-meme-carte-j.png). Ordre : Alex Grankin, Nathan Inline, **la nôtre**, Locally, SimplyExplain, Code Unpacked.

### La comparaison à 168 px

- **Elle se repère** : fond sombre et uni et une question (« TA CARTE BRIDÉE ? ») au milieu de quatre miniatures qui annoncent un chiffre (3×, 11 fois, 5X, 47 %) et d'une cinquième (« Which One? ») sur une photo d'ordinateur. Notre texte ne contient aucun chiffre : le « 2× » n'est que sur le compteur.
- **h** : le jaune de « BRIDÉE ? » est celui de la case « 5X FASTER » de SimplyExplain (juste en dessous) et du « 47% » de Code Unpacked ; il se confond un peu. **j** : le menthe n'existe nulle part ailleurs dans la colonne et DiCaprio qui pointe est le seul visage qui regarde ailleurs que l'objectif. **i** (sans visage) : le compteur de 1× à 2× devient petit à 168 px, c'est la plus discrète ; les voisines ont de gros chiffres et des visages.
- **Elle promet autre chose** : un doute (« ta carte est bridée ? »), là où les autres promettent un multiplicateur. Mais attention : à 168 px, Nathan Inline (« va 11 fois plus vite », 16 Go, tokens/s) raconte la même histoire en plus gros. Le titre A seul ne suffit pas à s'en séparer ; c'est la question « bridée » qui le fait.
- **Retouche avant de publier** : aucune. Le test h, i, j tranchera ; mon pari est j (même constat que pour Strata).

### L'enchaînement

- **Écran de fin, de 7:32 à 7:43** (les 11 dernières secondes ; la voix dit « on se dit à la prochaine » à 7:32 et finit à 7:34) : à gauche, la vidéo Strata ([`892vB0mRY8U`](https://www.youtube.com/watch?v=892vB0mRY8U), « Je l'ai testé chez moi ») ; à droite, la vidéo « 16 Go de VRAM » ([`jMZFDNbwRNI`](https://www.youtube.com/watch?v=jMZFDNbwRNI), *16 Go de VRAM : Est-ce vraiment suffisant pour les LLM ?*). YouTube demande au moins 5 s : 11 s, c'est bon. Remplace la vidéo de droite par *Qwen 27B sur 8 Go* à sa sortie, le lun. 23/11.
- **Fiche pendant le plateau de rétention** : vers **4:15 à 4:22**, vers la vidéo Strata (`892vB0mRY8U`) : la voix dit « celles de ma vidéo précédente sont affichées à l'écran » (4:15) puis « dans la vidéo précédente, je te l'ai montré : la RAM pleine, et le disque qui se met à lire » (4:19). Plateau inconnu : recale-la sur la courbe au radar du 19/11. Une seconde fiche possible à 3:47 (« comme dans la vidéo précédente ») vers la même vidéo.
- **Renvois** : dans la vidéo Strata (`892vB0mRY8U`), l'écran de fin ou une fiche près de la fin peut pointer cette vidéo (« jeudi : même carte, 2 fois plus rapide » est déjà dans sa description).

## À vérifier avant l'upload

- **Écoute les sous-titres une fois sur la vidéo** : je n'ai pas écouté l'audio ; les temps sont ceux de `voix.words.json`. Doutes de transcription :
  - **« des 6 mesures du début »** (6:30) : `voix.words.json` écrit « du modèle » ; j'ai mis « du début » (téléprompteur, et seul sens possible) ; réécoute 6:30 ;
  - **« comment faire pour faire tenir »** (7:24) : j'ai retiré la répétition (« comment faire tenir ») ;
  - **vouvoiement** de la fin (« j'espère que vous avez aimé… boostez la vidéo », 7:26 à 7:32) : gardé tel que dit ;
  - « le drop violent de vitesse » (6:16) : l'anglicisme est dit, gardé ;
  - la « 4060 Ti » (1:39) est découpée par la transcription (« ti » sur 0,01 s) : sans effet.
- **Chiffres relus contre `sources.md`** : à 1:03, la voix dit « sur une 5080, on passe de 53 à 101 » (M1 : 53,4 → 101,3 ✓) ; « 15 à presque 29 » (M4 : 15,2 → 28,7 ✓) ; « les 6 mesures ont toutes été faites sur llama.cpp » (3:30 : M3, M4 et M6 n'ont pas leur moteur écrit dans `sources.md`, section A l'affirme pour M1 à M6).
- **Avant de coller** : le lien Strata de la description pointe la version 0.2.14 (le 15/11) ; si le projet sort un correctif d'ici jeudi, c'est toujours la bonne page de version.
- `calendrier.md` dit encore « Montage » : passe la ligne à « Programmé » une fois la vidéo chargée (et le README).
- Après la sortie : skill `radar` (règle du dépôt).
