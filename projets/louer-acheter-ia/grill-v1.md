# Grill du script « Louer, acheter ou s'abonner » v1 (23/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Version finale : [`script.md`](script.md).
> Grille : `youtube-script-grill`, mode B (après l'écriture), **variante storytelling** (test des 30 secondes, axe 10 des liaisons, axes S1 à S6), plus les 5 règles du format calculé (`strategie.md`, pilier 2).
> Hypothèses : titre *Louer, acheter ou s'abonner : j'ai fait le calcul pour l'IA*, miniature verte à concevoir ; public de 18-30 ans, surtout africain, qui paie (ou hésite à payer) un abonnement d'IA et a parfois un PC de jeu ; arrivée par la recherche (« ia en local », « abonnement claude prix ») et par la suite de « Combien coûte Claude en local ? ». Objectif : la vidéo « Help » du pilier 2, sortie pour les bonnes résolutions de janvier.
> Faits revérifiés le 23/10 : voir « Vérification des faits » en bas, et les lignes 28 et 29 ajoutées à [`sources.md`](sources.md). Calcul refait de zéro : `/private/tmp/claude-501/-Users-innocent-Dev-youtubeSkill/e157317b-e0c6-49ed-a993-29af06a1f505/scratchpad/roast-louer/seuils.py` (temporaire).

## Note globale : 6/10

5 🟢, 11 🟠, 1 🔴. Les chiffres sont justes (je retrouve chaque seuil au dixième près), les sources sont dites tôt et le ton est déjà conversationnel (2,1 liaisons pour 100 mots). Mais le verdict se trompe de gagnant pour le profil qui compte le plus, et le hook retient la réserve « 16 Go » que la fiche exige dans les 30 s.

## Verdict

C'est une vidéo qui manque en français : trois routes, des euros TTC, le tarif bleu d'EDF, une carte de 2018 démasquée chez OVH, et une formule que le spectateur peut refaire chez lui. Le format calculé est bien respecté presque partout, et la pique « le seul abonnement à garder, il est gratuit » est dans ta voix.

**Le plus gros problème : le titre pose « qu'est-ce qui coûte le moins cher ? », et la V1 répond « acheter » au profil Max alors que ses propres chiffres disent « louer ».** À 4 h par jour, la RTX 5080 louée sur Vast.ai coûte 32 à 50 € par mois ; l'achat ne la rattrape qu'après 45 à 79 mois. Même la frise du script le montre (la location reste sous l'achat sur 36 mois), mais la voix ne le dit jamais. Un spectateur qui fait le calcul le dira en commentaire, et c'est exactement la faille de Kai (`etudes/kai.md`, section 6).

Deuxième problème : le hook annonce « dix-neuf mois » et cache la réserve (« pour ce qu'un modèle de 16 Go sait faire ») derrière « il y a un piège » jusqu'à 8:13. La fiche (« Corrections de la 2e vérification ») demande qu'elle tombe dans les 30 s.

## La promesse, le problème profond, la chaîne « mais / donc »

- **La promesse** (titre) : on compare trois routes et on dit laquelle coûte le moins cher, calcul à l'appui. La V1 livre deux routes en détail (s'abonner, acheter), traite la troisième après le « piège », et son verdict garde l'achat comme horizon pour le profil Max (« la carte se rembourse en dix-neuf mois environ. Mais avant de sortir mille neuf cents euros, loue une 5080 quelques heures »). La location y devient un essai avant l'achat, alors qu'à 4 h par jour c'est elle la moins chère pendant presque quatre ans.
- **Le problème de surface** : quelle route coûte le moins cher pour faire de l'IA.
- **Le problème profond** : la fatigue des abonnements (« je coupe mes abonnements », ton « 60 abonnements par mois ») et la question honnête derrière : « rentable » pour faire quoi ? Le second est bien posé (le piège, les astérisques). Le premier reste un ⟦à écrire⟧ à 0:45 et un [À ÉCRIRE] dans le verdict : sans ta phrase, la vidéo n'a pas de narrateur qui veut quelque chose. Pistes, à toi de dire laquelle est vraie : [ce que tu paies chaque mois en abonnements] ; [la limite des cinq heures atteinte en plein travail] ; [l'envie que tes données ne sortent pas de chez toi : c'est le commentaire le plus liké chez Kai (364 likes), et c'est cohérent avec ta règle de ne jamais coller une clé d'API dans un outil tiers].
- **La chaîne** (V1) : Pro à 20 $, **mais** pas un euro sur la page, **donc** conversion → **et** ChatGPT → **mais** rationné → **et** 13 $ par développeur en entreprise (« et aussi ») → acheter : 1 900 €, **sauf qu'**elle valait 1 179 €, **donc** pari → **et** le PC → électricité : 8,40 € → le calcul : 19 mois → **mais** une égalité non vérifiée → **sauf que** la carte ne fait pas tourner Claude, **donc** 16 Go → « Il reste une troisième route » (**et ensuite**) → verdict.
  Le maillon faible est l'entrée de la location : elle arrive comme un chapitre de plus, après le retournement. Dans `script.md` : 19 mois, **sauf qu'**on n'a regardé que deux routes sur trois → la même carte à 0,27 € de l'heure, **donc** 32 € par mois → la location reste sous l'achat sur trois ans → **sauf que** le taximètre tourne même quand la carte n'écrit rien → Scaleway coûte plus qu'un Max, OVH loue une carte de 2018 → **mais** louer ou acheter quoi, au juste ? Un modèle de 16 Go → **donc** le verdict par profil.

## Les 5 règles du calculé

| Règle | V1 | Verdict | Dans `script.md` |
|---|---|---|---|
| 1. Les sources dites tôt (« je n'ai pas cette machine, alors j'ai fait le calcul, et voici d'où viennent les chiffres ») | > « Je n'ai pas fait tourner Claude chez moi, donc j'ai fait le calcul, chaque prix à l'écran avec sa source. » (0:30) | 🟢 dans les 30 s | « D'après mon calcul » dès la 1re phrase ; « ma carte ne fait pas tourner Claude » et « chaque prix est à l'écran, avec sa source » à 0:23 ; bandeau « Calcul · prix relevés le … » dès la 1re image |
| 2. Chaque chiffre daté | Bandeau permanent « Prix relevés le 23/10/2026 » ; EDF « depuis le premier août » ; Vast.ai daté à l'écran | 🟠 deux dates seront fausses le 4 janvier : « Je les ai relevés le vingt-trois octobre, au moment où j'écris ce script » et « cet été, elle est même descendue à mille deux cents euros » | Date du relevé en crochet ; « l'été dernier » ; relevés regroupés dans une liste (R1 à R10) |
| 3. Le calcul à l'écran, puis confronté à une mesure | Chaque division à l'écran ; la mesure attendue est ⟦mesure de Claude #1⟧ | 🟠 le calcul est exemplaire, la confrontation dépend de Claude #1 (essais des 23-24/10) | Inchangé ; la consigne du ⟦⟧ dit de refaire les sections 4 et 5 si la mesure existe |
| 4. Aucune estimation présentée comme une mesure | > « Plus de dix ans. C'est le temps qu'il faut à une RTX 5080… » ; > « plus de trente mille euros par mois de serveur » | 🟠 le chiffre du hook est dit comme un fait (« calcul » n'est qu'à l'écran) ; les 30 000 € de Coût Claude perdent « en location, d'après mon calcul » ; les 350 W sont bien « une hypothèse, pas une mesure » | « D'après mon calcul, c'est le temps qu'il faut… » ; « plus de trente mille euros par mois, rien que pour louer le serveur » (après « j'en ai fait le calcul ») |
| 5. Euros et électricité au tarif français | Euros TTC partout, tarif bleu EDF, taux BCE ; Vast.ai et RunPod converties sans TVA, et c'est dit | 🟢 | Inchangé ; la vidéo anglaise « qui calcule avec un prix américain » justifie la règle à l'oral |

**À signaler hors de ce script** : *Combien coûte Claude en local ?* (16 nov.) dit « 2 500 € ÷ 89 € ≈ 28 mois de Claude Max » et « Pro : 20 $ ≈ 18 € », donc des prix **sans TVA**. Ici, le Max est à 107 € **avec** TVA. Un abonné qui voit les deux vidéos lit 89 € puis 107 € pour le même abonnement. Le plus simple : passer Coût Claude en TTC avant sa sortie (question 8 pour toi).

## Le calcul des seuils, refait

Script indépendant, mêmes hypothèses que la V1 (1 899,95 €, 4 049,95 €, 0,2001 €/kWh, 350 W, 1 € = 1,1205 $, TVA 20 %, 120 h et 240 h). **Je trouve la même chose, au dixième près**, pour chaque chiffre dit ou affiché :

| Cas | V1 | Grill |
|---|---|---|
| Électricité, 350 W × 120 h / 240 h | 8,40 € / 16,81 € | 8,40 € / 16,81 € |
| Fourchette 300 W × 120 h ; 450 W × 240 h | 7,20 € ; 21,61 € | 7,20 € ; 21,61 € |
| Pro / Max 5x / Max 20x en euros | 21,42 / 107,10 / 214,19 € | identique |
| Carte contre Pro, Max 5x, Max 20x (120 h) | 146 ; 19,3 ; 9,2 mois | 146,0 ; 19,3 ; 9,2 |
| PC complet contre Max 5x (120 h) | 41 mois | 41,0 |
| Carte à 1 200 € contre Max 5x | 12,2 mois | 12,2 |
| Carte contre location Vast.ai (120 h) : la moins chère / médiane | 79 ; 45,5 mois | 79,0 ; 45,5 |
| Scaleway L4 et OVH Quadro (120 h) | 113,76 € ; 51,84 € | identique |

Trois écarts, tous dans la façon de le dire :
- **Annexe, sensibilité à 240 h** : « 21,0 à 22,2 mois » est la plage de 350 à 450 W ; à 300 W, c'est 20,5 mois. Corrigé dans l'annexe de `script.md` et ajouté en ligne 29 de `sources.md`.
- **« la carte se rembourse en un an et demi au plus »** (fin de la section 5) : faux dès 240 h (21 mois) et avec le PC complet (41 mois). Devient « environ ».
- **Les deux chiffres que la V1 ne calcule pas** et qui changent le verdict : sur 36 mois à 120 h, le Max coûte ≈ 3 856 €, l'achat ≈ 2 202 €, la location Vast.ai médiane ≈ 1 804 € (la moins chère ≈ 1 168 €) ; et la location dépasse Pro dès ≈ 51 h par mois à la médiane (≈ 79 h au plus bas), soit environ 2 h par jour. La V1 disait « dès quelques heures par jour » : juste, mais vague.

## Le test des 15 premières secondes

Relues seules, à 145 mots/min (environ 36 mots) :

> « Plus de dix ans. C'est le temps qu'il faut à une RTX 5080 pour devenir moins chère qu'un abonnement Claude à vingt dollars. Contre l'abonnement à cent dollars, environ dix-neuf mois. Et contre celui à deux… »

🟢 **Oui, c'est le moment le plus fort qui tienne sans préparation** : un chiffre contre-intuitif, sans contexte ni présentation, et un contraste (dix ans contre dix-neuf mois) qui donne envie de savoir pourquoi. Deux retouches :
- **« d'après mon calcul »** dans la première phrase (règle 4) : quatre mots, et le format est dit dès la 3e seconde ;
- **trois nombres en 15 s, c'est un de trop** à l'oreille : le Max à 200 $ (« neuf mois ») reste sur le compteur à l'écran et sort de la voix. Le contraste demandé par la fiche, c'est « jamais » contre « dix-neuf mois ».

## Le test des 30 secondes

| Tranche | Ce que dit la V1 | Verdict |
|---|---|---|
| 0-5 s | > « Plus de dix ans. C'est le temps qu'il faut à une RTX 5080 pour devenir moins chère qu'un abonnement Claude à vingt dollars. » | 🟢 Le sujet et une tension, raccord avec le titre. Il manque « d'après mon calcul ». |
| 5-15 s | > « Contre l'abonnement à cent dollars, environ dix-neuf mois. Et contre celui à deux cents, neuf mois. » | 🟢 Le contraste, avec sa preuve à l'écran (« calcul, prix du 23/10/2026, 4 h par jour »). Un chiffre de trop dans la voix. |
| 15-30 s | > « Du coup, en janvier, quand tu fais le ménage dans tes abonnements : louer, acheter ou rester abonné, qu'est-ce qui coûte le moins cher ? » | 🟢 La question centrale, une seule, en mots simples, vers le 60e mot (la règle : avant le 90e). |
| Pont | > « Je n'ai pas fait tourner Claude chez moi, donc j'ai fait le calcul, chaque prix à l'écran avec sa source. Sauf qu'il y a un piège dedans. » | 🟠 « Il y a un piège » annonce sans rien livrer (faux suspens, `anti-ia.md` section 2), et le piège, c'est justement la réserve que la fiche veut dans les 30 s. Le spectateur entend « dix-neuf mois » sans savoir que ça ne remplace pas Claude, pendant huit minutes. |

**Budget :** 89 mots ≈ 37 s à 145 mots/min, 30 s à 180. 🟢
**À couper :** « Et contre celui à deux cents, neuf mois » (à l'écran seulement).
**Réécriture des 30 s** (99 mots ≈ 40 s à 145, 33 s à 180 : 10 mots de plus, pour la réserve exigée par la fiche) :

> Plus de dix ans. D'après mon calcul, c'est le temps qu'il faut à une RTX 5080 pour coûter moins cher qu'un abonnement Claude à vingt dollars.
> Contre celui à cent dollars, environ dix-neuf mois.
> Du coup, quand tu fais le ménage dans tes abonnements en janvier : louer, acheter ou rester abonné, qu'est-ce qui coûte le moins cher ?
> Sauf que ma carte ne fait pas tourner Claude. Donc ces dix-neuf mois, c'est pour un modèle de seize gigas. Et chaque prix est à l'écran, avec sa source.
> Et cette même carte se loue dès trente centimes de dollar de l'heure.

La question tombe au 57e mot. Le pont change de nature : au lieu d'un « piège » annoncé, un chiffre précis (le taximètre à l'écran) qui ouvre la deuxième question, « et si louer coûtait moins cher que les deux ? », refermée à 7:59.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🔴 | Le titre demande la route la moins chère ; le verdict garde l'achat pour le profil Max alors que la location coûte 32 à 50 € par mois et ne se fait rattraper qu'après 45 à 79 mois. |
| 2. Alignement | 🟢 | Rien à vendre, les limites sont dites (« on compare des prix, pas des services »), et la formule est donnée pour refaire le calcul. |
| 3. Problème profond | 🟠 | « Rentable pour quoi ? » est bien porté par le piège ; ta fatigue des abonnements reste deux crochets. |
| 4. Public & complexité | 🟢 | Une seule formule, introduite par une phrase simple (« l'argent que tu gardes ») avant d'être appliquée trois fois. |
| 5. Valeur & originalité | 🟢 | Trois routes, euros TTC, EDF, la Quadro de 2018 démasquée : aucune vidéo française ne le fait (recherche vidIQ du 23/10). |
| 6. Structure & transformation | 🟠 | La location arrive après le retournement, comme un chapitre de plus, et les 13 $ par développeur sortent des trois routes. |
| 7. Histoire (enquête par le calcul) | 🟠 | Un bon retournement (la carte ne fait pas tourner Claude), mais l'enquêteur n'a pas d'envie à lui tant que ton enjeu n'est pas écrit. |
| 8. Mais / donc | 🟠 | Très bon dans les sections 2 à 5 ; « Il reste une troisième route » et « Pour situer, en entreprise… » s'enchaînent en « et ensuite ». |
| 9. Engagement actif | 🟠 | Le spectateur ne se situe jamais avant le verdict ; « Dis-le en commentaire » à la fin seulement. |
| 10. Rythme, oralité & liaisons | 🟢 | 2,1 liaisons pour 100 mots (40 pour 1 876 mots), des réactions (« Huit euros. Ouais… », « Douze ans. ») ; trois rafales de chiffres (détail plus bas) et quatre « Bref ». |
| 11. Tics d'IA | 🟠 | Peu nombreux mais visibles : un écho en faux suspens, un « la bonne question, c'est plutôt », un « piège » annoncé, deux généralisations. |
| S1. Les 30 premières secondes | 🟠 | Question à temps, sources dites ; il manque « d'après mon calcul » et la réserve « 16 Go ». |
| S2. Le pont | 🟠 | « Il y a un piège dedans » ouvre une question, mais floue et en faux suspens. |
| S3. Les retournements | 🟠 | 22 relances en 12:56, une toutes les 35 s ; des trous de 50 s (1:05-1:55, 9:30-10:25). |
| S4. Planté / récolté et motif | 🟢 | Les compteurs du hook remplis puis barrés, le pari sur le prix récolté (12 mois), la promesse de Coût Claude tenue. |
| S5. Personnages et enjeu | 🟠 | Le « tu » des profils porte la vidéo ; le « je » n'a pas d'enjeu écrit. |
| S6. La fin | 🟠 | Elle ouvre une question (« quel modèle je calcule ensuite ? ») mais passe par une reformulation-morale (« la bonne question, en janvier, c'est plutôt… »). |

## Le grill

### 1. Le verdict se trompe de gagnant pour le profil Max

> « Si tu paies un Max à cent dollars, et que ce qui te sert tient dans un modèle de seize gigas, la carte se rembourse en dix-neuf mois environ. Mais avant de sortir mille neuf cents euros, loue une 5080 quelques heures, pour trois fois rien. »
> « Bref, louer, c'est la route des petits usages. […] Et si tu passes tes journées dessus, l'achat finit par gagner. »

**Pourquoi ça coince** : à 120 h par mois, les trois routes coûtent, sur trois ans, environ 3 856 € (Max), 2 202 € (achat) et 1 804 € (location Vast.ai médiane). L'achat ne passe devant la location qu'après 45,5 mois à la médiane, 79 au plus bas. Le « petit usage » de la V1, c'est donc tout le cas type de la vidéo, 4 h par jour. La frise de la V1 le dessine (« location Vast.ai (droite douce) ») sans que la voix le dise. Le titre promet la route la moins chère : c'est elle.

**Correction** (appliquée) :
- en section 6, la location remplace le piège comme relance forte, avec la coupure musicale : « Regarde la frise : sur trois ans, la location reste sous l'achat du début à la fin. » ;
- elle est tout de suite tempérée par un fait vérifié (ligne 28 de `sources.md`) : « Tu paies à la seconde tant que la machine est allumée, même quand elle n'écrit rien. Et le stockage se paie en continu, même machine arrêtée, d'après la doc de Vast.ai. » ;
- le bilan dit qui gagne, et quand ça bascule : « si tu paies un Max, à quatre heures par jour, la location sur Vast.ai est la moins chère des trois routes pendant presque quatre ans. Mais à trente-deux euros, tu as déjà dépassé Pro. Et si tu passes tes journées dessus, à huit heures par jour, l'achat repasse devant en deux à trois ans environ » ;
- le profil Max devient « commence par louer. À quatre heures par jour, c'est trente à cinquante euros par mois, plus le stockage, au lieu de cent sept ».

### 2. La réserve « 16 Go » arrive à 8:13, la fiche la veut avant 30 s

> « Contre l'abonnement à cent dollars, environ dix-neuf mois. […] Sauf qu'il y a un piège dedans. »

**Pourquoi ça coince** : la 2e vérification (fiche, et fait 23) est nette : la réponse du hook doit dire « jamais » contre 20 €, « environ 19 mois » contre un Max, « et seulement pour ce qu'un modèle de 16 Go sait faire ». Pendant huit minutes, le spectateur croit que 1 900 € remplacent son Claude Max. C'est le genre de promesse que les commentaires corrigent, et que YouTube compare au contenu.

**Correction** (appliquée) : l'astérisque tombe à 0:23 (« Sauf que ma carte ne fait pas tourner Claude. Donc ces dix-neuf mois, c'est pour un modèle de seize gigas. »). Le « piège » ne pouvant plus surprendre à 63 %, la relance forte passe à la location (n° 1), et l'ex-section 6 devient « Ce que sait faire un modèle de 16 Go », juste avant le verdict, où elle sert : « Mais louer ou acheter quoi, au juste ? »

### 3. Trois phrases vont plus loin que le calcul ou la source

> « Donc sur le papier, si tu paies un Max, la carte se rembourse en un an et demi au plus. »
> « Tu vois le problème : tu paies au mois, et tu es rationné à la journée. »
> « C'est la question qui revient sous toutes les vidéos anglaises, parce qu'elles calculent avec un kilowattheure américain. »

**Pourquoi ça coince** :
- « au plus » : 21 mois à 240 h, 41 mois avec le PC complet ;
- la limite est une fenêtre glissante de **cinq heures** plus une limite **hebdomadaire** (fait 3), pas une limite à la journée ;
- « toutes les vidéos anglaises » : `sources.md` ne relève qu'un fil, sous une vidéo de Kai (135 likes, 44 réponses, d'après `etudes/kai.md`).

**Correction** : « en un an et demi environ » ; « rationné toutes les cinq heures » ; « Sous une grosse vidéo anglaise sur l'IA en local, c'est un des commentaires les plus discutés, parce qu'elle calcule avec un prix américain. »

### 4. Les 350 W et les 360 W se contredisent

> « Pour la consommation, NVIDIA annonce trois cent soixante watts pour la carte. Moi, je prends trois cent cinquante watts pendant qu'elle écrit. »

**Pourquoi ça coince** : le fait 19 donne 300 à 450 W **pour un PC complet**, et ta mesure se fera **à la prise**, donc pour tout le PC. La V1 attribue les 350 W à la carte seule, juste sous le chiffre de NVIDIA : le spectateur attentif se demande pourquoi l'hypothèse est sous la fiche technique, et le jour où la mesure arrive (PC complet), le chiffre change de sens.

**Correction** (appliquée) : la phrase des 360 W sort de la voix ; « je prends trois cent cinquante watts pour tout le PC pendant qu'il écrit. C'est une hypothèse, pas une mesure. » L'étiquette à l'écran devient « hypothèse, PC complet ». La sensibilité reste dite : « contre un Max, une erreur sur les watts change le résultat d'un ou deux mois au plus » (fait 27).

### 5. Les 13 $ par développeur sortent des trois routes

> « Pour situer, en entreprise, Claude Code coûte en moyenne treize dollars par développeur et par jour actif, d'après Anthropic, facturé au token. Donc à côté, l'abonnement à vingt dollars par mois, c'est presque un cadeau. Presque. »

**Pourquoi ça coince** : c'est un coût d'entreprise à la consommation (fait 24), comparé à un abonnement rationné : la comparaison ne tient pas, et elle n'aide ni à louer, ni à acheter, ni à s'abonner. « Presque. » est un écho en faux suspens. Et c'est 45 mots là où il faut en couper 100.

**Correction** : coupé. La jauge des cinq heures enchaîne directement sur l'appel à l'abonnement, qui y gagne : « le seul que je te demande de garder […] lui, il ne te rationne pas ».

### 6. Les dates seront fausses le 4 janvier

> « Je les ai relevés le vingt-trois octobre, au moment où j'écris ce script. »
> « Et cet été, elle est même descendue à mille deux cents euros. Aujourd'hui, mille neuf cents minimum. »

**Pourquoi ça coince** : la vidéo sort le 4 janvier et tu la voices pendant les fêtes. « Au moment où j'écris ce script » ne se dit pas à voix haute, et « cet été », en janvier, c'est l'été qui vient. Les dix lignes `[PRIX À RELEVER LE 2/01/2027 …]` sont justes, mais éparpillées : rien ne dit quoi refaire si un prix bouge.

**Correction** (appliquée) : la date du relevé est un crochet dans la voix et sur le bandeau ; « l'été dernier » ; les dix lignes deviennent des renvois `[RELEVÉ R1]` à `[RELEVÉ R10]` vers une seule liste en annexe (« Relevé avant la voix »), qui dit pour chaque prix quelles sections changent. Les phrases à chiffres sont isolées : si un prix bouge entre ta voix et le 2/01, tu ne réenregistres qu'elles. Un contrôle CRE (R8) est ajouté : le montant du 1er février peut être publié avant ta voix, et la phrase « pas encore publié » deviendrait fausse.

### 7. La location arrive en « et ensuite »

> « Il reste une troisième route, et c'est celle que presque personne ne calcule. »

**Pourquoi ça coince** : après le retournement de 8:13, « il reste » ouvre un chapitre de plus au lieu d'une conséquence. Et « presque personne ne calcule » est une généralisation que `sources.md` ne tient pas (on sait seulement qu'aucune vidéo française ne compare les trois routes).

**Correction** (appliquée) : la section 5 se termine sur le pont « Sauf qu'on n'a regardé que deux routes sur trois », et la section 6 récolte le taximètre planté dans le hook : « La troisième, c'est le taximètre du début. »

### 8. Les rafales de chiffres (axe 10)

Le compte est bon (2,1 liaisons pour 100 mots, au-dessus de la cible de 1,5), mais trois passages empilent des chiffres sans liaison ni réaction :

> « Vingt dollars au taux du jour, plus vingt pour cent de TVA : environ vingt et un euros par mois, d'après mon calcul. Le Max à cent dollars, environ cent sept euros. Et le Max à deux cents, environ deux cent quatorze euros. »

→ deux conversions dites, la troisième à l'écran.

> « Le tarif bleu d'EDF, option Base, c'est vingt centimes le kilowattheure, depuis le premier août. Pour la consommation, NVIDIA annonce trois cent soixante watts pour la carte. Moi, je prends trois cent cinquante watts pendant qu'elle écrit. Une hypothèse, pas une mesure. »

→ la phrase NVIDIA sort (n° 4) ; reste un fait, l'hypothèse, puis « Du coup… huit euros quarante » et la réaction « Ouais ».

> « Scaleway loue une carte L4 de vingt-quatre gigas, plus que ma 5080, à soixante-dix-neuf centimes de l'heure hors taxes. Avec la TVA, environ cent quatorze euros pour cent vingt heures. Chez OVHcloud, il y a moins cher, trente-six centimes de l'heure hors taxes. »

→ une réaction entre les deux hébergeurs : « Là, tu paies plus qu'un Max. » (113,76 € contre 107,10 €). Et « plus que ma 5080 » devient « plus de mémoire que ma 5080 » : la L4 a plus de mémoire, rien dans `sources.md` ne dit qu'elle est plus puissante.

**Les « Bref »** : quatre dans la V1 (« Bref, si un chiffre… », « Bref, l'entrée de gamme… », « Bref, pour un usage à vingt euros… », « Bref, louer… »). Le garde-fou du skill : varier. `script.md` en garde trois et remplace celui du verdict par « Alors ». Le compte final : 35 liaisons pour 1 760 mots, **2,0 pour 100** (`controle.py`).

### 9. Les tics d'IA

| Passage | Problème | Dans `script.md` |
|---|---|---|
| « c'est presque un cadeau. Presque. » | Écho en faux suspens | Coupé avec les 13 $ (n° 5) |
| « Sauf qu'il y a un piège dedans. » | Annonce sans rien livrer | Remplacé par la réserve dite et le taximètre (test des 30 s) |
| « Bon. On a tout. Maintenant, on pose le calcul. » | Annonce de remplissage | Coupé : la balance à l'écran suffit |
| « Mais ce calcul repose sur une égalité que je n'ai pas encore vérifiée. » | Faux suspens, et « égalité » ne se comprend pas à l'oral | « Sauf qu'on n'a regardé que deux routes sur trois. » |
| « Voilà pourquoi la bonne question, en janvier, c'est plutôt : de quel modèle j'ai vraiment besoin ? » | Reformulation « la vraie question », proche de la fausse opposition, et morale de fin | « Alors avant de couper ou d'acheter quoi que ce soit, demande-toi de quel modèle tu as vraiment besoin. » |
| « c'est celle que presque personne ne calcule » ; « sous toutes les vidéos anglaises » | Généralisations | Coupée ; ramenée au commentaire relevé (n° 3) |
| « Sur le papier, c'est le rêve. » | Cliché léger | Gardé : il prépare le « sauf que », et c'est du français parlé |
| « C'est une hypothèse, pas une mesure. » | Opposition | Gardée : c'est la règle 4 du calculé, une vraie distinction que le spectateur doit entendre |

### 10. Le spectateur ne se situe jamais

**Pourquoi ça coince** : la vidéo est faite de profils, et personne n'est invité à choisir le sien avant le verdict.

**Correction** (légère, appliquée) : « Ça dépend de ce que tu paies aujourd'hui, et de ce que tu demandes à l'IA. Repère ton profil. » ; et l'appel final demande les deux informations utiles à la suite : « tu paies combien aujourd'hui, et quel modèle je calcule ensuite ? ».

## La rétention

- **Hook** : question au 57e mot, réserve à 0:23, pont à 0:35. 🟢
- **0:30-1:30** : la V1 passe une minute sur la méthode (sources, dates, BCE), au moment où ArtCraft perdait le plus. `script.md` la ramène à 40 s : le rappel de Coût Claude et ton enjeu d'abord, puis une phrase de sources, la date, et la blague du patch de jeu. La liste des trois routes sort (elle est déjà dans la question du hook).
- **Relances** : 22 en V1 (une toutes les 35 s), 28 dans `script.md` (une toutes les 26 s). Plus long trou : 1:38-2:31 (53 s), la conversion en euros, tenue par le calcul ligne par ligne à l'écran.
- **Ponts** : « Sauf qu'on n'a regardé que deux routes sur trois » (fin de la section 5) et « Mais louer ou acheter quoi, au juste ? » (entrée de la section 7) remplacent « Il reste une troisième route » et l'égalité non vérifiée.
- **Appel à l'abonnement** : V1 à 3:30 (27 %), `script.md` à 2:48 (23 %, environ 24 % avec tes ajouts). Au même endroit, sur la jauge des cinq heures. 🟢
- **Relance forte** : V1 à 8:13 (63 %), le piège ; `script.md` à 7:59 (66 % sans tes ajouts, environ 63 % avec), la frise où la location reste sous l'achat, avec la coupure musicale.
- **Durée** : V1 1 876 mots (12:56 à 145) ; `script.md` 1 760 mots (12:04 à 145). Avec tes ~125 mots d'ajouts : environ 13 min à 145, 10 min 30 en coupes serrées.

## Ce que le rédacteur a signalé

| Signalement | Décision |
|---|---|
| Tes ajouts (~100 à 150 mots) font passer la vidéo au-dessus de 13 min : couper environ 100 mots | −116 mots net (environ 200 coupés, 80 ajoutés pour la location) : 13 $ par développeur, 3e conversion, « Bon. On a tout », phrase des 360 W, liste des trois routes, redite des « dix-neuf mois », doublon du commentaire épinglé, « Bref » du verdict |
| Les lignes `[PRIX À RELEVER LE 2/01/2027]` | Gardées sur le fond, regroupées en une liste R1 à R10 en annexe, avec ce qu'il faut refaire pour chaque prix ; contrôle CRE ajouté (R8) ; question 5 : la date de ta voix |
| Les 350 W restent une hypothèse ⟦mesure de Claude #1⟧ | Oui, et désormais pour **tout le PC** (fait 19), puisque la mesure se fera à la prise ; la phrase des 360 W de NVIDIA sort (n° 4). La sensibilité est dite : un à deux mois contre un Max |
| OpenRouter en 4e route, ou un autre épisode ? | **Un autre épisode.** Trois raisons : (1) on change d'unité (le prix au million de tokens demande une hypothèse de volume que ni toi ni `sources.md` n'avez, alors que les trois routes se comparent en heures) ; (2) c'est 100 à 150 mots de plus quand il faut en couper 100 ; (3) louer le modèle passe par une clé d'API chez un intermédiaire qui envoie tes requêtes à d'autres fournisseurs : le recommander irait contre ta règle de ne jamais coller une clé d'API dans un outil tiers. Le prix vérifié (0,20 $ / 2,50 $ par million de tokens, fait 21) reste dans `sources.md` pour plus tard |
| « comme moi » dans le verdict : tu joues sur ta 5080 ? | Rien dans les sources ni dans tes brouillons ne le dit : la phrase garde « parce que tu joues dessus » et « comme moi » devient un crochet à confirmer (question 4). Pas d'anecdote inventée |

## Vérification des faits du script

Chaque phrase de la V1 qui affirme quelque chose, contre `sources.md` (colonne « 2e vérif ») ou, à défaut, la source primaire relue aujourd'hui.

| Phrase de la V1 | Fait | Verdict | Dans `script.md` |
|---|---|---|---|
| « Plus de dix ans. C'est le temps qu'il faut à une RTX 5080… » | calcul, #23 | ⚠️ c'est un calcul, dit comme un fait | « D'après mon calcul, c'est le temps qu'il faut… » |
| « Contre l'abonnement à cent dollars, environ dix-neuf mois. Et contre celui à deux cents, neuf mois. » | calcul | ✅ (19,3 et 9,2) | 19 mois dits, 9 mois à l'écran |
| « Je n'ai pas fait tourner Claude chez moi » | #20 | ✅ | « ma carte ne fait pas tourner Claude » |
| « je t'avais promis cette vidéo pour le quatre janvier » | `cout-claude-local/script.md` | ✅ (« j'en fais une vidéo complète le quatre janvier ») | gardé |
| « Tous les prix viennent de boutiques et d'hébergeurs français, ou de la page officielle quand il n'y a pas d'euros » | tableau des prix | ✅ (Vast.ai : API publique, en dollars) | raccourci, même sens |
| « Je les ai relevés le vingt-trois octobre, au moment où j'écris ce script » | tableau des prix | ⚠️ vrai aujourd'hui, faux à la voix | « Je les ai relevés le [DATE DU RELEVÉ] » |
| « Claude Pro, c'est vingt dollars par mois » | #1 | ✅ | gardé |
| « cinq fois l'usage de Pro, à cent dollars, et vingt fois, à deux cents dollars, d'après le centre d'aide d'Anthropic » | #2 | ⚠️ le 200 $ vient du centre d'aide lu en résumé ; réessayé le 23/10 : toujours 404 à notre outil, et la recherche web ne donne que des résumés | gardé avec « d'après le centre d'aide », R2 à relire |
| « il n'y a pas un seul euro sur cette page » | #4 | ✅ | gardé |
| « en petit, « les prix n'incluent pas les taxes » » | #1 | ⚠️ citation inexacte : « Les prix affichés n'incluent pas les taxes applicables » | citation exacte |
| « environ vingt et un euros […] cent sept […] deux cent quatorze » | #4, #5 | ✅ calcul dit comme tel | deux dits, trois à l'écran |
| « Le vrai prix, tu ne le vois qu'à la caisse. » | #4 | ✅ (claude.ai/upgrade avant paiement) | gardé |
| « ChatGPT Plus est à environ vingt-trois euros, d'après la presse » | #6 | ✅ formulation de la 2e vérif | gardé |
| « l'entrée de gamme, partout, tourne autour de vingt euros » | #4, #6 | ⚠️ « partout » = deux services | coupé |
| « Les abonnements ont des limites sur une fenêtre glissante de cinq heures, et les formules payantes ajoutent des limites à la semaine » | #3 | ✅ pour Claude seulement | « Claude te limite sur une fenêtre glissante de cinq heures… » |
| « tu es rationné à la journée » | #3 | ❌ cinq heures et semaine | « rationné toutes les cinq heures » |
| « en entreprise, Claude Code coûte en moyenne treize dollars par développeur et par jour actif » | #8, #24 | ✅ formulation juste, mais hors sujet | coupé (n° 5) |
| « la RTX 5080 la moins chère est à 1 899,95 €, chez LDLC et chez Materiel.net » | #10 | ✅ | « presque mille neuf cents euros », exact à l'écran |
| « annoncée à mille cent soixante-dix-neuf euros à sa sortie, en janvier deux mille vingt-cinq, d'après la presse » | #11, #26 | ✅ formulation de la 2e vérif | gardé |
| « cet été, elle est même descendue à mille deux cents euros. Aujourd'hui, mille neuf cents minimum » | #11, #25 | ⚠️ formulation juste en octobre ; en janvier, c'est « l'été dernier » (le comparateur n'affiche pas l'année, et son historique est court : « pas assez de données ») | « l'été dernier » ; « Aujourd'hui… » coupé (redite) |
| « le premier PC complet avec une 5080 chez LDLC est à 4 049,95 € » | #12 | ✅ (PC fixe ; portables écartés) | « PC fixe », arrondi à 4 050 € |
| « C'est la question qui revient sous toutes les vidéos anglaises, parce qu'elles calculent avec un kilowattheure américain » | `sources.md` « Questions que se pose le public » (d'après `etudes/kai.md`) | ❌ « toutes » ; ✅ un fil de 135 likes et 44 réponses sous une vidéo de Kai, qui raisonne avec 15 cents le kWh | « Sous une grosse vidéo anglaise sur l'IA en local, c'est un des commentaires les plus discutés, parce qu'elle calcule avec un prix américain » |
| « vingt centimes le kilowattheure, depuis le premier août » | #17 | ✅ | gardé |
| « NVIDIA annonce trois cent soixante watts pour la carte » | #9 | ✅, mais contredit l'hypothèse PC complet (n° 4) | coupé |
| « je prends trois cent cinquante watts pendant qu'elle écrit. Une hypothèse, pas une mesure. » | #19 | ⚠️ la fourchette du fait 19 est celle d'un PC complet | « pour tout le PC pendant qu'il écrit » |
| « huit euros quarante […] seize euros quatre-vingts » ; « de sept à vingt-deux euros par mois » | #22 | ✅ | gardé |
| « une erreur sur les watts change le résultat d'un ou deux mois au plus » | #27 | ✅ contre un Max seulement (contre Pro, de 134 à 179 mois) | « contre un Max, … » |
| « le prochain mouvement du tarif tombe le premier février deux mille vingt-sept, quatre semaines après cette vidéo, d'après la CRE. Le sens et le montant ne sont pas encore publiés » | #17, #18 | ✅ au 23/10 ; ⚠️ peut être publié avant ta voix | gardé, + R8 |
| « cent sept euros moins huit euros quarante, ça laisse quatre-vingt-dix-huit euros » | calcul | ✅ (98,70) | « à peu près quatre-vingt-dix-neuf » (plus proche) |
| « Mille neuf cents divisés par treize, ça fait cent quarante-six mois. Plus de douze ans. » | calcul | ✅ (12,2 ans) | gardé |
| « quarante et un mois. Presque trois ans et demi. » | calcul | ✅ (3,4 ans) | gardé |
| « à mille deux cents euros cet été, le seuil […] tombait à environ douze mois. Un tiers de moins » | calcul | ✅ (12,2 ; − 37 %) | « l'été dernier » |
| « la carte se rembourse en un an et demi au plus » | calcul | ❌ 21 mois à 240 h, 41 avec le PC | « environ » |
| « Et aucune carte de particulier ne le fera, parce que ses poids ne sont pas publics » | #20 | ⚠️ « ne le fera » est une prédiction | « tant qu'Anthropic ne publie pas ses poids, aucune carte de particulier ne le fera tourner » |
| « le Qwen de vingt-sept milliards de paramètres pèse environ seize gigas en quatre bits. Il tient tout juste dans la carte. » | #20 | ✅ formulation de la 2e vérif | gardé |
| « Je l'ai testé dans l'épisode un de « Claude ou mon PC ? » » | calendrier (sortie le 2 nov.) | ✅ à condition que Claude #1 sorte avec un essai ; le résultat reste ton ⟦à écrire⟧ | gardé |
| « plus de trente mille euros par mois de serveur » | Coût Claude S12 | ⚠️ location, calcul (30 660 € HT) | « plus de trente mille euros par mois, rien que pour louer le serveur », après « j'en ai fait le calcul » |
| « celle que presque personne ne calcule » | « Ce qui existe en français » | ❌ généralisation | coupé |
| « sur Vast.ai, une RTX 5080 […] se loue dès trente centimes de dollar de l'heure. Environ vingt-sept centimes d'euro. » | #16 | ✅ formulation de la 2e vérif, datée à l'écran | gardé |
| « il change d'une heure à l'autre » | #16 | ⚠️ la source dit « set by supply and demand », pas « d'heure en heure » | « il bouge avec l'offre et la demande » |
| « environ trente-deux euros. À l'offre médiane, environ cinquante. » ; « soixante-dix-neuf mois […] quarante-cinq » | calcul | ✅ | gardé |
| « Tu paies les heures où la carte travaille, et rien les autres jours. » | absent de `sources.md` → doc de Vast.ai lue le 23/10 | ⚠️ on paie tant que la machine est **allumée** (pas seulement quand elle écrit), et le stockage même arrêtée | ligne 28 ajoutée à `sources.md` ; « Tu paies à la seconde tant que la machine est allumée, même quand elle n'écrit rien. Et le stockage se paie en continu, même machine arrêtée, d'après la doc de Vast.ai. » |
| « Scaleway loue une carte L4 de vingt-quatre gigas, plus que ma 5080 » | #9, #14 | ⚠️ « plus » de mémoire seulement | « plus de mémoire que ma 5080 » |
| « environ cent quatorze euros pour cent vingt heures » | #14, calcul | ✅ (113,76 €) | gardé, + « Là, tu paies plus qu'un Max » (calcul : 113,76 > 107,10) |
| « trente-six centimes de l'heure hors taxes. Sauf que c'est une Quadro RTX 5000 de deux mille dix-huit » | #13 | ✅ | gardé |
| « Sauf qu'à trente-deux euros, tu as dépassé le prix de Pro » | calcul | ✅ | gardé |
| « la location te coûterait plus cher dès quelques heures par jour » | calcul | ✅ mais vague | « dès deux heures par jour, environ » (51 à 79 h par mois, ligne 29) |
| « loue une 5080 quelques heures, pour trois fois rien » | calcul | ✅ (0,27 à 0,42 € de l'heure) | remplacé par le profil « commence par louer » chiffré |
| « parce que tu joues dessus, comme moi » | aucun | ❓ vécu non donné | crochet à confirmer |
| « huit euros par mois pour quatre heures par jour » | #22 | ✅ (hypothèse 350 W) | gardé |

**Faits ajoutés à `sources.md`** : ligne 28 (facturation de Vast.ai, doc lue le 23/10) ; ligne 29 (calcul refait au grill : sensibilité à 300 W et 240 h, frise sur 36 mois, seuil location contre Pro).
**Retirés ou reformulés** : « rationné à la journée », « au plus », « toutes les vidéos anglaises », « presque personne ne calcule », « plus que ma 5080 », « d'une heure à l'autre », les 360 W, les 13 $ par développeur, « l'entrée de gamme, partout », « cet été », « au moment où j'écris ce script », la citation inexacte d'Anthropic, « comme moi » (en crochet).

## Ce qu'il faut garder

- **« Plus de dix ans. »** : le chiffre d'ouverture est le bon, contre-intuitif et vrai.
- **« Il est gratuit, et il ne te rationne pas. »** : l'appel à l'abonnement le plus naturel de la chaîne, branché sur la pique des cinq heures.
- **« le prix d'une carte graphique bouge plus vite qu'un patch de jeu »** : ton humour gamer, et ça justifie la date à l'écran.
- **« Huit euros. Ouais, c'est moins que ton abonnement le moins cher. »** : la réaction après le chiffre, exactement ce que demande l'axe 10.
- **La Quadro RTX 5000 de 2018 « qui n'a rien d'une 5080, malgré le nom »** : un vrai piège de catalogue, démasqué avec un gag visuel.
- **Le pari sur le prix de la carte**, planté en section 3 et récolté à 12 mois : la meilleure graine de la vidéo.
- **Les compteurs du hook** remplis puis barrés d'astérisques : la boucle visuelle tient la vidéo d'un bout à l'autre.
- **« On compare des prix, pas des services »** dans les hypothèses : c'est ce qui manque à « Apple Just Killed AI Subscriptions Forever ».

## Plan d'action (appliqué dans `script.md`)

1. **Verdict** : la location devient la route la moins chère du profil Max à 4 h par jour, et la relance forte (n° 1).
2. **Hook** : « d'après mon calcul », la réserve « 16 Go » à 0:23, le taximètre en pont (n° 2, test des 30 s).
3. **Faits** : les reformulations du tableau ci-dessus, la ligne 28 dans `sources.md` (n° 3, 4).
4. **Coupes** : 13 $, 3e conversion, remplissage, redites (−116 mots net) ; les relevés regroupés (n° 5, 6).
5. **Avant la voix** (toi) : ton enjeu, le résultat de Claude #1, la mesure au wattmètre, la liste R1 à R10.

## Les questions pour toi

Elles sont reprises en bas de [`script.md`](script.md) :
1. Ton enjeu (section 1) : quel abonnement paies-tu vraiment, et à quel palier ?
2. Tes heures : combien d'heures par mois ta 5080 écrirait-elle ? Loin de 120 h, le verdict « louer d'abord » peut basculer.
3. La mesure au wattmètre, à la prise, est-elle faite ?
4. « Comme moi » : tu joues sur ta 5080 ?
5. La date de ta voix : avant ou après le 2 janvier ?
6. Ce que tu as payé ta 5080, et quand (optionnel).
7. La blague des douze ans : une carte d'il y a douze ans que ton public connaît ?
8. **Hors de ce script** : *Combien coûte Claude en local ?* (16 nov.) donne le Max à 89 € **sans TVA** ; ici, il est à 107 € **avec**. On passe Coût Claude en TTC avant sa sortie ?
