# Site rules and FAA — Sovereignty Ranch, Bandera County, Texas

**Scope:** legal/regulatory constraints on flying a *tethered* helium balloon at
Exit & Build 6, 5–8 November 2026.

> **NOT LEGAL ADVICE.** This is an engineering reading of the primary sources,
> retrieved 2026-10-22, so the design can be built to a defensible default. Get
> the organiser's own counsel/insurance to confirm before flight. Primary sources
> and retrieval method are recorded at the bottom so every claim is re-checkable.

---

## 1. Site facts

| Fact | Value | Source |
|---|---|---|
| Venue | Mollie Engelhart's Sovereignty Ranch, Bandera, Texas | event page |
| County | Bandera County | — |
| Approximate elevation | **471.6 m / 1547 ft AMSL** | DEM sample at site coordinates |
| Area | ~200 acres (≈900 m × 900 m) | event page |
| Nearest airfield #1 | **20TS — Bains Private Airport**, 1420 ft elev, 1900 ft runway, **3.43 mi** away | OurAirports runways.csv |
| Nearest airfield #2 | **US-5917 — Privilege Creek Ranch**, 1991 ft runway, **5.29 mi** away | same |
| Nearest airfield #3 | **US-3618 — Eagles Roost (closed)**, 1418 ft, **3.47 mi** | same |
| Terrain | Texas Hill Country, ~6–8 m cedar canopy | — |
| Season | November — convective storms possible, night-time temps near/below freezing | — |

**Population density at the event:** ~2,000 attendees. This matters for § 101.7.

### Consequence: § 101.13(a)(4) — the five-mile airport rule

`§ 101.13(a)(4)` prohibits moored-balloon operation **within five miles of the
boundary of any airport** unless paragraph (b) applies.

**20TS Bains Private Airport is 3.43 miles away — inside the five-mile ring.**
Two more fields are at 3.47 mi and 5.29 mi.

Paragraph (b) provides the only relief:

> "(b) Paragraph (a) of this section does not apply to the operation of a balloon
> or kite **below the top of any structure and within 250 feet of it**, if that
> shielded operation does not obscure any lighting on the structure."

A balloon at 150 ft AGL on a 200-acre open ranch is **not** a shielded operation
below the top of a structure. **So the plain reading of § 101.13(a)(4) prohibits a
normal tethered balloon flight at this site.**

> ⚠️ **This is the most important finding in this document, and it changes the
> plan.** It is not an altitude problem — it is a *location* problem. Lowering the
> balloon does not fix it. The rule is a flat prohibition, not a height threshold.

**This must be resolved with the organiser before any equipment is bought.** The
realistic paths are: (i) obtain FAA relief/authorisation for the specific site, or
(ii) get written confirmation from the controlling FAA ATC facility that they do
not consider the operation to fall under the prohibition (20TS is a *private*
strip — whether it counts as "an airport" for this purpose is exactly the kind of
question that needs an official answer, not an engineer's opinion), or (iii) design
the demo to avoid the rule entirely (see §5). **Do not assume private airfields
are exempt** — the regulation says "any airport".

---

## 2. Applicability thresholds — § 101.1

Part 101 Subpart B applies to a moored balloon only if it exceeds:

> **§ 101.1(a)(1)** — "any balloon that is moored to the surface of the earth or
> an object thereon and that has a **diameter of more than 6 feet** or a **gas
> capacity of more than 115 cubic feet**."

**This is a genuinely useful escape hatch.** A balloon at or below **6 ft (1.83 m)
diameter AND ≤115 ft³** is outside Part 101 Subpart B entirely.

| Balloon | Diameter | Gas capacity | In scope of Part 101 Subpart B? |
|---|---|---|---|
| 18" foil | 1.5 ft | ~1.8 ft³ | **No** |
| 24" foil | 2.0 ft | ~4.2 ft³ | **No** |
| 36" foil | 3.0 ft | ~14 ft³ | **No** |
| 4 ft foil | 4.0 ft | ~33 ft³ | **No** |
| 6 ft sphere | 6.0 ft | ~113 ft³ | **No** — at the threshold |
| >6 ft / >115 ft³ | — | — | **Yes** |

> **Design lever:** a cluster of several ≤6 ft balloons, or a single ≤6 ft
> balloon, stays outside Subpart B. Whether a *cluster* is treated as one balloon
> is itself a question — ask, do not assume. But the size threshold is real and
> it is the cheapest compliance path available.

---

## 3. The rules that apply IF you exceed the threshold

All quoted from 14 CFR Part 101 Subpart B, retrieved 2026-10-22, in force.

### § 101.13 Operating limitations

> (a) … no person may operate a moored balloon or kite—
> (1) **Less than 500 feet from the base of any cloud**;
> (2) **More than 500 feet above the surface of the earth**;
> (3) From an area where the **ground visibility is less than three miles**; or
> (4) **Within five miles of the boundary of any airport.**

**Hard ceiling: 500 ft AGL.** Not a notification threshold — a prohibition.
Our 150 ft / 300 ft design sits comfortably inside it.

### § 101.15 Notice requirements

> No person may operate an unshielded moored balloon … **more than 150 feet above
> the surface of the earth** unless, **at least 24 hours before** beginning the
> operation, he gives the following information to the **FAA ATC facility that is
> nearest** to the place of intended operation: (a) names and addresses of owners
> and operators; (b) size of the balloon; (c) location; (d) height above surface;
> (e) date, time, and duration.

**150 ft AGL is the notification line.** Above it → notify the nearest FAA ATC
facility ≥24 h ahead. Note this is *notification*, not approval — but given
§ 101.13(a)(4) above, treat it as a conversation, not a formality.

### § 101.17 Lighting and marking

> (a) … between **sunset and sunrise** unless the balloon … and its mooring lines
> are **lighted** so as to give a visual warning equal to that required for
> obstructions to air navigation…
> (b) … between **sunrise and sunset** unless its mooring lines have **colored
> pennants or streamers attached at not more than 50 foot intervals beginning at
> 150 feet** above the surface, **visible for at least one mile**.

**Practical consequence:** daylight-only operation above 150 ft requires pennants
every 50 ft from 150 ft upward. Multi-day operation that runs into the evening
requires lighting — which draws power and is another failure mode for a tethered
rig. **Recommend: daylight-only, and keep the tether below 150 ft where possible.**

### § 101.19 Rapid deflation device

> No person may operate a moored balloon unless it has a device that will
> **automatically and rapidly deflate the balloon if it escapes** from its
> moorings. If the device does not function properly, the operator shall
> immediately notify the nearest ATC facility …

**Engineering requirement:** a tether-failure deflation mechanism is mandatory if
in scope. For a foil balloon this is nontrivial — this is a real design cost, not
a checkbox.

### § 101.7 Hazardous operations

> (a) No person may operate any moored balloon … in a manner that **creates a
> hazard to other persons, or their property**.

With ~2,000 attendees this is the catch-all that governs the wind-limit rule and
the tether-hazard plan.

---

## 4. Summary decision table

| Design | Subpart B applies? | § 101.13(4) airport rule? | Notice >150 ft? | Deflation device? |
|---|---|---|---|---|
| ≤6 ft balloon, ≤150 ft AGL, daylight | **No** | **No** (outside Subpart B) | no | no |
| ≤6 ft balloon, >150 ft AGL | No | No | **no** — § 101.15 only binds in-scope balloons | no |
| ≤6 ft balloon, ≤150 ft AGL, **overnight (4-day)** | **No** | **No** | no | no — **but the rig is unattended at night; § 101.7 still applies** |
| >6 ft / >115 ft³, ≤150 ft AGL | **Yes** | **YES — 3.43 mi from 20TS fails it** | no | **yes** |
| >6 ft / >115 ft³, >150 ft AGL | Yes | YES | **yes, ≥24 h** | yes |

> **Read this table as the design brief:** stay under 6 ft diameter and you are
> outside the whole subpart. That is worth more than any amount of paperwork.

---

## 5. Design options in order of preference

1. **Multiple ≤6 ft foil balloons, ≤150 ft AGL, daylight only.** Outside Subpart B
   entirely. Cheapest, fastest, most defensible. Payload splits across balloons or
   one balloon carries a very light (<100 g) payload.
2. **Single ≤6 ft foil balloon** if one is enough for the payload mass.
3. If the payload genuinely needs more lift: consult the FAA ATC facility about
   the 20TS five-mile rule **before** buying, and be ready to fall back to (1).
4. **Do not** plan a >6 ft balloon without resolving § 101.13(a)(4) first — the
   airport is inside the ring and that is a flat prohibition, not a negotiation
   over altitude.

---

## 6. Actions

- [ ] **A1.** Confirm with the organiser whether the event has any existing FAA
      coordination, waivers, or drone operations plan (drones imply they have
      already spoken to someone about airspace).
- [ ] **A2.** Determine whether **20TS Bains Private Airport** is active and
      whether the FAA treats a private strip as "an airport" for § 101.13(a)(4).
      **Ask the FAA ATC facility directly — do not let this be an engineer's
      guess.**
- [ ] **A3.** Decide balloon size against the 6 ft / 115 ft³ threshold and record
      the decision.
- [ ] **A4.** If staying in scope: draft the § 101.15 notification and identify
      the nearest FAA ATC facility.
- [ ] **A5.** If staying in scope: design and test the § 101.19 rapid deflation
      device.
- [ ] **A6.** Write the § 101.7 wind-limit go/no-go rule (see logistics report).
- [ ] **A7.** Check whether the venue's own mesh/drone operations already occupy
      the airspace or the spectrum.

---

## 7. Sources and retrieval

Retrieved 2026-10-22 from the **eCFR API** (the HTML site blocks automated
access; the API requires an `Accept-Encoding` header that permits compression,
otherwise it returns HTTP 406).

```
curl --compressed \
  "https://www.ecfr.gov/api/versioner/v1/full/2026-10-01/title-14.xml?part=101&section=101.13"
```

- 14 CFR Part 101, Subpart B — Moored Balloons, Kites, Amateur Rockets, Unmanned
  Free Balloons: § 101.1 (applicability), § 101.7 (hazardous operations),
  § 101.13 (operating limitations), § 101.15 (notice), § 101.17 (lighting and
  marking), § 101.19 (rapid deflation)
- Airfield data: OurAirports `runways.csv` (public domain)
- Site elevation: DEM sample at venue coordinates

**Re-verify before the event.** Regulations and airfield status change; the
eleven-day gap between this retrieval and the event is small but not zero.

---

## 8. Addendum (2026-10-23) — 4-day hang-time: overnight and lighting

**Hang-time is CONFIRMED at 4 days** (operator, 2026-10-22). One consequence is
regulatory, and it is not free: **daylight-only is no longer a free choice.**
A rig that runs 5–8 November sits up overnight unless it is struck each evening.

| § 101.17 duty | When it applies | What it requires |
|---|---|---|
| **(b) marking** | sunrise → sunset | colored pennants/streamers at **≤50 ft intervals, beginning at 150 ft** above the surface, visible ≥1 mile |
| **(a) lighting** | sunset → sunrise | the balloon **and its mooring lines** lighted to give a visual warning equal to an obstruction to air navigation |

**The exemption is what keeps this cheap — and it is size-based, not
altitude-based.** § 101.1(a)(1) puts only balloons **>6 ft diameter or
>115 ft³** inside Subpart B. A ≤60 in sphere (65 ft³) or any Helikite in the
planned size class stays **outside Subpart B entirely**, so neither the
§ 101.17(b) pennants nor the § 101.17(a) lighting duty attaches. **Flying lower
buys nothing; flying smaller buys everything.** If the envelope ever crosses
6 ft / 115 ft³, all of § 101.13–101.19 return at once — including the five-mile
airport rule and the § 101.19 rapid-deflation device.

**Two design consequences for the 4-day run:**

1. **A night-capable rig must be designed for it or struck each evening.** If the
   envelope is in scope, lighting the envelope *and the line* for four nights is
   a real power draw and a new failure mode — it collides directly with the
   solar-vs-conductive-tether decision in `shopping-list.md` (section **Power**).
2. **Unattended overnight means the go/no-go rule does not end at dusk.** The rig
   must either be walked down or left in a state that survives the night wind;
   that dusk decision is specified in `docs/RUNBOOK-event-operations.md`.

**Recorded position: keep the envelope ≤6 ft and stay outside Subpart B, and
strike or secure the rig at dusk rather than light it.** That keeps the pennant
and lighting machinery, and the power it needs, out of the design. If the
organiser wants a lit overnight rig, that is a scope change with a power budget
attached — decide before ordering.

**What does not go away overnight:** § 101.7 (no hazard to persons or property)
still applies to an out-of-scope balloon, and an unattended line at 02:00 is
exactly the sort of thing it governs. Landowner permission does not expire at
sunset either.
