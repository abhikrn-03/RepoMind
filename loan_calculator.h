#ifndef LOAN_CALCULATOR_H
#define LOAN_CALCULATOR_H

#include "ad_calc.h"
#include <stdexcept>

class LoanCalculator : public Calculator {
public:
    // Function to calculate EMI
    double calculateEMI(double principal, double rate, int months);
};

#endif // LOAN_CALCULATOR_H
