import random
import math
from typing import List, Dict, Any

class MonteCarloEngine:
    def __init__(self, paths: int = 10000, steps: int = 5):
        self.paths = paths
        self.steps = steps

    def run_simulation(
        self,
        base_value: float,
        mu: float,
        sigma: float,
        portfolio_exposure: float
    ) -> Dict[str, Any]:
        """
        Executes a Monte Carlo simulation using Geometric Brownian Motion with pure Python.
        """
        dt = 1.0  # 1 year steps
        results = []

        for _ in range(self.paths):
            # We only need the final state for each path based on the logic in original code
            # paths_final = base_value * np.exp(total_drift + sigma * random_shocks.sum(axis=1))

            # Replicating the logic: sum of multiple random shocks
            # random_shocks.sum(axis=1) is sum of 'steps' N(0,1) variables
            # Sum of N(0,1) * steps is N(0, sqrt(steps))
            # Wait, the original code had:
            # drift_component = (mu - 0.5 * sigma**2) * time_grid
            # total_drift = drift_component[-1] # which is (mu - 0.5 * sigma**2) * steps

            total_drift = (mu - 0.5 * (sigma**2)) * self.steps

            # sum of 'steps' independent N(0,1) is N(0, sqrt(steps))
            sum_shocks = random.gauss(0, math.sqrt(self.steps))

            path_final = base_value * math.exp(total_drift + sigma * sum_shocks)

            impact_delta = (path_final - 1.0) * portfolio_exposure
            results.append(impact_delta)

        results.sort()

        def get_percentile(data, p):
            idx = int(len(data) * (p / 100))
            return data[min(idx, len(data) - 1)]

        impact_bands = [
            get_percentile(results, 10),
            get_percentile(results, 50),
            get_percentile(results, 90)
        ]

        confidence_intervals = [
            get_percentile(results, 2.5),
            get_percentile(results, 97.5)
        ]

        mean_impact = sum(results) / len(results)
        std_impact = math.sqrt(sum((x - mean_impact)**2 for x in results) / len(results))

        risk_deltas = {
            "acceleration_sensitivity": mean_impact / mu if mu != 0 else 0,
            "uncertainty_exposure": std_impact
        }

        return {
            "impact_bands": impact_bands,
            "risk_deltas": risk_deltas,
            "confidence_intervals": confidence_intervals,
            "mean_impact": mean_impact,
            "max_drawdown": min(results),
            "upside_potential": max(results)
        }

# Singleton instance
engine = MonteCarloEngine()
