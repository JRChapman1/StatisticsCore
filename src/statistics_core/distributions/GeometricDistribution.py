import numpy as np
from math import ceil, log

from src.statistics_core.distributions.base import DiscreteDistribution


class GeometricDistribution(DiscreteDistribution):

    def __init__(self, p: float) -> None:

        if not 0 < p <= 1:
            raise ValueError("p must be in (0, 1]")

        self.p = p

    def _calculate_mean(self):
        return 1 / self.p

    def _calculate_variance(self):
        return (1 - self.p) / self.p**2

    def simulate(self, n):
        # Use inverse transform sampling: for U ~ Uniform(0,1), X = ceil(log(1-U)/log(1-p))
        u = np.random.random(n)
        # log(1-p) < 0, so division gives positive values
        return np.ceil(np.log(1 - u) / np.log(1 - self.p)).astype(int)

    def cdf(self, x):
        return 1 - (1 - self.p) ** x

    def icdf(self, p):
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)
        
        if not 0 <= p <= 1:
            raise ValueError("p must be in [0,1]")
        if p == 0:
            return 0
        if p == 1:
            return float('inf')
        return int(ceil(log(1 - p) / log(1 - self.p)))

    def pmf(self, x):
        return self.p * (1 - self.p) ** (x - 1)

    def moment(self, n):
        raise NotImplementedError()  # TODO