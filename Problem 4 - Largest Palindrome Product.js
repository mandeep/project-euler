/*
Project: Project Euler - Problem 4: Largest Palindrome Product
Author: Mandeep Bhutani
Date: 03/13/2016

Problem: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
*/
result = 0;
for (var i = 100; i < 1000; i ++) {
    for (var j = 100; j < 1000; j++) {
        var product = (i * j);
        var reversed = product.toString().split("").reverse().join("");
        if (product == reversed && product > result) {
            result = reversed;
        }
    }
}
console.log(result);