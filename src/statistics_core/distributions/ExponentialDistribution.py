from math import exp

from src.statistics_core.distributions.GammaDistribution import GammaDistribution


class ExponentialDistribution(GammaDistribution):

    def __init__(self, rate):
        super().__init__(1, rate)

    def moment(self, n):
        pass    # TODO (inherit?)

    def cdf(self, x):
        return 1 - exp(-self.rate * x)

    def icdf(self, p):
        pass    # TODO

    def ipdf(self, p):
        pass    # TODO (inherit?)
