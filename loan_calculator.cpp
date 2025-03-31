#include "loan_calculator.h"
#include <iostream>

// Function to calculate EMI
double LoanCalculator::calculateEMI(double principal, double rate, int months) {
    try {
        if (principal <= 0 || rate <= 0 || months <= 0) {
            throw std::invalid_argument("Principal, rate, and months must be positive values.");
        }
        
        double monthlyRate = advanced_calculator.divide_abhik(rate, advanced_calculator.multiply_abhik(12, 100)); // Convert annual rate to monthly percentage
        double powerFactor = advanced_calculator.power_abhik(advanced_calculator.add_abhik(1, monthlyRate), months);
        double emi = advanced_calculator.divide_abhik(advanced_calculator.multiply_abhik(advanced_calculator.multiply_abhik(principal, monthlyRate), powerFactor), advanced_calculator.subtract_abhik(powerFactor, 1));
        
        return emi;
    } catch (const std::exception& e) {
        std::cerr << "Error calculating EMI: " << e.what() << std::endl;
        return 0.0;
    }
}