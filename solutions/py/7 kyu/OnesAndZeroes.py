#!/usr/bin/python3

# https://www.codewars.com/kata/578553c3a1b8d5c40300037c/
def binary_array_to_number(arr):
    return int("".join(str(b) for b in arr), 2)
