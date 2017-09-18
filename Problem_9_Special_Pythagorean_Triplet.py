"""
Project: Project Euler - Problem 9: Special Pythagorean Triplet
Author: Mandeep Bhutani
Date: 02/03/2015

Problem: A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 + 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of a*b*c.
"""


def pythagorean_triplet(p):
    for a in range(1, p+1):
        for b in range(a, p+1 - a):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c


print(pythagorean_triplet((1000)))
