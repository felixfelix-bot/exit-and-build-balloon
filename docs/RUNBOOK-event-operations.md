# Runbook — 4-day tethered relay operation, Exit & Build 6

**Site:** Sovereignty Ranch, 165 Wyatt Ranch Rd E, Bandera TX
**Window:** 5–8 November 2026 (4 days, confirmed)
**Rig:** Helikite primary + mast control; latex sphere as cheap fallback
**Altitude:** ≤150 ft AGL (hard cap — Part 77 notice threshold is 200 ft and the
OE/AAA portal is closed)

---

## 1. The one thing to understand before you rig anything

**This balloon is a range extender, not a network.** With two ground nodes it adds
one hop. It earns its place **only where the ground path is obstructed.**

| Ground separation | Direct margin (915, FLRC-1300) | Balloon adds | Verdict |
|---|---|---|---|
| 200 m | 51.8 dB | +5.2 dB, **halves throughput** | **Walk the laptops closer. Do not fly.** |
| 800 m, clean LOS | 39.8 dB | +5.96 dB | Marginal at best |
| 800 m, **blocked ≥6 m** | 39.8 dB − 14–20 dB | **+14–20 dB recovered** | **This is the only regime where it wins** |

**Walk the venue on 4 Nov and mark the endpoint positions so the obstruction is
real** — Barn, shelter, tree line, grade. If the two endpoints have clean LOS a
knowledgeable observer will correctly conclude the balloon is doing nothing, and
they will be right.

---

## 2. Daily cycle

| Time | Action |
|---|---|
| **06:30** | Wind check at 2 m. Apply the go/no-go table (§4). Weigh lift on the 0–500 g scale. Decide: fly / mast / no-fly. |
| **07:00–09:00** | **Primary demo window.** Mean wind 3.9 kn, ≤5 kn in 68% of hours. This is when the rig actually performs. |
| **09:00–10:00** | Run the A/B measurement (§5) while conditions hold. |
| **10:00** | Re-weigh lift. Top up if down >20% from morning. Inspect neck seal and line chafe. |
| **13:00** | Afternoon check. **Expect blow-over** — mean daylight wind is 7.6 kn and half of daylight hours are ≥8 kn. |
| **17:30** | Dusk decision: strike for the night, or leave up. **Leaving it up requires lighting** per §101.17(a). |
| Overnight | If left up: lit, streamers set, and someone on site. If struck: pack down. |

**The honest expectation: this rule costs roughly half the daylight hours.**
06:00–09:00 is the reliable slot. Build the event schedule around that.

---

## 3. Pre-flight checklist (each day)

- [ ] Anemometer reading at 2 m, sustained and gust
- [ ] Lift weight on calibrated scale (grams) — log it
- [ ] Line inspection: chafe, knots, swivel
- [ ] Anchor check: **two independent anchors**, ≥500 N hold at shallow angle
- [ ] Streamers present every 50 ft from 150 ft up (daylight requirement)
- [ ] **TFR/NOTAM check** — https://tfr.faa.gov/tfr2/list.html
- [ ] Drone situation: has anyone launched? Brief them if so
- [ ] Radio link up: payload beaconing, RSSI/SNR logged at both ends
- [ ] Payload power: tether feed voltage at the top, and at the ground

---

## 4. Go/no-go wind rule (anemometer, 2 m, on site)

| Sustained | Gust | Action |
|---|---|---|
| ≤3 kn | ≤6 kn | **GO** — full 150 ft, near-vertical |
| 3–6 kn | ≤10 kn | **GO** — 60–80° blow-over. **Report *effective* height, not 150 ft** |
| 6–9 kn | ≤14 kn | GO only with the Helikite. A sphere/foil cluster is a ground-level demo |
| **>9 kn** | **>14 kn** | **NO-GO — walk it down hand-over-hand** |
| Thunderstorm / virga / lightning <10 mi | — | **NO-GO — a wet line is a conductor** |

**Measure the effective height, don't assume it.** Photograph the line against a
marked post and log the angle against the anemometer reading. That number is
cheapest-and-most-valuable thing you will collect on site, because it tells you
what altitude you actually had — the link budget is only meaningful at a known
height.

---

## 5. The A/B measurement — this IS the deliverable

**Do not just demonstrate the relay. Measure what it buys.**

Two endpoints, fixed positions, obstructions present. Run each of these at
100 / 300 / 1000 / 3000 ft separation:

1. **Direct ground-to-ground** — balloon grounded or absent
2. **Via the balloon** — same positions, same power, same modulation
3. **Via the mast** — same positions, 20 ft and 120 ft

Record per configuration: PER (N ≥ 200 packets), RSSI, SNR, and the wind/angle at
the time.

**The direct-vs-relayed delta is the result.** It is what turns "we flew a
balloon" into "we measured what a balloon buys you" — and the mast row is what
separates "the balloon helped" from "altitude helped", which are very different
claims.

### Cheap, do these
- RSSI/SNR **vs payload altitude** at fixed ground distance — the headline number
- PER **vs distance** at the four separations, fixed everything else
- **Blow-over angle vs wind** — photo against a marked post
- **Balloon-vs-mast delta** — the value proposition, stated as a number
- **Lift decay in grams vs hours**, with temperature and humidity — free, and in no datasheet

### Do not attempt
- Calibrated received power (needs a power meter and known antenna gain; RSSI
  quoted as dBm without a calibration chain is a false claim)
- Antenna pattern / gain measurement
- Any **absolute range claim** — report "at this site, this day, this wind", with
  the blow-over angle attached
- Availability statistics from four days of one weather regime

---

## 6. Failure playbook

### The bridge radio locks up (the documented 3–5 min failure)
**Symptom:** link drops, then recovers — or does not. The valid-frame watchdog
resets the radio after 15 s of no valid FIPS frame.

- [ ] First: check it is not the harness. Is the marker file actually present on
      the remote side? A path bug reads exactly like a deaf radio.
- [ ] Check TX `sent_ok` — if TX sent and RX got zero, suspect the receiver side,
      not "nothing was transmitted".
- [ ] Confirm both ends got the **same** `START` line. An RX that never got it
      reports `crc_err = <n sent>`, which mimics RF death.
- [ ] If genuinely locked: power-cycle the bridge. Log the time and the run time
      since last reset — that is the MTBF data for the 4-day claim.

> **Known and expected:** 2.4 GHz RX degrades after ~2.5–5 min of sustained
> operation under WiFi interference. This is a measured limitation, not a fault.
> It is also the argument for 915 at the event.

### The balloon is at the wrong angle and the link is marginal
- [ ] Measure the actual angle. Report effective height.
- [ ] Switch to the mast — it does not care about wind.
- [ ] If the obstruction story is the point: move an endpoint, do not add power.

### Wind comes up mid-demo
- [ ] Walk it down hand-over-hand. Do not let the line run through hands.
- [ ] Do not chase it with a vehicle.

### A drone appears
- [ ] Halt flight, brief the pilot: hard altitude ceiling, 100 ft no-fly cylinder
      around the anchor.
- [ ] A **Dyneema line is nearly invisible to a drone camera** and the streamers
      are the only defence. This is the largest on-site safety exposure and no
      regulation covers it.

---

## 7. Teardown, every day and at the end

- [ ] Deflate / recover the Helikite or balloon
- [ ] **Recover every inch of line and every streamer** — a stranded Dyneema line
      is invisible and dangerous
- [ ] Pack the anchor hardware
- [ ] Log the day's lift decay, wind, effective height, and link results
- [ ] Charge / swap payload and ground batteries

---

## 8. What must be true for this runbook to be used at all

| Gate | Status |
|---|---|
| E80 boards flashable (SWD works) | **OPEN** — see `docs/E80-VERIFICATION-CHECKLIST.md` V1 |
| 915 MHz sweep passes | **OPEN** — V3. Fall back to 2.4 GHz if it fails |
| STM32 bridge firmware on the E80 (framing, FLRC pipe, watchdog) | **OPEN** — `fips_bridge.cpp` is ESP-IDF and does NOT run on STM32. See README "Why the ESP32-C3 was in the plan" |
| Host↔E80 serial link at ≥921600 baud | **OPEN** — at 115200 it caps the link at 11.5 kB/s, 4× worse than the radio. The E80 console supports 2 Mbaud |
| Helikite ordered and delivered | **OPEN** — UK lead time is the longest item |
| Written landowner permission | **OPEN** — operator action |

**If the E80 flash path does not resolve, this runbook has no radio to fly with.**
That is the first gate, not the last.
