'''
Name: Valid Parentheses
Problem URL: https://bit.ly/3g31MO5
Date Completed: May 31, 2021

Test Cases:
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true

'''


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '(': ')', '[': ']'}
        stack = []
        for i in s:
            if i in brackets:
                stack.append(i)
            elif stack and brackets[stack[-1]] == i:
                stack.pop()
            else:
                return False

        return False if stack else True


if __name__ == "__main__":
    s = "){"

    solve = Solution()
    print(solve.isValid(s))
