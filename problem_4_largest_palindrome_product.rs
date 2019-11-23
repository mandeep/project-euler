/*
"""
Author: Mandeep Bhutani
Date: 10/26/2016

Project Euler Problem 4 - Largest Palindrome Product:
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""
*/
fn is_palindrome(mut number: u32) -> bool {
    let length = (number as f32).log10().floor() as u32 + 1;
    let mut exponent = 10_u32.pow(length - 1);

    while number > 0 {
        if number / exponent != number % 10 {
            return false;
        }
        number %= exponent;
        number /= 10;
        exponent /= 100;
    }

    return true;
}

fn main() {
    let mut maximum: u32 = 0;
    for x in 100..1000 {
        for y in x..1000 {
            if is_palindrome(x * y) {
                maximum = maximum.max(x * y);
            }
        }
    }
    println!("{:?}", maximum);
}
