"""
Description:

You are given an array (which will have a length of at least 3, but could be very large)
containing integers. The array is either entirely comprised of odd integers or entirely
comprised of even integers except for a single integer N. Write a method that takes the
array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
"""

def find_outlier(integers):
    if integers[0] % 2 == integers[1] % 2:
        for char in integers:
            if char % 2 != integers[0] % 2:
                return char
    elif integers[0] % 2 == integers[2] % 2:
        return integers[1]
    else:
        return integers[0]