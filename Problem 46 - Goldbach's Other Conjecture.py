"""
Title: Project Euler - Problem 46: Goldbach's Other Conjecture
Author: Mandeep Bhutani
Date: 12/26/2015

Problem:
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.
What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    else:
        return True

number = 33
primes = [x for x in range(2, 10000) if is_prime(x) == True]
squares = [2 * (y ** 2) for y in range(1, 100)]
total = [p + s for p in primes for s in squares]
while True:
    number += 2
    if number not in total and is_prime(number) == False:
        print(number)
        break
