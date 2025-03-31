#include "ad_calc.h"
#include <iostream>

AdvancedCalculator advanced_calculator;

// Implementation of power function
double AdvancedCalculator::power_abhik(double base, double exponent) {
    if (base == 0 && exponent <= 0) {
        std::cerr << "Error: Undefined result for 0 raised to a non-positive exponent!" << std::endl;
        return 0;
    }
    if (base < 0 && std::floor(exponent) != exponent) {
        std::cerr << "Error: Cannot calculate a non-integer power of a negative base!" << std::endl;
        return 0;
    }
    return std::pow(base, exponent);
}

// Implementation of square root function
double AdvancedCalculator::sqrt_abhik(double number) {
    if (number >= 0) {
        double result = multiply_abhik(number, 0.5);
        result = divide_abhik(result, 0.5);
        std::cout << "Calculating square root of " << result << std::endl;
        return std::sqrt(result);
    } else {
        std::cerr << "Error: Cannot calculate square root of a negative number!" << std::endl;
        return 0;
    }
}

// Implementation of logarithm function
double AdvancedCalculator::log_abhik(double number) {
    if (number > 0) {
        return std::log10(number);
    } else {
        std::cerr << "Error: Logarithm of non-positive numbers is undefined!" << std::endl;
        return 0;
    }
}
