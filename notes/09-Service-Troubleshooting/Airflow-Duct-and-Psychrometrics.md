# Airflow, Duct & Psychrometrics

## The Numbers That Run Airside

- **400 CFM per ton** nominal (350 humid climates, 450 sensible-heavy)
- Total external static (residential target): **≤0.5" WC** (supply ~0.25, return ~0.15, coil ~0.1); commercial per design
- Temperature split cooling: **16–22°F** across the coil
- Sensible heat: **BTU/h = 1.08 × CFM × ΔT** · Total heat: **4.5 × CFM × Δh (enthalpy)** · Latent: 0.68 × CFM × Δgrains
- CFM from heat: CFM = BTU/h ÷ (1.08 × ΔT)

## Static Pressure Method (the truth-teller)

1. Drill 3/8" test ports: before and after blower, before and after coil (plug after)
2. Total external static = (supply side) + (return side), ignoring signs
3. Compare to blower table at that tap — gives REAL CFM, not guessed CFM
4. High static → undersized/closed duct, dirty coil, restrictive filter/grilles. High static kills ECM motors and freezes coils

## Duct Rules of Thumb

- Friction rate design: **0.1" WC per 100 ft** equivalent length (residential/light commercial)
- Flex duct: support every **4 ft max**, max sag 1/2" per ft, stretch TIGHT (compressed flex can lose 50% airflow), gentle radius (≥1 duct diameter)
- Equivalent length of a fitting ≈ 15–35 ft of straight duct — every elbow costs real static; minimize turns at the plenum
- Seal ALL joints (mastic, not cloth "duct tape"); SMACNA seal class per spec
- Duct leakage: a 20% leak is a ton of lost cooling per 5 tons — and it depressurizes/pressurizes the space
- Turning vanes in square elbows; no abrupt takeoffs off the plenum end cap

## Psychrometrics — What the Air Is Doing

- **Dry bulb** = thermometer temp · **Wet bulb** = temp with evaporation (measures total heat/moisture) · **Dew point** = where moisture condenses
- Relative humidity depends on temperature: cool air holds less water — same air at lower temp = higher RH
- Comfort target: ~75°F / 50% RH · ASHRAE IT inlet: 18–27°C, RH <60% (data-center work)
- Dew point rules everything cold: **insulate anything carrying fluid/air below the space dew point** — that's why cold pipes sweat and why vapor barrier sealing matters (punch walks)
- Condensate: ~1 pint per ton-hour in humid weather; drains sized, trapped (on draw-through AHUs the trap depth must exceed fan negative pressure or it never drains — classic water-in-the-unit problem)

## Fan Laws (like pump laws)

- CFM varies directly with RPM
- Static pressure varies with RPM²
- Brake HP varies with RPM³ — **a 10% overspeed costs 33% more power**; belt drives tune airflow by sheaves, not hope

## Kitchen/Exhaust & Makeup Air

- Exhaust out = makeup in, or the building sucks unconditioned air through every crack; negative buildings = doors hard to open, backdrafting flues, humidity problems
- Balance report targets: usually ±10% of design CFM per device
