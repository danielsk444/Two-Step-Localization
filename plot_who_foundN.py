import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_time_dif(file_name):
    # Define the file name

    # Load the Excel file
    df = pd.read_excel(file_name)

    # Check if the DataFrame has at least 34 columns
    if df.shape[1] < 34:
        raise ValueError("The Excel file does not contain at least 34 columns.")

    # Values to filter by in column 33 (index 32 in 0-based index)
    filter_values = [100, 200, 400, 1000]

    # Create subsets based on the 33rd column values and the 30th column values
    big_subset = df[df.iloc[:, 24] == 'BIG']
    ultrasat_subset = df[df.iloc[:, 24] == 'ULTRASAT']

    # Create a dictionary to store subsets of data for each filter value and 'BIG'
    data_subsets_big = {value: big_subset[big_subset.iloc[:, 33] == value] for value in filter_values}

    # Create subplots for column 11, 12, and 13 histograms
    plt.figure(figsize=(36, 24))  # Adjusted figure size to accommodate more plots

    # Plot for each filter value in 'BIG' subset
    for idx, value in enumerate(filter_values):
        subset = data_subsets_big[value]

        # Plotting column 11 for BIG
        plt.subplot(6, 4, 3 * idx + 1)  # Adjusted subplot position
        sns.histplot(subset.iloc[:, 11], kde=False, color='red', alpha=0.6)
        plt.title(f'BIG: Col 33 = {value} - Column 11')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

        # Plotting column 12 for BIG
        plt.subplot(6, 4, 3 * idx + 2)  # Adjusted subplot position
        sns.histplot(subset.iloc[:, 12], kde=False, color='green', alpha=0.6)
        plt.title(f'BIG: Col 33 = {value} - Column 12')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

        # Plotting column 13 for BIG
        plt.subplot(6, 4, 3 * idx + 3)  # Adjusted subplot position
        sns.histplot(subset.iloc[:, 13], kde=False, color='blue', alpha=0.6)
        plt.title(f'BIG: Col 33 = {value} - Column 13')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

    # Plotting column 11, 12, and 13 for ULTRASAT
    for i, (col, color, title_suffix) in enumerate(zip([11, 12, 13], ['red', 'green', 'blue'], ['11', '12', '13'])):
        plt.subplot(6, 4, len(filter_values) * 3 + i + 1)
        sns.histplot(ultrasat_subset.iloc[:, col], kde=False, color=color, alpha=0.6)
        plt.title(f'ULTRASAT - Column {title_suffix}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

    # Plotting column 11, 12, and 13 for all data
    for i, (col, color, title_suffix) in enumerate(zip([11, 12, 13], ['red', 'green', 'blue'], ['11', '12', '13'])):
        plt.subplot(6, 4, len(filter_values) * 3 + 3 + i + 1)
        sns.histplot(pd.concat([big_subset.iloc[:, col], ultrasat_subset.iloc[:, col]], axis=0), kde=False, color=color, alpha=0.6)
        plt.title(f'All Data - Column {title_suffix}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

# Call the function to execute
def plot_who_foundN(file_name):
    plot_time_dif(file_name)
