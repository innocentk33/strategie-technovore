#!/bin/sh
set -eu
cd "$(dirname "$0")"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p rendus photocraft apercu
profile=$(mktemp -d /tmp/miniature-modeles.XXXXXX)
trap 'rm -rf "$profile"' EXIT
for v in h i j; do
 "$CHROME" --headless=new --user-data-dir="$profile" --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 --virtual-time-budget=3000 --screenshot="$PWD/rendus/$v-kai.png" "file://$PWD/propositions/miniature-kai.html?v=$v" 2>/dev/null
 done
if [ "${1:-}" = "--psd" ]; then
 python3 -I export-psd.py
fi
python3 -I apercu.py
