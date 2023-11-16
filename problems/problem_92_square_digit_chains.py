"""
Project: Project Euler - Problem 92: Square Digit Chains
Author: Mandeep Bhutani
Date: 4/18/2015

Problem: A number chain is created by continuously adding the square of the digits in a number to form
a new number until it has been seen before. For example, 44 > 32 > 13 > 10 > 1 > 1, 
85 > 89 > 145 > 42 > 20 > 4 > 16 > 37 > 58 > 89. Therefore any chain that arrives at 1 or 89 will become
stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at
1 or 89. How many starting numbers below ten million will arrive at 89?
"""

result = 0
for y in xrange(1, 10000000):
    i = y
    count = 0
    while count != 2:
        i = sum((int(x) ** 2 for x in str(i)))
        if i == 89:
            count += 1
            result += 1
        elif i == 1:
            break
print result / 2
