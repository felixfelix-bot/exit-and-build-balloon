# Shopping list — Exit & Build 6 tethered relay

**Event:** 5–8 November 2026 · Sovereignty Ranch, 165 Wyatt Ranch Rd E, Bandera, TX
**Buyer:** US. Everything must ship to Texas.
**Decision (operator, 2026-10-22):** **Helikite primary + mast control**, latex sphere as
the cheap fallback.

> **Nothing here has been ordered.** Prices and stock were read on 2026-10-22 and move.
> Items marked **UNVERIFIED** could not be confirmed and must be checked at quote time.

---

## 0. Why a Helikite and not a balloon

A spherical tethered balloon blows downwind until tension balances drag,
`tan θ = drag ÷ free lift`. Measured venue wind (KERV ASOS, Nov 2019–2025, 158,912 obs):
**mean daylight 7.6 kn, ≥8 kn in 50% of daylight hours.**

| Wind | Foil cluster angle | Effective height (150 ft line) |
|---|---|---|
| 2 kn | 37° | 119 ft |
| 3 kn | 60° | 76 ft |
| 5 kn | 78° | **31 ft** |
| 8 kn | 85° | **12 ft** |

Adding balloons does not fix it — drag scales with count exactly as lift does
(4 → 20 × 36 in moves the 45° wind from 2.3 kn to only 3.7 kn). **A foil cluster is
a low-wind-only, wrong-shaped asset.** A Helikite generates lift *into* the wind,
so it holds altitude when a sphere lies down.

**45° blow-over wind by asset:**

| Asset | 45° blow-over at |
|---|---|
| 36 in foil cluster (4 balloons) | 2.3 kn |
| 36 in latex sphere | ~5.7 kn |
| 48 in sphere | ~8.9 kn |
| 60 in sphere | ~10.7 kn |
| **Helikite** | *aerofoil — holds altitude into wind* |

---

## 1. PRIMARY — Helikite

| Item | Vendor | Link | Notes |
|---|---|---|---|
| Helikite, small (sub-200 g payload, 50–150 ft) | **Allsopp Helikites Ltd** (UK) | https://www.helikites.com/shop | **UNVERIFIED pricing** — the shop is a JS app that could not be scraped. Get a quote: `info@helikites.com`, +44 (0)1425 654967. **UK→US: customs + 1–3 week transit — this is a lead-time risk.** |
| US distributor / reseller | **NONE FOUND** | — | **Searched 2026-10-23 and found no US reseller.** Search engines blocked this host (DuckDuckGo returned 202 challenge pages; Marginalia and Mojeek returned no relevant hits). This is a **negative result, not an absence of effort** — treat "no US Helikite source" as the working assumption until a human confirms otherwise. |

> ⚠️ **Consequence of the negative result: the latex sphere is now the DEFAULT, not
> the fallback.** UK lead time (1–3 weeks transit + customs + the same 7-working-day
> processing problem that affects the E80, see `reports/ELECTRONICS-SOURCING-US-2026-11.md` §2)
> against a 5 Nov event means the Helikite is only viable if ordered **immediately**.
> Decide now: order the Helikite today and accept the risk, or go latex-sphere primary.

---

## 2. FALLBACK — latex sphere + HI-FLOAT

**Still legally outside 14 CFR 101 Subpart B** (a 48–60 in sphere is 33–65 ft³, under the
115 ft³ / 6 ft thresholds), so the pennant, notice and rapid-deflation machinery does not
attach.

| Item | Qty | Where | Notes |
|---|---|---|---|
| 36–48 in round **latex** balloon | 4–6 | US party/hobby mail-order | Spheres, not foil — **foil volume scales as D², so up-sizing foil barely helps** |
| **HI-FLOAT** barrier coat | 1 kit | Same supplier | Claimed "up to 25×" float life; latex alone loses a large lift fraction in 12–24 h |
| 18 in foil spares | 4 | Any US party supplier | Cheap spares / markers |

> The barrier coat is what makes latex survive a Texas night. Without it, latex is a
> one-day asset.

---

## 3. CONTROL — mast (fly when wind says no)

**This is not optional.** The report's own point: *"the balloon-vs-mast delta — same link at
20 ft and 120 ft; that difference **is** the value proposition."* A mast is both the
wind-proof fallback and the measurement control that makes the balloon's contribution
provable rather than asserted.

| Item | Spec | Where | Notes |
|---|---|---|---|
| Telescoping fibreglass mast | 30–40 ft, ≥200 g top payload, 3+ guy points | **Jackite Inc (US) — best lead**, product page not yet confirmed | See **`docs/MAST-SPEC.md`** for the verified vendor survey (Jackite HTTP 200; DX Commander/Spiderbeam 403; SOTABEAMS 404; MFJ 429; REI unreachable). **Fibreglass preferred — a metal mast detunes the antenna under test.** No SKU or price confirmed yet; do not quote the third-party "~\$1/ft" review figure as a price. |

---

## 4. Tether and rigging

**Material is where the mass budget dies.** Paracord is **unusable** — 320 g per 150 ft
exceeds the entire ~230 g lift budget.

| Line | Break | Mass / 150 ft | Mass / 300 ft | Verdict |
|---|---|---|---|---|
| **1.0 mm Dyneema** | ~880 N | **46 g** | 91 g | use at 300 ft |
| **1.5 mm Dyneema** | ~1.96 kN | **101 g** | 201 g | use at 150 ft |
| 3 mm nylon braid | ~1.1 kN | 252 g | 503 g | 3–4× heavier, stretches 5–8% |
| 6 mm 550 paracord | ~2.5 kN | **320 g** | 640 g | **unusable** |

> ⚠️ Breaking strengths are **[DERIVED]** from Samson's AmSteel table, area-scaled and ~50%
> derated for small braids — **verify against the datasheet of the line actually bought.**

Worst-case load (4 × 36 in foil, 10/20/30 kn): **19.0 / 75.6 / 170 N**. Design to 200 N with
SF ≥ 5 → **≥1 kN MBL**; 1.5 mm Dyneema gives SF ≈ 10.

| Item | Qty | Where | Notes |
|---|---|---|---|
| Dyneema/Spectra 1.5 mm, 200 ft spool | 1 | arborist / marine / Amazon.com US | 150 ft deployment + tail |
| Dyneema/Spectra 1.0–1.2 mm, 300 ft spool | 1 | same | 300 ft option |
| Swivel (neck) + carabiner | 2 ea | marine supplier | stop the line sawing the balloon |
| Ground anchor: vehicle hitch receiver shackle | 1 | Amazon.com US | park so the line leaves **over the cab, not the glass** |
| Sandbags 20 kg | 3–4 | Amazon.com US | second independent anchor |
| Ground screw 12 in + breaker bar | 2 | Amazon.com US | caliche; second independent anchor |
| **Anemometer** (handheld, kn) | 1 | Amazon.com US | drives the go/no-go rule — **required** |
| Streamers / coloured pennants | — | any | mark the **whole** line; streamer every 50 ft |

**Anchoring rule:** hold **≥500 N at a shallow angle** → **two independent anchors** always.

---

## 5. Helium

| Item | Where | Notes |
|---|---|---|
| **Balloon-grade He, ≥99.99%**, 1 industrial cylinder | **Airgas San Antonio** — 335 N WW White Rd 78219, **(210) 337-7255**; 5929 Distribution Rd 78218, **(210) 661-6000** (~1 h from site) | ask for single-day will-call |
| | **nexAir** — https://www.nexair.com/location-finder/ | |
| | **Linde Welding Gas**, 330 New Laredo Hwy, SA 78211 | |
| | **Matheson–Nippon Sanso** — https://us.nipponsanso.com/contact-us/ | |
| | Kerrville / Bandera welding-gas dealer | ~20 min — usually cheapest; check local listings |
| Party route (one-hour demo only) | Tractor Supply 220 SH-173 S, Bandera; Walmart & 2× H-E-B, Kerrville | Balloon Time 8.9 ft³ **$56.99**, 14.9 ft³ **$75.99** = **$5.10/ft³** |

### Volume math (pure He @ 28 °C = 27.2 g/ft³)

**Hang-time is CONFIRMED at 4 days** (operator, 2026-10-22). The requirement is the
4-day row; the one-hour row is kept only as a comparison, not as a planning basis.

| Scenario | Net lift needed | Pure He | 80/20 party mix |
|---|---|---|---|
| *comparison only:* 4 × 36 in, one demo hour | 330 g | 12.1 ft³ | 15.1 ft³ |
| *comparison only:* 6 × 36 in, one demo hour | 470 g | 17.3 ft³ | 21.6 ft³ |
| **REQUIREMENT — 4-day tether, 20%/day top-up** | — | **~30 ft³** | **~37 ft³** |

> **Buy ~30 ft³ of balloon-grade ≥99.99% helium.** That is the number the 4-day
> hang-time costs. If forced onto an 80/20 party mix the same duty cycle needs
> **~37 ft³**, and you also pay the 20% lift penalty twice (volume *and* top-up).

### 4-day top-up ritual (this is an operating procedure, not a footnote)

Helium leaks out of every soft envelope; over 96 h the loss is what sets the
volume, not the initial fill. Plan for a **20 %/day top-up**:

1. **Morning lift-weigh, every morning.** Calibrated 0–500 g scale, same time of
   day (temperature swings site lift by ~4 % between a 10 °C dawn and a 28 °C
   afternoon). Record grams. This is *your* leak number, not the vendor's.
2. **Top up to the recorded morning lift target** before the first demo slot.
3. **Log the top-up volume.** The 4-day total is what the cylinder must hold;
   if consumption drifts above ~7.5 ft³/day something is wrong (seam leak, or a
   valve not fully closed).
4. **Weigh again in the early afternoon** (13:00 check, `docs/RUNBOOK-event-operations.md`).
   A second daily weigh is what converts "roughly 30 ft³" into a measured number.

> **Consumer party tanks cannot supply this economically.** Balloon Time at
> **$5.10/ft³** (8.9 ft³ = $56.99) versus a USGS Grade-A base of **~$0.33/ft³**
> (~$330/Mcf) — a **~15× retail premium**. Thirty-plus ft³ over four days plus a
> reserve is an industrial-cylinder purchase, not a stack of party tanks. Buy
> balloon-grade from an industrial distributor (§5 supply table above).

> ⚠️ **Site lift is 28 g/ft³, not the sea-level 1.02 kg/m³.** 471.6 m elevation costs ~2%; a
> 28 °C afternoon another 4%.
>
> ⚠️ **Consumer tanks are ≥80% helium, not pure** (Balloon Time's own sell sheet) — that is a
> **20% lift penalty**. Buy industrial **balloon-grade ≥99.99%**, not welding grade, not a
> party mix.
>
> ⚠️ **Cylinder size, valve outlet and regulator requirement are UNVERIFIED.** Common
> industrial He is 20/40/80/125/300 ft³ at ~2,000–2,400 psig on a **CGA 580** outlet
> (0.965″-14 NGO RH). Party tanks need no regulator. Confirm at quote time; budget a
> **cylinder deposit/demurrage** plus **hazmat handling**.

### Supply context — this is a non-event

USGS MCS 2026: 2025 US helium sales **81 million m³ (2.9 B ft³), ~$970 M**; Grade-A base
**~$330/Mcf, DOWN from $390/Mcf in 2024**. The Federal Helium System was privatised — closed
to **Messer 27 Jun 2024** with ~800 M ft³ of crude helium. Six new US plants came online in
2025 and a **helium storage cavern at Beaumont, TX** entered service. **The retail premium is
the whole story** — Balloon Time at $5.10/ft³ is ~15× the base price, which is exactly the gap
an industrial distributor closes at this volume.

---

## 6. Radio hardware

**Source: `reports/ELECTRONICS-SOURCING-US-2026-11.md`** (curl-verified, prices read
from the store's own Shopify `products.json` on 2026-10-23; its integer fields are
**cents**, and that was independently re-verified).

> 🔴 **LEAD TIME IS THE FINDING THAT CHANGES THE PLAN.** EBYTE's own shipping
> policy: **7 working days processing** + **7–30 working days** surface shipping
> (US routed via Yanwen Express Line). **Total 14–37 working days → lands
> ≈ 12 Nov – 17 Dec 2026. It MISSES the 5 Nov event.**
>
> **Therefore the event build must use existing inventory** (D10: 20× ESP32-C3
> Mini V1, 4× NiceRF LR2021, 3× E28-2G4M27S). Order anyway for spares — just do
> not plan the demo around arrival.

### The critical item — verified prices, in stock

Product page (carries the whole E80 variant matrix):
`https://ebyteiot.com/products/ebyte-e80-400m2213s-semtech-multi-band-lora-lr1121-chip-21-5-13dbm-433m-2-4ghz-lora-dual-band-wireless-rf-transceiver-module-副本`
(HTTP 200; the CJK `副本` must be URL-encoded as `%E5%89%AF%E6%9C%AC`.)

| Variant | USD | In stock | Notes |
|---|---|---|---|
| **`E80-900MBL-02`** — the EVAL BOARD (STM32F103 + LR2021) | **$18.56** | yes | **The bench item.** This is what `E80-VERIFICATION-CHECKLIST.md` V1 operates on |
| `E80-900M2212S(LR2021)` — bare module | **$9.48** | yes | Spare |
| `E80-900M2213S` (LR1121) + 915 FPC + 2.4 G FPC antennas | **$8.25** | yes | Bundle — both antennas included |
| `E80-400MBL-02` / `-01` | $18.56 / $17.02 | yes | **400 MHz — wrong band for D2** |

> ⚠️ **`…M2212S` = LR2021; `…M2213S` = LR1121. Different chips, different
> datasheets.** The repo's bench inventory is LR2021 → order `2212S` if matching
> inventory matters.
>
> ⚠️ **The product page describes dual-band but shows NO connector map.** Do not
> infer the 2.4 GHz antenna jack from the listing — that is V0.1 in the checklist
> and it must be confirmed on the physical board.

### Other radio items

| Item | Vendor / status |
|---|---|
| LR2021 bare chip / dev kit | Semtech page HTTP 200, **no published price**. DigiKey = **403 blocked**, Mouser = **no connection** from this host → **UNVERIFIED** |
| NiceRF LoRa2021 module | `nicerf.com` HTTP 200; the specific module path returned **404** → **UNVERIFIED**, need the right URL |
| E28-2G4M27S (SX1281, +27 dBm) | EBYTE store, listing verified |
| ESP32-C3 boards, LiPo, JST-PH, anemometer | Adafruit + PiShop reachable (HTTP 200 on search paths) — specific SKUs not pinned |

**Every unverified row above carries a real reason and a route to settle it.** None
of them were invented. See the sourcing report's §10 for the full HTTP status log.

---

## 6.1 Power — conductive tether vs solar

**Decision: power the payload from the ground, up the tether.** The 4-day
hang-time settles this; solar stops being attractive the moment the rig has to
run 96 h with an overnight.

### Why not solar

| | Value |
|---|---|
| Total energy needed over 96 h | **~14.4 Wh** at **~0.15 W** average |
| Load | ESP32-C3 + LR2021, mostly-RX, **30–60 mA at 3.3 V** |
| Storage sizing | 14.4 Wh ÷ 3.3 V ≈ **4.4 Ah** of usable energy, plus overnight margin and conversion losses — this is not a supercap |
| Existing repo design mass | 12× 52×19 mm cells + BAT54 + 1.0 F 5.5 V supercap + TPS7A02 ≈ **25–35 g** |

The 25–35 g solar design is **intermittent** and introduces a **new failure mode
overnight**, precisely when nobody is watching and when a 4-day run cannot
tolerate a dead payload. A 1.0 F supercap holds ~4 J at 5 V — orders of
magnitude short of 14.4 Wh. Solar is the wrong architecture for this duty cycle,
and the mass it saves is smaller than the tether option's worst case (§ below).

### Why the conductive tether works

**2-conductor run at 150 ft = 45.7 m.**

| Cable | Mass (pair, 45.7 m) | Resistance per leg | Drop @ 50 mA (loop) | Drop @ 20 mA (loop) |
|---|---|---|---|---|
| **AWG28** | **66 g** | **9.7 Ω** | **0.97 V** | **0.39 V** |
| **AWG30** | **42 g** | **15.5 Ω** | **1.55 V** | **0.62 V** |

**DC drop is manageable at the real duty cycle — but only if you do not try to
pass 3.3 V over 45 m.** At 20 mA an AWG28 pair loses 0.39 V; at 50 mA it loses
0.97 V, which is 29 % of a 3.3 V rail. Regulating at the payload instead of at
the ground removes that as a design constraint.

**RECOMMENDED — feed a higher voltage up, regulate at the payload:** raise the
feed to e.g. **12 V** and step down at the top with a small buck/linear. At 12 V
the same 66 g AWG28 pair carries 0.15 W at ~12.5 mA for a loop drop of ~0.24 V
(2 %) — the drop becomes irrelevant rather than merely tolerable.

**⚠️ Confirm the payload regulator's input range before ordering.** This is the
one number that decides whether the 12 V feed is safe: the on-payload regulator
must accept the *no-load* feed voltage (a 12 V supply feeding a 12 mA load sits
near its open-circuit value) and its dropout must be small at 12 mA. Marked
**UNVERIFIED** until the chosen part's datasheet is read.

**Mass check:** 66 g (AWG28, 150 ft pair) + a small on-payload regulator (~2–5 g)
against a **~230 g lift budget** (`§4`) — but note that a 2-conductor copper pair
is **additional** to a Dyneema load line, not a replacement: Dyneema carries the
load, copper carries the power. Budget both.

### OPEN ITEM — copper pair alongside the Dyneema line

**Nobody has checked this, and it should be checked before it is flown.**

A copper pair running alongside a Dyneema load line adds:

- **mass** (above) and **wind area** (a second line, however thin, is drag);
- **a conductor near the antenna** — and the whole point of the relay is the
  antenna's view of the ground node.

**Proposed check:** keep the pair **away from the antenna feed** (run it down
the opposite side of the tether bundle, and do not dress it against the antenna
mast); then **measure desensitisation** — compare PER/RSSI/SNR with and without
the power pair energised, at the same positions, using the A/B procedure in
`docs/RUNBOOK-event-operations.md`. If the delta is not measurable, close the
item. Do not design around an unmeasured effect silently.

### Parts to add

| Item | Spec | Where |
|---|---|---|
| 2-conductor lightweight cable, 150 ft | AWG28 (66 g/pair) preferred; AWG30 (42 g/pair) if mass-critical | US wire supplier — **link UNVERIFIED, see `reports/ELECTRONICS-SOURCING-US-2026-11.md`** |
| Connectors | 2-pin locking, keyed (payload side must not unplug in wind) | US distributor — **UNVERIFIED** |
| On-payload regulator | buck or linear, input must accept the 12 V feed, output 3.3 V @ ≥60 mA | US distributor — **UNVERIFIED** |
| Ground-side supply | 12 V bench/battery supply at the anchor, with current logging | already on site |

> **Interaction with the lighting question:** if the organiser ever wants a
> night-lit rig, the lighting load lands on this same power budget
> (`docs/SITE-RULES-AND-FAA.md` §8). The recorded position is to stay outside
> Subpart B and strike at dusk rather than light the rig — which keeps the power
> budget where it is. Re-decide here if that changes.

---

## 7. Site and safety

| Item | Why |
|---|---|
| **Printed copy of 14 CFR Part 101 and Part 77** + any FAA correspondence | carry on site |
| High-visibility line marking | a **Dyneema line is nearly invisible to a drone camera** |
| Drone pilot brief | hard altitude ceiling + 100 ft no-fly cylinder around the anchor. **Largest on-site safety exposure and no regulation covers it.** |
| Calibrated 0–500 g scale | weigh lift every morning; get *your* leak numbers, not the vendor's |
| TFR/NOTAM check each flight day | https://tfr.faa.gov/tfr2/list.html |

---

## 8. Go/no-go wind rule (anemometer at 2 m, on site)

| Sustained | Gust | Action |
|---|---|---|
| ≤3 kn | ≤6 kn | **GO** — full 150 ft, near-vertical |
| 3–6 kn | ≤10 kn | **GO** — 60–80° blow-over; report *effective* height, not 150 ft |
| 6–9 kn | ≤14 kn | GO only with Helikite; a foil cluster is a ground-level demo |
| **>9 kn** | **>14 kn** | **NO-GO — walk it down hand-over-hand** |
| Thunderstorm / virga / lightning <10 mi | — | **NO-GO — a wet line is a conductor** |

**Expect this to cost roughly half the daylight hours.** On 5–8 Nov 2019–2025 the daily max
sustained wind at KERV never reached 20 kn (max 18 kn); 14% of days had a daily max ≥15 kn.
**06:00–09:00 is the reliable demo slot** (mean 3.9 kn, ≤5 kn in 68% of hours).

---

## 9. Open items before ordering

| # | Item | Owner |
|---|---|---|
| 1 | ~~**Hang-time decision**~~ **CLOSED 2026-10-22 — 4 days.** Helium volume is now **~30 ft³ balloon-grade** (§5); tether spec and the 4-day timeline follow from it. | — closed |
| 2 | **Helikite US availability** — sourcing pass running; if none, latex sphere becomes primary | engineering |
| 3 | **Form 7460-1** — the FAA OE/AAA portal was **closed by the government shutdown** as of 2026-10-22 and is refusing new Part 77 notices. **Cap at 150–200 ft AGL and do not depend on a determination arriving.** | organiser |
| 4 | **§ 101.13(a)(4) five-mile airport question** — 20TS Bains Private is 3.4 mi away. Only binds if the balloon exceeds 6 ft / 115 ft³. | organiser / FAA |
| 5 | Cylinder size / outlet / regulator / deposit | at quote |
| 6 | Dyneema breaking strengths — verify against the datasheet bought | at purchase |
