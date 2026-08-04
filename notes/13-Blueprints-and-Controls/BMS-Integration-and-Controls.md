# BMS, Integration & Controls — What Talks to What

*How buildings get wired into a brain: protocols, points, panels, and the field realities of integration work.*

## The Layers

1. **Field devices** — sensors, valves, dampers, VFDs, leak-detection rope, thermostats
2. **DDC controllers** — panels (usually in/near the mech room or on the unit) that read inputs and drive outputs
3. **Supervisory layer** — the BMS front end ( Niagara, Desigo, Metasys, etc.): graphics, trends, alarms, schedules
4. **EPMS** (data centers) — Electrical Power Monitoring System: switchgear, UPS, PDU, generators. Separate from BMS but often integrated into the same dashboard/DCIM

Rule of thumb: **BMS watches mechanical, EPMS watches electrical, DCIM watches both + IT load.**

## Protocols You'll Meet

| Protocol | What it looks like | Field notes |
|---|---|---|
| **BACnet MS/TP** | 2-wire shielded serial trunk, daisy-chained | MAC address on each device (often a sticker/dial); EOL/termination resistors at trunk ends; NEVER break a live trunk mid-chain without telling controls — everything downstream drops |
| **BACnet/IP** | Over the building's controls network (Ethernet) | Device instances + IP plan; IT-managed switches — coordinate before unplugging anything |
| **Modbus RTU/TCP** | Serial or IP, common on chillers, VFDs, power meters | Register maps in the IOM; wrong register offset = nonsense values |
| **Gateways** | Boxes translating chiller/pump/CRAH native protocols to BACnet | The gateway config is the integration — document it |

## Points Lists — Reading the Integration Map

- **AI/AO** = analog in/out (temps, pressures, valve position 0–10V/4–20mA) · **DI/DO** = digital in/out (status, alarms, enable) · **AV/BV** = software setpoints
- **Monitored** vs **commanded**: knowing a point is read-only vs writable tells you what the BMS can actually DO to the machine
- Typical FAU/CRAH points: supply/return air temp, fan status + speed command, CHW valve position + command, filter differential-pressure alarm, leak detection, condensate float
- Typical chiller points: enable, leaving-water setpoint, % load, status, alarm, demand limit — often via gateway, read the IOM's comm section

## Controls Drawings (M6) vs Mechanical Drawings

- **Controls schematics** show points per equipment (one diagram per system type) — the tag on the schematic matches the equipment tag on the M2 plan
- **Network riser diagrams** show the trunk architecture: which panels on which MS/TP trunk, which switch, which gateway
- **Sequences of operation** = the written logic (in spec or on M6 sheets): what happens on call for cooling, failure, alarm. The sequence is the law for how the system should behave

## Data-Center Specifics

- CRAH/FAU rows usually on MS/TP trunks per room/row; CDUs and chillers integrated via gateway or BACnet/IP
- Leak-detection rope reports zone alarms to BMS — know the zone map before water finds you first
- Hot/cold aisle temp sensors drive CRAH fan/valve response — don't block or relocate them casually
- EPMS and BMS alarms feed 24/7 monitoring — an unexpected alarm from your work area gets a phone call. Tell the control room BEFORE testing

## Field Integration Etiquette (keeps you employed)

- Photo every panel interior, MAC label, and termination BEFORE touching
- Land wires per the controls submittal, landed and labeled both ends
- Never power-cycle a DDC panel without knowing what's on it — it may serve equipment outside your area
- Points checkout is witnessed: have the point list in hand, verify one point at a time, document pass/fail
