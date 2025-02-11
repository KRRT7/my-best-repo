from functools import lru_cache


def is_prime(num):
    # Use a simple cache mechanism
    if not hasattr(is_prime, "cache"):
        is_prime.cache = {}
    if num in is_prime.cache:
        return is_prime.cache[num]

    if num < 2:
        result = False
    elif num == 2:
        result = True
    elif num % 2 == 0:  # Eliminate even numbers greater than 2
        result = False
    else:
        result = True
        for i in range(3, int(num**0.5) + 1, 2):  # Check only odd numbers
            if num % i == 0:
                result = False
                break

    is_prime.cache[num] = result
    return result
