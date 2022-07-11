#!/usr/bin/python3

# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/
def find_nb(m):
    c = 0
    while m > 0:
        c += 1
        m -= pow(c, 3)
    return -1 if m else c