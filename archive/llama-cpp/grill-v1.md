# Grill du script llama.cpp v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Version finale : [`script.md`](script.md). Grille : `youtube-script-grill`, mode B, **variante storytelling** (test des 30 s, axes S1 à S6, axe 10 compté).
> Hypothèses : titre *Le dev qui a mis un ChatGPT dans ton PC*, miniature à faire (charte noire), public de 18-30 ans curieux de tech, surtout africain, avec une part de devs qui connaissent Ollama de nom ; objectif : une « grande histoire » qui sert de pont vers « IA chez moi ». Sortie le lun. 8 févr. 2027 (fiche et `strategie.md`).
> Faits revérifiés à la source le 23/10/2026 : tableau « Vérification des faits » plus bas ; 9 lignes ajoutées à `sources.md` (faits 29 à 37).

**Note globale : 🟠 6,5/10.** 5 🟢 · 11 🟠 · 1 🔴 sur les 17 axes, plus des faits 🔴 avant correction. Bon squelette d'enquête, des récoltes qui marchent, une voix proche de la tienne ; le hook ne dit pas « IA » avant 0:20, la fin s'arrête sur une promo et sept affirmations n'étaient pas sourcées.

## Verdict

Le récit tient. Le fil du README (« hacked in an evening ») est le bon : il ouvre, il revient, et la section 3 le retourne (« une soirée posée sur six mois de travail »). Les images gamer sont à toi (PNJ buggé, speedrun, open world, diaporama) et l'aveu du titre (« mon titre triche un peu ») rend crédible tout le reste.

Le plus gros problème est au bout : la fin ne répond pas au README, abandonne le sous-texte (l'avenir de l'IA chez toi) posé par la section 8, et finit sur ton résultat de Claude #1, écrit au présent alors que rien n'a encore tourné sur ta 5080. Deuxième problème : sept faits ajoutés par le rédacteur sans passer par `sources.md`, dont deux faux ou invérifiables (« ceux qui ont fabriqué la puce de ma 5080 », « le plus gros vendeur de cartes graphiques »). Troisième : les 15 premières secondes donnent une citation, une date et une ville, sans dire qu'il s'agit d'une IA.

Rien de bloquant : la V2 garde 80 % du texte.

## La promesse, le problème profond, la chaîne « mais / donc »

- **Promesse** (titre + miniature) : l'histoire du dev grâce à qui une IA « comme ChatGPT » tourne sur ton PC. Le script la tient, et corrige honnêtement le « ChatGPT » à 1:30.
- **Problème de surface** : comment un programme d'une soirée devient le moteur de l'IA locale.
- **Problème profond** (sous-texte de la fiche) : une IA chez toi, et non chez eux, tient à très peu de chose (un dev, une soirée), et son avenir se joue maintenant. Posé en creux dans le hook, monté en section 8, **jamais résolu** : la section 9 passe à « ce que ça change pour toi » puis à Claude #1.
- **Chaîne « mais / donc »** : solide de 0:37 à 8:33. L'IA vit dans les data centers, **mais** les poids fuitent ; **mais** 13 Go ne rentrent pas ; **donc** le README vise 4 bits ; **sauf que** la soirée cache six mois ; **donc** il a le moteur ; **mais** il reste les 13 Go ; **donc** la quantification ; **et pourtant** le Raspberry Pi répond ; **donc** comment le rendre utilisable ? La chaîne casse en section 7 (« Ensuite, le vingt et un août… », « Et la même année, il monte une boîte… », « Bref… ») : trois faits en « et ensuite ».

## Test des 15 premières secondes

À 145 mots/min, 15 s font environ 36 mots. Lues seules :

> « Bricolé en une soirée. Aucune idée si ça marche correctement. » Ça, c'est le README d'un petit programme publié le dix mars deux mille vingt-trois par un dev de Sofia. Et pourtant,

**Verdict 🟠.** La citation est une bonne ouverture (une tension : ça ne devrait pas marcher). Mais le reste est du contexte : une date complète, une ville. Le spectateur ne sait pas encore qu'on parle d'IA, ni de son PC, ni que le programme a réussi. Le moment le plus fort (« une soirée » contre « 132 000 étoiles, et le moteur d'Ollama et LM Studio ») tombe entre 0:15 et 0:22. Règle du 22/10 : le chiffre le plus fou ou le contraste passe avant 15 s.

**Correction** : dire « une IA sur un MacBook » dans la phrase qui suit la citation, retirer le jour et la ville (ils reviennent en section 2), et faire tomber les étoiles vers 0:12.

## Test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Bricolé en une soirée. Aucune idée si ça marche correctement. » | 🟢 sujet et tension ; raccord avec « le dev » du titre, pas encore avec « ChatGPT » ni « ton PC » |
| 5-15 s | > « Ça, c'est le README d'un petit programme publié le dix mars deux mille vingt-trois par un dev de Sofia. » | 🟠 contexte (date, ville) ; on ne sait pas que c'est une IA |
| 15-30 s | > « Et pourtant, aujourd'hui, il a plus de cent trente-deux mille étoiles sur GitHub, et c'est le moteur qui tourne dans LM Studio et sur lequel Ollama a été construit. Du coup, comment un truc fait en une soirée a fini par mettre une IA dans des PC comme le tien ? » | 🟢 contraste, puis une question centrale unique et simple. 🟠 « 132 000 étoiles » ne parle qu'aux devs, et « le moteur qui tourne dans LM Studio » n'est pas traduit pour celui qui ne connaît pas ces applis |
| Pont | > « Pour le comprendre, il faut commencer par une fuite. Sur 4chan. » | 🟢 départ inattendu, annoncé comme tel ; ouvre une 2e question |

**Budget :** 90 mots ≈ 37 s à 145 mots/min (29 s à 180). La question centrale finit au 79e mot (≈ 33 s à 145, 26 s à 180) : dans la limite des 90 mots, juste au-dessus de 30 s à ton débit pauses comprises.
**À couper :** « le dix mars deux mille vingt-trois », « de Sofia » (déplacés en section 1-2).
**Réécriture des 30 s** (celle de la V2, 94 mots, question au 83e) :

> « Bricolé en une soirée. Aucune idée si ça marche correctement. » Un dev écrit ça en mars deux mille vingt-trois, sous un petit programme qui fait tourner une IA sur un MacBook.
>
> Et pourtant, aujourd'hui, ce programme a plus de cent trente-deux mille étoiles sur GitHub. Et si t'as déjà lancé une IA sur ton PC avec Ollama ou LM Studio, dessous, il y avait son travail.
>
> Du coup, comment un truc bricolé en une soirée a fini dans des PC comme le tien ?
>
> Pour le comprendre, il faut commencer par une fuite. Sur 4chan.

« IA » arrive à 0:07, les étoiles à 0:12, « ton PC » à 0:20. « Dessous, il y avait son travail » est vrai pour les deux applis (faits 15, 16, 36) et devient une promesse que la section 7 récolte.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟠 | Tenue sur la durée, avec un bel aveu sur « ChatGPT » ; mais « IA » n'est pas dit avant 0:20. |
| 2. Alignement | 🟢 | Aucune vente ; un appel à l'abonnement court, à 28 %. |
| 3. Problème profond | 🟠 | « L'avenir se décide maintenant » est monté en section 8, puis lâché par la fin. |
| 4. Public & complexité | 🟢 | Poids, jeton, tenseur, pull request, quantification : chacun défini avant usage, avec une image. |
| 5. Valeur & originalité | 🟢 | Aucun récit en français (vidIQ, 23/10) ; les six mois de ggml et le 13 → 3,9 Go sont des pépites. |
| 6. Structure & transformation | 🟠 | Enquête claire jusqu'à 8:33 ; la fin résume au lieu de répondre au README. |
| 7. Histoire | 🟠 | Georgi n'a pas d'envie dite (son « main goal » est pourtant dans le README) et disparaît comme personnage après la section 7. |
| 8. Mais / donc | 🟠 | Excellent jusqu'à la section 6 ; section 7 en « Ensuite… Et la même année… Bref ». |
| 9. Engagement actif | 🟠 | Un seul « Tu vois le problème ? » ; aucune devinette, alors que le 13 → 3,9 Go s'y prête. |
| 10. Rythme, oralité & liaisons | 🟠 | 2,8 pour 100 mots au total, mais 1,4 et 1,2 dans les sections 7 et 8 ; « en gros » 7 fois. |
| 11. Tics d'IA | 🟠 | Une dizaine, légers (liste plus bas) ; un avis prêté (« je trouve ça encore plus fort »). |
| S1. Les 30 premières secondes | 🟠 | Question avant 90 mots et pont fort ; 5-15 s en contexte. |
| S2. Le pont | 🟢 | « Une fuite. Sur 4chan. » ouvre une 2e question. |
| S3. Les retournements | 🟠 | Un toutes les 30 s jusqu'à 8:33 ; trou d'environ 1 min 10 en section 7 (de « Tu vois le truc ? » à « Sauf que l'histoire… »). |
| S4. Planté / récolté et motif | 🟢 | « Quatre bits », « treize gigas », le README, le Raspberry Pi récoltés ; la chronologie fait le motif. |
| S5. Personnages et enjeu | 🟠 | Georgi, Justine, Artem, Jensen ; seule Justine « veut » quelque chose (le titre de sa PR). |
| S6. La fin | 🔴 | Elle s'arrête sur « Voilà pourquoi je voulais te raconter cette histoire », puis sur tes résultats non mesurés. |

## Le grill

### 1. La fin ne répond pas au README, et elle parle d'un test qui n'existe pas encore

> « Voilà pourquoi je voulais te raconter cette histoire. Quand tu fais tourner une IA chez toi […] derrière, il y a un README qui disait « je sais pas si ça marche ». »
> « Moi, je l'ai fait sur ma 5080 et ses seize gigas de VRAM : [TON RÉSULTAT DANS CLAUDE #1…] »
> « Dans l'épisode un de « Claude ou mon PC », le modèle que j'ai fait tourner sur ma 5080 était lui aussi quantifié »

**Pourquoi ça coince :**
- « Voilà pourquoi je voulais te raconter » te prête un motif et assène la morale ; la variante storytelling l'interdit (« jamais de morale assénée »).
- Le README pose une question (« I have no idea if it works correctly ») que personne ne referme. C'est la meilleure récolte possible, et elle n'est pas faite.
- Le sous-texte monté en section 8 (« est-ce que ça va changer quelque chose ? ») reste sans réponse : la fin repart sur ton PC.
- « Je l'ai fait », « j'ai fait tourner » : au 20/10, rien n'a tourné sur ta 5080 (mémoire du projet). Claude #1 sort avant le 8 févr., mais son résultat n'est pas écrit ; ces phrases doivent rester conditionnelles.

**Correction** (V2, section 9) : refermer le README avec des faits datés, puis retourner le sous-texte.
> Tu te rappelles la phrase du début ? « I have no idea if it works correctly. » Aucune idée si ça marche.
>
> Presque quatre ans plus tard, on a la réponse : en fait, ça marche si bien que plus de deux mille personnes ont ajouté du code dans le projet, et il a été copié plus de vingt-quatre mille fois sur GitHub.
>
> Du coup, au départ, l'IA chez toi tenait à un seul dev et à une soirée, posée sur six mois de travail. Aujourd'hui, elle tient à plus de deux mille personnes et à une licence. Et même si Hugging Face passe chez Nvidia, la licence MIT laisse à n'importe qui le droit de reprendre le code et de continuer ailleurs.

Les lignes sur ta 5080 (sections 4 et 9) passent entre `[SI …]` : elles se lisent seulement si Claude #1 a les chiffres.

### 2. Sept faits du rédacteur absents de `sources.md`

Le V1 les listait lui-même (« Hors `sources.md`, connaissances générales à confirmer »). Vérifiés un par un le 23/10 (détail dans le tableau des faits) :

| Affirmation de la V1 | Verdict | Ce que fait la V2 |
|---|---|---|
| « plus de cent trente-deux mille étoiles » | ✅ fait 17, et API relue : 132 122 le 23/10/2026 | gardé, daté à l'écran |
| « Dans le fichier de Meta, chaque paramètre est un nombre rangé sur seize bits » | ⚠️ le README d'origine convertit en « FP16 » (fait 29) ; le format des fichiers de Meta n'est pas lu | « Au départ, chaque paramètre du modèle est un nombre rangé sur seize bits » |
| mmap : « les morceaux arrivent au moment où on en a besoin » | ✅ description de la PR #613 + Wikipédia (fait 31) | gardé ; et la PR est écrite **avec slaren** (fait 33), donc « leur méthode » |
| « licence MIT, une des licences les plus libres qui existent : tu peux […] en faire ce que tu veux » | ⚠️ MIT ✅ ; « en faire ce que tu veux » oublie la seule condition (garder la mention de copyright) ; « une des plus libres » est un jugement (fait 30) | « n'importe qui peut le copier, le modifier, même le revendre, tant qu'il garde la mention des auteurs » |
| whisper.cpp | ✅ « Port of OpenAI's Whisper model », reconnaissance vocale (fait 32) | ajouté en section 3 : il avait déjà fait le coup avec une IA d'OpenAI |
| Nat Friedman, « l'ancien patron de GitHub » (question 3 de la V1) | ✅ CEO de 2018 à 2021 (CNBC, fait 34) | ajouté en section 7 |
| « le moteur qui tourne dans LM Studio et sur lequel Ollama a été construit » | ✅ LM Studio (doc ouverte directement, fait 36) ; Ollama ✅ au départ (fait 15) ; depuis mai 2025, son propre moteur remercie ggml (fait 36) | hook : « dessous, il y avait son travail » ; section 7 : le moteur de 2025 devient un retournement |

### 3. Trois affirmations fausses ou sans mesure

> « Ouais, t'as bien entendu. Nvidia. Ceux qui ont fabriqué la puce de ma 5080. »

Nvidia conçoit la puce ; « fabriqué » est faux au sens propre, et un dev en commentaire le relèvera. **V2 :** « Nvidia. La marque de ma 5080. »

> « Hugging Face s'apprête à passer chez le plus gros vendeur de cartes graphiques »

Ni « s'apprête » (la clôture dépend des autorités : formulaire 8-K, fait 35) ni « le plus gros vendeur » (aucune part de marché dans `sources.md`). **V2 :** « Hugging Face pourrait bientôt appartenir à Nvidia, qui vend des cartes graphiques. »

> « Les deux outils les plus utilisés pour faire tourner une IA chez soi tiennent sur le code de la soirée du dix mars. »

Le fait 24 propose cette tournure, mais personne n'a mesuré « les plus utilisés ». Et « le code de la soirée » est faux pour Ollama depuis 2025. **V2 :** « LM Studio, en fait, l'autre nom que tu croises dès que tu parles d'IA en local », et le moteur d'Ollama raconté tel quel.

Plus petit : « Trois virgule neuf gigas, c'est moins lourd qu'une mise à jour de Call of Duty » n'a pas de source (la taille des mises à jour varie). **V2 :** « c'est à peu près le quart des seize gigas de ma 5080 » (3,9 ÷ 16 ≈ 0,24, un calcul).

### 4. Les 15 premières secondes en contexte

Voir le test plus haut. C'est la règle du 22/10 : la date et la ville ne sont pas le moment le plus fort.

### 5. Section 7 : trois faits en « et ensuite », au moment de la relance

> « Ensuite, le vingt et un août deux mille vingt-trois, Georgi fusionne GGUF […] Et la même année, il monte une boîte, ggml.ai. Le financement de départ vient de Nat Friedman et Daniel Gross. Le montant, par contre, le site ne le donne pas. »

Trois faits sans rien entre eux, à 9:45-10:15, c'est-à-dire au point de décrochage que les notes de la V1 jugent « élevé ». Et l'ouverture de la relance est une annonce :

> « Et maintenant, le moment où llama.cpp arrive sur ton PC sans que tu le saches. »

**Correction :**
- ouvrir sur la récolte du hook : « Tu te rappelles, au début ? Si t'as déjà lancé Ollama ou LM Studio, dessous, il y avait son travail. Bah voilà comment c'est arrivé. » ;
- donner une raison à ggml.ai (le site : « to support the development of ggml ») et un nom qui parle (Nat Friedman, l'ancien patron de GitHub) ;
- finir la section sur un retournement sourcé :
> Sauf qu'en mai deux mille vingt-cinq, Ollama annonce son propre moteur, pour les modèles qui lisent aussi les images. Et dans la même annonce, il remercie l'équipe de ggml pour la bibliothèque de tenseurs qui fait tourner ses calculs. Oui, ggml, la bibliothèque de septembre deux mille vingt-deux. Celle d'avant la soirée.

C'est la deuxième récolte de la section 3, et elle remplace « même si aujourd'hui il a aussi son propre moteur pour certains modèles », qui ne disait pas lequel.

### 6. Le spectateur ne devine jamais

> « Et le gain, il est écrit dans le README d'avril deux mille vingt-trois. Le modèle de sept milliards passe de treize gigas à trois virgule neuf. »

Le chiffre est le meilleur « clac » de la vidéo : il mérite deux secondes d'attente.
**V2 :** « Alors à ton avis, en quatre bits, il pèse combien, le modèle ? Garde ton chiffre en tête. » puis la réponse.

### 7. Georgi n'a pas d'envie, et Justine est seule

> « Et l'objectif est écrit noir sur blanc : faire tourner le modèle sur un MacBook, en quatre bits. »

C'est son envie (« The main goal is… ») : la V2 dit « son objectif ». Et le premier README contient un aveu qui le rend humain : « only LLaMA-7B is supported since I haven't figured out how to merge the tensors of the bigger models » (fait 29). **V2 :** « Il prévient aussi que pour l'instant, seul le plus petit modèle marche, parce qu'il a pas encore trouvé comment assembler les plus gros. »

> « Avec sa méthode, qui s'appelle mmap »

La PR dit « written in collaboration with @slaren ». Le dire renforce ta phrase suivante (« plus le bricolage d'un seul dev »).

### 8. Les liaisons (axe 10)

Comptées avec `controle.py` (liste du skill) sur la voix off de la V1 : **56 liaisons pour 2 011 mots, soit 2,8 pour 100 mots**. Au-dessus du repère de 1,5, et loin de tes téléprompteurs (0,7 à 0,9). Le problème est leur répartition et leur variété :

| Section | Mots | Liaisons | Pour 100 mots |
|---|---|---|---|
| 0. Hook | 90 | 2 | 2,2 |
| 1. La fuite | 242 | 9 | 3,7 |
| 2. Le soir du dix mars | 257 | 7 | 2,7 |
| 3. Six mois avant | 156 | 10 | 6,4 |
| 4. Quatre bits | 195 | 7 | 3,6 |
| 5. Raspberry Pi | 132 | 5 | 3,8 |
| 6. PR #613 | 167 | 5 | 3,0 |
| **7. L'été** | 281 | 4 | **1,4** |
| **8. 2026** | 322 | 4 | **1,2** |
| 9. Fin | 169 | 3 | 1,8 |

- Les deux sections les plus faibles sont celles de la relance à 60 % et du climax.
- « en gros » revient 7 fois, « tu vois » 7 fois : le tic remplace la liaison.
- Rafales de faits sans liaison ni réaction :
  > « Dans l'annonce, il écrit que c'est pour « keep future AI truly open », garder l'IA de demain vraiment ouverte. L'équipe y consacre cent pour cent de son temps, et le projet reste cent pour cent open source et piloté par la communauté. D'ailleurs, le code est toujours sous licence MIT… »
  > « Ensuite, le vingt et un août […] Et la même année, il monte une boîte, ggml.ai. Le financement de départ vient de Nat Friedman et Daniel Gross. »

  (« L'équipe y consacre » ne dit pas non plus à quoi : la source dit « maintaining ggml/llama.cpp ».)

**V2 :** 2,8 pour 100 mots au total ; sections 7, 8 et 9 à 2,1, 1,8 et 1,9 ; « en gros » 4 fois.

### 9. Les tics d'IA

| Passage de la V1 | Tic | V2 |
|---|---|---|
| « Ensuite, il y a la meilleure phrase : » | annonce (faux suspens) | « Un peu plus bas, il y a la phrase du début : » |
| « Voilà comment démarre le projet : un dev, un commit, et un patch avant minuit. » | rafale de trois | « Voilà comment démarre le projet : avec un patch avant minuit, le soir même. » |
| « Et je trouve ça encore plus fort, parce que c'est exactement comme un speedrun. » | avis prêté (cas « j'ai résilié Netflix » d'ArtCraft) | « C'est comme un speedrun : » ; ton avis, si tu l'as, à dire en improvisant |
| « C'est lui, la clé. » | phrase-choc | « C'est lui qui règle le problème. » |
| « Et maintenant, le moment où llama.cpp arrive sur ton PC sans que tu le saches. » | annonce | récolte du hook (grill n° 5) |
| « Sauf que l'histoire aurait pu s'arrêter là, en happy end. Et en deux mille vingt-six, deux annonces la font basculer. » | annonce vague | « …la deuxième pèse presque treize milliards de dollars. » (un chiffre au lieu d'un mot) |
| « Voilà pourquoi je voulais te raconter cette histoire. » | morale, motif prêté | supprimé (grill n° 1) |
| « C'est comme un jeu qui leak avant sa sortie : tout le monde l'a déjà sur son disque. » | exagération | « le studio peut râler, les fichiers circulent déjà » |
| « sur ton processeur, sur ton Mac, sur un Raspberry Pi » | rafale de trois | gardée, la seule du script : ce sont trois faits (4, 10) |
| « Tu paies l'électricité, pas un abonnement tous les mois. » | forme « B, pas A » | gardée : c'est ton pique contre les abonnements, et le « A » est réel |
| « Attention, ça, c'est la promesse du titre, pas une mesure. » | opposition | gardée : elle corrige une idée que le titre de la PR met vraiment en tête (fait 12) |

### 10. Petits points

- **Le patch « avant minuit »** : 21 h 46 UTC, soit 23 h 46 à Sofia. Vrai dans les deux fuseaux ; la ligne du README (22 h 51 UTC) tombe après minuit à Sofia, donc la V2 ne date que le patch.
- **« milliers de nuances »** : 16 bits font 65 536 valeurs. La V2 dit « soixante-cinq mille nuances » contre « seize couleurs » (2^4) : c'est plus fort et c'est exact.
- **Le prix de Nvidia** : le formulaire 8-K donne 11,9 Md$ plus jusqu'à 1 Md$ de rétention, le billet de Huang le total (12 930 300 000 $). On garde le billet (fait 28), et la clôture attendue au 1er semestre 2027 vient maintenant d'une source primaire (fait 35).
- **Calendrier** : `calendrier.md` place encore llama.cpp au 8 mars (« pour les 4 ans ») et Mobile Money au 8 févr., alors que la fiche et `strategie.md` disent 8 févr. depuis le 23/10. Je n'ai pas touché aux fichiers pilotes : à corriger.
- **L'écran de fin** pointe Claude #1 (playlist IA), alors que la règle du dépôt veut la vidéo suivante de la playlist du pilier (Histoires). Question 4 du script.

## La rétention

| Repère | V1 | V2 |
|---|---|---|
| Relances | 28 en 13:52, une toutes les 30 s | 33 en 14:44, une toutes les 27 s |
| Appel à l'abonnement | 3:50, ~28 % (dans le récit, après le patch) 🟢 | 3:55, ~27 % 🟢 |
| Relance forte vers 60 % | 8:33 (~62 %) : une annonce | 8:43 (~59 %) : la récolte du hook, puis le retournement d'Ollama en 2025 |
| Trou sans retournement | ~1 min 10 en section 7 | le plus long : ~50 s (l'annonce Hugging Face, section 8, avant « Mais le trois septembre ») |
| Ponts | 5 boucles, toutes refermées 🟢 | 6 (le README est refermé à la fin) |

## Vérification des faits du script V1, phrase par phrase

| Phrase de la V1 | Source | Verdict |
|---|---|---|
| « un petit programme publié le dix mars deux mille vingt-trois par un dev de Sofia » | faits 1, 2 | ✅ (« de Sofia », jamais « bulgare » : respecté partout) |
| « plus de cent trente-deux mille étoiles sur GitHub » | faits 17, 37 | ✅ 132 122 le 23/10/2026 |
| « c'est le moteur qui tourne dans LM Studio et sur lequel Ollama a été construit » | faits 15, 16, 36 | ✅ (LM Studio : llama.cpp, plus MLX sur Mac ; Ollama : au départ) |
| « Pour parler à une IA, en février deux mille vingt-trois, tu passes par un site » | cadre général | ⚠️ sans chiffre ; la V2 ajoute « en général » |
| « le vingt-quatre février, Meta annonce LLaMA […] de sept à soixante-cinq milliards de paramètres » ; licence de recherche, non commerciale | fait 6 | ✅ |
| « début mars, les poids du modèle fuitent sur 4chan » ; « Quelqu'un poste un torrent, Meta envoie des demandes de retrait » | fait 7 | ✅ formulation juste du ⚠️ (« début mars », pas de jour, pas de détail inventé) |
| « tout le monde l'a déjà sur son disque » | — | ❌ exagération ; reformulé |
| « llama.cpp n'a jamais fait tourner ChatGPT. Il fait tourner LLaMA, le modèle de Meta. » | faits 8, 23 | ✅ |
| « le plus petit, celui de sept milliards de paramètres, pèse treize gigas » | fait 22 | ✅ |
| « à dix-huit heures quarante, heure de Londres […] « Initial release » » | fait 2 | ✅ (Londres = UTC le 10/03/2023) |
| « en C et C++ pur, sans dépendances. Ça tourne sur le processeur, et les puces Apple sont prioritaires » ; « sur un MacBook, en quatre bits » | faits 3, 4 | ✅ |
| « This was hacked in an evening. I have no idea if it works correctly. » ; « se dégrade après trente ou quarante jetons » | fait 3 | ✅ |
| « trois heures après le premier commit, il corrige déjà un bug dans un calcul » ; « si tu vois des résultats poubelle, mets-toi à jour » | fait 5 | ✅ |
| « Une semaine sur deux, je teste ce qui tient dans ma carte, et je calcule le reste » | `strategie.md`, pilier 2 | ✅ (ligne éditoriale) |
| « Le dix-huit septembre deux mille vingt-deux […] ggml » ; « Une semaine plus tard, il sort whisper.cpp, un autre projet bâti sur ggml » | faits 9, 32 | ✅ |
| « Dans le fichier de Meta, chaque paramètre est un nombre rangé sur seize bits » | fait 29 | ⚠️ « dans le fichier de Meta » non lu ; reformulé |
| « Le modèle de sept milliards passe de treize gigas à trois virgule neuf. Divisé par plus de trois. » | fait 22 | ✅ (13 ÷ 3,9 ≈ 3,3) |
| « moins lourd qu'une mise à jour de Call of Duty » | — | ❌ sans source ; remplacé par un calcul |
| « Dans l'épisode un de « Claude ou mon PC », le modèle que j'ai fait tourner sur ma 5080 était lui aussi quantifié » | — | ❌ test pas encore fait ; passé en `[SI …]` |
| « Le douze mars […] Artem Andreenko […] Raspberry Pi quatre, avec quatre gigas de RAM » ; « Simon Willison […] relaie […] environ dix secondes par jeton » | fait 10 | ✅ formulation juste du ⚠️ (« relayé par Simon Willison ») |
| « Fin mars, une développeuse, Justine Tunney, ouvre une pull request : la six cent treize » ; titre ; « la promesse du titre, pas une mesure » ; 29 → 30 mars | faits 12, 33 | ✅, mais **avec slaren** : ajouté |
| mmap, « les morceaux arrivent au moment où on en a besoin » | fait 31 | ✅ |
| « vingt jours après la soirée du README, le projet n'est déjà plus le bricolage d'un seul dev » | faits 2, 12, 33 | ✅ (10 → 30 mars ; deux contributeurs extérieurs) |
| Ollama, juin 2023 ; « call llama.cpp directly from go » ; README « llama.cpp project founded by Georgi Gerganov » | fait 15 | ✅ |
| « même si aujourd'hui il a aussi son propre moteur pour certains modèles » | fait 36 | ✅ précisé : moteur de mai 2025, qui remercie ggml |
| « LM Studio […] utilise llama.cpp lui aussi, et MLX sur Mac » | faits 16, 36 | ✅ |
| « Les deux outils les plus utilisés pour faire tourner une IA chez soi » | fait 24 | ❌ aucune mesure ; retiré |
| « le vingt et un août deux mille vingt-trois, Georgi fusionne GGUF, un nouveau format de fichier » ; PR 2398 | fait 13 | ✅ (« nouveau format », pas « cassant ») |
| « il monte une boîte, ggml.ai. Le financement de départ vient de Nat Friedman et Daniel Gross. Le montant, par contre, le site ne le donne pas. » | faits 14, 34 | ✅ |
| « Le vingt février deux mille vingt-six […] ggml.ai rejoint Hugging Face » ; « keep future AI truly open » ; « cent pour cent open source et piloté par la communauté » | fait 18 | ✅ |
| « L'équipe y consacre cent pour cent de son temps » | faits 18, 30 | ⚠️ « y » ambigu (à Hugging Face ?) ; la source dit « maintaining ggml/llama.cpp » |
| « licence MIT, une des licences les plus libres qui existent : tu peux […] en faire ce que tu veux » | fait 30 | ⚠️ reformulé avec la condition |
| « Jensen Huang, le patron de Nvidia, publie un billet. Nvidia annonce un accord pour racheter Hugging Face. Le prix : douze milliards neuf cent trente millions » | fait 19 | ✅ |
| « Ceux qui ont fabriqué la puce de ma 5080 » | — | ❌ Nvidia conçoit, ne fabrique pas ; reformulé |
| « c'est un accord annoncé. Au moment où j'enregistre, le rachat n'est pas conclu. [STATUT DU RACHAT À REVÉRIFIER…] » | faits 19, 35 | ✅ ; la V2 ajoute la clôture attendue (8-K) et garde la note de statut, pour le tournage **et** la sortie |
| « Hugging Face restera une plateforme ouverte » ; « NVIDIA compute will not be required » | fait 19 | ✅ |
| « Hugging Face s'apprête à passer chez le plus gros vendeur de cartes graphiques » | — | ❌ deux affirmations sans source ; reformulé |
| « une licence MIT qui permet à n'importe qui de copier le code demain matin » | fait 30 | ✅ |
| « Moi, je l'ai fait sur ma 5080 et ses seize gigas de VRAM » ; « Sur ma carte, c'est [TA VITESSE…] » | — | ❌ au présent avant tout test ; passé en `[SI …]` |
| « En moins de quatre ans, le diaporama est devenu une conversation. » | dépend de ta mesure | ⚠️ déplacé dans le `[SI …]` |

**Ce que j'ai corrigé dans la V2** : la puce « fabriquée » par Nvidia, « le plus gros vendeur de cartes graphiques », « s'apprête à », « les deux outils les plus utilisés », Call of Duty, « tout le monde l'a déjà sur son disque », « dans le fichier de Meta », « en faire ce que tu veux », « l'équipe y consacre », « sa méthode » (avec slaren), et les quatre phrases sur ta 5080 passées en conditionnel.

**Ajouté et sourcé** (faits 29 à 37 de `sources.md`) : « seul le plus petit modèle marche », whisper.cpp et la reconnaissance vocale d'OpenAI, Nat Friedman ancien patron de GitHub, ggml.ai « pour soutenir le développement de ggml », le moteur d'Ollama de mai 2025 et son merci à ggml, la clôture attendue au 1er semestre 2027 (8-K), les 2 161 contributeurs et les 24 731 forks.

## Les points critiques du sujet

- **« de Sofia », jamais « bulgare »** : ✅ respecté dans la V1, gardé.
- **LLaMA, pas ChatGPT** : ✅ la V1 l'assume très bien (titre barré à 1:30). La V2 ajoute une ironie sourcée : avant LLaMA, Georgi avait déjà fait tourner en local une IA d'OpenAI (whisper.cpp). Le « ChatGPT » du titre gagne un clin d'œil vrai.
- **Nvidia / Hugging Face, accord annoncé** : ✅ dans la V1 ; la V2 retire « s'apprête » et ajoute « pourrait bientôt », « si les autorités donnent leur feu vert » et une note de statut à relire le jour du tournage **et** le jour de la sortie (la clôture est attendue au moment même où la vidéo sort).
- **La fuite sur 4chan** : ✅ sourcée (fait 7, presse concordante) et dite sans jour précis, sans auteur, sans chiffre. Seul excès : « tout le monde l'a déjà sur son disque », retiré.
- **Le sous-texte** (une IA chez soi qui tient à un projet d'une soirée, et dont l'avenir se joue maintenant) : bon, et doublement vrai en février 2027, puisque la clôture du rachat est attendue au 1er semestre. Deux réserves :
  - « tient à un projet d'une soirée » n'est vrai qu'avec les six mois de ggml : la V1 le dit, il faut le redire à la fin ;
  - « l'avenir se joue maintenant », laissé sans réponse, pousse vers l'inquiétude alors que les sources disent l'inverse (MIT, « NVIDIA compute will not be required », 24 000 copies). Le laisser ouvert ressemble à du suspense gratuit.

  La V2 garde l'hommage (« une soirée posée sur six mois ») et l'enjeu (Nvidia, la clôture en 2027), puis répond avec des faits : au départ un seul dev ; aujourd'hui plus de deux mille personnes et une licence. C'est une proposition : si tu voulais finir sur l'inquiétude, dis-le (question 3 du script).

## Ce qu'il faut garder

- « Petite précision, parce que mon titre triche un peu. » L'honnêteté qui rend le reste crédible.
- « Donc ton IA tient deux phrases, et après, elle parle comme un PNJ buggé. » Ton registre, et une traduction parfaite des « 30-40 tokens ».
- « Il lui manque juste la carrosserie. » puis le speedrun : la meilleure façon de dire « six mois de ggml ».
- « Retiens ce « quatre bits », parce qu'on y revient dans deux minutes. » Un planté annoncé, puis récolté.
- « en jeu vidéo, on appellerait ça un diaporama » et « Et pourtant, c'est vivant. »
- « C'est un open world […] il charge le coin où tu marches. »
- « Ouais, t'as bien entendu. Nvidia. » Une vraie réaction, à la Cam.
- La note de statut sur le rachat, en crochets : à garder jusqu'à la sortie.

## Plan d'action

1. **Fin** : refermer le README et répondre au sous-texte (grill n° 1) ; valider la proposition ou finir sur l'inquiétude (question 3 du script).
2. **Faits** : appliquer les corrections du grill n° 2 et n° 3 ; relire le statut du rachat et les compteurs (étoiles, forks, contributeurs) le jour du tournage et le jour de la sortie.
3. **Hook** : « une IA sur un MacBook » avant 0:10, les étoiles vers 0:12 (test des 30 s).
4. **Section 7** : récolte du hook, Nat Friedman, le moteur d'Ollama de 2025 (grill n° 5).
5. **Passe de détail** : la devinette des 13 Go, slaren, « seul le 7B marche », les tics, et tes chiffres de Claude #1 dans les `[SI …]`.

Tout est fait dans [`script.md`](script.md) : 2 137 mots, 2,8 liaisons pour 100 mots, question centrale au 83e mot, 0 « vous ».
