
import pandas as pd

import openpyxl

def insersionsort(arr):
    n = len(arr)
      
    # Traverse through all array elements
    for i in range(1, n):
        swapped = False

        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


def read_excel_file(file_path):

    try:

        # Read the Excel file using pandas

        df = pd.read_excel(file_path)

 
        file_path = file_path.apply(pd.to_numeric, errors='coerce').dropna()

       
        # Print the entire DataFrame

        print("Data in the Excel file:")

        print(df)

        insersionsort(file_path)

 

    except FileNotFoundError:

        print(f"File not found at path: {file_path}")

    except pd.errors.ParserError:

        print(f"Error parsing the file at path: {file_path}")

 

if __name__ == "__main__":

    

    file_path = r"C:\Users\Liam\OneDrive\Documents\Snake\.venv\numbers.xlsx"

    read_excel_file(file_path)