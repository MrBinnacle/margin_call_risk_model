
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from var_engine import run_var_analysis
from config import DEFAULT_CONFIDENCE_LEVEL, DEFAULT_STRESS_MULTIPLIER
from scenario_presets import SCENARIO_PRESETS
from lore_utils import margin_call_lore_leverage_impact, margin_call_lore_intro
import numpy as np

def load_data(uploaded_file) -> pd.DataFrame:
    try:
        df = pd.read_csv(uploaded_file)
        if 'Price' not in df.columns:
            st.error("CSV must contain a 'Price' column.")
            return pd.DataFrame()
        return df
    except Exception as e:
        st.error(f"Failed to read file: {e}")
        return pd.DataFrame()

def generate_simulated_path(df: pd.DataFrame, vol_multiplier: float, drawdown_days: int, recovery_days: int) -> pd.DataFrame:
    prices = df['Price'].copy()
    base_price = prices.iloc[-1]
    returns = prices.pct_change().dropna()
    mean_ret = returns.mean()
    std_ret = returns.std() * vol_multiplier

    crash_returns = np.random.normal(loc=mean_ret - 0.1, scale=std_ret, size=drawdown_days)
    recovery_returns = np.random.normal(loc=mean_ret + 0.02, scale=std_ret / 2, size=recovery_days)
    total_returns = np.concatenate([crash_returns, recovery_returns])
    sim_prices = [base_price]
    for r in total_returns:
        sim_prices.append(sim_prices[-1] * (1 + r))

    return pd.DataFrame({'Day': list(range(len(sim_prices))), 'Simulated Price': sim_prices})


import plotly.graph_objects as go
from var_engine import simulate_liquidation

def display_simulation_plot(sim_data, drawdown_days=5):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=sim_data["Day"], y=sim_data["Simulated Price"], mode="lines+markers", name="Price"))

    liq_day = simulate_liquidation(sim_data["Simulated Price"])
    if liq_day is not None:
        liq_price = sim_data["Simulated Price"].iloc[liq_day]
        fig.add_vline(x=liq_day, line_dash="dash", line_color="red", annotation_text="💥 Liquidation", annotation_position="top left")
        fig.add_trace(go.Scatter(x=[liq_day], y=[liq_price], mode="markers", marker=dict(size=12, color="red"), name="Liquidation"))

    fig.update_layout(title="Simulated Crisis Timeline", xaxis_title="Day", yaxis_title="Price", height=500)
    st.plotly_chart(fig, use_container_width=True)


# 💥 Explainer Panel
with st.expander("📊 What Just Happened?"):
    if stressed_cvar > 0:
        st.markdown(f"**You were margin called on Day `{liq_day}`** when your margin ratio dropped below the required `{params['maintenance_margin']:.2f}`.")
    else:
        st.markdown("**No margin call occurred.** Your leverage and volatility were low enough to avoid liquidation.")
    st.caption("🔍 This simulation shows how leverage amplifies small drops into catastrophic failures.")


# 🧠 Tooltip help
with st.expander("ℹ️ Risk Term Glossary"):
    st.markdown("""
- **VaR**: Value at Risk. The most you can expect to lose, with X% confidence, in a set period.
- **CVaR**: Conditional Value at Risk. The average of losses *worse than* the VaR — the tail risk.
- **Leverage Ratio**: Borrowed capital as a multiple of equity.
- **Margin Call**: If your equity falls below a threshold, your position is forcibly liquidated.
- **Stressed Scenarios**: Simulated events with volatility scaled up.
    """)


def main():
    st.title("📉 Margin Call Risk Model")
    st.markdown("Upload price data (CSV with a 'Price' column) to calculate VaR and visualize forced liquidation under crisis scenarios.")

    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    scenario = st.selectbox("Choose Stress Scenario", list(SCENARIO_PRESETS.keys()))
    params = SCENARIO_PRESETS[scenario]
    confidence = st.slider("Confidence Level", 0.90, 0.99, DEFAULT_CONFIDENCE_LEVEL, 0.01)

    if uploaded_file:
        df = load_data(uploaded_file)
        if not df.empty:
            st.markdown(f"**Scenario Description:** {params['description']}")
            var, stressed_var, cvar, stressed_cvar = run_var_analysis(df, confidence, params['vol_multiplier'])

            st.success(f"VaR at {confidence:.0%} confidence: {var:.4f}")
            st.warning(f"Stressed VaR (x{params['vol_multiplier']}): {stressed_var:.4f}")
st.info(f"CVaR at {confidence:.0%} confidence: {cvar:.4f}")
st.error(f"Stressed CVaR (x{params['vol_multiplier']}): {stressed_cvar:.4f}")

            sim_data = generate_simulated_path(df, params['vol_multiplier'], params['drawdown_days'], params['recovery_days'])
            display_simulation_plot(sim_data, drawdown_days=params['drawdown_days'])

            # Triggered insights
            margin_call_lore_intro()
            if params['vol_multiplier'] >= 3.0:
                margin_call_lore_leverage_impact()

if __name__ == "__main__":
    main()
