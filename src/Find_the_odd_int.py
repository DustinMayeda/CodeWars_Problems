"""
Description:

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

from collections import Counter

def find_it(seq):
    dict = Counter(seq)
    for integer in dict:
        if dict[integer] % 2 == 1:
            return integer
