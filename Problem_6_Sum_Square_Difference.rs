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
fn sum_squares(n: u64) -> u64 {
    let sum: u64 = (1..n+1)
        .fold(0, |sum, x| sum + (x * x));
    sum
}

fn square_sum(n: u64) -> u64 {
    let sum: u64 = (1..n+1).fold(0, |sum, x| sum + x);
    sum * sum
}

fn main () {
    let difference = square_sum(100) - sum_squares(100);
    println!("{}", difference);
}