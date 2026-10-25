# Recommendation — postpone the balloon flight; what to do at Exit & Build instead

**Date:** 2026-10-25. **Author:** manager. **Status:** recommendation for operator
decision. **Nothing ordered.**

**Question answered here:** (1) should we postpone the balloon flight to a later
event and wait for the v10 flight boards from `balloon-fresh`? (2) what is the
bare minimum to buy if they still want a bent-pipe LR2021 test at Exit & Build?

---

## 1. The recommendation

**Yes — postpone the balloon. Do not postpone the radio test.**

Those are two different things and the plan currently conflates them.

| | Fly the balloon at Exit & Build | Fly it at a later event |
|---|---|---|
| Flight boards (v10) | **cannot make 5 Nov** (§2) | available |
| Airspace posture | needs the balloon as the *point* | same |
| Measurement rig | inherits an unrouted, unbuilt flight board | built and known |
| Rehearsal | none — first flight IS the event | can be flown before the event |

**Fly the *experiment* at Exit & Build; fly the *balloon* when the boards are
real.** The bent-pipe LR2021 link test is the thing that produces knowledge, and
it does not need a flight board — it needs three radios, a mast and an anemometer.
The balloon is a *lifting asset*, and at Exit & Build it is the least proven part
of the system.

---

## 2. Why the flight boards cannot make 5 Nov — measured, not assumed

This is not a hunch. From `balloon-fresh`, branch `feat/foam-wing-3d`:

**v10 is at "placement approved, routing not started".**

- `docs/fab/v10/GATE-LOG.md` — the operational placement gate (ADR-120 R3) has
  **7 logged rounds**. The final entries are a **REJECTED** routing attempt
  (operator caught, by eye: a `U_C.9` short at 0.000 mm, two dead-end stubs, and
  copper routed **through the F33 module body**) and a directive that **A* with
  vias is the only permitted routing method** — straight/L routing is **banned**.
- `hub_board_v10.kicad_pcb` on that branch: **0 segments, 0 vias**. The board has
  **zero copper.**
- Commit `a7ac6848` — rip-up-and-reroute tooling exists and is **"NOT YET PROVEN
  to improve the result."**
- `tracker/hardware/connectivity/OPEN-ITEMS.md` — open blockers that must close
  before routing can be trusted:
  - `OPEN-16` — ESP32-S3 **GPIO0 pad number unverified** (an earlier guess was
    wrong and had clobbered another net; reverted).
  - `OPEN-E28-EN` — the E28 PA/LNA enables are **unassigned**; blocked on the same
    missing datasheet table.
  - `OPEN-17/OPEN-25` — **the board's last ADC input is contested** between the
    supercap rail monitor and four cut-sense lines. This is **blocking two
    functions that are both in the design.**
  - ADR-129's own note: **ERC 11 errors still outstanding** (7 label_dangling,
    2 pin_not_driven, 2 power_pin_not_driven).
- ADR-031 §59: *"One PCB order. Populate the cheap, robust passives and connectors
  on all N. Ship the exotics as a consigned loose-parts bag with the board order."*
  — the fab order is a *designed* step that has not happened.

**The chain to a flight-ready v10, honestly:**

```
close 3 open pin blockers  →  A*-route 26 nets (method just changed, tool unproven)
  → DRC clean  →  order 4-layer JLCPCB (~3–5 d + 5–10 d shipping, or 24–72 h quick-turn)
  → assemble + staged bring-up per ADR-031  →  bench-verify the radio  →  THEN fly
```

JLCPCB's own published numbers (quick-turn guide; multilayer lead-time update):
**3–5 business days** standard production, **plus 5–10 days** shipping; quick-turn
is 24–72 h at a premium. Even at the fastest tier, **you have ~10 days to the
event and three unclosed pin blockers standing between you and a gerber.** That
is not a schedule, it is a hope.

> **Correction to an assumption in our own plan:** `exit-and-build-balloon` D10
> says *"Do NOT fabricate the v10 hub PCB"* because the E80 board is the rig. That
> was the right call for the E80 path — but it means the repo was **never** on a
> path to having v10 boards at the event. D10 and "wait for the flight boards" are
> mutually exclusive, and nobody had put those two sentences next to each other.

---

## 3. The real blocker the flight board would have solved — and still doesn't

Worth naming, because it undercuts the premise of waiting: **v10 may not fix the
problem that actually stops the bent pipe.**

The bridge constraint in our plan is *"add a bridge mode to the E80 bench
firmware"* — i.e. an MCU must relay UART↔SPI at 2 Mbaud while FLRC-1300 is active,
and **72 MHz is unproven for that** (checklist V8).

**v10 does not retire V8.** v10 is ESP32-**S3** + E28, not an E80. So:

- Building v10 gets you a better *flight* board, not a validated *relay* board.
- The relay throughput question is answered by **measuring it**, on hardware you
  already have, in an afternoon — not by a fab order.

**Conclusion: the V8 measurement is independent of v10.** It should happen at Exit
& Build (or before), with three E80 boards and a mast. Waiting for v10 buys
nothing on this axis.

---

## 4. BARE MINIMUM if they want a bent-pipe LR2021 test at Exit & Build

**Three boards, one mast, one anemometer.** Everything else is comfort.

| # | Item | Qty | Why it is irreducible | Source | Cost |
|---|---|---|---|---|---|
| **B1** | **`E80-900MBL-02` eval board** | **3** — 2 ground + 1 relay | One radio per ground node plus one in the air. With 2 you cannot measure while relaying. | ✅ **RobotShop/Botstore, in stock, US-fulfilled**, SKU `RM-BOTS-1GP`, §8 of PURCHASE-PLAN | `0758` each |
| **B2** | **Fibreglass mast** (Jackite 28 ft, in stock) | 1 | The relay must be *above* something. A mast is a structure → **no airspace permission, no notice, no wind rule.** | ✅ Hamsource, in stock, §3 of PURCHASE-PLAN | `188c` — *do not* re-buy if already owned |
| **B3** | **Anemometer, knots** | 1 | The go/no-go wind rule is the entire safety case for a filament in the air. Without a reading the rule cannot be applied. | Amazon US | ~`08fc`–`1388` |

**Plus, zero-cost and already in inventory:** 2 laptops, 2 USB cables, the Dyneema
line and anchors, and the ground power. **No helium, no envelope, no flight board,
no PCB order.**

**Minimum cash: three boards + one mast + one anemometer.** Given the mast is
already owned, that is **three boards and an anemometer** — well under a hundred
dollars, and the boards are **in US stock with a days-long lead time**, so the
order can be placed late and still arrive.

### 4.1 Optional, and only if the measurement must be independent

| # | Item | Cost | Buys |
|---|---|---|---|
| O1 | `E80-900M2212S` bare module + an owned RP2040 | `03b4` | A **listen-only sniffer** — an independent observer logging PER/RSSI/SNR during a relay run. Cannot relay. |
| O2 | Guy ring + guying kit | `0127` + `11f3` | The mast needs ≥3 guy points or it whips. Buy with the mast. |

---

## 5. What the Exit & Build deliverable becomes

**Not** "balloon over obstruction". That claim needs the balloon, a written
landowner permission, a 4-day helium duty cycle and a wind-governed schedule — all
of which survive better at a later event with real boards.

**Instead: "transparent LR2021 bent-pipe relay at a known, stated height."**

That is a smaller, fully-claimable result and it is honest about what was built:

1. **V8 answered** — can the STM32 relay UART↔SPI at 2 Mbaud with FLRC-1300
   active? Measured, not assumed. (This is the number the whole architecture
   rests on, and it is currently unknown.)
2. **The bent pipe works** — laptop A → E80 → air → E80 → air → E80 → laptop B,
   FIPS above it, opaque frames through it.
3. **The A/B relay delta** — same link, with and without the relay board in
   circuit, at a measured height. This is the measurement that makes the mast
   worth having.
4. **A rig that is one rig** — the board that measures is the board that relays,
   so the numbers cannot disagree with each other.

And **the balloon becomes the later event's headline**, with v10 flown, with
rehearsal behind it, and with the relay already proven so a failure on the day is
a balloon failure — a single, clean, debuggable cause instead of an untested board
and an untested relay failing together.

---

## 6. Costs of this recommendation, stated plainly

- **The headline demo gets smaller.** No balloon at Exit & Build. If the
  organisers want a *balloon*, this is a downgrade and they should say so.
- **It concedes the event is a bench, not a flight.** The plan already admitted
  this at D7 (*"fly the relay only where the ground path is obstructed"*) — a mast
  at 28 ft cannot reach that regime anyway, over a 6 m cedar canopy.
- **The postponed event still has to be chosen and staffed.** "Later" is not a
  date. v10 also still needs the three open blockers closed before it is
  orderable — that work is the same work whether or not we fly in November.

---

## 7. Decision requested

1. **Postpone the balloon flight?** (recommended: yes)
2. **Run the bent-pipe LR2021 relay test at Exit & Build instead?** (recommended: yes)
3. **Order 3 × `E80-900MBL-02` from RobotShop/Botstore + the anemometer now?**
   (recommended: yes — in US stock, cheap, arrives in days, and V8 is the unknown
   the whole architecture rests on)
