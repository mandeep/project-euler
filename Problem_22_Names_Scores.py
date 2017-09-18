"""
Project: Project Euler - Problem 22: Names Scores
Author: Mandeep Bhutani
Date: 03/29/2015

Problem: Using names.txt, a 46K text file, containing over five-thousand first
names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score. For example, when the list is
sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9
+ 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938
x 53 = 49714. What is the total of all the name scores in the file?

"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = dict(zip(letters, range(1, 27)))

total = 0

with open("names.txt") as names_file:
    names = sorted(names_file.read().split(','))

for name in names:
    count = sum(key[char] for char in name if char.isalpha())
    total += count * (names.index(name) + 1)

print(total)
