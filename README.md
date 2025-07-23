# 🧠 Margin Call Risk Model

> A narrative-driven financial margin risk simulator — inspired by *Margin Call (2011)* and the 2008 financial crisis.

[![CI](https://github.com/MrBinnacle/margin_call_risk_model/actions/workflows/ci.yml/badge.svg)](https://github.com/MrBinnacle/margin_call_risk_model/actions)
[![Streamlit App](https://img.shields.io/badge/Launch-Streamlit-blue)](https://share.streamlit.io/MrBinnacle/margin_call_risk_model/main/margin_call_sim/app.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📦 What It Does

Simulates real-time **margin call risk**, including:
- Volatility shocks
- Leverage and liquidity effects
- Crisis-specific scenarios
- Fire sale dynamics and VaR failure analysis

---

## 🧰 Key Features

- 🎬 **Lore Mode**: quotes and logic inspired by *Margin Call*
- 🧪 **Scenarios**: crypto flash crashes, credit spirals, QE unwind, and more
- 🧠 **VaR Model Simulation**: daily stress, forced liquidation, recovery chances
- 🎛️ **Streamlit App**: Interactive visualization + scenario builder

---

## 📈 Run the App (Locally)

```bash
pip install -r margin_call_sim/requirements.txt
streamlit run margin_call_sim/app.py
