'''
Name:Interleaving String
URL: https://bit.ly/3id0DWE
Date: June 2, 2021

Test Cases:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
'''


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1 + s2) != len(s3):
            return False

        a = b = 0
        for c in s3:
            if c == s1[a]:
            if s3[indx]:
                # print(s3[indx], s3)
                s3 = s3[:indx] + s3[indx+1:]
            else:
                return False

        return True


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    solve = Solution()
    print(solve.isInterleave(s1, s2, s3))
