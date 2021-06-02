
'''
Name: Longest Palindromic Substring
URL: https://leetcode.com/problems/longest-palindromic-substring/
Date: June 2,2021

Test Cases:
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_pal(s):
            return True if s == s[::-1] else False

        def dive(s, l, r):
            if l > r or r <= 0:
                return ""

            if is_pal(s[l:r]):
                return s[l:r]

            left = dive(s, l+1, r)
            right = dive(s, l, r-1)
            return left if len(left) > len(right) else right

        return dive(s, 0, len(s))


if __name__ == "__main__":
    s = "abbcccbbbcaaccbababcbcabca"
    solve = Solution()
    print(solve.longestPalindrome(s))
