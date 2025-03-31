#include "financial_calculator.h"
#include <iostream>
#include <stdexcept>

// Compute Loan EMI using LoanCalculator
double FinancialCalculator::computeEMI(double principal, double rate, int months) {
    try {
        LoanCalculator loanCalc;
        return loanCalc.calculateEMI(principal, rate, months);
    } catch (const std::exception& e) {
        std::cerr << "Error computing EMI: " << e.what() << std::endl;
        return 0.0;
    }
}

// Compute Simple Interest using InterestCalculator
double FinancialCalculator::computeSimpleInterest(double principal, double rate, double time) {
    try {
        InterestCalculator interestCalc;
        return interestCalc.calculateSimpleInterest(principal, rate, time);
    } catch (const std::exception& e) {
        std::cerr << "Error computing Simple Interest: " << e.what() << std::endl;
        return 0.0;
    }
}

// Compute Compound Interest using InterestCalculator
double FinancialCalculator::computeCompoundInterest(double principal, double rate, double time, int timesCompounded) {
    try {
        InterestCalculator interestCalc;
        return interestCalc.calculateCompoundInterest(principal, rate, time, timesCompounded);
    } catch (const std::exception& e) {
        std::cerr << "Error computing Compound Interest: " << e.what() << std::endl;
        return 0.0;
    }
}

// Compute Tax using TaxCalculator
double FinancialCalculator::computeTax(double amount, double taxRate) {
    try {
        TaxCalculator taxCalc;
        return taxCalc.calculateTax(amount, taxRate);
    } catch (const std::exception& e) {
        std::cerr << "Error computing Tax: " << e.what() << std::endl;
        return 0.0;
    }
}

// Convert Currency using CurrencyConverter
double FinancialCalculator::convertCurrency(double amount, const std::string& from, const std::string& to) {
    try {
        CurrencyConverter currencyConv;
        return currencyConv.convert(amount, from, to);
    } catch (const std::exception& e) {
        std::cerr << "Error converting currency: " << e.what() << std::endl;
        return 0.0;
    }
}
