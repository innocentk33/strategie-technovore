# Qwen 27B sur une carte de 8 Go : 5 fois plus vite avec un seul fichier

> **Cadrage confirmé après recherche : vidéo entièrement calculée, comme la référence SimplyExplain. Aucun essai, téléchargement de modèle ou capture LM Studio à fournir par l’auteur. Les mesures sont publiées par des tiers ; les visuels sont des sources, graphiques et schémas. Le titre actif est celui de `script.md`, sans ×5 généralisé. Les hypothèses et chiffres ci-dessous sont le brief historique ; `sources.md` fait foi après vérification.**
>
> Fiche du 16/11/2026, à ta demande. Placée au **lun. 23 nov., 18 h**, à la place de [32 Go de VRAM](../deux-cartes-occasion/fiche.md), qui recule au lun. 30 nov. Idée 35 de [`strategie.md`](../../strategie.md), non notée (ta demande). Vidéo **calculée**, sans essai de l’auteur (clarification confirmée). Titre provisoire.
>
> ⚠️ **Rien n'est encore vérifié.** Tous les chiffres de cette fiche viennent des deux vidéos d'inspiration (transcriptions et description YouTube, relevées le 16/11). La recherche et la double vérification restent à faire : `sources.md` à créer.

**Inspirations** (transcrites dans `etudes/transcriptions/`) :
- SimplyExplain, [*Your 8GB GPU Runs Qwen 3.8 27B 5x Faster Now (One New File)*](https://www.youtube.com/watch?v=u_DYZhTZ2IM), 7 min 45 s, publiée le 13/11 : **8 748 vues en 3 jours, avec 2 070 abonnés** (page YouTube, 16/11). [Transcription](../../etudes/transcriptions/simplyexplain-u_DYZhTZ2IM.md).
- Red Stapler, [*I ran Qwen3.8 27B on single 8GB Card! (Better than expected)*](https://www.youtube.com/watch?v=ye50BbXEczo), 5 min 14 s, publiée le 24/08 : **788 287 vues, avec 180 K abonnés** (page YouTube, 16/11 ; 588 K au relevé de `strategie.md`). [Transcription](../../etudes/transcriptions/redstapler-ye50BbXEczo.md).
- **Leur angle (à ne pas reprendre)** : Red Stapler filme son essai (4 à 6 tok/s, 1 h 30 à 2 h 30 par page, comparaison avec Opus). SimplyExplain fait le mode d'emploi de llama.cpp, ligne de commande à l'appui.
- **Notre angle** : l'avant/après raconté pour quelqu'un qui a **LM Studio** et une carte de joueur de 8 Go (une carte sur quatre chez les joueurs, d'après Steam : chiffre d'octobre noté dans [`radar.md`](../../etudes/radar.md), à relire à la source). Ce que tu gagnes (la vitesse), ce que tu paies (le contexte et la qualité en 2 bits), et pour quel usage ça vaut le coup. En français, avec le renvoi vers l'installation de LM Studio.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi |
| **Format** | Longue, 8-10 min. Calculée : mesures publiées, aucune vitesse à toi |
| **Trafic visé** | Suggestions sous Red Stapler et SimplyExplain, recherche (« qwen 8 go vram », « ia locale 8 go ») |
| **Type de hook** | Résultat chiffré : sur une carte bridée à 8 Go, le même modèle passe de 3 à 18 tokens par seconde en changeant un seul fichier |
| **Production** | 1 à 2 jours |

## Ce que disent les deux vidéos (à vérifier à la source)

- **Avant** : Qwen 3.8 27B sur 8 Go, c'était un fichier 4 bits (IQ4_XS, environ 14 Go) dont une partie reste en RAM. Red Stapler : 26 couches sur une RTX 4060, 4,2 à 5 tok/s en moyenne, 1 h 30 à 2 h 30 par page web. SimplyExplain : 3,2 tok/s avec 33 couches sur 65.
- **Le nouveau fichier** : Unsloth a envoyé le 11/11 un `UD-IQ2_XS` de **7,63 Go** (« Dynamic 3.1 »). C'est le premier fichier 2 bits jugé bon qui tient en entier dans 8 Go. Les anciens 2 bits faisaient environ 8,4 Go.
- **Après** : 18,0 tok/s conversation vide, 16,9 à 4 K, 15,3 à 13,8 K tokens (GTX 1080 Ti dont 3 Go sont bloqués, pour laisser 7 955 Mio libres ; llama.cpp ; 3 passes). D'où le « ×5 ». La lecture du prompt ne change pas (210 à 280 tok/s).
- **Le prix à payer, n° 1, le contexte** : environ 14 K tokens avec un cache KV en 8 bits, 22,5 K en 4 bits (11,6 tok/s une fois plein). Qwen 3.8 réfléchit beaucoup (environ 20 K tokens sur une page web) : il faut couper la réflexion ou la mettre au minimum. Chaque 100 Mo pris par le bureau coûte environ 3 000 tokens.
- **Le prix à payer, n° 2, la qualité** (chiffres d'Unsloth, pas indépendants) : environ 95 % du score du modèle complet sur LiveCodeBench, 94 à 97 % sur MMLU-Pro et les maths ; mais **moins de 13 % contre environ 40 %** sur DeepSWE (le travail d'agent sur un vrai dépôt). Donc : oui pour discuter, expliquer, écrire un fichier ; non pour un agent.
- **10 et 12 Go** : le nouveau `Q2_K_XL` (un peu moins de 10 Go) garde bien mieux le travail d'agent. Les `IQ3_XXS` et `IQ3_S` n'ont pas été refaits.
- **Le piège** : un contexte trop grand se charge, puis plante quand il se remplit (leur essai : 25,6 K en 4 bits, plantage vers 24 K).
- **À côté** : une équipe a fait compresser ce modèle dans 8 Go par Claude (CompressionBench, arXiv 2611.06858) ; le fichier n'est pas téléchargeable et il est environ 3 fois plus lent.

## À ne pas confondre avec

- [Même carte, 2 fois plus rapide](../meme-carte-plus-rapide/fiche.md) (19 nov.) : là, le modèle tient déjà dans 16 Go et on gagne avec un réglage (le MTP). Ici, le gain vient du fait que le modèle **rentre enfin** dans la carte. Sur 8 Go, le MTP ne tient pas (1,37 Go de plus) : dis-le, c'est le pont entre les deux vidéos.
- [16 Go de VRAM suffisent](../claude-ou-mon-pc-1/fiche.md) (publiée) : même idée (« le bon fichier »), un palier au-dessus.
- [Quel modèle ta carte peut faire tourner ? De 4 à 16 Go](../modele-par-vram/fiche.md) (18 janv.) : elle reprendra ce résultat en une ligne pour le palier 8 Go.

## Points à vérifier (avant le script)

1. **Le « ×5 » repose sur une seule mesure**, d'une chaîne de 2 K abonnés, sur une carte de 2017 bridée. Règle 3 du calculé : cherche une deuxième mesure sur une vraie carte de 8 Go (RTX 3070, 4060…). S'il n'y en a pas, le hook dit « une mesure publiée », et le titre ne promet pas « 5× » comme un fait général.
2. La taille du fichier (7,63 Go), sa date (11/11) et les tailles des autres, sur Hugging Face (`unsloth/Qwen3.8-27B-GGUF`).
3. Les scores d'Unsloth, sur leur page (`unsloth.ai/docs/models/qwen3.8`) : à présenter comme « leurs propres mesures ».
4. La part des cartes de 8 Go dans l'enquête Steam du dernier mois.
5. **Les réglages dans LM Studio** (ton public n'a pas llama.cpp) : couches sur la carte, taille du contexte, cache KV quantifié, réflexion coupée. À lire dans la doc de LM Studio.
6. **Tranché : calculé exclusivement.** Aucun bridage de carte, test ou avant/après à filmer par l’auteur. Pas de crochet de test à remplir.
7. Pas de nom de chaîne dans la voix (« un testeur », « une chaîne anglophone »). Les noms restent dans `sources.md`.
8. Modèle sorti après les connaissances des IA qui aident à écrire : rien de mémoire, tout à la source.

## Titres (provisoires)

1. *Ta carte de 8 Go fait tourner Qwen 27B 5 fois plus vite (un seul fichier à changer)*
2. *Qwen 27B sur 8 Go de VRAM : de 3 à 18 tokens par seconde, sans rien acheter*
3. *8 Go de VRAM, c'est fini ? Ce nouveau fichier dit le contraire*

Le « 5 fois » ne reste dans le titre que si le point 1 tient.

## Miniature

Style « à la manière de Kai » (h, i, j), voir [`plan-kai-31-12.md`](../../ressources/miniatures/plan-kai-31-12.md). Texte proposé : « 8 GO / 5× PLUS VITE ? ». Objet : la jauge de 8 Go et le fichier de 7,63 Go qui rentre juste. Visage : un meme connu, à choisir (Fry reste aux 32 Go).

## Les 15 premières secondes (brouillon, sous réserve du point 1)

> « Sur une carte de 8 gigas, ce modèle écrivait à 3 tokens par seconde. [IMAGE : le texte qui s'affiche lettre par lettre] Un testeur a changé un seul fichier, et il passe à 18. [IMAGE : le même texte, qui file] Même carte, même modèle. Sauf que ce fichier a un prix, et il ne se paie pas en euros. »

Puis, avant 30 s : la règle du calculé (« ces chiffres sont les siens, je n'ai rien testé chez moi »), et le plan en livrables : le fichier à télécharger, les réglages dans LM Studio, ce que tu perds en mémoire de conversation, et le seul usage où il vaut mieux garder l'ancien fichier.
