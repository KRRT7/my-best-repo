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
    segment_builder = []

    for char in string:
        if char in numbers:
            stack.append(int(char))
        elif "a" <= char <= "z" or "A" <= char <= "Z":
            stack.append(char)
        elif char == "}":
            segment_builder.clear()
            while isinstance(stack[-1], str):
                segment_builder.append(stack.pop())
            segment_builder.reverse()
            segment = "".join(segment_builder)
            num = stack.pop()
            stack.append(segment * num)

    return "".join(stack)
