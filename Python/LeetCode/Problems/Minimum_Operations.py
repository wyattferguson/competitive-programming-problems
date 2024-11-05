'''
Name: Minimum Operations to Reduce X to Zero
URL: https://bit.ly/3yR2q9W
Date: May 30, 2021

Test Cases:
Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.
Example 2:

Input: nums = [5,6,7,8,9], x = 4
Output: -1
Example 3:

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
 
'''


class Solution:
    def minOperations(self, nums, x, ops=0) -> int:
        if x == 0:
            return ops

        if x < 0 or not nums:
            return -1

        left = self.minOperations(nums[1:], (x - nums[0]), ops+1)
        right = self.minOperations(nums[:-1], (x - nums[-1]), ops+1)

        return min(left, right) if left > 0 and right > 0 else max(left, right)


if __name__ == "__main__":
    nums = [5, 6, 7, 8, 9]
    x = 4
    solve = Solution()
    print(solve.minOperations(nums, x, 0))
