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
    """Find the pythagorean triplet using Euclid's formula.

    Euclid's formula states that any pythagorean triplet (a, b, c)
    can be written as a = m^2 - n^2, b = 2mn, c = m^2 + n^2.
    Since a + b + c = 1000 we can substitute the variables in
    Euclid's formula for a, b, and c to obtain:
    m^2 - n^2 + 2mn + m^2 + n^2 = 1000. Simplifying we obtain:
    2m^2 + 2mn = 1000 and then m(m + n) = 500.
    """
    for n in range(1, 500):
        for m in range(n + 1, 500 - n):
            if m ** 2 + m * n == 500:
                return (m ** 2 - n ** 2) * (2 * m * n) * (m ** 2 + n ** 2)


print(pythagorean_triplet((1000)))
