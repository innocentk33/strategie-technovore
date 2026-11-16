# DeepSeek sans carte graphique : ce que coûtent vraiment les 64 Go

V1 documentaire 16/11/2026, créneau 3 décembre. Sujet corrigé :V4 Flash 0731. Cible 10–12 min à 145 mots/min. PrixRAMd'exemples marchands, pas minima marché. RéférencesFmuettes.

| Partie | Repère |
|---|---|
| Résultat, coût caché, question |0:00–0:30|
| Quel modèle et quelle machine |0:30–2:20|
| Ce que la compression enlève |2:20–4:20|
|64/96/128 Go : dépenses et limites |4:20–7:15|
| API et décision |7:15–fin|

## Voix

Un DeepSeek de 284 milliards de paramètres écrit sans carte graphique, sur une machine avec 64 gigas de RAM. Une mesure publiée donne environ 9 tokens par seconde. Sauf que le fichier est fortement compressé, et la mémoire peut coûter plus cher que prévu. [F1,F2]

Ces chiffres sont les leurs, je n’ai rien testé chez moi. Alors, acheter de la RAM pour ce modèle, c’est une économie ou une nouvelle dépense ?

[VISUEL : fiche du dépôt et tableau de mesure, zéroGPU surligné ; aucun essai personnel.]

On identifie le fichier exact, on chiffre le compromis de qualité, puis on compare des kits 64,96 et 128 gigas en euros et en FCFA. Et on termine par le calcul qui évite de confondre un modèle local et l’API qui porte presque le même nom.

La réponse qu’on peut déjà donner, c’est oui : le projet publie un résultat CPU sur 64 gigas. Mais le nom exact est DeepSeekV4 Flash 0731. LeV4.1 de la promesse de départ correspond à un autre modèle. Donc le titre doit suivre le fichier qui a produit le résultat, sinon toute la comparaison commence avec la mauvaise étiquette. [F1,F9]

Le test publié utilise un Ryzen 99955 HX, un processeur de portable, avec de laDDR5. On ne peut pas promettre la même vitesse à n’importe quel ordinateur qui possède 64 gigas. Le processeur et la mémoire travaillent ensemble ; ajouter de la capacité ne transforme pas ton vieuxPCen cette machine. [F2]

[VISUEL : ligne matérielle source puis silhouette de portable ; petite étiquette résultat unique.]

La vitesse citée concerne l’écriture de la réponse. La lecture du prompt, avant cette réponse, a son propre chiffre. Et dans un usage avec un long document, cette attente peut compter autant que le texte qui apparaît ensuite. Donc on garde deux colonnes au tableau. [F2]

Si ton objectif, c’est discuter tranquillement, une génération progressive peut te convenir. Si tu attends qu’un agent relise un dépôt entier et multiplie les actions, le ressenti sera différent. Le mot « tourne » décrit un fonctionnement ; il laisse encore beaucoup de place entre confortable et pénible.

Comment autant de paramètres tiennent en RAM ? Le modèle est un mélange d’experts. Imagine une équipe avec plusieurs spécialistes : chaque morceau de texte mobilise une partie de l’équipe. Les autres spécialistes restent dans le bâtiment, mais ils ne travaillent pas tous sur ce mot. Donc il faut stocker le modèle entier, tout en lisant seulement une partie de ses poids à chaque étape. [F4]

Voilà pourquoi ce résultat CPU mérite qu’on s’y intéresse. Par contre, ça ne permet pas de charger tous les énormes modèles de la même façon. Un modèle dont presque tous les poids participent à chaque mot impose une autre quantité de travail.

[VISUEL : plusieurs groupes d’experts, quelques groupes actifs ; poids présents enRAM, pas disparition des experts.]

Le fichier prend environ 61 gigas décimaux sur le disque. La source l’annonce avec une autre unité,56,93 gibioctets. Dans les deux cas, on décrit la même taille. Ça compte parce que la marge semble plus grande si on mélange les unités au milieu du calcul. [F1]

Et ce fichier n’est pas le seul occupant de la mémoire. Il reste le système, le logiciel et la conversation. Du coup,64 gigas, c’est un résultat documenté sur une configuration précise. Ce n’est pas une invitation à remplir la machine puis à espérer que tout passera.

Maintenant, le prix qu’on paie pour compresser. Sur une évaluation de perplexité publiée par le projet, le résultat est moins bon que celui de sa référence. Le calcul donne environ 61%de hausse de perplexité. Ça ne veut pas dire 61%de réponses fausses, ni 61%de compétences perdues. [F3]

La perplexité mesure la surprise du modèle devant une suite de texte. Elle aide à détecter une dégradation. Mais elle ne résume pas à elle seule la fiabilité d’un résumé, la correction d’un programme ou la réussite d’une longue tâche. Donc on ne colle pas une jauge « intelligence restante » sur ce pourcentage.

[VISUEL : deux colonnes de perplexité àla source ; mention mesure statistique, pas taux d’erreurs.]

Ce qu’on peut en tirer, c’est un avertissement concret : le nomDeepSeek ne garantit pas que ce petit fichier conserve toutes les capacités du modèle de référence. La compression permet le fonctionnement ; elle peut aussi rendre certains usages moins solides. L’achat doit intégrer ce compromis.

Il faut aussi distinguer les améliorations du logiciel et la qualité des poids. Une accélération peut modifier la façon de calculer, une autre peut demander des approximations supplémentaires. Si on mélange les options, on risque d’attribuer à un seul fichier le résultat d’une recette plus compliquée.

Du coup, pour le budget, le premier cas est le plus favorable : ta machine possède déjà la mémoire et une configuration compatible. La dépense immédiate en matériel peut alors être nulle. Ça ne garantit aucune vitesse précise sur tonPC, mais ça change complètement le calcul financier. [F12]

Le deuxième cas, c’est une extension de mémoire. On a relevé des références de bureau chezLDLCle 16 novembre 2026. Les prix affichés sont TTC. Ils servent d’exemples actuels, avec la disponibilité indiquée ; ce ne sont pas des minima de tous les marchands. [F5–F7]

Pour 64 gigas, un kitG.SkillAegis 5 est affiché 1299,95 euros, avec un délai annoncé. Converti au taux de parité, ça représente environ 853000 FCFA. Attention : c’est la conversion du prix français, sans transport ni éventuels frais locaux. [F5,F8]

[VISUEL : tableau 64 Go ; référence exacte ; prix affiché 16/11/2026 ; délai ; conversion explicitement calculée.]

Pour 96 gigas, le kitCorsairretenu est affiché 1723,95 euros, lui aussi avec un délai. Ça donne environ 1131000 FCFApar conversion. Donc le simple fait de passer à une capacité supérieure peut engager une somme importante. [F6,F8]

Pour 128 gigas, la ficheCorsairaffiche 2879,95 euros, mais le kit est en rupture. Je te donne le prix affiché et son indisponibilité ensemble. Ça représente environ 1889000 FCFAconvertis ; ce n’est pas une commande garantie à ce tarif. [F7,F8]

Ces trois kits sont des barrettes pourPCde bureau. Ils ne sont pas la liste de courses du portable qui a produit la mesure. En fait, avant même de regarder le prix, il faut que le format et la capacité soient acceptés par la machine. Sinon le panier le plus impressionnant reste un panier inutile. [F12]

Si cette vidéo t’a évité un mauvais achat, abonne-toi.

Mais acheter 96 ou 128 gigas ne rend pas automatiquement le même fichier plus intelligent. Si tu charges exactement les mêmes poids, tu gagnes surtout de la marge. Pour améliorer la qualité conservée, il faut sélectionner un autre fichier, avec sa propre évaluation et ses besoins réels.

[VISUEL : même fichier dans uneRAMplus grande, qualité inchangée ; second fichier plus gros marqué qualitéàvérifier.]

C’est pour ça que je ne colle pas un pourcentage de qualité en face de chaque kit. L’échelle complète qu’on avait comme piste n’a pas été vérifiée avec des fichiers et un protocole suffisamment clairs. Donc 96 gigas n’obtiennent pas magiquement une médailleargent, et 128 une médailleor. [F11]

Le vrai tableau a deux décisions : combien de mémoire tonPCpeut recevoir, puis quelle version du modèle justifie cette mémoire. L’ordre compte. Si une version plus grosse n’améliore pas l’usage qui t’intéresse, tu peux payer davantage pour une différence que tu ne verras pas.

Maintenant, comparons avec le service en ligne. La documentation de l’APIindique que le nom actuelDeepSeekFlashsertV4.1 Flash 1017. Les anciens nomsV4 peuvent rediriger vers ce modèle. Du coup, un appel en ligne et notre fichier local ne sont pas une comparaison du même cerveau à deux endroits. [F9]

Un exemple de facturation permet quand même de voir l’ordre du calcul. Pour 1 million de tokens d’entrée sans cache et 1 million de sortie, la grille actuelle donne 0,75 dollar en période creuse et 1,50 dollar en pointe. Ce sont des dollars, hors outils, taxes et change non établis ici. [F9,F10]

[VISUEL : formule entrée+sortie ;USDen évidence ; avertissement modèlesdifférents.]

Je ne convertis pas ce montant en euros en douce pour annoncer un nombre d’années de rentabilité. Il faudrait connaître ton usage, les conditions de facturation, le change et ce que tu compares exactement. Une petite factureAPIpeut aussi être plus raisonnable qu’une extension deRAMachetée pour quelques requêtes.

Àl’inverse, une machine locale peut répondre à un besoin qui dépasse la facture : travailler avec un modèle disponible sur ton matériel et choisir tes propres fichiers. Là, ton critère peut être l’autonomie. Le calcul financier reste utile, mais il ne remplace pas ce choix.

Donc voilà les profils. Tu as déjà une machine proche de celle documentée et laRAMnécessaire : le résultatCPUest une piste crédible, avec sa compression et sa mesure unique. Tu dois acheter la mémoire seulement pour cet usage : compare le coût supplémentaire à ton volume réel avant d’ajouter une grosse somme au panier.

Tu veux exactement leV4.1 du service actuel, ou une qualité proche du modèle de référence : le résultat 64 gigas ne répond pas directement à cette promesse. Il faut un autre fichier, d’autres mesures et un autre budget. [F1,F9]

[CROCHET : ton avis sur le compromis attente/qualité/autonomie, sans expérience inventée.]

La bonne surprise, c’est qu’une carte graphique n’est pas obligatoire pour ce résultat précis. Le piège, c’est d’en déduire que la machine, le fichier et la qualité sont devenus gratuits. Pour choisir la suite, garde séparés le prix de laRAM, la taille des poids et l’usage que tu veux réussir.

Allez, salut !

## Notes de production

Schémas et relevés publics uniquement. Les prix 3 décembre sont[PRIX À RELEVER]si besoin d’actualité ; aucune demande de testàl’auteur. Risques :nouvelleversionnom, prixdisponibilité, PPLmalinterprétée. Mesures uniques signalées. Avis facultatif ; aucune anecdotepersonnelle. Pas de modèleuncensored affiché.
