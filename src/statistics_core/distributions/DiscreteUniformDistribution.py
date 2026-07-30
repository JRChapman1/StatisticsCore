import numpy as np
from math import floor, ceil

from src.statistics_core.distributions.base import DiscreteDistribution


class DiscreteUniformDistribution(DiscreteDistribution):

    def __init__(self, lower: int | float, upper: int | float, num_steps: int) -> None:

        if num_steps < 1:
            raise ValueError("At least 1 step is required")

        if lower >= upper:
            raise ValueError("lower must be less than upper")

        self.lower = lower
        self.upper = upper
        self.num_steps = num_steps
        self.step_size = (upper - lower) / num_steps

    @property
    def _state_space(self) -> np.ndarray:
        return np.linspace(self.lower, self.upper, self.num_steps + 1)

    def _calculate_mean(self) -> float:
        return (self.lower + self.upper) / 2

    def _calculate_variance(self) -> float:
        return self.step_size ** 2 * ((self.num_steps + 1) ** 2 - 1) / 12

    def sample(self, n: int) -> np.ndarray:
        return self.lower + self.step_size * np.random.randint(0, self.num_steps+1, n)

    def pmf(self, x: int | float) -> float:
        if np.any(np.isclose(x, self._state_space)):
            return 1 / (self.num_steps + 1)
        return 0.0

    def cdf(self, x):
        m = floor((x - self.lower) / self.step_size)
        return min(max((m+1) / (self.num_steps+1), 0), 1)

    def icdf(self, p):

        if not 0 < p <= 1:
            raise ValueError(f"Probability p must be greater than 0 and less than or equal to 1, got {p}")

        if p == 1:
            return self.upper

        return self.lower + (ceil((self.num_steps + 1) * p) - 1) * self.step_size

    def moment(self, n):
        raise NotImplementedError() # TODO
