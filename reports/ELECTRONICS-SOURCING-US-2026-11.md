# Electronics sourcing — US, Exit & Build 6 (Nov 2026)

**Retrieved:** 2026-10-23 by direct `curl` from this host. **No purchase made, no
account created** (D11).
**Method:** Shopify `products.json` for the EBYTE official store (machine-readable
price + variant + stock), plain HTML for vendor pages, `findchips` for
distributor stock. Every URL below was fetched and its HTTP status recorded —
see §10 for the log.

> **Prices move.** A price is quoted only where it was read from a live price
> field today. Everything else is marked **UNVERIFIED** with the reason and a
> route to settle it. **A price is not a stock promise** — check stock at order
> time.

---

## 1. The critical item — EBYTE E80 series (LR2021 / LR1121 dev boards)

**VERIFIED: the E80-900M2212S variant exists, at $9.48.** This is the item the
previous sourcing pass died before confirming.

Product (single page carrying the whole E80 variant matrix):
`https://ebyteiot.com/products/ebyte-e80-400m2213s-semtech-multi-band-lora-lr1121-chip-21-5-13dbm-433m-2-4ghz-lora-dual-band-wireless-rf-transceiver-module-副本`
— HTTP **200**, fetched 2026-10-23. (The handle genuinely ends in the CJK
characters `副本`; URL-encode them as `%E5%89%AF%E6%9C%AC` if your client is
picky.)

**The `948` field is $9.48.** Confirmed from the store's own JSON price field
`"price":"9.48"` — the store's currency is USD (its policy pages quote `$`
amounts). Not a cent-value, not a different unit.

| Variant as listed | Variant id | USD | In stock |
|---|---|---|---|
| **`E80-900M2212S(LR2021)`** | **48564857176269** | **$9.48** | yes |
| `E80-400M2212S(LR2021)` | 48564857143501 | $9.48 | yes |
| **`E80-900MBL-02`** (eval board, 915) | **48564857241805** | **$18.56** | yes |
| `E80-400MBL-02` | 48564857209037 | $18.56 | yes |
| `E80-900MBL-01` | 48564857307341 | $18.56 | yes |
| `E80-400MBL-01` | 48564857340109 | $17.02 | yes |
| `E80-900M2213S` (LR1121) | 48564857274573 | $7.35 | yes |
| `E80-400M2213S` (LR1121) | 48564856848589 | $7.35 | yes |
| `E80-900M2212S + TX2400-JKS-IPX20 + TX433-JKS-IPX20` bundle | 48564858126541 | $12.50 | yes |

**Reading the matrix correctly (this matters for V0.2 in the checklist):**

- `…M2212S` = **LR2021**; `…M2213S` = **LR1121**. They are *different chips* with
  different datasheets. The repo's bench inventory is LR2021, so order the
  **2212S** part if matching inventory matters.
- `…M2212S` module is **$9.48**; the `MBL-02` **eval board** that carries it is
  **$18.56**. The board is what you want for a bench bring-up; the bare module is
  what you want as a spare.
- `-900` and `-400` denote the sub-GHz band option (850–930 vs 410–493 MHz).
  **D2 flies 915 → order `-900`.**

**Still open (carried from `E80-VERIFICATION-CHECKLIST.md`):** whether the `-900`
board's 2.4 GHz path is populated on the same module footprint, and whether the
E80 has a 2.4 GHz antenna jack. The product page describes dual-band
(410–493/850–930 MHz + 2.4 GHz) but **does not show a connector map** — do not
infer pinout from the listing.

## 2. Lead time — this is the finding that changes the plan

`https://ebyteiot.com/policies/shipping-policy` — HTTP **200**. Verbatim from
the policy:

- **Processing time: 7 working days.**
- **Shipping time: 7–30 working days** by China Post Air Mail.
- "Due to the temporary inability of postal channels to ship to Europe and the
  United States, goods to Europe and the United States will be delivered via
  **Yanwen Express Line**."
- Free shipping applies only to wireless modules over **$89.99**; express
  (DHL/FedEx/UPS) is available at extra cost via a dedicated postage link.
- Max quoted worst case: *"several months … due to … customs clearance."*

**Total 14–37 working days.** From 23 Oct 2026 that lands **≈ 12 Nov – 17 Dec
2026 at the earliest-and-latest** — i.e. **it misses the 5 Nov event.** This is
not a reason not to order (spares and the 300 ft option still want them), but it
**is** a reason the event build must rely on existing inventory (D10: 4× NiceRF
LR2021 already in hand).

**Unless** express is chosen at checkout: express removes the 7–30-day surface
leg but not the 7-working-day processing time, so the realistic express floor is
still ~10–14 calendar days. **UNVERIFIED** — the express rate and transit for
this specific SKU were not quoted without a checkout.

## 3. LR2021 bare chip / dev kit

| Item | Vendor | URL | Status |
|---|---|---|---|
| LR2021 product page (chip + dev-kit family) | Semtech | https://www.semtech.com/products/wireless-rf/lora-plus/lr2021 | **HTTP 200** — page exists, **no price published** |
| LR2021 distributor stock & pricing | Findchips aggregator | https://www.findchips.com/search/LR2021 | **HTTP 200** — result page renders **0 authorized / 0 independent** distributor rows for the bare part |
| LR2021 at DigiKey | DigiKey | `https://www.digikey.com/en/products/result?keywords=LR2021` | **HTTP 403 — blocked to automated fetch.** Cannot verify price or stock. Do not quote. |
| LR2021 at Mouser | Mouser | `https://www.mouser.com/c/?q=LR2021` | **connection failed (HTTP 000)** from this host. Cannot verify. |

**Conclusion: LR2021 has NO verified US distributor price today.** The chip is
announced and has a product page; distribution stock did not appear in the
aggregator. **Do not plan to buy LR2021 modules for this event** — the four
NiceRF LR2021 modules in inventory (D10) are the build. If a spare is mandatory,
the E80-900M2212S above ($9.48) is the verified route, with the lead time in §2.

**UNVERIFIED:** NiceRF `LoRa2021` module price. `https://www.nicerf.com/` returns
HTTP 200 but product pages return **HTTP 403** to automated fetch. Route: the
NiceRF contact form / sales email on the site, or a reseller quote. **No price
invented here.**

## 4. EBYTE E28-2G4M27S (2.4 GHz, SX1281) — verified

Same store, product page:
`https://ebyteiot.com/products/ebyte-e28-series-sx1281-lora-module-2-4ghz-rf-transceiver-lora-spread-spectrum-smart-home-lora-wan-parking-sensor-module-rohs`
— HTTP **200** via the store JSON API.

| Variant | Variant id | USD | In stock |
|---|---|---|---|
| **E28-2G4M27S** | **48527944089805** | **$8.18** | yes |
| E28-2G4M20S | 48527944122573 | $7.42 | yes |
| E28-2G4M12S | 48527943991501 | $5.40 | yes |
| E28-2G4M27S + TX2400-JKS-IPX20 | 48527945400525 | $9.69 | yes |

Inventory already holds **3× E28-2G4M27S** — this row is a *spare* line, not a
requirement.

## 5. ESP32-C3 boards

| Item | Vendor | URL | Status |
|---|---|---|---|
| ESP32-C3 dev boards (search: DevKitM-01, STEMMA QT board, DevKit-RUST-2) | Adafruit (US) | https://www.adafruit.com/search?q=esp32-c3 | **HTTP 200**, prices rendered on page (from $4.50; boards $9.95–$24.99) |
| ESP32-C3 stock | PiShop.us (US) | https://www.pishop.us/ | **HTTP 200** (storefront); product-level price **UNVERIFIED** |

**Buy zero.** Inventory has **20× ESP32-C3 Mini V1** (D10). This row exists only
so a dead board does not stop the build; any US next-day source is fine.

## 6. Antennas (915 and 2.4 GHz)

**Correction to the brief:** the collection URLs in the task
(`…/collections/antenna-868-915mhz` and `…/collections/antenna-2-4g`) are
**HTTP 404** as written. The live collections are:

| Collection | URL | HTTP |
|---|---|---|
| 868/915/433 MHz antennas | https://ebyteiot.com/collections/antenna868-915-433mhz | **200** |
| 2.4 GHz antennas | https://ebyteiot.com/collections/antenna2-4g | **200** |
| Lightweight antenna series | https://ebyteiot.com/collections/lightweight-iot-antenna-series | **200** |
| RF modules (all) | https://ebyteiot.com/collections/rf-module | **200** |
| LoRa modules | https://ebyteiot.com/collections/lora-module | **200** |

**Prices not quoted** — the collection pages list the SKUs but the price read
was not done per-SKU, and the repo already has wire-dipole antennas. What the
design actually needs (from `shopping-list.md` §6): **2.4 GHz λ/2 = 3.1 cm** and
**915 MHz λ/2 = 16.4 cm**, lightweight, SMA. For 150 g of payload, **wire
dipoles made in-house are lighter than any cased antenna** — this row is a
convenience purchase, not a requirement.

**AliExpress route — DEAD as written:** `https://cdebyte.aliexpress.com/store/2077046`
redirects to `https://www.aliexpress.com/s/error/404`. The store id may have
moved; **do not cite it.** Use `ebyteiot.com` (the official store) instead.

## 7. LiPo, protection, JST-PH

| Item | Vendor | URL | Status |
|---|---|---|---|
| 1S LiPo cells + protection boards | Adafruit (US) | https://www.adafruit.com/search?q=lipo | **HTTP 200**, prices on page — **specific cell not selected** |
| JST-PH connector kit | Adafruit (US) | https://www.adafruit.com/search?q=jst-ph | **HTTP 200**, prices on page |
| Handheld anemometer | Adafruit (US) | https://www.adafruit.com/search?q=anemometer | **HTTP 200** — but Adafruit does not stock a handheld cup/vane anemometer; **this is the wrong vendor for that item** (see `HELIKITE-AND-TETHER-SOURCING-US-2026-11.md` §6) |

**Note:** if D12 (power up the tether) is adopted, the **on-payload LiPo becomes
a backup, not the primary** — the flight battery only has to carry the payload
through a tether break, not through 96 h. That reduces the LiPo requirement to a
small buffer cell.

## 8. What this changes in the BOM

1. **E80-900MBL-02 at $18.56 is verified and cheap.** Order 2 if ordering at all.
2. **It will not arrive before 5 Nov on standard shipping** (§2). The bench and
   the event run on inventory (D10). The order is for the *next* iteration.
3. **2-conductor tether cable, locking connectors and an on-payload 12 V→3.3 V
   regulator (D12) have no verified US link yet** — see
   `HELIKITE-AND-TETHER-SOURCING-US-2026-11.md` §5. Marked UNVERIFIED rather
   than guessed.

## 9. Not purchased, not ordered

No order was placed. No account was created. Prices are read-only observations.

## 10. HTTP verification log (2026-10-23)

| URL | HTTP |
|---|---|
| `ebyteiot.com/products/…-副本` (E80 matrix) | 200 |
| `ebyteiot.com/collections/rf-module` | 200 |
| `ebyteiot.com/collections/lora-module` | 200 |
| `ebyteiot.com/collections/antenna868-915-433mhz` | 200 |
| `ebyteiot.com/collections/antenna2-4g` | 200 |
| `ebyteiot.com/collections/lightweight-iot-antenna-series` | 200 |
| `ebyteiot.com/policies/shipping-policy` | 200 |
| `ebyteiot.com/collections/antenna-868-915mhz` (as briefed) | **404** |
| `ebyteiot.com/collections/antenna-2-4g` (as briefed) | **404** |
| `ebyteiot.com/products/e80-900m2212s` (guessed slug) | **404** |
| `cdebyte.aliexpress.com/store/2077046` | 200 → **AliExpress 404 page** |
| `semtech.com/products/wireless-rf/lora-plus/lr2021` | 200 |
| `findchips.com/search/LR2021` | 200 |
| `digikey.com/en/products/result?keywords=LR2021` | **403 blocked** |
| `mouser.com/c/?q=LR2021` | **000 (no connection)** |
| `nicerf.com` | 200 |
| `nicerf.com/lora-module/lora2021-module.html` | **404** |
| `adafruit.com/search?q=esp32-c3` | 200 |
| `adafruit.com/search?q=lipo` | 200 |
| `adafruit.com/search?q=jst-ph` | 200 |
| `adafruit.com/search?q=anemometer` | 200 |
| `pishop.us` | 200 |
