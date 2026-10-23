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

| Item | Price | Source | Ships to Texas |
|---|---|---|---|
| **`E80-900MBL-02`** eval board (STM32F103 + LR2021) | **$18.56** | EBYTE, China | ⚠️ **14–37 working days → arrives 12 Nov–17 Dec, MISSES the event** |
| `E80-900M2212S(LR2021)` bare module | **$9.48** | EBYTE | same |
| `E80-900M2213S` + 915 & 2.4 G antennas bundle | **$8.25** | EBYTE | same |
| ESP32-C3 boards, LR2021 modules, E28-2G4M27S | **$0** — already owned | inventory | n/a (in Germany) |

> 🔴 **The one hard constraint:** EBYTE ships from China with 7 working days
> processing + 7–30 working days transit. **The boards must come from the existing
> German inventory, or be ordered express and accepted at ~10–14 days.**

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
