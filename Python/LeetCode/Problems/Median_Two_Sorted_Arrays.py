'''
Name: Median of Two Sorted Arrays
Problem URL: https://leetcode.com/problems/median-of-two-sorted-arrays/
Date Completed: June 1, 2021

Test Cases:
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000

'''


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1 += nums2
        nums1.sort()
        m = len(nums1) - 1
        if m % 2:
            n = (nums1[m//2] + nums1[(m//2)+1]) / 2
        else:
            n = nums1[int(m/2)]
        return n


if __name__ == "__main__":
    nums1 = [1]
    nums2 = []

    solve = Solution()
    print(solve.findMedianSortedArrays(nums1, nums2))
