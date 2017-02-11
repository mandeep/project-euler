/* 
Title: Project Euler - Problem 357: Prime Generating Integers
Author: Mandeep Bhutani
Date: 02/11/2017

Problem: Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
*/
extern crate num;
extern crate rayon;

use rayon::prelude::*;

use std::collections::HashSet;

fn is_prime(n: u64) -> bool {
    if n < 2 { return false; }
    let limit = (n as f64).sqrt() as u64;
    for i in 2..limit+1 { if n % i == 0 { return false; } }
    true
}

fn find_divisors(m: u64) -> HashSet<u64> {
    let limit = (m as f64).sqrt() as u64;
    let divisors = (1..limit+1).into_par_iter()
                               .filter(|&i| m % i == 0)
                               .collect();
    divisors
}

fn is_prime_generating(o: u64) -> bool {
    if !is_prime(o + 1) { return false; }
    let prime_generating = find_divisors(o).into_par_iter()
                                           .all(|d| is_prime(d + (o / d)));
    prime_generating
}

fn main() {
    let summation: u64 = (1..100000000u64).into_par_iter()
                                          .filter(|&k| is_prime_generating(k))
                                          .sum();
    println!("{:?}", summation);
}