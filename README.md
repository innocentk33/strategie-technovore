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
| [Le meilleur modèle possible pour 16 Go de VRAM (Strata, testé)](projets/strata-test/fiche.md) | Longue (testé) | lun. 16 nov., 18 h | **Montage** (15/11) : voix nettoyée et vérifiée (10 min 25 s), montage HyperFrames v6 dans `HyperStudio/premium-noir/2026-11-strata-test/renders/strata-montage-v6.mp4` (5 passes de correction, critique indépendante finale 7,5/10) ; reprises de voix à faire (« un peu moins d'une demi-heure », « près de 2 heures », « quelques lignes », « mais il n'en faut plus qu'un petit ») · avant : **Script** (11/11) : [plan de tests](projets/strata-test/plan-tests.md) (installeur Windows 0.2.13, harnais Pi), [storyboard](projets/strata-test/storyboard.md), [V3](projets/strata-test/script.md) le 14/11 au soir (résultats d'abord, structure à la Red Stapler, plus de pronostic ; [V2](projets/strata-test/script-v2.md) après [grill](projets/strata-test/grill-v1.md), 6 → 7,5/10), [téléprompteur](projets/strata-test/teleprompteur.txt) ; résultats remplis le 14/11 (tests, moniteur, rushes) : **prêt pour la voix** (storyboard à recaler après l'enregistrement) ; captures web faites le 14/11 (sauf la miniature du 19/11) ; miniatures : test A/B [ancien texte contre PEAK](projets/strata-test/miniature/propositions.md) (12/11) |
| [Même carte, 2 fois plus rapide](projets/meme-carte-plus-rapide/fiche.md) | Longue (calculé) | jeu. 19 nov., 18 h | **Fiche** (10/11), idée 16 |
| [32 Go de VRAM pour Qwen 27B, au moins cher (ex-deux cartes d'occasion)](projets/deux-cartes-occasion/fiche.md) | Longue (calculé, sans achat) | lun. 23 nov., 18 h | **Fiche** (recentrée le 10/11 sur les 32 Go, inspirée de RepoChad) et [sources](projets/deux-cartes-occasion/sources.md) vérifiées deux fois (24/10) · prix d'occasion à relever par toi |
| [La meilleure carte graphique pour l'IA locale, à chaque budget (Black Friday)](projets/carte-par-budget/fiche.md) | Longue (calculé) | jeu. 26 nov., 18 h | **Fiche** (14/11), inspirée de [Locally](https://www.youtube.com/watch?v=-ImyaGElyfk) |
| [DeepSeek V4.1 Flash sans carte graphique : 64 Go de RAM suffisent ?](projets/cout-deepseek-flash/fiche.md) | Longue (calculé, actu) | lun. 30 nov., 18 h | **Fiche** (10/11) · angle du 15/11 d'après [Kai](https://www.youtube.com/watch?v=wiMs92u-dk0) · avancée du 18 janv. |
| [RAM, VRAM ou mémoire unifiée : laquelle fait tourner ton IA le plus vite ?](projets/ram-vram-unifiee/fiche.md) | Longue (calculé) | jeu. 3 déc., 18 h | **Fiche** (14/11), inspirée de [Locally](https://www.youtube.com/watch?v=WpHKek1GV70), contre-pied avec Strata |
| [Deux cartes graphiques pour l'IA : à savoir avant d'acheter la deuxième](projets/multi-gpu/fiche.md) | Longue (calculé) | lun. 7 déc., 18 h | **Fiche** (14/11), inspirée de [Weights & Wonders](https://www.youtube.com/watch?v=sF_P1OICoEw) |
| [Mac mini ou PC gamer pour l'IA en local ?](projets/mac-mini-ia/fiche.md) | Longue (calculé) | jeu. 10 déc., 18 h | **Fiche** (24/10), inspirée de [Locally](https://www.youtube.com/watch?v=evkv0_HrhFM) · recherche et double vérification à faire |
| [Combien coûte Claude Fable 5.2 chez toi ?](projets/cout-claude-local/fiche.md) | Longue (calculé, actu) | lun. 14 déc., 18 h | **Script** : [v2](projets/cout-claude-local/script.md) à refaire en v3 (fusion avec Kimi le 15/11, modèle de calcul d'environ 1 To, inspirée de [Pop Theory](https://www.youtube.com/watch?v=yw5mMVq6gas)) ; [grill](projets/cout-claude-local/grill-v1.md) du 22/10 |
| [Le Black Friday a-t-il vraiment fait baisser les prix de l'IA en local ?](projets/prix-apres-black-friday/fiche.md) | Longue (calculé) | jeu. 17 déc., 18 h | **Fiche** (10/11) |
| [IA en local : comment lire le nom d'un modèle](projets/bases-ia-locale/fiche.md) | Longue (calculé, vulgarisation) | lun. 21 déc., 18 h | **Script** (23/10) : [final](projets/bases-ia-locale/script.md), [grill](projets/bases-ia-locale/grill-v1.md), [sources](projets/bases-ia-locale/sources.md) vérifiées deux fois ; tes crochets à remplir (sans essai depuis le 25/10 : prends les replis écrits) ; miniature et kit d'upload à faire ; renvois vers la vidéo d'installation à reprendre ; passée du 2 nov. au 7 déc. le 24/10 (la base d'abord) |
| [Le cadeau IA locale : quel budget pour une machine qui tourne sans le cloud ?](projets/cadeau-ia-locale/fiche.md) | Longue (calculé) | jeu. 24 déc., 18 h | **Fiche** (10/11) |
| [Louer, acheter ou s'abonner ?](projets/louer-acheter-ia/fiche.md) | Longue (calculé) | lun. 28 déc., 18 h | **Script** (23/10) : [final](projets/louer-acheter-ia/script.md), [grill](projets/louer-acheter-ia/grill-v1.md), [sources](projets/louer-acheter-ia/sources.md) vérifiées deux fois ; tes crochets à remplir ; prix à relever le 2/01, ⟦résultat de Claude #1⟧ (calculé) |
| [Claude Code gratuit sur ton PC : ça marche vraiment ?](projets/claude-code-gratuit/fiche.md) | Longue (calculé) | jeu. 7 janv., 18 h | **Fiche** (15/11), inspirée de Sharbel A., Kevin Stratvert, Cedric Oden · provisoire |
| [Ton IA locale est-elle vraiment privée ?](projets/ia-locale-privee/fiche.md) | Longue (calculé) | lun. 11 janv., 18 h | **Fiche** (10/11) · reculée du 26 nov. le 14/11, provisoire |
| [Créer un jeu vidéo avec une IA locale, sur une carte de 16 Go](projets/jeu-video-ia-locale/fiche.md) | Longue (calculé) | jeu. 14 janv., 18 h | **Fiche** (15/11), inspirée de [PΔX](https://www.youtube.com/watch?v=qOywnuU2ypM) · provisoire |
| [Quel modèle ta carte peut faire tourner ? De 4 à 16 Go de VRAM](projets/modele-par-vram/fiche.md) | Longue (calculé) | lun. 18 janv., 18 h | **Fiche** (14/11, ex-petits budgets), inspirée de [Codacus](https://www.youtube.com/watch?v=tek-IY9BRWc), provisoire |
| [54 Go de VRAM pour 35 $ : les vieilles cartes de minage pour l'IA locale](projets/cartes-minage/fiche.md) | Longue (calculé) | jeu. 21 janv., 18 h | **Fiche** (15/11), inspirée de Kai, DiscoverID · provisoire |
| [Ollama, LM Studio ou llama.cpp : lequel choisir pour ton IA locale ?](projets/choisir-moteur/fiche.md) | Longue (calculé) | lun. 25 janv., 18 h | **Fiche** (15/11), inspirée de The Dark Factory · provisoire |
| [Des petits modèles experts peuvent-ils battre les géants ?](projets/petits-modeles-experts/fiche.md) | Longue (calculé) | jeu. 28 janv., 18 h | **Fiche** (15/11), inspirée de Codacus, Nerdy Kings · provisoire |

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
