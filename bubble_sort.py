from functools import lru_cache


def sorter(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


@lru_cache(maxsize=None)
def cached_function(arg):
    """A simple function with lru_cache."""
    return arg + 1, cached_function.cache_info()


class TestClass:
    @lru_cache(maxsize=None)
    def cached_method(self, arg):
        return arg + 2, self.cached_method.cache_info()
