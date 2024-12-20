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


def decompress_braces(string: str) -> str:
    numbers = "123456789"
    stack: list[str | int] = []

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
                segment = str(popped_char) + segment
            num = stack.pop()
            stack.append(segment * int(num))
    return "".join([str(item) for item in stack])


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)


def find_last_node(nodes, edges):
    """This function receives a flow and returns the last node."""
    sources = {e["source"] for e in edges}
    return next((n for n in nodes if n["id"] not in sources), None)
