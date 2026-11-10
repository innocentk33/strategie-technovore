#!/bin/sh
# Rend les miniatures du 9 nov. en PNG 3840×2160 (page de 1280×720 rendue à ×3) : ./rendre.sh [a b c d e]  → rendus/<v>.png
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for v in ${@:-a b c d e}; do
  "$CHROME" --headless=new --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 \
    --virtual-time-budget=3000 --screenshot="$PWD/rendus/$v.png" "file://$PWD/propositions/miniature.html?v=$v" 2>/dev/null
done
ls rendus
