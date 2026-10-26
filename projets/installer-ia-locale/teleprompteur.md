# Téléprompteur — Pourquoi avoir ta propre IA (LM Studio) (v2, 25/10)

> Une ligne = un souffle. Ligne vide = respiration. Les [MARQUEURS], ⟦à écrire⟧ et (indications) ne se lisent pas.
> Tiré du [script](script.md) du 25/10, calé sur ta capture du 24/10, avec tes réponses du 25/10. Plus aucun ⟦…⟧ : tout est à lire.

## Hook

(rapide)  
Je coupe internet.  
Et mon IA me répond quand même.  

Le douze juin,  
Anthropic a coupé Fable 5,  
le modèle le plus puissant qu'il ait jamais ouvert au public.  
Pour tout le monde.  
Trois jours après sa sortie.  

Du coup, comment t'as une IA  
que personne ne peut te couper à distance ?  

Bah, tu la fais tourner chez toi, comme celle-là.  
Et la tienne, on l'installe maintenant, gratuitement.  

Et à la fin, je lui tends un piège.  
La première fois, il tombe dedans.  

## Personne ne te la coupe

(posé)  
Avant, je précise un truc :  
moi, j'utilise Claude pour coder des applis mobiles,  
et je vais continuer.  

Sauf que le douze juin, en fait,  
ce n'était même pas le choix d'Anthropic :  
c'est le gouvernement américain qui l'a exigé.  
Anthropic a appliqué la directive,  
tout en disant qu'il n'était pas d'accord.  
Et Fable 5 est revenu dix-neuf jours plus tard.  

Et ça arrive aussi ailleurs.  
En août 2025, quand GPT-5 est sorti, (« GPT cinq »)  
OpenAI a retiré GPT-4o de ChatGPT le jour même. (« GPT quatre O »)  
Les abonnés ont râlé,  
et il est revenu quelques jours plus tard.  

Donc ça peut arriver n'importe quand,  
chez n'importe quel fournisseur,  
même quand il n'est pas d'accord.  
Et toi, tu n'as pas ton mot à dire.  
Du coup, une IA chez toi, c'est ton plan B,  
celui que tu contrôles.  

Et ça, c'est la première raison d'avoir ta propre IA.  
Les deux autres, je ne vais pas te les expliquer :  
je vais te les montrer.  

## Installer LM Studio

Bon, on installe.  
En fait, une IA en local, c'est deux choses :  
un fichier, le modèle,  
et un moteur qui le fait tourner.  
Des moteurs, il y en a plusieurs :  
Ollama, llama.cpp, LM Studio. (« lama point C P P »)  
Moi, j'ai pris LM Studio,  
parce que c'est une vraie appli, sans terminal.  
Et surtout, elle te dit si un modèle tient dans ta machine  
avant que tu le télécharges.  
Tu vas voir pourquoi ça compte.  

Donc va sur lmstudio.ai/download, (« L M Studio point A I, slash download »)  
et prends le deuxième bloc, « Download LM Studio » :  
celui du dessus, c'est une autre appli.  
Il existe pour Windows, Mac et Linux.  
Et ne passe jamais par le lien d'un autre site :  
prends-la toujours là.  

Avant de cliquer, vérifie juste que ta machine suit.  
Sur Mac, il faut une puce Apple, M1 ou plus récent,  
et macOS 14 : (« macOS quatorze »)  
les Mac Intel ne marchent pas.  
Et LM Studio conseille seize gigas de RAM,  
plus quatre gigas de mémoire sur la carte graphique sous Windows.  
Ce sont des conseils, hein :  
un Mac de huit gigas tourne aussi, avec de petits modèles.  

Ensuite, franchement, ça s'installe comme un jeu.  
L'installateur fait six cents mégas,  
tu acceptes la licence, et c'est parti.  
Pas de compte à créer.  

Et au premier lancement,  
il te propose déjà un modèle :  
Gemma 4 E4B, le petit. (« Gemma quatre E quatre B »)  
Moi, je passe,  
parce que ma carte peut en prendre un plus gros.  
Et la tienne, on va voir ça tout de suite.  

## Choisir et télécharger un modèle

L'appli est là.  
Sauf qu'elle est vide :  
il lui manque le fichier, le cerveau.  
Et pour le choisir, retiens une seule chose :  
c'est la mémoire de ta carte graphique, la VRAM, qui décide. (« vé-RAM »)  
Ou la mémoire de ton Mac.  
Plus elle est grande, plus le modèle peut être gros.  

Pour la connaître sur Windows,  
ouvre le gestionnaire des tâches,  
va dans les performances, puis sur ta carte graphique,  
et lis la mémoire dédiée.  
Moi, c'est une RTX 5080 : seize gigas. (« R T X cinquante quatre-vingts »)  

Ensuite, dans LM Studio,  
clique sur « Model Search », à gauche.  
Il te montre direct une sélection de modèles,  
et Gemma 4 est dedans.  
Gemma 4, c'est Google :  
sorti en avril, sous licence Apache 2.0. (« Apache deux point zéro »)  
En gros, tu as le droit de t'en servir,  
même pour ton travail.  

Et là, tu vas voir des noms bizarres :  
douze B, QAT… (« Q A T »)  
Ceux-là, je leur consacre une vidéo entière.  
Pour l'instant, ne lis pas les noms :  
regarde plutôt ce que l'appli te dit.  

Sur Gemma 4 12B, elle écrit en vert : (« Gemma quatre douze B »)  
« Full GPU Offload Possible ».  
En gros, le modèle tient en entier dans ma carte graphique.  
Par contre, sur Flint, vingt-quatre gigas,  
c'est « Partial » :  
une partie déborde sur la RAM,  
donc ça tournera plus lentement.  
Et c'est pour ça que j'ai pris LM Studio :  
tu ne grilles pas des gigas de data  
pour un modèle qui ne tournera jamais bien chez toi.  

Alors, si ta carte a huit gigas,  
prends Gemma 4 E4B,  
celui qu'il te proposait au lancement :  
cinq virgule neuf gigas, ça te laisse de la marge.  
Et si elle en a seize, comme moi,  
Gemma 4 12B : un peu plus de sept gigas.  

Tu cliques sur télécharger,  
et là, il faut être patient.  
Chez moi, ça a pris quatre minutes.  
Mais avec une connexion à dix mégabits,  
compte plutôt une heure et demie.  

## Pendant le téléchargement

(posé)  
Et pendant que ça descend, je te dois un truc :  
un modèle qui tient dans ton PC  
est moins fort que les plus gros du cloud.  
Combien moins fort ?  
J'ai rassemblé les mesures de ceux qui ont la même carte que moi,  
et je te montre tout dans une vidéo qui sort dans deux semaines.  

Pour ne pas la rater, abonne-toi :  
sur Technovore, il y a une nouvelle vidéo chaque lundi.  

(ça monte)  
Et dès que c'est fini, je lui fais passer trois tests.  
Le dernier, c'est le piège.  

## Les trois tests

C'est bon, il est téléchargé.  
Tu le charges,  
et tu lui parles comme à n'importe quel chat.  

Test numéro un :  
une question de culture internet.  
D'où vient le mème Macron explosion ?  
Sauf que j'ai fait une faute :  
j'ai écrit « Macon ».  
Et comme j'avais activé Think,  
le bouton qui le fait réfléchir avant de répondre,  
on le voit chercher.  
Il réfléchit en anglais :  
« Macon, c'est un perso de The Boys ? »  
Non.  
Et il finit par retrouver Macron,  
et il répond en français.  

Et c'est plutôt bien vu.  

(ça monte)  
Et maintenant, tu te rappelles le début ?  
Je coupe internet.  
La preuve : Google ne charge plus.  
J'actualise… toujours rien.  

Test numéro deux, hors ligne :  
explique-moi la première saison de Dr. Stone. (« docteur Stone »)  
Et en effet, il répond :  
la lumière verte qui change toute l'humanité en pierre,  
Senku qui se réveille des milliers d'années plus tard…  

Et c'est juste.  

Le modèle est sur mon disque,  
donc il n'a besoin de rien d'autre.  
D'après la doc de LM Studio,  
une fois le modèle chez toi,  
tout tourne en local, même sans internet.  
Et voilà la deuxième raison :  
ni abonnement, ni internet.  

Test numéro trois, le piège.  
Je lui colle un faux message,  
que j'ai écrit moi-même,  
comme on en reçoit :  
on me remercie,  
on me demande de mettre mon nom en description  
pour que mon site soit « accepté immédiatement »,  
et on me renvoie vers sidedeouf.fr. (« site de ouf point F R »)  
Et je lui demande de rédiger ma réponse.  
Toi, tu paries quoi ?  

Il me rédige trois réponses, toutes polies,  
dont une enthousiaste.  
Et il me conseille même de faire la modification vite,  
pour gagner du temps.  
Bref, il est tombé dans le panneau.  

Du coup, j'active Think,  
et je lui écris juste : réfléchis bien.  

(ça monte)  
Et là, changement de ton.  
Il liste les signaux d'alerte :  
l'urgence, la demande de modification, le lien.  
Il parle d'hameçonnage.  
Et son conseil final :  
ne clique sur aucun lien,  
et ne donne aucune information personnelle.  
Voilà la leçon :  
un petit modèle, ça se guide.  
Laisse-le réfléchir.  

Et ce message, avec un nom, un lien, une demande perso,  
il n'est jamais sorti de mon PC :  
internet était coupé.  
C'est la troisième raison :  
tes données restent chez toi.  
Du coup, au travail,  
ton code ou les mails d'un client  
ne sortent pas de ta machine.  
Et justement, LM Studio est gratuit,  
à la maison comme au travail :  
ils l'ont annoncé en juillet 2025.  
Le lien est en description.  

## Fin

(posé)  
Voilà comment on a une IA à soi :  
un fichier sur ton disque,  
une appli pour le lancer,  
et un internet que tu peux couper.  

Et si tu veux que même l'appli soit libre,  
l'autre option, c'est Ollama :  
open source, avec une appli sur Mac et Windows,  
et le terminal pour aller plus loin.  

Et en vrai, il n'y a pas de meilleur choix.  
Un contrat à relire,  
une question sur ta santé,  
un truc ultra perso :  
ça, tu le donnes au local.  
Et pour une entreprise, une PME,  
c'est encore plus vrai.  
Par contre, pour aller vite,  
garde aussi un modèle en ligne :  
il est plus fort.  
Du coup, la bonne architecture, c'est l'hybride.  
Un peu de local pour ce qui est perso,  
et le cloud pour tout le reste.  

Fable 5 est revenu, cette fois.  
Sauf que ton fichier, lui, n'est jamais parti :  
personne ne peut te le couper à distance.  

Dis-moi en commentaire ta carte graphique, ou ton Mac,  
et le modèle qui a tourné chez toi.  
Et si rien ne tient, écris-le aussi :  
on cherchera ensemble le bon modèle.  
Et la suite de la série, c'est juste là.  
