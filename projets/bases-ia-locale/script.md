# IA en local : comment lire le nom d'un modèle : script final

**Titre** : *IA en local : comment lire le nom d'un modèle (35B, A3B, Q4_K_M…)* (titre 3 de la fiche, recommandé).

**Version finale du 23/10/2026** (phase 4, après le [grill](grill-v1.md)). L'ancienne version reste dans [`script-v1.md`](script-v1.md). Faits : [`sources.md`](sources.md), colonne « 2e vérif », plus les lignes 55 à 60 ajoutées au grill. Sortie : **lun. 7 déc. 2026, 18 h** (d'abord le 30 nov., puis le 2 nov. ; passée au 7 déc. le 24/10, derrière la vidéo d'installation).

## Changements depuis la V1

1. **Les unités** (faits) : le V1 opposait « dix-huit » (Go de Hugging Face, base 1 000) à « seize » (Gio de la carte, base 1 024), sans le dire. Le hook garde ses deux chiffres, mais la section 3 dit maintenant la comparaison juste : « dans la même unité, dix-sept contre seize, ça dépasse toujours ». La barre du hook est dessinée à l'échelle réelle (6 % de dépassement, pas 14 %).
2. **« Plus de la moitié du fichier est en trois bits »** (faits) : faux en octets. L'en-tête relu au grill donne 59 % des **nombres** en IQ3_S, mais 49 % des **octets**, et l'IQ3_S fait environ 3,4 bits. Devient « cinquante-neuf pour cent des nombres sont en IQ trois, autour de trois bits et demi ».
3. **Le PC de 8 Go** (faits) : « le Q4 laisse moins d'un giga » mélangeait aussi les unités (8 Gio de RAM contre 7,12 Go). Il reste environ 1,4 Gio : devient « à peine un giga et demi ».
4. **Le banc de touche** (faits + logique) : le V1 disait « les autres attendent, donc on les laisse en RAM », comme si les experts en RAM ne jouaient jamais. Faux : à chaque mot, l'entraîneur peut appeler n'importe lequel. Devient : une partie de l'effectif joue sur un terrain annexe (la RAM), et c'est le processeur qui les fait jouer. Le réglage `--n-cpu-moe` est sourcé (ligne 58).
5. **Le repli du crochet du hook** : « Et pourtant, je vais le lancer » promettait un essai que la vidéo (calculée) ne montre pas. Devient « Et pourtant, il y a un moyen de le faire tourner », que la fin tient.
6. **La section 1 coupée** (50 s sans morceau du nom) : la règle du calculé passe à 0:30, le sous-texte devient un planté-récolté (« mot de passe Wi-Fi » au hook, « tu viens de le lire d'une traite » à la fin) au lieu de l'opposition « code d'initiés / juste un code », dite deux fois.
7. **Le pont du hook** : « Aujourd'hui, pas de mesure : on apprend à lire » n'ouvrait rien. Devient « c'est écrit dans le nom. Sauf qu'un des morceaux ne dit pas toute la vérité », récolté au moment d'UD.
8. **Les licences raccrochées au nom** : « Un truc que je vois mélangé partout » arrivait en « et ensuite ». Devient « il y a une chose que le nom ne te dit pas : ce que tu as le droit d'en faire ». Le harnais s'ouvre aussi sur un « mais » (« il sait répondre, mais il ne sait rien faire »).
9. **Les tics coupés** : « Ce n'est pas une arnaque, c'est la recette », « Pas une erreur : deux façons de compter », « surprise », « Sauf que voilà le piège », « Bonne nouvelle », la rafale « la place, comment il calcule, à quel point il est bête », la morale « Retiens juste ça ».
10. **Coupés pour la durée** (1 995 → 1 890 mots) : LiteLLM, le renvoi aux « vidéos de novembre », « Aucune doc ne définit ces lettres mieux que ça », safetensors, les modèles gratuits d'OpenRouter (à mettre en description : « openrouter free models » monte), « LM Studio n'est pas open source », « le mot juste, c'est poids ouverts », le récapitulatif « bout à bout » (la carte mentale le fait à l'image), le port `11434` (celui d'Ollama, pas de llama-server).
11. **Petits faits** : « le même Qwen que mon fichier » dans le cloud devient « le même modèle » (le fournisseur ne fait pas tourner ton fichier quantifié) ; la définition de l'OSI dit « un système équivalent », pas « refaire le modèle » ; « l'autre fichier que je télécharge » devient « que j'ai choisi pour ma carte » (`modeles-5080.md`), sans dire que tu l'as lancé.

**Durée** : 1 931 mots de voix off (mesure de `controle.py`, refaite le 24/10, nuit, après le renvoi vers la vidéo d'installation), contre 1 995 au V1. À ton débit (145 mots/min) : 13 min, plus tes crochets. Timecodes calculés à 145 mots/min, à recaler sur la vraie prise.

**Texte et sous-texte** :
- **Texte** : un nom de fichier se lit morceau par morceau, et avec une règle de trois (paramètres × bits ÷ 8) tu sais s'il rentre dans ton PC avant de le télécharger.
- **Sous-texte** : ce nom a l'air d'un mot de passe ; à la fin, tu le lis d'une traite. Personne ne te l'explique, alors on le fait ensemble (0:40). Et la même règle marche sur un PC de 8 Go (section 4).

**Fil rouge** : `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf`, le fichier choisi pour ta 5080 dans `modeles-5080.md`. On le découpe de gauche à droite (sections 1 à 5), puis on suit ce qui l'entoure : moteur → API → (droits) → routeur → harnais → toi. La fin relit le nom d'une traite.

**Boucles ouvertes** :
1. « Dix-huit gigas, ma carte en a seize » (0:10) → refermée à la fin (le terrain annexe), préparée par le bus (section 2) et l'unité (section 3).
2. « Un des morceaux ne dit pas toute la vérité » (0:25) → refermée à UD (5:00).
3. « Il manque deux gigas, ils sont passés où ? » (4:40) → refermée 30 s plus tard (l'en-tête).
4. « L'une de ces pièces peut envoyer tes textes ailleurs » (relance à 58 %, 7:10) → refermée dans la section 7 (le routeur).

**Place dans la série** (ta décision du 24/10, nuit : une progression douce) : la vidéo sort le 7 déc., la deuxième marche **après** [la vidéo d'installation](../installer-ia-locale/fiche.md) (2 nov.), et après Claude #1 (16 nov., testé) et Coût Claude (23 nov., calculé). Elle renvoie à la vidéo d'installation à 0:40 (carte YouTube) ; l'écran de fin pointe Claude #1, déjà en ligne.

**Format** : vulgarisation, **calculé** (règle 1 dite à 0:30). Aucune vitesse, aucun benchmark à toi. Depuis le 25/10, plus d'essais sur la 5080 : les crochets d'essai ont été remplacés par leurs replis.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Les noms de fichier s'écrivent en code dans les visuels et se disent comme ils se lisent (« IQ quatre XS »).

**Les images de la vidéo** (aucune n'est le « JPEG » de Tech With Tim et Mark Kashef) :
- le nom = une **étiquette** qu'on découpe en morceaux ;
- les experts = une **équipe de foot** : tout l'effectif dans le bus, neuf joueurs sur le terrain à chaque mot ; à la fin, un **terrain annexe** (la RAM) ;
- la quantification = le **menu graphique** d'un jeu (Ultra, Élevé, Moyen, Bas) ;
- le moteur = l'**émulateur**, le gguf = la ROM.

---

## 0. Hook (0:00 – 0:32) · objectif : 75 % à 0:15, 70 % à 0:30

[VISUEL : écran noir. Le nom se tape lettre par lettre, en gros, police mono : `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf`. Pas de titre, pas de logo, pas de visage.]
[SON : clavier mécanique, une touche par caractère, accéléré.]

Qwen trois point six, trente-cinq B, A trois B, UD, IQ quatre XS, point gguf.

On dirait un mot de passe Wi-Fi. En fait, c'est une IA, en local. Dix-huit gigas.

[VISUEL : sous le nom, une barre « 18,2 Go » se remplit. À côté, la jauge de la RTX 5080 : « 16 Go ». La barre dépasse la jauge, clignote en rouge. **À l'échelle réelle** : 16,96 contre 16 Gio, la barre dépasse d'environ 6 %.]
[SON : buzzer bref, façon « Game Over » de borne d'arcade.]

Sauf que ma carte graphique en a seize.

Et pourtant, il y a un moyen de le faire tourner.

Donc comment tu sais si un modèle rentre dans ton PC, avant de griller dix-huit gigas de data ?

[VISUEL : le nom se fend en cinq étiquettes, chacune avec un « ? ». Le « ? » d'« IQ4_XS » clignote une fois de plus que les autres.]

En fait, c'est écrit dans le nom. Sauf qu'un des morceaux ne dit pas toute la vérité.

---

## 1. Qwen3.6 et 35B : le nombre de nombres (0:32 – 1:35)

[VISUEL : tampon vert « CALCUL » en coin d'écran, il reste toute la vidéo.]

Ici, pas de mesure : je fais des calculs, et chaque chiffre a sa source en description.

[VISUEL : capture de Hugging Face, la liste des fichiers du dépôt Unsloth de Qwen3.6, des dizaines de noms du même genre qui défilent.]

Des noms comme ça, tu en vois des listes entières sur Hugging Face. Et dans LM Studio aussi, dès que tu cherches un modèle. D'ailleurs, si t'as jamais installé d'IA chez toi, commence par ma vidéo où on le fait pas à pas, je te la mets là.

[VISUEL : carte YouTube vers *Pourquoi avoir ta propre IA, et comment l'installer*.]

Et personne ne t'explique comment ça se lit. Alors on le découpe ensemble, de gauche à droite.

[CROCHET : TA PREMIÈRE FOIS DEVANT UN NOM COMME ÇA, CE QUE TU AS PENSÉ OU FAIT, EN UNE OU DEUX PHRASES. SINON, RIEN.]

[VISUEL : la carte mentale, en gris, encore éteinte : modèle → fichier → moteur → API → routeur → harnais → toi. Elle revient à chaque chapitre, une case s'allume. La case « modèle » s'allume. Le nom revient, seuls « Qwen3.6 » et « 35B » restent en couleur.]
[SON : « clac » d'étiquette qu'on arrache.]

Premier morceau : Qwen trois point six. Facile : la famille, puis la version.

Deuxième morceau : trente-cinq B. B, c'est billion en anglais, donc milliard. Trente-cinq milliards de paramètres.

Et un paramètre, en fait, c'est juste un nombre. Un modèle, c'est un énorme tas de nombres, réglés pendant l'entraînement. Tu lui poses une question, il calcule avec ces nombres, et un mot sort. Puis un autre.

[VISUEL : un mur de nombres à virgule qui défilent ; une phrase sort mot par mot de l'autre côté.]

Et quand on ouvre l'en-tête du fichier, on en compte bien trente-cinq virgule cinq milliards. Sur ce morceau-là, le nom dit vrai.

[VISUEL : l'en-tête du GGUF en capture, le compteur « 35 505 251 456 » surligné.]

Plus il y a de nombres, plus le fichier est lourd. Retiens ça, parce que c'est la moitié de notre calcul.

---

## 2. A3B : tout l'effectif dans le bus (1:35 – 2:55)

[VISUEL : le nom, « A3B » s'allume. Un gros « ? » au-dessus, comme sur la miniature.]

Troisième morceau, et là, ça se complique : A trois B. A comme activated. Trois milliards activés.

Attends. Il en a trente-cinq, ou trois ?

En fait, les deux. C'est un modèle à experts. Imagine une équipe de foot avec un effectif énorme : chez Qwen, deux cent cinquante-six experts. Et pour chaque mot, l'entraîneur en fait jouer neuf : huit choisis pour ce mot-là, plus un qui joue tout le temps. Du coup, sur trente-cinq milliards de nombres, trois milliards travaillent à chaque mot.

[VISUEL : un terrain vu de haut, 256 petits joueurs sur le banc et les tribunes ; 9 s'allument et entrent sur le terrain, puis 9 autres au mot suivant. Compteur « 3 milliards actifs / 35 ».]
[SON : coup de sifflet à chaque changement.]

Sauf que ça réduit le calcul, et pas la place. Pour aller au match, tout l'effectif monte dans le bus, même ceux qui finiront sur le banc. Le fichier contient bien les trente-cinq milliards.

[VISUEL : le bus, plein à craquer, étiqueté « 18,2 Go ». Légende : « A3B : moins de calcul, autant de place ».]

En face, l'autre fichier que j'ai choisi pour ma carte : Gemma quatre, douze B. Pas de A, parce que c'est un modèle dense : tout le monde joue, à chaque mot.

[VISUEL : `gemma-4-12b-it-Q6_K.gguf` à côté du nom de Qwen ; sur son terrain, tous les joueurs s'allument en même temps.]

Donc un A dans un nom, ça veut dire moins de calcul, mais autant de poids. Et garde le bus en tête, il va resservir.

[VISUEL : carton discret, 3 s : « S'abonner », bouton qui pulse une fois.]

Au passage, si un nom comme ça t'a déjà fait fermer l'onglet, abonne-toi : ici, on ouvre ce qu'il y a dedans.

---

## 3. IQ4_XS : le menu graphique du modèle (2:55 – 6:00)

[VISUEL : carte mentale, la case « fichier » s'allume. Le nom : « UD » grisé, « IQ4_XS » en couleur.]

On saute UD, on y revient. Le gros morceau, c'est IQ quatre XS : la quantification. Et l'idée, tu la connais déjà.

Tu joues sur PC ? Alors tu connais le menu des graphismes : textures en Ultra, en Élevé, en Moyen. Plus tu baisses, moins ça prend de mémoire, et plus l'image bave. Eh ben la quantification, c'est ce réglage-là, pour un modèle.

[VISUEL : un menu d'options graphiques façon jeu vidéo, « Qualité des textures : Ultra ». On descend d'un cran à chaque mot : Ultra, Élevé, Moyen, Bas. À droite, une jauge « VRAM » qui baisse.]
[SON : le « bip » de menu à chaque cran.]

En pleine précision, chaque nombre prend seize bits. Quantifier, c'est l'arrondir, pour le ranger sur moins de bits.

[VISUEL : `0,817346…` → `0,817` → `0,82` → `0,8`. Sous chaque étape, le nombre de bits : 16, 8, 4, 2.]

Et le chiffre dans le nom, c'est à peu près ça : le nombre de bits. Q huit, c'est l'Ultra, le plus proche de l'original. Q quatre, c'est le Moyen. Q deux, c'est le Bas, et là, ça se voit.

En effet, sur un modèle testé par un labo indépendant, le quatre bits fait aussi bien que l'original. À deux bits, ça baisse nettement. Et à un bit, il répond presque au hasard.

[VISUEL : trois barres, « Q4 = original », « Q2 : en baisse nette », « 1 bit : presque le hasard ». Source à l'écran : Quesma, 26/08/2026, sur Qwen3.8-27B.]

Les lettres autour : le K, c'est une famille de méthodes. Le I, c'est une matrice d'importance : en gros, elle repère les nombres qui comptent le plus. Et le XS, c'est la variante : plus elle est petite, plus le fichier est léger.

[VISUEL : l'étiquette « IQ4_XS » découpée : « I » = importance, « Q4 » = environ 4 bits, « XS » = variante légère.]

Du coup, voilà la règle de calcul. Paramètres, fois bits, divisé par huit. Et tu as la taille en gigas, à quelques pour cent près.

[VISUEL : la formule en grand : `paramètres × bits ÷ 8 ≈ Go`.]

On l'essaie sur le Gemma, en Q six K, donc environ six bits et demi. Douze milliards, fois six et demi, divisé par huit : à peu près neuf virgule huit gigas. Et le fichier sur Hugging Face ? Neuf virgule soixante-dix-neuf. Pile.

[VISUEL : le calcul qui se pose, puis la capture Hugging Face « 9.79 GB » qui vient se coller à côté. Tampon « ✓ ».]
[SON : « ding » de bonne réponse.]

Maintenant, notre Qwen, en IQ quatre XS, donc environ quatre bits et demi. Trente-cinq virgule cinq, fois quatre et demi, divisé par huit : à peu près vingt gigas. Sauf que le fichier en fait dix-huit. Il manque deux gigas. Ils sont passés où ?

[VISUEL : « ≈ 20 Go » contre « 18,2 Go », un trou entre les deux barres.]
[SON : musique coupée net.]

Tu te rappelles le morceau qu'on a sauté ? UD. C'est la recette maison d'Unsloth, l'équipe qui a fabriqué ce fichier : chaque couche reçoit son propre nombre de bits. Et quand tu ouvres l'en-tête, le nom a beau dire IQ quatre, cinquante-neuf pour cent des nombres sont en IQ trois, autour de trois bits et demi.

[VISUEL : un camembert qui se remplit : « 59 % des nombres en IQ3_S », « 29,5 % en IQ4_XS », le reste en Q8_0, Q6_K et autres. Au centre : « 4,10 bits en moyenne ».]

Du coup, en moyenne, ça fait quatre virgule un bits. Et trente-cinq virgule cinq, fois quatre virgule un, divisé par huit… dix-huit virgule deux. Au chiffre près.

[VISUEL : le calcul qui tombe sur « 18,2 Go », le trou se referme. Le « ? » d'« IQ4_XS » tombe.]

Voilà le morceau qui ne disait pas toute la vérité. Et c'est voulu : certaines couches gardent huit bits, d'autres descendent à trois et demi. Donc la règle tient, et le nom arrondit.

Et avant que tu me l'écrives : Windows affichera environ dix-sept gigas. En fait, Hugging Face compte par mille, Windows et ta carte graphique par mille vingt-quatre. Du coup, dans la même unité, c'est dix-sept contre seize. Ça dépasse toujours.

[VISUEL : « 18,2 Go » (Hugging Face) et « 16,9 Go » (Windows) côte à côte, une flèche « mêmes octets ». Puis « 16,9 » contre la jauge « 16 », toujours en rouge.]

---

## 4. Et sur un PC de huit gigas ? (6:00 – 7:05)

[VISUEL : la jauge passe de « 16 Go » à « 8 Go de RAM, pas de carte graphique ».]

Et si tu n'as pas de carte à seize gigas ? En fait, la règle marche sur n'importe quelle machine.

Un petit modèle de quatre milliards, en Q quatre, environ quatre virgule neuf bits : à peu près deux virgule quatre gigas. Donc sur le papier, il rentre dans huit gigas de RAM, même sans carte graphique. Sur le papier : c'est un calcul.

[VISUEL : le calcul, avec un tampon « CALCUL » (pas « TESTÉ »).]

Et le Gemma, lui, va de vingt-trois virgule huit gigas en pleine précision à quatre virgule deux en IQ deux.

[VISUEL : la balance. À gauche, les cinq fichiers de Gemma 12B qui rétrécissent (23,8 → 12,7 → 9,79 → 7,12 → 4,21 Go). À droite, un plateau « 8 Go ». On les pose un par un.]

Sur huit gigas, le Q quatre, à sept virgule un, te laisse à peine un giga et demi pour Windows et ta conversation, qui grandit avec sa longueur. C'est trop juste. L'IQ deux, lui, rentre. Sauf qu'à deux bits, on l'a vu, la qualité baisse nettement.

Bref, tout ça, tu le sais avant de télécharger. Et quand tu paies ta data au giga, c'est dix-huit gigas que tu ne grilles pas pour rien.

---

## 5. .gguf : la ROM et l'émulateur (7:05 – 8:15) · relance à 56 %

[VISUEL : le nom, « .gguf » s'allume en dernier.]

Dernier morceau : point gguf, le format. Il a été créé par Georgi Gerganov, l'auteur de llama.cpp, et il range dans un seul fichier les nombres et leur fiche d'identité.

[SON : coupure de la musique, silence d'une seconde.]
[VISUEL : un double-clic sur le fichier. Rien. Le curseur tourne, puis s'arrête.]

Voilà, tu sais lire le nom. Sauf que si tu double-cliques sur ce fichier, il ne se passe rien. Dix-huit gigas de nombres, et pas de bouton Play. Entre lui et toi, il manque encore des pièces. Et l'une d'elles peut envoyer tes textes chez quelqu'un d'autre.

[VISUEL : carte mentale, la case « moteur » s'allume.]

La première, c'est le moteur. Tu as déjà joué à un vieux jeu sur émulateur ? Tu vois, la ROM toute seule ne fait rien. Ici, c'est pareil : le gguf, c'est la ROM, et le moteur, c'est l'émulateur. Il charge les nombres et il fait les calculs.

[VISUEL : une cartouche « .gguf » qui glisse dans une console étiquetée « moteur ».]

Le plus connu, c'est llama.cpp, un logiciel libre. Et Ollama et LM Studio, que tu as sûrement déjà vus passer, reposent sur lui ou sur sa base de calcul.

[VISUEL : les trois noms en cartes, avec une étiquette chacun : « libre », « libre », « appli fermée ». Pas de logo.]

Et le moteur ouvre une porte : une API. En gros, une adresse sur ton PC, où les autres programmes envoient leurs questions.

[VISUEL : carte mentale, la case « API » s'allume : `http://localhost:…`, sans numéro de port.]

---

## 6. Ce que le nom ne dit pas : tes droits (8:15 – 9:45)

[VISUEL : le nom découpé revient ; une sixième étiquette vide apparaît au bout, « droits ? ».]

Sauf qu'il y a une chose que le nom ne te dit pas : ce que tu as le droit d'en faire. Et là, trois mots se mélangent partout : local, open, open source.

[VISUEL : trois portes côte à côte : « Local », « Poids ouverts », « Open source (OSI) ».]
[SON : grincement de porte.]

Local, ça veut dire qu'il tourne chez toi, et que rien ne sort.

Poids ouverts, ça veut dire que les nombres sont publics : tout le monde peut les télécharger. Qwen trois point six et Gemma quatre sont dans ce cas, sous licence Apache deux point zéro. Du coup, tu peux les utiliser, les modifier, et même t'en servir pour un business.

Open source, c'est plus exigeant. L'OSI, qui tient la définition de l'open source, a publié fin deux mille vingt-quatre sa version pour l'IA. Elle demande les poids, le code d'entraînement, et assez d'infos sur les données pour qu'un spécialiste construise un modèle équivalent.

[VISUEL : trois cases à cocher : « poids », « code d'entraînement », « infos sur les données ». Qwen et Gemma cochent la première seulement.]

Sauf que Qwen et Gemma ne publient ni leurs données, ni ce code. Donc, avec cette définition, ça ne passe pas : ce sont des poids ouverts, sous une licence que l'OSI approuve.

Et Llama ? Meta dit open source, et l'OSI répond que sa licence n'en est pas une.

[VISUEL : bulle « open source » sortant d'un nom « Meta » (texte seul), barrée par un tampon « OSI : non ».]

Dernier piège : le même modèle, Qwen trois point six, trente-cinq B, A trois B, tu peux aussi l'utiliser dans le cloud, sans rien télécharger. Ouvert ne veut pas dire local.

[VISUEL : l'icône du Qwen passe la porte « Poids ouverts », puis s'envole vers un nuage.]

---

## 7. Le routeur : la porte d'à côté (9:45 – 10:45)

[VISUEL : carte mentale, la case « routeur » s'allume, en pointillés (elle est optionnelle).]

Dans le cloud, mais où ? Par exemple chez OpenRouter. Ça, c'est un routeur : une seule API pour des centaines de modèles. Ta question passe par lui, puis par un fournisseur qui fait tourner le modèle sur ses machines.

[VISUEL : capture d'openrouter.ai, la liste des modèles, recherche « qwen3.6-35b-a3b ». Aucune connexion à un compte, aucune clé à l'écran.]
[VISUEL : schéma : toi → routeur → fournisseur → réponse. Une clé dessinée, floutée, dans la main du « toi ».]

Pour un modèle qui ne rentre pas dans ton PC, c'est la porte d'à côté. Tu paies le prix du fournisseur, sans majoration, et OpenRouter prend cinq virgule cinq pour cent quand tu achètes des crédits.

[VISUEL : la page « Pricing » d'openrouter.ai, « 5.5% » surligné. Bandeau : « relevé le 23/10/2026 ».]

Sauf que là, ton texte sort de chez toi. Forcément : il faut bien que quelqu'un d'autre fasse le calcul. OpenRouter dit qu'il ne garde pas tes textes, sauf si tu l'acceptes. Mais le fournisseur, c'est une autre boîte. Du coup, c'est dans tes réglages que tu choisis si tes demandes peuvent aller chez un fournisseur qui s'en sert pour s'entraîner. Voilà la pièce qui peut envoyer tes textes ailleurs.

[VISUEL : le point de la requête quitte la maison, traverse le routeur, arrive chez le fournisseur ; un interrupteur « entraînement : oui / non » s'affiche sur le trajet. Dessiné, pas filmé.]

---

## 8. Le harnais : des mains pour le modèle (10:45 – 11:45)

[VISUEL : carte mentale, la case « harnais » s'allume.]

Chez toi ou dans le cloud, ton modèle sait répondre. Mais il ne sait rien faire. Tu lui demandes de corriger un bug, il t'écrit la correction, et c'est toi qui fais le copier-coller.

Le harnais, c'est ce qui lui donne des mains. Avec lui, le modèle peut ouvrir tes fichiers, les modifier lui-même, lancer des commandes. Anthropic le dit comme ça pour Claude Code : c'est la couche autour du modèle, qui lui donne ses outils et qui gère ce qu'il voit.

[VISUEL : la citation d'Anthropic en anglais, traduite en sous-titre. Puis une boucle qui tourne : « chercher le contexte → agir → vérifier ».]

Et il tourne en boucle : il cherche le contexte, il agit, il vérifie, puis il recommence. Du coup, quand tu entends « agent IA », c'est souvent de ça qu'on parle. Le moteur le fait tourner ; le harnais, lui, le fait agir.

[VISUEL : deux cartes : « moteur = il tourne », « harnais = il agit ».]

Et plusieurs harnais acceptent un modèle local : OpenCode, Cline, Aider, et même Codex CLI, d'OpenAI. Claude Code, lui, ça se bricole, mais Anthropic ne le prend pas en charge.

[VISUEL : les cinq noms, une coche « modèle local » pour les quatre premiers, « non pris en charge » pour Claude Code. Dossier vide en arrière-plan, aucun projet Flutter.]

[CROCHET : TON PREMIER HARNAIS, ET CE QUE ÇA T'A FAIT LA PREMIÈRE FOIS QU'IL A MODIFIÉ UN FICHIER TOUT SEUL. UNE OU DEUX PHRASES. SINON, RIEN.]

---

## 9. Fin : relis le nom avec moi (11:45 – 13:00)

[VISUEL : la carte mentale en entier, un point lumineux la traverse d'un bout à l'autre.]
[SON : la musique du hook revient.]

Donc maintenant, relis le nom avec moi. Qwen trois point six : la famille. Trente-cinq B : la place. A trois B : le calcul. UD IQ quatre XS : le réglage, autour de quatre bits. Point gguf : pour le moteur.

[VISUEL : le nom du hook se reforme, chaque étiquette garde sa traduction en dessous. Plus aucun « ? ».]

Tout à l'heure, ça ressemblait à un mot de passe Wi-Fi. Là, tu viens de le lire d'une traite.

Il reste ma question du début : dix-huit gigas, sur une carte de seize. Tu te rappelles le bus ? Tout l'effectif doit venir au match, mais pas forcément sur le même terrain. Du coup, le plan, c'est de mettre une partie des experts sur un terrain annexe : la RAM du PC. Quand l'entraîneur appelle un joueur qui est là-bas, c'est le processeur qui le fait jouer. Et llama.cpp a une option exprès pour ça.

[VISUEL : le terrain revient : la carte graphique = le terrain principal, la RAM = un terrain annexe à côté. Une partie de l'effectif y passe ; quand un joueur de l'annexe est appelé, il s'allume sur place, avec une étiquette « processeur ». La barre « 18,2 Go » repasse sous la jauge « 16 Go ». Légende : « plan, d'après mon calcul ».]

Ce que ça donne, d'après ceux qui l'ont mesuré, c'est dans ma vidéo sur les seize gigas. Je te la mets là.

Et la prochaine fois que tu tombes sur un nom comme ça, tu fais le calcul avant de télécharger.

[CROCHET : CE QUE TU UTILISES, TOI : UN MODÈLE, UN MOTEUR, UN HARNAIS. UNE PHRASE.]

Écris en commentaire un nom de fichier à décoder, avec la mémoire de ton PC. Et si tu veux savoir ce que ces fichiers donnent pour de vrai, j'ai rassemblé les mesures de ceux qui ont une carte comme la mienne : la vidéo est juste là.

[VISUEL : écran de fin, 20 s : « 16 Go de VRAM suffisent-ils pour remplacer Claude ? » à gauche (en ligne depuis le 16/11), bouton « S'abonner » à droite.]

---

## Relances d'attention

Timecodes à 145 mots/min, sans tes crochets.

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel + son | Le nom tapé lettre par lettre, au clavier mécanique |
| 0:14 | Chiffre + son | 18,2 Go contre 16 Go, buzzer d'arcade |
| 0:17 | Question centrale | « Comment tu sais si ça rentre, avant de griller 18 gigas de data ? » |
| 0:26 | Boucle ouverte | « Un des morceaux ne dit pas toute la vérité » |
| 1:22 | Récolte partielle | « Sur ce morceau-là, le nom dit vrai » |
| 1:41 | Question | « Il en a trente-cinq, ou trois ? » |
| 1:47 | Image | L'équipe de foot, neuf joueurs sur le terrain |
| 2:07 | Retournement | « Tout l'effectif monte dans le bus » |
| 2:44 | Appel à l'action | Abonnement (21 %) |
| 3:02 | Lien au vécu | Le menu des graphismes, Ultra → Bas |
| 3:42 | Chiffre | 4 bits = l'original, 2 bits en baisse, 1 bit = le hasard |
| 4:23 | Son + preuve | La règle tombe pile sur Gemma, « ding » |
| 4:54 | Boucle ouverte + coupure | « Il manque deux gigas, ils sont passés où ? » |
| 4:58 | Récolte | UD, le camembert : 59 % des nombres en IQ3 ; le « ? » tombe |
| 5:43 | Anticipation | « Avant que tu me l'écrives » : 17 contre 16, ça dépasse toujours |
| 6:00 | Changement d'enjeu | Le PC de 8 Go |
| 6:25 | Visuel | La balance des cinq Gemma |
| 6:52 | Récolte | « Dix-huit gigas que tu ne grilles pas pour rien » |
| 7:16 | Coupure + relance (56 %) | Le double-clic qui ne fait rien ; « l'une d'elles peut envoyer tes textes » |
| 7:37 | Image gamer | La ROM et l'émulateur |
| 8:16 | Retournement | « Le nom ne dit pas ce que tu as le droit d'en faire » |
| 9:25 | Retournement | Meta dit open source, l'OSI dit non |
| 9:32 | Pont | Le même modèle dans le cloud → le routeur |
| 10:40 | Boucle refermée | « Voilà la pièce qui peut envoyer tes textes ailleurs » |
| 10:43 | Retournement | « Ton modèle sait répondre. Mais il ne sait rien faire » |
| 12:01 | Récolte | Le nom relu d'une traite ; « un mot de passe Wi-Fi » |
| 12:09 | Boucle refermée | Le bus → le terrain annexe = la RAM |

**Total** : 27 relances en 13 min, environ une toutes les 29 secondes. Le seul trou de plus d'une minute est entre 10:43 et 12:01 (le harnais) : ton crochet du premier harnais tombe au milieu.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:12-0:18 | Moyen | Le crochet de l'essai reste vide tant que tu n'as pas lancé le fichier | Repli écrit (« il y a un moyen »), que la fin tient ; la barre qui dépasse porte l'enjeu à l'image |
| 0:30-0:45 | Moyen | La règle du calculé, puis Hugging Face, avant le premier morceau | 15 s seulement ; le tampon « CALCUL » à l'image, la liste qui défile |
| Les lettres K, I, XS | Élevé | Trois sigles en 20 s, la zone « glossaire » | Étiquette découpée à l'écran ; la règle de calcul arrive juste après |
| La règle sur Gemma et Qwen | Moyen | Des nombres à virgule dits à voix haute | Le calcul s'écrit à l'écran pendant qu'il se dit ; le « ding », puis le trou |
| Les unités (5:30) | Moyen | Paragraphe technique juste après le meilleur moment | 40 mots, une image (deux barres, mêmes octets) ; il referme la boucle du hook honnêtement |
| Relance (~58 %) | Élevé | Le nom est fini : risque de « j'ai eu ma réponse » | Coupure, double-clic qui ne fait rien, nouvelle menace (« tes textes ailleurs »), boucle du bus encore ouverte |
| Licences | Moyen | Sujet juridique, peu visuel | La sixième étiquette « droits ? » qui raccroche au nom ; trois portes, trois cases, le tampon « OSI : non » |
| Harnais | Moyen | Fin de vidéo, beaucoup de noms | Le copier-coller en image, cinq noms en une phrase ; ton crochet juste après |

## Notes de montage

- **Composants à construire une fois** : le nom découpé en étiquettes (plus la sixième, « droits ? »), la carte mentale (7 cases), le terrain de foot (256 experts, 9 actifs, puis le terrain annexe = RAM), le menu graphique, la balance 8/16 Go. La carte mentale et le nom découpé resservent pour llama.cpp (8 févr.) et Louer ou acheter.
- **Barres à l'échelle** : la barre du hook (16,96 contre 16 Gio, +6 %) et celle du PC de 8 Go (6,63 contre 8 Gio) sont dessinées dans la même unité. Un spectateur qui mesure l'écran doit retrouver les vrais rapports.
- **Charte verte « IA chez moi »**, police mono pour tous les noms de fichier.
- **Interdits à l'écran** : aucune clé d'API collée, aucune connexion d'OpenRouter à un harnais, aucun nom ni dépôt « abliterated » ou « uncensored », aucun projet Flutter en arrière-plan (dossier vide), aucun logo de moteur ou d'entreprise en gros.
- **Captures autorisées** : Hugging Face (dépôts Unsloth et Google), en-tête du GGUF, openrouter.ai (liste des modèles, page Pricing, sans compte connecté), doc d'Anthropic (citation du harnais).
- **Tampons** : « CALCUL » sur tout chiffre calculé (2,4 Go, la balance, le plan du terrain annexe), « TESTÉ » seulement sur ce que tu as vraiment lancé.
- **Énergie** : calme, montée toutes les 2 à 3 min : 18 contre 16 (0:10), le bus (2:15), le trou puis le camembert (4:40-5:00), le double-clic (7:10), le terrain annexe (11:55).
- **Miniature** : celle de la fiche (le nom découpé, « ? » sous « A3B »). Le hook reprend son image dès la première seconde.

## Faits utilisés

| Ce que dit le script | Section | Ligne de `sources.md` | Statut |
|---|---|---|---|
| Le fichier `Qwen3.6-35B-A3B-UD-IQ4_XS.gguf` pèse 18,2 Go (Hugging Face) | 0, 3, 5, 9 | 13 | ✅ |
| La RTX 5080 a 16 Go (16 Gio) de mémoire | 0, 3, 9 | 55 | ✅ (ajouté au grill) |
| Dans la même unité : 17 (16,96 Gio) contre 16, ça dépasse ; Windows affiche environ 17 | 3 | 46, 55 | ✅ (calcul) |
| Il y a un moyen de le faire tourner : une partie des experts en RAM, calculés par le processeur (`--n-cpu-moe`) | 0, 9 | 58 ; 45 | ✅ (option documentée) ; le résultat reste en crochet |
| 35,5 milliards de nombres dans l'en-tête | 1 | 12, 56 | ✅ (relu au grill : 35 505 251 456) |
| 35 milliards au total, 3 milliards activés, 256 experts, 8 + 1 par mot | 2 | 12, 56 | ✅ |
| A3B réduit le calcul, pas la place | 2 | 44 | ✅ |
| Gemma 4 12B est dense, choisi pour ta carte | 2 | 14 ; `modeles-5080.md` | ✅ |
| Quantifier = réduire la précision ; 16 bits en pleine précision | 3 | 4, 1 | ✅ |
| Le chiffre ≈ les bits ; Q6_K ≈ 6,5 ; IQ4_XS ≈ 4,5 ; Q4_K_M ≈ 4,9 (dits « environ ») | 3, 4 | 1, 50 | ⚠️ formulation de la 2e vérif (« environ ») |
| « Sur un modèle testé par un labo indépendant, le 4 bits fait aussi bien que l'original ; à 2 bits, baisse nette ; à 1 bit, presque le hasard » | 3 | 3 | ⚠️ formulation de la 2e vérif, mot pour mot |
| K = une famille de méthodes ; I = matrice d'importance | 3 | 7, 8, 4 | ✅ |
| XS = la variante, plus ou moins légère | 3 | 50 | ⚠️ formulation de la 2e vérif |
| Règle : paramètres × bits ÷ 8, « à quelques pour cent près » ; Gemma Q6_K ≈ 9,8 contre 9,79 | 3 | 2 | ⚠️ formulation de la 2e vérif |
| Qwen à 4,5 bits ≈ 20 Go (35,5 × 4,5 ÷ 8 = 19,97) | 3 | 2 | ✅ (calcul) |
| UD = la recette maison d'Unsloth, chaque couche son nombre de bits | 3 | 9 | ⚠️ formulation de la 2e vérif |
| 59 % des **nombres** en IQ3_S (≈ 3,4 bits), 29,5 % en IQ4_XS, des couches en Q8_0 ; 4,10 bits en moyenne ; 35,5 × 4,1 ÷ 8 = 18,2 | 3 | 47, 56, 8 | ✅ (en-tête relu au grill) ; « plus de la moitié du fichier » retiré |
| Hugging Face compte par 1 000, Windows par 1 024 | 3 | 46 | ✅ |
| 4 milliards × 4,9 ÷ 8 ≈ 2,4 Go | 4 | 53 | ✅ (calcul, dit comme tel) |
| Gemma 12B : 23,8 Go en pleine précision → 4,2 en UD-IQ2_M (les cinq tailles à l'écran) | 4 | 14 | ✅ |
| Sur 8 Go, le Q4 (7,12 Go) laisse à peine 1,5 Go : trop juste | 4 | 52, 57 | ⚠️ estimation, corrigée au grill (« moins d'un giga » était faux) |
| La mémoire de la conversation grandit avec sa longueur | 4 | 51 | ✅ (aucun chiffre dit) |
| GGUF créé par Georgi Gerganov, nombres + métadonnées dans un seul fichier | 5 | 5 | ✅ |
| llama.cpp, logiciel libre (MIT) | 5 | 39 | ✅ |
| Ollama et LM Studio « reposent sur llama.cpp ou sur sa base de calcul » (Ollama a son propre moteur sur GGML depuis mai 2025) | 5 | 40, 41 | ⚠️ formulation qui couvre les deux cas de la 2e vérif |
| Le moteur ouvre une API (serveur compatible OpenAI, adresse locale) | 5 | 39, 40, 41 | ✅ |
| Qwen3.6 et Gemma 4 sous Apache 2.0 : utiliser, modifier, usage commercial | 6 | 20 | ✅ |
| Apache 2.0 est une licence approuvée par l'OSI | 6 | 60 | ✅ (ajouté au grill) |
| Définition de l'OSI (fin 2024) : poids, code d'entraînement, infos sur les données pour un système équivalent | 6 | 19 | ✅ |
| Qwen et Gemma ne publient ni données ni code d'entraînement : ça ne passe pas la définition | 6 | 21 | ⚠️ tranché en 2e vérif ; dit comme notre lecture de la définition (l'OSI n'a pas d'avis nommé) |
| Meta dit open source, l'OSI dit non | 6 | 48, 23 | ⚠️ formulation de la 2e vérif |
| Le même Qwen3.6-35B-A3B est proposé dans le cloud (OpenRouter) | 6, 7 | 26 | ✅ |
| OpenRouter : une seule API, des centaines de modèles | 7 | 26, 27 | ⚠️ « des centaines », pas « 500 » |
| Prix du fournisseur sans majoration, 5,5 % à l'achat de crédits | 7 | 27 | ⚠️ formulation de la 2e vérif |
| OpenRouter ne garde pas tes textes, sauf si tu l'acceptes | 7 | 30, 59 | ✅ (FAQ relue au grill : « zero logging […] unless you opt-in ») |
| C'est dans tes réglages que tu choisis si un fournisseur qui entraîne peut recevoir tes textes | 7 | 31, 59 | ⚠️ formulation de la 2e vérif ; la position par défaut reste ❓ (pas dite) |
| Le harnais : « la couche autour du modèle » ; ouvrir, modifier, lancer des commandes ; la boucle contexte → action → vérification | 8 | 34, 36 | ✅ |
| OpenCode, Cline, Aider, Codex CLI acceptent un modèle local | 8 | 35, 36, 37, 38 | ✅ |
| Claude Code : « ça se bricole, mais Anthropic ne le prend pas en charge » | 8 | 43 | ⚠️ formulation de la 2e vérif |

Non utilisés, volontairement (durée) : safetensors, les modèles gratuits d'OpenRouter, 128K = 131 072 tokens, la date de Gemma 4, vLLM, thinking, distill, `it`, MXFP4, QAT, BYOK, LiteLLM, Llama 3.1 et ses 700 millions, le cache KV chiffré, le Qwen3.8-27B « tient / déborde », le port d'Ollama.

## Mesure (`controle.py`, 23/10/2026, refaite le 24/10)

| Mots de voix off | Durée à 145 / 165 mots/min | Mots du hook | Liaisons / 100 mots | « vous » | Crochets à remplir |
|---|---|---|---|---|---|
| 1 895 | 13 min 04 / 11 min 29 | 74 | 2,7 | 0 | 6 vrais crochets (`controle.py` en compte 11 : il lit aussi les liens et la ligne des conventions) |

« Dix-huit gigas » tombe au 31e mot (≈ 0:13 à 145 mots/min), « seize » au 39e (≈ 0:16 ; 0:13 à 180), la question centrale finit au 57e (≈ 0:24), le pont au 74e (≈ 0:31, plus le crochet). Par section, les liaisons vont de 1,7 (section 5) à 5,0 (hook) pour 100 mots.

## Questions pour l'auteur

1. ~~**Le crochet du hook**~~ : **réglé le 25/10**, plus d'essais. Le repli « Et pourtant, il y a un moyen de le faire tourner » est écrit dans le script, comme celui de la fin.
2. **« Dix-huit contre seize »** : je l'ai gardé dans le hook (le chiffre de la page qu'on télécharge, et celui de la boîte), et la section 3 rétablit « dix-sept contre seize dans la même unité ». L'autre option : dire « dix-sept » dès le hook (ce que tu verras dans Windows), mais le « dix-huit virgule deux, au chiffre près » de la règle perd son écho. Lequel ?
3. **L'écran de fin** : **réglé le 24/10** (la vidéo sort le 7 déc., après Claude #1). Il pointe Claude #1, déjà en ligne. La dernière phrase dit « la vidéo qui vient juste après celle-ci » : elle reste vraie avant comme après le 16.
4. **Le foot** : la fin dépend maintenant du bus et du terrain annexe. Si tu préfères rappeler le boss de Monster Hunter de Coût Claude pour la continuité, il faut refaire la fin avec lui.
5. **Le menu graphique** : un jeu précis dont le menu parle à ton public (en motion design, sans capture) ?
6. **Les réglages d'OpenRouter** : sur un compte neuf, l'interrupteur « entraînement » est-il ouvert ou fermé au départ ? Aucune page ne le dit. Si tu le regardes sur un compte jetable (sans créer de clé), on peut dire « par défaut, il est… » au lieu de « regarde ce réglage ».
7. **Tes crochets vécus** : ta première fois devant un nom comme ça (section 1), ton premier harnais (section 8), ce que tu utilises (fin). Rien n'est écrit à ta place ; s'ils restent vides, la phrase d'avant tient seule.
