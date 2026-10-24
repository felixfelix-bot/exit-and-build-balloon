# Mast — spec, sources, and rigging

**Why this document exists:** the mast is now the **primary asset** (D8b), and
until now it had a one-line "20–40 ft, holds ~150 g payload" spec and no vendor.
The whole permission-free argument depends on the mast actually being buildable.

> ⚠️ **Not sourced to a specific SKU.** What follows is a *verified vendor survey*
> with real specs and reachable URLs, not an order. Prices are quoted only where
> read from a live page; everything else is marked **UNVERIFIED** with the reason.

---

## 1. Why the mast is the primary

Repeating the load-bearing point, because everything below follows from it:

| Regime | Balloon | Mast |
|---|---|---|
| 14 CFR 101 Subpart B | applies >6 ft / >115 ft³ | **does not apply — not a balloon** |
| 14 CFR 77 notice (>200 ft AGL) | applies above 200 ft | n/a below 200 ft |
| Landowner airspace permission | required | **not required** |
| §101.15 notice / §101.17 streamers / §101.19 deflation device | in scope | **none** |
| Wind go/no-go rule | governs the demo | **structural only** |

**A mast below 200 ft is an ordinary structure.** No filing, no notice, no
permission, no wind rule. If the organiser cannot grant balloon permission, the
mast demo proceeds unchanged.

---

## 2. Required spec

| Parameter | Value | Why |
|---|---|---|
| **Deployed height** | **30–40 ft** (target 40) | Must exceed the ~6 m (20 ft) cedar canopy by as much as possible. 40 ft gives ~20 ft of clearance; more is better but availability drops |
| **Retracted length** | ≤5 ft | must fit a vehicle |
| **Top-payload capacity** | **≥200 g** comfortably | payload is the **E80 board** (STM32F103 + LR2021 + CH340 + 2 SMA jacks) + feed wire + mount + wind load. **Its mass is NOT yet measured** — weigh it before sizing the mast head |
| **Guy points** | ≥3, at ≥2 heights, below the top section | a 40 ft pole needs support in the upper third or it whips |
| **Wind rating** | **≥25 kn static, guyed** | the balloon's 9 kn rule does not apply, but the pole still has a structural limit |
| **Material** | fibreglass preferred | non-conductive — the payload is a radio, and a metal mast is a detuned antenna next to the antenna under test |
| **Ground mount** | guyed base / drive-on plate | must survive the venue's 7.6 kn mean wind |

> 🔴 **The fibreglass point is not cosmetic.** A metal mast alongside a 915 MHz or
> 2.4 GHz antenna changes the pattern and the impedance. If the only mast available
> is aluminium, that has to be measured for, not assumed away — it becomes a
> **confound in the A/B result** and must be stated in the report.

---

## 3. Verified sources

Fetched 2026-10-23. Status recorded per URL; nothing invented.

| Source | URL | HTTP | What it is | Note |
|---|---|---|---|---|
| **Jackite Inc** (US) | https://www.jackite.com/antenna | **200** | US maker of **fibreglass telescoping poles**, widely used by radio amateurs | **The strongest find.** See §4 |
| McMaster-Carr | https://www.mcmaster.com/telescoping-poles/ | 200 | Industrial telescoping poles | Category page reachable; spec/price not read |
| Amazon US | https://www.amazon.com/s?k=telescoping+mast+pole+40ft | 200 | Generic search | Results not parsed — do not quote a price from this |
| DX Commander | https://dxcommander.com/ | **403 blocked** | Ham antenna masts | Blocked from this host |
| Spiderbeam | https://www.spiderbeam.com/ | **403 blocked** | Fibreglass masts (EU) | Blocked; also EU → lead time |
| SOTABEAMS | https://www.sotabeams.co.uk/masts/ | **404** | Portable masts (UK) | Wrong path; UK → lead time |
| MFJ Enterprises | https://mfjenterprises.com/ | **429 rate-limited** | Telescoping masts (US) | Retry later |
| REI | https://www.rei.com/search?q=telescoping+pole | **000 no connection** | — | Unreachable from this host |

**No US mast SKU was confirmed with a price.** The Jackite page is the best lead;
its products need a targeted fetch or a phone call.

---

## 4. Jackite — what the page actually supports

From https://www.jackite.com/antenna (HTTP 200), the page carries third-party
amateur-radio write-ups, not a clean product table. Verified statements:

- Jackite makes **fibreglass telescoping poles**; two **30 ft** poles are used to
  support a wire receiving antenna.
- Poles **"collapse to around 4 feet in length, and are easily and quickly
  telescoped to full length."**
- Amateur reports reference an **orange 31 ft** pole and a **27 ft** pole
  (the 31 ft tip is thinner than the "platinum" tip variant).
- Cost commentary: **"around $1 a foot"** — i.e. a 30 ft pole is roughly **$30**
  — **as a third-party quote in a review, NOT a Jackite price. Treat as indicative
  only.**
- Rigging precedent on the page: **two 5 ft pieces of 1½ in PVC + a 1½ in cross**
  as a base, with **~2 ft of PVC inside the pole** — a usable mount pattern.

**Route to settle:** fetch a product page directly or call Jackite. The catalog
has a dedicated products section (`/dupont-tyvek`, `/cool-designs`, `/about-…`);
the `/antenna` page is a use-case page, not the shop.

> **Do not order from the "$1/foot" review quote.** It is the only price signal on
> the page and it is second-hand.

---

## 5. Rigging plan (works with any 30–40 ft pole)

Derived from the precedents above plus standard practice:

1. **Base:** drive-on plate or a PVC cross-base (1½ in cross + two 5 ft legs, ~2 ft
   of pole inside the PVC). A vehicle drive-on plate is more robust on caliche.
2. **Guys:** 3 × at the upper third, 1 × at mid. Anchor to ground screws or
   sandbags — **the same anchor hardware listed in `shopping-list.md` §4 can be
   reused**, which is a real saving if the balloon is dropped.
3. **Guy line:** 3 mm Dyneema or better. The mast does **not** have the balloon's
   mass constraint, so here you optimise for strength and abrasion, not grams.
4. **Payload mount:** at the very top, on a non-conductive stub. Keep the antenna
   clear of the pole and of the guy lines.
5. **Cable:** the conductive-tether decision (D12) applies to the mast too —
   ground power up the mast, regulator at the top. Shorter run means **less drop
   than the balloon case**, so the AWG can be lighter or the feed voltage lower.

---

## 6. The measurement consequence — this is the good news

With the mast the A/B becomes **cleaner** than the balloon version:

| Run | What it isolates |
|---|---|
| Ground-to-ground, no mast | baseline |
| Ground-to-ground, **mast at known height** | the effect of height alone, at an exact, stated altitude |
| (if permitted) via balloon | the balloon's contribution over the mast |

**The mast gives an exact altitude number**; the balloon gives an *effective*
altitude that must be measured with a protractor and an anemometer. The mast row
is therefore the more defensible datum, and the headline measurement becomes
**height-vs-performance at a known height** plus the relay delta.

**Record which of these confounds apply:** metal in the mast, guy lines crossing
the antenna's near field, feed cable routing. State them in the report rather
than letting a reader assume an idealised setup.

---

## 7. Open items

- [ ] **M1.** Get a Jackite product page or phone quote: model, length, price,
      shipping to Texas. → *blocks the order, not the plan*
- [ ] **M2.** Confirm top-section payload capacity — can a 30–40 ft fibreglass
      pole carry ~200 g at the tip without guying the top itself?
- [ ] **M3.** Confirm wind rating and decide whether the 3-guy pattern is enough
      for the venue's 7.6 kn mean.
- [ ] **M4.** Decide metal-vs-fibreglass definitively; if metal is the only option,
      add an antenna-pattern caveat to the measurement plan.
- [ ] **M5.** Add mast parts to `shopping-list.md` §3 once M1 resolves.
