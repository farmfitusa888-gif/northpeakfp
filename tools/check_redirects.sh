#!/usr/bin/env bash
# Verify every URL form resolves the way the redirect rules intend, against a
# real Netlify redirect engine rather than by reading the rules and hoping.
#
#   ./tools/check_redirects.sh                 # local, via `netlify dev`
#   ./tools/check_redirects.sh https://northpeakfp.com   # against production
#
# Exits non-zero if any URL misbehaves, so it can gate a deploy.

set -uo pipefail
BASE="${1:-}"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOCAL_PID=""

if [[ -z "$BASE" ]]; then
  PORT=8899
  netlify dev --dir site --port "$PORT" --offline >/tmp/np-netlify-dev.log 2>&1 &
  LOCAL_PID=$!
  BASE="http://localhost:$PORT"
  for _ in $(seq 1 45); do
    curl -fsS -o /dev/null "$BASE/" 2>/dev/null && break
    sleep 1
  done
fi
cleanup() { [[ -n "$LOCAL_PID" ]] && kill "$LOCAL_PID" 2>/dev/null; }
trap cleanup EXIT

fail=0
pass=0

# url | expected status | expected Location suffix ("-" when none expected)
check() {
  local url="$1" want_status="$2" want_loc="$3"
  local out status loc hops
  out=$(curl -sS -o /dev/null -D - "$BASE$url" 2>/dev/null)
  status=$(printf '%s' "$out" | awk 'NR==1{print $2}')
  loc=$(printf '%s' "$out" | tr -d '\r' | awk 'tolower($1)=="location:"{print $2}')
  # follow the chain to catch loops and multi-hop redirects
  hops=$(curl -sS -o /dev/null -w '%{num_redirects} %{http_code}' -L --max-redirs 5 "$BASE$url" 2>/dev/null)

  local ok=1
  [[ "$status" == "$want_status" ]] || ok=0
  if [[ "$want_loc" != "-" ]]; then
    [[ "$loc" == *"$want_loc" ]] || ok=0
  fi
  # more than one hop means a redirect chain; 0 hops + non-200 final means a loop
  local nhops final
  nhops=${hops%% *}; final=${hops##* }
  [[ "$nhops" -le 1 ]] || ok=0
  [[ "$final" == "200" ]] || ok=0

  if [[ "$ok" == 1 ]]; then
    pass=$((pass+1)); printf '  ok    %-34s %s  (%s hop, final %s)\n' "$url" "$status" "$nhops" "$final"
  else
    fail=$((fail+1)); printf '  FAIL  %-34s got %s loc=%s hops=%s final=%s (want %s %s)\n' \
      "$url" "$status" "${loc:--}" "$nhops" "$final" "$want_status" "$want_loc"
  fi
}

echo "Checking $BASE"
echo
echo "Canonical URLs must return 200 directly:"
for u in / /about /services /contact /resources /articles/ /service-areas/ /articles/llc-vs-s-corp; do
  check "$u" 200 -
done

echo
echo ".html forms must 301 to the canonical URL, in exactly one hop:"
check /index.html            301 /
check /about.html            301 /about
check /services.html         301 /services
check /contact.html          301 /contact
check /resources.html        301 /resources
check /articles/index.html   301 /articles/
check /articles/llc-vs-s-corp.html 301 /articles/llc-vs-s-corp

echo
echo "Legacy Squarespace URLs must 301 straight to the final URL, no chain:"
check /new-page   301 /about
check /new-page-1 301 /articles
check /submit     301 /contact
check /cart       301 /services

echo
echo "─────────────────────────────────────────"
printf 'passed %d   failed %d\n' "$pass" "$fail"
[[ "$fail" -eq 0 ]] || exit 1
