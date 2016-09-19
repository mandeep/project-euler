/*
Title: Project Euler - Problem 7: 10001st Prime
Author: Mandeep Bhutani
Date: 09/19/2016

Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13. What is the 10,001st prime number?
*/
#include <iostream>
#include <math.h>

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= pow(n, 0.5); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int number = 0;
    for (int count = 0; count < 10001;) {
        ++number;
        if (isPrime(number)) {
            count++;
        }
    }
    std::cout << number << std::endl;
}