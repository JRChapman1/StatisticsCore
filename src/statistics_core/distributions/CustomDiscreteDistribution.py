from typing import Callable

from src.statistics_core.distributions.base import DiscreteDistribution


class CustomDiscreteDistribution(DiscreteDistribution):

    def __init__(self, pmf: str, parameters: dict,  state_space: list):
        self.state_space = state_space
        self.__dict__ = self.__dict__ | parameters
        self._pmf = eval('lambda x: ' + pmf)
        print(self._pmf(3))

    def pmf(self, x):
        return self._pmf(x)

    def _calculate_mean(self):
        mu = 0
        for x in self.state_space:
            mu += x * self.pmf(x)
        return mu

    def _calculate_variance(self):
        second_moment = 0
        for x in self.state_space:
            second_moment += x**2 * self.pmf(x)
        return second_moment - self.mean()**2

    def moment(self, n):
        pass

    def sample(self, n):
        pass

    def cdf(self, x):
        cdf = 0
        for x in self.state_space[self.state_space <= x]:
            cdf += self.pmf(x)
        return cdf

    def icdf(self, p):
        q = 0
        for x in self.state_space:
            q += self.pmf(x)
            if q > p:
                return x
        return self.state_space.max()



if __name__ == '__main__':
    import numpy as np
    from math import comb
    from src.statistics_core.distributions.BinomialDistribution import BinomialDistribution
    geo = BinomialDistribution(0.4, 20)
    print(geo.icdf(0.5))

    parameters = {'p': 0.4, 'n': 20}
    pmf_str = '{p} ** x * (1 - {p}) ** ({n} - x) * comb({n}, x)'

    geoc = CustomDiscreteDistribution('self.p ** x * (1 - self.p) ** (self.n - x) * comb(self.n, x)', parameters, np.arange(0, 20))
    print(geoc.icdf(0.5))