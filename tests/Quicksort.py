def quick_sort(arr):
    lesser = []
    equal = []
    greater = []
    if len(arr)>1:
        pivot = arr[len(arr)-1]
        start = 0
        while start<len(arr):
            if arr[start] > pivot:
                greater.append(arr.pop(start)) 
            elif arr[start] < pivot:
                lesser.append(arr.pop(start))
            else:
                start = start + 1

        return (quick_sort(lesser) + arr + quick_sort(greater))

    else:
        return arr




    