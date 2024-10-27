def sorter(arr):
    arr.sort()
    return arr


def decompress_braces(string):
    numbers = "123456789"
    stack = []
    segment = []
    append_str = segment.append
    pop_str = segment.pop
    append_stack = stack.append
    pop_stack = stack.pop

    for char in string:
        if char in numbers:
            append_stack(int(char))
        elif char.isalpha():
            append_stack(char)
        elif char == "}":
            while isinstance((current := pop_stack()), str):
                append_str(current)
            num = current
            segment.reverse()
            append_stack("".join(segment) * num)
            segment.clear()

    return "".join(stack)


def sorter_one_level_depth(arr):
    return sorter(arr)
