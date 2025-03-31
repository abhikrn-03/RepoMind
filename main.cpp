#include "calculator.h"
#include "ad_calc.h"
#include "loan_calculator.h"
#include "interest_calculator.h"
#include "tax_calculator.h"
#include "currency_converter.h"
#include <iostream>

int main() {
    Calculator calc;
    AdvancedCalculator advCalc;
    LoanCalculator loanCalc;
    InterestCalculator interestCalc;
    TaxCalculator taxCalc;
    CurrencyConverter currencyConv;
    
    // Demonstrate basic arithmetic
    std::cout << "Addition: " << calc.add_abhik(10, 5) << std::endl;
    std::cout << "Multiplication: " << calc.multiply_abhik(10, 5) << std::endl;

    // Demonstrate advanced calculations
    std::cout << "Power: " << advCalc.power_abhik(2, 3) << std::endl;
    std::cout << "Square Root: " << advCalc.sqrt_abhik(25) << std::endl;

    // Loan EMI Calculation
    double emi = loanCalc.calculateEMI(10000, 10, 12);
    std::cout << "EMI: " << emi << std::endl;

    // Interest Calculation
    double simpleInterest = interestCalc.calculateSimpleInterest(5000, 5, 2);
    double compoundInterest = interestCalc.calculateCompoundInterest(5000, 5, 2, 4);
    std::cout << "Simple Interest: " << simpleInterest << std::endl;
    std::cout << "Compound Interest: " << compoundInterest << std::endl;

    // Tax and Discount Calculation
    double tax = taxCalc.calculateTax(1000, 18);
    double discountedPrice = taxCalc.applyDiscount(1000, 10);
    std::cout << "Tax: " << tax << std::endl;
    std::cout << "Discounted Price: " << discountedPrice << std::endl;

    // Currency Conversion
    double convertedAmount = currencyConv.convert(100, "USD", "INR");
    std::cout << "Converted Amount (USD to INR): " << convertedAmount << std::endl;

    return 0;
}
