import numpy as np
from src.statistics_core.distributions.BernoulliDistribution import BernoulliDistribution
from src.statistics_core.distributions.BinomialDistribution import BinomialDistribution
from src.statistics_core.distributions.GeometricDistribution import GeometricDistribution
from src.statistics_core.distributions.PoissonDistribution import PoissonDistribution
from src.statistics_core.distributions.NegativeBinomialDistribution import NegativeBinomialDistribution
from src.statistics_core.distributions.HypergeometricDistribution import HypergeometricDistribution
from src.statistics_core.distributions.CustomDiscreteDistribution import CustomDiscreteDistribution
from math import comb

def run():
    print('--- Bernoulli ---')
    d = BernoulliDistribution(0.3)
    print('pmf 0,1,2:', d.pmf(0), d.pmf(1), d.pmf(2))
    print('cdf -1,0,0.5,1,2:', [d.cdf(x) for x in [-1, 0, 0.5, 1, 2]])
    print('icdf 0,0.2,0.7,1:', [d.icdf(q) for q in [0, 0.2, 0.7, 1]])

    print('\n--- Binomial ---')
    b = BinomialDistribution(0.4, 5)
    print('pmf 0..5:', [b.pmf(i) for i in range(6)])
    print('cdf(2):', b.cdf(2))
    print('icdf(0.5):', b.icdf(0.5))

    print('\n--- Geometric ---')
    g = GeometricDistribution(0.3)
    print('pmf 1..4:', [g.pmf(i) for i in range(1,5)])
    print('sample(5):', g.simulate(5))
    print('icdf 0.5:', g.icdf(0.5))

    print('\n--- Poisson ---')
    p = PoissonDistribution(3.0)
    print('pmf 0..5:', [p.pmf(i) for i in range(6)])
    print('cdf(3):', p.cdf(3))
    print('icdf(0.5):', p.icdf(0.5))

    print('\n--- Negative Binomial ---')
    nb = NegativeBinomialDistribution(0.4, 3)
    print('pmf k..k+4:', [nb.pmf(i) for i in range(3, 8)])
    print('cdf(5):', nb.cdf(5))
    print('icdf(0.5):', nb.icdf(0.5))

    print('\n--- Hypergeometric ---')
    hg = HypergeometricDistribution(20, 7, 5)
    print('pmf sample range:', [hg.pmf(i) for i in range(0, 6)])
    print('cdf(2):', hg.cdf(2))
    print('icdf(0.5):', hg.icdf(0.5))

    print('\n--- CustomDiscrete (Binomial-like) ---')
    params = {'p': 0.4, 'n': 5}
    pmf_str = 'self.p ** x * (1 - self.p) ** (self.n - x) * comb(self.n, x)'
    cd = CustomDiscreteDistribution(pmf_str, params, np.arange(0, 6))
    print('custom pmf 0..5:', [cd.pmf(i) for i in range(6)])
    print('custom icdf(0.5):', cd.icdf(0.5))
    print('custom sample(5):', cd.simulate(5))

if __name__ == '__main__':
    run()

