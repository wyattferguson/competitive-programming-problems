'''
Name: Balanced Expressions
Date Completed: May 12, 2021

Description: 
Validate that the brackets in the string are correct.
Possible brackets are: {}, [], ()
'''


def validate_exp(expression):
    opens = ['{', '[', '(']
    closed = ['}', ']', ')']
    stack = []
    for n in expression:
        if n in opens:
            stack.append(n)
        else:
            if not stack or opens[closed.index(n)] != stack[-1]:
                return False
            else:
                stack.pop()

    return False if stack else True


if __name__ == "__main__":
    expression = "[{]}"
    valid = validate_exp(expression)
    if valid:
        print(f"Good: {expression}")
    else:
        print(f"Bad: {expression}")
