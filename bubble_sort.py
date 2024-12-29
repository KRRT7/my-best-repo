from __future__ import annotations


def sorter_one_level_depth(arr):
    return sorter(arr)


def sorter(arr):
    arr.sort()  # Using Python's built-in Timsort algorithm
    return arr


def sorter_typed(arr: list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


def sorter_one_level_depth_lower(arr):
    return sorter(arr)


def add(a, b):
    return a + b


def add_one_level_depth(a, b):
    return add(a, b)


def find_last_node_untyped(nodes, edges):
    """This function receives a flow and returns the last node."""
    return next((n for n in nodes if all(e["source"] != n["id"] for e in edges)), None)


def find_last_node_typed(
    nodes: list[dict[str, int]], edges: list[dict[str, int]]
) -> dict[str, int] | None:
    """This function receives a flow and returns the last node."""
    return next((n for n in nodes if all(e["source"] != n["id"] for e in edges)), None)
