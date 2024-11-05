'''
Name: ZigZag Conversion
Problem URL: https://leetcode.com/problems/zigzag-conversion/
Date Completed: June 4, 2021

Test Cases:
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"

'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        zigzag = [""] * numRows
        idx = 1
        dir = 1

        for ch in s:
            zigzag[idx-1] += ch
            if idx == numRows:
                dir = -1
            elif idx == 1:
                dir = 1

            idx += dir

        return "".join(zigzag)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3
    solve = Solution()
    print(solve.convert(s, numRows))
