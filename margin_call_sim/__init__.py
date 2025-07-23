"""Top-level package for the Margin Call Simulator."""

from .var_engine import run_var_analysis
from .liquidation import simulate_liquidation
from .replay_utils import build_scenario_summary, ScenarioSummary
from .config import (
    DEFAULT_CONFIDENCE_LEVEL,
    DEFAULT_STRESS_MULTIPLIER,
    DEFAULT_LEVERAGE_RATIO,
    DEFAULT_MAINTENANCE_MARGIN,
    LORE_MODE,
)

__all__ = [
    "run_var_analysis",
    "simulate_liquidation",
    "build_scenario_summary",
    "ScenarioSummary",
    "DEFAULT_CONFIDENCE_LEVEL",
    "DEFAULT_STRESS_MULTIPLIER",
    "DEFAULT_LEVERAGE_RATIO",
    "DEFAULT_MAINTENANCE_MARGIN",
    "LORE_MODE",
]

__version__ = "1.1.1"
