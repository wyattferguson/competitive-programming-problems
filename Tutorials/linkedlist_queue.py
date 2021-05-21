'''
Name: Queue Implementation using a Linked List
Date: May 20, 2021
'''


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Queue():
    def __init__(self):
        self.front = self.back = None

    def add(self, n=0):
        node = Node(n)
        if self.front is None:
            self.front = self.back = node
        else:
            self.back.next = node
            self.back = self.back.next

    def pop(self):
        if self.front == None:
            return None
        val = self.front.val
        self.front = self.front.next
        return val

    def peek(self):
        return self.front.val if self.front else None

    def __str__(self):
        tmp = []
        cur = self.front
        while cur:
            tmp.append(cur.val)
            cur = cur.next

        return str(tmp)


if __name__ == "__main__":
    test = Queue()
    test.add(3)
    test.add(1)
    test.add(6)
    test.add(5)
    print(test)
    print(test.pop())
    print(test.pop())
    test.add(9)
    print(test)

    print(test.peek())
