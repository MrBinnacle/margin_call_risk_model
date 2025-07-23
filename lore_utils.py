import streamlit as st

def display_lore_mode():
    lore_explainers = {
        "VaR and Why It Fails": """**Value at Risk (VaR) and Why It Fails**

Value at Risk (VaR) was once the industry gold standard, a seemingly elegant number that promised to quantify financial risk. But as *Margin Call* revealed, it was blind to extreme events and built entirely on historical data — like driving while only looking in the rearview mirror.

VaR collapses when volatility spikes or correlations break. It gave firms a false sense of safety and enabled dangerous leverage, directly fueling collapses like the ones simulated here.""",
        "What Triggers a Margin Call": """**What Actually Triggers a Margin Call**

A margin call isn’t about total loss — it’s about breaching the broker’s required equity ratio. When your position falls too far, too fast, you’re forced to sell — often at the worst moment.

This simulator lets you see *exactly* when that happens — before your broker does.""",
        "The Broker Floor Illusion": """**The Broker Floor Illusion**

Brokers set thresholds — 25%, 30% — that feel fixed. But in reality, they shift with volatility, correlation, and liquidity.

This simulator exposes how fast your buffer disappears, even when you think you're safe. The market doesn't wait for your comfort zone."""
    }

    st.markdown("### 📚 Lore Mode: Systemic Risk Context")
    for title, content in lore_explainers.items():
        with st.expander(f"🔍 {title}"):
            st.markdown(content)