# Flag: "512 B gets us the full 2.6 Mbit" conflicts with the repo's own audit

**Date:** 2026-10-25. **Raised by:** operator correction to `docs/S3-AND-AMAZON-PRICING.md`.
**Status: CLOSED 2026-10-25 — see `THROUGHPUT-SETTLED-by-measurement.md`.**

You said the 1377/838 kbps figures are outdated because bumping the packet from
255 to 512 B yields the full 2.6 Mbit. I went to apply that. **The repo says
otherwise, in three independent documents including one that was written
specifically to settle this exact question.** So I am flagging rather than
rewriting — if I just made the edit, I would be overwriting a measured finding
with a claim I cannot find support for.

---

## What the repo concludes

**`docs/FLRC-512B-THROUGHPUT-AUDIT-2026-10-06.md`** — card `balloon/t_6b68897c`,
titled *"FLRC 512 B / 2.6 Mbps — settled"*. Verdict, quoted:

> **The 2.6 Mbps figure is the configured FLRC *air rate*, not delivered goodput.**
> No payload size can make goodput reach it, and a ~2.6 Mbps *goodput* figure is
> not merely unmeasured, it is **impossible under every model below**.

> **The 512 B run does not exist.** Payloads `{16, 64, 128, 192, 255, 256, 300,
> 384, 448, 511}` were measured; **512 was never measured anywhere on disk, and
> cannot be — 511 B is the driver's documented maximum.**

Two in-repo sources fix the 511 B ceiling:

- `lr20xx_radio_flrc_types.h:210` — `pld_len_in_bytes` *"FLRC payload length in byte
  - in [6:511]"*
- `bench_cmd.h:157` — `#define BENCH_START_LEN_MAX_FLRC 511u`, enforced at both TX
  and RX start branches

**The corrected ceiling at 511 B is ~1910 kbps, not 2600** — because the firmware
ships **CR 3/4**, and CR 3/4 costs 4/3 in air time, capping payload rate at
2600 × 3/4 ≈ 1950 kbps. That ~1910 figure agrees to **0.6 %** with an independently
computed on-air figure already in the repo (1921.8 kbps). The audit's own
cross-check, on its own numbers:

> **the ceiling gain from 255 B → 511 B is +2.1 % (1870.9 → 1909.9 kbps), not ~2×.**
> Doubling the payload doubles the air time too; it only amortises the fixed
> preamble/sync/AGC overhead better.

**Best measured sustained figure on disk: 1484.9 kbps** (BR2600, LEN 127, 0.00 % PER,
TX-side limited at ~1487 kbps).

### Two corroborating sources

- `docs/lr2021-flrc-24ghz-datasheet-audit-2026-07-26.md:78` — *"The '2600 kbps'
  figure is the RAW AIR RATE (physical-layer symbol bit rate), **NOT achievable
  goodput**."*
- `docs/P4.1-DMA-CHAINING-ZERO-COPY.md` — *"Throughput is still **air-limited**
  (PHY max ≈ 2600 kbps)"*, and states the LR2021 holds **one** TX packet in its
  FIFO at a time, so there is no free-running packet chain.

---

## Where I think the confusion comes from — and it may be partly mine

The most recent explicit statement I applied, **ADR-026**, is dated **2026-07-29** —
**older** than the 2026-10-06 audit that contradicts it. So you are right that my
quoted table is **superseded**, and I should not have carried it forward as current.

But "superseded" resolves to **1910 kbps / air-limited**, not to **2600 kbps
achieved**. Those are different corrections:

| Claim | Supported by |
|---|---|
| "1377/838 kbps at 255 B" is the current state | ❌ **no** — superseded by later optimisation work |
| "the 255→512 lever is the big win" | ❌ **no** — the audit prices it at **+2.1 %**, and 512 is **not a legal length** (511 max) |
| "full 2.6 Mbps *goodput* is achieved" | ❌ **no source found** — contradicted by 3 documents, one written to settle it |

**My reading:** probably the *air rate* is 2.6 Mbps and the framing got compressed
somewhere — the configured air rate really is 2.6 Mbps. That is true and it is in
the repo. It is just not delivered payload.

---

## What I need from you

One of these, and I will land the edit in the same commit:

1. **A source newer than 2026-10-06** that measures 511 B goodput at (or near)
   2600 kbps — a sweep CSV, a session log, a commit. I will take a measured number
   over a document every time. **This is the fastest close.**
2. **"The audit is wrong"** — then tell me *which* of its three legs fails: the
   511 B driver bound, the CR-3/4 airtime model, or the "air rate ≠ goodput"
   distinction. I will re-derive from there.
3. **"2.6 Mbps is the air rate, I meant the framing"** — then nothing needs
   changing except my wording, and I will say so explicitly.

**Until one of those lands, the S3 answer does not change anyway** — and this is
the part that matters for the purchase decision:

> The S3 argument never rested on 1377 vs 838. It rested on **"an ESP32 does not
> answer V8"**, because V8 asks about the **STM32F103**. Correcting the throughput
> numbers changes the *performance context*, not the *subject of the test*. **The
> comparison table is now marked superseded; the recommendation stands.**

---

## What I am not doing

Not silently overwriting a measured audit with an unsourced figure. Not deleting
the audit's conclusions. Not asserting you are wrong — your correction is right
that my numbers were stale, and the audit itself is now five weeks old and may
itself have been overtaken by the P4.1 DMA work, which it predates.

**The honest state: two repo documents disagree, and I cannot tell from here which
one is current.** That is exactly the kind of thing that should reach you rather
than get resolved by whichever file I happened to read last.
