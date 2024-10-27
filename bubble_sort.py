def sorter(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def decompress_braces(string):
    numbers = "123456789"
    stack = []

    for char in string:
        if char in numbers:
            stack.append(int(char))
        elif char == "{":
            continue
        elif char.isalpha():
            stack.append(char)
        elif char == "}":
            segment_chars = []
            while isinstance(stack[-1], str):
                segment_chars.append(stack.pop())
            segment_chars.reverse()
            segment = "".join(segment_chars)
            num = stack.pop()
            stack.append(segment * num)
    return "".join(stack)


def sorter_one_level_depth(arr):
    return sorter(arr)
