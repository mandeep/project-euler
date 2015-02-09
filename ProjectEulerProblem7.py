"""
Title: Project Euler - Problem 7: 10001st Prime
Author: Mandeep Bhutani
Date: 2/9/2015

Problem: By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10001st prime number?
"""
# First a function is defined in order to return prime numbers
def is_prime(x):
    if x == 2:
        return True
    elif x < 2:
        return False
    elif x > 2:
        for n in range(2,x-1):
            if x % n == 0:
                return False
        else:
            return True

# This function searches a range of prime numbers and returns the prime number for term n.
def term(n):
    count = 0
    for i in range(2,500000):
        if is_prime(i) == True:
            count += 1
            if count == n:
                print i
term(10001)
