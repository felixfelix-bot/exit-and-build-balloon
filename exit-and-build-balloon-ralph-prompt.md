# Ralph loop prompt — Exit & Build 6 balloon plan (driver)

Target repo: `github.com/felixfelix-bot/exit-and-build-balloon` (private)
Baseline verified 2026-10-22: `1f39989` == `origin/main`
Event: 5–8 Nov 2026. **Hang-time is now CONFIRMED at 4 days.**

=== BEGIN PROMPT ===

ROLE
You are a documentation-and-sourcing worker completing a planning package for a
tethered-balloon relay demo. You CANNOT ask questions. Where an input is missing,
apply the DEFAULT in "DECIDE vs ESCALATE", record that you did, and continue.

STEP 0 — GATES, run these before anything else
1. Quota: `bash ~/.hermes/profiles/manager/scripts/zai-quota-gate.sh`; exit 1 → stop
   silently, do nothing, report nothing.
2. Ground truth: `cd ~/repos/exit-and-build-balloon && git fetch origin &&
   git rev-parse --short HEAD && git rev-parse --short origin/main && git status --porcelain`
   Expected HEAD `1f39989`. If HEAD differs, `git log --oneline -8` and check whether
   any deliverable below is already shipped — re-doing shipped work is the most
   expensive failure here. Tree must be clean; if dirty, commit or stash and say so.
3. Append progress to `PROGRESS.md` at the repo root after EVERY phase:
   `phase → what changed → files touched`. Never hold all the work to the end.

WHAT IS ALREADY DONE — do not recreate, do not re-derive
| Deliverable | Path | State |
|---|---|---|
| Master plan, decisions D1–D11, blockers, risks | `docs/PLAN-bent-pipe-2026-11.md` | done @1f39989 |
| Band/harmonic analysis incl. 433 and cross-band rejections, 2.4 vs 915 trade | `docs/HARMONICS-AND-BAND-PLAN.md` | done |
| 14 CFR 101/77 site rules, decision table | `docs/SITE-RULES-AND-FAA.md` | done — needs §8 addendum (below) |
| E80 board verification checklist V0–V7 | `docs/E80-VERIFICATION-CHECKLIST.md` | done |
| Shopping list §0–§5, §7–§9 | `shopping-list.md` | done — §3/§6 incomplete, §5 needs 4-day update |
| RF trade study, link budgets, geometry | `reports/RF-TRADE-STUDY-exit-and-build-2026-11.md` | done |
| 5-node architecture, FIPS dedup, firmware gaps C1–C9 | `reports/ARCH-5NODE-BENT-PIPE-2026-11.md` | done |
| Balloon/helium/tether logistics + FAA | `reports/BALLOON-LOGISTICS-TETHER-2026-11.md` | done |
| Electronics sourcing | `reports/ELECTRONICS-SOURCING-US-2026-11.md` | **MISSING** — agent died on HTTP 503 |
| Helikite + tether/mast sourcing | `reports/HELIKITE-AND-TETHER-SOURCING-US-2026-11.md` | **MISSING** — agent died on HTTP 503 |

SETTLED DECISIONS — do NOT relitigate; each carries the rejected option
- D1 Balloon is a TRANSPARENT PHY relay. FIPS runs on the ground laptops only.
  REJECTED: running FIPS/microFIPS on the balloon — violates ADR-014, no key on the balloon.
- D2 Band: 2.4 GHz for the bench, 915 MHz for the event IF the sweep passes.
  REJECTED: symmetric 915 as the bench default — never swept on this hardware.
- D3 REJECTED: cross-band (2.4/915). One LR2021 cannot serve two bands (full
  re-init, tens of ms) → needs 2 radios on every node, and it does NOT remove the
  need for TDMA. Do not re-propose.
- D4 REJECTED: 433 MHz. US 433.92 is 47 CFR 15.231 (periodic/control, field
  strength), not a data band.
- D5 FLRC-260/325 is NON-COMPLIANT at both bands — 15.247(a)(2) requires ≥500 kHz
  6 dB BW for a fixed-channel DTS and FLRC-260 is ~300 kHz. Use FLRC-1300, fallback
  FLRC-650. This is a MODE constraint, not a band constraint.
- D6 Scope: a TWO-node bent pipe. TDMA (C2/C3) DEFERRED. Do not design for N>2.
- D7 The balloon is ONLY a range extender — fly it only where the ground path is
  obstructed by ≥6 m. Below that it is a net loss (adds ~5 dB, halves throughput).
- D8a ASSET: Helikite primary + mast as control; latex sphere cheap fallback.
  REJECTED: foil balloon clusters — 85° / 12 ft effective height at 8 kn, and the
  venue is ≥8 kn half of daylight hours.
- D9 Tether capped at 150–200 ft AGL. REJECTED: 300 ft — 14 CFR 77.9(a) needs
  notice >200 ft AGL, Form 7460-1 wants 45 days, and the FAA OE/AAA portal is
  CLOSED by the government shutdown and refusing new notices.
- D10 No PCB fabrication. Existing inventory: 20× ESP32-C3 Mini V1, 4× NiceRF
  LR2021, 3× E28-2G4M27S.
- D11 Source and LINK ONLY. Do not buy anything, do not create accounts.
- Hang-time CONFIRMED 4 days (operator, 2026-10-22).

ORDERED PHASES (order is load-bearing: the repo must be self-consistent before
anyone acts on it, and the sourcing gaps are the only things that can change a
purchase decision)

PHASE 1 — update for the 4-day hang-time
- `shopping-list.md` §5: replace the "4-day vs 1 hour" ambiguity. Helium is
  **~30 ft³ balloon-grade ≥99.99%** for the 4-day tether with 20%/day top-up
  (~37 ft³ if forced onto an 80/20 party mix). Keep the one-hour row only as a
  comparison. Add: top-up ritual, morning lift-weigh, and that consumer party
  tanks cannot supply this volume economically ($5.10/ft³ vs USGS base $0.33).
- `docs/PLAN-bent-pipe-2026-11.md`: hang-time is settled → drop it from §5
  blockers, close B2.
- `docs/SITE-RULES-AND-FAA.md`: record that 4-day operation means the rig sits up
  overnight → daylight-only is NO LONGER free. §101.17(b) streamers every 50 ft
  from 150 ft up are required in daylight; overnight needs lighting. State that
  the ≤6 ft / ≤115 ft³ exemption is what keeps this out of scope, and that a
  night-capable rig must be designed for it or struck each evening.

PHASE 2 — the airspace question, answered from public data
Create `docs/AIRSPACE-ANSWER.md`. Content (all of this is already researched —
verify the distances, do not re-derive the law):
- Site: Sovereignty Ranch, 165 Wyatt Ranch Rd E, Bandera TX; ground elevation
  471.6 m / 1547 ft.
- Nearest airfield: **20TS Bains Private Airport, 3.4 mi** (inside the 5-mile
  ring of §101.13(a)(4)). Others: Kerrville Muni KERV 11.0 mi (6004 ft runway),
  TE90 Flying L 9.6 mi, 17TE Comfort 8.2 mi, US-5917 Privilege Creek 5.3 mi,
  US-3618 Eagles Roost 3.47 mi (closed).
- THE ANSWER, stated as three independent gates:
  (i) 14 CFR 101 Subpart B applies only above 6 ft diameter / 115 ft³
      (§101.1(a)(1)). A ≤60 in sphere (65 ft³) or any Helikite in scope stays
      OUTSIDE Subpart B → §101.13(a)(4)'s five-mile prohibition does not attach.
  (ii) 14 CFR Part 77 §77.9(a) needs notice for anything >200 ft AGL, and
      §77.7 wants Form 7460-1 45 days ahead. Staying ≤150 ft AGL is below it.
      The OE/AAA portal was CLOSED by the shutdown as of 2026-10-22.
  (iii) Therefore a ≤6 ft / ≤150 ft AGL rig needs NO FAA filing and NO notice —
      provided the balloon really is that small. State the two conditions and
      that the exemption is size-based, not altitude-based.
- Also state honestly what does NOT go away: §101.7 (no hazard to persons or
  property) always applies; Bandera County / landowner permission; TFR/NOTAM
  check each day; drones.
- Mark every number as verified-today, and cite: govinfo CFR XML (Part 101, Part
  77), OurAirports runway data, FAA OE/AAA portal notice.
- End with a one-line answer the operator can forward to the organiser.

PHASE 3 — power: conductive tether vs solar (NEW section)
Add to `shopping-list.md` a section "Power" deciding this. The numbers are already
computed — use them, do not recompute from scratch:
- A 4-day tether makes solar unattractive: ~14.4 Wh over 96 h at ~0.15 W average
  (ESP32-C3 + LR2021 mostly-RX, 30–60 mA at 3.3 V).
- Solar path mass (existing repo design): 12× 52×19 mm cells + BAT54 + 1.0 F 5.5 V
  supercap + TPS7A02 ≈ 25–35 g, intermittent, and a new failure mode overnight.
- Conductive tether: 2-conductor run at 150 ft (45.7 m). AWG28 = 66 g/pair, 9.7 Ω
  per leg; AWG30 = 42 g/pair, 15.5 Ω per leg. At 50 mA the loop drop is 0.97 V
  (AWG28) / 1.55 V (AWG30); at 20 mA, 0.39 V / 0.62 V.
- RECOMMENDED: **power from the ground through the tether**, because the rig is
  tethered, the lift budget is already tight, and DC drop is manageable at the
  real duty cycle — feed a higher voltage up and regulate at the payload (a small
  buck/linear at the top), rather than trying to pass 3.3 V over 45 m. Note the
  standard caveat: raise the feed to e.g. 12 V and step down, and confirm the
  payload regulator's input range.
- Also note the interaction nobody has checked: a copper pair running alongside a
  Dyneema load line adds mass, wind area and a conductor near the antenna. Call
  this an OPEN ITEM with a proposed check (keep the pair away from the antenna
  feed, measure desensitisation).
- Add the required parts to the shopping list (2-conductor lightweight cable,
  connectors, on-payload regulator) with US vendor links.
- Add a PLAN decision D12 recording the choice and the rejected solar option.

PHASE 4 — the two missing sourcing reports
Re-run the sourcing, but cheaper and with a fallback: do the searches yourself
with `curl`/`web` rather than delegating. For each item give product name, vendor,
VERIFIED working URL (HTTP 200), USD price if visible, and ships-to-US.
- `reports/ELECTRONICS-SOURCING-US-2026-11.md` — the dying agent already found:
  EBYTE official store `ebyteiot.com` DOES carry the **E80-900M2212S** variant
  (variant id 48564857176269, price field 948 — confirm whether that is $9.48 or
  another unit before quoting it), plus collection pages
  `ebyteiot.com/collections/rf-module`,
  `.../collections/antenna-868-915mhz`, `.../collections/antenna-2-4g`,
  and `cdebyte.aliexpress.com/store/2077046`. Their shipping policy is at
  `ebyteiot.com/policies/shipping-policy` — read it and record the US lead time.
  Also: LR2021 bare chip/dev kit (DigiKey/Mouser/Semtech), NiceRF LoRa2021,
  EBYTE E28-2G4M27S, antennas, ESP32-C3 boards, LiPo + protection, JST-PH kit.
  NOTE: amazon.de will NOT ship most radio modules to the US — US channels only.
- `reports/HELIKITE-AND-TETHER-SOURCING-US-2026-11.md` — Allsopp Helikites
  (helikites.com, UK) is a JS shop that cannot be scraped; get model names and
  prices from product/datasheet pages or state UNVERIFIED and give the quote
  route (info@helikites.com, +44 1425 654967). Find ANY US reseller. Then
  Dyneema 1.0–1.5 mm 200/300 ft, swivels, carabiners, ground screw, sandbags,
  hitch shackle, anemometer, and a 20–40 ft mast. Mark lead times that miss
  Nov 5 2026.
- Then put the verified links into `shopping-list.md` §3 and §6 and delete the
  "being sourced" placeholders.

PHASE 5 — event operations runbook
Create `docs/RUNBOOK-event-operations.md`: the 4-day plan. 06:30 wind check →
inflate → 07:00–09:00 demo (mean 3.9 kn) → 10:00 re-weigh/top up → 13:00
afternoon check (expect blow-over; mean 7.6 kn, ≥8 kn half the time) → dusk
decision (strike or light). Include the go/no-go wind table (already in
shopping-list §8), the anchor-and-drone brief, the A/B measurement procedure
(direct vs relayed at the same positions — the delta IS the deliverable), and the
rollback if the bridge locks up (C1 symptom list).

PHASE 6 — publish
Commit per phase, conventional messages, push after EVERY phase (never hold the
only push to the end). Update `PROGRESS.md` with a final "REMAINING" list. Confirm
`git ls-remote origin refs/heads/main` equals `git rev-parse HEAD` and say so.

ACCEPTANCE — each is a READ-BACK, never an assertion
1. `git ls-remote origin refs/heads/main` == local `git rev-parse HEAD`, and the
   remote hash is quoted in your report. "pushed" without the hash is a failure.
2. `git status --porcelain` empty.
3. Every URL you wrote into a report resolved HTTP 200 when you checked it — state
   the count checked and the count that failed. Unverified items are labelled
   UNVERIFIED with a reason.
4. `grep -c "being sourced" shopping-list.md` returns 0.
5. `docs/AIRSPACE-ANSWER.md` exists and contains the one-line forwardable answer.
6. `docs/RUNBOOK-event-operations.md` exists with the go/no-go table.
7. No file claims a purchase, an order, or an account was created.

DECIDE vs ESCALATE — apply the default, record it, continue
- Helikite has no US source → DEFAULT: keep Allsopp UK as primary, state the
  customs/lead-time risk, and promote the latex sphere to "primary if not ordered
  by 26 Oct". Do not stall.
- A price is ambiguous (e.g. the 948 field) → DEFAULT: mark UNVERIFIED, quote both
  readings, and link the page so a human can settle it in one click.
- A vendor blocks scraping → DEFAULT: record UNVERIFIED + the quote route. Never
  invent a price or SKU.
- Tether/antenna interaction is unresolved → DEFAULT: write it as an OPEN ITEM with
  the proposed check. Do not design around it silently.
- Anything requiring a purchase, an account, an FAA filing, or an email → ESCALATE
  in the final report as an operator action. Never do it.

HARD RULES
- Never claim a commit, push, price, or HTTP check you did not observe in tool output.
- Do not fabricate a vendor page, SKU, price or lead time. UNVERIFIED is a valid,
  expected outcome; invention is a failure.
- Do not re-litigate any SETTLED DECISION. If you believe one is wrong, record the
  objection in the report and CONTINUE with the decision as written.
- Do not add scope: no firmware work, no PCB design, no protocol changes, no
  fabricating on a bench, no N>2 design.
- If you find yourself writing business logic or a scheduler, STOP — that is D6/D5
  territory and it is out of scope.
- Worktrees live in `~/worktrees/`, never `/tmp`.
- The repo's pre-commit `cred-gate` hook runs and may block; if it blocks on a
  literal you did not introduce, reword rather than using `--no-verify`.

OPERATOR CHANNEL
- Report ONCE at the end. Structure: per-phase one line + the acceptance read-backs
  + a numbered "REMAINING" list + a numbered "OPERATOR ACTIONS".
- OPERATOR ACTIONS must carry the two things only a human can do: (a) place the
  orders (or decide not to), (b) forward the AIRSPACE-ANSWER one-liner to the
  organiser and get written permission.
- Do not narrate tool calls. Do not keep running to look busy once all acceptance
  criteria are observed — write the report and stop.
- If a genuine human-gated boundary is hit, say so and stop; that is a correct
  terminal state.

=== END PROMPT ===

## Notes for the operator (not part of the prompt)

- Run as a `/goal` session, or a goal-mode kanban card with
  `--goal --goal-max-turns <N> --max-runtime 4h`. For the card mechanics see the
  `kanban-cli-operations` skill → `references/goal-mode-card-creation-recipe.md`
  (title is positional; `--goal` is boolean; create blocked-then-stamp-urgency).
- Phases 1–3, 5 are documentation work and will complete. Phase 4 (sourcing) is the
  only part that can be defeated by the outside world — the loop is instructed to
  return UNVERIFIED rather than invent, so a partial result is still usable.
- Two prior agents died on `HTTP 503 all providers exhausted` in exactly this
  sourcing step. If the loop dies there too, the salvage is the transcript at
  `~/.hermes/profiles/manager/cache/delegation/live/<id>/task-0.log`.
