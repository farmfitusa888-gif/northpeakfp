#!/usr/bin/env bash
# Regenerate the trimmed three.js bundle that the hero scene imports.
#
# The full three.module.js is 1.27MB raw / 256KB gzipped. The hero uses a small
# fraction of it, so this re-exports only the symbols summit.js imports and lets
# esbuild tree-shake the rest away — about 119KB gzipped, 54% smaller.
#
# The OUTPUT is committed to the repo. This script only needs to run when the
# three.js version changes or summit.js starts importing a new symbol, which
# means the Netlify build never needs Node installed.
#
#   ./tools/build_three.sh
#
# If summit.js imports something that is not in the export list below, the page
# fails with "does not provide an export named X". Add it here and re-run.

set -euo pipefail
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENDOR="$REPO/generators/static/assets/vendor"
THREE_VERSION="0.160.0"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

echo "Fetching three@$THREE_VERSION ..."
curl -sSf --max-time 120 -o "$WORK/three.js" \
  "https://unpkg.com/three@${THREE_VERSION}/build/three.module.js"

# Keep this list in sync with the import block at the top of
# generators/static/assets/summit.js
cat > "$WORK/entry.js" <<'EOF'
export {
  Scene, PerspectiveCamera, WebGLRenderer, Color, FogExp2,
  PlaneGeometry, BufferGeometry, BufferAttribute, Float32BufferAttribute,
  MeshStandardMaterial, MeshBasicMaterial, ShaderMaterial,
  Mesh, Points, Group, HemisphereLight, DirectionalLight,
  CanvasTexture, AdditiveBlending
} from './three.js';
EOF

mkdir -p "$VENDOR"
npx --yes esbuild "$WORK/entry.js" --bundle --format=esm --minify \
  --tree-shaking=true --legal-comments=inline \
  --outfile="$VENDOR/three.summit.js" --log-level=warning

raw=$(wc -c < "$VENDOR/three.summit.js")
gz=$(gzip -9c "$VENDOR/three.summit.js" | wc -c)
full_gz=$(gzip -9c "$WORK/three.js" | wc -c)
printf 'three.summit.js  %s raw  %s gzip   (full library would be %s gzip)\n' \
  "$raw" "$gz" "$full_gz"
