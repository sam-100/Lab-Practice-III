# Problem Statement
# Classify the email using the binary classification method. Email Spam detection has two
# states: a) Normal State – Not Spam, b) Abnormal State – Spam. Use K-Nearest Neighbors and
# Support Vector Machine for classification. Analyze their performance.
# Dataset link: The emails.csv dataset on the Kaggle

# Import libraries
import numpy as np
import pandas as pd
import sklearn as skl

# Read the data and perform preprocessing

df = pd.read_csv('emails.csv')
df

df.head()

df.dtypes

df.drop(['Email No.'], axis = 1, inplace=True)

df

df.isna().sum()

# Split the dataset into feature-set (X) and target-set (y)

X = df.drop(['Prediction'], axis = 1)
y = df['Prediction']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)

# Feature scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# KNN Classifier
from sklearn.neighbors import KNeighborsClassifier

# 1. Train
knn_classifier = KNeighborsClassifier(n_neighbors=10)
knn_classifier.fit(X_train_scaled, y_train)

# 2. Predict
y_pred_knn = knn_classifier.predict(X_test_scaled)
y_pred_knn

# SVM Classifier
from sklearn.svm import SVC

# 1. Train
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_scaled, y_train)

# 2. Predict
y_pred_svm = svm_classifier.predict(X_test_scaled)
y_pred_svm

# Performance Evaluation
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

accuracy_knn = accuracy_score(y_test, y_pred_knn)
accuracy_svm = accuracy_score(y_test, y_pred_svm)
print('Accuracy of KNN = ', accuracy_knn)
print('Accuracy of SVM = ', accuracy_svm)

print('KNN\'s classification report: ')
print(classification_report(y_test, y_pred_knn))
print('SVM\'s classification report: ')
print(classification_report(y_test, y_pred_svm))

print('KNN\'s confusion matrix')
print(confusion_matrix(y_test, y_pred_knn))
print('SVM\'s confusion matrix')
print(confusion_matrix(y_test, y_pred_svm))
