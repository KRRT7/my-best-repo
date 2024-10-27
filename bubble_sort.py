def sorter(arr):
    arr.sort()
    return arr


def decompress_braces(string):
    # Store the valid characters and digits for faster checks
    numbers = set("123456789")
    stack = []
    i = 0
    length = len(string)

    while i < length:
        char = string[i]

        # Check if the character is a digit
        if char in numbers:
            stack.append(int(char))

        # Check if it's a letter
        elif char.isalpha():
            stack.append(char)

        # Handling closing braces
        elif char == "}":
            segment = []
            while isinstance(stack[-1], str):
                segment.append(stack.pop())
            segment.reverse()
            num = stack.pop()
            stack.append("".join(segment) * num)

        # Move to the next character
        i += 1

    return "".join(stack)


def sorter_one_level_depth(arr):
    arr.sort()
    return arr
