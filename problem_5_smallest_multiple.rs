/*
Title: Project Euler - Problem 5: Smallest Multiple
Author: Mandeep Bhutani
Date: 10/23/2016

Problem: 2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
*/
extern crate num;

use num::integer::lcm;

fn main() {
    let multiple = (1..20+1).fold(1, |a, b| lcm(a, b));
    println!("{}", multiple);
}
