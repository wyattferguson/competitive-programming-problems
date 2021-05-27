'''
Name: Longest Substring Without Repeating Characters
URL: https://bit.ly/3vuaCKX
Date: May 27, 2021

Test Cases:
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0

s = "dvdf"
output: 3
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 1 if s else 0
        hld = []
        for i in range(len(s)):
            if s[i] in hld:
                max_sub = max(len(hld), max_sub)
                snip = hld.index(s[i]) + 1
                hld = hld[snip:]
            hld.append(s[i])

        return max(len(hld), max_sub)


if __name__ == "__main__":
    s = "pwwkew"
    solve = Solution()
    print(solve.lengthOfLongestSubstring(s))
