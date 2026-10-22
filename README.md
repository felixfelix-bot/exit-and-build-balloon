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
laptop A ── fips ── PTY ── serial_udp_bridge.py ── USB CDC ── ESP32-C3 ── LR2021 ──┐
                                                                                 │ 915 MHz
                                                                       BALLOON relay
                                                                                 │ 915 MHz
laptop B ── fips ── PTY ── serial_udp_bridge.py ── USB CDC ── ESP32-C3 ── LR2021 ──┘
```

## Status: PLANNING — feasibility verification in progress

Nothing has been procured, fabricated or flashed. Read `docs/PLAN-bent-pipe-2026-11.md`
first; it carries the decision record and the open blockers.

## Documents

| File | What it is |
|---|---|
| `docs/PLAN-bent-pipe-2026-11.md` | **Master plan** — decisions, phases, worker-sized tasks, open blockers |
| `docs/HARMONICS-AND-BAND-PLAN.md` | Band choice: why not 433, harmonic/intermod analysis, why symmetric 915 |
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
