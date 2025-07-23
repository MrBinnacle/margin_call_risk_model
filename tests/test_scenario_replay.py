
import pandas as pd
import json
from margin_call_project.var_engine import run_var_analysis

def test_scenario_summary_keys():
    returns = [-0.02, 0.01, -0.03, 0.04, -0.05]
    prices = [100]
    for r in returns * 10:
        prices.append(prices[-1] * (1 + r))
    df = pd.DataFrame({"Price": prices})

    var, stressed_var, cvar, stressed_cvar, summary = run_var_analysis(df, 0.95, 1.5)

    assert isinstance(summary, dict)
    assert "liq_day" in summary
    assert "var" in summary
    assert "hit" in summary
    assert summary["confidence"] == 0.95
    assert summary["vol_multiplier"] == 1.5

    # Serialize the summary for future replay
    with open("/mnt/data/replay_summary.json", "w") as f:
        json.dump(summary, f)

    # Validate reload works
    with open("/mnt/data/replay_summary.json") as f:
        reloaded = json.load(f)
        assert reloaded["hit"] == summary["hit"]
        assert reloaded["liq_day"] == summary["liq_day"]
