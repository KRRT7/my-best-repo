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
    app = stack.append
    stack_pop = stack.pop

    for char in string:
        if char in numbers:
            app(int(char))
        elif char == "{":
            continue
        elif char.isalpha():
            app(char)
        elif char == "}":
            segment = []
            while isinstance(stack[-1], str):
                segment.append(stack_pop())
            segment.reverse()
            num = stack_pop()
            app("".join(segment) * num)
    return "".join(stack)
