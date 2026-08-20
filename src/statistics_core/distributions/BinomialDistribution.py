import numpy as np
from math import comb, floor
from functools import cache

from src.statistics_core.distributions.base import DiscreteDistribution


class BinomialDistribution(DiscreteDistribution):

    def __init__(self, p: float, n: int) -> None:
        self.p = p
        self.n = n

    @property
    def _state_space(self) -> np.ndarray:
        return np.arange(0, self.n + 1)

    def _calculate_mean(self) -> float:
        return self.p * self.n

    def _calculate_variance(self) -> float:
        return self.n * self.p * (1 - self.p)

    def simulate(self, num_sims: int) -> np.ndarray:
        successes = np.random.random((num_sims, self.n)) <= self.p
        return np.where(successes, 1, 0).sum(axis=1)

    @cache
    def pmf(self, x: int | float) -> float:
        if (x == int(x)) and (0 <= x <= self.n):
            return self.p ** x * (1 - self.p) ** (self.n - x) * comb(self.n, x)
        return 0.0

    @cache
    def cdf(self, x):
        # Sum pmf from 0 up to floor(x) inclusive
        k = int(floor(x))
        if k < 0:
            return 0.0
        if k >= self.n:
            return 1.0
        return sum(self.pmf(z) for z in range(0, k + 1))

    def icdf(self, p):
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)
        
        if not 0 <= p <= 1:
            raise ValueError(f"Probability p must be between 0 and 1, got {p}")
        if p == 0:
            return 0
        if p == 1:
            return self.n
        cumulative = 0.0
        x = 0
        while cumulative < p and x <= self.n:
            cumulative += self.pmf(x)
            x += 1
        return x - 1

    def moment(self, n):
        raise NotImplementedError() # TODO

if __name__ == '__main__':
    d = BinomialDistribution(0.7, 100)
    print(d.icdf(0.5))
