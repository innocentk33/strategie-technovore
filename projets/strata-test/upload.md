# Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) : kit d'upload YouTube

> **Publiée le 16/11/2026 :** [Voir sur YouTube](https://www.youtube.com/watch?v=892vB0mRY8U)

> **Vidéo** : `/Users/innocent/HyperStudio/premium-noir/2026-11-strata-test/renders/strata-montage-v9-4k.mp4`, rendue le 15/11 : 3840×2160, 30 i/s, 575,1 s (9:35). Les temps viennent de la voix finale (`sources/voix.words.json`, la voix démarre à 0 : temps de la voix = temps de la vidéo).
> **Sortie** : **lun. 16 nov. 2026, 18 h** ([`calendrier.md`](../../calendrier.md), ligne 1). Faits : [`sources.md`](sources.md) (T1 à T47).
> **vidIQ, 15/11 : 0 crédit dépensé.** `vidiq_keyword_research`, `vidiq_outliers` et `vidiq_youtube_search` ne sont pas chargés dans cette session (ToolSearch ne les trouve pas). Les volumes ci-dessous sont repris des kits voisins, datés ; les vidéos hôtes viennent de la page de résultats de YouTube (curl, 15/11), pas de vidIQ.

## Mots-clés (relevés vidIQ des 23, 24 et 26/10 : aucun n'est refait)

| Mot-clé | Recherches/mois | Concurrence | Usage |
|---|---|---|---|
| **strata** | **non mesuré** (outil absent le 15/11) | — | Titre, description, tags : le nom du projet |
| **qwen 3.8 flash next** | **non mesuré** | — | Première ligne de la description, tags |
| qwen | 179 672 (8 045 en France), vidIQ 23/10 | 48,3 | Description, tags |
| ia en local | 21 403, vidIQ 23/10 ; 15 204, vidIQ 26/10 | 41,6 / 42 | Hashtag, tags : le mot-clé du pilier |
| ia local | 111 094 (8 546 en France), vidIQ 26/10 | 58 | Tags |
| ia locale | 9 059, vidIQ 26/10 | 53 | Tags |
| local llm | 87 763, vidIQ 24/10 | 52 | Tags |
| local ai | 278 076 (10 112 en France), vidIQ 24/10 | 70 | Non utilisé (trop large) |
| vram | 15 336, vidIQ 24/10 | 69 | Titre (« 16 Go de VRAM »), tags |
| lm studio | 247 028 (5 146 en France), vidIQ 26/10 | 59 | Lien vers ta vidéo LM Studio seulement |

**Lecture** : « 16 Go de VRAM » est la forme que le public tape et voit (vidéos de 59 K et 64 K vues ce mois-ci avec « 4 Go à 16 Go de VRAM », relevé YouTube du 15/11). « Strata » et « Flash-Next » sont des mots neufs, non mesurés : ils restent dans la description et les tags, pas en tête du titre.

## Titres

| | Titre | Car. | Ce que la vidéo tient |
|---|---|---|---|
| **A · Calendrier (recommandé)** | Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé) | 62 | « Testé » : oui, filmé chez toi. « Le meilleur possible » : la voix ne le dit pas mot pour mot, mais elle dit qu'avec 32 Go de RAM la doc ne propose que le Coder (4:22) ; c'est le seul fichier de Flash-Next prévu pour 32 Go et une carte de 12 à 16 Go (T5). Les 32 Go de RAM sont dans la première ligne de la description |
| B · Résultat | Qwen 3.8 Flash-Next sur 16 Go de VRAM : il a codé un mini-Minecraft | 68 | Oui (1:25 à 1:42), avec 3 relances, dites dans la vidéo |
| C · Précis | 16 Go de VRAM, 32 Go de RAM : le meilleur modèle de code possible | 64 | Oui (« de code » : le Coder, plus faible hors du code, 2:11) ; titre 2 de `miniature/propositions.md` |

- **Publie avec A seul**, pour les trois miniatures : le test A/B décidé le 15/11 (h, i, j) ne doit tester que l'image.
- A et la miniature ne se répètent pas : le titre dit la config, l'image pose la question (« TON PC SUFFIT ? », Qwen contre Claude), à laquelle la vidéo répond à 8:13.
- Écarté : « 125 milliards sur 16 Go » (interdit pour le Coder, `sources.md`), « 16 Go suffisent » (faux sans les 32 Go de RAM), « un seul prompt » (pas tenu pour le site et le mini-Minecraft).

## Description

```
Qwen 3.8 Flash-Next (sa version Coder) tourne avec Strata sur une carte de 16 Go et 32 Go de RAM, à près de 70 tokens par seconde en moyenne. Il m'a codé une île en 3D, un casse-briques, un site d'agence de voyage et un mini-Minecraft.

Testé sur ma RTX 5080 (le haut de la fourchette pour 16 Go), avec l'agent Pi, sans jamais toucher au code : les résultats, la vitesse, l'installation, mes erreurs pour que tu les évites, et si ça remplace un abonnement à Claude.

CHAPITRES
0:00 16 Go de VRAM, près de 70 tokens/s
0:20 Les résultats : île 3D, casse-briques, site, mini-Minecraft
1:42 Qwen 3.8 Flash-Next et sa version Coder
2:33 Comment un si gros modèle tient sur 16 Go
2:59 La vitesse, et sur ta carte
4:17 Installer Strata avec 32 Go de RAM
4:51 Brancher Pi et la limite de réponse
5:19 Erreur 1 : 32 000 tokens, pas assez
5:32 Le site raté, puis le plan de Claude
6:27 Mini-Minecraft : « écrit et vérifié »… sans fichier
7:03 Et Claude ?
7:24 Les bugs chez les autres
8:13 Verdict : ça remplace l'abonnement ?
8:37 La liste pour le refaire ce soir

LES PROMPTS (tapés tels quels dans Pi ; une relance = « continue » ou une phrase courte)
Vitesse : Tell me a short story about a dragon who loves video games.

Île 3D (aucune relance) :
Create a 3D voxel island in one file, index.html, using three.js r128 loaded with a classic script tag from exactly this URL: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js (no ES modules, no OrbitControls, no other library).
1. A procedural island from your own noise function: at least 48x48 columns of cubes drawn with THREE.InstancedMesh, colored by height (sand, grass, rock, snow).
2. A semi-transparent blue water plane around the island.
3. At least 15 trees made of cubes (trunk and leaves), only on grass.
4. Drag the mouse to orbit around the island and use the wheel to zoom (write this yourself); when the mouse is idle, the island turns slowly.
5. A sun with shadows, a sky-blue background, and the N key switches between day and night.
It must render as soon as I open index.html, with no errors in the console. Write the whole file in one go.

Casse-briques (aucune relance) :
Create a complete Breakout game in one file, index.html. No libraries, no external files: all HTML, CSS and JavaScript inline. 800x600 canvas, dark background, neon colors.
1. 6 rows of colored bricks, a paddle moved with the mouse or the left/right arrow keys, and a ball that bounces off the walls, the paddle and the bricks.
2. A score, 3 lives, and a game over screen and a win screen that both say "Press SPACE to restart".
3. Some bricks drop a power-up when destroyed: either a wider paddle or 3 balls at once.
4. Short sound effects made with the Web Audio API, and small particles when a brick breaks.
5. It must run as soon as I open index.html, with no errors in the console.
Write the whole file in one go, then give me a two-line summary.

Le mini-Minecraft (3 relances), le site essai 1, le fichier de Pi et les crédits des photos : LIEN_DU_GIST
Le site final (Sillage) : une consigne courte, et Pi a suivi un plan de 770 lignes écrit par Claude Opus 5.5.

PRÉCISIONS
« Un seul prompt » : vrai pour l'île et le casse-briques ; 3 relances pour le mini-Minecraft, 2 pour le site final.
« Mes photos » : 12 photos de Wikimedia Commons (CC BY-SA) que j'ai choisies ; crédits dans le lien plus haut.
Le plan de Claude contenait les 228 textes du site et un tiers des lignes de la page. L'installation a pris un peu plus d'une demi-heure.

LIENS
Strata : https://github.com/Niko1221/Strata
Qwen 3.8 Flash-Next : https://huggingface.co/Qwen/Qwen3.8-Flash-Next
La version Coder : https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-Coder-GGUF
Pi : https://github.com/earendil-works/pi
Ta première IA en local (LM Studio) : https://www.youtube.com/watch?v=9hr_zaJuUbM
16 Go de VRAM, le bon fichier : https://www.youtube.com/watch?v=jMZFDNbwRNI

MUSIQUES : « Future Minimal » par kissan4 et « Dark Ambient for Crime and Tension » par megalix (Pixabay).

Ta carte, ta RAM, et ce que tu veux que je lui fasse coder : dis-le en commentaire.
Sur Technovore, j'ouvre le capot de l'IA que tu utilises. Si ce test t'a fait gagner une soirée, abonne-toi : c'est le seul abonnement qui ne te prélèvera jamais rien.
Jeudi 19/11 : même carte, 2 fois plus rapide.

#IAenLocal #Strata #Qwen
```

- **Taille : 4 349 caractères sur 5 000** (compté par script le 15/11, `LIEN_DU_GIST` compris ; ≈ 4 407 avec un vrai lien de gist). Corps hors chapitres, prompts et liens : 1 279 caractères, PRÉCISIONS comprises.
- **⚠️ `LIEN_DU_GIST` est à remplacer avant de coller.** Les quatre prompts font à eux seuls 4 300 caractères : avec le reste, la description passait à 5 400. J'ai gardé dans la description les trois plus courts (vitesse, île, casse-briques) et mis le reste dans un gist, que tu crées toi-même (rien n'a été mis en ligne) : contenu prêt plus bas. **Le gist n'est pas facultatif** : la voix dit « tous les fichiers sont en description » (5:17) et « le fichier est en description » (9:08), donc le `models.json` de Pi doit être accessible depuis la description. Si tu préfères ne rien héberger ailleurs, colle ce contenu dans un commentaire épinglé (10 000 caractères max) et écris « dans le commentaire épinglé » à la place du lien.
- **Prompts vérifiés** : casse-briques vu à l'écran (`Strata config avec pi.mp4`, 4:48, identique mot pour mot), mini-Minecraft vu à l'écran (`test 3 pi qwen.mp4`, 0:02, identique sauf quelques mots cachés par la souris). Île : historique git du plan et T41, pas vu à l'écran. Site essai 1 : section 6.2 du plan et T41, pas vu à l'écran. Sillage : `test voyage debut.mp4` montre une consigne courte (avec un chemin `D:\…`) et `AGENTS.md` chargé en contexte : je ne la recopie pas (chemin, et le vrai travail est dans le plan).
- **PRÉCISIONS** corrige ce que la voix dit de travers : « à partir d'un seul prompt » (0:06 ; Sillage a eu 2 relances, le mini-Minecraft 3, T41), « mes propres photos » (1:08 et 7:13 ; Wikimedia Commons, CC BY-SA, plan-tests 6.2), « quelques lignes de la page étaient dans le plan » (6:13 ; 228 textes et 36 % des lignes, T42 : `sources.md` interdit de minimiser le plan) et « un peu moins d'une demi-heure » (4:28 ; 19 h 30 → 20 h 06, T45). **Pas corrigé** faute de place : « près de 2 heures » perdues sur Chrome (6:39 ; 2 h 22 au total, T41) et « entre 200 mégas par seconde » (4:45 ; 165 à 239 Mo/s, T45).
- **Aucune chaîne nommée** ; pas de chemin de dossier ; la seule « clé » est la valeur factice `strata-local` du gist.
- Chiffres de la description : près de 70 tok/s en moyenne (T45), 16 Go + 32 Go (T5), 770 lignes et Claude Opus 5.5 (T42), 3 et 2 relances (T41), 228 textes et un tiers des lignes (T42).
- La voix ne dit plus « jeudi, on cherche comment aller plus vite » (phrase coupée au montage) : la dernière ligne annonce la vidéo du **jeu. 19/11** (*Même carte, 2 fois plus rapide*, `calendrier.md`), sans lien.
- Musiques : `style/media.json` (kissan4, megalix, Pixabay) ; `index.html` du montage utilise bien `music-minimal` et `music-tension`.

### Chapitres : vérification

| Début | Titre | Ce qui l'ouvre dans la voix | Vérification (`voix.words.json`) |
|---|---|---|---|
| 0:00 | 16 Go de VRAM, près de 70 tokens/s | « Ces tests ont été réalisés » | 0,11 s |
| 0:20 | Les résultats : île 3D, casse-briques, site, mini-Minecraft | « D'abord les résultats » | 20,34 s (« temps » finit à 19,88) |
| 1:42 | Qwen 3.8 Flash-Next et sa version Coder | « Pour comprendre ces résultats » | 102,62 s (« minutes » finit à 102,19) |
| 2:33 | Comment un si gros modèle tient sur 16 Go | « En fait, le modèle est découpé » | 152,85 s ; le montage dit 2:32, qui tombe dans « comment il tient » |
| 2:59 | La vitesse, et sur ta carte | « Maintenant, concernant la vitesse » | 179,06 s ; le montage dit 2:58, qui tombe dans « open source » |
| 4:17 | Installer Strata avec 32 Go de RAM | « Pour l'installer » | 257,41 s |
| 4:51 | Brancher Pi et la limite de réponse | « Ensuite, je branche Pi » | 291,24 s, **ajouté** |
| 5:19 | Erreur 1 : 32 000 tokens, pas assez | « Et justement, voilà ma première erreur » | 319,02 s ; le montage dit 5:18, qui tombe dans « description » |
| 5:32 | Le site raté, puis le plan de Claude | « Le site, lui, ne s'est pas fait du premier coup » | 332,10 s, **ajouté** |
| 6:27 | Mini-Minecraft : « écrit et vérifié »… sans fichier | « Pour le mini-Minecraft » | 387,28 s (« destination » finit à 387,05), **ajouté** |
| 7:03 | Et Claude ? | « Bon, et Claude dans tout ça » | 423,21 s |
| 7:24 | Les bugs chez les autres | « Chez moi, le moteur n'a jamais planté » | 444,69 s ; à 7:24, on entend encore la fin de « détaillée » (444,29) : 0,3 s, acceptable (7:25 tomberait dans « moteur ») |
| 8:13 | Verdict : ça remplace l'abonnement ? | « Alors, est-ce que ça remplace mon abonnement » | 493,38 s |
| 8:37 | La liste pour le refaire ce soir | « Et si tu veux le refaire ce soir » | 517,20 s, **ajouté** ; le chapitre « À la prochaine » (9:22) est retiré : il ne cherche rien |

14 chapitres, premier à 0:00, le plus court fait 13 s (5:19 → 5:32) : les trois règles de YouTube sont tenues.

### Contenu du gist (à créer par toi, puis lien dans la description)

```
# Technovore : Qwen 3.8 Flash-Next (Coder) sur 16 Go de VRAM avec Strata et Pi

Strata 0.2.13, modèle coder-iq1_m (contexte 128K), Pi 1.5.2, réflexion « high ». Prompts tapés tels quels dans Pi. Relance = « continue » ou une phrase courte.

## Mini-Minecraft (3 relances)

Create a small playable Minecraft-style voxel game in one file, index.html, using three.js r128 loaded with a classic script tag from exactly this URL: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js (no ES modules, no PointerLockControls, no other library, no image files).
1. A 64x64 world, 32 blocks high, from your own noise function: hills, a lake at sea level with sand around it, grass on top of dirt, stone below, and at least 10 trees.
2. Minecraft-style pixel textures drawn in code on 16x16 canvases (grass top and side, dirt, stone, sand, wood, leaves), with NearestFilter so they stay crisp. Semi-transparent blue water.
3. First-person controls: click to lock the mouse, mouse look, WASD, space to jump, gravity, and collision so I cannot walk through blocks.
4. A crosshair; left click breaks the block I look at, right click places the block chosen with keys 1 to 5, shown in a hotbar at the bottom of the screen.
5. One mesh per 16x16 chunk with only the visible faces, rebuilt when a block changes, so it stays smooth. Sky-blue background with fog.
It must run as soon as I open index.html, with no errors in the console. Write the whole file in one go.

## Site d'agence de voyage, essai 1 (texte rendu en anglais malgré la consigne)

Create a stunning, premium website for a fictional travel agency called "Sanaka Voyages" that sells trips across Africa and the Indian Ocean. One file, index.html, all CSS and JavaScript inline, no libraries. All visible text in French. Use the real photos in the images/ folder: list it first. You cannot see them, but each file name says what it shows.
1. A full-screen hero with a photo slowly zooming in the background, a big headline, and a search bar (destination, date, travellers).
2. At least 6 destination cards with a photo, the place, the trip length and a price; the photo zooms when the mouse is over the card.
3. A full-width photo band with a parallax effect, then 3 traveller testimonials in a slider that moves on its own.
4. A photo gallery: clicking a photo opens it full screen with previous/next arrows, and Escape closes it.
5. A header that stays on top and becomes solid when I scroll, sections that fade in as they appear, and it must look right on a phone (375 px wide) and on a desktop, with no errors in the console.
Write the whole file in one go.

## Site final (Sillage)

Pas de long prompt : une consigne courte, et Pi a suivi AGENTS.md, un plan de 770 lignes écrit par Claude Opus 5.5 (étapes, textes français dans i18n.js, contrôle après chaque étape).

## Le fichier de Pi : ~/.pi/agent/models.json

L'adresse et le Model ID viennent de la page Serving de l'appli Strata. apiKey : une valeur factice, l'appli n'en demande pas. maxTokens : j'avais mis 32000, et une réponse a été coupée : monte plus haut (je n'ai pas vérifié jusqu'où Strata accepte).

{
  "$schema": "https://pi.dev/schemas/models.schema.json",
  "providers": {
    "strata": {
      "baseUrl": "http://127.0.0.1:47831/v1",
      "api": "openai-completions",
      "apiKey": "strata-local",
      "compat": { "supportsDeveloperRole": false, "supportsReasoningEffort": false },
      "models": [
        {
          "id": "coder-iq1_m",
          "name": "Qwen3.8-Flash-Next Coder IQ1_M (Strata, local)",
          "reasoning": true,
          "input": ["text"],
          "contextWindow": 131072,
          "maxTokens": 32000,
          "cost": { "input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0 }
        }
      ]
    }
  }
}

## Crédits des photos (Wikimedia Commons, CC BY-SA)

[À COLLER : le contenu de credits.txt, auteur, licence et lien pour chacune des 12 photos]
```

## Tags

```
strata, strata coder, qwen 3.8 flash next, qwen3.8 flash next, flash next, qwen coder, 16 go vram, 16gb vram, 32 go ram, ia en local, ia locale, ia local, llm local, local llm, pi coding agent, agent de code, rtx 5080, rtx 5060 ti, qwen 4, minecraft ia, technovore
```

**264 caractères sur 500.**

## Suggestions

Le pourquoi est dans [`etudes/suggestions-2026-10-23.md`](../../etudes/suggestions-2026-10-23.md). **vidIQ indisponible** (outils de recherche absents) : recherches YouTube « ia en local 16 go vram », « qwen 3.8 flash next » et « strata qwen flash next », filtre « ce mois-ci », par curl le **15/11/2026** ; titres d'origine et pistes audio lus sur la page de chaque vidéo. Pas un recensement complet.

### Les vidéos hôtes

| # | Vidéo | Chaîne | Langue | Vues (15/11) | Sortie |
|---|---|---|---|---|---|
| 1 | *192 Go de VRAM : NVIDIA a un ÉNORME PROBLÈME !* (`1TRRE7_R8KQ`) | Makertronic Tech | Français (piste anglaise en plus) | 25 652 | 08/11 |
| 2 | *Les géants de l'IA veulent votre RAM : ce qu'un vieux PC fait VRAIMENT tourner (Qwen, RTX 5060 Ti)* (`9IRXDZpU1mQ`) | Build & Mind | Français | 6 553 | 10/11 |
| 3 | *Mon IA locale va 11 fois plus vite (même PC)* (`VFC16Tb3lwU`) | Nathan Inline | Français | 9 056 | 14/11 |
| 4 | *Qwen 3.8 27B or Flash Next on Strata? Which one your GPU should run..* (`d79k2cEPKuw`) | KernelBrief | Anglais, piste française doublée | 8 024 | 10/11 |
| 5 | *What's the Best AI Model Your GPU Can Actually Run? 4GB to 16GB VRam* (`tek-IY9BRWc`) | Codacus | Anglais, piste française doublée | 59 266 | 02/11 |

**Les mots qu'on partage, et ce qu'on ne prend pas** :
1. Makertronic : « VRAM ». Pas le scandale NVIDIA.
2. Build & Mind : « Qwen », « faire tourner ». Pas « vieux PC » ni le matériel déjà là.
3. Nathan Inline : « IA locale », la même carte (16 Go, 177B à l'image). **Son angle « 11 fois plus vite, même PC » est celui de ta vidéo de jeudi** (*Même carte, 2 fois plus rapide*) : à regarder avant de la finir, pour ne pas sortir une copie.
4. KernelBrief : « Flash Next », « Strata », « GPU » : le sujet exact, en piste doublée. Pas « Buy RAM first ».
5. Codacus : « meilleur modèle », « 16 Go de VRAM » : c'est le mot du titre A. Pas le classement de 4 à 16 Go (c'est ta vidéo du 18 janv.).

À surveiller hors planche : *16GB VRAM (+RAM): Local AI Coding Setup* (Unbiased Bob, 38 301 vues, 28/10, piste française) : notre config, mais sortie en octobre.

### La planche

Les cinq miniatures sont dans [`miniature/hotes/`](miniature/hotes/) (1280×720). `planches.py` a tourné sur des copies renommées (`strata-test-h.png`, `-i`, `-j`) pour ne pas écraser d'autres planches : [`suggestions-strata-test-h.png`](../../ressources/miniatures/planches/suggestions-strata-test-h.png), [`-i`](../../ressources/miniatures/planches/suggestions-strata-test-i.png), [`-j`](../../ressources/miniatures/planches/suggestions-strata-test-j.png). Ordre : Makertronic, Build & Mind, **la nôtre**, Nathan Inline, KernelBrief, Codacus.

### La comparaison à 168 px

- **Elle se repère** : c'est la seule à fond sombre et uni avec une question (« TON PC SUFFIT ? ») ; les voisines crient (cadre jaune, orange, « BUY RAM FIRST. »), et deux montrent des cartes ou de la RAM en gros.
- **h** : le jaune du mot « SUFFIT ? » rejoint le jaune de Makertronic et de KernelBrief, juste au-dessus et en dessous. **j** : le menthe n'existe nulle part ailleurs dans la colonne, et le visage la distingue de i. **i** (sans visage) est la plus discrète : la carte et les tuiles deviennent petites.
- **Elle promet autre chose** : un duel (Qwen contre Claude) et un doute, là où les autres promettent un chiffre (192 Go, 11 fois, 4 à 16 Go) ou un conseil d'achat. Seule Nathan Inline montre aussi des tokens/s et « 16GB ».
- **Retouche avant de publier** : aucune. Le test h, i, j tranchera ; mon pari est j.

### L'enchaînement

- **Écran de fin, de 9:24 à 9:35** (les 11 dernières secondes ; la voix dit « commence plutôt par la vidéo sur LM Studio, je te la mets juste là » à 9:17, puis « à la prochaine » à 9:22) : à gauche, la vidéo LM Studio ([`9hr_zaJuUbM`](https://www.youtube.com/watch?v=9hr_zaJuUbM), miniature « aucune connexion, ET IL PARLE. ») ; à droite, la vidéo suivante (*Même carte, 2 fois plus rapide*, miniature « Ta carte bridée ? ») : **à ajouter le jeu. 19/11**, à sa sortie ; d'ici là, mets la vidéo 16 Go (`jMZFDNbwRNI`). YouTube demande au moins 5 s pour un écran de fin : 11 s, c'est bon.
- **Fiche pendant le plateau de rétention** : vers **4:51** (« ensuite je branche Pi »), vers la vidéo 16 Go (`jMZFDNbwRNI`), que la voix cite à 2:27 (« lundi dernier je te disais… »). Plateau inconnu : recale-la sur la courbe au radar du 19/11. Une seconde fiche possible à 1:51 (« le modèle dont je te parlais jeudi dernier ») vers la vidéo Qwen 4 (`JuiZAwEiX-o`).
- **Renvois** : dans la vidéo Qwen 4 (`JuiZAwEiX-o`), la fiche 3 (8:06) et l'écran de fin passent à cette vidéo le 16/11 (checklist de son kit).

## À vérifier avant l'upload

- **Crédits des photos** : `credits.txt` n'existe que sur ton PC Windows (`D:\strata-demo\_photos`) : colle-le dans le gist. La licence CC BY-SA l'exige pour montrer les photos.
- **Le gist** : crée-le, remplace `LIEN_DU_GIST`, ouvre le lien une fois.
- **« À 48 gigas… à 64 tu les prends toutes »** (9:10) : ce seuil n'est pas dans `sources.md` (seul S8 de `claude-ou-mon-pc-1` donne ≥ 44 à 60 Go). Je ne l'ai pas repris.
- **Sous-titres** : [`strata-test.fr.srt`](strata-test.fr.srt) et [`strata-test.en.srt`](strata-test.en.srt) sont dans le dossier (écrits par un autre agent, je ne les ai pas relus). Dans Studio : « Avec synchronisation », langue de la vidéo en français.
- `calendrier.md` dit encore « montage v6 rendu » : passe la ligne à « Programmé » une fois la vidéo chargée (et le README).
- Après la sortie : skill `radar` (règle du dépôt).
