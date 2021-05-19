"""
Singularly Linked List
"""


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


if __name__ == "__main__":
    # generate linked list
    nodes = None
    for n in range(10):
        nodes = Node(n, nodes)

    # print list
    while nodes is not None:
        print(nodes)
        nodes = nodes.next
