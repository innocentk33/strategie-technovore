# llama.cpp : script v2 (version finale)

**Titre** : *Le dev qui a mis un ChatGPT dans ton PC*

**Durée** : environ 2 137 mots de voix off (contrôle du 23/10/2026). À 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises) : environ 14 min 44 ; à 165 mots/min : 12 min 57. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Changements depuis la V1** (le détail et les citations sont dans [`grill-v1.md`](grill-v1.md)) :
- **Hook** : l'IA arrive dans la deuxième phrase (« un petit programme qui fait tourner une IA sur un MacBook ») et « ton PC » dans la quatrième, au lieu de 0:20 ; Sofia passe dans le récit ; le contraste (132 000 étoiles) tombe vers 0:12 ; Ollama et LM Studio deviennent une promesse à récolter (« dessous, il y avait son travail »).
- **Faits corrigés** : « ceux qui ont fabriqué la puce de ma 5080 » devient « la marque de ma 5080 » ; « le plus gros vendeur de cartes graphiques » et « les deux outils les plus utilisés » sont retirés (aucune mesure) ; Call of Duty remplacé par un calcul (le quart des 16 Go de ta carte) ; « l'équipe y consacre 100 % de son temps » dit maintenant à quoi (ggml et llama.cpp) ; la PR #613 est écrite par Justine Tunney **avec slaren** ; le prix de Nvidia reste celui du billet, et la clôture attendue vient du formulaire 8-K de Nvidia.
- **Faits ajoutés, vérifiés à la source** (lignes 29 à 37 de `sources.md`) : les 16 bits du modèle de départ, mmap, la licence MIT et ce qu'elle permet, whisper.cpp (la reconnaissance vocale d'OpenAI), Nat Friedman ancien patron de GitHub, le moteur d'Ollama de mai 2025 qui remercie ggml, les 2 000 contributeurs et les 24 000 copies, « seul le 7B marche » dans le premier README.
- **Récoltes** : le hook « dessous, il y avait son travail » est récolté en section 7 ; ggml (section 3) revient sous le moteur d'Ollama de 2025 ; whisper.cpp prépare le titre (il avait déjà fait le coup avec une IA d'OpenAI).
- **Fin réécrite** : elle répond au README (« aucune idée si ça marche ») et retourne le sous-texte : l'IA chez toi tenait à un seul dev, elle tient aujourd'hui à plus de 2 000 contributeurs et à une licence qui laisse n'importe qui reprendre le code. Ton test sur la 5080 passe en conditionnel, comme dans la section 4.
- **Engagement** : une devinette avant le chiffre des 4 bits.
- **Tics** : « Ensuite, il y a la meilleure phrase », « un dev, un commit, et un patch », « Et je trouve ça encore plus fort » (avis prêté), « Voilà pourquoi je voulais te raconter », « Et maintenant, le moment où… » retirés ; « en gros » passe de 7 à 4.
- **Liaisons** : les sections 7 et 8 (1,4 et 1,2 pour 100 mots dans la V1) remontent à 2,1 et 1,8, la fin à 1,9 ; 2,8 liaisons pour 100 mots sur tout le script.

**Texte et sous-texte** (repris de la fiche) :
- **Texte** : l'histoire de llama.cpp. Un développeur publie le 10 mars 2023 un petit programme pour faire tourner LLaMA, le modèle de Meta, sur un MacBook ; il devient le moteur de LM Studio et la base sur laquelle Ollama a été construit.
- **Sous-texte** : une IA qui tourne chez toi et non chez eux, ça tient à un projet commencé en une soirée (sur six mois de travail). Ce que tu appelles « IA chez moi » a une histoire et un auteur, et son avenir se joue en ce moment. Proposition du grill (à valider, question 3) : la fin répond que ça ne tient plus à un seul homme.

**Fil rouge** : le README du 10 mars 2023 (« hacked in an evening – I have no idea if it works correctly »). Il ouvre la vidéo, on le relit dans la section 2, et la fin lui répond : ça marche, et ça ne tient plus à lui seul.

**Boucles ouvertes** :
1. « Comment un truc bricolé en une soirée a fini dans des PC comme le tien ? » (hook, refermée dans la section 7).
2. « Il faut commencer par une fuite. Sur 4chan. » (hook, refermée dans la section 1).
3. « Le plus petit pèse treize gigas » (section 1, refermée dans la section 4).
4. « La phrase "bricolé en une soirée" raconte pas toute l'histoire » (section 2, refermée dans la section 3).
5. « La deuxième annonce pèse presque treize milliards de dollars » (section 7, refermée dans la section 8).
6. « I have no idea if it works correctly » (hook, refermée dans la section 9).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi ; une ligne qui commence par `[SI …]` ne se lit que si la condition est vraie. Nombres en lettres pour la lecture. « llama.cpp » se dit « lama point C P P » ; « GGUF » et « ggml » se disent en lettres.

---

## 0. Hook (0:00 – 0:39)

[VISUEL : écran noir. Le README d'origine s'écrit lettre par lettre, police mono : « This was hacked in an evening - I have no idea if it works correctly. » La traduction s'affiche dessous. Pas de titre, pas de logo.]
[SON : un clavier, rien d'autre.]

« Bricolé en une soirée. Aucune idée si ça marche correctement. » Un dev écrit ça en mars deux mille vingt-trois, sous un petit programme qui fait tourner une IA sur un MacBook.

[VISUEL : le compteur d'étoiles GitHub s'emballe jusqu'à 132 000. En petit : « 23/10/2026 ». Puis les logos d'Ollama et de LM Studio, et sous chacun, en transparence, le même bloc de code.]
[SON : un « tic » qui accélère avec le compteur.]

Et pourtant, aujourd'hui, ce programme a plus de cent trente-deux mille étoiles sur GitHub. Et si t'as déjà lancé une IA sur ton PC avec Ollama ou LM Studio, dessous, il y avait son travail.

[VISUEL : un PC de joueur dans le noir ; la tour s'allume en vert.]

Du coup, comment un truc bricolé en une soirée a fini dans des PC comme le tien ?

Pour le comprendre, il faut commencer par une fuite. Sur 4chan.

[VISUEL : un fichier torrent qui clignote, puis coupe au noir.]

---

## 1. La fuite (0:39 – 2:23)

[VISUEL : chronologie en bas de l'écran. Un seul point allumé : « 24/02/2023 ».]

Début deux mille vingt-trois, pour parler à une IA, en général, tu passes par un site, et ton message part sur les serveurs de quelqu'un d'autre. Et le vingt-quatre février, Meta annonce LLaMA, son grand modèle de langage, en quatre tailles : de sept à soixante-cinq milliards de paramètres.

Sauf que tu peux pas le télécharger comme ça. Il faut faire une demande, et la licence est réservée à la recherche, sans usage commercial. Bref, c'est un club fermé, et toi, t'es pas sur la liste.

[VISUEL : un videur devant une porte marquée « LLaMA – chercheurs uniquement ».]

Mais début mars, les poids du modèle fuitent sur 4chan. Les poids, en fait, c'est le modèle lui-même : des milliards de nombres rangés dans des fichiers. Quelqu'un poste un torrent, Meta envoie des demandes de retrait, mais un torrent qui tourne, ça se rattrape pas. C'est comme un jeu qui leak avant sa sortie : le studio peut râler, les fichiers circulent déjà.

[VISUEL : le titre de la vidéo s'affiche, « un ChatGPT » est barré et remplacé par « LLaMA ».]

Petite précision, parce que mon titre triche un peu. llama.cpp n'a jamais fait tourner ChatGPT. Il fait tourner LLaMA, le modèle de Meta. Si je dis « un ChatGPT », c'est pour l'idée : une IA à qui tu écris et qui te répond. Sauf que là, elle va tourner chez toi.

Bon, le modèle est dans la nature. Le souci, c'est qu'il est lourd : rien que le plus petit, celui de sept milliards de paramètres, pèse treize gigas. Tu vois le problème ? Treize gigas à faire tenir dans la mémoire d'un ordi normal.

[VISUEL : un fichier de 13 Go qui essaie d'entrer dans un MacBook, et qui coince.]

Et le dix mars, un dev de Sofia, en Bulgarie, pousse un commit.

---

## 2. Le soir du dix mars (2:23 – 4:15)

[VISUEL : capture de l'historique GitHub, le commit 26c08466 « Initial release », zoom sur l'heure.]
[SON : notification GitHub.]

Le dix mars deux mille vingt-trois, à dix-huit heures quarante, heure de Londres, Georgi Gerganov publie un commit qui s'appelle « Initial release ». Le projet s'appelle llama.cpp, et franchement, le README est d'une honnêteté rare.

En gros, il dit : voilà LLaMA, le modèle de Facebook, en C et C++ pur, sans dépendances. Ça tourne sur le processeur, et les puces Apple sont prioritaires. Et son objectif est écrit noir sur blanc : faire tourner le modèle sur un MacBook, en quatre bits. Retiens ce « quatre bits », parce qu'on y revient dans deux minutes.

[VISUEL : les puces du README s'affichent une par une ; « 4-bit » reste surligné.]

Un peu plus bas, il y a la phrase du début : « This was hacked in an evening. I have no idea if it works correctly. » Il prévient aussi que pour l'instant, seul le plus petit modèle marche, parce qu'il a pas encore trouvé comment assembler les plus gros. Et que le texte généré démarre bien, mais qu'en général il se dégrade après trente ou quarante jetons. Un jeton, pour faire simple, c'est un bout de mot. Donc ton IA tient deux phrases, et après, elle parle comme un PNJ buggé.

[VISUEL : une réponse qui démarre propre, puis les lettres glitchent et partent en bouillie.]
[SON : un bug sonore de vieille console.]

Et trois heures après le premier commit, il corrige déjà un bug dans un calcul. Du coup, le README gagne une ligne : si tu vois des résultats poubelle, mets-toi à jour. Voilà comment démarre le projet : avec un patch avant minuit, le soir même.

D'ailleurs, si t'aimes quand on ouvre le capot de ces trucs, abonne-toi. Une semaine sur deux, je teste ce qui tient dans ma carte, et je calcule le reste, sources à l'appui.

[VISUEL : bouton d'abonnement discret en bas, deux secondes.]

Sauf que la phrase « bricolé en une soirée » raconte pas toute l'histoire.

---

## 3. Six mois avant la soirée (4:15 – 5:24)

[VISUEL : la chronologie recule. Un point s'allume : « 18/09/2022 ».]

Pour ça, il faut remonter six mois plus tôt. Le dix-huit septembre deux mille vingt-deux, Georgi Gerganov crée un dépôt qui s'appelle ggml : une bibliothèque en C pour manipuler des tenseurs. Les tenseurs, c'est des grands tableaux de nombres. Et une IA, en fait, c'est surtout ça : des tableaux qu'on multiplie entre eux, encore et encore.

Une semaine plus tard, il sort whisper.cpp, construit sur ggml. Et whisper.cpp fait tourner Whisper, l'IA de reconnaissance vocale d'OpenAI, directement sur ton ordi. Ouais : avant LLaMA, il avait déjà fait le coup une fois, avec une IA d'OpenAI.

[VISUEL : un moteur étiqueté « ggml » ; d'abord une carrosserie « whisper.cpp », puis une deuxième, « llama.cpp », qui vient se poser dessus.]

Donc quand LLaMA fuite en mars, il a déjà le moteur. Il lui manque juste la carrosserie. La soirée, elle est vraie, mais c'est une soirée posée sur six mois de travail. C'est comme un speedrun : tu vois le mec finir le jeu en vingt minutes, mais tu vois pas les heures d'entraînement derrière.

[VISUEL : un chrono de speedrun « 0:20:00 », puis derrière, un compteur d'heures qui défile.]

Bon. Il a le moteur, il a le modèle. Mais il reste le problème des treize gigas.

---

## 4. Le tour de magie : quatre bits (5:24 – 6:41)

[VISUEL : retour sur le README, « 4-bit » qui clignote.]

Tu te rappelles le « quatre bits » du README ? C'est lui qui règle le problème.

Au départ, chaque paramètre du modèle est un nombre rangé sur seize bits. Donc sept milliards de paramètres, c'est sept milliards de nombres à seize bits. Résultat : treize gigas.

La quantification, c'est d'arrondir. Au lieu de garder chaque nombre sur seize bits, on le range sur quatre. Imagine une photo : tu passes de soixante-cinq mille nuances à une palette de seize couleurs. De loin, c'est la même image. De près, tu vois bien que c'est moins fin. Voilà le pari : perdre un peu de précision pour gagner énormément de place.

[VISUEL : un tableau de nombres à virgule qui s'arrondissent en petits blocs ; une photo qui passe en 16 couleurs.]

Alors à ton avis, en quatre bits, il pèse combien, le modèle ? Garde ton chiffre en tête.

[VISUEL : « 13 Go → ? Go », deux secondes.]

Le README d'avril deux mille vingt-trois donne la réponse : de treize gigas, il passe à trois virgule neuf. Divisé par plus de trois. Du coup, il tient dans la mémoire d'un portable. Pour te donner une idée, c'est à peu près le quart des seize gigas de ma 5080.

[VISUEL : une barre de mémoire de 13 Go qui fond jusqu'à 3,9 Go ; le fichier entre enfin dans le MacBook.]
[SON : « clac » quand il rentre.]

[SI LE MODÈLE DE CLAUDE #1 ÉTAIT QUANTIFIÉ : « Et en fait, c'est encore le principe qu'on utilise aujourd'hui : le modèle que j'ai testé sur ma carte était lui aussi quantifié, en [TA QUANTIFICATION, EX. Q4]. »]

Bon, sur un MacBook, ça passe. Mais les gens vont vite essayer beaucoup plus petit.

---

## 5. Deux jours plus tard : un Raspberry Pi (6:41 – 7:31)

[VISUEL : la chronologie avance. « 12/03/2023 ».]

Et en effet, deux jours après le premier commit, le douze mars, un certain Artem Andreenko le lance sur un Raspberry Pi quatre, avec quatre gigas de RAM. Tu vois, ce petit ordi de bricoleur qui tient dans la main. Simon Willison, un dev qui suit tout ça de près, relaie le résultat : environ dix secondes par jeton.

[VISUEL : un Raspberry Pi en gros plan ; un curseur qui clignote, un mot qui apparaît toutes les dix secondes.]
[SON : tic-tac d'horloge, très lent.]

Dix secondes par bout de mot. Pour une seule phrase, t'en as pour plusieurs minutes. Ça fait zéro virgule un jeton par seconde : en jeu vidéo, on appellerait ça un diaporama.

Et pourtant, ça répond. Un modèle de sept milliards de paramètres tourne sur un ordi qui tient dans ta main. Du coup, la question suivante, c'est : comment on rend ça vraiment utilisable ?

---

## 6. La pull request six cent treize (7:31 – 8:43)

[VISUEL : capture de la PR #613 sur GitHub, le titre en gros, puis les deux pseudos.]

Fin mars, une développeuse, Justine Tunney, ouvre une pull request, la six cent treize, écrite avec un autre contributeur, slaren. Une pull request, en gros, c'est une proposition de modif : « voilà mon code, tu le prends ? ». Et son titre est culotté : « Make loading weights 10-100x faster ». Charger les poids dix à cent fois plus vite.

Attention, ça, c'est la promesse du titre, pas une mesure. Mais l'idée derrière est maligne. Normalement, pour lancer le modèle, le programme lit tout le fichier et le recopie en mémoire avant de commencer. Avec leur méthode, qui s'appelle mmap, le programme branche le fichier directement sur la mémoire, et le système va chercher chaque morceau au moment où on en a besoin.

[VISUEL : une barre de mémoire qui se remplissait d'un bloc ; maintenant, elle se remplit par petites cases, au fil de la lecture.]

C'est un open world, en fait : le jeu charge pas toute la carte au lancement, il charge le coin où tu marches.

La pull request est ouverte le vingt-neuf mars au soir, et le lendemain, c'est fusionné. Donc vingt jours après la soirée du README, le bricolage d'un seul dev est déjà devenu un chantier à plusieurs.

---

## 7. L'été où tout se branche dessus (8:43 – 11:00) · relance à ~59 %

[VISUEL : retour éclair sur le hook : les logos d'Ollama et de LM Studio, le bloc de code en transparence. Puis la chronologie avance : « 26/06/2023 ».]

Tu te rappelles, au début ? Si t'as déjà lancé Ollama ou LM Studio, dessous, il y avait son travail. Bah voilà comment c'est arrivé.

Juin deux mille vingt-trois : un nouveau projet apparaît sur GitHub, Ollama. Et quand tu lis ses tout premiers commits, début juillet, il y a cette ligne : « call llama.cpp directly from go ». Appeler llama.cpp directement. Donc Ollama, au départ, c'est une appli construite par-dessus llama.cpp. D'ailleurs, son README le remercie encore aujourd'hui : « llama.cpp project founded by Georgi Gerganov ».

[VISUEL : capture du commit d'Ollama, la ligne surlignée ; puis la ligne du README.]

Et LM Studio, en fait, l'autre nom que tu croises dès que tu parles d'IA en local, le dit dans sa doc : il fait tourner les modèles avec llama.cpp, sur Mac, Windows et Linux, et aussi avec MLX sur les Mac à puce Apple.

[VISUEL : deux applis en façade ; on soulève le capot, et dessous, le même moteur « llama.cpp ».]

Et là, le vingt et un août deux mille vingt-trois, Georgi fusionne GGUF, un nouveau format de fichier pour les modèles. Si t'as déjà téléchargé un modèle en local, t'as sûrement vu passer un fichier qui finit par point gguf. Eh ben voilà d'où il vient : de la pull request deux mille trois cent quatre-vingt-dix-huit, cinq mois après la soirée.

La même année, pour faire vivre ggml, il monte une boîte : ggml.ai. Et l'argent de départ vient de Nat Friedman, l'ancien patron de GitHub, et de Daniel Gross. Le montant, par contre, le site le donne pas.

[VISUEL : la chronologie saute à « 15/05/2025 ». Capture du billet d'Ollama, la phrase de remerciement surlignée.]

Sauf qu'en mai deux mille vingt-cinq, Ollama annonce son propre moteur, pour les modèles qui lisent aussi les images. Et dans la même annonce, il remercie l'équipe de ggml pour la bibliothèque de tenseurs qui fait tourner ses calculs. Oui, ggml, la bibliothèque de septembre deux mille vingt-deux. Celle d'avant la soirée.

Bref, en deux ans, le bricolage d'une soirée est devenu une entreprise, et le moteur sous le capot des applis d'IA locale.

[VISUEL : coupure. La musique s'arrête net.]

Sauf que l'histoire s'arrête pas sur ce happy end. En deux mille vingt-six, il y a deux annonces, et la deuxième pèse presque treize milliards de dollars.

---

## 8. Deux mille vingt-six : Hugging Face, puis Nvidia (11:00 – 13:16)

[VISUEL : la chronologie saute. « 20/02/2026 ». Capture de la discussion GitHub #19759.]
[SON : nouvelle musique, plus grave.]

Le vingt février deux mille vingt-six, Georgi publie un message sur GitHub : ggml.ai rejoint Hugging Face. Hugging Face, si tu connais pas, c'est en gros le GitHub des modèles d'IA : c'est là que tu vas chercher tes modèles.

Dans l'annonce, il explique que c'est pour « keep future AI truly open », garder l'IA de demain vraiment ouverte. Lui et son équipe continuent à bosser à cent pour cent sur ggml et llama.cpp, et le projet reste cent pour cent open source et piloté par la communauté. Le code, d'ailleurs, est toujours sous licence MIT : n'importe qui peut le copier, le modifier, même le revendre, tant qu'il garde la mention des auteurs.

Bon, jusque-là, ça va. Mais le trois septembre deux mille vingt-six, Jensen Huang, le patron de Nvidia, publie un billet : Nvidia annonce un accord pour racheter Hugging Face. Le prix : douze milliards neuf cent trente millions de dollars.

[VISUEL : le chiffre s'écrit en entier, « 12 930 300 000 $ », puis le logo de Nvidia se pose au-dessus de celui de Hugging Face.]
[SON : coup de basse.]

Ouais, t'as bien entendu. Nvidia. La marque de ma 5080.

Et attention : c'est un accord annoncé, le rachat n'est pas conclu. D'après Nvidia, la clôture est attendue au premier semestre deux mille vingt-sept, si les autorités donnent leur feu vert. Donc au moment où tu regardes cette vidéo, ça se joue peut-être encore.

[STATUT DU RACHAT À REVÉRIFIER LE JOUR DU TOURNAGE ET LE JOUR DE LA SORTIE]

Dans son billet, Jensen Huang promet deux choses. Hugging Face restera une plateforme ouverte pour tout l'écosystème. Et il écrit : « NVIDIA compute will not be required ». Pour faire simple, t'auras pas besoin de puces Nvidia pour utiliser Hugging Face.

[VISUEL : les deux citations du billet, surlignées.]

Donc si on suit la chaîne : le projet lancé par un dev de Sofia est maintenu par une équipe de Hugging Face, et Hugging Face pourrait bientôt appartenir à Nvidia, qui vend des cartes graphiques. Sauf que llama.cpp, c'est justement le projet qui fait tourner des IA sans carte Nvidia : sur ton processeur, sur ton Mac, et même sur un Raspberry Pi.

Est-ce que ça va changer quelque chose ? Honnêtement, personne peut le dire aujourd'hui. [TON AVIS EN UNE OU DEUX PHRASES : CONFIANCE, MÉFIANCE ?]

Et toi, t'en penses quoi ? Dis-le-moi en commentaire, je lis tout.

---

## 9. Fin : la réponse au README (13:16 – 14:44)

[VISUEL : retour au README du début, « I have no idea if it works correctly » surligné.]
[SON : la musique du hook revient.]

Tu te rappelles la phrase du début ? « I have no idea if it works correctly. » Aucune idée si ça marche.

Presque quatre ans plus tard, on a la réponse : en fait, ça marche si bien que plus de deux mille personnes ont ajouté du code dans le projet, et il a été copié plus de vingt-quatre mille fois sur GitHub.

[VISUEL : un seul point lumineux, « 10/03/2023 », qui se divise en milliers de points ; compteurs « 2 161 contributeurs » et « 24 731 forks », datés « 23/10/2026 ».]
[CHIFFRES À RELEVER DE NOUVEAU AVANT LA SORTIE]

Du coup, au départ, l'IA chez toi tenait à un seul dev et à une soirée, posée sur six mois de travail. Aujourd'hui, elle tient à plus de deux mille personnes et à une licence. Et même si Hugging Face passe chez Nvidia, la licence MIT laisse à n'importe qui le droit de reprendre le code et de continuer ailleurs.

Et pour toi, en gros, ça change quoi ? Avec un PC correct, tu peux faire tourner ton propre assistant chez toi, même sans connexion. Tu paies l'électricité, pas un abonnement tous les mois.

[VISUEL : ta tour qui s'allume en vert, un terminal qui répond.]

[SI CLAUDE #1 EST SORTIE AVEC TON TEST : « Moi, je l'ai fait sur ma 5080 et ses seize gigas : [TON RÉSULTAT DANS CLAUDE #1 : LE MODÈLE, L'OUTIL, LA VITESSE]. Le Raspberry Pi sortait un jeton toutes les dix secondes ; ma carte en sort [TA VITESSE] par seconde, donc à peu près [LE RAPPORT, CALCULÉ] fois plus. Le diaporama est devenu une conversation. »]

Bricolé en une soirée, aucune idée si ça marche ? Bah, ça marche. Et c'est peut-être sur ton PC que ça tourne en ce moment.

Et si tu veux savoir si seize gigas suffisent vraiment pour lâcher Claude, j'ai fait le test en entier. C'est cette vidéo-là : « Seize gigas de VRAM suffisent-ils pour remplacer Claude ? ». Va voir jusqu'où ma carte a tenu.

[VISUEL : écran de fin, la vidéo Claude #1 à gauche, le bouton d'abonnement à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel | Le README s'écrit lettre par lettre, traduit dessous |
| 0:12 | Chiffre + contraste | 132 000 étoiles, puis Ollama et LM Studio avec le même code dessous |
| 0:34 | Question centrale | « Comment un truc bricolé en une soirée a fini dans des PC comme le tien ? » (0:30 à 165 mots/min) |
| 0:37 | Pont | « Il faut commencer par une fuite. Sur 4chan. » (refermée à 1:15) |
| 1:05 | Humour | Le videur du club LLaMA |
| 1:35 | Aveu | Le titre barré : LLaMA, pas ChatGPT |
| 2:10 | Boucle ouverte | Les treize gigas qui ne rentrent pas (refermée à 6:20) |
| 2:25 | Capture | Le commit « Initial release », 18 h 40 |
| 3:20 | Humour + son | « Seul le plus petit modèle marche », puis le PNJ buggé |
| 3:55 | Appel à l'action | Abonnement (~27 %) |
| 4:10 | Boucle ouverte | « raconte pas toute l'histoire » (refermée à 5:00) |
| 4:40 | Révélation | whisper.cpp : il avait déjà fait le coup avec une IA d'OpenAI |
| 5:10 | Référence | Le speedrun : vingt minutes, des heures d'entraînement |
| 5:25 | Récolte | Le « quatre bits » planté à 2:55 |
| 6:05 | Devinette | « À ton avis, il pèse combien ? Garde ton chiffre en tête. » |
| 6:20 | Visuel + son | 13 Go → 3,9 Go, le « clac » dans le MacBook |
| 6:55 | Son | Le tic-tac du Raspberry Pi, dix secondes par jeton |
| 7:15 | Humour | « On appellerait ça un diaporama » |
| 7:35 | Capture | Le titre culotté de la PR #613 |
| 8:20 | Référence | L'open world qui charge le coin où tu marches |
| 8:43 | Relance forte (~59 %) | Récolte du hook : « dessous, il y avait son travail. Bah voilà comment c'est arrivé. » |
| 9:35 | Révélation | On soulève le capot d'Ollama et de LM Studio |
| 9:55 | Lien au vécu | Le fichier « .gguf » que tu as déjà téléchargé |
| 10:15 | Nom connu | Nat Friedman, l'ancien patron de GitHub |
| 10:30 | Retournement + récolte | Le moteur d'Ollama de 2025 tourne sur ggml, la bibliothèque d'avant la soirée |
| 10:55 | Coupure musique | « La deuxième pèse presque treize milliards » |
| 11:55 | Chiffre + son | 12 930 300 000 $, coup de basse |
| 12:00 | Réaction | « La marque de ma 5080 » |
| 12:45 | Retournement | « Sauf que llama.cpp fait tourner des IA sans carte Nvidia » |
| 13:10 | Engagement | Question en commentaire sur le rachat |
| 13:16 | Boucle fermée | « I have no idea if it works correctly » : la réponse |
| 13:45 | Retournement du sous-texte | Un seul dev → plus de deux mille personnes et une licence |
| 14:35 | Écran de fin | Claude #1 |

**Total** : 33 relances en 14 min 44, environ une toutes les 27 secondes.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:00-0:15 | Moyen | Une citation en anglais pour ouvrir | La traduction à l'écran et à la voix, puis « une IA sur un simple MacBook » dans la même phrase |
| Section 1, la précision sur ChatGPT | Moyen | Avouer que le titre « triche » peut sembler casser la promesse | 20 s maximum, avec le titre barré à l'écran ; la phrase finit sur « elle va tourner chez toi » |
| Section 3, ggml et les tenseurs | Moyen | Le passage le plus technique avant la moitié | Une seule définition, puis whisper.cpp (une IA d'OpenAI : un nom connu), le moteur et la carrosserie, le speedrun |
| Section 4, la quantification | Élevé | Bits et paramètres peuvent perdre les non-devs | La photo en 16 couleurs, la devinette, la barre 13 → 3,9 Go et le « clac » ; un seul calcul à l'écran |
| Section 7, la relance (~59 %) | Élevé | Trois dates à la suite | Elle s'ouvre sur la récolte du hook, et le retournement du moteur d'Ollama (2025) tombe avant la coupure musicale |
| Section 8, Nvidia | Moyen | Sujet d'actu qui peut avoir changé d'ici la sortie | Note de statut, « accord annoncé », clôture attendue d'après Nvidia, question en commentaire |

## Notes de montage

- **Statut du rachat Nvidia / Hugging Face** : à revérifier avant le tournage et le jour de la sortie (billet de Jensen Huang du 03/09/2026 ; formulaire 8-K de Nvidia : accord signé le 02/09/2026, clôture attendue au 1er semestre 2027 sous réserve des autorités). Si le rachat est conclu ou abandonné d'ici là, réécrire les phrases « c'est un accord annoncé… », « pourrait bientôt appartenir » et « même si Hugging Face passe chez Nvidia ».
- **Compteurs** : 132 122 étoiles, 24 731 forks et 2 161 contributeurs le 23/10/2026 (API GitHub). À relever de nouveau avant la sortie et à dater à l'écran. « Plus de deux mille » compte aussi les contributeurs anonymes de l'API (`anon=1`).
- **La chronologie** : un composant qui revient à chaque section (18/09/2022 ggml, 25/09/2022 whisper.cpp, 10/03/2023, 12/03/2023, 30/03/2023, 26/06/2023, 21/08/2023, 15/05/2025, 20/02/2026, 03/09/2026). Elle sert aussi de fond aux chapitres.
- **Les captures GitHub** sont autorisées (pages publiques) : README au commit 77532806 (garder la faute « significanlty » ou couper la phrase à l'écran), commit 26c08466, PR #613 (avec la ligne « written in collaboration with @slaren »), PR #2398, discussion #19759, premiers commits d'Ollama, billet d'Ollama du 15/05/2025. Pas de photo de Georgi Gerganov, de Justine Tunney ni de Nat Friedman : leurs noms à l'écran suffisent.
- **Call of Duty a disparu** ; restent PNJ buggé, speedrun, open world : en motion design seulement, sans logo ni extrait.
- **Charte** : noire (grande histoire), avec le vert d'« IA chez moi » qui n'apparaît qu'au moment où le PC s'allume (hook et fin) : c'est le pont entre les deux piliers.
- **Durée** : à 175-180 mots/min (coupes serrées, comme sur Uber), environ 12 min, plus les pauses du montage. La parenthèse mmap (section 6, deux phrases) et la ligne « seul le plus petit modèle marche » (section 2) peuvent sauter au montage sans casser le récit.
- **Écran de fin** : Claude #1 (« 16 Go de VRAM suffisent-ils pour remplacer Claude ? »), dans la playlist IA. La règle du dépôt veut la vidéo suivante de la playlist du pilier : voir la question 4.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1 | « un dev de Sofia, en Bulgarie » ; « le projet lancé par un dev de Sofia » (jamais « bulgare ») |
| 2 | « Le dix mars deux mille vingt-trois, à dix-huit heures quarante, heure de Londres, Georgi Gerganov publie un commit qui s'appelle "Initial release". » |
| 3, 27 | « Bricolé en une soirée. Aucune idée si ça marche correctement. » ; « faire tourner le modèle sur un MacBook, en quatre bits » ; « il se dégrade après trente ou quarante jetons » ; « Un dev écrit ça en mars deux mille vingt-trois, sous un petit programme qui fait tourner une IA sur un MacBook » |
| 4 | « en C et C++ pur, sans dépendances. Ça tourne sur le processeur, et les puces Apple sont prioritaires » |
| 5 | « trois heures après le premier commit, il corrige déjà un bug dans un calcul » ; « si tu vois des résultats poubelle, mets-toi à jour » ; « un patch avant minuit » (21 h 46 UTC) |
| 6 | « le vingt-quatre février, Meta annonce LLaMA […] de sept à soixante-cinq milliards de paramètres » ; « la licence est réservée à la recherche, sans usage commercial » |
| 7 (⚠️) | « début mars, les poids du modèle fuitent sur 4chan » ; « Quelqu'un poste un torrent, Meta envoie des demandes de retrait » |
| 8, 23 | « llama.cpp n'a jamais fait tourner ChatGPT. Il fait tourner LLaMA, le modèle de Meta. » |
| 9 | « Le dix-huit septembre deux mille vingt-deux, Georgi Gerganov crée un dépôt qui s'appelle ggml » ; « Une semaine plus tard, il sort whisper.cpp » |
| 10 (⚠️) | « Artem Andreenko le lance sur un Raspberry Pi quatre, avec quatre gigas de RAM » ; « Simon Willison […] relaie le résultat : environ dix secondes par jeton » |
| 12 (⚠️), 33 | « la six cent treize » ; « Make loading weights 10-100x faster » ; « ça, c'est la promesse du titre, pas une mesure » ; « écrite avec un autre contributeur, slaren » ; « ouverte le vingt-neuf mars au soir, et le lendemain, c'est fusionné » |
| 13 (⚠️) | « le vingt et un août deux mille vingt-trois, Georgi fusionne GGUF, un nouveau format de fichier » |
| 14, 34 | « il monte une boîte : ggml.ai » ; « pour faire vivre ggml » ; « l'argent de départ vient de Nat Friedman […] et de Daniel Gross » ; « Le montant, par contre, le site le donne pas » |
| 15 (⚠️) | « Juin deux mille vingt-trois : […] Ollama » ; « call llama.cpp directly from go » ; « llama.cpp project founded by Georgi Gerganov » |
| 16, 36 | « LM Studio […] fait tourner les modèles avec llama.cpp, sur Mac, Windows et Linux, et aussi avec MLX sur les Mac à puce Apple » |
| 17 | « plus de cent trente-deux mille étoiles sur GitHub » (daté à l'écran) |
| 18, 30 | « ggml.ai rejoint Hugging Face » ; « keep future AI truly open » ; « Lui et son équipe continuent à bosser à cent pour cent sur ggml et llama.cpp » ; « cent pour cent open source et piloté par la communauté » |
| 19 (⚠️), 35 | « Nvidia annonce un accord pour racheter Hugging Face. Le prix : douze milliards neuf cent trente millions de dollars » ; « la deuxième pèse presque treize milliards » ; « c'est un accord annoncé, le rachat n'est pas conclu » ; « la clôture est attendue au premier semestre deux mille vingt-sept, si les autorités donnent leur feu vert » ; « Hugging Face restera une plateforme ouverte » ; « NVIDIA compute will not be required » |
| 22 | « de treize gigas, il passe à trois virgule neuf » ; « il tient dans la mémoire d'un portable » |
| 25 (⚠️) | « La soirée, elle est vraie, mais c'est une soirée posée sur six mois de travail » |
| 29 | « Au départ, chaque paramètre du modèle est un nombre rangé sur seize bits » ; « seul le plus petit modèle marche, parce qu'il a pas encore trouvé comment assembler les plus gros » |
| 31 | « mmap […] le programme branche le fichier directement sur la mémoire, et le système va chercher chaque morceau au moment où on en a besoin » |
| 32 | « whisper.cpp, construit sur ggml » ; « fait tourner Whisper, l'IA de reconnaissance vocale d'OpenAI » |
| 34 | « Nat Friedman, l'ancien patron de GitHub » |
| 36 | « en mai deux mille vingt-cinq, Ollama annonce son propre moteur, pour les modèles qui lisent aussi les images » ; « il remercie l'équipe de ggml pour la bibliothèque de tenseurs qui fait tourner ses calculs » |
| 17, 37 | « Plus de deux mille personnes ont ajouté du code dans le projet, et il a été copié plus de vingt-quatre mille fois sur GitHub » |
| 30 | « licence MIT : n'importe qui peut le copier, le modifier, même le revendre, tant qu'il garde la mention des auteurs » ; « la licence MIT laisse à n'importe qui le droit de reprendre le code et de continuer ailleurs » |

**Calculs faits dans le script** (pas de source à citer, l'arithmétique se refait à l'écran) : 13 ÷ 3,9 ≈ 3,3 (« divisé par plus de trois ») ; 2^16 = 65 536 et 2^4 = 16 (« soixante-cinq mille nuances », « seize couleurs ») ; 3,9 Go ≈ le quart de 16 Go ; 10 s par jeton = 0,1 jeton/s ; 10 → 30 mars = 20 jours ; 12 930 300 000 $ ≈ « presque treize milliards » ; mars 2023 → février 2027 = « presque quatre ans ».

**Non utilisés, exprès** : la démo sur téléphone (fait 11), la déclaration de Gerganov après Nvidia (fait 20), les pseudos des ingénieurs de Hugging Face (fait 21), « 30B dans 1,5 Go » (fait 12), « plus gros rachat de Nvidia », le découpage 11,9 + 1 Md$ et les 395 M$ (faits 19, 28), « les deux outils les plus utilisés » (fait 24 : aucune mesure), « le plus gros vendeur de cartes graphiques », la mise à jour de Call of Duty, les 184 000 étoiles d'Ollama.

**Images assumées, sans source à chercher** : « Hugging Face, c'est en gros le GitHub des modèles d'IA » (analogie) ; « un club fermé » ; « le studio peut râler, les fichiers circulent déjà » (image de la fuite, après les faits du 7) ; « début deux mille vingt-trois, pour parler à une IA, en général, tu passes par un site » (cadre général, sans chiffre).

## Questions pour l'auteur

1. **Claude #1** (sortie avant le 8 févr.) : quel modèle as-tu fait tourner, avec quel outil (Ollama, LM Studio ou llama.cpp en direct), quelle quantification et quelle vitesse ? Les sections 4 et 9 attendent ces chiffres ; sans eux, les deux lignes `[SI …]` sautent et le script tient quand même. Si c'était Ollama ou LM Studio, le hook devient vrai pour toi aussi : « dessous, il y avait son travail ».
2. **Ton avis sur Nvidia** (section 8) : confiance ou méfiance ? Une ou deux phrases à toi ; je n'ai rien écrit à ta place.
3. **Le sous-texte** : la V1 finissait sur « ton IA tient à un projet d'une soirée, et son avenir se décide en ce moment ». La V2 garde l'hommage et l'enjeu, puis retourne : « au départ, elle tenait à un seul dev ; aujourd'hui, à plus de deux mille personnes et à une licence ». C'est ce que tu veux dire, ou tu préfères finir sur l'inquiétude (l'avenir qui se joue chez Nvidia) ?
4. **L'écran de fin** : la règle du dépôt pointe la vidéo suivante de la playlist du pilier (Histoires : *Tu n'as jamais possédé tes jeux*, provisoire le 22 févr.). Le script pointe Claude #1, parce que la vidéo sert de pont vers « IA chez moi ». Tu gardes Claude #1 ?
5. **Un test sur ta 5080** (bonus de la fiche, +5 h) : lancer llama.cpp en direct à l'écran pendant la section 9 remplacerait la capture de Claude #1. Tu le fais ?
