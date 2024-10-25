def sorter(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
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
