"""
Project: Project Euler - Problem 43: Sub-string Divisibility
Author: Mandeep Bhutani
Date: 4/18/2015

Problem: A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it lexicographic
order. The lexicographic permutations of 0, 1 and 2 are:
012, 021, 102, 120, 201, 210. What is the millionth lexicographic permutation
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
from itertools import permutations

result = 0
primes = [2, 3, 5, 7, 11, 13, 17]

for x in permutations(str(1234567890)):
    total = []
    y = "".join(x)
    for i in xrange(1, 8):
        divisors = int(y[i] + y[i+1] + y[i+2])
        if divisors % primes[i-1] == 0:
            total.append(True)
    if all(total) == True and len(total) == 7:
        result += int("".join(x))
print result
