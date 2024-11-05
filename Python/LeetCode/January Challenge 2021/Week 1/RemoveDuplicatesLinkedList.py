'''
Name: Remove Duplicates from Sorted List II
Problem URL: https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3593/
Date Completed: May 20, 2021

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sent = ListNode(0, head)
        prev = sent
        # while the list still has nodes
        while head:
            # the current node equals the next node
            if head.next and head.val == head.next.val:
                # skip over all duplicates
                while head.next and head.val == head.next.val:
                    head = head.next
                # connect the last none duplicate to the new head
                prev.next = head.next
            else:
                # move holder pointer forward
                prev = prev.next

            # move head forward
            head = head.next
        return sent.next
