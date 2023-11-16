"""
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 02/24/2015

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""


def sieve_of_eratosthenes(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


summation = sum(sieve_of_eratosthenes(2000000))
print(summation)
