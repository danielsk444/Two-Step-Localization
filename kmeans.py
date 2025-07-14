import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from count_distinct import count_distinct
from is_globe import is_globe
import matplotlib.pyplot as plt


def kmeans(bulkra, bulkdec):
    data = {'x': bulkra, 'y': bulkdec}
    df = pd.DataFrame(data)
    print('len(bulkra),len(bulkdec)',len(bulkra),len(bulkdec))
    nbrs = NearestNeighbors(n_neighbors=5).fit(df)
    neigh_dist, neigh_ind = nbrs.kneighbors(df)

    # Sort the neighbor distances in ascending order
    sort_neigh_dist = np.sort(neigh_dist, axis=0)
    k_dist = sort_neigh_dist[:, 4]

    # Cluster the data using DBSCAN
    dbscan = DBSCAN(eps=5, min_samples=2).fit(df)
    labels = dbscan.labels_

    # Compute the centroids for each cluster
    unique_labels = np.unique(labels)
    centroids = []

    for label in unique_labels:
        if label == -1:
            # Skip noise points
            continue
        cluster_points = df[labels == label]
        centroid = cluster_points.mean(axis=0)
        centroids.append(centroid)

    centroids = np.array(centroids)
    '''
    # Optional: Plotting the clusters and centroids
    plt.scatter(bulkra, bulkdec, c=labels, cmap="plasma", marker='o', label='Data Points')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', label='Centroids')
    plt.title('DBSCAN Clustering with Centroids')
    plt.xlabel('Phi')
    plt.ylabel('Theta')
    plt.legend()
    plt.show()
    '''
    labels1 = list(labels)
    for i in range(4):
        labels, globe, globe1, globe2, globemin, globemax = is_globe(bulkra, bulkdec, labels)

    nkmeans = count_distinct(labels)
    if nkmeans< len(set(labels)):
        max_labels=max(labels)
        for i in range(len(labels)):
            if labels[i] == max_labels:
                labels[i] = max_labels-1
    #print('labels',len(labels),len(bulkra),len(bulkdec))
    #plt.plot(2,2)
    #plt.show()
    return labels, labels1, nkmeans, centroids
