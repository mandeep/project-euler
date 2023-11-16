"""
Project: Project Euler - Problem 55: Lychrel Numbers
Author: Mandeep Bhutani
Date: 4/18/2015

Problem: If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example, 349 + 943 = 1292,
1292 + 2921 = 4213, 4213 + 3124 = 7337. That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume
that a number is Lychrel until proven otherwise. In addition you are given that for every
number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or,
(ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
How many Lychrel numbers are there below ten-thousand?
"""
result = 0
for x in range(1, 10000):
    lychrel = int(str(x)[::-1]) + x
    count = 0
    while str(lychrel) != str(lychrel)[::-1]:
        lychrel += int(str(lychrel)[::-1])
        count += 1
        if count > 50:
            result += 1
            break
print(result)
