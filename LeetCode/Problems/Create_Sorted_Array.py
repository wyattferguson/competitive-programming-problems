'''
Name: Create Sorted Array through Instructions
URL: https://bit.ly/3bZrYHW
Date: May 27, 2021

Test Cases:
Example 1:
Input: instructions = [1,5,6,2]
Output: 1
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 5 with cost min(1, 0) = 0, now nums = [1,5].
Insert 6 with cost min(2, 0) = 0, now nums = [1,5,6].
Insert 2 with cost min(1, 2) = 1, now nums = [1,2,5,6].
The total cost is 0 + 0 + 0 + 1 = 1.

Input: instructions = [1,2,3,6,5,4]
Output: 3
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 2 with cost min(1, 0) = 0, now nums = [1,2].
Insert 3 with cost min(2, 0) = 0, now nums = [1,2,3].
Insert 6 with cost min(3, 0) = 0, now nums = [1,2,3,6].
Insert 5 with cost min(3, 1) = 1, now nums = [1,2,3,5,6].
Insert 4 with cost min(3, 2) = 2, now nums = [1,2,3,4,5,6].
The total cost is 0 + 0 + 0 + 0 + 1 + 2 = 3.

Input: instructions = [1,3,3,3,2,4,2,1,2]
Output: 4
Explanation: Begin with nums = [].
Insert 1 with cost min(0, 0) = 0, now nums = [1].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3].
Insert 3 with cost min(1, 0) = 0, now nums = [1,3,3,3].
Insert 2 with cost min(1, 3) = 1, now nums = [1,2,3,3,3].
Insert 4 with cost min(5, 0) = 0, now nums = [1,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(1, 4) = 1, now nums = [1,2,2,3,3,3,4].
​​​​​​​Insert 1 with cost min(0, 6) = 0, now nums = [1,1,2,2,3,3,3,4].
​​​​​​​Insert 2 with cost min(2, 4) = 2, now nums = [1,1,2,2,2,3,3,3,4].
The total cost is 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4.

Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.subtree = 0
        self.left = None
        self.right = None


class Solution:
    def createSortedArray(self, instructions):
        def create_tree(nums, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            root = Node(nums[mid])
            root.left = create_tree(nums, start, mid-1)
            root.right = create_tree(nums, mid + 1, end)
            return root

        def insert(v, root):
            if v < root.val:
                insert(v, root.left)
            elif v > root.val:
                insert(v, root.right)
            else:
                root.count += 1
            root.subtree += 1

        cost = 0
        cln = list(set(instructions))
        cln.sort()
        root = create_tree(cln, 0, len(cln)-1)
        for v in instructions:
            insert(v, root)

            left_cost = right_cost = 0
            cur = root
            while v != cur.val:
                if v < cur.val:
                    right_cost += (cur.right.subtree if cur.right else 0) + cur.count
                    cur = cur.left
                elif v > cur.val:
                    left_cost += (cur.left.subtree if cur.left else 0) + cur.count
                    cur = cur.right

            left_cost += cur.left.subtree if cur.left else 0
            right_cost += cur.right.subtree if cur.right else 0
            cost += min(left_cost, right_cost)
            #print(v, left_cost, right_cost, cost)
        return cost % (10**9 + 7)


if __name__ == "__main__":
    #instructions = [1, 5, 6, 2]
    #instructions = [1, 2, 3, 6, 5, 4]
    #instructions = [1, 3, 3, 3, 2, 4, 2, 1, 2]

    instructions = [9, 8, 7, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7,
                    9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7, 9, 8, 7]
    solve = Solution()
    print(solve.createSortedArray(instructions))
