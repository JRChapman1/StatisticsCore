import numpy as np
from math import ceil, log

from base import DiscreteDistribution


class GeometricDistribution(DiscreteDistribution):

    def __init__(self, p: float) -> None:

        if not 0 <= p <= 1:
            raise ValueError("p must be between 0 and 1")

        self.p = p

    def _calculate_mean(self):
        return 1 / self.p

    def _calculate_variance(self):
        return (1 - self.p) / self.p**2

    def sample(self, n):
        pass

    def cdf(self, x):
        return 1 - (1 - self.p) ** x

    def icdf(self, p):
        return ceil(log(1 - p) / log((1 - self.p)))

    def pmf(self, x):
        return self.p * (1 - self.p) ** (x - 1)

    def moment(self, n):
        raise NotImplementedError()  # TODO