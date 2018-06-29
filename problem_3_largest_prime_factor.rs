/*
Author: Mandeep Bhutani
Date: 10/22/2016

Project Euler Problem 3 - Largest Prime Factor:
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
*/


fn largest_prime_factor(mut number: u64) -> u64 {
    let mut i = 2;

    while i * i < number {
        while number % i == 0 {
            number /= i;
        }
        i += 1;
    }

    number
}
fn main() {
    println!("{}", largest_prime_factor(600851475143));
}
