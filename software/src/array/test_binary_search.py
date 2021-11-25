import unittest

from .binary_search2 import binary_search2
from .binary_search3 import binary_search3


class TestBinarySearch2(unittest.TestCase):

    def exec2(self, xx, target, expected_index):
        self.assertEqual(binary_search2(xx, target), expected_index)

    def exec(self, xx, target, expected_index):
        self.exec2(xx, target, expected_index)
        self.exec3(xx, target, expected_index)

    def exec3(self, xx, target, expected_index):
        self.assertEqual(binary_search3(xx, target), expected_index)

    def test_empty(self):
        self.exec([], 1, 0)

    def test_not_found(self):
        self.exec(list(range(5)), 9, 5)
        self.exec(list(range(5)), -1, 0)
        self.exec([1, 1, 2, 2], 3, 4)

    def test_easy_find(self):
        for i in range(8):
            self.exec(list(range(9)), i, i)

    def test_binary_search2(self):
        self.exec2([], 1, 0)
        self.exec2([0, 1, 1, 2], 1, 1)
        self.exec2([0, 1, 1, 2], 2, 3)
        self.exec2([0, 1, 1, 3], 2, 3)




if __name__ == '__main__':
    unittest.main()



