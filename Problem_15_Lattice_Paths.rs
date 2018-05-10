/*
Project: Project Euler - Problem 15: Lattice Paths
Author: Mandeep Bhutani
Date: 10/25/2016

Problem: Starting in the top left corner of a 2 x 2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the bottom right
corner. How many such routes are there through a 20 x 20 grid?

References: https://en.wikipedia.org/wiki/Pascal's_triangle
*/
extern crate num;

use num::BigUint;
use num::traits::{One};


fn factorial(n: usize) -> BigUint {
    (1..n+1).fold(One::one(), |sum, x| sum * BigUint::from(x))
}


fn main() {
    let paths: BigUint = factorial(40) / (factorial(20) * factorial(20));
    println!("{}", paths);
}
