import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering

# Load the dataset
df = pd.read_csv("sales_data_sample.csv")  # Update with the actual file path

# Display the first few rows of the dataset
print(df.head())

# Extract relevant features for clustering
features = df[['Sales', 'Quantity']]

# Standardize the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# K-Means clustering and the Elbow Method
inertia_values = []
possible_k_values = range(1, 11)

for k in possible_k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(features_scaled)
    inertia_values.append(kmeans.inertia_)

# Plotting the Elbow Method graph
plt.plot(possible_k_values, inertia_values, marker='o')
plt.title('Elbow Method for Optimal k (K-Means)')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.show()

# Hierarchical Clustering and Dendrogram
linked = linkage(features_scaled, method='ward')
dendrogram(linked, orientation='top', distance_sort='descending', show_leaf_counts=True)
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('Sample Index')
plt.ylabel('Cluster Distance')
plt.show()

# Determine the optimal number of clusters using Silhouette Score for K-Means
silhouette_scores = []

for k in possible_k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(features_scaled)
    silhouette_scores.append(silhouette_score(features_scaled, labels))

# Plotting Silhouette Scores for K-Means
plt.plot(possible_k_values, silhouette_scores, marker='o')
plt.title('Silhouette Score for Optimal k (K-Means)')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.show()

# Determine the optimal number of clusters using Silhouette Score for Hierarchical Clustering
silhouette_scores_hierarchical = []

for k in possible_k_values:
    hierarchical = AgglomerativeClustering(n_clusters=k)
    labels = hierarchical.fit_predict(features_scaled)
    silhouette_scores_hierarchical.append(silhouette_score(features_scaled, labels))

# Plotting Silhouette Scores for Hierarchical Clustering
plt.plot(possible_k_values, silhouette_scores_hierarchical, marker='o')
plt.title('Silhouette Score for Optimal k (Hierarchical Clustering)')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Silhouette Score')
plt.show()
