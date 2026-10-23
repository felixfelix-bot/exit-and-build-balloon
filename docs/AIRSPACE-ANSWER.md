# Airspace answer — tethered balloon at Exit & Build 6

**Question asked:** does flying a tethered helium balloon at Sovereignty Ranch
require an FAA filing, a notice, or a waiver?

**Answer: no — provided the balloon stays at or under 6 ft diameter / 115 ft³
*and* at or under 150 ft AGL.** The exemption is **size-based, not
altitude-based**. Below are the three independent gates, each verified against
primary sources on **2026-10-23**.

> **NOT LEGAL ADVICE.** An engineering reading of the primary sources, retrieved
> and re-checked today, so the rig can be built to a defensible default. The
> retrieval commands are in §6 so every claim is re-checkable. Get the
> organiser's own counsel/insurance to confirm before flight.

---

## 1. Site facts (verified 2026-10-23)

| Fact | Value | Source |
|---|---|---|
| Venue | Sovereignty Ranch, 165 Wyatt Ranch Rd E, Bandera, TX | event page |
| Coordinates | **29.8292 N, −99.0153 W** | Nominatim (recorded in `reports/BALLOON-LOGISTICS-TETHER-2026-11.md`) |
| Ground elevation | **471.6 m / 1,547 ft AMSL** | OpenTopoData NED10m (same report) |
| County | Bandera County, Texas | — |
| Event | Exit & Build 6, **5–8 November 2026** | event page |
| Hang-time | **4 days, confirmed** (operator, 2026-10-22) | this repo |

Ground elevation matters twice: it is ~2 % of the site lift figure, and it sets
what "150 ft AGL" means in AMSL for any notice that would otherwise be needed.

### Airfields — re-verified today from OurAirports

Distances are **great-circle from the venue coordinates above**, recomputed
2026-10-23 from the OurAirports `airports.csv` public-domain dataset (downloaded
today, HTTP 200; 12,750,621 bytes). Runway data from `runways.csv` (HTTP 200;
3,970,464 bytes).

| Ident | Name | Distance | Longest runway | Surface / lighted | Type |
|---|---|---|---|---|---|
| **20TS** | **Bains Private Airport** | **3.43 mi** | 1,900 ft | DIRT-TURF, **unlighted** | small_airport |
| US-3618 | Eagles Roost Airport | 3.47 mi | — | — | **closed** |
| US-5917 | Privilege Creek Ranch Airport | 5.29 mi | 1,991 ft *(previously recorded; no runway row in today's CSV)* | — | small_airport |
| 17TE | Comfort Airpark | 8.24 mi | 1,950 ft | TURF, unlighted | small_airport |
| TE90 | Flying L Airport | 9.55 mi | 3,600 ft | TURF, unlighted | small_airport |
| KERV | Kerrville / Kerr County (Louis Schreiner Field) | 11.03 mi | **6,004 ft** | ASPHALT, **lighted** | small_airport |

**20TS Bains Private is 3.43 mi away — inside the five-mile ring** that
§ 101.13(a)(4) describes. That is the fact that makes the size gate
load-bearing rather than academic.

---

## 2. The answer, as three independent gates

### Gate (i) — 14 CFR 101 Subpart B does not apply to this balloon

§ 101.1(a)(1) (verbatim, retrieved today) puts inside the part only:

> "any balloon that is moored to the surface of the earth or an object thereon
> and that has a **diameter of more than 6 feet** or a **gas capacity of more
> than 115 cubic feet**."

A **≤60 in sphere is 5.0 ft diameter / ~65 ft³**, and a Helikite in the planned
size class is smaller still on both axes. Both are **below both thresholds**,
therefore **outside Subpart B**. § 101.13(a)(4) lives *inside* Subpart B, so its
five-mile airport prohibition **does not attach** to this balloon — 20TS at
3.43 mi is irrelevant at this size.

The only relief inside the rule, § 101.13(b), is a *shielded* operation below the
top of a structure and within 250 ft of it. A balloon on a 200-acre open ranch
does not qualify — so **there is no altitude-based escape here.** The size gate
is the whole answer.

### Gate (ii) — 14 CFR Part 77 notice does not attach either

§ 77.9(a) (verbatim, retrieved today): notice is required for

> "(a) Any construction or alteration that is **more than 200 ft. AGL** at its
> site."

and § 77.7(b) requires **FAA Form 7460-1 at least 45 days before** the start
date. **Staying at or under 150 ft AGL is below the 200 ft trigger**, with 50 ft
of margin. The Part 77 imaginary-surface tests in § 77.9(b) scale off the nearest
runway of airports in § 77.9(d) — they are additional triggers, and the
200 ft / 45-day clock is the one this rig would otherwise trip.

**Portal status.** On 2026-10-22 the FAA OE/AAA portal was recorded as closed by
the government shutdown and refusing new notices. Re-checked **today
(2026-10-23)**: `https://oeaaa.faa.gov/oeaaa/external/portal.jsp` resolves with
an HTTP 200 to the portal shell at `/oeaaa/oe3a/main/#/home`. That tells us the
portal *serves*, not that a determination would arrive in time — **no filing was
made and no filing is proposed.** The design deliberately does not depend on a
determination arriving.

### Gate (iii) — therefore: no FAA filing, no notice

A rig that is **≤6 ft diameter / ≤115 ft³** *and* **≤150 ft AGL** needs:

- **no** Form 7460-1 (below § 77.9(a)'s 200 ft),
- **no** § 101.15 notice (the balloon is not in Subpart B at all; and § 101.15's
  own line is 150 ft AGL, which the rig also does not cross),
- **no** § 101.13(a)(4) airport conversation (the prohibition does not attach),
- **no** § 101.19 rapid-deflation device (Subpart B requirement, not applicable).

**The two conditions, stated as the conditions they are:**

1. **Diameter ≤ 6.0 ft AND gas capacity ≤ 115 ft³** — this is a *size* gate.
   Lowering the balloon does not buy compliance; only staying small does.
2. **Height ≤ 150 ft AGL** — keeps the Part 77 notice trigger (200 ft) and the
   § 101.15 notice line (150 ft) both uncrossed.

If either condition fails, **every** requirement above returns at once — and the
five-mile rule then fails outright at this site (20TS at 3.43 mi). That is the
cliff edge, and it is why the size gate must be treated as a hard constraint, not
a preference.

---

## 3. What does NOT go away

None of the above is a licence to be careless. The following still apply in full:

| Still applies | Why |
|---|---|
| **§ 101.7** — no hazard to persons or property | It governs **any** moored balloon, including one outside Subpart B ("Except as provided for in § 101.7" is written into § 101.1(a)(1) itself). With ~2,000 attendees this is the operative rule. |
| **Landowner / Bandera County permission** | The regulation is silent on private land. Written permission is required regardless. |
| **TFR / NOTAM check, every flight day** | Airspace closures are not Part 101 questions. Check each day of the 4-day run: `https://tfr.faa.gov/tfr2/list.html` (resolves HTTP 200 → `tfr3/`). |
| **Drones** | The venue's own drone operations, and any guest drones, are the largest on-site safety exposure and **no regulation in this document covers them.** Drone pilot brief + 100 ft no-fly cylinder + whole-line marking (`shopping-list.md` §7). |
| **Overnight / lighting** | The 4-day hang-time means the rig sits up overnight. See `docs/SITE-RULES-AND-FAA.md` §8: the ≤6 ft exemption also keeps the § 101.17 pennant/lighting duty away, but § 101.7 does not expire at dusk. |
| **Re-verify before flight** | The retrieval is 13 days before the event. Small gap, not zero. |

---

## 4. One-line answer to forward to the organiser

> **We are flying a tethered helium balloon at Sovereignty Ranch that is at or
> under 6 ft in diameter and at or under 150 ft above ground level — which keeps
> it entirely outside 14 CFR Part 101 Subpart B (the >6 ft / >115 ft³ threshold)
> and below the Part 77 200 ft notice threshold, so **no FAA filing, notice or
> waiver is required**; we just need your confirmation that (a) there is no TFR
> or local airspace restriction in force 5–8 Nov and (b) we have your **written
> permission** for the tethered operation on the property.**

---

## 5. Conditions attached to the answer (carry these, do not drop them)

1. The balloon must be **measured** before flight, not assumed: diameter ≤6.0 ft,
   gas capacity ≤115 ft³. A 60 in sphere is ~65 ft³ — fine. A 6 ft sphere is
   ~113 ft³ — at the threshold, not over it. **Anything larger re-enters
   Subpart B and this answer is void.**
2. Height of the **highest point of the balloon** ≤150 ft AGL, not the tether
   payout. A blow-over lowers effective height; it does not raise it.
3. This answer is **site-specific**. It applies to Sovereignty Ranch as
   characterised in §1. A different site with a nearer airport or a different
   elevation re-opens the question.
4. It is an **engineering reading**, not counsel. The organiser's own counsel or
   insurer should confirm — that is the operator action in the final report.

---

## 6. Sources and retrieval (2026-10-23)

All retrieved with `curl`. HTTP status recorded per request.

**CFR text — eCFR versioner API** (the eCFR HTML site and `/current/` path
redirect to a government-unblock interstitial; the API serves the XML directly):

```
curl --compressed \
  "https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-14.xml?part=101&section=101.1"
```

| Section | URL | HTTP |
|---|---|---|
| § 101.1 Applicability | `…title-14.xml?part=101&section=101.1` | **200** |
| § 101.13 Operating limitations | `…title-14.xml?part=101&section=101.13` | **200** |
| § 101.17 Lighting and marking | `…title-14.xml?part=101&section=101.17` | **200** |
| § 77.9 Construction or alteration requiring notice | `…title-14.xml?part=77&section=77.9` | **200** |
| § 77.7 Form and time of notice | `…title-14.xml?part=77&section=77.7` | **200** |

- CFR text edition retrieved: **2026-10-01**. The same text is published on
  govinfo (`govinfo.gov` CFR XML bulk data); eCFR is the continuously-updated
  official source and is what was fetched here.
- **Airfield data:** OurAirports public-domain CSVs —
  `https://davidmegginson.github.io/ourairports-data/airports.csv` (HTTP 200) and
  `…/runways.csv` (HTTP 200). Distances recomputed great-circle from
  29.8292 N, −99.0153 W.
- **FAA OE/AAA portal:** `https://oeaaa.faa.gov/oeaaa/external/portal.jsp` →
  HTTP 200 → `https://oeaaa.faa.gov/oeaaa/oe3a/main/#/home` (checked 2026-10-23).
  No filing made.
- **TFR list:** `https://tfr.faa.gov/tfr2/list.html` → HTTP 200 → `tfr3/`.

**Re-verify before the event.** Regulations and airfield status change; the
13-day gap between this retrieval and the event is small but not zero.
