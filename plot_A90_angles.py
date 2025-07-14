import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
def plot_A90_angles(file_name):

    # Load the data
    df = pd.read_excel(file_name)
    for j in range(3):
        # Extract columns
        x = df.iloc[:, 35].values  # Column 15
        y = df.iloc[:, 36].values  # Column 16
        z = df.iloc[:, 20+j].values   # Column 2

        # Create a grid for interpolation
        xi, yi = np.meshgrid(np.linspace(x.min(), x.max(), 100),
                             np.linspace(y.min(), y.max(), 100))
        zi = griddata((x, y), z, (xi, yi), method='linear')

        # Plotting
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(xi, yi, zi, shading='auto', cmap='viridis')
        plt.colorbar(label='Column 2 value')
        plt.xlabel('Column 15')
        plt.ylabel('Column 16')
        plt.title('Colormap of Column 2 Dependence on Columns 15 and 16')
        plt.show()
    for j in range(3):
        # Extract columns
        x = df.iloc[:, 37].values  # Column 15
        y = df.iloc[:, 38].values  # Column 16
        z = df.iloc[:, 20+j].values   # Column 2

        # Create a grid for interpolation
        xi, yi = np.meshgrid(np.linspace(x.min(), x.max(), 100),
                             np.linspace(y.min(), y.max(), 100))
        zi = griddata((x, y), z, (xi, yi), method='linear')

        # Plotting
        plt.figure(figsize=(8, 6))
        plt.pcolormesh(xi, yi, zi, shading='auto', cmap='viridis')
        plt.colorbar(label='Column 2 value')
        plt.xlabel('Column 15')
        plt.ylabel('Column 16')
        plt.title('Colormap of Column 2 Dependence on Columns 15 and 16')
        plt.show()

    fig = plt.figure(figsize=(14, 7))

    # Plot the colormaps on a sphere
    for j in range(3):
        ax = fig.add_subplot(2, 3, j + 1, projection='3d')

        # Extract columns
        theta = df.iloc[:, 35].values  # Column 15
        phi = df.iloc[:, 36].values  # Column 16
        z = df.iloc[:, 20 + j].values  # Column 2

        # Convert spherical coordinates to Cartesian coordinates
        x = np.sin(phi) * np.cos(theta)
        y = np.sin(phi) * np.sin(theta)
        z = np.cos(phi)

        # Create a grid for interpolation
        xi, yi = np.meshgrid(np.linspace(theta.min(), theta.max(), 100),
                             np.linspace(phi.min(), phi.max(), 100))
        zi = griddata((theta, phi), z, (xi, yi), method='linear')

        # Convert grid to Cartesian coordinates for plotting
        xi_cart = np.sin(yi) * np.cos(xi)
        yi_cart = np.sin(yi) * np.sin(xi)
        zi_cart = np.cos(yi)

        # Plotting
        surf = ax.plot_surface(xi_cart, yi_cart, zi_cart, facecolors=plt.cm.viridis(zi_cart), rstride=1, cstride=1, antialiased=False)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Colormap of Column 2-{j + 1} on Sphere')

    # Repeat for the second set of columns
    for j in range(3):
        ax = fig.add_subplot(2, 3, j + 4, projection='3d')

        # Extract columns
        theta = df.iloc[:, 37].values  # Column 15
        phi = df.iloc[:, 38].values  # Column 16
        z = df.iloc[:, 20 + j].values  # Column 2

        # Convert spherical coordinates to Cartesian coordinates
        x = np.sin(phi) * np.cos(theta)
        y = np.sin(phi) * np.sin(theta)
        z = np.cos(phi)

        # Create a grid for interpolation
        xi, yi = np.meshgrid(np.linspace(theta.min(), theta.max(), 100),
                             np.linspace(phi.min(), phi.max(), 100))
        zi = griddata((theta, phi), z, (xi, yi), method='linear')

        # Convert grid to Cartesian coordinates for plotting
        xi_cart = np.sin(yi) * np.cos(xi)
        yi_cart = np.sin(yi) * np.sin(xi)
        zi_cart = np.cos(yi)

        # Plotting
        surf = ax.plot_surface(xi_cart, yi_cart, zi_cart, facecolors=plt.cm.viridis(zi_cart), rstride=1, cstride=1, antialiased=False)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f'Colormap of Column 2-{j + 1} on Sphere')

    plt.tight_layout()
    plt.show()
