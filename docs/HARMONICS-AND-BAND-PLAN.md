# Band plan and harmonic analysis — 433 vs 915 vs 2450 MHz

**Question asked:** should the relay use 433 MHz + 2.4 GHz instead of 915 + 2.4 GHz,
and will the two channels interfere with each other through harmonics?

**Answer: no to 433. And the cross-band idea should be dropped too — but not for
harmonic reasons.** Reasoning below.

---

## 1. 433 MHz in the United States: not a data band

433.92 MHz in the US is **not** a general-purpose ISM band of the kind EU 433 is.
It is governed by two narrow rules:

| Rule | Band | Nature | Why it fails us |
|---|---|---|---|
| 47 CFR 15.231 | 40.66–40.70, 433.05–434.79 MHz | **Periodic / control transmissions** — field-strength limits, not conducted power; explicit duty-cycle and transmission-length limits | Designed for remotes, sensors, alarms. Not continuous data. A FIPS link is continuous bidirectional traffic. |
| 47 CFR 15.240 | 433.5–434.5 MHz | RFID / tagging interrogators | Narrower still; wrong application |

The blocker is not the radio hardware — the LR2021's LF PA covers roughly
400–960 MHz and the E80-400MBL-02 eval board exists precisely to exercise the
400 MHz sub-range — it is the **regulation**. At 902–928 MHz we get 47 CFR
15.247: **+30 dBm conducted, +36 dBm EIRP**, no duty-cycle limit for DTS, and
digital modulation explicitly permitted. That is a data band. 433 is not.

**Do not design around 433. Treat it as closed for this demo.**

---

## 2. Harmonic analysis — the good news

The instinct to check harmonics was right, and the result is that the two bands
are actually **harmonically compatible**:

| Product | Frequency | Lands on the other channel? | Restricted band? |
|---|---|---|---|
| 915 fundamental | 915 MHz | — | no |
| 915 × 2 | 1830 MHz | no | no |
| **915 × 3** | **2745 MHz** | no | **yes — 15.205(a)** |
| 2450 fundamental | 2450 MHz | — | no |
| 2450 × 2 | 4900 MHz | no | **yes — 15.205(a)** |
| 915 × 2.68 | 2450 MHz | only at a non-integer multiple — no coherent harmonic | — |

So **neither band's harmonic lands on the other band's fundamental.** The
915/2450 pair is a clean pairing from a frequency-planning standpoint.

**But two real problems remain, and they are what actually kill the cross-band design:**

1. **The 3rd harmonic of 915 (2745 MHz) and the 2nd harmonic of 2450 (4900 MHz)
   both land in 47 CFR 15.205(a) restricted bands.** The E80 board's output
   filter is **undocumented** — we do not know its harmonic rejection. This is an
   *unmeasured compliance risk on whichever band we pick*, and it must be
   resolved by measurement, not assumption. It applies to the symmetric 915
   design too. **Action item, not a design change.**
2. **Receiver desensitisation is not a harmonic problem, it is a blocking
   problem.** In a cross-band relay the balloon transmits on 915 while receiving
   on 2450. The frequency offset is 1525 MHz — far outside any harmonic — but a
   +22 dBm local transmitter 1525 MHz away still presents a blocking challenge to
   the receiver front end, and the E80's front-end filtering is also undocumented.

---

## 3. Why the cross-band design is being dropped anyway

This is the important correction. The cross-band bent pipe (balloon RX 2.4 GHz /
TX 915, ground nodes the reverse) was my earlier recommendation. The consultants
found three reasons it is the wrong call, and they are decisive:

### 3.1 One LR2021 cannot serve two bands at once

The LR2021 is dual-band **as a chip family capability**, not as a simultaneous
mode. It has one transceiver and one frequency synthesiser; a band change is a
full re-initialisation costing tens of milliseconds. Cross-band therefore
requires **two LR2021 modules on the balloon** — and two on *every ground node*
too, because each ground node must TX one band and RX the other.

Cost: 2× radio modules everywhere (≈ +1.8 g and +1 antenna per payload), plus a
second SPI chip-select, plus a whole new firmware capability (band switching,
`ARCH-5NODE` §4 C8, ~2–3 days).

### 3.2 It does not remove the need for TDMA

Cross-band partitions the ground nodes into two RF islands (say 3 on 2.4 GHz, 2
on 915). **Each island is still a half-duplex collision domain with N>1 nodes in
it.** You still need the schedule. So cross-band buys you self-interference
removal at the cost of 2× radios — and self-interference was never the binding
constraint once TDMA exists.

### 3.3 It costs 18.55 dB on half the link

The 2.4 GHz leg runs at the LR2021's HF PA limit of **+12 dBm** versus **+22 dBm**
at sub-GHz — a 10 dB deficit — on top of 8.55 dB of extra free-space loss. That
is 18.55 dB of budget thrown away on the leg that needs it most, and the venue is
the most contested slice of spectrum on site (a 2,000-person outdoor event with
several hundred 2.4 GHz emitters).

---

## 4. Decision: symmetric 915 MHz, single shared channel

| | Value | Why |
|---|---|---|
| Band | **915 MHz (902–928)** | 18.55 dB more budget than 2.4 GHz; no consumer devices; local interferers are low-duty-cycle |
| Modulation | **FLRC 1300 kbps, CR 3/4** | 1200 kHz width clears the 15.247(a)(2) 6 dB BW floor comfortably; 96 kB/s |
| TX power | **+22 dBm** (LR2021 LF PA max) | EIRP +24 dBm with a 2 dBi dipole — 12 dB under the legal ceiling, so **the PA binds, not the law** |
| Antenna | 2 dBi dipole both ends | |
| Channel | one shared channel, all nodes | TDMA arbitrates; no frequency plan needed |
| Reserve | FLRC-650 @ 915 | Narrowest mode still DTS-compliant if 915 is dirty on site |

### The one compliance trap

> **FLRC-260 and FLRC-325 occupy ~300 kHz of bandwidth. A fixed-channel FLRC-260
> link does NOT comply with 47 CFR 15.247(a)(2), which requires ≥500 kHz of 6 dB
> bandwidth for a DTS.** We do not implement frequency hopping, so we cannot
> claim FHSS instead. FLRC-260 is off the table for 915 — not because of
> sensitivity, but because it is not a legal fixed-channel mode.

This must be re-verified by **measuring** the actual 6 dB bandwidth of FLRC-650
on the real hardware before the event; the 600 kHz figure is nominal.

---

## 5. If cross-band is ever revisited

Keep it on the shelf as a **stretch goal** with these preconditions met:
two LR2021 modules demonstrated coexisting on one payload (crystal/TCXO and
antenna coupling verified), the band-switch firmware written and soak-tested, and
measured front-end blocking/harmonic data for the E80 board. That is not a
two-week project.
