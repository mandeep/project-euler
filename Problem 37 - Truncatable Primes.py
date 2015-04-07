"""
Project: Project Euler - Problem 37: Truncatable Primes
Author: Mandeep Bhutani
Date: 4/6/2015

Problem: The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain prime at
each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3. Find the sum of the only eleven primes that are both
truncatable from left to right and right to left. NOTE: 2, 3, 5, and 7 are not
considered to be truncatable primes.
"""
from math import sqrt


def is_prime(n):
    if n <= 1:
        return False
    for i in xrange(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    else:
        return True

x = 10
count, result = 0, 0
while count < 11:
    x += 1
    left = (is_prime(int(str(x)[j:])) for j in xrange(0, len(str(x))))
    right = (is_prime(int(str(x)[:k])) for k in xrange(1, len(str(x))))
    if all(left) == True and all(right) == True:
        result += x
        count += 1
print result
