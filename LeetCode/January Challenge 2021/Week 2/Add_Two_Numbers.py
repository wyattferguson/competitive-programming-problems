"""
Name: Add Two Numbers
Problem URL: https://bit.ly/3c3xjhq
Date Completed: May 29, 2021

Description:
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


class Solution:
    def addTwoNumbers(self, list1: ListNode, list2: ListNode):
        def extract(node):
            k = ""
            while node:
                k += str(node.val)
                node = node.next
            return k[::-1]

        a = extract(list1)
        b = extract(list2)
        total = int(a) + int(b)

        ll = None
        for v in str(total):
            ll = ListNode(v, ll)
        return ll
