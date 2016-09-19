/*
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 09/19/2016

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/
#include <iostream>
#include <math.h>

bool isPrime(int n) {
    if (n < 2) {
        return false;
    }
    for (int i = 2; i <= pow(n, 0.5); ++i) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    long long int sum = 0;
    for (int i = 2; i < 2000000; ++i) {
        if (isPrime(i)) {
            sum += i;
        }
    }
    std::cout << sum << std::endl;
}