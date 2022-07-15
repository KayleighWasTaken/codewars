#!/usr/bin/python3

# https://www.codewars.com/kata/5270d0d18625160ada0000e4/
def score(dice):
    scores = [100, 20, 30, 40, 50, 60]
    return sum((scores[i] * 10) * ((d := dice.count(i + 1)) // 3) + (scores[i] * (d % 3) * (i in [0, 4])) for i in range(6))
