import numpy as np

from src.statistics_core.distributions.GammaDistribution import GammaDistribution


class ChiSquareDistribution(GammaDistribution):
    def __init__(self, degrees_of_freedom: int):
        super().__init__(degrees_of_freedom/2, 0.5)