#!/usr/bin/python3

# https://www.codewars.com/kata/51b66044bce5799a7f000003/
class RomanNumerals:
    numerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
                "V": 5, "IV": 4, "I": 1}

    def arabic_to_roman(arabic):
        roman = ""
        for symbol, value in RomanNumerals.numerals.items():
            while arabic >= value:
                roman += symbol
                arabic -= value
        return roman

    def roman_to_arabic(roman):
        arabic = 0
        for symbol in RomanNumerals.numerals:
            while roman.startswith(symbol):
                roman = roman.replace(symbol, "", 1)
                arabic += RomanNumerals.numerals[symbol]
        return arabic
