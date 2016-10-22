"""
Title: Project Euler - Problem 25: 1000-Digit Fibonacci Number
Author: Mandeep Bhutani
Date: 3/9/2015

Problem: The Fibonacci sequence is defined by the recurrence relation:
Fn = Fn-1 + Fn-2 where F1 = 0 and F2= 1. The 12th term, F12 is the first term
to contain three digits. What is the first term in the Fibonacci sequence to
contain 1000 digits?
"""
term = 0
a, b = 0, 1

while len(str(a)) <= 1000:
    a, b = b, a + b
    term += 1
print(term)
