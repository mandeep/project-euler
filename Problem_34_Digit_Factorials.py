"""
Project: Project Euler - Problem 34: Digit Factorials
Author: Mandeep Bhutani
Date: 03/12/2015

Problem: 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of
their digits. Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Analysis: Factorial(9) is used as the upper bound 
"""
from math import factorial

result = []
for number in range(1, factorial(9)):
    total = [factorial(int(digit)) for digit in str(number)]
    if sum(total) == number and sum(total) > 2:
        result.append(number)
print(sum(result))
