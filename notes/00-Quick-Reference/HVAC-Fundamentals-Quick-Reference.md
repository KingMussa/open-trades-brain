# HVAC Fundamentals — Field Quick Reference

General trade reference. Manufacturer-specific values always come from the unit's rating plate and service manual — check the manuals section once loaded.

## The Refrigeration Cycle (4 Components)

1. **Compressor** — pumps low-pressure vapor, compresses it to high-pressure hot vapor
2. **Condenser coil** — rejects heat; hot vapor condenses to high-pressure liquid
3. **Metering device** (TXV or piston/fixed orifice) — drops pressure; liquid flashes to cold low-pressure mix
4. **Evaporator coil** — absorbs heat from indoor air; refrigerant boils off to vapor, back to compressor

## Superheat & Subcooling

- **Superheat** = suction line temp − saturation temp at suction pressure. Measured at the outdoor unit suction service port. Used to charge **fixed-orifice (piston)** systems. Typical target 8–20°F depending on indoor wet-bulb and outdoor temp (use manufacturer's charging chart).
- **Subcooling** = saturation temp at liquid pressure − liquid line temp. Used to charge **TXV** systems. Typical target 8–12°F (rating plate usually lists it).
- High superheat + low subcooling → undercharge. Low superheat + high subcooling → overcharge. Verify airflow BEFORE charging.

## Standard Pressure-Temperature Reference (approximate, psig)

| Temp (°F) | R-410A | R-22 |
|---|---|---|
| 40 | 118 | 69 |
| 50 | 142 | 84 |
| 60 | 170 | 102 |
| 70 | 201 | 121 |
| 80 | 235 | 144 |
| 90 | 274 | 168 |
| 100 | 317 | 196 |

- R-410A operates roughly 60% higher pressure than R-22. Never mix refrigerants; never use R-22 gauges/manifold-rated-only equipment on 410A unless rated for it.
- R-454B and R-32 (A2L, mildly flammable) are the current R-410A replacements — follow A2L handling and ventilation requirements.

## Airflow Rules of Thumb

- **400 CFM per ton** nominal (350 for humid climates/latent removal, up to 450 dry climates)
- 12,000 BTU = 1 ton
- Temperature split (supply vs return): **16–22°F** across the evaporator in cooling. Low split → low airflow or capacity problem; high split → restricted airflow.

## Electrical Basics

- **Capacitor test**: discharge first. µF reading within ±6% (or marked tolerance) of rating. Bulging top = replace.
- **Contactor**: pitted/burnt points cause voltage drop to compressor; coil voltage typically 24VAC.
- **Compressor terminals**: C, R, S. C–R + C–S = R–S resistance. Any terminal to ground (copper) = grounded compressor, replace.
- **Sequence of operation (cooling call)**: thermostat Y+G → indoor blower + 24V to contactor → condenser fan + compressor run.

## Common Symptom → Likely Causes

| Symptom | Check first |
|---|---|
| Frozen suction line / coil | Airflow (filter, blower, closed vents), then low charge |
| Short cycling | Oversized stat anticipator/location, high-pressure switch, low charge, dirty coil |
| Unit runs, no cooling | Compressor actually running? Capacitor, contactor, charge |
| High head pressure | Dirty condenser, overcharge, non-condensables, condenser fan |
| High suction + low head | Compressor valves / reversing valve bypass |
| Blower runs, no 24V outside | Float switch tripped (clogged drain), low-voltage short, thermostat |
| Water around air handler | Clogged condensate drain, frozen coil melting, cracked pan |

## Safety

- Lock out / tag out before opening electrical. Verify with meter — don't trust the disconnect handle.
- Refrigerant burns: frostbite on contact; R-410A blends must be charged as **liquid**.
- A2L refrigerants (R-32, R-454B): no open flames/brazing without purging, ensure ventilation, use A2L-rated recovery equipment.
