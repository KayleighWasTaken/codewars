#!/usr/bin/python3

# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/
def persistence(n, c=0):
    return c if n < 10 else persistence(eval("*".join(d for d in str(n))), c + 1)
