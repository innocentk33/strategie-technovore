# Pourquoi avoir ta propre IA, et comment l'installer (LM Studio) : script final

**Titre recommandé** : *IA en local : installe ta propre IA, gratuite et sans abonnement* (titre 3 de la fiche, sans chiffre). Ta capture ne tient pas « 10 minutes » : d'après l'horloge de ta barre des tâches, l'installateur est téléchargé à 18 h 10 et la première réponse arrive à 18 h 23, soit 13 minutes, dont 4 de téléchargement du modèle (18 h 18 → 18 h 22). Il en reste 9, mais avec le détour par le gestionnaire des tâches et les modèles qu'on regarde : trop juste pour l'écrire dans un titre.

**Version 3 du 25/10/2026**, calée sur ta capture du 24/10 (`installation lm studio et test avec gemma 4.mp4`, 11 min 39). La version 2, celle d'après le [grill](grill-v1.md), reste dans [`script-v2.md`](script-v2.md), la V1 dans [`script-v1.md`](script-v1.md). Faits : [`sources.md`](sources.md) et ta capture (colonne « Capture » des faits). Sortie : **lun. 2 nov. 2026, 18 h**.

## Changements depuis la V2 (25/10, tes retours)

1. **La vidéo suit ta capture, et rien d'autre** : l'installation de LM Studio, Gemma 4 12B, trois tests, internet coupé. Partent : le test du document (les conditions de LM Studio et son plan B), le test sans carte graphique, Ctrl+2 (tu passes par « Model Search » dans la barre de gauche), le chrono.
2. **Plus de « piège » sur le site officiel.** Le moteur, chacun le choisit (Ollama, llama.cpp, LM Studio) : la vidéo le dit maintenant, et dit pourquoi toi, tu as pris LM Studio. La boucle du hook devient le troisième test (le message louche, où il tombe dans le panneau la première fois). De Bionic, il ne reste qu'une demi-phrase pratique (« celui du dessus, c'est une autre appli »), gardée (ta décision du 25/10).
3. **AVX2 et son crochet sont coupés.**
4. **Ton vécu** : « moi, j'utilise Claude pour coder des applis mobiles, et je vais continuer ».
5. **« Les deux autres, je te les donne pendant le téléchargement, parce qu'on a le temps »** devient « Les deux autres, je ne vais pas te les expliquer : je vais te les montrer. » Et les tests les montrent : Dr Stone hors ligne (ni abonnement, ni internet), le message louche (tes données restent chez toi).
6. **« Je coupe le wifi » devient « je coupe internet »** : ta capture ne montre pas l'icône du wifi, elle montre Google qui ne charge plus (« Ce site est inaccessible »), même quand tu actualises la page plusieurs fois.
7. **Les crochets sont remplis avec ce qu'on voit à l'écran** : pas de compte à créer, Gemma 4 E4B proposé au premier lancement, ta RTX 5080 et ses 16 Go dans le gestionnaire des tâches, « Full GPU Offload Possible » en vert sur Gemma 4 12B QAT (7,15 Go), « Partial GPU Offload Possible » sur Flint (24,17 Go), 4 minutes de téléchargement.
8. **Nouveau temps fort** : le bouton Think. Sans lui, Gemma rédige une réponse enthousiaste au message louche ; avec lui et « réfléchis bien », il repère l'hameçonnage. C'est l'aveu « moins fort que le cloud », montré au lieu d'être dit.

**Durée** : voir la mesure en bas. Timecodes calculés à 145 mots/min, à recaler sur la vraie prise.

**Texte et sous-texte** :
- **Texte** : une IA en local, c'est un fichier chez toi et un moteur qui le fait tourner. Avec LM Studio, ça s'installe comme un jeu.
- **Sous-texte** : ce que tu ne possèdes pas, on peut te le retirer. **Montré, jamais dit** : Fable 5 coupé (hook), le modèle qui répond internet coupé (section 4), récolté à la fin (« Ton fichier, lui, n'est jamais parti »).
- **À ne pas recadrer** : ce n'est pas une vidéo contre le cloud. Tu utilises Claude pour coder tes applis et tu le dis : le local, c'est le plan B que tu contrôles.

**Fil rouge** : internet coupé. Au hook (la preuve), annoncé pendant le téléchargement, coupé en vrai à la section 4, et rappelé dans la phrase-bilan de la fin. **Motif secondaire** : les trois raisons (une dite à la section 1, les deux autres montrées par les tests).

**Boucles ouvertes** :
1. « Comment t'as une IA que personne ne peut te couper à distance ? » (hook) → tenue à la section 4 (internet coupé, en vrai), récoltée à la fin.
2. « Je lui tends un piège… la première fois, il tombe dedans » (hook) → tenue par le troisième test.
3. « Les deux autres, je vais te les montrer » (section 1) → tenue par les tests 2 et 3.
4. « Combien moins fort que le cloud ? » (section 3) → ouverte exprès, refermée par Claude #1 (16 nov.).

**Format** : tuto **testé**, filmé sur ta machine le 24/10/2026 (LM Studio 0.4.26, Windows, RTX 5080). Les libellés d'interface cités sont ceux de ta capture.

**Conventions** : texte normal = voix off. `[VISUEL : …]` = animation ou capture (avec le timecode dans ta capture, « capture 6:20 »). `[SON : …]` = bruitage ou musique. `[CROCHETS EN MAJUSCULES]` = à remplir ou à vérifier par toi. Nombres en lettres pour la lecture.

**Interdits à l'écran** (tes règles) : aucune clé d'API ; aucun modèle « uncensored » ni « abliterated » (ta liste « Staff picks » n'en a pas) ; aucune appli ni aucun document de travail ; aucun lien tiers vers LM Studio. **À flouter** : rien de repéré ; vérifie seulement la barre des tâches (tes applis épinglées) si tu ne veux pas les montrer.

---

## 0. Hook (0:00 – 0:34) · objectif : 75 % à 0:15, 50 % à 1:00

[VISUEL : capture 10:08-10:14 : le nouvel onglet, Google qui ne charge plus, « Ce site est inaccessible » en gros. Pas de titre, pas de logo, pas de visage. Garde un clic sur « Actualiser » : la page reste en erreur.]
[SON : clic sec, puis le souffle du PC, rien d'autre.]

Je coupe internet.

[VISUEL : capture 10:15-10:35 : la question sur Dr Stone envoyée, la réponse qui s'écrit. Garde l'onglet Google « inaccessible » visible en vignette dans le coin.]

Et mon IA me répond quand même.

[VISUEL : coupe nette sur fond sombre. « 12 juin 2026 » en gros, puis la capture du communiqué d'Anthropic du 12/06/2026 (anthropic.com/news/fable-mythos-access), date visible. Frise : 9 juin (sortie) → 12 juin (coupure), « 3 jours ».]
[SON : coupure de courant, façon serveur qui s'éteint.]

Le douze juin, Anthropic a coupé Fable 5, le modèle le plus puissant qu'il ait jamais ouvert au public. Pour tout le monde. Trois jours après sa sortie.

[VISUEL : retour sur ta machine, Google toujours « inaccessible ».]

Du coup, comment t'as une IA que personne ne peut te couper à distance ?

Bah, tu la fais tourner chez toi, comme celle-là. Et la tienne, on l'installe maintenant, gratuitement.

[VISUEL : flash d'une demi-seconde sur le message louche (capture 10:42), « sidedeouf.fr » surligné, puis la réponse enthousiaste de Gemma (capture 11:00), floutée.]

Et à la fin, je lui tends un piège. La première fois, il tombe dedans.

---

## 1. Personne ne te la coupe (0:34 – 1:40)

[VISUEL : trois cases vides à l'écran, charte verte. Seule la première s'allume : « Personne ne la coupe ». Les deux autres restent grises jusqu'aux tests.]

Avant, je précise un truc : moi, j'utilise Claude pour coder des applis mobiles, et je vais continuer.

[VISUEL : la frise du hook revient : 12 juin → 1er juillet, « 19 jours ». En petit sous la frise : « directive américaine de contrôle des exportations, appliquée par Anthropic ». Si tu veux, la phrase d'Anthropic en anglais, datée (sources.md, « Formulations exactes »).]

Sauf que le douze juin, en fait, ce n'était même pas le choix d'Anthropic : c'est le gouvernement américain qui l'a exigé. Anthropic a appliqué la directive, tout en disant qu'il n'était pas d'accord. Et Fable 5 est revenu dix-neuf jours plus tard.

[VISUEL : capture des notes de version d'OpenAI ou de l'article de Simon Willison (08/08/2025), date en gros.]

Et ça arrive aussi ailleurs. En août 2025, quand GPT-5 est sorti, OpenAI a retiré GPT-4o de ChatGPT le jour même. Les abonnés ont râlé, et il est revenu quelques jours plus tard.

Donc ça peut arriver n'importe quand, chez n'importe quel fournisseur, même quand il n'est pas d'accord. Et toi, tu n'as pas ton mot à dire. Du coup, une IA chez toi, c'est ton plan B, celui que tu contrôles.

[VISUEL : les trois cases ; la première allumée, les deux autres avec un point d'interrogation.]

Et ça, c'est la première raison d'avoir ta propre IA. Les deux autres, je ne vais pas te les expliquer : je vais te les montrer.

---

## 2. Installer LM Studio (1:40 – 3:21)

[VISUEL : schéma très simple, deux blocs : « un fichier (le modèle) » + « un moteur (l'appli) » = ton IA. Sous le bloc « moteur », trois logos : Ollama, llama.cpp, LM Studio ; celui de LM Studio s'allume.]

Bon, on installe. En fait, une IA en local, c'est deux choses : un fichier, le modèle, et un moteur qui le fait tourner. Des moteurs, il y en a plusieurs : Ollama, llama.cpp, LM Studio. Moi, j'ai pris LM Studio, parce que c'est une vraie appli, sans terminal. Et surtout, elle te dit si un modèle tient dans ta machine avant que tu le télécharges. Tu vas voir pourquoi ça compte.

[VISUEL : capture 0:20-0:50 : la page lmstudio.ai/download, les deux blocs ; le deuxième, « Download LM Studio », entouré en vert. Texte à l'écran, 3 secondes : « lmstudio.ai/download → 2e bloc ». Le même texte en description.]
[SON : « ding » sur le deuxième bloc.]

Donc va sur lmstudio.ai/download, et prends le deuxième bloc, « Download LM Studio » : celui du dessus, c'est une autre appli. Il existe pour Windows, Mac et Linux. Et ne passe jamais par le lien d'un autre site : prends-la toujours là.

[VISUEL : deux colonnes, « Mac » et « PC », sur la page de téléchargement floutée. Chaque condition s'écrit pendant qu'elle se dit. Source à l'écran : lmstudio.ai/docs/app/system-requirements, relevé le 24/10/2026.]

Avant de cliquer, vérifie juste que ta machine suit. Sur Mac, il faut une puce Apple, M1 ou plus récent, et macOS 14 : les Mac Intel ne marchent pas. Et LM Studio conseille seize gigas de RAM, plus quatre gigas de mémoire sur la carte graphique sous Windows. Ce sont des conseils, hein : un Mac de huit gigas tourne aussi, avec de petits modèles.

[VISUEL : capture 1:00-1:50, en accéléré : le fichier `LM-Studio-0.4.26-4-x64.exe` (590 Mo) dans Téléchargements, la licence, la barre d'installation.]
[SON : le « ding » de fin d'installation d'un launcher.]

Ensuite, franchement, ça s'installe comme un jeu. L'installateur fait six cents mégas, tu acceptes la licence, et c'est parti. Pas de compte à créer.

[VISUEL : capture 2:10-2:20 : l'écran « Your first model », google/gemma-4-e4b proposé, puis le clic sur « Skip for now ».]

Et au premier lancement, il te propose déjà un modèle : Gemma 4 E4B, le petit. Moi, je passe, parce que ma carte peut en prendre un plus gros. Et la tienne, on va voir ça tout de suite.

---

## 3. Choisir et télécharger un modèle (3:21 – 6:10)

[VISUEL : le schéma revient, le bloc « fichier » s'allume, encore vide. Puis une jauge « VRAM » vide à côté d'une carte graphique. Deux repères : 8 Go, 16 Go. Sur la ligne du Mac : « mémoire du Mac ».]

L'appli est là. Sauf qu'elle est vide : il lui manque le fichier, le cerveau. Et pour le choisir, retiens une seule chose : c'est la mémoire de ta carte graphique, la VRAM, qui décide. Ou la mémoire de ton Mac. Plus elle est grande, plus le modèle peut être gros.

[VISUEL : capture 3:20-3:30 : le gestionnaire des tâches, « Processeur graphique », « NVIDIA GeForce RTX 5080 », la ligne de la mémoire GPU dédiée (« 16,0 Go ») entourée.]

Pour la connaître sur Windows, ouvre le gestionnaire des tâches, va dans les performances, puis sur ta carte graphique, et lis la mémoire dédiée. Moi, c'est une RTX 5080 : seize gigas.

[VISUEL : capture 2:50-3:00 : le clic sur « Model Search » dans la barre de gauche, la liste « Staff picks ».]

Ensuite, dans LM Studio, clique sur « Model Search », à gauche. Il te montre direct une sélection de modèles, et Gemma 4 est dedans. Gemma 4, c'est Google : sorti en avril, sous licence Apache 2.0. En gros, tu as le droit de t'en servir, même pour ton travail.

[VISUEL : les noms de la liste grossissent, « 12B » et « QAT » surlignés, puis un tampon « vidéo à part » se pose dessus.]

Et là, tu vas voir des noms bizarres : douze B, QAT… Ceux-là, je leur consacre une vidéo entière. Pour l'instant, ne lis pas les noms : regarde plutôt ce que l'appli te dit.

[VISUEL : capture 5:40-5:50 : la fiche de google/gemma-4-12b-qat, l'étiquette verte « Full GPU Offload Possible » en gros plan, 7,15 GB. Puis capture 4:20 : Flint, l'étiquette « Partial GPU Offload Possible », 24.17 GB.]

Sur Gemma 4 12B, elle écrit en vert : « Full GPU Offload Possible ». En gros, le modèle tient en entier dans ma carte graphique. Par contre, sur Flint, vingt-quatre gigas, c'est « Partial » : une partie déborde sur la RAM, donc ça tournera plus lentement. Et c'est pour ça que j'ai pris LM Studio : tu ne grilles pas des gigas de data pour un modèle qui ne tournera jamais bien chez toi.

[VISUEL : deux cartes, façon sélection de personnage : « 8 Go de VRAM → Gemma 4 E4B, 5,9 Go » et « 16 Go → Gemma 4 12B QAT, 7,15 Go ». Légende : « catalogue de LM Studio, 24/10/2026 ».]

Alors, si ta carte a huit gigas, prends Gemma 4 E4B, celui qu'il te proposait au lancement : cinq virgule neuf gigas, ça te laisse de la marge. Et si elle en a seize, comme moi, Gemma 4 12B : un peu plus de sept gigas.

[VISUEL : capture 5:30-6:20 : le clic sur « Download », la barre qui avance (« Downloading 8% »), l'horloge de la barre des tâches visible (18:18), puis « Download Completed! » (18:22). En surimpression, le calcul : « 7,15 Go · chez moi : 4 min · 100 Mbit/s ≈ 10 min · 10 Mbit/s ≈ 1 h 35 ».]

Tu cliques sur télécharger, et là, il faut être patient. Chez moi, ça a pris quatre minutes. Mais avec une connexion à dix mégabits, compte plutôt une heure et demie.

### Pendant le téléchargement

[VISUEL : retour face caméra ou capture fixe, sans effet. La barre de téléchargement reste en fond, floutée.]

Et pendant que ça descend, je te dois un truc : un modèle qui tient dans ton PC est moins fort que les plus gros du cloud. Combien moins fort ? J'ai rassemblé les mesures de ceux qui ont la même carte que moi, et je te montre tout dans une vidéo qui sort dans deux semaines.

Pour ne pas la rater, abonne-toi : sur Technovore, il y a une nouvelle vidéo chaque lundi.

[VISUEL : bouton « S'abonner », 3 secondes, en bas à droite. Pas d'animation de cloche.]

[VISUEL : « Download Completed! », puis trois cases numérotées 1, 2, 3 ; la troisième porte un hameçon.]
[SON : la musique baisse, un tic-tac.]

Et dès que c'est fini, je lui fais passer trois tests. Le dernier, c'est le piège.

---

## 4. Les trois tests (6:10 – 9:05)

[VISUEL : capture 6:30-6:40 : « Use in New Chat », la fenêtre de discussion vide, « gemma-4-12b-qat » sélectionné.]

C'est bon, il est téléchargé. Tu le charges, et tu lui parles comme à n'importe quel chat.

[VISUEL : capture 7:20-7:40 : la question « d'ou vient le meme macon explosion », le bloc « Thinking… » ouvert ; la ligne « Is it the "Macon" from The Boys? No. » surlignée. Puis capture 9:20-9:50 : sa réponse, « L'expression « Macron explosion »… ».]

Test numéro un : une question de culture internet. D'où vient le mème Macron explosion ? Sauf que j'ai fait une faute : j'ai écrit « Macon ». Et comme j'avais activé Think, le bouton qui le fait réfléchir avant de répondre, on le voit chercher. Il réfléchit en anglais : « Macon, c'est un perso de The Boys ? » Non. Et il finit par retrouver Macron, et il répond en français.

Et c'est plutôt bien vu.

[VISUEL : capture 10:08-10:14 : le nouvel onglet, Google « Ce site est inaccessible », puis tes clics sur « Actualiser », en accéléré : la page reste en erreur. Même plan qu'au hook.]
[SON : le même clic sec qu'à 0:00.]

Et maintenant, tu te rappelles le début ? Je coupe internet. La preuve : Google ne charge plus. J'actualise… toujours rien.

[VISUEL : capture 10:15-10:35 : « Explique-moi la 1ère saison de Dr Stone », la réponse qui s'écrit, sans coupe entre l'onglet Google et la réponse. La deuxième case s'allume : « Ni abonnement, ni internet ».]

Test numéro deux, hors ligne : explique-moi la première saison de Dr. Stone. Et en effet, il répond : la lumière verte qui change toute l'humanité en pierre, Senku qui se réveille des milliers d'années plus tard…

Et c'est juste.

Le modèle est sur mon disque, donc il n'a besoin de rien d'autre. D'après la doc de LM Studio, une fois le modèle chez toi, tout tourne en local, même sans internet. Et voilà la deuxième raison : ni abonnement, ni internet.

[VISUEL : capture 10:40-10:45 : le message collé, en gros. Surligne « mettre votre nom en description », « accepté immédiatement » et « sidedeouf.fr ». En petit, dans un coin : « message et site inventés pour le test ».]

Test numéro trois, le piège. Je lui colle un faux message, que j'ai écrit moi-même, comme on en reçoit : on me remercie, on me demande de mettre mon nom en description pour que mon site soit « accepté immédiatement », et on me renvoie vers sidedeouf.fr. Et je lui demande de rédiger ma réponse. Toi, tu paries quoi ?

[VISUEL : capture 10:48-11:05 : les trois options de réponse ; « Option 3 : Enthousiaste » et le conseil « Action immédiate : N'oubliez pas de faire la modification… pour gagner du temps ! » surlignés en rouge.]
[SON : buzzer d'arcade.]

Il me rédige trois réponses, toutes polies, dont une enthousiaste. Et il me conseille même de faire la modification vite, pour gagner du temps. Bref, il est tombé dans le panneau.

[VISUEL : capture 11:05-11:15 : le clic sur « Think », « reflechi bien » tapé, le bloc « Thinking… ».]

Du coup, j'active Think, et je lui écris juste : réfléchis bien.

[VISUEL : capture 11:15-11:39 : « Les “Signaux d'alerte” (Red Flags) », « Phishing (hameçonnage) », puis « Mon conseil final » surligné en vert. La troisième case s'allume : « Tes données restent chez toi ».]
[SON : « ding ».]

Et là, changement de ton. Il liste les signaux d'alerte : l'urgence, la demande de modification, le lien. Il parle d'hameçonnage. Et son conseil final : ne clique sur aucun lien, et ne donne aucune information personnelle. Voilà la leçon : un petit modèle, ça se guide. Laisse-le réfléchir.

[VISUEL : l'onglet Google « inaccessible » (capture 11:20) en vignette, puis le message louche qui reste dans le PC, une flèche vers un nuage barrée.]

Et ce message, avec un nom, un lien, une demande perso, il n'est jamais sorti de mon PC : internet était coupé. C'est la troisième raison : tes données restent chez toi. Du coup, au travail, ton code ou les mails d'un client ne sortent pas de ta machine. Et justement, LM Studio est gratuit, à la maison comme au travail : ils l'ont annoncé en juillet 2025. Le lien est en description.

[VISUEL : capture du billet « free for work » de LM Studio, date du 08/07/2025 visible.]

---

## 5. Fin (9:05 – 10:28)

[VISUEL : le schéma complet : fichier + moteur = ton IA. Google « inaccessible » en vignette à côté.]
[SON : la musique du début revient, plus posée.]

Voilà comment on a une IA à soi : un fichier sur ton disque, une appli pour le lancer, et un internet que tu peux couper.

Et si tu veux que même l'appli soit libre, l'autre option, c'est Ollama : open source, avec une appli sur Mac et Windows, et le terminal pour aller plus loin.

[VISUEL : capture de ollama.com, sans compte connecté, 3 secondes.]

[VISUEL : deux colonnes. À gauche, « Local » : un contrat, une question de santé, les données d'une PME. À droite, « En ligne » : tout le reste. Au milieu, un « + ».]

Et en vrai, il n'y a pas de meilleur choix. Un contrat à relire, une question sur ta santé, un truc ultra perso : ça, tu le donnes au local. Et pour une entreprise, une PME, c'est encore plus vrai. Par contre, pour aller vite, garde aussi un modèle en ligne : il est plus fort. Du coup, la bonne architecture, c'est l'hybride. Un peu de local pour ce qui est perso, et le cloud pour tout le reste.

[VISUEL : la frise de Fable 5, en petit : « coupé le 12 juin, revenu le 1er juillet ». À côté, le fichier du modèle sur ton disque, qui n'a pas bougé.]

Fable 5 est revenu, cette fois. Sauf que ton fichier, lui, n'est jamais parti : personne ne peut te le couper à distance.

Dis-moi en commentaire ta carte graphique, ou ton Mac, et le modèle qui a tourné chez toi. Et si rien ne tient, écris-le aussi : on cherchera ensemble le bon modèle. Et la suite de la série, c'est juste là.

[VISUEL : écran de fin, 20 s, charte verte. **Jusqu'au 16 nov.** : la vidéo IA la plus récente, *OpenCode a été gravement piraté (explication !)* (21 oct.). **Dès le 16 nov.** : « 16 Go de VRAM suffisent-ils pour remplacer Claude ? ». Bouton « S'abonner » à droite. La phrase dite (« la suite de la série ») tient dans les deux cas.]

---

## Plans de ta capture (24/10, 11 min 39)

Timecodes approximatifs (relevés toutes les 2 à 10 s), heure de ta barre des tâches entre parenthèses.

| Capture | Ce qu'on voit | Section |
|---|---|---|
| 0:00-0:50 | Chrome en invité, lmstudio.ai puis lmstudio.ai/download, les deux blocs, version 0.4.26 | 2 |
| 1:00-1:10 | `LM-Studio-0.4.26-4-x64.exe`, 590 Mo, dans Téléchargements (18:10) | 2 |
| 1:20-1:50 | La licence, la barre d'installation | 2 |
| 2:10-2:20 | « Your first model » : google/gemma-4-e4b proposé, « Skip for now » | 2 |
| 2:30-3:00 | L'accueil, puis « Model Search » et la liste « Staff picks » | 3 |
| 3:20-3:30 | Le gestionnaire des tâches : RTX 5080, 16,0 Go de mémoire GPU dédiée | 3 |
| 4:20 | Flint (recursivesi/flint), 24.17 GB, « Partial GPU Offload Possible » | 3 |
| 4:30-5:20 | Qwen3.8 27B (« Partial »), Gemma 4 12B QAT, 26B A4B QAT, 31B QAT | 3 (option) |
| 5:30-6:20 | google/gemma-4-12b-qat, 7.15 GB, Q4_0, « Full GPU Offload Possible », téléchargement (18:18) jusqu'à « Download Completed! » (18:22) | 3 |
| 6:30-7:10 | « Use in New Chat », la discussion vide | 4 |
| 7:20-7:50 | Test 1 : « d'ou vient le meme macon explosion », Think, le raisonnement en anglais (18:23) | 4 |
| 8:00-9:10 | Doublon (retour à la recherche, l'infobulle de Think, « Use in New Chat ») : **à couper**, sauf l'infobulle « Controls whether the model will think before replying » si tu veux montrer Think | — |
| 9:20-9:50 | La réponse du test 1 (« Origine du même Macron ») | 4 |
| 9:56-10:14 | Test 2 tapé, puis l'onglet Google : « Ce site est inaccessible » | 0, 4 |
| 10:15-10:35 | La réponse sur Dr Stone | 0, 4 |
| 10:40-11:05 | Test 3 sans Think : trois réponses, dont l'enthousiaste | 0, 4 |
| 11:05-11:39 | Think + « reflechi bien » : signaux d'alerte, hameçonnage, conseil final ; Google toujours inaccessible (≈ 11:20) | 4 |

**L'ordre, confirmé par toi le 25/10** : le test 1 est fait connecté, puis tu coupes internet (Google « inaccessible »), puis les tests 2 et 3, hors ligne. Le script suit cet ordre.

## Relances d'attention

Timecodes de la voix seule, à 145 mots/min (tes crochets les décaleront).

| Temps | Type | Ce qui se passe |
|---|---|---|
| 0:00 | Visuel + son | « Ce site est inaccessible », clic sec |
| 0:01 | Preuve | La réponse qui s'écrit, Google toujours coupé |
| 0:04 | Chiffre + coupe | « 12 juin », le communiqué daté, la frise, « 3 jours » |
| 0:15 | Question centrale | « Comment t'as une IA que personne ne peut te couper à distance ? » (finit à 0:21) |
| 0:21 | Promesse | « Comme celle-là » : retour sur ta machine |
| 0:28 | Boucle ouverte | Le piège : « la première fois, il tombe dedans » |
| 0:34 | Lien au vécu | « J'utilise Claude pour coder des applis mobiles » |
| 0:42 | Retournement | « Ce n'était même pas son choix » |
| 1:00 | Exemple daté | GPT-4o retiré le jour même |
| 1:29 | Boucle ouverte | « Je ne vais pas te les expliquer : je vais te les montrer » |
| 1:55 | Choix | Les trois moteurs, « moi, j'ai pris LM Studio » |
| 2:10 | Geste + son | lmstudio.ai/download, « ding » sur le deuxième bloc |
| 2:28 | Liste visuelle | Les deux colonnes Mac / PC |
| 2:55 | Image gamer + son | « Ça s'installe comme un jeu » |
| 3:05 | Surprise | Il propose déjà un modèle ; « moi, je passe » |
| 3:21 | Relance | « Elle est vide : il lui manque le cerveau » |
| 3:42 | Geste | Le gestionnaire des tâches, 16 Go |
| 3:55 | Geste | « Model Search » |
| 4:16 | Boucle repoussée | Les noms bizarres, tampon « vidéo à part » |
| 4:30 | Promesse tenue | « Full GPU Offload Possible », en vert |
| 4:41 | Contraste | Flint, « Partial » |
| 5:02 | Choix | Les deux cartes « sélection de personnage » |
| 5:21 | Chiffre | Quatre minutes, ou une heure et demie |
| 5:33 | Honnêteté + boucle | « Combien moins fort ? » |
| 5:57 | Appel à l'action | Abonnement |
| 6:04 | Relance | « Trois tests. Le dernier, c'est le piège » |
| 6:17 | Test 1 + humour | La faute de frappe, « Macon, c'est un perso de The Boys ? » |
| 6:48 | Boucle refermée + son | Internet coupé, même plan qu'au hook |
| 6:55 | Preuve | Dr Stone, hors ligne |
| 7:10 | Boucle refermée | Deuxième raison : ni abonnement, ni internet |
| 7:28 | Pari | Le message louche ; « Toi, tu paries quoi ? » à 7:48 |
| 7:50 | Retournement + son | Il tombe dans le panneau, buzzer |
| 8:03 | Retournement | Think, « réfléchis bien » : il repère l'hameçonnage |
| 8:28 | Boucle refermée | Troisième raison : tes données restent chez toi |
| 9:22 | Récolte | « Sauf que ton fichier, lui, n'est jamais parti » |

**Total** : 35 relances en 10 min 28 de voix, une toutes les 17 secondes environ. Les plus longs trous : 1:00 → 1:29 (la conclusion de la section 1) et 8:28 → 9:22 (la troisième raison, la fin et Ollama).

## Points de décrochage

| Moment | Risque | Problème | Parade |
|---|---|---|---|
| Section 1 | Moyen | Encore du « pourquoi » avant le premier geste | 1 min 06 ; deux faits datés ; la boucle du piège encore ouverte ; « je vais te les montrer » promet des preuves, pas un cours |
| Section 2, la configuration | Faible | Une liste de conditions techniques | Courte (plus d'AVX2) ; lue sur la page, au moment où elle sert |
| Le téléchargement | Faible | Un temps mort à l'écran | 4 min chez toi, en accéléré ; par-dessus, l'aveu « moins fort », l'abonnement et la relance des trois tests |
| Test 1 | Moyen | Une réponse longue à lire | Montre le raisonnement (la faute de frappe, The Boys), puis la réponse en accéléré ; « Et c'est plutôt bien vu » (relue par toi le 25/10) |

## Notes de montage

- **Charte verte « IA chez moi »**, police mono pour les adresses et les noms de modèle.
- **Google « Ce site est inaccessible »** est le motif de la vidéo : au hook, au test 2, en vignette au test 3 et à la fin. Le montage ne coupe pas entre l'onglet Google et la réponse du test 2 (preuve).
- **Coupe le doublon 8:00-9:10** de la capture (retour à la recherche) et accélère les attentes (téléchargements, installation, réponses longues).
- **Les trois cases** : la première à la section 1, la deuxième au test 2, la troisième au test 3.
- **Composants à construire une fois** : les trois cases, le schéma « fichier + moteur », les deux cartes de sélection 8/16 Go, la jauge VRAM. Le schéma resservira pour llama.cpp (8 févr.) ; la jauge pour *IA en local : comment lire le nom d'un modèle* (7 déc.).
- **Captures web** (connexion revenue) : le communiqué d'Anthropic du 12/06/2026, la page de Simon Willison du 08/08/2025, la page des configurations requises, le billet « free for work », ollama.com.
- **Énergie** : rapide sur le hook, posée sur la section 1, montées à 6:48 (internet coupé) et 7:50 (il tombe dans le panneau).
- **Carte YouTube** : vers *IA en local : comment lire le nom d'un modèle* à 4:16 (« je leur consacre une vidéo entière »), **à ajouter le 7 déc.** Vers Claude #1 à 5:40 (« combien moins fort ? »), **à ajouter le 16 nov.**
- **Miniature** : piste corrigée le 25/10 dans la [fiche](fiche.md) : la page « Ce site est inaccessible » en fond, la réponse de Gemma qui s'écrit par-dessus. C'est le plan d'ouverture du hook (capture 10:08-10:35) : la vidéo commence bien sur la scène de la miniature.

## Faits utilisés

| Ce que dit le script | Section | Source | Statut |
|---|---|---|---|
| « Je coupe internet. Et mon IA me répond quand même. » | 0, 4 | Capture 10:08-10:35 ; H1 | ✅ (Google inaccessible, puis réponse) |
| Le 12 juin, Fable 5 coupé pour tout le monde, 3 jours après sa sortie | 0 | F1, F2, H2, H4 | ✅ |
| « le modèle le plus puissant qu'il ait jamais ouvert au public » | 0 | F11, F12, H3 | ⚠️ formulation de la 2e vérif, mot pour mot |
| « une IA que personne ne peut te couper à distance » | 0, 5 | H6, H11 | ⚠️ formulation de la 2e vérif |
| « gratuitement » | 0, 4 | F16, F18, H9 | ✅ |
| « le gouvernement américain l'a exigé » ; « tout en disant qu'il n'était pas d'accord » | 1 | F3, F6, F7, H7 | ⚠️ formulation de la 2e vérif, mot pour mot |
| Revenu 19 jours plus tard | 1, 5 | F8, F9, H5, H8 | ⚠️ formulation de la 2e vérif |
| GPT-4o retiré le jour de GPT-5, revenu quelques jours plus tard | 1 | F13 | ⚠️ formulation de la 2e vérif |
| « j'utilise Claude pour coder des applis mobiles » | 1 | toi, le 25/10 | ✅ |
| Trois moteurs : Ollama, llama.cpp, LM Studio | 2 | F31, F33 ; `../llama-cpp/` | ✅ |
| LM Studio, une vraie appli, sans terminal | 2 | capture (tout se fait à la souris) | ✅ |
| lmstudio.ai/download, deuxième bloc « Download LM Studio » ; Windows, Mac et Linux | 2 | capture 0:20-0:50 ; F23, F27 | ✅ |
| Mac : puce Apple, macOS 14, pas de Mac Intel ; 16 Go de RAM ; 4 Go de VRAM sous Windows ; Mac de 8 Go avec de petits modèles | 2 | F20 | ✅ |
| Installateur de « six cents mégas » ; licence ; pas de compte | 2 | capture 1:00-1:50 (590 Mo, 604 283 Ko) | ✅ |
| Gemma 4 E4B proposé au premier lancement | 2, 3 | capture 2:10 | ✅ |
| La VRAM (ou la mémoire du Mac) décide | 3 | déduit de F20, F35, F36 | ⚠️ déduction, dite sans chiffre |
| Gestionnaire des tâches → performances → carte graphique → mémoire dédiée ; RTX 5080, 16 Go | 3 | capture 3:20-3:30 | ✅ (vérifie le nom exact de l'onglet sur ta capture) |
| « Model Search », à gauche ; une sélection où Gemma 4 est dedans | 3 | capture 2:50-3:00 (« Staff picks ») | ✅ |
| Gemma 4 : Google, avril 2026, Apache 2.0, utilisable au travail | 3 | F34 ; `../bases-ia-locale/sources.md` | ⚠️ formulation de la 2e vérif |
| « Full GPU Offload Possible », en vert, sur Gemma 4 12B QAT ; « Partial » sur Flint, 24 Go | 3 | capture 4:20 et 5:40 ; F29 | ✅ (à l'écran) |
| « Partial » : une partie déborde sur la RAM, donc plus lent | 3 | F29 | ⚠️ sens de l'étiquette, connu des utilisateurs, pas écrit par LM Studio : garde « plus lentement », sans chiffre |
| 8 Go → Gemma 4 E4B, 5,9 Go ; 16 Go → Gemma 4 12B, « un peu plus de sept gigas » | 3 | F35 (catalogue) ; capture 5:40 (7.15 GB) | ✅ / ⚠️ E4B : taille du catalogue, pas de ta capture |
| Quatre minutes chez moi ; une heure et demie à 10 Mbit/s | 3 | capture (18:18 → 18:22) ; calcul 7,15 × 8 ÷ 10 = 5 720 s ≈ 1 h 35 | ✅ calcul |
| Moins fort que les plus gros du cloud ; vidéo dans deux semaines ; une vidéo chaque lundi | 3 | fiche ; `calendrier.md` | ✅ |
| Think : « le bouton qui le fait réfléchir avant de répondre » | 4 | capture 8:00-9:10 (infobulle « Controls whether the model will think before replying ») | ✅ |
| Le raisonnement en anglais, « Macon », The Boys | 4 | capture 7:30 | ✅ |
| Dr Stone : lumière verte, humanité pétrifiée, Senku réveillé des milliers d'années plus tard | 4 | capture 10:20-10:35 (réponse du modèle) | ✅ relue par toi le 25/10 (« Et c'est juste ») |
| « tout tourne en local, même sans internet » | 4 | H1 | ✅ |
| Test 3 : trois réponses dont une enthousiaste, « pour gagner du temps » ; puis, avec Think, signaux d'alerte, hameçonnage, conseil final | 4 | capture 10:48-11:39 | ✅ |
| « Un petit modèle, ça se guide » | 4 | ce test seul | ⚠️ leçon tirée d'un seul essai : ne dis pas « toujours » |
| L'hybride : le local pour le perso (contrat, santé, données d'une PME), en ligne pour le reste, « plus fort » | 5 | ton avis (25/10) ; « moins fort que les plus gros du cloud » (section 3, Claude #1 le chiffrera) ; données qui restent chez toi (H1, test 3) | ✅ c'est un avis, dit comme tel ; pas de chiffre de vitesse |
| LM Studio gratuit, à la maison comme au travail, annoncé en juillet 2025 | 4 | F16, F18 | ✅ |
| Ollama : open source, appli sur Mac et Windows, terminal | 5 | F31, F33, H12 | ✅ |

Coupés depuis la V2 : Bionic expliqué (F22, F23, F25), AVX2 (F20, F21), le test sans carte graphique (F21), Ctrl+2 (F26), le chrono, les tokens par seconde (H15), le document et les conditions de LM Studio (F17, F30).

## Mesure (25/10/2026)

Comptée sur la voix off seule (sections 0 à 5, sans titres, sans `[…]`, sans tableaux), en séparant aux espaces, avec la même méthode que la V2.

| Mots de voix off | Durée à 145 / 165 mots/min | Mots avant la question centrale | Mots du hook (pont compris) | Liaisons / 100 mots (liste stricte) | Liaisons / 100 mots (liste du grill) | « vous » |
|---|---|---|---|---|---|---|
| 1 517 | 10 min 28 / 9 min 11 | 52 (≈ 0:21 / 0:19) | 84 (≈ 0:34 / 0:31) | 1,52 (23) | 1,98 (30) | 0 |

- **Par section** (liste du grill) : hook 1,2 ; section 1 : 2,5 ; section 2 : 1,6 ; section 3 : 2,0 ; section 4 : 2,1 ; fin : 2,0. Le hook est sous 1,5 : il est fait de phrases courtes et d'images (« Je coupe internet. »), c'est voulu ; si le grill le relève, la piste est « Et tu vas voir : la première fois, il tombe dedans ».
- **Les 15 premières secondes** (36 mots à 145 mots/min) vont jusqu'à « …Pour tout le monde » (33e mot) : internet coupé, la réponse et Fable 5 coupé y sont tous les trois ; « trois jours après sa sortie » finit à 0:16.
- **Plus long que la V2** (1 517 mots contre 1 332, après tes réponses du 25/10) : les trois tests (≈ 400 mots) remplacent le document, et la fin hybride ajoute 80 mots. Avec les captures en accéléré, compte 11 min environ. Si tu veux raccourcir, coupe dans la section 3 (les noms bizarres, Flint), pas dans les tests.

## Questions pour l'auteur

Réglées le 25/10 : le test 1 est fait **avant** de couper internet (le script suit cet ordre) ; le message du test 3 et `sidedeouf.fr` sont **inventés** (la voix le dit, un petit texte aussi ; le domaine n'existait pas le 25/10, revérifie-le la veille de la sortie) ; la demi-phrase sur Bionic est **gardée** ; les réponses des tests 1 et 2 sont **justes** ; la miniature est **corrigée** dans la fiche.

Réglées aussi le 25/10 : tu as coupé la connexion, et la capture le prouve (Chrome reste sur « Ce site est inaccessible » à chaque actualisation, montrée au hook et à la section 4). Ta fin n'est pas personnelle : c'est l'usage hybride, écrit à la section 5.

Plus de question ouverte. Prochaine étape : le grill sur la fin (voir `etapes.md`).
