from src.statistics_core.distributions.base import ContinuousDistribution


class ContinuousUniformDistribution(ContinuousDistribution):

    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def _calculate_mean(self):
        return (self.a + self.b) / 2

    def _calculate_variance(self):
        return (self.b - self.a) ** 2 / 12

    def moment(self, n):
        pass    # TODO

    def simulate(self, n):
        pass    # TODO

    def cdf(self, x):
        return (x - self.a) / (self.b - self.a)

    def icdf(self, p):
        return p * (self.b - self.a) + self.a

    def ipdf(self, p):
        pass    # TODO

    def pdf(self, x):
        return 1 / (self.a + self.b)