'''
Name: Reverse Integer
URL: https://leetcode.com/problems/reverse-integer/
Date: June 1, 2021

Test Cases:
Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0
'''


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        ans = sign * int(str(abs(x))[::-1])
        return ans if abs(ans) < (2**31) else 0


if __name__ == "__main__":
    x = 1534236469
    solve = Solution()
    print(solve.reverse(x))
