'''
Name: Container With Most Water
Problem URL: https://leetcode.com/problems/container-with-most-water/
Date Completed: June 6, 2021

Test Cases:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Input: height = [1,1]
Output: 1

Input: height = [4,3,2,1,4]
Output: 16

Input: height = [1,2,1]
Output: 2
'''


class Solution:
    def maxArea(self, height) -> int:
        l = result = 0
        r = len(height) - 1
        while l < r:
            d = (r - l)
            if height[l] < height[r]:
                result = max(result, d*height[l])
                l += 1
            else:
                result = max(result, d*height[r])
                r -= 1
        return result


if __name__ == "__main__":
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solve = Solution()
    print(solve.maxArea(height))
