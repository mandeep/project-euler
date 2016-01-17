"""
Project: Project Euler - Problem 48: Self Powers
Author: Mandeep Bhutani
Date: 03/29/2015

Problem: The series 1^1 + 2^2 + 3^3 ... + 10^10 = 10405071317. Find the last
ten digits of the series 1^1 + 2^2 + 3^3 ... + 1000^1000.
"""

result = sum((x ** x for x in range(1, 1000+1)))
print(str(result)[-10:])
