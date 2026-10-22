# PLAN — Tethered balloon bent-pipe relay, Exit & Build 6

**Event:** 5–8 November 2026 · Sovereignty Ranch, Bandera TX
**Urgency: NOW** — hard deadline, ~2 weeks to event, procurement lead times are the binding constraint
**Quota basis at planning:** z.ai keys locked (ours 999%); dispatch ALLOWED via `opencode_go` lane
@ $0.0016/M (glm-5.2), ceiling $0.70/M — not paid burn
**Status:** planning complete for phase 0–1; feasibility gates open

---

## 1. Objective

Fly one or more **tethered** helium balloons carrying a **transparent radio relay**
so that **FIPS** IP traffic crosses the venue, and use the same rig to collect
radio-characterisation data (PER / RSSI / SNR vs distance and altitude).

Secondary: demonstrate that **TollGate** can run over the same path.

**Non-goals:** free-flight, long duration, solar power, PCB fabrication, or any
protocol work on the balloon. The balloon is a dumb pipe.

---

## 2. Decisions taken (with the evidence)

| # | Decision | Rationale |
|---|---|---|
| D1 | **Balloon is a transparent PHY relay; FIPS stays on the ground** | ADR-014. The bridge holds no key and must not inspect payload. There is already a *proven* FIPS-over-LR2021 bridge (June 2026: Noise XK handshake, 1071 B / 5-fragment datagram, 30-min link survival). Zero new protocol work for 2 nodes. |
| D2 | **Symmetric 915 MHz, FLRC-1300 kbps, +22 dBm** | 18.55 dB more budget than 2.4 GHz (10 dB PA + 8.55 dB FSPL). FLRC-1300's 1200 kHz width clears the 15.247(a)(2) 6 dB BW floor. **FLRC-260 is non-compliant** as a fixed-channel DTS (300 kHz). |
| D3 | **Drop the cross-band (2.4 GHz / 915) design** | One LR2021 cannot serve two bands at once (full re-init, tens of ms) → needs 2 radios *everywhere*; it does not remove the need for TDMA (each RF island is still a collision domain); and it throws away 18.55 dB on the 2.4 GHz leg. Superseded by D2. |
| D4 | **Do not use 433 MHz** | US 433.92 is 47 CFR 15.231 (periodic/control, field-strength limits) — not a data band. 902–928 gives +30 dBm conducted / +36 dBm EIRP with no duty-cycle limit. |
| D5 | **Scheduling is ground-derived from absolute UTC; the balloon only follows** — *deferred: not needed at 2 nodes* | A fixed UTC-derived slot table is a *constant*, not a decision — so the relay stays ADR-014 transparent while collisions are prevented. 50 ms frame / 8 slots / balloon relays slot 6. **With a single ground pair there is no N² collision problem, so this drops to OPTIONAL** (see §3.1). |
| D6 | **Scope: a 2-node bent pipe** (operator decision, 2026-10-22) | The balloon is a bent pipe between exactly two ground nodes for now. This removes the transport-topology blocker (FIPS serial is point-to-point: one bridge = one peer) and removes the TDMA requirement. N=5 is documented in `reports/ARCH-5NODE-BENT-PIPE-2026-11.md` as a future option, not this event's deliverable. |
| **D7** | **FLY THE RELAY ONLY WHERE THE GROUND PATH IS OBSTRUCTED. This is the entire justification for the balloon.** | See §2.1 — this is the load-bearing decision, not a caveat. |
| D8 | **Mylar/foil balloons, not latex** | Latex loses helium in ~12–24 h; a 4-day event means daily re-inflation. Foil holds for weeks. |
| D9 | **≤150 ft (45.7 m) AGL by default; 300 ft if paperwork allows** | 150 ft is the easy 14 CFR 101 Subpart B envelope. **300 ft costs only 0.16 dB of FSPL but more than doubles near-end clearance** (x_min 11.9 m vs 30.4 m) — pursue it for *geometry*, not power. |
| D10 | **Do NOT fabricate the v10 hub PCB** | JLCPCB 2-layer + assembly is ~2 weeks — lands on the event with zero margin. Existing inventory (20× ESP32-C3 Mini V1, 4× NiceRF LR2021, 3× E28-2G4M27S) builds a working rig today. |
| D11 | **Buy nothing ourselves; source and link only** | Operator instruction. Deliverable is a shopping list with verified US links. |

---

## 2.1 Why the balloon exists at all — **read this before rigging anything**

**With two ground nodes the balloon is nothing more than a range extender on a
line between them. It is not a network. It is not a mesh. It is one extra hop.**

That is not a flaw — it is the entire design — but it means the balloon has to
**earn its place on every single flight**, and the numbers say it usually does not:

| Ground separation | Direct ground path margin (915, FLRC-1300) | Balloon's contribution | Verdict |
|---|---|---|---|
| 200 m | **51.8 dB** | **+5.2 dB** relay gain — and it **halves** throughput (half-duplex) | **The balloon is a net loss.** Do not fly it. |
| 800 m, clean LOS | 39.8 dB | +5.96 dB — a rounding error beside 40 dB | **Marginal. Probably not worth it.** |
| 800 m, **blocked by ≥6 m** | 39.8 dB minus 14–20 dB of knife-edge loss | **+14–20 dB recovered** | **This is the only regime where the balloon wins.** |

### The one thing the balloon actually sells

**Line of sight over an obstruction.** Nothing else.

Knife-edge diffraction loss, `L = 6.9 + 20·log10(√((v−0.1)²+1) + v − 0.1)`:

| Obstruction above the direct LOS path | 200 m @915 | 800 m @915 | 800 m @2450 |
|---|---|---|---|
| 1.5 m (a person) | 10.5 dB | 8.3 dB | 9.7 dB |
| 3 m (a vehicle / cedar) | 14.2 | 10.5 | 13.0 |
| **6 m (canopy)** | 19.4 | **14.2** | 17.8 |

So: **fly the relay only when the 800 m ground path is obstructed by ≥6 m of
terrain, cedar canopy, buildings or vehicles.** In that regime the balloon
recovered 14–20 dB — which beats the ~6 dB it costs in path length plus the
throughput halving. Outside that regime, terminate both endpoints on the ground
and leave the balloon in the bag.

### Consequences for how we present it

1. **The demo must be staged so that the obstruction is real and visible.** If the
   two laptops have clean LOS, a knowledgeable observer will correctly conclude
   the balloon is doing nothing. Pick the endpoint positions to put the Barn,
   shelter, tree line or grade between them.
2. **Measure both paths, not just the balloon path.** A/B the direct link and the
   relayed link at the same positions. The delta *is* the deliverable — it is what
   turns "we flew a balloon" into "we measured what a balloon buys you."
3. **This is also the range data.** The same A/B at several separations produces
   the PER/RSSI/SNR-vs-distance characterisation the bench programme wants, with
   the balloon as a controlled variable rather than a novelty.

### Near-end grazing is the quiet failure mode

The ray leaves an endpoint at 1.5 m and rises linearly. At 800 m separation and
150 ft altitude it is only **2.6 m above ground 10 m from the endpoint**, 3.7 m at
20 m, 7.0 m at 50 m. A crowd, a truck, a tent or a parked RV inside the first
~30 m blocks it outright:

- First-Fresnel clearance past a 3 m obstruction needs **x_min = 30.4 m** at
  45.7 m (150 ft) altitude, versus **11.9 m at 91.4 m (300 ft)**.

> **This is the argument for 300 ft.** It costs only 0.16 dB of FSPL — nothing —
> but it more than halves the near-end clearance distance. Pursue the higher
> altitude for **geometry**, not for power. If § 101.15 notice and the
> § 101.13(a)(4) airport question can be resolved, 300 ft is the better rig.

---

## 3. Architecture

```
laptop A ── fips ── PTY ── serial_udp_bridge.py ── USB CDC ── ESP32-C3 ── LR2021 ──┐
                                                                                 │ 915 MHz
                                                              BALLOON  relay     │ slot 6
                                                                                 │ 915 MHz
laptop B ── fips ── PTY ── serial_udp_bridge.py ── USB CDC ── ESP32-C3 ── LR2021 ──┘
```

Chain at both ends: `fips → PTY → serial_udp_bridge.py → USB CDC → ESP32-C3 → LR2021 → antenna`

The balloon carries the **same modem pair, cut-through** — no FIPS in the air.

### Link budget (915 MHz, +22 dBm, 2 dBi dipoles, FLRC-1300)

| | Value |
|---|---|
| EIRP | +24 dBm (12 dB under the legal ceiling — **the PA binds, not the law**) |
| Sensitivity | −104.5 dBm |
| Margin @ 403 m leg (800 m separation, 150 ft) | **45.7 dB** |
| Margin @ 800 m direct | 39.8 dB |
| Relay gain over direct | **+5.96 dB** |
| Airtime | 3.19 ms/frame, 9.6 ms/hop |
| Goodput | ≈49 kB/s ≈ 394 kbps sustained (half-duplex) |

---

## 4. Phases

### Phase 0 — Feasibility gates (**do this week; nothing else proceeds until green**)

| Gate | What | Blocks |
|---|---|---|
| G1 | **E80 board SKU identified** — 400 or 900? Is there a 2.4 GHz jack? | Band plan, payload radio choice |
| G2 | **Flash path resolved** (SWD chip-detect at minimum) | Everything hardware |
| G3 | **915 MHz sweep runs** — never been run on this bench | D2 |
| G4 | **FIPS revision with serial transport pinned & vendored** | The entire ground chain |
| G5 | Watchdog soak ≥4 h — mean time between failures | 4-day operation |
| G6 | Organiser answers: hang-time (4 days vs 1 hour), helium supply | Logistics, BOM |

See `docs/E80-VERIFICATION-CHECKLIST.md` for the executable form of G1–G5.

### Phase 1 — Bench: 2 nodes over the bridge (no balloon)

Prove the ground chain end-to-end on a desk, then at 10–100 m outdoors.
Reuse the E80 range-bench tooling (`range_check.py`, `merge_csvs.py`,
`e80_bench_ctl.py`) for PER/RSSI/SNR capture.

**Band order revised: run this on 2.4 GHz first** (proven path, session
`2608222108`), then repeat at 915 MHz (V3). See
`HARMONICS-AND-BAND-PLAN.md` §6 for the full trade.

Deliverable: a pass/fail matrix over {260, 650, 1300 kbps} × {10, 50, 100 m} on
both bands, plus the measured FLRC-650 6 dB bandwidth.

### Phase 2 — Firmware (`ARCH-5NODE` §4)

Ordered by risk; **C1 first** — until one task owns the radio, nothing else can
be made deterministic.

**Scope revised 2026-10-22: the deliverable is a 2-node bent pipe, so C2 (TDMA)
is no longer required.** The bridge's existing 0–3 ms TX jitter was designed for
exactly the 2-node case.

| Item | Effort | Required for a 2-node demo? |
|---|---|---|
| C1 single radio owner + TX queue | ~1.5 d | **YES** — root cause of the 3–5 min lockup |
| C2 TDMA slot gate; delete jitter | ~1 d | **NO — deferred.** No N² collision problem at N=2. Needed only if we go >2 nodes. |
| C3 UTC time base | ~1 d + GPS wiring | **NO — deferred.** Only exists to serve C2. |
| C4 4-day-survivable watchdog | ~0.5 d | **YES** if the balloon stays up; else a shorter soak is acceptable |
| C5 variable packet length | ~2 h | **YES** — ~4–5× airtime recovery |
| C6 unattended safety (blink loops, counters, RTC persistence) | ~0.5 d | **YES** — without counters a failure on site is undiagnosable |
| C7 addressing / ingress suppression | ~3–5 d | no |
| C8 band switching | ~2–3 d | no |
| C9 queue depth | folded into C1 | — |

**Revised critical path:**

```
E80 flash path (V1)  →  2.4 GHz 2-node link over the bridge  →  C1  →  C5  →  C6
                                                                 ↓
                                                    balloon rig + A/B obstruction test
                                                                 ↓
                                                     915 sweep passes? → event band
```

TDMA (C2/C3) and the whole 5-node analysis stay in the repo as documented future
work; they are **not** on this event's path.

### Phase 3 — Balloon integration

Rig assembly, measured mass budget, tether, and the **relay-only-when-obstructed**
block map of the venue. Fly at 150 ft, then 300 ft if paperwork allows.

### Phase 4 — Event operation

4-day (or scheduled-hour) run with the soak-tested watchdog, stats telemetry, and
a go/no-go wind rule.

---

## 5. Open blockers (operator input required)

| # | Blocker | Owner | Impact |
|---|---|---|---|
| B1 | ~~Which E80 SKUs?~~ **RESOLVED 2026-10-22:** dual-band confirmed (2.4 GHz HF path proven by the 2026-08-22 sweep). Remaining: record `-400` vs `-900` per board (V0.2) — only affects the 915 *option*. | operator | 915 option only |
| B2 | **Hang-time decision** — 4 days vs one scheduled hour | organiser | Helium volume, tether spec, entire logistics timeline |
| B3 | **Helium supply** — is balloon-grade He available and legal to bring on site? | organiser | Demo viability |
| B4 | **FIPS serial transport revision** — pin & vendor the v0.3.0-dev-era tree | engineering | Ground chain |
| B5 | ~~N=5 transport topology~~ **RESOLVED 2026-10-22 (operator): scope is a 2-node bent pipe.** The point-to-point serial limit is irrelevant at N=2. The 5-node analysis remains in `reports/ARCH-5NODE-BENT-PIPE-2026-11.md` as future work. | — | closed |
| B6 | Venue RF survey (2.4 GHz occupancy, 915 noise floor) | engineering | D2 confirmation |

---

## 6. Top risks, ranked

1. **The bridge has no single owner of the radio state machine.** One task fires
   raw SPI TX while another drives `standby()`/`startReceive()`; only the SPI
   *bus* is mutexed, not the radio *state machine*. Most likely cause of the
   documented 3–5 min lockup, and it must be fixed before TDMA is deterministic.
2. **Watchdog durability over 4 days** — never proven beyond minutes, and the
   trigger has an inverted incentive: MMP heartbeats every 10 s mean more peers →
   more valid frames → **the watchdog never trips precisely when the radio is
   broken.**
3. **The serial bridge is 4× slower than the relay chain.** `serial_udp_bridge.py`
   at 115200 baud = 11.5 kB/s = 122 ms per 1404 B datagram. **≥921600 baud is a
   prerequisite.**
4. **The balloon may add nothing.** Decide its purpose (obstruction bypass vs
   demonstration) before rigging, or it is an expensive way to halve throughput.
5. **Procurement lead time.** The `-900MBL-02` is realistically an
   AliExpress/CDEBYTE-direct item with a 2–3 week lead time to the US.
6. **Regulatory hygiene.** FLRC-260 non-compliant at 915; 2745 MHz (3rd harmonic
   of 915) and 4900 MHz (2nd of 2450) both land in 15.205(a) restricted bands
   with an **undocumented E80 output filter**. Measure, do not assume.

---

## 7. What we deliberately are NOT doing

- No PCB fabrication (D10)
- No cross-band relay (D3)
- No 433 MHz (D4)
- No FIPS on the balloon (D1)
- No protocol changes — the bridge moves opaque bytes
- No frequency hopping implementation (we qualify as DTS instead)
