"""
Project: Project Euler - Problem 80: Square Root Digital Expansion
Author: Mandeep Bhutani
Date: 01/11/2016

Problem:
It is well known that if the square root of a natural number is not an integer, then it is irrational.
The decimal expansion of such square roots is infinite without any repeating pattern at all.
The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal
digits is 475. For the first one hundred natural numbers, find the total of the digital sums of the first
one hundred decimal digits for all the irrational square roots.

Analysis: The problem seems easy on first view, however there a few tricks embedded within.
First, we need to set a precision greater than 100 in order to eliminate rounding issues.
Second, both the integer part and the fractional part need to be included in the digit sum.
Lastly, we need to remove the integer part of all rational numbers less than 10
since they are perfect squares.
"""
from decimal import Decimal, getcontext
from math import sqrt

getcontext().prec = 102

perfect_squares = [x for x in range(1, 10)]
digit_sum = -sum(perfect_squares)

for number in range(1, 100):
    fractional_part = str(Decimal(number).sqrt())[2:101]
    integer_part = str(sqrt(number))[:1]
    digit_sum += sum([int(x) for x in fractional_part]) + int(integer_part)

print(digit_sum)
