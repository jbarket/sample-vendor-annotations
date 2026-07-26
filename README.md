# sample-vendor-annotations

Machine-readable facts about how sample vendors structure their libraries:
pack boundaries, folder grammar, naming conventions, format trees. The stuff
every sample-management tool re-discovers by hand, captured once as data.

A vendor ships a library with *some* internal logic — "top-level dirs are
packs", "WAV/ is the canonical audio, the rest are parallel format exports",
"one-shots live in a folder called `01. Individual Hits`... or `Individual
Hits`... or `01. One Hits`, depending on the pack's vintage". None of it is
documented, all of it is inferable, and everyone infers it separately.

This repo is the shared inference. Tools consume it to browse by pack,
select by category ("one-shots", "loops") instead of by glob archaeology,
ignore sidecar noise, and apply vendor-aware rename rules.

## What an annotation is

**Facts, not taste.** "SFM pitched files end `_<note><octave>` and use `#`
for sharps" is a fact — it ships here. "The 808 kick sounds better with the
long decay" is taste — it stays local. The test: two independent observers
looking at the same library would write the same annotation.

Every fact is *observed*, from a real copy of the library, and annotations
carry the observation date. Vendors re-cut their packs; annotations note the
variants they've seen rather than pretending one truth.

## Layout

```
vendors/<slug>/vendor.toml   # the annotation: grammar, formats, categories
SCHEMA.md                    # field-by-field format definition
```

## Consumers

Built for [materialized-tunes](https://github.com/jbarket/materialized-tunes)
(pack-first browsing, device-aware selection, rename policies), but there's
nothing mtunes-specific in the data: it's TOML describing directory trees.

## Contributing

Own a library from a vendor that isn't here? Write its `vendor.toml` from
what you can actually see on disk, note the date and rough library version,
and open a PR. Partial annotations are welcome — a correct `[packs]` section
with no `[categories]` beats no annotation. Corrections beat both: if your
copy of a pack disagrees with an annotation, that's a variant worth
recording, not a conflict.
