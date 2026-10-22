# Tethered helium balloon: logistics + legality plan — Exit & Build 6, Bandera TX, Nov 2026

**Purpose.** Buy, fly and legally cover a cheap tethered helium balloon lofting a ~100–150 g radio
payload (ESP32-C3 + LR2021 + battery) for a ground-to-ground FIPS relay demo, Exit & Build 6,
**Nov 5–8 2026**, Sovereignty Ranch, 165 Wyatt Ranch Rd E, Bandera, TX.

**Method.** Every external claim was fetched live on **2026-10-22** and carries its URL. Arithmetic I
performed is marked **[DERIVED]**; unreachable primary sources are **UNVERIFIED** and routed to a
supplier or professional. Physics is computed for this site, not copied from a sea-level chart.

> **Not legal advice.** §4 states the regulation text; whether it governs your operation is a call
> for the San Antonio FSDO (and, for anything contractual, a Texas attorney).

## 0. Site facts

| Item | Value | Basis |
|---|---|---|
| Coordinates / ground elevation | 29.8292 N, −99.0153 W / **471.6 m (1,547 ft)** | Nominatim; OpenTopoData NED10m |
| Nearest airport | **Kerrville Muni (KERV)**, 6,004 ft runway, **11.0 mi** | OurAirports CSVs; Wikipedia |
| Other strips | **20TS Bains Private 3.4 mi**; TE90 Flying L (3,600 ft) 9.6 mi; 17TE Comfort 8.2 mi; several private/closed <8 mi | same **[DERIVED]** |
| Nov wind, 09–18 local | mean **7.6 kn**, p90 13 kn, **≥8 kn in 50% of hours** | KERV ASOS 5-min archive, Nov 2019–2025 (158,912 obs) via Iowa Mesonet **[DERIVED]** |
| Nov wind, 05–07 local | mean **3.9 kn**, ≤5 kn in **68%** of hours | same |

**The decisive fact:** Hill Country November is not a low-wind month. Half of daylight is ≥8 kn.
Everything below follows from that.

---

## 1. Balloon type and size

**Foil, not latex, for a 4-day tether.** Latex is a porous elastic membrane and helium diffuses
through the polymer itself. The same manufacturer quotes **5–7 hours** float for its latex balloons
and **1–2 days** for foil *from the same tank* ([Balloon Time](https://www.balloontime.com/pages/how-to-use)).
The vendor figure is the conservative indoor-party case; outdoor foil runs **1–3 weeks** before a
top-up. Latex loses a large fraction of lift **within 12–24 h** and will not survive one Texas
night. The only way to make latex survive is an internal barrier coat — HI-FLOAT, claimed to make
latex float "up to 25 times longer" ([Betallic](https://www.betallic.com/pages/hi-float-chart)),
i.e. 5–7 h → days, at the cost of a coat-and-dry prep ritual.

**Lift arithmetic at 471 m** (ISA shifted to site altitude, p/p₀ = 0.9478):

| Condition | Net lift per m³ | per ft³ |
|---|---|---|
| 15 °C (Nov morning) | 1,003 g | **28.4 g** |
| 28 °C (afternoon) | 960 g | **27.2 g** |

**[DERIVED]** The usual "1.02 kg/m³" is a sea-level figure; here you have ~2% less, and a warm
afternoon costs 4% more. Budget **1.00 kg/m³ / 28 g per ft³**. Bigger correction: consumer tanks
are **not pure helium** — Balloon Time states "a mixture of Helium and Air with **not less than 80%
Helium**" ([sell sheet](https://www.balloontime.com/cdn/shop/files/BT-Sell-Sheet_Medium-Jumbo_2026.pdf)),
which costs **20% of your lift**. Buy industrial **balloon-grade ≥99.99%** instead.

Foil balloons are flat pillows, so capacity is far below the sphere of the same diameter. Anchoring
on the manufacturer's own fill counts (14.9 ft³ fills **27 × 18 in** or **4 × 36 in** foil,
[Jumbo tank](https://www.balloontime.com/products/jumbo-helium-tank)):

| Balloon | Capacity | Gross @28 g/ft³ | Net lift |
|---|---|---|---|
| 18 in foil | 0.55 ft³ **[DERIVED]** | 16 g | **11 g** |
| 24 in foil | ~1.05 ft³ **UNVERIFIED** | 29 g | **20 g** |
| 36 in foil | 3.73 ft³ **[DERIVED]** | 106 g | **78 g** |

**Budget:** 150 g payload + 60 g tether + margin = **~230 g net lift needed**. That is **21 × 18 in**,
**12 × 24 in**, or **4 × 36 in** (312 g net, 82 g surplus). **Buy 6 × 36 in round foil** — 4 flying,
2 spares, ~15 ft³ of helium. Note foil volume scales with D², so up-sizing foil barely helps; a
36 in *latex sphere* holds ~14 ft³ (~370 g net) and replaces four foil numbers **[DERIVED]**.

---

## 2. Helium supply in Texas

**Supply picture (verified, USGS/BLM).** 2025 US sales were **81 million m³ (2.9 B ft³), ~$970 M**;
base Grade-A price **~$12/m³ = $330/Mcf, down from $390/Mcf in 2024**, plus producer surcharges
([USGS MCS 2026](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-helium.pdf);
[2024 figure](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-helium.pdf)). The Federal Helium
System was privatised — bid Jan 2024, closed to **Messer 27 Jun 2024** with ~800 M ft³ of crude
helium ([BLM](https://www.blm.gov/press-release/blm-completes-sale-federal-helium-system)); six new
US plants came online in 2025 and a **helium storage cavern at Beaumont, TX** entered service.
**For a small buyer this is a non-event:** the price is falling. What you feel is the retail premium
— Balloon Time Jumbo is **$75.99 / 14.9 ft³ = $5.10/ft³**, ~**15× the USGS base price [DERIVED]** —
which is exactly the gap an industrial distributor closes at your volume.

**Vendors (verified reachable from the site):**

| Vendor | Nearest branch | Note |
|---|---|---|
| **Airgas** (Air Liquide) | San Antonio — 335 N WW White Rd 78219, **(210) 337-7255**; 5929 Distribution Rd 78218, **(210) 661-6000** (~1 h) | markets "Balloon helium"; [branch list](https://locations.airgas.com/tx/sanantonio) |
| **nexAir** / **Linde Welding Gas** (330 New Laredo Hwy, SA 78211) / **Matheson–Nippon Sanso** | San Antonio region | [nexAir](https://www.nexair.com/location-finder/) · [Matheson](https://us.nipponsanso.com/contact-us/) |
| **Kerrville/Bandera welding-gas dealer** | ~20 min | usually cheapest; check local listings |
| **Party route** | Tractor Supply, 220 SH-173 S, Bandera; Walmart & 2× H-E-B, Kerrville | Balloon Time 8.9 ft³ **$56.99**, 14.9 ft³ **$75.99** |

Ask for **balloon-grade (Grade A, ≥99.99%)**, not welding grade and not a He/air party mix.

**Volume math** (pure He @28 °C = 27.2 g/ft³):

| Scenario | Net lift needed | Pure He | 80/20 party mix |
|---|---|---|---|
| 4 × 36 in, one demo hour | 330 g | **12.1 ft³** | 15.1 ft³ |
| 6 × 36 in | 470 g | **17.3 ft³** | 21.6 ft³ |
| **4-day, 6 × 36 in, 20%/day top-up** | — | **~30 ft³** | ~37 ft³ |

**[DERIVED]** The 20%/day allowance covers handling, re-tying and neck-seal loss, not permeation.
Verify by weighing lift each morning on a calibrated 0–500 g scale.

**Cylinder/regulator.** One 14.9 ft³ party tank covers the one-hour demo only; the 4-day tether
needs **one industrial cylinder**, far cheaper than 2–3 party tanks. Industrial helium ships in
high-pressure steel cylinders (common 20/40/80/125/300 ft³, ~2,000–2,400 psig) on a **CGA 580**
outlet (0.965″-14 NGO RH external, standard inert fitting). **UNVERIFIED — confirm size, pressure,
outlet and whether a regulator is required at quote time.** Party tanks need none (built-in nozzle).
Budget a **cylinder deposit/demurrage** plus **hazmat handling**; ask for single-day will-call, and
transport upright and strapped — a closed vehicle on a 28 °C afternoon is a pressure vessel.

---

## 3. Tether system

**Material is where the mass budget dies.** **[DERIVED]** from Samson's AmSteel strength/weight
table ([samsonrope.com](https://www.samsonrope.com/product/amsteel)), area-scaled and ~50% derated
for small braids — verify against the product datasheet:

| Line | Break | Mass / 150 ft | Mass / 300 ft |
|---|---|---|---|
| 1.0 mm Dyneema | ~880 N | **46 g** | 91 g |
| **1.5 mm Dyneema** | ~1.96 kN | **101 g** | 201 g |
| 3 mm nylon braid | ~1.1 kN | 252 g | 503 g |
| 6 mm 550 paracord | ~2.5 kN | **320 g** | 640 g |

**Paracord is unusable** — 320 g per 150 ft exceeds the entire 230 g lift budget. Nylon/Dacron are
3–4× heavier and stretch 5–8%, making the tether a spring in gusts. **Use 1.0–1.2 mm Dyneema at
300 ft, 1.5 mm at 150 ft.**

**Worst-case load.** F = ½ρv²C_dA; 36 in balloon A = 0.657 m² (C_d 0.47 sphere / ~0.9 flat foil)
**[DERIVED]**: 4 × 36 in foil cluster = **19.0 N at 10 kn, 75.6 N at 20 kn, 170 N (38 lbf) at
30 kn**; a single 36 in sphere is 4.7 / 19.0 / 42.6 N. Design to 200 N with SF ≥ 5 → **≥1 kN MBL**;
1.5 mm Dyneema gives SF ≈ 10.

**Length and anchoring.** 150 ft = 46 m, 300 ft = 91 m; on a ~0.9 km-wide venue 150 ft buys the same
span for half the tether mass. Anchor, in order: **vehicle hitch / 2 in receiver shackle** (park so
the line leaves over the cab, not the glass), **3–4 × 20 kg sandbags on an anchor plate**, **12 in
ground screw** in caliche (bring a breaker bar). Hold **≥500 N** at a shallow angle, so use **two
independent anchors** plus a **swivel** at the neck and a carabiner so the line cannot saw the
balloon. Mark the *whole* line: bright orange plus a **streamer every 50 ft**.

**Blow-over — the real limit.** A tethered balloon blows downwind until tension balances drag:
**tan θ = drag ÷ free lift** **[DERIVED]**. For 4 × 36 in foil (free lift 0.99 N):

| Wind | Angle | Effective height, 150 ft line | 300 ft line |
|---|---|---|---|
| 2 kn | 37° | 119 ft | 238 ft |
| 3 kn | 60° | 76 ft | 151 ft |
| 5 kn | 78° | **31 ft** | 62 ft |
| 8 kn | 85° | **12 ft** | 25 ft |

**Adding balloons does not fix this** — drag scales with count exactly as lift does; 4 → 20 × 36 in
moves the 45° wind from 2.3 to only 3.7 kn. Because lift ∝ D³ but drag ∝ D², **the fix is one bigger
balloon**: 45° blow-over at **2.3 kn** for the foil cluster, **~5.7 kn** for a 36 in latex sphere,
**~8.9 kn** for 48 in, **~10.7 kn** for 60 in **[DERIVED]**. This is the strongest finding in the
document: **a foil cluster is a low-wind-only, wrong-shaped asset.** For a Texas afternoon either
fly one large latex sphere + HI-FLOAT, buy a **Helikite** (aerofoil kite-balloon that flies *up* into
the wind), or use a 40–60 ft mast.

**Go/no-go (anemometer at 2 m, on site):**

| Sustained | Gust | Action |
|---|---|---|
| ≤3 kn | ≤6 kn | GO — full 150 ft, near-vertical |
| 3–6 kn | ≤10 kn | GO — 60–80° blow-over; report *effective* height, not 150 ft |
| 6–9 kn | ≤14 kn | GO only with large-sphere/Helikite; foil cluster is a ground-level demo |
| **>9 kn** | **>14 kn** | **NO-GO — walk it down hand-over-hand** |
| Thunderstorm/virga/lightning <10 mi | — | **NO-GO** — a wet line is a conductor |

On 5–8 Nov 2019–2025 the daily max sustained wind at KERV never hit 20 kn (max 18 kn); 14% of days
had a daily max ≥15 kn **[DERIVED]**. A 9 kn rule will cost roughly **half the daylight hours** —
**06:00–09:00 is the reliable demo slot**.

---

## 4. FAA rules for moored balloons — 14 CFR Part 101 Subpart B

Text read from govinfo CFR XML ([Part 101](https://www.govinfo.gov/content/pkg/CFR-2024-title14-vol2/xml/CFR-2024-title14-vol2-part101.xml)).

**§101.1(a)(1) — the trigger.** Subpart B applies to "any balloon that is moored to the surface of
the earth or an object thereon and that has a **diameter of more than 6 feet or a gas capacity of
more than 115 cubic feet**." Two independent tests; either one triggers it.

| Balloon | Diameter | Capacity | Subpart B? |
|---|---|---|---|
| 18–36 in foil | 1.5–3 ft | 0.55–3.7 ft³ | **NO** |
| 48–60 in latex sphere | 4–5 ft | 33–65 ft³ | **NO** |
| 72 in sphere | 6.0 ft (not *more than* 6) | ~113 ft³ | **NO, borderline both tests** |
| 96 in sphere | 8 ft | ~256 ft³ | **YES — both fail** |

**So a party-size — even a 60 in — balloon sits entirely outside Subpart B.** The 150/500 ft,
pennant and rapid-deflation machinery does **not** attach to it. That is why a cheap demo is
possible at all.

**If you go big, these attach:**
- **§101.13:** no operation **<500 ft below cloud base**, **>500 ft AGL**, where ground visibility
  **<3 mi**, or **within 5 miles of any airport boundary**. *(§101.13(b) exempts a balloon below a
  structure's top and within 250 ft of it.)*
  → **This binds at your site.** KERV is 11 mi (clear), but **20TS Bains Private is 3.4 mi** and
  several strips sit at 5.2–9.6 mi **[DERIVED]**. A >6 ft / >115 ft³ balloon here would be inside
  20TS's 5-mile ring. **Clear it with the San Antonio FSDO before scaling up.**
- **§101.15:** unshielded balloon **>150 ft AGL** requires giving the **nearest FAA ATC facility**
  owner/operator names, balloon size, location, height, and date/time/duration — **≥24 h before**.
- **§101.17:** sunset–sunrise, balloon **and mooring lines** lit to FAA *Obstruction Marking and
  Lighting* standard; sunrise–sunset, lines need **colored pennants/streamers at ≤50 ft intervals
  beginning at 150 ft AGL, visible ≥1 mile**.
- **§101.19:** a device that **automatically and rapidly deflates the balloon if it escapes**; if it
  malfunctions, notify ATC immediately with location, time, estimated flight path.
- **§101.5 / §101.7:** prohibited/restricted areas; no hazard to persons or property.

**Part 77 — the one that bites even a small balloon.** Not scoped to balloon size
([Part 77](https://www.govinfo.gov/content/pkg/CFR-2024-title14-vol2/xml/CFR-2024-title14-vol2-part77.xml)):
**§77.9(a)** requires notice for "any construction or alteration that is **more than 200 ft AGL**";
**§77.7** files it on **FAA Form 7460-1 at least 45 days before**; **§77.17(a)(1)** makes >499 ft AGL
an obstruction. A balloon held **≤200 ft AGL** is below the notice threshold; a **300 ft tether**
(200–300 ft effective) can cross it. **If you fly 300 ft, file 7460-1 and carry a copy.**

> **Live risk (seen 2026-10-22):** the FAA OE/AAA portal reads *"Due to the government shutdown the
> FAA is unable to accept any new notices under 14 CFR Part 77... all submittals should be presumed
> to be a hazard to air navigation until advised otherwise"* ([oeaaa.faa.gov](https://oeaaa.faa.gov/oeaaa/external/portal.jsp)).
> **Do not depend on a Part 77 determination arriving before Nov 5.** Stay ≤200 ft AGL, or accept
> and document the risk.

**Separate gates, not aviation law:** (1) Bandera County ordinance and the organiser's written OK;
(2) check **TFR/NOTAM** every flight day ([tfr.faa.gov](https://tfr.faa.gov/tfr2/list.html));
(3) **drones** — brief every pilot on a hard altitude ceiling and a 100 ft no-fly cylinder around the
anchor; a Dyneema line is nearly invisible to a drone camera and the streamers are the only defence;
(4) **radio** is FCC Part 15 / band rules for the LR2021, not Part 101 — confirm the module's
authorised band, power and duty cycle.

---

## 5. Backwards logistics

| When | Do |
|---|---|
| **Now → 10 Oct** | Written landowner/organiser permission. **Decide one-hour demo vs 4-day tether.** Confirm whether drones fly. |
| **By 12 Oct** | Order **6 × 36 in round foil** + 4 × 18 in spares + **1.5 mm Dyneema** (200 ft and 300 ft). US supplier, 3–5 day ground. |
| **By 12 Oct** | **File Form 7460-1** if anything exceeds 200 ft AGL — §77.7 wants 45 days, and 12 Oct + 45 = 26 Nov. **File now or cap the tether at 150 ft.** |
| **By 19 Oct** | Quote helium at Airgas SA, nexAir, Linde, and the Kerrville dealer: **balloon-grade ≥99.99%**, single-day will-call, cylinder size, valve outlet, deposit, demurrage, hazmat fee. |
| **By 24 Oct** | **Home test:** inflate one balloon, weigh lift on a calibrated 0–500 g scale at 0/6/24/48 h; log it. Get *your* leak and lift numbers, not the vendor's. |
| **By 31 Oct** | **Bench-test the payload end-to-end** — ESP32-C3 + LR2021 through the relay; log RSSI/SNR at 100/300/1,000 ft on the ground. |
| **1–2 Nov** | **Tether dry-run**: 150 ft, anchor, swivel, streamers; two people walk it up and down; **practise the takedown**. |
| **3–4 Nov** | Pack spares (balloon, line, battery) and a **printed copy** of Part 101/77 and any FAA correspondence. |
| **Wed 4 Nov** | Site walk: anchor point upwind of the ground stations, overhead lines, drone launch area, line-of-sight to the far node. |
| **Thu 5 Nov** | **06:30** wind check → inflate → **07:00–09:00 demo** → **10:00** re-weigh, top up → **13:00** afternoon check (expect blow-over) → **17:30** down for the night, or leave up only if <5 kn with lighting and streamers set. |
| **Fri 6 – Sat 7** | Repeat: 06:30 lift re-weigh/top-up/neck-seal and line-chafe inspection; 13:00 go/no-go; log RSSI/SNR per altitude hourly. |
| **Sun 8 Nov** | Final flights, harvest range data, deflate, **recover every inch of line and every streamer** and pack out. |

---

## 6. Range data you can actually get

**Cheap, do these:** (1) **RSSI/SNR vs payload altitude** at fixed ground distance — the headline
deliverable, and it validates the link budget (`rf-link-budget` skill); (2) **PER vs distance** at
100/300/1,000/3,000 ft with fixed TX power, SF/BW, packet length, N ≥ 200 per point; (3) **blow-over
angle vs wind** — photograph the line against a marked post, log against the anemometer; cheapest
and most valuable on-site number, because it gives your *effective* height; (4) **the balloon-vs-mast
delta** — same link at 20 ft and 120 ft; that difference *is* the value proposition; (5) **lift decay
in grams vs hours** with temperature and humidity — free, and in no datasheet.

**Not cheap, don't attempt:** calibrated received power (needs a power meter and known antenna gain
— RSSI quoted as dBm without a calibration chain is a false claim); antenna pattern/gain; **any
absolute range claim** (report "at this site, this day, this wind", with blow-over angle attached);
availability statistics from four days of one weather regime.

---

## Open risks / human call

1. **The design may be wind-infeasible as specified.** A 4 × 36 in foil cluster is near-horizontal
   above ~4 kn and daylight is ≥8 kn half the time. **Decide now:** (a) dawn-only demo, (b) upsize to
   a 36–48 in latex sphere + HI-FLOAT, or (c) buy a Helikite. This is the deciding question and it
   is not the question the brief asked.
2. **Part 77 filing is currently blocked** by the FAA shutdown notice. Cap at 150 ft, or accept and
   document.
3. Cylinder size / valve outlet / regulator requirement **UNVERIFIED** — confirm at quote.
4. Tether breaking strengths are **[DERIVED]**, not datasheet — verify against the product bought.
5. **Drones + tether line** is the largest on-site safety exposure and no regulation covers it.
6. LR2021 **radio authorisation** is a separate FCC question — ask the vendor.

## Sources

**Regulation:** [14 CFR Part 101 (CFR-2024 title14 vol2)](https://www.govinfo.gov/content/pkg/CFR-2024-title14-vol2/xml/CFR-2024-title14-vol2-part101.xml) ·
[14 CFR Part 77](https://www.govinfo.gov/content/pkg/CFR-2024-title14-vol2/xml/CFR-2024-title14-vol2-part77.xml) ·
[FAA OE/AAA](https://oeaaa.faa.gov/oeaaa/external/portal.jsp) · [TFR list](https://tfr.faa.gov/tfr2/list.html)

**Government data:** [USGS MCS 2026 helium](https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-helium.pdf) ·
[USGS MCS 2025](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-helium.pdf) ·
[BLM helium sale](https://www.blm.gov/press-release/blm-completes-sale-federal-helium-system) ·
[BLM helium](https://www.blm.gov/programs/energy-and-minerals/helium) ·
[KERV ASOS archive](https://mesonet.agron.iastate.edu/request/download.phtml) ·
[OpenTopoData](https://api.opentopodata.org/v1/ned10m?locations=29.8292,-99.0153) ·
[OurAirports airports](https://davidmegginson.github.io/ourairports-data/airports.csv) /
[runways](https://davidmegginson.github.io/ourairports-data/runways.csv) ·
[Nominatim](https://nominatim.openstreetmap.org/search?q=165%20Wyatt%20Ranch%20Rd%2C%20Bandera%2C%20TX&format=json)

**Manufacturer/supplier:** [Balloon Time float times](https://www.balloontime.com/pages/how-to-use) ·
[tips](https://www.balloontime.com/pages/tips-and-tricks) ·
[Jumbo tank](https://www.balloontime.com/products/jumbo-helium-tank) ·
[Medium tank](https://www.balloontime.com/products/9-5-helium-tank) ·
[sell sheet](https://www.balloontime.com/cdn/shop/files/BT-Sell-Sheet_Medium-Jumbo_2026.pdf) ·
[Betallic HI-FLOAT](https://www.betallic.com/pages/hi-float-chart) ·
[Airgas San Antonio](https://locations.airgas.com/tx/sanantonio) ·
[nexAir](https://www.nexair.com/location-finder/) · [Matheson/Nippon Sanso](https://us.nipponsanso.com/contact-us/) ·
[Samson AmSteel](https://www.samsonrope.com/product/amsteel)

**Other:** [KERV](https://en.wikipedia.org/wiki/Kerrville_Municipal_Airport) ·
[Sovereignty Ranch](https://www.sovereigntyranch.com/)
