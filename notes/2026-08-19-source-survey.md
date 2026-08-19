# Link-out source survey — 2026-08-19

Research pass behind SCHEMA `[acquisition]` / materialized-tunes SPEC §11.6:
which big sources of free (and paid) sample packs can be pointed at without
annoying anyone or breaking laws. "Verified" = page fetched on 2026-08-19;
"search-only" = from search snippets; "NOT VERIFIED" = fetch failed
(403/404). Verdicts are about *pointer targets*, not about whether the
samples are good. **Green** = link the product/pack page freely; **yellow**
= page-level only / caveat; **red** = never a pointer (may still be where
you *find* the vendor URL).

Standing rule that fell out of every green entry: **link the page, never
the file.** MusicRadar CDN zips, Goldbaby's MediaFire links, Legowelt's
WeTransfer links all rotate or bypass the page the vendor wants you on.
Lint L2 enforces the extension half of that; the rest is the `observed`
date and `--live`.

## Summary

| Source | Type | Scale | License | Gate | Verdict | Verified |
|---|---|---|---|---|---|---|
| MusicRadar / SampleRadar | free archive | ~99k samples, hundreds of packs, live 2026 | royalty-free, "don't re-distribute" | none | GREEN (article page; not the CDN zip) | yes |
| Samples From Mars | house, free shelf | 9 $0 products | RF, no redist, music-only | $0 checkout (email) | GREEN | yes |
| Goldbaby | house, free shelf | ~40 packs | RF, no redist, **no AI/ML training** | none | GREEN (freestuff page, not MediaFire) | yes |
| Wave Alchemy | house | few | RF, text unverified | none / Loopmasters acct | YELLOW | partial |
| Loopmasters | **distributor** | 12 free + label samplers | RF, no isolation/competitive | account + $0 cart | GREEN | partial |
| Native Instruments Komplete Start | vendor free | bundle (instruments mostly) | RF, no standalone redist | account + Native Access | GREEN (flag: containers) | yes |
| Ableton packs | vendor free | several (.alp) | EULA | account | YELLOW | no |
| Spitfire LABS | instruments | 80+ | EULA, no isolation | account | flag / omit | no |
| Splice free packs | **distributor** | many | RF, no isolation / repack | account | GREEN | partial |
| Cymatics | vendor free | ~60 | RF, no redist (license only on request) | **email** | YELLOW | partial |
| Black Octopus | vendor free | several | RF commercial OK | $0 checkout? | GREEN (prov.) | no |
| Ghosthack | vendor free | 25+ | RF | **email** | YELLOW | yes |
| Function Loops | vendor free | 10 | RF | none | GREEN | yes |
| 99Sounds | vendor free | dozens | RF, no redist | none | GREEN | yes |
| Bedroom Producers Blog (own packs) | vendor free | ~8 | RF, no redist | none | GREEN (own packs only; for roundups point at the vendor) | partial |
| Reverb Drum Machines | vendor free | 53 packs / 50+ machines | RF (text not found) | Reverb account | GREEN (prov.) | no |
| MusicTech → BandLab Sounds | distributor | 18 packs | RF | BandLab account | YELLOW | no |
| Future Music / FileSilo | defunct (2024) | — | subscriber code | code | RED | no |
| Sample Magic | via Splice | — | RF | account | YELLOW (Splice label page) | no |
| Blu Mar Ten (Bandcamp) | artist free | 1–2 packs | "not to be sold"; **samples of commercial records, at your own risk**; ARR | none/email | YELLOW — legit pointer, uncleared content | yes |
| Legowelt | artist free | ~18 packs | informal ("donate for karma") | none (WeTransfer) | GREEN (page only) | yes |
| Pianobook | instruments, user-uploaded | many | RF, provenance disclaimed | account | YELLOW | yes |
| Decent Samples | instruments | — | — | — | NOT VERIFIED | no |
| Freesound | per-sound | huge | CC0 / CC-BY / CC-BY-NC mixed | account | GREEN (per-item; use API not crawl) | yes |
| Looperman | user loops | huge | RF user-granted; acapellas NC | account | YELLOW | yes |
| archive.org "drum-machines-collection" etc. | anon mirror | 48k samples | none stated | none | **RED** | yes |
| KB6 (samples.kb6.de) | aggregator | 332 machines | claims RF; "found on the internet" | none | **RED / grey** | yes |
| drumkito / free-sample-packs.com / soundpacks.com / freewavesamples etc. | re-hosters | — | — | — | **RED** as targets | search-only |
| Roland Cloud sample packs | paid | many | RF (paid) | membership | GREEN (paid) | no |
| Korg volca packs | vendor free | few | software EULA click-through | click-through | YELLOW | yes |
| Elektron soundpacks | vendor free | 3 | unstated | account | YELLOW | yes |
| Polyend Palettes | vendor | paid + bonus | — | account | YELLOW | no |
| Teenage Engineering OP-1 | vendor | 2 | unstated | none | YELLOW | yes |
| Novation Components | vendor free | 2 | RF | account | GREEN (prov.) | no |
| Arturia | — | none | — | — | omit | no |

## Licensed redistributors (fine to point at as `class = "distributor"`)

Loopmasters (label samplers / free shelf), Splice Sounds, BandLab Sounds,
ADSR, LANDR Samples, Loopcloud — storefronts with their own license over
other labels' material. Bandcamp / Gumroad / itch.io are *self*-distribution
(the vendor's own page on a platform) — treat the platform host as one of
the vendor's `domains`, as done for Blu Mar Ten.

## Classic drum-machine archives — triage

Legit: Reverb Drum Machines, Goldbaby freebies, SFM free 808/MPC60/101,
BPB Cassette 808/909/606, Legowelt, Wave Alchemy RYTM kicks, the hardware
vendors' own packs. Grey → avoid: KB6, the anonymous archive.org
compilations (almost certainly re-ups of the above), aggregator mirrors.
Individual hardware rips: the sound-recording right in the rip is the
ripper's; link only if the ripper is the publisher and it's their page.

## Etiquette

No surveyed site states a deep-link prohibition or runs hotlink
protection. Walls (Cymatics/Ghosthack email; Loopmasters/Splice/Reverb/
Ableton/NI/Spitfire/Pianobook/Freesound/Looperman account) are theirs —
link to the walled page, never around it. Freesound asks bulk users to use
the API / Data Packs. Goldbaby (and others) forbid AI/ML training use —
relevant if anyone ever tries to fingerprint by downloading.

## License enum (adopted in SCHEMA `[acquisition] license`)

- `royalty-free` — use in music incl. commercial OK; no standalone
  redistribution / repackaging. The overwhelming majority (SFM, Goldbaby,
  Loopmasters, Splice, NI, Cymatics, Ghosthack, Function Loops, 99Sounds,
  BPB, SampleRadar). Vendor-specific riders (music-only, no-ML,
  no-isolation) are prose in the vendor's terms, not enum values.
- `cc0`, `cc-by`, `cc-by-nc` — Freesound, some Pianobook.
- `informal-free` — "free, use it, donate if you like", no written terms
  (Legowelt, TE). Treated as royalty-free in practice; recorded as such so
  nobody mistakes it for a licence.
- `uncleared` — all rights reserved / at-your-own-risk / contains
  third-party material the publisher didn't clear (Blu Mar Ten), or a
  software EULA standing in for a sample licence (Korg click-through).
- `purchase` — terms come with the sale (houses' paid catalogs, Roland
  Cloud).
- `unknown` — not yet read.

Orthogonal, not enum: `gate` (none / email / account / purchase), and
container format is the pack's business (`[formats]`), not the pointer's.

## Details per source

Verification date for everything: 2026-08-19.

### MusicRadar / SampleRadar
Hub: https://www.musicradar.com/news/tech/free-music-samples-royalty-free-loops-hits-and-multis-to-download-sampleradar ; packs under `musicradar.com/music-tech/samples/sampleradar-*`. Future plc's archive; hub says 98,823 free sample downloads, "last updated June 26, 2026". License sentence on every pack page: "Because they're royalty-free, you're welcome to use the samples in your music in any way you like - all we ask is that you don't re-distribute them." Files are direct zips on `cdn.mos.musicradar.com/audio/` — link the article, not the zip. No gate.

### Samples From Mars
https://samplesfrommars.com/collections/free (9 $0 products; `/pages/free-samples` 404s). T&C: 100% royalty-free incl. commercial releases; no redistribution "free or paid, individually or as a group"; music only ("not in any website, application, or software"); non-transferable. Shopify $0 checkout captures email.

### Goldbaby
https://www.goldbaby.co.nz/freestuff.html (~40 packs, MediaFire-hosted by the vendor). Terms (https://www.goldbaby.co.nz/termsandconditio.html): commercial compositions OK, no redistribution in any reformatted form, **no ML/AI training without permission**. No gate. Link the freestuff page; MediaFire URLs rotate.

### Wave Alchemy
https://www.wavealchemy.co.uk/blog/free-analog-rytm-kicks/ (own-host zip). T&C page is generic store terms; sample licence ships inside packs (unverified). Older freebies via Loopmasters label samplers (account).

### Loopmasters / Loopcloud
Free shelf https://www.loopmasters.com/genres/136-Free-Samples (12 items at $0); Label Samplers https://www.loopmasters.com/genres/91-Label-Samplers — third-party labels' free samplers under Loopmasters' licence: a genuine licensed distributor. Licence: royalty-free incl. free packs; "may not use the Sounds in isolation as sound effects or as loops or within any competitive products". Account + $0 cart. Licence page 403'd to the fetcher.

### Native Instruments — Komplete Start
https://www.native-instruments.com/en/products/komplete/bundles/komplete-start/ ; EULA allows commercial use of samples/instruments/presets; forbids standalone distribution and building sound libraries. NI account + Native Access. Mostly instruments in proprietary containers — awkward to fingerprint.

### Ableton free packs — NOT VERIFIED (site refused fetch). Account-gated `.alp`; EULA governs.

### Spitfire LABS — instruments, proprietary container, EULA requires combination with other sounds; out of scope for a WAV registry.

### Splice
https://splice.com/sounds/free-packs (SPA, not renderable headless). Licensing FAQ https://support.splice.com/en/articles/8652642-splice-sounds-licensing-faq : commercial OK; no sublicensing in isolation, no repacking; perpetual after cancellation. Account. Distributor for Sample Magic, SFM, Black Octopus etc.

### Cymatics
https://cymatics.fm/pages/free-download-vault (~60 packs). Licence page is a request form; Scribd copy says RF, no redistribution/repackaging, single user. Email/login gate; heavy funnel.

### Black Octopus — https://blackoctopus-sound.com/free-downloads/ 403'd. Search: RF, commercial OK, "no strings attached". Provisional green.

### Ghosthack — https://www.ghosthack.de/free_sample_packs/ (25+ packs, ~0.7–1 GB each). RF usage licence, copyright retained, no credit needed. Newsletter email gate.

### Function Loops — https://www.functionloops.com/free-samples.html (10 packs). "100% royalty-free … commercial projects with no strings attached." No gate stated.

### 99Sounds — https://99sounds.org/ ; licence https://99sounds.org/license/ : personal + commercial projects OK; no selling/redistributing audio on its own; credit optional; no noise/sleep-sound apps. No gate.

### Bedroom Producers Blog — https://bedroomproducersblog.com/free-samples/ ; own packs (Cassette 808/909/606, C64 Sessions, Analog Kicks): free incl. commercial, no redistribution. For BPB roundups of third-party packs, point at the vendor, not BPB.

### Reverb Drum Machines — https://reverb.com/software/samples-and-loops/reverb/3514-reverb-drum-machines-the-complete-collection (403'd). 53 packs, 24-bit WAV, 1.4 GB, free since 2019, Reverb-commissioned recordings; account required; licence text not found.

### MusicTech / Future Music — Future Music ceased Sept 2024; FileSilo content subscriber-code-gated: red. MusicTech free packs via BandLab Sounds (18 packs; account): yellow.

### Sample Magic — folded into Splice; samplemagic.com is a shell. Splice label page.

### Blu Mar Ten — https://blumarten.bandcamp.com/album/blu-mar-ten-jungle-jungle-1989-to-1999-samplepack (650+ items, 390 MB, 16-bit). "created for fun and is not to be sold"; "These are all samples (or samples of samples) from commercially released tracks, use them in your productions at your own risk"; all rights reserved. Legit pointer; content is uncleared → `license = "uncleared"`.

### Legowelt — https://legowelt.org/samples/ (~18 packs). "free to download and use in your productions … donate some $$$ for good karma." All downloads are WeTransfer links: pointer is the `/samples/` page only.

### Pianobook — https://www.pianobook.co.uk/faq/ : user-uploaded instruments; commercial use allowed by uploaders; "cannot guarantee sample packs uploaded to this site are copyright free". Account. Decent Samples free category 403'd.

### Freesound — https://freesound.org/help/faq/ : per-sound CC0 / CC-BY / CC-BY-NC (+ legacy Sampling+); account to download; bulk via API / Data Packs, not crawling. Link sound/pack pages.

### Looperman — https://www.looperman.com/help/terms : user-uploaded loops, RF incl. commercial for registered users; acapellas NC by default; login to download. Provenance is the uploader's word.

### archive.org — https://archive.org/details/drum-machines-collection (3.8 GB, 470 zips, anonymous uploader, no rights statement; front-end drum-machine.app). Other IA sample compilations likewise anonymous. Red unless a rights-holder uploaded it with a licence.

### KB6 — https://samples.kb6.de/ (332 machines, donations for bandwidth). KVR thread https://www.kvraudio.com/forum/viewtopic.php?t=412122 : "a collection of samples found over the internet", uncredited third-party libraries. Red/grey — the "everyone knows where" class.

### Aggregators — drumkito.com, free-sample-packs.com, polynominal.com, freewavesamples.com, soundpacks.com, fattony.de: re-hosters; fine for *finding* the vendor URL, never as the pointer.

### Hardware vendors
- Roland Cloud sample packs: RF WAV but Pro/Ultimate membership or Lifetime Key — paid.
- Korg volca packs: free on korg.com support downloads behind a *software* licence click-through (https://www.korg.com/us/support/download/software/0/370/4607/) — terms written for software, not music use.
- Elektron https://www.elektron.se/shop/soundpacks : Twinshot / EuroKlang / Super Glue free, device-format, no licence text on page.
- Polyend Palettes https://polyend.com/palettes/ paid + monthly bonus; Backstage community freebies; coupon-gated freebies are time-limited.
- Teenage Engineering https://teenage.engineering/downloads/op-1/sound-packs : 2 OP-1 packs, no licence text.
- Novation: Circuit Rhythm Sample Expansion (550+) and Heritage Sample Pack (842 MB) via Components (account); RF per search.
- Arturia: no free WAV program; omit.
