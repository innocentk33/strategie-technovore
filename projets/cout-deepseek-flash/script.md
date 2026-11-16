# DeepSeek V4 Flash sans carte graphique : les 64 Go valent-ils leur coût ?

Script corrigé du 16/11/2026, publication prévue le 3 décembre. **1529 mots, environ 10:33 à 145 mots/min.** Prix relevés le 16 novembre ; trois exemples de kits de bureau, sans classement du marché. Mesure CPU unique explicitement attribuée.

| Partie | Timecodes calculés |
|---|---|
| Résultat et question | 0:00–0:24 |
| Plan concret | 0:24–0:44 |
| Version, machine et mémoire | 0:44–3:17 |
| Compression et qualité | 3:17–5:03 |
| Dépense existante et kits | 5:03–7:58 |
| API, profils et suite | 7:58–10:33 |

## Voix

Un DeepSeek de 284 milliards de paramètres écrit sans carte graphique, sur 64 gigas de RAM. Une mesure publiée donne environ 9 tokens par seconde. Ces chiffres sont les leurs, je n’ai rien testé chez moi. Sauf que la compression dégrade le modèle. Donc acheter la mémoire pour le faire tourner, est-ce que ça vaut le coût ? [F1,F2]

[VISUEL : fiche du dépôt et tableau de mesure, zéro GPU surligné ; aucun essai personnel.]

On identifie le fichier et sa dégradation mesurée, puis on compare trois exemples de kits de bureau de 64, 96 et 128 gigas en euros et en FCFA. Et on termine par le calcul qui évite de confondre un modèle local et l’API qui porte presque le même nom.

Le fichier mesuré est DeepSeek V4 Flash 0731. Le rapport utilise un Ryzen 9 9955HX avec 64 gigas de DDR5. Donc ce résultat décrit cette machine et ce fichier. L’API actuelle sert une autre version ; cette différence compte aussi pour comparer les dépenses. [F1,F2,F9]

Une même capacité de RAM ne promet pas la même vitesse sur un autre ordinateur. Le processeur et la mémoire travaillent ensemble. Ajouter de la place permet de ranger le fichier ; le temps nécessaire pour le faire travailler dépend encore du reste de la machine.

[VISUEL : ligne matérielle source puis silhouette de portable ; petite étiquette résultat unique.]

En fait, la vitesse citée concerne l’écriture de la réponse. La lecture du prompt, avant cette réponse, a son propre chiffre. Et dans un usage avec un long document, cette attente peut compter autant que le texte qui apparaît ensuite. Donc on garde deux colonnes au tableau. [F2]

Si ton objectif, c’est discuter tranquillement, une génération progressive peut te convenir. Si tu attends qu’un agent relise un dépôt entier et multiplie les actions, le ressenti sera différent. Le mot « tourne » décrit un fonctionnement ; il laisse encore beaucoup de place entre confortable et pénible.

Comment autant de paramètres tiennent en RAM ? Le modèle est un mélange d’experts. Imagine une équipe avec plusieurs spécialistes : chaque morceau de texte mobilise une partie de l’équipe. Les autres spécialistes restent dans le bâtiment, mais ils ne travaillent pas tous sur ce mot. Donc il faut stocker le modèle entier, tout en lisant seulement une partie de ses poids à chaque étape. [F4]

Voilà pourquoi ce résultat CPU mérite qu’on s’y intéresse. Par contre, ça ne permet pas de charger tous les énormes modèles de la même façon. Un modèle dont presque tous les poids participent à chaque mot impose une autre quantité de travail.

[VISUEL : plusieurs groupes d’experts, quelques groupes actifs ; poids présents en RAM, pas disparition des experts.]

Le fichier prend environ 61 gigas décimaux sur le disque. La source l’annonce avec une autre unité, 56,93 gibioctets. Dans les deux cas, on décrit la même taille. Ça compte parce que la marge semble plus grande si on mélange les unités au milieu du calcul. [F1]

Et ce fichier n’est pas le seul occupant de la mémoire. Il reste le système, le logiciel et la conversation. Du coup, 64 gigas, c’est un résultat documenté sur une configuration précise.

Sauf que faire tenir le fichier demande aussi de compresser. Sur une évaluation de perplexité publiée par le projet, le résultat est moins bon que celui de sa référence. Le calcul donne environ 61 % de hausse de perplexité. Ça ne veut pas dire 61 % de réponses fausses, ni 61 % de compétences perdues. [F3]

En fait, la perplexité mesure la surprise du modèle devant une suite de texte. Elle aide à détecter une dégradation. Mais elle ne résume pas à elle seule la fiabilité d’un résumé, la correction d’un programme ou la réussite d’une longue tâche. Donc on ne colle pas une jauge « intelligence restante » sur ce pourcentage.

[VISUEL : deux colonnes de perplexité à la source ; mention mesure statistique, pas taux d’erreurs.]

Du coup, ce qu’on peut en tirer, c’est un avertissement concret : le nom DeepSeek ne garantit pas que ce petit fichier conserve toutes les capacités du modèle de référence. La compression permet le fonctionnement ; elle peut aussi rendre certains usages moins solides. L’achat doit intégrer ce compromis.

En fait, il faut aussi distinguer les améliorations du logiciel et la qualité des poids. Une accélération peut modifier la façon de calculer, une autre peut demander des approximations supplémentaires. Si on mélange les options, on risque d’attribuer à un seul fichier le résultat d’une recette plus compliquée.

Du coup, pour le budget, le premier cas est le plus favorable : ta machine possède déjà la mémoire et une configuration compatible. La dépense immédiate en matériel peut alors être nulle. Ça ne garantit aucune vitesse précise sur ton PC, mais ça change complètement le calcul financier. [F12]


Le budget de départ mérite aussi une distinction. Si tu possèdes déjà assez de mémoire, son ancien prix ne devient pas une nouvelle dépense aujourd’hui. Si tu dois la remplacer, c’est le montant supplémentaire qui compte. Et si l’ordinateur entier doit changer pour accepter ces barrettes, le kit seul ne décrit plus le coût du projet.

Donc le même fichier peut être une bonne occasion pour quelqu’un et un achat peu convaincant pour quelqu’un d’autre. La différence vient de la machine déjà disponible et de la fréquence d’utilisation. Le résultat technique reste intéressant dans les deux cas ; la décision financière, elle, change.

Par contre, le deuxième cas demande une extension de mémoire. On a relevé des références de bureau chez LDLC le 16 novembre 2026. Les prix affichés sont TTC. Ils servent d’exemples actuels, avec la disponibilité indiquée ; ce ne sont pas des minima de tous les marchands. [F5–F7]

Pour 64 gigas, un kit G.Skill Aegis 5 est affiché 1299,95 euros, avec un délai annoncé. Converti au taux de parité, ça représente environ 853000 FCFA. Attention : c’est la conversion du prix français, sans transport ni éventuels frais locaux. [F5,F8]

[VISUEL : tableau 64 Go ; référence exacte ; prix affiché 16/11/2026 ; délai ; conversion explicitement calculée.]

Pour 96 gigas, le kit Corsair retenu est affiché 1723,95 euros, lui aussi avec un délai. Ça donne environ 1131000 FCFA par conversion. Donc le simple fait de passer à une capacité supérieure peut engager une somme importante. [F6,F8]

Pour 128 gigas, la fiche Corsair affiche 2879,95 euros, mais le kit est en rupture. Je te donne le prix affiché et son indisponibilité ensemble. Ça représente environ 1889000 FCFA convertis ; ce n’est pas une commande garantie à ce tarif. [F7,F8]

Donc ces trois kits sont des barrettes pour PC de bureau. Ils ne sont pas la liste de courses du portable qui a produit la mesure. En fait, avant même de regarder le prix, il faut que le format et la capacité soient acceptés par la machine. Sinon le panier le plus impressionnant reste un panier inutile. [F12]

Si cette vidéo t’a évité un mauvais achat, abonne-toi.

Ces trois prix comparent la mémoire achetée. Pour le même fichier, davantage de RAM apporte de la marge. Un autre niveau de qualité demanderait un autre fichier et une évaluation comparable ; cette correspondance n’est pas établie ici. [F11]

[VISUEL : même fichier dans une RAM plus grande ; qualité inchangée.]

Du coup, le vrai tableau a deux décisions : combien de mémoire ton PC peut recevoir, puis quelle version du modèle justifie cette mémoire. L’ordre compte. Si une version plus grosse n’améliore pas l’usage qui t’intéresse, tu peux payer davantage pour une différence que tu ne verras pas.

Mais le service en ligne change encore la comparaison. La documentation de l’API indique que le nom actuel DeepSeek Flash sert V4.1 Flash 1017. Les anciens noms V4 peuvent rediriger vers ce modèle. Du coup, un appel en ligne et notre fichier local ne sont pas une comparaison du même cerveau à deux endroits. [F9]

Un exemple de facturation permet quand même de voir l’ordre du calcul. Pour 1 million de tokens d’entrée sans cache et 1 million de sortie, la grille actuelle donne 0,75 dollar en période creuse et 1,50 dollar en pointe. Ce sont des dollars, hors outils, taxes et change non établis ici. [F9,F10]

[VISUEL : formule entrée+sortie ;USD en évidence ; avertissement modèles différents.]

L’exemple API reste en dollars et porte sur une autre version du modèle. Pour calculer une rentabilité en euros, il manque encore le volume réel, les taxes et le change. Une petite facture peut être plus raisonnable qu’une extension de RAM achetée pour quelques requêtes.

À l’inverse, une machine locale peut répondre à un besoin qui dépasse la facture : travailler avec un modèle disponible sur ton matériel et choisir tes propres fichiers. Là, ton critère peut être l’autonomie. Le calcul financier reste utile, mais il ne remplace pas ce choix.

Donc voilà les profils. Tu as déjà une machine proche de celle documentée et la RAM nécessaire : le résultat CPU est une piste crédible, avec sa compression et sa mesure unique. Tu dois acheter la mémoire seulement pour cet usage : compare le coût supplémentaire à ton volume réel avant d’ajouter une grosse somme au panier.

Tu veux exactement le V4.1 du service actuel, ou une qualité proche du modèle de référence : le résultat 64 gigas ne répond pas directement à cette promesse. Il faut un autre fichier, d’autres mesures et un autre budget. [F1,F9]

[CROCHET : ton avis sur le compromis attente/qualité/autonomie, sans expérience inventée.]

Donc, si la machine est déjà équipée, le résultat CPU ouvre une possibilité intéressante. Si tu dois acheter beaucoup de mémoire, le coût de cette extension doit répondre à un usage réel. Et si tu veux une autre qualité, le choix du fichier vient avant celui du kit.

Lundi 7 décembre, on regarde une autre route : plusieurs cartes graphiques. Ce sera l’occasion de comparer ce que la mémoire permet et ce que la répartition du travail demande au PC.

Allez, salut !

## Notes de production

Utiliser uniquement les pages publiques, tableaux et schémas. Prix au 3 décembre : [PRIX À RELEVER] si actualisation. Ne pas demander d’essai, de capture ni d’ouverture de LM Studio à l’auteur. Le kit 128 Go reste affiché en rupture. Les conversions FCFA sont celles des prix français, hors frais locaux. Aucun fichier non aligné à l’écran.

Le crochet d’avis est facultatif. Limites persistantes : une seule équipe pour la mesure CPU ; pas de score qualité par capacité 96/128 Go ; pas de rentabilité euros à modèle identique.
