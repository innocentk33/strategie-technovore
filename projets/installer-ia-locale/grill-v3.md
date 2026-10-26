# Grill du script « Pourquoi avoir ta propre IA, et comment l'installer », V3 (25/10/2026)

> Script grillé : [`script.md`](script.md), V3 calée sur ta capture du 24/10, avec tes réponses du 25/10 (fin hybride comprise). Grille : `youtube-script-grill`, mode B, **variante storytelling** (test des 30 secondes, axe 10, axes S1 à S6), plus `anti-ia.md`.
> Hypothèses : titre *IA en local : installe ta propre IA, gratuite et sans abonnement* ; miniature « Hors ligne » de la [fiche](fiche.md) (la page « Ce site est inaccessible », la bulle de Gemma qui répond) ; public de 18-30 ans, surtout en Afrique, des PC modestes et de la data payée au giga ; débit de 145 mots/min (165 en rapide).
> Le grill de la V1 est dans [`grill-v1.md`](grill-v1.md). Ce grill ne touche pas au script : les corrections proposées sont en bas, à valider.

## Verdict

La V3 est nettement plus solide que la V1. Le tuto commence à 1:40 au lieu de 4:05, et la promesse de la miniature (« hors ligne ») est tenue deux fois, au hook puis en vrai à 6:50. Surtout, le script a enfin une crise : au test 3, le modèle tombe dans le panneau, puis se rattrape avec Think. C'est un échec honnête qui bat l'attente, et c'est le moment que les autres tutos n'ont pas.

Le plus gros problème est **la fin** : 1 min 23, avec Ollama au milieu, et une phrase qui se contredit (« il n'y a pas de meilleur choix… la bonne architecture, c'est l'hybride »). Juste après Ollama, le spectateur entend « pas de meilleur choix entre LM Studio et Ollama », pas « entre le local et le cloud ». Le reste se joue sur des détails d'écriture : un « Et » en tête d'une phrase sur trois, une fausse opposition (que j'ai écrite moi-même), et un trou de 55 s dans la section 3.

**Note globale : 🟢, 8/10.** Sur les 11 axes : 7 🟢, 4 🟠, 0 🔴. Variante storytelling : 4 🟢, 2 🟠. Avec les corrections ci-dessous, la V3 passerait à 8,5-9/10.

## Tableau de bord

| Axe | Note | En une phrase |
|---|---|---|
| 1. Promesse | 🟢 | « Installe » à 1:40, « hors ligne » à 0:00 et 6:50, le piège tenu à 8:00. Un seul accroc : « on l'installe maintenant », suivi d'une minute de « pourquoi ». |
| 2. Alignement | 🟢 | Aucune vente, l'aveu « moins fort que le cloud » est là, et la fin conseille l'hybride. |
| 3. Problème profond | 🟢 | Dépendre d'un service qu'on ne contrôle pas : posé par Fable 5, montré par internet coupé, récolté par « ton fichier n'est jamais parti ». |
| 4. Public & complexité | 🟢 | La VRAM, Think et « Full GPU Offload » sont traduits au moment où ils servent ; les noms (12B, QAT) sont renvoyés à leur vidéo. |
| 5. Valeur & originalité | 🟢 | Fable 5, et le même modèle qui tombe dans le piège puis le repère avec Think : aucun tuto français ne montre ça. |
| 6. Structure & transformation | 🟠 | Départ « on peut te couper ton IA », arrivée « ton fichier n'est jamais parti » : clair. La fin traîne (1:23) et Ollama y brouille le message. |
| 7. Histoire | 🟢 | Un tuto porté par un défi, avec une vraie crise (« il est tombé dans le panneau ») et une récompense (Think). |
| 8. Mais / donc | 🟠 | Très bon dans les sections 1 et 3 ; les tests s'enchaînent par numéros (« Test numéro deux », « Test numéro trois ») au lieu d'un « donc ». |
| 9. Engagement actif | 🟢 | « Toi, tu paries quoi ? » et « tu te rappelles le début ? » marchent ; il manque une question dans la section 3 (le trou de 55 s). |
| 10. Rythme & liaisons | 🟠 | 1,98 liaison pour 100 mots, c'est très bien. Mais 36 phrases sur 124 commencent par « Et », et « En gros » revient deux fois en 30 s. |
| 11. Tics d'IA | 🟠 | Une fausse opposition (« je ne vais pas te les expliquer : je vais te les montrer »), un faux suspens léger (« Et là, changement de ton »), une petite morale (« Voilà la leçon »), deux listes de trois dans la fin. |
| S1. Les 30 secondes | 🟢 | Les 6 questions passent ; à corriger : « il » pour « mon IA », « maintenant », et 84 mots (0:34). |
| S2. Le pont | 🟢 | « Je lui tends un piège. La première fois, il tombe dedans » ouvre une deuxième boucle, tenue à 8:00. |
| S3. Les retournements | 🟠 | Un toutes les 20 à 30 s presque partout ; deux trous : 3:21 → 4:16 (55 s) et 9:16 → 10:01 (45 s, la fin). |
| S4. Planté / récolté | 🟢 | Fable 5 (hook → fin), le clic d'internet coupé (hook → 6:50), les trois raisons, Gemma E4B (lancement → choix du modèle), Think (test 1 → test 3), Claude (section 1 → l'hybride). |
| S5. Personnages & enjeu | 🟢 | Toi, qui veux une IA qu'on ne peut pas te couper ; le modèle, qui a un vrai moment de faiblesse. |
| S6. La fin | 🟠 | Le rappel de Fable 5 retourne bien le hook ; mais l'hybride se contredit, et la fin est trop longue. |

## Test des 30 secondes

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Je coupe internet. Et mon IA me répond quand même. » | 🟢 Le sujet et la tension en 9 mots, raccord avec la miniature « Hors ligne ». |
| 5-15 s | > « Le douze juin, Anthropic a coupé Fable 5, le modèle le plus puissant qu'il ait jamais ouvert au public. Pour tout le monde. Trois jours après sa sortie. » | 🟢 Le contraste (une IA coupée à distance, la tienne non), daté et prouvé par le communiqué. « Pour tout le monde. Trois jours après sa sortie. » est la seule cascade de fragments du script : elle frappe, garde-la. |
| 15-30 s | > « Du coup, comment t'as une IA que personne ne peut te couper à distance ? Bah, tu la fais tourner chez toi, comme celle-là. Et la tienne, on l'installe maintenant, gratuitement. » | 🟢 La question centrale à 0:21, en mots simples. La réponse tombe 4 s plus tard, mais c'est voulu : la vraie question devient « comment l'installer », celle du titre. 🟠 « maintenant » : la section 1 commence par « Avant, je précise un truc », et l'installation arrive à 1:40. |
| Pont | > « Et à la fin, je lui tends un piège. La première fois, il tombe dedans. » | 🟢 Une deuxième boucle, et un demi-spoiler malin (« la première fois ») qui ouvre une troisième question : et la deuxième fois ? 🟠 « il » : jusque-là, on parle de « mon IA » et de « la tienne », au féminin. Le spectateur cherche une seconde qui est « il ». |

**Budget :** 84 mots ≈ 0:34 à 145 mots/min, 0:31 à 165. Un peu au-dessus de 30 s, sans phrase de trop : rien à couper.
**Les 15 premières secondes** (règle du 22/10) : internet coupé, la réponse et Fable 5 coupé y sont tous les trois. 🟢
**À corriger :** deux mots, voir le grill, point 5.

## L'axe 10 : les liaisons

Mesure sur le texte dit (sans `[VISUEL]` ni `[SON]`), 1 517 mots : **1,98 liaison pour 100 mots** avec la liste du grill (30), 1,52 avec la liste stricte (23). Par section : hook 1,2 ; section 1 : 2,5 ; section 2 : 1,6 ; section 3 : 2,0 ; section 4 : 2,1 ; fin : 2,0. Le hook est sous 1,5 parce qu'il est fait de phrases courtes et d'images : c'est voulu. Aucun « vous ».

Les deux défauts sont ailleurs :
- **Le « Et » de tête** : 36 phrases sur 124 (29 %) commencent par « Et ». Lu à voix haute, ça devient une litanie (« Et ce message… Et justement… Et si tu veux… Et en vrai… Et pour une entreprise… »). Le « Et » relie sans dire pourquoi : il ne compte pas comme liaison, et il en a l'air.
- **Les répétitions proches** : « En gros, tu as le droit de t'en servir » (4:10) et « En gros, le modèle tient en entier » (4:35) ; « Du coup, j'active Think » (8:10) et « Du coup, au travail » (8:42).

## Le grill

### 1. La fin se contredit, et Ollama la brouille

> « Et si tu veux que même l'appli soit libre, l'autre option, c'est Ollama […]. Et en vrai, il n'y a pas de meilleur choix. […] Du coup, la bonne architecture, c'est l'hybride. »

**Pourquoi ça coince :** deux problèmes.
- **Ollama juste avant** : « il n'y a pas de meilleur choix » s'entend comme « entre LM Studio et Ollama ». Ton message (le local ET le cloud) n'arrive qu'au bout de la phrase suivante.
- **La contradiction** : dire « pas de meilleur choix » puis « la bonne architecture, c'est l'hybride », c'est quand même en désigner une.

En plus, la fin dure 1 min 23 : c'est là que les spectateurs partent, et l'écran de fin doit arriver vite.

**Correction :**
- Ollama passe à la section 2, en une phrase, là où on parle déjà des moteurs (après « parce que c'est une vraie appli, sans terminal ») : « Et si tu préfères l'open source, Ollama fait le même boulot : le lien est en description. »
- La fin devient :

> « Voilà comment on a une IA à soi : un fichier sur ton disque, une appli pour le lancer, et un internet que tu peux couper.
> Bon, en vrai, tu n'as pas à choisir entre ça et le cloud. Un contrat à relire, une question sur ta santé : ça, tu le donnes au local. Et pour une PME, c'est encore plus vrai. Par contre, pour bosser vite, garde aussi un modèle en ligne : il est plus fort, et tu as vu qu'un petit modèle, il faut le guider. Du coup, la bonne architecture, c'est l'hybride : le local pour ce qui est perso, le cloud pour tout le reste.
> Fable 5 est revenu, cette fois. Sauf que ton fichier, lui, n'est jamais parti : personne ne peut te le couper à distance. »

- Ce que ça change :
  - la fin perd une vingtaine de secondes ;
  - la liste de trois (« un contrat, ta santé, un truc ultra perso ») passe à deux ;
  - « il est plus fort » s'appuie sur ce qu'on vient de voir (le piège) sans prétendre que le cloud aurait réussi, ce qu'on n'a pas testé.

### 2. La fausse opposition de la section 1 (c'est ma phrase)

> « Les deux autres, je ne vais pas te les expliquer : je vais te les montrer. »

**Pourquoi ça coince :** c'est la forme « pas A, mais B ». Personne n'attendait une explication, et la phrase réfute une idée que le spectateur n'avait pas. Je l'ai écrite pour remplacer ta tournure du « téléchargement » : elle règle un problème et en crée un autre.

**Correction :** « Les deux autres, tu vas les voir pendant les tests. » La phrase est plus courte, et la boucle reste ouverte : quels tests ?

### 3. Le trou de 55 s dans la section 3

> 3:21 « Sauf qu'elle est vide » → 4:16 « Et là, tu vas voir des noms bizarres »

**Pourquoi ça coince :** une minute d'explications à la suite (la VRAM, le gestionnaire des tâches, Model Search, la licence de Gemma), sans retournement ni question. Elles sont utiles, et c'est souvent là que la courbe plonge.

**Correction :** fais travailler le spectateur, et récolte sa réponse 80 s plus tard.
- Après « et lis la mémoire dédiée » : « Et toi, t'as combien ? Garde ton chiffre en tête, il va servir. Moi, c'est une RTX 5080 : seize gigas. »
- À 5:02, « Alors, si ta carte a huit gigas » devient « Alors, ton chiffre : si ta carte a huit gigas… ».
- Et pour la répétition : « En gros, le modèle tient en entier dans ma carte graphique » devient « Traduction : le modèle tient en entier dans ma carte graphique. »

### 4. Le test 3 ne dit pas que Think est coupé

> Test 1 : « Et comme j'avais activé Think… » ; test 3 : « Du coup, j'active Think, et je lui écris juste : réfléchis bien. »

**Pourquoi ça coince :** au test 1, Think est allumé. Au test 3, le spectateur ne sait pas qu'il est éteint, donc la récompense (« j'active Think ») arrive sans avoir été préparée, et la leçon a l'air d'un tour de magie. En plus, le passage des tests 2 à 3 se fait par un numéro, sans « donc ».

**Correction :**

> « Test numéro trois, le piège. Et cette fois, Think est coupé. Je lui colle un faux message… »

Ensuite, pour enlever l'annonce et la petite morale :
- « Et là, changement de ton. Il liste les signaux d'alerte » devient « Cette fois, il liste les signaux d'alerte » ;
- « Voilà la leçon : un petit modèle, ça se guide. Laisse-le réfléchir. » devient « Donc, avec un petit modèle, sur un truc sensible : active Think. » C'est un conseil qu'on applique tout de suite, et il ne dit pas « toujours », puisqu'on n'a fait qu'un essai (voir les faits du script).
- « Du coup, au travail, ton code… » devient « Au travail, pareil : ton code ou les mails d'un client ne sortent pas de ta machine. » Ça évite le deuxième « Du coup » en 30 s.

### 5. Deux mots dans le hook

> « Et la tienne, on l'installe maintenant, gratuitement. […] La première fois, il tombe dedans. »

**Pourquoi ça coince :**
- « maintenant » promet le geste tout de suite, et la phrase suivante est « Avant, je précise un truc ». Le spectateur qui attendait l'installation entend « avant » à 0:34 : c'est un petit mensonge, au pire moment.
- « il » arrive alors qu'on parle de « mon IA » depuis le début.

**Correction :** « Et la tienne, on l'installe ensemble, gratuitement. » ; « La première fois, elle tombe dedans. » Même nombre de mots.

### 6. Le « Et » de tête

**Pourquoi ça coince :** voir l'axe 10, 29 % des phrases. Au téléprompteur, c'est ce qui fait « récité ».

**Correction :** enlève le « Et » de ces phrases. Elles tiennent seules, ou leur liaison est déjà dans la phrase d'avant :
- « Ça arrive aussi ailleurs. » (1:00)
- « Au premier lancement, il te propose déjà un modèle » (3:05)
- « Pour le choisir, retiens une seule chose » (3:30)
- « C'est pour ça que j'ai pris LM Studio » (4:55)
- « Dès que c'est fini, je lui fais passer trois tests. » (6:04)
- « Comme j'avais activé Think » (6:30)
- « Voilà la deuxième raison : ni abonnement, ni internet. » (7:28)

On descend à 23 %. Garde les « Et » qui portent une surprise ou une relance : « Et mon IA me répond quand même », « Et maintenant, tu te rappelles le début ? », « Et en effet, il répond », « Et il me conseille même ».

## Ce qu'il faut garder

- **« Je coupe internet. Et mon IA me répond quand même. »** : neuf mots, la miniature, la preuve. Le meilleur début de la série.
- **« Sauf que le douze juin, en fait, ce n'était même pas le choix d'Anthropic : c'est le gouvernement américain qui l'a exigé. »** C'est la seule opposition du script qui est juste : elle corrige ce que le hook a fait croire (« Anthropic a coupé »). Garde-la.
- **« Il réfléchit en anglais : « Macon, c'est un perso de The Boys ? » Non. »** : drôle, vrai, et ça montre ce que fait Think mieux qu'une définition.
- **« J'actualise… toujours rien. »** : la preuve dite en trois mots, avec la tension du geste.
- **« Toi, tu paries quoi ? »** puis **« Bref, il est tombé dans le panneau. »** : le pari, puis l'échec avoué. C'est le retournement de la vidéo.
- **« Tu ne grilles pas des gigas de data pour un modèle qui ne tournera jamais bien chez toi. »** : la raison du choix de LM Studio, dite pour ton public, qui paie la data au giga.
- **« Fable 5 est revenu, cette fois. Sauf que ton fichier, lui, n'est jamais parti. »** : la boucle du hook refermée.

## Plan d'action

1. **La fin** (point 1) : Ollama passe en section 2, et l'hybride est réécrit sans contradiction. C'est le plus gros gain.
2. **Le test 3** (point 4) : « cette fois, Think est coupé », plus les trois retouches.
3. **La section 3** (point 3) : « Et toi, t'as combien ? », récolté à 5:02.
4. **Le hook et la section 1** (points 2 et 5) : « ensemble », « elle », « tu vas les voir pendant les tests ».
5. **Les « Et » de tête** (point 6), puis on régénère le téléprompteur et on remesure.

## Faits

Rien de neuf à sourcer dans les corrections :
- **« un contrat à relire »** : LM Studio lit les .docx, .pdf et .txt joints à la discussion (F30) ;
- **« il est plus fort »** : c'est l'aveu de la section 3, que Claude #1 chiffrera ;
- **« tu as vu qu'un petit modèle, il faut le guider »** : c'est ce que montre le test 3, sans dire « toujours ».

La phrase « LM Studio est gratuit, à la maison comme au travail : ils l'ont annoncé en juillet 2025 » attribue bien l'annonce, comme le demandent F16 à F18. Elle reste juste.
