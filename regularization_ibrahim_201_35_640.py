# -*- coding: utf-8 -*-
"""Regularization_ibrahim_201-35-640.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-d3UY89jV_XwJdx4umpiRWsxV9FQBfl2

#Md Ibrahim
#ID: 201-35-640
#Section: A2
"""

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, r2_score

"""#Load and Prepare the Data:"""

data = pd.read_csv('/content/.config/linear-regression-dataset (2).csv')

# Define the independent variables (features) and the dependent variable (target)
X = data[['Hours', 'Practice', 'TeamWork']]
y = data['Scores']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""#Ridge Regression"""

# Create Ridge regression model
ridge_model = Ridge()

# Define hyperparameters to search
ridge_param_grid = {
    'alpha': [0.01, 0.1, 1.0, 10.0]
}

# Perform grid search
ridge_grid_search = GridSearchCV(ridge_model, ridge_param_grid, cv=5, scoring='neg_mean_squared_error')
ridge_grid_search.fit(X_train, y_train)

# Get the best Ridge model
best_ridge_model = ridge_grid_search.best_estimator_

# Make predictions
ridge_y_pred = best_ridge_model.predict(X_test)

# Evaluate Ridge model
ridge_mse = mean_squared_error(y_test, ridge_y_pred)
ridge_r2 = r2_score(y_test, ridge_y_pred)

"""#Lasso Regression"""

# Create Lasso regression model
lasso_model = Lasso()

# Define hyperparameters to search
lasso_param_grid = {
    'alpha': [0.01, 0.1, 1.0, 10.0]
}

# Perform grid search
lasso_grid_search = GridSearchCV(lasso_model, lasso_param_grid, cv=5, scoring='neg_mean_squared_error')
lasso_grid_search.fit(X_train, y_train)

# Get the best Lasso model
best_lasso_model = lasso_grid_search.best_estimator_

# Make predictions
lasso_y_pred = best_lasso_model.predict(X_test)

# Evaluate Lasso model
lasso_mse = mean_squared_error(y_test, lasso_y_pred)
lasso_r2 = r2_score(y_test, lasso_y_pred)

"""#ElasticNet Regression"""

# Create ElasticNet regression model
elasticnet_model = ElasticNet()

# Define hyperparameters to search
elasticnet_param_grid = {
    'alpha': [0.01, 0.1, 1.0, 10.0],
    'l1_ratio': [0.1, 0.3, 0.5, 0.7, 0.9]
}

# Perform grid search
elasticnet_grid_search = GridSearchCV(elasticnet_model, elasticnet_param_grid, cv=5, scoring='neg_mean_squared_error')
elasticnet_grid_search.fit(X_train, y_train)

# Get the best ElasticNet model
best_elasticnet_model = elasticnet_grid_search.best_estimator_

# Make predictions
elasticnet_y_pred = best_elasticnet_model.predict(X_test)

# Evaluate ElasticNet model
elasticnet_mse = mean_squared_error(y_test, elasticnet_y_pred)
elasticnet_r2 = r2_score(y_test, elasticnet_y_pred)

"""#Compare Results"""

print("Ridge Model - Mean Squared Error:", ridge_mse)
print("Ridge Model - R-squared:", ridge_r2)

print("Lasso Model - Mean Squared Error:", lasso_mse)
print("Lasso Model - R-squared:", lasso_r2)

print("ElasticNet Model - Mean Squared Error:", elasticnet_mse)
print("ElasticNet Model - R-squared:", elasticnet_r2)