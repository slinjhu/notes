import unittest

from binarytree import tree

from .dfs import dfs


class TestBinaryTree(unittest.TestCase):
    def test_dfs(self):
        root = tree(height=3, is_perfect=True)
        dfs(root)
        print(root)


if __name__ == '__main__':
    unittest.main()

