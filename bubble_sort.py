def sorter_one_level_depth(arr):
    return sorter(arr)


def sorter(arr):
    arr.sort()
    return arr


def decompress_braces(string):
    numbers = set("123456789")
    stack = []

    i = 0
    while i < len(string):
        if string[i] in numbers:
            num = 0
            while i < len(string) and string[i] in numbers:
                num = num * 10 + int(string[i])
                i += 1
            stack.append(num)
        elif string[i] == "{":
            i += 1
        elif "a" <= string[i] <= "z" or "A" <= string[i] <= "Z":
            stack.append(string[i])
            i += 1
        elif string[i] == "}":
            segment = []
            while isinstance(stack[-1], str):
                segment.append(stack.pop())
            stack.append("".join(reversed(segment)) * stack.pop())
            i += 1
    return "".join(stack)
