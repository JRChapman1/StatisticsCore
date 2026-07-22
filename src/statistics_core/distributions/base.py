from abc import ABC, abstractmethod, abstractproperty


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
    def sample(self, n):
        pass

    @abstractmethod
    def pdf(self, x):
        pass

    @abstractmethod
    def cdf(self, x):
        pass

    @abstractmethod
    def ipdf(self, x):
        pass

    @abstractmethod
    def icdf(self, x):
        pass
