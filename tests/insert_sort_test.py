import unittest
from algorithms.sorting.insert_sort import insert_sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertListEqual([2,3,5,14,23],insert_sort([5,23,3,14,2]))  # add assertion here


if __name__ == '__main__':
    unittest.main()
