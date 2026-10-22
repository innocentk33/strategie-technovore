# Combien coûte Claude en local ? : script v2

**Titre visé** : *Combien coûte Claude Opus 5.5 en local ? (j'ai fait le calcul)*

**v2 du 22/10/2026** : corrections du [grill](grill-v1.md) appliquées sur le [brouillon v1](brouillon-v1.md).
- **Accroche** : on garde « 30 660 € par mois » (ton choix), avec une phrase vers 0:20 qui annonce la version qui tient dans un PC gamer, pour tenir le « chez moi » de la miniature.
- **Retournement** : il reprend les mesures de ton essai sur la 5080, faites pour Claude #1 (sorti le 2 nov.). Sortie de cette vidéo : **lun. 16 nov.** (inversée avec Claude #1 le 22/10).
- Bloc technique allégé, Kimi K3 réduit à deux phrases, nombres arrondis dans la voix, antirez nommé, question au public sur le prix du Mac, tics corrigés.

**Durée** : environ 1 680 mots de voix off, plus tes ⟦à écrire⟧ (~200 mots) : 12 à 13 min à 145 mots/min.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = à l'écran. `(…)` = ton. `⟦à écrire⟧` = à toi. `[S…]` = source dans [`sources.md`](sources.md). `⚠️` = à revérifier le jour de la voix. Rien de tout ça ne se lit.

**Chapitres (YouTube)** :

| Minutage estimé | Chapitre |
|---|---|
| 0:00 | Trente mille euros par mois |
| 0:45 | La vraie question |
| 1:20 | On ne peut pas calculer Claude |
| 3:10 | Combien pèse le modèle |
| 4:40 | Palier 1 : ma 5080 et beaucoup de RAM |
| 6:20 | Palier 2 : un Mac Studio |
| 8:00 | Palier 3 : un serveur à huit cartes |
| 9:00 | La facture d'électricité |
| 9:40 | Ce qui tourne sur ma carte |
| 11:00 | Le verdict selon ton profil |

---

## 0. Trente mille euros par mois (0:00 – 0:45)

[VISUEL : l'image de la miniature : la RTX 5080 minuscule au pied d'une baie de serveurs géante. Sur la baie, un compteur s'allume : « 30 660 € / mois ». Pas de titre, pas de logo.]
[SON : un « tic » sec quand le compteur s'allume, puis silence.]

Trente mille six cent soixante euros. Par mois.

C'est le prix, d'après mon calcul, du plus petit serveur que j'ai trouvé en Europe pour faire tourner la version officielle d'un modèle de la trempe de Claude. En location. [S12]

[VISUEL : zoom sur la 5080, jauge « 16 Go ». À côté, la barre du modèle : « 163 à 500 Go ».]

Ma RTX 5080 a seize gigas de mémoire. Le modèle en pèse entre cent soixante et cinq cents. C'est un Rattata qui défie Mewtwo.

[VISUEL : un PC gamer apparaît à côté de la 5080, une étiquette « ?? ?? € » clignote dessus.]

Sauf qu'il existe une version compressée de ce modèle qui tient dans un PC gamer. Il lui manque juste beaucoup de RAM. Je te donne son prix, et ce qui tourne déjà sur ma carte.

(sec)

Je n'ai pas ces machines, alors j'ai fait le calcul. Chaque chiffre est à l'écran, et sa source est en description.

⟦à écrire : ton enjeu, en une ou deux phrases. Pourquoi toi tu voudrais Claude chez toi : l'abonnement, une limite atteinte en plein travail, ce que tu refuses de coller dans un outil en ligne, la dépendance à une boîte américaine… Une chose vraie.⟧

---

## 1. La vraie question (0:45 – 1:20)

Tu as sûrement vu passer ces vidéos qui disent qu'on peut remplacer Claude par une IA qui tourne chez soi. Plus d'abonnement, tes données qui restent à la maison.

Alors j'ai regardé ce que répondent ceux qui s'y connaissent quand quelqu'un pose la question pour de vrai.

⟦à écrire : une vraie question trouvée sur Reddit (r/LocalLLaMA) ou sur X, « quelle machine pour un modèle niveau Claude chez soi ? », et trois réponses réelles qui se contredisent. Lien en description. Ne pas reformuler de mémoire.⟧

[VISUEL : trois captures de vraies réponses, pseudos floutés, trois secondes chacune, un montant en face de chaque.]

Trois réponses, trois ordres de grandeur. ⟦à écrire : ce qui leur manque, à confirmer sur les vraies captures (le calcul ? la source ?).⟧

On va poser le calcul, du moins cher au plus cher : ma carte, un Mac, un serveur.

---

## 2. On ne peut pas calculer Claude (1:20 – 3:10)

Première règle : on ne peut pas faire ce calcul avec Claude.

Anthropic ne publie ni sa taille ni ses poids. J'ai ouvert la page des modèles et celle d'Opus 5.5, sorti le vingt-deux septembre : prix, contexte, dates de retrait. Aucun nombre de paramètres. [S1] [S2]

[VISUEL : capture de la page d'Opus 5.5, un surlignage balaie chaque ligne ; à la fin, un point d'interrogation à la place de « paramètres ».]

Sans taille, pas de calcul. Alors on prend un modèle ouvert, dont les fichiers sont publics, et dont l'éditeur dit qu'il joue dans la même cour.

Mon choix : DeepSeek V4.1 Flash, sorti le dix septembre, licence MIT. Cinq cent cinquante-deux milliards de paramètres. [S3]

[VISUEL : « 552 000 000 000 » en gros, puis le chiffre se range dans une grille de petites cases.]

Ça paraît énorme, mais c'est un modèle à experts : trois cent quatre-vingt-quatre spécialistes, et six seulement travaillent pour chaque token, chaque morceau de mot. Au total, environ seize milliards de paramètres actifs à la fois.

[VISUEL : 384 points ; à chaque « tic », six s'allument. Légende : « 16 milliards actifs / token ».]

Un boss de Monster Hunter : une carcasse énorme, et à chaque instant, une seule patte qui bouge.

Pourquoi lui ? Sa fiche officielle le compare à Opus 5, la version d'avant. Voilà le tableau.

[VISUEL : tableau, DeepSeek contre Opus 5. Terminal-Bench 2.1 : 90,6 contre 89,1. DeepSWE : 74,2 contre 74,0. Terminal-Bench 4.0 : 31,2 contre 51,8. Humanity's Last Exam : 36,8 contre 56,3. Les deux premières lignes en vert, les deux dernières en rouge.] [S3]

Sur les deux premières lignes, il fait jeu égal, il passe même devant. Sur les tests les plus durs, il décroche, et de loin.

Donc « au niveau de Claude », c'est vrai sur certains tests et faux sur d'autres. Et ces chiffres viennent de DeepSeek lui-même, face à Opus 5 et pas au 5.5. Garde ça en tête : tout ce qui suit est le prix d'un modèle de la même cour, pas de Claude. [S3] [S4]

⚠️ La mise à jour « 1017 » du 17 octobre : architecture supposée identique (S4).

**Abonnement (≈ 3:00)**

Je te parle de te désabonner de quelque chose, et je te demande de t'abonner à autre chose. Celui-là est gratuit : ton budget d'abonnements respire.

[VISUEL : bouton « S'abonner » animé, 3 secondes, le tableau reste à l'écran.]

---

## 3. Combien pèse le modèle (3:10 – 4:40)

Une IA, c'est un fichier rempli de nombres. Sur seize bits, un nombre prend deux octets. Sur huit bits, un. Sur quatre bits, un demi.

[VISUEL : calcul posé ligne par ligne.
552 milliards × 2 octets = 1 104 Go (16 bits)
552 milliards × 1 octet = 552 Go (8 bits)
552 milliards × 0,5 octet = 276 Go (4 bits)]

Réduire les bits, ça s'appelle la quantification. C'est le JPEG de l'IA : tu écrases les détails, ça pèse moins lourd, et tu perds un peu de qualité.

Pour vérifier, j'ai pris les fichiers d'antirez. C'est le développeur qui a créé Redis, et il a écrit son propre moteur pour faire tourner ce modèle sur Mac. Sa version en quatre bits fait trois cent seize gigas, celle en deux bits cent soixante-trois. La formule tombe juste. [S5] [S5 bis]

[VISUEL : 316 × 8 ÷ 552 = 4,6 bits ; 163 × 8 ÷ 552 = 2,4 bits. Deux barres : « Q4 : 316 Go », « Q2 : 163 Go ».]

Alors pourquoi le fichier officiel pèse-t-il cinq cent dix gigas ? [S3]

Parce que le modèle emporte une deuxième pièce, Engram : un dictionnaire d'environ deux cents gigas. Le moteur d'antirez le laisse sur le SSD et va y lire seulement la page dont il a besoin. [S3] [S5]

[VISUEL : un bureau et une bibliothèque. Le cœur du modèle sur le bureau (« mémoire rapide »), le dictionnaire Engram sur l'étagère (« SSD »).]

⚠️ « Les 510 Go contiennent Engram » est une déduction (S5).

La mémoire de la conversation, elle, tient dans moins d'un giga, même pour un énorme projet de code. [S3]

Ce qu'il faut retenir : cent soixante-trois gigas au plus serré, trois cent seize pour une version correcte.

---

## 4. Du moins cher au plus cher (4:40 – 9:00)

### Palier 1 : ma 5080 et beaucoup de RAM (4:40 – 6:20)

(ton de défi)

Ma carte, d'abord. Seize gigas. Au moment où je tourne, une 5080 coûte environ deux mille euros chez le moins cher des marchands français. [S6] [S7]

⚠️ Prix d'un seul modèle sur un comparateur, presque le double du prix de lancement : à relever à la main le jour de la voix. ⟦à écrire, si tu veux : ce que tu as payé la tienne, et quand.⟧

[VISUEL : « RTX 5080 : 16 Go » face à « modèle : 163 Go minimum ». La barre ne rentre pas.]

Cent soixante-trois gigas dans seize : non.

Mais le cœur du modèle peut vivre dans la RAM de l'ordinateur. Avec cent quatre-vingt-douze gigas de RAM, la version en deux bits tient, de justesse. Et la RAM, en ce moment, c'est de l'or : un kit de trente-deux gigas dépasse les quatre cents euros. Pour cent quatre-vingt-douze, compte au moins deux mille cinq cents euros. [S8]

[VISUEL : « 192 Go de DDR5 : 2 500 € et plus ». L'étiquette « ?? ?? € » du PC gamer de l'intro se remplit.]

⚠️ Aucun prix actuel trouvé pour un kit de 4 × 48 Go (dernier prix LDLC : 2 859 €). **Ton PC (22/10)** : 32 Go (2 × 16 Go), payés 99 € en 2025 ; le même kit est affiché à 491,99 $ aujourd'hui. Pour passer à 192 Go, il faudrait **remplacer** ces barrettes par 4 × 48 Go, pas en ajouter : les 2 500 € ne s'ajoutent pas à ce que tu as. Vérifie aussi que ta B850M accepte 4 × 48 Go et à quelle vitesse : avec 4 barrettes de DDR5, la RAM tourne souvent moins vite, ce qui ferait baisser les 6 tokens/s. ⟦à écrire, si tu veux : « mes 32 Go, je les ai payés 99 euros en 2025 ; aujourd'hui, le même kit est affiché à près de 500 dollars ». C'est ta preuve vécue de la pénurie, et ça colle avec le ×5,6 d'overclocking.com (S8). Relève le prix actuel du kit Klevv en euros avant de le dire.⟧

Ça tient. Mais tenir ne dit pas si ça va vite.

À chaque token, ta machine relit tous les paramètres actifs. En deux bits, ça fait environ cinq gigas. Donc la vitesse maximale, c'est la vitesse de ta mémoire divisée par ces cinq gigas.

[VISUEL : « vitesse max = bande passante ÷ Go lus par token ». Puis : « RAM de bureau : 90 Go/s ÷ 4,7 Go = 19 tokens/s (plafond) ».]

Une RAM de bureau, c'est environ quatre-vingt-dix gigas par seconde. Plafond : dix-neuf tokens par seconde. Et ce plafond, tu ne l'atteins jamais. Dans le palier suivant, on verra qu'en vrai on tourne autour d'un tiers. Donc environ six tokens par seconde. [S9]

[VISUEL : un curseur qui écrit au ralenti. « 3 000 tokens ÷ 6 / s ≈ 8 min ». Mention « estimation, non mesurée ».]

Une réponse de code de trois mille tokens, c'est plus de huit minutes à regarder le curseur. Et à deux bits, je n'ai trouvé aucune mesure de ce que le modèle perd en qualité.

⚠️ Estimation : aucune mesure de ce modèle sur une 5080 avec 192 Go de RAM. Les experts gardés sur la carte graphique pourraient accélérer.

### Palier 2 : un Mac Studio (6:20 – 8:00)

Deuxième palier : le Mac Studio avec la puce M5 Ultra. Jusqu'à cinq cent douze gigas de mémoire, et une mémoire bien plus rapide que celle d'un PC : mille deux cents gigas par seconde. [S10]

La version en quatre bits y tient. Antirez le dit lui-même : pour le quatre bits, il faut un Mac de cinq cent douze gigas. [S5]

[VISUEL : trois étiquettes : « 96 Go : 6 599 € », « 256 Go + 16 To : 20 679 € », « 512 Go : ? ».]

Pour situer : la version de base, quatre-vingt-seize gigas, est à six mille six cents euros. Une version à deux cent cinquante-six gigas, à plus de vingt mille. Et la version à cinq cent douze gigas, Apple n'a pas encore donné son prix. Tente ton chiffre en commentaire, j'épinglerai le vrai à côté. [S10]

⚠️ Si Apple publie le prix avant la voix : dis le vrai prix et remplace la question par « tu aurais parié combien ? ».

Pour la vitesse, je peux enfin confronter mon calcul à des mesures. Antirez publie les siennes, en deux bits. [S9]

Sur un Mac M5 Max, le plafond est à cent trente tokens par seconde. Il en mesure trente-neuf. Sur un DGX Spark de NVIDIA, plafond à cinquante-huit, il en mesure dix-huit. [S9] [S11]

[VISUEL : deux calculs côte à côte.
M5 Max : 614 ÷ 4,7 = 130 ; mesuré 39,4 → 30 %
DGX Spark : 273 ÷ 4,7 = 58 ; mesuré 18,1 → 31 %
Au centre : « ≈ 30 % du plafond ».]

Deux machines très différentes, la même proportion. Deux mesures, c'est peu. Je m'en sers comme d'une règle de pouce : trente pour cent du plafond.

Sur le M5 Ultra en quatre bits, ça donnerait environ quarante tokens par seconde. Une estimation, pas une mesure.

[VISUEL : « 1 200 ÷ 9,2 = 130 → × 0,3 ≈ 40 tokens/s (estimation) ».]

⚠️ Règle calibrée sur deux mesures en Q2, non datées ; la bande passante du M5 Max testé n'est pas confirmée (S9).

### Palier 3 : un serveur à huit cartes (8:00 – 9:00)

Pour la version officielle, sans compression, il n'y a plus de machine de particulier. Il faut des cartes de datacenter. Chez OVHcloud, un serveur avec huit cartes H200, plus de mille gigas de mémoire en tout : quarante-deux euros de l'heure, hors taxes. [S12]

(comme Thanos qui reçoit la facture)

Sur un mois entier, trente mille six cent soixante euros. Le chiffre du début.

[VISUEL : « 42 € × 730 h = 30 660 € HT » ; en dessous « 36 792 € TTC ». Le compteur du hook revient en haut de l'écran.]

Ce serveur se loue à l'heure : deux heures de test, quatre-vingt-quatre euros. Pour la vitesse, je n'ai trouvé aucune mesure sur cette machine.

⚠️ Prix du catalogue OVHcloud au 22/10, disponibilité non vérifiée.

Et si Claude est plus gros que DeepSeek ? Le plus gros modèle ouvert du moment, Kimi K3, ne tient déjà plus dans ces huit cartes. Pour Claude, personne en dehors d'Anthropic ne connaît la taille. [S13]

[VISUEL : l'escalier des prix, de bas en haut : RAM ≈ 2 500 € ; Mac 512 Go : ? ; 8 × H200 : 30 660 €/mois ; au-dessus, une marche dans le brouillard : « Claude : ? ».]

---

## 5. La facture d'électricité (9:00 – 9:40)

Il reste à brancher tout ça. Beaucoup de vidéos anglophones calculent avec un kilowattheure américain. En France, le tarif réglementé d'EDF, option Base, est à vingt centimes le kilowattheure depuis le premier août. [S15]

Le Mac Studio consomme au maximum quatre cent quatre-vingts watts, d'après Apple. Pour mon PC avec la 5080, ⟦à écrire : la consommation mesurée au wattmètre pendant les essais de Claude #1⟧. [S16] [S6]

[VISUEL : tableau, calcul à l'écran.
Mac Studio : 0,48 kW × 4 h × 30 j = 57,6 kWh → 11,5 €/mois ; 24 h/24 : 69 €/mois
PC avec la 5080 : 0,6 kW × 4 h × 30 j = 72 kWh → 14,4 €/mois ; 24 h/24 : 86 €/mois]

Quatre heures par jour, c'est le prix d'un abonnement de streaming. Même allumé jour et nuit, ça reste sous les cent euros par mois.

⚠️ Les 600 W du PC sont une estimation, pas une mesure. ⟦à écrire, si tu as un wattmètre : la conso réelle de ton PC pendant l'essai.⟧

---

## 6. Ce qui tourne sur ma carte (9:40 – 11:00)

[SON : la musique coupe net, une seconde de silence.]

Maintenant, compare avec ce que tu paies déjà. L'abonnement Claude Max, c'est cent dollars, environ quatre-vingt-dix euros par mois. Les deux mille cinq cents euros de RAM, c'est plus de deux ans d'abonnement Max. [S18] [S19]

[VISUEL : « 2 500 € ÷ 89 € ≈ 28 mois de Claude Max ». En dessous, en petit : « Pro : 20 $ ≈ 18 € ».]

Et pour une équipe qui paie Claude à l'usage ? Avec le budget du serveur, tu achètes environ un milliard sept cents millions de tokens d'Opus 5.5. Pour faire mieux, le serveur doit écrire six cent cinquante tokens par seconde, jour et nuit, tout le mois. [S2] [S19]

[VISUEL : « 30 660 € ≈ 34 355 $ ÷ 20 $ par million = 1,7 milliard de tokens ÷ (730 h × 3 600 s) ≈ 654 tokens/s ».]

⚠️ Tokens écrits au tarif de base seulement (S2).

Louer, acheter ou rester abonné, j'en fais une vidéo complète le quatre janvier.

Et sur ma carte, sans un euro de plus ? Je l'ai testé dans l'épisode un de « Claude ou mon PC ? ».

⟦à écrire : le résultat de Claude #1 en deux ou trois phrases. Quel modèle de 16 Go ou moins, sa vitesse mesurée, la tâche réelle et ce qu'il en a fait. Une scène vue à l'écran, pas un tableau.⟧

[VISUEL : extrait de Claude #1, le compteur de tokens par seconde en grand ; carte YouTube vers l'épisode 1.]

⟦à écrire : ton avis, avec tes mots. Ce que tu continues à confier à Claude, et ce que tu feras désormais chez toi. Ça répond à ton enjeu du début.⟧

---

## 7. Le verdict selon ton profil (11:00 – 12:20)

(rythme posé, un profil par phrase)

Si tu veux la meilleure qualité pour coder, garde l'abonnement. Oui, un de plus, mais il coûte des centaines de fois moins cher que le serveur.

Si ce qui te gêne, c'est que tes données partent chez quelqu'un, le Mac avec beaucoup de mémoire est la machine de bureau la plus simple. Attends juste le prix de la version à cinq cent douze gigas.

Si tu as une carte de seize gigas comme la mienne, ne cherche pas à faire tourner ce monstre. Demande-toi ce qu'un modèle de seize gigas sait faire pour toi.

Si tu diriges une équipe, fais le calcul avec tes volumes : en dessous de six cent cinquante tokens par seconde en continu, l'API coûte moins cher.

[VISUEL : la 5080 au pied de la baie ; le compteur se fige sur « 30 660 € / mois ».]

Trente mille euros par mois pour un cousin de Claude. Claude lui-même, personne ne sait combien il pèse.

Ce que donne vraiment un modèle de seize gigas sur ma carte, tout est mesuré dans « Claude ou mon PC ? », épisode un. Il est juste là. Et dis-moi en commentaire quelle carte tu as.

[VISUEL : écran de fin, 20 s : « Claude ou mon PC ? #1 » à gauche, « S'abonner » à droite.]

---

## Relances d'attention

| Temps (estimé) | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Résultat | « 30 660 € par mois » |
| 0:15 | Contraste | 16 Go contre 163 à 500 Go, Rattata et Mewtwo |
| 0:20 | Boucle ouverte | Une version tient dans un PC gamer : « ?? ?? € » |
| 0:30 | Enjeu | Ta raison à toi |
| 0:55 | Vraies réponses | Captures Reddit ou X qui se contredisent |
| 1:30 | Surprise | Aucun nombre de paramètres chez Anthropic |
| 2:05 | Humour | Monster Hunter |
| 2:30 | Tableau | Vert puis rouge |
| 3:00 | Appel à l'action | Abonnement |
| 3:50 | Personnage | Antirez, le créateur de Redis |
| 4:15 | Surprise | Engram sur l'étagère |
| 5:20 | Boucle fermée | « ?? ?? € » devient « 2 500 € et plus » |
| 6:00 | Concret | Huit minutes pour une réponse |
| 6:50 | Participation | « Tente ton chiffre en commentaire » |
| 7:30 | Mesures | 30 % du plafond |
| 8:20 | Retour au début | 42 € × 730 h = 30 660 € |
| 9:40 | Coupure musique | 28 mois de Claude Max |
| 10:20 | Boucle fermée | Le résultat de Claude #1 sur la 5080 |
| 11:00 | Verdict | Quatre profils |

## Points de décrochage

| Moment | Risque | Parade |
|---|---|---|
| 0:45 – 1:20 | Moyen | Captures courtes, trois secondes chacune |
| 3:10 – 4:40 | Moyen (était élevé en v1) | Bloc réduit : bits, JPEG, antirez, Engram. Une ligne de calcul à la fois |
| 9:40 | Élevé | Coupure musicale, puis le chiffre de 28 mois |

## Notes de montage

- **Les 15 premières secondes** : le compteur, la 5080 et la baie, rien d'autre.
- **L'étiquette « ?? ?? € » du PC gamer** est une boucle visuelle : posée à 0:20, remplie à 5:20.
- **Composants réutilisables** : l'escalier des prix, la jauge de mémoire, la ligne de calcul posée pas à pas.
- **Miniature** : [`vert-05.png`](../../ressources/miniatures/rendus/vert-05.png), avec « 30 660 € » dans l'étiquette, ou « 30 660 €/mois » si ça tient.
- **Captures** : documentation publique d'Anthropic seulement, pas l'appli. Captures Reddit ou X floutées.

## Avant la voix

1. Les ⟦à écrire⟧ : ton enjeu, la question Reddit ou X, le résultat de Claude #1, ton avis, ta RAM. (Ton brouillon de Claude #1 dit que tu paies Claude Max 200 $ par mois : c'est peut-être ton enjeu.)
2. Le jour de la voix, relève à la main : le prix de la 5080, un kit de 192 Go de DDR5 et le Mac Studio 512 Go.
3. Relis les `⚠️` restants dans [`sources.md`](sources.md), section 8.
4. Relis les 15 premières secondes seules : donnent-elles envie de rester ?
