import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_time_dif():

    # Define the file name
    filename = 'recordingsN16.xlsx'

    # Load the Excel file
    df = pd.read_excel(filename)

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

    # Create subplots for all data (BIG and ULTRASAT) in one figure
    plt.figure(figsize=(18, 5))

    # Plot for each filter value in 'BIG' subset
    for idx, value in enumerate(filter_values[:3]):  # Limit to first 3 values for one plot
        subset = data_subsets_big[value]

        # Extract the first and second columns of the subset
        first_column_values = subset.iloc[:, 0]
        second_column_values = subset.iloc[:, 1]

        # Plotting the first and second columns together
        plt.subplot(1, 3, idx + 1)  # One row, three columns
        sns.histplot(first_column_values, kde=True, label='First Column', color='blue', alpha=0.6)
        sns.histplot(second_column_values, kde=True, label='Second Column', color='orange', alpha=0.6)
        plt.title(f'BIG: Col 33 = {value}')
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.legend()

    # Combine all `ULTRASAT` data for plotting
    first_column_values_ultrasat = ultrasat_subset.iloc[:, 0]
    second_column_values_ultrasat = ultrasat_subset.iloc[:, 1]

    # Plotting the first and second columns together (ULTRASAT)
    plt.subplot(1, 3, 3)  # Last subplot
    sns.histplot(first_column_values_ultrasat, kde=True, label='First Column', color='blue', alpha=0.6)
    sns.histplot(second_column_values_ultrasat, kde=True, label='Second Column', color='orange', alpha=0.6)
    plt.title('ULTRASAT - Combined Columns')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Call the function to execute
plot_time_dif()
