# Pourquoi avoir ta propre IA, et comment l'installer (LM Studio)

> Fiche du 24/10/2026, à ta demande : « d'abord une vidéo de vulgarisation très simple, où on installe un modèle local avec l'outil le plus simple possible », puis la nomenclature. **Créneau : lun. 2 nov. 2026, 18 h**, à la place d'[*IA en local : comment lire le nom d'un modèle*](../bases-ia-locale/fiche.md), qui passe au 7 déc. Ta règle : une progression douce (d'abord la base, ensuite les noms), et chaque vidéo renvoie aux anciennes. Analyse : [`strategie.md`](../../strategie.md), idée 25. Planning : [`calendrier.md`](../../calendrier.md). Faits : [`sources.md`](sources.md) (recherche et double vérification du 24/10 : 24 ✅, 15 ⚠️, 1 ❌ ; les formulations exactes sont dans sa dernière section). **Fiche corrigée le 24/10 avec la 2e vérification.**

**L'outil : LM Studio**, l'option la plus simple pour un débutant (comparatifs de 2026, à recouper dans `sources.md`) : une vraie appli, sans terminal ; elle dit **avant le téléchargement** si un modèle tient dans ta machine ; elle est gratuite, y compris au travail ([blog de LM Studio, « free for work »](https://lmstudio.ai/blog/free-for-work), ton lien du 24/10). Ollama est cité en une phrase, comme l'autre option (il garde le terminal et l'API) ; on le retrouve dans llama.cpp (8 févr.) et l'idée 16.

| Champ | Détail |
|---|---|
| **Pilier** | IA chez moi (Help), la toute première marche : série « Abonnement ou IA locale ? » |
| **Format** | Longue, 9-11 min. **Testée** : capture d'écran de ton installation sur ta machine |
| **Trafic visé** | Recherche (« ia en local », « lm studio », « ollama ») + suggestions à côté des vidéos « IA locale pour débutants » du mois |
| **Mot-clé** | ia en local (18 376 par mois, +27 %, vidIQ 24/10, recherche de l'agent ; un autre appel du même jour donnait 21 403 : le volume bouge) ; installer ia en local (4 531, concurrence 28, vidIQ 24/10) ; ollama (9 849 en France) et lm studio (2 581 en France), vidIQ 23/10 |
| **Type de hook** | Démonstration (internet coupé, Google « inaccessible », et l'IA qui répond) + enjeu (Fable 5 coupé pour tout le monde) |
| **Production estimée** | ~12-15 h (estimation : capture d'écran, peu d'animations) |

## Titres

1. Recherche : *IA en local : installer ta propre IA gratuitement (LM Studio, tuto débutant)*
2. Curiosité : *Ton IA peut être coupée demain. Pas celle-là.*
3. Mixte (recommandé) : *IA en local : installe ta propre IA en 10 minutes (gratuit, sans abonnement)*, ou sans chiffre : *IA en local : installe ta propre IA, gratuite et sans abonnement*

« 10 minutes » doit être tenu : il faut télécharger environ 6,5 Go (l'appli, puis le modèle), soit plus d'une heure à 10 Mbit/s (F39). Garde le chiffre seulement si ton chrono le tient **hors téléchargement**, et dis-le dans la vidéo. Le titre 2 tient si la vidéo dit « à distance » (H6). Le titre de la vidéo du 7 déc. commence aussi par « IA en local : » : c'est le mot-clé, ça ne gêne pas, mais on pourra raccourcir le sien en *Comment lire le nom d'un modèle d'IA (35B, A3B, Q4_K_M…)*. [CROCHET : ton choix]

## Miniature (charte verte, trois versions)

Trois miniatures, comme pour chaque vidéo (règle du 24/10 dans `CLAUDE.md`) : a noir, b vert (la charte de la série, celle par défaut), c hors niche. **Piste corrigée le 25/10** : l'icône du wifi barrée n'est pas dans ta capture. Ce qu'elle montre, c'est la page « Ce site est inaccessible », puis Gemma qui répond quand même. La miniature reprend cette scène, qui est aussi le premier plan de la vidéo.

- **a et b, « Hors ligne »** (même scène, seules les couleurs changent) :
  - **fond** : la page d'erreur, recréée en grand et désaturée (la petite page triste, « Ce site est inaccessible ») ; pas de logo de Google ni de Chrome ;
  - **premier plan**, sur les deux tiers de droite : la bulle de réponse de Gemma, en couleur (menthe `#07c095` pour b), avec trois lignes de texte et le curseur qui clignote ;
  - **texte** : « HORS LIGNE », en haut à gauche ; sinon « ET POURTANT… » ;
  - **la question qu'elle pose** : comment ça répond, si rien ne charge ? L'émotion : la surprise. Le titre complète (« installe ta propre IA ») sans répéter l'image ;
  - **le risque** : à 168 px, la bulle doit se lire comme « ça répond » sans qu'on lise son texte. Teste-le dès la maquette (planche de lisibilité).
- **c, hors niche, « Le piège »** : inspirée des chaînes de « scam baiting » (Kitboga, par exemple ; la vidéo d'origine est à noter dans `propositions.md` au moment des références) :
  - le faux message du test 3, en gros, `sidedeouf.fr` et « accepté immédiatement » cerclés de rouge ;
  - texte « IL TOMBE DEDANS ? » ;
  - elle tient : la vidéo montre qu'il tombe dedans, puis qu'il se rattrape avec Think. Mais elle promet le test plus que l'installation : c'est le joker du test.

Pas de logo d'Anthropic ni de capture d'une annonce de Fable 5 en miniature : le sujet, c'est ton IA à toi, pas l'affaire.

## Les 15 premières secondes

Le meilleur moment tout de suite : la preuve qu'elle tourne chez toi.

> « Je coupe internet. [VISUEL : Google « Ce site est inaccessible », puis Gemma qui répond, en vrai, sur ta machine (capture du 24/10, 10:08-10:35)] Et mon IA me répond quand même. Le 12 juin, Anthropic a coupé Fable 5, le modèle le plus puissant qu'il ait jamais ouvert au public. Pour tout le monde. Trois jours après sa sortie. »

Puis, avant 30 s : « Et ce n'était même pas son choix : c'est le gouvernement américain qui l'a exigé. Fable 5 est revenu 19 jours plus tard. Sauf que du coup, on sait une chose : ça peut arriver n'importe quand, chez n'importe quel fournisseur, même quand il n'est pas d'accord. Alors aujourd'hui, on installe une IA qui tourne chez toi, que personne ne peut te couper à distance. »

Vérifié le 24/10 (`sources.md`, H1-H8) : sortie le 9 juin, coupure le 12 juin pour tous, retour le 1er juillet, tout confirmé par Anthropic ; une directive américaine de contrôle des exportations, qu'Anthropic a appliquée en disant ne pas être d'accord (citation exacte dans `sources.md`) ; « le plus puissant qu'il ait jamais ouvert au public », au passé (Mythos 5 existe, et Fable 5.1 est sorti en septembre). Internet est coupé **après** le téléchargement du modèle et le test 1 (ta capture du 24/10). Le hook à jour est celui du [script](script.md) V3 (25/10). Internet coupé, seul, n'est pas unique (Tomatech et 100 % Futuriste ouvrent dessus) : c'est Fable 5 qui fait notre différence, il reste dans les 15 s.

## Texte et sous-texte

- **Texte** : une IA en local, c'est un fichier chez toi et une appli qui le fait tourner. Avec LM Studio, ça s'installe comme un jeu.
- **Sous-texte** : ce que tu ne possèdes pas, on peut te le retirer. (Le même que *Tu n'as jamais possédé tes jeux*, 22 févr. : on pourra y renvoyer.) [CROCHET : ton sous-texte à toi ; celui-ci est une proposition]
- **À ne pas recadrer** : ce n'est pas une vidéo contre le cloud. Tu utilises Claude, et tu le dis : le local, c'est le plan B qu'on contrôle, et ce qu'on garde pour soi.

## Contenu (plan)

> Plan d'origine (24/10). Celui qui fait foi est le [script](script.md) V3 du 25/10, calé sur ta capture : plus de piège Bionic, plus de document, plus de tokens par seconde ; trois tests à la place.

1. **Hook (0:00-0:30)** : voir plus haut.
2. **Pourquoi une IA chez toi (0:30-2:30)**, trois raisons, une image chacune :
   - **personne ne te la coupe** : Fable 5, puis la règle générale (un fournisseur peut changer ses prix, ses conditions, ou couper un modèle ; tu ne décides pas de sa politique) ;
   - **tes données restent chez toi** : au travail, le code, les documents des clients ne sortent pas de la machine. Et LM Studio est gratuit au travail ([blog de LM Studio](https://lmstudio.ai/blog/free-for-work), date à vérifier) ;
   - **ni abonnement, ni internet** une fois le modèle téléchargé.
   - Et l'honnêteté tout de suite : un modèle qui tient chez toi est moins fort que les plus gros du cloud. Combien moins ? « J'ai fait le test sur ma carte » : c'est Claude #1 (16 nov.), à annoncer en une phrase.
3. **Ce qu'il te faut (2:30-3:30)** : la mémoire de ta carte graphique (ou de ton Mac) décide de la taille du modèle. Ce qui tient sur 8 Go, sur 16 Go ; sans carte graphique, ça marche aussi, plus lentement. Configuration minimale de LM Studio (à vérifier : Windows, Mac Apple Silicon, Linux ; processeur, mémoire). Pour ton public : « pas besoin d'un PC à 2 000 € pour commencer ».
4. **Installer LM Studio (3:30-5:00)** : **lmstudio.ai/download**, deuxième bloc « Download LM Studio » (la page d'accueil ne propose que LM Studio Bionic, une autre appli, un agent avec abonnements : à dire, c'est le piège du débutant ; jamais un lien tiers), le téléchargement, l'installation, le premier lancement. Ce que demande l'installation, écran par écran (à capturer).
5. **Choisir et télécharger un modèle (5:00-7:00)** : la recherche dans l'appli ; l'indicateur qui dit si le modèle tient ; un petit modèle récent qui tourne bien sur peu de mémoire 8 Go de VRAM → Gemma 4 E4B (5,9 Go dans le catalogue), 16 Go → Gemma 4 12B (7,4 Go dans le catalogue), sous réserve de ce que tu vois à l'écran (F34-F36) [CROCHET : ton choix] ; et un plus gros sur ta 5080. Les noms bizarres (« 12B », « Q4_K_M ») : « je t'explique tout ça dans une vidéo à part, pour l'instant, prends celui que l'appli met en vert ». Carte YouTube vers la vidéo du 7 déc. à ajouter le jour de sa sortie.
6. **Lui parler (7:00-9:00)** : la première question ; la vitesse affichée (tokens par seconde) ; **le wifi coupé**, en vrai ; donner un document à lire (si LM Studio le fait toujours, à vérifier) avec un document public, jamais un document de travail.
7. **Fin (9:00-10:00)** : ce que tu en fais toi [CROCHET : à écrire par toi] ; Ollama en une phrase, pour ceux qui veulent le terminal ; la suite de la série. Écran de fin : Claude #1 (« 16 Go de VRAM suffisent-ils pour remplacer Claude ? ») dès sa sortie le 16 nov. ; d'ici là, la vidéo IA la plus récente.

## Points à vérifier (phase 1 et 2)

1. **Fable 5** : date de sortie, date et motif de la coupure, qui l'a décidée, date du retour, déclaration d'Anthropic (sources primaires : annonce d'Anthropic, page de statut). Premières sources : [Security Boulevard](https://securityboulevard.com/tag/fable-5/), [Kami Labs](https://kami-labs.fr/ia/claude-fable-5-desactive-pour-les-etats-unis/), [iThome](https://www.ithome.com.tw/tags/claude-fable-5) (retour le 1er juillet).
2. **D'autres coupures** d'un modèle ou d'un service d'IA par un fournisseur (prix, conditions, retrait d'un modèle), pour la règle « n'importe quel fournisseur » : un ou deux exemples datés et sourcés.
3. **LM Studio gratuit au travail** : date et conditions exactes du billet.
4. **LM Studio aujourd'hui** : version, configuration minimale, l'indicateur de compatibilité (son nom exact dans l'interface), la discussion avec un document, la licence (l'appli est-elle open source ? non d'après ce qu'on sait : à vérifier, Ollama l'est).
5. **Ollama** : appli de bureau sur Windows et Mac (depuis 2025, à vérifier), licence.
6. **Mots-clés** : « installer ia en local », « lm studio tuto », « ia locale gratuite » (vidIQ, France) ; les vidéos françaises du mois sur le sujet (hôtes des suggestions, dont « Adieu le cloud pour les LLM ! Vive le local » de Le Lab IA, 47,8 K, ×24 au radar).
7. **« 10 minutes »** : ton chronomètre pendant la capture.
8. **Contraintes** : aucune clé d'API à l'écran (LM Studio n'en demande pas) ; aucun modèle « uncensored » ni « abliterated » dans la recherche à l'écran ; aucune appli ni document de travail.
