import pandas as pd

# Load the Excel file
file_name = 'recordingsN19.xlsx'
df = pd.read_excel(file_name)

# Ensure columns are correctly named; adjust if necessary
# Column 5 is index 4 and Column 6 is index 5 (0-based index)

# Filter rows where value in column 5 is greater than value in column 6
filtered_df = df[df.iloc[:, 6] < df.iloc[:, 5]]

# Output the rows where the condition is met
print('Rows where value in column 5 is greater than value in column 6:')
print(filtered_df)

# Optionally, if you just want to see the indices of these rows:
print('Indices of these rows:')
print(filtered_df.index.tolist())
