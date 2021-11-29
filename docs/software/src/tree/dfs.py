import binarytree
from collections import defaultdict


def dfs(node: binarytree.Node):
    if node:
        values['pre-order'].append(node.value)
        dfs(node.left)
        values['in-order'].append(node.value)
        dfs(node.right)
        values['post-order'].append(node.value)


if __name__ == '__main__':
    values = defaultdict(list)
    root = binarytree.tree(height=2, is_perfect=True)
    dfs(root)
    print(root)
    for k, v in values.items():
        print(f'{k}\t: {v}')

