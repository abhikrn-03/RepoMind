#ifndef ADVANCEDCALCULATOR_H
#define ADVANCEDCALCULATOR_H

#include "calculator.h"
#include <cmath>

class AdvancedCalculator : public Calculator {
public:
    // Function to calculate the power of a number
    double power_abhik(double base, double exponent);

    // Function to calculate the square root of a number
    double sqrt_abhik(double number);

    // Function to calculate the logarithm (base 10) of a number
    double log_abhik(double number);
};

extern AdvancedCalculator advanced_calculator;

#endif // ADVANCEDCALCULATOR_H
