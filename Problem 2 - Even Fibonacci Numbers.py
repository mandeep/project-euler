"""
Title: Project Euler - Problem 2: Even Fibonacci Numbers
Author: Mandeep Bhutani
Date: 01/30/2015

Problem: Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will
be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum of the even-valued terms.
"""

a, b = 0, 1
result = 0
while a < 4000000:
    if a % 2 == 0:
        result += a
    a, b = b, a + b
print(result)
