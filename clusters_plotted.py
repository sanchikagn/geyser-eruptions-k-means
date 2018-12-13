import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Import the data
data_frame = pd.read_csv('C:/Users/Admin/PycharmProjects/GeyserEruption/resources/faithful_geyser.csv')

# Standardize the data
X_std = StandardScaler().fit_transform(data_frame)

# Run local implementation of kmeans
km = KMeans(n_clusters=2, max_iter=100)
km.fit(X_std)
centroids = km.cluster_centers_

# Plot the clustered data
fig, ax = plt.subplots(figsize=(8, 8))
plt.scatter(X_std[km.labels_ == 0, 0], X_std[km.labels_ == 0, 1],
            c='green', label='cluster 1')
plt.scatter(X_std[km.labels_ == 1, 0], X_std[km.labels_ == 1, 1],
            c='blue', label='cluster 2')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='X', s=100,
            c='r', label='centroid')
plt.legend()
plt.xlim([-2, 2])
plt.ylim([-2, 2])
plt.xlabel('Eruption time (minutes)',  fontsize=16)
plt.ylabel('Waiting time to next eruption (minutes)', fontsize=16)
plt.title('Clustered Data from Old Faithful Geyser, \n Yellowstone, USA',  fontsize=20, fontweight='bold')
ax.set_aspect('equal')
plt.savefig('plot-clusters.png')
