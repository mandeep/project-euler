/*
Project: Project Euler - Problem 16: Power Digit Sum
Author: Mandeep Bhutani
Date: 09/19/2016

Problem:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?

Description: The shortest way to find the sum of digits in an integer
is to convert the integer into a string and then
add the digits of the string into a list.
Once in a list the digits need to be converted back
to an integer and then summed. With list
comprehension this can all be achieved in a single line.
*/
#include <iostream>
#include <math.h>
#include <string>

int main() {
    int sum = 0;
    std::string number = std::to_string(pow(2, 1000));
    for (int i = 0; i < number.length(); ++i) {
        int temp = number[i] - '0'; // Subtract '0' is a way of converting from char to int
        sum += temp;
    }
    std::cout << sum + 2 << std::endl; // Add 2 in order to account for pow's double precision
}