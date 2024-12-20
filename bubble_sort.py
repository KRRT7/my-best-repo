def sorter_one_level_depth(arr):
    return sorter(arr)


def sorter(arr):
    n = len(arr)
    for i in range(n):
        # Track if there was a swap
        swapped = False
        for j in range(
            n - i - 1
        ):  # Reduce the range as final elements are already sorted
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
    return arr


def decompress_braces(string: str) -> str:
    numbers = "123456789"
    stack: list[str | int] = []

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
                segment = str(popped_char) + segment
            num = stack.pop()
            stack.append(segment * int(num))
    return "".join([str(item) for item in stack])


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)
