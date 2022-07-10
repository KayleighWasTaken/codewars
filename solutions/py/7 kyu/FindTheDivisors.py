#!/usr/bin/python3

# https://www.codewars.com/kata/544aed4c4a30184e960010f4/
def divisors(integer):
    factors = [x for x in range(2, integer) if not (integer % x)]
    return factors if factors else f"{integer} is prime"
