import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def insertion_sort(arr):

 

    # Insertion sort implementation

 

    for i in range(1, len(arr)):

 

        key = arr[i]

 

        j = i - 1

 

        while j >= 0 and arr[j] > key:

 

            arr[j + 1] = arr[j]

 

            j -= 1

 

        arr[j + 1] = key

 

def read_excel_file(file_path):

    try:

        df = pd.read_excel(file_path)

 

        print("Data in Excel File")

        print(df)
        column_b = df['Price']
        column_b = column_b.apply(pd.to_numeric, errors='coerce').dropna()

        # Sort the data using insertion sort

        data_column_b = column_b.tolist()

        insertion_sort(data_column_b)
        
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