# RF Trade Study — Tethered Balloon Transparent Relay, FIPS Data Link
## Exit & Build 6 · Sovereignty Ranch, Bandera, Texas · 5–8 Nov 2026

**Status:** Recommendation. **Date:** 2026-10-22. Chain, both ends: `fips → PTY → serial_udp_bridge.py → USB CDC → ESP32-C3 → LR2021 → antenna`. Balloon carries the same modem pair, cut-through (no FIPS in the air). Site: ~450 m AMSL, ~200 acres (≈900 m × 900 m), 6–8 m cedar canopy, |S| ~2,000 people and several hundred 2.4 GHz emitters.

---

## 1. Regulatory: 47 CFR 15.247, 902–928 vs 2400–2483.5 MHz

Both bands carry **identical limits**. The choice is physics and hardware; the law does not separate them.

| Item | 902–928 | 2400–2483.5 | Citation |
|---|---|---|---|
| Max conducted (DTS / FHSS) | +30 dBm (1 W) | +30 dBm (1 W) | 15.247(b)(3) / (b)(1) |
| Free antenna gain | 6 dBi; above that, reduce conducted dB-for-dB | same | 15.247(b)(4)(i) |
| **Max EIRP** | **+36 dBm (4 W)** | **+36 dBm (4 W)** | 30 + 6 |
| PSD (DTS) | 8 dBm / 3 kHz | 8 dBm / 3 kHz | 15.247(e) |
| DTS min 6 dB BW | ≥ 500 kHz | ≥ 500 kHz | 15.247(a)(2) |
| FHSS ch. count / occupancy | ≥25 ch if 20 dB BW ≥250 kHz, 0.4 s per 10 s; ≥50 ch, 0.4 s per 20 s if <250 kHz | ≥75 ch, 0.4 s per 20 s | 15.247(a)(1)(i)/(ii) |
| Duty cycle (DTS) | none | none | — |
| Spurious | 20 dB down or 15.209 | same | 15.247(d) |

### 1.1 Our compliance path has one hard consequence

Firmware transmits on **one fixed channel** → we cannot claim FHSS, so we must qualify as a **DTS**. That makes the 500 kHz floor binding:

> **FLRC-260 and FLRC-325 occupy BWF = 300 kHz (datasheet Table 3-12). A fixed-channel FLRC-260 link is NOT compliant in 902–928 MHz.** It would only be legal as an FHSS system hopping ≥25 channels, which we do not implement.

DTS PSD feasibility, `PSD = P_tx − 10·log10(BW/3 kHz)`:

| Mode | BWF | @+22 dBm | @+30 dBm | DTS-legal? |
|---|---|---|---|---|
| FLRC-260/325 | 300 kHz | +2.0 | +10.0 | **No** — fails 6 dB BW |
| FLRC-650 | 600 kHz | −1.0 | +7.0 | Marginal — 6 dB BW thin |
| FLRC-1040/1300 | 1200 kHz | −4.0 | +4.0 | **Yes, comfortable** |
| FLRC-2600 | 2666 kHz | −7.5 | +0.5 | Yes, range-poor |
| LoRa BW500 | 500 kHz | −0.2 | +7.8 | Marginal — at the floor |
| LoRa BW125 | 125 kHz | +5.8 | +13.8 | **No** — fails 6 dB BW |

### 1.2 The law stops binding; the PA starts

| Config | Conducted | Ant | EIRP | Gap to +36 |
|---|---|---|---|---|
| 915, LR2021 LF PA (TXOPLF typ +22) | +22 | 2 dBi | **+24** | 12 dB |
| 915, LF PA + 6 dBi balloon Yagi | +22 | 6 dBi | +28 | 8 dB |
| 915, NiceRF F33 (2 W) + 6 dBi | +30 (backed off from +33) | 6 dBi | +36 | 0 dB |
| 2450, LR2021 HF PA (TXOPHF max +12) | +12 | 2 dBi | **+14** | 22 dB |
| 2450, SKY66112-11 FEM (+22) + 6 dBi | +22 | 6 dBi | +28 | 8 dB |

**Neither band is limited by Part 15 at this venue — both are limited by the LR2021 PA.** 915 sits 8 dB under the legal ceiling, 2.4 GHz 18 dB under. A waiver or a bigger antenna buys nothing until a FEM or the F33 module is fitted.

*Verify before the event:* (a) measured 6 dB BW of FLRC-650, not the nominal BWF; (b) **harmonics — 3×915 = 2745 MHz (radio-astronomy) and 2×2450 = 4900 MHz (aeronavigation) both land in 15.205(a) restricted bands, and the E80 output filter is undocumented**; (c) 15.247(c)(2) fixed point-to-point relief does **not** apply to a moving tether — do not rely on it; (d) FAA Part 101 Subpart B notice rules for moored balloons above 150 ft AGL.

---

## 2. Path loss, sensitivity, link budget

`FSPL(dB) = 20·log10(d_km) + 20·log10(f_MHz) + 32.44`

| | 50 m | 150 m | 300 m | 600 m | 1000 m |
|---|---|---|---|---|---|
| FSPL @915 | 65.65 | 75.19 | 81.21 | 87.23 | 91.67 |
| FSPL @2450 | 74.20 | 83.75 | 89.77 | 95.79 | 100.22 |
| Δ | 8.55 | 8.55 | 8.55 | 8.55 | 8.55 |

Δ = 20·log10(2450/915) = **8.55 dB**, distance-independent (the repo's 868 column shows 9.0 dB; 915 is 0.45 dB kinder).

### 2.1 Sensitivities — LR2021 datasheet Rev 2.1, 1% PER, G13 rx_boost=7

Tables 3-12 (FLRC sub-GHz), 3-13 (FLRC 2.4 GHz), 3-17/3-18 (LoRa). Measured, not estimated.

| Mode | BWF | @915 | @2450 |
|---|---|---|---|
| FLRC-260 | 300 kHz | −111.0 | −108.5 |
| FLRC-650 | 600 kHz | −107.0 | −104.0 |
| FLRC-1300 | 1200 kHz | −104.5 | −101.5 |
| FLRC-2600 | 2666 kHz | −100.5 | −99.0 |
| LoRa SF7/125 | 125 kHz | −127.5 | −123.0 (BW200) |
| LoRa SF9/125 | 125 kHz | −133.0 | −128.5 (BW200) |
| LoRa SF10/125 | 125 kHz | −136.0 | −131.0 (BW200) |
| LoRa SF7/500 | 500 kHz | −122.0 | −118.5 |
| LoRa SF9/500 | 500 kHz | −127.5 | −124.0 |
| LoRa SF10/500 | 500 kHz | −130.0 | −127.0 |

### 2.2 Margins, whip-to-whip, each band at its hardware maximum

`Prx = P_tx + G_tx − FSPL + G_rx − L`; `G = 2 dBi` both ends, `L = 1.0 dB` (SMA + cable + mismatch).

**915 MHz, +22 dBm, EIRP +24 dBm**

| Mode | 50 m | 150 m | 300 m | 600 m | 1000 m |
|---|---|---|---|---|---|
| FLRC-260 | 70.4 | 60.8 | 54.8 | 48.8 | 44.3 |
| FLRC-650 | 66.4 | 56.8 | 50.8 | 44.8 | 40.3 |
| FLRC-1300 | 63.9 | 54.3 | 48.3 | 42.3 | 37.8 |
| LoRa SF7/500 | 81.4 | 71.8 | 65.8 | 59.8 | 55.3 |
| LoRa SF9/125 | 92.4 | 82.8 | 76.8 | 70.8 | 66.3 |
| LoRa SF10/125 | 95.4 | 85.8 | 79.8 | 73.8 | 69.3 |

**2450 MHz, +12 dBm, EIRP +14 dBm**

| Mode | 50 m | 150 m | 300 m | 600 m | 1000 m |
|---|---|---|---|---|---|
| FLRC-260 | 49.3 | 39.8 | 33.7 | 27.7 | 23.3 |
| FLRC-650 | 44.8 | 35.3 | 29.2 | 23.2 | 18.8 |
| FLRC-1300 | 42.3 | 32.8 | 26.7 | 20.7 | 16.3 |
| LoRa SF7/500 | 63.8 | 54.3 | 48.2 | 42.2 | 37.8 |
| LoRa SF10/125 | 71.8 | 62.3 | 56.2 | 50.2 | 45.8 |

Every config closes at every distance to 1 km on both bands with ≥16 dB spare. **Link closure is not the problem.** 915's advantage is `10 dB PA + 8.55 dB FSPL = 18.55 dB` at equal antenna gain.

### 2.3 Airtime and datagram size

`FLRC airtime = (8N + 64)/R`; LoRa per AN1200.13 (`T_sym = 2^SF/BW`, 8-symbol preamble, explicit header, CRC on).

| Mode | Max payload | 511 B | 255 B | Goodput @2 ms gap |
|---|---|---|---|---|
| FLRC-260 | 511 B | 16.5 ms | 8.6 ms | 27.6 kB/s |
| FLRC-650 | 511 B | 6.6 ms | 3.4 ms | 59.4 kB/s |
| **FLRC-1300** | 511 B | **3.2 ms** | **1.6 ms** | **96.4 kB/s** |
| LoRa SF7/500 | 255 B | — | 100 ms | 2.5 kB/s |

FIPS TUN MTU 1404 B → **3 × 511 B FLRC frames**. One hop = 9.6 ms + 2 gaps; **cut-through relay both hops ≈ 31 ms/datagram**; half-duplex sustained goodput **≈49 kB/s ≈ 394 kbps** — roughly 80× a LoRa SF7/125 path, which needs ~2.5 s per 1404 B datagram.

> ⚠ **The radio is not the bottleneck.** `serial_udp_bridge.py` at 115200 baud caps at 11.5 kB/s = **122 ms per 1404 B datagram**, 4× slower than the relay chain. ≥921600 is a prerequisite.

---

## 3. Balloon geometry

`leg = sqrt((D/2)² + h²)`, `θ = atan(h/(D/2))`, `r₁ = sqrt(λ·d₁·d₂/D)`.

| D | h AGL | leg | total | θ | r₁@915 | r₁@2450 | relay gain |
|---|---|---|---|---|---|---|---|
| 200 m | 45.7 m (150 ft) | 110.0 | 219.9 | 24.6° | 3.00 | 1.83 | **+5.20 dB** |
| 200 m | 91.4 m (300 ft) | 135.5 | 271.0 | 42.4° | 3.33 | 2.04 | +3.38 |
| 800 m | 45.7 m | 402.6 | 805.2 | 6.5° | 5.74 | 3.51 | **+5.96 dB** |
| 800 m | 91.4 m | 410.3 | 820.6 | 12.9° | 5.80 | 3.54 | +5.80 |

Relay gain = `FSPL(D) − FSPL(leg)` per hop, free space.

### 3.1 Blunt finding: at short separation the balloon adds nothing

At 200 m, direct ground LOS at 915/FLRC-1300 already carries **51.8 dB**. The balloon returns **+5.2 dB** and *halves* throughput (half-duplex). **Not worth the airtime.** At 800 m, direct carries 39.8 dB and the balloon returns +5.96 dB — a rounding error beside 40 dB.

The balloon's only real product is **LOS over obstruction**. Knife-edge, `v = h_obs·sqrt(8/(λD))`, `L = 6.9 + 20·log10(sqrt((v−0.1)²+1) + v − 0.1)`:

| Obstruction above direct LOS | 200 m @915 | 800 m @915 | 800 m @2450 |
|---|---|---|---|
| 1.5 m (person) | 10.5 dB | 8.3 dB | 9.7 dB |
| 3 m (vehicle/cedar) | 14.2 | 10.5 | 13.0 |
| 6 m (canopy) | 19.4 | 14.2 | 17.8 |

So fly the relay **only when the 800 m ground path is obstructed by ≥6 m** — the one regime where 14–20 dB of recovered knife-edge loss beats the relay's cost. Otherwise terminate both endpoints on the ground.

### 3.2 Near-end grazing is the real risk

The ray leaves the endpoint at 1.5 m and rises linearly. At D = 800 m, h = 45.7 m it is **2.6 m up at 10 m out**, 3.7 m at 20 m, 7.0 m at 50 m. A crowd, truck, or tent inside the first ~30 m blocks it: first-Fresnel clearance past a 3 m obstruction needs **x_min = 30.4 m** at 45.7 m alt vs **11.9 m** at 91.4 m. At D = 200 m: 5.1 m vs 3.3 m.

**150 → 300 ft costs 0.16 dB of FSPL but more than doubles near-end clearance.** Go to 300 ft if the FAA paperwork allows — for geometry, not power.

---

## 4. Recommendation

**Band: 915 MHz.** 18.55 dB of free budget (10 dB PA + 8.55 dB FSPL) at identical legal limits, plus the venue argument: 2400–2483.5 at a 2,000-person outdoor event is the most contested slice of spectrum on site — every hotspot, AP, and camera. A 1.2 MHz FLRC channel there is a collision looking for a time. 915 has no consumer devices; local interferers (AMI meters, LoRaWAN US915) are low-duty-cycle and frequency-separated.

| | **Uplink** (endpoint → balloon) | **Downlink** (balloon → endpoint) |
|---|---|---|
| Band | 915 MHz, 902–928 | 915 MHz, same channel |
| Modulation | **FLRC 1300 kbps, CR 3/4** | **FLRC 1300 kbps, CR 3/4** |
| BWF / 6 dB BW | 1200 kHz | 1200 kHz |
| TX power | **+22 dBm** (LF PA max) | +22 dBm |
| Antenna | 2 dBi dipole | 2 dBi dipole |
| EIRP | +24 dBm | +24 dBm |
| Payload | 511 B × 3 per 1404 B datagram | same |
| Airtime | 3.19 ms/frame, 9.6 ms/hop | same |
| Margin @403 m leg | **45.7 dB** | 45.7 dB |
| Margin @800 m direct | 39.8 dB | 39.8 dB |

**Why FLRC-1300, not FLRC-260**, despite 6.5 dB less sensitivity: (1) FLRC-260's 300 kHz **fails the 15.247(a)(2) 6 dB BW floor** — not a legal fixed-channel DTS; (2) at 403 m we hold 45.7 dB of margin, so 6.5 dB of sensitivity is unspendable; (3) 1300 kbps gives 96 kB/s vs 27.6 kB/s, which is what makes a FIPS handshake tolerable. Trade margin we cannot use for compliance and throughput we can.

**Why symmetric:** the two legs differ by ≤0.2 dB, so an asymmetric PHY buys nothing but a second failure mode for the ADR ladder. The one legitimate asymmetry is power — if a SKY66112-class FEM or the F33 is fitted at the balloon, drop the downlink to +30 dBm conducted (+36 dBm EIRP at 6 dBi) for +8 dB of downlink margin at zero uplink cost.

**Reserve (one): FLRC-650 @915, +22 dBm, 2 dBi.** Sensitivity −107.0 dBm, and at 600 kHz it is the *narrowest* mode still clearing the DTS floor (−1.0 dBm/3 kHz), hence the least spectrum-hungry compliant fallback if 915 is dirty on site. Do **not** hold LoRa in reserve for FIPS: SF7/125 fails the BW floor and SF7/500 delivers 2.5 kB/s — a 2.4 s datagram that no FIPS handshake survives. LoRa stays where ADR-012 put it, on MeshCore telemetry and a second radio.

---

## 5. Top risks

1. **The serial bridge, not the RF link.** 115200 baud = 11.5 kB/s = 122 ms/datagram, 4× worse than the relay. Must be ≥921600 before flight.
2. **Near-end obstruction at 800 m.** Ray is 2.6 m above ground 10 m from the endpoint. Crowd/truck/tent blocks it. Fix with altitude or endpoint placement, not TX power.
3. **The balloon may add nothing.** At 200 m with 51.8 dB direct margin the relay returns +5.2 dB and halves throughput. Decide its purpose (obstruction bypass vs demonstration) before rigging.
4. **Regulatory hygiene.** Fixed-channel FLRC-260/325 is non-compliant at 915; 2745 and 4900 MHz harmonics sit in 15.205(a) restricted bands with an undocumented E80 output filter. Sweep the venue before assuming compliance.

---

## Sources
47 CFR 15.247(a)(1)(i)/(ii), (a)(2), (b)(1), (b)(3), (b)(4)(i), (c)(2), (d), (e); 15.205(a); 15.209; 14 CFR 101 Subpart B. Semtech LR2021/LR2022/LR2012 Datasheet Rev 2.1 (13/04/26), Tables 3-12, 3-13, 3-17, 3-18, TXOPLF/TXOPHF. Repo: `2G4-LINK-BUDGET-ANALYSIS.md`, `LR2021-THROUGHPUT-OPTIMIZATION-ANALYSIS.md`, `FLRC-RANGE-THROUGHPUT-ARCHITECTURE-ANALYSIS.md`, `adr/004`, `adr/005`, `adr/012`.
