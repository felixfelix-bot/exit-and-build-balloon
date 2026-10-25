# Balloon path — DEFERRED

**Status:** deferred, not cancelled. Moved out of the event README on 2026-10-25
because the event deliverable is now the **mast-based relay test**, not a flight.
Nothing here is required for Exit & Build 6.

**Why deferred:** see [`RECOMMENDATION-postpone-and-minimum.md`](RECOMMENDATION-postpone-and-minimum.md).
Short version — the flight board (v10, in `balloon-fresh`) is at *"placement
approved, routing not started"* with zero copper routed, and cannot reach 5 Nov.
The balloon is the least proven part of the system and the event does not need it.

**Reinstating this path** needs one thing: a working v10 flight board, plus a
chosen later event date. Both are outside this repo.

---

## Asset comparison — what lifts the relay

The **radio payload is the same in all three paths**. Only the thing that lifts it
(or doesn't) changes. Prices are indicative; **UNVERIFIED** means no live price was
read.

| | **MAST** | **BALLOON** (latex sphere) | **HELIKITE** |
|---|---|---|---|
| **Airspace permission** | **none required** | landowner permission | landowner permission |
| **Wind tolerance** | **structural, ~25 kn** | ~5.7 kn at 45° blow-over | **holds into wind** |
| **Effective height** | exact, as built | blows down: **12 ft at 8 kn** | holds |
| **Lead time** | **US domestic, days** | **US retail, days** | **UK, 1–3 wk + customs → likely MISSES 5 Nov** |
| **Indicative cost** | **~$30–120** | **~$250–450** | **UNVERIFIED** (no price published) |
| **Helium needed** | none | **~30 ft³** balloon-grade | yes, similar |
| **Fails if** | pole unavailable | wind >6 kn | ships late |
| **Regulatory surface** | **none below 200 ft** | 101 Subpart B *if* >6 ft / >115 ft³ | same |

> **Only the mast removes the permission question entirely** — 14 CFR Part 101
> governs *balloons*, not structures. The mast is the event path; the other two
> columns are here for the later event.

---

## Path B — BALLOON, latex sphere (headline ~$250–450)

| Item | Qty | Indicative | Where | Lead time |
|---|---|---|---|---|
| 36–48 in round **latex** balloon | 4–6 | ~$10–30 | US party retail | days |
| **HI-FLOAT** barrier coat | 1 kit | ~$10–20 | same | days |
| 18 in foil spares | 4 | ~$5–10 | same | days |
| **Helium, balloon-grade ≥99.99%**, ~30 ft³ | 1 cylinder | **$100–250** incl. deposit/hazmat | **Airgas San Antonio (210) 337-7255**; nexAir; Linde; Matheson | days, will-call |
| *(alt: Balloon Time 14.9 ft³)* | — | *$75.99 = $5.10/ft³, ~15× base price — one-hour demo only* | Tractor Supply Bandera | days |
| Tether 1.5 mm Dyneema 200 ft + 1.0 mm 300 ft | 2 | ~$45–65 | arborist / marine | days |
| Swivels, carabiners, streamers | 1 set | ~$20 | marine | days |
| Anchors + anemometer | 1 set | ~$90 | Amazon US | days |

⚠️ Consumer party tanks are **≥80 % helium only** (a 20 % lift penalty) — buy
industrial balloon-grade. Site lift is **28 g/ft³** at 471 m, not sea-level.

**The 4-day hang-time requirement:** ~30 ft³ balloon-grade at a 20 %/day top-up,
with a morning lift-weigh and an afternoon check. Full ritual in
`../shopping-list.md` §5.

---

## Path C — HELIKITE (cost UNVERIFIED)

| Item | Qty | Indicative | Where | Lead time |
|---|---|---|---|---|
| Helikite, sub-200 g payload, 150 ft | 1 | **UNVERIFIED** | **Allsopp Helikites (UK)** https://www.helikites.com/shop — `info@helikites.com`, +44 1425 654967 | ⚠️ **1–3 weeks + customs** |
| US reseller | — | — | **NONE FOUND** (searched 2026-10-23) | — |
| Tether, anchors, anemometer | — | ~$150 | as Path B | days |
| Helium | — | ~$100–250 | as Path B | days |

**Gate: only order if the quote shows a US warehouse or ≤5-day transit.**
Otherwise it cannot make an event on this timeline.

---

## The wind problem, precisely

A spherical tethered balloon blows downwind until tension balances drag,
`tan θ = drag ÷ free lift`. Measured venue wind (KERV ASOS, Nov 2019–2025,
158,912 obs): **mean daylight 7.6 kn, ≥8 kn in 50 % of daylight hours.**

| Wind | Foil cluster angle | Effective height (150 ft line) |
|---|---|---|
| 2 kn | 37° | 119 ft |
| 3 kn | 60° | 76 ft |
| 5 kn | 78° | **31 ft** |
| 8 kn | 85° | **12 ft** |

Adding balloons does not fix it — drag scales with count exactly as lift does.
**A foil cluster is a low-wind-only, wrong-shaped asset.**

**45° blow-over wind by asset:**

| Asset | 45° blow-over at |
|---|---|
| 36 in foil cluster (4 balloons) | 2.3 kn |
| 36 in latex sphere | ~5.7 kn |
| 48 in sphere | ~8.9 kn |
| 60 in sphere | ~10.7 kn |
| **Helikite** | *aerofoil — holds altitude into wind* |

---

## Why the balloon still matters (so this file doesn't read as a retreat)

The balloon is not a worse idea than the mast — it is a **different height**, and
height is the whole point:

- At **200 m** ground separation the direct path already has **51.8 dB** of margin;
  the relay returns only +5.2 dB and *halves* throughput. Flying there is a net loss.
- At **800 m blocked by ≥6 m** of terrain or cedar, the relay recovers **14–20 dB**
  of knife-edge loss. **That is the only regime where the balloon wins.**
- A 20–40 ft mast over a 6 m canopy gives ~20 ft of clearance — not enough for full
  first-Fresnel clearance at 400 m. **So the mast buys relay + measurement, probably
  not the full over-the-trees link.** The balloon is what closes that gap.

**Deferred, not dropped.** Fly it when the flight board is real and the event is
chosen — with the relay already proven, so a failure on the day is a *balloon*
failure and nothing else.

---

## Related

| File | What it is |
|---|---|
| `RECOMMENDATION-postpone-and-minimum.md` | Why this path is deferred |
| `ASSET-STRATEGY.md` | Full lifting-asset decision record (D8a/D8b) |
| `MAST-SPEC.md` | The event path — mast spec + verified vendor survey |
| `SITE-RULES-AND-FAA.md` | 14 CFR 101 Subpart B moored-balloon rules |
| `../reports/BALLOON-LOGISTICS-TETHER-2026-11.md` | Balloon/helium/tether logistics |
| `../shopping-list.md` §5 | Helium sourcing + the 4-day top-up ritual |
| `../docs/OUTBOUND-DRAFTS.md` | **DRAFTS, NOT SENT** — Helikite quote request, organiser airspace message |
