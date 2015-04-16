"""
Title: Project Euler - Problem 19: Counting Sundays
Author: Mandeep Bhutani
Date: 4/15/2015

Problem: You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday. Thirty days has September, April, June and November. All the rest have
thirty-one, saving February alone, which has twenty-eight, rain or shine. And on leap years,
twenty-nine. A leap year occurs on any year evenly divisible by 4, but not on a century unless it
is divisible by 400. How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""
from datetime import date

number_of_sundays = 0

for year in xrange(1901, 2001):
    for month in xrange(1, 13):
        if date(year, month, 1).isoweekday() == 7:
            number_of_sundays += 1

print number_of_sundays
