from src.statistics_core.distributions.NormalDistribution import NormalDistribution
from src.statistics_core.distributions.ContinuousUniformDistribution import ContinuousUniformDistribution
from src.statistics_core.distributions.ExponentialDistribution import ExponentialDistribution
from src.statistics_core.distributions.ChiSquareDistribution import ChiSquareDistribution
from src.statistics_core.distributions.LognormalDistribution import LognormalDistribution
from src.statistics_core.distributions.GammaDistribution import GammaDistribution
from src.statistics_core.distributions.PoissonDistribution import PoissonDistribution
from src.statistics_core.distributions.DiscreteUniformDistribution import DiscreteUniformDistribution
from src.statistics_core.distributions.BinomialDistribution import BinomialDistribution
from src.statistics_core.distributions.GeometricDistribution import GeometricDistribution


n_14_20 = NormalDistribution(14, 20)

print(f'1.i)\t\t{n_14_20.cdf(14)}')
print(f'1.ii)\t\t{1 - n_14_20.cdf(20)}')
print(f'1.iii)\t\t{n_14_20.cdf(9)}')
print(f'1.iv)\t\t{n_14_20.icdf(1 - 0.41294)}')

n_10_25 = NormalDistribution(10, 25)

print(f'2)\t\t\t{n_10_25.moment(3)}')

u_5_10 = ContinuousUniformDistribution(5, 10)
n_10_5 = NormalDistribution(10, 5)
exp_05 = ExponentialDistribution(0.5)
chi_5 = ChiSquareDistribution(5)
gamma_8_2 = GammaDistribution(8, 2)
log_n_2_5 = LognormalDistribution(2, 5**0.5)

print(f'3.i)\t\t{u_5_10.cdf(8)}')
print(f'3.ii)\t\t{n_10_5.cdf(8)}')
print(f'3.iii)\t\t{exp_05.cdf(8)}')
print(f'3.iv)\t\t{chi_5.cdf(8)}')
print(f'3.v)\t\t{gamma_8_2.cdf(8)}')
print(f'3.vi)\t\t{log_n_2_5.cdf(8)}')   # TODO: Incorrect

poi_36 = PoissonDistribution(3.6)

print(f'4.i)\t\t{poi_36.mode()}')
print(f'4.ii)\t\t{poi_36.variance() ** 0.5}')
print(f'4.iii)\t\tNegatively skewed, since the distribution is strictly positive.')

cu_m1_1 = ContinuousUniformDistribution(-1, 1)
du_m1_1_4 = DiscreteUniformDistribution(-1, 1, 4)

print(f'5.i)\t\t{cu_m1_1.variance()}')
print(f'5.i)\t\t{du_m1_1_4.variance()}')   # TODO: Incorrect

gamma_2_05 = GammaDistribution(2, 0.5)

print(f'6.i.a)\t\tMean={gamma_2_05.mean()}, std Dev={gamma_2_05.variance()**0.5}')
print(f'6.i.b)\t\tNegatively skewed, since the distribution is strictly positive and variance>mean.')
print(f'6.ii)\t\tDone in continuous_distributions.md')
print(f'6.iii.a)\tTODO')
print(f'6.iii.b)\tTODO')
print(f'6.iii.c)\t{gamma_2_05.icdf(0.66)}')

poi_4 = PoissonDistribution(4)
bin_03_7 = BinomialDistribution(0.3, 7)
bin_001_500 = BinomialDistribution(0.01, 500)
bin_001_7 = BinomialDistribution(0.01, 7)
geo_001 = GeometricDistribution(0.01)

print(f'7.i)\t\t{poi_4.cdf(7)}')
print(f'7.ii)\t\t{1 - bin_03_7.cdf(3)}')
print(f'7.iii)\t\t{bin_001_500.cdf(7)}')
print(f'7.iv)\t\t{geo_001.cdf(8)}')

log_n_10_2 = LognormalDistribution.from_mean_and_variance(10, 4)
print(f'8)\t\t\t{log_n_10_2.cdf(12.5) - log_n_10_2.cdf(7.5)}')