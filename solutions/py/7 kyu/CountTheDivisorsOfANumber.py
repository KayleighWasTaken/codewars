#!/usr/bin/python3

# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/
def divisors(n):
    return [i for i in range(n // 2) if not n % i]
