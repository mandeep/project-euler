/*
Project: Project Euler - Problem 9: Special Pythagorean Triplet
Author: Mandeep Bhutani
Date: 10/21/2016

Problem: A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 + 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product of a*b*c.
*/
fn main() {
    'outer: for a in 1..1000 {
        'inner: for b in 1..1000-a {
            let c = 1000 - a - b;
            if a * a + b * b == c * c {
                println!("{}", a * b * c);
                break 'outer;
            }
        }
    }
}