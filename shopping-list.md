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
| US distributor / reseller | *being sourced* | — | A dedicated sourcing pass is running (see `HELIKITE-AND-TETHER-SOURCING-US-2026-11.md` when it lands) |

> ⚠️ **Order this FIRST if the Helikite is the primary.** UK transit plus customs against a
> 5 Nov event means it is the longest-lead item in the whole list. If a US source cannot be
> found, the latex sphere (below) becomes the primary, not the fallback.

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
| Telescoping / tilt-over mast | 20–40 ft, holds ~150 g payload | *being sourced* | Must survive the same 9 kn go/no-go rule as the tether |

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

| Scenario | Net lift needed | Pure He | 80/20 party mix |
|---|---|---|---|
| 4 × 36 in, one demo hour | 330 g | **12.1 ft³** | 15.1 ft³ |
| 6 × 36 in | 470 g | **17.3 ft³** | 21.6 ft³ |
| **4-day, 6 × 36 in, 20%/day top-up** | — | **~30 ft³** | ~37 ft³ |

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

**Two sourcing passes are running.** This section will be completed with verified US links
when they land; see:

- `reports/ELECTRONICS-SOURCING-US-2026-11.md` — radio modules, antennas, dev boards
- `reports/HELIKITE-AND-TETHER-SOURCING-US-2026-11.md` — Helikite, tether, mast

**What is needed (spec, not yet linked):**

| Item | Spec | Note |
|---|---|---|
| E80 eval board | **`E80-900MBL-02`** preferred (915 option); `-400` variant is 400 MHz | Realistically AliExpress / CDEBYTE direct — **2–3 week lead time risk** |
| LR2021 module | NiceRF LoRa2021 (~1.8 g) | payload radio |
| ESP32-C3 board | SuperMini / XIAO ESP32C3 / Mini V1 | serial↔radio bridge |
| Antennas | 2.4 GHz and 915 MHz SMA, lightweight | 2.4 GHz λ/2 = 3.1 cm; 915 λ/2 = 16.4 cm |
| 1S LiPo + protection, regulator | small, lightweight | ~150 g payload budget |

> **Existing inventory covers the build without new fabrication:** 20× ESP32-C3 Mini V1,
> 4× NiceRF LR2021, 3× E28-2G4M27S, plus wire-dipole antennas. **No PCB order** (D10).

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
| 1 | **Hang-time decision** — 4-day tether vs one scheduled hour. Drives helium volume (12 vs 30 ft³) and tether spec. | organiser |
| 2 | **Helikite US availability** — sourcing pass running; if none, latex sphere becomes primary | engineering |
| 3 | **Form 7460-1** — the FAA OE/AAA portal was **closed by the government shutdown** as of 2026-10-22 and is refusing new Part 77 notices. **Cap at 150–200 ft AGL and do not depend on a determination arriving.** | organiser |
| 4 | **§ 101.13(a)(4) five-mile airport question** — 20TS Bains Private is 3.4 mi away. Only binds if the balloon exceeds 6 ft / 115 ft³. | organiser / FAA |
| 5 | Cylinder size / outlet / regulator / deposit | at quote |
| 6 | Dyneema breaking strengths — verify against the datasheet bought | at purchase |
