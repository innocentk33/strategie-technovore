# Combien coûte Claude en local ? : brouillon v1

**Titre visé** : *Combien coûte Claude Opus 5.5 en local ? (j'ai fait le calcul)*

**Durée** : environ 1 940 mots de voix off (hors `[VISUEL]`, `⟦…⟧`, `⚠️` et renvois `[S…]`), soit environ 13 min 20 à 145 mots/min (ton débit mesuré sur ArtCraft, pauses comprises). Les minutages sont à recaler sur la vraie prise.

**Format** : calculé (`strategie.md`, pilier 2). Rien n'a tourné sur la 5080 : les résultats de tes essais sont des `⟦à écrire⟧` et tout ce qui la concerne reste au conditionnel. Chaque chiffre est daté et sourcé dans [`sources.md`](sources.md) ; le numéro entre crochets (`[S5]`) renvoie à ce fichier. Les `[S…]` et les `⚠️` ne se lisent pas.

**Le fil du calcul** : un seul modèle de référence, DeepSeek V4.1 Flash, passé dans quatre machines, de la moins chère à la plus chère. Les trois nombres qui reviennent : **552 milliards** de paramètres, **16 milliards** actifs par token, **163 ou 316 Go** à garder en mémoire.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = ce qui s'affiche (les calculs sont posés pas à pas). `(…)` = indication de ton. `⟦à écrire : …⟧` = à remplir par toi. `⚠️ à vérifier` = point non confirmé, détaillé dans `sources.md`. Nombres en lettres dans la voix off ; les chiffres sont dans les `[VISUEL]`.

**Chapitres (YouTube)** :

| Minutage estimé | Chapitre |
|---|---|
| 0:00 | Le prix |
| 0:35 | La vraie question |
| 1:15 | On ne peut pas calculer Claude |
| 3:15 | Le calcul de mémoire |
| 5:20 | Du moins cher au plus cher |
| 9:40 | La facture d'électricité |
| 10:30 | Le retournement |
| 11:50 | Le verdict selon ton profil |

---

## 0. Le prix (0:00 – 0:35) · objectif : les 15 premières secondes sont les plus fortes

[VISUEL : l'image de la miniature : la RTX 5080 minuscule au pied d'une baie de serveurs géante. Sur la baie, un compteur s'allume : « 30 660 € / mois ». Pas de titre, pas de logo, pas de présentation.]
[SON : un « tic » sec quand le compteur s'allume, puis silence.]

Trente mille six cent soixante euros. Par mois.

C'est ce que coûte, d'après mon calcul, le plus petit serveur que j'ai trouvé en Europe pour faire tourner, en version officielle, un modèle de la trempe de Claude.

[VISUEL : zoom sur la 5080 ; une jauge de mémoire à côté : « 16 Go ». À côté, la barre du modèle : « 163 à 500 Go ».]

Ma RTX 5080 a seize gigas de mémoire. Le modèle que je vais calculer en pèse entre cent soixante et cinq cents, selon la version. C'est un Rattata qui défie Mewtwo.

(sec, sans sourire)

Je n'ai pas cette machine. Alors j'ai fait le calcul. Chaque chiffre est à l'écran, avec sa source en description.

---

## 1. La vraie question (0:35 – 1:15)

Tu as sûrement vu passer ces vidéos qui disent qu'on peut remplacer Claude par une IA qui tourne chez soi. Plus d'abonnement, tes données qui restent à la maison, le grand soir.

Alors j'ai regardé ce que répondent ceux qui s'y connaissent, quand quelqu'un pose la question pour de vrai.

⟦à écrire : une vraie question trouvée sur Reddit (r/LocalLLaMA) ou sur X, du genre « quelle machine pour faire tourner un modèle niveau Claude chez soi ? ». Recopier la question et trois réponses réelles qui se contredisent, avec le lien en description. Ne pas les reformuler de mémoire.⟧

[VISUEL : trois captures de vraies réponses, pseudos floutés, qui s'affichent l'une après l'autre. Elles se contredisent : un chiffre en face de chaque.]

Trois réponses, trois ordres de grandeur.

⟦à écrire : une phrase sur ce qui manque à ces réponses (le calcul ? la source ?), à confirmer sur les vraies captures avant de la dire.⟧

Ici, tout sera posé à l'écran.

On va du moins cher au plus cher : ma carte, un Mac, un serveur, puis encore plus gros. Et à la fin, je te dis ce qui tient vraiment chez moi. Ce n'est probablement pas ce que tu crois.

---

## 2. On ne peut pas calculer Claude (1:15 – 3:15)

Première règle : on ne peut pas faire ce calcul avec Claude.

Anthropic ne publie ni sa taille ni ses poids. J'ai ouvert la page des modèles et celle d'Opus 5.5, sorti le vingt-deux septembre : prix, contexte, dates de retrait. Pas un seul nombre de paramètres. [S1] [S2]

[VISUEL : capture de la page d'Opus 5.5, avec un surlignage qui balaie chaque ligne ; au bout, un point d'interrogation à la place de « paramètres ».]

Sans taille, pas de calcul. Alors on prend un modèle ouvert, dont les fichiers sont publics, et dont l'éditeur dit qu'il joue dans la même cour.

Mon choix : DeepSeek V4.1 Flash, sorti le dix septembre, licence MIT. Cinq cent cinquante-deux milliards de paramètres. [S3]

[VISUEL : « 552 000 000 000 » en gros, puis le chiffre se range dans une grille de petites cases.]

Ça fait énorme, mais c'est un modèle à experts : trois cent quatre-vingt-quatre spécialistes, dont six seulement sont consultés pour chaque token, un morceau de mot. Résultat : environ seize milliards de paramètres au travail par token, à l'écriture.

[VISUEL : 384 points ; à chaque « tic », six s'allument, les autres restent éteints. Légende : « 16 milliards actifs / token (génération) ».]

Un boss de Monster Hunter : une carcasse énorme, mais à chaque instant, une seule patte bouge.

Pourquoi lui ? Parce que sa fiche officielle le compare à Opus 5, la version d'avant, et pas à un vieux modèle choisi pour faire joli. Voilà le tableau.

[VISUEL : tableau à quatre lignes, DeepSeek contre Opus 5. Terminal-Bench 2.1 : 90,6 contre 89,1. DeepSWE : 74,2 contre 74,0. Terminal-Bench 4.0 : 31,2 contre 51,8. Humanity's Last Exam : 36,8 contre 56,3. Les deux premières lignes en vert, les deux dernières en rouge.] [S3]

Regarde les deux premières lignes : il fait jeu égal, il passe même devant. Regarde les deux dernières : sur les tests les plus durs, il décroche, et pas de peu.

Donc « au niveau de Claude », c'est vrai sur certains tests et faux sur d'autres.

Deux réserves. Ces chiffres viennent de DeepSeek lui-même, et ils visent Opus 5, pas Opus 5.5, sorti après. DeepSeek a aussi publié le dix-sept octobre une mise à jour, la « 1017 », avec de meilleurs scores et la même taille. Le calcul vaut pour les deux. [S3] [S4]

⚠️ à vérifier : les chiffres de l'architecture (experts, paramètres actifs) viennent de la fiche V4.1 Flash d'origine. La fiche de la « 1017 » ne les redonne pas.

**Abonnement (≈ 3:10, 25 %, juste après la première révélation)**

Je te parle de te désabonner de quelque chose, et je te demande de t'abonner à autre chose. Celui-là est gratuit : ton budget d'abonnements respire.

[VISUEL : bouton « S'abonner » animé, 3 secondes, le tableau reste à l'écran.]

---

## 3. Le calcul de mémoire (3:15 – 5:20)

Une IA, c'est un fichier rempli de nombres. Sur seize bits, un nombre prend deux octets. Sur huit bits, un. Sur quatre bits, un demi.

[VISUEL : calcul posé ligne par ligne, chaque ligne apparaît quand elle est dite.
552 milliards × 2 octets = 1 104 Go (16 bits)
552 milliards × 1 octet = 552 Go (8 bits)
552 milliards × 0,5 octet = 276 Go (4 bits)]

Réduire les bits, ça s'appelle la quantification. C'est le JPEG de l'IA : tu écrases les détails, ça pèse moins lourd, et tu perds un peu de qualité.

Je vérifie la formule sur de vrais fichiers, ceux d'un développeur de la communauté qui fait tourner ce modèle sur Mac.

La version « Q4 » : trois cent seize gigas pour le cœur du modèle. Je divise par cinq cent cinquante-deux milliards, je multiplie par huit : quatre bits et demi par paramètre. La formule tient. La « Q2 » : cent soixante-trois gigas, deux bits et quatre dixièmes. [S5]

[VISUEL : 316 × 8 ÷ 552 = 4,6 bits ; 163 × 8 ÷ 552 = 2,4 bits. Deux barres : « Q4 : 316 Go », « Q2 : 163 Go ».]

Alors pourquoi le fichier officiel pèse-t-il cinq cent dix gigas ? [S3]

Parce que le modèle emporte une deuxième pièce, Engram : cent quatre-vingt-seize milliards de paramètres qui servent de dictionnaire. Le projet sur Mac les laisse sur le SSD et ne lit que la page dont il a besoin : environ deux cents gigas qui n'entrent jamais en mémoire vive. [S3] [S5]

[VISUEL : un bureau et une bibliothèque. Le cœur du modèle sur le bureau (« mémoire rapide »), le dictionnaire Engram sur l'étagère (« SSD »).]

⚠️ à vérifier : 552 plus 196 ne font pas 763, le total affiché par Hugging Face. L'écart d'une quinzaine de milliards n'est pas expliqué sur la fiche (vision ?).

Reste le cache, la mémoire de la conversation. Ici, DeepSeek annonce environ huit cent quatre-vingt-dix octets par token. Un million de tokens, c'est un projet de code énorme : moins d'un giga. [S3]

[VISUEL : « 890 octets × 1 000 000 = 0,89 Go » ; la barre du cache est minuscule à côté de celle des poids.]

⚠️ à vérifier : chiffre de la fiche, constructeur, non mesuré. Le cache de fenêtre glissante s'ajoute.

Pour la mémoire, ce sont donc les poids qui décident : cent soixante-trois gigas au plus serré, trois cent seize pour une version correcte, et un dictionnaire sur le SSD.

Qu'un modèle tienne ne dit pas s'il va vite. À chaque token, ta machine relit les poids actifs : seize milliards de paramètres en quatre bits et demi, environ neuf gigas. La vitesse maximale, c'est la bande passante de ta mémoire divisée par ces neuf gigas.

[VISUEL : « vitesse max = bande passante ÷ Go lus par token ». Exemple : 1 200 Go/s ÷ 9,2 Go = 130 tokens/s. En dessous : « plafond théorique ».]

Ce plafond est un rêve. On va voir de combien.

---

## 4. Du moins cher au plus cher (5:20 – 9:40)

### Étape 1 : la RTX 5080

(ton de défi)

Ma carte, d'abord. Seize gigas de GDDR7. [S6] Au moment où je tourne, une 5080 se trouve à environ deux mille quarante euros chez le moins cher des marchands français. [S7]

[VISUEL : « RTX 5080 : 16 Go ≈ 2 040 € » ; face à « modèle : 163 Go minimum ». La barre ne rentre pas.]

Cent soixante-trois gigas dans seize : non. La carte seule ne suffit pas.

Mais le cœur du modèle peut vivre dans la RAM de l'ordinateur, la carte graphique prenant le reste. Avec cent quatre-vingt-douze gigas de RAM, la version Q2 tient, de justesse. La RAM coûte cher en ce moment : soixante-quatre gigas à huit cent trente-neuf euros, donc environ deux mille cinq cents euros pour cent quatre-vingt-douze. [S8]

⚠️ à vérifier : prix de la RAM (relevé sans date précise, triplé par mes soins), et ta carte mère doit accepter quatre barrettes de quarante-huit gigas.

La vitesse. Une mémoire de bureau, c'est environ quatre-vingt-dix gigas par seconde. Quatre virgule sept gigas lus par token en Q2 : plafond de dix-neuf tokens par seconde. On va voir qu'en vrai, c'est plutôt un tiers du plafond. Donc environ six tokens par seconde. À deux bits, je n'ai trouvé aucune mesure de ce que le modèle perd en qualité. [S9]

[VISUEL : « 90 Go/s ÷ 4,7 Go = 19 tokens/s (plafond) ; × 0,3 ≈ 6 tokens/s ». Mention « estimation, non mesurée ».]

⚠️ à vérifier : tout ce bloc est une estimation. Aucune mesure sur une 5080 avec ce modèle.

⟦à écrire : si tu as déjà lancé un essai sur ta machine avant le tournage, le résultat mesuré sur la 5080 ; sinon, une phrase qui dit que la réponse arrive le 16 novembre.⟧

### Étape 2 : un Mac Studio

Deuxième palier : le Mac Studio avec la puce M5 Ultra. Il se configure jusqu'à cinq cent douze gigas de mémoire unifiée, avec mille deux cents gigas par seconde de bande passante. [S10]

Le Q2 y tient largement. Le Q4 aussi, avec le dictionnaire sur le SSD : le projet indique d'ailleurs que le Q4 demande un Mac de cinq cent douze gigas. [S5]

Le prix ? Apple ne l'a pas encore publié, la configuration arrive fin octobre. Pour situer : la version de base, quatre-vingt-seize gigas, est à six mille cinq cent quatre-vingt-dix-neuf euros ; une version à deux cent cinquante-six gigas avec seize téraoctets de disque, à vingt mille six cent soixante-dix-neuf. [S10]

[VISUEL : trois étiquettes de prix : « 96 Go : 6 599 € », « 256 Go + 16 To : 20 679 € », « 512 Go : prix non publié ».]

⚠️ à vérifier : prix du M5 Ultra 512 Go, à relever sur apple.com/fr à sa sortie. Les deux repères viennent de la presse française, pas d'Apple.

Et la vitesse ? C'est ici que je confronte mon plafond à des mesures.

Le développeur du projet publie des mesures de la version Q2. Sur un Mac M5 Max, trente-neuf tokens par seconde, pour six cent quatorze gigas par seconde de bande passante. Mon plafond : cent trente. Mesuré : trente pour cent. [S9]

Sur un DGX Spark de NVIDIA, deux cent soixante-treize gigas par seconde : plafond de cinquante-huit, mesuré dix-huit. Trente et un pour cent. [S9] [S11]

[VISUEL : deux calculs côte à côte, posés ligne par ligne.
M5 Max : 614 ÷ 4,7 = 130 ; mesuré 39,4 → 30 %
DGX Spark : 273 ÷ 4,7 = 58 ; mesuré 18,1 → 31 %
Au centre, grand : « ≈ 30 % du plafond ».]

Deux machines très différentes, la même proportion. C'est ma règle des trente pour cent : deux mesures, c'est peu, mais c'est plus honnête qu'un plafond.

Appliquée au M5 Ultra en Q4 : cent trente, trente pour cent, environ quarante tokens par seconde. Une estimation, pas une mesure.

[VISUEL : « 1 200 ÷ 9,2 = 130 → × 0,3 ≈ 40 tokens/s (estimation) ».]

⚠️ à vérifier : règle des 30 % calibrée sur deux mesures en Q2, dates des mesures non indiquées ; la bande passante du M5 Max testé (614 Go/s) n'est pas confirmée.

### Étape 3 : un serveur à huit cartes

Troisième palier : le fichier officiel pèse cinq cent dix gigas, il lui faut des cartes de datacenter. Chez OVHcloud, le serveur « h200-1920 » : huit H200 de cent quarante et un gigas, donc mille cent vingt-huit gigas de mémoire. Quarante-deux euros de l'heure, hors taxes. [S12]

(comme Thanos qui reçoit la facture)

Sur les sept cent trente heures d'un mois moyen : trente mille six cent soixante euros hors taxes, trente-six mille sept cent quatre-vingt-douze avec la TVA. C'est le chiffre du début.

[VISUEL : « 42 € × 730 h = 30 660 € HT » ; en dessous « × 1,2 = 36 792 € TTC ». Le compteur du hook revient en haut de l'écran.]

⚠️ à vérifier : prix lu dans le catalogue public d'OVHcloud le 22/10/2026 ; disponibilité réelle du serveur non vérifiée.

Précision qui change tout : tu paies à l'heure. Deux heures de test, quatre-vingt-quatre euros, pas trente mille. Mais ces huit cartes ne te donnent pas Claude : elles te donnent un modèle ouvert qui joue dans la même cour sur certains tests. Pour la vitesse, je n'ai trouvé aucune mesure sur ce serveur.

⚠️ à vérifier : aucune mesure de vitesse trouvée sur ce serveur.

### Étape 4 : encore plus gros

Dernier palier. Le plus gros modèle ouvert du moment est Kimi K3, de Moonshot : deux mille huit cents milliards de paramètres, mille cinq cent soixante et un gigas de fichiers. Il ne tient plus dans les huit H200. [S13] Chez Scaleway, il faut huit cartes B300, plus de deux mille trois cents gigas : soixante euros de l'heure, quarante-trois mille huit cents euros par mois, et une pénurie affichée aujourd'hui. [S14]

[VISUEL : l'escalier des prix, de bas en haut : 5080 ≈ 2 040 € ; + RAM ≈ 2 500 € ; Mac 512 Go : prix non publié ; 8 × H200 : 30 660 €/mois ; 8 × B300 : 43 800 €/mois.]

Et Claude ? Personne ne sait s'il est plus petit ou plus gros que Kimi. S'il est bien plus gros, il faudrait plusieurs serveurs comme celui-là. C'est une hypothèse, pas un calcul.

---

## 5. La facture d'électricité (9:40 – 10:30)

Il reste ce que tu paies pour brancher tout ça. Beaucoup de vidéos anglophones calculent avec un kilowattheure américain. En France, le tarif réglementé d'EDF, option Base, est de vingt centimes du kilowattheure, taxes comprises, depuis le premier août. [S15]

[VISUEL : « 0,2001 € / kWh TTC (Base, EDF, 1er août 2026) ».]

Le Mac Studio, Apple annonce quatre cent quatre-vingts watts au maximum en continu. [S16] Une 5080 est annoncée à trois cent soixante watts à elle seule, et je compte environ six cents watts pour le PC entier. [S6]

⚠️ à vérifier : les 600 W du PC complet sont mon estimation, pas une mesure.

[VISUEL : tableau, calcul à l'écran.
Mac Studio : 0,48 kW × 4 h × 30 j = 57,6 kWh → 11,5 €/mois ; 24 h/24 : 69 €/mois
PC avec la 5080 : 0,6 kW × 4 h × 30 j = 72 kWh → 14,4 €/mois ; 24 h/24 : 86 €/mois
8 × H200 chez toi : 8 × 0,7 kW × 730 h = 4 088 kWh → 818 €/mois (cartes seules)]

À quatre heures par jour, c'est le prix d'un abonnement de streaming. En continu, on reste sous cent euros. Les huit H200 chez toi : huit cent dix-huit euros par mois pour les cartes seules. Un tarif de particulier n'existe pas à cette puissance, c'est juste un ordre de grandeur. [S17]

⚠️ à vérifier : tarif des datacenters différent du tarif réglementé ; consommation réelle sous charge non mesurée.

---

## 6. Le retournement (10:30 – 11:50) · relance à 55 %

[SON : la musique coupe net, une seconde de silence.]

Maintenant, la comparaison que ces vidéos oublient presque toutes.

Trente mille six cent soixante euros par mois, contre l'abonnement Claude Max : cent dollars, environ quatre-vingt-neuf euros. Il faut plus de trois cent quarante abonnements Max pour payer ce serveur. Le Pro, vingt dollars, dix-sept euros quatre-vingt-cinq : environ mille sept cent vingt fois moins. [S18] [S19]

[VISUEL : 30 660 ÷ 89,2 ≈ 344 abonnements Max. En dessous : « Pro : 20 $ ≈ 17,85 € ».]

Et si tu paies Claude à l'usage : Opus 5.5 coûte vingt dollars le million de tokens écrits. [S2] Trente mille six cent soixante euros, ce sont trente-quatre mille trois cent cinquante-cinq dollars, divisés par vingt : mille sept cent dix-huit millions. Pour battre l'API, le serveur doit écrire un milliard sept cents millions de tokens par mois, environ six cent cinquante tokens par seconde, jour et nuit. [S2] [S19]

[VISUEL : 30 660 € × 1,1205 = 34 355 $ ; ÷ 20 $ par million = 1 718 millions ; ÷ (730 h × 3 600 s) ≈ 654 tokens/s.]

⚠️ à vérifier : calcul au tarif de base des seuls tokens écrits (ni lecture, ni cache, ni remise batch), et pour un modèle qui n'a pas le niveau d'Opus 5.5 partout.

Le serveur ne se justifie donc que pour une équipe qui fait tourner l'IA en continu. Pour toi tout seul, jamais.

Alors, qu'est-ce qui reste sur ta carte ?

⟦à écrire : résultat mesuré sur la 5080 (si un essai est fait avant le tournage) : quel modèle de 16 Go ou moins tu as lancé, à quelle vitesse, et ce qu'il a su faire. Sinon : une phrase qui dit que tu l'as sous la main et que tu ne te prononces pas avant les mesures.⟧

⟦à écrire : ton avis, tes mots : ce que tu confies à Claude aujourd'hui, ce que tu aimerais garder chez toi. Pas d'anecdote inventée.⟧

Un modèle de seize gigas ne sera probablement pas Claude, mais il pourrait faire le quotidien : compléter du code, résumer, reformuler. Les tâches les plus dures resteraient dans le cloud. Un mélange, donc, pas un grand soir.

---

## 7. Le verdict selon ton profil (11:50 – 13:20)

Selon ton profil.

(rythme posé, un profil par phrase)

Si tu veux la meilleure qualité pour coder, tu gardes l'abonnement. Oui, un de plus, mais il coûte au moins trois cent quarante fois moins que le serveur.

Si ce qui te gêne, c'est que tes données partent chez quelqu'un, un Mac avec beaucoup de mémoire est la machine de bureau la plus simple pour y arriver. Le prix du plus gros modèle n'est pas encore connu : attends la sortie fin octobre.

Si tu as une carte comme la mienne, de seize gigas, ne cherche pas à faire tourner ce monstre. La vraie question est ce que sait faire pour toi un modèle qui tient dans seize gigas.

Si tu diriges une équipe, fais le calcul avec tes volumes et le seuil de six cent cinquante tokens par seconde. En dessous, l'API est moins chère.

Le chiffre du début, trente mille six cent soixante euros par mois, vaut pour un modèle qui joue dans la même cour que Claude, pas pour Claude. Anthropic n'a jamais dit combien il pèse.

[VISUEL : la 5080 au pied de la baie de serveurs ; le compteur se fige sur « 30 660 € / mois ».]

La vraie réponse sur ma carte arrive le seize novembre : « Claude ou mon PC ? », épisode un, avec un modèle qui tient dans mes seize gigas, testé sur la machine. Abonne-toi pour ne pas le rater, et dis-moi en commentaire quelle carte tu as.

⟦à écrire : la vidéo à pousser en écran de fin (la vidéo précédente de la chaîne).⟧

[VISUEL : écran de fin, 20 s : vidéo à gauche, bouton « S'abonner » à droite, une vignette « 16 nov. : Claude ou mon PC ? #1 ».]

---

## Relances d'attention

| Temps (estimé) | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Résultat | « 30 660 € par mois » |
| 0:15 | Contraste | 16 Go contre 163 à 500 Go, Rattata et Mewtwo |
| 0:25 | Promesse | « Je n'ai pas cette machine, alors j'ai fait le calcul » |
| 0:50 | Vraies réponses | Captures Reddit ou X qui se contredisent |
| 1:30 | Surprise | Aucun nombre de paramètres chez Anthropic |
| 2:05 | Humour | Monster Hunter : une seule patte bouge |
| 2:30 | Tableau | DeepSeek contre Opus 5, vert puis rouge |
| 3:10 | Appel à l'action | Abonnement (25 %) |
| 3:30 | Calcul | 552 milliards × octets |
| 4:30 | Surprise | Le dictionnaire Engram laissé sur le SSD |
| 5:30 | Prix | 5080 ≈ 2 040 € |
| 7:20 | Mesures | Deux machines, 30 % du plafond |
| 8:20 | Chiffre | 42 € × 730 h = 30 660 € |
| 9:30 | Escalier | De 2 040 € à 43 800 €/mois |
| 10:30 | Coupure musique | Retournement : 344 abonnements Max |
| 11:00 | Calcul | Seuil de 650 tokens par seconde |
| 11:50 | Verdict | Quatre profils |
| 13:00 | Annonce | Épisode du 16 novembre |

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| 0:35 – 1:15 | Moyen | La question Reddit peut traîner | Captures courtes, trois secondes chacune |
| 3:15 – 5:20 | Élevé | Bloc le plus dense : formules, Engram, cache | Une ligne de calcul à la fois, l'analogie bureau et bibliothèque, pas de GiB, que des Go |
| 5:20 – 9:40 | Moyen | Quatre étapes de suite | Une étiquette de prix par étape, l'escalier en fil rouge |
| 10:30 | Élevé | Chute classique du milieu | Coupure musicale, puis le chiffre de 344 abonnements |

## Notes de montage

- **Les 15 premières secondes** : le compteur, la 5080 et la baie de serveurs, rien d'autre. Pas de logo ni de titre.
- **Composants à construire une fois** : l'escalier des prix (resservira pour les épisodes « combien ça coûte »), la jauge de mémoire, la ligne de calcul qui se pose pas à pas.
- **Miniature** : [`vert-05.png`](../../ressources/miniatures/rendus/vert-05.png). Ajouter « 30 660 € » à l'étiquette « ?? ??? € » si la mention « /mois » tient dans le cadre ; sinon la mettre dans le titre.
- **Pas de vraie capture d'une appli Claude** : la page de documentation d'Anthropic est un document public, pas l'appli. Les captures de Reddit ou X sont à flouter.

## Ce qui reste à faire avant le script

1. Les `⟦à écrire⟧` (6 blocs).
2. Relever le prix du Mac Studio M5 Ultra 512 Go dès qu'Apple le publie (fin octobre).
3. Relire les `⚠️ à vérifier` et trancher dans [`sources.md`](sources.md).
4. Passer le grill (`grill-v1.md`) : 15 premières secondes seules, tics d'IA, longueur.
