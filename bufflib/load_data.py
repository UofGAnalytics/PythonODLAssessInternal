""" Data methods for the buffalo library

This module consists of methods which will be useful to load the buffalo
data for your assignment. It also contains the implementation of the class
structure which will represent the Buffalo.

The classes in this module are:
    * Buffalo

The functions in this module are:
    * load_data

"""
import random as rd
import numpy as np


class IncorrectArgument(Exception):
    """ Custom exception to capture incorrect arguments
    """
    pass


class Buffalo:
    """
        This is a simple class representing a Buffalo

        This class does not have any public attributes
        and thus you should use the methods to get and update
        each of the Buffalo's attributes.
    """

    def __init__(self, start_pos, end_pos, age):
        """Setting up the Buffalo class


        Args:
            start_pos (array_like) Array of the start position of the Buffalo
            end_pos (array_like) Array of the end position of the Buffalo
            age : (int or float) Array of the end position of the Buffalo

        Returns:
            None
        """

        self.start_pos = start_pos
        self.end_pos = end_pos
        self.age = age

    def get_pos(self, time):
        """Get position of the Buffalo at a certain time


        Args:
            time (int) Integer giving the time at which we require the position

        Returns:
            array_like: Returns the requested position
        """
        if time == 0:
            return self.start_pos

        if time == 1:
            return self.end_pos

        raise IncorrectArgument("Unknown time requested")

    def get_stats(self):
        """Getting statistics on this Buffalo

        Args:
            None

        Returns:
            dict: A dictionary mapping each of the properties of the Buffalo to
            the respective value.

        """
        return {"age": self.age}


def load_data(data_set_id):
    """
    Loads a specific Buffalo dataset from all of the datasets
    we collect every year

    Args:
        data_set_id: The ID of the dataset you wish to load


    Returns:
        list of Buffalo in this dataset, each Buffalo is represented by the
        Buffalo class
    """

    np.random.seed(data_set_id)

    # Number of individuals in each cluster
    num_individuals = 100
    num_clusters = 3

    # Generate random positions for each cluster
    cluster_centers = np.array([
        [10, 10],  # Center of Cluster 1
        [30, 30],  # Center of Cluster 2
        [50, 10]   # Center of Cluster 3
    ])

    # Average ages of each cluster:
    mean_age = np.array([12, 6, 10])
    std_deviation = 5
    # Generate random positions around cluster centers
    positions = []
    ages = []

    for i in range(num_clusters):
        center = cluster_centers[i]
        cluster_positions = center + np.random.randn(
            num_individuals // num_clusters, 2) * 5
        cluster_ages = np.random.normal(
            mean_age[i],
            std_deviation,
            num_individuals //
            num_clusters)
        positions.append(cluster_positions)
        ages.append(cluster_ages)

    # Ensure all ages are positive
    ages = np.maximum(0, ages)

    # Convert ages to integers if needed
    ages = ages.astype(int)

    ages = np.hstack(ages)

    # move one time step:

    # Initialize velocities for each cluster
    cluster_velocities = np.array([
        [-0.5, -0.5],  # Velocity of Cluster 1 towards the center
        [-0.5, 0],     # Velocity of Cluster 2 to the left
        np.random.randn(2) * 0.2  # Random velocity for Cluster 3
    ])

    # Generate random positions around cluster centers
    positions = []
    for i in range(num_clusters):
        center = cluster_centers[i]
        cluster_positions = center + np.random.randn(
            num_individuals // num_clusters, 2) * 5
        positions.append(cluster_positions)

    # Combine positions from all clusters
    positions_initial = np.vstack(positions)

    
    # Update positions based on velocities for each cluster
    for i in range(num_clusters):
        positions[i] += cluster_velocities[i]

    # Combine positions from all clusters
    positions_final = np.vstack(positions)

    data = []
    for i in range(num_individuals-1):
        pos1 = positions_initial[i, :]
        pos2 = positions_final[i, :]
        age = ages[i]
        data.append(Buffalo(pos1, pos2, age))

    rd.shuffle(data)

    return data
