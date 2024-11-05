'''
Name: Check If Two String Arrays are Equivalent
URL: https://bit.ly/34nqYt1
Date: May 27, 2021

Test Cases:
Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
Example 2:

Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false
Example 3:

Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true
'''


class Solution:
    def arrayStringsAreEqual(self, word1, word2) -> bool:
        return True if ''.join(word1) == ''.join(word2) else False


if __name__ == "__main__":
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    solve = Solution()
    print(solve.arrayStringsAreEqual(word1, word2))
