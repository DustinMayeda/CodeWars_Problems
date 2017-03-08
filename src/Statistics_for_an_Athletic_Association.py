"""
Description:

You are the "computer man" of a local Athletic Association (C.A.A.).
Many teams of runners come to compete. Each time you get a string of all race
results of every team who has run. For example here is a string showing the individual
results of a team of 5:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Each part of the string is of the form: h|m|s where h, m, s are positive or null
integer (represented as strings) with one or two digits. There are no traps in this
format.

To compare the results of the teams you are asked for giving three statistics;
range, average and median.

Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the
lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

Mean or Average : To calculate mean, add together all of the numbers in a set and then
divide the sum by the total count of numbers.

Median : In statistics, the median is the number separating the higher half of a data
sample from the lower half. The median of a finite list of numbers can be found by
arranging all the observations from lowest value to highest value and picking the
middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of
observations. If there is an even number of observations, then there is no single middle
value; the median is then defined to be the mean of the two middle values (the median of
{3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above,
the string result will be

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

of the form:

"Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"

where hh, mm, ss are integers (represented by strings) with each 2 digits.

Remarks:

if a result in seconds is ab.xy... it will be given truncated as ab.
if the given string is "" you will return ""
"""

import numpy as np
from math import floor

def median(lst):
    lst.sort()
    if len(lst) % 2 == 1:
        return lst[int((len(lst) - 1) / 2)]
    else:
        return (lst[int(len(lst) / 2)] + lst[int((len(lst) / 2) - 1)]) / 2

def parse(time):
    time = time.split("|")
    hours = int(time[0])
    minutes = int(time[1])
    if len(time[2]) == 3:
        time[2] = time[2].replace(",", "")
        seconds = int(time[2])
    else:
        seconds = int(time[2])
    return (hours, minutes, seconds)

def convert_sec(tup):
    return (tup[0] * 60 * 60) + (tup[1] * 60) + tup[2]

def convert_standard(sec):
    hours = floor(sec / (60 ** 2))
    minutes = floor((sec - hours * 60 ** 2) / 60)
    seconds = sec - (hours * 60 ** 2) - (minutes * 60)
    hours = str(int(hours))
    minutes = str(int(minutes))
    seconds = str(int(seconds))
    if len(hours) == 1:
        hours = '0' + hours
    if len(minutes) == 1:
        minutes = '0' + minutes
    if len(seconds) == 1:
        seconds = '0' + seconds
    return hours + '|' + minutes + '|' + seconds

def stat(strg):
    if len(strg) == 0:
        return ""
    strg = strg.split()
    result = []
    for char in strg:
        char = parse(char)
        result.append(convert_sec(char))
    result = sorted(result)
    result = np.array(result)
    Range = floor(result.max() - result.min())
    Range = convert_standard(Range)
    Average = floor(result.mean())
    Average = convert_standard(Average)
    Median = floor(median(result))
    Median = convert_standard(Median)
    return "Range: {} Average: {} Median: {}".format(Range, Average, Median)
