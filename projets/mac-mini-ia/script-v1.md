# Mac mini ou PC gamer pour l’IA locale :32 Go ne racontent pas toute l’histoire

V1 documentaire 16/11/2026. Calendrier 10 décembre. Cible 11–13 min,145 mots/min. RéférencesmuettesF. Prixactuelpasprévision.

| Partie | Repère |
|---|---|
| Résultat et question |0:00–0:30|
| Le modèle qui tient et sa marge |0:30–3:00|
| Vitesse publiée contre plafond |3:00–6:15|
| Prix et quatre cas |6:15–9:40|
| Verdict |9:40–fin|

## Voix

Un Mac mini peut avoir 32 gigas de mémoire pour ton IA, face aux 16 gigas d’une RTX 5080. Pourtant, la 5080 dispose d’une mémoire beaucoup plus rapide. Donc la petite boîte peut accueillir un modèle plus encombrant, sans gagner automatiquement la course. [F1,F2]

Ces chiffres sont les leurs, je n’ai rien testé chez moi. Alors, pour ton usage, tu choisis la place ou la vitesse ?

[VISUEL : jauges mémoire 32 et 16 ;bandes passantes séparées ;pages constructeurs datées.]

On regarde un fichier qui met la mémoire sous pression, deux séries de vitesses publiées sur Mac, et le prix d’une configuration précise. Puis on fait le calcul dans quatre cas : tu as déjà une machine ou tu pars de zéro, avec un usage léger ou intensif. À la fin, tu sauras quel compromis correspond à ton besoin.

Le cas concret, c’est un Qwen 27 B compressé en 4 bits. Son fichier tourne autour de 16 gigas et demi. Ça laisse beaucoup plus de marge dans un Mac de 32 gigas que sur une carte de 16 gigas. Mais la marge exacte dépend aussi du logiciel, de la conversation et du système. [F7]

Donc une jauge qui dépasse ne suffit pas pour annoncer « impossible ». Sur PC, une partie du modèle peut être prise en charge ailleurs dans la machine. En revanche, si ton objectif est de garder le travail dans la mémoire rapide de la carte, le manque de place devient vite important.

Sur le Mac, la mémoire est unifiée : le processeur, la puce graphique et le système utilisent la même réserve. Ces 32 gigas ne sont donc pas un coffre réservé au modèle. Le système est déjà installé à table avant que l’IA arrive. [F1]

[VISUEL : réserve unique Mac, zone système/modèle/conversation sans chiffrage mémoire arbitraire ;carte PC séparée RAM/VRAM.]

Du coup, on compare des capacités utiles, pas seulement les nombres imprimés sur les boîtes. Une machine peut avoir assez de place pour les poids, puis être à l’étroit quand tu ajoutes un gros document ou une conversation longue. La mémoire de conversation est un deuxième bagage.

Le piège du modèle de base, c’est ça. Tu vois le même nom Mac mini, la même famille de puce, et tu imagines la même liberté. Mais une configuration avec moins de mémoire peut te bloquer sur un fichier que la version 32 gigas accepte. Le choix de la capacité change les modèles accessibles. [F1]

À l’inverse, si ton besoin tient déjà dans la plus petite configuration, acheter davantage de mémoire ne garantit pas une réponse plus intelligente. Le fichier et ses compétences restent les mêmes. La réserve supplémentaire devient utile quand tu la remplis avec un modèle plus gros, un contexte plus long ou d’autres applications.

Voilà le premier verdict : pour savoir quelle machine fait tourner la plus grosse IA, il faut d’abord préciser le fichier. Le nombre de paramètres tout seul cache la compression. Et quand une version très compressée rentre, il faut regarder ce qu’elle a perdu pour maigrir.

[VISUEL : même Qwen 27 B en plusieurs compressions ;taille et qualité sur deux axes.]

Maintenant, la vitesse. Pour la 5080 X3 OC, le constructeur annonce 960 gigas par seconde de bande passante mémoire. Pour le Mac mini M6 avec 32 gigas, Apple annonce 170. Les configurations de base sont listées à 153. Donc les deux chiffres qui circulaient sur le Mac correspondent à des configurations différentes. [F1,F2]

Ça donne un rapport de bande passante d’environ 5,6. Mais ce rapport ne signifie pas que chaque réponse sera 5,6 fois plus rapide sur le PC. C’est une propriété du matériel. Le résultat dépend du modèle et de la manière de le faire calculer. [F7]

Imagine deux cuisines. L’une fait passer les ingrédients plus vite, l’autre a un plus grand garde-manger. Ça aide à comprendre la différence. Mais le débit de la porte ne te donne pas le temps exact pour préparer n’importe quel plat.

Un calcul très simplifié consiste à diviser la bande passante par la quantité de poids lus à chaque mot. Pour un modèle dense d’environ 16,6 gigas,170 divisé par 16,6 donne un peu plus de 10 tokens par seconde. C’est un plafond théorique sous ces hypothèses, pas un résultat mesuré. [F7]

[VISUEL : calcul 170 ÷ 16,6≈10,2 ;tampon estimation simplifiée ;ne pas afficher comme benchmark.]

Le logiciel ajoute des coûts, et certaines optimisations changent ce qui est lu ou calculé à chaque étape. Donc le plafond sert à poser une question au banc d’essai. Il ne remplace pas le banc d’essai.

Justement, deux publications documentent un Mac mini M6 de 32 gigas. Dans la première, la vitesse varie beaucoup selon le modèle, le format et le type de texte. Une campagne d’octobre fait tourner plusieurs modèles dans LM Studio, avec les moteurs llama.cpp, MLX ou Splash. [F4,F5]

Pour un Qwen à experts, un des tableaux tourne autour de 64 tokens par seconde en MLX sur plusieurs questions. Pour un Qwen 27 B dense, les réponses en prose sont beaucoup plus lentes dans les exemples publiés. Donc « le Mac est lent » est une conclusion trop grossière : la recette compte énormément. [F4,F5]

Le modèle à experts mobilise une partie de ses poids pour chaque mot. Du coup, même avec beaucoup de paramètres stockés, il peut demander moins de lectures qu’un modèle dense de taille voisine. Le nombre sur le logo ne raconte pas toute l’histoire de la vitesse.

[VISUEL : modèles denses et experts, stockage et poids actifs séparés ;aucun chiffre personnel.]

La deuxième publication donne un exemple encore plus frappant : sur une question JSON avec un Qwen 27 B en 4 bits, elle mesure 8,5 tokens par seconde sans spéculation, contre 69,3 avec Splash. C’est une mesure publiée, sur une tâche précise. Les fichiers diffèrent entre les moteurs, donc le gain ne vient pas seulement du logiciel. [F6]

Et le JSON, c’est un format prévisible. On ne peut pas prendre ce chiffre et le promettre pour une explication en français, une histoire ou un raisonnement long. C’est comme regarder un temps sur piste sèche pour prédire toute une saison. Ça donne une information ; ça ne garantit pas les autres courses.

Donc le duel utile demande ton modèle, ton type de réponse et ton logiciel, sur des machines dont les conditions peuvent être comparées. Ici, on a des résultats Mac publics. On n’a pas un deuxième chronomètre identique côté PC. [F12]

Pour le prix, on peut poser une référence précise. Le Mac mini M6 avec 32 gigas et 512 gigas de SSD est affiché 1709 euros TTC chez LDLC le 16 novembre 2026. La page annonce un délai de plus de 15 jours. Donc ce prix ne promet pas une livraison immédiate. [F3]

[VISUEL : référence 32/512, page LDLC, date, prix, délai.]

Ce prix couvre un ordinateur. Le prix d’une 5080 couvre seulement une carte. Donc si le PC n’existe pas encore, il faut ajouter le reste de la machine. Et si tu as déjà un PC pour jouer, son coût historique est déjà engagé. On ne peut pas le facturer une deuxième fois pour faire gagner le Mac.

Voilà pourquoi les quatre cas donnent des réponses différentes. Premier cas : tu as déjà un PC et un usage léger. Si ton petit modèle répond à ce que tu veux, conserver ce PC évite un achat. Une pomme en plus sur le bureau n’améliore pas automatiquement ton résumé.

Deuxième cas : tu as déjà un PC, mais un usage intensif que la mémoire de la carte bloque. Le Mac peut apporter plus de place. Mais le coût utile, c’est le prix de l’extension que tu achètes en plus, avec le vrai modèle qui doit justifier cette extension. Le choix peut aussi se porter sur une autre carte ou un autre format de machine.

[VISUEL : matrice PC déjà là ou départ de zéro, usage léger ou intensif.]

Troisième cas : tu pars de zéro, avec un usage léger. Acheter une machine entière uniquement pour quelques requêtes demande de vérifier le besoin. Une configuration plus petite ou un service en ligne peuvent répondre à cet usage avec une autre dépense. Le choix est différent si le Mac sert aussi pour le travail de tous les jours.

Quatrième cas : tu pars de zéro, avec un usage intensif. Là, tu compares des machines complètes, la capacité dont ton modèle a besoin et le temps d’attente acceptable. Le Mac 32 gigas devient une référence concrète. Le PC doit avoir sa propre fiche complète, avec tous les composants, avant qu’on parle de prix gagnant.

Si cette vidéo t’a évité un mauvais achat, abonne-toi.

On peut ensuite faire un calcul d’économies, sans inventer un abonnement. Si ton usage local t’évite réellement 20 euros de dépense par mois, 1709 euros se compensent en environ 85 mois. Si l’économie est de 100 euros par mois, on descend autour de 17 mois. Ces montants mensuels sont des hypothèses d’économies. [F10]

[VISUEL : prix divisé par économie mensuelle ; hypothèses en évidence.]

Le mot réellement fait tout le travail. Si tu gardes ton abonnement parce que le modèle local ne remplit qu’une partie des tâches, tu n’économises pas l’intégralité de la facture. Tu as acheté un outil complémentaire. Ça peut être utile, mais le remboursement calculé change.

Et un service payant peut donner accès à plusieurs fonctions. Si tu remplaces seulement les résumés, tu peux continuer à payer pour d’autres besoins. Du coup, le nombre de mois obtenu avec une division ne suffit pas à décider si la machine est rentable pour toi.

Une autre façon de lire ce calcul, c’est de partir de ce que tu fais vraiment chaque semaine. Tu écris de petits messages, tu relis de longs documents, ou tu fais travailler un agent pendant longtemps ? Ces usages demandent des quantités de mémoire et des temps d’attente différents. La configuration idéale suit cette charge réelle.

Le jeu compte aussi. Un PC gamer peut remplir deux usages avec le même matériel. Un Mac peut être plus adapté à ton environnement de travail, mais ce duel IA ne décide pas de toute la machine à ta place. Donc on garde les besoins quotidiens dans le calcul.

Pour quelqu’un qui veut un modèle plus gros, qui accepte un débit variable et dont les logiciels tournent sur Mac, la configuration 32 gigas mérite un comparatif. Pour quelqu’un qui veut jouer et utiliser des outils liés à son environnement NVIDIA, garder le PC peut être le choix le plus cohérent.

Et si tu as déjà une carte qui fait tenir ton modèle, la première question est simplement ce qu’un Mac nouveau résoudrait. Plus de mémoire devient précieux quand le manque de mémoire est ton problème.

[CROCHET : ton avis sur l’usage d’une deuxième machine, sans prétendre avoir testé un Mac.]

Pour les autres routes vers beaucoup de mémoire, le comparatif 32 gigas détaille les options déjà publiées. Et le 31 décembre, on reprendra le dessin RAM, VRAM et mémoire unifiée, pour voir pourquoi ces gigas ne s’additionnent pas toujours comme on l’imagine.

Allez, salut !

## Notes

Visuels documentaires uniquement. Aucun essai ni ouverture de LM Studio demandés. Prix du 10 décembre : [PRIX À RELEVER] si actualisation nécessaire. Risques : rapport de bande passante confondu avec une mesure, échantillons Mac différents, économies hypothétiques prises pour une facture. Avis facultatif.
