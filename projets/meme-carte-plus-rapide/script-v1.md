# Même carte, 2 fois plus rapide : script (V1, 15/11/2026)

**Sortie** : jeu. 19/11/2026, 18 h. **Vidéo calculée** (décision du 15/11) : aucun nouveau test, aucune vitesse à toi sauf le renvoi à Strata (section F de `sources.md`), qui n'est **jamais un avant/après**. Faits : [`sources.md`](sources.md) (M1…M38, F). Miniature : [`miniature/propositions.md`](miniature/propositions.md) (« TA CARTE BRIDÉE ? », compteur à « 2× »).

| | |
|---|---|
| **Titre visé** | **« 16 Go de VRAM : le réglage qui fait écrire 2 fois plus vite, et celui qui ne sert à rien »** (titre 3 de `sources.md` § H : MTP M1-M6 ; cache KV M26-M27). Il annonce la checklist et le retournement de la fin, ce que la vidéo concurrente française n'a pas. Repli : titre 2, « Ton IA locale peut écrire 2 fois plus vite, sans changer de carte ». |
| **Durée estimée** | ≈ 9 min 32 s (1 383 mots ÷ 145) ; avec les respirations et les plans muets, 9 min 30 à 10 min. Hook : 69 mots, la question tombe vers 0:28 |
| **Mots de voix** | 1 383, comptés par script (titres, `[VISUEL]`, `[CROCHET]`, identifiants et tableaux exclus) |
| **Liaisons pour 100 mots** | **1,59** (22 : « donc » 6, « du coup » 5, « en fait » 4, « sauf que » 4, « voilà » 2, « en effet » 1) ; 2,60 en comptant aussi « par contre », « parce que », « alors », « justement », « en gros », « bref » (14) |

## Ce que la vidéo dit (texte et sous-texte)

- **Texte** : sur une carte de 16 Go, un seul réglage, le MTP, fait écrire un modèle de 27 milliards jusqu'à 2 fois plus vite ; six testeurs l'ont mesuré. Voilà les réglages, du plus rentable au plus inutile, chacun avec sa mesure.
- **Sous-texte** : ta carte n'est pas trop petite, elle est mal réglée ; avant d'acheter, règle. Et méfie-toi des « ×10 » : un chiffre ne vaut que par ses conditions.
- **Ce qui nous distingue de la vidéo française du 14/11** (M38) : pas de récit de trois mois sur une machine ; une checklist où chaque gain a sa mesure, la lecture du prompt séparée de l'écriture, et le réglage « qui ne sert à rien pour la vitesse ».

## Structure

| Temps (≈) | Partie | Ce qui s'y passe | Relance qui la ferme |
|---|---|---|---|
| 0:00-0:30 | 0. Hook | Le compteur 26 → 59 sur une 5060 Ti ; six testeurs ; la question « bridée ? » | — |
| 0:30-1:05 | 0 bis. Conditions et plan | Écriture, modèle qui tient, code ; lecture du prompt ; le plan en 4 livrables + le retournement | « Le réglage qui double, c'est… » |
| 1:05-2:50 | 1. Le MTP | La réponse tout de suite, les mesures, code contre texte, à experts, « bridée » | « Sauf que le MTP a un prix » |
| 2:50-4:20 | 2. Le fichier qui tient | La place du MTP, le fichier qui déborde, la falaise, les gains qui ne s'additionnent pas ; **abonne-toi** | « Et ensuite, le moteur » |
| 4:20-5:45 | 3. Le moteur et sa version | Ollama, LM Studio, le « ×10 » d'un autre, la mise à jour qui ralentit, les versions du jour | « Et si ton modèle déborde quand même ? » |
| 5:45-6:35 | 4. Les experts | Renvoi à Strata ; où vont les experts ; une mesure chacune | — |
| 6:35-7:30 | 5. Le piège du contexte | Un tiers de vitesse en moins à 64 000 tokens | « Et c'est là qu'arrive le réglage que tout le monde conseille » |
| 7:30-8:40 | 6. Le réglage qui ne sert à rien | Le cache KV compressé : pas de vitesse, de la place ; 8 bits, pas 4 | — |
| 8:40-9:20 | 7. La liste et la suite | La checklist dans l'ordre ; écran de fin vers 32 Go | — |

Timecodes estimés à 145 mots/min, à recaler sur la voix montée.

**Boucles ouvertes** : « ta carte est-elle bridée ? » (0:25 → fin de la section 1) ; « le réglage que tout le monde conseille et qui ne sert à rien » (plan → section 6) ; « deux réglages à 10-30 % » (plan → sections 3 et 4) ; « le prix du MTP » (fin de 1 → 2) ; « un tiers de ta vitesse » (plan → section 5).

**Conventions** : texte normal = voix. `[VISUEL : …]` = plan. `[CROCHET : …]` = à dire par toi, avec tes mots (avis, réaction) : rien n'y est inventé. `[M…]` et `[F]` = identifiant de `sources.md`, **ne se lit pas** (à retirer au téléprompteur). Nombres en chiffres, pour l'audit. **Aucun nom de chaîne, de créateur ni de pseudo** dans la voix. Les chiffres de la vidéo Strata (près de 70, la RAM, le disque) ne sont **jamais** un « avant ».

---

## 0. Hook (0:00 – 0:30)

[VISUEL : plein écran, le compteur de la miniature (aiguille, zone rouge). Bandeau en bas, permanent : « Mesure publiée · RTX 5060 Ti 16 Go · Qwen3.8-27B · même fichier · seul le MTP change ». L'aiguille se pose sur 26,3, un clic d'interrupteur, elle file à 59,5 et « 2× » s'allume. Pas de titre, pas de logo.]
Une 5060 Ti de 16 gigas. Même modèle, même fichier : 26 tokens par seconde [M2]. On allume un seul réglage… 59 [M2]. Plus du double, sur la même carte, sans rien acheter.

[VISUEL : les six cartes qui tombent l'une après l'autre en vignettes (5080, 5060 Ti, 4060 Ti, RX 9060 XT, 5060 Ti, 3080 Ti portable), chacune avec son « ×1,9 » à « ×2,3 » ; puis « TA CARTE BRIDÉE ? » en gros, le texte de la miniature.]
Et 6 testeurs, sur 5 cartes de 16 gigas, trouvent entre 1,9 et 2,3 fois plus vite [M1-M6]. Du coup : est-ce que ta carte est bridée, sans que tu le saches ?

---

## 0 bis. Les conditions et le plan (0:30 – 1:05)

[VISUEL : trois cases qui se cochent : « ÉCRITURE », « LE MODÈLE TIENT DANS LA CARTE », « SURTOUT DU CODE » ; puis une quatrième, barrée en rouge : « LECTURE DU PROMPT ».]
Par contre, cette fois, je n'ai rien mesuré chez moi : ce sont leurs chiffres, et ils ont des conditions. C'est la vitesse d'écriture, sur Qwen 3.8 27B, un modèle qui tient en entier dans la carte, et ça gagne surtout sur du code [M3]. La lecture de ton prompt, elle, ralentissait dans les premiers tests de mai [M7].

[VISUEL : le plan en 4 lignes qui s'écrivent avec la voix ; la 5e ligne arrive en rouge : « LE RÉGLAGE QUI NE SERT À RIEN ».]
Je vais te montrer le réglage qui double, celui à régler avant lui, deux réglages qui rapportent de 10 à 30 % [M17, M19, M29, M30], et le piège qui te vole un tiers de ta vitesse [M22]. Et à la fin, le réglage que tout le monde conseille, alors qu'il ne sert à rien pour la vitesse.

---

## 1. Le réglage qui double : le MTP (1:05 – 2:50)

[VISUEL : animation simple sur fond sombre : le modèle pose 3 tokens fantômes d'avance, une coche verte les valide d'un coup ; un fantôme faux devient rouge et disparaît.]
Le réglage qui double, c'est le MTP. En fait, le modèle devine plusieurs tokens d'avance, puis il les vérifie tous d'un coup. Quand il a deviné juste, tu as écrit plusieurs tokens pour le prix d'un.

[VISUEL : le tableau des mesures, ligne par ligne, une carte à la fois, « sans MTP → avec MTP » en gros (M1, M3, M4) ; une capture du tableau du dépôt public, noms floutés.]
Et ça se voit sur les cinq modèles de cartes. Chez un testeur, sur une 5080, on passe de 53 à 101 tokens par seconde [M1]. Sur une 4060 Ti, de 17,6 à 40 [M3]. Même sur une Radeon, la RX 9060 XT, de 15 à presque 29 [M4].
Sauf que 5 de ces 6 mesures viennent du même tableau, avec le même script de test [M1-M6]. Du coup, la plus solide, c'est la sixième : un testeur à part, sur une 5060 Ti, passe de 29 à 64 [M5]. Il trouve pareil.

[VISUEL : deux barres côte à côte sur la 4060 Ti : « TEXTE ×1,8 » et « CODE » plus haute, sans chiffre ; puis une icône de modèle à experts avec « ×1,5 ».]
En fait, ce « 2 fois » est une moyenne sur du code, du texte et des commandes, avec la réflexion coupée [M1-M6]. Sur du texte seul, c'est moins : 1,8 fois sur la 4060 Ti [M3]. C'est sur du code que ça gagne le plus [M3]. Et sur les gros modèles à experts, ça rapporte moins : un testeur mesure 1,5 fois [M10, M11].

[VISUEL : un terminal, la commande llama.cpp avec `--spec-type draft-mtp` surligné ; puis deux noms de fichiers côte à côte, celui avec « -mtp » surligné (S38 de M8) ; puis la page des nouveautés de LM Studio 0.4.22, « MTP » surligné (M30b).]
Alors, pourquoi je dis « bridée » ? Parce que dans llama.cpp, le MTP ne s'allume pas tout seul : il faut le demander, et il faut un fichier qui contient les têtes MTP, un petit bout de modèle en plus [M8]. LM Studio, lui, le gère depuis la version 0.4.22 [M30b].
[CROCHET : vérifie dans LM Studio 0.4.28 (M35) où s'allume le MTP et s'il est allumé par défaut, puis dis-le avec tes mots. Si tu ne vérifies pas, garde seulement la phrase qui suit.]
Donc va vérifier qu'il est bien allumé chez toi.

---

## 2. Celui à régler avant lui : le fichier qui tient (2:50 – 4:20)

[VISUEL : une jauge de VRAM de 16 Go qui se remplit : le modèle, puis un bloc « MTP » qui s'ajoute et touche le bord rouge.]
Sauf que le MTP a un prix : il prend de la place. Selon les testeurs, entre 1 et 2,5 gigas de VRAM en plus [M9]. Et sur une carte de 16, c'est justement là que ça coince [M9].

[VISUEL : la page du banc de la 4080 (M12), les deux lignes surlignées : « IQ4_XS 15,0 Go · 20,5 » et « UD-IQ3_XXS 11,5 Go · 45,3 », étiquette « Qwen3.5-27B » ; une flèche vers le haut.]
Parce que le vrai réglage numéro un, c'est que le modèle tienne en entier dans la carte. Sur une 4080 de 16 gigas, avec un modèle de 27 milliards : un fichier de 15 gigas qui déborde un peu, 20 tokens par seconde. Un fichier de 11,5 gigas qui tient, 45 [M12]. Donc plus du double, juste en prenant un fichier plus petit.

[VISUEL : une courbe en falaise : « toutes les couches sur la carte · 43 » puis « 8 couches dehors · 12,5 », étiquette « Qwen2.5-Coder-14B, débordement forcé » (M13).]
Et si une partie du modèle sort de la carte, c'est la chute. Sur une 5060 Ti, un testeur a fait exprès de laisser dehors 8 couches sur 48 d'un modèle plus petit : on tombe de 43 à 12,5 [M13]. En fait, ce qui sort de la carte est calculé beaucoup plus lentement, et tout le reste attend.

[VISUEL : la miniature de la vidéo du 09/11 (« 16 Go de VRAM suffisent »), 2 s ; puis une étiquette « QUALITÉ PERDUE : NON MESURÉE ».]
C'est ce que je te disais dans la vidéo sur les 16 gigas de VRAM : prends le bon fichier. Par contre, un fichier plus petit est plus compressé, et aucune de ces pages ne mesure ce que tu perds en qualité [M12].

[VISUEL : deux blocs « MTP » et « FICHIER QUI TIENT » qui ne s'empilent pas ; un panneau « NE S'ADDITIONNENT PAS ».]
Et attention, ces gains ne s'additionnent pas. Si le MTP fait déborder ton fichier, tu perds d'un côté ce que tu gagnes de l'autre [M9, CALCUL]. Du coup, d'abord un fichier qui tient avec la place du MTP, ensuite le MTP.

[VISUEL : retour au compteur du hook, l'aiguille à « 2× » ; ton visage ou la caméra si tu en filmes une.]
Bon, voilà déjà de quoi faire écrire ta carte actuelle jusqu'à 2 fois plus vite [M1-M6]. Donc avant d'en racheter une plus grosse, essaie ça. Si cette vidéo t'a évité un mauvais achat, abonne-toi.
[CROCHET : une phrase à toi, si tu veux : ton avis sur ces deux premiers réglages, ou celui que tu essaierais en premier.]

---

## 3. Le moteur, et sa version (4:20 – 5:45)

[VISUEL : trois barres « llama.cpp 77,0 · LM Studio 76,8 · Ollama 69,1 » sur une 5060 Ti (M29) ; puis la 3090 avec « −30 % » sur Ollama (M30).]
Ensuite, le moteur, le programme qui fait tourner le modèle. Quand tout tient dans la carte, Ollama a été mesuré 10 % plus lent que llama.cpp sur une 5060 Ti [M29], et jusqu'à 30 % plus lent sur une 3090 [M30]. LM Studio, lui, est presque pareil que llama.cpp : 76,8 contre 77 [M29]. Et du coup, si tu l'as installé avec ma vidéo sur LM Studio, tu es déjà du bon côté.

[VISUEL : un « ×10 » énorme qui se fissure ; dessous, trois étiquettes : « 1 MACHINE », « RTX 50 + LINUX », « VERSIONS ? RÉGLAGES ? ». Aucun nom, aucune capture de la vidéo.]
Et justement, un créateur français vient de passer de 8 à 83 tokens par seconde sur une 5060 Ti, surtout en changeant de moteur [M38]. Sauf que son moteur ne marche que sur les cartes RTX 50, sous Linux, et il ne donne ni ses versions ni ses réglages [M38]. En gros, c'est le résultat d'une machine, pas une promesse pour la tienne.

[VISUEL : les deux tickets de Strata (M31), « 117,0 » contre « 86,1 » surlignés ; puis la page de la 0.2.14 (M32), « chat 17,5 (19,4) » surligné.]
Et même une mise à jour peut te ralentir. Sur une 5080 avec Strata, un utilisateur a perdu 25 % en passant d'une version du moteur à l'autre [M31]. Et la version 0.2.14, sortie le 15 novembre, lit le prompt plus vite, mais écrit environ 10 % moins vite sur une 5070 Ti, d'après le projet lui-même [M32]. Donc, comme je te disais lundi, note bien ta version.

[VISUEL : une carte texte « Versions du 15/11/2026 : llama.cpp v1.0.0 · LM Studio 0.4.28 · Ollama 0.40.16 · Strata 0.2.14 » (M33-M36).]
Pour info, au 15 novembre, on en est à llama.cpp 1.0, LM Studio 0.4.28 et Ollama 0.40.16 [M33-M35].

---

## 4. Et si le modèle déborde quand même : les experts (5:45 – 6:35)

[VISUEL : la capture du moniteur de Strata de lundi (MON3), sans s'attarder sur les chiffres ; la miniature de la vidéo Strata (2 s).]
Et si ton modèle est trop gros pour la carte, comme le modèle à experts de lundi ? Lundi, avec Strata, j'ai mesuré près de 70 tokens par seconde [F], et tu as vu ma RAM se remplir et le disque se mettre à lire [F]. Là, le réglage, c'est où vont les experts : lesquels restent sur la carte, et lesquels partent en RAM. Et attention, les chiffres qui suivent ne sont pas les miens, et ils viennent de llama.cpp, pas de Strata.

[VISUEL : trois vignettes « 3060 12 Go +12 % » (M17), « 5060 Ti 16 Go +29 % » (M19), « 3090 24 Go +34 % » (M17), avec un tampon « 1 MESURE ».]
Dans llama.cpp, sur une 3060 de 12 gigas, bien régler les experts a fait gagner 12 % [M17]. Sur une 5060 Ti de 16, avec le nouveau cache d'experts de llama.cpp, 29 % [M19]. Et sur une 3090 de 24, 34 % [M17]. Par contre, c'est une seule mesure chacune : à prendre avec des pincettes.

---

## 5. Le piège qui te vole un tiers de ta vitesse : le contexte (6:35 – 7:30)

[VISUEL : une conversation qui s'allonge à l'écran, le compteur qui descend : « 4 000 tokens · 29 » → « 32 000 · 24 » → « 64 000 · 20 » (M22).]
Maintenant, le piège. Plus ta conversation est longue, plus ça ralentit. Sur le même modèle de 27 milliards et une 5060 Ti, passer de 4 000 à 64 000 tokens de conversation fait tomber l'écriture de 29 à 20 tokens par seconde [M22]. Donc un tiers de vitesse en moins [M22]. C'est ce que je te disais lundi : la vitesse baisse quand la conversation grandit.

[VISUEL : sur la 4080 (M23), la courbe « 45 » → « moins de 10 », avec la mémoire de la conversation qui déborde de la carte.]
Et ça peut être bien pire. En effet, la mémoire de la conversation prend de la place dans la carte. Quand elle pousse le modèle dehors, on retombe dans la falaise de tout à l'heure : sur une 4080, de 45 à moins de 10 tokens par seconde, à 128 000 tokens [M23].
Bref, la solution est toute bête : une nouvelle conversation dès que tu changes de sujet.

---

## 6. Le réglage qui ne sert à rien pour la vitesse : le cache KV compressé (7:30 – 8:40)

[VISUEL : un tutoriel générique « Astuce : compresse ton cache KV ! » avec un éclair ; on le tamponne « VITESSE : NON ».]
Et c'est là qu'arrive le réglage que tout le monde conseille : compresser le cache KV, c'est-à-dire la mémoire de la conversation. Sauf que pour la vitesse, ça ne sert à rien.

[VISUEL : trois barres sur une 5060 Ti : « normal 81,8 · 8 bits 76,4 · 4 bits 80,3 » (M26) ; puis « −35 % à 64 000 tokens » (M27), étiqueté « machine Nvidia pour l'IA, pas une carte de joueur ».]
Sur une 5060 Ti, en 8 bits, l'écriture est 6,6 % plus lente. En 4 bits, 1,8 % plus lente [M26]. Et sur une machine de Nvidia faite pour l'IA, à 64 000 tokens, l'écriture perd même 35 % [M27].

[VISUEL : la jauge de conversation qui s'étire : « 32 000 » → « 128 000+ » (M28).]
Alors pourquoi tout le monde le conseille ? Parce qu'en fait, il donne de la place. Un testeur passe de 32 000 à plus de 128 000 tokens de conversation, sur la même carte [M28]. Et voilà le retournement : il ne va pas plus vite, mais il fait tenir la conversation dans la carte, et c'est ça qui t'évite le piège de tout à l'heure.

[VISUEL : deux jauges de ressemblance avec l'original : « 8 bits · 82 % » en vert, « 4 bits · 8 % » en rouge (M26).]
Par contre, attention au 4 bits. Dans un test de ressemblance avec la réponse d'origine, le 8 bits garde 82 %, le 4 bits seulement 8 % [M26]. Du coup, si tu compresses, reste en 8 bits.
[CROCHET : ta réaction à ce retournement, avec tes mots (sans inventer d'expérience : tu ne l'as pas testé).]

---

## 7. La liste, et la suite (8:40 – 9:20)

[VISUEL : la checklist qui s'écrit, une ligne par phrase, chaque ligne avec son repère : « FICHIER QUI TIENT · ≥ ×2 » · « MTP · jusqu'à ×2, code » · « llama.cpp / LM Studio · Ollama −10 à −30 % » · « EXPERTS · +10 à 30 %, 1 mesure » · « CONVERSATION NEUVE · −1/3 à 64K » · « CACHE 8 BITS · place, pas vitesse » · « NOTE TA VERSION ».]
Donc, dans l'ordre : un fichier qui tient dans ta carte, avec la place du MTP. Le MTP allumé, surtout pour du code. Llama.cpp ou LM Studio, plutôt qu'Ollama. Si ton modèle déborde, règle où vont les experts. Une conversation neuve quand elle s'allonge. Le cache en 8 bits si tu manques de place, pas pour la vitesse. Et note ta version.
[CROCHET : ton verdict en une ou deux phrases : ce que tu retiens, ou ce que tu vas régler toi-même.]

[VISUEL : écran de fin, carte vers « 32 Go de VRAM pour Qwen 27B, au moins cher » (lun. 23/11).]
Et si 16 gigas ne te suffisent plus, lundi prochain, on cherche 32 gigas de VRAM au moins cher. Allez, salut !

---

## Chiffre → source

| Chiffre dit (section) | Ce que c'est | Source |
|---|---|---|
| 26 → 59 tok/s (0) | RTX 5060 Ti 16 Go, Qwen3.8-27B, sans → avec MTP, écriture | M2 |
| 6 testeurs, 5 modèles de cartes, ×1,9 à ×2,3 (0) ; « jusqu'à 2 fois » (2) | Six mesures du MTP sur 16 Go | M1-M6 |
| « surtout sur du code » (0 bis, 1) | Le code gagne le plus (4060 Ti) | M3 |
| La lecture du prompt ralentissait en mai (0 bis) | P ×0,51 et ×0,60, deux machines à deux cartes, Qwen3.6 ; aucun chiffre dit | M7 |
| 10 à 30 % (0 bis) | Experts +12 à +34 % ; Ollama −10 à −30 % | M17, M19, M29, M30 |
| Un tiers de ta vitesse (0 bis, 5) | −32 % de 4K à 64K | M22 |
| 53 → 101 (1) | RTX 5080, MTP | M1 |
| 17,6 → 40 (1) | RTX 4060 Ti, MTP | M3 |
| 15 → presque 29 (1) | RX 9060 XT, 15,2 → 28,7 | M4 |
| 5 des 6 mesures du même tableau (1) | Même dépôt, même `probe.py` | M1-M6 (conclusion de § A) |
| 29 → 64 (1) | RTX 5060 Ti, testeur indépendant, 29,18 → 63,89 à 4K | M5 |
| Moyenne code + texte + commandes, réflexion coupée (1) | Conditions du ×2 | M1-M6 (conditions de § A) |
| ×1,8 sur du texte (1) | 4060 Ti, 17,6 → 32,3 | M3 |
| ×1,5 sur un modèle à experts (1) | MoE 35B-A3B, 98 → 144 (×1,47) | M10, M11 |
| MTP non automatique, fichier avec têtes MTP (1) | `--spec-type draft-mtp` ; fichier « -mtp » | M8 (et § H) |
| LM Studio 0.4.22 (1) | Support du MTP, 28/08/2026 | M30b |
| LM Studio 0.4.28 (crochet de 1, 3) | Version du jour | M35 |
| 1 à 2,5 Go de VRAM en plus (2) | +1,16 ; +1,58 ; +2,49 Gio | M9 |
| 15 Go qui déborde, 20 tok/s → 11,5 Go qui tient, 45 (2) | RTX 4080 16 Go, Qwen3.5-27B, 20,5 → 45,3 | M12 |
| 8 couches sur 48 dehors, 43 → 12,5 (2) | RTX 5060 Ti, Qwen2.5-Coder-14B, `-ngl 40` | M13 |
| Qualité perdue non mesurée (2) | Aucune page ne la mesure | M12 (conclusion de § B) |
| Les gains ne s'additionnent pas (2) | Déduction : le MTP prend de la VRAM | M9, CALCUL |
| Ollama −10 % (3) | 77,0 contre 69,1, RTX 5060 Ti | M29 |
| Ollama jusqu'à −30 % (3) | RTX 3090, ×1,41 en faveur de llama.cpp | M30 |
| LM Studio 76,8 contre 77 (3) | RTX 5060 Ti | M29 |
| 8 → 83 tok/s, RTX 50 et Linux, ni versions ni réglages (3) | Vidéo française du 14/11 (7,9 → 83), anonyme dans la voix | M38 |
| −25 % après une mise à jour (3) | Strata, RTX 5080, moteur 0.1.54 → 0.1.56 | M31 |
| 0.2.14 du 15/11, écriture −10 % sur 5070 Ti (3) | Chiffres du projet | M32 |
| llama.cpp 1.0, LM Studio 0.4.28, Ollama 0.40.16 (3) ; Strata 0.2.14 (visuel) | Versions du 15/11 | M33, M35, M34, M36 |
| Près de 70 tok/s, RAM qui se remplit, disque qui lit (4) | Renvoi à la vidéo Strata, **pas un avant** ; aucun chiffre de RAM ni de disque redit | F (T45, srt 3:14-3:18, 4:36-4:51) |
| +12 % sur 3060 12 Go (4) | `--n-cpu-moe` ajusté | M17 |
| +29 % sur 5060 Ti 16 Go (4) | Cache d'experts, 14,95 → 19,26, une mesure | M19 |
| +34 % sur 3090 24 Go (4) | `--n-cpu-moe` ajusté | M17 |
| 4 000 → 64 000 tokens, 29 → 20 (5) | Qwen3.8-27B, 5060 Ti, sans MTP, 29,18 → 19,77 | M22 |
| 45 → moins de 10 à 128 000 (5) | RTX 4080, 45,3 → 9,6 | M23 |
| 8 bits −6,6 %, 4 bits −1,8 % (6) | RTX 5060 Ti, 81,8 · 76,4 · 80,3 | M26 |
| −35 % à 64 000 tokens (6) | DGX Spark, f16 → q4_0 | M27 |
| 32 000 → plus de 128 000 tokens (6) | La place gagnée | M28 |
| Ressemblance 82 % (8 bits), 8 % (4 bits) (6) | Similarité de sortie avec f16 | M26 |

**Ce que la voix ne dit pas** (§ G de `sources.md`) : aucun « ×4 » ni « ×10 » comme promesse, aucun nom de chaîne ni de pseudo, aucun chiffre de RAM ou de disque de la vidéo Strata, aucun avant/après chez toi, aucun réglage par défaut de LM Studio, aucune baisse chiffrée du contexte pour les modèles à experts, aucun numéro du moteur embarqué de LM Studio.
