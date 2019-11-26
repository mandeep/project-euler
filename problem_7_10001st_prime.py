"""
Title: Project Euler - Problem 7: 10001st Prime
Author: Mandeep Bhutani
Date: 03/03/2015

Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13. What is the 10,001st prime number?
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    elif n % 2 == 0:
        return n == 2
    elif n % 3 == 0:
        return n == 3
    for i in range(5, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def find_prime(limit):
    count = 0
    prime = 1
    while count < limit:
        prime += 1
        if is_prime(prime):
            count += 1
    return prime

print(find_prime(10001))
