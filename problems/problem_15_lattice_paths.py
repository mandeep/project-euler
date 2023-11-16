"""
Project: Project Euler - Problem 15: Lattice Paths
Author: Mandeep Bhutani
Date: 3/28/2015

Problem: Starting in the top left corner of a 2 x 2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the bottom right
corner. How many such routes are there through a 20 x 20 grid?

References: https://en.wikipedia.org/wiki/Pascal's_triangle

"""
from math import factorial


def find_lattice_paths(n):
    """Find the number of lattice paths given an n x n grid."""
    return factorial(2 * n) // (factorial(n) * factorial(n))

print(find_lattice_paths(20))
