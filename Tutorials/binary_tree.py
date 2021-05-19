class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.val)


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def traverse(self, start, traversal=[]):
        # root, left, right traversal
        if start:
            traversal.append(start.val)
            traversal = self.traverse(start.left, traversal)
            traversal = self.traverse(start.right, traversal)
        return traversal

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


if __name__ == "__main__":
    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7

    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.traverse(tree.root))

    print(tree.height(tree.root))
