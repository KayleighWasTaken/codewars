#!/usr/bin/python3

# https://www.codewars.com/kata/5913152be0b295cf99000001/
def divisions(n, divisor):
    d = 0
    while n > 1:
        n //= divisor
        d += 1
