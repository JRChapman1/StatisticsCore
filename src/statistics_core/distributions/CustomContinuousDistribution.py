import numpy as np
import math

from src.statistics_core.distributions.base import ContinuousDistribution
from src.statistics_core.globals import CDF_STEPS


class CustomContinuousDistribution(ContinuousDistribution):

    def __init__(self, pmf: str, parameters: dict, state_space_min: float, state_space_max: float):
        # store state space constraints
        self.cdf_step_size = (state_space_max - state_space_min) / CDF_STEPS
        self.state_space = np.linspace(state_space_min, state_space_max, CDF_STEPS+1)
        # merge provided parameters into self so pmf expression can refer to self.<param>
        self.__dict__ = self.__dict__ | parameters
        # create a relatively-sandboxed lambda where 'self' and 'comb' are available
        # bind self as a default argument to make it available when the lambda executes
        safe_globals = {"__builtins__": {}}
        # provide self and comb at eval time so default arg self=self binds correctly
        safe_locals = {"self": self, "math": math, "np": np}
        # bind both self and comb as default args so they're available when lambda runs
        self._pdf = eval('lambda x, self=self, math=math, np=np: ' + pmf, safe_globals, safe_locals)

    def pdf(self, x):
        return self._pdf(x)

    def ipdf(self, p):
        pass

    def _calculate_mean(self):
        mu = 0
        for x in self.state_space:
            mu += x * self.pdf(x)
        return mu

    def _calculate_variance(self):
        second_moment = 0
        for x in self.state_space:
            second_moment += x ** 2 * self.pdf(x)
        return second_moment - self.mean() ** 2

    def moment(self, n):
        pdf_values = self.pdf(self.state_space) * self.cdf_step_size
        return sum(self.state_space ** n * pdf_values)

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


if __name__ == '__main__':

    parameters = {'mean': 14, 'variance': 20}
    pmf_str = '1 / np.sqrt(2 * math.pi * self.variance) * np.exp(-0.5 * ((x - self.mean) / np.sqrt(self.variance))**2)'
    n_14_20 = CustomContinuousDistribution(pmf_str, parameters, -1000, 1000)

    print(f'1.iv) {n_14_20.icdf(1 - 0.41294)}')

    print(n_14_20.cdf(14.95))
    print(1 - 0.41294)