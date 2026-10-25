#!/usr/bin/env python3
"""Tethered-balloon trade study — balloon size vs tether vs payload vs helium cost.

PHYSICS BASE (all figures derived here, no magic numbers except the two anchors below)

  Site lift density  28 g/ft^3 at 471.6 m elevation and ~28 C afternoon.
    Derivation: sea-level dry-air/helium difference is ~1.0562 kg/m^3 at 15 C;
    at 471.6 m (pressure ratio 0.9463) and 28 C (288.15/303.15 = 0.9505)
    => 1.0562 * 0.9463 * 0.9505 = 0.9499 kg/m^3 = 28.0 g/ft^3. Matches the
    repo's stated 28 g/ft^3, so the anchor is self-consistent.

  Sphere geometry (NOT foil clusters — D8 rejected those):
    Volume      V = pi/6 * D^3
    Gross lift  L = V * 28.0 g/ft^3
    Envelope    A = pi * D^2   (surface area)
    Drag        Fd = 0.5 * rho * Cd * A * v^2,  Cd = 0.47 (sphere, Re ~ 1e5-1e6)

  Blow-over angle:  tan(theta) = Fd / (L - payload - tether), i.e. free net lift
  above everything hanging below. Effective height = L_tether * cos(theta).

TETHER: mass per metre taken from the repo's own measured figures
  (shopping-list.md §4): 1.0 mm Dyneema 46 g / 150 ft, 1.5 mm 101 g / 150 ft.
  A power pair is ADDITIVE to the load line (copper carries power, Dyneema
  carries load), so PoE cases add a separate conductor mass per metre.

COST: helium priced per ft^3 at an industrial balloon-grade rate. The repo
records ~$0.33/ft^3 as the USGS Grade-A base and $5.10/ft^3 as retail party
tanks; a real industrial cylinder lands between. This study uses $1.20/ft^3
as the planning figure and shows sensitivity, because the base rate is a
commodity quote and the delivered rate includes deposit + hazmat + top-ups.

Everything is arithmetically reproducible: run this file, it prints the tables
that the markdown quotes.
"""
from __future__ import annotations

import numpy as np

# ---- anchors ---------------------------------------------------------------
G_PER_FT3 = 28.0          # site lift, derived in the docstring
CD_SPHERE = 0.47
RHO_AIR = 1.0             # kg/m^3, site density (471.6 m, 28 C) — close enough
FT3_PER_M3 = 35.3147
HE_USD_PER_FT3 = 1.20     # planning figure; sensitivity shown separately


def ft2m(x):
    return x * 0.3048


def sphere_volume_ft3(d_in: float) -> float:
    """Volume of a sphere in ft^3 from diameter in inches."""
    d_ft = d_in / 12.0
    return np.pi / 6.0 * d_ft ** 3


def sphere_area_m2(d_in: float) -> float:
    """PROJECTED (frontal) area of a sphere: pi*d^2/4.

    CORRECTED 2026-10-25 — this was pi*d^2, which is 4x the true frontal area.
    A sphere's silhouette is a CIRCLE of area pi*r^2 = pi*d^2/4; pi*d^2 is the
    SURFACE area, not the drag reference area. The bug made every blow-over
    angle in the first render wildly pessimistic (60 in at 8 kn read 73 deg /
    43 ft instead of the true ~40 deg / 115 ft). Caught by the visual consultant
    checking the arithmetic, then verified by hand.
    """
    d_m = ft2m(d_in / 12.0)
    return np.pi * d_m ** 2 / 4.0


def gross_lift_g(d_in: float) -> float:
    return sphere_volume_ft3(d_in) * G_PER_FT3


def drag_n(d_in: float, wind_kn: float) -> float:
    v = wind_kn * 0.514444
    return 0.5 * RHO_AIR * CD_SPHERE * sphere_area_m2(d_in) * v ** 2


def tether_mass_g(length_ft: float, g_per_150ft: float, n_lines: int = 1,
                  extra_g_per_m: float = 0.0) -> float:
    """Load line(s) plus optional conductor pair, over `length_ft`."""
    base = (length_ft / 150.0) * g_per_150ft * n_lines
    return base + extra_g_per_m * ft2m(length_ft)


def blowover_deg(d_in: float, wind_kn: float, payload_g: float,
                 tether_g: float) -> float:
    free = gross_lift_g(d_in) - payload_g - tether_g
    if free <= 0:
        return 90.0
    return np.degrees(np.arctan(drag_n(d_in, wind_kn) / (free / 1000.0 * 9.80665)))


def helium_usd(d_in: float, topup_frac: float = 0.20, days: int = 4) -> float:
    """Fill plus a daily top-up for `days`, as a fraction of fill per day."""
    v = sphere_volume_ft3(d_in)
    return v * (1.0 + topup_frac * days) * HE_USD_PER_FT3


# ---- the tables the markdown quotes ---------------------------------------
DIAMETERS = [36, 48, 60, 72, 84, 96, 120, 144]

print("TABLE 1 — sphere lift, volume, helium cost")
print(f"{'D_in':>6} {'ft3':>8} {'lift_g':>8} {'He_4day_USD':>12}")
for d in DIAMETERS:
    print(f"{d:>6} {sphere_volume_ft3(d):>8.1f} {gross_lift_g(d):>8.0f} "
          f"{helium_usd(d):>12.2f}")

print("\nTABLE 2 — useful payload at 150 ft, 1.0 mm Dyneema, per wind")
print("payload_g = gross_lift - tether - (a reserve fraction)")
for d in [60, 72, 84, 96, 120, 144]:
    t = tether_mass_g(150, 46)
    g = gross_lift_g(d)
    print(f"D={d:>4}in lift={g:>6.0f}g tether150={t:>5.0f}g "
          f"payload@80%={0.8*g - t:>6.0f}g helium=${helium_usd(d):>7.2f}")

print("\nTABLE 3 — blow-over angle (deg) at 150 ft tether, payload = 50% of net")
print("rows = diameter, cols = wind kn")
print(f"{'D':>5}" + "".join(f"{w:>7}" for w in [3, 5, 6, 8, 10, 12, 15]))
for d in [60, 72, 84, 96, 120, 144]:
    row = []
    for w in [3, 5, 6, 8, 10, 12, 15]:
        t = tether_mass_g(150, 46)
        net = gross_lift_g(d) - t
        payload = 0.5 * net
        row.append(blowover_deg(d, w, payload, t))
    print(f"{d:>5}" + "".join(f"{a:>7.0f}" for a in row))

print("\nTABLE 4 — effective height (ft) at 8 kn, 150 ft line")
print("effective = 150 * cos(theta)")
for d in [60, 72, 84, 96, 120, 144]:
    t = tether_mass_g(150, 46)
    net = gross_lift_g(d) - t
    payload = 0.5 * net
    th = blowover_deg(d, 8, payload, t)
    print(f"D={d:>4}in theta={th:>5.0f}deg effective={150*np.cos(np.radians(th)):>6.0f}ft")

print("\nTABLE 5 — tether mass vs length and conductor, per line")
print(f"{'len_ft':>7} {'1.0mm':>7} {'1.5mm':>7} {'+AWG28pair':>11} {'+AWG26pair':>11}")
for L in [50, 100, 150, 200, 300]:
    base1 = tether_mass_g(L, 46)
    base15 = tether_mass_g(L, 101)
    # AWG28 pair ~ 1.44 g/m total copper; AWG26 ~ 2.3 g/m
    print(f"{L:>7} {base1:>7.0f} {base15:>7.0f} "
          f"{tether_mass_g(L,46,extra_g_per_m=1.44):>11.0f} "
          f"{tether_mass_g(L,46,extra_g_per_m=2.30):>11.0f}")

print("\nTABLE 6 — PoE payload budget (the organiser's request)")
print("A PoE injector + 2 radios + camera + mount is ~400-800 g before cable.")
for need in [300, 500, 800, 1200, 2000]:
    # required gross lift = payload + tether(150ft,1.0mm) with 20% reserve
    t = tether_mass_g(150, 46)
    req = (need + t) / 0.8
    # solve V so that V*28 = req
    v = req / G_PER_FT3
    d_ft = (6 * v / np.pi) ** (1 / 3)
    print(f"payload {need:>5}g -> gross {req:>6.0f}g -> V {v:>7.1f}ft3 -> "
          f"D {d_ft*12:>6.1f}in -> He 4-day ${helium_usd(d_ft*12):>8.2f}")

print("\nSENSITIVITY — helium $/ft^3 vs 4-day cost at D=96in")
v4 = sphere_volume_ft3(96) * (1 + 0.2 * 4)
for price in [0.33, 0.75, 1.20, 2.00, 5.10]:
    print(f"  ${price:>4.2f}/ft3 -> ${v4*price:>8.2f} for {v4:.0f} ft3")
