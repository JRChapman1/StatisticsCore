import numpy as np
from math import factorial, exp, ceil
from functools import cache

from src.statistics_core.distributions.base import DiscreteDistribution


class PoissonDistribution(DiscreteDistribution):

    def __init__(self, rate: float) -> None:
        self.rate = rate

    def _calculate_mean(self) -> float:
        return self.rate

    def _calculate_variance(self) -> float:
        return self.rate

    def simulate(self, num_sims: int) -> np.ndarray:
        # Use numpy's poisson RNG
        return np.random.poisson(self.rate, size=num_sims)

    @cache
    def pmf(self, x: int | float) -> float:
        # validate domain: x must be integer >= 0
        if x != int(x) or x < 0:
            return 0.0
        x = int(x)
        return self.rate**x * exp(-self.rate) / factorial(x)

    @cache
    def cdf(self, x):
        from math import floor
        k = int(floor(x))
        if k < 0:
            return 0.0
        # sum pmf from 0..k
        s = 0.0
        for i in range(0, k + 1):
            s += self.pmf(i)
        return min(max(s, 0.0), 1.0)

    def icdf(self, p):
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            # vectorized operation for arrays
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)
        
        # scalar case
        if not 0 <= p <= 1:
            raise ValueError(f"Probability p must be between 0 and 1, got {p}")
        if p == 0:
            return 0
        cumulative = 0.0
        x = 0
        while cumulative < p:
            cumulative += self.pmf(x)
            x += 1
            # safety break for pathological cases
            if x > 10**7:
                break
        return x - 1

    def moment(self, n):
        raise NotImplementedError() # TODO

    def mode(self):
        return ceil(self.rate - 1)
