# Technovore : planification et suivi

Planification et suivi de la chaîne YouTube Technovore : stratégie, calendrier, un dossier par vidéo, idées en réserve et idées abandonnées.

## Organisation

| Emplacement | Contenu |
|---|---|
| [`strategie.md`](strategie.md) | Stratégie v4 : positionnement, piliers, vidéos d'inspiration, objectifs à 1, 3 et 6 mois, idées classées |
| [`calendrier.md`](calendrier.md) | Une vidéo longue chaque lundi à 18 h, jusqu'au 26 avril 2027 ; production semaine par semaine jusqu'au 31 janvier |
| [`idees.md`](idees.md) | Boîte à idées : sujets en réserve, pas encore planifiés |
| [`projets/`](projets/) | Un dossier par vidéo |
| [`etudes/`](etudes/) | Études de chaînes concurrentes (données vidIQ) et [`radar.md`](etudes/radar.md), le journal du radar fait à chaque sortie |
| [`ressources/`](ressources/) | Ce qui sert à plusieurs vidéos : animations Remotion, miniatures, audio, voix |
| [`archive/`](archive/) | Projets et idées abandonnés, avec la raison |
| `claude-youtube/` | Copie locale du skill `/youtube`, non suivie par git. Le skill utilisé est celui de `~/.claude/skills/` (installation : `git clone https://github.com/AgriciDaniel/claude-youtube && ./claude-youtube/install.sh`) |

## Suivi des projets

| Projet | Format | Publication | Statut |
|---|---|---|---|
| [ArtCraft](projets/artcraft/fiche.md) | Longue | lun. 19 oct., 18 h | **Publié** : [*Il a cloné TOUTES les applications ADOBE et c'est gratuit*](https://www.youtube.com/watch?v=FVFb4dnUmLA) |
| [OpenCode piraté](projets/opencode/fiche.md) | Longue (actu) | mer. 21 oct., 13 h | **Publié** : [*OpenCode a été gravement piraté (explication !)*](https://www.youtube.com/watch?v=LeZ9hgwvXy0) |
| [Uber](projets/uber/fiche.md) | Longue | lun. 26 oct., 18 h | Montage fini (9:59,6), en ligne en privé : titre et tags à corriger ; [kit d'upload](projets/uber/upload.md), sous-titres FR/EN et miniatures corrigées prêts |
| [Combien coûte Claude en local ?](projets/cout-claude-local/fiche.md) | Longue (calculé) | lun. 2 nov., 18 h | Fiche |
| [Waze](projets/waze/fiche.md) | Longue | lun. 9 nov., 18 h | Fiche |
| [Claude ou mon PC ? #1 : 16 Go de VRAM](projets/claude-ou-mon-pc-1/fiche.md) | Longue (testé) | lun. 16 nov., 18 h | Brouillon |
| [Pseudo déjà pris](projets/pseudo/fiche.md) | Longue | lun. 23 nov., 18 h (joker) | Fiche |
| [iPhone plus fluide](projets/iphone-fluide/fiche.md) | Longue | lun. 7 déc., 18 h | Fiche |
| [Pixel](projets/pixel/fiche.md) | Longue | lun. 14 déc., 18 h | Brouillon |
| [Python](projets/python/fiche.md) | Longue | lun. 28 déc., 18 h | Brouillon |
| [Louer, acheter ou s'abonner ?](projets/louer-acheter-ia/fiche.md) | Longue (calculé) | lun. 4 janv., 18 h | Fiche |
| [WhatsApp](projets/whatsapp/fiche.md) | Longue | lun. 11 janv., 18 h | Fiche |
| [Claude ou mon PC ? #2](projets/claude-ou-mon-pc-2/fiche.md) | Longue (testé) | lun. 18 janv., 18 h | Fiche |
| [Windows Phone](projets/windows-phone/fiche.md) | Longue | lun. 25 janv., 18 h | Brouillon |

**Statuts** : Fiche → Brouillon → Recherche → Script → Voix → Montage → Programmé → Publié (ajouter le lien YouTube).
Les créneaux sans projet (30 nov., 21 déc., puis à partir de février) sont choisis par le radar : voir [`calendrier.md`](calendrier.md).

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
