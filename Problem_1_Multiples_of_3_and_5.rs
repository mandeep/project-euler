/*
Project: Project Euler - Problem 1: Multiples of 3 and 5
Author: Mandeep Bhutani
Date: 10/20/2016

Problem:
If we list all the natural numbers below 10 that are multiples of
3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
*/


fn main() {
    let summation: u64 = (1..1000)
        .filter(|&x| x % 3 == 0 || x % 5 == 0)
        .sum();
    println!("{}", summation);
}