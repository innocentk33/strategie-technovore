#!/bin/sh
set -eu
cd "$(dirname "$0")"
mkdir -p rendus photocraft apercu
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PROFILE=$(mktemp -d /tmp/technovore-usages.XXXXXX)
trap 'rm -rf "$PROFILE"' EXIT
if [ "${1:-}" = "--psd" ]; then
 shift
 python3 -IB export-psd.py "$@"
 exit
fi
for v in ${@:-h i j}; do
 "$CHROME" --headless=new --user-data-dir="$PROFILE" --hide-scrollbars --allow-file-access-from-files --window-size=1280,720 --force-device-scale-factor=3 --virtual-time-budget=3000 --screenshot="$PWD/rendus/$v-kai.png" "file://$PWD/propositions/miniature-kai.html?v=$v" 2>/dev/null
done
