"""
Title: Project Euler - Problem 8: Largest Product in a Series
Date: 3/15/2015

Problem: The four adjacent digits in the 1000-digit number that have the
greatest product are 9 x 9 x 8 x 9 = 5832.
Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""
number = []
count, total = 0, 0

with open('problem8number.txt') as text:
    for line in text:
        for char in line:
            if char.isdigit() == True:
                number.append(int(char))

while count < len(number):
    for x in range(0, len(number) - 12):
        count += 1
        product = number[x] * number[x + 1] * number[x + 2] * number[x + 3] * \
            number[x + 4] * number[x + 5] * number[x + 6] * number[x + 7] * \
            number[x + 8] * number[x + 9] * number[x + 10] * number[x + 11] * \
            number[x + 12]
        if product > total:
            total = product

print total
