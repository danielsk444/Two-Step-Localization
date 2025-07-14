import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata
def plot_time_start_end_points(file_name):

    # Load the data
    df = pd.read_excel(file_name)
    for i in range(3):
        for j in range(3):
            # Extract columns
            x = df.iloc[:, 15+i].values  # Column 15
            y = df.iloc[:, 16+i].values  # Column 16
            z = df.iloc[:, 2+j].values   # Column 2

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
