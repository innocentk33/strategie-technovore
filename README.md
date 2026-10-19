# Technovore : planification et suivi

Planification et suivi de la chaîne YouTube Technovore : stratégie, calendrier, un dossier par vidéo, idées en réserve et idées abandonnées.

## Organisation

| Emplacement | Contenu |
|---|---|
| [`strategie.md`](strategie.md) | Positionnement v3, piliers, vidéos d'inspiration, objectifs J30/J60/J90, les 10 idées classées |
| [`calendrier.md`](calendrier.md) | Grille de publication et production semaine par semaine, jusqu'au 31 janvier 2027 |
| [`idees.md`](idees.md) | Boîte à idées : sujets en réserve, pas encore planifiés |
| [`projets/`](projets/) | Un dossier par vidéo (longue ou Short autonome) |
| [`etudes/`](etudes/) | Études de chaînes concurrentes ou d'inspiration (données vidIQ) |
| [`ressources/`](ressources/) | Ce qui sert à plusieurs vidéos : animations Remotion, miniatures, audio, voix |
| [`archive/`](archive/) | Projets et idées abandonnés, avec la raison |
| `claude-youtube/` | Copie locale du skill `/youtube`, non suivie par git. Le skill utilisé est celui de `~/.claude/skills/` (installation : `git clone https://github.com/AgriciDaniel/claude-youtube && ./claude-youtube/install.sh`) |

## Suivi des projets

| Projet | Format | Publication | Statut |
|---|---|---|---|
| [Windows 10](projets/short-windows-10/fiche.md) | Short | jeu. 15 oct., 18 h | À faire |
| [Vorssaint, l'app qui répare macOS](projets/short-vorssaint/fiche.md) | Short | jeu. 22 oct., 18 h | Fiche |
| [ArtCraft](projets/artcraft/fiche.md) | Longue | lun. 26 oct., 20 h | Montage |
| [Uber](projets/uber/fiche.md) | Longue | lun. 9 nov., 20 h | Brouillon |
| [Claude ou mon PC ? #1 : 16 Go de VRAM](projets/claude-ou-mon-pc-1/fiche.md) | Longue | lun. 23 nov., 20 h | Brouillon |
| [Waze](projets/waze/fiche.md) | Longue | lun. 7 déc., 20 h | Fiche |
| [Pixel](projets/pixel/fiche.md) | Longue | lun. 21 déc., 20 h | Brouillon |
| [Combien coûte Claude en local ?](projets/cout-claude-local/fiche.md) | Longue | lun. 4 janv., 20 h | Fiche |
| [WhatsApp](projets/whatsapp/fiche.md) | Longue | lun. 18 janv., 20 h | Fiche |
| [Claude ou mon PC ? #2](projets/claude-ou-mon-pc-2/fiche.md) | Longue | lun. 1er févr., 20 h | Fiche |

**Statuts** : Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié (ajouter le lien YouTube).
Les Shorts tirés d'une vidéo longue sont listés dans la fiche de cette vidéo.

## Un dossier projet

```
projets/<nom>/
├── fiche.md        titres, miniature, contenu, points à vérifier, Shorts
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
