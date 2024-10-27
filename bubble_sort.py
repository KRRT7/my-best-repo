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

    append_to_stack = stack.append
    pop_from_stack = stack.pop

    for char in string:
        if char in numbers:
            append_to_stack(int(char))
        elif "a" <= char <= "z" or "A" <= char <= "Z":
            append_to_stack(char)
        elif char == "}":
            segment = []
            while isinstance(stack[-1], str):
                segment.append(pop_from_stack())
            segment.reverse()
            num = pop_from_stack()
            append_to_stack("".join(segment) * num)

    return "".join(stack)


def sorter_one_level_depth(arr):
    return sorter(arr)
