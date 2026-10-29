#!/bin/sh
# Builds MillenaireCobblemon-CurseForge.zip from the packwiz pack.
# The 5 mods that are pulled from Modrinth / bundled for packwiz go back into the
# manifest as CurseForge entries, because the CurseForge App can download them.
# When you update one of those 5 mods, update its fileID in tools/original-manifest.json too.
set -e
cd "$(dirname "$0")/.."
packwiz curseforge export -o /tmp/millenaire-cf-raw.zip
python3 -I tools/fix_cf.py /tmp/millenaire-cf-raw.zip tools/original-manifest.json MillenaireCobblemon-CurseForge.zip
rm -f /tmp/millenaire-cf-raw.zip
