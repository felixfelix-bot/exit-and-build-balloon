#!/usr/bin/env python3
"""Render the balloon trade-study figure. All numbers come from balloon_model.py."""
from __future__ import annotations

import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from balloon_model import (  # noqa: E402
    DIAMETERS, G_PER_FT3, blowover_deg, gross_lift_g, helium_usd,
    sphere_volume_ft3, tether_mass_g,
)

OUT = Path(__file__).parent / "balloon-tradeoffs.png"

# A restrained, legible style: no chartjunk, direct labels, one accent colour.
plt.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linewidth": 0.6,
    "axes.edgecolor": "#444444",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "legend.frameon": False,
})

ACCENT = "#1f6feb"
WARN = "#b3261e"
GREY = "#6b7280"

fig, axes = plt.subplots(2, 2, figsize=(13.0, 9.5))
fig.suptitle("Tethered balloon trade study — Exit & Build, Sovereignty Ranch (471.6 m)",
             fontsize=14, fontweight="bold", y=0.985)

D = np.linspace(30, 150, 400)

# ---------------------------------------------------------------- panel 1
ax = axes[0, 0]
lift = np.array([gross_lift_g(d) for d in D])
ax.plot(D, lift, color=ACCENT, lw=2.2, label="gross lift")
ax.plot(D, lift * 0.8 - tether_mass_g(150, 46), color=WARN, lw=2.0, ls="--",
        label="usable payload\n(80 % of lift, less 150 ft tether)")
for d in [48, 60, 72, 96, 120]:
    ax.plot([d], [gross_lift_g(d)], "o", color=ACCENT, ms=5, zorder=4)
    ax.annotate(f"{gross_lift_g(d):.0f} g", (d, gross_lift_g(d)),
                textcoords="offset points", xytext=(6, 6), fontsize=8.5, color=ACCENT)
ax.set_xlabel("balloon diameter (in)")
ax.set_ylabel("mass (g)")
ax.set_title("1 — Lift grows as D³ (volume), not D²")
ax.legend(loc="upper left", fontsize=8.5)
ax.set_xlim(30, 150)
ax.set_ylim(0, 30000)

# ---------------------------------------------------------------- panel 2
ax = axes[0, 1]
he = np.array([helium_usd(d) for d in D])
ax.plot(D, he, color=ACCENT, lw=2.2)
ax.fill_between(D, he * 0.33 / 1.20, he * 5.10 / 1.20, color=ACCENT, alpha=0.12,
                label="range: \\$0.33–\\$5.10 /ft³")
ax.plot(D, he, color=ACCENT, lw=2.2)
ax.set_xlabel("balloon diameter (in)")
ax.set_ylabel("helium cost, 4-day duty (USD)")
ax.set_title("2 — Helium is the recurring cost; it scales with D³ too")
ax.legend(loc="upper left", fontsize=8.5)
ax.set_xlim(30, 150)
ax.axhline(0, color=GREY, lw=0.8)
ax.annotate("planning figure\n$1.20/ft³ + 20 %/day top-up", (100, helium_usd(100)),
            textcoords="offset points", xytext=(-120, 22), fontsize=8.5, color=GREY)

# ---------------------------------------------------------------- panel 3
ax = axes[1, 0]
winds = np.linspace(1, 16, 200)
for d, style in [(60, ":"), (84, "-."), (120, "-")]:
    t = tether_mass_g(150, 46)
    net = gross_lift_g(d) - t
    payload = 0.5 * net
    eff = 150 * np.cos(np.radians([blowover_deg(d, w, payload, t) for w in winds]))
    ax.plot(winds, eff, style, lw=2.0, label=f"{d} in sphere")
ax.axhline(20, color=WARN, lw=1.2, ls="--")
ax.annotate("20 ft — approx. cedar canopy", (1.2, 24), fontsize=8.5, color=WARN)
ax.set_xlabel("sustained wind (kn)")
ax.set_ylabel("effective height on a 150 ft line (ft)")
ax.set_title("3 — Height in wind: tan θ = drag ÷ free lift\n(each curve loaded to 50 % of its net lift)")
ax.legend(loc="upper right", fontsize=8.5)
ax.set_xlim(1, 16)
ax.set_ylim(0, 155)
# venue note sits BELOW the curves' upper region and left of the legend box,
# which occupies roughly x>12.5, y>110 at 150 ft full scale.
ax.annotate("venue: mean daylight 7.6 kn,\n≥8 kn in 50 % of Nov daylight hours",
            (1.5, 96), fontsize=8.5, color=GREY, va="top",
            bbox=dict(boxstyle="round,pad=0.35", fc="#f3f4f6", ec="none"))

# ---------------------------------------------------------------- panel 4
ax = axes[1, 1]
payload_need = np.array([200, 300, 500, 800, 1200, 2000, 4000])
t = tether_mass_g(150, 46)
req_d = []
for need in payload_need:
    v = ((need + t) / 0.8) / G_PER_FT3
    req_d.append((6 * v / np.pi) ** (1 / 3) * 12)
req_he = [helium_usd(d) for d in req_d]

ax.plot(req_d, payload_need, color=ACCENT, lw=2.2, marker="o", ms=5)
for d, p in zip(req_d, payload_need):
    ax.annotate(f"{d:.0f} in", (d, p), textcoords="offset points",
                xytext=(7, -3), fontsize=8.5, color=ACCENT)
ax.set_xlabel("minimum balloon diameter (in)")
ax.set_ylabel("payload to lift (g)")
ax.set_title("4 — Payload vs required diameter\n(budget: 80 % of gross lift, less 46 g tether)")
# Part 101 Subpart B applies at diameter > 6 ft (72 in) OR gas capacity > 115 ft3.
# For an ideal sphere the 72 in diameter test binds FIRST: 72 in = 113.1 ft3,
# so 115 ft3 would not be reached until 72.4 in. Shade to 72, not 60.
ax.axvspan(30, 72, color=WARN, alpha=0.06)
ax.annotate("ideal spheres ≤72 in:\nneither §101.1(a)(1)\nsize threshold exceeded",
            (31, 2600), fontsize=8.5, color=WARN)
ax.set_xlim(30, 150)

fig.text(0.5, 0.012,
         "Ideal model: rigid sphere V=πD³/6, frontal area πD²/4, site lift 28 g/ft³, Cd 0.47, "
         "straight tether, balloon drag only (no tether drag, sag or envelope mass). "
         "Reproduce: analysis/balloon_model.py",
         ha="center", fontsize=8, color=GREY)

fig.tight_layout(rect=(0, 0.028, 1, 0.965))
fig.savefig(OUT, dpi=150)
print(f"wrote {OUT}")
