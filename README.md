# Technovore : planification et suivi

Planification et suivi de la chaîne YouTube Technovore : stratégie, calendrier, un dossier par vidéo, idées en réserve et idées abandonnées.

## Organisation

| Emplacement | Contenu |
|---|---|
| [`strategie.md`](strategie.md) | Stratégie v4 : positionnement, piliers, vidéos d'inspiration, objectifs à 1, 3 et 6 mois, idées classées |
| [`calendrier.md`](calendrier.md) | Une vidéo longue chaque lundi à 18 h, jusqu'au 26 avril 2027 ; production semaine par semaine jusqu'au 31 janvier |
| [`idees.md`](idees.md) | Boîte à idées : sujets en réserve, pas encore planifiés |
| [`projets/`](projets/) | Un dossier par vidéo |
| [`etudes/`](etudes/) | Études de chaînes concurrentes (données vidIQ), audits de la chaîne (le dernier : [22/10](etudes/audit-2026-10-22.md)) et [`radar.md`](etudes/radar.md), le journal du radar fait à chaque sortie |
| [`ressources/`](ressources/) | Ce qui sert à plusieurs vidéos : animations Remotion, miniatures, audio, voix, et [la régie](ressources/regie/PRODUCT.md) (lecteur des `.md` et suivi des vidéos : `node ressources/regie/regie.mjs`) |
| [`archive/`](archive/) | Projets et idées abandonnés, avec la raison |
| `claude-youtube/` | Copie locale du skill `/youtube`, non suivie par git. Le skill utilisé est celui de `~/.claude/skills/` (installation : `git clone https://github.com/AgriciDaniel/claude-youtube && ./claude-youtube/install.sh`) |

## Suivi des projets

| Projet | Format | Publication | Statut |
|---|---|---|---|
| [ArtCraft](projets/artcraft/fiche.md) | Longue | lun. 19 oct., 18 h | **Publié** : [*Il a cloné TOUTES les applications ADOBE et c'est gratuit*](https://www.youtube.com/watch?v=FVFb4dnUmLA) |
| [OpenCode piraté](projets/opencode/fiche.md) | Longue (actu) | mer. 21 oct., 13 h | **Publié** : [*OpenCode a été gravement piraté (explication !)*](https://www.youtube.com/watch?v=LeZ9hgwvXy0) |
| [Uber](projets/uber/fiche.md) | Longue | lun. 26 oct., 18 h | **Programmé** (lun. 26 oct., 18 h) : titre et tags corrigés (vérifié dans vidIQ le 22/10) ; [kit d'upload](projets/uber/upload.md) |
| [Pourquoi avoir ta propre IA, et comment l'installer (LM Studio)](projets/installer-ia-locale/fiche.md) | Longue (testé, vulgarisation) | lun. 2 nov., 18 h | **Script** (24/10) : [final](projets/installer-ia-locale/script.md), [grill](projets/installer-ia-locale/grill-v1.md), [sources](projets/installer-ia-locale/sources.md) vérifiées deux fois, [étapes jusqu'à la sortie](projets/installer-ia-locale/etapes.md) ; ta capture (crochets de l'écran), ta voix, 3 miniatures et kit d'upload à faire ; nouvelle, ta demande du 24/10 (la base d'abord) |
| [Waze](projets/waze/fiche.md) | Longue | lun. 9 nov., 18 h | **Script** (23/10) : [final](projets/waze/script.md), [grill](projets/waze/grill-v1.md), [sources](projets/waze/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Abonnement ou IA locale ? #1 : 16 Go de VRAM suffisent-ils ?](projets/claude-ou-mon-pc-1/fiche.md) | Longue (testé) | lun. 16 nov., 18 h | Brouillon · essais sur la 5080 les 23-24/10 · revenue au 16 nov. le 23/10, derrière la vidéo d'installation |
| [Combien coûte Claude en local ?](projets/cout-claude-local/fiche.md) | Longue (calculé) | lun. 23 nov., 18 h (avancée le 24/10 : avant le Black Friday) | Script : [v2](projets/cout-claude-local/script.md) à compléter (résultats de Claude #1, tes ⟦à écrire⟧) ; [grill](projets/cout-claude-local/grill-v1.md) du 22/10 |
| [Pseudo déjà pris](projets/pseudo/fiche.md) | Longue | lun. 30 nov., 18 h (joker, reculé le 24/10) | **Script** (23/10) : [final](projets/pseudo/script.md), [grill](projets/pseudo/grill-v1.md), [sources](projets/pseudo/sources.md) vérifiées deux fois ; tes crochets à remplir ; « en une milliseconde » gardé, tenu côté serveur (fait 33) |
| [IA en local : comment lire le nom d'un modèle](projets/bases-ia-locale/fiche.md) | Longue (calculé, vulgarisation) | lun. 7 déc., 18 h | **Script** (23/10) : [final](projets/bases-ia-locale/script.md), [grill](projets/bases-ia-locale/grill-v1.md), [sources](projets/bases-ia-locale/sources.md) vérifiées deux fois ; tes crochets à remplir avec les résultats des essais ; miniature et kit d'upload à faire ; renvois vers la vidéo d'installation à reprendre ; passée du 2 nov. au 7 déc. le 24/10 (la base d'abord) |
| [Pixel : d'un pixel à 3,7 milliards de joueurs](projets/pixel/fiche.md) | Longue | lun. 14 déc., 18 h | **Script** (23/10) : [final](projets/pixel/script.md), [grill](projets/pixel/grill-v1.md), [sources](projets/pixel/sources.md) vérifiées deux fois ; tes crochets à remplir ; 3,7 milliards (Newzoo 2026), tranché le 23/10 |
| [Deux cartes d'occasion pour le max de VRAM](projets/deux-cartes-occasion/fiche.md) | Longue (calculé, sans achat) | lun. 21 déc., 18 h | **Fiche** et [sources](projets/deux-cartes-occasion/sources.md) vérifiées deux fois (24/10) · prix d'occasion à relever par toi |
| [Python, le langage de l'IA, est un cadeau de Noël](projets/python/fiche.md) | Longue | lun. 28 déc., 18 h | **Script** (23/10) : [final](projets/python/script.md), [grill](projets/python/grill-v1.md), [sources](projets/python/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Louer, acheter ou s'abonner ?](projets/louer-acheter-ia/fiche.md) | Longue (calculé) | lun. 4 janv., 18 h | **Script** (23/10) : [final](projets/louer-acheter-ia/script.md), [grill](projets/louer-acheter-ia/grill-v1.md), [sources](projets/louer-acheter-ia/sources.md) vérifiées deux fois ; tes crochets à remplir ; prix à relever le 2/01, ⟦mesure de Claude #1⟧ |
| [WhatsApp](projets/whatsapp/fiche.md) | Longue | lun. 11 janv., 18 h | **Script** (23/10) : [final](projets/whatsapp/script.md), [grill](projets/whatsapp/grill-v1.md), [sources](projets/whatsapp/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Abonnement ou IA locale ? #2 : le dernier modèle sorti](projets/claude-ou-mon-pc-2/fiche.md) | Longue (testé) | lun. 18 janv., 18 h | Fiche |
| [Ton téléphone est une brique (Windows Phone)](projets/windows-phone/fiche.md) | Longue | lun. 25 janv., 18 h | **Script** (23/10) : [final](projets/windows-phone/script.md), [grill](projets/windows-phone/grill-v1.md), [sources](projets/windows-phone/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Mac mini ou PC gamer pour l'IA en local ?](projets/mac-mini-ia/fiche.md) | Longue (calculé) | lun. 1er févr., 18 h (provisoire) | **Fiche** (24/10), inspirée de [Locally](https://www.youtube.com/watch?v=evkv0_HrhFM) · recherche et double vérification à faire |
| [Le dev qui a mis un ChatGPT dans ton PC (llama.cpp)](projets/llama-cpp/fiche.md) | Longue | lun. 8 févr., 18 h (provisoire) | **Script** (23/10) : [final](projets/llama-cpp/script.md), [grill](projets/llama-cpp/grill-v1.md), [sources](projets/llama-cpp/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [iPhone plus fluide](projets/iphone-fluide/fiche.md) | Longue | lun. 15 févr., 18 h (provisoire, reculée le 24/10) | **Script** (23/10) : [final](projets/iphone-fluide/script.md), [grill](projets/iphone-fluide/grill-v1.md), [sources](projets/iphone-fluide/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Tu n'as jamais possédé tes jeux](projets/jeux-possedes/fiche.md) | Longue | lun. 22 févr., 18 h (provisoire) | **Script** (23/10) : [final](projets/jeux-possedes/script.md), [grill](projets/jeux-possedes/grill-v1.md), [sources](projets/jeux-possedes/sources.md) vérifiées deux fois ; tes crochets à remplir ; actualité à remettre à jour avant la sortie ; on garde le 22 févr., loin de la vague de GTA 6 (19/11) |
| [Pourquoi tu meurs derrière un mur (le lag)](projets/lag/fiche.md) | Longue | lun. 8 mars, 18 h (provisoire) | **Script** (23/10) : [final](projets/lag/script.md), [grill](projets/lag/grill-v1.md), [sources](projets/lag/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Sans cette base de données, ton téléphone ne marche pas (SQLite)](projets/sqlite/fiche.md) | Longue | lun. 22 mars, 18 h (provisoire) | **Script** (23/10) : [final](projets/sqlite/script.md), [grill](projets/sqlite/grill-v1.md), [sources](projets/sqlite/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Le génie caché du paiement sans contact](projets/sans-contact/fiche.md) | Longue | lun. 5 avr., 18 h (provisoire) | **Script** (23/10) : [final](projets/sans-contact/script.md), [grill](projets/sans-contact/grill-v1.md), [sources](projets/sans-contact/sources.md) vérifiées deux fois ; tes crochets à remplir |
| [Il n'y a pas de blanc sur ton écran](projets/ecran-blanc/fiche.md) | Longue | lun. 19 avr., 18 h (provisoire) | **Script** (23/10) : [final](projets/ecran-blanc/script.md), [grill](projets/ecran-blanc/grill-v1.md), [sources](projets/ecran-blanc/sources.md) vérifiées deux fois ; tes crochets à remplir |

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
