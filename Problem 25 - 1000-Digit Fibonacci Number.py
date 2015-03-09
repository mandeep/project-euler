"""
Title: Project Euler - Problem 25: 1000-Digit Fibonacci Number
Author: Mandeep Bhutani
Date: 3/9/2015

Problem: The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn-1 + Fn-2 where F1 = 0 and F2= 1. The 12th term, F12 is the first term
to contain three digits. What is the first term in the Fibonacci sequence to
contain 1000 digits?
"""


def fib(n):
    a, b = 0, 1
    term = 0
    while len(str(a)) < n:
        a, b = b, a+b
        term += 1
    return term
print fib(1000)
