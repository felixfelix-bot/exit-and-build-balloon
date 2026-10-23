# Outbound messages — DRAFTS, not sent

**Status: NOT SENT.** These are staged for operator review.

The operator's instruction (2026-10-23): *"Please don't send this yet. Document it
on the default branch. I will ask a friend for approval before we send this."*

So: both messages below are **drafts awaiting approval**. Nothing has been sent,
no account has been created, and no vendor has been contacted.

---

## Draft 1 — Helikite quote request

**To:** `info@helikites.com`
**Method requested by operator:** via `cashu.email`
**Status:** **BLOCKED** — see §3

**Subject:** Helikite quote — small payload, 150 ft tether, US shipping

> Hello,
>
> I'm planning a small tethered radio-relay demonstration in Texas in early
> November and would like to quote a Helikite.
>
> 1. **Which model** is the smallest that will lift a **sub-200 g payload** on a
>    **150 ft tether**, and hold altitude in a **6–9 knot** wind?
> 2. **Price**, and what is included (kite, line, anchor, any rigging)?
> 3. **Shipping to a US address (Texas).** Do you have a **US warehouse or US
>    reseller**, or is it shipped from the UK? What is the realistic **transit
>    time** including customs?
> 4. Do you have a **lead time** you can commit to for delivery before
>    **5 November 2026**?
>
> If UK shipping is the only route and transit is more than about five business
> days, that's useful to know plainly — I'll plan around a different asset.
>
> Thank you,
> Felix

**Why the last line is there:** it invites the honest "no" instead of a
best-case quote. A vendor who knows you'll walk will tell you the real transit
time.

---

## Draft 2 — Airspace / permission message to the organiser

**To:** the Exit & Build organiser (via the operator's own channel — **not** an
agent-sent email)
**Status:** **DRAFT — awaiting the operator's friend's approval**

> We're planning a tethered radio-mesh demo at the ranch, 5–8 Nov, **≤150 ft AGL**.
>
> Because the balloon is **under 6 ft diameter**, it falls outside **14 CFR Part
> 101 Subpart B** — so the five-mile airport rule does not apply (the nearest
> strip, 20TS Bains Private, is 3.4 mi), and **no FAA notice or filing is
> required.**
>
> Two things I need from you:
>
> 1. **Written landowner permission** to anchor a tether on the property for the
>    four days.
> 2. **Confirmation of whether anyone has already coordinated airspace.** If
>    you're flying drones at the event you probably already have a contact — I'd
>    like the tether line included in that brief, because a Dyneema line is
>    nearly invisible to a drone camera.
>
> If either of those is difficult, I have a **mast-based alternative that needs no
> airspace permission at all** and still delivers the relay demo — so this is not
> a blocker either way.

**Why the closing line matters:** it gives the organiser a cheap "no". Presenting
only the balloon version makes the permission request sound like a hard
dependency, which invites either a hasty yes or an awkward stall. Offering the
mast up front makes the request low-stakes and easier to answer honestly.

**Why the ≤6 ft constraint is stated up front:** it is the entire basis of the
no-filing claim. If anyone later wants a bigger balloon the claim evaporates, so
the constraint needs to be on the record *with* the claim.

---

## 3. Why Draft 1 could not be sent

The operator asked for the Helikite enquiry to go out via **cashu.email /
nomail.name**. Three blockers on this host:

| # | Blocker | Evidence |
|---|---|---|
| 1 | **Session cookie expired** | `GET /api/auth/me` → **HTTP 401 `{"error":"Unauthorized"}`** with `~/.nomail_cookies` |
| 2 | **The nsec is missing** | `~/.nomail_nsec` does not exist (only the cookie file at `~/.nomail_cookies`, 131 bytes). Re-auth needs the nsec and there is no copy on this host |
| 3 | **`nak` is not installed** | `command -v nak` → not found; `~/go/bin/nak` absent. The auth flow signs the challenge with `nak event --sec <nsec>` |

The helper `~/.hermes/profiles/manager/scripts/wa_mail_watch_nomail.py` documents
the intended flow (`~/.nomail_nsec` + `nak`) but cannot run without items 2 and 3.

### To unblock, the operator needs to provide ONE of:

- **(a)** the `nsec` (or a restored `~/.nomail_nsec`) **and** install `nak`
  (`go install github.com/fiatjaf/nak@latest`), then the draft can be sent for
  100 sats of Cashu postage via `POST /api/send`; **or**
- **(b)** send it from the operator's own mail client — the text above is final
  and copy-pasteable.

**Note on deliverability (from the `nomail-cashu-email` skill):** both
`nomail.name` and `cashu.email` are on **disposable-email blocklists**. That
mainly affects *signup forms*; outbound mail to a real business address should
deliver, but if the vendor's spam filter rejects it, route (b) is the fallback.
Worth knowing before blaming the vendor for not replying.

---

## 4. Also not sent

- No order has been placed with EBYTE or any other vendor.
- No account has been created anywhere.
- No FAA contact has been made.
- The airspace message has **not** gone to the organiser.

Everything above is a draft. The operator gates both messages.
