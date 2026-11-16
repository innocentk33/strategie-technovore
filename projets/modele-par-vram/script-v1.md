# De 4 à 16 Go : un modèle utile pour la carte que tu as déjà

V1 documentaire du 16/11/2026, créneau provisoire 18/01/2027. Cible 12–14 min à 145 mots/min. Candidats par usage, limites et mesures publiées ; aucun essai auteur.

| Partie | Repère |
|---|---|
| Résultat et question |0:00–0:30|
|4 Go : petit fichier, vrai usage |0:30–3:00|
|6 et 8 Go : modèle ou conversation |3:00–6:15|
|12 Go : le spécialiste du code |6:15–8:45|
|16 Go : plus grand, sous conditions |8:45–11:00|
|Verdict |11:00–fin|

## Voix

Sur une carte de 4 gigas, un utilisateur publie 96 tokens par seconde avec un petit Qwen en 4 bits. Sur la même machine, le modèle plus gros déborde et ralentit. Donc ta petite carte peut encore servir, si le fichier correspond à sa mémoire. [F2]

Ces chiffres sont les leurs, je n’ai rien testé chez moi. Alors, quel modèle choisir avec les gigas que tu possèdes déjà ?

[VISUEL : source publique 4 Go, mesure unique, Qwen 2 B4 bits, contexte 4 K.]

On garde un candidat pour 4,6,8,12 et 16 gigas, sa taille de fichier et un usage concret. On regarde aussi les vitesses publiées et ce qu’elles ne permettent pas de promettre. Et à la fin, tu sauras quand garder un petit modèle plutôt que forcer un gros à rentrer.

Avec 4 gigas, le premier candidat est Qwen 3.5-2 B en Q4_K_M. Son fichier de poids fait 1,28 giga. Donc il laisse davantage de place que les modèles plus encombrants. Ce chiffre ne comprend pas à lui seul la conversation, le logiciel et toutes les fonctions de vision. [F1]

Le résultat du début vient d’un portable avec une RTX 3050 Ti de 4 gigas,32 gigas de RAM et Ubuntu. L’utilisateur mesure une génération chaude, après chargement, avec Ollama, sur un contexte de 4096 tokens. La valeur est la médiane de trois passages. C’est une mesure publiée sur cette machine, avec ce modèle. [F2]

[VISUEL : poids 1,28 Go d’un côté ;mémoirechargée≈2,4 Go source de l’autre ;unités/réglagesdistingués.]

En fait, les deux nombres n’ont pas le même rôle. La taille du téléchargement t’aide à choisir le fichier. L’occupation pendant le fonctionnement t’aide à comprendre ce qui reste dans la carte. Les poids ne sont pas seuls au bureau.

L’usage réaliste pour ce palier, c’est une petite demande bien cadrée : reformuler un message, expliquer un paragraphe, proposer un brouillon court. Le modèle peut répondre vite et se tromper quand même. Donc le débit ne remplace pas la vérification du contenu.

Le même utilisateur montre aussi ce qui se passe quand il monte en taille : son 4 B atteint 25 tokens par seconde, avec une partie du travail passée au processeur. Ce n’est pas un duel de qualité, mais une limite matérielle visible. Le plus gros modèle peut demander plus d’attente sans rendre le même service. [F2]

Du coup, le bon choix sur 4 gigas est souvent celui qui garde une marge. Si un autre programme occupe déjà la mémoire, le modèle dispose de moins de place. Et si tu ajoutes des documents ou des fonctions de vision, le besoin augmente encore.

[VISUEL : jauge 4 Go, petite marge, fenêtre etprojecteur séparés.]

Avec 6 gigas, on peut regarder Qwen 3.5-4 B en Q4_K_M. Le fichier pèse 2,74 gigas. C’est un candidat pour un assistant un peu plus ambitieux, tout en conservant de la place pour le reste du fonctionnement. La marge réelle doit être évaluée avec le contexte choisi. [F3]

Une publication sur une RTX 4050 de portable avec 6 gigas donne environ 50 tokens par seconde sur un Qwen 4 B, selon la longueur du contexte. Mais le format exact n’est pas identifié dans la ligne de résultats. Donc cette mesure décrit la configuration publiée ; elle ne devient pas une vitesse promise pour notre fichier. [F4]

Par contre, elle rappelle une chose utile : la conversation peut changer le débit. La même famille de modèle n’affiche pas forcément la même vitesse au début et après plusieurs échanges. On garde donc le contexte à côté du nombre de tokens.

Pour quelqu’un qui résume de petits textes, cette marge peut être plus importante que de gagner encore des paramètres. Un modèle qui reste à l’aise dans la carte est un meilleur point de départ qu’un téléchargement choisi uniquement parce qu’il est plus gros.

[VISUEL : palier 6 Go, Qwen 4 B2,74 Go ;vitesse source séparée etformatnonidentifié.]

Il faut aussi savoir quel fichier on compare. Le nom Qwen 4 Bpeut désigner plusieurs compressions. Une version 8 bits et une version 4 bits n’occupent pas la même place. Du coup, « j’ai le même modèle » ne suffit pas pour expliquer deux résultats différents.

Et une application peut proposer plusieurs versions presque côte àcôte. La bonne ligne contient le modèle, la compression et le nom du fichier. Une fois ces trois informations identifiées, le conseil devient beaucoup plus concret.

Avec 8 gigas, le candidat suivant est Qwen 3.5-9 B en Q4_K_M. Le fichier de poids est affiché 5,68 gigas. Donc la question devient plus serrée : combien reste-t-il pour la conversation, le bureau et les allocations du logiciel ? [F5]

Une source publie son propre banc d’essai sur une RTX 4060 de 8 gigas, avec 32 gigas de RAM. En génération courte, elle obtient 45,6 tokens par seconde. Avec 16000 tokens déjà présents dans le contexte, elle relève 41,6. Le modèle reste en 4 bits, avec le moteur llama.cpp et l’accélération CUDA. [F6]

[VISUEL : profondeur 0→16 K, génération 45,6→41,6 ;préremplissagedansuneautrecolonne.]

Ces deux valeurs viennent d’une même équipe et ne constituent pas deux reproductions indépendantes. Mais elles montrent un effet concret : le débit du début n’est pas automatiquement celui d’une conversation remplie. La lecture du prompt est encore une autre colonne ; elle ne doit pas être confondue avec l’écriture de la réponse. [F6]

En fait, c’est un palier intéressant pour expliquer des textes et garder un assistant généraliste. On monte en capacité de modèle, avec un fichier encore assez petit pour laisser une partie de la carte disponible. Mais le nombre de milliards ne garantit pas qu’il remplacera un service très puissant sur toutes les questions.

Si tu possèdes déjà une carte de 8 gigas, le premier achat à éviter, c’est parfois une carte neuve alors que le bon fichier répond à ton besoin. Une nouvelle référence peut rendre le travail plus rapide, mais il faut savoir quelle limite on cherche à résoudre.

Le Qwen 27 Btrèscompressé peut aussi attirer sur ce palier. On l’a traité à part, avec son prix en qualité et en mémoire de conversation. Ici, le 9 B sert de candidat plus modeste ; on ne transforme pas la petite carte en terrain de records à chaque demande.

[VISUEL : grosmodèlecompressé à côté du 9 B ;objectifusageplutôtquerecord.]

Avec 12 gigas, le candidat choisi change aussi d’usage. Qwen 2.5-Coder-14 B en Q4_K_M est spécialisé dans le code. Son fichier est affiché 8,99 gigas. Donc il reste une marge à partager entre le contexte et le fonctionnement du moteur. [F7]

Une mesure publiée sur une RTX 3060 de 12 gigas obtient environ 35 tokens par seconde, avec Ollama sous Windows, un cache 8 bits et un contexte de 16000 tokens. La publication date du 28 août 2026. Elle décrit ce matériel et ces conditions. [F8]

Une autre équipe publie 28,5 tokens par seconde sur le même nom de modèle et une 3060 de 12 gigas. Son protocole utilise un petit prompt et des réponses plafonnées à 200 tokens. Donc les deux résultats montrent un fonctionnement concret, mais ils ne donnent pas une vitesse identique à garantir. [F9]

[VISUEL : deuxmesures séparées 35 et 28,5 ;dates/protocoles ;aucunemoyennetrompeuse.]

Pour ce palier, l’usage proposé est donc l’aide sur du code : comprendre une fonction, rédiger un morceau bien délimité ou expliquer une erreur. Le fait qu’un modèle écrive vite ne signifie pas qu’il réussira seul une longue opération dans un dépôt entier.

La différence est facile à imaginer. Une fonction courte arrive presque entièrement dans la conversation. Un projet ajoute d’autres fichiers, des dépendances et des résultats d’outils. Du coup, la taille du contexte devient une contrainte à part entière.

Et tu peux choisir un modèle plus petit sur une carte de 12 gigas. Rien n’oblige à remplir le compteur. Si le 9 B fait ce que tu veux et laisse davantage de place aux documents, cette liberté peut valoir plus qu’un modèle plus gros avec un contexte serré.

Le passage de 8 à 12 gigas ne doit donc pas être compris comme une obligation de monter en paramètres. Il donne des options : compression moins forte, conversation plus longue, ou modèle plus encombrant. Le bon choix suit la tâche.

[VISUEL : troisusagesdelamarge, poids/qualité/conversation, sanschiffreestimé.]

Avec 16 gigas, on peut aborder Qwen 3.8-27 B en UD-IQ4_XS. Le fichier actuel tourne autour de 14,4 gigas. C’est un gros candidat, avec une marge plus étroite. Donc le contexte et les fonctions supplémentaires demandent une attention particulière. [F10]

Dans une mesure publiée sur une 5060 Ti 16 gigas, le modèle écrit 28 tokens par seconde avec un contexte de 8192 tokens et un cache 8 bits. On garde cette vitesse sans l’accélération qui, dans la même publication, utilise une deuxième carte pour le brouillon. [F10]

Par contre, le chiffre du fichier actuel et la mesure d’octobre ne sont pas un nouveau test de la version publiée aujourd’hui. Le conseil repose sur une famille de fichiers et des conditions documentées. Les mises àjour peuvent déplacer légèrement la taille et les besoins.

[VISUEL : palier 16 Go, fichier 14,4 Go, contexte 8 Ksource ;mentionmesureuniqueoctobre.]

Ce palier peut donc convenir à quelqu’un qui veut un modèle plus grand pour expliquer, écrire et travailler sur des tâches courtes. Mais si tu attends beaucoup de mémoire de conversation, un modèle plus petit peut encore être un meilleur compagnon.

Il reste la RAM du PC. Les machines publiées dans certains exemples possèdent 32 gigas. Ça décrit leur configuration ; ça ne démontre pas un minimum universel pour chaque palier. Et une partie du modèle gardée en RAM ne transforme pas cette mémoire en VRAM rapide. [F11]

Donc la bonne fiche contient trois lignes : capacité de la carte, mémoire du PC et fichier exact. Si on retire une de ces lignes, la promesse devient floue. Une démonstration sur un énorme modèle partiellement en RAM peut être intéressante, avec un compromis très différent d’un petit modèle entièrement sur la carte.

Pour les prix et les cartes disponibles en Afrique, le comparatif par budget donne la méthode d’achat et les limites des relevés. Ici, on part du matériel déjà présent. Aucun prix de janvier ni aucune disponibilité locale ne sont inventés. [F12]

Le verdict tient en cinq candidats, pas en cinq obligations.4 gigas : petit Qwen 2 B pour les demandes courtes.6 gigas :Qwen 4 Bavec davantage de marge.8 gigas :Qwen 9 B pour un assistant généraliste.12 gigas :Coder 14 B pour des tâches de code cadrées.16 gigas :Qwen 27 Bcompressé, avec un contexte choisi en connaissance de cause. [F1–F10]

[CROCHET : ton avis sur le compromis petit modèle rapide ou gros modèle plus lent, sans résultat personnel inventé.]

Et si deux fichiers semblent équivalents, regarde aussi le moteur qui les fait tourner. Le 25 janvier, on compare Ollama, LM Studio et llama.cpp pour choisir selon ton usage et ton PC.

Allez, salut !

## Notes

Aucun essai, aucune capture ni commande à exécuter demandés. Prix cartes :[PRIX À RELEVER] seulement si besoin d’un encart d’achat. Visuels documentaires. Risques : mesures uniques, quantification 6 Go non identifiée, capacité théorique prise comme garantie. Aucun modèle non aligné affiché.
