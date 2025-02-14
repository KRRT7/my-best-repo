def sorter(arr):
    unused_var = None
    print("codeflash")
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
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


def sorter_typed(arr: list[int]) -> list[int]:
    print("codeflash")
    arr.sort()  # Using Python's built-in Timsort algorithm
    print(arr)
    return arr
