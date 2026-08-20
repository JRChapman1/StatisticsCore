import numpy as np
from math import comb, floor
from functools import cache

from src.statistics_core.distributions.base import DiscreteDistribution


class NegativeBinomialDistribution(DiscreteDistribution):

    def __init__(self, p: float, k: int) -> None:
        self.p = p
        self.k = k

    def _calculate_mean(self) -> float:
        return self.k / self.p

    def _calculate_variance(self) -> float:
        # For the parameterization where X is number of trials to get k successes:
        # Var(X) = k * (1 - p) / p^2
        return self.k * (1 - self.p) / (self.p ** 2)

    def simulate(self, num_sims: int) -> np.ndarray:
        raise NotImplementedError() # TODO

    @cache
    def pmf(self, x: int | float) -> float:
        if (x == int(x)) and (x >= self.k):
            return self.p ** self.k * (1 - self.p) ** (x - self.k) * comb(x - 1, self.k - 1)
        return 0.0

    @cache
    def cdf(self, x):
        k = int(floor(x))
        if k < 0:
            return 0.0
        return sum(self.pmf(z) for z in range(0, k + 1))

    def icdf(self, p):
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)
        
        if not 0 <= p <= 1:
            raise ValueError(f"Probability p must be between 0 and 1, got {p}")
        if p == 0:
            return 0
        # for p == 1 the distribution is unbounded but probabilities sum to 1; handle normally
        cumulative = 0.0
        x = 0
        while cumulative < p:
            cumulative += self.pmf(x)
            x += 1
            # safety: stop if x grows very large
            if x > 10**7:
                break
        return x - 1

    def moment(self, n):
        raise NotImplementedError() # TODO

