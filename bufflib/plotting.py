""" Plotting methods for the buffalo library

This module consists of methods which will be useful to plot data.

The functions in this module are:
    * plot_xy
    * kde_plot
    * quiver_plot

"""
import matplotlib.pyplot as plt
import seaborn as sns


def plot_xy(x_values, y_values, title="", x_label="", y_label=""):
    """
    Plot X and Y values.

    Args:
        x_values (list or numpy.ndarray): The X-axis values.
        y_values (list or numpy.ndarray): The Y-axis values.
        title (str): The plot title (optional).
        x_label (str): The X-axis label (optional).
        y_label (str): The Y-axis label (optional).

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))  # Optional: Set the figure size

    plt.scatter(x_values, y_values, label="Data")  # Plot X and Y values

    plt.title(title)  # Optional: Set the plot title
    plt.xlabel(x_label)  # Optional: Set the X-axis label
    plt.ylabel(y_label)  # Optional: Set the Y-axis label

    plt.legend()  # Optional: Show legend if multiple datasets are plotted

    plt.grid(True)  # Optional: Add a grid to the plot

    plt.show()  # Show the plot


def kde_plot(x_data, y_data, title="", x_label="", y_label=""):
    """
    Create a Kernel Density Estimation (KDE) plot.

    Args:
        x_data (list or numpy.ndarray): The data for the X-axis.
        y_data (list or numpy.ndarray): The data for the Y-axis.
        title (str): The plot title (optional).
        x_label (str): The X-axis label (optional).
        y_label (str): The Y-axis label (optional).

    Returns:
        None
    """
    sns.set(style="whitegrid")  # Set seaborn style

    plt.figure(figsize=(8, 6))  # Optional: Set the figure size

    sns.kdeplot(x=x_data, y=y_data, cmap="Blues", shade=True, cbar=True)

    plt.title(title)  # Optional: Set the plot title
    plt.xlabel(x_label)  # Optional: Set the X-axis label
    plt.ylabel(y_label)  # Optional: Set the Y-axis label

    plt.show()  # Show the plot


def quiver_plot(x, y, u, v, scale=1, title="", x_label="", y_label=""):
    """
    Create a quiver plot to visualize vector fields.

    Args:
        x (list or numpy.ndarray): X-coordinates of the grid points.
        y (list or numpy.ndarray): Y-coordinates of the grid points.
        u (list or numpy.ndarray): X-component of the vectors.
        v (list or numpy.ndarray): Y-component of the vectors.
        scale (float): Scaling factor for the arrow length (default is 1).
        title (str): The plot title (optional).
        x_label (str): The X-axis label (optional).
        y_label (str): The Y-axis label (optional).

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))  # Optional: Set the figure size

    plt.quiver(
        x,
        y,
        u,
        v,
        scale=scale,
        angles='xy',
        scale_units='xy',
        color='b')

    plt.title(title)  # Optional: Set the plot title
    plt.xlabel(x_label)  # Optional: Set the X-axis label
    plt.ylabel(y_label)  # Optional: Set the Y-axis label

    plt.grid(True)  # Optional: Add a grid to the plot

    plt.show()  # Show the plot
