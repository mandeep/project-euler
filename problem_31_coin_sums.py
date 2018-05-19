"""
Project: Project Euler - Problem 31: Coin Sums
Author: Mandeep Bhutani
Date: 12/25/2015

Problem:
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
result = 0
for one_pence in range(0, 200+1):
    for two_pence in range(0, 200+1 - one_pence, 2):
        for five_pence in range(0, 200+1 - one_pence - two_pence, 5):
            for ten_pence in range(0, 200+1 - one_pence - two_pence - five_pence, 10):
                for twenty_pence in range(0, 200+1 - one_pence - two_pence - five_pence - ten_pence, 20):
                    for fifty_pence in range(0, 200+1 - one_pence - two_pence - five_pence - ten_pence - twenty_pence, 50):
                        for one_hundred_pence in range(0, 200+1 - one_pence - two_pence - five_pence - ten_pence - twenty_pence - fifty_pence, 100):
                            for two_hundred_pence in range(0, 200+1 - one_pence - two_pence - five_pence - ten_pence - twenty_pence - fifty_pence - one_hundred_pence, 200):
                                if one_pence + two_pence + five_pence + ten_pence + twenty_pence + fifty_pence + one_hundred_pence + two_hundred_pence == 200:
                                    result += 1
print(result)
