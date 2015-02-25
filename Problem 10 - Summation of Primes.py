"""
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 2/24/2015

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

References: http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes;
https://docs.python.org/2/library/stdtypes.html
"""


def eratosthenes(n):
    total = set()  # Used to generate unique multiples
    result = []
    for p in range(2, n+1):  # The range extends to n+1 in order to include
        # n in the calculation
        if p not in total:
            result.append(p)  # Add all primes to result
            total.update(range(p*p, n+1, p))  # Enumerating multiples
            # by counting to n in increments of p
    return result

print sum(eratosthenes(2000000))
