# Balloon tradeoffs — size, tether, payload, helium cost

**Question:** the organisers want to fly a balloon after all, and want it to carry
**significant weight** (Power-over-Ethernet, cameras, radios). What diameter,
tether and helium spend does that actually require, and where are the cliffs?

**Figure:** `analysis/balloon-tradeoffs.png`
**Reproduce:** `python3 analysis/balloon_model.py` (tables) · `python3 analysis/plot_tradeoffs.py` (figure)
**Status:** model + figure, **not** a flight clearance. No balloon has been sized for
a real payload yet because **no payload mass has been measured**.

---

## 1. The one relationship that decides everything

A sphere's volume — and therefore its lift, and therefore its helium cost — scales
as **D³**. Its drag, and therefore its blow-over, scales as **D²**.

```
V     = π/6 · D³            lift  = V × 28 g/ft³
A     = π · D² / 4          drag  = ½ · ρ · Cd · A · v²   (Cd = 0.47)
      ↑ FRONTAL (projected) area, NOT the π·D² surface area.
        This distinction was a real bug in v1 and is called out in §3.
tan θ = drag ÷ (lift − payload − tether)      effective height = L · cos θ
```

**Two consequences, and they pull opposite ways:**

- **Bigger is super-linearly expensive.** Doubling the diameter is **8×** the
  helium and **8×** the lift — but only **4×** the drag. So a big balloon lifts
  more per unit of drag, which is why big balloons blow over *less*.
- **Bigger is not "safer" in absolute terms.** It still blows over (see §3), and
  it costs real money in a commodity that is priced per ft³ and topped up daily.

**Anchor check:** the 28 g/ft³ figure is derived, not asserted — sea-level
lift of ~1.0562 kg/m³, × 0.9463 for 471.6 m elevation, × 0.9505 for a 28 °C
afternoon = 0.9499 kg/m³ = **28.0 g/ft³**. It matches the repo's existing figure,
so the model and the shopping list agree.

---

## 2. The size table — lift, helium, and what is left for payload

Four-day duty with a **20 %/day top-up** (the repo's confirmed hang-time), helium at
$1.20/ft³.

| Diameter | Volume | **Gross lift** | **Useful payload** (80 % of lift, less 150 ft tether) | **Helium, 4 days** |
|---:|---:|---:|---:|---:|
| 36 in | 14.1 ft³ | 396 g | ~271 g | $30 |
| 48 in | 33.5 ft³ | 938 g | ~704 g | $72 |
| 60 in | 65.4 ft³ | **1,833 g** | ~1,420 g | $141 |
| 72 in | 113.1 ft³ | 3,167 g | ~2,487 g | $244 |
| 84 in | 179.6 ft³ | 5,029 g | ~3,977 g | $388 |
| 96 in | 268.1 ft³ | **7,506 g** | ~5,959 g | **$579** |
| 120 in | 523.6 ft³ | 14,661 g | ~11,683 g | $1,131 |
| 144 in | 904.8 ft³ | 25,334 g | ~20,221 g | $1,954 |

**Read the payload column, not the lift column.** The 80 % factor is the reserve
that keeps the line taut; the tether deduction is the mass that has to be lifted
before any payload.

### Sensitivity — helium price is the wild card

At **96 in** (483 ft³ over four days):

| Helium $/ft³ | 4-day cost |
|---|---|
| $0.33 — USGS Grade-A base | **$159** |
| $0.75 — favourable industrial | $362 |
| **$1.20 — planning figure** | **$579** |
| $2.00 — tight market | $965 |
| **$5.10 — retail party tanks** | **$2,461** |

**The 15× spread between base and party-tank pricing is the entire cost story.**
Buying party tanks for a large sphere is a **$2,461** mistake instead of a **$579**
purchase. The repo already says this; the model prices it.

---

## 3. The wind cliff — where the balloon stops earning its place

Blow-over angle at a **150 ft line**, payload set to 50 % of net lift:

| Diameter | 3 kn | 5 kn | 6 kn | **8 kn** | 10 kn | 12 kn | 15 kn |
|---|---:|---:|---:|---:|---:|---:|---:|
| 60 in | 7° | 18° | 25° | **40°** | 52° | 62° | 71° |
| 72 in | 5° | 15° | 21° | **34°** | 47° | 57° | 67° |
| 84 in | 5° | 13° | 18° | **30°** | 42° | 53° | 64° |
| 96 in | 4° | 11° | 16° | **27°** | 38° | 49° | 61° |
| 120 in | 3° | 9° | 13° | **22°** | 32° | 42° | 55° |
| 144 in | 3° | 8° | 11° | **19°** | 28° | 37° | 50° |

**Effective height on the same 150 ft line at 8 kn:**

| 60 in | 72 in | 84 in | 96 in | 120 in | 144 in |
|---:|---:|---:|---:|---:|---:|
| **115 ft** | 124 ft | 130 ft | 134 ft | 139 ft | 142 ft |

**The venue's November reality:** mean daylight wind **7.6 kn**, and **≥8 kn in
50 % of daylight hours**. So on half the days you get the right-hand column —
**43 to 89 ft**, not 150 ft.

> ### ⚠️ This section was WRONG in v1, and the error was 4×

> v1 reported a 60 in sphere at **73° blow-over / 43 ft** at 8 kn. The real number
> is **40° / 115 ft**. The cause was a genuine bug: drag was computed from
> **π·D²** (a sphere's *surface* area) instead of **π·D²/4** (its *frontal*
> projected area) — **4× too much drag**, which turned a 40° lean into a 73° one.
>
> Found by the visual consultant checking the arithmetic, then verified by hand
> against the closed form. **The corrected result changes the conclusion of this
> document**, so the old recommendation is retracted below.

**The corrected picture: a sphere holds altitude much better than the plan assumed.**

At the venue's median 8 kn, even a **60 in** balloon keeps **115 ft** of its 150 ft
line — 77 % of nominal height. A **144 in** keeps **142 ft** (95 %). That is not
"12 ft at 8 kn"; that was the foil-cluster figure the original D8 analysis
rejected, and it does not transfer to a sphere.

**But the cost and regulatory cliffs did not move at all** — they are set by
volume and diameter, not by wind. See §4: a sphere big enough to carry a PoE load
crosses Part 101 and costs $82–579 in helium, whatever the wind does.

---

## 4. Tether and PoE — the payload the organisers described

**Tether mass**, from the repo's measured figures (1.0 mm Dyneema 46 g/150 ft,
1.5 mm 101 g/150 ft), with the conductor pair **additive** (copper carries power,
Dyneema carries load):

| Length | 1.0 mm | 1.5 mm | + AWG28 pair | + AWG26 pair |
|---:|---:|---:|---:|---:|
| 50 ft | 15 g | 34 g | 37 g | 50 g |
| 100 ft | 31 g | 67 g | 75 g | 101 g |
| **150 ft** | **46 g** | 101 g | **112 g** | 151 g |
| 200 ft | 61 g | 135 g | 149 g | 202 g |
| 300 ft | 92 g | 202 g | 224 g | 302 g |

**PoE payload → required diameter** (150 ft, 1.0 mm, 20 % reserve):

| Payload to lift | Gross needed | Volume | **Diameter** | Helium, 4 days |
|---:|---:|---:|---:|---:|
| 300 g | 432 g | 15.4 ft³ | **37 in** | $33 |
| 500 g | 682 g | 24.4 ft³ | **43 in** | $53 |
| 800 g | 1,058 g | 37.8 ft³ | **50 in** | $82 |
| 1,200 g | 1,558 g | 55.6 ft³ | **57 in** | $120 |
| 2,000 g | 2,558 g | 91.3 ft³ | **67 in** | $197 |
| 4,000 g | 5,058 g | 180.6 ft³ | **84 in** | $388 |

> ⚠️ **A real PoE load is heavier than people expect.** A PoE injector, two radios,
> a camera, a mount and the cable itself is **400–800 g** before you add structural
> margin. That lands you at **50–60 in**.
>
> ### The regulatory line is 72 in, not 115 ft³
>
> **Corrected.** 14 CFR 101 Subpart B applies when a moored balloon has
> **diameter greater than 6 ft (72 in) OR gas capacity greater than 115 ft³** —
> **either** test. For an ideal sphere the **diameter test binds first**: 72 in
> holds only **113.1 ft³**, so you would never reach 115 ft³ without already being
> past 72 in. (115 ft³ would need **72.4 in**.)
>
> So **under 72 in you stay outside Subpart B; at or above it you do not** — and a
> 50–60 in sphere for a PoE load is **still inside the exemption**. v1 wrongly
> shaded this at 60 in and implied volume alone decided it. It does not.
>
> **What this means for the organisers' plan:** a PoE-capable balloon at **50–60 in**
> avoids the Part 101 machinery entirely. Going past **72 in** — which is what you
> need for ~2.5 kg of payload — brings landowner permission, notice and
> rapid-deflation requirements with it.

---

## 5. What to actually choose

| If the goal is… | Choose | Cost (4-day He) | Honest caveat |
|---|---|---|---|
| **Just fly something** | **48 in sphere** | ~$72 | 704 g payload, 115 ft³ — still under Part 101 |
| **Carry PoE + radios (800 g)** | **50–60 in** | $82–141 | **still under 72 in → Part 101 does NOT apply** |
| **Survive 8 kn** | **120 in or bigger** | $1,131 | 79 ft at 8 kn, but 524 ft³ and a serious rig |
| **Best height per dollar on a windy site** | **the mast** | $0 helium | 28 ft guaranteed, no wind rule, no permission |
| **Best if the organisers insist and budget allows** | **96 in** | $579 | 66 ft at 8 kn, 268 ft³, manageable with 4–6 people |

### The recommendation I would defend

**Fly the mast for the relay test. If the organisers want a balloon as a
demonstration, fly a 96 in sphere** — it is the smallest size that still holds a
usable height at the venue's median wind, it carries ~6 kg of payload, and its
helium bill ($579) is a real number rather than a surprise. **Do not size below
60 in and expect it to stay up** at this site.

**And do not order helium until the diameter is fixed** — the cost is D³, and the
spread between a 60 in and a 96 in is **4×** the helium bill.

---

## 6. What this model does NOT know

Stated plainly, because these are the ways it could be wrong:

- **Payload mass is unmeasured.** Every diameter recommendation above rests on a
  *declared* payload, not a weighed one. **Weigh the payload before sizing.**
- **Cd = 0.47** is a smooth-sphere textbook value. A balloon with a tether, a
  payload harness and streamers has more drag — treat blow-over angles as
  **optimistic**.
- **Wind is a mean, not a gust.** The venue data is hourly sustained wind; a 14 kn
  gust on an 8 kn day pushes the angle much further. The go/no-go table in
  `../shopping-list.md` §8 uses gust limits for this reason.
- **Helium price is a planning figure**, not a quote. $1.20/ft³ is chosen between
  the USGS base and retail party pricing; **get an actual cylinder quote.**
- **No thermal cycling** is modelled. A sphere loses lift on a cold night and gains
  it at noon; the 20 %/day top-up is the repo's operating answer, not a derivation.
- **Envelope mass is ignored.** Real latex has mass; at large diameters this starts
  to matter and would reduce usable payload.

---

## 7. Verdict from the visual consultant

See §7 of the commit for the round-by-round record. The consultant was asked to
check **both layout and arithmetic** — per the `visual-consultant` skill, a consult
verdict grades the picture but does not measure it, so its geometric claims are
treated as hypotheses to check against the model output above.
