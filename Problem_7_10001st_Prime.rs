/*
Title: Project Euler - Problem 7: 10001st Prime
Author: Mandeep Bhutani
Date: 10/21/2016

Problem: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13. What is the 10,001st prime number?
*/
fn is_prime(n: u32) -> bool {
    if n < 2 { return false; }
    let limit: u32 = (n as f32).sqrt() as u32;
    for i in 2..limit+1 { if n % i == 0 { return false; } }
    true
}

fn main() {
    let number: Vec<u32> = (1..)
        .filter(|&x| is_prime(x))
        .take(10001)
        .collect();
    println!("{:?}", number.last());
}