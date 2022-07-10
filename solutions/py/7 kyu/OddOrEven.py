#!/usr/bin/python3

# https://www.codewars.com/kata/5949481f86420f59480000e7/
def odd_or_even(arr):
    return ["even", "odd"][sum(arr) & 1]
