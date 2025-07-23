
from margin_call_sim.config import DEFAULT_LEVERAGE_RATIO, DEFAULT_CONFIDENCE_LEVEL, DEFAULT_STRESS_MULTIPLIER
from margin_call_sim.replay_utils import build_scenario_summary
from margin_call_sim.liquidation import simulate_liquidation
import numpy as np

def run_var_analysis(prices_df, confidence_level=DEFAULT_CONFIDENCE_LEVEL, stress_multiplier=DEFAULT_STRESS_MULTIPLIER):
    prices = prices_df["Price"].values
    returns = np.diff(prices) / prices[:-1]
    simulated_returns = np.random.choice(returns, size=1000, replace=True)
    stressed_returns = simulated_returns * stress_multiplier

    simulated_prices = [prices[-1]]
    for r in simulated_returns:
        simulated_prices.append(simulated_prices[-1] * (1 + r))

    var = np.percentile(simulated_returns, (1 - confidence_level) * 100)
    stressed_var = np.percentile(stressed_returns, (1 - confidence_level) * 100)
    cvar = simulated_returns[simulated_returns <= var].mean()
    stressed_cvar = stressed_returns[stressed_returns <= stressed_var].mean()

    liq_day = simulate_liquidation(simulated_prices)
    summary = build_scenario_summary(
        var, stressed_var, cvar, stressed_cvar,
        liq_day, confidence_level, stress_multiplier, DEFAULT_LEVERAGE_RATIO
    )

    return var, stressed_var, cvar, stressed_cvar, summary.to_dict()
