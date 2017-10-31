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

fn pythagorean_triplet(n: i32) -> i32 {
    for a in 1..n {
        for b in a..n-a {
            let c = n - a - b;
            if a * a + b * b == c * c {
                return a * b * c;
            }
        }
    }
    return 0;
}


fn main() {
    println!("{:?}", pythagorean_triplet(1000));
}
