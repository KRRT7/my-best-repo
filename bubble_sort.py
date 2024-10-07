def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                swapped = True
        if not swapped:
            break
    return arr
