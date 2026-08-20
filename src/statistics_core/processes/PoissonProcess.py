from src.statistics_core.processes.base import Process
from src.statistics_core.distributions.PoissonDistribution import PoissonDistribution


class PoissonProcess(Process):

    def __init__(self, rate: float, step_size: float, initial_value: float = 0):
        increment_distribution = PoissonDistribution(rate * step_size)
        super().__init__(increment_distribution, step_size, initial_value)