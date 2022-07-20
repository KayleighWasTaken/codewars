#!/usr/bin/python3

# https://www.codewars.com/kata/56853c44b295170b73000007/
def is_square(arr):
    return all(map(lambda x: (x ** 0.5).is_integer(), arr)) if arr else None
