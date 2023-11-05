""" Clustering methods for the buffalo library

This module consists of methods which will be useful to cluster data.

The functions in this module are:
    * kmeans_cluster
    * elbow_method_plot

"""

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def kmeans_cluster(data, n_clusters=3):
    """
    Perform KMeans clustering on data and plot the clustered points.

    Args:
        data (list of tuples or numpy.ndarray): The data points in the format
           [(xi, yi), ...].
        n_clusters (int): The number of clusters to create (default is 3).

    Returns:
        A list with the i-th element of the list a list of members of
        the i-th cluster.
    """
    # Create a KMeans model with the specified number of clusters
    kmeans = KMeans(n_clusters=n_clusters)

    # Fit the KMeans model to the data
    kmeans.fit(data)

    # Extract cluster labels assigned to each point
    labels = kmeans.labels_

    # Separate data into clusters based on labels
    clustered_data = [[] for _ in range(n_clusters)]
    for i, datapoint in enumerate(data):
        clustered_data[labels[i]].append((i, datapoint))

    return clustered_data


def elbow_method_plot(data, max_clusters=10):
    """
    Perform the elbow method and plot the results.

    Args:
        data (list of tuples or numpy.ndarray): The data points in the format
            [(xi, yi), ...].
        max_clusters (int): The maximum number of clusters to consider (default
            is 10).

    Returns:
        None
    """
    inertias = []

    for i in range(1, max_clusters + 1):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    plt.plot(range(1, max_clusters + 1), inertias, marker='o')
    plt.title('Elbow Method')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()
