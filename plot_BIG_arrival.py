import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
def plot_BIG_arrival(file_name):
    # Define the file name

    # Load the Excel file
    df = pd.read_excel(file_name)

    # Check if the DataFrame has at least 34 columns
    if df.shape[1] < 34:
        raise ValueError("The Excel file does not contain at least 34 columns.")

    # Values to filter by in column 33 (index 32 in 0-based index)
    filter_values1 = ['BIG','Swope']
    filter_values2 = ['ULTRASAT','Swope']

    # Create subsets based on the 33rd column values and the 30th column values
    big_subset = df[df.iloc[:, 24] == 'BIG']
    ultrasat_subset = df[df.iloc[:, 24] == 'ULTRASAT']

    # Create a dictionary to store subsets of data for each filter value and 'BIG'
    data_subsets_big1 = {value: big_subset[big_subset.iloc[:, 11] == value] for value in filter_values1}
    data_subsets_big2 = {value: big_subset[big_subset.iloc[:, 12] == value] for value in filter_values1}
    data_subsets_big3 = {value: big_subset[big_subset.iloc[:, 13] == value] for value in filter_values1}
    data_subsets_ULTRASAT1 = {value: ultrasat_subset[ultrasat_subset.iloc[:, 11] == value] for value in filter_values2}
    data_subsets_ULTRASAT2 = {value: ultrasat_subset[ultrasat_subset.iloc[:, 12] == value] for value in filter_values2}
    data_subsets_ULTRASAT3 = {value: ultrasat_subset[ultrasat_subset.iloc[:, 13] == value] for value in filter_values2}

    swope_subset1 = data_subsets_big1['Swope']
    swope_subset2 = data_subsets_big2['Swope']
    swope_subset3 = data_subsets_big3['Swope']
    big_subset1 = data_subsets_big1['BIG']
    big_subset2 = data_subsets_big2['BIG']
    big_subset3 = data_subsets_big3['BIG']
    ULTRASAT_subset1 = data_subsets_ULTRASAT1['ULTRASAT']
    ULTRASAT_subset2 = data_subsets_ULTRASAT2['ULTRASAT']
    ULTRASAT_subset3 = data_subsets_ULTRASAT3['ULTRASAT']

    time_dif1_big1 = big_subset1.iloc[:, 0]
    time_dif2_big1 = big_subset1.iloc[:, 1]
    time_dif1_big2 = big_subset2.iloc[:, 0]
    time_dif2_big2 = big_subset2.iloc[:, 1]
    time_dif1_big3 = big_subset3.iloc[:, 0]
    time_dif2_big3 = big_subset3.iloc[:, 1]
    time_dif1_ULTRASAT1 = ULTRASAT_subset1.iloc[:, 0]
    time_dif2_ULTRASAT1 = ULTRASAT_subset1.iloc[:, 1]
    time_dif1_ULTRASAT2 = ULTRASAT_subset2.iloc[:, 0]
    time_dif2_ULTRASAT2 = ULTRASAT_subset2.iloc[:, 1]
    time_dif1_ULTRASAT3 = ULTRASAT_subset3.iloc[:, 0]
    time_dif2_ULTRASAT3 = ULTRASAT_subset3.iloc[:, 1]

    time_big1 = big_subset1.iloc[:, 5]
    time_big2 = big_subset2.iloc[:, 7]
    time_big3 = big_subset3.iloc[:, 9]

    time_ULTRASAT1 = ULTRASAT_subset1.iloc[:, 5]
    time_ULTRASAT2 = ULTRASAT_subset2.iloc[:, 7]
    time_ULTRASAT3 = ULTRASAT_subset3.iloc[:, 9]

    # Initialize lists for plotting
    value1arr = []
    value2arr = []
    Indexarr = []

    # Plotting for big_subset1 vs big_subset2
    for index1, value1 in time_big1.items():
        for index2, value2 in time_big2.items():
            if index1 == index2:
                Indexarr.append(index1)
                value1arr.append(value1)
                value2arr.append(value2)
    big_1_2 = [value2arr[i] - value1arr[i] for i in range(len(value2arr))]

    plt.plot(Indexarr, value1arr, 'o', label='Big1 vs Big2')
    plt.plot(Indexarr, value2arr, 'x', label='Big2 vs Big2')
    plt.show()

    value1arr = []
    value2arr = []
    Indexarr = []

    # Plotting for big_subset1 vs big_subset3
    for index1, value1 in time_big1.items():
        for index2, value2 in time_big3.items():
            if index1 == index2:
                Indexarr.append(index1)
                value1arr.append(value1)
                value2arr.append(value2)
    big_1_3 = [value2arr[i] - value1arr[i] for i in range(len(value2arr))]

    plt.plot(Indexarr, value1arr, 'o', label='Big1 vs Big3')
    plt.plot(Indexarr, value2arr, 'x', label='Big3 vs Big3')
    plt.show()

    value1arr = []
    value2arr = []
    Indexarr = []

    # Plotting for ULTRASAT_subset1 vs ULTRASAT_subset2
    for index1, value1 in time_ULTRASAT1.items():
        for index2, value2 in time_ULTRASAT2.items():
            if index1 == index2:
                Indexarr.append(index1)
                value1arr.append(value1)
                value2arr.append(value2)
    ULTRASAT_1_2 = [value2arr[i] - value1arr[i] for i in range(len(value2arr))]

    plt.plot(Indexarr, value1arr, 'o', label='ULTRASAT1 vs ULTRASAT2')
    plt.plot(Indexarr, value2arr, 'x', label='ULTRASAT2 vs ULTRASAT2')
    plt.show()

    value1arr = []
    value2arr = []
    Indexarr = []

    # Plotting for ULTRASAT_subset1 vs ULTRASAT_subset3
    for index1, value1 in time_ULTRASAT1.items():
        for index2, value2 in time_ULTRASAT3.items():
            if index1 == index2:
                Indexarr.append(index1)
                value1arr.append(value1)
                value2arr.append(value2)
    ULTRASAT_1_3 = [value2arr[i] - value1arr[i] for i in range(len(value2arr))]

    plt.plot(Indexarr, value1arr, 'o', label='ULTRASAT1 vs ULTRASAT3')
    plt.plot(Indexarr, value2arr, 'x', label='ULTRASAT3 vs ULTRASAT3')
    plt.show()

    # Show legend
    #plt.legend()

    sns.histplot(big_1_2, kde=True, label='First Column (All)', color='blue', alpha=0.6)
    sns.histplot(big_1_3, kde=True, label='Second Column (All)', color='orange', alpha=0.6)
    plt.title('Combined Data - All Categories')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()

    plt.tight_layout()

    plt.show()

    sns.histplot(ULTRASAT_1_2, kde=True, label='First Column (All)', color='blue', alpha=0.6)
    sns.histplot(ULTRASAT_1_3, kde=True, label='Second Column (All)', color='orange', alpha=0.6)
    plt.title('Combined Data - All Categories')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()

    plt.show()
    # Show the plot
