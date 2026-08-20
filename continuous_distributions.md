# Uniform

A continuous uniform random variable, $X$, takes any value in the interval $[a, b]$ with equal probability. 

## PDF

The probability density function (PDF) of a continuous uniform distribution is given by:
$$
f_X(x) = \frac{1}{b-a}
$$

## CDF

The cumulative distribution function (CDF) of a continuous uniform distribution is given by:
$$
F_X(x) = \int_{a}^x f_X(t) dt = \int_{a}^x \frac{1}{b-a} dt = \frac{x-a}{b-a} \quad \text{for } a \leq x \leq b
$$

## Inverse CDF

From the CDF, he have
$$
x = \frac{F_X^{-1}(x)-a}{b-a}
$$
Rearranging this we get
$$
F_X^{-1}(x) = x (b-a) + a
$$

## Mean

The mean of a continuous uniform distribution is given by:
$$
\mathbb{E}[X] = \int_a^b x f(x) dx = \int_a^b \frac{x}{b-a} dx = \left[ \frac{x^2}{2(b-a)} \right]_a^b = \frac{b^2 - a^2}{2(b-a)} = \frac{(b-a)(b+a)}{2(b-a)} = \frac{b+a}{2}
$$

## Variance

The second moment of a continuous uniform distribution is given by:
$$
\mathbb{E}[X^2] = \int_a^b x^2 f(x) dx = \int_a^b \frac{x^2}{b-a} dx = \left[ \frac{x^3}{3(b-a)} \right]_a^b = \frac{b^3 - a^3}{3(b-a)}
$$
The variance is thus
$$
\text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \frac{b^3 - a^3}{3(b-a)} - \frac{(a+b)^2}{4} = \frac{b^3 - a^3 + 3a^2b - 3ab^2}{12(b-a)} = \frac{(b-a)^2}{12}
$$

# Gamma

A gamma random variable, $X$, represents the waiting time until the $k$-th event in a Poisson process with rate parameter $\lambda$. It can be regarded as the continuous analogue of the negative binomial distribution. The gamma distribution is defined for $x > 0$, $k > 0$, and $\lambda > 0$.

## CDF

Let $X$ be a gamma random variable representing the waiting time until the $k$-th event in a Poisson process with rate parameter $\lambda$. The cumulative distribution function (CDF) of $X$ can be expressed in terms of a Poisson random variable $Y \sim \text{Poisson}(\lambda x)$ as:
$$
F_X(x) = P(X \leq x) = P(Y \geq k) = \sum_{i=k}^{\infty} \frac{e^{-\lambda x} (\lambda x)^i}{i!}
$$

## PDF

$$
\begin{align}
f_X(x) =& \frac{d}{dx}F_X(x) \\\\
=& \frac{d}{dx} \left[ \sum_{i=k}^{\infty} \frac{e^{-\lambda x} (\lambda x)^i}{i!} \right] \\\\
=& \sum_{i=k}^{\infty} \frac{\lambda^i}{i!} \frac{d}{dx} \left[ e^{-\lambda x} x^i \right] \\\\
=& \sum_{i=k}^{\infty} \frac{\lambda^i}{i!} \left( ix^{i-1} - \lambda x^i \right) e^{-\lambda x} \\\\
=& \lambda e^{-\lambda x} \left[ \sum_{i=k}^{\infty} \frac{\lambda^{i-1}}{(i-1)!} x^{i-1} - \sum_{i=k}^{\infty} \frac{\lambda^i}{i!} x^i \right] \\\\
=& \lambda e^{-\lambda x} \left[ \sum_{i=k-1}^{\infty} \frac{\lambda^{i}}{i!} x^{i} - \sum_{i=k}^{\infty} \frac{\lambda^i}{i!} x^i \right] \\\\
=& \lambda e^{-\lambda x} \frac{\lambda^{k-1}}{(k-1)!} x^{k-1} \\\\
=& \frac{\lambda^{k}}{(k-1)!} x^{k-1} e^{-\lambda x} \\\\
\end{align}
$$

The gamma distribution does not require that the parameter $k$ be an integer. To allow for non-integer values of $k$, we can use the gamma function, $\Gamma(k)$, which generalizes the factorial function. The PDF of the gamma distribution can then be expressed as:
$$
f_X(x) = \frac{\lambda^{k}}{\Gamma(k)} x^{k-1} e^{-\lambda x}
$$

## Mean

The mean of a gamma distribution is given by:
$$
\begin{align}
\mathbb{E}[X] =& \int_0^{\infty} x f_X(x) dx \\\\
=& \int_0^{\infty} \frac{\lambda^{k}}{\Gamma(k)} x^{k} e^{-\lambda x} dx \\\\
=& \frac{k}{\lambda} \int_0^{\infty} \frac{\lambda^{k+1}}{\Gamma(k+1)} x^{k} e^{-\lambda x} dx \\\\
=& \frac{k}{\lambda} \int_0^{\infty} f_Z(x) dx \hspace{20mm} \text{(where $Z \sim \text{Gamma}(k+1, \lambda)$)} \\\\
=& \frac{k}{\lambda}
\end{align}
$$

## Variance

The second moment of a gamma distribution is given by:
$$
\begin{align}
\mathbb{E}[X^2] =& \int_0^{\infty} x^2 f_X(x) dx \\\\
=& \int_0^{\infty} \frac{\lambda^{k}}{\Gamma(k)} x^{k+1} e^{-\lambda x} dx \\\\
=& \frac{(k+1)k}{\lambda^2} \int_0^{\infty} \frac{\lambda^{k+2}}{\Gamma(k+2)} x^{k+1} e^{-\lambda x} dx \\\\
=& \frac{(k+1)k}{\lambda^2} \int_0^{\infty} f_W(x) dx \hspace{20mm} \text{(where $W \sim \text{Gamma}(k+2, \lambda)$)} \\\\
=& \frac{(k+1)k}{\lambda^2}
\end{align}
$$
The variance is thus
$$
\text{Var}[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \frac{(k+1)k}{\lambda^2} - \frac{k^2}{\lambda^2} = \frac{k}{\lambda^2}
$$

## Special Case 1: Exponential

The exponential distribution is a special case of the gamma distribution where $k=1$. It represents the waiting time until the first event in a Poisson process with rate parameter $\lambda$. 

### PDF

$$
f_X(x) = \frac{\lambda^{1}}{\Gamma(1)} x^{1-1} e^{-\lambda x} = \lambda e^{-\lambda x}
$$

### CDF

$$
F_X(x) = \sum_{i=1}^{\infty} \frac{e^{-\lambda x} (\lambda x)^i}{i!} = 1 - \frac{e^{-\lambda x} (\lambda x)^0}{0!} = 1 - e^{-\lambda x}
$$


### Mean

The mean of a gamma distribution is given by:
$$
\mathbb{E}[X] = \frac{1}{\lambda}
$$

### Variance

$$
\text{Var}[X] = \frac{1}{\lambda^2}
$$

## Special Case 2: Chi-Squared

The chi-squared distribution is a special case of the gamma distribution where $k = \frac{v}{2}$ and $\lambda = \frac{1}{2}$, with $v$ being the degrees of freedom. It represents the sum of squares of $v$ independent standard normal random variables.

### PDF

$$
f_X(x) = \frac{1}{2^\frac{v}{2} \Gamma \left( \frac{v}{2} \right)} x^{\frac{v}{2}-1} e^{-\frac{x}{2}}
$$

### CDF

$$
F_X(x) = \sum_{i=k}^{\infty} \frac{e^{-\frac{x}{2}} (\frac{x}{2})^i}{i!}
$$


### Mean

The mean of a gamma distribution is given by:
$$
\mathbb{E}[X] = \frac{1}{\lambda}
$$

### Variance

$$
\text{Var}[X] = \frac{1}{\lambda^2}
$$

$$
\Gamma (\alpha + 1) = \alpha \Gamma (\alpha)
$$

$$
\begin{align}
\Gamma(c + 0.5) =& \sqrt{\pi} \prod_{i=1}^{c} \left( i - 0.5 \right) \\
\end{align}
$$


# Beta

The beta distribution describes the probability of a probability, or some other proportion, and is thus defined on the interval $[0, 1]$.

## PDF

Suppose that $Y$ is a Bernoulli random variable with success probability $p$, where $p$ is an unknown quantity. Suppose we perform $s+f$ independent Bernoulli trials and observe $s$ successes and $f$ failures. The likelihood function for $p$ satisfies
$$
L(p) \propto p^s (1-p)^f
$$

To construct a PDF from this likelihood function, we must normalise it by finding some function, $g$, of $f$ and $s$ such that
$$
\int_0^1 g(s, f) p^s (1-p)^f \, dp = 1
$$
Since $g$ does not depend on $p$, it can be taken outside of the integral
$$
g(s, f) \int_0^1 p^s (1-p)^f \, dp = 1 \hspace{10mm} \Rightarrow \hspace{10mm} g(s, f) = \frac{1}{\int_0^1 p^s (1-p)^f \, dp} = \frac{1}{B(s+1, f+1)}
$$
Where $B$ is the beta function.

The conventional parameterisation of the gamma distribution is $X \sim \text{Gamma} (\alpha, \beta)$ where, in the context of the above analyses, $\alpha = s+1$ and $\beta = f+1$. This gives the PDF
$$
f_X(x) = \frac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)}
$$
Note that the beta function can be calculated from the gamma function using the relationship
$$
B(\alpha, \beta) = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma (\alpha + \beta)}
$$

## CDF

TODO


## Mean

Since
$$
\Gamma (\alpha + 1) = \alpha \Gamma (\alpha)
$$
we have
$$
B(\alpha+1, \beta) = \frac{\Gamma(\alpha + 1)\Gamma(\beta)}{\Gamma (\alpha + \beta + 1)} = \frac{\alpha \Gamma(\alpha)\Gamma(\beta)}{(\alpha + \beta)\Gamma (\alpha + \beta)} = \frac{\alpha}{\alpha + \beta} B(\alpha, \beta)
$$
or
$$
B(\alpha, \beta) = \frac{\alpha + \beta}{\alpha} B(\alpha+1, \beta)
$$
Using this result enables us to easily derive the mean of the beta distribution:
$$
\begin{align}
\mathbb{E}[X] =& \int_0^1 x f_X(x) \, dx \\\\
=& \int_0^1 \frac{x^{\alpha} (1 - x)^{\beta - 1}}{B(\alpha, \beta)} \, dx \\\\
=& \int_0^1 \frac{x^{\alpha} (1 - x)^{\beta - 1}}{\frac{\alpha + \beta}{\alpha} B(\alpha+1, \beta)} \, dx \\\\
=& \frac{\alpha}{\alpha + \beta} \int_0^1 \frac{x^{\alpha} (1 - x)^{\beta - 1}}{B(\alpha+1, \beta)} \, dx \\\\
=& \frac{\alpha}{\alpha + \beta} \int_0^1 f_Y(y) dy \hspace{10mm} \text{where } Y \sim \text{Beta}(\alpha + 1, \beta) \\\\
=& \frac{\alpha}{\alpha + \beta}
\end{align}
$$


## Variance

Since
$$
\Gamma (\alpha + 1) = \alpha \Gamma (\alpha)
$$
we have
$$
B(\alpha+2, \beta) = \frac{\Gamma(\alpha + 2)\Gamma(\beta)}{\Gamma (\alpha + \beta + 2)} = \frac{\alpha(\alpha + 1)\Gamma(\alpha)\Gamma(\beta)}{(\alpha + \beta)(\alpha + \beta + 1) \Gamma (\alpha + \beta)} = \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} B(\alpha, \beta)
$$
or
$$
B(\alpha, \beta) = \frac{(\alpha + \beta)(\alpha + \beta + 1)}{\alpha(\alpha + 1)} B(\alpha + 2, \beta)
$$
Using this result enables us to easily derive the second moment of the beta distribution:
$$
\begin{align}
\mathbb{E}[X^2] =& \int_0^1 x^2 f_X(x) \, dx \\\\
=& \int_0^1 \frac{x^{\alpha + 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)} \, dx \\\\
=& \int_0^1 \frac{x^{\alpha + 1} (1 - x)^{\beta - 1}}{\frac{(\alpha + \beta)(\alpha + \beta + 1)}{\alpha(\alpha + 1)} B(\alpha + 2, \beta)} \, dx \\\\
=& \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} \int_0^1 \frac{x^{\alpha + 1} (1 - x)^{\beta - 1}}{B(\alpha + 2, \beta)} \, dx \\\\
=& \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} \int_0^1 f_Y(y) dy \hspace{10mm} \text{where } Y \sim \text{Beta}(\alpha + 1, \beta) \\\\
=& \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} \\\\
\end{align}
$$
The variance is thus
$$
\text{Var}[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \frac{\alpha(\alpha + 1)}{(\alpha + \beta)(\alpha + \beta + 1)} - \frac{\alpha^2}{(\alpha + \beta)^2}
$$

# Lognormal Distribution

Recall that the normal distribution can be interpreted as the limiting case of many small additive effects such that the nomalised limit of $S_n$ converges to a normally distributed random variable, where
$$
S_n = X_1 + X_2 + \dots + X_n
$$
By contrast, the lognormal distribution can be considered the limiting case of many small *multiplicative* effects such that
$$
R_n = X_1 \times X_2 \times \dots \times X_n
$$
Taking the natural logarithm of both sides gives
$$
\ln R_n = \ln X_1 + \ln X_2 + \dots + \ln X_n
$$
Then, if $\ln R_n$ is normally distributed, we say that $R_n$ is lognormally distributed.


## PDF

Let $S := \ln R$ be normally distributed with mean $\mu$ and variance $\sigma^2$. Then
$$
f_R(r) = f_S (e^r) \left| \frac{ds}{dr} \right| = \frac{1}{r} f_S (\ln r) = \frac{1}{r} \frac{1}{\sigma\sqrt{2\pi}} \exp \left( -\frac{1}{2}\left( \frac{\ln r - \mu}{\sigma} \right)^2 \right)
$$

# t Distribution

If
$$
X_1, \dots, X_n \overset{\text{iid}}{\sim} N(\mu, \sigma^2)
$$
then the random variable
$$
T = \frac{\bar{X} - \mu}{S / \sqrt{n}}
$$
has $t$ distribution with $\nu = n-1$ degrees of freedom where
$$
\bar{X} = \frac{1}{n} \sum_{i=1}^n X_i
$$
is the sample mean and
$$
S^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \bar{X})^2
$$
is the sample variance.

The population mean, $\mu$, is assumed to be a fixed but unknown quantity.

The t-distribution therefore arises from the ratio
$$
\frac{\text{sample mean error}}{\text{estimated standard error}}
$$
It can therefore be interpreted as the distribution of the sample mean after centring by the population mean and scaling by the estimated standard error.

## PDF

Let
$$
Z := \frac{\bar{X} - \mu}{\sigma / \sqrt{n}}
$$
and
$$
U := \frac{(n-1)S^2}{\sigma^2}
$$
Then
$$
T = \frac{\bar{X} - \mu}{S / \sqrt{n}} = \frac{\frac{\bar{X} - \mu}{\sigma / \sqrt{n}}}{\frac{S / \sqrt{n}}{\sigma / \sqrt{n}}} = \frac{Z}{\frac{S}{\sigma}} = \frac{Z}{\sqrt{\frac{(n-1)S^2}{(n-1)\sigma^2}}} = \frac{Z}{\sqrt{\frac{U}{n-1}}} = \frac{Z}{\sqrt{U / \nu}}
$$
where $\nu := n-1$.

We have
$$
\mathbb{E} [ \bar{X} ] = \mathbb{E} \left[ \frac{1}{n} \sum_{i=1}^n X_i \right] = \frac{1}{n} \sum_{i=1}^n \mathbb{E} \left[ X_i \right] = \frac{1}{n} \times n \times \mu = \mu
$$
and
$$
\text{Var} ( \bar{X} ) = \text{Var} \left( \frac{1}{n} \sum_{i=1}^n X_i \right) = \frac{1}{n^2} \sum_{i=1}^n \text{Var} \left( X_i \right) = \frac{1}{n^2} \times n \times \sigma^2 = \frac{\sigma^2}{n}
$$

The sum of $n$ independent normal random variables is itself a normal random variable, so $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$ and $Z \sim N(0, 1)$.

Recall that the Chi-Square distribution with $\nu$ degrees of freedom represents the sum of the squares of $\nu$ independent standard normal random variables, so
$$
\left( \sum_{i=1}^n Z_i^2 \right) \sim \text{Chi}(n)
$$
We have
$$
\begin{align}
U =& \frac{(n-1)S^2}{\sigma^2} \\\\
=& \frac{1}{\sigma^2} \sum_{i=1}^n (X_i - \bar{X})^2 \\\\
=& \frac{1}{\sigma^2} \left( \sum_{i=1}^n (X_i - \mu)^2 - n (\bar{X} - \mu)^2 \right) \\\\
=& \sum_{i=1}^n \left( \frac{X_i - \mu}{\sigma} \right)^2 - \left(\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \right)^2
\end{align}
$$
Since $X_i \sim N(\mu, \sigma^2)$, we have $\frac{X_i - \mu}{\sigma} \sim N(0, 1)$. Thus, 
$$
\sum_{i=1}^n \left( \frac{X_i - \mu}{\sigma} \right)^2 \sim \chi_n^2
$$
Similarly, since $\bar{X} \sim N(\mu, \frac{\sigma^2}{n})$, we have $\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$, so
$$
\left(\frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \right)^2 \sim \chi_1^2
$$
Thus (#TODO: show this)
$$
U \sim \chi_{n-1}^2
$$
and
$$
f_U(u) = \frac{1}{2^\frac{n-1}{2} \Gamma \left( \frac{n-1}{2} \right)} u^{\frac{n-1}{2}-1} e^{-\frac{u}{2}}
$$
The sample mean $\bar{X}$ and sample variance $\S^2$ are independent (#TODO: Show this), $U$ and $Z$ are independent. Thus
$$
\begin{align}
f_{U, Z} (u, z) =& f_U(u) \times f_Z(z) \\\\
=& \frac{1}{2^\frac{n-1}{2} \Gamma \left( \frac{n-1}{2} \right)} u^{\frac{n-1}{2}-1} e^{-\frac{u}{2}} \times \frac{1}{\sqrt{2\pi}} e^{-\frac{z^2}{2}} \\\\
=& \frac{1}{\sqrt{2^{n}\pi} \Gamma \left( \frac{n-1}{2} \right)} u^{\frac{n-1}{2}-1} e^{-\frac{u + z^2}{2}}
\end{align}
$$