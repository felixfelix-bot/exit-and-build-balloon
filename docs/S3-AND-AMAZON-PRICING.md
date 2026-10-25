# Two questions answered — why not S3, and is Amazon cheaper

**Date:** 2026-10-25. Companion to `docs/SOURCING-CHEAPEST-ONTIME.md`.

---

## Q1 — "Why not S3?"

Because **the S3 does not do the job either** — and the S3 belongs to a *different*
part of this project than the one that is blocked.

### First, the numbers we actually have

`balloon-fresh` ADR-026 records the **measured** radio-layer throughput at FLRC
2600 kbps, 1000/1000 packets verified:

| MCU | Throughput | % of air rate |
|---|---|---|
| RP2040 (Pico SDK, batched SPI) | **1377 kbps** | 54% |
| ESP32-C3 (ESP-IDF, raw SPI) | **838 kbps** | 33% |

RP2040 is **64% faster** than the C3 at the radio layer. The reason is
architectural, not clock speed:

1. **Batched SPI** — the RP2040 builds a whole multi-byte transaction in one DMA
   buffer (NSS low → wait BUSY → opcode+payload → NSS high). No per-byte gaps.
2. **Nothing else running** — the RP2040 runs *only* the radio stack. No WiFi/BT
   stack stealing cycles, no RTOS scheduling jitter.
3. **Lower IRQ latency** — bare-metal IRQ beats preempted FreeRTOS dispatch.

### So why is S3 not the answer to the relay problem?

Three separate reasons, and the first one is the decisive one:

1. **An ESP32 does not answer V8 at all.** V8 is *"can the **STM32F103** relay
   UART↔SPI at 2 Mbaud while FLRC-1300 is active?"* Swapping in an S3 replaces the
   subject of the question. You would learn how fast an S3 is — a fact we do not
   need — and still not know whether the E80 board can be the relay. That is the
   entire reason the E80 purchase exists.
2. **The S3 is already spoken for.** ADR-028 lists it as the *future migration
   target* for the application MCU (more GPIO, more RAM, 240 MHz) — not the radio
   processor. The radio processor in this architecture is the **RP2040**, chosen
   precisely because it measured faster than an ESP32. If you want a faster radio
   path than the C3, **the answer on the evidence is RP2040, not a faster ESP32** —
   and we already own two of those.
3. **An ESP32 in the path reintroduces the thing we removed.** The C3 left the BOM
   because the E80 already carries an MCU, a USB bridge and a radio. Putting an S3
   in front of the E80 spools the same "second MCU + second toolchain" cost back
   in, for a measurement it cannot produce.

**Where the S3 *would* legitimately go:** if you decide the relay should be
ESP32-based rather than STM32-based — i.e. you abandon V8 and accept a different
architecture. That is a different project decision, not a sourcing optimisation,
and it should be made explicitly rather than slipped in through a BOM line.

> **Consistency check on our own recommendation:** this is why the ESP32-C3 boards
> on the buy list are justified **only as an SWD probe**, never as the relay. If
> they drifted into being "the relay host", they would be answering a question we
> did not ask. The README says so; this file is the reasoning behind it.

---

## Q2 — "Are the parts you found cheaper than on Amazon?"

**Split answer: the E80 is a RobotShop-only part (Amazon is not a real option), and
on the commodity lines Amazon is often *cheaper* than the vendors I named.** I was
optimising for *US-domestic and definitely-arrives*, not for the last dollar.

### Line by line

| Line | My vendor | Amazon reality | Verdict |
|---|---|---|---|
| **E80-900MBL-02 ×3** | RobotShop $18.80 | CDEBYTE storefront lists an E80 item, **no price, no ship date, reads as a redirected variant page** | **No real Amazon option.** RobotShop stands |
| **ESP32-C3 dev board ×2** | Adafruit ~$10 ea → ~$20 | **$9.99 for 2 (AITRIP)** · $12.99 for 2 + 2 expansion · catalogue price **~$3 each** | ⚠️ **Amazon is cheaper — by ~$10–14** |
| SWD wire + jumpers | Adafruit ~$14 | commodity; on Amazon typically ~$8–10 for a 40-pin Dupont set + hookup wire | ⚠️ **Amazon likely cheaper** |
| **Mast 28 ft** | Hamsource $62.84 | not a commodity Amazon item | **Hamsource stands** (in stock, US) |
| Guy ring $2.95 · Guying kit $45.95 | Hitched4fun | not on Amazon | **Hitched4fun stands** |

**Revised basket if you take Amazon on lines 2–3:** ≈ $202 → **≈ $188**. A ~$14
saving, and it costs you vendor certainty on two consumable items.

### The one place you should *not* chase the cheapest price

**Do not buy the E80 from a cheaper Chinese marketplace listing.** The $13–14
AliExpress/Alibaba boards are real and genuinely cheaper. They also add 7–15 days
transit plus customs, and at 10 days out that is the difference between having a
board and not having one. **The 24-cent premium (RobotShop over EBYTE direct) and
the ~$5/board premium (RobotShop over AliExpress) is buying the calendar, not the
board.** That is the cheapest thing on this list per unit of risk removed.

### What I am *not* claiming

I could **not** read live Amazon prices programmatically — every amazon.com search
and product fetch returned a bot-wall stub (2.6 KB, no price fields) and the
`dp/` page returned no content. **The Amazon prices above come from search-result
snippets, not from a page I verified myself.** Treat them as indicative. If you
want the last $14, open the two product pages in a browser and compare — that is
five minutes and it is the only way to be sure.

---

## Bottom line

- **S3: no.** It does not answer V8, it is architecturally the *application* MCU,
  and the measured evidence says the faster radio path is RP2040 — which we own.
- **Amazon: cheaper on the commodities, not available for the E80.** Switching
  lines 2–3 to Amazon saves ~$14. Keeping RobotShop for the E80 is not a price
  decision; it is the only decision that arrives.
- **Unchanged:** the mast and rigging vendors stand, and #1 (E80 ×3, RobotShop)
  remains the line to order first.
