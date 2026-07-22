import numpy as np

from statistics_core.distributions.base import Distribution


class DiscreteUniformDistribution(Distribution):

    def __init__(self, lower: int | float, upper: int | float, step: int | float) -> None:

        if step <= 0:
            raise ValueError("step must be positive")

        if lower > upper:
            raise ValueError("lower must be less than upper")

        self.lower = lower
        self.upper = upper
        self.step = step
        self._k = (upper - lower) / step + 1

    def _calculate_mean(self):
        return (self.lower + self.upper) / 2

    def _calculate_variance(self):
        return self.step ** 2 * (self._k**2 - 1) / 12

    def sample(self, n):
        return self.lower + self.step * np.random.randint(1, self._k, n)
