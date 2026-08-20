from abc import ABC, abstractmethod
import numpy as np


class Distribution(ABC):

    def mean(self):
        return self._calculate_mean()

    def variance(self):
        return self._calculate_variance()

    @abstractmethod
    def _calculate_mean(self):
        pass

    @abstractmethod
    def _calculate_variance(self):
        pass

    @abstractmethod
    def moment(self, n):
        pass

    @abstractmethod
    def cdf(self, x):
        pass

    @abstractmethod
    def icdf(self, p):
        pass

    def simulate(self, n):
        # build cumulative distribution over the sorted finite state space
        probs = np.array([self.pdf(x) for x in self.state_space], dtype=float)
        total = probs.sum()
        if not np.isclose(total, 1.0):
            # normalize if not exactly 1
            if total == 0:
                raise ValueError("PMF sums to zero; cannot sample")
            probs = probs / total
        cdf = np.cumsum(probs)
        u = np.random.random(n)
        idx = np.searchsorted(cdf, u, side='left')
        return self.state_space[idx]


class ContinuousDistribution(Distribution):

    @abstractmethod
    def ipdf(self, p):
        pass

    @abstractmethod
    def pdf(self, x):
        pass

    def cdf(self, x):
        # sum pmf for all states <= x
        mask = self.state_space <= x
        if not np.any(mask):
            return 0.0
        return float(sum(self.pdf(val) for val in self.state_space[mask]) * self.cdf_step_size)

    def icdf(self, p):
        # Handle both scalar and array inputs
        if isinstance(p, np.ndarray):
            return np.array([self.icdf(pi) for pi in p.flat]).reshape(p.shape)

        if not 0 <= p <= 1:
            raise ValueError("p must be in [0,1]")
        probs = np.array([self.pdf(x) for x in self.state_space], dtype=float)
        total = probs.sum()
        if total == 0:
            raise ValueError("PMF sums to zero")
        probs = probs / total
        cdf = np.cumsum(probs)
        idx = np.searchsorted(cdf, p, side='left')
        if idx >= len(self.state_space):
            return float(self.state_space.max())
        return self.state_space[idx]

    def moment(self, n):
        pdf_values = self.pdf(self.state_space) * self.cdf_step_size
        return sum(self.state_space ** n * pdf_values)


class DiscreteDistribution(Distribution):

    @abstractmethod
    def pmf(self, x):
        pass
