import numpy as np

from src.statistics_core.distributions.base import DiscreteDistribution


class BernoulliDistribution(DiscreteDistribution):

    def __init__(self, p: float) -> None:

        if not 0<= p <= 1:
            raise ValueError("p must be between 0 and 1")

        self.p = p

    def _calculate_mean(self):
        return self.p

    def _calculate_variance(self):
        return self.p * (1 - self.p)

    def simulate(self, n):
        successes = np.random.uniform(low=0.0, high=1.0, size=n) <= self.p
        return np.where(successes, 1, 0)

    def cdf(self, x):
        # CDF for Bernoulli: P(X <= x) = 0 for x < 0; = 1-p for 0 <= x < 1; = 1 for x >= 1
        if x < 0:
            return 0.0
        if x < 1:
            return 1.0 - self.p
        return 1.0

    def icdf(self, p):
        # inverse CDF (quantile): smallest x such that CDF(x) >= p
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)
        
        if not 0 <= p <= 1:
            raise ValueError("p must be between 0 and 1")
        if p <= 1.0 - self.p:
            return 0
        return 1

    def pmf(self, x):
        if x == 0:
            return 1 - self.p
        elif x == 1:
            return self.p
        else:
            return 0
            
    def moment(self, n):
        raise NotImplementedError() # TODO