# Exit & Build 6 — Tethered Balloon Mesh-Relay Demo

**Event:** Exit & Build 6 "Freedom in Action" · **5–8 November 2026**
**Site:** Mollie Engelhart's Sovereignty Ranch, Bandera, Texas (~200 acres, ≈900 m × 900 m, site elevation 471.6 m / 1547 ft)
**Organiser contact:** Live Free Academy (John Bush et al.)

## What this is

A cheap, tethered helium balloon that carries a **transparent radio relay** so that
**FIPS** mesh traffic can cross the venue. Secondary purpose: the same rig is a
radio-characterisation bench (PER / RSSI / SNR vs distance and altitude) that
feeds the balloon-fresh range-test programme.

The balloon is a **dumb pipe**. It holds no key, inspects no payload byte, and
makes no routing decision. FIPS runs on laptops on the ground; the balloon is a
PHY repeater between them. This is the ADR-014 bent-pipe contract.

```
 GROUND A                                                        GROUND B
 laptop A ─ fips ─ PTY ─ serial_udp_bridge ─ USB
                                              │
                                 ┌────────────┴───────────┐
                                 │  E80 #1  bridge-ground │  STM32F103 + on-board
                                 └────────────┬───────────┘  CH340 + LR2021
                                              │ 915 MHz FLRC-1300, half-duplex
                                 ┌────────────┴───────────┐
                                 │  E80 #2  bridge-relay  │ ← mast or balloon
                                 └────────────┬───────────┘   20–45 m up
                                              │ 915 MHz
                                 ┌────────────┴───────────┐
                                 │  E80 #3  bridge-ground │
                                 └────────────┬───────────┘
                                              │ USB
 laptop B ─ fips ─ PTY ─ serial_udp_bridge ───┘
```

> **The relay is the E80 board itself** — its STM32F103 is the MCU, its on-board
> CH340 is the USB bridge, and its LR2021 is the radio. **No ESP32-C3 is required.**
> All three boards run **one firmware image** in different modes. See "One rig,
> not two" below.

## Shopping overview — pick a path

The **radio payload is the same in all three paths**. Only the thing that lifts it
(or does not) changes. Prices are indicative; **UNVERIFIED** means no live price
was read.

### Path comparison

| | **MAST** (recommended) | **BALLOON** (latex sphere) | **HELIKITE** |
|---|---|---|---|
| **Airspace permission** | **none required** | landowner permission | landowner permission |
| **Wind tolerance** | **structural, ~25 kn** | ~5.7 kn at 45° blow-over | **holds into wind** |
| **Effective height** | exact, as built | blows down: **12 ft at 8 kn** | holds |
| **Lead time** | **US domestic, days** | **US retail, days** | **UK, 1–3 wk + customs → likely MISSES 5 Nov** |
| **Indicative cost** | **~$30–120** | **~$250–450** | **UNVERIFIED** (no price published) |
| **Helium needed** | none | **~30 ft³** balloon-grade | yes, similar |
| **Fails if** | pole unavailable | wind >6 kn | ships late |
| **Regulatory surface** | **none below 200 ft** | 101 Subpart B *if* >6 ft / >115 ft³ | same |

> **Only the mast removes the permission question entirely** — 14 CFR Part 101
> governs *balloons*, not structures. See `docs/ASSET-STRATEGY.md`.

### Common to all paths — the radio

| Item | Qty | Price | Source | Ships to Texas |
|---|---|---|---|---|
| **`E80-900MBL-02`** eval board (STM32F103 + LR2021) | **3** — 2 ground + 1 relay | **$18.56 ea** | EBYTE, China | ⚠️ **14–37 working days → arrives 12 Nov–17 Dec, MISSES the event** |
| `E80-900M2212S(LR2021)` bare module | 1–2 spare | **$9.48** | EBYTE | same |
| `E80-900M2213S` + 915 & 2.4 G antennas bundle | 1 spare | **$8.25** | EBYTE | same |
| ESP32-C3 boards, LR2021 modules, E28-2G4M27S | **$0** — already owned | — | inventory | n/a (in Germany), **not needed for the relay** |

> 🔴 **The one hard constraint:** EBYTE ships from China with 7 working days
> processing + 7–30 working days transit. **The boards must come from the existing
> German inventory, or be ordered express and accepted at ~10–14 days.**
>
> 🔴 **Count check — the number changed, and it is not 2.** A 2-node bent pipe is
> **three radios**, not two: one at each ground node *plus one in the air*. The
> German bench inventory is **2 × E80-900MBL-02**. So the event rig needs **one
> more board than we own**, or the bench rig comes apart to fly. Decide this
> together with the Germany→Texas shipping question (`docs/ASSET-STRATEGY.md` §1),
> not separately — see open item **B12** in the plan.

### Path A — MAST (headline ~$30–120)

| Item | Qty | Indicative | Where | Lead time |
|---|---|---|---|---|
| Fibreglass telescoping pole, 27–31 ft | 1–2 | **~$30 ea** ⚠️ *third-party "~$1/ft" quote, not a vendor price* | **Jackite Inc (US)** https://www.jackite.com/antenna | US domestic, days |
| Guy line 3 mm Dyneema | 100 ft | ~$25 | arborist / marine | days |
| Anchors (ground screws / sandbags / hitch shackle) | 1 set | ~$60 | Amazon US | days |
| **Anemometer** | 1 | ~$30 | Amazon US | days |
| Helium | — | **$0** | — | — |

Full spec, rigging pattern and the verified vendor survey: **`docs/MAST-SPEC.md`**.
⚠️ Jackite model/price not yet confirmed — see open items M1–M5.

### Path B — BALLOON, latex sphere (headline ~$250–450)

| Item | Qty | Indicative | Where | Lead time |
|---|---|---|---|---|
| 36–48 in round **latex** balloon | 4–6 | ~$10–30 | US party retail | days |
| **HI-FLOAT** barrier coat | 1 kit | ~$10–20 | same | days |
| 18 in foil spares | 4 | ~$5–10 | same | days |
| **Helium, balloon-grade ≥99.99%**, ~30 ft³ | 1 cylinder | **$100–250** incl. deposit/hazmat | Airgas SA **(210) 337-7255**; nexAir; Linde; Matheson | days, will-call |
| *(alt: Balloon Time 14.9 ft³)* | — | *$75.99 = $5.10/ft³, ~15× base price — one-hour demo only* | Tractor Supply Bandera | days |
| Tether 1.5 mm Dyneema 200 ft + 1.0 mm 300 ft | 2 | ~$45–65 | arborist / marine | days |
| Swivels, carabiners, streamers | 1 set | ~$20 | marine | days |
| Anchors + anemometer | 1 set | ~$90 | Amazon US | days |

⚠️ Consumer party tanks are **≥80% helium only** (a 20% lift penalty) — buy
industrial balloon-grade. Site lift is **28 g/ft³** at 471 m, not sea-level.

### Path C — HELIKITE (cost UNVERIFIED)

| Item | Qty | Indicative | Where | Lead time |
|---|---|---|---|---|
| Helikite, sub-200 g payload, 150 ft | 1 | **UNVERIFIED** | **Allsopp Helikites (UK)** https://www.helikites.com/shop — `info@helikites.com`, +44 1425 654967 | ⚠️ **1–3 weeks + customs** |
| US reseller | — | — | **NONE FOUND** (searched 2026-10-23) | — |
| Tether, anchors, anemometer | — | ~$150 | as Path B | days |
| Helium | — | ~$100–250 | as Path B | days |

**Gate: only order if the quote shows a US warehouse or ≤5-day transit.**
Otherwise it cannot make 5 Nov.

> **No purchase has been made.** This repo sources and links only.

---

## Why the ESP32-C3 was in the plan — and why it should not be

**Corrected 2026-10-23 (operator challenge).** The architecture diagrams previously
showed `ESP32-C3 ── LR2021` between the laptop and the radio. That was **wrong as
a design choice**, and the reason is instructive: it was copied from an older
bridge (`mesh-stack/flrc-bench-espidf/main/fips_bridge.cpp`) that exists only
because *that* rig had a bare LR2021 module with no MCU attached. The E80 board
**has an MCU attached**.

### What the E80 already provides

| Need | E80 board | ESP32-C3 would add |
|---|---|---|
| MCU | **STM32F103C8T6, 72 MHz** | redundant |
| USB↔serial bridge | **on-board CH340** | redundant |
| Radio | **LR2021 on SPI** | redundant |
| Dual-band antennas | **two SMA-K jacks** | redundant |
| Debug | SWD header | — |
| GPIO / LEDs / keys | 3 LEDs, 2 keys, headers | — |

**Every part of the ESP32-C3's job is already on the E80.** Using it would mean
wiring an external MCU to a board that already has one — more parts, more points
of failure, more mass, and a second toolchain (ESP-IDF) for no capability.

### What has to change in the firmware

The repo's working bridge (`fips_bridge.cpp`) is **ESP-IDF code for an ESP32-C3**.
It cannot be dropped onto an STM32F103. But the E80 bench firmware already
provides the hard half:

- ✅ **LR2021 driver** — full Semtech LR20xx v1.3.1 linked (LoRa, FSK, **FLRC**,
  LR-FHSS, 802.15.4, …). No new radio work.
- ✅ **UART command console** at 115200/2 M baud, and a **transparent
  serial→radio mode**: *any unrecognised UART byte is transmitted over the air as
  received*.
- ❌ **No FLRC bridge path** — the transparent mode is hardcoded to LoRa and a
  fixed payload length. FLRC is compiled in and switchable via `MOD flrc <br>`,
  but the transparent pipe does not use it.
- ❌ **No stream framing** — no SLIP/COBS, no FIPS-magic detection, no variable
  length, no relay queue.
- ❌ **No watchdog / unattended hardening.**

So the work is **"add a bridge mode to the existing STM32 bench firmware"**, not
"port an ESP32 application". It is smaller than the original C1–C6 task list,
because the radio layer is solved.

### Consequences that change the plan

1. **The ESP32-C3 leaves the BOM.** Existing stock is unaffected (owned already),
   but it is no longer a required part and must not appear in the critical path.
2. **The bridge becomes a firmware task on a board we already have** — and the
   board is already the thing under test, so **there is one rig, not two**. This
   has a consequence beyond tidiness: see "One rig, not two" below.
3. **The E80's known blockers become the bridge's blockers** — above all the
   **flash path** (SWD-only, currently failing). If the board cannot be reflashed,
   it cannot become the bridge either. `docs/E80-VERIFICATION-CHECKLIST.md` V1
   therefore gates *more* than before, not less.
4. **Board count is 3, not 2.** A 2-node bent pipe is three radios: two ground
   bridges plus the one in the air. Inventory is 2. See B12 in the plan.
5. **New open item:** whether the STM32 bridge can hold a FIPS session at the
   required throughput. **72 MHz with a UART↔SPI relay is plausible but unproven**
   — it must be measured, not assumed. The ESP32-C3 at 160 MHz was never measured
   either. This is now an explicit bench task (see checklist V8).

> **Honest framing: this is a simplification, not a free win.** It removes a part
> and a toolchain, and it concentrates the risk on one board that is currently
> unflashable. The flash path was already the first gate; it is now the only gate.

### One rig, not two — and why that is a measurement property, not a slogan

Before this change there were two different things in the project:

- a **bench rig** that measures the link (PER / RSSI / SNR vs distance), and
- a **relay** built from a different board (the ESP32-C3) that flies.

The problem with two rigs is that they can disagree silently. A bug in the relay
— a dropped fragment, a stalled state machine, a bad flush — would show up as
*"the link performs badly"* in the measurements, while the bench hardware
underneath was innocent. Worse: the bench could report a clean link for a relay
that never actually passed the traffic, because the bench never ran that code.

**With the change, the board that measures the link is the board that relays it.**

- The measurement firmware and the relay firmware are **one image in two modes**,
  on the same silicon, same SPI bus, same radio, same clock.
- A bridge bug cannot hide behind a separate box — it appears in the very
  PER/RSSI/SNR numbers being logged, because that path *is* the path.
- The throughput answer (V8) and the range answer come from the same rig, so a
  bad number has exactly one candidate explanation to eliminate instead of two.
- It also kills a class of false confidence: "the bench passed" and "the relay
  works" become the same statement, which is either true or obviously false.

**What it does not buy:** correctness. A single rig can be wrong in one way and
report it consistently for four days. It removes *disagreement between rigs*, not
*miscalibration* — the A/B obstruction test and the independent reference (a
second receiver, or FIPS' own path-MTU behaviour) are still what keep the numbers
honest.

**Cost of the change:** the relay and the measurement now contend for the same
board, so you cannot measure the link while relaying on one board — you need a
third E80 for that (B10). And a failed flash now fails both jobs at once.

---

## Status: PLANNING — feasibility verification in progress

Nothing has been procured, fabricated or flashed. Read `docs/PLAN-bent-pipe-2026-11.md`
first; it carries the decision record and the open blockers.

## Documents

| File | What it is |
|---|---|
| `docs/PLAN-bent-pipe-2026-11.md` | **Master plan** — decisions, phases, worker-sized tasks, open blockers |
| `docs/HARMONICS-AND-BAND-PLAN.md` | Band choice: why not 433, harmonic/intermod analysis, why symmetric 915 |
| `docs/ASSET-STRATEGY.md` | **Lifting-asset decision** — mast primary (permission-free), sphere second, Helikite only on a fast US quote |
| `docs/MAST-SPEC.md` | **Mast spec + verified vendor survey** — the primary asset; why fibreglass, required heights, rigging, and the measurement consequence |
| `docs/OUTBOUND-DRAFTS.md` | **DRAFTS, NOT SENT** — Helikite quote request + organiser airspace message, staged for approval |
| `docs/E80-VERIFICATION-CHECKLIST.md` | Board bring-up checklist — run this FIRST, it gates everything |
| `docs/SITE-RULES-AND-FAA.md` | Bandera site facts + 14 CFR 101 Subpart B moored-balloon rules |
| `shopping-list.md` | US-sourced parts with vendor links (radio, balloons, helium, tether) |
| `reports/RF-TRADE-STUDY-exit-and-build-2026-11.md` | RF link budget, 47 CFR 15.247, geometry, recommendation |
| `reports/ARCH-5NODE-BENT-PIPE-2026-11.md` | 5-node architecture, FIPS dedup analysis, TDMA spec, firmware gaps |
| `reports/BALLOON-LOGISTICS-TETHER-2026-11.md` | Balloon/helium/tether logistics |
| `reports/ELECTRONICS-SOURCING-US-2026-11.md` | US sourcing channels for the radio hardware |

## The three findings that shape everything

1. **The balloon only earns its place over an obstruction.** At 200 m separation the
   direct ground path already has 51.8 dB of margin; the relay returns +5.2 dB and
   *halves* throughput. Fly it where the 800 m ground path is blocked by ≥6 m of
   terrain/cedar — that is the one regime where 14–20 dB of recovered knife-edge
   loss beats the relay's cost.
2. **Band: symmetric 915 MHz, FLRC-1300.** Not cross-band, not 433. 915 gives
   18.55 dB more budget than 2.4 GHz (10 dB PA + 8.55 dB FSPL) and is far less
   contested at a 2,000-person event. FLRC-1300 because FLRC-260's 300 kHz width
   **fails the 47 CFR 15.247(a)(2) 6 dB bandwidth floor** for a fixed-channel DTS.
3. **The scheduling must live on the ground, and the balloon only follows.** A
   fixed UTC-derived slot table is a *constant*, not a decision — so the relay
   stays transparent while collisions are still prevented. 50 ms frame, 8 slots,
   balloon relays slot 6.

## Single largest risk

`fips_bridge.cpp` has **no single owner of the radio state machine**: one task
fires raw SPI TX while another drives `standby()`/`startReceive()`. Only the SPI
*bus* is mutexed, not the radio *state machine*. This is the most likely cause of
the documented 3–5 minute lockup, and it must be fixed before TDMA can be made
deterministic at all. See `ARCH-5NODE-BENT-PIPE-2026-11.md` §4 C1.

## Related repositories

- `felixfelix-bot/balloon-fresh` — firmware, bench tooling, ADRs (source of the bridge)
- `felixfelix-bot/balloon-e80bench` — E80 STM32 range-bench toolchain
- `Amperstrand/microfips` — FIPS leaf node implementations (ESP32-C3, ESP32-S3, STM32)
- `jmcorgan/fips` — upstream FIPS
