# IA en local : comment lire le nom d'un modèle : script v1

**Titre** : *IA en local : comment lire le nom d'un modèle (35B, A3B, Q4_K_M…)* (titre 3 de la fiche, recommandé).

**V1 du 23/10/2026** (phase 3), écrite d'après la [fiche](fiche.md) (corrections de la 2e vérification comprises) et [`sources.md`](sources.md) (colonne « 2e vérif »). Sortie : **lun. 30 nov. 2026, 18 h**. Le grill vient ensuite (`grill-v1.md`).

**Durée** : 1 995 mots de voix off (mesure de `controle.py` en bas), plus tes crochets. À 165 mots/min : 12 min ; à ton débit d'ArtCraft (145) : 13 min 45. Les timecodes ci-dessous sont approximatifs ; à recaler sur la vraie prise.

**Texte et sous-texte** :
- **Texte** : un nom de fichier se lit morceau par morceau, et avec une règle de trois (paramètres × bits ÷ 8) tu sais s'il rentre dans ton PC avant de le télécharger.
- **Sous-texte** : ce vocabulaire a l'air d'un code d'initiés, c'est juste un code. L'IA locale n'est pas réservée aux grosses machines : la même règle marche sur un PC de 8 Go. Et personne ne te l'explique, alors c'est moi. (Dit à 0:40, repris dans la fin.)

**Fil rouge** : le vrai fichier que tu télécharges pour tes essais, `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf`. On le découpe de gauche à droite (sections 2 à 6), puis on suit ce qui l'entoure : moteur → API → routeur → harnais → toi (sections 6 à 9). La fin relit le nom d'une traite.

**Boucles ouvertes** :
1. « Dix-huit gigas, ma carte en a seize » (0:10) → refermée dans la fin (le banc de touche, préparé dans la section 3).
2. « Il manque deux gigas, où ils sont passés ? » (5:20) → refermée 30 s plus tard (on ouvre le fichier : plus de la moitié en 3 bits).
3. « L'une de ces pièces peut envoyer tes textes ailleurs » (relance à 60 %, 7:40) → refermée dans la section 8 (le routeur).

**Place dans la série** : la vidéo sort après Claude #1 (2 nov., testé) et Coût Claude (16 nov., calculé). C'est le guide de lecture de la série : on y renvoie à 0:30 (« tu les as vus défiler ») et l'écran de fin pointe Claude #1, où ces fichiers tournent pour de vrai.

**Format** : vulgarisation, **calculé** (règle 1 dite à 0:25 et 1:10). Aucune vitesse, aucun benchmark : les mesures sont dans Claude #1. Tant que tes essais sur la 5080 ne sont pas faits, tout ce qui tourne ou s'affiche chez toi est entre crochets.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture ; les noms de fichier s'écrivent en code dans les visuels et se disent comme ils se lisent (« IQ quatre XS »). Rien de tout ça ne se lit, sauf la voix off.

**Les images de la vidéo** (aucune n'est le « JPEG » de Tech With Tim et Mark Kashef) :
- le nom = une **étiquette** qu'on découpe en morceaux ;
- les experts = une **équipe de foot** : tout l'effectif dans le bus, neuf joueurs sur le terrain, le reste sur le banc ;
- la quantification = le **menu graphique** d'un jeu (Ultra, Élevé, Moyen, Bas) ;
- le moteur = l'**émulateur**, le gguf = la ROM.

---

## 0. Hook (0:00 – 0:30) · objectif : 70 % de rétention à 0:30

[VISUEL : écran noir. Le nom se tape lettre par lettre, en gros, police mono : `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf`. Pas de titre, pas de logo, pas de visage.]
[SON : clavier mécanique, une touche par caractère, accéléré.]

Qwen trois point six, trente-cinq B, A trois B, UD, IQ quatre XS, point gguf.

On dirait un mot de passe Wi-Fi. En fait, c'est une IA, à faire tourner chez moi. Dix-huit gigas.

[VISUEL : sous le nom, une barre « 18,2 Go » se remplit. À côté, la jauge de la RTX 5080 : « 16 Go ». La barre dépasse la jauge, clignote en rouge.]
[SON : buzzer bref, façon « Game Over » de borne d'arcade.]

Sauf que ma carte graphique en a seize.

[CROCHET : CE QUI S'EST PASSÉ QUAND TU L'AS LANCÉ, APRÈS TON ESSAI, EN UNE PHRASE. TANT QUE L'ESSAI N'EST PAS FAIT : « ET POURTANT, JE VAIS LE LANCER. »]

Chaque morceau de ce nom te dit la place qu'il prend, comment il calcule, et à quel point il est bête. Donc comment tu sais si un modèle rentre dans ton PC, avant de griller dix-huit gigas de data ?

[VISUEL : le nom se fend en cinq étiquettes, chacune avec un « ? ».]

Aujourd'hui, pas de mesure : on apprend à lire.

---

## 1. Un code, pas un secret (0:30 – 1:20)

[VISUEL : capture de Hugging Face, la liste des fichiers du dépôt Unsloth de Qwen3.6, des dizaines de noms du même genre qui défilent.]

Ce genre de nom, tu le croises sur Hugging Face, là où tout le monde dépose ses modèles. Et si tu as vu mes vidéos de novembre sur Claude, tu les as vus défiler.

Sauf que personne ne t'explique comment ça se lit. Du coup, ça a l'air d'un code d'initiés. En fait, c'est juste un code.

[CROCHET : TA PREMIÈRE FOIS DEVANT UN NOM COMME ÇA, CE QUE TU AS PENSÉ OU FAIT, EN UNE OU DEUX PHRASES.]

On le découpe de gauche à droite, puis on regarde ce qu'il y a autour, parce que le fichier tout seul ne fait rien. Et à la fin, je te dis comment on compte lancer dix-huit gigas avec une carte de seize.

[VISUEL : la carte mentale, en gris, encore éteinte : modèle → fichier → moteur → API → routeur → harnais → toi. Elle revient à chaque chapitre, une case s'allume à chaque fois.]

Les mesures, elles sont dans ma vidéo sur les seize gigas de VRAM. Ici, je fais des calculs, et chaque chiffre a sa source en description.

---

## 2. Qwen3.6 et 35B : le nombre de nombres (1:20 – 2:30)

[VISUEL : carte mentale, la case « modèle » s'allume. Le nom revient, seuls « Qwen3.6 » et « 35B » restent en couleur.]
[SON : « clac » d'étiquette qu'on arrache.]

Premier morceau : Qwen trois point six. Facile : la famille, puis la version.

Deuxième morceau : trente-cinq B. B, c'est billion en anglais, donc milliard. Trente-cinq milliards de paramètres.

Et un paramètre, en fait, c'est juste un nombre. Un modèle, c'est un énorme tas de nombres, réglés pendant l'entraînement. Tu lui poses une question, il calcule avec ces nombres, et un mot sort. Puis un autre.

[VISUEL : un mur de nombres à virgule qui défilent ; une phrase sort mot par mot de l'autre côté.]

Donc trente-cinq B, c'est le nombre de nombres dans le fichier. Et dans l'en-tête du fichier, on en compte trente-cinq virgule cinq milliards. Le nom ne ment pas.

[VISUEL : l'en-tête du GGUF en capture, le compteur « 35 505 000 000 » surligné.]

Plus il y a de nombres, plus le fichier est gros. Retiens ça, parce que c'est la moitié de notre règle de calcul.

---

## 3. A3B : trente-cinq milliards dans le bus (2:30 – 3:45)

[VISUEL : le nom, « A3B » s'allume. Un gros « ? » au-dessus, comme sur la miniature.]

Troisième morceau, et là, ça devient bizarre : A trois B. A comme activated. Trois milliards activés.

Attends. Il en a trente-cinq, ou trois ?

Les deux. C'est un modèle à experts. Imagine une équipe de foot avec un effectif énorme. Chez Qwen, il y a deux cent cinquante-six experts, et pour chaque mot, l'entraîneur en fait jouer neuf : huit choisis pour ce mot-là, plus un qui joue tout le temps. Résultat : sur trente-cinq milliards de nombres, trois milliards travaillent à chaque mot.

[VISUEL : un terrain vu de haut, 256 petits joueurs sur le banc et les tribunes ; 9 s'allument et entrent sur le terrain, puis 9 autres au mot suivant. Compteur « 3 milliards actifs / 35 ».]
[SON : coup de sifflet à chaque changement.]

Sauf que voilà le piège. Ça réduit le calcul. Ça ne réduit pas la place. Pour le match, tout l'effectif doit monter dans le bus, même ceux qui restent sur le banc. Le fichier contient bien les trente-cinq milliards.

[VISUEL : le bus, plein à craquer, étiqueté « 18,2 Go ». Légende : « A3B : moins de calcul, pas moins de place ».]

En face, l'autre fichier que je télécharge : gemma quatre, douze B, de Google. Douze milliards, et pas de A. Normal : c'est un modèle dense. Tout le monde joue, à chaque mot.

[VISUEL : `gemma-4-12b-it-Q6_K.gguf` à côté du nom de Qwen ; sur son terrain, tous les joueurs s'allument en même temps.]

Donc un A dans un nom, ça veut dire : moins de calcul, mais autant de poids. Et garde le banc de touche en tête, il va resservir.

[VISUEL : carton discret, 3 s : « S'abonner », bouton qui pulse une fois.]

Au passage, si un nom comme ça t'a déjà fait fermer l'onglet, abonne-toi : ici, je fais tourner l'IA chez moi et je t'explique ce qu'il y a dedans.

---

## 4. IQ4_XS : les réglages graphiques du modèle (3:45 – 6:45)

[VISUEL : carte mentale, la case « fichier » s'allume. Le nom : « UD » grisé, « IQ4_XS » en couleur.]

On saute UD, on y revient. Le gros morceau, c'est IQ quatre XS : la quantification. Le mot fait peur, l'idée, tu la connais.

Tu joues sur PC ? Tu connais le menu des graphismes. Textures en Ultra, en Élevé, en Moyen. Plus tu baisses, moins ça prend de mémoire, et plus l'image bave. La quantification, c'est ce réglage-là, pour un modèle.

[VISUEL : un menu d'options graphiques façon jeu vidéo, « Qualité des textures : Ultra ». On descend d'un cran à chaque mot : Ultra, Élevé, Moyen, Bas. À droite, une jauge « VRAM » qui baisse.]
[SON : le « bip » de menu à chaque cran.]

En fait, en pleine précision, chaque nombre prend seize bits. Quantifier, c'est l'arrondir pour le ranger sur moins de bits.

[VISUEL : `0,817346…` → `0,817` → `0,82` → `0,8`. Sous chaque étape, le nombre de bits : 16, 8, 4, 2.]

Et le chiffre dans le nom, c'est à peu près ça : le nombre de bits. Q huit, c'est l'Ultra, le plus proche de l'original. Q quatre, c'est le Moyen. Q deux, c'est le Bas, et là, ça se voit.

D'ailleurs, sur un modèle testé par un labo indépendant, le quatre bits fait aussi bien que l'original. À deux bits, ça baisse nettement. Et à un bit, il répond presque au hasard.

[VISUEL : trois barres, « Q4 = original », « Q2 : en baisse nette », « 1 bit : presque le hasard ». Source à l'écran : Quesma, 26/08/2026, sur Qwen3.8-27B.]

Les lettres autour, maintenant. K, c'est une famille de méthodes. Le I devant, c'est une matrice d'importance : elle repère les nombres qui comptent le plus, pour les arrondir avec soin. Et le XS derrière, c'est la variante : plus elle est petite, plus le fichier est léger. Aucune doc ne définit ces lettres mieux que ça.

[VISUEL : l'étiquette « IQ4_XS » découpée : « I » = importance, « Q4 » = environ 4 bits, « XS » = variante légère.]

Du coup, voilà la règle de calcul. Paramètres, fois bits, divisé par huit. Et tu as la taille en gigas, à quelques pour cent près.

[VISUEL : la formule en grand : `paramètres × bits ÷ 8 ≈ Go`.]

On l'essaie sur le Gemma, en Q six K : environ six virgule cinq bits. Douze milliards, fois six virgule cinq, divisé par huit : neuf virgule huit gigas. Et le fichier sur Hugging Face ? Neuf virgule soixante-dix-neuf. Pile.

[VISUEL : le calcul qui se pose, puis la capture Hugging Face « 9.79 GB » qui vient se coller à côté. Tampon « ✓ ».]
[SON : « ding » de bonne réponse.]

Maintenant, notre Qwen, en IQ quatre XS, donc environ quatre bits et demi. Ça devrait faire à peu près vingt gigas. Sauf que le fichier en fait dix-huit. Il manque deux gigas. Où ils sont passés ?

[VISUEL : « ≈ 20 Go » contre « 18,2 Go », un trou entre les deux barres.]
[SON : musique coupée net.]

C'est là qu'UD revient. UD, c'est la recette maison d'Unsloth, l'équipe qui a fabriqué ce fichier : chaque couche du modèle reçoit son propre nombre de bits. Et quand on lit l'en-tête, surprise. Le nom dit IQ quatre. Mais plus de la moitié du fichier est en trois bits.

[VISUEL : un camembert qui se remplit : 59 % IQ3_S, 29,5 % IQ4_XS, le reste en Q8_0, Q6_K et autres. Au centre : « 4,10 bits en moyenne ».]

Cinquante-neuf pour cent en IQ trois. En moyenne, quatre virgule un bits. Et trente-cinq virgule cinq, fois quatre virgule un, divisé par huit… dix-huit virgule deux. Au chiffre près.

[VISUEL : le calcul qui tombe sur « 18,2 Go », le trou se referme.]

Ce n'est pas une arnaque, c'est la recette. Retiens juste ça : la règle est juste, c'est le nom qui ne dit pas tout.

Et avant que tu me l'écrives : Hugging Face dit dix-huit virgule deux, Windows dira environ dix-sept. Pas une erreur : deux façons de compter les gigas.

[VISUEL : « 18,2 Go » (Hugging Face) et « 16,9 Go » (Windows) côte à côte, une flèche « mêmes octets ».]

---

## 5. Et sur un PC de huit gigas ? (6:45 – 7:40)

[VISUEL : la jauge passe de « 16 Go » à « 8 Go de RAM, pas de carte graphique ».]

Et si tu n'as pas de carte à seize gigas ? Bonne nouvelle : la règle marche sur n'importe quelle machine.

Un petit modèle de quatre milliards, en Q quatre, environ quatre virgule neuf bits : environ deux virgule quatre gigas. Donc ça passe dans huit gigas de RAM, même sans carte graphique. Plus lentement, mais ça passe. C'est un calcul, pas un test.

[VISUEL : le calcul, avec un tampon « CALCUL » (pas « TESTÉ »).]

Et regarde le Gemma à tous les réglages : de vingt-trois virgule huit gigas en pleine précision, jusqu'à quatre virgule deux en IQ deux.

[VISUEL : la balance. À gauche, les cinq fichiers de Gemma 12B qui rétrécissent (23,8 → 12,7 → 9,79 → 7,12 → 4,21 Go). À droite, un plateau « 8 Go ». On les pose un par un.]

Sur un PC de huit gigas, le Q quatre, à sept virgule un gigas, laisse moins d'un giga pour ton système et ta conversation. C'est trop juste. L'IQ deux, lui, rentre. Sauf qu'à deux bits, on l'a vu, la qualité baisse nettement.

Et ta conversation prend de la place en plus, qui grandit avec sa longueur.

Et tout ça, tu le sais avant de télécharger. Quand chaque giga de data se paie, c'est tout l'intérêt.

---

## 6. .gguf : la ROM et l'émulateur (7:40 – 8:50) · relance à 60 %

[VISUEL : le nom, « .gguf » s'allume en dernier.]

Dernier morceau : point gguf, le format. Créé par Georgi Gerganov, l'auteur de llama.cpp, il range dans un seul fichier les nombres et leur fiche d'identité. Son cousin, safetensors, ne contient que les nombres.

[SON : coupure de la musique, silence d'une seconde.]
[VISUEL : un double-clic sur le fichier. Rien. Le curseur tourne, puis s'arrête.]

Voilà, tu sais lire le nom. Sauf que si tu double-cliques sur ce fichier, il ne se passe rien. Dix-huit gigas de nombres, et aucun bouton Play. Entre lui et toi, il manque encore des pièces. Et l'une d'elles peut envoyer tes textes chez quelqu'un d'autre.

[VISUEL : carte mentale, la case « moteur » s'allume.]

La première, c'est le moteur. Tu as déjà joué à un vieux jeu sur émulateur ? La ROM toute seule ne fait rien. Ici, le gguf, c'est la ROM, et le moteur, c'est l'émulateur : il charge les nombres et fait les calculs.

[VISUEL : une cartouche « .gguf » qui glisse dans une console étiquetée « moteur ».]

Le plus connu, c'est llama.cpp, libre. Ollama est né dessus, et il a maintenant son propre moteur, sur la même base de calcul. LM Studio, une appli avec des boutons, s'appuie aussi dessus, mais elle n'est pas open source.

[VISUEL : les trois noms en cartes, avec une étiquette chacun : « libre », « libre », « appli fermée ». Pas de logo.]

Et le moteur ouvre une porte : une API. En gros, une adresse sur ton PC, à laquelle les autres programmes envoient leurs questions. Retiens ce mot, parce que tout le reste passe par là.

[VISUEL : carte mentale, la case « API » s'allume : `localhost:11434`.]
[CROCHET : SI TES ESSAIS SONT FAITS, 5 S DU JOURNAL DE LLAMA-SERVER AU CHARGEMENT DU QWEN (DOSSIER VIDE EN ARRIÈRE-PLAN, AUCUN PROJET FLUTTER).]

---

## 7. Open ne veut pas dire local (8:50 – 10:00)

[VISUEL : trois portes côte à côte : « Local », « Poids ouverts », « Open source (OSI) ».]
[SON : grincement de porte.]

Un truc que je vois mélangé partout : local, open, open source. En fait, c'est trois portes différentes.

Local : il tourne chez toi, rien ne sort.

Poids ouverts : les nombres sont publics, tout le monde peut les télécharger. Qwen trois point six et Gemma quatre, c'est ça, sous licence Apache deux point zéro : tu peux les utiliser, les modifier, même pour un business.

Open source, c'est autre chose. L'OSI, qui tient la définition de l'open source, exige depuis deux mille vingt-quatre trois choses : les poids, le code d'entraînement, et assez d'infos sur les données pour refaire le modèle.

[VISUEL : trois cases à cocher : « poids », « code d'entraînement », « infos sur les données ». Qwen et Gemma cochent la première seulement.]

Qwen et Gemma ne publient ni leurs données ni ce code. Donc au sens de l'OSI, ce n'est pas de l'open source : c'est des poids ouverts, sous une vraie licence libre.

Et Llama ? Meta dit open source. L'OSI dit que sa licence n'en est pas une. Le mot juste, c'est poids ouverts.

[VISUEL : bulle « open source » sortant d'un logo générique « Meta » (texte seul), barrée par un tampon « OSI : non ».]

Maintenant, le piège inverse. Le même Qwen trois point six que mon fichier, on peut l'utiliser dans le cloud, sans rien télécharger. Ouvert ne veut pas dire local. Par contre, pour le local, il te faut des poids que tu peux télécharger.

[VISUEL : l'icône du Qwen passe la porte « Poids ouverts », puis s'envole vers un nuage.]

---

## 8. Le routeur : la porte d'à côté (10:00 – 11:00)

[VISUEL : carte mentale, la case « routeur » s'allume, en pointillés (elle est optionnelle).]

Dans le cloud, où ça ? Par exemple chez OpenRouter. Ça, c'est un routeur : une seule API pour des centaines de modèles. Ta question passe par lui, jusqu'à un fournisseur qui fait tourner le modèle.

[VISUEL : capture d'openrouter.ai, la liste des modèles, recherche « qwen3.6-35b-a3b ». Aucune connexion à un compte, aucune clé à l'écran.]
[VISUEL : schéma : toi → routeur → fournisseur → réponse. Une clé dessinée, floutée, dans la main du « toi ».]

Pourquoi j'en parle ici ? Parce que pour un modèle qui ne rentre pas dans ton PC, c'est la porte d'à côté. Le prix, c'est celui du fournisseur, sans majoration, et OpenRouter prend cinq virgule cinq pour cent quand tu achètes des crédits. Il y a même une vingtaine de modèles gratuits, avec une limite de requêtes par jour.

[VISUEL : la page « Pricing » d'openrouter.ai, « 5.5% » surligné. Bandeau : « relevé le 23/10/2026 ».]

Sauf que là, ton texte sort de chez toi. OpenRouter ne garde pas tes textes par défaut. Mais le fournisseur, c'est une autre boîte. Donc c'est toi qui choisis, dans tes réglages, si tes demandes peuvent aller chez un fournisseur qui s'en sert pour s'entraîner. Voilà la pièce qui peut envoyer tes textes ailleurs.

[VISUEL : le point de la requête quitte la maison, traverse le routeur, arrive chez le fournisseur ; un interrupteur « entraînement : oui / non » s'affiche sur le trajet.]

La même idée, hébergée chez toi, existe aussi : LiteLLM, open source.

---

## 9. Le harnais : des mains pour le modèle (11:00 – 12:05)

[VISUEL : carte mentale, la case « harnais » s'allume.]

Dernière pièce. Jusqu'ici, ton modèle sait répondre, mais il ne sait rien faire. Tu lui demandes de corriger un bug, il t'écrit la correction, et c'est toi qui fais le copier-coller.

Le harnais, c'est ce qui lui donne des mains. Il peut ouvrir tes fichiers et les modifier tout seul. Anthropic le dit comme ça pour Claude Code : c'est la couche autour du modèle, qui lui donne ses outils et qui gère ce qu'il voit.

[VISUEL : la citation d'Anthropic en anglais, traduite en sous-titre. Puis une boucle qui tourne : « chercher le contexte → agir → vérifier ».]

La boucle : chercher le contexte, agir, vérifier. Et recommencer. Quand tu entends « agent IA », c'est souvent de ça qu'on parle.

Par contre, le moteur le fait tourner. Le harnais le fait agir.

[VISUEL : deux cartes : « moteur = il tourne », « harnais = il agit ».]

Et plusieurs harnais acceptent un modèle local : OpenCode, Cline, Aider, et même Codex CLI, d'OpenAI. Claude Code, lui, ça se bricole, mais Anthropic ne le prend pas en charge.

[VISUEL : les cinq noms, une coche « modèle local » pour les quatre premiers, « non pris en charge » pour Claude Code. Dossier vide en arrière-plan, aucun projet Flutter.]

[CROCHET : TON PREMIER HARNAIS, ET CE QUE ÇA T'A FAIT LA PREMIÈRE FOIS QU'IL A MODIFIÉ UN FICHIER TOUT SEUL. UNE OU DEUX PHRASES.]

---

## 10. Fin : relis le nom avec moi (12:05 – 13:05)

[VISUEL : la carte mentale en entier, un point lumineux la traverse d'un bout à l'autre.]
[SON : la musique du hook revient.]

Donc bout à bout : le modèle, c'est des milliards de nombres. Le fichier les range, arrondis. Le moteur les charge et ouvre une API. Le routeur, s'il le faut, passe par le cloud. Le harnais donne des mains. Et au bout, toi.

Maintenant, relis le nom avec moi. Qwen trois point six : la famille. Trente-cinq B : la place. A trois B : le calcul. UD IQ quatre XS : le réglage, environ quatre bits. Point gguf : pour le moteur.

[VISUEL : le nom du hook se reforme, chaque étiquette garde sa traduction en dessous. Plus aucun « ? ».]

Il reste ma question du début : dix-huit gigas, sur une carte de seize. Tu te rappelles le banc de touche ? À chaque mot, neuf experts jouent, et les autres attendent. Du coup, le plan, c'est de laisser une partie des experts dans la RAM du PC, sur le banc, et de garder le reste sur la carte.

[VISUEL : le terrain revient : la carte graphique = le terrain, la RAM = le banc. Une partie des joueurs descend sur le banc, la barre « 18,2 Go » repasse sous la jauge « 16 Go ». Légende : « plan, d'après mon calcul ».]

[CROCHET : CE QUE ÇA A DONNÉ À L'ESSAI : COMBIEN DE COUCHES SUR LA CARTE, COMBIEN D'EXPERTS EN RAM (JOURNAL DE LLAMA-SERVER), CE QU'AFFICHENT NVIDIA-SMI ET WINDOWS. SANS ESSAI : « LE RÉSULTAT, JE TE LE MONTRE DANS MA VIDÉO SUR LES SEIZE GIGAS. »]

Ce nom avait l'air d'un code d'initiés. C'est juste un code. Et maintenant, tu sais le lire : la prochaine fois, tu fais le calcul avant de télécharger.

[CROCHET : CE QUE TU UTILISES, TOI : UN MODÈLE, UN MOTEUR, UN HARNAIS. UNE PHRASE.]

Écris en commentaire un nom de fichier à décoder, avec la mémoire de ton PC. Et pour voir ces fichiers tourner pour de vrai sur ma carte, c'est la vidéo juste là.

[VISUEL : écran de fin, 20 s : « 16 Go de VRAM suffisent-ils pour remplacer Claude ? » à gauche, bouton « S'abonner » à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel + son | Le nom tapé lettre par lettre, au clavier mécanique |
| 0:10 | Chiffre + son | 18,2 Go contre 16 Go, buzzer d'arcade |
| 0:25 | Boucle ouverte | « Comment tu sais si ça rentre, avant de griller 18 gigas de data ? » |
| 0:45 | Sous-texte | « Un code d'initiés ? Juste un code » |
| 1:05 | Visuel récurrent | La carte mentale éteinte (une case s'allume à chaque chapitre) |
| 1:55 | Visuel | Le mur de nombres, la phrase qui sort |
| 2:35 | Question | « Il en a trente-cinq, ou trois ? » |
| 2:55 | Image | L'équipe de foot, neuf joueurs sur le terrain |
| 3:20 | Retournement | « Tout l'effectif monte dans le bus » |
| 3:40 | Appel à l'action | Abonnement (28 %) |
| 4:00 | Lien au vécu | Le menu des graphismes, Ultra → Bas |
| 4:50 | Chiffre | 4 bits = l'original, 2 bits en baisse, 1 bit = le hasard |
| 5:40 | Son + preuve | La règle tombe pile sur Gemma, « ding » |
| 6:00 | Boucle ouverte + coupure | « Il manque deux gigas, où ils sont passés ? » |
| 6:15 | Surprise | Le camembert : 59 % en 3 bits |
| 6:35 | Anticipation | « Avant que tu me l'écrives » : 18,2 contre 17 |
| 6:50 | Changement d'enjeu | Le PC de 8 Go |
| 7:15 | Visuel | La balance des cinq Gemma |
| 7:55 | Coupure + relance (60 %) | Le double-clic qui ne fait rien ; « l'une d'elles peut envoyer tes textes » |
| 8:15 | Image gamer | La ROM et l'émulateur |
| 8:50 | Son + visuel | Les trois portes |
| 9:35 | Retournement | Meta dit open source, l'OSI dit non |
| 10:00 | Boucle refermée | Le même Qwen dans le cloud → le routeur |
| 10:40 | Boucle refermée | « Voilà la pièce qui peut envoyer tes textes ailleurs » |
| 11:00 | Image | Le copier-coller : le modèle sans mains |
| 12:15 | Récapitulatif | Le nom relu d'une traite, plus de « ? » |
| 12:35 | Boucle refermée | Le banc de touche = la RAM |

**Total** : 27 relances en 13 min, environ une toutes les 29 secondes.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:15-0:25 | Moyen | Le crochet de l'essai reste vide tant que tu n'as pas lancé le fichier | Phrase de repli écrite dans le crochet ; la barre qui dépasse la jauge porte l'enjeu à l'image |
| Section 1 | Moyen | 50 s sans nouveau morceau du nom | Captures Hugging Face qui défilent, carte mentale ; à couper en grill si la v2 est longue |
| Les lettres K, I, XS | Élevé | Trois sigles en 25 s, la zone « glossaire » | Une étiquette découpée à l'écran, une seule idée par phrase ; la règle de calcul arrive juste après |
| La règle sur Gemma | Moyen | Des nombres à virgule dits à voix haute | Le calcul s'écrit à l'écran pendant qu'il se dit ; le « ding » sur le résultat |
| Relance (~60 %) | Élevé | Le nom est fini : risque de « j'ai eu ma réponse » | Coupure, double-clic qui ne fait rien, nouvelle menace (« tes textes ailleurs »), boucle du banc de touche encore ouverte |
| Licences | Moyen | Sujet juridique, peu visuel | Trois portes, trois cases à cocher, le tampon « OSI : non » |
| Harnais | Moyen | Fin de vidéo, beaucoup de noms | Cinq noms en une phrase, une seule image (les mains) ; ton crochet vécu juste après |

## Notes de montage

- **Composants à construire une fois** : le nom découpé en étiquettes, la carte mentale (7 cases), le terrain de foot (256 experts, 9 actifs, banc = RAM), le menu graphique, la balance 8/16 Go. La carte mentale et le nom découpé resservent pour llama.cpp (8 févr.) et Louer ou acheter.
- **Charte verte « IA chez moi »**, police mono pour tous les noms de fichier.
- **Interdits à l'écran** : aucune clé d'API collée, aucune connexion d'OpenRouter à un harnais, aucun nom ni dépôt « abliterated » ou « uncensored », aucun projet Flutter en arrière-plan (dossier vide), aucun logo de moteur ou d'entreprise en gros.
- **Captures autorisées** : Hugging Face (dépôts Unsloth et Google), en-tête du GGUF, openrouter.ai (liste des modèles, page Pricing, sans compte connecté), doc d'Anthropic (citation du harnais).
- **Tampons** : « CALCUL » sur tout chiffre calculé (2,4 Go, la balance, le plan du banc de touche), « TESTÉ » seulement sur ce que tu as vraiment lancé.
- **Énergie** : calme, montée toutes les 2 à 3 min : 18 vs 16 (0:10), le bus (3:20), le camembert (6:15), le double-clic (7:55), le banc de touche (12:35).
- **Miniature** : celle de la fiche (le nom découpé, « ? » sous « A3B »). Le hook reprend son image dès la première seconde.

## Faits utilisés

| Ce que dit le script | Section | Ligne de `sources.md` | Statut (2e vérif) |
|---|---|---|---|
| Le fichier `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf` pèse 18,2 Go | 0, 4, 10 | 13 | ✅ |
| 18,2 Go ne tiennent pas dans 16 Go ; il tourne avec une partie des experts en RAM (plan, pas essai) | 0, 10 | 45 ; `modeles-5080.md` | ❌ corrigé (« ça tient » n'est jamais dit) ; plan en crochet |
| 35 milliards au total, 3 milliards activés, 256 experts, 8 + 1 par mot | 3 | 12 | ✅ |
| L'en-tête compte 35,5 milliards de nombres ; A3B réduit le calcul, pas la place | 2, 3 | 12, 44 | ✅ |
| Gemma 4 12B est dense, 11,95 milliards de paramètres | 3, 4 | 14 | ✅ |
| Quantifier = réduire la précision des nombres | 4 | 4 | ✅ |
| Q4_K_M ≈ 4,8 à 4,9 bits ; Q6_K ≈ 6,56 ; IQ4_XS ≈ 4,5 (dits « environ ») | 4, 5 | 1 | ⚠️ formulation de la 2e vérif (« environ ») |
| « Sur un modèle testé par un labo indépendant, le 4 bits fait aussi bien que l'original ; à 2 bits, baisse nette ; à 1 bit, presque le hasard » | 4 | 3 | ⚠️ formulation de la 2e vérif, mot pour mot |
| K = K-quants ; I = matrice d'importance | 4 | 7, 8 | ✅ |
| `_M`, `_S`, `_XS` = la variante, plus ou moins légère ; aucune doc ne les définit | 4 | 50 | ⚠️ formulation de la 2e vérif |
| Règle : paramètres × bits ÷ 8, « à quelques pour cent près » ; Gemma Q6_K : 9,8 calculés contre 9,79 | 4 | 2 | ⚠️ formulation de la 2e vérif |
| UD = la recette maison d'Unsloth, chaque couche son nombre de bits | 4 | 9 | ⚠️ formulation de la 2e vérif |
| 59 % en IQ3_S, 29,5 % en IQ4_XS, 4,10 bits en moyenne ; 35,5 × 4,1 ÷ 8 = 18,2 | 4 | 47, 2 | ✅ (mesure sur le fichier) |
| 18,2 Go sur Hugging Face, environ 17 sous Windows | 4 | 46 | ⚠️ formulation de la 2e vérif |
| 4 milliards × 4,9 ÷ 8 ≈ 2,4 Go | 5 | 53 | ✅ (calcul, dit comme tel) |
| Gemma 12B : 23,8 Go en pleine précision, 7,1 en Q4_K_M, 4,2 en UD-IQ2_M (les cinq tailles à l'écran) | 5 | 14 | ✅ |
| Sur 8 Go, le Q4 laisse moins d'un giga : trop juste | 5 | 52 | ⚠️ estimation, tampon « CALCUL » |
| La mémoire de la conversation grandit avec sa longueur | 5 | 51 | ✅ (aucun chiffre dit) |
| GGUF créé par Georgi Gerganov, nombres + métadonnées ; safetensors = les nombres seuls | 6 | 5, 6 | ✅ |
| llama.cpp en C/C++, libre (MIT), serveur compatible OpenAI | 6 | 39 | ✅ |
| Ollama né sur llama.cpp, son propre moteur depuis, même base de calcul ; port 11434 (à l'écran seulement) | 6 | 40 | ⚠️ formulation de la 2e vérif |
| LM Studio s'appuie sur llama.cpp ; l'appli n'est pas open source | 6 | 41 | ✅ (nuance de la 2e vérif) |
| Qwen3.6 et Gemma 4 sous Apache 2.0 : utiliser, modifier, usage commercial | 7 | 20 | ✅ |
| Définition de l'OSI (oct. 2024) : poids, code d'entraînement, informations sur les données | 7 | 19 | ✅ |
| Qwen et Gemma 4 ne sont pas open source au sens de l'OSI | 7 | 21 | ⚠️ tranché en 2e vérif, formulation reprise |
| Meta dit « open source », l'OSI dit non | 7 | 48, 23 | ❌ corrigé (Meta ne dit pas « open weights ») ; ⚠️ formulation de la 2e vérif |
| Le même Qwen3.6-35B-A3B est proposé sur OpenRouter | 7, 8 | 26 | ✅ |
| OpenRouter : des centaines de modèles, une seule API | 8 | 26, 27 | ✅ / ⚠️ (« des centaines », pas « 500 ») |
| Prix du fournisseur sans majoration, 5,5 % à l'achat de crédits | 8 | 27 | ⚠️ formulation de la 2e vérif |
| Une vingtaine de modèles gratuits, avec une limite par jour | 8 | 29 | ⚠️ chiffre daté, à l'écran « relevé le 23/10/2026 » |
| OpenRouter ne garde pas tes textes par défaut ; c'est toi qui choisis dans tes réglages | 8 | 30, 31 | ⚠️ formulation de la 2e vérif, mot pour mot |
| LiteLLM, open source, à héberger chez toi | 8 | 33 | ⚠️ « open source », pas « tout en MIT » |
| Le harnais : « la couche autour du modèle » ; la boucle contexte → action → vérification | 9 | 34 | ✅ |
| OpenCode, Cline, Aider, Codex CLI acceptent un modèle local | 9 | 35, 36, 37, 38 | ✅ |
| Claude Code : « ça se bricole, mais Anthropic ne le prend pas en charge » | 9 | 43 | ⚠️ formulation de la 2e vérif |

Non utilisés, volontairement (durée) : 128K = 131 072 tokens, le passage de Gemma 4 à Apache 2.0 (31/03/2026), vLLM, thinking, distill, `it`, MXFP4, QAT, BYOK, les 700 millions d'utilisateurs de Llama, le cache KV chiffré (1,3 Go à 64K, calcul : la fiche demande le chiffre du journal de llama-server à la place), le Qwen3.8-27B « tient / déborde ».

## Mesure (`controle.py`, 23/10/2026)

| Mots de voix off | Durée à 145 / 165 mots/min | Mots du hook | Liaisons / 100 mots | « vous » | Crochets à remplir |
|---|---|---|---|---|---|
| 1 995 | 13 min 45 / 12 min 05 | 89 | 2,1 | 0 | 9 |

À ton débit d'ArtCraft (145), on dépasse 13 min avant tes crochets : le grill dira quoi couper (la section 1 et le paragraphe Windows sont les premiers candidats).

## Questions pour l'auteur

1. **Le crochet du hook** : si ton essai du 23-24/10 montre que le Qwen tourne, une phrase comme « et pourtant, il tourne » est le meilleur moment des 15 s. S'il ne tourne pas, on garde « je vais le lancer » et la fin renvoie à Claude #1. Lequel ?
2. **L'unité de la jauge** : ta carte a 16 Gio, soit environ 17,1 Go comme compte Hugging Face (`modeles-5080.md`, ligne 25). Le fichier, lui, fait 16,96 Gio. Il dépasse dans les deux unités, donc le hook reste vrai, mais un spectateur pointilleux peut l'écrire. On garde « 18 contre 16 » (le chiffre de la page et celui de la boîte de ta carte) ?
3. **L'écran de fin** : j'ai gardé Claude #1 (on y voit ces fichiers tourner). La 2e vérif proposait plutôt la prochaine vidéo IA du calendrier (21 déc., encore au radar). Si le radar du 16/11 choisit un sujet qui ouvre un fichier de modèle (llama.cpp avance au 8 févr.), pointer celle-ci serait plus frais. Ton choix ?
4. **L'image du foot** : le boss de Monster Hunter de Coût Claude expliquait déjà les experts. J'ai pris une équipe de foot, parce que le banc de touche sert aussi à fermer la boucle (la RAM). Tu préfères rappeler le boss pour la continuité de la série ?
5. **Le menu graphique** pour la quantification : il évite le « JPEG » des concurrents. Tu as un jeu précis dont le menu parle à ton public (sans capture, en motion design) ?
6. **La section 1** (50 s avant le premier morceau) est la plus coupable si la v2 est trop longue. On la garde pour le sous-texte, ou on le déplace dans le hook et la fin seulement ?
7. **Tes crochets vécus** : ta première fois devant un nom comme ça (section 1), ton premier harnais (section 9), ce que tu utilises (fin). Rien n'est écrit à ta place.
