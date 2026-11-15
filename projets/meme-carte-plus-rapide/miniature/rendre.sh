#!/bin/sh
# Rend les miniatures « à la manière de Kai » de « Même carte, 2 fois plus rapide » → rendus/h-kai.png, i-kai.png, j-kai.png (3840×2160)
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for v in ${@:-h i j}; do
  "$CHROME" --headless=new --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 \
    --virtual-time-budget=3000 --screenshot="$PWD/rendus/$v-kai.png" "file://$PWD/propositions/miniature-kai.html?v=$v" 2>/dev/null
done
ls rendus
