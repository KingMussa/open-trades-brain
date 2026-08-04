# Equipment Tags & Schedules — The Lookup System

*Every tagged item on a job is an address. Learn the addressing scheme and the whole building becomes searchable.*

## Tag Anatomy

Most tagging schemes follow **TYPE-SYSTEM/AREA-SEQUENCE**:

- **FAU-0300-7** → FAU (fan coil/air unit type) · 0300 (system, level, or area number) · 7 (unit sequence)
- Once you know the scheme, the tag alone tells you roughly WHERE it is and WHAT system feeds it

## Common Tag Prefixes

| Tag | Equipment | Tag | Equipment |
|---|---|---|---|
| AHU | Air handling unit | P- | Pump |
| FAU | Fan-assisted / fan coil air unit | CH- | Chiller |
| MAU | Makeup air unit | B- | Boiler |
| RTU | Rooftop unit | HX- | Heat exchanger |
| CRAH | Computer room A/C (DX or CW) | CDU | Coolant distribution unit |
| CRAC | Computer room A/C (DX) | T- / TK- | Tank |
| FCU | Fan coil unit | EF / KEF | Exhaust / kitchen exhaust fan |
| VAV | Variable air volume box | VRF | Variable refrigerant flow system |
| ERV/HRU | Energy recovery unit | CT- | Cooling tower |

**Valve tags** are usually system-prefixed by service: CHWS/CHWR (chilled supply/return), SCHWS/SCHWR (secondary CHW), HW, CD (condenser), DHW, G (gas), with sequential numbers — often grouped by area/sector so nearby valves share number ranges.

## Schedules = Where the Specs Live

Every tag appears in a schedule (M5 sheets or spec tables). What each gives you:

- **Fan/FAU schedule:** CFM, external static, HP, volts/phase, MCA/MOP, filter size, weight
- **Pump schedule:** GPM, head (ft), HP, RPM, seal type, VFD yes/no
- **Chiller schedule:** tons, refrigerant, electrical, weight, flow/ΔT
- **CRAH/CDU schedule:** capacity, flow, connection sizes, control valve type
- **E-series panel schedule:** panel name, breaker, circuit, load — the power chain for the tag

## The Chained Lookup (the function you're describing)

**One tag in → everything out:**

1. Tag → **M5 schedule** = machine specs
2. Tag → **M2 floor plan** = physical location (level, area, grid) + what connects to it
3. Connected valve/pipe tags → **valve schedule/tag map** = isolation points and attached system
4. Tag → **M4 connection detail** = hookup requirements (sizes, flexible connections, strainers, PT ports)
5. Tag → **E panel schedule** = power source
6. Tag → **M6 controls** = integration points and sequence

Keep a **master tag index** for your project: one table, one row per tag, columns for specs / location / system / power / controls / drawing refs / status. Build it from the schedules the day you get them — it pays for itself the first time someone asks "where's FAU-xxx and what feeds it."

## Nameplate vs Schedule

- Schedule = design intent; **nameplate = as-built truth** (actual electrical data, serial, charge, test dates)
- For ordering parts, warranty, or electrical work → the nameplate wins, every time. Photo every nameplate at receipt and at final set
