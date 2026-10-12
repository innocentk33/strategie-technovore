# Claude ou mon PC ? #1 : brouillon V1 (version grill)

**Titres proposés**
1. *Claude Opus 5.5 ou ma carte graphique ?* (recommandé : il promet le duel, colle à la miniature « LEQUEL ? » et reprend le nom de la série)
2. *J'ai mis ma carte graphique face à Claude Opus 5.5*
3. *Le second pouvoir de votre carte graphique* (ta formule : très bonne pour le guide du 4 janvier, moins claire ici sur le duel)

**Hook choisi** : la scène in medias res. Deux sites identiques, une question (« A ou B ? »), un prix (200 $/mois). Le spectateur joue dès la 5e seconde, et la miniature est confirmée tout de suite.

**Choix techniques supposés** (à confirmer pendant les essais du 2 au 13 nov.) : Qwen3.8-Flash-Next via Strata, piloté par pi. Si tu passes par LM Studio (qwen3.8-27b), seule la partie 3 change : la variante est en fin de fichier.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture. `[crochets]` = à remplir après les essais, rien n'est inventé.

---

## 0. Hook (0:00 – 0:35)

[VISUEL : deux navigateurs côte à côte, le même site, aucun logo. Étiquettes « A » et « B ».]

Ces deux sites ont été codés par une IA. Même prompt, mêmes images, même consigne.

L'un vient de Claude Opus 5.5, d'Anthropic. Mon abonnement, Claude Max, me coûte deux cents dollars par mois.

Oooh my god.

[VISUEL : une RTX 5080 en 2D, les ventilateurs se mettent à tourner.]

L'autre vient de ma carte graphique. Une RTX 5080, qui jusqu'ici me servait surtout à déchirer des Rathalos sur Monster Hunter.

Alors, lequel est Claude ? A ou B ? Gardez votre réponse en tête. On va faire trois manches, de plus en plus dures, et à la fin on verra pour qui ça vaut vraiment le coup.

[SON : petit « ding » de quiz sur « A ou B ? ».]

## 1. Les règles du duel (0:35 – 1:05)

Avant la réponse, les règles.

Chaque IA travaille dans son outil. Claude dans Claude Code, avec mon abonnement. Qwen, le modèle qui tourne sur ma carte, dans pi, un petit harnais open source.

Un harnais, c'est ce qui donne des mains au modèle : il peut ouvrir vos fichiers et les modifier tout seul. Sans lui, même le meilleur modèle du monde vous répond dans une fenêtre de chat, et c'est vous qui copiez-collez.

Pour le reste, c'est pareil des deux côtés : même prompt, mêmes images, et [deux] relances maximum pour corriger les bugs. À chaque manche, je donne le point au meilleur résultat, et je vous montre pourquoi.

[VISUEL : panneau « Règles » en 2D, les lignes apparaissent une par une.]

> **Variante, si Claude Code se branche sur Strata** (Strata expose une API de style Anthropic en local, à tester) : « Les deux travaillent dans le même outil, Claude Code. Seul le cerveau change. » C'est plus équitable, et ça ne demande aucune clé API.

## 2. Manche 1 : le site (1:05 – 2:30)

Manche 1. Le prompt : [ton prompt, ex. « la landing page d'une marque de sneakers, avec ces quatre images »].

[VISUEL : le prompt s'écrit à l'écran en accéléré, puis deux chronos A et B qui tournent.]

Côté A, [X] minutes. Côté B, [Y] minutes.

[Ta réaction au résultat : un détail précis qui impressionne, un détail qui cloche. Ex. « Regardez le menu sur mobile… »]

Alors, A ou B ?

[VISUEL : écran noir une seconde, « A ou B ? » au centre.]

Claude, c'était [A/B]. L'autre a été codé ici.

[VISUEL : capture des réglages réseau, Wi-Fi désactivé, avec la génération qui tourne en fond.]

Wi-Fi coupé, pendant toute la génération. Rien n'est sorti de chez moi.

Point pour [Claude / ma carte], parce que [ta raison en une phrase]. [Score : X – Y.]

Et là, vous devriez avoir une question. Comment une carte faite pour jouer arrive à coder un site sans internet ?

## 3. Comment c'est possible (2:30 – 4:00)

Claude, lui, tourne sur des serveurs chez Anthropic. Et des serveurs, tout le monde peut en avoir. C'est juste une machine, un ordi quoi.

Le souci, c'est la puissance. Si vous prenez le vieil ordi de tata Jacqueline, votre IA va vous répondre plus lentement qu'Oogway dans Kung Fu Panda.

[VISUEL : une tortue en 2D qui tape au clavier, une touche toutes les trois secondes.]

C'est pour ça qu'on passe par les cartes graphiques. À la base, une carte graphique, ça sert à calculer des triangles. Des millions de triangles, qui finissent en écailles de Rathalos sur votre écran.

[VISUEL : un dragon en fil de fer, qui se remplit de triangles puis de textures.]

Pour afficher tout ça soixante fois par seconde, elle fait des milliers de petits calculs en même temps. Un processeur en fait quelques-uns à la fois, très vite. Et une IA, au fond, c'est des milliards de petits calculs. Donc la carte graphique est parfaite pour ça.

Mais pour calculer, il faut de la mémoire. Sur une carte graphique, elle s'appelle la VRAM, et c'est elle qui décide quelle IA rentre ou pas. Ma 5080 en a seize gigas.

Le modèle que j'utilise s'appelle Qwen 3.8 Flash Next. Il vient d'Alibaba, et ses poids sont publics : n'importe qui peut le télécharger et le faire tourner gratuitement. Il fait cent vingt-cinq milliards de paramètres. Soixante-dix gigas à télécharger.

Soixante-dix gigas, dans une carte qui en a seize.

[VISUEL : un gros bloc « 70 Go » qui essaie d'entrer dans une petite boîte « 16 Go » et reste coincé.]

Normalement, ça ne rentre pas. Mais les goats d'Alibaba l'ont construit d'une façon un peu spéciale. Le modèle est découpé en [experts], des petits spécialistes, et pour chaque mot qu'il écrit, il n'en réveille que quelques-uns. Strata, l'outil open source qui le fait tourner chez moi, en profite : il garde les experts les plus utilisés dans la carte graphique, et range les autres dans la RAM de l'ordi.

[VISUEL : les experts sont de petits personnages. Les plus actifs restent dans la boîte « VRAM », les autres attendent dans la boîte « RAM ».]

Ma RAM, c'est trente-deux gigas de DDR5. Et la RAM, en ce moment, c'est devenu une des ressources les plus précieuses de la tech. Y a qu'à voir le prix sur Amazon. La mienne, je l'ai payée [prix d'achat]. Aujourd'hui, elle est à [prix actuel]. Non mais c'est une crypto ce truc.

[VISUEL : la courbe de prix de la barrette, habillée comme un graphique de crypto, avec une fusée.]

Dernier détail. Cent vingt-cinq milliards de paramètres dans soixante-dix gigas, c'est déjà compressé. On appelle ça la quantization : on arrondit chaque nombre du modèle pour qu'il prenne moins de place, un peu comme quand vous enregistrez une photo en JPEG. On perd un peu de finesse. Et justement, les deux prochaines manches vont montrer combien.

## 4. L'installation en accéléré (4:00 – 5:00)

Côté installation, j'ai fait simple.

Si vous avez une autre carte, le site [nom exact de « caniarun », à vérifier] vous dit quels modèles elle peut faire tourner. Pour Strata, il faut au moins douze gigas de VRAM et trente-deux de RAM. Chez moi, ça passe.

Ensuite, un double-clic sur l'installeur. Il détecte la carte tout seul, puis il télécharge les soixante-dix gigas. [Durée du téléchargement chez toi.]

[VISUEL : la barre de téléchargement en accéléré, un compteur de gigas qui monte.]

À partir de là, ça marche, mais c'est encore brut. Strata ouvre une petite page web pour discuter avec le modèle. C'est pas encore sexy : nous, on veut qu'il crée des choses. Donc on le branche à pi.

[VISUEL : le terminal de pi, la ligne qui pointe vers le serveur local de Strata.]

Premier test : « Bonjour, dis-moi qui tu es. »

[VISUEL : la réponse qui s'écrit en direct, le compteur de tokens par seconde en grand.]

[La réponse du modèle.] Regardez la vitesse du truc : [X] tokens par seconde. Claude, chez moi, répond à [Y] tokens par seconde.

Mais dire bonjour, n'importe quel chatbot sait le faire. Donc manche 2.

## 5. Manche 2 : le jeu (5:00 – 7:00)

Un site, c'est du texte et des boutons qui restent à leur place. Un jeu doit réagir à vos touches sans planter au bout de dix secondes.

Le prompt : [ton jeu, ex. « un petit jeu de chasse au dragon en 2D, vu du dessus, avec une barre de vie »].

[VISUEL : les deux chronos, puis les deux jeux côte à côte, A et B, en train d'être joués.]

[Temps côté A et côté B, nombre de relances utilisées.]

[Ta réaction : ce qui marche, ce qui bugge, le détail qui te fait rire.]

A ou B ?

Claude, c'était [A/B]. Point pour [qui], parce que [ta raison]. [Score : X – Y.]

Jusqu'ici, [Qwen tient le choc / Claude mène]. Mais un site et un petit jeu, ça tient dans un ou deux fichiers. Quand on code pour de vrai, on travaille sur des projets de dizaines de fichiers, avec du code écrit par d'autres. Donc pour la dernière manche, j'ai cherché exprès la tâche qui allait le faire craquer.

[SON : la musique baisse, plus grave.]

## 6. Manche 3 : la tâche qui fait craquer (7:00 – 9:00)

> **À choisir pendant les essais** (garde celle qui casse vraiment) :
> - (a) faire évoluer un projet de [N] fichiers, en ajoutant une fonctionnalité qui touche plusieurs fichiers ;
> - (b) trouver et corriger un bug dans du code existant, par exemple dans un de tes anciens projets Flutter des tutos de la chaîne ;
> - (c) une très longue session où il doit se souvenir de consignes données au début.

Manche 3. Le prompt : [la tâche].

[Ce qui se passe côté Qwen, raconté dans l'ordre :] Au [X]e essai, [ce qui casse]. Je relance. [Ce qui se passe.] [Ce que tu as compris de la limite : il oublie les fichiers du début, il tourne en rond, il invente une fonction qui n'existe pas…]

[VISUEL : l'erreur à l'écran, zoom sur la ligne qui casse. C'est le moment le plus important de la vidéo, montre-le en entier.]

Côté Claude : [ce qui se passe, en combien d'essais].

Point pour [qui]. Score final : [X – Y].

[Une phrase honnête sur ce que ça t'a fait, avec tes mots.]

## 7. Le compte (9:00 – 10:00)

Maintenant, faisons les comptes, parce que « gratuit », c'est vite dit.

Côté Claude : deux cents dollars par mois, que je code une heure ou cinquante.

Côté carte : le modèle est gratuit, Strata et pi aussi. Mais pendant qu'elle code, ma carte tire [X] watts. Sur [Y] heures de code par mois, ça fait [Z] euros d'électricité.

[VISUEL : un compteur électrique en 2D, les euros qui défilent lentement, à côté d'un compteur « 200 $ » fixe.]

Et surtout, il faut avoir la carte. Une 5080, c'est [prix] euros. Si vous l'avez déjà pour jouer, l'IA est un bonus. Si vous comptez l'acheter juste pour ça, il faut [N] mois d'abonnement Claude pour la rembourser.

Côté vitesse : [tokens par seconde, des deux côtés]. Côté relances : [combien de corrections il a fallu à chacun].

## 8. Pour qui ça vaut le coup ? (10:00 – 11:00)

Alors, pour qui ça vaut le coup ?

Vous avez déjà une carte avec [au moins douze gigas de VRAM, selon tes tests] et elle sert surtout à jouer ? [Ton verdict, ex. « Installez-le ce soir. Pour un site ou un petit jeu, il fait le travail. »]

Vous bossez sur des gros projets ? [Ton verdict après la manche 3.]

Vous manipulez du code ou des documents que vous ne voulez envoyer à personne ? Là, le local a un vrai avantage : rien ne quitte votre machine.

Et si vous pensiez acheter une carte juste pour ça : [ton verdict, avec le calcul d'au-dessus].

Moi, [ce que tu fais concrètement maintenant : ce que tu confies à Qwen, ce que tu gardes pour Claude]. [Seulement si c'est vrai :] En tout cas, ma carte sert enfin à autre chose qu'à chasser des Rathalos.

## 9. La suite (11:00 – 11:25)

Cette série, c'est un épisode par modèle. Le prochain que je mets face à Claude, c'est vous qui le choisissez : Gemma, Mistral, un autre ? Dites-le en commentaire, et abonnez-vous pour ne pas le rater.

Et dans un prochain épisode, je vous montre une interface qui se construit toute seule selon ce que vous lui demandez. Vous allez croire que vous êtes sur ChatGPT.

[VISUEL : trois secondes de démo d'OpenIntelligentUI, puis écran de fin.]

---

## Notes de montage
- **Droits** : Oogway et le Rathalos sont des personnages protégés. Utilise une tortue et un dragon génériques en 2D, l'allusion suffit.
- **Score** : un compteur fixe en coin d'écran pendant les manches, avec un « ding » à chaque point.
- **Révélations** : une coupure de musique d'une seconde juste avant chaque « Claude, c'était… ».

## Variante LM Studio (qwen3.8-27b)
Remplace le passage « Le modèle que j'utilise… » jusqu'à « la RAM de l'ordi » par :
« Le modèle que j'utilise s'appelle Qwen 3.8, la version de vingt-sept milliards de paramètres. Il vient d'Alibaba, et ses poids sont publics. Le fichier fait seize gigas et un dixième. Ma carte en a seize. Il manque un dixième de giga, plus la place pour la conversation. Donc LM Studio met une partie du modèle dans la RAM de l'ordi, et c'est là que ma DDR5 sert à quelque chose. » Puis la blague sur le prix de la RAM, sans changement. Dans ce cas, la partie installation passe par LM Studio, et pi se branche sur son serveur local.

## À vérifier avant le tournage
- Le nom exact et l'origine de **Qwen3.8-Flash-Next** : est-ce une version officielle d'Alibaba ? Combien de paramètres sont actifs par mot ? Est-ce bien un modèle à « experts » ?
- **Strata** : la taille réelle du téléchargement, les tokens par seconde sur ta 5080, et si Claude Code peut se brancher sur son API de style Anthropic (variante des règles).
- **pi** : comment se brancher sur Strata ou LM Studio (fournisseur personnalisé dans `models.json`).
- Le site **« caniarun »** : le nom exact et l'URL.
- Le prix de ta RAM à l'achat et aujourd'hui (une capture Amazon).
- Les watts de la carte pendant la génération : un wattmètre sur la prise, ou le logiciel de la carte.
- **OpenIntelligentUI** : ce que fait vraiment le dépôt, avant de le teaser.
- **Voix clonée** : fais lire le texte dans `/voix-off-ia` (ex. « Qwen 3.8 », « RTX 5080 », « DDR5 », « tokens »).
