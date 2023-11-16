"""
Project: Project Euler - Problem 28: Number Spiral Diagonals
Author: Mandeep Bhutani
Date: 12/24/2015

Problem:
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

Analysis: Using the sample spiral, we can deduce a formula for each of the corners as follows:

Bottom-Right: n ** 2 - 3n + 3
Bottom-Left: n ** 2 - 2n + 2
Top-Left: n ** 2 - n + 1
Top-Right: n ** 2

Adding all of these corners yields: 4 * (n ** 2) - (6 * n) + 6

To find the sum of the diagonals of the largest square, we use the formula to find the number in the corners
of each of the smaller squares.
"""


def sum_spiral_diagonals(n):
    traces = 0
    for entry in range(3, n+1, 2):
        traces += (4 * (entry ** 2) - (6 * entry) + 6)
    return traces


print(sum_spiral_diagonals(1001))
