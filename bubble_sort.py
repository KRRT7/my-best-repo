def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # To track if any swap happens
        for j in range(n - 1 - i):  # Reduce the range of j in each pass
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swap happened, the list is sorted
            break
    return arr
