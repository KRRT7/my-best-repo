def sorter(arr):
    # Using Python's built-in sort method, which is highly optimized
    arr.sort()
    print(arr)
    return arr


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
