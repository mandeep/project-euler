/*
Project: Project Euler - Problem 6: Sum Square Difference
Author: Mandeep Bhutani
Date: 09/19/2016

Problem:
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
*/
#include <iostream>
#include <math.h>
#include <stdio.h>

int main() {
    int sum_squares = 0, square_sum = 0;
    for (int i = 1; i<= 100; i++) {
        sum_squares += pow(i, 2);
        square_sum += i;
    }
    int result = pow(square_sum, 2) - sum_squares;
    printf("%d", result);
}