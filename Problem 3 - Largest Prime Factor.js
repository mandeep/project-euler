/*
Title: Project Euler - Problem 3: Largest Prime Factor
Author: Mandeep Bhutani
Date: 03/13/2016

Problem: The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
*/
var i = 2;
var n = 600851475143;

while (i * i < n) {
    if (n % i === 0) {
        n /= i;
    }
    else {
        i++;
    }
}
console.log(n);