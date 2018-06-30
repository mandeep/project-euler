"""
Title: Project Euler - Problem 102: Triangle Containment
Author: Mandeep Bhutani
Date: 10/27/2016

Problem: Three distinct points are plotted at random on a Cartesian plane,
for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:
A(-340,495), B(-153,-910), C(835,-947)
X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin,
whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file
containing the co-ordinates of one thousand "random" triangles, find the number
of triangles for which the interior contains the origin.
"""


def cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
    """Convert cartesian coordinates to barycentric coordinates and return all > 0.

    Reference: https://en.wikipedia.org/wiki/Barycentric_coordinate_system_(mathematics)
    """
    alpha = (((y2 - y3) * (0 - x3) + (x3 - x2) * (0 - y3)) /
             ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    beta = (((y3 - y1) * (0 - x3) + (x1 - x3) * (0 - y3)) /
            ((y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)))
    gamma = 1 - alpha - beta

    return alpha > 0 and beta > 0 and gamma > 0

count = 0
with open('p102_triangles.txt') as text:
    for triangle in text.read().split():
        x1, y1, x2, y2, x3, y3 = [int(coord) for coord in triangle.split(',')]
        if cartesian_to_barycentric(x1, y1, x2, y2, x3, y3):
            count += 1
print(count)
