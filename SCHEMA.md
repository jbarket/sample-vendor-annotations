# vendor.toml schema (v0)

One file per vendor at `vendors/<slug>/vendor.toml`. Every section is
optional except `[vendor]` — annotate what you've observed, skip what you
haven't. All glob patterns are [doublestar](https://github.com/bmatcuk/doublestar)
syntax, matched against paths relative to the vendor's library root.

## [vendor]

```toml
[vendor]
name     = "Samples From Mars"    # display name
slug     = "samples-from-mars"    # dir name; lowercase, hyphens
aliases  = ["SFM"]                # what people actually call it
homepage = "https://samplesfrommars.com"
observed = 2026-07-18             # date the facts below were last checked
                                  # against a real copy of the library
```

## [packs] — where pack boundaries are

```toml
[packs]
grammar     = "top-level-dirs"    # each top-level dir is one pack
dir_pattern = "* From Mars"       # naming convention; not a guarantee —
                                  # note exceptions in `exceptions`
exceptions  = ["Databenders Toolkit"]
sibling_zip = "archival-original" # <pack>.zip beside the pack dir is the
                                  # vendor's original download, not a pack
zip_name_grammar = "lower_snake or lower-hyphen of the dir name"
```

`grammar` values: `top-level-dirs` (the only one defined so far; propose
others as vendors demand them).

## [formats] — canonical audio vs parallel exports

Vendors ship the same sounds cut for many hosts. One tree is the canonical
audio; the rest are format exports and sidecar files that audio tools
should skip.

```toml
[formats]
canonical_dir      = "WAV"        # per-pack dir holding plain audio
parallel_dirs      = ["Ableton Live", "Kontakt", "Maschine", "..."]
sidecar_extensions = [".asd", ".als", ".nki", "..."]  # metadata riding
                                  # alongside audio anywhere in the tree
```

## [[category]] — folder grammar → shared vocabulary

The payoff section: maps a vendor's (inconsistent) folder names to a
shared category vocabulary, so "give me the one-shots" needs no globs.
`match` patterns apply to directory names under the canonical tree, at any
depth. A vendor's variants stay visible — they're the observed fact.

Vocabulary so far: `one-shots`, `loops`, `kits`, `multisamples`, `fx`.
Extend it in a PR when a vendor genuinely doesn't fit.

```toml
[[category]]
id    = "one-shots"
match = ["*Individual Hits*", "*One Shots*", "*One Hits*"]

[[category]]
id             = "loops"
match          = ["*Loop*", "*Full Beats*"]
dedicated_packs = ["* Loops From Mars"]   # whole packs that ARE this category
```

## [naming] — filename grammar

Conventions inside filenames, for tools that rename for constrained
displays and filesystems (note-aware sanitizing, distinguishing-first
reordering, common-token stripping).

```toml
[naming]
dir_order_prefix = "NN. "         # "01. Individual Hits" — ordering only,
                                  # safe to strip for display
note_suffix      = "_<note><octave>"  # pitched files: "..._C#4.wav";
                                  # sharps use '#'
take_suffix      = " NN"          # variations count up at the tail —
                                  # the distinguishing token is LAST
```

## Pack files — `vendors/<vendor>/packs/<slug>.toml`

One file per pack. Two audiences at once: display metadata for UIs, and a
machine-readable map of the pack's layout. Generated stubs (see
`tools/generate-packs.py`) carry `[pack]` + `[identity]` and a commented
directory skeleton; humans add `[meta]` and the `[[dir]]` map.

### [pack]

```toml
[pack]
name = "Acid From Mars"
slug = "acid-from-mars"
dir  = "Acid From Mars"    # dir name as the vendor ships it
url  = "https://samplesfrommars.com/products/acid-from-mars"
archives = ["acid_from_mars.zip"]  # download names as the vendor ships them —
                                   # the dumbest identity signal there is, and
                                   # it catches everyone who unzips-and-leaves-it
provider = "Sample Tools by Cr2"   # for distributor vendors (Splice): the
                                   # label the pack is BY; omit when the
                                   # vendor is the label
samples_listed = 315               # the vendor's own sample count — the
                                   # honest denominator when local copies
                                   # are partial (Splice downloads
                                   # per-sample); omit for unzip-the-whole-
                                   # pack vendors
```

### [meta] — display metadata, og:-style

Lifted from the vendor's product page (OpenGraph tags exist for exactly
this). For UI cards: image, type, blurb.

```toml
[meta]
title       = "ACID FROM MARS"   # og:title as published
type        = "product"          # og:type
image       = "https://samplesfrommars.com/cdn/shop/products/acid-from-mars_grande.jpg"
description = "TB-303 through tubes and tape — acid bass, spacey organs, subs, weirdo FX."
```

No prices — they date instantly and are one click away via `url`.

### [identity] — "oh, you have this pack"

Computed over **audio files only** (`.wav`/`.aif*`), because format trees
(Ableton/Kontakt/…) and docs get pruned by users; the audio is the pack.
Path-free, so renames and re-organizations don't break recognition.

```toml
[identity]
algo        = "sha256-sorted-v1"
audio_files = 533
audio_bytes = 1372294742
digest      = "<sha256 of the manifest file bytes>"
anchors     = ["<first 8 sha256s of the sorted list>"]
manifest    = "manifests/acid-from-mars.sha256"
```

The manifest sidecar is the full sorted list of per-file content SHA-256s,
one hex digest per line. Match semantics for consumers:

- **exact**: your computed digest equals `digest`
- **partial**: fraction of manifest lines present in your catalog
  ("you have 96% of Acid From Mars") — report the fraction, don't round
  it to a lie
- **probable**: ≥2 `anchors` present — cheap indexed lookup across all
  packs without loading manifests; confirm with the manifest before
  asserting

### [[dir]] — the layout map

What's where and why. Paths are relative to the pack dir, globs allowed.
Semantics: a file's governing entry is the **deepest matching** `[[dir]]`;
`category` comes from the governing entry; `tags` are the **union** of
every matching prefix's tags; `desc` is for humans and UIs. Where no
`[[dir]]` claims a path, the vendor-level `[[category]]` rules still
apply — pack maps override, they don't replace.

`role` marks structural facts: `canonical-audio` (the real content),
`format-tree` (parallel DAW/sampler exports — audio tools skip these),
`docs` (manuals, artwork). `category`/`tags` describe musical content and
usually live under the canonical tree.

```toml
[[dir]]
path = "WAV"
role = "canonical-audio"

[[dir]]
path     = "WAV/Acid Synths"
category = "multisamples"
tags     = ["303", "acid"]
desc     = "Multisampled TB-303 patches, per-note, tube/tape processed"

[[dir]]
path     = "WAV/Acid Synths/Basic Sub"
tags     = ["sub", "bass"]
```

This is where the free stuff comes from: **views by pack** (identity),
**views by category** (dir map + vendor rules), **tags** (path unions) —
any consumer that can walk a tree gets them without understanding the
vendor's naming.

## What does not belong

- Taste ("the good kicks are in folder X")
- Per-user state (ratings, favorites)
- Anything you haven't verified against a real copy of the library
- Content hashes (planned — content-SHA pack identity so declared packs
  are recognizable across users — but the shape isn't settled; don't
  freelance it)
