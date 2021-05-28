'''
Name: Merge Two Sorted Lists
Problem URL: https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3592/
Date Completed: May 19, 2021

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''


class Solution:
    def mergeTwoLists(self, l1, l2):
        # keep track of head as merged moves to next
        head = merged = ListNode()

        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next

            merged = merged.next

        # attach whatevers remaining in non-empty list
        merged.next = l1 or l2

        # return next to remove leading 0 from list init
        return head.next
