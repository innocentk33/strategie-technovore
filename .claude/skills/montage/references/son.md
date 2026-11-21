# Son : voix, musique, coupures, bruitages

Pistes (dans `build.py`) : voix sur la piste 10 (volume 0,794), musique sur 11-12, bruitages sur 20-31 répartis par famille sans chevauchement, mèmes muets.

## Musique

**Toujours les deux mêmes musiques**, dans toutes les vidéos longues depuis Strata : c'est une signature de la chaîne. N'en change pas sans l'accord de l'auteur. Ce sont deux musiques Pixabay libres d'usage, sans attribution obligatoire ; on les crédite quand même dans la description :

| Fichier du projet | Musique | Pixabay | Rôle |
|---|---|---|---|
| `assets/audio/music-minimal.flac` | « Future Minimal », de kissan4 | n° 358346 (fichier d'origine `kissan4-future-minimal-358346.mp3`, 85,16 s) | calme, électronique : introduction, solution, écran de fin |
| `assets/audio/music-tension.flac` | « Dark Ambient for Crime and Tension », de megalix | n° 360762 (fichier d'origine `megalix-dark-ambient-for-crime-and-tension-360762.mp3`, 91,13 s) | sombre : le cœur du problème |

- **Les versions courtes** sont les mp3 d'origine décodés en FLAC (48 kHz, 24 bits). Elles sont dans chaque projet, donc dans chaque dépôt git, et rien n'est à télécharger.
- **Les mp3 d'origine** sont rangés sur la machine de l'auteur dans `~/Dev/essais V2F/premium/audio/music/`. `style/media.json` les référence (`premium-musique:…`).
- **Les retrouver sur Pixabay** : cherche leur numéro sur pixabay.com/music.

**Versions longues** (`music-*-long.flac`, ce que lit `montage.py`) : une courte ne couvre pas une vidéo de 10 minutes, d'où des boucles.
- **Contenu** : 9 copies de la courte, débarrassée de son début et de sa fin sous −24 dB, enchaînées par des fondus croisés de 3 s. Durées : minimal 617,25 s, tension 781,5 s.
- **Pas dans git** : elles font 123 et 141 Mo, au-delà de la limite de 100 Mo de GitHub.
- **Pour les refaire** : `uv run --no-project --with numpy python scripts/musique_longue.py`, à lancer après un clone ou dans un nouveau projet. Il ne refait que celles qui manquent (`--force` pour tout refaire) et redonne un audio **identique au bit près** (vérifié le 21/11 sur un clone du 32 Go : `index.html` régénéré identique, `check` passé).

Structure : minimal sous l'introduction, tension pendant le cœur du problème (les pièges, la partie où ça coince), retour du minimal quand la solution arrive, et le minimal plus fort sur l'écran de fin. Exemple du 32 Go :

```python
# 21/11 (v5, retour de l'auteur : « la musique est trop forte ») : tout ×0,56 sous la voix (≈ −5 dB), écran de fin ×0,7
MUS = .56
music = [(MIN, 0, t_r1, .24 * MUS, 0),                              # 0,134
         (TEN, t_r1, t_r3, .2 * MUS, 0),                            # 0,112
         (MIN, t_r3, voice + .3, .24 * MUS, 90),                    # 0,134
         (MIN, voice + .3, END, .42 * .7, 90 + voice + .3 - t_r3)]  # 0,294 sur l'écran de fin
```

Niveaux : les volumes ont d'abord monté d'une vidéo à l'autre (0,11 sur Strata, 0,15 sur « Même carte », 0,19 sur le 8 Go, 0,24 sur les premières versions du 32 Go), parce que les critiques la trouvaient inaudible sur téléphone. Puis **l'auteur a trouvé la musique trop forte** sur le 32 Go (21/11) : tout est revenu à ×0,56 (0,11 à 0,13 sous la voix, 0,29 sur l'écran de fin), avec un écart voix-musique passé d'environ 13 dB à 18 dB. **Ce sont ces valeurs qu'on garde.** Vise 15 à 22 dB sous la voix, mesuré par tranches de 10 s (médiane ~18 dB). En cas de doute, plus bas plutôt que plus fort : c'est l'avis de l'auteur, pas celui des critiques, qui compte.

**Les coupures font le montage** : la musique se coupe environ 0,35 s avant chaque chute (un mot choc, une révélation) et reprend 1,2 s après :

```python
cuts = [T('c est de l or') - .35, T('noël sans cartes') - .35, T('rien c est la même carte') - .35]
```

Choisis 3 ou 4 chutes, celles où la voix a aussi un petit temps avant (`voix-clonee.md`).

## Bruitages

Dans `assets/sfx/*.flac`, posés par `sfx(sc, t, 'nom', vol)` ou par les briques (pop sur un prix, tick sur un surlignage, click sur le bouton d'abonnement). `build.py` :
- **interdit** `impact`, `impact-doux`, `riser-court`, `powerdown`, `whoosh-long` (« pas de boum, pas de son d'extinction ») ;
- ne garde qu'un whoosh par plan ; il en pose un sur chaque plan fouetté (`whip`), et les cadres qui glissent (`frame(..., entry='left'|'right')`) en apportent un aussi ;
- fixe des volumes bas (whoosh 0,05, pop 0,07, tick 0,05, slide 0,055…) et abandonne un son s'il y en a déjà trois de la même famille en même temps.
`montage.py` retire en plus tout bruitage à moins de 0,3 s du précédent dans le même plan.

Un bruitage a un sens (un prix qui tombe, une carte qui glisse, une coche) ; 0 à 2 par plan. Deux bruitages CC BY demandent un crédit (`assets/sfx/CREDITS.md` : `bubble-pop`, `papers-rustling`) : si tu les utilises, crédite-les dans la description.

## Contrôle

Mesure le rendu final (et pas seulement la voix) :

```bash
ffmpeg -nostats -i renders/<rendu>.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:" | tail -2
```

Repères : rendu entre −16 et −14 LUFS (32 Go : −15,1 LUFS, crête −2,8 dB) ; voix seule −16 LUFS, −2,5 dBTP. Écoute (par mesure) autour des mèmes, des titres de partie et des coupures : la musique s'arrête-t-elle vraiment avant la chute ?
