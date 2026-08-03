# Formulas & Conversions — Master Sheet

## Hydronics / Heat Transfer

- **BTU/h = 500 × gpm × ΔT(°F)** (water) · gpm = BTU/h ÷ (500 × ΔT)
- With glycol: replace 500 with (485 × specific gravity × specific heat) — 50% PG ≈ 460
- 1 ton = **12,000 BTU/h** · 1 boiler HP = 33,475 BTU/h · 1 kW = 3,412 BTU/h
- Chilled water: gpm = tons × 24 ÷ ΔT (10°F ΔT → 2.4 gpm/ton; 12°F → 2.0; 15°F → 1.6)
- Condenser water rule: ~3 gpm per ton at 10°F range
- Pump head (ft) = psi × 2.31 ÷ SG · psi = head (ft) × 0.433 × SG
- **Pump affinity laws:** flow ∝ RPM · head ∝ RPM² · brake HP ∝ RPM³. Same laws for fans (CFM / static / BHP)

## Electrical

- Ohm's law: V = I × R · **Watts = V × I** (1Ø) · **W = V × I × 1.732 × PF** (3Ø)
- Amps from kW (3Ø, 480V, PF 1.0): I = kW × 1000 ÷ (480 × 1.732) ≈ kW × 1.2
- 1 HP ≈ 746 W · motor FLA rough (3Ø 460V): ~1.25 A/HP
- kWh cost = kW × hours × rate

### THHN Copper Ampacity (90°C column — derate + termination ratings apply)

| AWG | Amps | AWG | Amps |
|---|---|---|---|
| 14 | 25 | 2 | 130 |
| 12 | 30 | 1 | 145 |
| 10 | 40 | 1/0 | 170 |
| 8 | 55 | 2/0 | 195 |
| 6 | 75 | 3/0 | 225 |
| 4 | 95 | 4/0 | 260 |
| 3 | 115 | 250 kcmil | 290 |

*(Breakers usually sized off 60/75°C termination limits — 12 AWG → 20 A, 10 → 30 A, 8 → 40/50 A in practice)*

## Pipe & Flow

- v (ft/s) = 0.408 × gpm ÷ ID² · gpm = 2.448 × ID² × v
- Pipe steel lb/ft = 10.69 × (OD − wall) × wall
- Water in pipe lb/ft = 0.3405 × ID² · gal/ft = 0.0408 × ID²
- Velocity head pressure drop ~ ΔP ∝ (flow)² — double the flow, 4× the friction
- Expansion: carbon steel 0.82" per 100 ft per 100°F · copper ~0.92" · stainless 304 ~1.2" · PVC ~3.3"

## Air

- Sensible: BTU/h = 1.08 × CFM × ΔT · Total: 4.5 × CFM × Δh · Latent: 0.68 × CFM × Δgr
- 400 CFM/ton · fresh air ~15–20 CFM/person typical design
- Duct area (in²) = 144 × CFM ÷ FPM velocity · round duct CFM ≈ FPM × πr²/144

## Refrigeration

- 1 ton = 12,000 BTU/h = 4.7 gpm at 6°F... (use chw formula above)
- Compression ratio = absolute discharge ÷ absolute suction (psia = psig + 14.7) — high ratio kills efficiency/valves
- Superheat = suction line temp − saturation temp (at suction pressure)
- Subcooling = saturation temp (at liquid pressure) − liquid line temp

## Conversions

- Length: 1" = 25.4 mm · 1 m = 3.281 ft · 1 mile = 5,280 ft
- Area: 1 ft² = 144 in² · Volume: 1 ft³ = 7.48 gal · 1 gal = 231 in³
- Weight: 1 ton (short) = 2,000 lb · 1 metric tonne = 2,205 lb · 1 kg = 2.205 lb
- Pressure: 1 psi = 2.31 ft H₂O = 27.7" WC · 1" WC = 0.036 psi · 1 bar = 14.5 psi · 1" Hg = 0.491 psi
- Temperature: °F = °C × 1.8 + 32 · °C = (°F − 32) ÷ 1.8 · (−40 is the same in both)
- Energy: 1 BTU = 778 ft-lb · 1 therm = 100,000 BTU · 1 kWh = 3,412 BTU
- Power: 1 HP = 746 W = 2,545 BTU/h · 1 ton refrig = 3.52 kW

## Shop Triangles (when the laser's dead)

- 3-4-5 (and multiples 6-8-10, 9-12-15) = perfect right angle
- Diagonal of a square = side × 1.414 · 45-45-90: legs equal, hypotenuse = leg × 1.414
- Circle: A = πr² = 0.7854 × d² · C = πd
