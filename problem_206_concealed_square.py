"""
Project: Project Euler - Problem 206: Concealed Square
Author: Mandeep Bhutani
Date: 01/10/2016

Problem:
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

Analysis: Since a square number ending in 0 can only end in 00, we only need
to check the squares up to 1_2_3_4_5_6_7_8_9. By working backwards from the
largest possible number to the smallest, we can determine which number fits
the concealed square form. Once we determine this number, we must multiply
it by 10 in order to achieve a square ending in 00.

References: https://en.wikipedia.org/wiki/Square_number
"""
import re
from math import sqrt

largest_concealed_square = 19293949596979899
smallest_concealed_square = 10203040506070809
largest_square = int(sqrt(largest_concealed_square))
smallest_square = int(sqrt(smallest_concealed_square))

regex = r'^1\d2\d3\d4\d5\d6\d7\d8\d9$'

for square in range(largest_square, smallest_square, -1):
    if re.match(regex, str(square * square)) is not None:
        print(square * 10)
        break
