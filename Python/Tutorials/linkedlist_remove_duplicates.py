'''
Name: Remove Duplicates from a sorted LinkedList
Date: May 20, 2021

Example:
Input:
{1, 2, 2, 2, 3, 4, 4, 5}
Output:
{1, 2, 3, 4, 5}

'''


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_ll(head):
    l = []
    cur = head
    while cur:
        l.append(cur.val)
        cur = cur.next

    print(l)


def remove_dupes(head):
    cur = head
    while cur:
        if cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
                continue
        cur = cur.next
    return head


if __name__ == "__main__":
    # read input list into linkedlist
    node = head = None
    input = [1, 1, 1, 2, 2, 2, 3, 4, 4, 5]
    for n in input:
        if node == None:
            node = head = Node(n)
        else:
            node.next = Node(n)
            node = node.next

    print_ll(head)
    remove_dupes(head)
    print_ll(head)
