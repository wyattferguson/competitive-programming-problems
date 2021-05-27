'''
Name: Read Phone Number
URL: https://bit.ly/2Ry0HFP
Date: May 23, 2021

Test Cases:
3
15012233444 3-4-4
15012233444 3-3-5
12223 2-3

Output:
Case #1: one five zero one double two three three triple four
Case #2: one five zero one double two double three triple four
Case #3: one two double two three

notes:
- if more then 10 numbers consequtively match just print the numbers
- format will always add to number length
'''


def solve(number, format):
    nums = ['zero', 'one', 'two', 'three', 'four',
            'five', 'six', 'seven', 'eight', 'nine']
    sets = ['double', 'tripple', 'quadruple',
            'quintuple', 'sextuple', 'septuple', 'octuple', 'nonuple', 'decuple']

    phone = []
    a = 0
    for x in format:
        zone = number[a:a+int(x)]
        for z in zone:
            phone.append(nums[int(z)])
        a += int(x)

    return ' '.join(phone)


if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        number, form = map(str, input().split())
        result = solve(number, form.split('-'))
        print(f"Case #{case}: {result}")
