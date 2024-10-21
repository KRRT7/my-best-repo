def sorter(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def decompress_braces(string):
    numbers = "123456789"
    stack = []

    for char in string:
        if char in numbers:
            stack.append(int(char))
        elif char == "{":
            continue
        # Below condition tells about what to be done when we encounter alphabyte.
        elif "a" <= char <= "z" or "A" <= char <= "Z":
            stack.append(char)
        # Here you can use "else" also, but for better understanding(to know when
        # this code block will execute, i am keeping "elif" here).
        elif char == "}":
            segment = ""
            while isinstance(stack[-1], str):
                popped_char = stack.pop()
                segment = popped_char + segment
            num = stack.pop()
            stack.append(segment * num)
    return "".join(stack)
