import numpy as np
from math import floor

from src.statistics_core.distributions.base import DiscreteDistribution


class BernoulliDistribution(DiscreteDistribution):

    def __init__(self, p: float) -> None:

        if not 0<= p <= 1:
            raise ValueError("p must be between 0 and 1")

        self.p = p

    def _calculate_mean(self):
        return self.p

    def _calculate_variance(self):
        return self.p * (1 - self.p)

    def sample(self, n):
        successes = np.random.uniform(low=0.0, high=1.0, size=n) <= self.p
        return np.where(successes, 1, 0)

    def cdf(self, x):
        if floor(x) <= 0:
            return 1 - self.p
        return 1.0

    def icdf(self, p):
        if p < self.p:
            return 0
        else:
            return 1

    def pmf(self, x):
        if x == 0:
            return 1 - self.p
        elif x == 1:
            return self.p
        else:
            return 0
            
    def moment(self, n):
        raise NotImplementedError() # TODO