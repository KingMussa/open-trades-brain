# Heating & Electrical Service

## Gas Furnace / RTU Sequence of Operation (know it cold)

1. Thermostat W call → 2. Inducer motor starts → 3. **Pressure switch proves** (venting) → 4. Ignitor energizes (HSI 15–30 sec warm-up) → 5. Gas valve opens → 6. Flame proves (flame sensor, ~1–10 µA DC) → 7. Blower on after delay → 8. Limit switches watch temperature the whole time

**Read faults backwards from where it stops:**
- Nothing at all → power, door switch, transformer (24 VAC at R–C), fuse
- Inducer runs, no ignition → **pressure switch** (blocked vent, cracked hose, weak inducer, condensate backup)
- Ignitor glows, no flame → gas supply, gas valve (24 V at valve?), ignitor position
- Flame lights then dies in 3–10 sec → **flame sensor** — clean with fine emery (microamps below ~2 µA = clean/replace); also ground path
- Short cycles on heat → high limit tripping = **airflow** (filter, blower, closed registers) or failed limit
- Blower never stops / no heat → fan/limit switch

## Component Numbers

- **HSI (hot surface ignitor):** resistance typically **40–400 Ω** cold; handle by the base — skin oil kills them; check for hairline cracks
- **Flame sensor:** 1–10 µA DC in series (meter on µA); clean yearly
- **Gas valve:** 24 VAC across terminals during trial; manifold pressure natural gas ~**3.5" WC**, LP ~**10–11" WC** (verify rating plate); inlet NG ~7" WC
- **Pressure switches:** rated in "WC negative — verify rating matches, hoses uphill, ports clear

## Motors & Drives

- **PSC motor:** needs its capacitor — weak cap = hot slow motor; check µF within ±6%
- **ECM/x13:** programmed module — check low-voltage taps/PWM signal before condemning the motor; surge kills modules
- **Three-phase:** all three legs within ~2–3% voltage balance; a blown leg = single-phasing = compressor death; rotation matters on scroll/screw — any two wires swapped fixes backwards rotation
- Capacitor math: run cap in spec, start cap + potential relay on hard starts; discharge caps before touching (resistor, not a screwdriver)

## Low-Voltage / Controls

- 24 VAC system: R (hot), C (common), Y (cool), G (fan), W (heat), O/B (reversing valve)
- Most "dead stat" = open float switch in series on R (condensate full) — check the drain safety FIRST
- Short on 24V circuit = blown 3A fuse on the board; find the rubbed wire (usually at the outdoor unit or through cabinet holes)
- Contactor: pitted points drop voltage to the compressor — measure across points under load (>~2–3V drop = replace); coil 24 VAC
- Relays/sequencers: NO/NC logic — prove with the meter, not by eye

## Meter Essentials

- **Voltage:** test meter on a KNOWN source first; LOTO means verify-dead with a live-dead-live check
- **Amps:** clamp ONE conductor; inrush vs running — compare RLA on the plate
- **Ohms:** only on de-energized, isolated components (capacitors out of circuit)
- **µA DC:** flame sensor in series
- Megger for compressor/motor insulation-to-ground when a winding reads suspicious but not dead

## Heat Pump Extras

- Reversing valve: energized in cooling (O) on most; stuck halfway = both suction/discharge warm, poor capacity
- Defrost: board demands it on outdoor coil temp + timer; defrost fault = iced outdoor coil = no heat; sensors and board inputs first
- Aux/emergency heat strips: sequencers bring stages; check airflow — strips + low airflow = limit trips
