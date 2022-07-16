#!/usr/bin/python3

# https://www.codewars.com/kata/57a083a57cb1f31db7000028/
def powers_of_two(n):
    return [1 << i for i in range(n + 1)]
