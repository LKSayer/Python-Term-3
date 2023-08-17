# Quick Sort Algorithm

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
 
 
# Driver code
if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)
 
    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")




    