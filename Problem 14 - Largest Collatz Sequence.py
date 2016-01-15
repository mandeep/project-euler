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


def collatz(x):
    result = [x]
    while x > 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        result.append(x)
    return result


def largest_collatz(y):
    total = []
    for x in range(1, y):
        total.append((int(len(collatz(x)))))
    largest = max(total)
    return (total.index(largest) + 1)
print(largest_collatz(1000001))
