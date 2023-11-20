# Problem Statement: 
# Predict the price of the Uber ride from a given pickup point to the agreed drop-off location.
# Perform following tasks:
# 1. Pre-process the dataset.
# 2. Identify outliers.
# 3. Check the correlation.
# 4. Implement linear regression and random forest regression models.
# 5. Evaluate the models and compare their respective scores like R2, RMSE, etc.

# Import the packages

import numpy as np
import pandas as pd
import sklearn as skl
import matplotlib.pyplot as plt

# 1. Preprocess the dataset

# Read the csv and remove null records

df = pd.read_csv('uber.csv')
df

df.isna().sum()

df = df.dropna(axis = 0, how = 'any')
df.isna().sum()

# 2. Identify Outliers

# Identify and Remove Outliers

plt.boxplot(df['fare_amount'])
plt.title('Box plot of Uber fare amounts')
plt.show()

df.plot(kind = 'box', subplots = True, layout = (7, 2), figsize = (15, 20))

Q1 = np.percentile(df['fare_amount'], 25)
Q3 = np.percentile(df['fare_amount'], 75)
IQR = Q3-Q1
IQR

lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
outliers = ((df['fare_amount'] < lower_bound) | (df['fare_amount'] > upper_bound))

print('Identified Outliers:')
df[outliers]

df = df[~outliers]

df

plt.boxplot(df['fare_amount'])
plt.title('Box plot of Uber fare amounts')
plt.show()

df.plot(kind = 'box', subplots = True, layout = (7, 2), figsize = (15, 20))

df.columns

for feature in df.columns:
    Q1 = np.percentile(df[feature], 25)
    Q3 = np.percentile(df[feature], 75)
    IQR = Q3-Q1
    
    lower_bound = Q1 - 1.5*IQR
    upper_bound = Q3 + 1.5*IQR
    outliers = ((df[feature] < lower_bound) | (df[feature] > upper_bound))
    
    df = df[~outliers]

df.plot(kind = 'box', subplots = True, layout = (7, 2), figsize = (15, 20))

# 3. Check Correlation
df

df = df.drop(['Unnamed: 0', 'key'], axis = 1)
df = df.drop(['pickup_datetime'], axis = 1)



correlation_matrix = df.corr()
correlation_matrix

import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap = 'coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# 4. Implement Linear Regression and Random forest regression models

import sklearn as skl
from sklearn.model_selection import train_test_split

target_variable = 'fare_amount'

X = df.drop(target_variable, axis = 1)
y = df[target_variable]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=45)

# Linear Regression

from sklearn.linear_model import LinearRegression

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)

# Random forest 

from sklearn.ensemble import RandomForestRegressor

rf_model = RandomForestRegressor(n_estimators=100, random_state = 5)

rf_model.fit(X_train, y_train)

y_pred_rf = rf_model.predict(X_test)

# 5. Evaluate the models and compare their respective scores like R2, RMSE, etc.

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Peformance Evaluation of Linear Regression Model

r2_linear_reg = r2_score(y_true=y_test, y_pred=y_pred_linear)
rmse_linear_reg = np.sqrt(mean_squared_error(y_true=y_test, y_pred=y_pred_linear))
mae_linear_reg = mean_absolute_error(y_true=y_test, y_pred=y_pred_linear)

print('Evaluation metrics for Linear Regression')
print('R2 score = ', r2_linear_reg)
print('RMSE = ', rmse_linear_reg)
print('MAE = ', mae_linear_reg)

# Performance Evaluation of Random Forest Model

r2_rf = r2_score(y_true=y_test, y_pred=y_pred_rf)
rmse_rf = np.sqrt(mean_squared_error(y_true=y_test, y_pred=y_pred_rf))
mae_rf = mean_absolute_error(y_true=y_test, y_pred=y_pred_rf)

print('Evaluation metrics for Random Forest')
print('R2 score = ', r2_rf)
print('RMSE = ', rmse_rf)
print('MAE = ', mae_rf)
