# OpenCode piraté : script v1

**Titre provisoire** : *OpenCode s'est fait pirater : pourquoi tes clés API valent de l'or*

**Durée visée** : environ 8 min. **La v1 est trop longue** : 1 777 mots de voix off, soit environ 10 min 10 à ton débit en coupes serrées (175 mots/min, mesuré sur Uber), plus environ 30 s de pauses au montage. Il faut couper environ 350 mots pendant le grill. Les timecodes ci-dessous sont ceux du plan à 8 min, à recalculer en v2.

**Fil rouge** : un « ok » à moins deux dollars quinze. On part d'une requête absurde trouvée dans les logs d'une victime, et on remonte : où étaient rangées les clés, pourquoi elles valent de l'argent, et le réglage qui décide combien tu perds. Boucle ouverte dans le hook (« pourquoi payer pour un "ok" ? »), refermée dans la section 4.

**Angle Technovore** : l'ingénierie de la faille, pas un résumé d'actu. Ce que les vidéos anglaises n'expliquent pas : **pourquoi on ne peut pas hasher une clé API**, alors qu'on hashe un mot de passe.

**Conventions** (comme Uber) : texte normal = voix off. `[VISUEL : …]` = animation Remotion ou capture. `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir par toi. Nombres en lettres pour la lecture. Toutes les heures sont à l'heure de Paris. Chaque fait renvoie à [`sources.md`](sources.md).

---

## 0. Hook (0:00 – 0:35) · objectif : 70 % de rétention à 0:30

[VISUEL : un tableau de bord de facturation sombre, des compteurs qui défilent à toute vitesse. Pas de titre, pas de logo.]
[SON : tic-tic-tic de compteur qui s'emballe.]

Samedi dix-sept octobre. Max Weinbach ouvre son compte OpenAI. Trente-cinq millions de tokens. Huit mille neuf cent soixante-six requêtes. Et un solde à moins deux dollars quinze.

[VISUEL : les trois chiffres se figent l'un après l'autre. « −2,15 $ » en rouge.]

Il n'a rien lancé. Dans ses logs, il publie une requête, écrite en chinois : « Réponds ok. » Et le modèle a répondu : « ok ».

[VISUEL : une bulle « 请回复ok », puis une bulle « ok ». Silence d'une seconde.]
[SON : la musique coupe.]

Quelqu'un a pris sa clé API, avec sa carte bancaire derrière, pour faire dire « ok » à une IA. Cette nuit-là, ce sont les clés d'un virgule quatre pour cent des utilisateurs de la Console d'OpenCode qui sont parties dans la nature.

Le code d'OpenCode est public. Alors on va l'ouvrir, voir comment tes clés y étaient rangées, et comprendre pourquoi des pirates se battent pour elles en 2026.

Et si t'as déjà collé une clé API dans un outil, n'importe lequel, la fin de la vidéo te concerne directement.

⚠️ **Risque de rétention** : le spectateur doit comprendre en 10 s ce qu'est une clé API. Mitigation : sous-titre à l'écran sur « clé API » : « le mot de passe qui permet à une appli d'utiliser une IA… et de payer avec ta carte ».

---

## 1. Deux OpenCode (0:35 – 1:35)

[VISUEL : un terminal, le logo OpenCode, des logos de modèles qui se branchent comme des cartouches.]

OpenCode, c'est un agent de code open source qui tourne dans ton terminal. Un peu comme Claude Code, sauf que tu branches le modèle que tu veux : Claude, GPT, Gemini, DeepSeek.

D'après OpenCode, plus de seize millions de développeurs s'en servent chaque mois. Et deux jours avant le piratage, leur post « DeepSeek V4.1 Flash est gratuit dans OpenCode » faisait trois virgule sept millions de vues. En plus, gratuit, mais comment on peut avoir la force de pirater quelque chose de gratuit et open source ? 

[VISUEL : compteur « 3,73 M vues », une foule de petits curseurs qui accourt.]


Sauf qu'il y a deux OpenCode.

[VISUEL : écran coupé en deux. À gauche, un PC avec une clé enfermée dedans. À droite, un nuage « Console ».]

L'appli sur ton PC : tes clés restent chez toi. Et la Console : un tableau de bord sur le web, où tu peux enregistrer tes propres clés OpenAI, Anthropic ou Google, pour que les serveurs d'OpenCode s'en servent à ta place. On appelle ça « bring your own key », apporte ta propre clé.

C'est la Console qui a été touchée. Dax Raad, un des fondateurs, l'a écrit tout de suite : « C'est la Console, pas OpenCode lui-même. Ces clés-là ne nous arrivent jamais. »

[VISUEL : capture du post de Dax, la phrase surlignée.]

Donc si tu utilises seulement l'appli, tu peux souffler. Mais pour ceux qui avaient rempli la Console, la nuit a été longue.

---

## 2. La nuit du 17 octobre (1:35 – 2:50)

[VISUEL : une frise horaire de nuit, une lune, l'heure qui avance.]
[SON : horloge.]

Deux heures trente du matin. D'après l'e-mail envoyé ensuite par OpenCode, c'est le moment le plus tôt où les clés ont pu être exposées.

Pendant la journée, des développeurs voient leurs factures grimper. Google, lui, réagit tout seul : il envoie des e-mails pour dire qu'il a baissé les limites d'utilisation de certains comptes.

[VISUEL : un e-mail Google qui tombe, « temporarily lowered the allowed usage limits ».]

Dix-sept heures trente. Matt Johansen, qui suit la cybersécurité, poste une capture de l'e-mail reçu par des clients : « Confirmé. OpenCode piraté. Clés volées. » Sept cent quatre-vingt-trois mille vues.

Vingt heures. OpenCode officialise. Une brèche « liée à une attaque de distillation à grande échelle », qui touche un virgule quatre pour cent des utilisateurs de la Console. Et une phrase : « Si tu n'as pas reçu d'e-mail, tu n'es pas concerné. » Deux millions huit cent mille vues.

[VISUEL : le post d'OpenCode, « distillation » qui clignote. On y reviendra.]

Dans la soirée, Lydia Hallie, chez Anthropic, annonce qu'ils ont révoqué les clés Claude qu'ils pensaient touchées. Et Dax écrit que ses comptes perso se font attaquer aussi : « un tout nouveau monde, avec le piratage assisté par IA ».

Petit détail rapporté par TechCrunch : pendant qu'il analysait l'attaque, Dax trouvait « un peu frustrant » que les IA refusent de l'aider. Les garde-fous censés bloquer les pirates… bloquaient la victime.

[VISUEL : une IA qui fait non de la tête à Dax ; derrière lui, le pirate passe en sifflotant.]
[SON : buzzer « accès refusé ».]

Bon. Mais concrètement, comment des clés se retrouvent dans la nature ? Pour ça, il faut ouvrir le code.

---

## 3. Comment tes clés étaient rangées (2:50 – 4:30)

[VISUEL : l'e-mail aux victimes, une phrase surlignée.]

Dans l'e-mail aux victimes, OpenCode parle d'un accès non autorisé à un « ancien système qu'on était en train de démanteler ».

Et dans le dépôt GitHub, on trouve un commit du douze octobre. Cinq jours avant. Son nom : « supprimer l'ancienne base de données de la Console ». Cent quatre-vingt-trois mille lignes effacées.

[VISUEL : le commit sur GitHub, le compteur « −183 758 » qui s'affiche en rouge.]

Sauf que dans leur code d'infrastructure, la base de production n'est pas créée par ce code. Elle est seulement référencée : le code dit « cette base existe, elle est là ». Le mot de passe, lui, est créé par le code. Résultat : quand tu effaces le code, le mot de passe saute au déploiement suivant. La base, elle, ne bouge pas.

[VISUEL : un RPG. Tu retires un perso de ton équipe : il disparaît de l'écran… et on le retrouve à la taverne, avec tout son inventaire.]

C'est comme retirer un perso de ton équipe dans un RPG. Il disparaît de ton écran, mais il est toujours à la taverne, avec tout son inventaire.

Attention : rien ne prouve que le pirate est passé par là. OpenCode n'a toujours pas dit comment il est entré. Mais ça montre une chose : un « ancien système », ça peut encore contenir des clés bien vivantes.

[SON : transition.]

Et justement, comment elles étaient rangées, ces clés ? Dans l'ancien schéma, il y a une table « provider », une colonne « credentials », de type texte. Ta clé y est enregistrée telle que tu l'as collée.

[VISUEL : un tableau, une ligne, la clé en clair « sk-proj-… » qui s'écrit lettre par lettre.]

La preuve la plus simple, c'est la page de réglages. Elle t'affiche ta clé masquée : les huit premiers caractères, des points, les huit derniers. Et dans le code, ce masque est calculé à partir de la valeur stockée. Pour afficher les huit derniers caractères de ta clé… il faut avoir ta clé.

[VISUEL : `slice(0, 8)` et `slice(-8)` en surbrillance, puis la clé masquée « sk-proj-…f1YA ».]

Alors là, tu vas me dire : « Mais pourquoi ils ne l'ont pas hashée, comme un mot de passe ? »

Parce qu'ils ne peuvent pas.

[VISUEL : deux colonnes, « Mot de passe » et « Clé API ».]

Un mot de passe, le site n'a jamais besoin de le relire. Quand tu te connectes, il hashe ce que tu tapes et il compare les deux empreintes. Une clé API, OpenCode doit l'envoyer à OpenAI à chaque requête, en entier. Une empreinte, OpenAI n'en fait rien.

[VISUEL : le hash part vers OpenAI, qui le renvoie avec un tampon « invalide ».]

Donc une clé API, on ne la hashe pas : on la chiffre, avec une autre clé rangée ailleurs, dans un coffre. Pour la lire, le pirate doit voler deux choses au lieu d'une. Dans ce code-là, il n'y a pas ce coffre.

Pour être honnête : l'hébergeur de la base chiffre sûrement le disque. Ça te protège si quelqu'un vole le disque dur. Ça ne sert à rien face à quelqu'un qui peut interroger la base.

---

## Abonnement (≈ 4:30, juste après la première révélation)

Si tu aimes comprendre ce qu'il y a sous le capot des outils que tu utilises tous les jours, abonne-toi : sur Technovore, on les ouvre un par un.

[VISUEL : bouton « S'abonner » animé en bas à droite, 3 secondes, la colonne « credentials » reste à l'écran.]

> Placé à environ 55 % de la vidéo plutôt qu'à 25 % : avant, il couperait la chronologie. Si le grill propose mieux, on déplace.

---

## 4. Pourquoi tes clés valent de l'or (4:30 – 6:20)

[VISUEL : un gros cerveau « Claude » et un petit cerveau qui copie sur lui, comme en interro.]

Maintenant, le mot bizarre de l'annonce : distillation.

La distillation, c'est copier sur le premier de la classe. Tu poses des millions de questions à un gros modèle, tu gardes toutes ses réponses, et tu entraînes un petit modèle à répondre pareil. Tu récupères une bonne partie de son niveau pour beaucoup moins cher.

En février, Anthropic a accusé trois labos chinois, DeepSeek, Moonshot et MiniMax, d'avoir fait ça avec plus de seize millions d'échanges, via environ vingt-quatre mille faux comptes. En septembre, la NSA, la CISA et le FBI ont publié un avis commun : des entreprises chinoises auraient aspiré des milliards de tokens aux modèles américains.

[VISUEL : un compteur « 16 000 000 » puis une armée de vingt-quatre mille petits comptes.]

Alors les labos ferment la porte. Le douze octobre, cinq jours avant le piratage, Anthropic publie ses nouvelles défenses : entre quatre-vingt-dix et quatre-vingt-dix-neuf pour cent de données récoltées en moins, et des faux comptes souvent bannis en moins de deux heures. Une de ces protections ne s'applique qu'aux comptes créés à partir du trente et un août.

[VISUEL : une porte blindée qui se ferme sur une file de faux comptes tout neufs.]

Tu vois le problème ? Un faux compte tout neuf se fait repérer. Mais un vrai compte de développeur, avec un an d'historique et une vraie carte bancaire, il a l'air parfaitement normal.

Dans son rapport de septembre, Anthropic écrit que voler des clés API est devenu le seul objectif de plusieurs groupes criminels. Des réseaux de revente font tourner des clés volées jusqu'à ce qu'elles soient vides.

[VISUEL : une clé passe de main en main dans une file, son « solde » descend à chaque passage.]

Et OpenCode connaît ce marché. En juillet, Dax racontait avoir banni une seule personne qui gérait huit mille faux comptes et revendait quatre cent quatre-vingt mille dollars de tokens par mois.

[UNEXPECTED STAT — VISUEL : « 480 000 $ / mois » plein écran.]

Une clé API, c'est donc une carte bancaire déjà branchée sur une IA.

Alors, c'était de la distillation ? Reviens au « ok » de Max Weinbach. On n'entraîne pas un modèle avec « réponds ok ». Ça ressemble plutôt à un test : « Est-ce que cette clé marche ? » Le chercheur Nathan Lambert l'a dit sans détour : il y a quelque chose de très bizarre si une cyberattaque pour voler des clés API est rangée sous le même mot que la distillation. Et dans TechCrunch, des sceptiques parlent d'exagération.

[VISUEL : le « ok » du début revient, avec une étiquette « test de clé ? ».]

La vérité, c'est qu'au moment où je te parle, on ne sait pas. OpenCode n'a publié ni le point d'entrée, ni le nombre de clés.

---

## 5. Le réglage qui décide de ta facture (6:20 – 7:35) · relance

[SON : la musique coupe net.]
[VISUEL : retour sur « −2,15 $ ».]

Ça, c'est l'histoire d'OpenCode. Maintenant, parlons de ta clé à toi. Parce que le jour où elle fuit, ce n'est pas le pirate qui décide combien tu perds. C'est ton plafond.

Max Weinbach avait des crédits prépayés chez OpenAI. Le pirate a tout vidé, jusqu'à moins deux dollars quinze, et il s'est arrêté là. Le solde, c'était le plafond.

[VISUEL : une jauge de crédits qui se vide et bute sur zéro.]

Chez OpenAI, attention au piège : une alerte de dépenses, ça t'envoie un e-mail. Ça n'arrête rien. La doc le dit noir sur blanc. Il faut activer la vraie limite, à part. Et même là, OpenAI prévient qu'elle n'est pas appliquée instantanément.

[VISUEL : une alarme qui sonne pendant que les billets continuent de s'envoler.]

Chez Anthropic, c'est du prépayé : quand c'est vide, ça s'arrête. Sauf si tu as activé le rechargement automatique. Là, ton solde se recharge tout seul… avec ta carte. Et si tu n'as rien réglé, ton plafond, c'est celui de ton palier : jusqu'à cinq cents dollars par mois au premier niveau, deux cent mille tout en haut.

Chez Google, pour Gemini, le premier palier plafonne à deux cent cinquante dollars par mois, mais la facturation peut avoir une dizaine de minutes de retard. Dix minutes, pour un script qui tourne à fond, c'est long.

[VISUEL : checklist qui se coche ligne par ligne.]

Donc ce soir :
Un, si tu as reçu l'e-mail, révoque ta clé chez le fournisseur, pas dans l'outil. La supprimer de la Console ne la tue pas.
Deux, une clé par outil. Si une fuite arrive, tu sais d'où elle vient, et tu ne coupes qu'elle.
Trois, un vrai plafond, un petit solde, et pas de rechargement automatique.
Quatre, supprime les clés que tu as oubliées. Tout le monde en a une qui traîne d'un vieux tuto.

---

## 6. Fin (7:35 – 8:15)

[VISUEL : ton PC, un ventilateur qui tourne, aucune clé à l'écran.]

[TON AVIS EN 2 OU 3 PHRASES : est-ce que tu as déjà collé une clé dans un outil comme ça ? Qu'est-ce que cette histoire change pour toi ?]

Moi, j'en retiens une chose : la seule clé qu'on ne peut pas te voler, c'est celle que tu n'as pas.

Sur ma RTX 5080, je fais tourner des modèles sans aucune clé, sans facture. Est-ce que ça peut remplacer Claude ? C'est la question de ma prochaine série, et la réponse risque de te surprendre.

[VISUEL : écran de fin. Carte vers la vidéo ArtCraft.]

En attendant, si tu veux voir ce que Claude sait faire quand il est entre de bonnes mains, regarde comment un développeur a recréé sept logiciels Adobe avec lui. C'est juste ici.

---

## Journal des relances d'attention

| Timecode | Type | Description |
|---|---|---|
| 0:00 | Visuel | compteurs qui s'emballent |
| 0:20 | Son | la musique coupe sur le « ok » |
| 1:05 | Visuel | écran coupé en deux, deux OpenCode |
| 1:40 | Son | horloge, frise de nuit |
| 2:35 | Gag | l'IA qui refuse d'aider Dax |
| 3:10 | Gag | le perso de RPG à la taverne |
| 3:45 | Révélation | `slice(-8)` |
| 4:05 | Question | « pourquoi ne pas la hasher ? » |
| 4:45 | Visuel | le cerveau qui copie en interro |
| 5:40 | Chiffre | 480 000 $ par mois |
| 6:20 | Son | la musique coupe, relance |
| 7:00 | Visuel | checklist |

**Environ 12 relances, en moyenne une toutes les 40 s.**

## Carte des risques de rétention

| Timecode | Risque | Problème | Solution |
|---|---|---|---|
| 0:00-0:15 | ⚠️ Élevé | « clé API » pas compris par les non-développeurs | Sous-titre explicatif à l'écran dès 0:10 |
| 1:35-2:50 | ⚠️ Moyen | La chronologie, c'est une suite d'heures | Frise animée, une capture par heure, le gag de Dax en sortie |
| 3:20-3:45 | ⚠️ Moyen | Base référencée et ressource gérée : passage technique | La métaphore du RPG porte tout ; montrer le code 2 s maximum |
| 4:45-5:30 | ⚠️ Moyen | Bloc de chiffres sur la distillation | Un seul chiffre à l'écran à la fois |

## Notes de montage

- Toutes les captures X : floute les avatars et les pseudos des victimes qui ne sont pas des personnalités publiques. Weinbach, Johansen, Dax, Lydia Hallie et Lambert parlent publiquement : on peut les montrer.
- Jamais de vraie clé à l'écran, même partielle : utilise une fausse clé `sk-proj-…f1YA`.
- Musique : tension basse pendant la section 2, plus légère pendant les gags.
- Miniature : un « ok » géant dans une bulle de chat, une facture rouge « −2,15 $ » à côté, texte « OpenCode piraté ». Moment candidat : 0:20.
