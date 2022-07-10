#!/usr/bin/python3

# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/
def find_next_square(sq):
    return int(pow(pow(sq, 0.5) + 1, 2)) if pow(sq, 0.5).is_integer() else -1
