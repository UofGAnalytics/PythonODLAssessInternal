from sklearn.cluster import KMeans


def kmeans_cluster_and_plot(data, n_clusters=3):
    """
    Perform KMeans clustering on data and plot the clustered points.

    Args:
        data (list of tuples or numpy.ndarray): The data points in the format
        [(xi, yi), ...].  n_clusters (int): The number of clusters to create
        (default is 3).

    Returns:
        A dictionary with keys cluster/group id and values a list of members of
        the group
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
