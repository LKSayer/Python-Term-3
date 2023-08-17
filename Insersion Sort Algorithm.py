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
  
  
# Driver code to test above
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
  
    insersionsort(arr)
  
    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")