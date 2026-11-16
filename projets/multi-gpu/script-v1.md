# Deux cartes pour ton IA : les points à vérifier avant l'achat

V1 documentaire · 7 décembre 2026 · cible10–12min,145mots/minute. Sources publiques du16/11. Aucune installation,mesure ou capture demandée à l'auteur.

| Partie | Repère |
|---|---|
| Deux cartes, réponse plus lente | 0:00 |
| Ce que la seconde carte doit résoudre | 0:30 |
| Les deux répartitions | 2:00 |
| Ports, câbles et place | 4:00 |
| Deux marques et logiciels | 6:30 |
| La facture complète et verdict | 8:30 |

## Voix

[VISUEL : graphique original36,05→34,03→47,06, légendé «une mesure publiée, Qwen27B, deux7900XTX,13/09/2026». F1.]

Une carte écrit à 36 tokens par seconde. Le même testeur en ajoute une deuxième : il tombe à 34. Puis il change la répartition, et monte à 47. Ces chiffres sont les leurs, je n'ai rien testé chez moi. Donc, avant de payer ta deuxième carte, qu'est-ce qui décide si elle t'aide vraiment ?

On va identifier la mémoire qui te manque, distinguer les deux répartitions, puis regarder les ports, les câbles et la place dans la tour. À la fin, tu auras une décision selon ton PC : ajouter, remplacer, ou garder ton argent. Le piège, c'est qu'un deuxième port long peut cacher une liaison beaucoup plus étroite.

[GRAPHIC] [VISUEL : trois cartes «manque de mémoire»,«réponse lente»,«plusieurs utilisateurs». F4/F6.]

Si ton modèle déborde en RAM, la seconde carte peut lui donner de la place sur les GPU. Si tout tient déjà, tu cherches surtout une meilleure vitesse. Et si plusieurs personnes utilisent ta machine, le débit total pose encore une autre question. Du coup, la bonne carte dépend du problème que tu essaies de résoudre.

Prends le premier cas. Ton modèle fait une partie du travail avec la RAM de ton PC, parce que la carte est pleine. Ajouter une carte peut garder davantage de poids en mémoire graphique. Donc tu peux gagner de la capacité et de la vitesse en même temps. Ça paraît évident, mais c'est précisément ce qu'un slogan trop court sur le multi-GPU peut faire oublier.

Un rapport indépendant le montre avec une paire NVIDIA de capacités différentes. Sur le même Qwen en 4 bits, le testeur passe d'environ 11 à 12 tokens par seconde à environ 21, en répartition par couches. Le modèle débordait auparavant en RAM. C'est une mesure publiée sur sa machine, avec son contexte ; on ne transforme pas ce gain en promesse pour ta paire.

Par contre, quand le fichier tient déjà entièrement sur une carte, on ne supprime plus cette attente-là. Il faut alors regarder ce que la deuxième fait réellement pendant la réponse. Les deux situations peuvent donner des résultats opposés sans que personne ait truqué le benchmark.

Donc, avant la marque et le prix, écris ton manque en une phrase. «Je veux garder une conversation plus longue.» Ou «je veux une copie moins compressée.» Ou encore «je veux réduire mon attente avec le fichier actuel». Cette phrase évite de payer pour une capacité qui ne répond pas à ton besoin.

[VISUEL : modèle découpé en deux piles ;une flèche traverse les deux. F4/F5.]

Dans llama.cpp, la répartition par couches est le mode par défaut. Chaque carte garde sa tranche du modèle et le cache associé. Pour une conversation, le calcul passe successivement par ces tranches. C'est un peu comme un colis qui traverse deux ateliers : avoir deux ateliers donne de la place, mais le même colis doit encore faire le trajet.

Le mode tensor partage les calculs à l'intérieur des couches. Les cartes travaillent davantage ensemble, et elles doivent aussi se transmettre des résultats plus souvent. Donc la liaison entre elles compte davantage. La documentation le marque encore expérimental : modèle, moteur et version peuvent limiter ce qui fonctionne.

C'est ce qui explique notre premier graphique. Sur deux Radeon, un testeur obtient environ 36 tokens par seconde avec une carte, 34 en couches, puis 47 en tensor. Il utilise Qwen 27B, llama.cpp, et des ports PCIe 4 avec huit lignes chacun. On parle ici de génération. La lecture du prompt est une autre mesure, et certaines de ses séries sont trop variables pour qu'on leur fasse raconter la même histoire.

Une deuxième expérience, sur une paire NVIDIA différente, trouve aussi un gain en changeant de mode. Mais le facteur change. Donc on retient qu'une répartition peut améliorer la réponse ; le chiffre exact reste attaché à la machine qui l'a produit. Personne ne gagne un multiplicateur universel en branchant un câble.

Si cette vidéo t'a évité un mauvais achat, abonne-toi.

Et pour deux cartes de 16 gigas, oui, les capacités physiques s'additionnent. Sauf qu'une partie sert aux tampons, au cache de conversation et parfois à l'affichage. Il faut de la marge sur les cartes concernées. On ne peut donc pas promettre un bloc de 32 gigas entièrement libre pour les seuls poids.

[GRAPHIC] [VISUEL : port long,étiquette «formatx16»,puis schéma «liaisonx4». F9.]

Le manuel de la carte mère peut te faire économiser davantage qu'une promotion. Le connecteur a une longueur physique. Les lignes actives sont la liaison réelle. Un port long peut donc fonctionner avec moins de lignes que le premier, ou partager ses ressources avec d'autres éléments.

Dans l'exemple documenté du dossier, le premier port est relié au processeur. Le second passe par le chipset et fonctionne en PCIe 3 avec quatre lignes. Donc deux connecteurs qui se ressemblent peuvent offrir des chemins différents. Ce renseignement doit venir du manuel de la référence précise.

Attention aussi à la génération. «Quatre lignes» ne décrit pas le même débit théorique à toutes les générations PCIe. Et la vitesse finalement obtenue dépend du mode de répartition, des échanges et des cartes. C'est pour ça qu'on ne colle pas une pénalité fixe à tous les ports x4.

Imagine un jeu coopératif où deux joueurs doivent s'envoyer un message après chaque mouvement. Si la liaison prend du temps, la puissance de leurs machines ne règle pas tout. Un autre jeu demande seulement de transmettre le relais à certains moments : le même réseau peut alors être moins gênant. C'est l'idée à garder pour comprendre pourquoi les modes ne réagissent pas pareil.

Du coup, un port étroit peut rester utile pour ajouter de la capacité, sans devenir la bonne base pour chercher l'accélération maximale. Et remplacer la carte mère pour obtenir une meilleure liaison change le prix de ton projet. Il faut le compter avant de dire que la seconde carte est une affaire.

[VISUEL : silhouettes à l'échelle des cartes et du boîtier, puis connecteurs dessinés. F9.]

La place se vérifie dans toutes les directions. La longueur de la carte, son épaisseur, l'espace sous le dernier port et la proximité des ventilateurs. Si le radiateur d'une carte bloque l'entrée d'air de l'autre, elles ne bénéficient pas du même environnement que dans une machine de benchmark ouverte.

L'alimentation demande la même précision. Son nombre de watts ne raconte pas tous les câbles disponibles. Les modèles partenaires d'une même famille peuvent demander des prises différentes. Donc on regarde la référence exacte de la carte, celle du bloc, et la documentation du fabricant.

Pas besoin de transformer cette étape en séance de bricolage. Une feuille suffit : dimensions, ports utilisables, câbles compatibles et marge d'alimentation. Si une ligne reste inconnue, elle entre dans le coût à vérifier. Acheter d'abord et improviser ensuite, c'est une façon particulièrement chère de découvrir le manuel.

[VISUEL : cartesNVIDIA/AMD,icônes desmoteurs ;aucune capture de logiciel personnel. F6–F8.]

Deux marques différentes peuvent participer à certains montages avec un moteur adapté. Le support multi-GPU de Vulkan existe, et des projets explorent aussi les assemblages de moteurs. Par contre, cela ne garantit pas la même compatibilité ni les mêmes performances pour chaque carte et chaque modèle.

Donc une vieille carte qui traîne dans un tiroir peut être intéressante. Elle mérite d'abord une vérification des pilotes et du moteur utilisable. Son prix d'achat est déjà payé, mais le temps de configuration et ses contraintes restent devant toi. Et si elle impose une autre version du logiciel, c'est encore un élément du choix.

Dans Ollama, la documentation dit que le modèle est chargé sur une seule carte s'il y tient entièrement. Sinon, il peut être réparti. Du coup, voir une deuxième carte peu occupée n'est pas automatiquement un défaut. Le logiciel a pu choisir la route qui limite les transferts.

LM Studio propose aussi des contrôles pour sélectionner des cartes et gérer leur priorité d'allocation. Les fonctionnalités dépendent du moteur et de la version ; le billet qui les présente ne prouve pas que chaque option existe pour chaque marque aujourd'hui. Et priorité d'allocation ne veut pas dire que tu viens d'activer le mode tensor.

La documentation actuelle de llama.cpp ajoute une réserve utile : le tensor a ses propres restrictions, notamment sur le cache et les architectures. Donc une commande trouvée dans un rapport plus ancien peut employer un comportement différent. Pour une décision d'achat, il faut une preuve sur le couple que tu envisages, pas une ligne magique sortie de son contexte.

[VISUEL : facture en quatre cases«carte»,«boîtier»,«alimentation»,«carte mère».]

Voilà la vraie addition. La seconde carte, puis les changements nécessaires pour qu'elle fonctionne correctement. Si tu dois changer le bloc, le boîtier et la carte mère, compare le total avec une carte unique de capacité suffisante. Les prix exacts sont dans le dossier des routes vers 32 gigas ; les offres bougent, les ruptures comptent.

Si tu as déjà les ports, la place et les câbles, ajouter peut être cohérent pour garder un modèle en VRAM. Si tu cherches seulement à accélérer un fichier déjà à l'aise, exige une mesure publiée sur une configuration proche. Et si tu pars de zéro avec un budget serré, la simplicité d'une seule carte a aussi une valeur.

Enfin, garde le contexte voulu dans la comparaison. Une réponse courte et un agent qui relit un gros dépôt n'ont pas la même pression mémoire. Une machine plus rapide à conversation vide peut demander un compromis une fois remplie. Donc le bon benchmark donne le fichier, le contexte, le moteur, la génération et la lecture du prompt séparément.

[CROCHET :ton avis sur le niveau de bricolage que tu accepterais,facultatif.]

Avant l'achat, ta décision tient sur quatre lignes : ce qui manque, ce que les ports permettent, ce que le boîtier accepte et ce que le moteur sait faire. Si les quatre sont cohérentes, la deuxième carte peut rendre service. Sinon, le giga le moins cher du tableau risque de devenir le plus encombrant de ton bureau. Allez, salut !

## Hors voix

Visuels : schémasoriginaux et pagesdes sourcesuniquement. Risques : expliquerlayer/tensor avec uneanimation avant les noms ;sortir immédiatement du tableau aprèsdeuxmesures ;la checklist clôt sans tutoriel ni essai demandé. Aucune vitessen'est attribuée à l'auteur. Dates et réserves restent à l'écran. Les référencesF1–F10 correspondent auxfaitsdu fichier sources.md.
