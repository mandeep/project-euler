"""
Project: Project Euler - Problem 12 - Highly Divisible Triangular Number
Author: Mandeep Bhutani
Date: 3/28/2015

Problem:The sequence of triangle numbers is generated by adding the natural
numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55,...
Let us list the factors of the first seven triangle numbers:
1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred
divisors?

Description: This is a brute force approach that tries every number starting
from 1 until a solution is reached.
"""
from math import sqrt


def find_divisors(n):
    result = []
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0:
            result.append(i)
            result.append(n / i)
    return result


def find_triangular(n):
    x = 1
    while True:
        number = int(x * (x + 1) / 2)
        x += 1
        if len(find_divisors(number)) > n:
            return number


print(find_triangular(500))
