/*
Project: Project Euler - Problem 6: Sum Square Difference
Author: Mandeep Bhutani
Date: 10/21/2016

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
fn sum_squares(n: i64) -> i64 {
    let mut summation: i64 = 0;
    for i in 1..n+1 {
        summation += i * i;
    }
    summation
}

fn square_sum(n: i64) -> i64 {
    let mut summation: i64 = 0;
    for i in 1..n+1 {
        summation += i;
    }
    summation * summation
}

fn main () {
    let difference = square_sum(100) - sum_squares(100);
    println!("{}", difference);
}