"""
Project: Project Euler - Problem 99: Largest Exponential
Author: Mandeep Bhutani
Date: 02/07/2016

Problem:
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.
However, confirming that 632382518061 > 519432525806 would be much more
difficult, as both numbers contain over three million digits.
Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file
containing one thousand lines with a base/exponent pair on each line, determine
which line number has the greatest numerical value.

References: https://en.wikipedia.org/wiki/List_of_logarithmic_identities
"""
from math import log

largest_exponential, max_line = 0, 0
with open('base_exp.txt', 'r') as f:
    for line_number, line in enumerate(f, 1):
        base, exponent = [int(x) for x in line.strip().split(',')]
        exponential = exponent * log(base)
        if exponential > largest_exponential:
            largest_exponential = exponential
            max_line = line_number
print(max_line)
