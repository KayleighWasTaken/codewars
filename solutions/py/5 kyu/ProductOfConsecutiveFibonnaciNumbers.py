#!/usr/bin/python3

# https://www.codewars.com/kata/5541f58a944b85ce6d00006a/
from decimal import *


def productFib(prod):
    getcontext().prec = 100
    root_five = Decimal(5).sqrt()
    capital_phi = (1 + root_five) / 2
    minus_phi = (1 - root_five) / 2
    fib = lambda n: int(((capital_phi ** n) - (minus_phi ** n)) / root_five)
    i = 0
    while True:
        fib_prod = fib(i) * fib(i + 1)
        if fib_prod == prod:
            return [fib(i), fib(i + 1), True]
        elif fib_prod > prod:
            return [fib(i), fib(i + 1), False]
        i += 1
