import unittest
from algorithms.sorting.merge_sort import *


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual([2,3,5,14,23],merge_sort_all([5,23,3,14,2]))  # add assertion here
        self.assertListEqual([1, 2, 3, 4, 5, 6, 6, 14, 17, 22, 23, 23],merge_sort_all([5, 22, 23, 4, 6, 1, 3, 6, 23, 17, 14, 2]))


if __name__ == '__main__':
    unittest.main()
