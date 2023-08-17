# Linear Search in Python
 
#defining the term "linearSearch"
def linearSearch(arr, N, x):
 
 #if I is in the range of elements, return i, else return -1
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
    
    # Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40, 1, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    x = 9
    N = len(arr)
  
    # Function call
    result = linearSearch(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)



