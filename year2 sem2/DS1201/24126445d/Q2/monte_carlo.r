# Q2 Monte Carlo Simulation
# Log-normal distribution, corresponding to normal μ=0.02, σ=0.05

# Load necessary libraries
library(ggplot2)

# Set seed
set.seed(1234)

# (a) Simulate 10000 samples (forbidden to use rlnorm())
cat("(a) Simulating 10000 log-normal distribution samples\n")
n <- 10000
mu <- 0.02
sigma <- 0.05

# First draw normal distribution samples, then apply exponential transformation to get log-normal distribution
normal_samples <- rnorm(n, mean=mu, sd=sigma)
lognormal_samples <- exp(normal_samples)

# Plot histogram
histogram_plot <- ggplot(data.frame(x=lognormal_samples), aes(x=x)) +
  geom_histogram(aes(y=..density..), bins=30, fill="lightblue", alpha=0.7) +
  labs(title="Log-normal Distribution Sample Histogram", x="Value", y="Density") +
  theme_minimal()

# (b) Draw theoretical density curve using dlnorm(), displayed in the same plot as the histogram
cat("(b) Drawing theoretical density curve\n")
histogram_plot <- histogram_plot +
  stat_function(fun=dlnorm, args=list(meanlog=mu, sdlog=sigma), 
                color="red", size=1.5) +
  labs(title="Log-normal Distribution: Sample Histogram and Theoretical Density Curve")

# Save plot
ggsave("Q2/histogram_density.png", plot=histogram_plot, width=8, height=6)

# (c) Theoretical mean and variance derivation (non-programming part)
# Here we only print theoretical values for reference
cat("(c) Theoretical mean and variance:\n")
theoretical_mean <- exp(mu + sigma^2/2)
theoretical_var <- (exp(sigma^2) - 1) * exp(2*mu + sigma^2)
cat("Theoretical mean: ", theoretical_mean, "\n")
cat("Theoretical variance: ", theoretical_var, "\n")

# Calculate experimental mean and variance for different sample sizes
sample_sizes <- c(10, 100, 1000, 10000, 100000)
experimental_means <- numeric(length(sample_sizes))
experimental_vars <- numeric(length(sample_sizes))

for (i in 1:length(sample_sizes)) {
  n_i <- sample_sizes[i]
  normal_samples_i <- rnorm(n_i, mean=mu, sd=sigma)
  lognormal_samples_i <- exp(normal_samples_i)
  experimental_means[i] <- mean(lognormal_samples_i)
  experimental_vars[i] <- var(lognormal_samples_i)
}

cat("Experimental mean and variance for different sample sizes:\n")
results <- data.frame(
  Sample_Size = sample_sizes,
  Experimental_Mean = experimental_means,
  Experimental_Var = experimental_vars,
  Theoretical_Mean = rep(theoretical_mean, length(sample_sizes)),
  Theoretical_Var = rep(theoretical_var, length(sample_sizes))
)
print(results)

# (d) Monte Carlo simulation: Estimate the probability of daily stock price increase ≥ 0.05
cat("(d) Monte Carlo simulation to estimate the probability of daily stock price increase ≥ 0.05\n")
# Stock price increase = log-normal variable - 1
price_increases <- lognormal_samples - 1
prob_mc <- mean(price_increases >= 0.05)
cat("Monte Carlo estimated probability: ", prob_mc, "\n")

# (e) Directly calculate the probability using R built-in functions and compare
cat("(e) Calculate probability using R built-in functions\n")
# P(X >= 1.05) where X~log-normal(mu, sigma^2)
prob_exact <- 1 - plnorm(1.05, meanlog=mu, sdlog=sigma)
cat("Exact probability: ", prob_exact, "\n")
cat("Difference between the two: ", abs(prob_mc - prob_exact), "\n")