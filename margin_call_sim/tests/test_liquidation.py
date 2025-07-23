
import pandas as pd
from margin_call_sim.liquidation import simulate_liquidation

def test_liquidation_trigger_detected():
    prices = pd.Series([100, 80, 60])
    result = simulate_liquidation(prices, leverage=3.0, maintenance_margin=0.25)
    assert result["hit"] is True
    assert result["liq_day"] == 1

def test_no_liquidation_with_low_leverage():
    prices = pd.Series([100, 99, 98, 97, 96])
    result = simulate_liquidation(prices, leverage=1.1, maintenance_margin=0.25)
    assert result["hit"] is False
