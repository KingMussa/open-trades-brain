# Pipe Math & Layout

*The fitter's calculator, offline. Verify critical dimensions against the fitting manufacturer's catalog.*

## Core Constants

- π = 3.1416 · Circumference = π × OD
- 45° factor = **1.414** · 30° factor = 2.000 · 60° factor = 1.155 (offset × factor = travel)
- 1 psi = **2.31 ft of water head** · 1 ft head = 0.433 psi
- Water: 62.4 lb/ft³ · 8.34 lb/gal · 7.48 gal/ft³
- Steel: 490 lb/ft³ · Concrete: ~150 lb/ft³

## 45° Offset (the daily one)

- **Travel (diagonal) = offset × 1.414**
- **Advance = offset** (each 45 moves you over by the offset amount)
- Center-to-center of the two 45s = travel minus fitting take-offs (both ends)
- Example: 8" offset with 4" weld 45s (take-off 2-1/2" each): travel = 8 × 1.414 = 11-5/16"; cut piece = 11-5/16 − 5" = 6-5/16"

## Any-Angle Offset

- Travel = offset ÷ sin(angle) · Advance = offset ÷ tan(angle)
- 22.5°: travel = offset × 2.61 · 30°: travel = offset × 2.00 · 60°: travel = offset × 1.155

## Rolling Offset (offset in two planes at once)

- **True offset = √(rise² + run²)** (the two offsets combined)
- Travel = true offset × 1.414 (for 45° fittings); advance = true offset
- Lay it out: box it — rise is one side, run is the other, true offset is the diagonal of that box; then treat as a simple offset

## Butt-Weld Fitting Take-Offs (rule-of-thumb, LR)

| Fitting | Take-off (center-to-end) |
|---|---|
| 90° LR elbow | **1.5 × nominal size** (4" → 6") |
| 45° elbow | **5/8 × nominal size** (4" → 2-1/2") |
| Tee (run or branch) | ~1 × nominal (verify B16.9 by size) |
| Concentric reducer | ~1/2 × larger nominal |

## Grooved Systems

- Cut groove: verify with go/no-go tape per the groove manufacturer's spec; cut length = coupling-to-coupling minus pad gaps
- Roll groove uses different end prep than cut groove — check the fitting schedule before cutting
- Allow angular deflection per coupling at each joint (Victaulic publishes per-size values) — use it for long offsets instead of fittings where allowed

## Pipe End Prep

- Bevel 37.5° ±2.5° for butt weld, 1/16" land (typical WPS — verify)
- Threading: hand-tight + wrench-tight engagement; taper 3/4" per foot (NPT); engagement ≈ 4–5 threads hand-tight for 2" and under

## Useful Field Formulas

- Velocity (ft/s) in pipe: **v = 0.408 × gpm ÷ d²** (d = actual ID, inches)
- Flow from velocity: **gpm = 2.448 × d² × v**
- Pipe steel weight (lb/ft): **10.69 × (OD − wall) × wall**
- Water weight in pipe (lb/ft): **0.3405 × d²** (d = ID inches) — a full pipe's total weight = steel + water; always use TOTAL for hangers
- Cylinder/tank volume: π × r² × L · gallons = ft³ × 7.48
- Metal expansion: **ΔL = coefficient × L × ΔT** — carbon steel ≈ 0.82" per 100 ft per 100°F (0.0000065 in/in/°F); copper ≈ 1.1× that; stainless 304 ≈ 1.5×

## Level & Grade

- 1/4" per foot = ~1.19° = 2% grade · 1/8" per foot = ~1%
- Sight-grade check: a 4-ft level with a 1" block under one end = 1/4"/ft (block = 1/3" per ft of level)
- Laser/transit: rise = rod reading difference; don't trust a bent tripod
