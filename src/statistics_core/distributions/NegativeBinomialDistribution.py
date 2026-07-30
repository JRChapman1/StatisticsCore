import numpy as np
from math import comb, ceil
from functools import cache

from src.statistics_core.distributions.base import DiscreteDistribution


class NegativeBinomialDistribution(DiscreteDistribution):

    def __init__(self, p: float, k: int) -> None:
        self.p = p
        self.k = k

    def _calculate_mean(self) -> float:
        return self.k / self.p

    def _calculate_variance(self) -> float:
        return self.k * (self.k + 1) / self.p ** 2

    def sample(self, num_sims: int) -> np.ndarray:
        raise NotImplementedError() # TODO

    @cache
    def pmf(self, x: int | float) -> float:
        if (x == int(x)) and (x >= self.k):
            return self.p ** self.k * (1 - self.p) ** (x - self.k) * comb(x - 1, self.k - 1)
        return 0.0

    @cache
    def cdf(self, x):
        return sum([self.pmf(z) for z in range(0, ceil(x))])

    def icdf(self, p):
        if not 0 < p <= 1:
            raise ValueError(f"Probability p must be greater than 0 and less than or equal to 1, got {p}")
        q = 0
        x = 0
        while q <= p:
            q += self.pmf(x)
            x += 1
        return x - 1

    def moment(self, n):
        raise NotImplementedError() # TODO

