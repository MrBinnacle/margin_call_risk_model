"""
Utility functions and dataclass for replaying margin call scenarios.
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class ScenarioSummary:
    var: float
    stressed_var: float
    cvar: float
    stressed_cvar: float
    liq_day: Optional[int]
    hit: bool
    leverage: float
    confidence: float
    vol_multiplier: float

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

def build_scenario_summary(var, stressed_var, cvar, stressed_cvar, liq_day, confidence_level, stress_multiplier, leverage_ratio):
    return ScenarioSummary(
        var=var,
        stressed_var=stressed_var,
        cvar=cvar,
        stressed_cvar=stressed_cvar,
        liq_day=liq_day,
        hit=liq_day is not None,
        leverage=leverage_ratio,
        confidence=confidence_level,
        vol_multiplier=stress_multiplier
    )
