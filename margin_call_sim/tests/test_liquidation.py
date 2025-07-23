
import pandas as pd
from var_engine import simulate_liquidation

def test_liquidation_trigger_detected():
    prices = pd.Series([100, 95, 90, 85, 70, 60, 50, 40])
    liq_day = simulate_liquidation(prices, leverage_ratio=3.0, maintenance_margin=0.25)
    assert isinstance(liq_day, int)
    assert 0 <= liq_day < len(prices)

def test_no_liquidation_with_low_leverage():
    prices = pd.Series([100, 99, 98, 97, 96])
    liq_day = simulate_liquidation(prices, leverage_ratio=1.1, maintenance_margin=0.25)
    assert liq_day is None

def test_edge_liquidation_on_exact_margin_hit():
    prices = pd.Series([400, 300, 250, 200])  # Triggers at 200 with 50 equity, 0.25 margin
    liq_day = simulate_liquidation(prices, leverage_ratio=2.0, maintenance_margin=0.25)
    assert isinstance(liq_day, int)
    assert liq_day == 2

def test_liquidation_on_first_day_crash():
    prices = pd.Series([100, 60])
    liq_day = simulate_liquidation(prices, leverage_ratio=3.0)
    assert liq_day == 1

def test_no_liquidation_with_recovery():
    prices = pd.Series([100, 90, 80, 85, 100])
    liq_day = simulate_liquidation(prices, leverage_ratio=1.8)
    assert liq_day is None

def test_slow_decline_never_triggers():
    prices = pd.Series([100, 99, 98, 97, 96])
    liq_day = simulate_liquidation(prices, leverage_ratio=1.5)
    assert liq_day is None
