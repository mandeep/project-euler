"""
Project: Project Euler - Problem 17: Number Letter Counts
Author: Mandeep Bhutani
Date: 4/7/2015

Problem: If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the
numbers from 1 to 1000 (one thousand) inclusive were written out in words, how
many letters would be used?

Description: For every value of x, the value is searched for in the elements
dictionary. If the value is not defined, subtraction takes places until the
value is determined. For example, 102 is added as one hundred then as two to
define "one hundred two".
"""
elements = ((1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five"),
            (6, "six"), (7, "seven"), (8, "eight"), (9, "nine"), (10, "ten"),
            (11, "eleven"), (12, "twelve"), (13, "thirteen"), (14, "fourteen"),
            (15, "fifteen"), (16, "sixteen"), (17, "seventeen"),
            (18, "eighteen"), (19, "nineteen"), (20, "twenty"), (30, "thirty"),
            (40, "forty"), (50, "fifty"), (60, "sixty"), (70, "seventy"),
            (80, "eighty"), (90, "ninety"), (100, "one hundred"),
            (200, "two hundred"), (300, "three hundred"), (400, "four hundred"),
            (500, "five hundred"), (600, "six hundred"), (700, "seven hundred"),
            (800, "eight hundred"), (900, "nine hundred"), (1000, "one thousand"))

combination = ""
for i in range(1, 1001):
    for number, word in elements[::-1]:
        while i >= number:
            combination += word
            i -= number

combination = combination.replace(" ", "")

result = len(combination)

# Because the problem uses British English, the word and needs to be added.
# One hundred sixty two in American English, a.k.a., best English, needs to
# be one hundred and sixty two.
for british in range(100, 1000):
    result += 3

# There are nine values between one hundred and one thousand that don't use
# the word "and". They are one hundred, two hundred, three hundred,...
print(result - (9 * 3))
