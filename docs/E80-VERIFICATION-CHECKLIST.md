# E80 board verification checklist — run this FIRST

**Why this exists:** every load-bearing assumption in the plan is currently
**unmeasured**. The E80 boards are the measurement instrument, so if they cannot
be flashed or driven, the plan is not feasible and we need to know that this week,
not in November.

**Status legend:** `[ ]` not tested · `[x]` pass · `[!]` FAIL/blocked · `[?]` inconclusive

Run items in order. Item **V1 gates everything else** — do not proceed past a
failed V1 without deciding the hardware question.

---

## V0 — Identify the boards (5 min, no power needed)

Read the silkscreen on each board and record the exact SKU.

- [ ] Board #1 SKU: `E80-______-02`
- [ ] Board #2 SKU: `E80-______-02`

**What the SKUs mean** (from `docs/e80-900mbl-02-eval/E80-900MBL-02_CAPABILITY_REPORT.md`
and `docs/2G4-LINK-BUDGET-ANALYSIS.md` in `balloon-fresh`):

| SKU | Module on board | LF band | 2.4 GHz? |
|---|---|---|---|
| `E80-400MBL-02` | `E80-400M2212S` (LR2021) | ~400–550 MHz (different PA tuning) | **yes** (LR2021 HF path) |
| `E80-900MBL-02` | `E80-900M2212S` (LR2021) | ~850–960 MHz | **yes** (LR2021 HF path) |

> ✅ **CORRECTED 2026-10-22 (operator correction).** An earlier version of this
> checklist claimed the E80 eval board was single-band per SKU. **That was
> wrong.** The board has **dual SMA jacks** (one sub-GHz, one 2.4 GHz) and the
> LR2021's HF path is wired out. Evidence in our own repo:
> - `2G4-LINK-BUDGET-ANALYSIS.md`: *"The E80-900MBL-02 board CAN and SHOULD test
>   at 2.4 GHz alongside 868 MHz… The board has dual SMA jacks (one sub-GHz, one
>   2.4 GHz), the LR2021 chip has a dedicated HF PA path (+12 dBm max at 2.4 GHz
>   vs +22 dBm at sub-GHz), and the bench firmware already auto-switches PA/RX
>   path when frequency ≥ 1.6 GHz (`radio_bench.c:321-343`)."*
> - **A full 2.4 GHz sweep was already run successfully on 2026-08-22** (session
>   `2608222108`) — the hardware path is *proven*, not assumed.
>
> The capability report's own line 28 ("supported module SKUs… 400 MHz band /
> 900 MHz band") describes the **module SKUs**, not the board's RF capability.
> The 400 vs 900 distinction is which LF sub-range the module is *tuned* for; the
> HF 2.4 GHz path is present on the LR2021 either way.
>
> **Practical consequence: the E80 eval board can serve both bands of the
> design.** The `-400` vs `-900` distinction still matters for the *sub-GHz* leg
> (a `-400` board will not do 915 well), but not for 2.4 GHz.

- [x] V0.1 **2.4 GHz antenna jack present** — dual SMA confirmed, HF path proven
      by the 2026-08-22 sweep.
- [ ] V0.2 Record which LF sub-range each board's module is tuned for
      (`-400` vs `-900`) — this decides whether that board can do 915 MHz.

---

## V1 — Flash path (the hard blocker) — **GATES THE PLAN**

Both documented write paths are currently **dead**. Resolve before anything else.

### V1a — SWD (the only viable write path)

- [ ] Probe enumerates as CMSIS-DAP: `lsusb | grep 2e8a` → expect `2e8a:000c`
- [ ] Dry-run chip detect only (**no writes, no reset**):
      `openocd -f <cfg> -c init -c targets -c shutdown` under `sudo`
- [ ] Record the exact failure mode if it fails

**Known state (2026-10-14):** probe handshake, interface init and clock control
all succeed; `cannot read IDR` / `AP #0x0` at **every** speed tried
(4000, 1000, 500, 200, 100, 50, 20 kHz) on both hosts. Cause **not determined**.

Ruled OUT already — do not re-investigate:
- firmware repurposing PA13/PA14 (LED1/KEY2 are PB13/PB14 — different port)
- unflashed Pico (it enumerates and initialises SWD cleanly)
- BOOTSEL being required (it is not, and it would *disable* the probe)
- target unpowered (the board answers on UART immediately)

Remaining candidates, cheapest first:
1. **SWCLK/SWDIO swapped** on the 3-wire harness. Correct: Pico **GP2 → SWCLK**,
   Pico **GP3 → SWDIO**, Pico **GND → GND**. A swap is invisible to openocd
   diagnostics — it looks identical to an unseated harness. **Test this first.**
2. Continuity / solder fault — a joint that did not take, or a data line shorted
   to GND (a short reads exactly like "target does not respond").
3. Drive strength on a long harness.

- [ ] V1a.1 Continuity Pico-pin → E80-pad, all three wires
- [ ] V1a.2 Neither data line shorted to GND
- [ ] V1a.3 Swap-test GP2/GP3
- [ ] V1a.4 `adapter speed 20`–`100`, `reset_config none`
- [ ] V1a.5 Full power-cycle with the adapter already attached
- [ ] V1a.6 **Chip detected** → record `DP IDR` / `IDCODE`

### V1b — UART ROM-ISP (expected dead — confirm once, then drop)

- [ ] `FLASH\n` over console → expect `OK JUMPING TO BOOTLOADER`
      (`\r` gives `ERR UNKNOWN` — the console is **LF**-terminated)
- [ ] `stm32flash` sync attempt after the jump

**Mechanism (schematic-verified):** BOOT0 is tied to GND via 10 k with **no
jumper, pad or testpoint**, and there is no CH340 DTR/RTS → BOOT0/NRST
auto-download circuit. The ROM bootloader never gets selected, so the jump lands
nowhere. **This is a hardware fact and will not be fixed by newer firmware.**

- [ ] V1b.1 Verdict recorded: dead / works

> ⚠️ **Do not restate or retract this without a fresh measurement.** The claim
> went green→red→green within one day in October. Record the *measured* state,
> the *terminator*, and the *schematic reason*.

---

## V2 — Console basics (15 min)

- [ ] V2.1 Board answers at all. **Baud is not necessarily 115200** — deployed
      fw `5fa7912` runs 115200, but `bench.c` in the repo now defaults to
      **2,000,000**. Sweep `115200, 2000000, 921600, 460800, 230400, 57600, 9600`
      before declaring a board dead.
- [ ] V2.2 `ID` command → expect `ID E80BENCH v1.2 …`
- [ ] V2.3 `STAT?` → `err=0`, `chip="SX1280 V3B A9B7"` on the T3S3; on the E80
      expect the LR2021 identity. Record exactly what it returns.

> ⚠️ **Stock demo firmware hazard:** the factory demo is a transparent LoRa
> bridge — any unrecognised UART byte is **transmitted over the air at 850 MHz /
> +22 dBm**. Never sync-spam or write random bytes to a board running stock
> firmware. Confirm bench firmware is flashed before any bulk UART work.

> ⚠️ An **armed** board refuses `FLASH` (`ERR POWER-CYCLE FIRST`) and IWDG-resets
> out from under long command chains. Bring it to `role=NONE armed=0` first, and
> keep any pre-flash command chain short.

---

## V3 — 915 MHz sweep — **NEVER BEEN RUN**

Every sweep on record is 2.4 GHz or 868 MHz (EU). 902–928 MHz is **new** for the
bench. The whole band decision depends on it working.

- [ ] V3.1 Set a 915 MHz config and confirm the board accepts it without error
- [ ] V3.2 Confirm the LF PA path is selected (`freq < 2400000000` → `PA_SEL_LF`)
- [ ] V3.3 Confirm **+22 dBm** is reachable (LF PA max)
- [ ] V3.4 Two-board loopback at 915 MHz, FLRC-1300, short range — record PER/RSSI/SNR
- [ ] V3.5 **Measure the actual 6 dB bandwidth of FLRC-650** — nominal is 600 kHz
      but the DTS compliance argument depends on the real number
- [ ] V3.6 **Measure the 3rd harmonic (2745 MHz) level.** It lands in a
      15.205(a) restricted band and the E80 output filter is undocumented.
      If we lack the instrument for this, record that we lack it.

---

## V4 — Watchdog durability soak — **TOP PROJECT RISK**

The bridge's raw-SPI TX path is documented to lock the radio up after **3–5
minutes**; a 15 s valid-frame watchdog was added to auto-recover, but it has
**never been proven over hours, let alone 4 days.**

- [ ] V4.1 Run the bridge continuously for **≥4 hours**; log every watchdog fire
- [ ] V4.2 Count lockups and recoveries. Record the mean time between failures.
- [ ] V4.3 Note whether recovery is **complete** or degrades over successive resets
- [ ] V4.4 Test the known inverted-incentive failure: the watchdog fires on "no
      valid frame in 15 s", but MMP heartbeats run every 10 s — so **more peers
      means more valid frames means the watchdog never trips, precisely when the
      radio is broken.** With 5 peers, valid frames arrive ~every 2 s.
- [ ] V4.5 Verdict: is a 4-day unattended run plausible? Yes / No / with caveats

---

## V5 — 2.4 GHz interference baseline (venue-like conditions)

- [ ] V5.1 Sweep 2400–2483.5 with a spectrum analyser or the board's RSSI scan
- [ ] V5.2 Record noise floor and occupied channels
- [ ] V5.3 Repeat at the venue if possible — the ranch runs its own mesh and the
      event will add several hundred 2.4 GHz emitters

**Known:** repo measurements show 2.4 GHz RX degrades after ~5 min of sustained
operation under WiFi interference (RX active ~2.5 min at 868 MHz, ~5 min at
2.4 GHz). This is a **measured limitation**, not a surprise.

---

## V6 — Dual-module coexistence (only if cross-band is revisited)

- [ ] V6.1 Two LR2021 modules on one board, both antennas fitted
- [ ] V6.2 No crystal/TCXO interference between them
- [ ] V6.3 Antenna coupling acceptable (measure desensitisation)
- [ ] V6.4 Band-switch latency measured (expected: tens of ms, full re-init)

---

## V8 — CAN THE STM32 BE THE BRIDGE AT ALL? (new 2026-10-23)

**Context:** the E80 board is now the relay (D14). Its STM32F103C8T6 at 72 MHz must
do what an ESP32-C3 at 160 MHz did in `fips_bridge.cpp`: relay opaque frames
between UART and the LR2021 at 921600–2 Mbaud.

**This is unproven.** The ESP32-C3 figure was never measured either, so there is no
baseline to compare against — but 72 MHz is the lowest clock in the project.

- [ ] V8.1 Measure a UART↔SPI relay loop at 2 Mbaud with fixed 255 B frames.
      Record sustained bytes/sec and dropped frames.
- [ ] V8.2 Compare against the requirement: one 1404 B FIPS datagram = 3 × 511 B
      FLRC frames; the RF hop is 9.6 ms, so the serial side must beat ~122 ms.
- [ ] V8.3 Test with FLRC-1300 active (not just loopback) — SPI contention with the
      radio matters.
- [ ] V8.4 If throughput is insufficient, record the ceiling and decide: lower
      fragment size, drop to FLRC-650, or reintroduce a faster MCU.
- [ ] V8.5 Verdict: STM32 bridge adequate / adequate with limits / not adequate

**Do this before writing the bridge firmware**, not after — it decides whether the
firmware is worth writing.

---

## V7 — Firmware gaps (from `ARCH-5NODE` §4) — verify against the real tree

These are **code changes**, not board tests, but confirm the diagnosis on the
actual `fips_bridge.cpp`:

- [ ] V7.1 **C1 (REQUIRED, ~1.5 d)** — ⚠️ **this is ESP-IDF code and does not run
      on an STM32.** Confirm the diagnosis (no single owner of the radio state
      machine) still applies to the E80 bench firmware, then implement it there.
      Original note: confirm there is no single owner of the
      radio state machine: one task fires raw SPI TX while another drives
      `standby()`/`startReceive()`. Only the SPI *bus* is mutexed, not the radio
      *state machine*. **This is the most likely cause of the 3–5 min lockup and
      must be fixed before TDMA can be deterministic at all.**
- [ ] V7.2 **C2 (REQUIRED, ~1 d)** — TDMA slot gate; delete the 0–3 ms random
      jitter (jitter and TDMA are mutually exclusive arbitration mechanisms)
- [ ] V7.3 **C3 (REQUIRED, ~1 d + GPS wiring)** — UTC time base (ADR-021 priority
      chain: GPS epoch → laptop SET_TIME → millis)
- [ ] V7.4 **C4 (REQUIRED, ~0.5 d)** — watchdog that survives 4 days; make
      `radioInit()` the single shared init path returning `esp_err_t`
- [ ] V7.5 **C5 (REQUIRED, ~2 h)** — variable packet length; today every frame is
      padded to 255 B, so a 37 B heartbeat costs 785 µs of air instead of 114 µs
      (≈4–5× wasted airtime with duplication)
- [ ] V7.6 **C6 (REQUIRED for 4 days, ~0.5 d)** — kill the infinite blink loops
      (a dead balloon with a working LED), emit the counters that already exist,
      distinguish USB failure, persist counters in RTC memory

---

## Blocking findings to carry forward

1. **Upstream FIPS master (`6c3e1c8`) has NO serial transport implementation.**
   `TransportType::SERIAL` is declared but `TransportsConfig` has no `serial`
   field, and `src/transport/mod.rs` declares only loopback, nym, socks5, tcp,
   tor, udp, ethernet, ble. The June 2026 test used FIPS **v0.3.0-dev**, which
   did have `src/transport/serial/mod.rs`. **Pin and vendor the exact revision
   that has the serial transport — do not let a `cargo update` remove the
   transport the entire architecture depends on.**
2. **FIPS serial transport is explicitly point-to-point** — "connect exactly two
   endpoints". **One serial transport instance = one link = one peer.** A ground
   node cannot hold four peers over one bridge; it needs four bridges, or must
   reach the others by FIPS *transit*. **The real answer to "how many ground
   peers share one bent-pipe relay" is two, under the proven design.** N=5 is a
   transport-topology problem, not a peer-count problem (peer capacity is 128).
