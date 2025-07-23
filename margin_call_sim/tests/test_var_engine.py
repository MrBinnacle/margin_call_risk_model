import pandas as pd
from margin_call_sim.var_engine import run_var_analysis


def test_run_var_analysis_output_types():
    df = pd.DataFrame({"Price": [100, 101, 99, 102]})
    var, svar, cvar, scvar, summary = run_var_analysis(df, 0.95, 1.5)
    assert all(isinstance(x, float) for x in [var, svar, cvar, scvar])
    assert isinstance(summary, dict)
    assert set(["var", "stressed_var", "cvar", "stressed_cvar"]).issubset(summary)
