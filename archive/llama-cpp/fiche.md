# Le dev qui a mis un ChatGPT dans ton PC

> Analyse (hook, pourquoi, score) : [`strategie.md`](../../strategie.md), idée 9. Planning : [`calendrier.md`](../../calendrier.md), **lun. 8 févr. 2027 à 18 h, provisoire** (avancé du 8 mars le 23/10 : le hook n'est donc plus « les 4 ans »). Sources : [`sources.md`](sources.md). Fiche créée le 23/10/2026 (phase 1).

| Champ | Détail |
|---|---|
| **Pilier** | Les grandes histoires de la tech (Hero), avec un pied dans « IA chez moi » |
| **Format** | Longue, 15-18 min |
| **Trafic visé** | Accueil (+ suggestions à côté des vidéos Ollama / LM Studio) |
| **Mot-clé** | ollama (335 K/mois dans le monde, 9,8 K en France) / llama.cpp (21 K/mois) / ia en local (21,4 K, +91 %), vidIQ 23/10/2026 |
| **Type de hook** | Récit (un soir de mars 2023) |
| **Production estimée** | ~35 h (estimation : récit, motion design de code et de mémoire, pas d'essai ; un test sur la RTX 5080 en option) |

**Titres** :
1. Recherche : *L'histoire de llama.cpp*
2. Curiosité : *Il a codé ça en une soirée. Maintenant l'IA tourne sur ton PC.*
3. Mixte (recommandé) : *Le dev qui a mis un ChatGPT dans ton PC*

**Texte et sous-texte** (le « problème de surface / problème profond » du skill grill) :
- **Texte** : l'histoire de llama.cpp. Un développeur seul publie le 10 mars 2023 un petit programme pour faire tourner le modèle LLaMA de Meta sur un MacBook ; en trois ans il devient la brique sur laquelle reposent Ollama, LM Studio et la plupart des IA qu'on fait tourner chez soi.
- **Sous-texte** : une IA qui tourne chez toi et non chez eux, ça tient à un projet qu'un seul homme a commencé en une soirée. Ce que tu appelles « IA chez moi » a une histoire et un auteur (à confirmer avec toi : lecture de ton titre « le dev qui a mis un ChatGPT dans ton PC »).
- **Garde-fou factuel** : llama.cpp faisait tourner LLaMA (Meta), pas ChatGPT. « Un ChatGPT » garde l'idée, sans l'erreur : à dire dans la vidéo (ça fait une scène).

**Les 15 premières secondes** : le hook de `strategie.md` (« Mars 2023. Un développeur bulgare publie un petit programme… ») ne tient plus tel quel : *bulgare* repose sur la localisation de son profil GitHub (Sofia), pas sur une nationalité. Piste : afficher le premier README (« This was hacked in an evening - I have no idea if it works correctly »), puis le chiffre d'aujourd'hui (plus de 132 000 étoiles sur GitHub le 23/10/2026). Question avant 30 s : comment un projet fait « en une soirée » est devenu la base de l'IA locale ?

**Contenu** (ordre proposé, faits dans `sources.md`) :
1. Mars 2023 : l'IA ne vit que dans les data centers. Meta annonce LLaMA (24/02/2023), réservé aux chercheurs ; les poids fuitent le 03/03/2023.
2. Le 10 mars 2023 à 18 h 40 (UTC), Georgi Gerganov publie « Initial release » : LLaMA en C/C++ sans dépendances, quantification en 4 bits, MacBook en priorité. Le README : « hacked in an evening ».
3. Pourquoi ça marche : la quantification (rapport de taille entre un modèle de 7 milliards de paramètres en 16 bits et en 4 bits : à calculer en phase 2), ggml, la bibliothèque qu'il écrit depuis septembre 2022 pour whisper.cpp.
4. Les démos qui font le tour du monde : MacBook, Raspberry Pi 4 (Artem Andreenko, 12/03/2023, environ 10 secondes par jeton), téléphone. Ce moment-là, c'est la vidéo : montre l'écran lent et pourtant vivant.
5. Le moment où ça devient « utilisable » : la PR de Justine Tunney du 30/03/2023 (chargement des poids 10 à 100 fois plus rapide), puis GGUF (21/08/2023) et ggml.ai (financé par Nat Friedman et Daniel Gross).
6. L'écosystème : Ollama (juin 2023) et LM Studio construits dessus, llama-server, le format GGUF sur Hugging Face.
7. Aujourd'hui : le 20/02/2026, ggml.ai rejoint Hugging Face (le projet reste MIT et ouvert) ; le 03/09/2026, Nvidia annonce racheter Hugging Face pour 12,9 Md$ (clôture non confirmée). Que devient le projet d'un seul homme ? Retour au sous-texte : ton PC fait tourner l'IA parce que quelqu'un l'a voulu, et ça pourrait changer.

**Miniature** : à faire. Ton idée du 21/10 (silhouette devant un écran de code, cerveau d'IA qui sort d'un PC, « IL A TOUT CHANGÉ ») est à comparer avec les miniatures des vidéos hôtes (Codacus, Devsplainers, The Stack) avant de dessiner. Charte : noire (histoire).

**À vérifier** (détail et sources dans `sources.md`) :
- nationalité de Georgi Gerganov (profil GitHub : Sofia, Bulgarie ; aucune source de nationalité lue) ;
- 10/03/2023 comme premier commit (✅ historique GitHub) ; l'heure, 18 h 40 UTC, vaut pour « Initial release » ;
- « hacked in an evening » : ✅ README original ;
- le chiffre de réduction de mémoire de la quantification (7B en 4 bits ≈ 4 Go selon une vidéo de seconde main, ❓) ;
- les soutiens de ggml.ai et leurs montants (le site ne donne que les noms) ;
- le rachat de Hugging Face par Nvidia : annonce confirmée par la presse, pas de communiqué de Nvidia lu, clôture attendue ❓ ;
- « un ChatGPT » : à expliquer, pas à cacher.

## Corrections de la 2e vérification (23/10)

Le titre tient (« un ChatGPT » reste une image, à expliquer). À changer dans le contenu :
- **Point 4** : « téléphone » n'est pas sourcé (aucune démo d'origine trouvée, fait 11 de `sources.md`). Garde le MacBook et le Raspberry Pi 4.
- **Point 5** : la PR de Justine Tunney *promet* « 10 à 100 fois plus rapide » dans son titre ; ce n'est pas une mesure (fait 12).
- **Point 3** : le chiffre est trouvé dans le README d'avril 2023 : 7B passe de 13 Go à 3,9 Go en 4 bits (fait 22).
- **Point 7** : le rachat de Hugging Face est un accord annoncé par Nvidia (billet de Jensen Huang, 03/09/2026), pas un rachat conclu (fait 19). À relire le jour du tournage.
- **Les 15 premières secondes** : « bulgare » reste interdit ; « un développeur de Sofia » est sûr (fait 1).
