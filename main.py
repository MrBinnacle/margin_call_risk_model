
def generate_lore(summary, leverage, stress):
    if summary["hit"]:
        return f"""
💣 **Liquidation Alert**

- 🧪 Stress Multiplier: **{stress}x**
- ⚖️ Leverage Ratio: **{leverage}x**
- 📉 Breach occurred on **Day {summary['liq_day']}**
- 🟥 Margin ratio fell below **{summary['margin_threshold']:.1%}**

Stay sharp, trader. One stress too far.
"""
    else:
        return f"""
🛡️ **Portfolio Survived**

- 🧪 Stress Multiplier: **{stress}x**
- ⚖️ Leverage Ratio: **{leverage}x**
- 📈 Worst drawdown: **{summary['min_margin']:.1%}**
- ✅ No liquidation during simulation

Zen mode: activated.
"""


import json

import altair as alt
import pandas as pd
import streamlit as st

from margin_call_sim.var_engine import run_var_analysis

st.set_page_config(page_title="📉 Margin Call Simulator Dashboard", layout="wide")
st.title("📉 Margin Call Simulator Dashboard")

with st.sidebar:
    st.header("🛠️ Simulation Settings")
    narrator_mode = st.checkbox("🧙 Grimoire Narrator Mode")
    if st.checkbox("🔤 Dyslexia-Friendly Mode"):
        st.markdown('''
<link href="https://fonts.cdnfonts.com/css/open-dyslexic" rel="stylesheet">
<style>
body, * {
    font-family: 'OpenDyslexic', sans-serif !important;
}
</style>
''', unsafe_allow_html=True)
    confidence = st.slider("Confidence Level", 0.90, 0.99, 0.95, step=0.01)
    stress = st.slider("Stress Multiplier", 1.0, 2.5, 1.5, step=0.1)
    leverage = st.slider("Leverage Ratio", 1.0, 5.0, 2.0, step=0.1)
    lore_mode = st.toggle("🧠 Lore Mode")

uploaded_file = st.file_uploader("📤 Upload CSV with 'Price' column", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    if "Price" not in df.columns:
        st.error("CSV must contain 'Price' column")
    else:
        st.success("✅ File uploaded successfully.")
        st.dataframe(df.head())

        if st.button("Run Simulation"):
            var, svar, cvar, scvar, summary = run_var_analysis(df, confidence, stress)
            liq_day = summary["liq_day"]

            # Plot with Altair
            st.subheader("📈 Price Simulation")
            df["Day"] = range(len(df))
            chart = alt.Chart(df).mark_line().encode(
                x="Day:Q",
                y="Price:Q"
            )
            if liq_day is not None:
                liq_rule = alt.Chart(pd.DataFrame({"liq_day": [liq_day]})).mark_rule(color="red").encode(
                    x="liq_day:Q"
                )
                chart += liq_rule

            st.altair_chart(chart, use_container_width=True)

            # Metrics
            st.subheader("📊 Risk Metrics")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("VaR", f"{var:.4f}")
            col2.metric("Stressed VaR", f"{svar:.4f}")
            col3.metric("CVaR", f"{cvar:.4f}")
            col4.metric("Stressed CVaR", f"{scvar:.4f}")

            # Summary
            st.subheader("🧾 Replay Summary")
            st.json(summary)
            st.download_button("Download Summary", json.dumps(summary), "summary.json")

            if lore_mode:
                st.subheader("📚 Narrative")
                st.markdown(generate_lore(summary, leverage, stress))

            if narrator_mode:
                if summary["hit"]:
                    st.markdown(
                        f"💀 *Day {summary['liq_day']}. The reckoning came swift. Liquidation struck like lightning.*"
                    )
                else:
                    st.markdown(
                        "*🛡️ Your positions stood firm. No call from the void.*"
                    )

else:
    st.info("👈 Upload a CSV file to begin.")
