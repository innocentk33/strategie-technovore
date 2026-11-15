#!/bin/sh
# Rend les miniatures « à la manière de Kai » de « Même carte, 2 fois plus rapide » (3840×2160) :
#   rendus/i-kai.png (sans visage), rendus/h-<visage>.png et j-<visage>.png pour chaque visage (fry, dicaprio)
# ./rendre.sh            tout ;  ./rendre.sh "h&p=fry"  une seule (→ rendus/h-fry.png)
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for v in ${@:-i "h&p=fry" "j&p=fry" "h&p=dicaprio" "j&p=dicaprio"}; do
  out=$(echo "$v" | sed 's/&p=/-/'); [ "$out" = i ] && out=i-kai
  "$CHROME" --headless=new --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 \
    --virtual-time-budget=3000 --screenshot="$PWD/rendus/$out.png" "file://$PWD/propositions/miniature-kai.html?v=$v" 2>/dev/null
done
ls rendus
