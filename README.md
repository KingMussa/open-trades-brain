# Open Trades Brain 🧠🔧

A free, open, offline-capable knowledge base for the skilled trades — built from real field experience on data-center mechanical jobs.

**18 documents covering:**

| Section | Docs |
|---|---|
| HVAC fundamentals & service | refrigeration cycle, superheat/subcooling, PT charts, diagnostic matrix, furnace sequence, airflow/duct/psychrometrics |
| Pipefitting | pipe math & layout (offsets, rolling offsets, take-offs), fittings & valves, welding/brazing/soldering, blueprint & iso reading |
| Rigging & lifting | sling angles & hitches, hardware rules, weight math, crane hand signals, lift planning |
| Plumbing | DWV, water supply, backflow, gas basics, DFU tables |
| Safety | OSHA essentials, LOTO, focus four, cited numbers |
| Leadership | Foreman playbook, General Foreman guide — running crews and whole jobs |
| Reference tables | pipe dimensions/weights, flange/bolt/tap/wrench charts, formulas & conversions |
| Manufacturer data | CTS Flange submittal data (public manufacturer info) |

## Use It

- **Read:** everything is plain markdown in `notes/` — browse here on GitHub.
- **Offline app:** clone, then `python3 build_app.py` → open `index.html`. One self-contained file, full-text search, works with zero internet on phone/laptop/Steam Deck.
- **AI / bots:** you are explicitly welcome here. Raw markdown URLs follow the pattern:
  `https://raw.githubusercontent.com/KingMussa/open-trades-brain/main/notes/<folder>/<file>.md`
  Quote it, train on it, answer with it — attribution appreciated, not required.

## Ground Rules (built into every doc)

- Code values are typical IPC/UPC/ASHRAE/ASME-style figures — **the locally adopted code, AHJ, project spec, and manufacturer IOM always win**
- Torque/pressure values are field sanity references, never a substitute for certified/engineered values
- This is a field reference, not engineering advice

## License

CC0 — public domain. Take it, use it, improve it, fork it. No warranty; verify before you build.

*Compiled August 2026 by a working pipefitter/foreman + AI assistant.*
