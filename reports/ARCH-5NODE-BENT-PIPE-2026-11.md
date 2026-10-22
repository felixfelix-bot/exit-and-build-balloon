# 5 Ground FIPS Nodes Through One Transparent Bent-Pipe Balloon

**Date:** 2026-11-01 · **Event:** Exit & Build 6, Nov 5–8 2026, Sovereignty Ranch, Bandera TX (~200 acres, ~0.9 km)
**Status:** Analysis only. No firmware modified, nothing committed.

**Evidence:** `flrc-bench-espidf/main/fips_bridge.cpp`; `FIPS-BRIDGE-STATUS.md`; `RESULTS.md` (2026-06-19/23);
ADR-014, 012, 021, 026; `tracker/firmware/components/tdma/`; `jmcorgan/fips` @ `6c3e1c8` (2026-10-22, v0.6.0-dev),
cloned to `/data/repos/fips-upstream`.

## Bottom line

One balloon, one LR2021, one channel **cannot** isolate five ground nodes. A transparent single-frequency
relay is a repeater inside one half-duplex collision domain. Only a schedule prevents simultaneous
transmission, and the schedule must derive from absolute UTC so the balloon follows it without inspecting
a payload byte.

**Recommended: option (a)** — one shared 2.4 GHz FLRC channel, ground-derived UTC TDMA, balloon relays in a
fixed slot. One relay hop 3–6 ms, ~80 kbps/node usable, ~838 kbps raw channel. No new radios, ADR-014 compliant.

**Highest-risk gap:** the bridge has no concept of *time* or of *radio ownership*. `uartToRadioTask` fires raw
SPI TX with hardcoded 0–3 ms random jitter (`fips_bridge.cpp:106`) while the main task concurrently drives
`standby()`/`startReceive()`/`setPacketReceivedAction()`. Only the SPI *bus* is mutexed (`:76`, `:87`), not the
radio *state machine*. Most likely cause of the documented 3–5 min lockup — and jitter is exactly what TDMA
must delete, not tune.

---

## 1. Options for N=5

### (a) Single shared channel, store-and-forward relay

All six bridges on 2450 MHz / 2600 kbps / +12 dBm (`fips_bridge.cpp:43-44`). The balloon re-transmits what it hears.

**Does traffic traverse the balloon?** Trivially yes — that is the problem. The balloon is a PHY repeater, not a
FIPS hop (it holds no key), so the FIPS link is ground-to-ground and the balloon is a shared-medium amplifier.
Every repeat reaches all five nodes including the originator. On 200 acres with +12 dBm omni dipoles, some pairs
hear each other and some do not: a partial mesh whose edges move with body position — worse than either extreme.

**What breaks.** Collisions. FIPS has no MAC; `docs/design/fips-transport-layer.md:149-153` says it *tolerates*
loss, reordering and duplication rather than preventing them. Five unsynchronised transmitters push collision
probability up as ~N². The only mitigation today is `esp_random() % 3000` (`:106`) — 3 ms against a 15–20 ms
per-packet processing time (`RESULTS.md:197`). Collapse is already visible at N=2: 50% PER at 0 ms spacing,
20 ms needed for 0% (`RESULTS.md:45`). At N=5 unmanaged, expect unusable within seconds.

**Latency.** 255 B @ 2600 kbps = 785 µs air; raw-SPI RX 188 µs (`RESULTS.md:236`); 1200 µs post-TX settle
(`:115`); 0–3000 µs jitter. One hop ≈ **3–6 ms**. Two orders better than ADR-014's 15 ms RadioLib figure — the
raw-SPI path bought that.

**Throughput.** Raw ceiling 838.8 kbps at 0% PER (`RESULTS.md:237`). Across five nodes plus a repeat pass,
~80 kbps/node — ample against ADR-026's "single FIPS link ~9 kbps net" (`026:148`).

**Verdict:** workable **only** with TDMA (§3).

### (b) Cross-band bridge, two RF islands

3 nodes on 2.4 GHz, 2 on 868 MHz; balloon bridges bands.

**Two blockers.** One LR2021 cannot serve two bands at once — two antenna ports, one radio
(`012:11`); a band change is a full re-init costing tens of ms. And cross-island traffic needs a buffer and a
second radio; `fips_bridge.cpp` has no queue at all. ADR-014's crossbar assumes N×LR2021 behind an iCE40/RP2040
(`014:50-82`); this bridge is ESP32-C3 + one LR2021.

**Traversal.** Cross-island: yes, necessarily. Intra-island: no — the balloon is irrelevant and each island
degenerates to (a) with N=3 and N=2.

**What breaks.** Asymmetry. Cross-band peers get a different PHY per direction plus a relay; FIPS path-MTU
converges only after MtuExceeded signalling (`docs/design/fips-mtu.md`), and the 868 path degrades 2.5× faster
(RX active ~2.5 min vs ~5 min, `RESULTS.md:354-357`).

**Verdict:** not achievable on current hardware in four days.

### (c) K independent transparent pipes, one frequency each

Five radios, one per node, one channel each. Private half-duplex channel per node.

**Traversal:** unavoidable — the only option where it is *guaranteed*. No duplicates, no hidden node.

**What breaks.** (i) 5× radio BOM and SPI pin budget; ADR-014 caps the iCE40 UP5K crossbar at 6 radios
(`014:63`) — zero headroom. (ii) A fixed all-pipes cross-connect fans every ingress frame to the other four =
**5× airtime amplification** — option (a) with a 5× bandwidth tax and far more power. (iii) Selective fan-out
needs the destination, which the relay cannot read: the only cleartext address is `receiver_idx`, receiver-chosen
and scoped to `(transport_id, receiver_idx)` (`src/node/dataplane/encrypted.rs:88`). It names the *receiver*, not
the sender, so the relay cannot suppress delivery to the originator's pipe.

**Verdict:** architecturally cleanest, practically wrong for this event.

---

## 2. Duplicate flooding: does FIPS dedupe?

**Yes — by AEAD counter, not by datagram ID. The duplicate is not free.**

**No ID and no visible TTL.** The FMP established header is 16 bytes and wholly cleartext
(`core/src/proto/fmp/wire.rs:326-346`):

```
[ver+phase:1][flags:1][payload_len:2 LE][receiver_idx:4 LE][counter:8 LE]
```

TTL lives in `SessionDatagram`, which is *inside* the AEAD: `ttl:1, path_mtu:2, src_addr:16, dest_addr:16`,
`SESSION_DATAGRAM_HEADER_SIZE = 36`, default `ttl = 64` (`core/src/proto/link.rs:106-127`, `:171`). A transparent
relay therefore sees phase, flags, payload_len, receiver_idx, counter — **no source, destination, TTL, hop count
or sequence ID.**

**Two dedup layers, both counter-based:**
1. **FMP per-link replay window**, `REPLAY_WINDOW_SIZE = 2048` compile-time (`core/src/noise/cipher.rs:68`;
   non-configurable per `docs/reference/configuration.md:592`). A second copy raises `NoiseError::ReplayDetected`,
   increments `peer.increment_replay_suppressed()`, and is dropped (`src/node/dataplane/encrypted.rs:358-380`).
2. **FSP end-to-end counter**, doubling as the AEAD nonce (`core/src/proto/fsp/wire.rs:169-183`), with its own
   window checked before and after decryption (`core/src/noise/session.rs:91-126`).

**No data-plane dedup at transit nodes.** `core/src/proto/routing/core.rs` and its README describe exactly five
decisions — local-vs-forward, TTL decrement, bloom match, path-MTU min-fold, ECN — plus an error rate limiter. No
seen-set. Dedup caches exist **only for control floods**: lookup by origin+timestamp
(`core/src/proto/lookup/state.rs:180`), bloom `sequence` documented "for freshness/dedup"
(`core/src/proto/bloom/wire.rs:26`), STP 8-byte `sequence` (`core/src/proto/stp/wire.rs:96`).

**Damage — not double delivery:**
- **Airtime.** Every frame is heard twice by every node in direct range. With `fixedPacketLengthMode(255)`
  (`:100`) even a 37-byte heartbeat (`RESULTS.md:294`) costs 255 B of air: 785 µs instead of 114 µs. So ~2×
  duplication on top of ~2.2× padding ≈ **4–5× the airtime the traffic deserves**, on a channel serving five nodes.
- **Failure counters.** Each replay hit calls `peer.record_failed(...)` (`encrypted.rs:360`) and bumps the
  suppressed counter; `past_threshold()` (`:367`) then silences logging. I found **no** path where replay tears
  down a session — honest statement: unproven, must be instrumented.
- **Indistinguishable from attack.** To the receiver, a transparent repeater is byte-identical to an on-path
  replayer, because the cleartext header carries nothing to distinguish them.

**Plainly: no corruption, but doubled channel load, inflated failure counters, and replay-detection noise that
will make 4-day logs unreadable unless relay-duplicate is separated from real problem.**

---

## 3. Who schedules: balloon or ground?

**Ground derives it; the balloon only follows — legitimately, because the table is a pure function of UTC.**

ADR-014: the relay "just physically relays already-encrypted FIPS frames — it cannot decrypt or modify them"
(`014:98`), data plane "completely transparent to all higher layers" (`:96`). Scheduling is control-plane. A
balloon that *decided* slots would need node identities, link membership and demand — encrypted or participatory.
Violation.

A *fixed UTC-derived table* is not a decision, it is a constant — exactly ADR-021's proven pattern:
`phase = phaseTable[utcSeconds % totalCycleSeconds]`, priority **GPS epoch → laptop SET_TIME → millis**
(`021:44-57`), and ADR-021 also records the trap: a 60 s blocking GPS gate at boot desynchronised everything when
the fix was slow (`:19-32`). Use the 5 s probe.

The balloon needs three constants: frame length, slot count, its own slot. All configuration. **It never
inspects a payload byte.**

### Ground-derived TDMA specification

| Parameter | Value | Rationale |
|---|---|---|
| Frame | **50 ms** | Divides 1 s, 60 s, 1 h exactly — no rollover discontinuity |
| Slots | **8** | Exactly `TDMA_MAX_SLOTS` (`tdma.h:33`): 1 beacon + 5 node TX + 1 relay + 1 contention |
| Slot duration | **6250 µs** | 0.9 ms air + ~2.5 ms turnaround + ~2.8 ms guard |
| Guard | **≥ 2500 µs** | **`TDMA_GUARD_US = 200` (`:35`) is ~12× too small**; TX→RX turnaround alone is 1200 µs (`:115`) |
| Slot index | `(utcMillis()/6250) % 8` | Pure UTC function, identical on all six radios |
| Assignment | node *i* TX in slot *i* (1–5) | Static config |
| Balloon | relays in **slot 6 only** | Static config |
| Latency | **1 frame = 50 ms** | TX in slot *i*, relayed slot 6, heard same frame |

Per-node airtime: one 255 B frame per 50 ms = 40.8 kbps sustained, ~5× a single FIPS link's ~9 kbps. Headroom
covers MMP heartbeats (`heartbeat_interval_secs = 10`), tree/bloom announces, lookups, and the 120 s rekey
(`rekey.after_secs = 120`) in slot 7.

### `tdma.c` reuse

**Reusable:** slot table + `tdma_set_slot()`, callback registration, `tdma_get_current_slot()`,
`tdma_get_frame_number()`, the `advance_to_slot()` shape.

**Not reusable as-is:**
1. **2 s default frame** (`:34`) → 2–4 s ground latency; store-and-forward, not interactive. Re-init at 50 ms.
2. **200 µs guard** — see above.
3. **`tdma_tick(elapsed_us)` is caller-fed.** Feed it UTC-derived elapsed time; FreeRTOS ticks reintroduce
   exactly the drift ADR-021 eliminated.
4. **`tdma_pps_pulse()` is dead here** — no PPS line on the C3; UTC arrives by GPS NMEA or host `SET_TIME` over
   USB CDC.
5. **`band` field and RX callback unused** — `radioTx()` must be driven from the TX callback, not called inline
   from `uartToRadioTask`.
6. **`TDMA_MAX_SLOTS = 8` leaves zero headroom**; a sixth node is a source change.

---

## 4. Firmware changes, ordered by risk

### C1 — Single radio owner + TX queue · **REQUIRED** · ~1.5 d

The root defect: `uartToRadioTask` calls `radioTx()` inline (`:174`) while the main task calls `radioRx()`
(`:259`); both do `standby()` + `startReceive()` (`:118-120`, `:129-131`). The mutex protects the bus, not the
state machine.

```diff
-static TaskHandle_t radioRxTask = NULL;
+static TaskHandle_t radioTask = NULL;
+static QueueHandle_t txQueue = NULL;
+#define TX_QUEUE_DEPTH 32
+#define TX_QUEUE_ITEM  256
@@ uartToRadioTask
-                    radioTx(frame, pktLen);
+                    if (xQueueSend(txQueue, frame, pdMS_TO_TICKS(20)) != pdTRUE)
+                        txDropCount++;   // never touch the radio from this task
```

Depth 32 × 256 B = 8 KB, ~2% of 400 KB SRAM. Turns a radio race into a measurable counter.

### C2 — TDMA slot gate; delete jitter · **REQUIRED** · ~1 d (needs C3)

```diff
 static void radioTx(const uint8_t *data, size_t len) {
-    esp_rom_delay_us(esp_random() % 3000);
+    // Jitter and TDMA are mutually exclusive: the slot boundary is the
+    // arbitration mechanism; a random delay is a second, conflicting one.
```
Gate every transmit with `if (utcSlot() != MY_SLOT) return;` in the radio task.

### C3 — UTC time base · **REQUIRED for TDMA** · ~1 d + GPS wiring

```diff
+static uint64_t utcMillis(void) {              // ADR-021 priority chain
+    if (gps.hasUnixTime) return gps.unixTimeMs;                   // 1. GPS
+    if (hostTimeValid)   return hostTimeMs +
+        (esp_timer_get_time()/1000 - hostTimeAtMs);                // 2. SET_TIME
+    return esp_timer_get_time() / 1000;                            // 3. millis (drifts)
+}
+static inline uint8_t  utcSlot(void)  { return (uint8_t)((utcMillis()/6250ULL) % 8); }
+static inline uint32_t utcFrame(void) { return (uint32_t)(utcMillis()/50ULL); }
```

GPS on GPIO0/1 (`docs/fips-flrc-validation-plan.md` TRACK 3) or `SET_TIME` over CDC — the latter suffices for a
tethered balloon with a ground laptop.

### C4 — Watchdog that survives 4 days · **REQUIRED** · ~0.5 d

Inverted incentive today: it fires on 15 s with no valid FIPS frame (`:282`). MMP heartbeats run every 10 s, so
**more peers → more valid frames → watchdog never trips, precisely when the radio is broken.** With 5 peers,
valid frames arrive every ~2 s.

```diff
-        if (nowMs - lastValidRxMs > 15000) {
+        // Local liveness, not mesh liveness: with N peers the mesh's own
+        // heartbeat rate masks a dead radio. Never re-init more than once
+        // a minute, so a reset storm cannot hide a hardware fault.
+        if ((nowMs - lastValidRxMs > 15000 || txNoDoneCount > 10)
+            && (nowMs - lastRadioInitMs > 60000)) {
```

Also: `radioInit()` (`:95-103`) is **not** the boot path (`:227-239`) — it ignores `beginFLRC`'s return and does
not reset counters, so recovery is indistinguishable from a hang. Make it the single shared init path, returning
`esp_err_t`.

### C5 — Variable packet length · **REQUIRED** · ~2 h, careful retest

Cheapest change with the largest capacity effect. Every frame is padded to 255 B (`:108-112`), so a 37 B
heartbeat costs 785 µs of air instead of 114 µs.

```diff
-    radio->fixedPacketLengthMode(255);
+    radio->variablePacketLengthMode(255);
```
Drop `pad[]` from `radioTx()`; the RX trim (`:265-270`) becomes a sanity check. **Caveat:** this is what
previously broke RX — `RESULTS.md:262` records "sequential config runs corrupt radio state … one config per
build." Verify as one configuration, never toggled at runtime. Gives an FLRC serial MTU of **238 payload bytes**
(255 − 13 header − 4 CRC) — matching `fragment_payload_max = 238` already in
`docs/fips-flrc-validation-plan.md:69`.

### C6 — Unattended safety · **REQUIRED for 4 days** · ~0.5 d

- **Kill the infinite blink loops** (`:213-218`, `:230-235`). On `beginFLRC` failure the firmware spins forever
  blinking — a dead balloon with a working LED. Bounded retry (10 attempts, then 30 s sleep-and-retry).
- **Emit the counters that already exist** (`:54-56` never printed). 60 s stats line over CDC: counts, queue
  drops, watchdog resets, current slot, UTC source. ~2 h. Without it a 4-day failure is undiagnosable.
- **Distinguish USB failure.** `usb_serial_jtag_driver_install` returning `ESP_ERR_INVALID_STATE` is silently
  tolerated (`:211-212`) — a headless, invisible bridge. Give it a distinct LED pattern. ~1 h.
- **Persist counters in RTC memory** across resets so "how many resets in 4 days" is answerable. ~2 h.

### C7 — Addressing / ingress suppression · **OPTIONAL** · ~3–5 d

Only for (b)/(c). The sole usable address is `receiver_idx` (cleartext, offset 4,
`core/src/proto/fmp/wire.rs:326-346`), receiver-chosen and scoped to `(transport_id, receiver_idx)`. It names
the receiver, not the sender, so on a single shared channel it buys nothing.

### C8 — Band switching · **OPTIONAL** · ~2–3 d

Only for (b). One LR2021 cannot serve two bands (`012:11`); a change is a full re-init costing tens of ms, not
per-packet. Needs a second radio — ADR-014's crossbar.

### C9 — Queue depth / backpressure · **OPTIONAL** · folded into C1

Depth 32 suits the demo. If stats share the CDC link, watch the 64-byte read chunk (`:158`) against the 1024-byte
USB RX buffer (`:207`).

---

## 5. FIPS peer capacity and configuration

**Capacity is not the constraint.**

| Limit | Default | Source |
|---|---|---|
| `node.limits.max_peers` | **128** | `src/config/node.rs:51`; `configuration.md:173` |
| `max_connections` / `max_links` | 256 / 256 | `src/config/node.rs:50,52` |
| `max_pending_inbound` / `max_sessions` | 1000 / 1024 | `src/config/node.rs:53-54` |

Up to **128 authenticated peers**; 4 peers per ground node is nowhere near it. Msg1 arriving at the cap is
silently dropped without a Msg2 (`src/node/handlers/handshake.rs:921-922`).

**The transport is the constraint.** Serial is explicitly **point-to-point**: "connect exactly two endpoints",
MTU 256–1500, "SLIP/COBS framing" (`docs/design/fips-transport-layer.md:135-140`), setup "Physical connection
(static)" (`:196`). **One serial transport instance = one link = one peer.** A ground node cannot hold four peers
over one bridge; it needs four bridges, or must reach the others by FIPS *transit*. **So the real answer to "how
many ground peers can share one bent-pipe relay" is two, under the proven design.** N=5 is a transport-topology
problem, not a peer-count problem.

**Peers are static, not discovered.** `peers:` is a first-class section (`configuration.md:94`, "Static peer
list"); each entry is `PeerAddress { transport, addr, priority }` (`src/config/peer.rs:97-127`), with
`ConnectPolicy::AutoConnect` — per the source comment "the only policy supported in the initial implementation"
(`peer.rs:12-16`). Discovery exists but **not for serial/radio**: mDNS (`README.md:380`), BLE/Ethernet beacons,
Nostr adverts. UDP advertises IP-reachable endpoints and explicitly cannot advertise "radio, BLE, serial"
(`fips-transport-layer.md:962`). The bridge is not a peer — it is a transparent PHY, and there is no path for the
balloon to learn who is on the ground.

**Blocking finding.** Upstream master `6c3e1c8` has **no serial transport implementation**.
`TransportType::SERIAL` is declared (`src/transport/mod.rs:355`) and `fips-transport-layer.md:1407` lists it as
"Future direction", but `src/transport/mod.rs:8-16` declares only loopback, nym, socks5, tcp, tor, udp, ethernet,
ble, and `TransportsConfig` (`src/config/transport.rs:951-975`) has no `serial` field. The June test used FIPS
**v0.3.0-dev** with `src/transport/serial/mod.rs` (`RESULTS.md:307` cites a fix at `:388`) — **not in this
checkout**. Pin and vendor the exact revision; do not let a `cargo update` remove the transport the whole
architecture depends on.

---

## 6. Recommendation

Run **(a)**: one shared 2.4 GHz FLRC channel, five ground nodes, ground-derived UTC TDMA at 50 ms / 8 slots,
balloon relaying slot 6. Ship C1–C6 as one firmware revision; C7–C9 out of scope. Pin the FIPS revision that has
the serial transport.

Accept in writing before the event:

- ~3–6 ms per relay hop; ground→ground within one 50 ms frame.
- ~80 kbps/node usable, ~838 kbps raw channel.
- The balloon cannot address, filter or suppress — every repeat reaches every node.
- Duplicates are dropped by replay windows but cost ~2× airtime and inflate per-peer failure counters. Instrument
  the separation.
- RX degrades after 2–5 min of sustained operation (`RESULTS.md:348-360`) with ~30 s watchdog recoveries recurring
  over 4 days. A known, measured limitation, not a surprise.

**Close C1 first.** Until one task owns the radio, nothing — TDMA included — can be made deterministic.
