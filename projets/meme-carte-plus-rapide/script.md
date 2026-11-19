# Même carte, 2 fois plus rapide : script (V3, 18/11/2026)

**Sortie** : jeu. 19/11/2026, 18 h. **Vidéo calculée** (décision du 15/11) : aucun nouveau test, aucune vitesse à toi. Faits : [`sources.md`](sources.md) (M1…M38, F). La V2 reste dans [`script-v2.md`](script-v2.md), la V1 dans [`script-v1.md`](script-v1.md), sa critique dans [`grill-v1.md`](grill-v1.md).

### V3 corrigée après grill-v3, 18/11

Appliqué de [`grill-v3.md`](grill-v3.md) : B1 (« 6 mesures publiées » et « j'ai rien testé » vers 0:17, conditions avant le plan), B2 variante A (la révélation reste ouverte : « un réglage que tu as peut-être allumé pour aller plus vite » ; plus de « qui ne la change pas », faux d'après M26-M27), B3 (« je n'ai trouvé écrit nulle part »), B4 (téléprompteur à 15 mots par ligne au plus), A1 (llama.cpp nommé comme le moteur), A2 (Flash Next « beaucoup trop gros pour 16 gigas »), A3 (82 % et 8 % rattachés au modèle de 7 milliards ; qualité des 6 mesures non mesurée), A4, A5, A6, A7 (3080 de PC portable, M28 = M14), A8, A10, A11. Refusé : A9 (dernière phrase imposée), A12 (rallonge), A13 (hook de l'auteur mot pour mot), variante B du plan (« divisée par 3 » vient de M13, un débordement forcé, pas d'un fichier qui déborde).

**18/11, tes retouches** : le MTP de LM Studio est dans le panneau des réglages du modèle sélectionné (ton constat, à la place de « je n'ai trouvé écrit nulle part ») ; le passage « une chaîne française vient de passer de 8 à 83 » est supprimé (M38 ne sert plus dans la voix).

### V3 du 18/11 : ce qui change

1. **Script complet** : plus aucun crochet à dire (voir la note ci-dessus pour la section 1).
2. **Un seul renvoi** dans le corps : section 4, « Dans la vidéo précédente, je te l'ai montré » [F]. Le seul autre « lundi » est l'annonce finale.
3. **Hook** à ta phrase (29 → 64, M5 ; ta paire 24 → 50 n'existe pas dans les sources). L'origine des chiffres est dite une fois, avant 30 s.
4. **Plan** sur ton idée : « doubler », jamais « décupler » (×1,9 à ×2,3).

| | |
|---|---|
| **Titre visé** | « 16 Go de VRAM : le réglage qui fait écrire 2 fois plus vite, et celui qui ne sert à rien » (inchangé) |
| **Durée estimée** | 1612 mots : ≈ 11 min 07 s à 145 mots/min (voix posée) ; ≈ 6 min 55 s à 233 mots/min (débit mesuré sur la vidéo Strata, d'après `grill-v3.md`) |
| **Liaisons pour 100 mots** | ≈ 1,86 sur la liste courte (30 liaisons) |

## Structure

| Temps (≈) | Partie | Ce qui s'y passe | Relance qui la ferme |
|---|---|---|---|
| 0:00-0:20 | 0. Hook | « tu allumes un seul paramètre » : 29 → 64 ; 6 mesures ; « bridée ? » | — |
| 0:20-0:55 | 0 bis. Plan et conditions | doubler · le moteur · ce qu'il faut éviter · le réglage à démystifier ; mesures publiées, écriture, modèle qui tient | « Ce réglage, c'est le MTP » |
| 0:55-2:50 | 1. Le MTP | Le clavier ; le prompt ; 5 cartes ; la mesure à part ; code contre texte ; « bridée » | « Sauf que le MTP a un prix » |
| 2:50-4:30 | 2. Le fichier qui tient | 20 → 45 ; la falaise ; pas d'addition ; abonne-toi | « Mais tout ça dépend aussi du moteur » |
| 4:30-5:35 | 3. Le moteur et sa version | Ollama, LM Studio ; Strata qui ralentit ; note ta version | « Et si ton modèle est trop gros ? » |
| 5:35-7:00 | 4. Le modèle qui déborde | **Le seul renvoi** ; la vidéo française ; les experts | « Maintenant, le piège » |
| 7:00-8:05 | 5. Le piège du contexte | 29 → 20 ; la 4080 qui retombe ; deux gestes | « il reste un dernier réglage » |
| 8:05-9:45 | 6. Le réglage qui ne sert à rien pour la vitesse | Question ; pas de vitesse ; de la place ; 8 bits | — |
| 9:45-10:50 | 7. La liste, la réponse, la suite | Checklist ; « bridée ? » ; Qwen 27B sur 8 Go | — |

Timecodes estimés à 145 mots/min, à recaler sur la voix montée.

**Conventions** : texte normal = voix. `[VISUEL : …]` = plan. `[M…]`, `[F]`, `[CALCUL]` = identifiant de `sources.md`, ne se lit pas. Aucun nom de chaîne ni de créateur dans la voix.

---

## 0. Hook (0:00 – 0:28)

[VISUEL : plein écran, le compteur de la miniature (aiguille, zone rouge). Bandeau en bas, permanent : « Mesure publiée · RTX 5060 Ti 16 Go · Qwen3.8-27B · écriture · même fichier · seul le MTP change ». L'aiguille se pose sur 29, un clic d'interrupteur, elle file à 64 et « 2× » s'allume. Pas de titre, pas de logo.]
Sur une carte de 16 gigas, tu allumes un seul paramètre, et ton IA écrit 2 fois plus vite : de 29 à 64 tokens par seconde [M5]. Même fichier, même carte, rien acheté.

[VISUEL : les six cartes qui tombent l'une après l'autre en vignettes (5080, 5060 Ti, 4060 Ti, RX 9060 XT, 5060 Ti, 3080 Ti portable), chacune avec son « ×1,9 » à « ×2,3 » ; puis « TA CARTE BRIDÉE ? » en gros, le texte de la miniature.]
Et c'est ce que trouvent 6 mesures publiées, sur 5 modèles de cartes de 16 gigas : entre 1,9 et 2,3 fois plus vite [M1-M6]. Du coup, ta carte, elle serait pas bridée, sans que tu le saches ?

Et attention : ça vaut pour l'écriture, sur Qwen 3.8 27B, un modèle qui tient en entier dans la carte [M1-M6].

---

## 0 bis. Le plan, et ses conditions (0:28 – 1:00)

[VISUEL : le plan en 3 lignes qui s'écrivent avec la voix : « LE RÉGLAGE ×2 » · « LE BON MOTEUR » · « CE QU'IL FAUT ÉVITER : −30 %, −1/3 » ; la 4e ligne arrive en rouge : « LE RÉGLAGE QUI NE SERT À RIEN (POUR LA VITESSE) ».]
Aujourd'hui, on va voir le réglage qui peut doubler la vitesse de ta carte graphique [M1-M6], et le moteur qui te permet d'y arriver [M8, M30b, § A]. Et surtout, tout ce qu'il faut éviter pour ne pas perdre ce que tu as gagné : une conversation trop longue, et c'est déjà un tiers de ta vitesse qui part [M22]. Et reste jusqu'à la fin, parce qu'on va démystifier un réglage que tu as peut-être allumé pour aller plus vite [M26-M28].

---

## 1. Le réglage qui double : le MTP (1:00 – 3:03)

[VISUEL : un clavier de téléphone qui propose trois mots au-dessus des touches ; puis la même idée sur fond sombre : le modèle pose 3 tokens fantômes d'avance, une coche verte les valide d'un coup ; un fantôme faux devient rouge et disparaît.]
Le réglage qui double, c'est le MTP, un petit module en plus dans le modèle. En gros, c'est comme les suggestions du clavier de ton téléphone : le modèle propose plusieurs tokens d'avance, puis il les vérifie tous d'un coup. Et quand il a deviné juste, il en écrit plusieurs pour le prix d'un.

[VISUEL : deux barres « ÉCRITURE » qui s'allonge, « LECTURE DU PROMPT » qui raccourcit, étiquette « premiers tests, mai 2026 » (M7).]
Par contre, ça ne joue que sur l'écriture. La lecture de ton prompt, elle, ralentissait avec le MTP dans les premiers tests de mai [M7].

[VISUEL : la ligne « RTX 5080 16GB » du tableau public, 53,4 → 101,3 surlignés, noms floutés (M1) ; puis les vignettes 4060 Ti (M3) et RX 9060 XT (M4).]
Sur une 5080, on passe de 53 à 101 [M1]. Sur une 4060 Ti, de 17,6 à 40 [M3]. Et même chez AMD, sur une RX 9060 XT, de 15 à presque 29 [M4]. Donc même la Radeon double presque.

[VISUEL : « 5 SUR 6 : MÊME TABLEAU, MÊME SCRIPT » ; la vignette du testeur du hook se détache : « mesuré à part · 5 essais ».]
Sauf que 5 de ces 6 mesures viennent du même tableau en ligne, avec le même script de test [M1-M6]. Du coup, la plus solide, c'est celle du début, le 29 à 64 : elle a été mesurée à part, 5 fois [M5]. Et elle trouve pareil.

[VISUEL : deux barres côte à côte sur la 4060 Ti : « TEXTE ×1,8 » et « CODE » plus haute, sans chiffre ; puis une icône de modèle à experts avec « ×1,5 ».]
En fait, dans le tableau, ce « 2 fois », c'est une moyenne sur du code, du texte et des commandes, avec la réflexion coupée [M1-M6]. Sur du texte seul, ça tombe à 1,8 fois sur la 4060 Ti [M3]. C'est sur du code que ça gagne le plus [M3]. Et sur un modèle à experts, les mesures tombent à 1,5 fois au mieux [M10, M11].

[VISUEL : un terminal, la commande llama.cpp avec `--spec-type draft-mtp` surligné ; puis deux noms de fichiers côte à côte, celui avec « -mtp » surligné (S38 de M8) ; puis la page des nouveautés de LM Studio 0.4.22, « MTP » surligné (M30b).]
Alors, pourquoi je dis « bridée » ? Parce que dans llama.cpp, le MTP ne s'allume pas tout seul. Il faut le demander, et il faut un fichier qui contient le module, un petit bout de modèle en plus [M8]. LM Studio, lui, le gère depuis la version 0.4.22 [M30b]. Tu le trouves dans le panneau des réglages du modèle que tu as sélectionné [ton constat du 18/11]. Donc, que tu sois sur l'un ou sur l'autre, va vérifier qu'il est bien allumé chez toi.

---

## 2. Celui à faire avant lui : le fichier qui tient (3:03 – 4:53)

[VISUEL : une jauge de VRAM de 16 Go qui se remplit : le modèle, puis un bloc « MTP » qui s'ajoute et touche le bord rouge.]
Sauf que le MTP a un prix : il prend de la place. Selon les mesures, entre 1 et 2,5 gigas de VRAM en plus [M9]. Et sur une carte de 16, c'est justement là que ça coince [M9].

[VISUEL : la page du banc de la 4080 (M12), les deux lignes surlignées : « IQ4_XS 15,0 Go · 20,5 » et « UD-IQ3_XXS 11,5 Go · 45,3 », étiquette « Qwen3.5-27B » ; une flèche vers le haut.]
Donc le vrai réglage numéro un, c'est que le modèle tienne en entier dans la carte. Sur une 4080 de 16 gigas, avec un Qwen de 27 milliards plus ancien : un fichier de 15 gigas qui déborde un peu, 20 tokens par seconde. Un fichier de 11,5 gigas qui tient, 45 [M12]. Plus du double, juste en prenant un fichier plus petit.

[VISUEL : une courbe en falaise : « toutes les couches sur la carte · 43 » puis « 8 couches dehors · 12,5 », étiquette « Qwen2.5-Coder-14B, débordement forcé » (M13).]
Et si une partie du modèle sort de la carte, c'est la chute. Sur une 5060 Ti, quelqu'un a laissé dehors exprès 8 couches sur 48 d'un modèle plus petit : on tombe de 43 à 12,5 [M13]. En fait, la partie restée en RAM va beaucoup plus lentement, et la carte l'attend [M16, CALCUL].

[VISUEL : une étiquette « QUALITÉ PERDUE : NON MESURÉE ».]
Par contre, un fichier plus petit est plus compressé, et aucune de ces mesures ne dit ce que tu perds en qualité [M12].

[VISUEL : deux blocs « MTP » et « FICHIER QUI TIENT » qui ne s'empilent pas ; un panneau « ×2 ET ×2 ≠ ×4 ».]
Sauf que ces 2 gains ne s'additionnent pas. Si le MTP fait déborder ton fichier, la chute mange ce qu'il te fait gagner [M9, M13, CALCUL]. Du coup, d'abord un fichier qui tient avec la place du MTP, ensuite le MTP.

[VISUEL : retour au compteur du hook, l'aiguille à « 2× » ; ton visage ou la caméra si tu en filmes une.]
Bon, rien qu'avec ces 2 réglages, ton modèle peut écrire jusqu'à 2 fois plus vite, sur la carte que tu as déjà [M1-M6, M12]. Donc avant d'en racheter une plus grosse, essaie ça. Si cette vidéo t'a évité un mauvais achat, abonne-toi.

---

## 3. Le moteur, et sa version (4:53 – 5:58)

[VISUEL : trois barres « llama.cpp 77,0 · LM Studio 76,8 · Ollama 69,1 » sur une 5060 Ti, étiquette « 1 testeur » (M29) ; puis la 3090 avec « −30 % » sur Ollama (M30).]
Et le moteur qui te permet d'y arriver, le programme qui fait tourner le modèle, c'est llama.cpp : les 6 mesures du début ont toutes été faites dessus [§ A, M1-M6]. Quand tout tient dans la carte, Ollama a été mesuré 10 % plus lent que llama.cpp, sur une 5060 Ti [M29]. Et jusqu'à 30 % plus lent, sur une 3090 [M30]. Et LM Studio était presque à égalité avec llama.cpp : 76,8 contre 77 [M29]. Du coup, si tu es sur LM Studio, de ce côté-là, t'es tranquille.

[VISUEL : les deux tickets de Strata (M31), « 117,0 » contre « 86,1 » surlignés ; puis la page de la 0.2.14 (M32), « chat 17,5 (19,4) » surligné ; enfin une carte texte « Versions du 15/11/2026 : llama.cpp v1.0.0 · LM Studio 0.4.28 · Ollama 0.40.16 · Strata 0.2.14 » (M33-M36), qui reste à l'écran pendant la dernière phrase.]
Et même une mise à jour peut te ralentir. Sur une 5080 avec Strata, un autre moteur, un utilisateur a perdu 25 % en passant à une version plus récente [M31]. Et sa version 0.2.14, sortie le 15 novembre, lit ton prompt plus vite, mais écrit environ 10 % moins vite sur une 5070 Ti, d'après le projet lui-même [M32, M36]. Voilà pourquoi il faut noter ta version, pour savoir d'où vient un ralentissement. Celles du 15 novembre sont à l'écran [M33-M36].

---

## 4. Et si ton modèle déborde : les experts (5:58 – 7:19)

[VISUEL : la capture du moniteur de Strata de la vidéo précédente (MON3), recadrée sur la RAM et la lecture disque, **sans le compteur de vitesse** ; sa miniature (2 s), seul renvoi visuel de la vidéo.]
Et si ton modèle est trop gros pour la carte ? Dans la vidéo précédente, je te l'ai montré : la RAM pleine, et le disque qui se met à lire [F].

[VISUEL : un schéma de la carte et de la RAM : des petits blocs « experts » qui passent de l'une à l'autre ; en surimpression, `--n-cpu-moe` puis `--moe-cache-mib` ; puis deux vignettes « 3060 12 Go +12 % » (M17) et « 5060 Ti 16 Go +29 % » (M19), tampon « 1 MESURE », étiquette « PC de 32 et 64 Go de RAM ».]
Sur un modèle à experts, dans llama.cpp, il y a un réglage à toi : où vont les experts, ces petits spécialistes du modèle. Lesquels restent sur la carte, et lesquels partent en RAM. Le bon réglage, c'est d'en garder sur la carte autant que possible, juste avant que ça plante [M17, CALCUL]. Sur une 3060 de 12 gigas, ça a fait gagner 12 % [M17]. Sur une 5060 Ti de 16, avec le cache d'experts arrivé dans llama.cpp en octobre, 29 % [M18, M19]. Une seule mesure chacune, donc à prendre avec des pincettes. Et leurs PC avaient 32 et 64 gigas de RAM [M17, M19].

---

## 5. Le piège qui te vole un tiers de ta vitesse : le contexte (7:19 – 8:28)

[VISUEL : une conversation qui s'allonge à l'écran, le compteur du hook qui descend : « 4 000 tokens · 29 » → « 32 000 · 24 » → « 64 000 · 20 » ; puis la ligne avec MTP : « 64 » → « 39 », le « ×2 » qui reste affiché entre les deux (M5, M22).]
Maintenant, le piège. Plus ta conversation est longue, plus ça ralentit. Tu te rappelles la mesure du début, à 29 tokens par seconde ? À 64 000 tokens de conversation, elle tombe à 20 [M22]. Donc un tiers de vitesse en moins. Et avec le MTP, les 64 deviennent 39 [M22]. Le MTP double toujours, mais tout descend [M5].

[VISUEL : retour à la page de la 4080 (M23), même fichier de 11,5 Go : la courbe « 45 » → « 23 à 64 000 » → « moins de 10 à 128 000 », la jauge de la carte où la mémoire de la conversation pousse le modèle dehors ; la falaise de la section 2 en fond.]
Et ça peut être bien pire. En fait, la mémoire de la conversation se range aussi dans la carte. Et la 4080 qui montait à 45 avec le petit fichier ? À 128 000 tokens de conversation, cette mémoire pousse le modèle dehors, et la carte tombe sous les 10 tokens par seconde [M23]. La falaise, encore.

[VISUEL : deux gestes en icônes : « + NOUVELLE CONVERSATION » et un curseur « longueur de conversation » qu'on baisse.]
Bref, 2 gestes tout bêtes : une nouvelle conversation dès que tu changes de sujet, et une taille de conversation réglée au plus juste dans ton moteur [CALCUL]. Et si tu as vraiment besoin d'une longue conversation, il reste un dernier réglage.

---

## 6. Le réglage qui ne sert à rien pour la vitesse : le cache KV compressé (8:28 – 9:52)

[VISUEL : plein écran, « COMPRESSER LE CACHE KV = PLUS VITE ? », un point d'interrogation qui clignote ; 1 s de silence après la question.]
Ce réglage, c'est compresser le cache KV, la mémoire de la conversation. À ton avis, est-ce que ça fait écrire plus vite ? Garde ta réponse.

[VISUEL : trois barres sur une 5060 Ti : « normal 81,8 · 8 bits 76,4 · 4 bits 80,3 », étiquette « modèle de 7 milliards » (M26) ; puis « 4 bits : −35 % à 64 000 tokens » (M27), étiqueté « machine Nvidia pour l'IA, pas une carte de joueur » ; tampon final « VITESSE : NON ».]
Sur une 5060 Ti, avec un petit modèle de 7 milliards, l'écriture est 6,6 % plus lente en 8 bits, et 1,8 % plus lente en 4 bits [M26]. Et sur une machine de Nvidia faite pour l'IA, en 4 bits, à 64 000 tokens, elle perd même 35 % [M27]. Donc pour la vitesse, il ne sert à rien.

[VISUEL : la jauge de conversation qui s'étire : « 32 000 » → « 128 000+ » (M28) ; puis une jauge de carte neutre (sans nom de carte) : la conversation compressée prend moins de place, le modèle reste dedans (illustration, pas une mesure).]
Sauf qu'il fait de la place. Sur une 3080 de PC portable de 16 gigas, avec Qwen 3.8 27B, on passe de 32 000 à plus de 128 000 tokens de conversation [M28]. Du coup, il fait tenir beaucoup plus de conversation dans la carte, avant que le modèle soit poussé dehors [M28, CALCUL]. Il ne t'évite pas le tiers de vitesse en moins, puisque la mesure du début avait déjà le cache compressé [M5]. Par contre, il peut t'éviter la falaise.

[VISUEL : deux jauges de ressemblance avec la réponse d'origine : « 8 bits · 82 % » en vert, « 4 bits · 8 % » en rouge (M26) ; puis les six vignettes du hook, trois d'entre elles marquées « cache en 4 bits » (M1, M4, M5).]
Attention au 4 bits, quand même. Sur le petit modèle de 7 milliards de tout à l'heure, la réponse en 8 bits ressemble à 82 % à celle d'origine. En 4 bits, à 8 % seulement [M26]. Et au moins 3 des 6 mesures du début étaient en 4 bits, sur un modèle bien plus gros : ce que ça leur a coûté en qualité, aucune ne le dit [M1, M4, M5, M26]. Du coup, si tout tient en 8 bits chez toi, reste en 8 bits. Voilà le réglage démystifié : lui, il sert à tenir plus longtemps [M26, M28].

---

## 7. La liste, la réponse, et la suite (9:52 – 10:34)

[VISUEL : la checklist qui s'écrit, une ligne par phrase, chaque ligne avec son repère : « FICHIER QUI TIENT · au moins ×2 » · « MTP · jusqu'à ×2, code » · « llama.cpp / LM Studio · Ollama −10 à −30 % » · « EXPERTS · +12 à +29 %, 1 mesure » · « CONVERSATION NEUVE · −1/3 à 64K » · « CACHE 8 BITS · place, pas vitesse » · « NOTE TA VERSION » ; en bas, en petit et en permanence : « ×2 ET ×2 ≠ ×4 ».]
Donc, dans l'ordre : un fichier qui tient dans ta carte, avec la place du MTP. Le MTP allumé, surtout pour du code. Llama.cpp ou LM Studio, plutôt qu'Ollama. Si ton modèle déborde, règle où vont les experts. Une conversation neuve quand elle s'allonge. Le cache en 8 bits si tu manques de place. Et note ta version.

[VISUEL : retour à la miniature, « TA CARTE BRIDÉE ? » ; le point d'interrogation tombe.]
Alors, ta carte, bridée ? Si le MTP est éteint, ou si ton fichier déborde, oui. Et ça se répare ce soir, sans rien acheter.

[VISUEL : écran de fin, carte vers « Qwen 27B sur une carte de 8 Go » (lun. 23/11) ; « 32 Go de VRAM » est passée au lun. 30/11 (16/11).]
Et si ta carte n'a que 8 gigas, lundi, on regarde le nouveau fichier qui fait tenir Qwen 27B en entier dedans. Allez, salut !

> 16/11 : fin réécrite, la vidéo de lundi 23/11 est « Qwen 27B sur 8 Go » ; « 32 Go de VRAM » passe au 30/11. « Tient en entier » est à confirmer dans `../qwen-27b-8go/sources.md` avant d'enregistrer.

---

## Chiffre → source

| Chiffre dit (section) | Ce que c'est | Source |
|---|---|---|
| 29 → 64 tok/s, « 2 fois plus vite » (0, 1, 5) | RTX 5060 Ti 16 Go, Qwen3.8-27B, testeur indépendant, médiane de 5, 4K, sans → avec MTP, écriture (29,18 → 63,89, ×2,19) | M5 |
| 6 testeurs, 5 modèles de cartes, ×1,9 à ×2,3 (0) ; « jusqu'à 2 fois » (2) | Six mesures du MTP sur 16 Go | M1-M6 |
| Écriture, modèle qui tient dans la carte, leurs chiffres (0 bis) | Conditions de § A et § H | M1-M6 |
| « Le moteur qui te permet d'y arriver » = llama.cpp, les 6 mesures faites dessus (0 bis, 3) | En-tête de § A | M1-M6, M8 |
| Un tiers de ta vitesse (0 bis, 5) | −32 % de 4K à 64K | M22 |
| La lecture du prompt ralentissait en mai (1) | P ×0,51 et ×0,60, deux machines à deux cartes, Qwen3.6 ; aucun chiffre dit | M7 |
| 53 → 101 sur 5080 (1) | RTX 5080, MTP | M1 |
| 17,6 → 40 (1) | RTX 4060 Ti, MTP | M3 |
| 15 → presque 29, « double presque » (1) | RX 9060 XT, 15,2 → 28,7 (×1,89) | M4 |
| 5 des 6 mesures du même tableau (1) | Même dépôt, même `probe.py` | M1-M6 (conclusion de § A) |
| Le testeur du début mesuré à part, 5 fois (1) | Blog indépendant, médiane de 5 | M5 |
| Moyenne code + texte + commandes, réflexion coupée (1) | Conditions du ×2 | M1-M6 (conditions de § A) |
| ×1,8 sur du texte (1) | 4060 Ti, 17,6 → 32,3 | M3 |
| ×1,5 sur un modèle à experts (1) | MoE 35B-A3B, 98 → 144 (×1,47) | M10, M11 |
| MTP non automatique, fichier qui contient le module (1) | `--spec-type draft-mtp` ; fichier « -mtp » | M8 (et § H) |
| LM Studio 0.4.22 (1) | Support du MTP, 28/08/2026 | M30b |
| LM Studio 0.4.28 (visuel de 3) | Version du jour | M35 |
| « personne n'a vérifié s'il l'allume tout seul » (1) | Réglage par défaut non vérifié | M30b |
| « il sert à tenir plus longtemps » (6) | Pas de vitesse, de la place | M26, M28 |
| « Beaucoup trop gros pour 16 gigas » (4) | 125 milliards ; fichier de 78 Go | M37, M19 |
| 3080 de PC portable 16 Go, 32 000 → 128 000+ (6) | Autodidacts | M28, M14 |
| 1 à 2,5 Go de VRAM en plus (2) | +1,16 ; +1,58 ; +2,49 Gio | M9 |
| 15 Go qui déborde, 20 tok/s → 11,5 Go qui tient, 45 (2) | RTX 4080 16 Go, Qwen3.5-27B, 20,5 → 45,3 | M12 |
| 8 couches sur 48 dehors, 43 → 12,5 (2) | RTX 5060 Ti, Qwen2.5-Coder-14B, `-ngl 40` | M13 |
| La partie en RAM va plus lentement, la carte l'attend (2) | « spilling to system RAM collapses throughput » ; le reste est une explication | M16, CALCUL |
| Qualité perdue non mesurée (2) | Aucune page ne la mesure | M12 (conclusion de § B) |
| Les gains ne s'additionnent pas (2) | Le MTP prend de la VRAM ; la falaise | M9, M13, CALCUL |
| « jusqu'à 2 fois », sur la carte que tu as (2) | MTP ×1,9 à ×2,3 ; fichier qui tient ×2,2 ; jamais multipliés | M1-M6, M12 |
| Ollama −10 % (3) | 77,0 contre 69,1, RTX 5060 Ti, un testeur (le modèle, repris de B et non relu, n'est pas dit) | M29 |
| Ollama jusqu'à −30 % (3) | RTX 3090, ×1,41 en faveur de llama.cpp | M30 |
| LM Studio 76,8 contre 77 (3) | RTX 5060 Ti, même testeur | M29 |
| −25 % après une mise à jour (3) | Strata, RTX 5080, moteur 0.1.54 → 0.1.56 | M31 |
| 0.2.14 du 15/11, écriture −10 % sur 5070 Ti (3) | Chiffres du projet ; ta vidéo en 0.2.13 | M32, M36 |
| Versions du 15/11 à l'écran (3) | llama.cpp v1.0.0, LM Studio 0.4.28, Ollama 0.40.16, Strata 0.2.14 | M33, M35, M34, M36 |
| « Dans la vidéo précédente », RAM pleine, disque qui lit (4) | Seul renvoi ; vidéo Strata, **pas un avant** ; aucun chiffre redit | F (T45, srt 4:36-4:51) |
| Garder sur la carte autant d'experts que possible, juste avant que ça plante (4) | `-ncmoe 29` le meilleur, `-ncmoe 26` = OOM (3090) ; la règle est une déduction | M17, CALCUL |
| +12 % sur 3060 12 Go (4) | `--n-cpu-moe` ajusté, Flash-Next | M17 |
| +29 % sur 5060 Ti 16 Go, cache d'experts d'octobre (4) | 14,95 → 19,26, une mesure (commit d'un fork qui porte la PR fusionnée le 07/10) | M18, M19 |
| PC de 32 et 64 Go de RAM (4) | 31 Go (3060) ; 62 Go (5060 Ti) | M17, M19 |
| 4 000 → 64 000 tokens, 29 → 20 ; 64 → 39 avec MTP (5) | Qwen3.8-27B, 5060 Ti, 29,18 → 19,77 ; 63,89 → 39,06 | M22 (= M5) |
| « Le MTP double toujours » (5) | ×1,98 à 64K | M5 |
| 45 → moins de 10 à 128 000, même fichier de 11,5 Go (5) | RTX 4080, 45,3 → 9,6 ; le cache du contexte pousse le modèle hors de la carte | M23 |
| Deux gestes : nouvelle conversation, taille réglée au plus juste (5) | Conseils tirés de M22 et M23 | CALCUL |
| Petit modèle de 7 milliards ; 8 bits −6,6 %, 4 bits −1,8 % (6) | RTX 5060 Ti, Qwen2.5-Coder-7B, 81,8 · 76,4 · 80,3 | M26 |
| 4 bits, −35 % à 64 000 tokens (6) | DGX Spark, f16 → q4_0 | M27 |
| 32 000 → plus de 128 000 tokens (6) | La place gagnée | M28 |
| Plus de conversation dans la carte avant que le modèle soit poussé dehors ; « peut t'éviter la falaise » (6) | Déduction de M23 et M28 ; rien n'est mesuré sur la 4080 (on ne sait pas si son banc avait déjà le cache compressé) | M23, M28, CALCUL |
| Le testeur du début avait déjà le cache compressé (6) | KV q4_0 | M5 |
| Ressemblance 82 % (8 bits), 8 % (4 bits) (6) | Similarité de sortie avec f16 (81,6 % ; 8,3 %) | M26 |
| Au moins 3 des 6 testeurs en 4 bits (6) | KV q4_0 chez M1, M4, M5 (non précisé pour M2, M3, M6) | M1, M4, M5 |
| Repères de la checklist (7) | Ceux des sections 1 à 6 | voir plus haut |

**Ce que la voix ne dit pas** (§ G de `sources.md`) : aucun « ×4 » ni « ×10 » comme promesse, aucun nom de chaîne ni de pseudo, aucun chiffre de vitesse, de RAM ou de disque de la vidéo Strata, aucun avant/après chez toi, aucun réglage par défaut ni emplacement du MTP dans LM Studio, aucune baisse chiffrée du contexte pour les modèles à experts, aucun numéro du moteur embarqué de LM Studio, aucun « ×3 » pour le code (M3 donne ×2,78 : § H interdit d'aller au-delà de 2), aucun « tout le monde conseille ».

## Questions pour toi (hors voix)

1. Section 1 : si tu vérifies dans LM Studio 0.4.28 où s'allume le MTP et s'il est allumé par défaut, tu peux remplacer « personne n'a vérifié s'il l'allume tout seul » par ce que tu vois (la doc officielle n'en dit rien dans `sources.md`, M30b).
2. Fin : « tient en entier » est tenu par `../qwen-27b-8go/sources.md` F1-F2 (une seule mesure, d'après `grill-v3.md`).
3. Versions « du 15 novembre » : relis M33-M36 le 19 au matin si tu veux.
