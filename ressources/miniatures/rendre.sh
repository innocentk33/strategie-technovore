#!/bin/sh
# Rend les miniatures en PNG 1280×720 : ./rendre.sh [vert|noir] [n…]  (sans argument : toutes)
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
render() { # style n
  out="$PWD/rendus/$1-$(printf %02d "${2%b}")${2#"${2%b}"}.png"
  "$CHROME" --headless=new --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 \
    --virtual-time-budget=3000 --screenshot="$out" "file://$PWD/$1.html?n=$2" 2>/dev/null
}
if [ -n "$1" ]; then
  style=$1; shift
  for n in ${@:-$( [ "$style" = vert ] && echo 2 5 9 10 || echo 1 1b 3 4 6 7 8 )}; do render "$style" "$n"; done
else
  for n in 2 5 9 10; do render vert "$n"; done
  for n in 1 1b 3 4 6 7 8; do render noir "$n"; done
fi
ls rendus
