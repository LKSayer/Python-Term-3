# Quick Sort Plot

#import important things
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define Partition

def partition(array, low, high):
    # Choose element furthest in the array as pivot
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # Compare every element to the pivot
    for j in range(low, high):

        # Swap Element if it is lower than pivot
        if array[j] <= pivot: 
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element if the element specified by i is greater than the pivot 
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# Function to perform quicksort
def quicksort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quicksort(array, low, pi - 1)  
 
        # Recursive call on the right of pivot
        quicksort(array, pi + 1, high)
 

def read_excel_file(file_path):

    try:

        df = pd.read_excel(file_path)

 

        print("Data in Excel File")

        print(df)
        column_b = df['Price']
        column_b = column_b.apply(pd.to_numeric, errors='coerce').dropna()

        # Sort the data using quicksort

        data_column_b = column_b.tolist()

        quicksort(data_column_b)
        
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




    