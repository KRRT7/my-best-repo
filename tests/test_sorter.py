from bubble_sort import sorter


def test_sorter():
    assert sorter([3, 2, 1]) == [1, 2, 3]
    assert sorter([1, 2, 3]) == [1, 2, 3]
    assert sorter([1, 3, 2]) == [1, 2, 3]
    assert sorter([3, 1, 2]) == [1, 2, 3]
    assert sorter([2, 3, 1]) == [1, 2, 3]
