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
    append_stack = stack.append

    for char in string:
        if char in numbers:
            append_stack(int(char))
        elif "a" <= char <= "z" or "A" <= char <= "Z":
            append_stack(char)
        elif char == "}":
            segment = []
            while isinstance(stack[-1], str):
                segment.append(stack.pop())
            segment.reverse()
            num = stack.pop()
            append_stack("".join(segment) * num)

    return "".join(stack)


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)
