#include "tax_calculator.h"
#include <iostream>

// Function to calculate tax on an amount
double TaxCalculator::calculateTax(double amount, double taxRate) {
    try {
        if (amount < 0 || taxRate < 0) {
            throw std::invalid_argument("Amount and tax rate must be non-negative values.");
        }
        return advanced_calculator.divide_abhik(advanced_calculator.multiply_abhik(amount, taxRate), 100);
    } catch (const std::exception& e) {
        std::cerr << "Error calculating Tax: " << e.what() << std::endl;
        return 0.0;
    }
}

// Function to apply discount on an amount
double TaxCalculator::applyDiscount(double amount, double discountRate) {
    try {
        if (amount < 0 || discountRate < 0 || discountRate > 100) {
            throw std::invalid_argument("Amount must be non-negative and discount rate should be between 0 and 100.");
        }
        return advanced_calculator.subtract_abhik(amount, advanced_calculator.divide_abhik(advanced_calculator.multiply_abhik(amount, discountRate), 100));
    } catch (const std::exception& e) {
        std::cerr << "Error applying Discount: " << e.what() << std::endl;
        return 0.0;
    }
}