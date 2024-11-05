'''
Name: Palindrome Number
Problem URL: https://leetcode.com/problems/palindrome-number/
Date Completed: June 4, 2021

Test Cases:
Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    x = -121
    solve = Solution()
    print(solve.isPalindrome(x))
