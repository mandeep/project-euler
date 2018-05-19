"""
Title: Project Euler - Problem 26: Reciprocal Cycles
Author: Mandeep Bhutani
Date: 4/15/2015

Problem: A unit fraction contains 1 in the numerator. Where 0.1(6) means 0.166666...,
and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle. 
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
its decimal fraction part.

Analysis: By setting the precision of the decimal module to 300 we are able to find
the longest reciprocal cycle of a unit fraction between 1 and 1000. The cycle lengths
omit numbers with cycles greater than 3000 due to a precision rounding error, and -1
due to the find function's error exception.
"""
from decimal import getcontext, Decimal

getcontext().prec = 3000

total = [str(Decimal(1) / Decimal(x))[2:] for x in range(1, 1000)]
result = []
for number in total:
    cycle_length = (number * 2).find(number[:2000], 1, -1)
    if cycle_length < 3000 and cycle_length != -1:
        result.append((cycle_length, total.index(number) + 1))
print(max(result))
