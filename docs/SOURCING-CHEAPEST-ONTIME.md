# Sourcing study — cheapest option that still arrives for 5 November

**Date:** 2026-10-25. **Question:** find the cheapest options that deliver on time
for the event. **Conclusion up front:** for the E80 board the answer is
**RobotShop, $18.80, in US stock** — but the cheapest *board* is not where the
money is, and this study found a much larger cost item that the previous plan had
priced at zero.

---

## 1. The finding that outweighs every price on this page

**You already own radios that can prove the bent pipe end-to-end, with no E80
purchase at all.**

From the `balloon-fresh` inventory (verified, `docs/HANDOVER-PROMPT.md`):

| Owned | Qty | What it is |
|---|---|---|
| NiceRF LoRa2021 modules | **4×** | LR2021 radio (Semtech LR2021 die) — the **same radio** as the E80's |
| RP2040-Zero + LR2021 rigs | **2×** | assembled, LR2021 over SPI, firmware proven |
| ESP32-C3 Mini V1 | **20×** | already the platform for the LR2021 firmware |

So: **two ground nodes and a relay can be built from 2 of the 4 bare LR2021
modules plus RP2040/ESP32-C3 hosts, costing $0.** The radio link would be the same
radio, the same modulation, the same band — the *relay* would be different silicon.

**Why this does not replace the E80 plan anyway — the honest reason:**

- **V8 would go unanswered.** V8 asks whether the *STM32F103 at 72 MHz* can relay
  UART↔SPI at 2 Mbaud with FLRC-1300 active. A C3/RP2040 relay answers a
  *different* question. Buying the E80 is buying the **answer to V8** — and V8 is
  the unknown the whole architecture rests on.
- The E80 is also the **existing bench platform**, so its firmware work is already
  partly done (LR20xx v1.3.1 driver linked, FLRC linked, 2 Mbaud console).

**Verdict:** the $0 path is a real, cheap *fallback* if the E80 order slips — it
proves the bent pipe, it just does not prove the STM32. Keep it in your pocket.
It is not the recommendation, because V8 is the point.

---

## 2. E80-900MBL-02 — every channel, priced and timed

| Channel | Unit | Ships from | Lead time | Total for 3 | Arrives for 5 Nov? |
|---|---|---|---|---|---|
| **RobotShop / Botstore** | **$18.80** | **US** (marketplace, US-fulfilled) | days | **$56.40** | ✅ **yes** |
| EBYTE official (ebyteiot.com) | $18.56 | China | 7 d processing + 7–30 d transit | $55.68 + express | ❌ **no** — 12 Nov–17 Dec |
| EBYTE / CDEBYTE on amazon.com | varies, listing exists | China or 3P | not stated | ? | ⚠️ **unverified** — no stock/date shown |
| AliExpress (Ebyte store) | **~$13–14** for the -01 | China | 7–15 d + customs | ~$40 | ❌ **no** |
| Alibaba (Ebyte) | $13.83 @ 2–99 pcs | China | MOQ 2, export docs | ~$28 + | ❌ **no** |
| cdebyte.com (factory) | quote-only | China | "send inquiry" | — | ❌ **no** |
| Semtech **LR2021EVK1XCS1** (2 radios, 915) | **$130** | US distributors | **11 wk lead**, 0 in stock | — | ❌ **no** |
| Semtech LR2021EVK2XCS1 | $152.62 | DigiKey | **0 stock**, next 04-Jan-2027 | — | ❌ **no** |
| **Seeed LR2021 kit US915** | **$99** | **US warehouse** | 2–3 d UPS 2nd Day | $297 | ✅ yes, but see below |

### Verdict on the E80

**RobotShop at $18.80 is both the cheapest *and* the only one that arrives.** It is
24 cents above EBYTE direct — and EBYTE direct misses the event by one to six
weeks. The China channels are genuinely cheaper per unit ($13–14) and genuinely
useless here.

> ⚠️ **Not verified, and not pretended otherwise:** the amazon.com CDEBYTE
> storefront (seller `A2UAWLKK6DOFSC`) does list an "E80-…(E80-900MBL-02)" item and
> asks to "check each product page for other buying options" — i.e. **it is
> probably a redirected/variant listing, and no price or ship date was shown.** Do
> not count on it. Confirm at checkout if you want to try it; RobotShop is the
> verified path.

### Why Seeed's $99 kit is NOT the answer, despite being US-stock

It is a genuine US-warehouse option that arrives on time — but:

- **$99 vs $18.80** — 5.3× the price, so 3 kits cost **$297** against $56.40.
- It is built around **Wio-LR2021 + XIAO nRF54L15**, not an STM32F103. So it does
  **not answer V8** either — it replaces the very board V8 is about.
- `LR2021EVK1XCS1` (the Wio variant, 2 radios) is **discontinued by Semtech**.

**If the STM32 question matters, $18.80 beats $99.**

---

## 3. Everything else on the list, cheapest that arrives

| Item | Cheapest that arrives | Price | vs alternative |
|---|---|---|---|
| **Mast** — Jackite 31 ft | Hitched4fun, $112.95 | — | ✅ in stock |
| **Mast** — Jackite 28 ft | **Hamsource, $62.84** | **$62.84** | ✅ **cheapest, in stock.** Hamsource's own 31 ft is **out of stock** at all three colours; Whistlergroup's 16 ft is sold out |
| Guy wire ring | Hitched4fun, $2.95 | $2.95 | only US source found |
| Guying kit | Hitched4fun, **$45.95 on sale** (list $68.52) | **$45.95** | the sale price is live |
| **ESP32-C3 dev boards** | Adafruit / SparkFun, ~$10 ea | ~$20 for 2 | US domestic 2–4 d |
| SWD hookup wire + jumpers/headers | Adafruit / SparkFun / Amazon | ~$14 | US domestic |

**Nothing on this list has a cheaper on-time alternative.** These are short,
commodity, US-domestic items where the vendor survey already landed on the low
end.

> ⚠️ **One thing worth checking before you skip it:** the master inventory lists
> **20× ESP32-C3 Mini V1** and **2× RP2040-Zero** already owned. **If those are
> reachable in time, drop line 2 and line 3 entirely — that is ~$34 saved for
> nothing.** They are recorded as being in Germany, which is why they are on the
> buy list; confirm before ordering.

---

## 4. The recommendation: cheapest on-time basket

| # | Item | Qty | Cheapest on-time | Line total |
|---|---|---|---|---|
| 1 | `E80-900MBL-02` — RobotShop/Botstore | 3 | $18.80 ea | **$56.40** |
| 2 | ESP32-C3 dev board — Adafruit/SparkFun | 2 | ~$10 ea | **~$20.00** |
| 3 | SWD harness wire + jumpers/headers | 1 set | ~$14 | **~$14.00** |
| 4 | Jackite 28 ft mast — Hamsource | 1 | $62.84 | **$62.84** |
| 5 | Guy wire ring — Hitched4fun | 1 | $2.95 | **$2.95** |
| 6 | Guying kit — Hitched4fun (sale) | 1 | $45.95 | **$45.95** |
| | | | **Total** | **≈ $202.14** |

**Against a non-optimised basket:** using the 31 ft mast ($112.95 instead of
$62.84, +$50.11) and the list-price guying kit ($68.52 instead of $45.95, +$22.57)
would come to **≈ $274.82** — **$72.68 more for the same experiment.** Optimising
the mast line alone saves a quarter of the budget.

**If the German inventory is reachable:** drop lines 2–3 → **≈ $168.14**.

---

## 5. What could NOT be verified (stated, not hidden)

| Claim | Status |
|---|---|
| amazon.com CDEBYTE listing price / ship date for E80-900MBL-02 | **UNVERIFIED** — listing exists, no price or date exposed to this host |
| RobotShop marketplace line ships from a US warehouse *for this item* | **UNCONFIRMED** — RobotShop runs US logistics and states 24 h handling, and its marketplace terms require US marketplaces to ship duty/tax-free; the per-item ship-from was not readable (Cloudflare 403). **Check at checkout.** |
| Hamsource 28 ft exact delivery time to Austin | **UNVERIFIED** — US domestic vendor in Shelton CT, in stock; transit not stated |
| Anemometer options | **out of scope** — operator instruction: not ordering one |
| Whether the German ESP32-C3 / RP2040 inventory can reach Texas | **UNKNOWN** — would delete line 2 and 3 |

---

## 6. Ordering priority

1. **Line 1 (E80 ×3) — today.** Cheapest that arrives, and the only line that can
   slip. Everything else is domestic.
2. **Lines 4–6 (mast + rigging) — today or tomorrow.** US domestic, and the mast is
   the primary asset.
3. **Lines 2–3 — this week**, after checking whether the German ESP32-C3 boards are
   reachable. If they are, this line is free.
