#ifndef TAX_CALCULATOR_H
#define TAX_CALCULATOR_H

#include "ad_calc.h"
#include <stdexcept>

class TaxCalculator : public Calculator {
public:
    // Function to calculate tax on an amount
    double calculateTax(double amount, double taxRate);
    
    // Function to apply discount on an amount
    double applyDiscount(double amount, double discountRate);
};

#endif // TAX_CALCULATOR_H
