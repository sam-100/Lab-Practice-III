# Problem Statement:
# Implement K-Means clustering/ hierarchical clustering on sales_data_sample.csv dataset.
# Determine the number of clusters using the elbow method.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data_sample.csv', encoding="unicode_escape")

df.head()

df.dtypes

df.shape

df.isna().sum()

df['ADDRESSLINE2'] = df['ADDRESSLINE2'].fillna('NA')
df['STATE'] = df['STATE'].fillna('NA')
df = df.dropna(axis = 0, subset=['POSTALCODE', 'TERRITORY'])

df.isna().sum()

df_numeric = df.select_dtypes(include=[np.number])

df_numeric

# Scaling and Normalization
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_numeric)

df_scaled

# K means clustering
from sklearn.cluster import KMeans

inertia = []
k_min, k_max = 1, 21

for i in range(k_min, k_max):
    kmeans = KMeans(n_clusters=i, random_state=45, n_init=10)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)
inertia

plt.plot(range(k_min, k_max), inertia, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow method for optimal K')
plt.show()


