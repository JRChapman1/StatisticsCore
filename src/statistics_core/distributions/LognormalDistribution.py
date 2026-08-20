import numpy as np
from math import pi, log, sqrt

from src.statistics_core.distributions.base import ContinuousDistribution
from src.statistics_core.distributions.NormalDistribution import NormalDistribution


class LognormalDistribution(ContinuousDistribution):

    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma
        self._normal_dist = NormalDistribution(mu, sigma**2)

    @classmethod
    def from_mean_and_variance(cls, mean: float, variance: float):
        sigma = sqrt(log(1 + variance / mean**2))
        mu = log(mean) - 0.5 * sigma**2
        return cls(mu, sigma)

    def _calculate_mean(self):
        return np.exp(self.mu + 0.5*self.sigma**2)

    def _calculate_variance(self):
        return (np.exp(self.sigma**2) - 1) * np.exp(2 * self.mu + self.sigma**2)

    def moment(self, n):
        pass

    def simulate(self, n):
        pass

    def cdf(self, x):
        return self._normal_dist.cdf(np.log(x))

    def icdf(self, p):
        pass

    def ipdf(self, p):
        pass

    def pdf(self, x):
        return 1 / (x * self.sigma * np.sqrt(2 * pi)) * np.exp( - (np.log(x) - self.mu)**2 / (2 * self.sigma ** 2))