"""
Project: Project Euler - Problem 32: Pandigital Products
Author: Mandeep Bhutani
Date: 12/25/2015

Problem:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital. The product 7254 is unusual, as the 
identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

Analysis: 
From the problem, we are able to deduce that the product will be four numbers in length.
The only multiplicands and multipliers to produce this product are a single digit number multiplied by a
quadruple digit number and a double digit number multiplied by a triple digit number.
"""
result = []
for a in range(1, 10):
    for b in range(1000, 10000):
        formula_one = (str(a) + str(b) + str(a * b))
        if (str((int("".join(sorted(formula_one)))))) == "123456789" and len(str(a * b)) == 4:
            result.append(a * b)
for c in range(10, 100):
    for d in range(100, 1000):
        formula_two = (str(c) + str(d) + str(c * d))
        if (str((int("".join(sorted(formula_two)))))) == "123456789" and len(str(c * d)) == 4 and (c * d) not in result:
            result.append(c * d)
print((sum(result)))