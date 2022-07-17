#!/usr/bin/python3

# https://www.codewars.com/kata/5966e33c4e686b508700002d/
def sum_str(a, b):
    return f"{int(a) + int(b)}" if a and b else a or b or "0"
