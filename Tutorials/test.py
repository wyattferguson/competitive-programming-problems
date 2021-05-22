# Data structure to store a binary tree node
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Utility function to check if a given node is a leaf node
def isLeaf(node):
    return node.left is None and node.right is None


# Function to apply an operator `op` to values `x` and `y` and return the result
def process(op, x, y):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '×':
        return x * y
    if op == '/':
        return x / y


# Recursive function to evaluate a binary expression tree
def evaluate(root):

    # base case: invalid input
    if root is None:
        return 0

    # the leaves of a binary expression tree are operands
    if isLeaf(root):
        return int(root.val)

    # recursively evaluate the left and right subtree
    x = evaluate(root.left)
    y = evaluate(root.right)

    # apply the operator at the root to the values obtained in the previous step
    return process(root.val, x, y)


if __name__ == '__main__':

    root = Node('+')
    root.left = Node('×')
    root.right = Node('/')
    root.left.left = Node('-')
    root.left.right = Node('5')
    root.right.left = Node('21')
    root.right.right = Node('7')
    root.left.left.left = Node('10')
    root.left.left.right = Node('5')

    print('The value of the expression tree is', evaluate(root))
