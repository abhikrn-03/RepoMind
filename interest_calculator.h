#ifndef INTEREST_CALCULATOR_H
#define INTEREST_CALCULATOR_H

#include "ad_calc.h"
#include <stdexcept>

class InterestCalculator : public Calculator {
public:
    // Function to calculate Simple Interest
    double calculateSimpleInterest(double principal, double rate, double time);
    
    // Function to calculate Compound Interest
    double calculateCompoundInterest(double principal, double rate, double time, int timesCompounded);
};

#endif // INTEREST_CALCULATOR_H
