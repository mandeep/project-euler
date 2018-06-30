"""
Project: Project Euler - Problem 67: Maxiumum Path Sum 2
Author: Mandeep Bhutani
Date: 4/14/2015

Problem: By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.
   3
  7 4
 2 4 6
8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a 
triangle with one-hundred rows.

Description: By transposing the triangle from largest row on top to smallest row on the
bottom, we can iterate through each number allowing us to add the max of two numbers to
a number adjacent to it in the row that follows. The maximums continually add until the
max path sum is found. 
"""
with open('triangle.txt') as triangle:
    triangle = triangle.readlines()
    triangle = [[int(x) for x in row.split()] for row in triangle]
    for row in xrange(len(triangle)-1, 0, -1):
        for column in xrange(0, row):
            triangle[row - 1][column] += max(triangle[row][column], triangle[row][column + 1])
    print triangle[row - 1][column]
