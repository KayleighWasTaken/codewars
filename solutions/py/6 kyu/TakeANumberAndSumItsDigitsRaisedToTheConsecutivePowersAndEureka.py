#!/usr/bin/python3

# https://www.codewars.com/kata/5626b561280a42ecc50000d1/
def sum_dig_pow(a, b):
    return [*filter(lambda x: x == sum(int(d) ** (i + 1) for i, d in enumerate(str(x))), range(a, b + 1))]
