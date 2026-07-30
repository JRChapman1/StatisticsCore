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

    def sample(self, num_sims: int) -> np.ndarray:
        raise NotImplementedError() # TODO

    @cache
    def pmf(self, x: int | float) -> float:
        return comb(self.k, x) * comb(self.N - self.k, self.n - x) / comb(self.N, self.n)

    @cache
    def cdf(self, x):
        pass

    def icdf(self, p):
        pass

    def moment(self, n):
        raise NotImplementedError() # TODO

