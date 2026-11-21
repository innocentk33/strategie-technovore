# Son : voix, musique, coupures, bruitages

Pistes (dans `build.py`) : voix sur la piste 10 (volume 0,794), musique sur 11-12, bruitages sur 20-31 répartis par famille sans chevauchement, mèmes muets.

## Musique

Deux musiques Pixabay libres d'usage, dans `assets/audio/` (versions longues bouclées `-long.flac`) :
- `music-minimal(-long).flac` : « Future Minimal » de kissan4 ;
- `music-tension(-long).flac` : « Dark Ambient for Crime and Tension » de megalix.
Crédit dans la description (`style/media.json` les liste).

Structure : minimal sous l'introduction, tension pendant le cœur du problème (les pièges, la partie où ça coince), retour du minimal quand la solution arrive, et le minimal plus fort sur l'écran de fin. Exemple du 32 Go :

```python
music = [(MIN, 0, t_r1, .24, 0),
         (TEN, t_r1, t_r3, .2, 0),
         (MIN, t_r3, voice + .3, .24, 90),
         (MIN, voice + .3, END, .42, 90 + voice + .3 - t_r3)]
```

Niveaux : les volumes ont monté d'une vidéo à l'autre (0,11 sur Strata, 0,15 sur « Même carte », 0,19 sur le 8 Go, 0,24 sur le 32 Go) parce que les critiques la trouvaient inaudible sur téléphone et que les coupures ne s'entendaient pas. Vise **15 à 22 dB sous la voix**, mesuré par tranches de 10 s (médiane ~17 dB) : jamais au point de couvrir la voix.

**Les coupures font le montage** : la musique se coupe environ 0,35 s avant chaque chute (un mot choc, une révélation) et reprend 1,2 s après :

```python
cuts = [T('c est de l or') - .35, T('noël sans cartes') - .35, T('rien c est la même carte') - .35]
```

Choisis 3 ou 4 chutes, celles où la voix a aussi un petit temps avant (`voix-clonee.md`).

## Bruitages

Dans `assets/sfx/*.flac`, posés par `sfx(sc, t, 'nom', vol)` ou par les briques (pop sur un prix, tick sur un surlignage, click sur le bouton d'abonnement). `build.py` :
- **interdit** `impact`, `impact-doux`, `riser-court`, `powerdown`, `whoosh-long` (« pas de boum, pas de son d'extinction ») ;
- ne met un whoosh que sur une vraie entrée fouettée, un seul par plan ;
- fixe des volumes bas (whoosh 0,05, pop 0,07, tick 0,05, slide 0,055…) et abandonne un son s'il y en a déjà trois de la même famille en même temps.
`montage.py` retire en plus tout bruitage à moins de 0,3 s du précédent dans le même plan.

Un bruitage a un sens (un prix qui tombe, une carte qui glisse, une coche) ; 0 à 2 par plan. Deux bruitages CC BY demandent un crédit (`assets/sfx/CREDITS.md` : `bubble-pop`, `papers-rustling`) : si tu les utilises, crédite-les dans la description.

## Contrôle

Mesure le rendu final (et pas seulement la voix) :

```bash
ffmpeg -nostats -i renders/<rendu>.mp4 -af ebur128=peak=true -f null - 2>&1 | grep -E "I:|Peak:" | tail -2
```

Repères : rendu entre −16 et −14 LUFS (32 Go : −15,1 LUFS, crête −2,8 dB) ; voix seule −16 LUFS, −2,5 dBTP. Écoute (par mesure) autour des mèmes, des titres de partie et des coupures : la musique s'arrête-t-elle vraiment avant la chute ?
