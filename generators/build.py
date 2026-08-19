#!/usr/bin/env python3
"""
NorthPeak site build — single entry point.

Runs every generator in the one order that produces a correct site. Replaces the
"remember to run five scripts in the right sequence" failure mode described in
the original handoff.

    python3 generators/build.py              # build into <repo>/site
    NP_ROOT=/tmp/out python3 generators/build.py   # build somewhere else

Exit code is non-zero if any stage fails, so CI can gate on it.
"""
import os
import pathlib
import re
import runpy
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
ROOT = pathlib.Path(os.environ.get("NP_ROOT") or (REPO / "site"))

# Order matters. build_site defines shell() and writes assets; everything else
# imports from it. Articles must build after build_pages2 so the hub and sitemap
# already exist for them to slot into.
STAGES = [
    ("build_site.py", "assets: style.css, app.js, favicon"),
    ("build_pages.py", "homepage"),
    ("build_pages2.py", "services, about, hub, resources, contact, 404, robots, sitemap"),
    ("build_articles_shell.py", "25 article pages"),
    ("build_areas.py", "service-area hub + town pages"),
]


def run(script: str, note: str) -> None:
    print(f"\n\033[1m── {script}\033[0m  ({note})")
    r = subprocess.run([sys.executable, str(HERE / script)], cwd=str(HERE),
                       capture_output=True, text=True)
    if r.stdout.strip():
        print("   " + r.stdout.strip().replace("\n", "\n   "))
    if r.returncode != 0:
        print("   " + (r.stderr.strip() or "no stderr").replace("\n", "\n   "),
              file=sys.stderr)
        raise SystemExit(f"BUILD FAILED at {script} (exit {r.returncode})")


def clean() -> None:
    """Empty the output directory before building.

    Everything in site/ comes from either a generator or generators/static/, so
    wiping it is safe and it is the only way to guarantee the deploy contains no
    stale files. Without this, renaming or dropping an asset leaves the old copy
    behind forever — it is still on disk, still committed, and still served.
    (That is exactly how a superseded 1.2MB three.module.js survived a rebuild
    here and would have shipped.)
    """
    if not ROOT.exists():
        return
    dupes = [f for f in ROOT.rglob("*")
             if f.is_file() and re.search(r" \d+(\.[A-Za-z0-9]+)?$", f.name)]
    if dupes:
        print(f"  NOTE: {len(dupes)} iCloud/Finder conflict copies found and removed "
              f"(e.g. {dupes[0].name}). This repo is on an iCloud-synced Desktop; "
              f"see README.")
    removed = 0
    for child in sorted(ROOT.iterdir()):
        if child.is_dir():
            removed += sum(1 for _ in child.rglob("*") if _.is_file())
            shutil.rmtree(child)
        else:
            removed += 1
            child.unlink()
    print(f"cleaned {removed} file(s) from previous build")


def main() -> None:
    print(f"Output: {ROOT}")
    ROOT.mkdir(parents=True, exist_ok=True)
    clean()
    for script, note in STAGES:
        run(script, note)

    # Files the generators do not write but the deploy needs. Kept in the repo
    # under generators/static/ so they are versioned rather than hand-placed.
    static = HERE / "static"
    if static.is_dir():
        print("\n\033[1m── static passthrough\033[0m")
        for src in sorted(static.rglob("*")):
            if src.is_file() and src.name != ".DS_Store":
                dst = ROOT / src.relative_to(static)
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                print(f"   {src.relative_to(static)}")

    pages = sorted(ROOT.rglob("*.html"))
    print(f"\n\033[1m✓ build complete\033[0m — {len(pages)} HTML pages in {ROOT}")


if __name__ == "__main__":
    main()
