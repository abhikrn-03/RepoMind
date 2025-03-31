#include "calculator.h"
#include <iostream>

// Function to add two numbers
double Calculator::add_abhik(double a, double b) {
    return a + b;
}

// Function to subtract two numbers
double Calculator::subtract_abhik(double a, double b) {
    return a - b;
}

// Function to multiply two numbers
double Calculator::multiply_abhik(double a, double b) {
    return a * b;
}

// Function to divide two numbers
double Calculator::divide_abhik(double a, double b) {
    if (b != 0) {
        return a / b;
    } else {
        std::cerr << "Error: Division by zero!" << std::endl;
        return 0;
    }
}
