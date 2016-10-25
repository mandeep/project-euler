/*
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 10/22/2016

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/
fn is_prime(n: u64) -> bool {
    if n < 2 { return false; }
    let temp = n as f64;
    let limit = temp.sqrt() as u64;
    for i in 2..limit+1 { if n % i == 0 { return false; } }
    true
}

fn main() {
    let sum: u64 = (1..2000000).filter(|&x| is_prime(x)).sum();
    println!("{:?}", sum);
}