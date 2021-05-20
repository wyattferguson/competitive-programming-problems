"""
Name: Number letter counts
Problem URL: https://projecteuler.net/problem=17
Date Completed: May 15 2021 

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


SOLUTION:
This could be greatly cleaned up but I wanted to print all the actual word to number translations. If you removed that and just add the length to the totally it would clean up this alot.
"""

if __name__ == "__main__":
    numbers = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
        0: "Zero",
    }

    # start with the len of one thousand
    cnt = 11
    for n in range(1, 1000):
        pos = 0
        k = ""
        if n > 99:
            k += numbers[int(str(n)[pos])] + "hundred"
            pos += 1
            if str(n)[pos:] != "00":
                k += "and"
                if str(n)[pos] == "0":
                    pos += 1

        if int(str(n)[pos:]) > 19:
            k += numbers[int(str(n)[pos] + "0")]
            pos += 1
            if int(str(n)[pos]) > 0:
                k += numbers[int(str(n)[pos])]
            else:
                pos += 1

        elif int(str(n)[pos:]) > 9:
            k += numbers[int(str(n)[pos:])]
        elif int(str(n)[pos]) > 0:
            k += numbers[int(str(n)[pos])]

        cnt += len(k)
        print(k)

print(cnt)
