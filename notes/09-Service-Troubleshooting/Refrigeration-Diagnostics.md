# Refrigeration & Cooling Diagnostics

## The Five-Minute Field Method

1. **Verify airflow FIRST** — filter, blower, coil face, registers. Most "refrigerant problems" are airflow problems
2. Measure: suction pressure + line temp → **superheat** · liquid pressure + line temp → **subcooling** · indoor ΔT (supply vs return)
3. Read the matrix below, THEN decide — never add refrigerant on suction pressure alone

## Diagnostic Matrix

| Suction | Head | Superheat | Subcool | Likely cause |
|---|---|---|---|---|
| Low | Low | **High** | **Low** | **Undercharge / leak** — find the leak first |
| High | High | Low | **High** | **Overcharge** — recover to spec, weigh it |
| Low | Low–Normal | High | Normal–High | Restriction (drier, TXV screen, kink) — frost AT the restriction is the tell |
| High | Low | High | Low | **Inefficient compressor** (valves/rings) or reversing valve bypass |
| Low | Normal | Low | Low | **Low airflow** — frozen coil path; fix airflow |
| High | High | Normal | Normal–High | Dirty condenser / high ambient / non-condensables |

- Non-condensables (air in system): head pressure high for the condensing temp, gauge needle may flutter — recover, evacuate, recharge weighed
- TXV hunting: superheat swings wide — check bulb contact/insulation, charge, screen
- Fixed-orifice systems charge by SUPERHEAT chart (indoor wet bulb + outdoor dry bulb); TXV systems charge by SUBCOOL on the rating plate (typically 8–12°F)

## PT Reference (psig, rounded — use gauge temp rings for precision)

| °F | R-410A | R-22 | R-134a |
|---|---|---|---|
| 30 | 100 | 55 | 22 |
| 40 | 118 | 69 | 35 |
| 50 | 142 | 84 | 45 |
| 60 | 170 | 102 | 57 |
| 70 | 201 | 121 | 71 |
| 80 | 235 | 144 | 87 |
| 90 | 274 | 168 | 104 |
| 100 | 317 | 196 | 124 |
| 110 | 365 | 226 | 146 |
| 120 | 417 | 260 | 171 |

- R-410A: ~60% higher pressure than R-22; charge as **LIQUID** (blend); POE oil — keep systems sealed, it absorbs water fast
- R-407C/448A/449A: high GLIDE (~10°F) — use dew point for superheat, midpoint for subcooling; charge liquid
- R-32 / R-454B (A2L mildly flammable): ventilation, no ignition sources, A2L-rated recovery, purge before brazing
- R-513A: R-134a replacement; similar pressures to 134a

## Leak Test, Recovery, Evacuation (EPA 608 core)

- Standing nitrogen test: trace gas + N2 per manufacturer IOM/SOP (typical field SOP: staged steps up to test pressure, multi-hour hold, temperature-compensated); soap/electronic detector at every joint
- Recovery levels: ≤15" Hg for systems >200 lb charge (or per current 608 rules); never vent — ANY refrigerant, any amount, any excuse
- Evacuate to **500 microns**, decay test: isolate and hold — rise <1000 microns and holding = dry+tight; rising continuously = leak; rising then plateau = moisture
- Triple evacuation with N2 breaks for wet systems; change the drier any time the system was open
- Oil: POE (410A/134a blends) vs mineral (old R-22) — never mix; moisture test with acid kit when a compressor burned out

## Compressor Electrical Diagnosis

- Resistance: C–R + C–S should equal R–S (single phase); any terminal-to-ground = grounded = replace
- No resistance between windings = open winding; infinite on all = internal overload open (WAIT — it may reset cold)
- Locked rotor amps vs nameplate LRA tells you seized vs weak start components; always try a hard-start kit diagnosis before condemning
- Burnout cleanup: suction-line drier + liquid drier, acid test, flush — or the new compressor dies the same death

## Frozen Coil / Icing Logic

Ice at coil → check airflow (filter, blower, belts, closed dampers) → then charge → then TXV. Ice ONLY at one spot in the line → restriction right AT the ice. Ice on compressor/floodback → overcharge, failed TXV, or low load — liquid slugging kills compressors.
