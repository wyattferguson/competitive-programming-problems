"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:

- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

Ex 1.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Ex 2.
Input: l1 = [0], l2 = [0]
Output: [0]

Ex 3.
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998

Ex 4.
Input: l1 = [2,4,9], l2 = [5,6,4,9]
Output: [8,9,8,5]
Explanation: 942 + 9465 = 10407
Expected: [7,0,4,0,1]

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    sum1 = ""
    while l1:
        sum1 += str(l1.val)
        l1 = l1.next

    sum2 = ""
    while l2:
        sum2 += str(l2.val)
        l2 = l2.next

    fin = int(sum1) + int(sum2)

    result = None
    for n in range(len(str(fin))):
        result = ListNode(str(fin)[n], result)

    return result


if __name__ == "__main__":
    # setting up test cases in Linked List form
    list1 = [2, 4, 9]
    list2 = [5, 6, 4, 9]

    l1 = None
    for n in list1:
        l1 = ListNode(n, l1)

    l2 = None
    for n in list2:
        l2 = ListNode(n, l2)

    results = addTwoNumbers(l1, l2)
    while results:
        print(results.val)
        results = results.next
