# Téléprompteur — OpenCode piraté (v2, 20/10)

> Une ligne = un souffle. Ligne vide = respiration. Les [MARQUEURS] et (indications) ne se lisent pas.

## Hook

35 millions de tokens.  
En gros, de quoi écrire plus de vingt fois  
toute la saga Harry Potter.  
Cramés en moins d'une journée,  
avec les clés de Max Weinbach, (« ouaïne-bak »)  
volées chez OpenCode.  
Lui, il n'a rien lancé.  

Près de 9 000 requêtes.  
Son crédit OpenAI à moins 2 dollars 15.  
264 dollars partis sur sa clé Anthropic.  

Et dans ses logs, une requête, en chinois :  
« Réponds ok. »  
L'IA a répondu : « ok ».  

Quelqu'un a payé, avec l'argent d'un autre,  
pour faire dire « ok » à une IA.  
Pourquoi ?  

Le code d'OpenCode est public :  
on va voir où ces clés étaient rangées,  
et pourquoi on ne pouvait pas les hasher  
comme un mot de passe.  

Et si t'as déjà collé une clé API quelque part,  
la fin, c'est ta checklist pour ce soir.  

## Deux OpenCode

OpenCode, c'est un agent de code open source  
qui tourne dans ton terminal.  
Un peu comme Claude Code,  
mais tu branches le modèle que tu veux.  

Sauf qu'il y a deux OpenCode.  

L'appli sur ton PC.  
Et la Console :  
un tableau de bord sur le web,  
où tu peux enregistrer tes propres clés  
OpenAI, Anthropic ou Google.  
Ça s'appelle « bring your own key ».  

Moi, j'ai jamais collé une clé API dans un outil comme ça.  
J'y fais très attention.  

C'est la Console qui a été touchée.  
Le soir même, Dax Raad, d'OpenCode, a précisé :  
« C'est la Console, pas OpenCode lui-même.  
Ces clés-là ne nous arrivent jamais. »  

Donc si t'utilises seulement l'appli,  
tu peux souffler.  
Les autres…  

## La nuit du 17 octobre

2 h 30 du matin :  
d'après OpenCode, les clés ont pu être exposées  
dès cette heure-là.  

Dans la journée, les factures grimpent.  
Max reçoit un e-mail de Google :  
ses limites ont été « temporairement abaissées ».  
Google a nerfé son compte.  

17 h 30,  
Matt Johansen poste l'e-mail reçu par des clients :  
« Confirmé. OpenCode piraté. Clés volées. »  

20 h, OpenCode confirme :  
une attaque « de distillation à grande échelle »,  
1 virgule 4 pour cent des utilisateurs de la Console touchés.  
Retiens ce mot, distillation.  

Anthropic et Google bloquent les clés ;  
OpenAI rembourse, d'après TechCrunch.  
Toujours d'après TechCrunch,  
en analysant l'attaque,  
Dax trouvait « un peu frustrant »  
que les IA refusent de l'aider.  
Les garde-fous censés bloquer les pirates…  
bloquaient la victime.  

Mais comment des clés se retrouvent dans la nature ?  
On ouvre le code.  

## Comment tes clés étaient rangées

Le code de la Console est sur GitHub,  
avec tout son historique.  
Jusqu'au 12 octobre, on y trouve une table « provider »,  
avec une colonne « credentials », (« cré-den-chals »)  
de type texte.  
Quand tu enregistres ta clé,  
elle atterrit dans cette colonne  
telle que tu l'as collée.  

La preuve, c'est la page de réglages.  
Elle t'affiche ta clé masquée :  
les 8 premiers caractères,  
trois points,  
les 8 derniers.  
Et ce masque est calculé à partir de la valeur stockée.  
Pour t'afficher la fin de ta clé…  
il faut avoir ta clé.  

Alors, toi qui codes :  
pourquoi ils ne l'ont pas hashée, comme un mot de passe ?  
Prends deux secondes.  

*(pause de 2 s au montage)*

Un mot de passe,  
le site n'a jamais besoin de le relire :  
il hashe ce que tu tapes  
et compare les deux empreintes.  
Une clé API, il faut l'envoyer en entier au fournisseur,  
à chaque requête.  
Une empreinte, OpenAI n'en fait rien.  

Le seul qui peut se contenter d'une empreinte,  
c'est celui qui fabrique la clé :  
il n'a qu'à vérifier celle que tu lui montres.  
Un outil qui s'en sert à ta place  
doit pouvoir la relire.  

Donc une clé API, on la chiffre,  
avec une deuxième clé rangée ailleurs, dans un coffre.  
Pour la lire, le pirate doit voler deux choses au lieu d'une.  
Dans ce code-là, il n'y a pas de coffre.  

Pour être honnête,  
l'hébergeur chiffre peut-être ses disques.  
Ça protège si quelqu'un repart avec le disque dur,  
pas face à quelqu'un qui peut interroger la base.  

## Abonnement

Si t'aimes voir ce qu'il y a sous le capot  
des outils que tu utilises tous les jours,  
abonne-toi :  
sur Technovore, on les ouvre un par un.  
Et c'est le seul abonnement  
qui ne te prélèvera jamais rien.  

## L'ancien système

Dans l'e-mail aux victimes,  
OpenCode parle d'un accès à un  
« ancien système qu'on était en train de démanteler ».  
Rien ne relie ce qui suit à ce système :  
OpenCode n'a pas dit par où le pirate est entré.  
Mais c'est un piège que tout dev devrait connaître.  

Le 12 octobre, un commit retire l'ancienne base de données  
du code de la Console.  

Dans leur code d'infrastructure,  
cette base de production n'a jamais été créée par le code.  
Elle est seulement référencée :  
« elle existe, elle est là ».  
Son mot de passe, créé par le code,  
saute au déploiement suivant.  
La base reste.  

C'est comme retirer un perso de ton équipe dans un RPG.  
Il disparaît de ton écran,  
mais il t'attend toujours à la taverne,  
avec tout son inventaire.  

## Pourquoi tes clés valent de l'or

*(la musique coupe : repars avec de l'énergie)*

Il reste ma question du début :  
pourquoi payer, avec l'argent d'un autre, pour un « ok » ?  
Pour y répondre,  
faut savoir ce que vaut une clé API en 2026.  

Le mot de l'annonce, distillation,  
c'est copier sur le premier de la classe :  
tu poses des millions de questions à un gros modèle,  
et tu entraînes un petit modèle à répondre pareil,  
pour beaucoup moins cher.  

En février, Anthropic a accusé DeepSeek, Moonshot et MiniMax  
d'avoir fait ça avec environ 24 000 faux comptes.  
Le 12 octobre, il annonce de nouvelles défenses,  
avec des faux comptes souvent bannis en moins de deux heures.  
Et une de ces protections  
ne couvre que les comptes créés à partir du 31 août.  

Là, c'est une hypothèse, personne ne l'a confirmée :  
pour un pirate, le compte d'un vrai développeur,  
ouvert avant cette date,  
vaut sans doute bien plus qu'un faux compte tout neuf.  

Et les clés volées, ça se revend.  
Dans son rapport de septembre, Anthropic écrit  
que voler des clés API est devenu le seul objectif  
de plusieurs groupes criminels.  
Des réseaux de revente font tourner les clés volées  
jusqu'à les vider.  
Du farming, mais avec ta carte bancaire.  

En juillet, sans aucun lien avec la fuite,  
Dax racontait avoir banni une seule personne :  
8 000 faux comptes OpenCode,  
480 000 dollars de tokens revendus par mois.  
Faut pas abuser.  

Une clé API,  
c'est une carte bancaire déjà branchée sur une IA.  

Alors, ce « ok » ?  
Max l'a publié comme un exemple :  
une requête sur près de 9 000,  
pas forcément la première.  
Seule, elle ne prouve rien.  
Mais on n'entraîne pas un modèle avec « réponds ok ».  
Ça ressemble plutôt à un test :  
est-ce que cette clé marche ?  

Ranger un vol de clés sous le mot « distillation »,  
Nathan Lambert trouve ça « très bizarre ».  

Et une requête en chinois ne dit pas qui l'a envoyée.  
Au 20 octobre, OpenCode n'a publié  
ni le point d'entrée, ni le nombre de clés.  
On ne sait pas qui, ni pourquoi.  

## Le réglage qui décide de ta facture

Maintenant, ta clé à toi.  
Le jour où elle fuit,  
combien tu perds dépend surtout d'un réglage :  
ton plafond.  

Regarde le moins 2 dollars 15 de Max :  
son crédit est passé sous zéro.  
Le compteur ne coupe pas pile à zéro.  

Chez OpenAI, une alerte de dépenses ne bloque rien,  
c'est dans leur doc.  
Il faut une vraie limite, à part,  
et même elle n'est pas appliquée instantanément.  

Chez Anthropic, c'est du prépayé :  
quand c'est vide, ça s'arrête.  
Sauf si t'as activé le rechargement automatique :  
là, ton solde se recharge avec ta carte, pour le pirate.  
Le pire abonnement de ta vie.  
Sans réglage, ton plafond, c'est celui de ton palier :  
500 dollars par mois au premier,  
200 000 tout en haut.  

Chez Google, la facture de Gemini  
peut avoir jusqu'à une dizaine de minutes de retard.  
Pour un script qui tourne à fond, c'est long.  

Donc ce soir :  

Un, si t'as reçu l'e-mail,  
révoque ta clé chez le fournisseur.  
La supprimer de la Console ne la désactive pas.  

Deux, sans e-mail mais avec une clé Claude dans OpenCode,  
Anthropic conseille d'en créer une nouvelle, par prudence.  

Trois, une clé par outil :  
si elle fuit, tu sais d'où,  
et tu ne coupes qu'elle.  

Quatre, une vraie limite,  
et pas de rechargement automatique.  

Cinq, supprime les clés oubliées.  
On en a tous une qui traîne d'un vieux tuto.  

## Fin

Moi, je t'ai dit,  
j'ai jamais collé de clé dans ce genre d'outil.  
Et après avoir lu ce code,  
c'est pas demain que je vais commencer.  

Sur ma RTX 5080,  
je peux faire tourner des modèles sans aucune clé API.  
La seule facture, c'est l'électricité.  
Est-ce que ça peut remplacer Claude ?  
C'est la question de la série « Claude ou mon PC ? »,  
qui arrive sur la chaîne.  

En attendant, Claude entre de bonnes mains,  
c'est juste ici :  
un seul développeur, sept logiciels Adobe recréés.  

*(dernière phrase posée, lentement)*

Et la seule clé qu'on ne peut pas te voler,  
c'est celle que t'as pas.  
