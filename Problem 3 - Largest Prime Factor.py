"""
Title: Project Euler - Problem 3: Largest Prime Factor
Author: Mandeep Bhutani
Date: 02/01/2015

Problem: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


i = 2
n = 600851475143
while i * i < n:
    while n % i == 0:
        n //= i
    i += 1
print(n)
