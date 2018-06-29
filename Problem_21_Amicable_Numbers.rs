/*
Title: Project Euler - Problem 21: Amicable Numbers
Author: Mandeep Bhutani
Date: 10/29/2015

Problem: Let d(n) be defined as the sum of proper divisors of n (numbers less
than n which divide evenly into n). If d(a) = b and d(b) = a, where a != b,
then a and b are an amicable pair and each of a and b are called amicable
numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20,
22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220. Evaluate the sum of all the amicable
numbers under 10,000.

References: http://en.wikipedia.org/wiki/Amicable_numbers
*/
fn main() {
    let mut amicable: Vec<i64> = Vec::new();
    for n in 1..10000 {
        let x = (1..n).filter(|&d| n % d == 0).fold(0, |a, b| a + b);
        let y = (1..n).filter(|&d| x % d == 0).fold(0, |c, d| c + d);
        if y == n  && (x - y) > 1 {
            amicable.push(x);
            amicable.push(y)}
    }
    println!("{:?}", amicable.iter().fold(0, |a, b| a + b));
}