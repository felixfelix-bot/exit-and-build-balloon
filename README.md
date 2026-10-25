# Exit & Build 6 — Relay Test at Sovereignty Ranch, Bandera TX

**Event:** Exit & Build 6 "Freedom in Action" · **5–8 November 2026**
**Site:** Mollie Engelhart's Sovereignty Ranch, Bandera, Texas (~900 m × 900 m, site elevation 471.6 m / 1547 ft)
**Organiser contact:** Live Free Academy (John Bush et al.)

---

> ## 📌 CURRENT RECOMMENDATION (2026-10-25) — read this first
>
> **Postpone the balloon flight. Run the bent-pipe LR2021 relay test instead.**
>
> These are two different things, and this plan conflated them for too long:
>
> - **The relay test** is what produces knowledge. It needs three radios, a mast
>   and an anemometer. All of it exists or is **in US stock, days away**.
> - **The balloon** is a *lifting asset*. It is currently the **least proven part
>   of the system** — the flight board that would fly it has **zero copper routed**
>   and cannot reach the event.
>
> **Full reasoning:** [`docs/RECOMMENDATION-postpone-and-minimum.md`](docs/RECOMMENDATION-postpone-and-minimum.md).
>
> **Short version:** the flight board (v10, in `balloon-fresh`) is at *"placement
> approved, routing not started."* Its last routing attempt was **rejected**, its
> reroute tool is committed as **"NOT YET PROVEN to improve the result"**, three
> pin blockers are open — one of which blocks two functions that are both in the
> design — and `ADR-031` makes the fab order a designed step that has not
> happened. Against ~10 days to the event, that is not a schedule; it is a hope.
>
> **What is NOT postponed:** the radio test. That is the deliverable.

---

## Shopping list — order these

Side-by-side, both columns, for every line: **cheapest** and **arrives on time**.
Full pricing, alternatives and reasoning: [`docs/PURCHASE-PLAN.md`](docs/PURCHASE-PLAN.md).

| Item | Qty | 💰 **CHEAPEST** (link + price) | 🚚 **ARRIVES ON TIME** (link + price) | Delta |
|---|---|---|---|---|
| **`E80-900MBL-02`** eval board — STM32F103C8T6 + LR2021 | **3** | **AliExpress** ~**$13–14 ea** · ~**$40 / 3**<br>https://www.aliexpress.com/item/1005012863308600.html | **RobotShop / Botstore** **$18.80 ea** · **$56.40 / 3**<br>https://www.robotshop.com/products/botstore-e80-900mbl-02-dual-band-lora-module-development-board | **+$16.40** to arrive |
| **ESP32-C3 dev board** — second SWD flash probe | **2** | **Amazon** **$9.99 / 2** (AITRIP)<br>https://www.amazon.com/s?k=ESP32-C3+SuperMini | **Amazon** — same vendor arrives in 2–4 d<br>*alt:* **Adafruit** ~$10 ea https://www.adafruit.com/category/968 · **SparkFun** https://www.sparkfun.com/categories/999 | **$0** — same source |
| **Silicone wire + Dupont jumpers/headers** — SWD harness | 1 set | **Amazon** ~**$8–10**<br>https://www.amazon.com/s?k=dupont+jumper+wires+40pin | **Amazon** — same, 2–4 d<br>*alt:* **Adafruit / SparkFun** ~$14 | **$0** — same source |
| **Fibreglass telescoping mast** — Jackite 28 ft | 1 | **Hamsource** **$62.84**<br>https://hamsource.com/product/28-jackite-pole-black/ | **Hamsource** — same, **in stock**, US domestic<br>*(the 31 ft is **out of stock** in all three colours)* | **$0** — same source |
| **Guy wire ring** — 3 × 5/16″ holes | 1 | **Hitched4fun** **$2.95**<br>https://www.hitched4fun.com/product/1-inch-guy-wire-ring-for-31-ft-jackite-fiberglass-telescoping-pole/ | **Hitched4fun** — same, US | **$0** — same source |
| **Antenna Mast Guying Kit** — cord + tensioners + stakes | 1 | **Hitched4fun** **$45.95** (sale, list $68.52)<br>https://www.hitched4fun.com/product/antenna-mast-guying-kit-for-jackite-31-ft-ham-ready/ | **Hitched4fun** — same, US | **$0** — same source |

**Totals**

| | 💰 Cheapest | 🚚 On time |
|---|---|---|
| Basket | **≈ $160–175** | **≈ $188–202** |
| E80 boards alone | $40 | $56.40 |
| **Would it make 5 Nov?** | ❌ **no** — E80 ships from China, 7–15 d + customs | ✅ **yes** |

**The only line where the two columns differ is the E80 board.** Everything else
is a single US vendor that is simultaneously cheapest and fast.

### Read this before choosing the cheaper column

The E80 is the **one** line where cheapest ≠ arrives, and the gap is **$16.40**.

- **What the $16.40 buys:** 10 days to the event, and the vendor's own policy
  pages warn of a **10–20 % chance of a further 7–15 day customs delay** on
  US-bound *electronics* — this exact category. A customs hold doesn't cost you
  $16, it costs you the experiment.
- **RobotShop was verified in stock**, US-fulfilled, with 24 h order handling.
- **AliExpress ship-from and delivery date were not readable** (bot-wall stub, no
  price or shipping fields), so its 7–15 day figure is the vendor's *general*
  policy, not a quote for this item.

> **Both links are live and verified** — the AliExpress listing returns HTTP 200
> and genuinely carries all four E80 variants including the **MBL-02**.
>
> ⚠️ **Do not order the `-01` variant.** `E80-900MBL-01` is **LR1121**, not
> LR2021 — different chip, and its driver is not what the bench firmware links.
> The same AliExpress page lists several variants; **pick `MBL-02`.**

> ### Cheapest-that-arrives, in one paragraph
>
> **RobotShop's $18.80 is both the cheapest *and* the only E80 channel that makes
> 5 Nov** — EBYTE direct is $18.56 but 14–37 working days, landing 12 Nov – 17 Dec.
> Seeed's LR2021 kit is US-stock at $99 — 5.3× the price, and it is **not an
> STM32F103**, so it does not answer the question the boards are bought for.
>
> **Amazon is cheaper on the commodities** — ESP32-C3 boards at $9.99/2 versus ~$20
> at Adafruit; wire ~$8–10 versus ~$14. Amazon prices are from search snippets,
> **not** pages I could verify (every fetch hit a bot-wall) — check before ordering.
>
> **Two savings worth taking:** the **28 ft** mast ($62.84) over the 31 ft
> ($112.95) saves **$50**; the guying kit's **sale** price ($45.95, list $68.52)
> saves **$23**. Together **$73 for the same experiment.**
>
> **Worth checking:** the master inventory lists **20× ESP32-C3 Mini V1** and
> **2× RP2040-Zero already owned** (recorded as in Germany). If reachable in time,
> **delete lines 2–3 — ~$24–34 for nothing.**
>
> **Not ESP32-S3.** The throughput numbers I first quoted here (ADR-026's
> 1377/838 kbps) were **stale** — now replaced by the repo's **real 2.4 GHz
> sustained sweep**: **1484.9 kbps at BR2600, 57.1 % of air rate, 0.00 % PER over
> 21,923 packets**, and the limiter is the **host SPI/TX path (~1487 kbps flat
> across every bitrate)**, not the coding rate or payload size. Full derivation:
> [`docs/THROUGHPUT-SETTLED-by-measurement.md`](docs/THROUGHPUT-SETTLED-by-measurement.md).
>
> **Why the S3 conclusion is unchanged:** it never rested on those numbers. It
> rests on: an ESP32 **does not answer V8**, because V8 asks about the
> **STM32F103**. Correcting the throughput figures changes the *performance
> context*, not the *subject of the test*. If a faster radio path is wanted, the
> lever the measurement points at is **fixing the TX SPI bottleneck** — which is
> what the repo's throughput-fix plan and P4.1 already target — and we own two
> RP2040s to do it on.
>
> **The bigger finding, stated plainly:** we already own **4× NiceRF LR2021
> modules** and two RP2040+LR2021 rigs, so the bent pipe could be proven **for $0**
> on the same radio and band. It would not answer **V8** — which is precisely why
> the E80 is worth $56.40. That $0 path is the **fallback if the order slips**, and
> it is written up in the sourcing study.
>
> **Two long-lead items: the E80 boards and the mast.** **Order the E80 first** —
> it is the one that can slip. Everything else is domestic, cheap, and can wait.
>
> **Deliberately not on the list:** the anemometer (operator instruction), any PCB
> fabrication, helium, envelopes, and a Helikite.

### Why #2 — ESP32-C3 boards — is on the list

**Because you may need a second, known-good SWD probe.** Not for the relay.

The E80 flash path is **the only gate left** (checklist V1). Its diagnosed state
is *"probe handshake, interface init and clock control all succeed; `cannot read
IDR` / `AP #0x0` at every speed tried."* The open candidates, in order:

1. **SWCLK/SWDIO swapped** on the 3-wire harness — a swap is *invisible* to
   openocd diagnostics; it looks identical to an unseated harness.
2. A solder / continuity fault on a data line.
3. Drive strength on a long harness.

An RP2040-Pico probe is already in inventory and enumerates cleanly. **A second
probe of a different kind is how you turn "the probe is broken" from a hypothesis
into a measurement** — if the ESP32-C3 probe also fails to read the chip, the
fault is in the board or the harness, not the probe. That is the difference
between debugging and guessing, and it is why **two** are on the list, not one.

**An ESP32-C3 can act as a CMSIS-DAP SWD probe.** Two working implementations:
[`bkuschak/cmsis_dap_tcp_esp32`](https://github.com/bkuschak/cmsis_dap_tcp_esp32)
— tested against an **STM32F103 Blue Pill, the same MCU family as the E80** — and
[`windowsair/wireless-esp8266-dap`](https://github.com/windowsair/wireless-esp8266-dap).
The inventory already holds **20× ESP32-C3 Mini V1** in Germany, so this is a
*second known-good probe*, not an exotic new toolchain.

> ⚠️ **Honest caveat:** this requires flashing the boards with probe firmware
> (ESP-IDF v4.4.2 for the wireless-dap project). The cost is **time, not money**.
> The zero-cost fallback is to **swap SWCLK and SWDIO on a breadboarded harness**
> — that is checklist **V1a.3** and it must be tried **first**, before any probe
> firmware is built.

---

## The experiment, in one picture

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

The relay is the **E80 board itself** — its STM32F103 is the MCU, its on-board
CH340 is the USB bridge, its LR2021 is the radio. **No ESP32-C3 is required for
the relay.** All three boards run **one firmware image** in three modes
(`bench` / `ground` / `relay`).

**Requirement: 3 boards.** A 2-node bent pipe is two ground bridges **plus** the
one in the air. With only two you cannot measure the link *while* it relays.

### Why the relay goes up a mast, not under a balloon

At Exit & Build the relay goes **up a mast**. That is not a downgrade — it is the
entire regulatory story:

| | Balloon | **Mast** |
|---|---|---|
| Airspace permission | landowner permission required | **none** — a mast is a *structure*, not a balloon; 14 CFR Part 101 does not apply below 200 ft |
| Notice / Form 7460-1 | needed above 200 ft | **not needed** |
| Wind rule | ~5.7 kn blow-over on a sphere | **structural, ~25 kn, guyed** |
| Effective height | blows down: 12 ft at 8 kn | **exactly as built** |
| Helium | ~30 ft³ balloon-grade | **none** |

### "One rig, not two" — a measurement property, not a slogan

Before this change there were two things in the project: a **bench rig** that
measured the link, and a **relay** built from a different board that flew. Two
rigs can disagree silently — a bug in the relay would appear as *"the link
performs badly"* while the bench hardware underneath was innocent.

**Now the board that measures the link is the board that relays it.** One image,
same silicon, same SPI bus, same radio, same clock. A bridge bug appears in the
very PER/RSSI/SNR numbers being logged, because that path *is* the path.

**What it does not buy:** correctness. It removes *disagreement between rigs*, not
*miscalibration* — the A/B obstruction test and an independent observer still
carry the honesty. And with the relay and a ground role contending for one board,
you must buy the third to measure *while* relaying.

---

## What Exit & Build delivers

**Not** "balloon over obstruction" — that claim needs the balloon, a written
landowner permission, a 4-day helium duty cycle and a wind-governed schedule.

**Instead: "transparent LR2021 bent-pipe relay at a known, stated height."** A
smaller, fully-claimable result, honest about what was built:

1. **V8 answered** — can the 72 MHz STM32 relay UART↔SPI at 2 Mbaud with
   FLRC-1300 active? **Currently unknown**, and the whole architecture rests on
   it. Answered by *measuring*, on hardware already owned — not by a fab order.
2. **The bent pipe works** — laptop A → E80 → air → E80 → air → E80 → laptop B,
   FIPS above it, opaque frames through it.
3. **The A/B relay delta** — same link, with and without the relay in circuit, at
   a measured height. This is what makes the mast worth having.
4. **A rig that is one rig** — the numbers cannot disagree with each other.

**The balloon becomes the *later* event's headline** — with v10 built, rehearsal
behind it, and the relay already proven, so a failure on the day is a *balloon*
failure: one clean cause, instead of an untested board and an untested relay
failing together.

---

## Why the flight board cannot make 5 November

Measured from `balloon-fresh`, branch `feat/foam-wing-3d` — **not assumed**:

| Evidence | State |
|---|---|
| `hub_board_v10.kicad_pcb` | **0 segments, 0 vias. Zero copper.** |
| `docs/fab/v10/GATE-LOG.md` | Last routing attempt **REJECTED** — operator caught by eye: a `U_C.9` short at 0.000 mm, two dead-end stubs, copper through the F33 body |
| Binding directive | **A\* with vias is the only permitted routing method**; straight/L routing banned; no copper ships unless 4 gates pass |
| Reroute tool (commit `a7ac6848`) | Committed as **"NOT YET PROVEN to improve the result"** |
| `connectivity/OPEN-ITEMS.md` | **3 open pin blockers** — GPIO0 pad number unverified; E28 PA/LNA enables unassigned; **the last ADC input is contested**, blocking two functions both in the design |
| ADR-129 note | **11 ERC errors** outstanding |
| ADR-031 §59 | The fab order is a *designed* step that has not happened |

**Chain to a flight-ready v10:** close 3 blockers → A\*-route 26 nets with an
unproven tool → DRC clean → JLCPCB (3–5 d + 5–10 d shipping, or 24–72 h quick-turn)
→ assemble → staged bring-up → *then* fly.

**Two contradictions that had never been put side by side:**

1. **D10 forbids fabricating the v10 hub** — so this repo was **never** on a path
   to having v10 boards at the event. D10 and *"wait for the flight boards"* are
   **mutually exclusive**.
2. **v10 does not retire the actual blocker.** v10 is ESP32-**S3** + E28, not an
   E80 — so it does not answer V8. **Waiting for it buys nothing on this axis.**

---

## Why the ESP32-C3 is *not* the relay (it is only ever a probe or a helper)

**Corrected 2026-10-23 (operator challenge).** Earlier diagrams showed
`ESP32-C3 ── LR2021` between the laptop and the radio. That was **wrong as a
design choice**: it was copied from an older bridge
(`mesh-stack/flrc-bench-espidf/main/fips_bridge.cpp`) that exists only because
*that* rig had a bare LR2021 module with no MCU attached. The E80 has an MCU.

| Need | E80 board | ESP32-C3 would add |
|---|---|---|
| MCU | **STM32F103C8T6, 72 MHz** | redundant |
| USB↔serial bridge | **on-board CH340** | redundant |
| Radio | **LR2021 on SPI** | redundant |
| Dual-band antennas | **two SMA-K jacks** | redundant |
| Debug | SWD header | — |

The E80 bench firmware already provides the hard half of the bridge: the full
Semtech LR20xx v1.3.1 driver (**FLRC included**), a UART console at 115200/2 Mbaud,
and a transparent serial→radio mode. What is **missing**: an FLRC bridge path (the
transparent mode is hardcoded to LoRa and a fixed payload length), stream framing
(no SLIP/COBS, no FIPS-magic detection, no relay queue), and watchdog / unattended
hardening.

So the work is **"add a bridge mode to the existing STM32 bench firmware"** — not
"port an ESP32 application". Smaller than the original C1–C6 list, because the
radio layer is solved.

> **Honest framing: a simplification, not a free win.** It removes a part and a
> toolchain, and it concentrates the risk on one board that is currently
> unflashable. The flash path was already the first gate; it is now the only gate.

---

## Status: PLANNING — feasibility verification in progress

Nothing has been procured, fabricated or flashed. **No purchase has been made.**
This repo sources and links only.

## Documents

| File | What it is |
|---|---|
| **`docs/RECOMMENDATION-postpone-and-minimum.md`** | **The postponement recommendation, argued in full** |
| **`docs/PURCHASE-PLAN.md`** | **Buy list by lead time, US vs China sourcing, mast SKU survey** |
| **`docs/SOURCING-CHEAPEST-ONTIME.md`** | **Every E80 channel priced and timed; cheapest on-time basket; the $0 fallback** |
| **`docs/S3-AND-AMAZON-PRICING.md`** | **Why ESP32-S3 is not the answer; is Amazon cheaper** |
| **`docs/THROUGHPUT-SETTLED-by-measurement.md`** | **✅ CLOSED — real 2.4 GHz sustained sweep: 1484.9 kbps at BR2600, 0.00 % PER, TX/SPI-limited** |
| **`docs/BALLOON-PATH-deferred.md`** | **Deferred balloon path — helium, envelopes, Helikite, wind data. Not needed for the event.** |
| `docs/PLAN-bent-pipe-2026-11.md` | Master plan — decisions, phases, worker tasks, blockers (**B12** = board count) |
| `docs/E80-VERIFICATION-CHECKLIST.md` | Board bring-up — **run FIRST, it gates everything**. V1 = flash, V8 = throughput |
| `docs/ASSET-STRATEGY.md` | Lifting-asset decision + the Germany→Texas inventory problem |
| `docs/MAST-SPEC.md` | Mast spec + verified vendor survey (the 28 ft SKU is now priced) |
| `docs/RUNBOOK-event-operations.md` | On-site operations, gates, teardown |
| `docs/HARMONICS-AND-BAND-PLAN.md` | Why symmetric 915 MHz, why not 433, FLRC-1300 vs 260 |
| `docs/SITE-RULES-AND-FAA.md` | Bandera site facts + 14 CFR 101 Subpart B |
| `docs/OUTBOUND-DRAFTS.md` | **DRAFTS, NOT SENT** — staged for approval |
| `shopping-list.md` | Full shopping list (**§9.1** = purchase order by lead time) |
| `reports/RF-TRADE-STUDY-exit-and-build-2026-11.md` | Link budget, 47 CFR 15.247, geometry |
| `reports/ARCH-5NODE-BENT-PIPE-2026-11.md` | 5-node architecture, FIPS dedup analysis, TDMA spec, firmware gaps |

## The three findings that shape everything

1. **The relay only earns its place over an obstruction.** At 200 m separation the
   direct ground path already has 51.8 dB of margin; the relay returns +5.2 dB and
   *halves* throughput. Fly it where the 800 m ground path is blocked by ≥6 m of
   terrain/cedar — the one regime where 14–20 dB of recovered knife-edge loss beats
   the relay's cost.
2. **Band: symmetric 915 MHz, FLRC-1300.** Not cross-band, not 433. 915 gives
   18.55 dB more budget than 2.4 GHz (10 dB PA + 8.55 dB FSPL) and is far less
   contested at a 2,000-person event. FLRC-260's 300 kHz width **fails the
   47 CFR 15.247(a)(2) 6 dB bandwidth floor** for a fixed-channel DTS.
3. **Scheduling lives on the ground; the relay only follows.** A UTC-derived slot
   table is a *constant*, not a decision — so the relay stays ADR-014 transparent
   while collisions are prevented. 50 ms frame, 8 slots.

## Single largest risk

**V8 — the 72 MHz STM32 relay throughput is unproven.** It is the lowest clock in
the project, and it must relay UART↔SPI at 921600–2 Mbaud while FLRC-1300 is
active. Measure it **before** writing the bridge firmware, not after: it decides
whether that firmware is worth writing at all.

## Related repositories

- `felixfelix-bot/balloon-fresh` — firmware, bench tooling, ADRs, **the v10 flight board**
- `felixfelix-bot/balloon-e80bench` — E80 STM32 range-bench toolchain
- `Amperstrand/microfips` — FIPS leaf node implementations (ESP32-C3, ESP32-S3, STM32)
- `jmcorgan/fips` — upstream FIPS
