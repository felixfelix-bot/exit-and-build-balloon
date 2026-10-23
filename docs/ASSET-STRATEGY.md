# Asset strategy — Helikite vs latex sphere vs mast

**Decision:** D8a (Helikite primary + mast control) is **REVISED** by D8b below.
**Operator reframe (2026-10-23):** the boards are in Germany and must reach Texas
on time; the mast needs no permission, so it should be **primary, not control**.

---

## 1. The USA/Germany inventory problem

The E80 boards are in **Germany**. The event is in **Texas**. Anything flying at
the event has to be *in Texas*, which means either shipping the bench inventory
across the Atlantic or ordering fresh to a US address.

This is not just logistics — it changes which item is on the critical path.

| Item | Where | Ships to Texas? | Lead time |
|---|---|---|---|
| E80-900MBL-02 eval board | **EBYTE store, China** | yes | **14–37 working days → arrives 12 Nov – 17 Dec. MISSES the event.** |
| E80-900M2212S module | EBYTE, China | yes | same |
| Existing E80 boards | **Germany** | **operator must ship them** | transatlantic + customs, ~1–2 weeks, and they are the *bench* unit |
| Latex sphere + HI-FLOAT | US retail | yes | days |
| Helikite | Allsopp, UK | quote-only | 1–3 weeks + customs |
| Mast | US | yes | days |

> 🔴 **Consequence:** ordering from EBYTE does **not** solve the Texas problem on
> this timeline. `reports/ELECTRONICS-SOURCING-US-2026-11.md` §2 records the
> policy verbatim: 7 working days processing + 7–30 working days shipping, US
> routed via Yanwen Express Line.
>
> **The realistic paths are (a) ship the German bench boards to Texas, or (b) find
> a US-warehouse reseller / pay express and accept ~10–14 days.** Both need to
> start now. This supersedes the earlier "order for insurance" framing — the
> order is no longer insurance, it is the *only* source of boards in the US.

---

## 2. The wind problem, stated precisely

`tan θ = drag ÷ free lift`. A tethered lifting body blows downwind until tension
balances drag.

| Asset | 45° blow-over at | Effective height at 8 kn on a 150 ft line |
|---|---|---|
| 36 in foil cluster (4) | 2.3 kn | **~12 ft** |
| 36 in latex sphere | ~5.7 kn | better, but not good |
| 48 in sphere | ~8.9 kn | marginal |
| 60 in sphere | ~10.7 kn | holds |
| **Helikite** | aerofoil — lifts into wind | holds |
| **Mast** | n/a — not a lifting body | **exactly as built** |

Venue wind (KERV ASOS, Nov 2019–2025, 158,912 obs): **mean daylight 7.6 kn, ≥8 kn
in 50% of daylight hours; mean 3.9 kn 05:00–07:00, ≤5 kn in 68% of those hours.**

**So: a wind problem for half of daylight, and a working window for the other
half.** 06:00–09:00 is the reliable slot for any lifting asset.

---

## 3. Option A — Helikite

**For:** the only lifting asset that holds altitude in the venue's real wind.
Best physics for "over the obstruction".

**Against:**
- **UK-only.** No US reseller found (`shopping-list.md` §1, searched and recorded
  as a negative result).
- Lead time 1–3 weeks **plus** customs, against a 5 Nov event.
- Price **UNVERIFIED** — the Allsopp shop is a JS app that cannot be scraped.
- Still needs landowner permission for the tether.

**Verdict: order ONLY IF the quote comes back with a US warehouse or ≤5-day
transit.** Otherwise it cannot make the event.

---

## 4. Option B — latex sphere + HI-FLOAT

**For:** ships in days from US retail, ~$30–60, works today, and a 48–60 in
sphere (33–65 ft³) is **still outside 14 CFR 101 Subpart B** (6 ft / 115 ft³
thresholds).

**Against:** lies down in the wind, so only usable in the morning window.

**Verdict: buy it regardless.** It is the cheapest asset that works, it needs no
long lead time, and it doubles as the 06:00–09:00 asset.

---

## 5. Option C — MAST — **recommended primary**

**This is the operator reframe and it is correct.**

### Permission: none required

| Regime | Balloon | Mast |
|---|---|---|
| 14 CFR 101 Subpart B (moored balloons) | applies if >6 ft / >115 ft³ | **does not apply — not a balloon** |
| 14 CFR 77 (§77.9(a) notice >200 ft AGL) | applies above 200 ft | does not apply if <200 ft |
| Landowner airspace permission | required | **not required (ordinary structure)** |
| §101.15 notice, §101.17 streamers, §101.19 deflation device | apply in scope | **none** |
| Wind go/no-go rule | governs the whole demo | **structural only** |

**The entire regulatory surface disappears.** A mast below 200 ft is a structure,
not an aircraft operation.

### Physics: honest limitations

- **Effective height is exactly what you build.** No blow-over, ever.
- **Wind limit is structural**, far above 9 kn.
- **BUT: 20–40 ft of mast does not clear a 6 m (20 ft) cedar canopy by much.**
  A 40 ft mast over a 20 ft canopy gives ~20 ft of clearance; first-Fresnel
  clearance at 400 m wants meaningfully more. So the mast gets you **relay and
  measurement**, probably not the full "over the trees" link.

### What the mast demo actually proves

Not "balloon over obstruction". It proves **"relay at a known, stated height,
measured"** — which is closer to what a real ground mesh deployment looks like
anyway, and it is unfalsifiable in a way the balloon demo is not (nobody can say
the wind did it).

---

## 6. Decision — D8b

| Priority | Asset | When |
|---|---|---|
| **1** | **Mast (20–40 ft)** | **Build first.** Permission-free, cannot be blocked, is the measurement control |
| 2 | Latex sphere + HI-FLOAT | Buy now. The 06:00–09:00 asset |
| 3 | Helikite | **Only if the quote shows a US warehouse or ≤5-day transit** |
| — | Foil clusters | **REJECTED** — 12 ft effective height at 8 kn |

**If permission is hard to obtain: mast-only is a complete, valid demo.** It is
not a degraded fallback — it removes a whole regulatory class and a whole wind
class from the project. Everything in `RUNBOOK-event-operations.md` works with
the mast substituted for the balloon; the go/no-go wind table becomes advisory
rather than binding.

**Acceptance criterion that changes:** the headline measurement becomes
**height-vs-performance at a known mast height** plus the A/B relay delta, rather
than the balloon-vs-mast delta. Both are defensible; the mast version is simply
harder to argue with.

---

## 7. Actions

- [ ] **A1.** Decide the E80 supply path: ship the German bench boards to Texas, or
      pay express on a fresh EBYTE order (~10–14 days). **Start this today** — it
      is now the longest pole.
- [ ] **A2.** Quote the Helikite today (`info@helikites.com`). Gate: US warehouse
      or ≤5-day transit, else drop it.
- [ ] **A3.** Buy the latex sphere + HI-FLOAT kit.
- [ ] **A4.** Source the mast — spec + verified vendor survey now in
      **`docs/MAST-SPEC.md`**. Best lead: **Jackite Inc (US), fibreglass telescoping
      poles** (https://www.jackite.com/antenna, HTTP 200). Still need model + price.
      Blocks the order, not the plan.
- [ ] **A5.** Get landowner permission **only if** flying the balloon; the mast
      alone needs none.
- [ ] **A6.** Update the runbook's headline measurement to the mast-height
      framing once the mast is sourced.
