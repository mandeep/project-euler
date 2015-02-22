"""
Project: Project Euler - Problem 9: Special Pythagorean Triplet
Author: Mandeep Bhutani
Date: 2/3/2015

Problem: A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 + 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of a*b*c.

Description: A brute force method was used for this problem
with a runtime of 53.2 seconds.
"""
for a in range(1, 500):
    for b in range(1, 500):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print a*b*c
