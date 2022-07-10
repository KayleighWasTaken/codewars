#!/usr/bin/python3

# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/
def is_square(n):
    return pow(n, 0.5).is_integer() if n >= 0 else False
