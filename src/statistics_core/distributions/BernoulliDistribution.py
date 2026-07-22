import numpy as np

from statistics_core.distributions.base import Distribution


class BernoulliDistribution(Distribution):

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
