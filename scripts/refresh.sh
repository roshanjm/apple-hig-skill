#!/usr/bin/env bash
# Re-crawl developer.apple.com/design/human-interface-guidelines and rebuild references/hig/.
# Usage: scripts/refresh.sh  (takes ~2 minutes; needs network). Digests (references/*.md) are
# hand/agent-written and must be regenerated separately after a refresh.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
python3 -I "$HERE/scripts/crawl_hig.py" "$TMP/json"
python3 -I "$HERE/scripts/docc_to_md.py" "$TMP/json" "$TMP/md"
echo "Rendered pages in $TMP/md — copy into $HERE/references/hig/<section>/ and rebuild INDEX.md."
