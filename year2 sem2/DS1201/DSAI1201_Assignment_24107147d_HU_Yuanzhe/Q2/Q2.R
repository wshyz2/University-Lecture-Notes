# Monte Carlo Simulation for Log-Normal Distribution
# Question 2: Parts (a), (b), (d), (e)

# Set output directory
output_dir <- "/Users/huyuanzhesmacbookpro/Desktop/year2 sem2/DS1201/DSAI1201_Assignment_24107147d/Q2"

# Set random seed
set.seed(1234)

# Define parameters
mu <- 0.02
sigma <- 0.05
n_samples <- 10000

# PART (a): Monte Carlo Simulation
normal_samples <- rnorm(n_samples, mean = mu, sd = sigma)
lognormal_samples <- exp(normal_samples)

# Save part (a) histogram
png(file.path(output_dir, "part_a_histogram.png"), width = 800, height = 600)
hist(lognormal_samples, breaks = 50, 
     main = "Histogram of Log-Normal Distribution (Part a)",
     xlab = "Sample Values", ylab = "Frequency",
     col = "steelblue", border = "white")
dev.off()
cat("Part (a) saved\n")

# PART (b): Density Plot Combined with Histogram
png(file.path(output_dir, "part_b_histogram_density.png"), width = 900, height = 700)
hist(lognormal_samples, breaks = 50,
     main = "Log-Normal Distribution: Histogram and Density (Part b)",
     xlab = "Sample Values", ylab = "Frequency",
     col = rgb(70, 130, 180, alpha = 180, maxColorValue = 255),
     border = "white", freq = TRUE)

x_values <- seq(min(lognormal_samples), max(lognormal_samples), length.out = 1000)
density_values <- dlnorm(x_values, meanlog = mu, sdlog = sigma)
density_scaled <- density_values * n_samples * (max(lognormal_samples) - min(lognormal_samples)) / 50

lines(x_values, density_scaled, col = "red", lwd = 2.5)

legend("topright", legend = c("Histogram", "Theoretical Density"),
       col = c("steelblue", "red"), lwd = c(1, 2.5),
       fill = c(rgb(70, 130, 180, alpha = 180, maxColorValue = 255), NA))
dev.off()
cat("Part (b) saved\n")

# PART (d): Monte Carlo Simulation for Stock Price 
n_simulations <- 10000
daily_returns <- exp(rnorm(n_simulations, mean = mu, sd = sigma)) - 1

count_increase <- sum(daily_returns >= 0.05)
prob_monte_carlo <- count_increase / n_simulations

cat("\nPart (d) - Monte Carlo Results:\n")
cat("Estimated probability:", round(prob_monte_carlo, 6), "\n")

png(file.path(output_dir, "part_d_monte_carlo.png"), width = 900, height = 700)
hist(daily_returns, breaks = 100,
     main = "Distribution of Daily Stock Returns (Part d)",
     xlab = "Daily Return", ylab = "Frequency",
     col = "lightblue", border = "white")
abline(v = 0.05, col = "red", lwd = 2.5, lty = 2)
dev.off()
cat("Part (d) saved\n")

# PART (e): Using R Built-in Functions 
threshold_log <- log(0.05)
prob_theoretical <- 1 - pnorm(threshold_log, mean = mu, sd = sigma)

cat("\nPart (e) - Theoretical Results:\n")
cat("Theoretical probability:", round(prob_theoretical, 6), "\n")
cat("Monte Carlo estimate:", round(prob_monte_carlo, 6), "\n")
cat("Difference:", round(abs(prob_theoretical - prob_monte_carlo), 6), "\n")

png(file.path(output_dir, "part_e_comparison.png"), width = 1000, height = 600)
comparison_data <- c(prob_monte_carlo, prob_theoretical)
barplot(comparison_data, names.arg = c("Monte Carlo (d)", "Theoretical (e)"),
        main = "Comparison: Monte Carlo vs Theoretical Probability",
        ylab = "Probability", col = c("steelblue", "darkred"),
        ylim = c(0, max(comparison_data) * 1.2))
text(1:2, comparison_data + 0.002, round(comparison_data, 6), pos = 3, cex = 1.1, font = 2)
dev.off()
cat("Part (e) saved\n")

cat("\nAll results saved to:", output_dir, "\n")