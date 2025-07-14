import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot_time_runs(file_name):

    # Define the file name


    # Load the Excel file
    df = pd.read_excel(file_name)
    print(df.shape[1] )
    # Check if the DataFrame has at least 34 columns
    if df.shape[1] < 34:
        raise ValueError("The Excel file does not contain at least 34 columns.")

    # Values to filter by in column 33 (index 32 in 0-based index)
    filter_values = [3, 4, 5]

    # Create subsets based on the 33rd column values
    run3_subset = df[df.iloc[:, 34] == 3]
    run4_subset = df[df.iloc[:, 34] == 4]
    run5_subset = df[df.iloc[:, 34] == 5]

    # Set up the plotting area with 3 subplots
    fig, axes = plt.subplots(3, 1, figsize=(10, 18), sharex=True, sharey=True)

    # Plot histograms for column 2 in the first subplot
    sns.histplot(run3_subset.iloc[:, 2], kde=True, color='blue', bins=30, label='Run 3', alpha=0.5, ax=axes[0])
    sns.histplot(run4_subset.iloc[:, 2], kde=True, color='green', bins=30, label='Run 4', alpha=0.5, ax=axes[0])
    sns.histplot(run5_subset.iloc[:, 2], kde=True, color='red', bins=30, label='Run 5', alpha=0.5, ax=axes[0])
    axes[0].set_title('Histogram of Column 2 for Runs 3, 4, and 5')
    axes[0].set_ylabel('Frequency')
    axes[0].legend(title='Run')

    # Plot histograms for column 3 in the second subplot
    sns.histplot(run3_subset.iloc[:, 3], kde=True, color='blue', bins=30, label='Run 3', alpha=0.5, ax=axes[1])
    sns.histplot(run4_subset.iloc[:, 3], kde=True, color='green', bins=30, label='Run 4', alpha=0.5, ax=axes[1])
    sns.histplot(run5_subset.iloc[:, 3], kde=True, color='red', bins=30, label='Run 5', alpha=0.5, ax=axes[1])
    axes[1].set_title('Histogram of Column 3 for Runs 3, 4, and 5')
    axes[1].set_ylabel('Frequency')
    axes[1].legend(title='Run')

    # Plot histograms for column 4 in the third subplot
    sns.histplot(run3_subset.iloc[:, 4], kde=True, color='blue', bins=30, label='Run 3', alpha=0.5, ax=axes[2])
    sns.histplot(run4_subset.iloc[:, 4], kde=True, color='green', bins=30, label='Run 4', alpha=0.5, ax=axes[2])
    sns.histplot(run5_subset.iloc[:, 4], kde=True, color='red', bins=30, label='Run 5', alpha=0.5, ax=axes[2])
    axes[2].set_title('Histogram of Column 4 for Runs 3, 4, and 5')
    axes[2].set_xlabel('Value')
    axes[2].set_ylabel('Frequency')
    axes[2].legend(title='Run')

    # Adjust layout
    plt.tight_layout()

    # Show the plot
    plt.show()
