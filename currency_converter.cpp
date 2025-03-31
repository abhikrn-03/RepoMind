#include "currency_converter.h"
#include <iostream>

// Constructor to initialize exchange rates
CurrencyConverter::CurrencyConverter() {
    exchangeRates["USD"] = 1.0; // Base currency
    exchangeRates["EUR"] = 0.85;
    exchangeRates["GBP"] = 0.75;
    exchangeRates["INR"] = 74.50;
    exchangeRates["JPY"] = 110.0;
}

// Function to convert currency from one type to another
double CurrencyConverter::convert(double amount, const std::string& from, const std::string& to) {
    try {
        if (amount < 0) {
            throw std::invalid_argument("Amount must be non-negative.");
        }
        if (exchangeRates.find(from) == exchangeRates.end() || exchangeRates.find(to) == exchangeRates.end()) {
            throw std::invalid_argument("Invalid currency codes.");
        }
        double inUSD = advanced_calculator.divide_abhik(amount, exchangeRates[from]);
        return advanced_calculator.multiply_abhik(inUSD, exchangeRates[to]);
    } catch (const std::exception& e) {
        std::cerr << "Error converting currency: " << e.what() << std::endl;
        return 0.0;
    }
}
