#!/usr/bin/env python3
"""Generate pack stubs + identity manifests from an mtunes catalog.

Reads a catalog JSONL (path/size/sha256 per line), groups audio files by
top-level directory (the `top-level-dirs` pack grammar), and emits:

  vendors/<vendor>/manifests/<slug>.sha256   sorted content SHAs, one/line
  vendors/<vendor>/packs/<slug>.toml         [pack] + [identity] stub with a
                                             commented dir skeleton to annotate

Existing pack TOMLs are left alone (manifests are always regenerated —
they're derived data). Identity covers audio files only: format trees and
docs get pruned by users; the audio is the pack.

Usage:
  generate-packs.py --catalog sfm.jsonl --vendor vendors/samples-from-mars \
      [--url-base https://samplesfrommars.com/products/] [--check-urls] \
      [--observed 2026-07-18]
"""

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

AUDIO_EXT = {".wav", ".aif", ".aiff"}


def slugify(name: str) -> str:
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def toml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--vendor", required=True, help="vendors/<slug> directory")
    ap.add_argument("--url-base", default="", help="product URL prefix to guess <url-base><slug>")
    ap.add_argument("--check-urls", action="store_true", help="HEAD-check guessed URLs; only verified ones land in stubs")
    ap.add_argument("--observed", default="", help="observation date stamped into stubs (YYYY-MM-DD)")
    args = ap.parse_args()

    vendor = Path(args.vendor)
    packs_dir = vendor / "packs"
    manifests_dir = vendor / "manifests"
    packs_dir.mkdir(parents=True, exist_ok=True)
    manifests_dir.mkdir(parents=True, exist_ok=True)

    audio = defaultdict(list)   # top dir -> [(sha, size)]
    dirs = defaultdict(lambda: defaultdict(int))  # top dir -> "a/b" 2-level subpath -> file count
    archives = defaultdict(list)  # pack slug -> [zip filename] (sibling archival originals)
    for line in open(args.catalog):
        e = json.loads(line)
        parts = e["path"].split("/")
        if len(parts) < 2:
            # Top-level zips are archival originals; their names are the
            # dumbest possible identity signal (unzip-and-leave-it users).
            if len(parts) == 1 and parts[0].lower().endswith(".zip"):
                archives[slugify(parts[0][:-4])].append(parts[0])
            continue
        top = parts[0]
        sub = "/".join(parts[1:3][: len(parts) - 1])
        if sub:
            dirs[top][sub] += 1
        if Path(parts[-1]).suffix.lower() in AUDIO_EXT:
            audio[top].append((e["sha256"], e["size"]))

    url_ok = {}
    if args.check_urls and args.url_base:
        import concurrent.futures
        import urllib.request

        def check(slug: str) -> tuple[str, bool]:
            url = args.url_base + slug
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "sample-vendor-annotations/1.0"})
            try:
                with urllib.request.urlopen(req, timeout=10) as r:
                    return slug, r.status == 200
            except Exception:
                return slug, False

        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
            for slug, ok in ex.map(check, [slugify(t) for t in audio]):
                url_ok[slug] = ok

    made = skipped = 0
    for top in sorted(audio):
        # Dedupe by content: vendors ship the same WAV in several format
        # trees, and identity is about content presence, not copy count.
        uniq = dict(audio[top])
        shas = sorted(uniq)
        total = sum(uniq.values())
        slug = slugify(top)

        manifest = manifests_dir / f"{slug}.sha256"
        body = ("\n".join(shas) + "\n").encode()
        manifest.write_bytes(body)
        digest = hashlib.sha256(body).hexdigest()

        toml = packs_dir / f"{slug}.toml"
        if toml.exists():
            skipped += 1
            continue

        lines = [
            "# Generated stub — [pack]/[identity] are computed; add [meta] from the",
            "# product page and grow the [[dir]] map from the skeleton below.",
            "",
            "[pack]",
            f"name = {toml_str(top)}",
            f"slug = {toml_str(slug)}",
            f"dir  = {toml_str(top)}",
        ]
        if args.url_base and url_ok.get(slug):
            lines.append(f"url  = {toml_str(args.url_base + slug)}")
        elif args.url_base:
            lines.append(f"# url guess (unverified): {args.url_base}{slug}")
        if archives.get(slug):
            names = ", ".join(toml_str(a) for a in sorted(archives[slug]))
            lines.append(f"archives = [{names}]")
        if args.observed:
            lines.append(f"observed = {args.observed}")
        lines += [
            "",
            "[identity]",
            'algo        = "sha256-sorted-v1"',
            f"audio_files = {len(shas)}",
            f"audio_bytes = {total}",
            f"digest      = {toml_str(digest)}",
            "anchors     = [",
        ]
        lines += [f"  {toml_str(s)}," for s in shas[:8]]
        lines += [
            "]",
            f"manifest    = {toml_str(f'manifests/{slug}.sha256')}",
            "",
            "# Layout skeleton (top two levels, file counts) — annotate with [[dir]]:",
        ]
        for sub, n in sorted(dirs[top].items(), key=lambda kv: (-kv[1], kv[0]))[:20]:
            lines.append(f"#   {n:6d}  {sub}")
        toml.write_text("\n".join(lines) + "\n")
        made += 1

    print(f"{made} stubs written, {skipped} existing kept, {len(audio)} manifests regenerated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
