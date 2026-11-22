# Q3 Linear Regression

# Load necessary libraries
library(ggplot2)

# Read data
data <- read.csv("house_prices_dataset.csv")

# Rename columns for ease of use
colnames(data) <- c("Area", "Distance", "Age", "Condition", "Price")

# (a) Simple linear regression: fit house price with each of the 4 features separately
cat("(a) Simple linear regression\n")

# Model 1: Area vs Price
model1 <- lm(Price ~ Area, data=data)
cat("Model 1: Area vs Price\n")
print(summary(model1))
print(attributes(model1))
print(coefficients(model1))

# Model 2: Distance vs Price
model2 <- lm(Price ~ Distance, data=data)
cat("\nModel 2: Distance vs Price\n")
print(summary(model2))
print(attributes(model2))
print(coefficients(model2))

# Model 3: Age vs Price
model3 <- lm(Price ~ Age, data=data)
cat("\nModel 3: Age vs Price\n")
print(summary(model3))
print(attributes(model3))
print(coefficients(model3))

# Model 4: Condition vs Price
model4 <- lm(Price ~ Condition, data=data)
cat("\nModel 4: Condition vs Price\n")
print(summary(model4))
print(attributes(model4))
print(coefficients(model4))

# Plot 4 scatter plots + fitted lines, with regression equations annotated

# Plot 1: Area vs Price
coef1 <- coefficients(model1)
eqn1 <- paste("Price = ", round(coef1[1], 2), " + ", round(coef1[2], 2), " * Area", sep="")
plot1 <- ggplot(data, aes(x=Area, y=Price)) +
  geom_point() +
  geom_smooth(method="lm", formula=y~x, se=FALSE) +
  labs(title="Area vs Price", x="Area", y="Price") +
  geom_text(x=min(data$Area), y=max(data$Price), label=eqn1, hjust=0, vjust=1) +
  theme_minimal()

# Plot 2: Distance vs Price
coef2 <- coefficients(model2)
eqn2 <- paste("Price = ", round(coef2[1], 2), " + ", round(coef2[2], 2), " * Distance", sep="")
plot2 <- ggplot(data, aes(x=Distance, y=Price)) +
  geom_point() +
  geom_smooth(method="lm", formula=y~x, se=FALSE) +
  labs(title="Distance vs Price", x="Distance to City Center", y="Price") +
  geom_text(x=min(data$Distance), y=max(data$Price), label=eqn2, hjust=0, vjust=1) +
  theme_minimal()

# Plot 3: Age vs Price
coef3 <- coefficients(model3)
eqn3 <- paste("Price = ", round(coef3[1], 2), " + ", round(coef3[2], 2), " * Age", sep="")
plot3 <- ggplot(data, aes(x=Age, y=Price)) +
  geom_point() +
  geom_smooth(method="lm", formula=y~x, se=FALSE) +
  labs(title="Age vs Price", x="House Age", y="Price") +
  geom_text(x=min(data$Age), y=max(data$Price), label=eqn3, hjust=0, vjust=1) +
  theme_minimal()

# Plot 4: Condition vs Price
coef4 <- coefficients(model4)
eqn4 <- paste("Price = ", round(coef4[1], 2), " + ", round(coef4[2], 2), " * Condition", sep="")
plot4 <- ggplot(data, aes(x=Condition, y=Price)) +
  geom_point() +
  geom_smooth(method="lm", formula=y~x, se=FALSE) +
  labs(title="Condition vs Price", x="House Condition", y="Price") +
  geom_text(x=min(data$Condition), y=max(data$Price), label=eqn4, hjust=0, vjust=1) +
  theme_minimal()

# Save plots
ggsave("Q3/area_price.png", plot=plot1, width=8, height=6)
ggsave("Q3/distance_price.png", plot=plot2, width=8, height=6)
ggsave("Q3/age_price.png", plot=plot3, width=8, height=6)
ggsave("Q3/condition_price.png", plot=plot4, width=8, height=6)

# (b) Multiple linear regression: model with Area + Distance as independent variables
cat("\n(b) Multiple linear regression: Area + Distance\n")
model_multiple <- lm(Price ~ Area + Distance, data=data)
print(summary(model_multiple))

# Predict: Price when Area=250, Distance=5
new_data <- data.frame(Area=250, Distance=5)
predicted_price <- predict(model_multiple, newdata=new_data)
cat("Predicted price (Area=250, Distance=5): ", predicted_price, "\n")

# (c) Optimal feature combination: fit 6 two-feature models
cat("\n(c) Optimal feature combination\n")

# Model 1: Area + Distance
model_comb1 <- lm(Price ~ Area + Distance, data=data)
r2_1 <- summary(model_comb1)$r.squared

# Model 2: Area + Age
model_comb2 <- lm(Price ~ Area + Age, data=data)
r2_2 <- summary(model_comb2)$r.squared

# Model 3: Area + Condition
model_comb3 <- lm(Price ~ Area + Condition, data=data)
r2_3 <- summary(model_comb3)$r.squared

# Model 4: Distance + Age
model_comb4 <- lm(Price ~ Distance + Age, data=data)
r2_4 <- summary(model_comb4)$r.squared

# Model 5: Distance + Condition
model_comb5 <- lm(Price ~ Distance + Condition, data=data)
r2_5 <- summary(model_comb5)$r.squared

# Model 6: Age + Condition
model_comb6 <- lm(Price ~ Age + Condition, data=data)
r2_6 <- summary(model_comb6)$r.squared

# Summarize R² values
r2_values <- c(r2_1, r2_2, r2_3, r2_4, r2_5, r2_6)
model_names <- c("Area + Distance", "Area + Age", "Area + Condition", "Distance + Age", "Distance + Condition", "Age + Condition")
r2_df <- data.frame(Model=model_names, R_squared=r2_values)

cat("R² values for each model:\n")
print(r2_df)

# Find the optimal model
best_model_index <- which.max(r2_values)
best_model <- model_names[best_model_index]
best_r2 <- r2_values[best_model_index]

cat("\nOptimal model: ", best_model, ", R² value: ", best_r2, "\n")