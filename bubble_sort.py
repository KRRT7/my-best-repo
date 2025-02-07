from functools import lru_cache
from typing import Any


def sorter(arr: list[int]) -> list[int]:
    arr.sort()  # Efficient Timsort is applied here
    return arr


def add_numbers(x: int, y: int) -> int:
    """Adds two integers."""
    return x + y


def concatenate_strings(s1: str, s2: str) -> str:
    """Concatenates two strings."""
    return s1 + s2


def append_to_list(my_list: list[int], element: int) -> list[int]:
    """Appends an element to a list of integers."""
    my_list.append(element)
    return my_list


def get_dict_value(my_dict: dict[str, int], key: str) -> int | None:
    """Retrieves a value from a dictionary, handling potential KeyError."""
    return my_dict.get(key)


def union_sets(set1: set[int], set2: set[int]) -> set[int]:
    """Returns the union of two sets of integers."""
    return set1 | set2


def calculate_tuple_sum(my_tuple: tuple[int, int, int]) -> int:
    """Calculates the sum of elements in a 3-element integer tuple."""
    a, b, c = my_tuple
    return a + b + c


def check_number_range(num: int, lower: int, upper: int) -> bool:
    """Checks if a number is within a specified range (inclusive)."""
    return lower <= num <= upper


def format_greeting(name: str, age: int) -> str:
    """Formats a greeting string using name and age."""
    return f"Hello, {name}! You are {age} years old."


def process_value(value: int | str) -> str:
    """Processes a value that can be either an integer or a string."""
    if isinstance(value, int):
        return f"The number is: {value}"
    else:
        return f"The string is: {value}"


def filter_even_numbers(numbers: list[int]) -> list[int]:
    """Filters a list of integers, returning only the even numbers."""
    return [num for num in numbers if num % 2 == 0]


def process_any_value(value: Any) -> str:
    """Demonstrates the use of 'Any' type hint (avoid in production if possible)."""
    return f"Received value: {value}"
