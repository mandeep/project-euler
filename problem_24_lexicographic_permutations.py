"""
Project: Project Euler - Problem 24: Lexicographic Permutations
Author: Mandeep Bhutani
Date: 04/4/2015

Problem: A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it lexicographic
order. The lexicographic permutations of 0, 1 and 2 are:
012, 021, 102, 120, 201, 210. What is the millionth lexicographic permutation
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
from itertools import permutations


def nth_lexicographic_permutation(n):
    count = 0
    for number in permutations("0123456789"):
        count += 1
        if count == n:
            return "".join(number)

print(nth_lexicographic_permutation(1000000))
