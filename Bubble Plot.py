import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def bubbleSort(arr):
    n = len(arr)
      
    # Traverse through all array elements
    for i in range(n):
        swapped = False
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

 

def read_excel_file(file_path):

    try:

        df = pd.read_excel(file_path)

 

        print("Data in Excel File")

        print(df)
        column_b = df['Price']
        column_b = column_b.apply(pd.to_numeric, errors='coerce').dropna()

        # Sort the data using insertion sort

        data_column_b = column_b.tolist()

        bubbleSort(data_column_b)
        
        #plot unsorted data
        #column_b is not sorted yet
        plt.plot(column_b)

        #rest is the same
        plt.ylabel('Price')
        plt.title('Unsorted')
        plt.show()

        #plot sorted data
        #data_column_b is sorted
        plt.plot(data_column_b)
        
        #rest is the same       
        plt.ylabel('Price')
        plt.title('Sorted')
        plt.show()

 

 

 

        # Print the sorted data

 

        print("Sorted data in column B:")

 
        for value in data_column_b:

 

            print(value)
            

 

    except FileNotFoundError:

        print("File not found at path: {file_path}")

    except pd.errors.ParserError:

        print("Error parsing the file at path: {file_path}")



if __name__ == "__main__":

    file_path = r'C:\Users\Liam\OneDrive\Documents\Snake\.venv\DiamondValues.xlsx'

    read_excel_file(file_path)