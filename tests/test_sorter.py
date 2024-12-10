import unittest
from bubble_sort import sorter


class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(sorter([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        self.assertEqual(sorter([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(
            sorter([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
        )

    def test_empty_array(self):
        self.assertEqual(sorter([]), [])

    def test_single_element_array(self):
        self.assertEqual(sorter([1]), [1])

    def test_identical_elements_array(self):
        self.assertEqual(sorter([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])


if __name__ == "__main__":
    unittest.main()
