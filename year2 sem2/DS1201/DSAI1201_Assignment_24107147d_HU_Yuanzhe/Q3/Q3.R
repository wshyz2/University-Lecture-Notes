# Question 3: Linear Regression Analysis on House Prices Dataset

# Load the dataset
data <- read.csv("/Users/huyuanzhesmacbookpro/Desktop/year2 sem2/DS1201/DSAI1201_Assignment_24107147d/Q3/house_prices_dataset.csv")

# Display basic information about the dataset
head(data)
str(data)
summary(data)

# Part (a): Simple Linear Regression Analysis

# Model 1: House_Price ~ House_Area
model_area <- lm(House_Price ~ House_Area, data = data)

# Model 2: House_Price ~ Distance_to_Center
model_distance <- lm(House_Price ~ Distance_to_Center, data = data)

# Model 3: House_Price ~ House_Age
model_age <- lm(House_Price ~ House_Age, data = data)

# Model 4: House_Price ~ House_Condition
model_condition <- lm(House_Price ~ House_Condition, data = data)

# Print summaries for each model
cat("===== Simple Linear Regression Models =====\n\n")

cat("Model 1: House_Price ~ House_Area\n")
print(summary(model_area))
cat("\n")

cat("Model 2: House_Price ~ Distance_to_Center\n")
print(summary(model_distance))
cat("\n")

cat("Model 3: House_Price ~ House_Age\n")
print(summary(model_age))
cat("\n")

cat("Model 4: House_Price ~ House_Condition\n")
print(summary(model_condition))
cat("\n")

# Create scatter plots with regression lines for Part (a)
png(filename = "/Users/huyuanzhesmacbookpro/Desktop/year2 sem2/DS1201/DSAI1201_Assignment_24107147d/Q3/part_a_scatter_plots.png",
    width = 1200, height = 1000)

par(mfrow = c(2, 2))

# Plot 1: House_Area vs House_Price
plot(data$House_Area, data$House_Price,
     main = "House Price vs House Area",
     xlab = "House Area (sq units)",
     ylab = "House Price ($)",
     pch = 16, col = rgb(0.2, 0.4, 0.8, 0.5))
abline(model_area, col = "red", lwd = 2)
coef_area <- coefficients(model_area)
equation_area <- paste("House_Price =", round(coef_area[1], 2), "+", round(coef_area[2], 2), "* House_Area")
text(x = max(data$House_Area) * 0.5, y = max(data$House_Price) * 0.95,
     equation_area, cex = 0.9, bg = "white")

# Plot 2: Distance_to_Center vs House_Price
plot(data$Distance_to_Center, data$House_Price,
     main = "House Price vs Distance to Center",
     xlab = "Distance to Center (units)",
     ylab = "House Price ($)",
     pch = 16, col = rgb(0.2, 0.4, 0.8, 0.5))
abline(model_distance, col = "red", lwd = 2)
coef_distance <- coefficients(model_distance)
equation_distance <- paste("House_Price =", round(coef_distance[1], 2), "+", round(coef_distance[2], 2), "* Distance_to_Center")
text(x = max(data$Distance_to_Center) * 0.5, y = max(data$House_Price) * 0.95,
     equation_distance, cex = 0.9, bg = "white")

# Plot 3: House_Age vs House_Price
plot(data$House_Age, data$House_Price,
     main = "House Price vs House Age",
     xlab = "House Age (years)",
     ylab = "House Price ($)",
     pch = 16, col = rgb(0.2, 0.4, 0.8, 0.5))
abline(model_age, col = "red", lwd = 2)
coef_age <- coefficients(model_age)
equation_age <- paste("House_Price =", round(coef_age[1], 2), "+", round(coef_age[2], 2), "* House_Age")
text(x = max(data$House_Age) * 0.5, y = max(data$House_Price) * 0.95,
     equation_age, cex = 0.9, bg = "white")

# Plot 4: House_Condition vs House_Price
plot(data$House_Condition, data$House_Price,
     main = "House Price vs House Condition",
     xlab = "House Condition (score)",
     ylab = "House Price ($)",
     pch = 16, col = rgb(0.2, 0.4, 0.8, 0.5))
abline(model_condition, col = "red", lwd = 2)
coef_condition <- coefficients(model_condition)
equation_condition <- paste("House_Price =", round(coef_condition[1], 2), "+", round(coef_condition[2], 2), "* House_Condition")
text(x = max(data$House_Condition) * 0.5, y = max(data$House_Price) * 0.95,
     equation_condition, cex = 0.9, bg = "white")

dev.off()

cat("Part (a) scatter plots saved successfully.\n\n")

# Part (b): Multiple Linear Regression with House_Area and Distance_to_Center

model_multiple_b <- lm(House_Price ~ House_Area + Distance_to_Center, data = data)

cat("===== Multiple Linear Regression: House_Area + Distance_to_Center =====\n")
print(summary(model_multiple_b))
cat("\n")

# Make prediction for House_Area = 250 and Distance_to_Center = 5
prediction_b <- predict(model_multiple_b, newdata = data.frame(House_Area = 250, Distance_to_Center = 5))
cat("Prediction for House_Area = 250 and Distance_to_Center = 5:\n")
cat("House_Price =", prediction_b, "\n\n")

# Part (c): Compare Multiple Models with Different Feature Combinations

# Model 1: House_Area + Distance_to_Center
model1_c <- lm(House_Price ~ House_Area + Distance_to_Center, data = data)

# Model 2: House_Area + House_Age
model2_c <- lm(House_Price ~ House_Area + House_Age, data = data)

# Model 3: House_Area + House_Condition
model3_c <- lm(House_Price ~ House_Area + House_Condition, data = data)

# Model 4: Distance_to_Center + House_Age
model4_c <- lm(House_Price ~ Distance_to_Center + House_Age, data = data)

# Model 5: Distance_to_Center + House_Condition
model5_c <- lm(House_Price ~ Distance_to_Center + House_Condition, data = data)

# Model 6: House_Age + House_Condition
model6_c <- lm(House_Price ~ House_Age + House_Condition, data = data)

# Extract R-squared values for all models
r_squared_1 <- summary(model1_c)$r.squared
r_squared_2 <- summary(model2_c)$r.squared
r_squared_3 <- summary(model3_c)$r.squared
r_squared_4 <- summary(model4_c)$r.squared
r_squared_5 <- summary(model5_c)$r.squared
r_squared_6 <- summary(model6_c)$r.squared

# Create a comparison table
comparison_table <- data.frame(
  Model = c("Model 1", "Model 2", "Model 3", "Model 4", "Model 5", "Model 6"),
  Features = c(
    "House_Area + Distance_to_Center",
    "House_Area + House_Age",
    "House_Area + House_Condition",
    "Distance_to_Center + House_Age",
    "Distance_to_Center + House_Condition",
    "House_Age + House_Condition"
  ),
  R_squared = c(r_squared_1, r_squared_2, r_squared_3, r_squared_4, r_squared_5, r_squared_6)
)

cat("===== Model Comparison: R-squared Values =====\n")
print(comparison_table)

# Find the best model
best_model_index <- which.max(c(r_squared_1, r_squared_2, r_squared_3, r_squared_4, r_squared_5, r_squared_6))
best_model_name <- paste("Model", best_model_index)

cat("\n===== Best Model Summary =====\n")
cat("The R-squared values for all the models are", round(r_squared_1, 4), ",", round(r_squared_2, 4), ",",
    round(r_squared_3, 4), ",", round(r_squared_4, 4), ",", round(r_squared_5, 4), ",", round(r_squared_6, 4), ".\n")
cat("So the best model is", best_model_name, "\n\n")

# Visualization: R-squared Comparison

png(filename = "/Users/huyuanzhesmacbookpro/Desktop/year2 sem2/DS1201/DSAI1201_Assignment_24107147d/Q3/part_c_model_comparison.png",
    width = 1000, height = 600)

barplot(c(r_squared_1, r_squared_2, r_squared_3, r_squared_4, r_squared_5, r_squared_6),
        names.arg = c("Model 1", "Model 2", "Model 3", "Model 4", "Model 5", "Model 6"),
        main = "Model Comparison: R-squared Values",
        ylab = "R-squared",
        xlab = "Model",
        col = c("lightblue", "lightblue", "lightblue", "lightblue", "lightblue", "lightblue"),
        ylim = c(0, 1))

# Highlight the best model
barplot(c(r_squared_1, r_squared_2, r_squared_3, r_squared_4, r_squared_5, r_squared_6),
        names.arg = c("Model 1", "Model 2", "Model 3", "Model 4", "Model 5", "Model 6"),
        main = "Model Comparison: R-squared Values",
        ylab = "R-squared",
        xlab = "Model",
        col = ifelse(1:6 == best_model_index, "red", "lightblue"),
        ylim = c(0, 1),
        add = TRUE)

dev.off()

cat("Part (c) model comparison plot saved successfully.\n")
