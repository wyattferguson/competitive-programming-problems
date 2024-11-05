'''
Name: Evaluate a Binary Expression Tree
URL: https://www.techiedelight.com/evaluate-binary-expression-tree/
Date: May 21, 2021
'''


class Node:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

    def __str__(self):
        return str(self.val)


def is_leaf(root):
    return root.left is None and root.right is None


def process(exp, x=0, y=0):
    if exp == '+':
        return x + y
    if exp == '-':
        return x - y
    if exp == '×':
        return x * y
    if exp == '/':
        return x / y


def solve(root):
    if root == None:
        return 0

    if is_leaf(root):
        return int(root.val)

    a = solve(root.left)
    b = solve(root.right)
    return process(root.val, a, b)


if __name__ == "__main__":
    root = Node('+')
    root.left = Node('×')
    root.right = Node('/')
    root.left.left = Node('-')
    root.left.right = Node('5')
    root.right.left = Node('21')
    root.right.right = Node('7')
    root.left.left.left = Node('10')
    root.left.left.right = Node('5')
    n = solve(root)
    print(n)
