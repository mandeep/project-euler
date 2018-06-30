"""
Project: Project Euler - Problem 50: Consecutive Prime Sum
Author: Mandeep Bhutani
Date: 04/10/2015

Problem: The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below
one-hundred. The longest sum of consecutive primes below one-thousand that
adds to a prime, contains 21 terms, and is equal to 953. Which prime, below
one-million, can be written as the sum of the most consecutive primes?
"""
from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True

primes = [x for x in range(7, 1000000) if is_prime(x)]
total, result = 0, 0
for number in primes:
    total = max(total, total + number)
    if total < 1000000:
        result = max(total, result)
print(result)
