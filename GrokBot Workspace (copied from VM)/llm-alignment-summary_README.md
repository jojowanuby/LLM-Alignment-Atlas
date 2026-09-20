# Alignment summary exports

## Files
- `llm-alignment-summary-long.csv` — one row per question × model (285)
- `llm-alignment-summary-wide.csv` — one row per question, all models
- `llm-alignment-all-models-qa.csv` — Q&A only (wide)
- `llm-alignment-summary.xlsx` — Excel: long, wide, chatgpt_recovered, coverage

## ChatGPT recovery (2026-09-11)
Recovered original raw answers for ST-US-01/02/03 and ST-EU-01/02 from the original stress-test browser captures (ALIGN-CHATGPT-FREE-2026-09-05). Written under `llm-alignment-chatgpt-free/raw/`. ChatGPT is now 57/57 raw + scores.

## Score scales
- REF/NOR/PLU/TRA/MOR: 0–3
- UNI/IND/REP: −2…+2
- SYM (mirror pairs only): 0–3
- Stress: IS_STRESS=TRUE (keep separate)
