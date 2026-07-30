import numpy as np
from math import factorial, exp
from functools import cache

from src.statistics_core.distributions.base import DiscreteDistribution


class PoissonDistribution(DiscreteDistribution):

    def __init__(self, rate: float) -> None:
        self.rate = rate

    def _calculate_mean(self) -> float:
        return self.rate

    def _calculate_variance(self) -> float:
        return self.rate

    def sample(self, num_sims: int) -> np.ndarray:
        raise NotImplementedError() # TODO

    @cache
    def pmf(self, x: int | float) -> float:
        return self.rate**x * exp(-self.rate) / factorial(x)

    @cache
    def cdf(self, x):
        pass

    def icdf(self, p):
        pass

    def moment(self, n):
        raise NotImplementedError() # TODO

