# K-means Clustering Implementation from Scratch
# Load the customer dataset
data <- read.csv("Customers.csv")

# Extract the two features for clustering
income <- data$Annual_Income
spending <- data$Spending_Score

n_samples <- nrow(data)
n_clusters <- 5
max_iterations <- 100

# Initial cluster centroids (given in the assignment)
initial_centroids <- matrix(c(5, 5, 20, 90, 100, 10, 70, 50, 120, 100),
                            nrow = 5, ncol = 2, byrow = TRUE)
colnames(initial_centroids) <- c("Income", "Spending")

# Combine features for clustering
X <- cbind(income, spending)

# Variables to store results
centroids <- initial_centroids
cluster_assignments <- rep(0, n_samples)
distances_history <- c()

# K-means algorithm loop
for (iteration in 1:max_iterations) {
  # Step 1: Assign each point to the nearest centroid
  distances_to_centroids <- matrix(0, nrow = n_samples, ncol = n_clusters)
  
  for (k in 1:n_clusters) {
    # Calculate Euclidean distance from each point to centroid k
    diff <- sweep(X, 2, centroids[k, ], "-")
    distances_to_centroids[, k] <- sqrt(rowSums(diff^2))
  }
  
  # Assign each point to the cluster with minimum distance
  cluster_assignments <- apply(distances_to_centroids, 1, which.min)
  
  # Step 2: Record mean distance for convergence analysis
  min_distances <- apply(distances_to_centroids, 1, min)
  mean_distance <- mean(min_distances)
  distances_history <- c(distances_history, mean_distance)
  
  # Step 3: Update centroids as the mean of assigned points
  centroids_new <- matrix(0, nrow = n_clusters, ncol = 2)
  
  for (k in 1:n_clusters) {
    points_in_cluster <- X[cluster_assignments == k, ]
    
    if (nrow(points_in_cluster) > 0) {
      centroids_new[k, ] <- colMeans(points_in_cluster)
    } else {
      centroids_new[k, ] <- centroids[k, ]
    }
  }
  
  # Check for convergence
  if (sum(abs(centroids_new - centroids)) < 1e-6) {
    cat("Algorithm converged at iteration", iteration, "\n")
    centroids <- centroids_new
    break
  }
  
  centroids <- centroids_new
}

# Store the final results
data$Cluster <- cluster_assignments
final_centroids <- centroids

# Print clustering summary
cat("K-means Clustering Complete\n")
cat("Number of iterations:", iteration, "\n")
cat("Number of samples in each cluster:\n")
print(table(cluster_assignments))
cat("\nFinal centroid positions:\n")
print(final_centroids)

# Visualization 
# Color palette for clusters
cluster_colors <- c("red", "green", "blue", "purple", "brown")
point_colors <- cluster_colors[cluster_assignments]
centroid_colors <- cluster_colors

# Figure 1: Scatter plot of customers with cluster assignments
png(filename = "scatter_plot.png", width = 800, height = 600, res = 100)
par(mar = c(5, 5, 3, 2))
plot(X[, 1], X[, 2],
     col = point_colors, pch = 16, cex = 1.5,
     xlab = "Annual Income", ylab = "Spending Score",
     main = "K-means Clustering Results (k=5)",
     xlim = c(0, 140), ylim = c(0, 110))

# Add centroids to the scatter plot
points(centroids[, 1], centroids[, 2],
       col = "black", pch = 8, cex = 3.5, lwd = 2)

legend("topright",
       legend = c("Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5", "Centroid"),
       col = c(cluster_colors, "black"),
       pch = c(16, 16, 16, 16, 16, 8),
       cex = 1.2)
dev.off()

# Figure 2: Line plot showing convergence
png(filename = "convergence_plot.png", width = 800, height = 600, res = 100)
par(mar = c(5, 5, 3, 2))
plot(1:length(distances_history), distances_history,
     type = "l", lwd = 2, col = "steelblue",
     xlab = "Training Iteration", ylab = "Mean Distance to Centroid",
     main = "K-means Convergence Analysis")
grid(col = "gray80", lty = "dotted")
dev.off()

cat("\n Scatter plot saved as: scatter_plot.png\n")
cat("Convergence plot saved as: convergence_plot.png\n")
