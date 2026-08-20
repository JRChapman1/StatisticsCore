# Uniform

A discrete uniform random variable takes each value in its state space with equal probability.

## PMF

Let $X$ denote our discrete uniform random variable and let the state space of $X$ be comprised of $k+1$ elements
$$
\mathcal{S}_X = \{ a, a+s, a+2s, \dots a + ks =: b \}
$$
where $s$ is the step-size. Then the probability that $X$ takes a given value in the state space is
$$
P(X=x) = \frac{1}{k+1} \hspace{20mm} \forall x \in \mathcal{S}_X
$$

## CDF

For $x \in \mathcal{S}$ we have
$$
F_X(x) = P(X \le x) = \sum_{i \le x} P(X=x) = \sum_{i \le x} \frac{1}{k+1} = \frac{\frac{x-a}{s} + 1}{k+1}
$$
For $x \in \mathbb{R}$ such that $a \le x \le b$ we thus have
$$
F_X(x) = \frac{\lfloor \frac{x-a}{s} \rfloor + 1}{k+1}
$$

## Inverse CDF

For $x \in \mathcal{S}$ we have
$$
x = \frac{\frac{F_X(x) - a}{s} + 1}{k+1}
$$
Rearranging this gives
$$
F_X^{-1}(x) = (x (k+1) - 1) s + a
$$

## Mean

Consider the discrete uniform random variable $Y$ with state space $\mathcal{S}_Y = \{ 0, 1, 2, \dots, k \}$. This has mean
$$
\begin{align}
\mathbb{E}[Y] =& \sum_{y \in \mathcal{S}_Y} y \cdot P(Y=y) \\\\
=& \frac{\sum_{j=0}^{k} j}{k+1} \\\\
=& \frac{\frac{k(k+1)}{2}}{k+1} \\\\
=& \frac{k}{2}
\end{align}
$$

In the more general case of $X$, we have $X = a + sY$, so
$$
\mathbb{E}[X] = \mathbb{E}[a + sY] = a + s \mathbb{E}[Y] = a + s \frac{k}{2} = \frac{a + (a + sk)}{2} = \frac{a+b}{2}
$$

## Variance

Consider the discrete uniform random variable $Y$ with state space $\mathcal{S}_Y = \{ 0, 1, 2, \dots, k \}$. This has second moment
$$
\begin{align}
\mathbb{E}[Y^2] =& \sum_{y \in \mathcal{S}_Y} y^2 \cdot P(Y=y) \\\\
=& \frac{\sum_{j=0}^{k} j^2}{k+1} \\\\
=& \frac{\frac{k(k+1)(2k+1)}{6}}{k+1} \\\\
=& \frac{k(2k+1)}{6} \\\\
\end{align}
$$
So $Y$ has variance
$$
\text{var} (Y) = \mathbb{E}[Y^2] - \mathbb{E}[Y]^2 = \frac{k(2k+1)}{6} - \frac{k^2}{4} = \frac{2k(2k+1) - 3k^2}{12} = \frac{k(k+2)}{12}
$$

In the more general case of $X$, we have $X = a + sY$, so
$$
\text{var}(X) = \text{var}(a + sY) = s^2 \text{var}(Y) = \frac{k(k+2)s^2}{12}
$$


# Bernouilli

A Bernoulli random variable, $X$, takes value $1$ with probability $p$ and $0$ with probability $1-p$. It therefore has state space $\mathcal{S}_X = \{0, 1 \}$.

## PMF

The PMF of a $\text{Bernoulli}(p)$ random variable is
$$
P(X=x) = 
\begin{cases}
p & \text{if } x = 1 \\
1-p & \text{if } x = 0
\end{cases} \hspace{20mm} \forall x \in \mathcal{S}_X
$$

## CDF

For $x \in \mathbb{R}$ such that $a \le x \le b$
$$
P(X \le x) = \sum_{i \le x} P(X=x) = 
\begin{cases}
1-p & \forall x < 1  \\
1 & \forall x \geq 1
\end{cases}
$$

## Mean

$$
\mathbb{E}[X] = \sum_{x \in \mathcal{S}_X} x \cdot P(X=x) = 1 \times p + 0 \times (1-p) = p
$$

## Variance

$X$ has second moment
$$
\mathbb{E}[X^2] = \sum_{x \in \mathcal{S}_X} x^2 \cdot P(X=x) = 1^2 \times p + 0^2 \times (1-p) = p
$$
So the variance of $X$ is
$$
\text{var} (X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = p - p^2 = p (1 - p)
$$


# Binomial

A binomial random variable, $X$, represents the number of successes in $n$ independent Bernoulli trials, each with success probability $p$. It therefore has state space $\mathcal{S}_X = \{0, 1, \dots, n \}$.

## PMF

The PMF of a $\text{Binomial}(n, p)$ random variable is
$$
P(X=x) = p^x (1-p)^{n-x} {{n}\choose{x}} \hspace{20mm} \forall x \in \mathcal{S}_X
$$
Here:
* $p^x$ represents the probability of $x$ successes,
* $(1-p)^{n-x}$ represents the probability of $n-x$ failures
* So $p^x(1-p)^{n-x}$ represents the probability of a specific sequence of $x$ successes and $n-x$ failures from $n$ trials
* and ${{n}\choose{x}}$ represents the number of such sequences.

## CDF

For $x \in \mathbb{R}$ such that $a \le x \le b$
$$
P(X \le x) = \sum_{i=0}^x P(X=x) = \sum_{i=0}^x p^x (1-p)^{n-x} {{n}\choose{x}}
$$
There is no closed-form solution for the CDF.

## Mean

$$
\begin{align}
\mathbb{E}[X] =& \sum_{x \in \mathcal{S}_X} x \cdot P(X=x) \\\\
=& \sum_{x=0}^n x p^x (1-p)^{n-x} \frac{n!}{x!(n-x)!} \\\\
=& \sum_{x=0}^n p^x (1-p)^{n-x} \frac{n!}{(x-1)!(n-x)!} \\\\
=& np \sum_{x=0}^n p^{x-1} (1-p)^{n-x} \frac{(n-1)!}{(x-1)!(n-x)!} \\\\
=& np
\end{align}
$$

## Variance

To determine the second moment of $X$, we first consider $X(X-1)$. We have
$$
\begin{align}
\mathbb{E}[X(X-1)] =& \sum_{x \in \mathcal{S}_X} x(x-1) \cdot P(X=x) \\\\
=& \sum_{x=0}^n x (x-1) p^x (1-p)^{n-x} \frac{n!}{x!(n-x)!} \\\\
=& \sum_{x=0}^n p^x (1-p)^{n-x} \frac{n!}{(x-2)!(n-x)!} \\\\
=& \sum_{x=0}^n p^{x-2}p^2 (1-p)^{n-x} \frac{n(n-1)(n-2)!}{(x-2)!(n-x)!} \\\\
=& n(n-1) p^2 \sum_{x=0}^n p^{x-2} (1-p)^{n-x} \frac{(n-2)!}{(x-2)!(n-x)!} \\\\
=& n(n-1) p^2
\end{align}
$$
The second moment of $X$ is thus
$$
\mathbb{E}[X^2] = \mathbb{E}[X(X-1)] + \mathbb{E}[X] = n(n-1) p^2 + np = n^2 p^2 - np^2 + np
$$
So the variance of $X$ is
$$
\text{var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = n(n-1) p^2 + np = n^2 p^2 - np^2 + np - n^2 p^2 =  np ( 1 - p )
$$

# Geometric

A Geometric random variable, $X$, represents the number of Bernoulli trials needed to get the first success. It has state space $\mathcal{S}_X = \{1, 2, 3, \dots \}$.

## PMF

The PMF of a $\text{Geometric}(p)$ random variable is
$$
P(X=x) = p (1-p)^{x-1} \hspace{20mm} \forall x \in \mathcal{S}_X
$$
Here $p$ represents the probability of one success and $(1-p)^{x-1}$ represents the probability of $x-1$ failures. There is only one possible order ($x-1$ failures followed by one success) than results in $x$ trials being required to obtain the first success.

## CDF

For $x \in \mathbb{R}$ such that $a \le x \le b$
$$
\begin{align}
P(X \le x) =& \sum_{i=1}^x P(X=x) \\\\
=& \sum_{i=1}^x p (1-p)^{x-1} \\\\
=& p \sum_{i=0}^{x-1} (1-p)^{x} \\\\
&= p \frac{1 - (1-p)^{x}}{1 - (1-p)} \\\\
&= 1 - (1-p)^{x}
\end{align}
$$

## Mean

$$
\begin{align}
\mathbb{E}[X] =& \sum_{x \in \mathcal{S}_X} x \cdot P(X=x) \\\\
=& \sum_{x=1}^\infty x \cdot p q^{x-1} \hspace{20mm} \text{where } q := 1-p \\\\
=& p \sum_{x=1}^\infty \frac{d}{dq} \left[ q^{x} \right] \\\\
=& p \frac{d}{dq} \left[ \sum_{x=1}^\infty q^{x} \right] \\\\
=& p \frac{d}{dq} \left[ \frac{q}{1-q} \right] \\\\
=& p \left( \frac{1}{1-q} + \frac{q}{(1-q)^2} \right) \\\\
=& p \left( \frac{1}{p} + \frac{1-p}{p^2} \right) \\\\
=& \frac{1}{p}
\end{align}
$$

## Variance

To determine the second moment of $X$, we first consider $X(X-1)$. We have
$$
\begin{align}
\mathbb{E}[X (X-1)] =& \sum_{x \in \mathcal{S}_X} x(x-1) \cdot P(X=x) \\\\
=& \sum_{x=1}^\infty x(x-1) \cdot p q^{x-1} \hspace{20mm} \text{where } q := 1-p \\\\
=& p \sum_{x=1}^\infty q \frac{d^2}{dq^2} \left[ q^{x} \right] \\\\
=& pq \frac{d^2}{dq^2} \left[ \sum_{x=1}^\infty q^{x} \right] \\\\
=& pq \frac{d^2}{dq^2} \left[ \frac{q}{1-q} \right] \\\\
=& \frac{2pq}{(1-q)^3} \\\\
=& \frac{2(1-p)}{p^2}
\end{align}
$$
The second moment of $X$ is thus
$$
\mathbb{E}[X^2] = \mathbb{E}[X(X-1)] + \mathbb{E}[X] = \frac{2(1-p)}{p^2} + \frac{1}{p} = \frac{2-p}{p^2}
$$
So the variance of $X$ is
$$
\text{var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \frac{2-p}{p^2} - \frac{1}{p^2} = \frac{1-p}{p^2}
$$

# Negative Binomial

The negative binomial distribution is a generalisation of the Geometric distribution. It represents the number of trials required to obtain the $k^\text{th}$ success. A negative binomial random variable $X$ therefore has state space $\mathcal{S}_X = \{ k, k+1, k+2, \dots \}$.

## PMF

For $x$ trials to be required for the $k^\text{th}$ success to be obtained, we require $k$ successes and $x-k$ failures. Any particular sequence of $k$ successes and $x-k$ failures arises with probability $p^k (1-p)^{x-k}$.

The result of the $x^\text{th}$ trial must be a success for $X$ to be equal to $x$, but results of the other $x-1$ trials can be any sequence of $k-1$ successes and $x-k$ failures. There are ${{x-1}\choose{k-1}}$ such sequences. Thus, the PMF of $X$ is given by
$$
P(X=x) = p^k (1-p)^{x-k} {{x-1}\choose{k-1}} \hspace{20mm} \forall x \in \mathcal{S}_X
$$

## CDF

For $x \in \mathbb{R}$ such that $a \le x \le b$
$$
P(X \le x) = \sum_{i=0}^x P(X=x) = \sum_{i=k}^x p^k (1-p)^{x-k} {{x-1}\choose{k-1}}
$$
There is no closed-form solution for the CDF.

## Mean

$$
\begin{align}
\mathbb{E}[X] =& \sum_{x \in \mathcal{S}_X} x \cdot P(X=x) \\\\
=& \sum_{x=k}^\infty x p^k (1-p)^{x-k} \frac{(x-1)!}{(k-1)! (x-k)!} \\\\
=& \sum_{x=k}^\infty p^k (1-p)^{x-k} \frac{x!}{k! (x-k)!} k \\\\
=& \frac{k}{p} \sum_{x=k}^\infty p^{k+1} (1-p)^{x-k} \frac{x!}{k! (x-k)!} \\\\
=& \frac{k}{p}
\end{align}
$$

## Variance

To determine the second moment of $X$, we first consider $X(X+1)$. We have
$$
\begin{align}
\mathbb{E}[X(X+1)] =& \sum_{x \in \mathcal{S}_X} x(x+1) \cdot P(X=x) \\\\
=& \sum_{x=k}^\infty x(x+1) p^k (1-p)^{x-k} \frac{(x-1)!}{(k-1)! (x-k)!} \\\\
=& \sum_{x=k}^\infty p^k (1-p)^{x-k} \frac{(x+1)!}{(k+1)! (x-k)!} k(k+1) \\\\
=& \frac{k(k+1)}{p^2} \sum_{x=k}^\infty p^{k+2} (1-p)^{x-k} \frac{(x+1)!}{(k+1)! (x-k)!} \\\\
=& \frac{k(k+1)}{p^2}
\end{align}
$$
The second moment of $X$ is thus
$$
\mathbb{E}[X^2] = \mathbb{E}[X(X+1)] - \mathbb{E}[X] = \frac{k(k+1)}{p^2} - \frac{k}{p} = \frac{k(k+1) - kp}{p^2}
$$
So the variance of $X$ is
$$
\text{var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \frac{k(k+1) - kp}{p^2} - \frac{k^2}{p^2} = \frac{k(1-p)}{p^2}
$$


# Hypergeometric

The hypergeometric distribution is the finite population equivalent of the binomial distribution. A hypergeometric random variable, $X_n$, represents the number of successes obtained from a sample of size $n$ from a finite population consisting of $k$ successes and $N-k$ failures. The trials are not independent, since the result of each trial affects the remaining population for the subsequent trials (i.e. the population size reduces by 1 following each trial).

The state space of $X_n$ is therefore $\mathcal{S}_{X_n} = \{ 0, 1, 2, \dots, \min(k, n) \}$.

## PMF

Let $T_j$ denote the outcome of trial $j \leq n$ and let $S_j$ denote the number of successes obtained up to and including trial $j \leq n$. Then
$$
P(T_j = t_j \mid S_{j-1} = s_{j-1}) = 
\begin{cases}
\frac{k - s_{j-1}}{N - (j-1)} & \text{if } t_j = 1 \\\\
\frac{N - k - (j - 1 + s_{j-1})}{N - (j-1)} & \text{if } t_j = 0
\end{cases}
$$
Then
$$
\begin{align}
P(T_1 = t_1, T_2 = t_2, \dots , T_n = t_n) =& \prod_{j=1}^n \frac{t_j (k - s_{j-1}) + (1 - t_j) (N - k - (j - 1 - s_{j-1}))}{N - (j - 1)} \\\\
=&  \frac{\prod_{j=1, t_j=1}^n (k - s_{j-1}) \times \prod_{j=1, t_j=0}^n (N - k - (j - 1 - s_{j-1}))}{\prod_{j=1}^n (N - j + 1)} \\\\
=&  \frac{\prod_{j=0}^{x-1} (k - j) \times \prod_{j=0}^{n - x - 1} (N - k - j)}{\prod_{j=0}^{n-1} (N - j)} \\\\
=&  \frac{\frac{k!}{(k-x)!} \times \frac{(N-k)!}{(N-k-n+x)!}}{\frac{N!}{(N-n)!}} \\\\
=&  \frac{{{k}\choose{x}} {{N-k}\choose{n-x}}}{{{N}\choose{n}} {{n}\choose{x}}} \\\\
\end{align}
$$
This shows that the probability of obtaining $x$ successes and $n-x$ failures in any particular order is the same for all such sequences. Clearly there are ${{n}\choose{x}}$ such sequences, so the PMF of this distribution is
$$
P(X_n = x) = \frac{{{k}\choose{x}} {{N-k}\choose{n-x}}}{{{N}\choose{n}} {{n}\choose{x}}} \times {{n}\choose{x}} = \frac{{{k}\choose{x}} {{N-k}\choose{n-x}}}{{{N}\choose{n}}} 
$$

## CDF

For $x \in \mathbb{R}$ such that $a \le x \le b$
$$
P(X \le x) = \sum_{i=0}^x P(X=x) = \sum_{i=0}^x \frac{{{k}\choose{x}} {{N-k}\choose{n-x}}}{{{N}\choose{n}}}
$$
There is no closed-form solution for the CDF.

## Mean

$$
\begin{align}
\mathbb{E}[X] =& \sum_{x \in \mathcal{S}_X} x \cdot P(X=x) \\\\
=& \sum_{x=0}^n x \cdot \frac{\binom{k}{x} \binom{N-k}{n-x}}{\binom{N}{n}} \\\\
=& \sum_{x=0}^n x \cdot \frac{\frac{k!}{x! (k-x)!} \times \binom{N-k}{n-x}}{\frac{N!}{n! (N-n)!}} \\\\
=& \sum_{x=0}^n \frac{\frac{k(k-1)!}{(x-1)! (k-x)!} \times \binom{N-k}{n-x}}{\frac{N(N-1)!}{n(n-1)! (N-n)!}} \\\\
=& \frac{nk}{N} \sum_{x=0}^n \frac{\frac{(k-1)!}{(x-1)! (k-x)!} \times \binom{N-k}{n-x}}{\frac{(N-1)!}{(n-1)! (N-n)!}} \\\\
=& \frac{nk}{N} \sum_{x=0}^n \frac{\binom{k-1}{x-1} \times \binom{N-k}{n-x}}{\binom{N-1}{n-1}} \\\\
=& \frac{nk}{N}
\end{align}
$$

## Variance

To determine the second moment of $X$, we first consider $X(X-1)$. We have
$$
\begin{align}
\mathbb{E}[X(X-1)] =& \sum_{x \in \mathcal{S}_X} x (x-1) \cdot P(X=x) \\\\
=& \sum_{x=0}^n x (x-1) \cdot \frac{\binom{k}{x} \binom{N-k}{n-x}}{\binom{N}{n}} \\\\
=& \sum_{x=0}^n x (x - 1) \cdot \frac{\frac{k!}{x! (k-x)!} \times \binom{N-k}{n-x}}{\frac{N!}{n! (N-n)!}} \\\\
=& \sum_{x=0}^n x (x - 1) \frac{\frac{k(k-1)(k-2)!}{x(x-1)(x-2)! (k-x)!} \times \binom{N-k}{n-x}}{\frac{N(N-1)(N-2)!}{n(n-1)(n-2)! (N-n)!}} \\\\
=& \frac{k(k-1)n(n-1)}{N(N-1)} \sum_{x=0}^n \frac{\frac{(k-2)!}{(x-2)! (k-x)!} \times \binom{N-k}{n-x}}{\frac{(N-2)!}{(n-2)! (N-n)!}} \\\\
=& \frac{k(k-1)n(n-1)}{N(N-1)}
\end{align}
$$
The second moment of $X$ is thus
$$
\mathbb{E}[X^2] = \mathbb{E}[X(X-1)] + \mathbb{E}[X] = \frac{k(k-1)n(n-1)}{N(N-1)} + \frac{nk}{N} = \frac{nk[(k-1)(n-1) + N - 1]}{N(N-1)}
$$
So the variance of $X$ is
$$
\text{var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \frac{nk[(k-1)(n-1) + N - 1]}{N(N-1)} - \frac{n^2k^2}{N^2} = \frac{nk(N-n)(N-k)}{N^2(N-1)} 
$$




# Poisson

The Poisson distribution is a limiting case of a Binomial distribution as the number of trials, $n$, tends to infinity and the probability of success per trial, $p$, tends to zero with the product $np$ remaining constant.

A Poisson random variable, $X$, represents the number of events occurring in a fixed interval of time or space. It has state space $\mathcal{S}_X = \{ 0, 1, 2, \dots \}$.

The parameter $\lambda$ is known as the 'rate' of the process, representing the frequency with which events occur. Events are assumed to occur independently and one-at-a-time.

## PMF

Let $X \sim \text{Binomial} (n, p)$ and let $\lambda := np$ so that $p = \frac{\lambda}{n}$. We have previously shown that
$$
P(X = x) = \binom{n}{x} p^x (1-p)^{n-x} = \binom{n}{x} \left( \frac{\lambda}{n} \right)^x \left( 1-\frac{\lambda}{n} \right)^{n-x}
$$
As $n \to \infty$ and $p \to 0$ with $\lambda = np$ constant, $X$ converges to a $\text{Poisson}(\lambda)$ random variable with PMF
$$
\begin{align}
P(X=x) &= \lim_{n \to \infty} \left[ \frac{n!}{x! (n-x)!} \left( \frac{\lambda}{n} \right)^x \left( 1-\frac{\lambda}{n} \right)^{n-x} \right] \\\\
&= \lim_{n \to \infty} \left[ \frac{n (n-1) (n-2) \dots (n-x+1)}{x!} \frac{\lambda^x}{n^x} \left( 1+\frac{-\lambda}{n} \right)^{n-x} \right] \\\\
&= \lim_{n \to \infty} \left[ \frac{n}{n} \times \frac{n-1}{n} \times \frac{n-2}{n} \dots \frac{n-x+1}{n} \times \frac{\lambda^x}{x!} \left( 1+\frac{-\lambda}{n} \right)^{n-x} \right] \\\\
&= \lim_{n \to \infty} \left[ \frac{\lambda^x}{x!} \left( 1+\frac{-\lambda}{n} \right)^{n-x} \right] \hspace{20mm} \text{since } \lim_{n \rightarrow \infty} \frac{n-r}{n} = 1 \hspace{7mm} \forall r \\\\
&= \frac{\lambda^x}{x!} \lim_{n \to \infty} \left[ \left( 1+\frac{-\lambda}{n} \right)^{n} \left( 1+\frac{-\lambda}{n} \right)^{-x} \right] \\\\
&= \frac{\lambda^x e^{-\lambda}}{x!} \hspace{20mm} \text{since } \lim_{k \rightarrow \infty} \left( 1+\frac{z}{k} \right)^{k} = e^{z}
\end{align}
$$

## CDF

For $x \in \mathbb{R}$ such that $a \le x \le b$
$$
P(X \le x) = \sum_{i=0}^x P(X=x) = \sum_{i=0}^x \frac{\lambda^x e^{-\lambda}}{x!}
$$
There is no closed-form solution for the CDF.

## Mean

$$
\begin{align}
\mathbb{E}[X] =& \sum_{x \in \mathcal{S}_X} x \cdot P(X=x) \\
=& \sum_{x=0}^\infty x \frac{\lambda^x e^{-\lambda}}{x!} \\
=& \sum_{x=1}^\infty x \frac{\lambda \times \lambda^{x-1} e^{-\lambda}}{x(x-1)!} \\
=& \lambda \sum_{x=1}^\infty \frac{\lambda^{x-1} e^{-\lambda}}{(x-1)!} \\
=& \lambda \sum_{x=0}^\infty \frac{\lambda^{x} e^{-\lambda}}{x!} \\
=& \lambda \\
\end{align}
$$

## Variance

To determine the second moment of $X$, we first consider $X(X-1)$. We have
$$
\begin{align}
\mathbb{E}[X(X-1)] =& \sum_{x\in \mathcal{S}_X} x(x-1) \cdot P(X=x) \\
=& \sum_{x=0}^\infty x (x-1) \frac{\lambda^x e^{-\lambda}}{x!} \\
=& \sum_{x=2}^\infty x (x-1) \frac{\lambda^2 \times \lambda^{x-2} e^{-\lambda}}{x(x-1)(x-2)!} \\
=& \lambda^2 \sum_{x=2}^\infty \frac{\lambda^{x-2} e^{-\lambda}}{(x-2)!} \\
=& \lambda^2 \sum_{x=2}^\infty \frac{\lambda^{x-2} e^{-\lambda}}{(x-2)!} \\
=& \lambda^2 \sum_{x=0}^\infty \frac{\lambda^{x} e^{-\lambda}}{x!} \\
=& \lambda^2
\end{align}
$$
The second moment of $X$ is thus
$$
\mathbb{E}[X^2] = \mathbb{E}[X(X-1)] + \mathbb{E}[X] = \lambda^2 + \lambda
$$
So the variance of $X$ is
$$
\text{var}(X) = \mathbb{E}[X^2] - \mathbb{E}[X]^2 = \lambda^2 + \lambda - \lambda^2 = \lambda 
$$