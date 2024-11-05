'''
Name: Stack Implementation using a Linked List
Date: May 20, 2021
'''


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def push(self, n=0):
        node = Node(n)
        if self.head is None:
            self.head = node
        else:
            pointer = self.head
            self.head = node
            self.head.next = pointer

    def pop(self):
        if self.head == None:
            return None

        val = self.head.val
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.val if self.head else None

    def __str__(self):
        stack = []
        cur = self.head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        return str(stack)


if __name__ == "__main__":
    test = Stack()
    test.push(5)
    test.push(2)
    test.push(6)
    test.push(8)
    print(test)
    print("Pop:", test.pop())
    print("Peek:", test.peek())
    print(test)
    test.push(4)
    test.push(4)
    print("Pop:", test.pop())
    print(test)
