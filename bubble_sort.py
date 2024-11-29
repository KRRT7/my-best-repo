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
    numbers = set("123456789")
    stack = []

    for char in string:
        if char in numbers:
            stack.append(int(char))
        elif char == "{":
            continue
        elif char.isalpha():
            stack.append(char)
        elif char == "}":
            segment = []
            while isinstance(stack[-1], str):
                segment.append(stack.pop())
            segment.reverse()
            num = stack.pop()
            stack.append("".join(segment) * num)
    return "".join(stack)


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)
