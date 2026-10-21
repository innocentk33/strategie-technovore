# OpenCode piraté : kit d'upload YouTube

> Vidéo : `~/Downloads/OpenCode Montage Premium 2026-10-21 06.50.mp4` (copie dans `renders/` du projet HyperFrames) : 8:35,9, 3840×2160, 60 i/s, 22,8 Mb/s, 1,48 Go. Chapitres vérifiés sur les débuts de scène du projet (`index.html`), pas sur le script. Faits : [`sources.md`](sources.md).
> Recherche vidIQ et web du 21/10 : aucune vidéo longue en français sur le sujet, seulement des Shorts (IActu 35 vues, Tech Décryptée 12 vues). En anglais : Code Bear 180 K vues, Kai 36 K vues en un jour (1 300 vues/h), David Ondrej 89 K. Toujours **aucun post-mortem d'OpenCode** au 21/10 : le « on ne sait pas » de la vidéo reste vrai.

## Mots-clés (vidIQ, 21/10)

| Mot-clé | Recherches/mois | Concurrence | Usage |
|---|---|---|---|
| opencode | 442 K (14 K en France) | 51 | Titre, en premier mot |
| opencode hack | 21,9 K | 32 | Description, tags |
| opencode breach | 9,1 K | 20 | Tags |
| clé api | 5,1 K | 12 (très faible) | Titre, description |
| api key / openai api key / claude api | 38 K / 15,8 K / 53,6 K | 34 / 24 / 44 | Tags |
| distillation attack | 4,2 K | 36 | Description, tags |
| opencode piraté | < 750 | — | Personne ne le tape encore, mais c'est le seul mot français du sujet |

Le mot « OpenCode » porte la recherche. La forme française (« piraté ») ne pèse rien en volume, mais elle dit au spectateur francophone que la vidéo est pour lui.

## Titres à tester

| | Titre | Car. | Score vidIQ |
|---|---|---|---|
| **A · Mixte (recommandé)** | OpenCode piraté : j'ai lu le code, tes clés API étaient rangées telles quelles | 78 | 83 |
| B · Chiffre | OpenCode piraté : 35 millions de tokens cramés avec des clés volées | 67 | 84 |
| C · Curiosité | Pourquoi payer pour un « ok » ? Le piratage d'OpenCode expliqué | 63 | 84 |

- **Pourquoi A** : la miniature F crie déjà « OPENCODE HACKÉ ». Le titre A ajoute ce qu'aucune autre vidéo ne promet : tu as lu le code. C'est la vraie différence avec Code Bear et Kai, et c'est le cœur du chapitre 3. Sur mobile, on lit « OpenCode piraté : j'ai lu le code, tes clés API… ».
- **B** reprend le hook mot pour mot (0:00), donc le clic tombe pile sur ce qu'il a promis.
- **C** est le plus intrigant, mais « OpenCode » n'arrive qu'au 47e caractère : moins bon en recherche.
- **Les scores vidIQ (77 à 85) sont trop proches pour départager.** C'est le test qui tranchera.
- **Honnêteté vérifiée** :
  - A : « telles quelles » est exact, la clé était insérée telle que collée, sans chiffrement *dans le code*. Ne pas écrire « en clair » : un chiffrement des disques chez l'hébergeur reste possible (`sources.md`).
  - B : ce sont les clés qui ont été volées, pas les tokens. Les tokens ont été cramés avec.
  - C : c'est la question de la vidéo, qui ne lui donne pas de réponse ferme.
- **Écarté** : « 264 $ pour un ok » (faux : le ticket est celui de la clé, pas du « ok ») et « Il a payé pour un « ok » » (ambigu : Max n'a rien payé de son plein gré).

**Le test** : Studio > ta vidéo > « Tester et comparer », avec les titres A, B et C et **la miniature F pour les trois**, pour ne tester qu'une seule chose. Si ta chaîne ne propose que le test des miniatures, publie avec A et lance le test F/G/H de la fiche. Sinon, garde G et H pour un second test après celui des titres.

## Description

```
Le 17 octobre, OpenCode s'est fait pirater : les clés API OpenAI, Anthropic et Google enregistrées dans sa Console ont pu être exposées. Avec celles de Max Weinbach, quelqu'un a cramé 35 millions de tokens en moins d'une journée… et fait dire « ok » à une IA.

Le code de la Console est public, alors je l'ai lu. Dans cette vidéo : la différence entre l'appli OpenCode et la Console (BYOK), la nuit du 17 octobre heure par heure, où tes clés API étaient rangées (une colonne « credentials » en texte), pourquoi on ne peut pas hasher une clé API comme un mot de passe, le piège de l'« ancien système », ce que vaut une clé volée en 2026 (attaque par distillation, revente), et le réglage qui décide de ta facture le jour où ta clé fuit.

Si tu utilises seulement l'appli OpenCode sur ton PC, tu n'es pas concerné : tes clés ne passent pas par leurs serveurs. Au 21 octobre, OpenCode n'a publié ni le point d'entrée du pirate, ni le nombre de clés volées.

CHAPITRES
0:00 35 millions de tokens et un « ok »
0:45 Deux OpenCode : l'appli et la Console
1:33 La nuit du 17 octobre
2:22 Comment tes clés API étaient rangées
3:53 Le piège de l'« ancien système »
4:38 Pourquoi tes clés valent de l'or (distillation)
6:25 Le réglage qui décide de ta facture
7:19 Ta checklist pour ce soir
7:47 La seule clé qu'on ne peut pas te voler

TA CHECKLIST POUR CE SOIR
1. T'as reçu l'e-mail d'OpenCode ? Révoque ta clé chez le fournisseur. La supprimer de la Console ne la désactive pas.
2. Pas d'e-mail, mais une clé Claude dans OpenCode ? Anthropic conseille d'en créer une nouvelle, par prudence.
3. Une clé par outil : si elle fuit, tu sais d'où, et tu ne coupes qu'elle.
4. Une vraie limite de dépenses (une alerte ne bloque rien), et pas de rechargement automatique.
5. Supprime les clés oubliées.

PRÉCISIONS
À l'oral, je dis « 2 h du matin » : l'exposition commence à 00:30 UTC, soit 2 h 30 à Paris. Et c'est Matt Johansen, pas « Johnson ».
« Plus de vingt fois Harry Potter », c'est mon estimation : 35 millions de tokens font environ 26 millions de mots, la saga en fait environ 1,1 million (en anglais). C'est un ordre de grandeur.

SOURCES (vérifiées le 20 octobre 2026)
L'annonce d'OpenCode : https://x.com/opencode/status/2111519637049319818
Dax Raad, « pas OpenCode lui-même » : https://x.com/thdxr/status/2111572618340188393
Max Weinbach, ses factures et la requête « ok » : https://x.com/mweinbach/status/2111518053662064829 et https://x.com/mweinbach/status/2111518091360575677
Matt Johansen : https://x.com/mattjay/status/2111480005435719885
Lydia Hallie (Anthropic), clés révoquées : https://x.com/lydiahallie/status/2111563956666110287
Nathan Lambert : https://x.com/natolambert/status/2111549984373911572
TechCrunch : https://techcrunch.com/2026/10/19/hackers-hit-ai-coding-tool-opencode-running-up-charges-on-users-ai-accounts/
L'ancienne table « provider » : https://github.com/anomalyco/opencode/blob/773d8621d6bcd311067b225d837c917b3e83573e/packages/console/core/src/schema/provider.sql.ts
Le commit du 12 octobre : https://github.com/anomalyco/opencode/commit/b9ca4d21b4f241154081143a6f5bef648f5ccfd0
Anthropic, distillation (février) : https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks
Anthropic, nouvelles défenses (12 octobre) : https://www.anthropic.com/research/distillation-defenses
Anthropic, rapport de septembre sur les clés volées : https://www.anthropic.com/threat-intelligence-report-september-2026
Dax Raad, les 8 000 faux comptes : https://x.com/thdxr/status/2079248759439884453
Limites de dépenses OpenAI : https://developers.openai.com/api/docs/guides/spend-limits
Limites Anthropic : https://platform.claude.com/docs/en/api/rate-limits
Rechargement automatique Anthropic : https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-api-usage
Facturation Gemini : https://ai.google.dev/gemini-api/docs/billing

MUSIQUES
« Intrigue » par Savfk (free-stock-music.com), licence CC BY 4.0 : https://creativecommons.org/licenses/by/4.0/
« Singularity » par MokkaMusic et « Breath of Freedom » par Infraction (inaudio.org)
« A Complicated Profession », « The Fantasy » et « Blue Shirt Guy » par Fuzzeke
« Neverland » (Emotional Dark Orchestral Music)
« Energetic Drum Background » par Epic Music Waves
« Future Minimal » par kissan4 et « Dark Ambient for Crime and Tension » par megalix (Pixabay)
« This is fine » : KC Green, Gunshow.

T'as déjà collé une clé API dans un outil en ligne ? Et elle a un plafond ? Dis-le en commentaire, personne ne juge.

Sur Technovore, j'ouvre le capot des outils que tu utilises tous les jours. Abonne-toi : c'est le seul abonnement qui ne te prélèvera jamais rien.
À voir ensuite : un seul développeur a recréé 7 logiciels Adobe avec Claude.

#OpenCode #ClésAPI #Cybersécurité
```

- **Les deux premières lignes** (avant « … plus ») : « OpenCode » et « clés API » dans les 15 premiers mots, puis le hook.
- **« PRÉCISIONS »** corrige les deux erreurs gardées à l'oral (storyboard, « À vérifier à l'oreille »). Mieux vaut que ce soit toi qui le dises, avant un commentaire.
- **« This is fine »** : le chien est posé dans la Console au plan 23. Le crédit sert aussi si tu publies la miniature G.
- Si tu publies la miniature D (Elliot), ajoute le crédit photo de [`miniature/propositions.md`](miniature/propositions.md).

## Tags

```
opencode piraté, opencode hack, opencode hacked, opencode breach, opencode console, piratage opencode, clé api, clés api volées, api key, sécurité clé api, attaque par distillation, distillation attack, claude code, claude api, openai api key, anthropic, limite de dépenses api, byok, open code, technovore
```

Les tags pèsent très peu : YouTube lit surtout le titre, la description et la voix. Ils servent aux variantes (« open code », « hacked ») et aux mots anglais que tapent les devs.

## Commentaire épinglé

```
T'as déjà collé une clé API dans un outil en ligne ? Et elle a un plafond ? Sois honnête, ici on ne juge personne (moi, c'est zéro clé collée, et après avoir lu ce code, ça va rester comme ça).
```

## Réglages dans YouTube Studio

| Champ | Valeur |
|---|---|
| Miniature | **F** (« OPENCODE HACKÉ » + Anonymous), export de `miniature/photocraft/opencode-f.png`, moins de 2 Mo. **Jamais de vraie clé**, même partielle |
| Playlist | Celle du pilier IA, avec ArtCraft |
| Public | Non, la vidéo n'est pas conçue pour les enfants |
| Restriction d'âge | Non |
| Promotion payée | Non |
| Contenu modifié ou synthétique | Non : ta vraie voix (accélérée à 1,1), du motion design et de vraies captures. Aucune image réaliste générée par IA |
| Chapitres automatiques | Décocher (les tiens sont dans la description) |
| Langue de la vidéo et du titre | Français |
| Sous-titres | Sous-titres > Ajouter une langue > Importer un fichier > « Avec synchronisation » : [`opencode.fr.srt`](opencode.fr.srt) en français, [`opencode.en.srt`](opencode.en.srt) en anglais (173 blocs chacun). Tirés de l'horodatage mot à mot de la voix montée, avec le texte corrigé (Whisper écrivait « Anthropique », « Cloud Code », « DeepSick »…). Le texte suit ce que tu dis, sauf les noms : « Matt Johansen » est écrit juste. Calés sur la vidéo de 8:35,9 : à refaire si tu remontes la voix |
| Licence | Licence YouTube standard, intégration autorisée, publier dans le flux Abonnements |
| Remix Shorts | Autoriser la vidéo et l'audio |
| Catégorie | Science et technologie |
| Commentaires | Activés, modération « Standard » |
| Visibilité | **Programmée : jeudi 22/10/2026, 18:00, fuseau Paris** (fiche), soit 16 h à Abidjan et Dakar, 17 h à Douala et Kinshasa |
| Première | Non |

**Ou ce soir ?** Les 48 premières heures d'ArtCraft se terminent aujourd'hui à 18 h (mer. 21/10). Si l'export est prêt, publier ce soir à 20 h ne gêne plus ArtCraft, et une actu perd de sa valeur chaque jour : la recherche « opencode » baisse déjà (−20 % sur 30 jours). Kai a sorti sa vidéo le 20/10 et fait 1 300 vues/h. Le Short ArtCraft reste au dim. 25/10.

## Écran de fin et fiches

- **Écran de fin : de 8:15,9 à 8:35,9** (20 s, le maximum autorisé).
  - Élément vidéo dans la zone de droite : **la vidéo ArtCraft** (la voix dit « c'est juste ici : un seul développeur a recréé les 7 logiciels d'Adobe »).
  - Bouton « S'abonner » dans le cercle.
- 🟨 **Décalage de 6 s** (vérifié dans `compositions/fin.html`) :
  - les zones réservées apparaissent à **8:09,9** ;
  - la flèche se trace à **8:12,6**, pile sur « c'est juste ici », puis s'efface à **8:16,4** ;
  - YouTube ne peut pas poser l'écran de fin avant **8:15,9** (20 s avant la fin).
  
  Donc la flèche pointe une zone vide pendant 4 s, et disparaît une demi-seconde après l'arrivée de la vidéo. La correction : **couper 6 s de musique à la fin**. Ta dernière phrase finit à 8:20,4, la vidéo finirait à 8:29,9, avec encore 9,5 s de musique. L'écran de fin irait alors de 8:09,9 à 8:29,9. Dans le projet, il suffit de passer `#root` à `data-duration="509.93"`, la scène `fin` à `42.836` et `musique-fin` à `43.09` (fondu final avancé de 6 s), puis de réexporter. Je peux faire la modification si tu veux. Sinon, garde la vidéo telle quelle : l'élément arrive 3 s après la flèche.
- **Fiche 1, à 6:26** (début du chapitre 6, 75 %) : ta vidéo IA la plus vue. Aucune fiche avant : la vidéo répond au « ok » entre 6:00 et 6:25, et une fiche plus tôt offrirait une sortie avant la réponse.
- **Plus tard** : quand le premier épisode de « Claude ou mon PC ? » sortira, ajoute une fiche à **8:06** (« Est-ce que ça peut vraiment remplacer un abonnement Claude ? »).

## À vérifier avant l'upload

- **Les deux erreurs à l'oral** (« 2 h », « Johnson ») : si tu peux réenregistrer « Deux heures trente du matin » et « Matt Johansen », c'est mieux. Sinon, la description les corrige.
- **Le raccord « …et 264 $ »** (0:19), signalé dans le storyboard.
- **L'export est bon** : en 4K, YouTube encode en VP9 ou AV1, même pour ceux qui regardent en 1080p. C'est ce qui protège le mieux le fond noir de la recette « Premium noir ». YouTube conseille plutôt 53 à 68 Mb/s en 4K à 60 i/s (on est à 22,8), mais l'export est en qualité « high » à débit variable : pas besoin de réexporter pour ça. Compte un traitement 4K plus long après l'upload (1,48 Go) : mets la vidéo en ligne quelques heures avant l'heure prévue.
- **Extraits protégés** : Silicon Valley (HBO, 1,1 s), les mèmes. Ils sont très courts, mais si Studio affiche une revendication Content ID dans « Vérifications », remplace l'extrait avant de publier, plutôt que de laisser la monétisation partir.
- **L'image d'Anonymous** (miniature F) : l'origine n'est pas connue. Si elle vient d'Unsplash ou de Pexels, rien à faire ; sinon, retrouve l'auteur.
- **Juste avant de publier** : regarde si OpenCode a sorti un post-mortem. Si oui, change la phrase « Au 21 octobre, OpenCode n'a publié ni… » de la description et épingle un commentaire avec la nouvelle info.

## Checklist

- [ ] Titre A (titres B et C dans « Tester et comparer »)
- [ ] Description collée, chapitres à partir de 0:00
- [ ] Tags collés (moins de 500 caractères)
- [ ] Miniature F
- [ ] Catégorie, langue, public, promotion payée, contenu modifié
- [ ] Sous-titres FR et EN importés
- [ ] Écran de fin vers ArtCraft, fiche 1 à 6:26
- [ ] Vérifications Studio (droits d'auteur) sans revendication
- [ ] Programmée jeu. 22/10 à 18:00 (ou mer. 21/10 à 20:00)
- [ ] Commentaire épinglé, à poster dès la sortie
- [ ] Post-mortem d'OpenCode vérifié le jour J
