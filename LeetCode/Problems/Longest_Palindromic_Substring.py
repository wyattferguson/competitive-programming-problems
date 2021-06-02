
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

Example 5:
s = "abbcccbbbcaaccbababcbcabca"
output: bbcccbb
Runtime of the program is 0.0010001659393310547

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        N = len(s) - 1
        limit = 1
        # Start with window at max size of the string
        for l in range(N):
            for r in range(N, l, -1):
                # if the window gets smaller then size of the current max palindrome move on
                if (r-l) < limit:
                    break

                # Check that the ends equal before doing more complicated checks.
                if s[l] == s[r]:
                    cur = s[l:r+1]
                    # check if palindrome and its the longest we've seen
                    if cur == cur[::-1] and len(cur) > limit:
                        result = cur
                        limit = len(result)

        return result


if __name__ == "__main__":
    s = "abbcccbbbcaaccbababcbcabca"
    solve = Solution()
    print(solve.longestPalindrome(s))
