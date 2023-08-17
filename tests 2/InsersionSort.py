def insertion_sort(arr):

    # Insertion sort implementation

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1] = arr[j]

            j -= 1

        arr[j + 1] = key

    return arr
sorted1= insertion_sort([2,69,5,25,68,46])
print(sorted1)
