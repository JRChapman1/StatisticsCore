import numpy as np
from math import comb, ceil
from functools import cache

from src.statistics_core.distributions.base import DiscreteDistribution


class HypergeometricDistribution(DiscreteDistribution):

    def __init__(self, population_size, population_successes, sample_size) -> None:
        self.N = population_size
        self.k = population_successes
        self.n = sample_size

    def _calculate_mean(self) -> float:
        return self.n * self.k / self.N

    def _calculate_variance(self) -> float:
        return self.n * self.k * (self.N - self.n) * (self.N - self.k) / (self.N**2 * (self.N - 1))

    def simulate(self, num_sims: int) -> np.ndarray:
        # Use numpy's hypergeometric: returns number of successes in draws
        return np.random.hypergeometric(self.k, self.N - self.k, self.n, size=num_sims)

    @cache
    def pmf(self, x: int | float) -> float:
        return comb(self.k, x) * comb(self.N - self.k, self.n - x) / comb(self.N, self.n)

    @cache
    def cdf(self, x):
        from math import floor
        k = int(floor(x))
        if k < 0:
            return 0.0
        # sum pmf up to k
        s = 0.0
        # lower and upper bounds for possible successes
        min_x = max(0, self.n - (self.N - self.k))
        max_x = min(self.n, self.k)
        upper = min(k, max_x)
        for z in range(min_x, upper + 1):
            s += self.pmf(z)
        return min(max(s, 0.0), 1.0)

    def icdf(self, p):
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)
        
        if not 0 <= p <= 1:
            raise ValueError("p must be in [0,1]")
        if p == 0:
            # minimal possible number of successes
            return max(0, self.n - (self.N - self.k))
        cumulative = 0.0
        # iterate over feasible support
        min_x = max(0, self.n - (self.N - self.k))
        max_x = min(self.n, self.k)
        for x in range(min_x, max_x + 1):
            cumulative += self.pmf(x)
            if cumulative >= p:
                return x
        return max_x

    def moment(self, n):
        raise NotImplementedError() # TODO

