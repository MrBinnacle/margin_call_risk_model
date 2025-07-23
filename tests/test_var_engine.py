
import pytest
import pandas as pd
from var_engine import calculate_var, calculate_stressed_returns, run_var_analysis

def test_calculate_var_basic():
    returns = pd.Series([0.01, -0.02, 0.015, -0.005])
    var = calculate_var(returns, confidence_level=0.95)
    assert isinstance(var, float)

def test_stressed_returns():
    returns = pd.Series([0.01, -0.02, 0.03])
    stressed = calculate_stressed_returns(returns, 2.0)
    assert all(abs(s - r * 2) < 1e-6 for s, r in zip(stressed, returns))

def test_run_var_analysis():
    prices = pd.Series([100, 101, 99, 102])
    df = pd.DataFrame({"Price": prices})
    var, stressed_var, cvar, stressed_cvar = run_var_analysis(df, 0.95, 1.5)
    assert isinstance(var, float)
    assert isinstance(stressed_var, float)


from var_engine import calculate_cvar

def test_calculate_cvar_basic():
    returns = pd.Series([0.01, -0.02, 0.015, -0.005])
    cvar = calculate_cvar(returns, confidence_level=0.95)
    assert isinstance(cvar, float)

def test_run_var_analysis_with_cvar():
    prices = pd.Series([100, 101, 99, 102])
    df = pd.DataFrame({"Price": prices})
    var, stressed_var, cvar, stressed_cvar = run_var_analysis(df, 0.95, 1.5)
    assert all(isinstance(x, float) for x in [var, stressed_var, cvar, stressed_cvar])
