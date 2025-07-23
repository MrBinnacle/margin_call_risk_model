# 📦 Release Notes – Margin Call Risk Toolkit FINAL_CLEAN

**Version:** v1.0-final  
**Date:** 2025-07-22  
**Maintainer:** [Your Name or Team]

---

## ✅ Major Enhancements

### 🎯 Narrative Simulation Engine
- Full Lore Mode support added via `lore_utils.py`
- Three cinematic explainers embedded:
  - "VaR and Why It Fails"
  - "What Triggers a Margin Call"
  - "The Broker Floor Illusion"
- Toggle-enabled interface for immersive, educational sidebars

### 🧪 Scenario Expansion
- New simulation presets added to `scenario_presets.py`:
  - Evergrande Unwinding
  - Archegos Collapse
  - Crypto Flash Crash
  - Post-Rate-Hike ETF Implosion
  - Modern Bank Run (Digital Panic)

### 🖥️ UI + UX Enhancements
- Streamlit toggles and layout support
- Updated field labels for clarity
- Lore mode dynamically injects explainer content into UI
- Improved visual hierarchy for scenarios

### 🧱 Structural Improvements
- Modular codebase (`app.py`, `cli.py`, `config.py`, etc.)
- Replit + Streamlit config ready
- GitHub-compliant structure (`README.md`, `LICENSE`, `CONTRIBUTING.md`, `.gitignore`, `/tests/`)
- Unit test added for `var_engine.py`

### 📁 Assets & Collateral
- `/images/` folder added for badge + certificate placeholders
- Clean placeholder files for:
  - `badge_margin_survival_certified.png`
  - `certificate_shell.pdf`

---

## 🚀 Ready For:
- Local testing via `streamlit run main.py`
- CLI-based scenario runs via `cli.py`
- Gumroad packaging and async onboarding flow
- GitHub public release