#!/usr/bin/env bash
# Donne à une prise du Razer Seiren Mini (micro statique, brillant, qui capte la pièce)
# le son d'un Shure SM7B (micro dynamique : chaud, doux dans les aigus, peu de pièce).
# Usage : ./sm7b.sh prise.wav [sortie.wav]
set -euo pipefail

in="$1"
out="${2:-${in%.*}-sm7b.wav}"

# Réglages à ajuster à l'oreille (l'égaliseur passe après le compresseur, sinon il lui écrase la courbe)
BRUIT=-45      # dB, niveau du souffle à retirer (-30 = fort, -60 = léger)
GATE=0.015     # seuil de l'expandeur (~ -36 dB) : monte-le si la pièce s'entend encore entre les phrases
CHALEUR=4      # dB autour de 150 Hz : l'effet de proximité du SM7B
DOUCEUR=-5     # dB au-dessus de 8 kHz : le SM7B est sombre en haut, le Seiren brille

ffmpeg -hide_banner -loglevel error -y -i "$in" -af "\
highpass=f=70,\
afftdn=nf=$BRUIT:tn=1,\
agate=threshold=$GATE:ratio=2:range=0.25:attack=5:release=150,\
deesser=i=0.4,\
acompressor=threshold=-20dB:ratio=4:attack=5:release=80:makeup=2,\
bass=g=$CHALEUR:f=150:w=0.7,\
equalizer=f=350:t=q:w=1.2:g=-2,\
equalizer=f=4500:t=q:w=1.5:g=1.5,\
treble=g=$DOUCEUR:f=8000:w=0.7,\
loudnorm=I=-16:TP=-1.5:LRA=7" \
  -ar 48000 -c:a pcm_s24le "$out"

echo "$out"
