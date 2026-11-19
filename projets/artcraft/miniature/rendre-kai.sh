#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p rendus photocraft apercu/kai
profile=$(mktemp -d /tmp/miniature-kai.XXXXXX)
trap 'rm -rf "$profile"' EXIT
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for v in h i j; do
 "$CHROME" --headless=new --user-data-dir="$profile" --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 --virtual-time-budget=3000 --screenshot="$PWD/rendus/$v-kai.png" "file://$PWD/propositions/miniature-kai.html?v=$v" 2>/dev/null
 done
python3 -I apercu-kai.py
if [ "${1:-}" = "--psd" ]; then python3 -I export-kai-psd.py; fi
