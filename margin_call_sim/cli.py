import argparse
import pandas as pd
import logging

# ✅ FIXED IMPORT PATHS (use absolute module imports within the package)
from margin_call_sim.var_engine import run_var_analysis
from margin_call_sim.config import DEFAULT_CONFIDENCE_LEVEL, DEFAULT_STRESS_MULTIPLIER

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main(args=None):
    parser = argparse.ArgumentParser(description="Margin Call Risk Model CLI")
    parser.add_argument("--file", required=True, help="Path to CSV file with 'Price' column")
    parser.add_argument("--confidence", type=float, default=DEFAULT_CONFIDENCE_LEVEL,
                        help="Confidence level for VaR calculation (e.g., 0.95)")
    parser.add_argument("--stress", type=float, default=DEFAULT_STRESS_MULTIPLIER,
                        help="Stress multiplier (e.g., 1.5)")
    parsed = parser.parse_args(args)

    try:
        df = pd.read_csv(parsed.file)
        if 'Price' not in df.columns:
            raise ValueError("Input file must contain a 'Price' column.")

        var, stressed_var = run_var_analysis(df, parsed.confidence, parsed.stress)
        print(f"VaR ({parsed.confidence:.0%}): {var:.4f}")
        print(f"Stressed VaR (x{parsed.stress}): {stressed_var:.4f}")

    except Exception as e:
        logger.error(f"Failed to run analysis: {e}")
        exit(1)

if __name__ == "__main__":
    main()
