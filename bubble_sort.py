def sorter(arr):
    arr.sort()  # Python's built-in sort is optimized with Timsort and runs in O(n log n) time.
    return arr  # Removed the unnecessary print statements to streamline execution.


def sorterv2(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    total_sum = sum(arr)

    max_value = max(arr)

    return arr, total_sum, max_value
