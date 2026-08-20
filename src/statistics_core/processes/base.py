from abc import ABC
from argparse import ArgumentError
import numpy as np

from src.statistics_core.distributions.base import Distribution

class Process(ABC):

    def __init__(self, increment_distribution: Distribution, step_size: float, initial_value: float = 0):
        self.increment_dist = increment_distribution
        self.step_size = step_size
        self.initial_value = initial_value

    def simulate(self, num_steps: int = None, horizon: float = None, num_sims: int = 1):

        num_steps = self._validate_simulate_inputs(num_steps, horizon)
        z_scores = np.random.rand(num_steps, num_sims)
        increments = self.increment_dist.icdf(z_scores)
        initial_values = np.tile(self.initial_value, (1, num_sims))
        return np.vstack((initial_values, increments)).cumsum(axis=0)

    def _validate_simulate_inputs(self, num_steps: int, horizon: float):

        if num_steps is None and horizon is None:
            raise ArgumentError(None, 'Must specify one of either num_steps or horizon. Neither given.')

        elif num_steps is not None and horizon is not None:
            raise ArgumentError(None, 'Must specify one of either num_steps or horizon. Both given.')

        elif num_steps is None:
            num_steps = int(horizon / self.step_size)

        return num_steps

