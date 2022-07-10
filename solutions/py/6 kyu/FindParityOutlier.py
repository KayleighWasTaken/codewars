#!/usr/bin/python3

# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/
def find_outlier(integers):
    return sorted(integers, key=lambda x: x & 1)[-(sum(x & 1 for x in integers) % (len(integers) - 1))]  # no conditionals
