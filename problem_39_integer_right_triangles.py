"""
Project: Project Euler - Problem 39: Integers Right Triangles
Author: Mandeep Bhutani
Date: 3/29/2015

Problem: If p is the perimeter of a right angle triangle with integral length
sides, {a, b, c}, there are exactly three solutions for p = 120:
{20, 48, 52}, {24, 45, 51}, and {30, 40, 50}.
For which value of p <= 1000, is the number of solutions maximised?
"""


def maximal_right_triangles(n):
    number_solutions = 3
    maximum_perimeter = 0

    for p in range(1, n+1):
        solutions = set()
        for a in range(1, p):
            for b in range(a, p - a):
                c = p - a - b
                if a ** 2 + b ** 2 == c ** 2:
                    solutions.add((a, b, c))
        if len(solutions) > number_solutions:
            number_solutions = len(solutions)
            maximum_perimeter = p

    return maximum_perimeter


print(maximal_right_triangles(1000))
