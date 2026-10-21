# Grill du script OpenCode v1 (20/10/2026)

> Script grillé : [`script-v1.md`](script-v1.md). Grille : `youtube-script-grill`, mode B. Résultat : [`script.md`](script.md) (v2).
> Hypothèses : titre *OpenCode s'est fait pirater : pourquoi tes clés API valent de l'or*, miniature « ok » + « −2,15 $ » (voir [`fiche.md`](fiche.md)). Public : 18-34 ans, 63 % d'Afrique francophone, beaucoup de devs ou d'apprentis devs venus des tutos Flutter. Objectif : une vidéo d'actu qui se distingue de Code Bear et de Kai par l'ingénierie de la faille.
> Seule base factuelle : [`sources.md`](sources.md), vérifié le 20/10. Les numéros de ligne renvoient à `script-v1.md`.
> Comptage : la v1 annonce 1 777 mots. Mon script en trouve 1 770 en comptant tout ce qui est séparé par des espaces (guillemets et deux-points isolés compris), et 1 691 vrais mots. La v2 en a 1 449 avec la première méthode et 1 373 avec la seconde.

## Verdict

Le squelette tient. Le fil rouge du « ok » à moins deux dollars quinze est une vraie énigme, la section 3 apporte exactement ce que les vidéos anglaises n'ont pas (la colonne `credentials`, le `slice(-8)`, le hash impossible), et la checklist finale donne au spectateur quelque chose à faire le soir même.

Le plus gros problème est factuel, et il est grave pour une vidéo d'actu : sans jamais l'écrire, le script désigne deux coupables que `sources.md` interdit de nommer. Le « ok » en chinois, puis les « trois labos chinois » et les « entreprises chinoises », font conclure « c'est la Chine ». L'e-mail sur « l'ancien système », puis le commit « cinq jours avant », font conclure « c'est ce commit ». Le deuxième problème : on n'entend pas encore ta voix. Il n'y a ni toi, ni enjeu perso, et un seul gag gamer.

C'est réparable sans changer la structure. Il faut recaler une dizaine de phrases sur les sources, couper la chronologie que Code Bear a déjà faite, et réordonner la section 3 pour placer l'abonnement après la révélation du hash.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| Promesse | 🟠 | OpenCode n'est nommé qu'à 28 s (ligne 29), et « pourquoi tes clés valent de l'or » n'arrive qu'entre 57 et 79 % de la vidéo. |
| Alignement | 🟢 | Pas de vente forcée ; la checklist sert vraiment le spectateur. |
| Problème profond | 🔴 | Absent : le narrateur n'apparaît que dans le crochet de la fin (ligne 215), sans enjeu posé au début. |
| Public & complexité | 🟢 | Clé API sous-titrée, distillation expliquée par l'interro, hash expliqué par deux colonnes : la difficulté monte bien. |
| Valeur & originalité | 🟠 | La section 3 est la meilleure partie, mais elle arrive à 3:03, après 1 min 12 de chronologie que Code Bear a déjà racontée. |
| Structure & transformation | 🟠 | L'enquête est claire, mais l'ordre email → commit → avertissement fabrique une causalité, et l'abonnement tombe à 55 %. |
| Histoire | 🟠 | Une enquête avec une victime et un mystère, mais sans narrateur qui change d'avis. |
| Mais / donc | 🟠 | Bon dans la section 3 ; la section 2 est une suite d'heures (« et ensuite ») et la section 5 une liste « chez OpenAI / chez Anthropic / chez Google ». |
| Engagement actif | 🟠 | La boucle du « ok » est excellente, mais la question du hash (ligne 120) reçoit sa réponse une demi-seconde après. |
| Rythme & oralité | 🟢 | Phrases courtes, faites pour être dites, sans « vous ». |
| Tics d'IA | 🟠 | Dix-sept occurrences, dont une vraie fausse opposition (ligne 187) et un faux suspens en fin de vidéo (ligne 219). |

## Le grill

### 1. Le script désigne la Chine sans le dire

> « Dans ses logs, il publie une requête, écrite en chinois : « Réponds ok. » » (ligne 24)
> « En février, Anthropic a accusé trois labos chinois, DeepSeek, Moonshot et MiniMax… » (ligne 154)
> « des entreprises chinoises auraient aspiré des milliards de tokens aux modèles américains » (ligne 154)

**Pourquoi ça coince :** `sources.md`, « À NE PAS dire » : « Que l'attaquant est connu, que c'est la Chine, ou que la distillation est prouvée. » Aucune phrase ne l'affirme, mais l'enchaînement le fait. Le spectateur entend « requête en chinois », puis « labos chinois », puis « entreprises chinoises », et il conclut tout seul. En plus, ni « chinois » ni « américains » ne figurent dans les lignes de `sources.md` sur Anthropic (23/02) et sur l'avis AA26-251A. Et cet avis « ne parle pas de clés volées » : le citer au milieu d'une histoire de clés volées crée un lien qu'il ne fait pas. Avec 63 % de public africain, une vidéo qui laisse entendre « c'est les Chinois » sur un indice aussi mince serait aussi un mauvais signal pour la chaîne.

**Correction :** retirer toutes les nationalités, couper l'avis NSA/CISA/FBI (en réserve, avec sa nuance), et dire explicitement ce que vaut l'indice :
> Et une requête en chinois ne dit pas qui l'a envoyée. Au vingt octobre, OpenCode n'a publié ni le point d'entrée, ni le nombre de clés. On ne sait pas qui, ni pourquoi.

### 2. Le commit du 12/10 présenté comme une piste

> « Dans l'e-mail aux victimes, OpenCode parle d'un accès non autorisé à un « ancien système qu'on était en train de démanteler ». / Et dans le dépôt GitHub, on trouve un commit du douze octobre. Cinq jours avant. » (lignes 96-98)
> « Attention : rien ne prouve que le pirate est passé par là. […] Mais ça montre une chose : un « ancien système », ça peut encore contenir des clés bien vivantes. » (ligne 108)

**Pourquoi ça coince :** `sources.md` : « Rien ne relie ce commit à l'intrusion », et il ne faut pas dire « que le commit du 12/10 a causé la fuite ». Le script fait trois choses qui le suggèrent :
- il colle l'e-mail et le commit, avec « Cinq jours avant. » en phrase isolée, comme un indice ;
- l'avertissement n'arrive qu'après le gag du RPG, donc après que le spectateur s'est fait son idée ;
- la dernière phrase (« un « ancien système », ça peut encore contenir… ») reprend le mot de l'e-mail pour reparler du commit, et refait le lien que l'avertissement venait de défaire.

Petit souci de traduction en plus : « remove legacy database from Console » veut dire retirer la base *du code de la Console*. « Supprimer l'ancienne base », puis « Sauf que… », fait croire que le commit mentait.

**Correction :** l'avertissement d'abord, le titre du commit traduit fidèlement, pas de « cinq jours avant », et la scène sert de leçon de dev, pas d'indice (v2, section 3 bis) :
> Dans l'e-mail aux victimes, OpenCode parle d'un accès à un « ancien système qu'on était en train de démanteler ». Rien ne relie ce qui suit à ce système : OpenCode n'a pas dit par où le pirate est entré. Mais c'est un piège que tout dev devrait connaître.
> Le douze octobre, un commit retire l'ancienne base de données du code de la Console.

### 3. « Cinq jours avant », deux fois

> « un commit du douze octobre. Cinq jours avant. » (ligne 98)
> « Le douze octobre, cinq jours avant le piratage, Anthropic publie ses nouvelles défenses » (ligne 158)

**Pourquoi ça coince :** les deux événements datent du 12/10, et le script les rattache deux fois au piratage par le même compte à rebours. Ça construit un récit de cause à effet (« les labos ferment la porte, donc les pirates volent des clés ») qu'aucune source ne fait. Le raisonnement sur la protection du 31/08 peut rester, à condition d'être présenté comme ce qu'il est : une hypothèse sur ce qu'un pirate aurait intérêt à faire.
**Correction :** garder la date, retirer « cinq jours avant » aux deux endroits, et formuler la déduction sans l'attribuer à cette attaque : « Mais une de ces protections ne couvre que les comptes créés à partir du trente et un août. Le compte d'un vrai développeur, ouvert avant, passe à côté. »

### 4. Les chiffres de Max Weinbach : attribués, tronqués, prolongés

> « Max Weinbach ouvre son compte OpenAI. Trente-cinq millions de tokens. Huit mille neuf cent soixante-six requêtes. Et un solde à moins deux dollars quinze. » (ligne 20)
> « Le pirate a tout vidé, jusqu'à moins deux dollars quinze, et il s'est arrêté là. Le solde, c'était le plafond. » (ligne 189)

**Pourquoi ça coince :**
- `sources.md` liste « 35 026 055 tokens, 8 966 requêtes, crédit OpenAI à −2,15 $, 264,09 $ sur sa clé Anthropic, e-mail de Google ». Rien ne dit que les tokens et les requêtes s'affichaient sur le compte OpenAI : la v1 les y range.
- Les 264 $ de la clé Anthropic, la seule vraie perte en dollars, ont disparu.
- « Il s'est arrêté là » et « le solde, c'était le plafond » ne sont pas sourcés. On ne sait pas pourquoi l'usage s'est arrêté (révocation, blocage par le fournisseur, autre chose). Surtout, le chiffre dit l'inverse : le crédit est passé *sous* zéro, donc le compteur n'a pas coupé pile au plafond.

**Correction :** ne rien attribuer à un fournisseur en particulier, ajouter les 264 $, et tirer la vraie leçon du moins :
> Sur ses comptes, près de neuf mille requêtes. Son crédit OpenAI est à moins deux dollars quinze, et deux cent soixante-quatre dollars sont partis sur sa clé Anthropic.
> […] Regarde le moins deux dollars quinze de Max : son crédit est passé sous zéro. Le compteur ne coupe pas pile à zéro.

Avant le montage, vérifie sur sa capture à quel compte appartiennent les 35 M de tokens et les 8 966 requêtes (noté dans la v2).

### 5. Le « ok » : la nuance doit être dite, pas seulement respectée

> « Reviens au « ok » de Max Weinbach. On n'entraîne pas un modèle avec « réponds ok ». Ça ressemble plutôt à un test » (ligne 174)

**Pourquoi ça coince :** la v1 ne dit jamais « la première requête », c'est bien. Mais elle bâtit une conclusion sur une seule requête sans dire qu'elle est une sur 8 966. `sources.md` : Max la présente comme « a single logged request », « pas comme la première », et « ce n'est pas une preuve d'origine ». L'hypothèse du test de clé est de l'ingénierie honnête, à condition de montrer combien l'indice est mince.
**Correction :**
> Alors, ce « ok » ? Max l'a publié comme un exemple : une requête sur près de neuf mille, pas forcément la première. Seule, elle ne prouve rien. Mais on n'entraîne pas un modèle avec « réponds ok ». Ça ressemble plutôt à un test : est-ce que cette clé marche ?

### 6. Le narrateur n'existe pas

> « [TON AVIS EN 2 OU 3 PHRASES : est-ce que tu as déjà collé une clé dans un outil comme ça ?…] » (ligne 215)

**Pourquoi ça coince :** c'est la seule trace de toi en huit minutes, et elle arrive à 95 %. Pour une actu que Code Bear a déjà résumée à 170 000 vues, ton avantage, c'est un dev francophone qui lit le code *et* qui a peut-être collé ses propres clés quelque part. Le problème profond qu'on devine (« on colle nos clés partout parce que c'est pratique, ou pour éviter un abonnement de plus ») n'est ni posé ni résolu.
**Correction :** poser l'enjeu tôt et le résoudre à la fin. Deux crochets dans la v2 :
- section 1, après « bring your own key » : `[TOI, EN UNE OU DEUX PHRASES : est-ce que t'as déjà collé une clé API dans un outil comme ça ? Lequel, et pourquoi ? Si c'était pour éviter un abonnement de plus, dis-le, ça prépare la fin.]`
- fin : `[TON AVIS : reprends ta réponse de la section 1. Après avoir vu ce code, tu laisses ta clé dans ce genre d'outil, ou pas ?]`

La question est en bas de ce fichier. N'invente rien : si tu n'as jamais collé de clé nulle part, dis-le, c'est aussi une position.

### 7. L'abonnement à 55 %, la relance à 79 %

> « Placé à environ 55 % de la vidéo plutôt qu'à 25 % » (ligne 142)
> « Maintenant, le mot bizarre de l'annonce : distillation. » (ligne 150, à 57 %)

**Pourquoi ça coince :** compté au mot, l'abonnement tombe à 55,5 %, après la révélation du hash mais aussi après le commit et le RPG. La première vraie révélation (« pour afficher les huit derniers caractères… il faut avoir ta clé », puis « parce qu'ils ne peuvent pas ») arrive vers 45 %. À 57 %, au moment où on décroche d'habitude, le script ouvre un nouveau sujet (la distillation) au lieu de relancer. La seule coupure forte arrive à 79 % (ligne 184).
**Correction :**
- section 3 réordonnée : la colonne `credentials` et le hash d'abord, le commit ensuite (section 3 bis). L'abonnement tombe à 43 %, juste après « dans ce code-là, il n'y a pas de coffre » ;
- l'appel à l'abonnement prend ta pique : « Et c'est le seul abonnement qui ne te prélèvera jamais rien. » ;
- à 55 %, la musique coupe et le « ok » revient : « Il reste ma question du début : pourquoi payer, avec l'argent d'un autre, pour un « ok » ? »

### 8. Le hook confirme le clic trop tard

> « Samedi dix-sept octobre. Max Weinbach ouvre son compte OpenAI. […] Cette nuit-là, ce sont les clés d'un pour cent virgule quatre des utilisateurs de la Console d'OpenCode qui sont parties dans la nature. » (lignes 20-29)

**Pourquoi ça coince :** le titre et la miniature disent « OpenCode piraté », mais le mot n'arrive qu'à environ 28 s, et l'écran reste « sans titre, sans logo ». Le spectateur ne sait pas qui est Max Weinbach. Le hook fait 138 mots (47 s à ton débit) pour un plan à 35 s. Les trois chiffres en fragments (ligne 20) font une rafale de trois, et la bulle « ok » de la miniature n'apparaît qu'à la 3e phrase.
**Correction :** ouvrir sur la bulle, comme la miniature, et nommer OpenCode tout de suite :
> Cette requête est écrite en chinois. Elle dit : « Réponds ok. » Et l'IA a répondu : « ok ».
> Elle sort des logs de Max Weinbach, une des victimes du piratage d'OpenCode, le dix-sept octobre.

OpenCode est à l'écran à 3 s et dit à 9 s, la question « Pourquoi ? » tombe à 25 s, avant le seuil des 30 s.

### 9. La chronologie, c'est la vidéo de Code Bear

> lignes 64-88 : 212 mots, 1 min 12

**Pourquoi ça coince :** ta différence, c'est l'ingénierie de la faille, et la partie la plus longue avant le code est la frise horaire que tous les concurrents ont déjà faite. Dans le détail :
- « Google, lui, réagit tout seul : il envoie des e-mails pour dire qu'il a baissé les limites d'utilisation de certains comptes » (ligne 71) généralise un seul e-mail, celui de Max ;
- « Deux millions huit cent mille vues » (ligne 77) tronque 2,86 M ;
- « un pour cent virgule quatre » (ligne 29) et « un virgule quatre pour cent » (ligne 77) : choisis la seconde forme.

**Correction :** 130 mots, une capture par heure, l'info utile au spectateur ajoutée (Anthropic et Google bloquent les clés, OpenAI rembourse, d'après TechCrunch), et ta voix : « Max reçoit un e-mail de Google : ses limites ont été « temporairement abaissées ». Google a nerfé son compte. » Le passage sur Dax attaqué à son tour part en réserve.

### 10. Les seize millions qui invitent au faux calcul

> « D'après OpenCode, plus de seize millions de développeurs s'en servent chaque mois. Et deux jours avant le piratage, leur post […] faisait trois virgule sept millions de vues. » (ligne 45)

**Pourquoi ça coince :**
- Les seize millions concernent tout OpenCode, et la fuite touche 1,4 % de la *Console*. Un spectateur sur deux va calculer « 1,4 % de 16 M = 224 000 victimes », un chiffre que personne n'a donné.
- Trois minutes plus tard arrivent les « seize millions d'échanges » d'Anthropic (ligne 154) : deux « seize millions » sans rapport, faciles à confondre.
- Les 3,73 M de vues sont celles relevées le 20/10, pas celles du 15/10. « Faisait trois virgule sept millions de vues deux jours avant » est faux.
- Le paragraphe n'apporte rien au fil rouge.

**Correction :** en réserve, avec la phrase anti-calcul si tu le remets. La v2 garde les vingt-quatre mille faux comptes d'Anthropic et laisse tomber les seize millions d'échanges.

### 11. Petites inexactitudes

| Ligne | v1 | Problème | v2 |
|---|---|---|---|
| 56 | « Dax Raad, un des fondateurs, l'a écrit tout de suite » | Le rôle n'est pas dans `sources.md`. Et le post date de 21:38 UTC, soit 23 h 38 à Paris, trois heures et demie après l'annonce (heure décodée depuis l'identifiant du post) | « Le soir même, Dax Raad, d'OpenCode, a précisé » |
| 132 | « l'hébergeur de la base chiffre sûrement le disque » | `sources.md` : « reste possible » | « chiffre peut-être ses disques » |
| 75 | « Matt Johansen, qui suit la cybersécurité » | Description absente des sources | Supprimée |
| 174 | « Le chercheur Nathan Lambert l'a dit sans détour » | Rôle absent des sources, et formule creuse | « Nathan Lambert trouve ça « très bizarre » » |
| 162 | « avec un an d'historique » | Précision inventée | Remplacée par le seuil du 31/08, qui est sourcé |
| 199 | « une dizaine de minutes de retard » | La source dit « up to around 10 minutes » | « jusqu'à une dizaine de minutes » |
| 258 | fausse clé `sk-proj-…f1YA` | « f1YA » est la vraie fin d'une clé de victime, lue dans l'e-mail de suivi publié. Ça contredit ta propre règle (« jamais de vraie clé, même partielle »). En plus, le masque montre huit caractères à la fin, pas quatre | `sk-proj-Ab12Cd34…Wx98Yz76`, inventée de bout en bout |
| 219 | « je fais tourner des modèles sans aucune clé, sans facture » | Au calendrier, les premiers essais Qwen sont prévus la semaine du 26/10 : à confirmer. Et « sans facture » contredit ta future vidéo sur le coût du local (l'électricité) | « je peux faire tourner », un crochet `[À VÉRIFIER]`, et « La seule facture, c'est l'électricité. » |
| 219 | « C'est la question de ma prochaine série » | Pas de date, c'est bien. Mais « prochaine » peut s'entendre « prochaine vidéo », alors que la prochaine, c'est Uber | « la série « Claude ou mon PC ? », qui arrive sur la chaîne » |
| 54 | « pour que les serveurs d'OpenCode s'en servent à ta place » | Ce n'est pas dans `sources.md`, mais c'est la raison d'être d'une clé enregistrée (BYOK) | Présenté comme un principe d'ingénierie : « Un outil qui s'en sert à ta place doit pouvoir la relire. » |

### 12. L'argument du hash peut être plus tranchant

> « Une clé API, OpenCode doit l'envoyer à OpenAI à chaque requête, en entier. Une empreinte, OpenAI n'en fait rien. » (ligne 126)

**Pourquoi ça coince :** c'est juste, mais il manque la moitié qui fait dire « ah oui » aux devs : celui qui *fabrique* une clé peut très bien n'en garder qu'une empreinte, comme pour un mot de passe, parce qu'il n'a qu'à vérifier celle qu'on lui présente. C'est celui qui doit la *présenter* à ta place qui ne peut pas. Cette asymétrie explique tout le problème. C'est de l'ingénierie générale, aucun fait nouveau sur OpenAI.
**Correction :** une phrase, plus une devinette pour que le spectateur cherche avant d'avoir la réponse :
> Alors, toi qui codes : pourquoi ils ne l'ont pas hashée, comme un mot de passe ? Prends deux secondes.
> […] Le seul qui peut se contenter d'une empreinte, c'est celui qui fabrique la clé : il n'a qu'à vérifier celle que tu lui montres. Un outil qui s'en sert à ta place doit pouvoir la relire.

### 13. La fin retombe

> « Est-ce que ça peut remplacer Claude ? C'est la question de ma prochaine série, et la réponse risque de te surprendre. […] En attendant, si tu veux voir ce que Claude sait faire quand il est entre de bonnes mains, regarde comment un développeur a recréé sept logiciels Adobe avec lui. C'est juste ici. » (lignes 219-223)

**Pourquoi ça coince :** ta meilleure phrase (« la seule clé qu'on ne peut pas te voler, c'est celle que tu n'as pas ») est au milieu, puis viennent un faux suspens (« la réponse risque de te surprendre ») et une carte d'écran de fin. La vidéo finit sur une pub pour une autre vidéo.
**Correction :** l'avis perso, l'annonce de la série sans date, l'écran de fin en une phrase, et la phrase de la clé en dernier :
> En attendant, Claude entre de bonnes mains, c'est juste ici : un seul développeur, sept logiciels Adobe recréés.
> Et la seule clé qu'on ne peut pas te voler, c'est celle que t'as pas.

### 14. Ta voix : un seul gag gamer, pas d'argot, pas de pique sur les abonnements

La taverne du RPG (ligne 106) est le seul moment où on t'entend. Ajouts dans la v2, à garder ou à remplacer par tes vraies blagues :
- « Google a nerfé son compte. » (l'e-mail sur les limites abaissées) ;
- « Du farming, mais avec ta carte bancaire. » (les réseaux qui font tourner les clés volées) ;
- « Faut pas abuser. » (huit mille faux comptes) ;
- « Le pire abonnement de ta vie. » (le rechargement automatique qui paie pour le pirate) ;
- « le seul abonnement qui ne te prélèvera jamais rien » (l'appel à l'abonnement).

Le crochet `[TA BLAGUE ICI SI TU EN AS UNE]` (ligne 48) disparaît avec le bloc DeepSeek. Si tu as une blague sur le « ok » (un PNJ qui ne sait dire que ça ?), c'est l'endroit idéal, à 0:10.

## Les tics d'IA

| Ligne | Passage | Tic | v2 |
|---|---|---|---|
| 187 | « ce n'est pas le pirate qui décide combien tu perds. C'est ton plafond. » | Fausse opposition : personne ne pense que le pirate « décide » | « Le jour où elle fuit, combien tu perds dépend surtout d'un réglage : ton plafond. » |
| 219 | « et la réponse risque de te surprendre » | Faux suspens | Supprimé |
| 20 | « Trente-cinq millions de tokens. Huit mille… requêtes. Et un solde à… » | Rafale de trois fragments | Une phrase, deux chiffres |
| 31 | « on va l'ouvrir, voir comment…, et comprendre pourquoi… » | Triade | Deux promesses |
| 206 | « un vrai plafond, un petit solde, et pas de rechargement automatique » | Triade | « une vraie limite, et pas de rechargement automatique » |
| 45 | « Gratuit. Le mot qui fait sortir tout le monde de sa grotte. » | Fragment + formule toute faite | En réserve avec le bloc |
| 60 | « la nuit a été longue » | Cliché | « Les autres… » |
| 102 | « Résultat : quand tu effaces le code… » | Annonce | Supprimée |
| 71, 102 | « Google, lui, … », « Le mot de passe, lui, … La base, elle, … » | Tournure « X, lui, » répétée | Aucune dans la v2 |
| 108 | « Mais ça montre une chose : … » | Annonce + morale de fin de paragraphe | Supprimée (et elle refaisait le lien avec le commit) |
| 122 | « Parce qu'ils ne peuvent pas. » | Question et réponse immédiate | Devinette « Prends deux secondes » |
| 162 | « Tu vois le problème ? » | Faux suspens | Supprimé |
| 174 | « l'a dit sans détour » | Formule creuse | Supprimée |
| 178 | « La vérité, c'est qu'… » | Formule | « On ne sait pas qui, ni pourquoi. » |
| 189 | « Le solde, c'était le plafond. » | Morale (et non sourcée) | Supprimée |
| 193 | « La doc le dit noir sur blanc. » | Cliché | « c'est dans leur doc » |
| 217 | « Moi, j'en retiens une chose : » | Annonce de morale | La phrase de la clé seule, en dernier |

Tolérés, parce que ce sont de vraies oppositions dont le spectateur a besoin : « révoque ta clé chez le fournisseur, pas dans l'outil » (ligne 204, reformulé en v2), « on ne la hashe pas : on la chiffre » (ligne 130, juste après la question du hash), la citation de Dax « c'est la Console, pas OpenCode lui-même ». Il y a une seule morale assumée dans la v2 : « Une clé API, c'est une carte bancaire déjà branchée sur une IA. »

## Ce qu'il faut garder

- « Pour afficher les huit derniers caractères de ta clé… il faut avoir ta clé. » La meilleure preuve du script : un dev la comprend en une seconde, sans lire de SQL.
- « Une empreinte, OpenAI n'en fait rien. » Court, exact, et ça répond à la question que tout dev se pose.
- « Les garde-fous censés bloquer les pirates… bloquaient la victime. » Le seul vrai moment d'ironie de l'actu, et c'est sourcé (TechCrunch).
- La taverne du RPG pour la base seulement référencée. Elle porte une notion d'infra difficile, et c'est ton registre.
- « On n'entraîne pas un modèle avec « réponds ok ». » Le raisonnement d'ingénieur qui referme la boucle.
- « Une clé API, c'est donc une carte bancaire déjà branchée sur une IA. » La phrase-titre.
- « Pour être honnête : l'hébergeur… » Dire la limite de son propre argument rend crédible tout le reste.
- « Dix minutes, pour un script qui tourne à fond, c'est long. » et « Tout le monde en a une qui traîne d'un vieux tuto. » : ta voix.
- La checklist : concrète, faisable ce soir, et le point « révoque chez le fournisseur » est celui que les gens ratent.

## Plan d'action

1. **Faits** (n° 1 à 5, 10, 11) : nationalités, commit, « cinq jours avant », chiffres de Max, nuance du « ok ». Fait dans la v2.
2. **Section 3 réordonnée** (n° 7, 12) : credentials → hash → abonnement → commit. Fait.
3. **Hook et chronologie** (n° 8, 9) : la bulle « ok » en ouverture, OpenCode dit à 9 s, chronologie à 130 mots. Fait.
4. **Toi** (n° 6, 14) : réponds à la question ci-dessous, remplis les deux crochets, remplace mes blagues par les tiennes si elles sonnent faux.
5. **Avant la voix** : vérifie sur la capture de Max à quel compte appartiennent les chiffres. Regarde si OpenCode a publié un post-mortem (sinon, « au vingt octobre » reste juste). Dis-moi si tu as déjà fait tourner un modèle sur la 5080.

## Ce que la v2 coupe, et pourquoi

| Bloc | Mots | Pourquoi |
|---|---|---|
| Chronologie (section 2) | 212 → 130 | Code Bear et Kai l'ont faite ; on garde les heures et le gag de Dax |
| Seize millions + post DeepSeek | ~50 | Faux calcul possible, confusion avec les 16 M d'échanges, vues datées du 20/10 (réserve) |
| NSA, CISA, FBI | ~30 | Nationalités non sourcées, et l'avis ne parle pas de clés volées (réserve) |
| Dax attaqué à son tour | ~25 | Anecdote secondaire (réserve) |
| 90 à 99 % de récolte en moins | ~15 | Seul le bannissement en deux heures sert le raisonnement |
| Sceptiques de TechCrunch | ~10 | « Overstretch » sans objet précis ; Lambert suffit |
| Paliers Gemini à 250 $ | ~15 | Le retard de facturation suffit à la démonstration |
| Doublons de la section 5 (« le solde, c'était le plafond », « noir sur blanc »…) | ~40 | Tics ou faits non sourcés |
| Hook | 138 → 118 | Rafale de chiffres resserrée, une promesse en moins |

Ajouts : environ 60 mots (les 264 $, la phrase sur la langue de la requête, l'asymétrie du hash, la devinette, la relance à 55 %, Anthropic et Google qui bloquent, OpenAI qui rembourse, le conseil d'Anthropic aux gens sans e-mail).

## Faits vérifiés le 20/10

Tous les faits de la v2 viennent de `sources.md`. Les heures des posts sont décodées depuis leurs identifiants : Matt Johansen 15:30 UTC, Max Weinbach 18:01 UTC, OpenCode 18:08 UTC, Dax (ses comptes perso) 18:41 UTC, Lambert 20:08 UTC, Lydia Hallie 21:04 UTC, Dax (« c'est la Console ») 21:38 UTC. Les trois premières correspondent à `sources.md`.

| Fait de la v2 | Verdict | Source (`sources.md`) |
|---|---|---|
| « 请回复ok » → « ok », une requête parmi d'autres | ✅ « a single logged request », pas la première | Max Weinbach, 2111518091360575677 |
| Près de neuf mille requêtes, −2,15 $ chez OpenAI, 264 $ chez Anthropic, e-mail de Google | ✅ 8 966 ; 264,09 $ ; « temporarily lowered the allowed usage limits » | Max Weinbach, 2111518053662064829 |
| Exposition possible dès 2 h 30 (Paris) | ✅ 00:30 UTC, e-mail de suivi | Captures Johansen / Weinbach |
| 17 h 30, « Confirmé. OpenCode piraté. Clés volées. » | ✅ | Matt Johansen |
| 20 h, « distillation à grande échelle », 1,4 % de la Console, pas d'e-mail = pas touché | ✅ 18:08 UTC | Post d'OpenCode |
| Anthropic et Google bloquent, OpenAI rembourse ; Dax « un peu frustrant » | ✅ rapporté par TechCrunch | TechCrunch, 19/10 |
| « C'est la Console, pas OpenCode lui-même. Ces clés-là ne nous arrivent jamais. » | ✅ traduction fidèle, sans « serveurs » ni « appli locale » entre guillemets | Dax, 2111572618340188393 |
| Table `provider`, colonne `credentials` en texte, valeur insérée telle quelle ; masque 8 + 8 | ✅ pas de chiffrement dans le code ; chiffrement au repos possible | Commit parent 773d862 |
| Commit du 12/10 qui retire la base du code ; base seulement référencée ; mot de passe géré, supprimé au déploiement | ✅ sans lien établi avec l'intrusion | b9ca4d2 |
| « Ancien système qu'on était en train de démanteler » | ✅ | E-mail aux victimes |
| DeepSeek, Moonshot, MiniMax, ~24 000 faux comptes | ✅ sans nationalité | Anthropic, 23/02/2026 |
| Défenses du 12/10, bannissements souvent en moins de deux heures, protection limitée aux comptes créés à partir du 31/08 | ✅ | Anthropic, 12/10/2026 |
| Vol de clés devenu « le seul objectif » de plusieurs groupes ; clés qu'on fait tourner jusqu'à les vider | ✅ | Rapport de menace, septembre 2026 |
| 8 000 faux comptes, 480 000 $ par mois, en juillet | ✅ sans lien avec la fuite (dit dans le script) | Dax, 2079248759439884453 |
| Nathan Lambert, « très bizarre », « looped » | ✅ | 2111549984373911572 |
| Pas de point d'entrée ni de nombre de clés au 20/10 | ✅ à recontrôler avant la voix | « À NE PAS dire » |
| Les alertes OpenAI ne bloquent pas ; la limite n'est pas instantanée | ✅ | Doc OpenAI |
| Prépayé, rechargement auto, 500 $ au premier palier, 200 000 $ en haut | ✅ Start / Scale | Doc Anthropic |
| Gemini, facturation jusqu'à environ 10 min de retard | ✅ | Doc Gemini |
| Anthropic conseille de créer une nouvelle clé par prudence | ✅ « If you saved a key in OpenCode and want to be extra careful… » | Lydia Hallie |

Hors `sources.md`, mais de la connaissance d'ingénierie générale : la description d'OpenCode (agent de code dans le terminal), le principe du BYOK, le hash des mots de passe, le chiffrement avec une clé rangée dans un coffre, le fait que l'émetteur d'une clé peut n'en garder qu'une empreinte, la distillation expliquée, et le fait que supprimer une clé d'un outil ne la révoque pas chez le fournisseur. « Sept logiciels Adobe » vient de ta vidéo ArtCraft.

## La question

As-tu déjà collé une de tes clés API (OpenAI, Anthropic, Gemini…) dans un outil tiers, une extension ou un projet de tuto ? Si oui : lequel, pourquoi (pratique ? éviter un abonnement de plus ?), et as-tu réglé une limite ? Sinon, pourquoi tu t'en es toujours méfié ? C'est ce qui manque pour donner un enjeu au narrateur (n° 6). Les crochets de la section 1 et de la fin sont prévus pour ta réponse.
