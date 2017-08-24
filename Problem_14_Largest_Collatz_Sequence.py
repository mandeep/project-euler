"""
Title: Project Euler - Problem 14: Largest Collatz Sequence
Author: Mandeep Bhutani
Date: 2/24/2015

Problem: The following iterative sequence is defined for the set of positive
integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""
import numba


@numba.jit
def collatz(number):
    sequence = []
    while number > 1:
        sequence.append(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
    return sequence


@numba.jit
def largest_collatz(limit):
    total, largest_sequence = 0, 0
    for number in range(1, limit):
        if len(collatz(number)) > total:
            total = len(collatz(number))
            largest_sequence = number
    return largest_sequence


print(largest_collatz(1000001))
