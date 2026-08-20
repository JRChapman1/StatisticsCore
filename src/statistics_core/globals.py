from math import exp, sqrt

CDF_STEPS = 10_000

NORM_DIST_STATE_MIN = lambda mean, variance: mean - 8 * variance**0.5
NORM_DIST_STATE_MAX = lambda mean, variance: mean + 8 * variance**0.5

GAMMA_DIST_STATE_MIN = 0
GAMMA_DIST_STATE_MAX = lambda a, b: a / b + 8 * a ** 0.5 / b

LOG_NORM_DIST_STATE_MIN = 0
LOG_NORM_DIST_STATE_MAX = lambda mu, sigma: exp(mu + 0.5*sigma**2) + 8 * sqrt((exp(sigma**2) - 1) * exp(2 * mu + 2 * sigma**2))


