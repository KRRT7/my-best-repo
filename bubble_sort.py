def sorter_one_level_depth(arr):
    return sorter(arr)


def sorter(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def decompress_braces(string):
    numbers = set("123456789")  # Using set for O(1) lookups
    stack = []
    i = 0
    length = len(string)

    while i < length:
        char = string[i]

        if char in numbers:
            stack.append(int(char))
        elif char == "{":
            i += 1
            continue
        elif char.isalpha():  # Check if the character is an alphabet
            stack.append(char)
        elif char == "}":
            segment = []
            while stack and isinstance(stack[-1], str):
                segment.append(stack.pop())
            num = stack.pop()
            stack.append("".join(reversed(segment)) * num)

        i += 1

    return "".join(stack)


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)
