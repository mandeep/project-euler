fn is_prime(n: u64) -> bool {
    if n < 2 { return false; }
    let limit: u64 = (n as f64).sqrt() as u64;
    for i in 2..limit+1 { if n % i == 0 { return false; } }
    true
}

fn main() {
    let number: u64 = 600851475143;
    let limit = (number as f64).sqrt() as u64;
    let factors = (2..limit+1)
        .filter(|&i| number % i == 0);
    let prime_factors: Vec<u64> = factors
        .filter(|&j| is_prime(j))
        .collect();
    println!("{:?}", prime_factors.last().unwrap());
}