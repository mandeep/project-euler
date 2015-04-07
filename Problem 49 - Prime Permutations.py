"""
Project: Project Euler - Problem 49: Prime Permutations
Author: Mandeep Bhutani
Date: 4/7/2015

Problem: The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this
sequence?
"""
from math import sqrt


def is_prime(n):
    """Determine whether or not n is a prime number."""
    if n <= 1:
        return False
    for i in xrange(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True

# Generate a list of primes from 1,000 to 10,000 exclusive
primes = [int(j) for j in xrange(1000, 10000) if is_prime(j) == True]

# Look for primes in the primes list that are permutations of each other. By
# defining c = (b - a) + b we are able to check for equal distant numbers.
for a in primes:
    for b in primes:
        c = (b - a) + b
        if c > b > a and set(str(a)) == set(str(b)) == set(str(c)) \
                and c in primes:
            print "{0}{1}{2}" .format(a, b, c)
