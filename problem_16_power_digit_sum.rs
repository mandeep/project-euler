/*
Project: Project Euler - Problem 16: Power Digit Sum
Author: Mandeep Bhutani
Date: 10/25/2016

Problem: 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
*/
extern crate num;

use num::BigUint;
use num::Integer;
use num::ToPrimitive;
use num::pow;


fn main() {
    let mut number: BigUint = pow(BigUint::from(2 as u8), 1000);
    let mut digits: Vec<u32> = Vec::new();
    while number > BigUint::from(0 as u8) {
        let division = Integer::div_rem(&number, &BigUint::from(10 as u32));
        digits.push(ToPrimitive::to_u32(&division.1).unwrap());
        number = division.0;
    }
    let summation: u32 = digits.iter().sum();
    println!("{}", summation);
}