/*
Title: Project Euler - Problem 10: Summation of Primes
Author: Mandeep Bhutani
Date: 10/22/2016

Problem: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/
fn is_prime(n: i32) -> bool {
    if n < 2 { return false; }
    let temp = n as f64;
    let limit: i32 = temp.sqrt() as i32;
    for i in 2..limit+1 { if n % i == 0 { return false; } }
    true
}

fn sum_primes(limit: i32) -> i64 {
    let mut summation: i64 = 0;
    for number in 2..limit+1 {
        if is_prime(number) {
            let prime = number as i64;
            summation += prime; } }
    summation
}

fn main() {
    println!("{:?}", sum_primes(2000000));
}