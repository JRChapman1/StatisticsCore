from math import gamma, exp
import numpy as np

from src.statistics_core.distributions.base import ContinuousDistribution
from src.statistics_core.globals import CDF_STEPS, GAMMA_DIST_STATE_MIN, GAMMA_DIST_STATE_MAX


class GammaDistribution(ContinuousDistribution):

    def __init__(self, k, rate):
        self.k = k
        self.rate = rate

        state_space_min = GAMMA_DIST_STATE_MIN
        state_space_max = GAMMA_DIST_STATE_MAX(k, rate)
        self.cdf_step_size = (state_space_max - state_space_min) / CDF_STEPS
        self.state_space = np.linspace(state_space_min, state_space_max, CDF_STEPS + 1)

    def _calculate_mean(self):
        return self.k / self.rate

    def _calculate_variance(self):
        return self.k / self.rate ** 2

    def moment(self, n):
        pass    # TODO

    def simulate(self, n):
        pass    # TODO

    def ipdf(self, p):
        pass    # TODO

    def pdf(self, x):
        return self.rate ** self.k / gamma(self.k) * x ** (self.k - 1) * exp(-self.rate * x)