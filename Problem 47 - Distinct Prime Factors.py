"""
Title: Project Euler - Problem 2: Even Fibonacci Numbers
Author: Mandeep Bhutani
Date: 12/26/2015

Problem:
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""


def factors(n):
    p = 2
    prime_factors = set()
    while n > 1:
        while n % p == 0:
            prime_factors.add(p)
            n /= p
        p += 1
        if p * p > n:
            if n > 1:
                prime_factors.add(n)
                break
    return prime_factors

i = (2 * 3 * 5 * 7)
while True:
    i += 1
    if len(factors(i)) == 4 and len(factors(i + 1)) == 4 and len(factors(i + 2)) == 4 and len(factors(i + 3)) == 4:
        print(i)
        break
