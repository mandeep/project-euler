/*
Project: Project Euler - Problem 1: Multiples of 3 and 5
Author: Mandeep Bhutani
Date: 03/13/2015

Problem:
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/

function sumAll(n) {
    var result = 0;
    for (var i = 0; i < 1000; i++) {
        if (i % 3 == 0 || i % 5 == 0) {
            result += i;
        }
    }
    return result;
}
console.log(sumAll(1000));