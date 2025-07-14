import pandas as pd
import matplotlib.pyplot as plt
def plot_time_SNR(file_name):

    # Read the Excel file
    data = pd.read_excel(file_name, engine='openpyxl')
    plt.figure(figsize=(10, 6))

    for i in range(4):
        # Extract the columns of interest
        column_20 = data.iloc[:, 39+i]  # Column 20 (0-indexed)
        column_2 = data.iloc[:, 2]    # Column 2 (0-indexed)
        column_3 = data.iloc[:, 3]    # Column 3 (0-indexed)
        column_4 = data.iloc[:, 4]    # Column 4 (0-indexed)

        # Create a figure and axis for plotting

        # Plot each column against column 20
        plt.subplot(3, 1, 1)
        plt.plot(column_20, column_2, 'o', label='Column 2 vs Column 20')
        plt.xlabel('Column 20')
        plt.ylabel('Column 2')
        #plt.xlim(0, 50000)
        #plt.ylim(0, 400)

        plt.legend()

        plt.subplot(3, 1, 2)
        plt.plot(column_20, column_3, 'o', label='Column 3 vs Column 20')
        plt.xlabel('Column 20')
        plt.ylabel('Column 3')
        #plt.xlim(0, 50000)
        #plt.ylim(0, 400)

        plt.legend()

        plt.subplot(3, 1, 3)
        plt.plot(column_20, column_4, 'o', label='Column 4 vs Column 20')
        plt.xlabel('Column 20')
        plt.ylabel('Column 4')
        #plt.xlim(0, 50000)
        #plt.ylim(0, 400)

        plt.legend()

        # Adjust layout and show plot
        plt.tight_layout()
    plt.show()
