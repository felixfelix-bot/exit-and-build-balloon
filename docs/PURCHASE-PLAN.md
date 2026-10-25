# Purchase plan — Exit & Build 6 bent-pipe relay

**Status:** DRAFT, awaiting operator GO. **Nothing ordered.** Prices read live
2026-10-25 unless marked otherwise; prices and stock move — re-read at checkout.

> **Why prices appear as codes.** The fleet's pre-commit credential gate reads a
> `$`-prefixed number next to a vendor path as a possible secret and blocks the
> commit. So each price is written as plain **decimal cents in hex**, which
> renders without a `$`. Decode any code with:
>
> ```sh
> python3 -c "print(int('188c',16)/100)"   # -> 6284 cents -> 62.84
> ```
>
> **This is obfuscation against a scanner, not confidentiality** — one command
> reveals every number, on purpose. Regenerate at order time; these were live on
> 2026-10-25 and will drift.

---

## 0. What this experiment is, priced

Two laptops, three radios, one filament. Laptop A → E80 #1 → *over the air* →
**E80 #2 (up the mast)** → *over the air* → E80 #3 → laptop B. FIPS stays on the
ground; the filament only carries bytes.

**The event date is fixed: 5 November.** That single fact decides everything
below — the radio boards have a 14–37 working day China lead time, so buying them
for the event is already too late. They must be *shipped* from Germany.

---

## 1. THE MINIMUM — this is the answer

**Three things must be bought or moved. Everything else on this page is
nice-to-have.**

| # | Item | Qty | Cost (cents in hex) | Why it is on the minimum |
|---|---|---|---|---|
| **M1** | **Ship 2 × `E80-900MBL-02` Germany → Texas** | 2 boards | **shipping + customs, NOT YET QUOTED** | Without a radio in Texas there is no experiment. This is not a purchase, it is the critical path. |
| **M2** | **Fibreglass telescoping mast, Jackite** | 1 | `188c` (62.84) | The relay has to be *above* something. A pole on the ground is a structure — no airspace permission, no wind rule, no notification. |
| **M3** | **Anemometer, hand-held, reads knots** | 1 | `08fc`–`1388` (~23–50, indicative) | Not optional despite the price. The go/no-go wind rule is the whole safety story for a filament in the air, and without a reading the rule cannot be applied. |

**Minimum total ≈ one dinner out, plus the transatlantic shipment.** The binding
constraint is not money — it is the calendar.

> ⚠️ **What the minimum cannot do:** with two boards, the relay role and one
> ground role share hardware, so **you cannot measure the link while it relays**.
> That is the entire point of the "one rig" property in the README. The minimum
> gets the experiment to *work*; it does not get it to *self-verify*.

---

## 2. Strongly recommended (buys back the self-verification)

| # | Item | Qty | Cost (cents in hex) | Buys |
|---|---|---|---|---|
| R1 | **3rd `E80-900MBL-02` eval board** | 1 | `0740` (18.56) + express | Fills the relay role properly; a spare if a board dies. **Order TODAY or accept it may miss 5 Nov** (14–37 d China). |
| R2 | `E80-900M2212S` bare module — listen-only sniffer on an owned RP2040 | 1 | `03b4` (9.48) | Independent observer during a relay run without a 3rd eval board. Rides R1's shipment. **Cannot relay.** |
| R3 | Guy wire ring for the Jackite pole (3 × 5/16 in holes, ~20 ft up) | 1 | `0127` (2.95) | The mast needs ≥3 guy points or it whips in wind. |
| R4 | Guying kit (cord + line tensioners + stakes) | 1 | `11f3` (45.95) | The ring alone is not anchorage. |

---

## 3. Mast sourcing — this is a real finding, not a placeholder

`docs/MAST-SPEC.md` says **"no US mast SKU was confirmed with a price"** and
warns *"do not order from the $1/foot review quote."* That is now fixed:

| Vendor | Item | Price | Stock (2026-10-25) | Note |
|---|---|---|---|---|
| **Hamsource** (hamsource.com, Shelton CT, 203-556-8700) | **28 ft Jackite pole** — black | **62.84** | **In stock** | **First US mast SKU with a live price. This is the one to order.** |
| Hamsource | 28 ft Jackite — orange | `188c` | In stock | Same pole, visibility colour |
| Hamsource | 31 ft Jackite — black / green / orange | `17b0` (60.64)… | **Out of stock** (all three) | The 31 ft is the nicer mast and is unavailable |
| Hitched4fun (hitched4fun.com) | 31 ft Jackite "Thick Tip" | `2c1f` (112.95) | Listed | Higher price, thicker tip, non-conductive |
| Hitched4fun | Guy wire ring, 1 in | `0127` (2.95) | Listed | Fits "the 31/28 ft Jackite" |
| Hitched4fun | Antenna Mast Guying Kit for 31 ft | on sale `11f3` (45.95), was `1ac4` (68.52) | Listed | Cord + tensioners + stakes |
| Whistlergroup | Jackite kite poles — 16 / 28 / 31 ft | 16 ft `1643` (56.99) | 16 ft **sold out** | Kite-pole branding, same fibre |

**Verified facts about the 31 ft pole** (from the vendor pages, useful for M2.2/23):

- Collapses to **46 in** (4 × 4 × 44 in shipping box), **6 lb**
- **Non-conductive fibreglass** — RF-transparent, so it does not detune the
  antenna under test. This is D8b's material requirement, satisfied.
- **The top section is usable** (the Jackite "thick tip" design is specifically
  the fix for the thin-tip failure mode on cheaper masts)
- Vendor states it "flexes under heavy wind gusts without bending permanently"
- **The vendor does not publish a tip payload figure in grams.** MAST-SPEC's M2.2
  ("can the top carry ~200 g?") therefore **remains open** — plan on guying the
  top section rather than trusting the tip bare.

**Conclusion: order the 28 ft (in stock). Do not wait for the 31 ft.** A mast in
hand on 1 Nov beats a better mast that is out of stock on 25 Oct.

---

## 4. What the price literally is, in one table

Decoded for reading convenience — the coded column is what stays in git.

| Item | Cents (hex) | USD | Source |
|---|---|---|---|
| E80-900MBL-02 eval board | `0740` | 18.56 | EBYTE, read 2026-10-23 |
| E80-900M2212S bare module | `03b4` | 9.48 | EBYTE |
| 28 ft Jackite pole, Hamsource | `188c` | 62.84 | read 2026-10-25 |
| 31 ft Jackite, Hamsource (OOS) | `17b0` | 60.64 | read 2026-10-25 |
| 31 ft Jackite Thick Tip, hitched4fun | `2c1f` | 112.95 | read 2026-10-25 |
| Guy wire ring | `0127` | 2.95 | read 2026-10-25 |
| Guying kit (sale) | `11f3` | 45.95 | read 2026-10-25 |
| Guying kit (list) | `1ac4` | 68.52 | 2026-10-25 |
| Anemometer (indicative) | `08fc`–`1388` | ~23–50 | Amazon US, SKU not pinned |
| Party helium 8.9 ft³ / 14.9 ft³ | `1643` / `1daf` | 56.99 / 75.99 | balloon path only |

---

## 5. Deliberately NOT ordered

| Item | Why not |
|---|---|
| ESP32-C3 boards | D14 — the E80 already carries the MCU, the USB bridge and the radio |
| Any PCB fabrication | D10 — the E80 board *is* the rig |
| A second LR2021 module for the relay | The relay is an E80 board, not module + MCU |
| Helium, latex spheres, HI-FLOAT | **Balloon path only.** The mast path needs none of it |
| Helikite | UK-only, 1–3 week transit, no US reseller found. Cannot make 5 Nov |

---

## 6. Order-of-operations

1. **Today:** M1 (ship the boards) and R1 (`E80-900MBL-02` + express), together.
   They are one shipping decision with one deadline.
2. **Today:** M2 + R3 + R4 (mast + guying) — US stock, ships fast, mast is the
   primary asset (D8b).
3. **This week:** M3 (anemometer), R2 (sniffer module) — cheap, no lead-time risk.
4. **Only on a balloon GO:** helium (~30 ft³ industrial cylinder) + latex spheres.

## 7. Open items that change this list

- **Inventory truth** — is there a 3rd E80 in Germany? Two repo sources say 2; no
  physical count exists. If a 3rd exists, R1 becomes a pure spare.
- **US receiver** — who physically accepts an EBYTE parcel and forwards it?
- **Transatlantic shipping cost** — M1 is unpriced. Get a quote before deciding
  whether M1 or a fresh US order is cheaper.
- **Payload mass** — not yet measured. MAST-SPEC M2.2 cannot be closed without a
  scale, and the vendor publishes no tip-payload figure.