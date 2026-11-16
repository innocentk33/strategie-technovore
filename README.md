# Technovore : planification et suivi

Planification et suivi de la chaîne YouTube Technovore : stratégie, calendrier, un dossier par vidéo, idées en réserve et idées abandonnées.

## Organisation

| Emplacement | Contenu |
|---|---|
| [`strategie.md`](strategie.md) | Stratégie v4 : positionnement, piliers, vidéos d'inspiration, objectifs à 1, 3 et 6 mois, idées classées |
| [`calendrier.md`](calendrier.md) | 2 vidéos IA par semaine (lundi et jeudi, 18 h) jusqu'au 28 janvier, puis une le lundi, jusqu'au 26 avril 2027 |
| [`idees.md`](idees.md) | Boîte à idées : sujets en réserve, pas encore planifiés |
| [`projets/`](projets/) | Un dossier par vidéo |
| [`etudes/`](etudes/) | Études de chaînes concurrentes (données vidIQ), audits de la chaîne (le dernier : [11/11](etudes/audit-2026-11-11.md), rétention de « 16 Go ») et [`radar.md`](etudes/radar.md), le journal du radar fait à chaque sortie |
| [`ressources/`](ressources/) | Ce qui sert à plusieurs vidéos : animations Remotion, miniatures, audio, voix, et [la régie](ressources/regie/PRODUCT.md) (lecteur des `.md` et suivi des vidéos : `node ressources/regie/regie.mjs`) |
| [`archive/`](archive/) | Projets et idées abandonnés, avec la raison |
| `claude-youtube/` | Copie locale du skill `/youtube`, non suivie par git. Le skill utilisé est celui de `~/.claude/skills/` (installation : `git clone https://github.com/AgriciDaniel/claude-youtube && ./claude-youtube/install.sh`) |

## Suivi des projets

| Projet | Format | Publication | Statut |
|---|---|---|---|
| [ArtCraft](projets/artcraft/fiche.md) | Longue | lun. 19 oct., 18 h | **Publié** : [*Il a cloné TOUTES les applications ADOBE et c'est gratuit*](https://www.youtube.com/watch?v=FVFb4dnUmLA) |
| [OpenCode piraté](projets/opencode/fiche.md) | Longue (actu) | mer. 21 oct., 13 h | **Publié** : [*OpenCode a été gravement piraté (explication !)*](https://www.youtube.com/watch?v=LeZ9hgwvXy0) |
| [Uber](projets/uber/fiche.md) | Longue | lun. 26 oct., 18 h | **Publié** (03/11) (lun. 26 oct., 18 h) : titre et tags corrigés (vérifié dans vidIQ le 22/10) ; nouveau titre *La carte d'Uber est une illusion (et c'est génial)* et test à 3 miniatures (26/10) ; [kit d'upload](projets/uber/upload.md) |
| [Pourquoi avoir ta propre IA, et comment l'installer (LM Studio)](projets/installer-ia-locale/fiche.md) | Longue (testé, vulgarisation) | lun. 2 nov., 18 h | **Publié** (03/11, V3 calée sur ta capture du 24/10) : [final](projets/installer-ia-locale/script.md), grills [V1](projets/installer-ia-locale/grill-v1.md) et [V3](projets/installer-ia-locale/grill-v3.md), [sources](projets/installer-ia-locale/sources.md) vérifiées deux fois, [téléprompteur](projets/installer-ia-locale/teleprompteur.md) (V2, complet), [étapes jusqu'à la sortie](projets/installer-ia-locale/etapes.md) ; capture faite (24/10) ; ta voix, 3 miniatures et kit d'upload à faire ; nouvelle, ta demande du 24/10 (la base d'abord) |
| [16 Go de VRAM suffisent (si tu prends le bon fichier)](projets/claude-ou-mon-pc-1/fiche.md) | Longue (calculé) | lun. 9 nov., 18 h | **Publié** (09/11, 17 h) : [*16 Go de VRAM suffisent*](https://www.youtube.com/watch?v=jMZFDNbwRNI) ; montage fini le 09/11 : [kit d'upload](projets/claude-ou-mon-pc-1/upload.md) (09/11 : description, chapitres, tags, sous-titres FR et EN ; remplace les tags Flutter) · [final](projets/claude-ou-mon-pc-1/script.md), [téléprompteur](projets/claude-ou-mon-pc-1/teleprompteur.md), [grill V3](projets/claude-ou-mon-pc-1/grill-v3.md), [sources](projets/claude-ou-mon-pc-1/sources.md) |
| [Qwen 4 : quelle carte graphique acheter (ou pas) ?](projets/qwen-4-cartes/fiche.md) | Longue (calculé, actu) | jeu. 12 nov., 21 h 45 | **Publié** (12/11, 21 h 45) : [*Qwen 4 quelle carte graphique acheter (ou pas) ?*](https://www.youtube.com/watch?v=JuiZAwEiX-o) · rendu 4K (8:41), [kit d'upload](projets/qwen-4-cartes/upload.md), sous-titres FR et EN, miniatures : test A/B a contre a-peak, plus la variante c « mains » (12/11) · radar du 12/11 dans [`etudes/radar.md`](etudes/radar.md) |
| [Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé)](projets/strata-test/fiche.md) | Longue (testé) | lun. 16 nov., 18 h | **Publié** (16/11) : [Voir sur YouTube](https://www.youtube.com/watch?v=892vB0mRY8U) ; rendu final v9 en 4K (9 min 35 s, `HyperStudio/premium-noir/2026-11-strata-test/renders/strata-montage-v9-4k.mp4`), kit d'upload et sous-titres FR/EN prêts |
| [Même carte, 2 fois plus rapide](projets/meme-carte-plus-rapide/fiche.md) | Longue (calculé) | jeu. 19 nov., 18 h | **Script** (15/11) : [V2](projets/meme-carte-plus-rapide/script.md) après [grill](projets/meme-carte-plus-rapide/grill-v1.md) (6,5 → 8/10), [téléprompteur](projets/meme-carte-plus-rapide/teleprompteur.txt), [sources](projets/meme-carte-plus-rapide/sources.md) vérifiées deux fois (M1-M38) ; 4 crochets et 5 questions à toi ; idée 16 |
| [Qwen 27B sur 8 Go : plus rapide, mais à quel prix ?](projets/qwen-27b-8go/fiche.md) | Longue (calculé, actu) | lun. 23 nov., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Carte graphique pour l’IA locale : combien coûte la mémoire dont tu as besoin ?](projets/carte-par-budget/fiche.md) | Longue (calculé) | jeu. 26 nov., 18 h | **Script** + téléprompteur (16/11), double lecture et roast appliqué ; offres datées, classement exhaustif non établi |
| [32 Go pour Qwen 27B : les prix, les routes et leurs pièges](projets/deux-cartes-occasion/fiche.md) | Longue (calculé, sans achat) | lun. 30 nov., 18 h | **Script** + téléprompteur (16/11), double lecture et roast appliqué ; offres datées, classement exhaustif non établi |
| [DeepSeek V4 Flash sans carte graphique : les 64 Go valent-ils leur coût ?](projets/cout-deepseek-flash/fiche.md) | Longue (calculé, actu) | jeu. 3 déc., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Deux cartes pour ton IA : les points à vérifier avant l’achat](projets/multi-gpu/fiche.md) | Longue (calculé) | lun. 7 déc., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Mac mini ou PC gamer : quand les 32 Go justifient l’achat](projets/mac-mini-ia/fiche.md) | Longue (calculé) | jeu. 10 déc., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Combien coûte Claude Fable 5.2 chez toi ?](projets/cout-claude-local/fiche.md) | Longue (calculé, actu) | lun. 14 déc., 18 h | **Script** : [v2](projets/cout-claude-local/script.md) à refaire en v3 (fusion avec Kimi le 15/11, modèle de calcul d'environ 1 To, inspirée de [Pop Theory](https://www.youtube.com/watch?v=yw5mMVq6gas)) ; [grill](projets/cout-claude-local/grill-v1.md) du 22/10 |
| [Deux cartes suivies avant et après le Black Friday : la remise a-t-elle tenu ?](projets/prix-apres-black-friday/fiche.md) | Longue (calculé) | jeu. 17 déc., 18 h | **Brouillon** · préparation corrigée + téléprompteur ; prix BlackFriday/décembre futurs, résultat et validation finale ouverts |
| [IA en local : comment lire le nom d'un modèle](projets/bases-ia-locale/fiche.md) | Longue (calculé, vulgarisation) | lun. 21 déc., 18 h | **Script** (23/10) : [final](projets/bases-ia-locale/script.md), [grill](projets/bases-ia-locale/grill-v1.md), [sources](projets/bases-ia-locale/sources.md) vérifiées deux fois ; tes crochets à remplir (sans essai depuis le 25/10 : prends les replis écrits) ; miniature et kit d'upload à faire ; renvois vers la vidéo d'installation à reprendre ; passée du 2 nov. au 7 déc. le 24/10 (la base d'abord) |
| [Offrir une IA locale : trois budgets, avec leurs limites](projets/cadeau-ia-locale/fiche.md) | Longue (calculé) | jeu. 24 déc., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Louer, acheter ou s'abonner ?](projets/louer-acheter-ia/fiche.md) | Longue (calculé) | lun. 28 déc., 18 h | **Script** (23/10) : [final](projets/louer-acheter-ia/script.md), [grill](projets/louer-acheter-ia/grill-v1.md), [sources](projets/louer-acheter-ia/sources.md) vérifiées deux fois ; tes crochets à remplir ; prix à relever le 2/01, ⟦résultat de Claude #1⟧ (calculé) |
| [RAM, VRAM ou mémoire unifiée : laquelle aide vraiment ton IA ?](projets/ram-vram-unifiee/fiche.md) | Longue (calculé) | jeu. 31 déc., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Claude Code avec une IA locale : connexion, mémoire et tâches réalistes](projets/claude-code-gratuit/fiche.md) | Longue (calculé) | jeu. 7 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Ton IA locale est-elle vraiment privée ?](projets/ia-locale-privee/fiche.md) | Longue (calculé) | lun. 11 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Créer un petit jeu avec une IA locale : ce que montrent 16 Go](projets/jeu-video-ia-locale/fiche.md) | Longue (calculé) | jeu. 14 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [De 4 à 16 Go : un modèle utile pour la carte que tu as déjà](projets/modele-par-vram/fiche.md) | Longue (calculé) | lun. 18 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [54 Go pour 35 dollars : à qui cette récupération peut-elle servir ?](projets/cartes-minage/fiche.md) | Longue (calculé) | jeu. 21 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Ollama, LM Studio ou llama.cpp : lequel choisir pour ton usage ?](projets/choisir-moteur/fiche.md) | Longue (calculé) | lun. 25 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |
| [Un petit modèle peut-il remplacer ton IA du cloud ?](projets/petits-modeles-experts/fiche.md) | Longue (calculé) | jeu. 28 janv., 18 h | **Script** + téléprompteur (16/11), sources doublement vérifiées et roast indépendant appliqué |

**Statuts** : Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié (ajouter le lien YouTube).
Les créneaux sans projet (un lundi sur deux à partir du 1er mars) sont des vidéos IA choisies par le radar : voir [`calendrier.md`](calendrier.md) et la banque du radar IA dans [`etudes/calendrier-vidiq-2026-10-23.md`](etudes/calendrier-vidiq-2026-10-23.md).

## Un dossier projet

```
projets/<nom>/
├── fiche.md        titres, miniature, contenu, points à vérifier
├── brouillon*.md   premiers jets, notes en vrac
├── script.md       script final
└── sources.md      si la recherche déborde de la fiche
```

Les rushs, exports et prises de voix restent hors de git (voir `.gitignore`).

## Cycle de vie

1. **Nouvelle idée** : une ligne dans [`idees.md`](idees.md).
2. **Idée retenue** : créer `projets/<nom>/fiche.md` (partir d'une fiche existante), puis l'ajouter au tableau ci-dessus et au [calendrier](calendrier.md).
3. **Publiée** : statut « Publié » et lien YouTube. Le dossier reste dans `projets/`.
4. **Abandonnée** : déplacer le dossier dans `archive/` (`git mv`), et noter la date et la raison dans [`archive/README.md`](archive/README.md).
