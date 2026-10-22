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

---

## 6. "What if we use 2.4 GHz instead of 915?" — a real trade

**First, the FLRC-260 problem does not go away.** It is not a band problem.

`47 CFR 15.247(a)(2)` requires **≥500 kHz of 6 dB bandwidth** for a DTS in
**both** 902–928 MHz and 2400–2483.5 MHz. The limits are byte-identical in both
bands — *the law does not separate them*. FLRC-260's ~300 kHz fails in either
band, and FLRC-1300's 1200 kHz passes in either band.

> **So the compliance fix is "use FLRC-1300 (or 650)", not "change band".**
> Band choice is orthogonal to that problem.

### 6.1 The genuine arguments for 2.4 GHz

| # | Argument | Weight |
|---|---|---|
| 1 | **Proven on this exact hardware.** A full 2.4 GHz sweep ran 2026-08-22 (session `2608222108`). **915 MHz has never been swept on this bench.** | **Strong** — with ~2 weeks left, this is the biggest single de-risking available |
| 2 | **Zero firmware band work.** `fips_bridge.cpp` already runs `BRIDGE_FREQ 2450.0f` / `BRIDGE_POWER 12`. 915 means a config change plus re-verification of every knob | **Strong** |
| 3 | **Tiny antennas.** λ/2 = 3.1 cm at 2.4 GHz vs 16.4 cm at 915 — less tether interaction, less wind loading, easier payload integration | Moderate |
| 4 | **Wider band.** 83.5 MHz (2400–2483.5) vs 26 MHz (902–928) — more room to move off a dirty channel | Moderate |
| 5 | **Global ISM.** No regional variant risk; both the `-400` and `-900` eval boards work | Minor |

### 6.2 The genuine arguments against 2.4 GHz

| # | Argument | Weight |
|---|---|---|
| 1 | **18.55 dB less budget** — +12 dBm HF PA vs +22 dBm LF (10 dB), plus 8.55 dB extra FSPL | Moderate — see 6.3 |
| 2 | **Most contested spectrum on site.** 2,000-person outdoor event: every hotspot, AP, camera, phone. Plus the ranch's own mesh | **Strong for a live demo** |
| 3 | **Documented RX degradation.** The repo measured 2.4 GHz RX degrading after ~5 min of sustained operation under WiFi interference (RX active ~2.5 min at 868 MHz, ~5 min at 2.4 GHz) | **Strong for a 4-day run** |

### 6.3 Why the 18.55 dB deficit is mostly unspendable

From the RF trade study: at 2450 MHz / +12 dBm, **every configuration closes at
every distance to 1 km with ≥16 dB of spare margin.**

| Config | 403 m leg | 800 m direct |
|---|---|---|
| 915 MHz, FLRC-1300 | 45.7 dB | 39.8 dB |
| 2450 MHz, FLRC-1300 | 26.7 dB | 16.3 dB |

**You do not need 45.7 dB of margin for a 400 m link.** At venue scale (sub-km)
the 915 advantage is largely a number on a page. *Link closure is not the
binding constraint* — interference and hardware reliability are.

### 6.4 The option that changes the calculus: a FEM

The repo already carries a **SKY66112-11 front-end module** component
(`tracker/firmware/components/sky66112`, ADR-005). Fitting it recovers
**+10 dB** at 2.4 GHz: +12 → +22 dBm conducted, +28 dBm EIRP with a 6 dBi
antenna. That closes most of the PA gap and makes 2.4 GHz genuinely competitive
— at the cost of ~1 g, a few dB of insertion loss, and TX/RX switching logic.

### 6.5 Recommendation

**Run 2.4 GHz now as the bench default; target 915 MHz for the event; decide on
measured evidence, not on preference.**

| Phase | Band | Why |
|---|---|---|
| Bench bring-up, E80 verification, bridge firmware work (C1–C6) | **2.4 GHz** | Proven path, zero band work, fastest route to a working relay. De-risks the 2-week deadline. |
| 915 MHz sweep (checklist V3) | 915 | Cheap to attempt; it is the only thing that can *unlock* the better event band |
| Event | **915 MHz if the sweep passes, else 2.4 GHz** | 915 wins on uncontested spectrum and no WiFi-induced RX degradation. 2.4 GHz is a *proven* fallback, not a disaster. |
| Contingency if 915 fails and 2.4 GHz is dirty on site | 2.4 GHz + SKY66112 FEM | Recovers 10 dB |

**The deciding measurement is the venue RF survey.** Both bands are defensible on
paper; only a site survey distinguishes them. Book it as a Phase 0 gate.

**What is NOT recommended:** cross-band (two radios everywhere, and it does not
remove the need for TDMA), or 433 MHz (15.231, not a data band).
