/*
"""
Project: Project Euler - Problem 4: Largest Palindrome Product
Author: Mandeep Bhutani
Date: 10/26/2016

Problem: A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is: 9009 = 91 * 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""
*/
fn is_palindrome(number: u32) -> bool {
    let stringified = number.to_string();
    let digits: String = stringified.chars()
        .rev()
        .collect();
    stringified == digits
}

fn main() {
    let mut maximum: u32 = 0;
    for x in 100..1000 {
        for y in x..1000 {
            if is_palindrome(x * y) && x * y > maximum { maximum = x * y }
        }
    }
    println!("{:?}", maximum);
}
