#!/usr/bin/python3

# https://www.codewars.com/kata/51b66044bce5799a7f000003/
class RomanNumerals:
    numerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9,
                "V": 5, "IV": 4, "I": 1}

    def to_roman(val):
        out_string = ""
        for numeral, value in RomanNumerals.numerals.items():
            while val >= value:
                out_string = out_string + numeral
                val -= value
        return out_string

    def from_roman(roman_num):
        arabic = 0
        for numeral in RomanNumerals.numerals:
            while roman_num.startswith(numeral):
                roman_num = roman_num.replace(numeral, "", 1)
                arabic += RomanNumerals.numerals[numeral]
        return arabic
