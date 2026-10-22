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
| D5 | **Scheduling is ground-derived from absolute UTC; the balloon only follows** | A fixed UTC-derived slot table is a *constant*, not a decision — so the relay stays ADR-014 transparent while collisions are prevented. 50 ms frame / 8 slots / balloon relays slot 6. |
| D6 | **Show a mesh, not a star** | 5 ground FIPS nodes with *mixed* links: some direct LOS, some via the balloon. Demonstrates FIPS routing preferring/avoiding the balloon hop. No new medium-access work. |
| D7 | **Fly the relay only where the ground path is obstructed** | At 200 m the direct path already has 51.8 dB margin; the relay returns +5.2 dB and halves throughput. Only worth it where the 800 m path is blocked by ≥6 m (14–20 dB of recovered knife-edge loss). |
| D8 | **Mylar/foil balloons, not latex** | Latex loses helium in ~12–24 h; a 4-day event means daily re-inflation. Foil holds for weeks. |
| D9 | **≤150 ft (45.7 m) AGL by default; 300 ft if paperwork allows** | 150 ft is the easy 14 CFR 101 Subpart B envelope. **300 ft costs only 0.16 dB of FSPL but more than doubles near-end clearance** (x_min 11.9 m vs 30.4 m) — pursue it for *geometry*, not power. |
| D10 | **Do NOT fabricate the v10 hub PCB** | JLCPCB 2-layer + assembly is ~2 weeks — lands on the event with zero margin. Existing inventory (20× ESP32-C3 Mini V1, 4× NiceRF LR2021, 3× E28-2G4M27S) builds a working rig today. |
| D11 | **Buy nothing ourselves; source and link only** | Operator instruction. Deliverable is a shopping list with verified US links. |

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

Deliverable: a pass/fail matrix over {260, 650, 1300 kbps} × {10, 50, 100 m}
with the 915 MHz band, plus the measured FLRC-650 6 dB bandwidth.

### Phase 2 — Firmware C1–C6 (`ARCH-5NODE` §4)

Ordered by risk; **C1 first** — until one task owns the radio, nothing else can
be made deterministic.

| Item | Effort | Required? |
|---|---|---|
| C1 single radio owner + TX queue | ~1.5 d | **YES** — root cause of the 3–5 min lockup |
| C2 TDMA slot gate; delete jitter | ~1 d | **YES** (needs C3) |
| C3 UTC time base | ~1 d + GPS wiring | **YES for TDMA** |
| C4 4-day-survivable watchdog | ~0.5 d | **YES** |
| C5 variable packet length | ~2 h | **YES** — ~4–5× airtime recovery |
| C6 unattended safety (blink loops, counters, RTC persistence) | ~0.5 d | **YES for 4 days** |
| C7 addressing / ingress suppression | ~3–5 d | no (only for cross-band) |
| C8 band switching | ~2–3 d | no (only for cross-band) |
| C9 queue depth | folded into C1 | — |

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
| B1 | **Which E80 SKUs do we actually have?** The Amazon link supplied was `E80-400MBL-02` (400 MHz) — a different, useless variant for 915. | operator | Band plan |
| B2 | **Hang-time decision** — 4 days vs one scheduled hour | organiser | Helium volume, tether spec, entire logistics timeline |
| B3 | **Helium supply** — is balloon-grade He available and legal to bring on site? | organiser | Demo viability |
| B4 | **FIPS serial transport revision** — pin & vendor the v0.3.0-dev-era tree | engineering | Ground chain |
| B5 | **N=5 is a transport-topology problem, not a peer problem.** Serial is point-to-point: one bridge = one peer. 5 nodes need either 5 bridges per node or FIPS transit routing. **Resolve before promising 5 laptops.** | engineering | D6 scope |
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
