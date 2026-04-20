# Stochastic Simulation: Geometric Brownian Motion

## Project Objective
Implementation of the **Geometric Brownian Motion (GBM)** model used for modeling financial asset prices. The project combines the theory of stochastic processes with efficient computations in the Python environment.

## Technologies
* **Python / NumPy**: Full vectorization of matrix computations (elimination of `for` loops).
* **Matplotlib**: Advanced visualization of price paths and marginal distributions.

## Mathematical Model
The simulation is based on the solution of the stochastic differential equation (SDE):
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

The project utilizes the closed-form solution:
$$S_t = S_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma W_t\right)$$

## Key Insights
* **Terminal Distribution**: Simulations confirm that the terminal prices $S_T$ follow a **log-normal distribution**, which results from the additivity of logarithmic returns.
* **Impact of Volatility**: An increase in the $\sigma$ parameter increases the dispersion of results and shifts the median of the distribution below the expected value (the effect of the $-\frac{1}{2}\sigma^2$ term).
* **Convergence**: The empirical mean from the Monte Carlo simulation shows strong convergence to the theoretical expected value $E[S_t] = S_0 e^{\mu t}$, which verifies the correctness of the algorithm.
* **Efficiency**: The use of vectorization in NumPy allows for generating $10^5$ paths in real time.

## Visualization
![Geometric Brownian Motion Simulation](assets/chart.png)
