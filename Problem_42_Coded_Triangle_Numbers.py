"""
Project: Project Euler - Problem 42: Coded Triangle Numbers
Author: Mandeep Bhutani
Date: 03/29/2015

Problem: The nth term of the sequence of triangle numbers is given by,
fn = n * (n+1) / 2; so the first ten triangle numbers are:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = f(10). If the word
value is a triangle number then we shall call the word a triangle word. Using
words.txt, a 16K text file containing nearly two-thousand common English words,
how many are triangle words?

Analysis: If there were a 10 letter word consisting entirely of Zs, the
total of each character's alphabetical position would be 260. Because of the
small size of the value, just the first 25 triangular numbers are used in this
algorithm with the expectation that the value of each word in the given text
document doesn't exceed 260.
"""


def triangle_numbers(n):
    return [x * (x + 1) / 2 for x in range(1, n + 1)]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
values = dict(zip(letters, range(1, 27)))

result = []
with open("words.txt") as text:
    for data in text:
        data = data.split(",")
        for word in data:
            total = []
            for char in word:
                if char.isalpha():
                    total.append(values[char])
            result.append(sum(total))

count = 0
for number in result:
    if number in triangle_numbers(25):
        count += 1
print(count)
