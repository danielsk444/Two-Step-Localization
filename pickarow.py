import pandas as pd

def pickarow(row)  :
    row_values=[]
    filename = 'recordingsN19.xlsx'

    # Load the Excel file into a DataFrame
    df = pd.read_excel(filename)

    # Extract the values from row 13 (0-based index is 12)
    try:
        row_values = df.iloc[row].tolist()
        # Optionally convert values to float if they are not already
        row_values = [float(value) for value in row_values]
    except IndexError:
        print("Error: The file does not contain enough rows.")
    except ValueError:
        print("Warning: Some values in row 13 could not be converted to float.")

    return row_values