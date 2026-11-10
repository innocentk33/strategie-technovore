# llama.cpp : script v1

**Titre** : *Le dev qui a mis un ChatGPT dans ton PC*

**Durée** : environ 2011 mots de voix off. À 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises) : environ 13 min 52 ; à 165 mots/min : 12 min 11. Les timecodes ci-dessous sont calculés à 145 ; à recaler sur la vraie prise.

**Texte et sous-texte** (repris de la fiche) :
- **Texte** : l'histoire de llama.cpp. Un développeur publie le 10 mars 2023 un petit programme pour faire tourner LLaMA, le modèle de Meta, sur un MacBook ; il devient le moteur de LM Studio et la base sur laquelle Ollama a été construit.
- **Sous-texte** : une IA qui tourne chez toi et non chez eux, ça tient à un projet commencé en une soirée (sur six mois de travail). Ce que tu appelles « IA chez moi » a une histoire et un auteur, et son avenir se décide en ce moment.

**Fil rouge** : le README du 10 mars 2023 (« hacked in an evening »). Il ouvre la vidéo, on le relit dans le récit, et on y revient à la fin : de « je ne sais pas si ça marche » à l'IA qui tourne sur ton PC.

**Boucles ouvertes** :
1. « Comment un truc fait en une soirée a fini par mettre une IA dans des PC comme le tien ? » (hook, refermée dans la section 9).
2. « Il faut commencer par une fuite. Sur 4chan. » (hook, refermée dans la section 1).
3. « Le plus petit pèse treize gigas » (section 1, refermée dans la section 4).
4. « Il y a un truc que la phrase "bricolé en une soirée" ne raconte pas » (section 2, refermée dans la section 3).
5. « En 2026, deux annonces font basculer l'histoire » (section 7, refermée dans la section 8).

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. « llama.cpp » se dit « lama point C P P » ; « GGUF » se dit en lettres (G G U F) ; « ggml » aussi.

---

## 0. Hook (0:00 – 0:37)

[VISUEL : écran noir. Le README d'origine s'écrit lettre par lettre, police mono : « This was hacked in an evening - I have no idea if it works correctly. » Pas de titre, pas de logo.]
[SON : un clavier, rien d'autre.]

« Bricolé en une soirée. Aucune idée si ça marche correctement. » Ça, c'est le README d'un petit programme publié le dix mars deux mille vingt-trois par un dev de Sofia.

[VISUEL : le compteur d'étoiles GitHub s'emballe jusqu'à 132 000. En petit : « 23/10/2026 ».]
[SON : un « tic » qui accélère avec le compteur.]

Et pourtant, aujourd'hui, il a plus de cent trente-deux mille étoiles sur GitHub, et c'est le moteur qui tourne dans LM Studio et sur lequel Ollama a été construit.

Du coup, comment un truc fait en une soirée a fini par mettre une IA dans des PC comme le tien ?

[VISUEL : un PC de joueur dans le noir ; la tour s'allume en vert.]

Pour le comprendre, il faut commencer par une fuite. Sur 4chan.

[VISUEL : un fichier torrent qui clignote, puis coupe au noir.]

---

## 1. La fuite (0:37 – 2:17)

[VISUEL : chronologie en bas de l'écran. Un seul point allumé : « 24/02/2023 ».]

Pour parler à une IA, en février deux mille vingt-trois, tu passes par un site, et ton message part sur les serveurs de quelqu'un d'autre. Et le vingt-quatre février, Meta annonce LLaMA, son grand modèle de langage, en quatre tailles : de sept à soixante-cinq milliards de paramètres.

Sauf que tu peux pas le télécharger comme ça. Il faut faire une demande, et la licence est réservée à la recherche, sans usage commercial. En gros, c'est un club fermé, et toi, t'es pas sur la liste.

[VISUEL : un videur devant une porte marquée « LLaMA – chercheurs uniquement ».]

Mais début mars, les poids du modèle fuitent sur 4chan. Les poids, en fait, c'est le modèle lui-même : des milliards de nombres rangés dans des fichiers. Quelqu'un poste un torrent, Meta envoie des demandes de retrait, et forcément, c'est trop tard. C'est comme un jeu qui leak avant sa sortie : tout le monde l'a déjà sur son disque.

[VISUEL : le titre de la vidéo s'affiche, « un ChatGPT » est barré et remplacé par « LLaMA ».]

Petite précision, parce que mon titre triche un peu. llama.cpp n'a jamais fait tourner ChatGPT. Il fait tourner LLaMA, le modèle de Meta. Si je dis « un ChatGPT », c'est pour l'idée : une IA à qui tu écris et qui te répond. Sauf que là, elle va tourner chez toi.

Bon, maintenant, le modèle est dans la nature. Mais il est lourd : rien que le plus petit, celui de sept milliards de paramètres, pèse treize gigas. Tu vois le problème ? Treize gigas à faire tenir dans la mémoire d'un ordi normal.

[VISUEL : un fichier de 13 Go qui essaie d'entrer dans un MacBook, et qui coince.]

Et le dix mars, quelqu'un pousse un commit.

---

## 2. Le soir du dix mars (2:17 – 4:04)

[VISUEL : capture de l'historique GitHub, le commit 26c08466 « Initial release », zoom sur l'heure.]
[SON : notification GitHub.]

Le dix mars deux mille vingt-trois, à dix-huit heures quarante, heure de Londres, Georgi Gerganov publie un commit qui s'appelle « Initial release ». Le projet s'appelle llama.cpp. Et franchement, le README est d'une honnêteté rare.

En gros, il dit : voilà LLaMA, le modèle de Facebook, en C et C++ pur, sans dépendances. Ça tourne sur le processeur, et les puces Apple sont prioritaires. Et l'objectif est écrit noir sur blanc : faire tourner le modèle sur un MacBook, en quatre bits. Retiens ce « quatre bits », parce qu'on y revient dans deux minutes.

[VISUEL : les puces du README s'affichent une par une ; « 4-bit » reste surligné.]

Ensuite, il y a la meilleure phrase : « This was hacked in an evening. I have no idea if it works correctly. » Et un peu plus bas, il prévient : le texte généré commence de façon cohérente, mais en général, il se dégrade après trente ou quarante jetons. Un jeton, pour faire simple, c'est un bout de mot. Donc ton IA tient deux phrases, et après, elle parle comme un PNJ buggé.

[VISUEL : une réponse qui démarre propre, puis les lettres glitchent et partent en bouillie.]
[SON : un bug sonore de vieille console.]

Et le soir même, trois heures après le premier commit, il corrige déjà un bug dans un calcul. Du coup, le README gagne une ligne : si tu vois des résultats poubelle, mets-toi à jour. Voilà comment démarre le projet : un dev, un commit, et un patch avant minuit.

D'ailleurs, si t'aimes quand on ouvre le capot de ces trucs, abonne-toi. Une semaine sur deux, je teste ce qui tient dans ma carte, et je calcule le reste, sources à l'appui.

[VISUEL : bouton d'abonnement discret en bas, deux secondes.]

Sauf qu'il y a un truc que la phrase « bricolé en une soirée » ne raconte pas.

---

## 3. Six mois avant la soirée (4:04 – 5:08)

[VISUEL : la chronologie recule. Un point s'allume : « 18/09/2022 ».]

Pour ça, il faut remonter six mois plus tôt. Le dix-huit septembre deux mille vingt-deux, Georgi Gerganov crée un dépôt qui s'appelle ggml. C'est une bibliothèque en C pour manipuler des tenseurs. Les tenseurs, en gros, c'est des grands tableaux de nombres. Et une IA, en fait, c'est surtout ça : des tableaux qu'on multiplie entre eux, encore et encore.

Une semaine plus tard, il sort whisper.cpp, un autre projet bâti sur ggml. Donc quand LLaMA fuite en mars, il a déjà le moteur. Il lui manque juste la carrosserie.

[VISUEL : un moteur étiqueté « ggml » ; une carrosserie « llama.cpp » vient se poser dessus.]

Du coup, la soirée, elle est vraie. Mais c'est une soirée posée sur six mois de travail. Et je trouve ça encore plus fort, parce que c'est exactement comme un speedrun. Tu vois le mec finir le jeu en vingt minutes, mais tu vois pas les heures d'entraînement derrière.

[VISUEL : un chrono de speedrun « 0:20:00 », puis derrière, un compteur d'heures qui défile.]

Bon. Il a le moteur, il a le modèle. Mais il reste le problème des treize gigas.

---

## 4. Le tour de magie : quatre bits (5:08 – 6:29)

[VISUEL : retour sur le README, « 4-bit » qui clignote.]

Tu te rappelles le « quatre bits » du README ? C'est lui, la clé.

Dans le fichier de Meta, chaque paramètre est un nombre rangé sur seize bits. Donc un modèle de sept milliards de paramètres, c'est sept milliards de nombres à seize bits. Résultat : treize gigas.

L'idée de la quantification, c'est d'arrondir. Au lieu de garder chaque nombre sur seize bits, on le range sur quatre. Imagine une photo : tu passes de milliers de nuances à une palette de seize couleurs. De loin, c'est la même image. De près, tu vois bien que c'est moins fin. C'est ça, le pari : perdre un peu de précision pour gagner énormément de place.

[VISUEL : un tableau de nombres à virgule qui s'arrondissent en petits blocs ; une photo qui passe en 16 couleurs.]

Et le gain, il est écrit dans le README d'avril deux mille vingt-trois. Le modèle de sept milliards passe de treize gigas à trois virgule neuf. Divisé par plus de trois. Du coup, il tient dans la mémoire d'un portable. Trois virgule neuf gigas, c'est moins lourd qu'une mise à jour de Call of Duty.

[VISUEL : une barre de mémoire de 13 Go qui fond jusqu'à 3,9 Go ; le fichier entre enfin dans le MacBook.]
[SON : « clac » quand il rentre.]

Et en fait, c'est encore le principe qu'on utilise aujourd'hui. Dans l'épisode un de « Claude ou mon PC », le modèle que j'ai fait tourner sur ma 5080 était lui aussi quantifié : [TA QUANTIFICATION DANS CLAUDE #1, EX. « Q4 », SI C'EST LE CAS].

---

## 5. Deux jours plus tard : un Raspberry Pi (6:29 – 7:24)

[VISUEL : la chronologie avance. « 12/03/2023 ».]

Et là, les gens commencent à l'essayer sur tout ce qui leur tombe sous la main. Le douze mars, deux jours après le premier commit, un certain Artem Andreenko le lance sur un Raspberry Pi quatre, avec quatre gigas de RAM. Tu vois, ce petit ordi grand comme une carte bancaire. Simon Willison, un dev qui suit tout ça de près, relaie le résultat : environ dix secondes par jeton.

[VISUEL : un Raspberry Pi en gros plan ; un curseur qui clignote, un mot qui apparaît toutes les dix secondes.]
[SON : tic-tac d'horloge, très lent.]

Dix secondes par bout de mot. Pour une seule phrase, t'en as pour plusieurs minutes. C'est du zéro virgule un jeton par seconde : en jeu vidéo, on appellerait ça un diaporama.

Et pourtant, c'est vivant. Un modèle de sept milliards de paramètres répond sur une carte qui tient dans ta main. Du coup, la question suivante, c'est : comment on le rend vraiment utilisable ?

---

## 6. La pull request six cent treize (7:24 – 8:33)

[VISUEL : capture de la PR #613 sur GitHub, le titre en gros.]

Fin mars, une développeuse, Justine Tunney, ouvre une pull request : la six cent treize. Une pull request, en gros, c'est une proposition de modification : « voilà mon code, tu le prends ? ». Et son titre est culotté : « Make loading weights 10-100x faster ». Charger les poids dix à cent fois plus vite.

Attention, ça, c'est la promesse du titre, pas une mesure. Mais l'idée derrière est maligne. Normalement, pour lancer le modèle, le programme lit tout le fichier et le recopie en mémoire avant de commencer. Avec sa méthode, qui s'appelle mmap, le programme demande au système de relier le fichier à la mémoire, et les morceaux arrivent au moment où on en a besoin.

[VISUEL : une barre de mémoire qui se remplissait d'un bloc ; maintenant, elle se remplit par petites cases, au fil de la lecture.]

En gros, c'est un open world. Le jeu charge pas toute la carte au lancement : il charge le coin où tu marches.

Elle ouvre sa pull request le vingt-neuf mars au soir, et le lendemain, c'est fusionné. Donc vingt jours après la soirée du README, le projet n'est déjà plus le bricolage d'un seul dev.

---

## 7. L'été où tout se branche dessus (8:33 – 10:29)

[VISUEL : la chronologie avance. « 26/06/2023 ». Le logo d'Ollama apparaît en silhouette.]

Et maintenant, le moment où llama.cpp arrive sur ton PC sans que tu le saches.

Juin deux mille vingt-trois : un nouveau projet apparaît sur GitHub, Ollama. Et quand tu lis ses tout premiers commits, début juillet, il y a cette ligne : « call llama.cpp directly from go ». Appeler llama.cpp directement. Donc Ollama, au départ, c'est une appli construite par-dessus llama.cpp. D'ailleurs, son README le remercie encore : « llama.cpp project founded by Georgi Gerganov ».

[VISUEL : capture du commit d'Ollama, la ligne surlignée ; puis la ligne du README.]

Et LM Studio, l'autre outil star de l'IA en local, utilise llama.cpp lui aussi, et MLX sur Mac. Tu vois le truc ? Les deux outils les plus utilisés pour faire tourner une IA chez soi tiennent sur le code de la soirée du dix mars. Chez LM Studio, c'est le moteur. Chez Ollama, c'est là que tout a commencé, même si aujourd'hui il a aussi son propre moteur pour certains modèles.

[VISUEL : deux applis en façade ; on soulève le capot, et dessous, le même moteur « llama.cpp ».]

Ensuite, le vingt et un août deux mille vingt-trois, Georgi fusionne GGUF, un nouveau format de fichier pour les modèles. Si t'as déjà téléchargé un modèle en local, t'as sûrement vu passer un fichier qui finit par point gguf. Eh ben voilà d'où il vient : de la pull request deux mille trois cent quatre-vingt-dix-huit, cinq mois après la soirée.

Et la même année, il monte une boîte, ggml.ai. Le financement de départ vient de Nat Friedman et Daniel Gross. Le montant, par contre, le site ne le donne pas.

Bref, en quelques mois, le bricolage d'une soirée est devenu une entreprise, et le moteur des deux applis d'IA locale les plus utilisées.

[VISUEL : coupure. La musique s'arrête net.]

Sauf que l'histoire aurait pu s'arrêter là, en happy end. Et en deux mille vingt-six, deux annonces la font basculer.

---

## 8. Deux mille vingt-six : Hugging Face, puis Nvidia (10:29 – 12:42)

[VISUEL : la chronologie saute. « 20/02/2026 ». Capture de la discussion GitHub #19759.]
[SON : nouvelle musique, plus grave.]

Le vingt février deux mille vingt-six, Georgi publie un message sur GitHub : ggml.ai rejoint Hugging Face. Hugging Face, si tu connais pas, c'est en gros le GitHub des modèles d'IA : c'est là que tu vas chercher tes modèles.

Dans l'annonce, il écrit que c'est pour « keep future AI truly open », garder l'IA de demain vraiment ouverte. L'équipe y consacre cent pour cent de son temps, et le projet reste cent pour cent open source et piloté par la communauté. D'ailleurs, le code est toujours sous licence MIT, une des licences les plus libres qui existent : tu peux le reprendre, le modifier, en faire ce que tu veux.

Bon, jusque-là, ça va. Mais le trois septembre deux mille vingt-six, Jensen Huang, le patron de Nvidia, publie un billet. Nvidia annonce un accord pour racheter Hugging Face. Le prix : douze milliards neuf cent trente millions de dollars.

[VISUEL : le chiffre s'écrit en entier, « 12 930 300 000 $ », puis le logo de Nvidia se pose au-dessus de celui de Hugging Face.]
[SON : coup de basse.]

Ouais, t'as bien entendu. Nvidia. Ceux qui ont fabriqué la puce de ma 5080.

Et attention : c'est un accord annoncé. Au moment où j'enregistre, le rachat n'est pas conclu. [STATUT DU RACHAT À REVÉRIFIER LE JOUR DU TOURNAGE]

Dans son billet, Jensen Huang promet deux choses. Hugging Face restera une plateforme ouverte pour tout l'écosystème. Et il écrit : « NVIDIA compute will not be required ». En gros, t'auras pas besoin de matériel Nvidia pour t'en servir.

[VISUEL : les deux citations du billet, surlignées.]

Donc si on suit la chaîne : le projet d'un dev de Sofia est porté par une équipe chez Hugging Face, et Hugging Face s'apprête à passer chez le plus gros vendeur de cartes graphiques. Et llama.cpp, justement, c'est le projet qui fait tourner des IA sur ton processeur, sur ton Mac, sur un Raspberry Pi, sans carte Nvidia obligatoire.

Est-ce que ça va changer quelque chose ? Honnêtement, personne peut le dire aujourd'hui. Ce qu'on sait, c'est ce qui est écrit : une promesse d'ouverture, et une licence MIT qui permet à n'importe qui de copier le code demain matin. [TON AVIS EN UNE OU DEUX PHRASES : CONFIANCE, MÉFIANCE ?]

Et toi, t'en penses quoi ? Dis-le-moi en commentaire, je lis tout.

---

## 9. Fin : ce que ça change pour toi (12:42 – 13:52)

[VISUEL : retour au README du début, « This was hacked in an evening », qui s'efface lentement.]
[SON : la musique du hook revient.]

Voilà pourquoi je voulais te raconter cette histoire. Quand tu fais tourner une IA chez toi, sans abonnement et sans envoyer tes messages sur le serveur de quelqu'un d'autre, derrière, il y a un README qui disait « je sais pas si ça marche ». Et six mois de travail que personne n'a vus.

Ce que ça te change, concrètement : avec un PC correct, tu peux avoir ton propre assistant, qui tourne chez toi, même sans connexion. Tu paies l'électricité, pas un abonnement tous les mois.

[VISUEL : ta tour qui s'allume en vert, un terminal qui répond.]

Moi, je l'ai fait sur ma 5080 et ses seize gigas de VRAM : [TON RÉSULTAT DANS CLAUDE #1 : LE MODÈLE, LA VITESSE, TON VERDICT EN UNE PHRASE].

Et tu te rappelles le Raspberry Pi et ses dix secondes par mot ? Sur ma carte, c'est [TA VITESSE EN JETONS PAR SECONDE DANS CLAUDE #1], donc à peu près [LE RAPPORT, CALCULÉ] fois plus vite. En moins de quatre ans, le diaporama est devenu une conversation.

Et si tu veux savoir si seize gigas suffisent vraiment pour lâcher Claude, j'ai fait le test en entier. C'est cette vidéo-là : « Seize gigas de VRAM suffisent-ils pour remplacer Claude ? ». Va voir jusqu'où ma carte a tenu.

[VISUEL : écran de fin, la vidéo Claude #1 à gauche, le bouton d'abonnement à droite.]

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel | Le README s'écrit lettre par lettre, « hacked in an evening » |
| 0:12 | Chiffre | Le compteur d'étoiles monte jusqu'à 132 000 (contraste) |
| 0:25 | Question centrale | « Comment un truc fait en une soirée… » |
| 0:33 | Boucle ouverte | « Il faut commencer par une fuite. Sur 4chan. » (refermée à 1:15) |
| 1:00 | Humour | Le videur du club LLaMA |
| 1:30 | Aveu | Le titre barré : LLaMA, pas ChatGPT |
| 2:05 | Boucle ouverte | Les treize gigas qui ne rentrent pas (refermée à 5:50) |
| 2:20 | Capture | Le commit « Initial release », 18 h 40 |
| 3:05 | Humour + son | Le texte qui glitche, le PNJ buggé |
| 3:50 | Appel à l'action | Abonnement (~28 %) |
| 4:00 | Boucle ouverte | « Ce que la phrase ne raconte pas » (refermée à 4:40) |
| 4:45 | Référence | Le speedrun : vingt minutes, des heures d'entraînement |
| 5:10 | Rappel | Le « quatre bits » annoncé à 3:00 |
| 5:50 | Visuel + son | 13 Go → 3,9 Go, le « clac » dans le MacBook |
| 6:05 | Lien au vécu | Ta quantification dans Claude #1 |
| 6:35 | Son | Le tic-tac du Raspberry Pi, dix secondes par jeton |
| 7:05 | Humour | « On appellerait ça un diaporama » |
| 7:40 | Capture | Le titre culotté de la PR #613 |
| 8:15 | Référence | L'open world qui charge le coin où tu marches |
| 8:33 | Relance forte (~62 %) | « llama.cpp arrive sur ton PC sans que tu le saches » |
| 9:15 | Révélation | On soulève le capot d'Ollama et de LM Studio |
| 9:45 | Lien au vécu | Le fichier « .gguf » que tu as déjà téléchargé |
| 10:20 | Coupure musique | « Deux annonces la font basculer » |
| 11:15 | Chiffre + son | 12 930 300 000 $, coup de basse |
| 11:25 | Réaction | « Ceux qui ont fabriqué la puce de ma 5080 » |
| 12:30 | Engagement | Question en commentaire sur le rachat |
| 13:10 | Boucle fermée | Le Raspberry Pi contre ta 5080 |
| 13:40 | Écran de fin | Claude #1 |

**Total** : 28 relances en 13 min 52, environ une toutes les 30 secondes.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, 0:00-0:15 | Moyen | Une citation en anglais pour ouvrir | La traduction suit tout de suite, et le compteur d'étoiles porte le contraste à l'image |
| Section 1, la précision sur ChatGPT | Moyen | Avouer que le titre « triche » peut sembler casser la promesse | 20 s maximum, avec le titre barré à l'écran ; la phrase finit sur « elle va tourner chez toi », qui reconfirme le clic |
| Section 3, ggml et les tenseurs | Moyen | Le passage le plus technique avant la moitié | Une seule définition (« des grands tableaux de nombres »), puis l'image du moteur et de la carrosserie et le speedrun |
| Section 4, la quantification | Élevé | Bits et paramètres peuvent perdre les non-devs | L'image de la photo en 16 couleurs, la barre 13 → 3,9 Go et le « clac » ; un seul calcul à l'écran |
| Section 7, la relance (~60 %) | Élevé | Chute classique, et trois dates à la suite | Phrase d'entrée « llama.cpp arrive sur ton PC sans que tu le saches », capot soulevé, puis coupure musicale et annonce des deux virages |
| Section 8, Nvidia | Moyen | Sujet d'actu qui peut avoir changé d'ici la sortie | Note de statut, formulations « accord annoncé », question en commentaire |

## Notes de montage

- **Statut du rachat Nvidia / Hugging Face** : à revérifier avant le tournage et avant la sortie (billet de Jensen Huang du 03/09/2026 ; la presse parlait d'une clôture attendue au 1er semestre 2027, sous réserve des autorités). Si le rachat est conclu ou abandonné d'ici là, réécrire les deux phrases concernées de la section 8.
- **Compteur d'étoiles** : 132 116 le 23/10/2026. À relever de nouveau avant la sortie, et à dater à l'écran.
- **La chronologie** : un composant qui revient à chaque section (09/2022 ggml, 10/03/2023, 12/03/2023, 30/03/2023, 26/06/2023, 21/08/2023, 20/02/2026, 03/09/2026). Elle sert aussi de fond aux chapitres.
- **Les captures GitHub** sont autorisées (pages publiques) : README au commit 77532806 (garder la faute « significanlty » ou couper la phrase à l'écran), commit 26c08466, PR #613, PR #2398, discussion #19759, premiers commits d'Ollama. Pas de photo de Georgi Gerganov ni de Justine Tunney : leurs pseudos GitHub suffisent.
- **Call of Duty, PNJ buggé, speedrun, open world** : en motion design seulement, sans logo ni extrait.
- **Charte** : noire (grande histoire), avec le vert d'« IA chez moi » qui n'apparaît qu'au moment où le PC s'allume (hook et fin) : c'est le pont entre les deux piliers.
- **Durée** : sous les 12 min si tu coupes serré comme sur Uber (175-180 mots/min) ; la parenthèse mmap (section 6, trois phrases) peut sauter au montage sans casser le récit.
- **Écran de fin** : Claude #1 (« 16 Go de VRAM suffisent-ils pour remplacer Claude ? »), la vidéo suivante de la playlist IA.

## Faits utilisés

| N° (`sources.md`) | Phrase du script |
|---|---|
| 1 | « un dev de Sofia » (jamais « bulgare ») |
| 2 | « Le dix mars deux mille vingt-trois, à dix-huit heures quarante, heure de Londres, Georgi Gerganov publie un commit qui s'appelle "Initial release". » |
| 3 | « This was hacked in an evening. I have no idea if it works correctly. » ; « faire tourner le modèle sur un MacBook, en quatre bits » ; « il se dégrade après trente ou quarante jetons » |
| 4 | « en C et C++ pur, sans dépendances. Ça tourne sur le processeur, et les puces Apple sont prioritaires » |
| 5 | « trois heures après le premier commit, il corrige déjà un bug dans un calcul » ; « si tu vois des résultats poubelle, mets-toi à jour » ; « un patch avant minuit » (21 h 46 et 22 h 51 UTC) |
| 6 | « le vingt-quatre février, Meta annonce LLaMA […] de sept à soixante-cinq milliards de paramètres » ; « la licence est réservée à la recherche, sans usage commercial » |
| 7 (⚠️) | « début mars, les poids du modèle fuitent sur 4chan » ; « Meta envoie des demandes de retrait » |
| 8, 23 | « llama.cpp n'a jamais fait tourner ChatGPT. Il fait tourner LLaMA, le modèle de Meta. » |
| 9 | « Le dix-huit septembre deux mille vingt-deux, Georgi Gerganov crée un dépôt qui s'appelle ggml » ; « Une semaine plus tard, il sort whisper.cpp » |
| 10 (⚠️) | « Artem Andreenko le lance sur un Raspberry Pi quatre, avec quatre gigas de RAM » ; « Simon Willison […] relaie le résultat : environ dix secondes par jeton » |
| 12 (⚠️) | « la six cent treize » ; « "Make loading weights 10-100x faster" » ; « ça, c'est la promesse du titre, pas une mesure » ; « le vingt-neuf mars au soir, et le lendemain, c'est fusionné » |
| 13 (⚠️) | « le vingt et un août deux mille vingt-trois, Georgi fusionne GGUF, un nouveau format de fichier » |
| 14 | « il monte une boîte, ggml.ai. Le financement de départ vient de Nat Friedman et Daniel Gross. Le montant, par contre, le site ne le donne pas. » |
| 15 (⚠️) | « Juin deux mille vingt-trois : […] Ollama » ; « "call llama.cpp directly from go" » ; « "llama.cpp project founded by Georgi Gerganov" » ; « même si aujourd'hui il a aussi son propre moteur pour certains modèles » |
| 16 (⚠️) | « LM Studio […] utilise llama.cpp lui aussi, et MLX sur Mac » |
| 17 | « plus de cent trente-deux mille étoiles sur GitHub » (daté à l'écran) ; « licence MIT » |
| 18 | « Le vingt février deux mille vingt-six […] ggml.ai rejoint Hugging Face » ; « keep future AI truly open » ; « cent pour cent de son temps » ; « cent pour cent open source et piloté par la communauté » |
| 19 (⚠️) | « Nvidia annonce un accord pour racheter Hugging Face. Le prix : douze milliards neuf cent trente millions de dollars » ; « c'est un accord annoncé […] le rachat n'est pas conclu » ; « Hugging Face restera une plateforme ouverte » ; « NVIDIA compute will not be required » |
| 22 | « Le modèle de sept milliards passe de treize gigas à trois virgule neuf » ; « il tient dans la mémoire d'un portable » |
| 24 (⚠️) | « Les deux outils les plus utilisés pour faire tourner une IA chez soi » (formulation de `sources.md`, jamais « la plupart des IA locales ») |
| 25 (⚠️) | « la soirée, elle est vraie. Mais c'est une soirée posée sur six mois de travail » |

**Non utilisés, exprès** : la démo sur téléphone (fait 11), la déclaration de Gerganov après Nvidia (fait 20), les pseudos des ingénieurs de Hugging Face (fait 21), « 30B dans 1,5 Go » (fait 12), « plus gros rachat de Nvidia » et le découpage du prix (faits 19, 28), les 395 M$ levés par Hugging Face, les « millions de PC ».

**Hors `sources.md`, connaissances générales à confirmer** : « seize bits » par paramètre dans le fichier d'origine (cohérent avec 13 Go pour 7 milliards, fait 22) ; le principe de mmap (chargement à la demande) ; Hugging Face comme « le GitHub des modèles d'IA » ; MIT comme licence permissive ; Nvidia qui conçoit la puce de la RTX 5080 ; Ollama qui a « son propre moteur pour certains modèles » (fait 15, 2e vérif).

## Questions pour l'auteur

1. **Claude #1** : quel modèle as-tu fait tourner, avec quel outil (Ollama, LM Studio ou llama.cpp en direct) et quelle quantification ? Si c'était Ollama ou LM Studio, la section 4 peut dire « tu as vu llama.cpp tourner sans le savoir », ce qui serait plus fort.
2. **Ton avis sur Nvidia** (section 8) : confiance ou méfiance ? Une ou deux phrases à toi ; je n'ai rien écrit à ta place.
3. **whisper.cpp** : veux-tu dire ce qu'il fait (la transcription de la voix, avec Whisper d'OpenAI) ? C'est connu, mais pas encore dans `sources.md`. Même question pour Nat Friedman, « l'ancien patron de GitHub ».
4. **Le sous-texte** : la fin dit « ton IA chez toi tient à un projet commencé en une soirée, et son avenir se décide en ce moment ». C'est bien ce que tu voulais dire avec ton titre, ou c'est plutôt l'hommage à un dev ?
5. **Un test sur ta 5080** (bonus de la fiche, +5 h) : lancer llama.cpp en direct à l'écran pendant la section 9 remplacerait la capture de Claude #1. Tu le fais ?
