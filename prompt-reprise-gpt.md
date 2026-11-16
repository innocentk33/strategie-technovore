# Prompt de reprise : 4 scripts Technovore (à coller dans GPT)

> Écrit le 16/11/2026. Joins à la conversation les fichiers listés dans « Fichiers à joindre », puis colle tout ce qui suit la ligne.

**Fichiers à joindre** (dans cet ordre de priorité) :
1. `projets/meme-carte-plus-rapide/script.md` et `teleprompteur.txt` : le modèle à imiter (ma voix, le format).
2. `projets/meme-carte-plus-rapide/grill-v1.md` et `sources.md` : le format du roast et des sources.
3. Les 4 fiches : `projets/qwen-27b-8go/fiche.md`, `projets/carte-par-budget/fiche.md`, `projets/deux-cartes-occasion/fiche.md` (+ son `sources.md`), `projets/cout-deepseek-flash/fiche.md`.
4. `etudes/transcriptions/simplyexplain-u_DYZhTZ2IM.md` et `redstapler-ye50BbXEczo.md`.
5. `.claude/rules/script.md`.
6. Les skills, copiés dans `ressources/skills-gpt/` : `youtube-script-et-hook.md` (pour la V1) et `youtube-script-grill.md` (pour le roast). Les autres (montage, miniature, voix) serviront plus tard.

---

Les fichiers joints dont le nom commence par « Skill » sont des méthodes à suivre : ils ont été écrits pour un autre assistant, ignore ce qui parle d'outils ou de commandes que tu n'as pas, et garde la méthode.

Tu m'aides à préparer les scripts de ma chaîne YouTube **Technovore** : de la tech en français, surtout l'IA en local (faire tourner une IA sur son propre PC). Mon public : 63 % en Afrique francophone, 94 % a moins de 35 ans, beaucoup de joueurs. Nous sommes en novembre 2026. **Les modèles et les cartes dont on parle sont sortis après tes connaissances : ne te fie à aucun souvenir. Tout chiffre doit venir d'une page que tu ouvres aujourd'hui, ou des fichiers que je te donne.**

## Ce qu'il faut produire

Pour chacune des 4 vidéos ci-dessous, dans cet ordre et **une vidéo à la fois** :

1. **Recherche** : `sources.md`, des faits numérotés, chacun avec son URL exacte, sa date, le chiffre exact, et un statut : ✅ lu à la source primaire · ⚠️ source secondaire ou mesure unique · ❌ introuvable ou contredit.
2. **Deuxième vérification** : rouvre chaque source et relis chaque chiffre. Liste les corrections. Je tiens à ce que tout soit vérifié deux fois.
3. **Script V1** (`script-v1.md`), avec la méthode du fichier joint `youtube-script-et-hook.md`. Si elle contredit mes règles ci-dessous, mes règles gagnent.
4. **Roast** (`grill-v1.md`) : une critique sans complaisance de la V1, notée sur 10. Applique à la lettre le fichier joint `youtube-script-grill.md`, **variante storytelling** (test des 30 secondes, axe 10 sur les liaisons orales) ; la grille plus bas n'en est que le résumé.
5. **Script corrigé** (`script.md`), puis le **téléprompteur** (`teleprompteur.txt`).

Arrête-toi après chaque vidéo et attends mon « suivante ».

## Les 4 vidéos

Toutes sont **calculées** : je n'achète rien et je ne teste rien. Tout vient de mesures publiées par d'autres, de fiches techniques et de calculs.

**1. Lun. 23 nov. : Qwen 3.8 27B sur une carte de 8 Go, 5 fois plus vite avec un seul fichier** (8 à 10 min)
- Inspirée de deux vidéos (transcriptions jointes). Ne reprends pas leur angle : l'une filme son essai, l'autre fait le mode d'emploi de llama.cpp.
- Mon angle : l'avant/après pour quelqu'un qui a LM Studio et une carte de joueur de 8 Go. Ce qu'on gagne (la vitesse), ce qu'on paie (la mémoire de conversation, la qualité en 2 bits), et pour quel usage ça vaut le coup.
- À vérifier d'abord : le fichier `UD-IQ2_XS` de 7,63 Go sur `huggingface.co/unsloth/Qwen3.8-27B-GGUF` ; les scores sur `unsloth.ai/docs/models/qwen3.8` (ce sont leurs mesures, pas des mesures indépendantes) ; l'article arXiv 2611.06858 ; la part des cartes de 8 Go dans l'enquête Steam ; les réglages équivalents dans LM Studio.
- **Le point faible** : le « ×5 » (3 → 18 tokens par seconde) vient d'une seule mesure, sur une GTX 1080 Ti bridée à 8 Go. Cherche une deuxième mesure sur une vraie carte de 8 Go (Reddit r/LocalLLaMA, discussions Hugging Face, GitHub). S'il n'y en a pas, le script dit « une mesure publiée » et le titre ne promet pas « 5× » comme une vérité générale.

**2. Jeu. 26 nov. : La meilleure carte graphique pour l'IA locale, à chaque budget (veille du Black Friday)** (10 à 12 min)
- Paliers d'environ 300, 500, 800 et plus de 1 000 €, en euros TTC, chez des marchands français (LDLC, TopAchat, Materiel.net, Amazon.fr). Pour chaque carte : sa VRAM, le plus gros modèle qui tient en entier, une vitesse publiée.
- Le piège à montrer : une carte plus chère avec moins de VRAM (12 Go contre 16 Go).
- Un encart Afrique (Abidjan, Kinshasa, Douala) seulement si tu trouves des sources fiables ; sinon dis-le-moi.
- Vidéo d'achat : place la phrase « **Si cette vidéo t'a évité un mauvais achat, abonne-toi.** » juste après le moment où la vidéo rend service, jamais dans les 30 premières secondes.
- Elle annonce la vidéo des 32 Go, qui sort **après** elle (30 nov.).

**3. Lun. 30 nov. : 32 Go de VRAM pour Qwen 27B, au moins cher** (11 à 13 min)
- Les routes vers 32 Go, comparées en euros : deux cartes d'occasion, Tesla V100 32 Go, deux Intel Arc, Arc Pro, Radeon AI Pro R9700, Ryzen AI Max+, Mac à mémoire unifiée, deux RTX 5060 Ti 16 Go, une RTX 5090.
- Pourquoi 32 Go : le cache KV du contexte long remplit 24 Go avant le contexte complet.
- Mon angle : les euros, la garantie en France (2 ans même d'occasion chez un pro, 14 jours de rétractation), et ce que ça demande à un vrai PC (alimentation, emplacements).
- Les faits F1 à F79 de `sources.md` (joint) sont déjà vérifiés : ne les refais pas, complète-les.
- Elle sort 3 jours **après** le Black Friday : ne dis pas « avant le Black Friday ». Ma vidéo Qwen 4, déjà en ligne, l'avait annoncée pour le 23 : pas besoin d'en parler.

**4. Jeu. 3 déc. : DeepSeek V4.1 Flash sans carte graphique : 64 Go de RAM suffisent ?** (10 à 12 min)
- Fait de départ (à vérifier) : avec llama-modchip, un fichier de 56,93 Go à 1,71 bit par poids tourne à 8,66 tokens par seconde sur un portable avec 64 Go de DDR5, mais avec une perplexité 60,8 % moins bonne.
- Mon angle : le prix en euros et en FCFA de la RAM qu'il faut à chaque palier de qualité (64, 96, 128 Go), comparé à l'abonnement et à l'API.
- **À trancher à la source** : la version exacte du modèle (« V4 Flash 0731 » ou « V4.1 Flash »).
- Explique en quelques phrases pourquoi la RAM suffit ici (un modèle « MoE » ne lit qu'une petite partie de ses poids à chaque mot) : la vidéo qui l'expliquait en détail sort plus tard.

## Les règles du « calculé » (non négociables)

1. Dans les 30 premières secondes, je le dis : « ces chiffres sont les leurs, je n'ai rien testé chez moi ».
2. Chaque chiffre a sa source datée. Ne recopie jamais le chiffre d'une vidéo : remonte à sa source.
3. Pour un chiffre important, deux mesures qui concordent. S'il n'y en a qu'une, le script le dit.
4. Une estimation n'est jamais présentée comme une mesure (« environ », « au mieux », « d'après »). Jamais « j'ai testé », jamais de chiffre à moi.
5. Prix en euros, TVA comprise, avec la date et le mot « affiché » ou « demandé ». Si tu ne peux pas ouvrir la page du marchand, écris `[PRIX À RELEVER]`. Ne convertis jamais des dollars sans le dire. Pas de coût d'électricité.
6. Sépare toujours la vitesse d'écriture et la vitesse de lecture du prompt.
7. **N'invente jamais** : ni chiffre, ni citation, ni anecdote personnelle. Là où il faut mon vécu ou mon avis, laisse `[CROCHET : ce que je dois dire avec mes mots]`. Le script doit tenir sans les crochets.

## Ma façon de parler

- Je **tutoie** le spectateur et je dis « on ». Jamais « vous », jamais « nous allons ». Je parle comme à un ami, je ne récite pas une fiche.
- Les faits arrivent avec des **liaisons orales** et une réaction : « donc », « du coup », « en fait », « sauf que », « en effet », « par contre », « voilà comment ». Vise au moins 1,5 liaison pour 100 mots.
- Phrases courtes. Des images du quotidien pour expliquer (exemple à moi : « le MTP, c'est comme les suggestions du clavier de ton téléphone »).
- Humour de joueur et de pop culture, à petite dose (Monster Hunter, Thanos, « farmer l'aura », « faut pas abuser »), et des piques contre les abonnements.
- **Aucun nom de chaîne ou de créateur dans la voix** : « un testeur », « un utilisateur sur une 4060 », « une chaîne anglophone ». Les noms vont dans `sources.md`.
- Pas d'ouverture centrée sur moi (« cette carte, c'est la mienne »), pas de « salut à tous », pas de « dans cette vidéo ».
- Je finis par « Allez, salut ! ».
- À bannir, parce que ça « fait IA » : « plongeons », « décortiquons », « il est important de noter », « en résumé », « que vous soyez… ou… », les triplets d'adjectifs, les questions rhétoriques à la chaîne, les tirets longs, les phrases qui annoncent ce qu'on va dire au lieu de le dire.

Extrait de mon dernier téléprompteur, pour le ton :

> Sur une carte de 16 gigas, un testeur allume un seul réglage,
> et son IA écrit 2 fois plus vite :
> de 29 à 64 tokens par seconde.
> Même fichier, et rien acheté.
>
> Et ils sont 6 testeurs, sur 5 modèles de cartes de 16 gigas,
> à trouver entre 1,9 et 2,3 fois plus vite.
> Du coup, ta carte, elle serait pas bridée,
> sans que tu le saches ?

## La structure d'un script

- **0:00-0:15, le plus fort de la vidéo** : le résultat, le chiffre le plus fou ou l'image de la miniature. Aucun contexte, aucune présentation.
- **0:15-0:30** : aucune phrase de remplissage. Chaque phrase confirme le clic, ouvre une question ou fait monter l'enjeu. La question centrale est posée avant 30 s.
- **Vers 0:30, le plan en livrables concrets** : 3 ou 4 choses précises que le spectateur va obtenir, plus la révélation de la fin. Pas une étiquette vague (« on fait les comptes de ta carte » n'annonce rien).
- **Juste après le plan** : la première partie commence par une réponse ou une démonstration, jamais par une définition. La théorie vient quand on en a besoin.
- Compte **145 mots par minute**. Indique les `[VISUEL : …]` entre crochets. Montre aussi ce qui ne marche pas : c'est ce qui rend crédible.
- En tête du script : le titre, la durée estimée, un tableau des parties avec leurs timecodes. En fin : la liste des crochets à remplir et des questions pour moi.

**Le téléprompteur** (`teleprompteur.txt`) : une ligne = un souffle, une ligne vide = une respiration. Les nombres en chiffres (« 16 gigas », « 7900 euros », « 20 % »), sauf « un », « zéro » et ce qui n'est pas une quantité. Les `[MARQUEURS]` et les `(indications)` ne se lisent pas.

## La grille du roast

Note chaque axe sur 10, cite les phrases fautives, et propose la réécriture :
1. Les 15 premières secondes : est-ce vraiment le meilleur moment ?
2. Les 30 premières secondes : une seule phrase de remplissage, et c'est raté. La question centrale est-elle posée ?
3. Le plan : des livrables concrets, ou des étiquettes ?
4. La promesse du titre est-elle tenue, et où ?
5. Le problème profond : pourquoi ça compte pour quelqu'un qui a cette carte ?
6. L'enchaînement « mais / donc » entre les parties, au lieu de « et puis ».
7. Les liaisons orales (compte-les pour 100 mots) et le ton d'ami.
8. Les tics d'IA (liste-les tous).
9. Les faits : chaque chiffre a-t-il son numéro dans `sources.md` ? Y a-t-il une estimation présentée comme une mesure, un « j'ai testé », un nom de chaîne ?
10. La fin : un verdict par profil, mon avis en crochet, le renvoi vers la vidéo suivante.

Commence par la vidéo 1. Avant d'écrire, dis-moi ce que ta recherche confirme, ce qu'elle contredit dans la fiche, et s'il existe une deuxième mesure du « ×5 ».
