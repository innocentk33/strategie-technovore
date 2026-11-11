#!/bin/sh
# Rend les miniatures « Strata sur ma 5080 » en PNG 3840×2160 (page de 1280×720 rendue à ×3) : ./rendre.sh [a b c]  → rendus/<v>.png
# Pour c (après les tests) : ./rendre.sh "c&rouge=A%20GAGNÉ&toks=72"  → rendus/c.png
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for v in ${@:-a b}; do
  out=$(echo "$v" | cut -d'&' -f1)
  "$CHROME" --headless=new --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 \
    --virtual-time-budget=3000 --screenshot="$PWD/rendus/$out.png" "file://$PWD/propositions/miniature.html?v=$v" 2>/dev/null
done
ls rendus
