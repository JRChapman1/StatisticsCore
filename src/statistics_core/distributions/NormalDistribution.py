from math import exp, sqrt, pi
import numpy as np

from src.statistics_core.distributions.base import ContinuousDistribution
from src.statistics_core.globals import CDF_STEPS, NORM_DIST_STATE_MIN, NORM_DIST_STATE_MAX


class NormalDistribution(ContinuousDistribution):

    def __init__(self, mean: float, variance: float):
        self.mean = mean
        self.variance = variance

        state_space_min = NORM_DIST_STATE_MIN(mean, variance)
        state_space_max = NORM_DIST_STATE_MAX(mean, variance)
        self.cdf_step_size = (state_space_max - state_space_min) / CDF_STEPS
        self.state_space = np.linspace(state_space_min, state_space_max, CDF_STEPS + 1)

    def _calculate_mean(self):
        return self.mean

    def _calculate_variance(self):
        return self.variance

    def simulate(self, n):
        pass

    def ipdf(self, p):
        pass

    def pdf(self, x):
        return 1 / (np.sqrt(2 * pi * self.variance)) * np.exp(-0.5 * (x - self.mean)**2 / self.variance)