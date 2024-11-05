'''
Name: Merge Sorted Array
URL: https://bit.ly/3vyac6o
Date: May 29, 2021

Test Cases:
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
'''


class Solution:
    def merge(self, nums1, m: int, nums2, n: int):
        nums1[m:] = nums2[:n]
        nums1.sort()


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solve = Solution()
    solve.merge(nums1, m, nums2, n)
    print(nums1)
