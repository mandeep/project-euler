"""
Project: Project Euler - Problem 53: Combinatoric Selections
Author: Mandeep Bhutani
Date: 4/18/2015

Problem: There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345. In combinatorics, we use the notation, 5C3 = 10.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066. How many, not
necessarily distinct, values of nCr for 1 <= n <= 100 are greater than one million?
"""
from math import factorial

count = 0
for n in range(1, 100+1):
    for r in range(1, n+1):
        nCr = factorial(n) / (factorial(r) * factorial((n - r)))
        if nCr > 1000000:
            count += 1
print(count)
