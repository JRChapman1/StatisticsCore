import numpy as np

from statistics_core.distributions.base import Distribution


class BinomialDistribution(Distribution):

    def __init__(self, p: float, k: int) -> None:
        self.p = p
        self.k = k

    