from math import gamma

from src.statistics_core.distributions.base import ContinuousDistribution


class BetaDistribution(ContinuousDistribution):

    def __init__(self, alpha, beta):
        self.alpha = alpha
        self.beta = beta

    def _calculate_mean(self):
        return self.alpha / (self.alpha + self.beta)

    def _calculate_variance(self):
        return (self.alpha * self.beta) / ((self.alpha + self.beta)**2 * (self.alpha + self.beta + 1))

    def moment(self, n):
        pass    # TODO

    def simulate(self, n):
        pass    # TODO

    def cdf(self, x):
        pass    # TODO

    def icdf(self, p):
        pass    # TODO

    def ipdf(self, p):
        pass    # TODO

    def pdf(self, x):
        return x ** (self.alpha - 1) * (1 - x) ** (self.beta - 1) / self._beta

    @property
    def _beta(self):
        return gamma(self.alpha) * gamma(self.beta) / gamma(self.alpha + self.beta)