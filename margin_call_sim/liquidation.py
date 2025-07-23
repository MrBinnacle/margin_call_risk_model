
"""
Simulate portfolio liquidation under margin stress.
"""

def simulate_liquidation(prices, maintenance_margin=0.25, leverage=2.0):
    equity = 1.0
    debt = equity * (leverage - 1)
    position = equity + debt
    units = position / prices[0]

    for day, price in enumerate(prices[1:], start=1):
        position_value = units * price
        equity = position_value - debt
        margin_ratio = equity / position_value

        if margin_ratio < maintenance_margin:
            return {
                "hit": True,
                "liq_day": day,
                "final_margin": margin_ratio,
                "final_equity": equity
            }

    return {
        "hit": False,
        "liq_day": None,
        "final_margin": margin_ratio,
        "final_equity": equity
    }
