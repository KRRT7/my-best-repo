def sorter(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = (
                    arr[j + 1],
                    arr[j],
                )  # Use tuple unpacking for swapping
                swapped = True
        if not swapped:
            break  # Stop if no elements were swapped in the inner loop, meaning the array is sorted
    return arr


def decompress_braces(string):
    numbers = "123456789"
    stack = []

    for char in string:
        if char in numbers:
            stack.append(int(char))
        elif char == "{":
            continue
        elif "a" <= char <= "z" or "A" <= char <= "Z":
            stack.append(char)
        elif char == "}":
            segment = ""
            while isinstance(stack[-1], str):
                popped_char = stack.pop()
                segment = popped_char + segment
            num = stack.pop()
            stack.append(segment * num)
    return "".join(stack)


def sorter_one_level_depth(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)
