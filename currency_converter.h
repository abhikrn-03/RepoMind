#ifndef CURRENCY_CONVERTER_H
#define CURRENCY_CONVERTER_H

#include "ad_calc.h"
#include <stdexcept>
#include <unordered_map>
#include <string>

class CurrencyConverter : public Calculator {
private:
    std::unordered_map<std::string, double> exchangeRates;
public:
    // Constructor to initialize exchange rates
    CurrencyConverter();
    
    // Function to convert currency from one type to another
    double convert(double amount, const std::string& from, const std::string& to);
};

#endif // CURRENCY_CONVERTER_H
