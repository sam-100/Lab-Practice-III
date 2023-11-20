# Problem Statement: 
# Given a bank customer, build a neural network-based classifier that can determine whether
# they will leave or not in the next 6 months.
# Dataset Description: The case study is from an open-source dataset from Kaggle.
# The dataset contains 10,000 sample points with 14 distinct features such as
# CustomerId, CreditScore, Geography, Gender, Age, Tenure, Balance, etc.
# Link to the Kaggle project:
# https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling
# Perform following steps:
# 1. Read the dataset.
# 2. Distinguish the feature and target set and divide the data set into training and test sets.
# 3. Normalize the train and test data.
# 4. Initialize and build the model. Identify the points of improvement and implement the same.
# 5. Print the accuracy score and confusion matrix (5 points).

import pandas as pd
import numpy as np
import sklearn as skl

# Step-1: Read the dataset.

df = pd.read_csv('Churn_Modelling.csv')
df.head()

df.dtypes

# Clean: Remove unnecessary attributes
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis = 1)
df

# Convert Categorical data into numerical data
from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['Geography'] = label_encoder.fit_transform(df['Geography'])
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df

# Step-2: Distinguish the feature and target set and divide the dataset into training and test sets.

# 1. Feature and target set division
X = df.drop(['Exited'], axis=1)
y = df['Exited']

# 2. Split into training and testing sets.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# Step-3: Normalize the train and test data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step-4: Initialize and Build the model. Identify the points of improvement and implement the same.
from sklearn.neural_network import MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(100, 150, 100), max_iter=200, random_state=4)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
y_pred

# Step-5: Print the Accuracy score and confusion matrix

from sklearn.metrics import accuracy_score, confusion_matrix

accuracy = accuracy_score(y_test, y_pred)
print('Accuracy: ', accuracy)

conf_matrix = confusion_matrix(y_test, y_pred)
print('Confusion Matrix: ')
print(conf_matrix)

help(MLPClassifier)

