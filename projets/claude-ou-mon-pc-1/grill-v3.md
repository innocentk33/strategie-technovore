# Grill de la V3 : « 16 Go suffisent » (08/11/2026)

> Script critiqué : la V3 du 07/11, dans [`script.md`](script.md), corrigée dans le même fichier le 08/11 (les passages cités ci-dessous sont ceux d'avant correction). Faits : [`sources.md`](sources.md), S1 à S46. Skill : `youtube-script-grill`, mode B, variante storytelling. Débit de référence : 145 mots/min. Grill précédent : [`grill-v1.md`](grill-v1.md).

## Verdict

**V3 : 7,5/10. Après corrections : 8,5/10 (estimation).** La V3 a une vraie colonne vertébrale : la facture en trois lignes donne au spectateur un outil qu'il peut refaire avec sa carte, et ton Qwen lent devient une enquête qui se résout grâce à un indice planté en section 2 (la 5060 Ti avec ton fichier exact). C'est ce qu'aucune vidéo française ne fait. Le plus gros problème était le hook : **130 mots, environ 54 s**, alors que l'en-tête annonçait 32 s. Deuxième chantier : **quatre erreurs de faits** introduites par la réécriture, dont une qui contredisait la fin de la vidéo.

## Test des 30 secondes (V3 d'avant correction)

| Tranche | Ce que dit le script | Verdict |
|---|---|---|
| 0-5 s | > « Sur une RTX 5080, seize gigas, quelqu'un fait tourner Qwen, un vrai modèle de vingt-sept milliards de paramètres, à cent un tokens par seconde. » | 🟢 Raccord avec la miniature, un chiffre fort. Un peu longue : le « 101 » arrive à 7 s. « de paramètres » peut sauter. |
| 5-15 s | > « Un autre utilisateur, même carte, même modèle : treize. Huit fois moins. Et chez moi, sur la même carte, ce Qwen-là m'a paru super lent. » | 🟢 Le contraste et ton vécu, sans « cette carte, c'est la mienne ». « sur la même carte » répète « même carte ». |
| 15-30 s | > « J'ai fait aucun banc d'essai : j'ai rassemblé les mesures publiées, et j'ai refait les calculs. Et entre cent un et treize, il y a pas de meilleure carte. Il y a un fichier qui rentre, et un qui déborde. » | 🟠 La question centrale arrive vers 26 s, bien. Puis 15 mots de précaution déjà portés par le tampon « calculé, pas testé », et une fausse opposition (« il y a pas de meilleure carte » : personne ne l'a dit, la même carte vient d'être nommée). |
| Pont | > « Alors on va faire les comptes de ta carte, ligne par ligne. Et à la fin, je te dis ce qui clochait chez moi. » | 🟢 Deux boucles ouvertes : la méthode, et ton Qwen. Il arrive à 54 s : trop tard. |

**Budget V3** : 130 mots, environ 54 s.
**Coupé** : « de paramètres », « Il écrit bien plus vite que tu lis » (raccourci en « Plus vite que tu lis »), « sur la même carte », la phrase du banc d'essai (déplacée en tête de section 1), la fausse opposition.

**Réécriture appliquée (94 mots, environ 39 s)** :

> Sur une RTX 5080, seize gigas, quelqu'un fait tourner Qwen, un vrai modèle de vingt-sept milliards, à cent un tokens par seconde. Plus vite que tu lis. Un autre, même carte, même modèle : treize. Huit fois moins. Et chez moi, ce Qwen-là m'a paru super lent. Du coup, seize gigas, ça suffit ou pas ? Entre cent un et treize, la grosse différence, c'est le fichier : un qui rentre, un qui déborde. Alors on fait les comptes de ta carte, et à la fin, je te dis ce qui clochait chez moi.

- La question centrale tombe vers 22 s, le pont se termine vers 39 s. C'est encore au-dessus des 30 s visées : au débit d'une prise vive (170 mots/min), ça fait 33 s.
- « La grosse différence » au lieu de « la seule » : le 101 et le 13 n'ont pas les mêmes réglages (MTP, contexte), et la section 2 le dit.

## Tableau de bord

| Axe | V3 | Après corrections | En une phrase |
|---|---|---|---|
| 1. Promesse | 🟢 | 🟢 | « Si tu prends le bon fichier » est tenu dès la section 1, et le verdict reste pour la fin. |
| 2. Alignement | 🟢 | 🟢 | Tu cherches ce que le spectateur cherche : savoir ce que ta carte vaut, sans rêve vendu. |
| 3. Problème profond | 🟢 | 🟢 | « J'ai payé ma carte cher et ça rame » : ton Qwen lent le rend concret, et la fin le résout. |
| 4. Public & complexité | 🟠 | 🟢 | Section 1 dense (Gio, couches, kilo-octets). La facture à l'écran porte les chiffres ; Steam sortait du fil, il est déplacé. |
| 5. Valeur & originalité | 🟢 | 🟢 | Le budget refait avec le spectateur, l'agent compté en gigas, le débordement silencieux de Windows : personne en français. |
| 6. Structure & transformation | 🟢 | 🟢 | Fichier → vitesse → plus gros → Claude → enquête résolue : chaque section a besoin de la précédente. |
| 7. Histoire | 🟠 | 🟢 | V3 : une enquête, mais la fin concluait « exactement le problème de cette vidéo », trop fort pour deux suspects non prouvés. |
| 8. Mais / donc | 🟢 | 🟢 | « Sauf que Windows se sert aussi », « Et maintenant, le treize », « Sauf qu'un utilisateur l'a mesuré ». |
| 9. Engagement actif | 🟢 | 🟢 | « Fais le calcul avec moi », « Garde ce chiffre dans un coin », « Souviens-toi », et le Gestionnaire des tâches à ouvrir chez soi. |
| 10. Oralité & liaisons | 🟢 | 🟢 | 2,2 liaisons pour 100 mots (cible 1,5). Le patch de 3 Go avant l'écran titre est la meilleure traduction du script. |
| 11. Tics d'IA | 🟠 | 🟢 | Une fausse opposition dans le hook, deux « Ouais » + « six » presque identiques. |
| S1. 30 premières secondes | 🔴 | 🟠 | 54 s → 39 s à 145 mots/min ; la question centrale arrive avant 30 s, mais le pont déborde un peu. |
| S2. Le pont | 🟢 | 🟢 | Deux boucles, dont ton Qwen. |
| S3. Retournements | 🟢 | 🟢 | Le 13 (vers 5:00), la RAM qui s'inverse (6:50), « vitesse seulement » (8:00), « c'était pas la carte » (10:30). |
| S4. Planté / récolté | 🟢 | 🟢 | Le 4 bits de 14 Go (section 1, ajouté), le 80 % de la 5060 Ti (section 2), la RAM « presque inutile » (section 2) → récoltés en sections 3 et 5. |
| S5. Personnages | 🟠 | 🟠 | Toi, et des utilisateurs sans nom (ta règle). Normal pour une vidéo calculée. |
| S6. La fin | 🟢 | 🟢 | Elle résout ton Qwen, donne un geste à faire chez soi, puis ouvre sur le test Strata du 16 nov. |

## Le grill

### 1. Le hook durait près d'une minute
> « J'ai fait aucun banc d'essai : j'ai rassemblé les mesures publiées, et j'ai refait les calculs. »

**Pourquoi ça coince :** 130 mots, environ 54 s au débit de 145 mots/min, avec un en-tête qui annonçait 32 s. Sur une petite chaîne, c'est la minute qui coûte le plus. Cette phrase ne confirme rien, n'ouvre rien et ne fait rien monter : le tampon à l'écran la dit déjà.
**Correction (faite) :** la réécriture ci-dessus ; la phrase revient en tête de section 1 (« D'abord, je précise : … »), là où elle prépare la méthode.

### 2. « Les fichiers quatre bits passent pas » contredisait la fin
> « Résultat : les fichiers quatre bits qu'on te propose, entre seize et demi et dix-neuf gigas selon qui les publie, ils passent pas »

**Pourquoi ça coince :** faux en général. Ton propre fichier est un quatre bits (UD-IQ4_XS, 14,25 Go, S38) et il rentre, comme le Q4_K_S d'unsloth (15,36 Go). En section 5, tu dis « J'avais pris le fichier quatre bits de quatorze gigas » : un spectateur attentif voit la contradiction.
**Correction (faite) :** « le Q4_K_M, le quatre bits qu'on te propose le plus souvent, fait entre seize et demi et dix-neuf gigas » ; puis « Il existe des quatre bits plus serrés, vers quatorze gigas : c'est celui que j'avais pris, on en reparle à la fin. » Ça plante aussi ton fichier dès la section 1.

### 3. La comparaison sur la 5060 Ti mélangeait deux versions de Qwen
> « avec la version précédente de Qwen. Le fichier qui tient : vingt-six tokens par seconde. Le même modèle qui déborde de trois gigas : huit ou neuf. »

**Pourquoi ça coince :** le fichier qui tient (26,3 tok/s) est un Qwen3.8 ; celui qui déborde (7,7-9,2) est un Qwen3.6 (S41, précisé dans `sources.md`). « Le même modèle » est faux.
**Correction (faite) :** « Sur une seule carte, une 5060 Ti, quelqu'un a vécu les deux. Avec la version précédente de Qwen, son fichier débordait de trois gigas : huit ou neuf tokens par seconde. Avec un fichier du Qwen actuel qui tient dans la carte : vingt-six. Trois fois plus vite. »

### 4. Trois petites erreurs de faits
> « il reste moins de deux gigas pour la conversation et pour l'écran »

17,18 − 14,25 = 2,9 Go **avec** l'écran, environ 1,9 Go **une fois l'écran servi**. Corrigé : « une fois l'écran servi, il reste moins de deux gigas pour la conversation ».

> « plus faible hors de l'anglais et des langues asiatiques »

La doc dit l'anglais et le CJK : chinois, japonais, coréen. Le thaï ou le vietnamien sont aussi asiatiques. Corrigé.

> « Mais en tête de son rapport, il l'écrit lui-même »

Genre supposé, déjà corrigé une fois en V2. Corrigé : « la personne l'écrit elle-même ».

### 5. La fausse opposition du hook
> « Et entre cent un et treize, il y a pas de meilleure carte. Il y a un fichier qui rentre, et un qui déborde. »

**Pourquoi ça coince :** on réfute une idée que personne n'a eue (le script vient de dire « même carte »).
**Correction (faite) :** « Entre cent un et treize, la grosse différence, c'est le fichier : un qui rentre, un qui déborde. »

### 6. La fin promettait plus que l'enquête ne prouve
> « Bref, j'avais exactement le problème de cette vidéo. »

**Pourquoi ça coince :** tu présentes deux suspects, dont un seul est certain (la réflexion au maximum, qui n'est pas « le problème de cette vidéo »), et le second dépend de ton crochet sur le contexte. « Exactement » affirme ce que tu n'as pas mesuré. Même chose pour « Le premier, c'est sûr » : ce qui est sûr, c'est le réglage par défaut, pas qu'il explique tout.
**Correction (faite) :** « Le premier, je suis sûr qu'il était là » ; « Bref, ma carte était pas en cause : c'était ce que je lui demandais. » C'est une opposition, mais réelle : le spectateur pense depuis le hook que la carte est en cause.

### 7. Steam ouvrait la section 1 en détour
> « D'abord, t'es pas tout seul. Sur Steam, en octobre, plus d'un joueur sur quatre a une carte de seize gigas. »

**Pourquoi ça coince :** le pont vient de promettre les comptes de la carte ; le spectateur attend la première ligne, pas une statistique de contexte. Le chiffre est utile au moment où l'on parle des autres cartes.
**Correction (faite) :** déplacé avant les 8 et 12 Go : « Et si t'as pas seize gigas ? T'es loin d'être seul : sur Steam, en octobre, plus d'un joueur sur quatre a une carte de huit gigas, et un sur huit en a douze. »

### 8. Deux réactions jumelles
> « Ouais. Six fois le prix. » (section 3) et « Ouais, t'as bien entendu. Six. » (section 4)

Même mot, même chiffre, à une minute d'écart : l'oreille entend la recette. Corrigé : « Six fois le prix, pour les mêmes barrettes. » Le « t'as bien entendu » du 6 % reste.

### 9. Le budget oubliait le moteur
> « Là, il te reste environ quatre gigas. »

Des commentaires sous les vidéos concurrentes contestent qu'un IQ3_S + MTP avec 64K de contexte tienne en 16 Go : les tampons de calcul du moteur prennent aussi de la place. Corrigé : « environ quatre gigas, un peu moins une fois que le moteur s'est servi ». Le MTP est aussi relié : « le petit module d'accélération dont je te parlais ».

## Ce qu'il faut garder

- > « En fait, c'est le jeu qui te réclame un patch de trois gigas avant même l'écran titre. » Ta voix gamer, et la meilleure traduction d'un chiffre du script. Le rappel en section 4 (« le patch de trois gigas, c'est pas ta carte qui le paie ») la récolte.
- > « Garde ce chiffre dans un coin, il va servir. » / « Souviens-toi : la 5060 Ti en tire vingt-cinq tokens par seconde » : un vrai planté-récolté qui transforme une mesure en indice.
- > « Fais le calcul avec moi. » La section 3 se fait avec le spectateur.
- > « Pour le savoir chez toi : Gestionnaire des tâches, Performances, GPU » : la vidéo laisse un geste utile, ce que les concurrents ne font pas.
- La règle des noms est respectée partout : aucune chaîne citée dans la voix.

## Plan d'action

> **08/11 (soir), fait** : points 1 à 3 réglés avec tes réponses (contexte 64K puis 100K → le débordement est calculé ; ton choix écrit ; réglage de réflexion dans le panneau de droite). Tu as aussi retiré la phrase du banc d'essai en tête de section 1 : le tampon à l'écran suffit.

1. **Réponds au crochet ⟦à vérifier⟧ de la section 5** : avais-tu monté la longueur du contexte au-delà de 8 000 tokens ? Ça décide si le deuxième suspect est « possible » ou « probable ».
2. **Écris ton choix final** (⟦à écrire⟧ de la section 5), avec tes mots.
3. **Vérifie à l'écran de LM Studio** le réglage du niveau de réflexion avant de dire « tu peux le baisser dans les réglages du modèle » (S45 : pas confirmé dans la 0.4.28). Sinon, dis « dans les réglages avancés du modèle ».
4. **Lis le hook à voix haute et chronomètre** : vise 35 s au maximum. Si tu dépasses, coupe d'abord « Plus vite que tu lis », puis « Huit fois moins ».
5. Le jour de la voix : **le prix de la RAM** (92,95 € puis 560 €). Si le total dépasse 14 min, coupe d'abord le paragraphe AMD (environ 25 s).
