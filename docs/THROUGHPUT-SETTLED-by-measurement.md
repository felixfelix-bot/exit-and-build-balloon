# 512 B / 2.6 Mbps — CLOSED by measurement

**Date:** 2026-10-25. **Supersedes:** `docs/FLAG-512b-throughput-conflict.md` (now resolved).
**Card that produced the earlier verdict:** `balloon/t_6b68897c`.

You asked whether real measurement data exists in the repo proving this. **It does
— and it settles the question in a way neither of us stated.** I was wrong to keep
the flag open without first sweeping `balloon-fresh` for raw data rather than
documents.

---

## The measurement

**`balloon-fresh` → `docs/sustained-throughput-results-2026-07-23.md`**, Phase 1 FLRC
sustained sweep:

| Bitrate (kbps) | Packets RX | Sustained (kbps) | % of theoretical | PER |
|---:|---:|---:|---:|---:|
| **2600** | 21,923 | **1484.9** | **57.1 %** | **0.00 %** |
| 1300 | 11,906 | 806.4 | 62.0 % | 0.02 % |
| 650 | 6,203 | 420.1 | 64.6 % | 0.00 % |
| 325 | 3,543 | 240.0 | 73.8 % | 0.00 % |

Test config, stated in the same file: **2440 MHz, packet size 127 bytes, TX 12 dBm,
SPI 20 MHz, TX continuous (no inter-burst pause), 50,000 packet count**, RX window
15 s listen / 3 s silence timeout, raw 2-byte-opcode SPI (ADR-020, no RadioLib).

**3,135 bytes/ms × ... — no: 1484.9 kbps sustained at FLRC BR2600, with 0.00 % PER
over 21,923 packets.** That is the number. It is not 2600.

---

## Where BOTH of us were wrong

### The audit's cause was wrong

The audit attributed the gap to **CR 3/4**, deriving a ~1910 kbps ceiling at 511 B.
**The measurement contradicts that attribution.** The sweep ran at **LEN 127** and
still hit only **57.1 %** of 2600 — and at 127 B, CR-3/4 overhead would cap the
theoretical at 1798 kbps, so 1484.9 is 82.6 % of *that*. The missing third is not
in the air interface.

The document names the real cause in its own §"TX Rate Anomaly":

> **TX reports ~1487 kbps at ALL bitrates** (2600, 1300, 650, 325). This is because
> the TX loop time is dominated by **SPI overhead** (FIFO write + command
> sequence), not air time. At 325 kbps, air time per packet is 3.12 ms but SPI
> overhead is **~680 µs** — the TX loop sends at the same rate regardless of the
> radio's actual bitrate setting.

> This means the sustained throughput numbers above are **TX-limited, not
> RX-limited**.

**So the ceiling is a host-side SPI wall of ~1487 kbps, flat across every bitrate —
including 2600.** Not the coding rate, not the payload length.

### Your claim, checked against the same data

512 B / ~2.6 Mbps goodput: **not supported by this measurement.** The measured
sustained figure at BR2600 is **1484.9 kbps**, 57.1 % of air rate, 0.00 % PER.
But the *reason* I gave (CR 3/4 airtime) was the wrong reason, and the audit I was
quoting cited the wrong mechanism too.

### What the data says about the 512-lever

The sweep is **TX-limited at ~1487 kbps regardless of bitrate**, which means:

- **Payload size is not the binding constraint now** — the SPI write path is.
  A bigger payload amortises fixed per-packet overhead, so it should help
  *somewhat*, but it cannot exceed the ~1487 kbps wall that the 127 B run already
  sat against. The audit priced 255→511 at **+2.1 %**; that is consistent with a
  wall that is not set by payload length.
- **Is 512 B reachable at all?** No — **511 B is the driver's documented maximum**
  (`lr20xx_radio_flrc_types.h:210`), enforced in firmware
  (`BENCH_START_LEN_MAX_FLRC 511u`). 512 is not a legal length.
- **Nobody has measured sustained goodput at 511 B.** The 511 B rows on disk are
  *delivery* results (50/50 RX, bit_err 0) taken at a **40 ms inter-packet gap**,
  which floors the rate at ~90 kbps and cannot answer a throughput question. The
  audit says exactly this.

---

## Verdict

1. **The air rate is 2.6 Mbps. Best measured sustained goodput is 1484.9 kbps
   (57.1 %), 0.00 % PER, at LEN 127 / BR2600, 2.4 GHz.**
2. **The limiter is the host SPI/TX path (~1487 kbps flat across all bitrates),
   not CR 3/4 and not payload length.** This corrects the audit.
3. **512 B is not a legal payload** — 511 B is the driver maximum. The
   "255→512" framing cannot be executed as stated.
4. **The cheapest real lever is fixing the TX SPI bottleneck** — which is exactly
   what the repo's own `lr2021-throughput-fix-plan-2026-07-29.md` targets
   (Phase 0–3, quick wins → pipelining), and what `P4.1-DMA-CHAINING-ZERO-COPY`
   attacks. **A larger payload is downstream of that, not a substitute for it.**
5. **Wanted but not existing:** a sustained (no-gap) 511 B sweep. If you have run
   one since, its CSV closes point 4 with a real number — I found no such file.

### What this changes in our docs

`docs/S3-AND-AMAZON-PRICING.md` quoted ADR-026's 1377/838 kbps table. Now replaced
with the measured sustained figure above, which is **newer, from a real 2.4 GHz
sustained sweep, and consistent with the air-rate ceiling**. The S3 answer itself
is unchanged: an ESP32 does not answer V8, because V8 asks about the STM32F103.

### Correction to my own process

I raised the flag citing three *documents*. The repo also held the *data*, and I
did not look for it before escalating. **Documents can disagree; a sweep CSV with
21,923 packets and 0.00 % PER cannot.** That is the check I should have run first.
