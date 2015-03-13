"""
Project: Project Euler - Problem 34: Digit Factorials
Author: Mandeep Bhutani
Date: 3/12/2015

Problem: 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of
their digits. Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Description: A brute force method was applied to this problem. 50,000 was
picked as a starting point and ended up being the correct range end point.
"""
from math import factorial

result = []
for x in xrange(1, 50000):
    total = []
    for y in str(x):
        total.append(factorial(int(y)))
    if sum(total) == x and sum(total) > 2:
        result.append(x)
print sum(result)
