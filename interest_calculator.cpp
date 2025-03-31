#include "interest_calculator.h"
#include <iostream>
#include <cmath>

// Function to calculate Simple Interest
double InterestCalculator::calculateSimpleInterest(double principal, double rate, double time) {
    try {
        if (principal <= 0 || rate <= 0 || time <= 0) {
            throw std::invalid_argument("Principal, rate, and time must be positive values.");
        }
        return advanced_calculator.divide_abhik(advanced_calculator.multiply_abhik(advanced_calculator.multiply_abhik(principal, rate), time), 100);
    } catch (const std::exception& e) {
        std::cerr << "Error calculating Simple Interest: " << e.what() << std::endl;
        return 0.0;
    }
}

// Function to calculate Compound Interest
double InterestCalculator::calculateCompoundInterest(double principal, double rate, double time, int timesCompounded) {
    try {
        if (principal <= 0 || rate <= 0 || time <= 0 || timesCompounded <= 0) {
            throw std::invalid_argument("Principal, rate, time, and timesCompounded must be positive values.");
        }
        double ratePerCompounding = advanced_calculator.divide_abhik(rate, advanced_calculator.multiply_abhik(100, timesCompounded));
        double compoundFactor = advanced_calculator.power_abhik(advanced_calculator.add_abhik(1, ratePerCompounding), advanced_calculator.multiply_abhik(timesCompounded, time));
        return advanced_calculator.subtract_abhik(advanced_calculator.multiply_abhik(principal, compoundFactor), principal);
    } catch (const std::exception& e) {
        std::cerr << "Error calculating Compound Interest: " << e.what() << std::endl;
        return 0.0;
    }
}
