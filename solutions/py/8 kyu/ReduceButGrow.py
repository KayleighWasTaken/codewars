#!/usr/bin/python3

# https://www.codewars.com/kata/57f780909f7e8e3183000078/
def grow(arr):
    a = 1
    return [a := a * x for x in arr][-1]
