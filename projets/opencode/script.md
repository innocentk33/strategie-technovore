# OpenCode piraté : script v2

**Titre** : *OpenCode s'est fait pirater : pourquoi tes clés API valent de l'or*

**Durée** : 1 373 mots de voix off (compte au script, crochets, visuels et sons exclus ; 1 449 avec la méthode de la v1, qui compte aussi les guillemets et deux-points isolés). À 175 mots/min, ton débit en coupes serrées sur Uber : environ 7 min 50 de voix, plus environ 30 s de pauses au montage et l'écran de fin, soit environ 8 min 20. Les timecodes ci-dessous sont calculés à 175 mots/min, sans les pauses ; à recaler sur la vraie prise.

**Fil rouge** : un « ok » à moins deux dollars quinze. Boucle ouverte dans le hook (« pourquoi payer pour un "ok" ? »), relancée à 55 %, refermée dans la section 4.

**Angle Technovore** : l'ingénierie de la faille. Ce que Code Bear et Kai n'expliquent pas : pourquoi on ne peut pas hasher une clé API, alors qu'on hashe un mot de passe.

**Changements depuis la v1** (détails dans [`grill-v1.md`](grill-v1.md)) :
- faits recalés sur [`sources.md`](sources.md) : plus aucune nationalité (« labos chinois », « entreprises chinoises », « modèles américains » ne sont pas dans les sources, et collés au « ok » en chinois ils désignaient un coupable) ; la phrase « la requête est en chinois ne dit pas qui l'a envoyée » est ajoutée ;
- le commit du 12/10 n'est plus présenté comme une piste : l'avertissement passe avant l'explication, « cinq jours avant » disparaît (il était là deux fois), et le titre du commit est traduit « retirer… de la Console », pas « supprimer » ;
- chiffres de Max Weinbach : on ne dit plus que les 35 M de tokens viennent de son compte OpenAI, on ajoute les 264 $ de sa clé Anthropic, et « le pirate s'est arrêté là, le solde c'était le plafond » est retiré (non sourcé, et le crédit est passé sous zéro) ;
- « chiffre sûrement le disque » devient « peut-être » ; Dax n'écrit plus « tout de suite » (son post date de 23 h 38, trois heures et demie après l'annonce) et n'est plus « un des fondateurs » ;
- les seize millions de développeurs et le post DeepSeek passent en réserve : ils invitaient à faire un faux calcul (1,4 % de 16 M) et se mélangeaient avec les seize millions d'échanges d'Anthropic ;
- section 3 réordonnée : la colonne `credentials` et le hash d'abord, le commit ensuite. L'abonnement passe de 55 % à 43 %, juste après la révélation « ils ne pouvaient pas la hasher » ;
- vraie relance à 55 % : retour du « ok », coupure de musique ;
- hook : OpenCode à l'écran à 3 s et dit à 9 s, au lieu de 28 s dans la v1, la bulle « ok » en ouverture, comme sur la miniature ;
- ton enjeu perso (rempli le 20/10) : tu n'as jamais collé de clé API dans un outil tiers, et tu fais très attention ; la fin y renvoie ;
- 20/10 : la protection du 31/08 est présentée comme une **hypothèse**, pas comme un fait ; la 5080 reste au conditionnel (« je peux ») parce que rien n'a encore tourné dessus ; pas de post-mortem d'OpenCode au 20/10 ;
- **durée après ces ajouts** : environ 1 440 mots au compte de la v2 (1 516 avec la méthode de la v1), soit environ 8 min 15 de voix, et 8 min 45 avec les pauses ;
- ta voix : Google qui « nerfe », le farming de clés, « faut pas abuser », une pique sur les abonnements dans l'appel à l'abonnement et dans le rechargement automatique ;
- la fin ne promet plus une réponse « qui risque de te surprendre », ne dit plus « sans facture » (il reste l'électricité), et finit sur la phrase de la clé qu'on ne peut pas voler ;
- fausse clé à l'écran changée : « f1YA » est la vraie fin d'une clé de victime ;
- tics d'IA du grill retirés ;
- environ 320 mots coupés (1 691 → 1 373 au même compte) : la chronologie de 212 à environ 130 mots (Code Bear l'a déjà faite), le paragraphe NSA/CISA, le bloc DeepSeek, les doublons de la section 5. Les blocs coupés sont en réserve en bas.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation Remotion ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Toutes les heures sont à l'heure de Paris. Chaque fait renvoie à [`sources.md`](sources.md).

**À recontrôler juste avant la voix** : un post-mortem d'OpenCode est-il sorti (point d'entrée, nombre de clés) ? Si oui, réécrire la fin de la section 4 (« on ne sait pas »).

---

## 0. Hook (0:00 – 0:40) · objectif : 70 % de rétention à 0:30

[VISUEL : écran noir. Un compteur géant qui s'emballe et se fige sur « 35 026 055 tokens ». À 0:03, petit bandeau en bas : « OpenCode piraté · 17/10 ».]
[SON : tic-tic-tic de compteur qui accélère, coupé net au dernier chiffre.]

Trente-cinq millions de tokens. En gros, de quoi écrire plus de vingt fois toute la saga Harry Potter. Cramés en moins d'une journée, avec les clés de Max Weinbach, volées chez OpenCode. Lui, il n'a rien lancé.

[VISUEL : une pile de livres Harry Potter qui monte, « ×20 » en surimpression, puis la pile part en fumée. Sous-titre sur « clé » : « clé API : le mot de passe qui permet à une appli d'utiliser une IA… et de payer avec ton compte ».]

Près de neuf mille requêtes. Son crédit OpenAI à moins deux dollars quinze. Deux cent soixante-quatre dollars partis sur sa clé Anthropic.

[VISUEL : les chiffres tombent un par un, « −2,15 $ » en rouge, « 264 $ » en orange.]

Et dans ses logs, une requête, en chinois : « Réponds ok. » L'IA a répondu : « ok ».

[VISUEL : une bulle de chat « 请回复ok », puis une bulle « ok ».]
[SON : un « ding » de message, puis silence.]

Quelqu'un a payé, avec l'argent d'un autre, pour faire dire « ok » à une IA. Pourquoi ?

Le code d'OpenCode est public : on va voir où ces clés étaient rangées, et pourquoi on ne pouvait pas les hasher comme un mot de passe.

Et si t'as déjà collé une clé API quelque part, la fin, c'est ta checklist pour ce soir.

---

## 1. Deux OpenCode (0:40 – 1:14)

[VISUEL : un terminal, le logo OpenCode, des logos de modèles qui se branchent comme des cartouches.]

OpenCode, c'est un agent de code open source qui tourne dans ton terminal. Un peu comme Claude Code, mais tu branches le modèle que tu veux.

Sauf qu'il y a deux OpenCode.

[VISUEL : écran coupé en deux. À gauche, un PC avec une clé enfermée dedans. À droite, un nuage « Console ».]

L'appli sur ton PC. Et la Console : un tableau de bord sur le web, où tu peux enregistrer tes propres clés OpenAI, Anthropic ou Google. Ça s'appelle « bring your own key ».

Moi, j'ai jamais collé une clé API dans un outil comme ça. J'y fais très attention.

C'est la Console qui a été touchée. Le soir même, Dax Raad, d'OpenCode, a précisé : « C'est la Console, pas OpenCode lui-même. Ces clés-là ne nous arrivent jamais. »

[VISUEL : capture du post de Dax, la phrase surlignée.]

Donc si t'utilises seulement l'appli, tu peux souffler. Les autres…

---

## 2. La nuit du 17 octobre (1:14 – 1:59)

[VISUEL : une frise horaire de nuit, une lune, l'heure qui avance. Une capture par heure, deux secondes chacune.]
[SON : horloge, tension basse.]

Deux heures trente du matin : d'après OpenCode, les clés ont pu être exposées dès cette heure-là.

Dans la journée, les factures grimpent. Max reçoit un e-mail de Google : ses limites ont été « temporairement abaissées ». Google a nerfé son compte.

[VISUEL : l'e-mail Google, « temporarily lowered the allowed usage limits », avec un tampon « NERF ».]

Dix-sept heures trente, Matt Johansen poste l'e-mail reçu par des clients : « Confirmé. OpenCode piraté. Clés volées. » Vingt heures, OpenCode confirme : une attaque « de distillation à grande échelle », un virgule quatre pour cent des utilisateurs de la Console touchés. Retiens ce mot, distillation.

[VISUEL : le post d'OpenCode, « distillation » qui clignote.]

Anthropic et Google bloquent les clés ; OpenAI rembourse, d'après TechCrunch. Toujours d'après TechCrunch, en analysant l'attaque, Dax trouvait « un peu frustrant » que les IA refusent de l'aider. Les garde-fous censés bloquer les pirates… bloquaient la victime.

[VISUEL : une IA qui fait non de la tête à Dax ; derrière lui, le pirate passe en sifflotant.]
[SON : buzzer « accès refusé ».]

Mais comment des clés se retrouvent dans la nature ? On ouvre le code.

---

## 3. Comment tes clés étaient rangées (1:59 – 3:23)

[VISUEL : le dépôt GitHub d'OpenCode, l'historique des commits qui défile.]

Le code de la Console est sur GitHub, avec tout son historique. Jusqu'au douze octobre, on y trouve une table « provider », avec une colonne « credentials », de type texte. Quand tu enregistres ta clé, elle atterrit dans cette colonne telle que tu l'as collée.

[VISUEL : un tableau, une ligne, une fausse clé « sk-proj-Ab12Cd34… » qui s'écrit lettre par lettre.]

La preuve, c'est la page de réglages. Elle t'affiche ta clé masquée : les huit premiers caractères, trois points, les huit derniers. Et ce masque est calculé à partir de la valeur stockée. Pour t'afficher la fin de ta clé… il faut avoir ta clé.

[VISUEL : `slice(0, 8)` et `slice(-8)` en surbrillance, 2 s maximum, puis la fausse clé masquée « sk-proj-…Wx98Yz76 ».]

Alors, toi qui codes : pourquoi ils ne l'ont pas hashée, comme un mot de passe ? Prends deux secondes.

[VISUEL : un chrono de deux secondes. Deux colonnes, « Mot de passe » et « Clé API ».]
[SON : tic-tac, deux coups.]

Un mot de passe, le site n'a jamais besoin de le relire : il hashe ce que tu tapes et compare les deux empreintes. Une clé API, il faut l'envoyer en entier au fournisseur, à chaque requête. Une empreinte, OpenAI n'en fait rien.

[VISUEL : le hash part vers OpenAI, qui le renvoie avec un tampon « invalide ».]

Le seul qui peut se contenter d'une empreinte, c'est celui qui fabrique la clé : il n'a qu'à vérifier celle que tu lui montres. Un outil qui s'en sert à ta place doit pouvoir la relire.

Donc une clé API, on la chiffre, avec une deuxième clé rangée ailleurs, dans un coffre. Pour la lire, le pirate doit voler deux choses au lieu d'une. Dans ce code-là, il n'y a pas de coffre.

[VISUEL : un coffre qui apparaît à côté de la base, puis s'efface. La base reste seule.]

Pour être honnête, l'hébergeur chiffre peut-être ses disques. Ça protège si quelqu'un repart avec le disque dur, pas face à quelqu'un qui peut interroger la base.

---

## Abonnement (3:23 – 3:36, 43 %, juste après la révélation du hash)

Si t'aimes voir ce qu'il y a sous le capot des outils que tu utilises tous les jours, abonne-toi : sur Technovore, on les ouvre un par un. Et c'est le seul abonnement qui ne te prélèvera jamais rien.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, la colonne « credentials » reste à l'écran.]

---

## 3 bis. L'ancien système (3:36 – 4:19)

[VISUEL : l'e-mail aux victimes, une phrase surlignée.]

Dans l'e-mail aux victimes, OpenCode parle d'un accès à un « ancien système qu'on était en train de démanteler ». Rien ne relie ce qui suit à ce système : OpenCode n'a pas dit par où le pirate est entré. Mais c'est un piège que tout dev devrait connaître.

[VISUEL : le commit sur GitHub, le compteur « −183 758 » qui s'affiche en rouge.]

Le douze octobre, un commit retire l'ancienne base de données du code de la Console.

Dans leur code d'infrastructure, cette base de production n'a jamais été créée par le code. Elle est seulement référencée : « elle existe, elle est là ». Son mot de passe, créé par le code, saute au déploiement suivant. La base reste.

[VISUEL : un RPG. Tu retires un perso de ton équipe : il disparaît de l'écran… et on le retrouve à la taverne, avec tout son inventaire.]

C'est comme retirer un perso de ton équipe dans un RPG. Il disparaît de ton écran, mais il t'attend toujours à la taverne, avec tout son inventaire.

---

## 4. Pourquoi tes clés valent de l'or (4:19 – 6:07) · relance à 55 %

[SON : la musique coupe net.]
[VISUEL : le « ok » du hook revient, seul au milieu de l'écran.]

Il reste ma question du début : pourquoi payer, avec l'argent d'un autre, pour un « ok » ? Pour y répondre, faut savoir ce que vaut une clé API en 2026.

[VISUEL : un gros cerveau « Claude » et un petit cerveau qui copie sur lui, comme en interro.]

Le mot de l'annonce, distillation, c'est copier sur le premier de la classe : tu poses des millions de questions à un gros modèle, et tu entraînes un petit modèle à répondre pareil, pour beaucoup moins cher.

En février, Anthropic a accusé DeepSeek, Moonshot et MiniMax d'avoir fait ça avec environ vingt-quatre mille faux comptes. Le douze octobre, il annonce de nouvelles défenses, avec des faux comptes souvent bannis en moins de deux heures. Et une de ces protections ne couvre que les comptes créés à partir du trente et un août.

Là, c'est une hypothèse, personne ne l'a confirmée : pour un pirate, le compte d'un vrai développeur, ouvert avant cette date, vaut sans doute bien plus qu'un faux compte tout neuf.

[VISUEL : une porte blindée qui se ferme sur une file de faux comptes tout neufs ; un vieux compte s'approche de la porte de service, avec un gros « ? » au-dessus. Bandeau « hypothèse ».]

Et les clés volées, ça se revend. Dans son rapport de septembre, Anthropic écrit que voler des clés API est devenu le seul objectif de plusieurs groupes criminels. Des réseaux de revente font tourner les clés volées jusqu'à les vider. Du farming, mais avec ta carte bancaire.

[VISUEL : une clé passe de main en main dans une file, son « solde » descend à chaque passage.]

En juillet, sans aucun lien avec la fuite, Dax racontait avoir banni une seule personne : huit mille faux comptes OpenCode, quatre cent quatre-vingt mille dollars de tokens revendus par mois. Faut pas abuser.

[VISUEL : « 480 000 $ / mois » plein écran.]

Une clé API, c'est une carte bancaire déjà branchée sur une IA.

Alors, ce « ok » ? Max l'a publié comme un exemple : une requête sur près de neuf mille, pas forcément la première. Seule, elle ne prouve rien. Mais on n'entraîne pas un modèle avec « réponds ok ». Ça ressemble plutôt à un test : est-ce que cette clé marche ?

[VISUEL : le « ok » reprend sa place, avec une étiquette « test de clé ? ».]

Ranger un vol de clés sous le mot « distillation », Nathan Lambert trouve ça « très bizarre ».

Et une requête en chinois ne dit pas qui l'a envoyée. Au vingt octobre, OpenCode n'a publié ni le point d'entrée, ni le nombre de clés. On ne sait pas qui, ni pourquoi.

---

## 5. Le réglage qui décide de ta facture (6:07 – 7:25)

[SON : changement de musique, plus légère.]
[VISUEL : retour sur « −2,15 $ ».]

Maintenant, ta clé à toi. Le jour où elle fuit, combien tu perds dépend surtout d'un réglage : ton plafond.

Regarde le moins deux dollars quinze de Max : son crédit est passé sous zéro. Le compteur ne coupe pas pile à zéro.

[VISUEL : une jauge de crédits qui se vide, dépasse le zéro et glisse un peu dans le rouge.]

Chez OpenAI, une alerte de dépenses ne bloque rien, c'est dans leur doc. Il faut une vraie limite, à part, et même elle n'est pas appliquée instantanément.

[VISUEL : une alarme qui sonne pendant que les billets continuent de s'envoler.]

Chez Anthropic, c'est du prépayé : quand c'est vide, ça s'arrête. Sauf si t'as activé le rechargement automatique : là, ton solde se recharge avec ta carte, pour le pirate. Le pire abonnement de ta vie. Sans réglage, ton plafond, c'est celui de ton palier : cinq cents dollars par mois au premier, deux cent mille tout en haut.

Chez Google, la facture de Gemini peut avoir jusqu'à une dizaine de minutes de retard. Pour un script qui tourne à fond, c'est long.

[VISUEL : checklist qui se coche ligne par ligne.]

Donc ce soir :
Un, si t'as reçu l'e-mail, révoque ta clé chez le fournisseur. La supprimer de la Console ne la désactive pas.
Deux, sans e-mail mais avec une clé Claude dans OpenCode, Anthropic conseille d'en créer une nouvelle, par prudence.
Trois, une clé par outil : si elle fuit, tu sais d'où, et tu ne coupes qu'elle.
Quatre, une vraie limite, et pas de rechargement automatique.
Cinq, supprime les clés oubliées. On en a tous une qui traîne d'un vieux tuto.

---

## 6. Fin (7:25 – 7:49, plus l'écran de fin)

[VISUEL : ton PC, un ventilateur qui tourne, aucune clé à l'écran.]

Moi, je t'ai dit, j'ai jamais collé de clé dans ce genre d'outil. Et après avoir lu ce code, c'est pas demain que je vais commencer.

Sur ma RTX 5080, je peux faire tourner des modèles sans aucune clé API. La seule facture, c'est l'électricité. Est-ce que ça peut remplacer Claude ? C'est la question de la série « Claude ou mon PC ? », qui arrive sur la chaîne.

[VISUEL : écran de fin. Carte vers la vidéo ArtCraft.]

En attendant, Claude entre de bonnes mains, c'est juste ici : un seul développeur, sept logiciels Adobe recréés.

Et la seule clé qu'on ne peut pas te voler, c'est celle que t'as pas.

---

## Relances d'attention

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Chiffre + son | Compteur figé sur 35 026 055 tokens ; bandeau « OpenCode piraté » à 0:03 |
| 0:05 | Visuel | La pile de Harry Potter ×20 qui part en fumée |
| 0:12 | Chiffres | −2,15 $ et 264 $ qui tombent |
| 0:17 | Visuel + son | Bulle « 请回复ok », puis « ok » |
| 0:25 | Boucle ouverte | « Pourquoi ? » (relancée à 4:19, refermée à 5:35) |
| 0:49 | Visuel | Écran coupé en deux, deux OpenCode |
| 1:14 | Son | Horloge, frise de nuit |
| 1:26 | Gag | Tampon « NERF » sur l'e-mail de Google |
| 1:51 | Gag | L'IA qui refuse d'aider Dax |
| 2:14 | Révélation | `slice(-8)` : il faut avoir ta clé |
| 2:34 | Devinette | « Prends deux secondes » : pourquoi pas de hash ? |
| 2:47 | Visuel | Le hash renvoyé avec un tampon « invalide » |
| 3:23 | Appel à l'action | Abonnement (43 %) |
| 4:10 | Gag | Le perso de RPG à la taverne |
| 4:19 | Coupure musique | Relance : retour du « ok » (55 %) |
| 4:29 | Visuel | Le cerveau qui copie en interro |
| 5:17 | Humour | Du farming avec ta carte bancaire |
| 5:30 | Chiffre | 480 000 $ par mois, « faut pas abuser » |
| 5:35 | Boucle fermée | Le « ok » étiqueté « test de clé ? » |
| 6:07 | Changement de ton | Retour sur −2,15 $, ta clé à toi |
| 6:40 | Pique | Le rechargement automatique, « le pire abonnement de ta vie » |
| 6:57 | Visuel | Checklist qui se coche |
| 7:44 | Chute | « La seule clé qu'on ne peut pas te voler… » |

**Total** : 21 relances en 7 min 50 de voix, environ une toutes les 22 secondes.

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Hook, « clé API » | Élevé | Les non-devs ne savent pas ce que c'est | Sous-titre explicatif dès 0:10 ; la bulle « ok » porte l'énigme à l'image |
| Chronologie (section 2) | Moyen | C'est la partie que Code Bear a déjà faite | Coupée à environ 45 s, une capture par heure, le gag de Dax en sortie |
| Hash (section 3) | Moyen | Passage technique | La devinette d'abord, deux colonnes à l'écran, le tampon « invalide » |
| Base référencée (3 bis) | Moyen | Notion d'infrastructure | La taverne du RPG porte tout ; le code 2 s maximum |
| Relance (~55 %) | Élevé | Chute classique | Coupure de musique, retour du « ok », la question du début reposée |
| Distillation (section 4) | Moyen | Bloc de chiffres | Un seul chiffre à l'écran à la fois ; NSA/CISA déjà passé en réserve |

## Notes de montage

- Captures X : floute les avatars et les pseudos des victimes qui ne sont pas des personnalités publiques. Weinbach, Johansen, Dax, Lydia Hallie et Lambert parlent publiquement : on peut les montrer.
- Jamais de vraie clé à l'écran, même partielle. La v1 utilisait « …f1YA » : c'est la fin d'une vraie clé, lue dans l'e-mail de suivi publié par une victime. Utilise une clé inventée de bout en bout (ici « sk-proj-Ab12Cd34…Wx98Yz76 »), et montre huit caractères à la fin, comme le vrai masque.
- Capture de Max Weinbach : avant le montage, vérifie sur quel compte s'affichent les 35 M de tokens et les 8 966 requêtes. Le script ne les attribue à aucun fournisseur.
- Musique : tension basse pendant la section 2, plus légère pendant les gags, coupure nette à la relance.
- Miniature : un « ok » géant dans une bulle de chat, une facture rouge « −2,15 $ » à côté, texte « OpenCode piraté ». Moment candidat : 0:02.

## Sources

Tout est dans [`sources.md`](sources.md) (vérifié à la source le 20/10). Heures tirées des posts : Matt Johansen 17 h 30, Max Weinbach 20 h 01, annonce d'OpenCode 20 h 08, Dax « c'est la Console » 23 h 38 (heures de Paris, décodées depuis l'identifiant des posts listés dans `sources.md`).

## Blocs en réserve

### Seize millions de développeurs et DeepSeek gratuit (~15 s)

Coupé : les seize millions de développeurs concernent tout OpenCode, pas la Console, et le spectateur risque de calculer « 1,4 % de 16 M ». Le chiffre se mélangeait aussi aux seize millions d'échanges d'Anthropic. Si tu le remets, ajoute la phrase sur le calcul. Les vues du post DeepSeek sont celles du 20/10, pas celles du jour du piratage.

D'après OpenCode, plus de seize millions de développeurs s'en servent chaque mois. Attention, c'est OpenCode en entier : la Console, c'est une partie, et personne n'a donné le nombre de clés touchées. Donc ne fais pas le calcul. Et le quinze octobre, deux jours avant, leur post « DeepSeek V4.1 Flash est gratuit dans OpenCode » partait en flèche : il est aujourd'hui à trois virgule sept millions de vues. Gratuit, le mot qui fait sortir tout le monde de sa grotte.

### NSA, CISA et FBI (~15 s)

Coupé pour la durée, et parce que l'avis ne parle pas de clés volées. Ne remets pas « entreprises chinoises » ni « modèles américains » : ce n'est pas dans `sources.md`.

En septembre, la NSA, la CISA et le FBI ont publié un avis commun : six entreprises auraient aspiré des milliards de tokens en passant par des proxys. Cet avis-là ne parle pas de clés volées.

### Dax attaqué à son tour (~10 s)

À remettre en fin de section 2 si la vidéo est trop courte.

Et Dax écrit que ses comptes perso se font attaquer aussi : « un tout nouveau monde, avec le piratage assisté par IA ». Le lendemain, il parle de quarante-huit heures d'attaques.
