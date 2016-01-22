"""
Project: Project Euler - Problem 39: Integers Right Triangles
Author: Mandeep Bhutani
Date: 3/29/2015

Problem: If p is the perimeter of a right angle triangle with integral length
sides, {a, b, c}, there are exactly three solutions for p = 120:
{20, 48, 52}, {24, 45, 51}, and {30, 40, 50}.
For which value of p <= 1000, is the number of solutions maximised?
"""
result = []
for p in range(1, 1000+1):
    total = []
    for a in range(1, p):
        for b in range(1, p):
            c = p - a - b
            if a ** 2 + b ** 2 == c ** 2:
                if sorted((a, b, c)) not in total:
                    total.append(sorted((a, b, c)))
    if len(total) > 3:
        result.append((len(total), p))
print(max(result))
