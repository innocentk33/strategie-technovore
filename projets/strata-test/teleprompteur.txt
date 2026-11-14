TÉLÉPROMPTEUR — Le meilleur modèle possible pour 16 Go de VRAM (Strata) (V3, 14/11 au soir : résultats d'abord, plus de pronostic)
Une ligne = un souffle. Ligne vide = respiration. Les [MARQUEURS] et les (indications) ne se lisent pas.
Les nombres sont écrits en chiffres pour la lecture, mais tu les dis en entier.
Une seule phrase est à toi de valider : celle de ce qui t'a le plus surpris (section des erreurs).
Les prompts ne se lisent pas : ils sont à l'écran.

[ HOOK ]

(les quatre résultats défilent pendant que tu parles)

Ces tests ont été réalisés avec Qwen 3.8 Flash Next,
qui tourne sur une carte de 16 gigas, à près de 70 tokens par seconde.
Et tout ça, à partir d'un seul prompt.

Par contre, ce n'est que la moitié d'un modèle.
Alors, est-ce que ça remplace Claude ?

Je vais te montrer ce qu'il a réussi, pourquoi il est aussi fort,
à quelle vitesse il tourne et comment l'installer.
Et à la fin, les erreurs qui m'ont fait perdre plus de 2 heures.

[ LES RÉSULTATS ]

D'abord, les résultats.
À gauche, c'est Pi, l'outil qui laisse l'IA écrire les fichiers toute seule.
À droite, c'est le compteur de Strata, le programme qui fait tourner le modèle,
en tokens par seconde.
Un token, c'est à peu près trois quarts de mot.

J'écris mon prompt en anglais pour qu'il soit beaucoup plus efficace,
car sa doc dit qu'il est moins bon dans les autres langues.
Et je ne touche jamais au code.
S'il bloque, je le relance avec une phrase,
et je compte chaque relance, comme une pièce de plus à l'arcade.

Le premier, c'est une île en 3D.
Elle tourne à la souris, elle zoome,
et quand j'appuie sur N, la nuit tombe, avec les étoiles.
Il l'a écrite en 15 minutes et demie, sans aucune relance.

Ensuite, un casse-briques.
Il y a les vies, l'écran de game over, des bruitages,
et des bonus qui élargissent la raquette ou qui triplent la balle.
Celui-là, il l'a fait en 8 minutes, lui aussi sans relance.

Après, le site d'une agence de voyage qui n'existe pas, avec mes propres photos.
Le Kilimandjaro en grand à l'accueil,
les destinations avec leurs prix, et des témoignages de voyageurs.
Ça a vraiment l'air d'un site d'agence.
Il l'a écrit en 17 minutes, mais en suivant un plan écrit par Claude,
et je t'explique pourquoi un peu plus loin.

Et le plus dur, un mini-Minecraft.
Tu marches dans un monde en cubes, avec des arbres et du relief,
tu sautes, tu casses des blocs,
et tu construis avec de la terre, de la pierre, du sable et du bois.
Même les textures en pixels, c'est son code qui les dessine,
sans jamais voir ce qu'il dessine.
Là, il lui a fallu 3 relances et 35 minutes.

[ LA PUISSANCE DU MODÈLE ]

Pour comprendre ces résultats, il faut savoir d'où vient ce modèle.
Qwen 3.8 Flash Next, c'est l'avant-goût de Qwen 4,
sorti en août pour montrer sa nouvelle architecture.
Et en code, d'après les tests de Qwen, il fait mieux que Qwen 3.8 27B,
le modèle dont je te parlais jeudi dernier dans la vidéo sur Qwen 4.
Sur un test de code dans plusieurs langages,
il monte à 81, contre 74 pour le 27B.

Sauf que chez moi, il ne tourne pas en entier.
Avec 32 gigas de RAM, je ne peux prendre que le Coder,
c'est-à-dire le même modèle coupé de moitié et gardé pour le code.
Ses auteurs disent eux-mêmes qu'il est expérimental,
et plus faible en dehors du code et de l'anglais.
Mais sur leur test de code principal,
il garde quand même 95 % du score du modèle complet.
Ça, c'est leur chiffre.
Ce qu'il fait vraiment, tu viens de le voir.

Et même coupé de moitié, il reste bien plus gros que ma carte.
Lundi dernier, je te disais que 16 gigas suffisent,
si tu prends le bon fichier.
Du coup, comment il tient ?

[ D'OÙ VIENT CETTE PUISSANCE ]

En fait, le modèle est découpé en centaines de petits spécialistes,
qu'on appelle des experts.
Et à chaque mot, il n'en réveille que quelques-uns.
Sur 125 milliards de paramètres, il n'y en a que 6 milliards au travail.
C'est ce qui lui permet d'être à la fois très gros et rapide.
Et Strata, c'est le programme qui range tout ça.
La carte garde les experts les plus utilisés, la RAM garde le reste,
et une grosse table reste sur le SSD.
En plus, il est gratuit et open source.

[ LA VITESSE ]

Maintenant, la vitesse.
Pour la mesurer sans les outils au milieu,
je lui ai demandé une petite histoire,
celle d'un dragon qui adore les jeux vidéo.
Presque pas de réflexion, une réponse courte,
et le moniteur affiche 51 tokens par seconde.
Pendant les vrais tests, avec tout le code, c'est même plus rapide, bizarrement.
Près de 70 en moyenne, et selon le test, ça va de 43 à 84.

Pour te donner un repère,
un utilisateur d'une 5070 Ti, avec le même processeur que moi
et à peu près la même RAM,
mesure environ 70 tokens par seconde avec ce modèle.
Lui, il a coupé la réflexion, et il ne vérifie pas si le code marche.
Chez moi, c'est du même ordre,
mais avec la réflexion allumée, et du code qui doit marcher.

Et si ta carte est plus abordable ?
Sur une Radeon de 16 gigas, avec 30 gigas de RAM,
un autre utilisateur mesure environ 37 tokens par seconde,
toujours avec ce modèle.
Moi, j'ai une 5080, une carte haut de gamme,
et sa mémoire est 2 fois plus rapide que celle d'une 5060 Ti.
Donc mes chiffres, c'est plutôt le haut de la fourchette.
Sur ta carte de 16 gigas, ça tourne aussi, juste moins vite.

Et la vitesse baisse quand la conversation grandit.
C'est le projet lui-même qui le publie.
Sur une autre machine, avec un ancien moteur,
le Coder passe de 59 à 43 tokens par seconde
entre 1000 et 128 000 tokens de contexte.
Donc en gros, plus l'agent lit de code, plus il ralentit.
C'est pour ça que j'ai pris Pi :
ses instructions font 1500 tokens, contre 7400 pour OpenCode.
Ça lui fait moins à relire à chaque fois.

[ L'INSTALLATION CHEZ MOI ]

Pour l'installer, Strata a une règle simple :
ta RAM doit contenir les experts, plus une dizaine de gigas pour Windows.
C'est pour ça qu'avec 32 gigas, sa doc ne me propose que le Coder.
Ensuite, il y a une soixantaine de gigas à télécharger.
Chez moi, entre le clic sur Télécharger et mon premier message,
il s'est passé un peu plus d'une demi-heure.

Avant de le lancer, il faut tout fermer, navigateur compris,
parce que pendant qu'il écrit, ma RAM est pleine,
30,8 gigas sur 31.
Et regarde cette case du moniteur, c'est la lecture sur le disque.
Au repos, elle est à zéro.
Dès qu'il écrit, elle monte autour de 200 mégas par seconde.
La RAM est pleine, donc une partie passe par le SSD.

Ensuite, je branche Pi.
L'appli de Strata me donne une adresse,
et je la mets dans le fichier de Pi, avec le nom du modèle.

Au niveau de la réflexion, par contre, c'est un peu plus tricky.
Ce modèle réfléchit longtemps avant d'écrire,
et cette réflexion compte dans la longueur maximale de sa réponse.
Par défaut, Pi lui laisse 16 000 tokens,
et c'est aussi ce que Strata écrirait pour lui chez moi.
Un jeu complet plus la réflexion, ça peut déborder,
et le fichier s'arrête au milieu.
Donc avant le premier test, j'ai monté cette limite à la main, à 32 000.
Le fichier est en description.

[ LES ERREURS ]

Et justement, voilà ma première erreur.
32 000 tokens, ce n'était pas assez.
Une fois, il a été coupé net en plein milieu du site,
7 minutes perdues,
et derrière, il a dû écrire le fichier par morceaux.
Donc si tu le refais, monte encore plus haut.

Le site, lui, ne s'est pas fait du premier coup.
Au premier essai, je lui demande un écran d'accueil qui zoome doucement,
6 destinations, des avis qui défilent tout seuls,
une galerie en plein écran, et le tout doit tenir sur un téléphone.
Il écrit tout en une demi-heure,
mais en anglais, alors que je lui demandais du français.
Et à la fin, il veut se tester tout seul.
Il ouvre un Chrome invisible, et Chrome ne lui rend jamais la main.
Il est resté bloqué presque 2 heures, jusqu'à ce que je l'arrête.

Pour le deuxième essai, j'ai donné mes photos à Claude,
et je lui ai demandé un plan pour ce modèle-là,
avec les étapes, des morceaux de code,
et tous les textes en français déjà écrits.
Le modèle local n'avait plus qu'à le suivre, étape par étape.
Ça a donné le site que tu as vu, en 17 minutes,
avec zéro erreur au contrôle,
même s'il s'est encore bloqué 2 fois sur Chrome.

Il faut quand même savoir qu'un tiers des lignes de la page
étaient déjà dans le plan.
Et le plan a changé la commande :
plus de galerie en plein écran, et les avis ne défilent plus.
À la place, il y a un diaporama dans l'accueil,
et une fiche qui s'ouvre pour chaque destination.

Pour le mini-Minecraft, l'erreur vient de lui.
Au premier essai, il me répond « fichier écrit et vérifié ».
Sauf que le dossier est vide, il n'a rien écrit du tout.
Il a fallu 3 relances,
et à la dernière, il a même trouvé un vrai bug dans son propre code.

Au total, entre tous les blocages sur Chrome,
j'ai passé plus de 2 heures à attendre pour rien.
Et ce n'est pas son code, c'est l'outil :
Pi attendait une réponse que Chrome ne donnait jamais.
Donc dis-lui de ne pas ouvrir de navigateur pour se tester,
et s'il reste bloqué plus de 3 minutes sur une commande, appuie sur Échap.

(Phrase proposée le 14/11 : change-la si ce n'est pas ce qui t'a surpris.)
Mais ce qui m'a le plus surpris,
c'est que personne ne le lui demande,
et pourtant, il écrit ses propres scripts pour tester ses jeux.

[ ET CLAUDE ? ]

Et Claude, dans tout ça ?
Je ne lui ai pas redonné mes prompts mot pour mot,
donc je ne vais pas te faire un faux match.
Je lui ai juste demandé un site de voyage avec mes photos, en une phrase.
Il l'a fait en moins de 2 minutes et demie, en français,
et ça tient la route.
Mon modèle, lui, avait mis une demi-heure, en anglais,
avec une demande bien plus détaillée.

[ CHEZ LES AUTRES ]

Chez moi, le moteur n'a jamais planté pendant les tests.
Chez les autres, ce n'est pas toujours le cas.
Sur GitHub, un ticket encore ouvert décrit le moteur qui plante
avec ce Coder sur certaines longues demandes.
Plusieurs utilisateurs l'ont eu, sur des cartes de 8 et de 12 gigas,
et le message d'erreur accuse la RAM.
Sauf qu'en fait, des utilisateurs ont trouvé la vraie cause :
c'est un bug du moteur.
Un correctif est proposé,
mais il n'est pas encore dans la version que j'ai testée.

Un utilisateur de 5080 rapporte aussi une autre erreur, « non-finite logits »,
avec d'autres fichiers du même modèle.
Et un autre testeur a vu ce Coder rater une tâche de code dans Claude Code,
là où d'autres versions du modèle l'ont réussie.

Il faut dire que Strata est jeune.
Le projet a été créé le 24 septembre,
et il sort une version tous les 2 ou 3 jours.
Donc note bien ta version.
Et si ça casse chez toi, copie le message exact,
parce que c'est comme ça que la cause de ce bug a été trouvée.

[ LE VERDICT, ET CE SOIR ]

Alors, est-ce que ça remplace mon abonnement ?
Pas complètement.
Mais il n'en faut plus qu'un petit.
Avec l'abonnement à 20 dollars par mois, Claude écrit le plan,
et le modèle local l'exécute chez moi, sur ma carte.
C'est exactement ce qui a sauvé le site.
Et même sans plan, il s'en sort bien :
l'île et le casse-briques sans relance, et le mini-Minecraft au bout de 3.

Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Et si tu veux le refaire ce soir, voilà la liste.
1, il te faut une carte de 12 à 16 gigas,
au moins 32 gigas de RAM,
et environ 90 gigas de disque libres.
2, tu installes l'appli Strata, le lien est en description.
Dans sa liste de modèles,
elle te dit si chacun tient sur ton PC avant même de le télécharger.
3, tu prends le Coder, sans les images,
et avant de le lancer, tu fermes tout, navigateur compris.
4, tu branches Pi avec l'adresse que te donne l'appli,
et tu montes la limite de réponse, plus haut que mes 32 000.
Le fichier est en description.
Si tu as plus de RAM, d'après la doc,
à 48 gigas, tu passes aux petites tailles du modèle complet,
et à 64, à toutes.
Et si c'est ta toute première IA en local,
commence plutôt par la vidéo sur LM Studio, je te la mets juste là.

Et jeudi, on cherche comment aller plus vite avec la même carte.
La vidéo arrive juste là.
Allez, salut !
