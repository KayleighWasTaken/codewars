#!/usr/bin/python3

# https://www.codewars.com/kata/51b6249c4612257ac0000005/
def solution(roman):
    numerals = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
    arabic = 0
    for numeral in numerals:
        while roman.startswith(numeral):
            roman = roman.replace(numeral, "", 1)
            arabic += numerals[numeral]
    return arabic
