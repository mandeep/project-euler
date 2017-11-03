fn main() {
    let mut i = 2;
    let mut number: u64 = 600851475143;
    while i * i < number {
        while number % i == 0 {
            number /= i;
        }
        i += 1;
    }
    println!("{}", number);
}
