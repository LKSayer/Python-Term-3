# Python program for implementation of Selection
# Sort
import sys
def selection_sort(arr):

    # Selection sort implementation

    n = len(arr)

    for i in range(n):

        min_idx = i

        for j in range(i+1, n):

            if arr[j] < arr[min_idx]:

                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
 
#sorted1= selection_sort([2,69,5,25,68,46])
#print(sorted1)
