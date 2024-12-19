def sorter_one_level_depth(arr):
    return sorter(arr)


def sorter(arr):
    def quicksort(low, high):
        if low < high:
            pivot_index = partition(low, high)
            quicksort(low, pivot_index - 1)
            quicksort(pivot_index + 1, high)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    quicksort(0, len(arr) - 1)
    return arr


# def decompress_braces(string):
#     numbers = "123456789"
#     stack = []

#     for char in string:
#         if char in numbers:
#             stack.append(int(char))
#         elif char == "{":
#             continue
#         elif "a" <= char <= "z" or "A" <= char <= "Z":
#             stack.append(char)
#         elif char == "}":
#             segment = ""
#             while isinstance(stack[-1], str):
#                 popped_char = stack.pop()
#                 segment = popped_char + segment
#             num = stack.pop()
#             stack.append(segment * num)
#     return "".join(stack)


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)
