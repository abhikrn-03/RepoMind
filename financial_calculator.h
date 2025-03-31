#ifndef FINANCIAL_CALCULATOR_H
#define FINANCIAL_CALCULATOR_H

#include "loan_calculator.h"
#include "interest_calculator.h"
#include "tax_calculator.h"
#include "currency_converter.h"

class FinancialCalculator : public Calculator {
public:
    // Function to compute loan EMI
    double computeEMI(double principal, double rate, int months);
    
    // Function to compute simple interest
    double computeSimpleInterest(double principal, double rate, double time);
    
    // Function to compute compound interest
    double computeCompoundInterest(double principal, double rate, double time, int timesCompounded);
    
    // Function to compute tax
    double computeTax(double amount, double taxRate);
    
    // Function to convert currency
    double convertCurrency(double amount, const std::string& from, const std::string& to);
};

#endif // FINANCIAL_CALCULATOR_H
